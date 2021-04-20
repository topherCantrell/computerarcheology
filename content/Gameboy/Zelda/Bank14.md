![Bank 14](GBZelda.jpg)

# Bank 14

>>> cpu Z80GB

>>> binary 4000:zelda.gb[50000:54000]

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: 00         NOP
4001: 00         NOP
4002: 21 A1 22   LD           HL,$22A1
4005: 00         NOP
4006: 21 00 00   LD           HL,$0000
4009: 00         NOP
400A: 61         LD           H,C
400B: 00         NOP
400C: 00         NOP
400D: 61         LD           H,C
400E: 00         NOP
400F: 00         NOP
4010: 00         NOP
4011: C1         POP         BC
4012: 21 63 61   LD           HL,$6163
4015: 21 81 00   LD           HL,$0081
4018: 00         NOP
4019: 00         NOP
401A: 00         NOP
401B: 00         NOP
401C: 00         NOP
401D: 00         NOP
401E: 00         NOP
401F: 00         NOP
4020: 61         LD           H,C
4021: 00         NOP
4022: 00         NOP
4023: 00         NOP
4024: 00         NOP
4025: A1         AND         C
4026: 00         NOP
4027: 66         LD           H,(HL)
4028: C1         POP         BC
4029: 00         NOP
402A: 21 21 00   LD           HL,$0021
402D: 00         NOP
402E: 21 A7 21   LD           HL,$21A7
4031: 25         DEC         H
4032: 81         ADD         A,C
4033: 00         NOP
4034: 81         ADD         A,C
4035: 00         NOP
4036: 00         NOP
4037: 61         LD           H,C
4038: 00         NOP
4039: 63         LD           H,E
403A: 00         NOP
403B: 00         NOP
403C: 00         NOP
403D: 00         NOP
403E: 00         NOP
403F: 00         NOP
4040: 00         NOP
4041: 81         ADD         A,C
4042: 00         NOP
4043: 21 61 C1   LD           HL,$C161
4046: 00         NOP
4047: 00         NOP
4048: 81         ADD         A,C
4049: 21 00 00   LD           HL,$0000
404C: 00         NOP
404D: 81         ADD         A,C
404E: 61         LD           H,C
404F: 21 00 61   LD           HL,$6100
4052: 2B         DEC         HL
4053: 00         NOP
4054: 81         ADD         A,C
4055: 81         ADD         A,C
4056: 00         NOP
4057: 00         NOP
4058: 81         ADD         A,C
4059: 21 21 81   LD           HL,$8121
405C: 21 00 00   LD           HL,$0000
405F: 00         NOP
4060: 21 00 21   LD           HL,$2100
4063: 29         ADD         HL,HL
4064: C1         POP         BC
4065: 00         NOP
4066: 2A         LD           A,(HLI)
4067: A9         XOR         C
4068: 00         NOP
4069: 81         ADD         A,C
406A: 00         NOP
406B: 00         NOP
406C: 00         NOP
406D: 00         NOP
406E: 00         NOP
406F: 00         NOP
4070: 00         NOP
4071: 00         NOP
4072: 00         NOP
4073: 23         INC         HL
4074: 00         NOP
4075: 00         NOP
4076: 00         NOP
4077: 21 21 00   LD           HL,$0021
407A: 00         NOP
407B: 21 00 00   LD           HL,$0000
407E: 00         NOP
407F: 00         NOP
4080: 21 87 21   LD           HL,$2187
4083: 21 21 21   LD           HL,$2121
4086: 00         NOP
4087: 21 00 00   LD           HL,$0000
408A: 21 00 00   LD           HL,$0000
408D: 00         NOP
408E: 00         NOP
408F: 00         NOP
4090: 00         NOP
4091: 23         INC         HL
4092: 21 C1 2B   LD           HL,$2BC1
4095: 21 00 00   LD           HL,$0000
4098: 2B         DEC         HL
4099: 2C         INC         L
409A: 21 61 21   LD           HL,$2161
409D: 00         NOP
409E: 21 21 00   LD           HL,$0021
40A1: 00         NOP
40A2: 00         NOP
40A3: 00         NOP
40A4: 00         NOP
40A5: 00         NOP
40A6: 00         NOP
40A7: 00         NOP
40A8: 00         NOP
40A9: 00         NOP
40AA: 00         NOP
40AB: 00         NOP
40AC: 00         NOP
40AD: 00         NOP
40AE: 00         NOP
40AF: 00         NOP
40B0: 2C         INC         L
40B1: 2C         INC         L
40B2: 2B         DEC         HL
40B3: 00         NOP
40B4: 81         ADD         A,C
40B5: 21 0D 00   LD           HL,$000D
40B8: 2B         DEC         HL
40B9: 00         NOP
40BA: 2C         INC         L
40BB: 2B         DEC         HL
40BC: 21 2B 00   LD           HL,$002B
40BF: 21 61 23   LD           HL,$2361
40C2: A1         AND         C
40C3: 81         ADD         A,C
40C4: 45         LD           B,L
40C5: C1         POP         BC
40C6: 00         NOP
40C7: 21 2B 2B   LD           HL,$2B2B
40CA: 21 21 00   LD           HL,$0021
40CD: 00         NOP
40CE: 00         NOP
40CF: 00         NOP
40D0: 2B         DEC         HL
40D1: 21 21 21   LD           HL,$2121
40D4: 00         NOP
40D5: 00         NOP
40D6: 21 21 00   LD           HL,$0021
40D9: 00         NOP
40DA: 00         NOP
40DB: 00         NOP
40DC: 00         NOP
40DD: 00         NOP
40DE: 00         NOP
40DF: 00         NOP
40E0: 00         NOP
40E1: 00         NOP
40E2: 00         NOP
40E3: 00         NOP
40E4: 00         NOP
40E5: 00         NOP
40E6: 00         NOP
40E7: 00         NOP
40E8: 00         NOP
40E9: 00         NOP
40EA: 00         NOP
40EB: 00         NOP
40EC: 00         NOP
40ED: 00         NOP
40EE: 00         NOP
40EF: 00         NOP
40F0: 00         NOP
40F1: 00         NOP
40F2: 00         NOP
40F3: 00         NOP
40F4: 00         NOP
40F5: 00         NOP
40F6: 00         NOP
40F7: 00         NOP
40F8: 00         NOP
40F9: 00         NOP
40FA: 00         NOP
40FB: 00         NOP
40FC: 00         NOP
40FD: 00         NOP
40FE: 00         NOP
40FF: 00         NOP
4100: 00         NOP
4101: 00         NOP
4102: 00         NOP
4103: 00         NOP
4104: 00         NOP
4105: 00         NOP
4106: 00         NOP
4107: 00         NOP
4108: 00         NOP
4109: 00         NOP
410A: 48         LD           C,B
410B: 00         NOP
410C: 00         NOP
410D: 00         NOP
410E: 00         NOP
410F: 00         NOP
4110: 81         ADD         A,C
4111: 61         LD           H,C
4112: 6C         LD           L,H
4113: 21 00 00   LD           HL,$0000
4116: 00         NOP
4117: 00         NOP
4118: 00         NOP
4119: 00         NOP
411A: 00         NOP
411B: 81         ADD         A,C
411C: 61         LD           H,C
411D: 00         NOP
411E: 00         NOP
411F: 00         NOP
4120: 61         LD           H,C
4121: 00         NOP
4122: 00         NOP
4123: 00         NOP
4124: 67         LD           H,A
4125: 00         NOP
4126: 00         NOP
4127: 00         NOP
4128: C1         POP         BC
4129: 00         NOP
412A: 00         NOP
412B: 00         NOP
412C: 21 00 2A   LD           HL,$2A00
412F: 00         NOP
4130: 21 00 6E   LD           HL,$6E00
4133: 00         NOP
4134: 21 00 00   LD           HL,$0000
4137: 00         NOP
4138: 21 2B 21   LD           HL,$212B
413B: 00         NOP
413C: 00         NOP
413D: 61         LD           H,C
413E: 81         ADD         A,C
413F: C1         POP         BC
4140: 00         NOP
4141: 8F         ADC         A,A
4142: 21 21 00   LD           HL,$0021
4145: 21 65 00   LD           HL,$0065
4148: 00         NOP
4149: 00         NOP
414A: 00         NOP
414B: 00         NOP
414C: 81         ADD         A,C
414D: 6E         LD           L,(HL)
414E: 21 00 00   LD           HL,$0000
4151: 00         NOP
4152: 6E         LD           L,(HL)
4153: 23         INC         HL
4154: 21 00 21   LD           HL,$2100
4157: 21 23 00   LD           HL,$0023
415A: 8E         ADC         A,(HL)
415B: 21 00 00   LD           HL,$0000
415E: A1         AND         C
415F: 21 00 00   LD           HL,$0000
4162: 00         NOP
4163: 00         NOP
4164: 00         NOP
4165: 00         NOP
4166: 00         NOP
4167: 00         NOP
4168: 00         NOP
4169: 00         NOP
416A: 00         NOP
416B: 00         NOP
416C: 00         NOP
416D: 00         NOP
416E: 00         NOP
416F: 00         NOP
4170: 00         NOP
4171: 00         NOP
4172: 00         NOP
4173: 00         NOP
4174: 00         NOP
4175: 00         NOP
4176: 00         NOP
4177: 00         NOP
4178: 00         NOP
4179: 00         NOP
417A: 00         NOP
417B: 00         NOP
417C: 00         NOP
417D: 00         NOP
417E: 00         NOP
417F: 21 00 00   LD           HL,$0000
4182: 00         NOP
4183: 00         NOP
4184: 00         NOP
4185: 00         NOP
4186: 00         NOP
4187: 00         NOP
4188: 00         NOP
4189: 00         NOP
418A: 00         NOP
418B: 00         NOP
418C: 00         NOP
418D: 00         NOP
418E: 00         NOP
418F: 00         NOP
4190: 00         NOP
4191: 00         NOP
4192: 00         NOP
4193: 00         NOP
4194: 00         NOP
4195: 00         NOP
4196: 00         NOP
4197: 00         NOP
4198: 00         NOP
4199: 00         NOP
419A: 00         NOP
419B: 00         NOP
419C: 00         NOP
419D: 00         NOP
419E: 00         NOP
419F: 00         NOP
41A0: 00         NOP
41A1: 00         NOP
41A2: 00         NOP
41A3: 00         NOP
41A4: 00         NOP
41A5: 00         NOP
41A6: 00         NOP
41A7: 00         NOP
41A8: 00         NOP
41A9: 00         NOP
41AA: 00         NOP
41AB: 00         NOP
41AC: 00         NOP
41AD: 00         NOP
41AE: 00         NOP
41AF: 00         NOP
41B0: 00         NOP
41B1: 00         NOP
41B2: 00         NOP
41B3: 00         NOP
41B4: 00         NOP
41B5: 00         NOP
41B6: 00         NOP
41B7: 00         NOP
41B8: 00         NOP
41B9: 00         NOP
41BA: 00         NOP
41BB: 00         NOP
41BC: 00         NOP
41BD: 00         NOP
41BE: 00         NOP
41BF: 00         NOP
41C0: 00         NOP
41C1: 00         NOP
41C2: 00         NOP
41C3: 00         NOP
41C4: 00         NOP
41C5: 00         NOP
41C6: 21 00 00   LD           HL,$0000
41C9: 00         NOP
41CA: 00         NOP
41CB: 00         NOP
41CC: 00         NOP
41CD: 00         NOP
41CE: 00         NOP
41CF: 00         NOP
41D0: 00         NOP
41D1: 00         NOP
41D2: 81         ADD         A,C
41D3: 00         NOP
41D4: 00         NOP
41D5: 00         NOP
41D6: 2B         DEC         HL
41D7: 00         NOP
41D8: 00         NOP
41D9: 00         NOP
41DA: 00         NOP
41DB: 00         NOP
41DC: 00         NOP
41DD: 00         NOP
41DE: 00         NOP
41DF: 00         NOP
41E0: 21 21 00   LD           HL,$0021
41E3: 00         NOP
41E4: 00         NOP
41E5: 00         NOP
41E6: 00         NOP
41E7: 00         NOP
41E8: 00         NOP
41E9: 00         NOP
41EA: 00         NOP
41EB: 00         NOP
41EC: 00         NOP
41ED: 00         NOP
41EE: 00         NOP
41EF: 00         NOP
41F0: 21 00 00   LD           HL,$0000
41F3: 00         NOP
41F4: 00         NOP
41F5: 00         NOP
41F6: 00         NOP
41F7: 00         NOP
41F8: 00         NOP
41F9: 00         NOP
41FA: 00         NOP
41FB: 00         NOP
41FC: 00         NOP
41FD: 00         NOP
41FE: 00         NOP
41FF: 00         NOP
4200: 00         NOP
4201: 00         NOP
4202: 00         NOP
4203: 00         NOP
4204: 00         NOP
4205: 18 19      JR           $4220
4207: 00         NOP
4208: 00         NOP
4209: 00         NOP
420A: 00         NOP
420B: 00         NOP
420C: 00         NOP
420D: 1A         LD           A,(DE)
420E: 1B         DEC         DE
420F: 00         NOP
4210: 00         NOP
4211: 00         NOP
4212: 00         NOP
4213: 00         NOP
4214: 00         NOP
4215: 00         NOP
4216: 02         LD           (BC),A
4217: 00         NOP
4218: 00         NOP
4219: 03         INC         BC
421A: 04         INC         B
421B: 05         DEC         B
421C: 00         NOP
421D: 00         NOP
421E: 06 00      LD           B,$00
4220: 1D         DEC         E
4221: 00         NOP
4222: 07         RLCA
4223: 08 09 0A   LD           ($0A09),SP
4226: 0B         DEC         BC
4227: 00         NOP
4228: 1C         INC         E
4229: 0C         INC         C
422A: 0D         DEC         C
422B: 0E 0F      LD           C,$0F
422D: 10 11      STOP       $11
422F: 00         NOP
4230: 01 00 12   LD           BC,$1200
4233: 13         INC         DE
4234: 14         INC         D
4235: 00         NOP
4236: 00         NOP
4237: 00         NOP
4238: 00         NOP
4239: 15         DEC         D
423A: 16 17      LD           D,$17
423C: 00         NOP
423D: 00         NOP
423E: 00         NOP
423F: 00         NOP
4240: 00         NOP
4241: 00         NOP
4242: 00         NOP
4243: 00         NOP
4244: 00         NOP
4245: 00         NOP
4246: 00         NOP
4247: 00         NOP
4248: 00         NOP
4249: 20 21      JR           NZ,$426C
424B: 22         LD           (HLI),A
424C: 23         INC         HL
424D: 24         INC         H
424E: 25         DEC         H
424F: 00         NOP
4250: 00         NOP
4251: 00         NOP
4252: 26 00      LD           H,$00
4254: 00         NOP
4255: 27         DAA
4256: 00         NOP
4257: 00         NOP
4258: 00         NOP
4259: 28 29      JR           Z,$4284
425B: 3A         LD           A,(HLD)
425C: 3B         DEC         SP
425D: 2A         LD           A,(HLI)
425E: 2B         DEC         HL
425F: 00         NOP
4260: 00         NOP
4261: 2C         INC         L
4262: 00         NOP
4263: 3C         INC         A
4264: 3D         DEC         A
4265: 00         NOP
4266: 2D         DEC         L
4267: 00         NOP
4268: 00         NOP
4269: 2E 00      LD           L,$00
426B: 3E 3F      LD           A,$3F
426D: 00         NOP
426E: 2F         CPL
426F: 00         NOP
4270: 00         NOP
4271: 30 31      JR           NC,$42A4
4273: 32         LD           (HLD),A
4274: 33         INC         SP
4275: 34         INC         (HL)
4276: 35         DEC         (HL)
4277: 00         NOP
4278: 00         NOP
4279: 00         NOP
427A: 36 37      LD           (HL),$37
427C: 38 39      JR           C,$42B7
427E: 00         NOP
427F: 00         NOP
4280: 40         LD           B,B
4281: 41         LD           B,C
4282: 42         LD           B,D
4283: 43         LD           B,E
4284: 00         NOP
4285: AA         XOR         D
4286: AB         XOR         E
4287: 00         NOP
4288: 44         LD           B,H
4289: 45         LD           B,L
428A: 46         LD           B,(HL)
428B: 47         LD           B,A
428C: 00         NOP
428D: 00         NOP
428E: 00         NOP
428F: 00         NOP
4290: 48         LD           C,B
4291: 49         LD           C,C
4292: 4A         LD           C,D
4293: 4B         LD           C,E
4294: 00         NOP
4295: 00         NOP
4296: 54         LD           D,H
4297: 00         NOP
4298: 00         NOP
4299: 4C         LD           C,H
429A: 4D         LD           C,L
429B: 00         NOP
429C: 00         NOP
429D: 55         LD           D,L
429E: 56         LD           D,(HL)
429F: 57         LD           D,A
42A0: 00         NOP
42A1: 4E         LD           C,(HL)
42A2: 00         NOP
42A3: 00         NOP
42A4: 00         NOP
42A5: 00         NOP
42A6: 58         LD           E,B
42A7: 00         NOP
42A8: 00         NOP
42A9: 4F         LD           C,A
42AA: 50         LD           D,B
42AB: 00         NOP
42AC: 00         NOP
42AD: 00         NOP
42AE: 59         LD           E,C
42AF: 00         NOP
42B0: 00         NOP
42B1: 51         LD           D,C
42B2: 00         NOP
42B3: 00         NOP
42B4: 00         NOP
42B5: 00         NOP
42B6: 5A         LD           E,D
42B7: 00         NOP
42B8: 00         NOP
42B9: 52         LD           D,D
42BA: 53         LD           D,E
42BB: 00         NOP
42BC: 00         NOP
42BD: 00         NOP
42BE: 5B         LD           E,E
42BF: 5C         LD           E,H
42C0: 00         NOP
42C1: 00         NOP
42C2: 00         NOP
42C3: 00         NOP
42C4: 00         NOP
42C5: 00         NOP
42C6: 00         NOP
42C7: 00         NOP
42C8: 00         NOP
42C9: 00         NOP
42CA: 00         NOP
42CB: 60         LD           H,B
42CC: 61         LD           H,C
42CD: 00         NOP
42CE: 00         NOP
42CF: 00         NOP
42D0: 00         NOP
42D1: 62         LD           H,D
42D2: 00         NOP
42D3: 63         LD           H,E
42D4: 64         LD           H,H
42D5: 00         NOP
42D6: 65         LD           H,L
42D7: 00         NOP
42D8: EF         RST         0X28
42D9: 66         LD           H,(HL)
42DA: 67         LD           H,A
42DB: 68         LD           L,B
42DC: 69         LD           L,C
42DD: 6A         LD           L,D
42DE: 6B         LD           L,E
42DF: 00         NOP
42E0: FF         RST         0X38
42E1: 6C         LD           L,H
42E2: 6D         LD           L,L
42E3: 6E         LD           L,(HL)
42E4: 6F         LD           L,A
42E5: 70         LD           (HL),B
42E6: 71         LD           (HL),C
42E7: 00         NOP
42E8: 7C         LD           A,H
42E9: 7D         LD           A,L
42EA: 72         LD           (HL),D
42EB: 73         LD           (HL),E
42EC: 74         LD           (HL),H
42ED: 75         LD           (HL),L
42EE: 00         NOP
42EF: 00         NOP
42F0: 1E 1F      LD           E,$1F
42F2: 76         HALT
42F3: 77         LD           (HL),A
42F4: 78         LD           A,B
42F5: 79         LD           A,C
42F6: 00         NOP
42F7: 00         NOP
42F8: 5E         LD           E,(HL)
42F9: 5F         LD           E,A
42FA: 00         NOP
42FB: 7A         LD           A,D
42FC: 7B         LD           A,E
42FD: 00         NOP
42FE: 00         NOP
42FF: 00         NOP
4300: 00         NOP
4301: 80         ADD         A,B
4302: 81         ADD         A,C
4303: 82         ADD         A,D
4304: 83         ADD         A,E
4305: 84         ADD         A,H
4306: 00         NOP
4307: 00         NOP
4308: 00         NOP
4309: 00         NOP
430A: 00         NOP
430B: 85         ADD         A,L
430C: 86         ADD         A,(HL)
430D: 87         ADD         A,A
430E: 88         ADC         A,B
430F: 00         NOP
4310: 00         NOP
4311: 89         ADC         A,C
4312: 8A         ADC         A,D
4313: 8B         ADC         A,E
4314: 8C         ADC         A,H
4315: 8D         ADC         A,L
4316: 8E         ADC         A,(HL)
4317: 8F         ADC         A,A
4318: 00         NOP
4319: 00         NOP
431A: 00         NOP
431B: 00         NOP
431C: 00         NOP
431D: 90         SUB         B
431E: 91         SUB         C
431F: 92         SUB         D
4320: A2         AND         D
4321: A3         AND         E
4322: 00         NOP
4323: 93         SUB         E
4324: 94         SUB         H
4325: 95         SUB         L
4326: 96         SUB         (HL)
4327: 00         NOP
4328: A4         AND         H
4329: A5         AND         L
432A: 97         SUB         A
432B: 98         SBC         B
432C: 99         SBC         C
432D: 9A         SBC         D
432E: 00         NOP
432F: 00         NOP
4330: A6         AND         (HL)
4331: A7         AND         A
4332: 00         NOP
4333: 9B         SBC         E
4334: 9C         SBC         H
4335: 9D         SBC         L
4336: 00         NOP
4337: 00         NOP
4338: A8         XOR         B
4339: A9         XOR         C
433A: 00         NOP
433B: 00         NOP
433C: 9E         SBC         (HL)
433D: 9F         SBC         A
433E: A0         AND         B
433F: A1         AND         C
4340: D8         RET         C
4341: D9         RETI
4342: DA DB DC   JP           C,$DCDB
4345: DD                              
4346: 00         NOP
4347: 00         NOP
4348: B0         OR           B
4349: 00         NOP
434A: 00         NOP
434B: 00         NOP
434C: 00         NOP
434D: 00         NOP
434E: 00         NOP
434F: B1         OR           C
4350: B2         OR           D
4351: B3         OR           E
4352: 00         NOP
4353: B4         OR           H
4354: B5         OR           L
4355: 00         NOP
4356: B6         OR           (HL)
4357: B7         OR           A
4358: B8         CP           B
4359: B9         CP           C
435A: BA         CP           D
435B: BB         CP           E
435C: BC         CP           H
435D: BD         CP           L
435E: BE         CP           (HL)
435F: BF         CP           A
4360: C0         RET         NZ
4361: C1         POP         BC
4362: C2 C3 C4   JP           NZ,$C4C3
4365: C5         PUSH       BC
4366: C6 C7      ADD         $C7
4368: 00         NOP
4369: C8         RET         Z
436A: C9         RET
436B: CA CB CC   JP           Z,$CCCB
436E: CD 00 00   CALL       $0000
4371: CE CF      ADC         $CF
4373: 00         NOP
4374: 00         NOP
4375: D0         RET         NC
4376: D1         POP         DE
4377: 00         NOP
4378: 00         NOP
4379: D2 D3 D4   JP           NC,$D4D3
437C: D5         PUSH       DE
437D: D6 D7      SUB         $D7
437F: 00         NOP
4380: 00         NOP
4381: 11 12 00   LD           DE,$0012
4384: 00         NOP
4385: 00         NOP
4386: 00         NOP
4387: E8 13      ADD         SP,$13
4389: 14         INC         D
438A: 15         DEC         D
438B: 16 00      LD           D,$00
438D: 2B         DEC         HL
438E: 2C         INC         L
438F: F8 17      LDHL       SP,$17
4391: 18 19      JR           $43AC
4393: 1A         LD           A,(DE)
4394: 00         NOP
4395: 2D         DEC         L
4396: 2E 00      LD           L,$00
4398: 1B         DEC         DE
4399: 1C         INC         E
439A: 1D         DEC         E
439B: 1E 00      LD           E,$00
439D: 00         NOP
439E: 00         NOP
439F: 00         NOP
43A0: 01 02 03   LD           BC,$0302
43A3: 04         INC         B
43A4: 00         NOP
43A5: 1F         RRA
43A6: 20 00      JR           NZ,$43A8
43A8: 05         DEC         B
43A9: 06 07      LD           B,$07
43AB: 08 21 22   LD           ($2221),SP
43AE: 23         INC         HL
43AF: 24         INC         H
43B0: 09         ADD         HL,BC
43B1: 0A         LD           A,(BC)
43B2: 0B         DEC         BC
43B3: 0C         INC         C
43B4: 25         DEC         H
43B5: 26 27      LD           H,$27
43B7: 28 0D      JR           Z,$43C6
43B9: 0E 0F      LD           C,$0F
43BB: 10 00      STOP       $00
43BD: 29         ADD         HL,HL
43BE: 2A         LD           A,(HLI)
43BF: 00         NOP
43C0: 60         LD           H,B
43C1: 61         LD           H,C
43C2: 00         NOP
43C3: 30 31      JR           NC,$43F6
43C5: 00         NOP
43C6: 62         LD           H,D
43C7: 63         LD           H,E
43C8: 32         LD           (HLD),A
43C9: 64         LD           H,H
43CA: 65         LD           H,L
43CB: 34         INC         (HL)
43CC: 35         DEC         (HL)
43CD: 66         LD           H,(HL)
43CE: 67         LD           H,A
43CF: 37         SCF
43D0: 38 39      JR           C,$440B
43D2: 3A         LD           A,(HLD)
43D3: 3B         DEC         SP
43D4: 3C         INC         A
43D5: 3D         DEC         A
43D6: 3E 3F      LD           A,$3F
43D8: 00         NOP
43D9: 40         LD           B,B
43DA: 41         LD           B,C
43DB: 42         LD           B,D
43DC: 43         LD           B,E
43DD: 44         LD           B,H
43DE: 45         LD           B,L
43DF: 00         NOP
43E0: 00         NOP
43E1: 46         LD           B,(HL)
43E2: 47         LD           B,A
43E3: 48         LD           C,B
43E4: 49         LD           C,C
43E5: 4A         LD           C,D
43E6: 4B         LD           C,E
43E7: 00         NOP
43E8: 4C         LD           C,H
43E9: 4D         LD           C,L
43EA: 4E         LD           C,(HL)
43EB: 4F         LD           C,A
43EC: 50         LD           D,B
43ED: 51         LD           D,C
43EE: 52         LD           D,D
43EF: 53         LD           D,E
43F0: 54         LD           D,H
43F1: 55         LD           D,L
43F2: 56         LD           D,(HL)
43F3: 57         LD           D,A
43F4: 58         LD           E,B
43F5: 59         LD           E,C
43F6: 5A         LD           E,D
43F7: 5B         LD           E,E
43F8: 5C         LD           E,H
43F9: 68         LD           L,B
43FA: 69         LD           L,C
43FB: 5D         LD           E,L
43FC: 5E         LD           E,(HL)
43FD: 6A         LD           L,D
43FE: 6B         LD           L,E
43FF: 5F         LD           E,A
4400: 00         NOP
4401: 00         NOP
4402: 00         NOP
4403: 00         NOP
4404: 00         NOP
4405: 00         NOP
4406: 00         NOP
4407: 00         NOP
4408: 00         NOP
4409: 00         NOP
440A: 00         NOP
440B: 74         LD           (HL),H
440C: 00         NOP
440D: 00         NOP
440E: 00         NOP
440F: 00         NOP
4410: 00         NOP
4411: 00         NOP
4412: 00         NOP
4413: 73         LD           (HL),E
4414: 00         NOP
4415: 00         NOP
4416: 00         NOP
4417: 00         NOP
4418: 00         NOP
4419: 00         NOP
441A: 00         NOP
441B: 71         LD           (HL),C
441C: 00         NOP
441D: 00         NOP
441E: 00         NOP
441F: 00         NOP
4420: 00         NOP
4421: 00         NOP
4422: 00         NOP
4423: 72         LD           (HL),D
4424: 00         NOP
4425: 00         NOP
4426: 00         NOP
4427: 00         NOP
4428: 00         NOP
4429: 00         NOP
442A: 00         NOP
442B: 76         HALT
442C: 00         NOP
442D: 00         NOP
442E: 00         NOP
442F: 00         NOP
4430: 00         NOP
4431: 00         NOP
4432: 00         NOP
4433: 75         LD           (HL),L
4434: 00         NOP
4435: 00         NOP
4436: 00         NOP
4437: 00         NOP
4438: 00         NOP
4439: 00         NOP
443A: 00         NOP
443B: 70         LD           (HL),B
443C: 00         NOP
443D: 00         NOP
443E: 00         NOP
443F: 00         NOP
4440: 00         NOP
4441: 00         NOP
4442: 00         NOP
4443: 00         NOP
4444: 00         NOP
4445: 00         NOP
4446: 00         NOP
4447: 00         NOP
4448: 00         NOP
4449: 00         NOP
444A: 00         NOP
444B: 00         NOP
444C: 00         NOP
444D: 00         NOP
444E: 00         NOP
444F: 00         NOP
4450: 00         NOP
4451: 00         NOP
4452: 00         NOP
4453: 00         NOP
4454: 00         NOP
4455: 00         NOP
4456: 00         NOP
4457: 00         NOP
4458: 00         NOP
4459: 00         NOP
445A: 00         NOP
445B: 00         NOP
445C: 00         NOP
445D: 00         NOP
445E: 00         NOP
445F: 00         NOP
4460: 00         NOP
4461: 00         NOP
4462: 00         NOP
4463: 00         NOP
4464: 00         NOP
4465: 00         NOP
4466: 00         NOP
4467: 00         NOP
4468: 00         NOP
4469: 00         NOP
446A: 00         NOP
446B: 00         NOP
446C: 00         NOP
446D: 00         NOP
446E: 00         NOP
446F: 00         NOP
4470: 00         NOP
4471: 00         NOP
4472: 00         NOP
4473: 00         NOP
4474: 00         NOP
4475: 00         NOP
4476: 00         NOP
4477: 00         NOP
4478: 00         NOP
4479: 00         NOP
447A: 00         NOP
447B: 00         NOP
447C: 00         NOP
447D: 00         NOP
447E: 00         NOP
447F: 00         NOP
4480: B6         OR           (HL)
4481: B7         OR           A
4482: B8         CP           B
4483: B9         CP           C
4484: 85         ADD         A,L
4485: 86         ADD         A,(HL)
4486: FD                              
4487: F3         DI
4488: ED                              
4489: EE EA      XOR         $EA
448B: EB                              
448C: EC                              
448D: 87         ADD         A,A
448E: F1         POP         AF
448F: F2                              
4490: FE EF      CP           $EF
4492: BA         CP           D
4493: BB         CP           E
4494: BC         CP           H
4495: 8D         ADC         A,L
4496: F9         LD           SP,HL
4497: FA 80 81   LD           A,($8180)
449A: 82         ADD         A,D
449B: 83         ADD         A,E
449C: 84         ADD         A,H
449D: 8C         ADC         A,H
449E: 88         ADC         A,B
449F: 8A         ADC         A,D
44A0: 90         SUB         B
44A1: 91         SUB         C
44A2: 92         SUB         D
44A3: 00         NOP
44A4: 8E         ADC         A,(HL)
44A5: 9A         SBC         D
44A6: 89         ADC         A,C
44A7: 8B         ADC         A,E
44A8: 97         SUB         A
44A9: 93         SUB         E
44AA: 94         SUB         H
44AB: 95         SUB         L
44AC: 96         SUB         (HL)
44AD: 00         NOP
44AE: AB         XOR         E
44AF: AC         XOR         H
44B0: 98         SBC         B
44B1: 7A         LD           A,D
44B2: 7B         LD           A,E
44B3: 00         NOP
44B4: E6 E7      AND         $E7
44B6: 00         NOP
44B7: BD         CP           L
44B8: 00         NOP
44B9: 7C         LD           A,H
44BA: 7D         LD           A,L
44BB: 7E         LD           A,(HL)
44BC: F6 F7      OR           $F7
44BE: DE DF      SBC         $DF
44C0: 00         NOP
44C1: 11 12 00   LD           DE,$0012
44C4: 00         NOP
44C5: 00         NOP
44C6: 00         NOP
44C7: E8 13      ADD         SP,$13
44C9: 14         INC         D
44CA: 15         DEC         D
44CB: 16 00      LD           D,$00
44CD: 00         NOP
44CE: 00         NOP
44CF: F8 17      LDHL       SP,$17
44D1: 18 19      JR           $44EC
44D3: 1A         LD           A,(DE)
44D4: 00         NOP
44D5: 00         NOP
44D6: 00         NOP
44D7: 00         NOP
44D8: 1B         DEC         DE
44D9: 1C         INC         E
44DA: 1D         DEC         E
44DB: 1E 00      LD           E,$00
44DD: 00         NOP
44DE: 00         NOP
44DF: 00         NOP
44E0: 01 02 03   LD           BC,$0302
44E3: 04         INC         B
44E4: 00         NOP
44E5: 1F         RRA
44E6: 20 00      JR           NZ,$44E8
44E8: 05         DEC         B
44E9: 06 07      LD           B,$07
44EB: 08 21 2B   LD           ($2B21),SP
44EE: 2C         INC         L
44EF: 24         INC         H
44F0: 09         ADD         HL,BC
44F1: 0A         LD           A,(BC)
44F2: 0B         DEC         BC
44F3: 0C         INC         C
44F4: 25         DEC         H
44F5: 2D         DEC         L
44F6: 2E 28      LD           L,$28
44F8: 0D         DEC         C
44F9: 0E 0F      LD           C,$0F
44FB: 10 00      STOP       $00
44FD: 29         ADD         HL,HL
44FE: 2A         LD           A,(HLI)
44FF: 00         NOP
4500: 00         NOP
4501: 00         NOP
4502: 00         NOP
4503: 00         NOP
4504: 1B         DEC         DE
4505: 00         NOP
4506: 00         NOP
4507: 1B         DEC         DE
4508: 00         NOP
4509: 00         NOP
450A: 00         NOP
450B: 00         NOP
450C: 00         NOP
450D: 00         NOP
450E: 00         NOP
450F: 00         NOP
4510: 00         NOP
4511: 00         NOP
4512: 00         NOP
4513: 00         NOP
4514: 00         NOP
4515: 00         NOP
4516: 00         NOP
4517: 00         NOP
4518: 1B         DEC         DE
4519: 1D         DEC         E
451A: 00         NOP
451B: 00         NOP
451C: 00         NOP
451D: 20 00      JR           NZ,$451F
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
4533: 00         NOP
4534: 1B         DEC         DE
4535: 00         NOP
4536: 00         NOP
4537: 00         NOP
4538: 00         NOP
4539: 00         NOP
453A: 00         NOP
453B: 00         NOP
453C: 00         NOP
453D: 00         NOP
453E: 00         NOP
453F: 00         NOP
4540: 00         NOP
4541: 11 00 00   LD           DE,$0000
4544: 00         NOP
4545: 00         NOP
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
4552: 00         NOP
4553: 00         NOP
4554: 00         NOP
4555: 00         NOP
4556: 00         NOP
4557: 00         NOP
4558: 00         NOP
4559: 00         NOP
455A: 00         NOP
455B: 00         NOP
455C: 1C         INC         E
455D: 1C         INC         E
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
456C: 20 00      JR           NZ,$456E
456E: 00         NOP
456F: 00         NOP
4570: 00         NOP
4571: 20 00      JR           NZ,$4573
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
457D: 00         NOP
457E: 00         NOP
457F: 00         NOP
4580: 00         NOP
4581: 00         NOP
4582: 00         NOP
4583: 00         NOP
4584: 00         NOP
4585: 00         NOP
4586: 00         NOP
4587: 00         NOP
4588: 00         NOP
4589: 00         NOP
458A: 00         NOP
458B: 00         NOP
458C: 00         NOP
458D: 00         NOP
458E: 00         NOP
458F: 00         NOP
4590: 00         NOP
4591: 00         NOP
4592: 00         NOP
4593: 00         NOP
4594: 00         NOP
4595: 00         NOP
4596: 00         NOP
4597: 00         NOP
4598: 00         NOP
4599: 00         NOP
459A: 00         NOP
459B: 00         NOP
459C: 00         NOP
459D: 00         NOP
459E: 00         NOP
459F: 00         NOP
45A0: 00         NOP
45A1: 00         NOP
45A2: 00         NOP
45A3: 00         NOP
45A4: 00         NOP
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
45B4: 00         NOP
45B5: 00         NOP
45B6: 00         NOP
45B7: 00         NOP
45B8: 00         NOP
45B9: 00         NOP
45BA: 00         NOP
45BB: 00         NOP
45BC: 00         NOP
45BD: 00         NOP
45BE: 00         NOP
45BF: 00         NOP
45C0: 00         NOP
45C1: 00         NOP
45C2: 00         NOP
45C3: 00         NOP
45C4: 00         NOP
45C5: 00         NOP
45C6: 00         NOP
45C7: 00         NOP
45C8: 00         NOP
45C9: 00         NOP
45CA: 00         NOP
45CB: 00         NOP
45CC: 00         NOP
45CD: 00         NOP
45CE: 00         NOP
45CF: 00         NOP
45D0: 00         NOP
45D1: 00         NOP
45D2: 00         NOP
45D3: 00         NOP
45D4: 00         NOP
45D5: 00         NOP
45D6: 00         NOP
45D7: 00         NOP
45D8: 00         NOP
45D9: 00         NOP
45DA: 00         NOP
45DB: 00         NOP
45DC: 00         NOP
45DD: 00         NOP
45DE: 00         NOP
45DF: 00         NOP
45E0: 00         NOP
45E1: 00         NOP
45E2: 00         NOP
45E3: 00         NOP
45E4: 00         NOP
45E5: 1B         DEC         DE
45E6: 00         NOP
45E7: 00         NOP
45E8: 00         NOP
45E9: 00         NOP
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
4602: 00         NOP
4603: 00         NOP
4604: 00         NOP
4605: 00         NOP
4606: 00         NOP
4607: 00         NOP
4608: 19         ADD         HL,DE
4609: 00         NOP
460A: 18 00      JR           $460C
460C: 20 1C      JR           NZ,$462A
460E: 1A         LD           A,(DE)
460F: 00         NOP
4610: 00         NOP
4611: 00         NOP
4612: 00         NOP
4613: 1A         LD           A,(DE)
4614: 16 17      LD           D,$17
4616: 1A         LD           A,(DE)
4617: 00         NOP
4618: 00         NOP
4619: 00         NOP
461A: 00         NOP
461B: 00         NOP
461C: 00         NOP
461D: 07         RLCA
461E: 00         NOP
461F: 00         NOP
4620: 00         NOP
4621: 1C         INC         E
4622: 1A         LD           A,(DE)
4623: 00         NOP
4624: 00         NOP
4625: 00         NOP
4626: 18 19      JR           $4641
4628: 00         NOP
4629: 00         NOP
462A: 00         NOP
462B: 00         NOP
462C: 00         NOP
462D: 00         NOP
462E: 16 00      LD           D,$00
4630: 00         NOP
4631: 00         NOP
4632: 00         NOP
4633: 00         NOP
4634: 00         NOP
4635: 00         NOP
4636: 1B         DEC         DE
4637: 17         RLA
4638: 1A         LD           A,(DE)
4639: 1A         LD           A,(DE)
463A: 00         NOP
463B: 00         NOP
463C: 00         NOP
463D: 00         NOP
463E: 00         NOP
463F: 00         NOP
4640: 00         NOP
4641: 00         NOP
4642: 17         RLA
4643: 00         NOP
4644: 16 00      LD           D,$00
4646: 05         DEC         B
4647: 19         ADD         HL,DE
4648: 00         NOP
4649: 00         NOP
464A: 00         NOP
464B: 00         NOP
464C: 1B         DEC         DE
464D: 00         NOP
464E: 18 22      JR           $4672
4650: 1E 1A      LD           E,$1A
4652: 00         NOP
4653: 1A         LD           A,(DE)
4654: 1A         LD           A,(DE)
4655: 1A         LD           A,(DE)
4656: 00         NOP
4657: 00         NOP
4658: 00         NOP
4659: 00         NOP
465A: 00         NOP
465B: 00         NOP
465C: 00         NOP
465D: 00         NOP
465E: 00         NOP
465F: 00         NOP
4660: 0C         INC         C
4661: 00         NOP
4662: 00         NOP
4663: 00         NOP
4664: 00         NOP
4665: 1A         LD           A,(DE)
4666: 00         NOP
4667: 00         NOP
4668: 1A         LD           A,(DE)
4669: 1A         LD           A,(DE)
466A: 16 00      LD           D,$00
466C: 00         NOP
466D: 22         LD           (HLI),A
466E: 1B         DEC         DE
466F: 00         NOP
4670: 00         NOP
4671: 1A         LD           A,(DE)
4672: 00         NOP
4673: 00         NOP
4674: 00         NOP
4675: 1B         DEC         DE
4676: 19         ADD         HL,DE
4677: 00         NOP
4678: 17         RLA
4679: 18 00      JR           $467B
467B: 1A         LD           A,(DE)
467C: 00         NOP
467D: 00         NOP
467E: 00         NOP
467F: 00         NOP
4680: 00         NOP
4681: 00         NOP
4682: 00         NOP
4683: 18 00      JR           $4685
4685: 00         NOP
4686: 19         ADD         HL,DE
4687: 00         NOP
4688: 1B         DEC         DE
4689: 00         NOP
468A: 00         NOP
468B: 00         NOP
468C: 00         NOP
468D: 00         NOP
468E: 1B         DEC         DE
468F: 1A         LD           A,(DE)
4690: 00         NOP
4691: 00         NOP
4692: 00         NOP
4693: 00         NOP
4694: 00         NOP
4695: 00         NOP
4696: 21 1A 00   LD           HL,$001A
4699: 00         NOP
469A: 00         NOP
469B: 16 00      LD           D,$00
469D: 00         NOP
469E: 17         RLA
469F: 00         NOP
46A0: 1E 00      LD           E,$00
46A2: 00         NOP
46A3: 00         NOP
46A4: 00         NOP
46A5: 00         NOP
46A6: 00         NOP
46A7: 00         NOP
46A8: 00         NOP
46A9: 00         NOP
46AA: 00         NOP
46AB: 00         NOP
46AC: 00         NOP
46AD: 00         NOP
46AE: 00         NOP
46AF: 00         NOP
46B0: 1D         DEC         E
46B1: 1E 00      LD           E,$00
46B3: 17         RLA
46B4: 00         NOP
46B5: 00         NOP
46B6: 19         ADD         HL,DE
46B7: 00         NOP
46B8: 00         NOP
46B9: 18 00      JR           $46BB
46BB: 00         NOP
46BC: 00         NOP
46BD: 00         NOP
46BE: 1A         LD           A,(DE)
46BF: 00         NOP
46C0: 16 00      LD           D,$00
46C2: 00         NOP
46C3: 00         NOP
46C4: 00         NOP
46C5: 00         NOP
46C6: 00         NOP
46C7: 00         NOP
46C8: 00         NOP
46C9: 1D         DEC         E
46CA: 00         NOP
46CB: 00         NOP
46CC: 00         NOP
46CD: 00         NOP
46CE: 00         NOP
46CF: 1B         DEC         DE
46D0: 00         NOP
46D1: 1B         DEC         DE
46D2: 00         NOP
46D3: 00         NOP
46D4: 00         NOP
46D5: 00         NOP
46D6: 00         NOP
46D7: 1B         DEC         DE
46D8: 00         NOP
46D9: 00         NOP
46DA: 00         NOP
46DB: 00         NOP
46DC: 00         NOP
46DD: 00         NOP
46DE: 00         NOP
46DF: 00         NOP
46E0: 00         NOP
46E1: 00         NOP
46E2: 00         NOP
46E3: 00         NOP
46E4: 00         NOP
46E5: 00         NOP
46E6: 00         NOP
46E7: 00         NOP
46E8: 00         NOP
46E9: 00         NOP
46EA: 00         NOP
46EB: 00         NOP
46EC: 00         NOP
46ED: 00         NOP
46EE: 00         NOP
46EF: 00         NOP
46F0: 00         NOP
46F1: 00         NOP
46F2: 00         NOP
46F3: 00         NOP
46F4: 00         NOP
46F5: 00         NOP
46F6: 00         NOP
46F7: 00         NOP
46F8: 00         NOP
46F9: 00         NOP
46FA: 00         NOP
46FB: 00         NOP
46FC: 1E 20      LD           E,$20
46FE: 00         NOP
46FF: 00         NOP
4700: 00         NOP
4701: 20 00      JR           NZ,$4703
4703: 00         NOP
4704: 1A         LD           A,(DE)
4705: 00         NOP
4706: 00         NOP
4707: 00         NOP
4708: 00         NOP
4709: 18 00      JR           $470B
470B: 00         NOP
470C: 00         NOP
470D: 00         NOP
470E: 00         NOP
470F: 00         NOP
4710: 00         NOP
4711: 17         RLA
4712: 16 00      LD           D,$00
4714: 00         NOP
4715: 00         NOP
4716: 00         NOP
4717: 00         NOP
4718: 00         NOP
4719: 00         NOP
471A: 01 00 1C   LD           BC,$1C00
471D: 00         NOP
471E: 00         NOP
471F: 00         NOP
4720: 1D         DEC         E
4721: 00         NOP
4722: 00         NOP
4723: 00         NOP
4724: 19         ADD         HL,DE
4725: 00         NOP
4726: 00         NOP
4727: 00         NOP
4728: 00         NOP
4729: 00         NOP
472A: 00         NOP
472B: 00         NOP
472C: 00         NOP
472D: 00         NOP
472E: 00         NOP
472F: 00         NOP
4730: 00         NOP
4731: 00         NOP
4732: 19         ADD         HL,DE
4733: 00         NOP
4734: 00         NOP
4735: 1C         INC         E
4736: 00         NOP
4737: 04         INC         B
4738: 00         NOP
4739: 00         NOP
473A: 1B         DEC         DE
473B: 00         NOP
473C: 00         NOP
473D: 1A         LD           A,(DE)
473E: 00         NOP
473F: 00         NOP
4740: 1A         LD           A,(DE)
4741: 00         NOP
4742: 00         NOP
4743: 00         NOP
4744: 00         NOP
4745: 00         NOP
4746: 1A         LD           A,(DE)
4747: 00         NOP
4748: 00         NOP
4749: 00         NOP
474A: 00         NOP
474B: 00         NOP
474C: 00         NOP
474D: 1C         INC         E
474E: 00         NOP
474F: 16 00      LD           D,$00
4751: 00         NOP
4752: 00         NOP
4753: 00         NOP
4754: 00         NOP
4755: 1B         DEC         DE
4756: 00         NOP
4757: 00         NOP
4758: 00         NOP
4759: 22         LD           (HLI),A
475A: 00         NOP
475B: 00         NOP
475C: 17         RLA
475D: 00         NOP
475E: 00         NOP
475F: 18 00      JR           $4761
4761: 00         NOP
4762: 00         NOP
4763: 00         NOP
4764: 00         NOP
4765: 00         NOP
4766: 00         NOP
4767: 00         NOP
4768: 00         NOP
4769: 00         NOP
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
4774: 00         NOP
4775: 00         NOP
4776: 00         NOP
4777: 00         NOP
4778: 00         NOP
4779: 00         NOP
477A: 00         NOP
477B: 00         NOP
477C: 00         NOP
477D: 00         NOP
477E: 00         NOP
477F: 00         NOP
4780: 00         NOP
4781: 00         NOP
4782: 00         NOP
4783: 00         NOP
4784: 00         NOP
4785: 00         NOP
4786: 00         NOP
4787: 00         NOP
4788: 00         NOP
4789: 00         NOP
478A: 22         LD           (HLI),A
478B: 00         NOP
478C: 00         NOP
478D: 00         NOP
478E: 00         NOP
478F: 00         NOP
4790: 00         NOP
4791: 00         NOP
4792: 00         NOP
4793: 00         NOP
4794: 00         NOP
4795: 00         NOP
4796: 00         NOP
4797: 00         NOP
4798: 00         NOP
4799: 00         NOP
479A: 00         NOP
479B: 00         NOP
479C: 00         NOP
479D: 00         NOP
479E: 00         NOP
479F: 00         NOP
47A0: 00         NOP
47A1: 00         NOP
47A2: 00         NOP
47A3: 00         NOP
47A4: 02         LD           (BC),A
47A5: 00         NOP
47A6: 00         NOP
47A7: 00         NOP
47A8: 00         NOP
47A9: 00         NOP
47AA: 00         NOP
47AB: 1C         INC         E
47AC: 00         NOP
47AD: 00         NOP
47AE: 1C         INC         E
47AF: 1B         DEC         DE
47B0: 00         NOP
47B1: 00         NOP
47B2: 00         NOP
47B3: 1B         DEC         DE
47B4: 00         NOP
47B5: 00         NOP
47B6: 00         NOP
47B7: 00         NOP
47B8: 00         NOP
47B9: 00         NOP
47BA: 1B         DEC         DE
47BB: 1B         DEC         DE
47BC: 00         NOP
47BD: 1B         DEC         DE
47BE: 06 1D      LD           B,$1D
47C0: 00         NOP
47C1: 00         NOP
47C2: 00         NOP
47C3: 00         NOP
47C4: 00         NOP
47C5: 00         NOP
47C6: 00         NOP
47C7: 00         NOP
47C8: 20 00      JR           NZ,$47CA
47CA: 00         NOP
47CB: 00         NOP
47CC: 00         NOP
47CD: 1B         DEC         DE
47CE: 00         NOP
47CF: 00         NOP
47D0: 00         NOP
47D1: 00         NOP
47D2: 00         NOP
47D3: 00         NOP
47D4: 00         NOP
47D5: 00         NOP
47D6: 00         NOP
47D7: 00         NOP
47D8: 00         NOP
47D9: 00         NOP
47DA: 00         NOP
47DB: 00         NOP
47DC: 00         NOP
47DD: 00         NOP
47DE: 00         NOP
47DF: 00         NOP
47E0: 00         NOP
47E1: 00         NOP
47E2: 00         NOP
47E3: 00         NOP
47E4: 00         NOP
47E5: 00         NOP
47E6: 00         NOP
47E7: 00         NOP
47E8: 00         NOP
47E9: 1B         DEC         DE
47EA: 00         NOP
47EB: 00         NOP
47EC: 00         NOP
47ED: 00         NOP
47EE: 00         NOP
47EF: 00         NOP
47F0: 00         NOP
47F1: 00         NOP
47F2: 1C         INC         E
47F3: 00         NOP
47F4: 1B         DEC         DE
47F5: 00         NOP
47F6: 08 00 00   LD           ($0000),SP
47F9: 00         NOP
47FA: 00         NOP
47FB: 00         NOP
47FC: 20 00      JR           NZ,$47FE
47FE: 00         NOP
47FF: 00         NOP
4800: FF         RST         0X38
4801: FF         RST         0X38
4802: FF         RST         0X38
4803: FF         RST         0X38
4804: FF         RST         0X38
4805: FF         RST         0X38
4806: FF         RST         0X38
4807: FF         RST         0X38
4808: FF         RST         0X38
4809: FF         RST         0X38
480A: FF         RST         0X38
480B: FF         RST         0X38
480C: FF         RST         0X38
480D: FF         RST         0X38
480E: FF         RST         0X38
480F: FF         RST         0X38
4810: FF         RST         0X38
4811: FF         RST         0X38
4812: FF         RST         0X38
4813: FF         RST         0X38
4814: FF         RST         0X38
4815: FF         RST         0X38
4816: FF         RST         0X38
4817: FF         RST         0X38
4818: FF         RST         0X38
4819: FF         RST         0X38
481A: FF         RST         0X38
481B: FF         RST         0X38
481C: FF         RST         0X38
481D: FF         RST         0X38
481E: FF         RST         0X38
481F: FF         RST         0X38
4820: FF         RST         0X38
4821: FF         RST         0X38
4822: FF         RST         0X38
4823: FF         RST         0X38
4824: FF         RST         0X38
4825: FF         RST         0X38
4826: FF         RST         0X38
4827: FF         RST         0X38
4828: FF         RST         0X38
4829: FF         RST         0X38
482A: FF         RST         0X38
482B: FF         RST         0X38
482C: FF         RST         0X38
482D: FF         RST         0X38
482E: FF         RST         0X38
482F: FF         RST         0X38
4830: FF         RST         0X38
4831: FF         RST         0X38
4832: FF         RST         0X38
4833: FF         RST         0X38
4834: FF         RST         0X38
4835: FF         RST         0X38
4836: FF         RST         0X38
4837: FF         RST         0X38
4838: FF         RST         0X38
4839: FF         RST         0X38
483A: FF         RST         0X38
483B: FF         RST         0X38
483C: FF         RST         0X38
483D: FF         RST         0X38
483E: FF         RST         0X38
483F: FF         RST         0X38
4840: FF         RST         0X38
4841: FF         RST         0X38
4842: FF         RST         0X38
4843: FF         RST         0X38
4844: FF         RST         0X38
4845: FF         RST         0X38
4846: FF         RST         0X38
4847: FF         RST         0X38
4848: FF         RST         0X38
4849: FF         RST         0X38
484A: FF         RST         0X38
484B: FF         RST         0X38
484C: FF         RST         0X38
484D: FF         RST         0X38
484E: FF         RST         0X38
484F: FF         RST         0X38
4850: FF         RST         0X38
4851: FF         RST         0X38
4852: FF         RST         0X38
4853: FF         RST         0X38
4854: FF         RST         0X38
4855: FF         RST         0X38
4856: FF         RST         0X38
4857: FF         RST         0X38
4858: FF         RST         0X38
4859: FF         RST         0X38
485A: FF         RST         0X38
485B: FF         RST         0X38
485C: FF         RST         0X38
485D: FF         RST         0X38
485E: FF         RST         0X38
485F: FF         RST         0X38
4860: FF         RST         0X38
4861: FF         RST         0X38
4862: FF         RST         0X38
4863: FF         RST         0X38
4864: FF         RST         0X38
4865: FF         RST         0X38
4866: FF         RST         0X38
4867: FF         RST         0X38
4868: FF         RST         0X38
4869: FF         RST         0X38
486A: FF         RST         0X38
486B: FF         RST         0X38
486C: FF         RST         0X38
486D: FF         RST         0X38
486E: FF         RST         0X38
486F: FF         RST         0X38
4870: FF         RST         0X38
4871: FF         RST         0X38
4872: FF         RST         0X38
4873: FF         RST         0X38
4874: FF         RST         0X38
4875: FF         RST         0X38
4876: FF         RST         0X38
4877: FF         RST         0X38
4878: FF         RST         0X38
4879: FF         RST         0X38
487A: FF         RST         0X38
487B: FF         RST         0X38
487C: FF         RST         0X38
487D: FF         RST         0X38
487E: FF         RST         0X38
487F: FF         RST         0X38
4880: FF         RST         0X38
4881: FF         RST         0X38
4882: FF         RST         0X38
4883: FF         RST         0X38
4884: FF         RST         0X38
4885: FF         RST         0X38
4886: FF         RST         0X38
4887: FF         RST         0X38
4888: FF         RST         0X38
4889: FF         RST         0X38
488A: FF         RST         0X38
488B: FF         RST         0X38
488C: FF         RST         0X38
488D: FF         RST         0X38
488E: FF         RST         0X38
488F: FF         RST         0X38
4890: FF         RST         0X38
4891: FF         RST         0X38
4892: FF         RST         0X38
4893: FF         RST         0X38
4894: FF         RST         0X38
4895: FF         RST         0X38
4896: FF         RST         0X38
4897: FF         RST         0X38
4898: FF         RST         0X38
4899: FF         RST         0X38
489A: FF         RST         0X38
489B: FF         RST         0X38
489C: FF         RST         0X38
489D: FF         RST         0X38
489E: FF         RST         0X38
489F: FF         RST         0X38
48A0: FF         RST         0X38
48A1: FF         RST         0X38
48A2: FF         RST         0X38
48A3: FF         RST         0X38
48A4: FF         RST         0X38
48A5: FF         RST         0X38
48A6: FF         RST         0X38
48A7: FF         RST         0X38
48A8: FF         RST         0X38
48A9: FF         RST         0X38
48AA: FF         RST         0X38
48AB: FF         RST         0X38
48AC: FF         RST         0X38
48AD: FF         RST         0X38
48AE: FF         RST         0X38
48AF: FF         RST         0X38
48B0: FF         RST         0X38
48B1: FF         RST         0X38
48B2: FF         RST         0X38
48B3: FF         RST         0X38
48B4: FF         RST         0X38
48B5: FF         RST         0X38
48B6: FF         RST         0X38
48B7: FF         RST         0X38
48B8: FF         RST         0X38
48B9: FF         RST         0X38
48BA: FF         RST         0X38
48BB: FF         RST         0X38
48BC: FF         RST         0X38
48BD: FF         RST         0X38
48BE: FF         RST         0X38
48BF: FF         RST         0X38
48C0: FF         RST         0X38
48C1: FF         RST         0X38
48C2: FF         RST         0X38
48C3: FF         RST         0X38
48C4: FF         RST         0X38
48C5: FF         RST         0X38
48C6: FF         RST         0X38
48C7: FF         RST         0X38
48C8: FF         RST         0X38
48C9: FF         RST         0X38
48CA: FF         RST         0X38
48CB: FF         RST         0X38
48CC: FF         RST         0X38
48CD: FF         RST         0X38
48CE: FF         RST         0X38
48CF: FF         RST         0X38
48D0: FF         RST         0X38
48D1: FF         RST         0X38
48D2: FF         RST         0X38
48D3: FF         RST         0X38
48D4: FF         RST         0X38
48D5: FF         RST         0X38
48D6: FF         RST         0X38
48D7: FF         RST         0X38
48D8: FF         RST         0X38
48D9: FF         RST         0X38
48DA: FF         RST         0X38
48DB: FF         RST         0X38
48DC: FF         RST         0X38
48DD: FF         RST         0X38
48DE: FF         RST         0X38
48DF: FF         RST         0X38
48E0: FF         RST         0X38
48E1: FF         RST         0X38
48E2: FF         RST         0X38
48E3: FF         RST         0X38
48E4: FF         RST         0X38
48E5: FF         RST         0X38
48E6: FF         RST         0X38
48E7: FF         RST         0X38
48E8: FF         RST         0X38
48E9: FF         RST         0X38
48EA: FF         RST         0X38
48EB: FF         RST         0X38
48EC: FF         RST         0X38
48ED: FF         RST         0X38
48EE: FF         RST         0X38
48EF: FF         RST         0X38
48F0: FF         RST         0X38
48F1: FF         RST         0X38
48F2: FF         RST         0X38
48F3: FF         RST         0X38
48F4: FF         RST         0X38
48F5: FF         RST         0X38
48F6: FF         RST         0X38
48F7: FF         RST         0X38
48F8: FF         RST         0X38
48F9: FF         RST         0X38
48FA: FF         RST         0X38
48FB: FF         RST         0X38
48FC: FF         RST         0X38
48FD: FF         RST         0X38
48FE: FF         RST         0X38
48FF: FF         RST         0X38
4900: FF         RST         0X38
4901: FF         RST         0X38
4902: FF         RST         0X38
4903: FF         RST         0X38
4904: FF         RST         0X38
4905: FF         RST         0X38
4906: FF         RST         0X38
4907: FF         RST         0X38
4908: FF         RST         0X38
4909: FF         RST         0X38
490A: FF         RST         0X38
490B: FF         RST         0X38
490C: FF         RST         0X38
490D: FF         RST         0X38
490E: FF         RST         0X38
490F: FF         RST         0X38
4910: FF         RST         0X38
4911: FF         RST         0X38
4912: FF         RST         0X38
4913: FF         RST         0X38
4914: FF         RST         0X38
4915: FF         RST         0X38
4916: FF         RST         0X38
4917: FF         RST         0X38
4918: FF         RST         0X38
4919: FF         RST         0X38
491A: FF         RST         0X38
491B: FF         RST         0X38
491C: FF         RST         0X38
491D: FF         RST         0X38
491E: FF         RST         0X38
491F: FF         RST         0X38
4920: FF         RST         0X38
4921: FF         RST         0X38
4922: FF         RST         0X38
4923: FF         RST         0X38
4924: FF         RST         0X38
4925: FF         RST         0X38
4926: FF         RST         0X38
4927: FF         RST         0X38
4928: FF         RST         0X38
4929: FF         RST         0X38
492A: FF         RST         0X38
492B: FF         RST         0X38
492C: FF         RST         0X38
492D: FF         RST         0X38
492E: FF         RST         0X38
492F: FF         RST         0X38
4930: FF         RST         0X38
4931: FF         RST         0X38
4932: FF         RST         0X38
4933: FF         RST         0X38
4934: FF         RST         0X38
4935: FF         RST         0X38
4936: FF         RST         0X38
4937: FF         RST         0X38
4938: FF         RST         0X38
4939: FF         RST         0X38
493A: FF         RST         0X38
493B: FF         RST         0X38
493C: FF         RST         0X38
493D: FF         RST         0X38
493E: FF         RST         0X38
493F: FF         RST         0X38
4940: FF         RST         0X38
4941: FF         RST         0X38
4942: FF         RST         0X38
4943: FF         RST         0X38
4944: FF         RST         0X38
4945: FF         RST         0X38
4946: FF         RST         0X38
4947: FF         RST         0X38
4948: FF         RST         0X38
4949: FF         RST         0X38
494A: FF         RST         0X38
494B: FF         RST         0X38
494C: FF         RST         0X38
494D: FF         RST         0X38
494E: FF         RST         0X38
494F: FF         RST         0X38
4950: FF         RST         0X38
4951: FF         RST         0X38
4952: FF         RST         0X38
4953: FF         RST         0X38
4954: FF         RST         0X38
4955: FF         RST         0X38
4956: FF         RST         0X38
4957: FF         RST         0X38
4958: FF         RST         0X38
4959: FF         RST         0X38
495A: FF         RST         0X38
495B: FF         RST         0X38
495C: FF         RST         0X38
495D: FF         RST         0X38
495E: FF         RST         0X38
495F: FF         RST         0X38
4960: FF         RST         0X38
4961: FF         RST         0X38
4962: FF         RST         0X38
4963: FF         RST         0X38
4964: FF         RST         0X38
4965: FF         RST         0X38
4966: FF         RST         0X38
4967: FF         RST         0X38
4968: FF         RST         0X38
4969: FF         RST         0X38
496A: FF         RST         0X38
496B: FF         RST         0X38
496C: FF         RST         0X38
496D: FF         RST         0X38
496E: FF         RST         0X38
496F: FF         RST         0X38
4970: FF         RST         0X38
4971: FF         RST         0X38
4972: FF         RST         0X38
4973: FF         RST         0X38
4974: FF         RST         0X38
4975: FF         RST         0X38
4976: FF         RST         0X38
4977: FF         RST         0X38
4978: FF         RST         0X38
4979: FF         RST         0X38
497A: FF         RST         0X38
497B: FF         RST         0X38
497C: FF         RST         0X38
497D: FF         RST         0X38
497E: FF         RST         0X38
497F: FF         RST         0X38
4980: FF         RST         0X38
4981: FF         RST         0X38
4982: FF         RST         0X38
4983: FF         RST         0X38
4984: FF         RST         0X38
4985: FF         RST         0X38
4986: FF         RST         0X38
4987: FF         RST         0X38
4988: FF         RST         0X38
4989: FF         RST         0X38
498A: FF         RST         0X38
498B: FF         RST         0X38
498C: FF         RST         0X38
498D: FF         RST         0X38
498E: FF         RST         0X38
498F: FF         RST         0X38
4990: FF         RST         0X38
4991: FF         RST         0X38
4992: FF         RST         0X38
4993: FF         RST         0X38
4994: FF         RST         0X38
4995: FF         RST         0X38
4996: FF         RST         0X38
4997: FF         RST         0X38
4998: FF         RST         0X38
4999: FF         RST         0X38
499A: FF         RST         0X38
499B: FF         RST         0X38
499C: FF         RST         0X38
499D: FF         RST         0X38
499E: FF         RST         0X38
499F: FF         RST         0X38
49A0: FF         RST         0X38
49A1: FF         RST         0X38
49A2: FF         RST         0X38
49A3: FF         RST         0X38
49A4: FF         RST         0X38
49A5: FF         RST         0X38
49A6: FF         RST         0X38
49A7: FF         RST         0X38
49A8: FF         RST         0X38
49A9: FF         RST         0X38
49AA: FF         RST         0X38
49AB: FF         RST         0X38
49AC: FF         RST         0X38
49AD: FF         RST         0X38
49AE: FF         RST         0X38
49AF: FF         RST         0X38
49B0: FF         RST         0X38
49B1: FF         RST         0X38
49B2: FF         RST         0X38
49B3: FF         RST         0X38
49B4: FF         RST         0X38
49B5: FF         RST         0X38
49B6: FF         RST         0X38
49B7: FF         RST         0X38
49B8: FF         RST         0X38
49B9: FF         RST         0X38
49BA: FF         RST         0X38
49BB: FF         RST         0X38
49BC: FF         RST         0X38
49BD: FF         RST         0X38
49BE: FF         RST         0X38
49BF: FF         RST         0X38
49C0: FF         RST         0X38
49C1: FF         RST         0X38
49C2: FF         RST         0X38
49C3: FF         RST         0X38
49C4: FF         RST         0X38
49C5: FF         RST         0X38
49C6: FF         RST         0X38
49C7: FF         RST         0X38
49C8: FF         RST         0X38
49C9: FF         RST         0X38
49CA: FF         RST         0X38
49CB: FF         RST         0X38
49CC: FF         RST         0X38
49CD: FF         RST         0X38
49CE: FF         RST         0X38
49CF: FF         RST         0X38
49D0: FF         RST         0X38
49D1: FF         RST         0X38
49D2: FF         RST         0X38
49D3: FF         RST         0X38
49D4: FF         RST         0X38
49D5: FF         RST         0X38
49D6: FF         RST         0X38
49D7: FF         RST         0X38
49D8: FF         RST         0X38
49D9: FF         RST         0X38
49DA: FF         RST         0X38
49DB: FF         RST         0X38
49DC: FF         RST         0X38
49DD: FF         RST         0X38
49DE: FF         RST         0X38
49DF: FF         RST         0X38
49E0: FF         RST         0X38
49E1: FF         RST         0X38
49E2: FF         RST         0X38
49E3: FF         RST         0X38
49E4: FF         RST         0X38
49E5: FF         RST         0X38
49E6: FF         RST         0X38
49E7: FF         RST         0X38
49E8: FF         RST         0X38
49E9: FF         RST         0X38
49EA: FF         RST         0X38
49EB: FF         RST         0X38
49EC: FF         RST         0X38
49ED: FF         RST         0X38
49EE: FF         RST         0X38
49EF: FF         RST         0X38
49F0: FF         RST         0X38
49F1: FF         RST         0X38
49F2: FF         RST         0X38
49F3: FF         RST         0X38
49F4: FF         RST         0X38
49F5: FF         RST         0X38
49F6: FF         RST         0X38
49F7: FF         RST         0X38
49F8: FF         RST         0X38
49F9: FF         RST         0X38
49FA: FF         RST         0X38
49FB: FF         RST         0X38
49FC: FF         RST         0X38
49FD: FF         RST         0X38
49FE: FF         RST         0X38
49FF: FF         RST         0X38
4A00: FF         RST         0X38
4A01: FF         RST         0X38
4A02: FF         RST         0X38
4A03: FF         RST         0X38
4A04: FF         RST         0X38
4A05: FF         RST         0X38
4A06: FF         RST         0X38
4A07: FF         RST         0X38
4A08: FF         RST         0X38
4A09: FF         RST         0X38
4A0A: FF         RST         0X38
4A0B: FF         RST         0X38
4A0C: FF         RST         0X38
4A0D: FF         RST         0X38
4A0E: FF         RST         0X38
4A0F: FF         RST         0X38
4A10: FF         RST         0X38
4A11: FF         RST         0X38
4A12: FF         RST         0X38
4A13: FF         RST         0X38
4A14: FF         RST         0X38
4A15: FF         RST         0X38
4A16: FF         RST         0X38
4A17: FF         RST         0X38
4A18: FF         RST         0X38
4A19: FF         RST         0X38
4A1A: FF         RST         0X38
4A1B: FF         RST         0X38
4A1C: FF         RST         0X38
4A1D: FF         RST         0X38
4A1E: FF         RST         0X38
4A1F: FF         RST         0X38
4A20: FF         RST         0X38
4A21: FF         RST         0X38
4A22: FF         RST         0X38
4A23: FF         RST         0X38
4A24: FF         RST         0X38
4A25: FF         RST         0X38
4A26: FF         RST         0X38
4A27: FF         RST         0X38
4A28: FF         RST         0X38
4A29: FF         RST         0X38
4A2A: FF         RST         0X38
4A2B: FF         RST         0X38
4A2C: FF         RST         0X38
4A2D: FF         RST         0X38
4A2E: FF         RST         0X38
4A2F: FF         RST         0X38
4A30: FF         RST         0X38
4A31: FF         RST         0X38
4A32: FF         RST         0X38
4A33: FF         RST         0X38
4A34: FF         RST         0X38
4A35: FF         RST         0X38
4A36: FF         RST         0X38
4A37: FF         RST         0X38
4A38: FF         RST         0X38
4A39: FF         RST         0X38
4A3A: FF         RST         0X38
4A3B: FF         RST         0X38
4A3C: FF         RST         0X38
4A3D: FF         RST         0X38
4A3E: FF         RST         0X38
4A3F: FF         RST         0X38
4A40: FF         RST         0X38
4A41: FF         RST         0X38
4A42: FF         RST         0X38
4A43: FF         RST         0X38
4A44: FF         RST         0X38
4A45: FF         RST         0X38
4A46: FF         RST         0X38
4A47: FF         RST         0X38
4A48: FF         RST         0X38
4A49: FF         RST         0X38
4A4A: FF         RST         0X38
4A4B: FF         RST         0X38
4A4C: FF         RST         0X38
4A4D: FF         RST         0X38
4A4E: FF         RST         0X38
4A4F: FF         RST         0X38
4A50: FF         RST         0X38
4A51: FF         RST         0X38
4A52: FF         RST         0X38
4A53: FF         RST         0X38
4A54: FF         RST         0X38
4A55: FF         RST         0X38
4A56: FF         RST         0X38
4A57: FF         RST         0X38
4A58: FF         RST         0X38
4A59: FF         RST         0X38
4A5A: FF         RST         0X38
4A5B: FF         RST         0X38
4A5C: FF         RST         0X38
4A5D: FF         RST         0X38
4A5E: FF         RST         0X38
4A5F: FF         RST         0X38
4A60: FF         RST         0X38
4A61: FF         RST         0X38
4A62: FF         RST         0X38
4A63: FF         RST         0X38
4A64: FF         RST         0X38
4A65: FF         RST         0X38
4A66: FF         RST         0X38
4A67: FF         RST         0X38
4A68: FF         RST         0X38
4A69: FF         RST         0X38
4A6A: FF         RST         0X38
4A6B: FF         RST         0X38
4A6C: FF         RST         0X38
4A6D: FF         RST         0X38
4A6E: FF         RST         0X38
4A6F: FF         RST         0X38
4A70: FF         RST         0X38
4A71: FF         RST         0X38
4A72: FF         RST         0X38
4A73: FF         RST         0X38
4A74: FF         RST         0X38
4A75: FF         RST         0X38
4A76: FF         RST         0X38
4A77: FF         RST         0X38
4A78: FF         RST         0X38
4A79: FF         RST         0X38
4A7A: FF         RST         0X38
4A7B: FF         RST         0X38
4A7C: FF         RST         0X38
4A7D: FF         RST         0X38
4A7E: FF         RST         0X38
4A7F: FF         RST         0X38
4A80: FF         RST         0X38
4A81: FF         RST         0X38
4A82: FF         RST         0X38
4A83: FF         RST         0X38
4A84: FF         RST         0X38
4A85: FF         RST         0X38
4A86: FF         RST         0X38
4A87: FF         RST         0X38
4A88: FF         RST         0X38
4A89: FF         RST         0X38
4A8A: FF         RST         0X38
4A8B: FF         RST         0X38
4A8C: FF         RST         0X38
4A8D: FF         RST         0X38
4A8E: FF         RST         0X38
4A8F: FF         RST         0X38
4A90: FF         RST         0X38
4A91: FF         RST         0X38
4A92: FF         RST         0X38
4A93: FF         RST         0X38
4A94: FF         RST         0X38
4A95: FF         RST         0X38
4A96: FF         RST         0X38
4A97: FF         RST         0X38
4A98: FF         RST         0X38
4A99: FF         RST         0X38
4A9A: FF         RST         0X38
4A9B: FF         RST         0X38
4A9C: FF         RST         0X38
4A9D: FF         RST         0X38
4A9E: FF         RST         0X38
4A9F: FF         RST         0X38
4AA0: FF         RST         0X38
4AA1: FF         RST         0X38
4AA2: FF         RST         0X38
4AA3: FF         RST         0X38
4AA4: FF         RST         0X38
4AA5: FF         RST         0X38
4AA6: FF         RST         0X38
4AA7: FF         RST         0X38
4AA8: FF         RST         0X38
4AA9: FF         RST         0X38
4AAA: FF         RST         0X38
4AAB: FF         RST         0X38
4AAC: FF         RST         0X38
4AAD: FF         RST         0X38
4AAE: FF         RST         0X38
4AAF: FF         RST         0X38
4AB0: FF         RST         0X38
4AB1: FF         RST         0X38
4AB2: FF         RST         0X38
4AB3: FF         RST         0X38
4AB4: FF         RST         0X38
4AB5: FF         RST         0X38
4AB6: FF         RST         0X38
4AB7: FF         RST         0X38
4AB8: FF         RST         0X38
4AB9: FF         RST         0X38
4ABA: FF         RST         0X38
4ABB: FF         RST         0X38
4ABC: FF         RST         0X38
4ABD: FF         RST         0X38
4ABE: FF         RST         0X38
4ABF: FF         RST         0X38
4AC0: FF         RST         0X38
4AC1: FF         RST         0X38
4AC2: FF         RST         0X38
4AC3: FF         RST         0X38
4AC4: FF         RST         0X38
4AC5: FF         RST         0X38
4AC6: FF         RST         0X38
4AC7: FF         RST         0X38
4AC8: FF         RST         0X38
4AC9: FF         RST         0X38
4ACA: FF         RST         0X38
4ACB: FF         RST         0X38
4ACC: FF         RST         0X38
4ACD: FF         RST         0X38
4ACE: FF         RST         0X38
4ACF: FF         RST         0X38
4AD0: FF         RST         0X38
4AD1: FF         RST         0X38
4AD2: FF         RST         0X38
4AD3: FF         RST         0X38
4AD4: FF         RST         0X38
4AD5: FF         RST         0X38
4AD6: FF         RST         0X38
4AD7: FF         RST         0X38
4AD8: FF         RST         0X38
4AD9: FF         RST         0X38
4ADA: FF         RST         0X38
4ADB: FF         RST         0X38
4ADC: FF         RST         0X38
4ADD: FF         RST         0X38
4ADE: FF         RST         0X38
4ADF: FF         RST         0X38
4AE0: FF         RST         0X38
4AE1: FF         RST         0X38
4AE2: FF         RST         0X38
4AE3: FF         RST         0X38
4AE4: FF         RST         0X38
4AE5: FF         RST         0X38
4AE6: FF         RST         0X38
4AE7: FF         RST         0X38
4AE8: FF         RST         0X38
4AE9: FF         RST         0X38
4AEA: FF         RST         0X38
4AEB: FF         RST         0X38
4AEC: FF         RST         0X38
4AED: FF         RST         0X38
4AEE: FF         RST         0X38
4AEF: FF         RST         0X38
4AF0: FF         RST         0X38
4AF1: FF         RST         0X38
4AF2: FF         RST         0X38
4AF3: FF         RST         0X38
4AF4: FF         RST         0X38
4AF5: FF         RST         0X38
4AF6: FF         RST         0X38
4AF7: FF         RST         0X38
4AF8: FF         RST         0X38
4AF9: FF         RST         0X38
4AFA: FF         RST         0X38
4AFB: FF         RST         0X38
4AFC: FF         RST         0X38
4AFD: FF         RST         0X38
4AFE: FF         RST         0X38
4AFF: FF         RST         0X38
4B00: FF         RST         0X38
4B01: FF         RST         0X38
4B02: FF         RST         0X38
4B03: FF         RST         0X38
4B04: FF         RST         0X38
4B05: FF         RST         0X38
4B06: FF         RST         0X38
4B07: FF         RST         0X38
4B08: FF         RST         0X38
4B09: FF         RST         0X38
4B0A: FF         RST         0X38
4B0B: FF         RST         0X38
4B0C: FF         RST         0X38
4B0D: FF         RST         0X38
4B0E: FF         RST         0X38
4B0F: FF         RST         0X38
4B10: FF         RST         0X38
4B11: FF         RST         0X38
4B12: FF         RST         0X38
4B13: FF         RST         0X38
4B14: FF         RST         0X38
4B15: FF         RST         0X38
4B16: FF         RST         0X38
4B17: FF         RST         0X38
4B18: FF         RST         0X38
4B19: FF         RST         0X38
4B1A: FF         RST         0X38
4B1B: FF         RST         0X38
4B1C: FF         RST         0X38
4B1D: FF         RST         0X38
4B1E: FF         RST         0X38
4B1F: FF         RST         0X38
4B20: FF         RST         0X38
4B21: FF         RST         0X38
4B22: FF         RST         0X38
4B23: FF         RST         0X38
4B24: FF         RST         0X38
4B25: FF         RST         0X38
4B26: FF         RST         0X38
4B27: FF         RST         0X38
4B28: FF         RST         0X38
4B29: FF         RST         0X38
4B2A: FF         RST         0X38
4B2B: FF         RST         0X38
4B2C: FF         RST         0X38
4B2D: FF         RST         0X38
4B2E: FF         RST         0X38
4B2F: FF         RST         0X38
4B30: FF         RST         0X38
4B31: FF         RST         0X38
4B32: FF         RST         0X38
4B33: FF         RST         0X38
4B34: FF         RST         0X38
4B35: FF         RST         0X38
4B36: FF         RST         0X38
4B37: FF         RST         0X38
4B38: FF         RST         0X38
4B39: FF         RST         0X38
4B3A: FF         RST         0X38
4B3B: FF         RST         0X38
4B3C: FF         RST         0X38
4B3D: FF         RST         0X38
4B3E: FF         RST         0X38
4B3F: FF         RST         0X38
4B40: FF         RST         0X38
4B41: FF         RST         0X38
4B42: FF         RST         0X38
4B43: FF         RST         0X38
4B44: FF         RST         0X38
4B45: FF         RST         0X38
4B46: FF         RST         0X38
4B47: FF         RST         0X38
4B48: FF         RST         0X38
4B49: FF         RST         0X38
4B4A: FF         RST         0X38
4B4B: FF         RST         0X38
4B4C: FF         RST         0X38
4B4D: FF         RST         0X38
4B4E: FF         RST         0X38
4B4F: FF         RST         0X38
4B50: FF         RST         0X38
4B51: FF         RST         0X38
4B52: FF         RST         0X38
4B53: FF         RST         0X38
4B54: FF         RST         0X38
4B55: FF         RST         0X38
4B56: FF         RST         0X38
4B57: FF         RST         0X38
4B58: FF         RST         0X38
4B59: FF         RST         0X38
4B5A: FF         RST         0X38
4B5B: FF         RST         0X38
4B5C: FF         RST         0X38
4B5D: FF         RST         0X38
4B5E: FF         RST         0X38
4B5F: FF         RST         0X38
4B60: FF         RST         0X38
4B61: FF         RST         0X38
4B62: FF         RST         0X38
4B63: FF         RST         0X38
4B64: FF         RST         0X38
4B65: FF         RST         0X38
4B66: FF         RST         0X38
4B67: FF         RST         0X38
4B68: FF         RST         0X38
4B69: FF         RST         0X38
4B6A: FF         RST         0X38
4B6B: FF         RST         0X38
4B6C: FF         RST         0X38
4B6D: FF         RST         0X38
4B6E: FF         RST         0X38
4B6F: FF         RST         0X38
4B70: FF         RST         0X38
4B71: FF         RST         0X38
4B72: FF         RST         0X38
4B73: FF         RST         0X38
4B74: FF         RST         0X38
4B75: FF         RST         0X38
4B76: FF         RST         0X38
4B77: FF         RST         0X38
4B78: FF         RST         0X38
4B79: FF         RST         0X38
4B7A: FF         RST         0X38
4B7B: FF         RST         0X38
4B7C: FF         RST         0X38
4B7D: FF         RST         0X38
4B7E: FF         RST         0X38
4B7F: FF         RST         0X38
4B80: FF         RST         0X38
4B81: FF         RST         0X38
4B82: FF         RST         0X38
4B83: FF         RST         0X38
4B84: FF         RST         0X38
4B85: FF         RST         0X38
4B86: FF         RST         0X38
4B87: FF         RST         0X38
4B88: FF         RST         0X38
4B89: FF         RST         0X38
4B8A: FF         RST         0X38
4B8B: FF         RST         0X38
4B8C: FF         RST         0X38
4B8D: FF         RST         0X38
4B8E: FF         RST         0X38
4B8F: FF         RST         0X38
4B90: FF         RST         0X38
4B91: FF         RST         0X38
4B92: FF         RST         0X38
4B93: FF         RST         0X38
4B94: FF         RST         0X38
4B95: FF         RST         0X38
4B96: FF         RST         0X38
4B97: FF         RST         0X38
4B98: FF         RST         0X38
4B99: FF         RST         0X38
4B9A: FF         RST         0X38
4B9B: FF         RST         0X38
4B9C: FF         RST         0X38
4B9D: FF         RST         0X38
4B9E: FF         RST         0X38
4B9F: FF         RST         0X38
4BA0: FF         RST         0X38
4BA1: FF         RST         0X38
4BA2: FF         RST         0X38
4BA3: FF         RST         0X38
4BA4: FF         RST         0X38
4BA5: FF         RST         0X38
4BA6: FF         RST         0X38
4BA7: FF         RST         0X38
4BA8: FF         RST         0X38
4BA9: FF         RST         0X38
4BAA: FF         RST         0X38
4BAB: FF         RST         0X38
4BAC: FF         RST         0X38
4BAD: FF         RST         0X38
4BAE: FF         RST         0X38
4BAF: FF         RST         0X38
4BB0: FF         RST         0X38
4BB1: FF         RST         0X38
4BB2: FF         RST         0X38
4BB3: FF         RST         0X38
4BB4: FF         RST         0X38
4BB5: FF         RST         0X38
4BB6: FF         RST         0X38
4BB7: FF         RST         0X38
4BB8: FF         RST         0X38
4BB9: FF         RST         0X38
4BBA: FF         RST         0X38
4BBB: FF         RST         0X38
4BBC: FF         RST         0X38
4BBD: FF         RST         0X38
4BBE: FF         RST         0X38
4BBF: FF         RST         0X38
4BC0: FF         RST         0X38
4BC1: FF         RST         0X38
4BC2: FF         RST         0X38
4BC3: FF         RST         0X38
4BC4: FF         RST         0X38
4BC5: FF         RST         0X38
4BC6: FF         RST         0X38
4BC7: FF         RST         0X38
4BC8: FF         RST         0X38
4BC9: FF         RST         0X38
4BCA: FF         RST         0X38
4BCB: FF         RST         0X38
4BCC: FF         RST         0X38
4BCD: FF         RST         0X38
4BCE: FF         RST         0X38
4BCF: FF         RST         0X38
4BD0: FF         RST         0X38
4BD1: FF         RST         0X38
4BD2: FF         RST         0X38
4BD3: FF         RST         0X38
4BD4: FF         RST         0X38
4BD5: FF         RST         0X38
4BD6: FF         RST         0X38
4BD7: FF         RST         0X38
4BD8: FF         RST         0X38
4BD9: FF         RST         0X38
4BDA: FF         RST         0X38
4BDB: FF         RST         0X38
4BDC: FF         RST         0X38
4BDD: FF         RST         0X38
4BDE: FF         RST         0X38
4BDF: FF         RST         0X38
4BE0: FF         RST         0X38
4BE1: FF         RST         0X38
4BE2: FF         RST         0X38
4BE3: FF         RST         0X38
4BE4: FF         RST         0X38
4BE5: FF         RST         0X38
4BE6: FF         RST         0X38
4BE7: FF         RST         0X38
4BE8: FF         RST         0X38
4BE9: FF         RST         0X38
4BEA: FF         RST         0X38
4BEB: FF         RST         0X38
4BEC: FF         RST         0X38
4BED: FF         RST         0X38
4BEE: FF         RST         0X38
4BEF: FF         RST         0X38
4BF0: FF         RST         0X38
4BF1: FF         RST         0X38
4BF2: FF         RST         0X38
4BF3: FF         RST         0X38
4BF4: FF         RST         0X38
4BF5: FF         RST         0X38
4BF6: FF         RST         0X38
4BF7: FF         RST         0X38
4BF8: FF         RST         0X38
4BF9: FF         RST         0X38
4BFA: FF         RST         0X38
4BFB: FF         RST         0X38
4BFC: FF         RST         0X38
4BFD: FF         RST         0X38
4BFE: FF         RST         0X38
4BFF: FF         RST         0X38
4C00: FF         RST         0X38
4C01: FF         RST         0X38
4C02: FF         RST         0X38
4C03: FF         RST         0X38
4C04: FF         RST         0X38
4C05: FF         RST         0X38
4C06: FF         RST         0X38
4C07: FF         RST         0X38
4C08: FF         RST         0X38
4C09: FF         RST         0X38
4C0A: FF         RST         0X38
4C0B: FF         RST         0X38
4C0C: FF         RST         0X38
4C0D: FF         RST         0X38
4C0E: FF         RST         0X38
4C0F: FF         RST         0X38
4C10: FF         RST         0X38
4C11: FF         RST         0X38
4C12: FF         RST         0X38
4C13: FF         RST         0X38
4C14: FF         RST         0X38
4C15: FF         RST         0X38
4C16: FF         RST         0X38
4C17: FF         RST         0X38
4C18: FF         RST         0X38
4C19: FF         RST         0X38
4C1A: FF         RST         0X38
4C1B: FF         RST         0X38
4C1C: FF         RST         0X38
4C1D: FF         RST         0X38
4C1E: FF         RST         0X38
4C1F: FF         RST         0X38
4C20: FF         RST         0X38
4C21: FF         RST         0X38
4C22: FF         RST         0X38
4C23: FF         RST         0X38
4C24: FF         RST         0X38
4C25: FF         RST         0X38
4C26: FF         RST         0X38
4C27: FF         RST         0X38
4C28: FF         RST         0X38
4C29: FF         RST         0X38
4C2A: FF         RST         0X38
4C2B: FF         RST         0X38
4C2C: FF         RST         0X38
4C2D: FF         RST         0X38
4C2E: FF         RST         0X38
4C2F: FF         RST         0X38
4C30: FF         RST         0X38
4C31: FF         RST         0X38
4C32: FF         RST         0X38
4C33: FF         RST         0X38
4C34: FF         RST         0X38
4C35: FF         RST         0X38
4C36: FF         RST         0X38
4C37: FF         RST         0X38
4C38: FF         RST         0X38
4C39: FF         RST         0X38
4C3A: FF         RST         0X38
4C3B: FF         RST         0X38
4C3C: FF         RST         0X38
4C3D: FF         RST         0X38
4C3E: FF         RST         0X38
4C3F: FF         RST         0X38
4C40: FF         RST         0X38
4C41: FF         RST         0X38
4C42: FF         RST         0X38
4C43: FF         RST         0X38
4C44: FF         RST         0X38
4C45: FF         RST         0X38
4C46: FF         RST         0X38
4C47: FF         RST         0X38
4C48: FF         RST         0X38
4C49: FF         RST         0X38
4C4A: FF         RST         0X38
4C4B: FF         RST         0X38
4C4C: FF         RST         0X38
4C4D: FF         RST         0X38
4C4E: FF         RST         0X38
4C4F: FF         RST         0X38
4C50: FF         RST         0X38
4C51: FF         RST         0X38
4C52: FF         RST         0X38
4C53: FF         RST         0X38
4C54: FF         RST         0X38
4C55: FF         RST         0X38
4C56: FF         RST         0X38
4C57: FF         RST         0X38
4C58: FF         RST         0X38
4C59: FF         RST         0X38
4C5A: FF         RST         0X38
4C5B: FF         RST         0X38
4C5C: FF         RST         0X38
4C5D: FF         RST         0X38
4C5E: FF         RST         0X38
4C5F: FF         RST         0X38
4C60: FF         RST         0X38
4C61: FF         RST         0X38
4C62: FF         RST         0X38
4C63: FF         RST         0X38
4C64: FF         RST         0X38
4C65: FF         RST         0X38
4C66: FF         RST         0X38
4C67: FF         RST         0X38
4C68: FF         RST         0X38
4C69: FF         RST         0X38
4C6A: FF         RST         0X38
4C6B: FF         RST         0X38
4C6C: FF         RST         0X38
4C6D: FF         RST         0X38
4C6E: FF         RST         0X38
4C6F: FF         RST         0X38
4C70: FF         RST         0X38
4C71: FF         RST         0X38
4C72: FF         RST         0X38
4C73: FF         RST         0X38
4C74: FF         RST         0X38
4C75: FF         RST         0X38
4C76: FF         RST         0X38
4C77: FF         RST         0X38
4C78: FF         RST         0X38
4C79: FF         RST         0X38
4C7A: FF         RST         0X38
4C7B: FF         RST         0X38
4C7C: FF         RST         0X38
4C7D: FF         RST         0X38
4C7E: FF         RST         0X38
4C7F: FF         RST         0X38
4C80: FF         RST         0X38
4C81: FF         RST         0X38
4C82: FF         RST         0X38
4C83: FF         RST         0X38
4C84: FF         RST         0X38
4C85: FF         RST         0X38
4C86: FF         RST         0X38
4C87: FF         RST         0X38
4C88: FF         RST         0X38
4C89: FF         RST         0X38
4C8A: FF         RST         0X38
4C8B: FF         RST         0X38
4C8C: FF         RST         0X38
4C8D: FF         RST         0X38
4C8E: FF         RST         0X38
4C8F: FF         RST         0X38
4C90: FF         RST         0X38
4C91: FF         RST         0X38
4C92: FF         RST         0X38
4C93: FF         RST         0X38
4C94: FF         RST         0X38
4C95: FF         RST         0X38
4C96: FF         RST         0X38
4C97: FF         RST         0X38
4C98: FF         RST         0X38
4C99: FF         RST         0X38
4C9A: FF         RST         0X38
4C9B: FF         RST         0X38
4C9C: FF         RST         0X38
4C9D: FF         RST         0X38
4C9E: FF         RST         0X38
4C9F: FF         RST         0X38
4CA0: FF         RST         0X38
4CA1: FF         RST         0X38
4CA2: FF         RST         0X38
4CA3: FF         RST         0X38
4CA4: FF         RST         0X38
4CA5: FF         RST         0X38
4CA6: FF         RST         0X38
4CA7: FF         RST         0X38
4CA8: FF         RST         0X38
4CA9: FF         RST         0X38
4CAA: FF         RST         0X38
4CAB: FF         RST         0X38
4CAC: FF         RST         0X38
4CAD: FF         RST         0X38
4CAE: FF         RST         0X38
4CAF: FF         RST         0X38
4CB0: FF         RST         0X38
4CB1: FF         RST         0X38
4CB2: FF         RST         0X38
4CB3: FF         RST         0X38
4CB4: FF         RST         0X38
4CB5: FF         RST         0X38
4CB6: FF         RST         0X38
4CB7: FF         RST         0X38
4CB8: FF         RST         0X38
4CB9: FF         RST         0X38
4CBA: FF         RST         0X38
4CBB: FF         RST         0X38
4CBC: FF         RST         0X38
4CBD: FF         RST         0X38
4CBE: FF         RST         0X38
4CBF: FF         RST         0X38
4CC0: FF         RST         0X38
4CC1: FF         RST         0X38
4CC2: FF         RST         0X38
4CC3: FF         RST         0X38
4CC4: FF         RST         0X38
4CC5: FF         RST         0X38
4CC6: FF         RST         0X38
4CC7: FF         RST         0X38
4CC8: FF         RST         0X38
4CC9: FF         RST         0X38
4CCA: FF         RST         0X38
4CCB: FF         RST         0X38
4CCC: FF         RST         0X38
4CCD: FF         RST         0X38
4CCE: FF         RST         0X38
4CCF: FF         RST         0X38
4CD0: FF         RST         0X38
4CD1: FF         RST         0X38
4CD2: FF         RST         0X38
4CD3: FF         RST         0X38
4CD4: FF         RST         0X38
4CD5: FF         RST         0X38
4CD6: FF         RST         0X38
4CD7: FF         RST         0X38
4CD8: FF         RST         0X38
4CD9: FF         RST         0X38
4CDA: FF         RST         0X38
4CDB: FF         RST         0X38
4CDC: FF         RST         0X38
4CDD: FF         RST         0X38
4CDE: FF         RST         0X38
4CDF: FF         RST         0X38
4CE0: FF         RST         0X38
4CE1: FF         RST         0X38
4CE2: FF         RST         0X38
4CE3: FF         RST         0X38
4CE4: FF         RST         0X38
4CE5: FF         RST         0X38
4CE6: FF         RST         0X38
4CE7: FF         RST         0X38
4CE8: FF         RST         0X38
4CE9: FF         RST         0X38
4CEA: FF         RST         0X38
4CEB: FF         RST         0X38
4CEC: FF         RST         0X38
4CED: FF         RST         0X38
4CEE: FF         RST         0X38
4CEF: FF         RST         0X38
4CF0: FF         RST         0X38
4CF1: FF         RST         0X38
4CF2: FF         RST         0X38
4CF3: FF         RST         0X38
4CF4: FF         RST         0X38
4CF5: FF         RST         0X38
4CF6: FF         RST         0X38
4CF7: FF         RST         0X38
4CF8: FF         RST         0X38
4CF9: FF         RST         0X38
4CFA: FF         RST         0X38
4CFB: FF         RST         0X38
4CFC: FF         RST         0X38
4CFD: FF         RST         0X38
4CFE: FF         RST         0X38
4CFF: FF         RST         0X38
4D00: FF         RST         0X38
4D01: FF         RST         0X38
4D02: FF         RST         0X38
4D03: FF         RST         0X38
4D04: FF         RST         0X38
4D05: FF         RST         0X38
4D06: FF         RST         0X38
4D07: FF         RST         0X38
4D08: FF         RST         0X38
4D09: FF         RST         0X38
4D0A: FF         RST         0X38
4D0B: FF         RST         0X38
4D0C: FF         RST         0X38
4D0D: FF         RST         0X38
4D0E: FF         RST         0X38
4D0F: FF         RST         0X38
4D10: FF         RST         0X38
4D11: FF         RST         0X38
4D12: FF         RST         0X38
4D13: FF         RST         0X38
4D14: FF         RST         0X38
4D15: FF         RST         0X38
4D16: FF         RST         0X38
4D17: FF         RST         0X38
4D18: FF         RST         0X38
4D19: FF         RST         0X38
4D1A: FF         RST         0X38
4D1B: FF         RST         0X38
4D1C: FF         RST         0X38
4D1D: FF         RST         0X38
4D1E: FF         RST         0X38
4D1F: FF         RST         0X38
4D20: FF         RST         0X38
4D21: FF         RST         0X38
4D22: FF         RST         0X38
4D23: FF         RST         0X38
4D24: FF         RST         0X38
4D25: FF         RST         0X38
4D26: FF         RST         0X38
4D27: FF         RST         0X38
4D28: FF         RST         0X38
4D29: FF         RST         0X38
4D2A: FF         RST         0X38
4D2B: FF         RST         0X38
4D2C: FF         RST         0X38
4D2D: FF         RST         0X38
4D2E: FF         RST         0X38
4D2F: FF         RST         0X38
4D30: FF         RST         0X38
4D31: FF         RST         0X38
4D32: FF         RST         0X38
4D33: FF         RST         0X38
4D34: FF         RST         0X38
4D35: FF         RST         0X38
4D36: FF         RST         0X38
4D37: FF         RST         0X38
4D38: FF         RST         0X38
4D39: FF         RST         0X38
4D3A: FF         RST         0X38
4D3B: FF         RST         0X38
4D3C: FF         RST         0X38
4D3D: FF         RST         0X38
4D3E: FF         RST         0X38
4D3F: FF         RST         0X38
4D40: FF         RST         0X38
4D41: FF         RST         0X38
4D42: FF         RST         0X38
4D43: FF         RST         0X38
4D44: FF         RST         0X38
4D45: FF         RST         0X38
4D46: FF         RST         0X38
4D47: FF         RST         0X38
4D48: FF         RST         0X38
4D49: FF         RST         0X38
4D4A: FF         RST         0X38
4D4B: FF         RST         0X38
4D4C: FF         RST         0X38
4D4D: FF         RST         0X38
4D4E: FF         RST         0X38
4D4F: FF         RST         0X38
4D50: FF         RST         0X38
4D51: FF         RST         0X38
4D52: FF         RST         0X38
4D53: FF         RST         0X38
4D54: FF         RST         0X38
4D55: FF         RST         0X38
4D56: FF         RST         0X38
4D57: FF         RST         0X38
4D58: FF         RST         0X38
4D59: FF         RST         0X38
4D5A: FF         RST         0X38
4D5B: FF         RST         0X38
4D5C: FF         RST         0X38
4D5D: FF         RST         0X38
4D5E: FF         RST         0X38
4D5F: FF         RST         0X38
4D60: FF         RST         0X38
4D61: FF         RST         0X38
4D62: FF         RST         0X38
4D63: FF         RST         0X38
4D64: FF         RST         0X38
4D65: FF         RST         0X38
4D66: FF         RST         0X38
4D67: FF         RST         0X38
4D68: FF         RST         0X38
4D69: FF         RST         0X38
4D6A: FF         RST         0X38
4D6B: FF         RST         0X38
4D6C: FF         RST         0X38
4D6D: FF         RST         0X38
4D6E: FF         RST         0X38
4D6F: FF         RST         0X38
4D70: FF         RST         0X38
4D71: FF         RST         0X38
4D72: FF         RST         0X38
4D73: FF         RST         0X38
4D74: FF         RST         0X38
4D75: FF         RST         0X38
4D76: FF         RST         0X38
4D77: FF         RST         0X38
4D78: FF         RST         0X38
4D79: FF         RST         0X38
4D7A: FF         RST         0X38
4D7B: FF         RST         0X38
4D7C: FF         RST         0X38
4D7D: FF         RST         0X38
4D7E: FF         RST         0X38
4D7F: FF         RST         0X38
4D80: FF         RST         0X38
4D81: FF         RST         0X38
4D82: FF         RST         0X38
4D83: FF         RST         0X38
4D84: FF         RST         0X38
4D85: FF         RST         0X38
4D86: FF         RST         0X38
4D87: FF         RST         0X38
4D88: FF         RST         0X38
4D89: FF         RST         0X38
4D8A: FF         RST         0X38
4D8B: FF         RST         0X38
4D8C: FF         RST         0X38
4D8D: FF         RST         0X38
4D8E: FF         RST         0X38
4D8F: FF         RST         0X38
4D90: FF         RST         0X38
4D91: FF         RST         0X38
4D92: FF         RST         0X38
4D93: FF         RST         0X38
4D94: FF         RST         0X38
4D95: FF         RST         0X38
4D96: FF         RST         0X38
4D97: FF         RST         0X38
4D98: FF         RST         0X38
4D99: FF         RST         0X38
4D9A: FF         RST         0X38
4D9B: FF         RST         0X38
4D9C: FF         RST         0X38
4D9D: FF         RST         0X38
4D9E: FF         RST         0X38
4D9F: FF         RST         0X38
4DA0: FF         RST         0X38
4DA1: FF         RST         0X38
4DA2: FF         RST         0X38
4DA3: FF         RST         0X38
4DA4: FF         RST         0X38
4DA5: FF         RST         0X38
4DA6: FF         RST         0X38
4DA7: FF         RST         0X38
4DA8: FF         RST         0X38
4DA9: FF         RST         0X38
4DAA: FF         RST         0X38
4DAB: FF         RST         0X38
4DAC: FF         RST         0X38
4DAD: FF         RST         0X38
4DAE: FF         RST         0X38
4DAF: FF         RST         0X38
4DB0: FF         RST         0X38
4DB1: FF         RST         0X38
4DB2: FF         RST         0X38
4DB3: FF         RST         0X38
4DB4: FF         RST         0X38
4DB5: FF         RST         0X38
4DB6: FF         RST         0X38
4DB7: FF         RST         0X38
4DB8: FF         RST         0X38
4DB9: FF         RST         0X38
4DBA: FF         RST         0X38
4DBB: FF         RST         0X38
4DBC: FF         RST         0X38
4DBD: FF         RST         0X38
4DBE: FF         RST         0X38
4DBF: FF         RST         0X38
4DC0: FF         RST         0X38
4DC1: FF         RST         0X38
4DC2: FF         RST         0X38
4DC3: FF         RST         0X38
4DC4: FF         RST         0X38
4DC5: FF         RST         0X38
4DC6: FF         RST         0X38
4DC7: FF         RST         0X38
4DC8: FF         RST         0X38
4DC9: FF         RST         0X38
4DCA: FF         RST         0X38
4DCB: FF         RST         0X38
4DCC: FF         RST         0X38
4DCD: FF         RST         0X38
4DCE: FF         RST         0X38
4DCF: FF         RST         0X38
4DD0: FF         RST         0X38
4DD1: FF         RST         0X38
4DD2: FF         RST         0X38
4DD3: FF         RST         0X38
4DD4: FF         RST         0X38
4DD5: FF         RST         0X38
4DD6: FF         RST         0X38
4DD7: FF         RST         0X38
4DD8: FF         RST         0X38
4DD9: FF         RST         0X38
4DDA: FF         RST         0X38
4DDB: FF         RST         0X38
4DDC: FF         RST         0X38
4DDD: FF         RST         0X38
4DDE: FF         RST         0X38
4DDF: FF         RST         0X38
4DE0: FF         RST         0X38
4DE1: FF         RST         0X38
4DE2: FF         RST         0X38
4DE3: FF         RST         0X38
4DE4: FF         RST         0X38
4DE5: FF         RST         0X38
4DE6: FF         RST         0X38
4DE7: FF         RST         0X38
4DE8: FF         RST         0X38
4DE9: FF         RST         0X38
4DEA: FF         RST         0X38
4DEB: FF         RST         0X38
4DEC: FF         RST         0X38
4DED: FF         RST         0X38
4DEE: FF         RST         0X38
4DEF: FF         RST         0X38
4DF0: FF         RST         0X38
4DF1: FF         RST         0X38
4DF2: FF         RST         0X38
4DF3: FF         RST         0X38
4DF4: FF         RST         0X38
4DF5: FF         RST         0X38
4DF6: FF         RST         0X38
4DF7: FF         RST         0X38
4DF8: FF         RST         0X38
4DF9: FF         RST         0X38
4DFA: FF         RST         0X38
4DFB: FF         RST         0X38
4DFC: FF         RST         0X38
4DFD: FF         RST         0X38
4DFE: FF         RST         0X38
4DFF: FF         RST         0X38
4E00: FF         RST         0X38
4E01: FF         RST         0X38
4E02: FF         RST         0X38
4E03: FF         RST         0X38
4E04: FF         RST         0X38
4E05: FF         RST         0X38
4E06: FF         RST         0X38
4E07: FF         RST         0X38
4E08: FF         RST         0X38
4E09: FF         RST         0X38
4E0A: FF         RST         0X38
4E0B: FF         RST         0X38
4E0C: FF         RST         0X38
4E0D: FF         RST         0X38
4E0E: FF         RST         0X38
4E0F: FF         RST         0X38
4E10: FF         RST         0X38
4E11: FF         RST         0X38
4E12: FF         RST         0X38
4E13: FF         RST         0X38
4E14: FF         RST         0X38
4E15: FF         RST         0X38
4E16: FF         RST         0X38
4E17: FF         RST         0X38
4E18: FF         RST         0X38
4E19: FF         RST         0X38
4E1A: FF         RST         0X38
4E1B: FF         RST         0X38
4E1C: FF         RST         0X38
4E1D: FF         RST         0X38
4E1E: FF         RST         0X38
4E1F: FF         RST         0X38
4E20: FF         RST         0X38
4E21: FF         RST         0X38
4E22: FF         RST         0X38
4E23: FF         RST         0X38
4E24: FF         RST         0X38
4E25: FF         RST         0X38
4E26: FF         RST         0X38
4E27: FF         RST         0X38
4E28: FF         RST         0X38
4E29: FF         RST         0X38
4E2A: FF         RST         0X38
4E2B: FF         RST         0X38
4E2C: FF         RST         0X38
4E2D: FF         RST         0X38
4E2E: FF         RST         0X38
4E2F: FF         RST         0X38
4E30: FF         RST         0X38
4E31: FF         RST         0X38
4E32: FF         RST         0X38
4E33: FF         RST         0X38
4E34: FF         RST         0X38
4E35: FF         RST         0X38
4E36: FF         RST         0X38
4E37: FF         RST         0X38
4E38: FF         RST         0X38
4E39: FF         RST         0X38
4E3A: FF         RST         0X38
4E3B: FF         RST         0X38
4E3C: FF         RST         0X38
4E3D: FF         RST         0X38
4E3E: FF         RST         0X38
4E3F: FF         RST         0X38
4E40: FF         RST         0X38
4E41: FF         RST         0X38
4E42: FF         RST         0X38
4E43: FF         RST         0X38
4E44: FF         RST         0X38
4E45: FF         RST         0X38
4E46: FF         RST         0X38
4E47: FF         RST         0X38
4E48: FF         RST         0X38
4E49: FF         RST         0X38
4E4A: FF         RST         0X38
4E4B: FF         RST         0X38
4E4C: FF         RST         0X38
4E4D: FF         RST         0X38
4E4E: FF         RST         0X38
4E4F: FF         RST         0X38
4E50: FF         RST         0X38
4E51: FF         RST         0X38
4E52: FF         RST         0X38
4E53: FF         RST         0X38
4E54: FF         RST         0X38
4E55: FF         RST         0X38
4E56: FF         RST         0X38
4E57: FF         RST         0X38
4E58: FF         RST         0X38
4E59: FF         RST         0X38
4E5A: FF         RST         0X38
4E5B: FF         RST         0X38
4E5C: FF         RST         0X38
4E5D: FF         RST         0X38
4E5E: FF         RST         0X38
4E5F: FF         RST         0X38
4E60: FF         RST         0X38
4E61: FF         RST         0X38
4E62: FF         RST         0X38
4E63: FF         RST         0X38
4E64: FF         RST         0X38
4E65: FF         RST         0X38
4E66: FF         RST         0X38
4E67: FF         RST         0X38
4E68: FF         RST         0X38
4E69: FF         RST         0X38
4E6A: FF         RST         0X38
4E6B: FF         RST         0X38
4E6C: FF         RST         0X38
4E6D: FF         RST         0X38
4E6E: FF         RST         0X38
4E6F: FF         RST         0X38
4E70: FF         RST         0X38
4E71: FF         RST         0X38
4E72: FF         RST         0X38
4E73: FF         RST         0X38
4E74: FF         RST         0X38
4E75: FF         RST         0X38
4E76: FF         RST         0X38
4E77: FF         RST         0X38
4E78: FF         RST         0X38
4E79: FF         RST         0X38
4E7A: FF         RST         0X38
4E7B: FF         RST         0X38
4E7C: FF         RST         0X38
4E7D: FF         RST         0X38
4E7E: FF         RST         0X38
4E7F: FF         RST         0X38
4E80: FF         RST         0X38
4E81: FF         RST         0X38
4E82: FF         RST         0X38
4E83: FF         RST         0X38
4E84: FF         RST         0X38
4E85: FF         RST         0X38
4E86: FF         RST         0X38
4E87: FF         RST         0X38
4E88: FF         RST         0X38
4E89: FF         RST         0X38
4E8A: FF         RST         0X38
4E8B: FF         RST         0X38
4E8C: FF         RST         0X38
4E8D: FF         RST         0X38
4E8E: FF         RST         0X38
4E8F: FF         RST         0X38
4E90: FF         RST         0X38
4E91: FF         RST         0X38
4E92: FF         RST         0X38
4E93: FF         RST         0X38
4E94: FF         RST         0X38
4E95: FF         RST         0X38
4E96: FF         RST         0X38
4E97: FF         RST         0X38
4E98: FF         RST         0X38
4E99: FF         RST         0X38
4E9A: FF         RST         0X38
4E9B: FF         RST         0X38
4E9C: FF         RST         0X38
4E9D: FF         RST         0X38
4E9E: FF         RST         0X38
4E9F: FF         RST         0X38
4EA0: FF         RST         0X38
4EA1: FF         RST         0X38
4EA2: FF         RST         0X38
4EA3: FF         RST         0X38
4EA4: FF         RST         0X38
4EA5: FF         RST         0X38
4EA6: FF         RST         0X38
4EA7: FF         RST         0X38
4EA8: FF         RST         0X38
4EA9: FF         RST         0X38
4EAA: FF         RST         0X38
4EAB: FF         RST         0X38
4EAC: FF         RST         0X38
4EAD: FF         RST         0X38
4EAE: FF         RST         0X38
4EAF: FF         RST         0X38
4EB0: FF         RST         0X38
4EB1: FF         RST         0X38
4EB2: FF         RST         0X38
4EB3: FF         RST         0X38
4EB4: FF         RST         0X38
4EB5: FF         RST         0X38
4EB6: FF         RST         0X38
4EB7: FF         RST         0X38
4EB8: FF         RST         0X38
4EB9: FF         RST         0X38
4EBA: FF         RST         0X38
4EBB: FF         RST         0X38
4EBC: FF         RST         0X38
4EBD: FF         RST         0X38
4EBE: FF         RST         0X38
4EBF: FF         RST         0X38
4EC0: FF         RST         0X38
4EC1: FF         RST         0X38
4EC2: FF         RST         0X38
4EC3: FF         RST         0X38
4EC4: FF         RST         0X38
4EC5: FF         RST         0X38
4EC6: FF         RST         0X38
4EC7: FF         RST         0X38
4EC8: FF         RST         0X38
4EC9: FF         RST         0X38
4ECA: FF         RST         0X38
4ECB: FF         RST         0X38
4ECC: FF         RST         0X38
4ECD: FF         RST         0X38
4ECE: FF         RST         0X38
4ECF: FF         RST         0X38
4ED0: FF         RST         0X38
4ED1: FF         RST         0X38
4ED2: FF         RST         0X38
4ED3: FF         RST         0X38
4ED4: FF         RST         0X38
4ED5: FF         RST         0X38
4ED6: FF         RST         0X38
4ED7: FF         RST         0X38
4ED8: FF         RST         0X38
4ED9: FF         RST         0X38
4EDA: FF         RST         0X38
4EDB: FF         RST         0X38
4EDC: FF         RST         0X38
4EDD: FF         RST         0X38
4EDE: FF         RST         0X38
4EDF: FF         RST         0X38
4EE0: FF         RST         0X38
4EE1: FF         RST         0X38
4EE2: FF         RST         0X38
4EE3: FF         RST         0X38
4EE4: FF         RST         0X38
4EE5: FF         RST         0X38
4EE6: FF         RST         0X38
4EE7: FF         RST         0X38
4EE8: FF         RST         0X38
4EE9: FF         RST         0X38
4EEA: FF         RST         0X38
4EEB: FF         RST         0X38
4EEC: FF         RST         0X38
4EED: FF         RST         0X38
4EEE: FF         RST         0X38
4EEF: FF         RST         0X38
4EF0: FF         RST         0X38
4EF1: FF         RST         0X38
4EF2: FF         RST         0X38
4EF3: FF         RST         0X38
4EF4: FF         RST         0X38
4EF5: FF         RST         0X38
4EF6: FF         RST         0X38
4EF7: FF         RST         0X38
4EF8: FF         RST         0X38
4EF9: FF         RST         0X38
4EFA: FF         RST         0X38
4EFB: FF         RST         0X38
4EFC: FF         RST         0X38
4EFD: FF         RST         0X38
4EFE: FF         RST         0X38
4EFF: FF         RST         0X38
4F00: FF         RST         0X38
4F01: FF         RST         0X38
4F02: FF         RST         0X38
4F03: FF         RST         0X38
4F04: FF         RST         0X38
4F05: FF         RST         0X38
4F06: FF         RST         0X38
4F07: FF         RST         0X38
4F08: FF         RST         0X38
4F09: FF         RST         0X38
4F0A: FF         RST         0X38
4F0B: FF         RST         0X38
4F0C: FF         RST         0X38
4F0D: FF         RST         0X38
4F0E: FF         RST         0X38
4F0F: FF         RST         0X38
4F10: FF         RST         0X38
4F11: FF         RST         0X38
4F12: FF         RST         0X38
4F13: FF         RST         0X38
4F14: FF         RST         0X38
4F15: FF         RST         0X38
4F16: FF         RST         0X38
4F17: FF         RST         0X38
4F18: FF         RST         0X38
4F19: FF         RST         0X38
4F1A: FF         RST         0X38
4F1B: FF         RST         0X38
4F1C: FF         RST         0X38
4F1D: FF         RST         0X38
4F1E: FF         RST         0X38
4F1F: FF         RST         0X38
4F20: FF         RST         0X38
4F21: FF         RST         0X38
4F22: FF         RST         0X38
4F23: FF         RST         0X38
4F24: FF         RST         0X38
4F25: FF         RST         0X38
4F26: FF         RST         0X38
4F27: FF         RST         0X38
4F28: FF         RST         0X38
4F29: FF         RST         0X38
4F2A: FF         RST         0X38
4F2B: FF         RST         0X38
4F2C: FF         RST         0X38
4F2D: FF         RST         0X38
4F2E: FF         RST         0X38
4F2F: FF         RST         0X38
4F30: FF         RST         0X38
4F31: FF         RST         0X38
4F32: FF         RST         0X38
4F33: FF         RST         0X38
4F34: FF         RST         0X38
4F35: FF         RST         0X38
4F36: FF         RST         0X38
4F37: FF         RST         0X38
4F38: FF         RST         0X38
4F39: FF         RST         0X38
4F3A: FF         RST         0X38
4F3B: FF         RST         0X38
4F3C: FF         RST         0X38
4F3D: FF         RST         0X38
4F3E: FF         RST         0X38
4F3F: FF         RST         0X38
4F40: FF         RST         0X38
4F41: FF         RST         0X38
4F42: FF         RST         0X38
4F43: FF         RST         0X38
4F44: FF         RST         0X38
4F45: FF         RST         0X38
4F46: FF         RST         0X38
4F47: FF         RST         0X38
4F48: FF         RST         0X38
4F49: FF         RST         0X38
4F4A: FF         RST         0X38
4F4B: FF         RST         0X38
4F4C: FF         RST         0X38
4F4D: FF         RST         0X38
4F4E: FF         RST         0X38
4F4F: FF         RST         0X38
4F50: FF         RST         0X38
4F51: FF         RST         0X38
4F52: FF         RST         0X38
4F53: FF         RST         0X38
4F54: FF         RST         0X38
4F55: FF         RST         0X38
4F56: FF         RST         0X38
4F57: FF         RST         0X38
4F58: FF         RST         0X38
4F59: FF         RST         0X38
4F5A: FF         RST         0X38
4F5B: FF         RST         0X38
4F5C: FF         RST         0X38
4F5D: FF         RST         0X38
4F5E: FF         RST         0X38
4F5F: FF         RST         0X38
4F60: FF         RST         0X38
4F61: FF         RST         0X38
4F62: FF         RST         0X38
4F63: FF         RST         0X38
4F64: FF         RST         0X38
4F65: FF         RST         0X38
4F66: FF         RST         0X38
4F67: FF         RST         0X38
4F68: FF         RST         0X38
4F69: FF         RST         0X38
4F6A: FF         RST         0X38
4F6B: FF         RST         0X38
4F6C: FF         RST         0X38
4F6D: FF         RST         0X38
4F6E: FF         RST         0X38
4F6F: FF         RST         0X38
4F70: FF         RST         0X38
4F71: FF         RST         0X38
4F72: FF         RST         0X38
4F73: FF         RST         0X38
4F74: FF         RST         0X38
4F75: FF         RST         0X38
4F76: FF         RST         0X38
4F77: FF         RST         0X38
4F78: FF         RST         0X38
4F79: FF         RST         0X38
4F7A: FF         RST         0X38
4F7B: FF         RST         0X38
4F7C: FF         RST         0X38
4F7D: FF         RST         0X38
4F7E: FF         RST         0X38
4F7F: FF         RST         0X38
4F80: FF         RST         0X38
4F81: FF         RST         0X38
4F82: FF         RST         0X38
4F83: FF         RST         0X38
4F84: FF         RST         0X38
4F85: FF         RST         0X38
4F86: FF         RST         0X38
4F87: FF         RST         0X38
4F88: FF         RST         0X38
4F89: FF         RST         0X38
4F8A: FF         RST         0X38
4F8B: FF         RST         0X38
4F8C: FF         RST         0X38
4F8D: FF         RST         0X38
4F8E: FF         RST         0X38
4F8F: FF         RST         0X38
4F90: FF         RST         0X38
4F91: FF         RST         0X38
4F92: FF         RST         0X38
4F93: FF         RST         0X38
4F94: FF         RST         0X38
4F95: FF         RST         0X38
4F96: FF         RST         0X38
4F97: FF         RST         0X38
4F98: FF         RST         0X38
4F99: FF         RST         0X38
4F9A: FF         RST         0X38
4F9B: FF         RST         0X38
4F9C: FF         RST         0X38
4F9D: FF         RST         0X38
4F9E: FF         RST         0X38
4F9F: FF         RST         0X38
4FA0: FF         RST         0X38
4FA1: FF         RST         0X38
4FA2: FF         RST         0X38
4FA3: FF         RST         0X38
4FA4: FF         RST         0X38
4FA5: FF         RST         0X38
4FA6: FF         RST         0X38
4FA7: FF         RST         0X38
4FA8: FF         RST         0X38
4FA9: FF         RST         0X38
4FAA: FF         RST         0X38
4FAB: FF         RST         0X38
4FAC: FF         RST         0X38
4FAD: FF         RST         0X38
4FAE: FF         RST         0X38
4FAF: FF         RST         0X38
4FB0: FF         RST         0X38
4FB1: FF         RST         0X38
4FB2: FF         RST         0X38
4FB3: FF         RST         0X38
4FB4: FF         RST         0X38
4FB5: FF         RST         0X38
4FB6: FF         RST         0X38
4FB7: FF         RST         0X38
4FB8: FF         RST         0X38
4FB9: FF         RST         0X38
4FBA: FF         RST         0X38
4FBB: FF         RST         0X38
4FBC: FF         RST         0X38
4FBD: FF         RST         0X38
4FBE: FF         RST         0X38
4FBF: FF         RST         0X38
4FC0: FF         RST         0X38
4FC1: FF         RST         0X38
4FC2: FF         RST         0X38
4FC3: FF         RST         0X38
4FC4: FF         RST         0X38
4FC5: FF         RST         0X38
4FC6: FF         RST         0X38
4FC7: FF         RST         0X38
4FC8: FF         RST         0X38
4FC9: FF         RST         0X38
4FCA: FF         RST         0X38
4FCB: FF         RST         0X38
4FCC: FF         RST         0X38
4FCD: FF         RST         0X38
4FCE: FF         RST         0X38
4FCF: FF         RST         0X38
4FD0: FF         RST         0X38
4FD1: FF         RST         0X38
4FD2: FF         RST         0X38
4FD3: FF         RST         0X38
4FD4: FF         RST         0X38
4FD5: FF         RST         0X38
4FD6: FF         RST         0X38
4FD7: FF         RST         0X38
4FD8: FF         RST         0X38
4FD9: FF         RST         0X38
4FDA: FF         RST         0X38
4FDB: FF         RST         0X38
4FDC: FF         RST         0X38
4FDD: FF         RST         0X38
4FDE: FF         RST         0X38
4FDF: FF         RST         0X38
4FE0: FF         RST         0X38
4FE1: FF         RST         0X38
4FE2: FF         RST         0X38
4FE3: FF         RST         0X38
4FE4: FF         RST         0X38
4FE5: FF         RST         0X38
4FE6: FF         RST         0X38
4FE7: FF         RST         0X38
4FE8: FF         RST         0X38
4FE9: FF         RST         0X38
4FEA: FF         RST         0X38
4FEB: FF         RST         0X38
4FEC: FF         RST         0X38
4FED: FF         RST         0X38
4FEE: FF         RST         0X38
4FEF: FF         RST         0X38
4FF0: FF         RST         0X38
4FF1: FF         RST         0X38
4FF2: FF         RST         0X38
4FF3: FF         RST         0X38
4FF4: FF         RST         0X38
4FF5: FF         RST         0X38
4FF6: FF         RST         0X38
4FF7: FF         RST         0X38
4FF8: FF         RST         0X38
4FF9: FF         RST         0X38
4FFA: FF         RST         0X38
4FFB: FF         RST         0X38
4FFC: FF         RST         0X38
4FFD: FF         RST         0X38
4FFE: FF         RST         0X38
4FFF: FF         RST         0X38
5000: C7         RST         0X00
5001: 21 50 2E   LD           HL,$2E50
5004: 50         LD           D,B
5005: 3B         DEC         SP
5006: 50         LD           D,B
5007: 48         LD           C,B
5008: 50         LD           D,B
5009: 55         LD           D,L
500A: 50         LD           D,B
500B: 62         LD           H,D
500C: 50         LD           D,B
500D: 6F         LD           L,A
500E: 50         LD           D,B
500F: 7C         LD           A,H
5010: 50         LD           D,B
5011: 89         ADC         A,C
5012: 50         LD           D,B
5013: 96         SUB         (HL)
5014: 50         LD           D,B
5015: 96         SUB         (HL)
5016: 50         LD           D,B
5017: 96         SUB         (HL)
5018: 50         LD           D,B
5019: 96         SUB         (HL)
501A: 50         LD           D,B
501B: 96         SUB         (HL)
501C: 50         LD           D,B
501D: 96         SUB         (HL)
501E: 50         LD           D,B
501F: 96         SUB         (HL)
5020: 50         LD           D,B
5021: C5         PUSH       BC
5022: 21 11 D7   LD           HL,$D711
5025: 01 97 50   LD           BC,$5097
5028: 11 B8 50   LD           DE,$50B8
502B: C3 A7 33   JP           $33A7
502E: C5         PUSH       BC
502F: 21 11 D7   LD           HL,$D711
5032: 01 D8 50   LD           BC,$50D8
5035: 11 F1 50   LD           DE,$50F1
5038: C3 A7 33   JP           $33A7
503B: C5         PUSH       BC
503C: 21 11 D7   LD           HL,$D711
503F: 01 09 51   LD           BC,$5109
5042: 11 24 51   LD           DE,$5124
5045: C3 A7 33   JP           $33A7
5048: C5         PUSH       BC
5049: 21 11 D7   LD           HL,$D711
504C: 01 3E 51   LD           BC,$513E
504F: 11 57 51   LD           DE,$5157
5052: C3 A7 33   JP           $33A7
5055: C5         PUSH       BC
5056: 21 11 D7   LD           HL,$D711
5059: 01 6F 51   LD           BC,$516F
505C: 11 8A 51   LD           DE,$518A
505F: C3 A7 33   JP           $33A7
5062: C5         PUSH       BC
5063: 21 11 D7   LD           HL,$D711
5066: 01 A4 51   LD           BC,$51A4
5069: 11 B6 51   LD           DE,$51B6
506C: C3 A7 33   JP           $33A7
506F: C5         PUSH       BC
5070: 21 11 D7   LD           HL,$D711
5073: 01 C7 51   LD           BC,$51C7
5076: 11 D9 51   LD           DE,$51D9
5079: C3 A7 33   JP           $33A7
507C: C5         PUSH       BC
507D: 21 11 D7   LD           HL,$D711
5080: 01 EA 51   LD           BC,$51EA
5083: 11 FC 51   LD           DE,$51FC
5086: C3 A7 33   JP           $33A7
5089: C5         PUSH       BC
508A: 21 11 D7   LD           HL,$D711
508D: 01 0D 52   LD           BC,$520D
5090: 11 1F 52   LD           DE,$521F
5093: C3 A7 33   JP           $33A7
5096: C9         RET
5097: 00         NOP
5098: 01 02 03   LD           BC,$0302
509B: 04         INC         B
509C: 05         DEC         B
509D: 06 07      LD           B,$07
509F: 08 09 10   LD           ($1009),SP
50A2: 19         ADD         HL,DE
50A3: 20 29      JR           NZ,$50CE
50A5: 30 39      JR           NC,$50E0
50A7: 40         LD           B,B
50A8: 49         LD           C,C
50A9: 50         LD           D,B
50AA: 59         LD           E,C
50AB: 60         LD           H,B
50AC: 69         LD           L,C
50AD: 70         LD           (HL),B
50AE: 71         LD           (HL),C
50AF: 72         LD           (HL),D
50B0: 73         LD           (HL),E
50B1: 74         LD           (HL),H
50B2: 75         LD           (HL),L
50B3: 76         HALT
50B4: 77         LD           (HL),A
50B5: 78         LD           A,B
50B6: 79         LD           A,C
50B7: FF         RST         0X38
50B8: 25         DEC         H
50B9: 21 21 21   LD           HL,$2121
50BC: 21 21 21   LD           HL,$2121
50BF: 21 21 26   LD           HL,$2621
50C2: 23         INC         HL
50C3: 24         INC         H
50C4: 23         INC         HL
50C5: 24         INC         H
50C6: 23         INC         HL
50C7: 24         INC         H
50C8: 23         INC         HL
50C9: 24         INC         H
50CA: 23         INC         HL
50CB: 24         INC         H
50CC: 23         INC         HL
50CD: 24         INC         H
50CE: 27         DAA
50CF: 22         LD           (HLI),A
50D0: 22         LD           (HLI),A
50D1: 22         LD           (HLI),A
50D2: 22         LD           (HLI),A
50D3: 22         LD           (HLI),A
50D4: 22         LD           (HLI),A
50D5: 22         LD           (HLI),A
50D6: 22         LD           (HLI),A
50D7: 28 00      JR           Z,$50D9
50D9: 09         ADD         HL,BC
50DA: 10 19      STOP       $19
50DC: 20 29      JR           NZ,$5107
50DE: 30 39      JR           NC,$5119
50E0: 40         LD           B,B
50E1: 49         LD           C,C
50E2: 50         LD           D,B
50E3: 59         LD           E,C
50E4: 60         LD           H,B
50E5: 69         LD           L,C
50E6: 70         LD           (HL),B
50E7: 71         LD           (HL),C
50E8: 72         LD           (HL),D
50E9: 73         LD           (HL),E
50EA: 74         LD           (HL),H
50EB: 75         LD           (HL),L
50EC: 76         HALT
50ED: 77         LD           (HL),A
50EE: 78         LD           A,B
50EF: 79         LD           A,C
50F0: FF         RST         0X38
50F1: 23         INC         HL
50F2: 24         INC         H
50F3: 23         INC         HL
50F4: 24         INC         H
50F5: 23         INC         HL
50F6: 24         INC         H
50F7: 23         INC         HL
50F8: 24         INC         H
50F9: 23         INC         HL
50FA: 24         INC         H
50FB: 23         INC         HL
50FC: 24         INC         H
50FD: 23         INC         HL
50FE: 24         INC         H
50FF: 27         DAA
5100: 22         LD           (HLI),A
5101: 22         LD           (HLI),A
5102: 22         LD           (HLI),A
5103: 22         LD           (HLI),A
5104: 22         LD           (HLI),A
5105: 22         LD           (HLI),A
5106: 22         LD           (HLI),A
5107: 22         LD           (HLI),A
5108: 28 00      JR           Z,$510A
510A: 01 02 03   LD           BC,$0302
510D: 04         INC         B
510E: 05         DEC         B
510F: 06 07      LD           B,$07
5111: 08 09 10   LD           ($1009),SP
5114: 20 30      JR           NZ,$5146
5116: 40         LD           B,B
5117: 50         LD           D,B
5118: 60         LD           H,B
5119: 70         LD           (HL),B
511A: 71         LD           (HL),C
511B: 72         LD           (HL),D
511C: 73         LD           (HL),E
511D: 74         LD           (HL),H
511E: 75         LD           (HL),L
511F: 76         HALT
5120: 77         LD           (HL),A
5121: 78         LD           A,B
5122: 79         LD           A,C
5123: FF         RST         0X38
5124: 25         DEC         H
5125: 21 21 21   LD           HL,$2121
5128: 21 21 21   LD           HL,$2121
512B: 21 21 21   LD           HL,$2121
512E: 23         INC         HL
512F: 23         INC         HL
5130: 23         INC         HL
5131: 23         INC         HL
5132: 23         INC         HL
5133: 23         INC         HL
5134: 27         DAA
5135: 22         LD           (HLI),A
5136: 22         LD           (HLI),A
5137: 22         LD           (HLI),A
5138: 22         LD           (HLI),A
5139: 22         LD           (HLI),A
513A: 22         LD           (HLI),A
513B: 22         LD           (HLI),A
513C: 22         LD           (HLI),A
513D: 22         LD           (HLI),A
513E: 00         NOP
513F: 01 02 03   LD           BC,$0302
5142: 04         INC         B
5143: 05         DEC         B
5144: 06 07      LD           B,$07
5146: 08 09 10   LD           ($1009),SP
5149: 19         ADD         HL,DE
514A: 20 29      JR           NZ,$5175
514C: 30 39      JR           NC,$5187
514E: 40         LD           B,B
514F: 49         LD           C,C
5150: 50         LD           D,B
5151: 59         LD           E,C
5152: 60         LD           H,B
5153: 69         LD           L,C
5154: 70         LD           (HL),B
5155: 79         LD           A,C
5156: FF         RST         0X38
5157: 25         DEC         H
5158: 21 21 21   LD           HL,$2121
515B: 21 21 21   LD           HL,$2121
515E: 21 21 26   LD           HL,$2621
5161: 23         INC         HL
5162: 24         INC         H
5163: 23         INC         HL
5164: 24         INC         H
5165: 23         INC         HL
5166: 24         INC         H
5167: 23         INC         HL
5168: 24         INC         H
5169: 23         INC         HL
516A: 24         INC         H
516B: 23         INC         HL
516C: 24         INC         H
516D: 23         INC         HL
516E: 24         INC         H
516F: 00         NOP
5170: 01 02 03   LD           BC,$0302
5173: 04         INC         B
5174: 05         DEC         B
5175: 06 07      LD           B,$07
5177: 08 09 19   LD           ($1909),SP
517A: 29         ADD         HL,HL
517B: 39         ADD         HL,SP
517C: 49         LD           C,C
517D: 59         LD           E,C
517E: 69         LD           L,C
517F: 70         LD           (HL),B
5180: 71         LD           (HL),C
5181: 72         LD           (HL),D
5182: 73         LD           (HL),E
5183: 74         LD           (HL),H
5184: 75         LD           (HL),L
5185: 76         HALT
5186: 77         LD           (HL),A
5187: 78         LD           A,B
5188: 79         LD           A,C
5189: FF         RST         0X38
518A: 21 21 21   LD           HL,$2121
518D: 21 21 21   LD           HL,$2121
5190: 21 21 21   LD           HL,$2121
5193: 26 24      LD           H,$24
5195: 24         INC         H
5196: 24         INC         H
5197: 24         INC         H
5198: 24         INC         H
5199: 24         INC         H
519A: 22         LD           (HLI),A
519B: 22         LD           (HLI),A
519C: 22         LD           (HLI),A
519D: 22         LD           (HLI),A
519E: 22         LD           (HLI),A
519F: 22         LD           (HLI),A
51A0: 22         LD           (HLI),A
51A1: 22         LD           (HLI),A
51A2: 22         LD           (HLI),A
51A3: 28 00      JR           Z,$51A5
51A5: 10 20      STOP       $20
51A7: 30 40      JR           NC,$51E9
51A9: 50         LD           D,B
51AA: 60         LD           H,B
51AB: 70         LD           (HL),B
51AC: 71         LD           (HL),C
51AD: 72         LD           (HL),D
51AE: 73         LD           (HL),E
51AF: 74         LD           (HL),H
51B0: 75         LD           (HL),L
51B1: 76         HALT
51B2: 77         LD           (HL),A
51B3: 78         LD           A,B
51B4: 79         LD           A,C
51B5: FF         RST         0X38
51B6: 23         INC         HL
51B7: 23         INC         HL
51B8: 23         INC         HL
51B9: 23         INC         HL
51BA: 23         INC         HL
51BB: 23         INC         HL
51BC: 23         INC         HL
51BD: 27         DAA
51BE: 22         LD           (HLI),A
51BF: 22         LD           (HLI),A
51C0: 22         LD           (HLI),A
51C1: 22         LD           (HLI),A
51C2: 22         LD           (HLI),A
51C3: 22         LD           (HLI),A
51C4: 22         LD           (HLI),A
51C5: 22         LD           (HLI),A
51C6: 22         LD           (HLI),A
51C7: 09         ADD         HL,BC
51C8: 19         ADD         HL,DE
51C9: 29         ADD         HL,HL
51CA: 39         ADD         HL,SP
51CB: 49         LD           C,C
51CC: 59         LD           E,C
51CD: 69         LD           L,C
51CE: 70         LD           (HL),B
51CF: 71         LD           (HL),C
51D0: 72         LD           (HL),D
51D1: 73         LD           (HL),E
51D2: 74         LD           (HL),H
51D3: 75         LD           (HL),L
51D4: 76         HALT
51D5: 77         LD           (HL),A
51D6: 78         LD           A,B
51D7: 79         LD           A,C
51D8: FF         RST         0X38
51D9: 24         INC         H
51DA: 24         INC         H
51DB: 24         INC         H
51DC: 24         INC         H
51DD: 24         INC         H
51DE: 24         INC         H
51DF: 24         INC         H
51E0: 22         LD           (HLI),A
51E1: 22         LD           (HLI),A
51E2: 22         LD           (HLI),A
51E3: 22         LD           (HLI),A
51E4: 22         LD           (HLI),A
51E5: 22         LD           (HLI),A
51E6: 22         LD           (HLI),A
51E7: 22         LD           (HLI),A
51E8: 22         LD           (HLI),A
51E9: 28 00      JR           Z,$51EB
51EB: 01 02 03   LD           BC,$0302
51EE: 04         INC         B
51EF: 05         DEC         B
51F0: 06 07      LD           B,$07
51F2: 08 09 19   LD           ($1909),SP
51F5: 29         ADD         HL,HL
51F6: 39         ADD         HL,SP
51F7: 49         LD           C,C
51F8: 59         LD           E,C
51F9: 69         LD           L,C
51FA: 79         LD           A,C
51FB: FF         RST         0X38
51FC: 21 21 21   LD           HL,$2121
51FF: 21 21 21   LD           HL,$2121
5202: 21 21 21   LD           HL,$2121
5205: 26 24      LD           H,$24
5207: 24         INC         H
5208: 24         INC         H
5209: 24         INC         H
520A: 24         INC         H
520B: 24         INC         H
520C: 24         INC         H
520D: 00         NOP
520E: 01 02 03   LD           BC,$0302
5211: 04         INC         B
5212: 05         DEC         B
5213: 06 07      LD           B,$07
5215: 08 09 10   LD           ($1009),SP
5218: 20 30      JR           NZ,$524A
521A: 40         LD           B,B
521B: 50         LD           D,B
521C: 60         LD           H,B
521D: 70         LD           (HL),B
521E: FF         RST         0X38
521F: 25         DEC         H
5220: 21 21 21   LD           HL,$2121
5223: 21 21 21   LD           HL,$2121
5226: 21 21 21   LD           HL,$2121
5229: 23         INC         HL
522A: 23         INC         HL
522B: 23         INC         HL
522C: 23         INC         HL
522D: 23         INC         HL
522E: 23         INC         HL
522F: 23         INC         HL
5230: 18 20      JR           $5252
5232: 28 30      JR           Z,$5264
5234: 38 40      JR           C,$5276
5236: 48         LD           C,B
5237: 50         LD           D,B
5238: 58         LD           E,B
5239: 60         LD           H,B
523A: 68         LD           L,B
523B: 70         LD           (HL),B
523C: FA 62 D4   LD           A,($D462)
523F: A7         AND         A
5240: 28 0A      JR           Z,$524C
5242: 3D         DEC         A
5243: EA 62 D4   LD           ($D462),A
5246: 20 04      JR           NZ,$524C
5248: 3E 1B      LD           A,$1B
524A: E0 F3      LDFF00   ($F3),A
524C: FA 02 C5   LD           A,($C502)
524F: A7         AND         A
5250: 28 04      JR           Z,$5256
5252: 3D         DEC         A
5253: EA 02 C5   LD           ($C502),A
5256: FA AF C5   LD           A,($C5AF)
5259: A7         AND         A
525A: 28 0B      JR           Z,$5267
525C: 3D         DEC         A
525D: EA AF C5   LD           ($C5AF),A
5260: 20 05      JR           NZ,$5267
5262: F0 BF      LD           A,($BF)
5264: EA 68 D3   LD           ($D368),A
5267: FA A5 DB   LD           A,($DBA5)
526A: A7         AND         A
526B: 20 1F      JR           NZ,$528C
526D: F0 F6      LD           A,($F6)
526F: EA 54 DB   LD           ($DB54),A
5272: F0 F6      LD           A,($F6)
5274: FE F0      CP           $F0
5276: 38 14      JR           C,$528C
5278: FE F6      CP           $F6
527A: 30 10      JR           NC,$528C
527C: FA 14 C1   LD           A,($C114)
527F: 3C         INC         A
5280: FE A0      CP           $A0
5282: 20 05      JR           NZ,$5289
5284: 3E 0F      LD           A,$0F
5286: E0 F4      LDFF00   ($F4),A
5288: AF         XOR         A
5289: EA 14 C1   LD           ($C114),A
528C: FA 5B DB   LD           A,($DB5B)
528F: 5F         LD           E,A
5290: 50         LD           D,B
5291: 21 2D 52   LD           HL,$522D
5294: 19         ADD         HL,DE
5295: FA 5A DB   LD           A,($DB5A)
5298: BE         CP           (HL)
5299: 3E 00      LD           A,$00
529B: 20 01      JR           NZ,$529E
529D: 3C         INC         A
529E: EA A9 C5   LD           ($C5A9),A
52A1: FA AC C5   LD           A,($C5AC)
52A4: 3C         INC         A
52A5: FE 1A      CP           $1A
52A7: 20 01      JR           NZ,$52AA
52A9: AF         XOR         A
52AA: EA AC C5   LD           ($C5AC),A
52AD: F0 E7      LD           A,($E7)
52AF: E6 3F      AND         $3F
52B1: 20 0B      JR           NZ,$52BE
52B3: FA 47 DB   LD           A,($DB47)
52B6: FE FF      CP           $FF
52B8: 28 04      JR           Z,$52BE
52BA: 3C         INC         A
52BB: EA 47 DB   LD           ($DB47),A
52BE: FA 64 D4   LD           A,($D464)
52C1: A7         AND         A
52C2: C8         RET         Z
52C3: 3E E4      LD           A,$E4
52C5: EA 97 DB   LD           ($DB97),A
52C8: EA 99 DB   LD           ($DB99),A
52CB: 3E 1C      LD           A,$1C
52CD: EA 98 DB   LD           ($DB98),A
52D0: 21 64 D4   LD           HL,$D464
52D3: 35         DEC         (HL)
52D4: C8         RET         Z
52D5: 7E         LD           A,(HL)
52D6: 21 55 C1   LD           HL,$C155
52D9: 70         LD           (HL),B
52DA: FE 20      CP           $20
52DC: 38 1C      JR           C,$52FA
52DE: 17         RLA
52DF: 00         NOP
52E0: 00         NOP
52E1: 00         NOP
52E2: E6 04      AND         $04
52E4: D6 02      SUB         $02
52E6: EA 55 C1   LD           ($C155),A
52E9: 3E CC      LD           A,$CC
52EB: EA 97 DB   LD           ($DB97),A
52EE: EA 99 DB   LD           ($DB99),A
52F1: 3E 0C      LD           A,$0C
52F3: EA 98 DB   LD           ($DB98),A
52F6: 3E 02      LD           A,$02
52F8: E0 A1      LDFF00   ($A1),A
52FA: C9         RET
52FB: E4                              
52FC: E4                              
52FD: E4                              
52FE: E4                              
52FF: F9         LD           SP,HL
5300: F9         LD           SP,HL
5301: F9         LD           SP,HL
5302: F9         LD           SP,HL
5303: FE FE      CP           $FE
5305: FE FE      CP           $FE
5307: FF         RST         0X38
5308: FF         RST         0X38
5309: FF         RST         0X38
530A: FF         RST         0X38
530B: E4                              
530C: E4                              
530D: E4                              
530E: E4                              
530F: 94         SUB         H
5310: 94         SUB         H
5311: 94         SUB         H
5312: 94         SUB         H
5313: 40         LD           B,B
5314: 40         LD           B,B
5315: 40         LD           B,B
5316: 40         LD           B,B
5317: 00         NOP
5318: 00         NOP
5319: 00         NOP
531A: 00         NOP
531B: 00         NOP
531C: 00         NOP
531D: 00         NOP
531E: 01 01 00   LD           BC,$0001
5321: 00         NOP
5322: 00         NOP
5323: 00         NOP
5324: 00         NOP
5325: 00         NOP
5326: FA 96 DB   LD           A,($DB96)
5329: FE 07      CP           $07
532B: C0         RET         NZ
532C: FA 6B C1   LD           A,($C16B)
532F: FE 04      CP           $04
5331: C0         RET         NZ
5332: FA CB C3   LD           A,($C3CB)
5335: A7         AND         A
5336: 28 4F      JR           Z,$5387
5338: AF         XOR         A
5339: E0 D7      LDFF00   ($D7),A
533B: 57         LD           D,A
533C: FA 1C C1   LD           A,($C11C)
533F: 5F         LD           E,A
5340: 21 1B 53   LD           HL,$531B
5343: 19         ADD         HL,DE
5344: 7E         LD           A,(HL)
5345: A7         AND         A
5346: 20 3F      JR           NZ,$5387
5348: FA 9A DB   LD           A,($DB9A)
534B: FE 00      CP           $00
534D: 28 0E      JR           Z,$535D
534F: 21 7F C1   LD           HL,$C17F
5352: FA 9F C1   LD           A,($C19F)
5355: B6         OR           (HL)
5356: 20 05      JR           NZ,$535D
5358: FA CD C3   LD           A,($C3CD)
535B: E0 D7      LDFF00   ($D7),A
535D: FA CC C3   LD           A,($C3CC)
5360: 5F         LD           E,A
5361: F0 E7      LD           A,($E7)
5363: E6 03      AND         $03
5365: 83         ADD         A,E
5366: 5F         LD           E,A
5367: 21 FB 52   LD           HL,$52FB
536A: 19         ADD         HL,DE
536B: 7E         LD           A,(HL)
536C: EA 97 DB   LD           ($DB97),A
536F: EA AD C5   LD           ($C5AD),A
5372: F0 E7      LD           A,($E7)
5374: E6 01      AND         $01
5376: 20 0F      JR           NZ,$5387
5378: F0 D7      LD           A,($D7)
537A: 21 CC C3   LD           HL,$C3CC
537D: 96         SUB         (HL)
537E: 28 07      JR           Z,$5387
5380: E6 80      AND         $80
5382: 20 02      JR           NZ,$5386
5384: 34         INC         (HL)
5385: 34         INC         (HL)
5386: 35         DEC         (HL)
5387: C9         RET
5388: AF         XOR         A
5389: E0 BE      LDFF00   ($BE),A
538B: E0 F5      LDFF00   ($F5),A
538D: FA 95 DB   LD           A,($DB95)
5390: FE 07      CP           $07
5392: 28 4D      JR           Z,$53E1
5394: FA 24 C1   LD           A,($C124)
5397: 21 4F C1   LD           HL,$C14F
539A: B6         OR           (HL)
539B: 21 9F C1   LD           HL,$C19F
539E: B6         OR           (HL)
539F: 21 66 C1   LD           HL,$C166
53A2: B6         OR           (HL)
53A3: 20 3C      JR           NZ,$53E1
53A5: CD 91 08   CALL       $0891
53A8: 28 01      JR           Z,$53AB
53AA: 35         DEC         (HL)
53AB: CD 8C 08   CALL       $088C
53AE: 28 01      JR           Z,$53B1
53B0: 35         DEC         (HL)
53B1: 21 00 C3   LD           HL,$C300
53B4: 09         ADD         HL,BC
53B5: 7E         LD           A,(HL)
53B6: A7         AND         A
53B7: 28 01      JR           Z,$53BA
53B9: 35         DEC         (HL)
53BA: 21 80 C4   LD           HL,$C480
53BD: 09         ADD         HL,BC
53BE: 7E         LD           A,(HL)
53BF: A7         AND         A
53C0: 28 01      JR           Z,$53C3
53C2: 35         DEC         (HL)
53C3: F0 E7      LD           A,($E7)
53C5: E6 03      AND         $03
53C7: 20 06      JR           NZ,$53CF
53C9: CD 87 08   CALL       $0887
53CC: 28 01      JR           Z,$53CF
53CE: 35         DEC         (HL)
53CF: 21 20 C4   LD           HL,$C420
53D2: 09         ADD         HL,BC
53D3: 7E         LD           A,(HL)
53D4: A7         AND         A
53D5: 28 01      JR           Z,$53D8
53D7: 35         DEC         (HL)
53D8: CB 27      SLA         1,E
53DA: CB 27      SLA         1,E
53DC: E6 10      AND         $10
53DE: E0 ED      LDFF00   ($ED),A
53E0: C9         RET
53E1: AF         XOR         A
53E2: E0 ED      LDFF00   ($ED),A
53E4: C9         RET
53E5: 01 00 17   LD           BC,$1700
53E8: 50         LD           D,B
53E9: 7C         LD           A,H
53EA: 01 01 36   LD           BC,$3601
53ED: 50         LD           D,B
53EE: 7C         LD           A,H
53EF: 01 02 52   LD           BC,$5202
53F2: 50         LD           D,B
53F3: 7C         LD           A,H
53F4: 01 03 7A   LD           BC,$7A03
53F7: 50         LD           D,B
53F8: 7C         LD           A,H
53F9: 01 04 A1   LD           BC,$A104
53FC: 50         LD           D,B
53FD: 7C         LD           A,H
53FE: 01 05 D4   LD           BC,$D405
5401: 50         LD           D,B
5402: 7C         LD           A,H
5403: 01 06 0E   LD           BC,$0E06
5406: 50         LD           D,B
5407: 7C         LD           A,H
5408: 01 07 5D   LD           BC,$5D07
540B: 50         LD           D,B
540C: 7C         LD           A,H
540D: 01 08 70   LD           BC,$7008
5410: 50         LD           D,B
5411: 7C         LD           A,H
5412: 3B         DEC         SP
5413: 3A         LD           A,(HLD)
5414: 39         ADD         HL,SP
5415: 3B         DEC         SP
5416: 3F         CCF
5417: 3B         DEC         SP
5418: 39         ADD         HL,SP
5419: 3B         DEC         SP
541A: 3B         DEC         SP
541B: 3E 01      LD           A,$01
541D: EA 74 D4   LD           ($D474),A
5420: 3E 03      LD           A,$03
5422: EA 1C C1   LD           ($C11C),A
5425: FA A5 DB   LD           A,($DBA5)
5428: A7         AND         A
5429: 28 1F      JR           Z,$544A
542B: F0 F7      LD           A,($F7)
542D: FE 0A      CP           $0A
542F: 30 19      JR           NC,$544A
5431: 5F         LD           E,A
5432: CB 27      SLA         1,E
5434: CB 27      SLA         1,E
5436: 83         ADD         A,E
5437: 5F         LD           E,A
5438: 16 00      LD           D,$00
543A: 21 E5 53   LD           HL,$53E5
543D: 19         ADD         HL,DE
543E: 1E 05      LD           E,$05
5440: 01 01 D4   LD           BC,$D401
5443: 2A         LD           A,(HLI)
5444: 02         LD           (BC),A
5445: 03         INC         BC
5446: 1D         DEC         E
5447: 20 FA      JR           NZ,$5443
5449: C9         RET
544A: AF         XOR         A
544B: EA 01 D4   LD           ($D401),A
544E: EA 02 D4   LD           ($D402),A
5451: 3E 45      LD           A,$45
5453: EA 03 D4   LD           ($D403),A
5456: 3E 38      LD           A,$38
5458: EA 04 D4   LD           ($D404),A
545B: E0 98      LDFF00   ($98),A
545D: 3E 60      LD           A,$60
545F: EA 05 D4   LD           ($D405),A
5462: E0 99      LDFF00   ($99),A
5464: 3E 53      LD           A,$53
5466: EA 16 D4   LD           ($D416),A
5469: C9         RET
546A: E4                              
546B: E4                              
546C: E4                              
546D: E4                              
546E: 94         SUB         H
546F: 94         SUB         H
5470: 94         SUB         H
5471: 94         SUB         H
5472: 40         LD           B,B
5473: 40         LD           B,B
5474: 40         LD           B,B
5475: 40         LD           B,B
5476: 00         NOP
5477: 00         NOP
5478: 00         NOP
5479: 00         NOP
547A: 1C         INC         E
547B: 1C         INC         E
547C: 1C         INC         E
547D: 1C         INC         E
547E: 18 18      JR           $5498
5480: 18 18      JR           $549A
5482: 04         INC         B
5483: 04         INC         B
5484: 04         INC         B
5485: 04         INC         B
5486: 00         NOP
5487: 00         NOP
5488: 00         NOP
5489: 00         NOP
548A: 00         NOP
548B: 00         NOP
548C: 00         NOP
548D: 00         NOP
548E: 40         LD           B,B
548F: 40         LD           B,B
5490: 40         LD           B,B
5491: 40         LD           B,B
5492: 94         SUB         H
5493: 94         SUB         H
5494: 94         SUB         H
5495: 94         SUB         H
5496: E4                              
5497: E4                              
5498: E4                              
5499: E4                              
549A: 00         NOP
549B: 00         NOP
549C: 00         NOP
549D: 00         NOP
549E: 04         INC         B
549F: 04         INC         B
54A0: 04         INC         B
54A1: 04         INC         B
54A2: 18 18      JR           $54BC
54A4: 18 18      JR           $54BE
54A6: 1C         INC         E
54A7: 1C         INC         E
54A8: 1C         INC         E
54A9: 1C         INC         E
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
54B4: 00         NOP
54B5: 00         NOP
54B6: 00         NOP
54B7: 00         NOP
54B8: 00         NOP
54B9: 00         NOP
54BA: 00         NOP
54BB: 00         NOP
54BC: 00         NOP
54BD: 00         NOP
54BE: 00         NOP
54BF: 00         NOP
54C0: 00         NOP
54C1: 00         NOP
54C2: 00         NOP
54C3: 00         NOP
54C4: 00         NOP
54C5: 00         NOP
54C6: 00         NOP
54C7: 00         NOP
54C8: 00         NOP
54C9: 00         NOP
54CA: 00         NOP
54CB: 00         NOP
54CC: 00         NOP
54CD: 01 01 01   LD           BC,$0101
54D0: 01 01 01   LD           BC,$0101
54D3: 01 01 01   LD           BC,$0101
54D6: 01 01 00   LD           BC,$0001
54D9: 00         NOP
54DA: 00         NOP
54DB: 00         NOP
54DC: 00         NOP
54DD: FF         RST         0X38
54DE: FF         RST         0X38
54DF: FF         RST         0X38
54E0: FF         RST         0X38
54E1: FF         RST         0X38
54E2: FF         RST         0X38
54E3: FF         RST         0X38
54E4: FF         RST         0X38
54E5: FF         RST         0X38
54E6: FF         RST         0X38
54E7: FF         RST         0X38
54E8: 00         NOP
54E9: 00         NOP
54EA: 00         NOP
54EB: 00         NOP
54EC: 00         NOP
54ED: 00         NOP
54EE: 01 01 02   LD           BC,$0201
54F1: 02         LD           (BC),A
54F2: 02         LD           (BC),A
54F3: 02         LD           (BC),A
54F4: 02         LD           (BC),A
54F5: 01 01 00   LD           BC,$0001
54F8: 00         NOP
54F9: 00         NOP
54FA: 00         NOP
54FB: 00         NOP
54FC: 00         NOP
54FD: 00         NOP
54FE: FF         RST         0X38
54FF: FF         RST         0X38
5500: FE FE      CP           $FE
5502: FE FE      CP           $FE
5504: FE FF      CP           $FF
5506: FF         RST         0X38
5507: 00         NOP
5508: 00         NOP
5509: 00         NOP
550A: 00         NOP
550B: 01 01 02   LD           BC,$0201
550E: 02         LD           (BC),A
550F: 02         LD           (BC),A
5510: 03         INC         BC
5511: 03         INC         BC
5512: 03         INC         BC
5513: 03         INC         BC
5514: 03         INC         BC
5515: 02         LD           (BC),A
5516: 02         LD           (BC),A
5517: 02         LD           (BC),A
5518: 01 00 00   LD           BC,$0000
551B: FF         RST         0X38
551C: FF         RST         0X38
551D: FE FE      CP           $FE
551F: FE FD      CP           $FD
5521: FD                              
5522: FD                              
5523: FD                              
5524: FD                              
5525: FE FE      CP           $FE
5527: FE FF      CP           $FF
5529: 00         NOP
552A: 00         NOP
552B: 02         LD           (BC),A
552C: 02         LD           (BC),A
552D: 03         INC         BC
552E: 03         INC         BC
552F: 03         INC         BC
5530: 04         INC         B
5531: 04         INC         B
5532: 04         INC         B
5533: 04         INC         B
5534: 04         INC         B
5535: 03         INC         BC
5536: 03         INC         BC
5537: 03         INC         BC
5538: 02         LD           (BC),A
5539: 02         LD           (BC),A
553A: 00         NOP
553B: FE FE      CP           $FE
553D: FD                              
553E: FD                              
553F: FD                              
5540: FC                              
5541: FC                              
5542: FC                              
5543: FC                              
5544: FC                              
5545: FD                              
5546: FD                              
5547: FD                              
5548: FE FE      CP           $FE
554A: 00         NOP
554B: 01 01 02   LD           BC,$0201
554E: 02         LD           (BC),A
554F: 02         LD           (BC),A
5550: 03         INC         BC
5551: 03         INC         BC
5552: 03         INC         BC
5553: 03         INC         BC
5554: 03         INC         BC
5555: 02         LD           (BC),A
5556: 02         LD           (BC),A
5557: 02         LD           (BC),A
5558: 01 00 00   LD           BC,$0000
555B: FF         RST         0X38
555C: FF         RST         0X38
555D: FE FE      CP           $FE
555F: FE FD      CP           $FD
5561: FD                              
5562: FD                              
5563: FD                              
5564: FD                              
5565: FE FE      CP           $FE
5567: FE FF      CP           $FF
5569: 00         NOP
556A: 00         NOP
556B: 00         NOP
556C: 00         NOP
556D: 00         NOP
556E: 01 01 02   LD           BC,$0201
5571: 02         LD           (BC),A
5572: 02         LD           (BC),A
5573: 02         LD           (BC),A
5574: 02         LD           (BC),A
5575: 01 01 00   LD           BC,$0001
5578: 00         NOP
5579: 00         NOP
557A: 00         NOP
557B: 00         NOP
557C: 00         NOP
557D: 00         NOP
557E: FF         RST         0X38
557F: FF         RST         0X38
5580: FE FE      CP           $FE
5582: FE FE      CP           $FE
5584: FE FF      CP           $FF
5586: FF         RST         0X38
5587: 00         NOP
5588: 00         NOP
5589: 00         NOP
558A: 00         NOP
558B: 00         NOP
558C: 00         NOP
558D: 01 01 01   LD           BC,$0101
5590: 01 01 01   LD           BC,$0101
5593: 01 01 01   LD           BC,$0101
5596: 01 01 00   LD           BC,$0001
5599: 00         NOP
559A: 00         NOP
559B: 00         NOP
559C: 00         NOP
559D: FF         RST         0X38
559E: FF         RST         0X38
559F: FF         RST         0X38
55A0: FF         RST         0X38
55A1: FF         RST         0X38
55A2: FF         RST         0X38
55A3: FF         RST         0X38
55A4: FF         RST         0X38
55A5: FF         RST         0X38
55A6: FF         RST         0X38
55A7: FF         RST         0X38
55A8: 00         NOP
55A9: 00         NOP
55AA: 1E 0F      LD           E,$0F
55AC: 16 00      LD           D,$00
55AE: 21 80 C2   LD           HL,$C280
55B1: 19         ADD         HL,DE
55B2: 7E         LD           A,(HL)
55B3: FE 05      CP           $05
55B5: 20 41      JR           NZ,$55F8
55B7: 21 40 C3   LD           HL,$C340
55BA: 19         ADD         HL,DE
55BB: 7E         LD           A,(HL)
55BC: E6 20      AND         $20
55BE: 28 38      JR           Z,$55F8
55C0: 21 D0 C2   LD           HL,$C2D0
55C3: 19         ADD         HL,DE
55C4: 7E         LD           A,(HL)
55C5: FE 02      CP           $02
55C7: 20 2F      JR           NZ,$55F8
55C9: 21 00 C2   LD           HL,$C200
55CC: 19         ADD         HL,DE
55CD: F0 CE      LD           A,($CE)
55CF: C6 08      ADD         $08
55D1: 96         SUB         (HL)
55D2: C6 08      ADD         $08
55D4: FE 10      CP           $10
55D6: 30 20      JR           NC,$55F8
55D8: 21 10 C2   LD           HL,$C210
55DB: 19         ADD         HL,DE
55DC: F0 CD      LD           A,($CD)
55DE: C6 10      ADD         $10
55E0: 96         SUB         (HL)
55E1: C6 08      ADD         $08
55E3: FE 10      CP           $10
55E5: 30 11      JR           NC,$55F8
55E7: 21 50 C4   LD           HL,$C450
55EA: 19         ADD         HL,DE
55EB: 36 80      LD           (HL),$80
55ED: 21 D0 C2   LD           HL,$C2D0
55F0: 19         ADD         HL,DE
55F1: 72         LD           (HL),D
55F2: 21 F0 C2   LD           HL,$C2F0
55F5: 19         ADD         HL,DE
55F6: 36 18      LD           (HL),$18
55F8: 1D         DEC         E
55F9: 7B         LD           A,E
55FA: FE FF      CP           $FF
55FC: 20 B0      JR           NZ,$55AE
55FE: C9         RET
55FF: 0C         INC         C
5600: 0C         INC         C
5601: 0C         INC         C
5602: 0C         INC         C
5603: 0C         INC         C
5604: 0C         INC         C
5605: 0C         INC         C
5606: 0C         INC         C
5607: 0C         INC         C
5608: 0C         INC         C
5609: 0C         INC         C
560A: 0C         INC         C
560B: 0C         INC         C
560C: 0C         INC         C
560D: 0C         INC         C
560E: 0C         INC         C
560F: 0C         INC         C
5610: B6         OR           (HL)
5611: 0C         INC         C
5612: 0C         INC         C
5613: 0C         INC         C
5614: 0C         INC         C
5615: A3         AND         E
5616: 0C         INC         C
5617: 0C         INC         C
5618: 0C         INC         C
5619: 0C         INC         C
561A: 0C         INC         C
561B: 0C         INC         C
561C: 0C         INC         C
561D: 0C         INC         C
561E: 0C         INC         C
561F: 10 10      STOP       $10
5621: 10 10      STOP       $10
5623: 10 B5      STOP       $B5
5625: 10 10      STOP       $10
5627: 10 10      STOP       $10
5629: 10 10      STOP       $10
562B: 10 10      STOP       $10
562D: 10 10      STOP       $10
562F: A5         AND         L
5630: 10 A8      STOP       $A8
5632: 10 10      STOP       $10
5634: B7         OR           A
5635: B4         OR           H
5636: 10 10      STOP       $10
5638: 10 10      STOP       $10
563A: 10 10      STOP       $10
563C: 10 10      STOP       $10
563E: A1         AND         C
563F: 08 08 08   LD           ($0808),SP
5642: 08 10 B0   LD           ($B010),SP
5645: 10 10      STOP       $10
5647: 10 10      STOP       $10
5649: 10 83      STOP       $83
564B: 04         INC         B
564C: 04         INC         B
564D: 04         INC         B
564E: 04         INC         B
564F: A6         AND         (HL)
5650: 08 08 08   LD           ($0808),SP
5653: 10 10      STOP       $10
5655: 10 10      STOP       $10
5657: 10 10      STOP       $10
5659: 10 10      STOP       $10
565B: 04         INC         B
565C: BC         CP           H
565D: 04         INC         B
565E: 04         INC         B
565F: 08 08 A6   LD           ($A608),SP
5662: 08 10 B3   LD           ($B310),SP
5665: 10 10      STOP       $10
5667: 10 10      STOP       $10
5669: 10 10      STOP       $10
566B: 04         INC         B
566C: 04         INC         B
566D: 04         INC         B
566E: 04         INC         B
566F: 08 08 08   LD           ($0808),SP
5672: 08 B8 10   LD           ($10B8),SP
5675: 10 10      STOP       $10
5677: 10 10      STOP       $10
5679: 10 10      STOP       $10
567B: 04         INC         B
567C: 04         INC         B
567D: 04         INC         B
567E: 04         INC         B
567F: C4 10 0A   CALL       NZ,$0A10
5682: 0A         LD           A,(BC)
5683: 10 10      STOP       $10
5685: 10 10      STOP       $10
5687: 10 FC      STOP       $FC
5689: 9D         SBC         L
568A: 10 10      STOP       $10
568C: 10 10      STOP       $10
568E: BD         CP           L
568F: A0         AND         B
5690: 10 0A      STOP       $0A
5692: 0A         LD           A,(BC)
5693: A2         AND         D
5694: 10 10      STOP       $10
5696: 10 FB      STOP       $FB
5698: 10 10      STOP       $10
569A: 10 10      STOP       $10
569C: 10 10      STOP       $10
569E: 10 0A      STOP       $0A
56A0: 0A         LD           A,(BC)
56A1: 0A         LD           A,(BC)
56A2: 0A         LD           A,(BC)
56A3: 83         ADD         A,E
56A4: 10 10      STOP       $10
56A6: 10 BA      STOP       $BA
56A8: 10 B1      STOP       $B1
56AA: 10 10      STOP       $10
56AC: 10 10      STOP       $10
56AE: 10 0A      STOP       $0A
56B0: 0A         LD           A,(BC)
56B1: 0A         LD           A,(BC)
56B2: 83         ADD         A,E
56B3: A9         XOR         C
56B4: 10 10      STOP       $10
56B6: 10 10      STOP       $10
56B8: 10 10      STOP       $10
56BA: 10 10      STOP       $10
56BC: 10 10      STOP       $10
56BE: 10 A4      STOP       $A4
56C0: 10 10      STOP       $10
56C2: 10 AF      STOP       $AF
56C4: AF         XOR         A
56C5: B9         CP           C
56C6: 10 10      STOP       $10
56C8: 10 10      STOP       $10
56CA: B2         OR           D
56CB: 0B         DEC         BC
56CC: 0B         DEC         BC
56CD: 10 BE      STOP       $BE
56CF: 10 10      STOP       $10
56D1: 10 10      STOP       $10
56D3: AF         XOR         A
56D4: AF         XOR         A
56D5: F9         LD           SP,HL
56D6: FA 10 10   LD           A,($1010)
56D9: BB         CP           E
56DA: DB                              
56DB: 0B         DEC         BC
56DC: 0B         DEC         BC
56DD: 10 10      STOP       $10
56DF: 10 C3      STOP       $C3
56E1: 10 10      STOP       $10
56E3: 10 10      STOP       $10
56E5: 10 10      STOP       $10
56E7: 10 10      STOP       $10
56E9: 10 10      STOP       $10
56EB: 10 10      STOP       $10
56ED: 10 10      STOP       $10
56EF: 10 10      STOP       $10
56F1: 10 10      STOP       $10
56F3: 10 10      STOP       $10
56F5: 10 10      STOP       $10
56F7: 10 10      STOP       $10
56F9: 10 10      STOP       $10
56FB: 10 9E      STOP       $9E
56FD: 10 10      STOP       $10
56FF: 00         NOP
5700: 00         NOP
5701: 00         NOP
5702: 00         NOP
5703: 00         NOP
5704: 00         NOP
5705: 00         NOP
5706: 00         NOP
5707: 00         NOP
5708: 01 00 01   LD           BC,$0100
570B: 00         NOP
570C: 01 01 01   LD           BC,$0101
570F: 00         NOP
5710: 00         NOP
5711: 00         NOP
5712: 00         NOP
5713: 01 00 00   LD           BC,$0000
5716: 00         NOP
5717: 00         NOP
5718: 01 01 01   LD           BC,$0101
571B: 01 01 01   LD           BC,$0101
571E: 01 01 01   LD           BC,$0101
5721: 00         NOP
5722: 01 01 01   LD           BC,$0101
5725: 01 01 01   LD           BC,$0101
5728: 01 00 00   LD           BC,$0000
572B: 00         NOP
572C: 00         NOP
572D: 00         NOP
572E: 00         NOP
572F: 00         NOP
5730: 00         NOP
5731: 00         NOP
5732: 00         NOP
5733: 00         NOP
5734: 00         NOP
5735: 00         NOP
5736: 00         NOP
5737: 00         NOP
5738: 00         NOP
5739: 00         NOP
573A: 00         NOP
573B: 00         NOP
573C: 01 00 00   LD           BC,$0000
573F: 00         NOP
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
5759: 00         NOP
575A: 00         NOP
575B: 00         NOP
575C: 00         NOP
575D: 00         NOP
575E: 00         NOP
575F: 00         NOP
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
5779: 01 00 01   LD           BC,$0100
577C: 00         NOP
577D: 01 00 00   LD           BC,$0000
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
578C: 00         NOP
578D: 00         NOP
578E: 01 00 01   LD           BC,$0100
5791: 00         NOP
5792: 00         NOP
5793: 00         NOP
5794: 00         NOP
5795: 00         NOP
5796: 00         NOP
5797: 00         NOP
5798: 01 00 01   LD           BC,$0100
579B: 00         NOP
579C: 00         NOP
579D: 00         NOP
579E: 01 00 00   LD           BC,$0000
57A1: 00         NOP
57A2: 00         NOP
57A3: 00         NOP
57A4: 00         NOP
57A5: 00         NOP
57A6: 00         NOP
57A7: 00         NOP
57A8: 00         NOP
57A9: 00         NOP
57AA: 00         NOP
57AB: 00         NOP
57AC: 01 01 00   LD           BC,$0001
57AF: 01 00 00   LD           BC,$0000
57B2: 00         NOP
57B3: 00         NOP
57B4: 00         NOP
57B5: 00         NOP
57B6: 00         NOP
57B7: 00         NOP
57B8: 01 00 00   LD           BC,$0000
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
57C5: 01 00 00   LD           BC,$0000
57C8: 00         NOP
57C9: 00         NOP
57CA: 00         NOP
57CB: 01 00 00   LD           BC,$0000
57CE: 00         NOP
57CF: 00         NOP
57D0: 00         NOP
57D1: 00         NOP
57D2: 00         NOP
57D3: 00         NOP
57D4: 00         NOP
57D5: 00         NOP
57D6: 00         NOP
57D7: 00         NOP
57D8: 00         NOP
57D9: 00         NOP
57DA: 00         NOP
57DB: 00         NOP
57DC: 00         NOP
57DD: 00         NOP
57DE: 00         NOP
57DF: 01 00 00   LD           BC,$0000
57E2: 00         NOP
57E3: 00         NOP
57E4: 00         NOP
57E5: 00         NOP
57E6: 00         NOP
57E7: 00         NOP
57E8: 00         NOP
57E9: 00         NOP
57EA: 00         NOP
57EB: 00         NOP
57EC: 00         NOP
57ED: 00         NOP
57EE: 30 D0      JR           NC,$57C0
57F0: 00         NOP
57F1: 00         NOP
57F2: 18 E8      JR           $57DC
57F4: 00         NOP
57F5: 00         NOP
57F6: 30 D0      JR           NC,$57C8
57F8: 00         NOP
57F9: 00         NOP
57FA: 18 E8      JR           $57E4
57FC: 00         NOP
57FD: 00         NOP
57FE: 00         NOP
57FF: 00         NOP
5800: D0         RET         NC
5801: 30 00      JR           NC,$5803
5803: 00         NOP
5804: E8 18      ADD         SP,$18
5806: F4                              
5807: F4                              
5808: D0         RET         NC
5809: 00         NOP
580A: F8 F8      LDHL       SP,$F8
580C: E8 00      ADD         SP,$00
580E: 04         INC         B
580F: 04         INC         B
5810: 04         INC         B
5811: 04         INC         B
5812: 10 10      STOP       $10
5814: 10 10      STOP       $10
5816: 00         NOP
5817: 00         NOP
5818: 00         NOP
5819: 00         NOP
581A: 00         NOP
581B: 00         NOP
581C: 00         NOP
581D: 00         NOP
581E: 02         LD           (BC),A
581F: 06 00      LD           B,$00
5821: 04         INC         B
5822: FA 24 C1   LD           A,($C124)
5825: A7         AND         A
5826: 20 07      JR           NZ,$582F
5828: FA 1C C1   LD           A,($C11C)
582B: FE 06      CP           $06
582D: 20 0C      JR           NZ,$583B
582F: F0 EB      LD           A,($EB)
5831: FE A8      CP           $A8
5833: 28 06      JR           Z,$583B
5835: CD 7E 58   CALL       $587E
5838: C3 AF 3D   JP           $3DAF
583B: FA AE C5   LD           A,($C5AE)
583E: A7         AND         A
583F: 28 05      JR           Z,$5846
5841: 3D         DEC         A
5842: EA AE C5   LD           ($C5AE),A
5845: C9         RET
5846: FA 5C C1   LD           A,($C15C)
5849: FE 01      CP           $01
584B: C2 1E 59   JP           NZ,$591E
584E: 16 03      LD           D,$03
5850: F0 EB      LD           A,($EB)
5852: FE 02      CP           $02
5854: 20 02      JR           NZ,$5858
5856: 16 02      LD           D,$02
5858: 1E 10      LD           E,$10
585A: FA 00 DB   LD           A,($DB00)
585D: BA         CP           D
585E: 20 04      JR           NZ,$5864
5860: CB 23      SLA         1,E
5862: 18 08      JR           $586C
5864: FA 01 DB   LD           A,($DB01)
5867: BA         CP           D
5868: 28 02      JR           Z,$586C
586A: 1E 30      LD           E,$30
586C: F0 CC      LD           A,($CC)
586E: A3         AND         E
586F: CA 1E 59   JP           Z,$591E
5872: F0 9E      LD           A,($9E)
5874: 21 D0 C5   LD           HL,$C5D0
5877: 09         ADD         HL,BC
5878: 77         LD           (HL),A
5879: 21 F2 FF   LD           HL,$FFF2
587C: 36 08      LD           (HL),$08
587E: 21 80 C2   LD           HL,$C280
5881: 09         ADD         HL,BC
5882: 36 05      LD           (HL),$05
5884: F0 EB      LD           A,($EB)
5886: FE 02      CP           $02
5888: 20 07      JR           NZ,$5891
588A: CD 91 08   CALL       $0891
588D: 36 A0      LD           (HL),$A0
588F: 18 53      JR           $58E4
5891: 21 80 C2   LD           HL,$C280
5894: 09         ADD         HL,BC
5895: FE D6      CP           $D6
5897: 28 2F      JR           Z,$58C8
5899: FE D5      CP           $D5
589B: 28 2B      JR           Z,$58C8
589D: FE 6C      CP           $6C
589F: 28 27      JR           Z,$58C8
58A1: FE 9D      CP           $9D
58A3: 28 23      JR           Z,$58C8
58A5: FE A8      CP           $A8
58A7: 28 1F      JR           Z,$58C8
58A9: FE 98      CP           $98
58AB: 20 24      JR           NZ,$58D1
58AD: E5         PUSH       HL
58AE: F0 9E      LD           A,($9E)
58B0: 5F         LD           E,A
58B1: 50         LD           D,B
58B2: 21 1E 58   LD           HL,$581E
58B5: 19         ADD         HL,DE
58B6: 7E         LD           A,(HL)
58B7: 21 80 C3   LD           HL,$C380
58BA: 09         ADD         HL,BC
58BB: 77         LD           (HL),A
58BC: CD 91 08   CALL       $0891
58BF: CD ED 27   CALL       $27ED
58C2: E6 1F      AND         $1F
58C4: C6 30      ADD         $30
58C6: 77         LD           (HL),A
58C7: E1         POP         HL
58C8: 36 05      LD           (HL),$05
58CA: CD 8D 3B   CALL       $3B8D
58CD: 36 02      LD           (HL),$02
58CF: 18 13      JR           $58E4
58D1: FE 92      CP           $92
58D3: 20 09      JR           NZ,$58DE
58D5: 36 05      LD           (HL),$05
58D7: CD 8D 3B   CALL       $3B8D
58DA: 36 03      LD           (HL),$03
58DC: 18 06      JR           $58E4
58DE: FE 05      CP           $05
58E0: 28 02      JR           Z,$58E4
58E2: 36 08      LD           (HL),$08
58E4: 58         LD           E,B
58E5: F0 F9      LD           A,($F9)
58E7: A7         AND         A
58E8: 28 02      JR           Z,$58EC
58EA: 1E 08      LD           E,$08
58EC: F0 EB      LD           A,($EB)
58EE: FE 02      CP           $02
58F0: 20 04      JR           NZ,$58F6
58F2: 7B         LD           A,E
58F3: C6 04      ADD         $04
58F5: 5F         LD           E,A
58F6: F0 9E      LD           A,($9E)
58F8: 83         ADD         A,E
58F9: 5F         LD           E,A
58FA: 50         LD           D,B
58FB: 21 EE 57   LD           HL,$57EE
58FE: 19         ADD         HL,DE
58FF: 7E         LD           A,(HL)
5900: 21 40 C2   LD           HL,$C240
5903: 09         ADD         HL,BC
5904: 77         LD           (HL),A
5905: 21 FE 57   LD           HL,$57FE
5908: 19         ADD         HL,DE
5909: 7E         LD           A,(HL)
590A: 21 50 C2   LD           HL,$C250
590D: 09         ADD         HL,BC
590E: 77         LD           (HL),A
590F: 21 0E 58   LD           HL,$580E
5912: 19         ADD         HL,DE
5913: 7E         LD           A,(HL)
5914: 21 20 C3   LD           HL,$C320
5917: 09         ADD         HL,BC
5918: 77         LD           (HL),A
5919: 3E 0C      LD           A,$0C
591B: EA 9B C1   LD           ($C19B),A
591E: C9         RET
591F: AF         XOR         A
5920: EA 9F C1   LD           ($C19F),A
5923: C9         RET
5924: FA C9 C3   LD           A,($C3C9)
5927: A7         AND         A
5928: 20 0B      JR           NZ,$5935
592A: FA 1C C1   LD           A,($C11C)
592D: FE 03      CP           $03
592F: 28 EE      JR           Z,$591F
5931: FE 04      CP           $04
5933: 28 EA      JR           Z,$591F
5935: FA 95 DB   LD           A,($DB95)
5938: FE 01      CP           $01
593A: 28 1E      JR           Z,$595A
593C: FA CB C3   LD           A,($C3CB)
593F: A7         AND         A
5940: 20 18      JR           NZ,$595A
5942: F0 9D      LD           A,($9D)
5944: FE 6C      CP           $6C
5946: 28 12      JR           Z,$595A
5948: 3E 04      LD           A,$04
594A: EA 6B C1   LD           ($C16B),A
594D: 3E E4      LD           A,$E4
594F: EA 97 DB   LD           ($DB97),A
5952: EA 99 DB   LD           ($DB99),A
5955: 3E 1C      LD           A,$1C
5957: EA 98 DB   LD           ($DB98),A
595A: FA 01 D6   LD           A,($D601)
595D: A7         AND         A
595E: C0         RET         NZ
595F: 21 9F C1   LD           HL,$C19F
5962: 34         INC         (HL)
5963: C9         RET
5964: 21 7B C1   LD           HL,$C17B
5967: FA 24 C1   LD           A,($C124)
596A: B6         OR           (HL)
596B: 20 32      JR           NZ,$599F
596D: F0 98      LD           A,($98)
596F: D6 11      SUB         $11
5971: FE 7E      CP           $7E
5973: 38 14      JR           C,$5989
5975: F0 98      LD           A,($98)
5977: FE 50      CP           $50
5979: 30 07      JR           NC,$5982
597B: F0 98      LD           A,($98)
597D: 3C         INC         A
597E: E0 98      LDFF00   ($98),A
5980: 18 14      JR           $5996
5982: F0 98      LD           A,($98)
5984: 3D         DEC         A
5985: E0 98      LDFF00   ($98),A
5987: 18 0D      JR           $5996
5989: F0 99      LD           A,($99)
598B: D6 16      SUB         $16
598D: FE 5E      CP           $5E
598F: 38 0E      JR           C,$599F
5991: F0 99      LD           A,($99)
5993: 3D         DEC         A
5994: E0 99      LDFF00   ($99),A
5996: 3E 01      LD           A,$01
5998: E0 A1      LDFF00   ($A1),A
599A: 3E 02      LD           A,$02
599C: EA 11 C1   LD           ($C111),A
599F: C9         RET
59A0: 00         NOP
59A1: 02         LD           (BC),A
59A2: 00         NOP
59A3: FE 00      CP           $00
59A5: 00         NOP
59A6: 00         NOP
59A7: 00         NOP
59A8: 00         NOP
59A9: 00         NOP
59AA: 00         NOP
59AB: 00         NOP
59AC: 00         NOP
59AD: 02         LD           (BC),A
59AE: 00         NOP
59AF: FE FA      CP           $FA
59B1: 78         LD           A,B
59B2: C1         POP         BC
59B3: A7         AND         A
59B4: 28 04      JR           Z,$59BA
59B6: 3D         DEC         A
59B7: EA 78 C1   LD           ($C178),A
59BA: FA 57 C1   LD           A,($C157)
59BD: A7         AND         A
59BE: 28 1D      JR           Z,$59DD
59C0: 3D         DEC         A
59C1: EA 57 C1   LD           ($C157),A
59C4: E6 03      AND         $03
59C6: 21 58 C1   LD           HL,$C158
59C9: 86         ADD         A,(HL)
59CA: 5F         LD           E,A
59CB: 16 00      LD           D,$00
59CD: 21 A0 59   LD           HL,$59A0
59D0: 19         ADD         HL,DE
59D1: 7E         LD           A,(HL)
59D2: EA 55 C1   LD           ($C155),A
59D5: 21 A8 59   LD           HL,$59A8
59D8: 19         ADD         HL,DE
59D9: 7E         LD           A,(HL)
59DA: EA 56 C1   LD           ($C156),A
59DD: C9         RET
59DE: 21 11 D7   LD           HL,$D711
59E1: 19         ADD         HL,DE
59E2: F0 AF      LD           A,($AF)
59E4: FE 8E      CP           $8E
59E6: 20 35      JR           NZ,$5A1D
59E8: 36 AA      LD           (HL),$AA
59EA: CD 39 28   CALL       $2839
59ED: 21 01 D6   LD           HL,$D601
59F0: FA 00 D6   LD           A,($D600)
59F3: 5F         LD           E,A
59F4: C6 0A      ADD         $0A
59F6: EA 00 D6   LD           ($D600),A
59F9: 16 00      LD           D,$00
59FB: 19         ADD         HL,DE
59FC: F0 CF      LD           A,($CF)
59FE: 22         LD           (HLI),A
59FF: F0 D0      LD           A,($D0)
5A01: 22         LD           (HLI),A
5A02: 3E 81      LD           A,$81
5A04: 22         LD           (HLI),A
5A05: 3E 14      LD           A,$14
5A07: 22         LD           (HLI),A
5A08: 3E 16      LD           A,$16
5A0A: 22         LD           (HLI),A
5A0B: F0 CF      LD           A,($CF)
5A0D: 22         LD           (HLI),A
5A0E: F0 D0      LD           A,($D0)
5A10: 3C         INC         A
5A11: 22         LD           (HLI),A
5A12: 3E 81      LD           A,$81
5A14: 22         LD           (HLI),A
5A15: 3E 15      LD           A,$15
5A17: 22         LD           (HLI),A
5A18: 3E 17      LD           A,$17
5A1A: C3 E4 5A   JP           $5AE4
5A1D: FE D3      CP           $D3
5A1F: 20 03      JR           NZ,$5A24
5A21: C3 E9 5A   JP           $5AE9
5A24: FA A5 DB   LD           A,($DBA5)
5A27: A7         AND         A
5A28: CA 9F 5A   JP           Z,$5A9F
5A2B: F0 F9      LD           A,($F9)
5A2D: A7         AND         A
5A2E: 28 3B      JR           Z,$5A6B
5A30: F0 AF      LD           A,($AF)
5A32: FE 8A      CP           $8A
5A34: 20 35      JR           NZ,$5A6B
5A36: 36 04      LD           (HL),$04
5A38: CD 39 28   CALL       $2839
5A3B: 21 01 D6   LD           HL,$D601
5A3E: FA 00 D6   LD           A,($D600)
5A41: 5F         LD           E,A
5A42: C6 0A      ADD         $0A
5A44: EA 00 D6   LD           ($D600),A
5A47: 16 00      LD           D,$00
5A49: 19         ADD         HL,DE
5A4A: F0 CF      LD           A,($CF)
5A4C: 22         LD           (HLI),A
5A4D: F0 D0      LD           A,($D0)
5A4F: 22         LD           (HLI),A
5A50: 3E 81      LD           A,$81
5A52: 22         LD           (HLI),A
5A53: 3E 7E      LD           A,$7E
5A55: 22         LD           (HLI),A
5A56: 3E 7E      LD           A,$7E
5A58: 22         LD           (HLI),A
5A59: F0 CF      LD           A,($CF)
5A5B: 22         LD           (HLI),A
5A5C: F0 D0      LD           A,($D0)
5A5E: 3C         INC         A
5A5F: 22         LD           (HLI),A
5A60: 3E 81      LD           A,$81
5A62: 22         LD           (HLI),A
5A63: 3E 7E      LD           A,$7E
5A65: 22         LD           (HLI),A
5A66: 3E 7E      LD           A,$7E
5A68: C3 E4 5A   JP           $5AE4
5A6B: 36 0D      LD           (HL),$0D
5A6D: CD 39 28   CALL       $2839
5A70: 21 01 D6   LD           HL,$D601
5A73: FA 00 D6   LD           A,($D600)
5A76: 5F         LD           E,A
5A77: C6 0A      ADD         $0A
5A79: EA 00 D6   LD           ($D600),A
5A7C: 16 00      LD           D,$00
5A7E: 19         ADD         HL,DE
5A7F: F0 CF      LD           A,($CF)
5A81: 22         LD           (HLI),A
5A82: F0 D0      LD           A,($D0)
5A84: 22         LD           (HLI),A
5A85: 3E 81      LD           A,$81
5A87: 22         LD           (HLI),A
5A88: 3E 10      LD           A,$10
5A8A: 22         LD           (HLI),A
5A8B: 3E 12      LD           A,$12
5A8D: 22         LD           (HLI),A
5A8E: F0 CF      LD           A,($CF)
5A90: 22         LD           (HLI),A
5A91: F0 D0      LD           A,($D0)
5A93: 3C         INC         A
5A94: 22         LD           (HLI),A
5A95: 3E 81      LD           A,$81
5A97: 22         LD           (HLI),A
5A98: 3E 11      LD           A,$11
5A9A: 22         LD           (HLI),A
5A9B: 3E 13      LD           A,$13
5A9D: 18 45      JR           $5AE4
5A9F: F0 AF      LD           A,($AF)
5AA1: FE 20      CP           $20
5AA3: 20 0D      JR           NZ,$5AB2
5AA5: F0 F6      LD           A,($F6)
5AA7: FE 52      CP           $52
5AA9: 28 04      JR           Z,$5AAF
5AAB: FE 04      CP           $04
5AAD: 20 03      JR           NZ,$5AB2
5AAF: C3 0C 5B   JP           $5B0C
5AB2: 36 04      LD           (HL),$04
5AB4: CD 39 28   CALL       $2839
5AB7: 21 01 D6   LD           HL,$D601
5ABA: FA 00 D6   LD           A,($D600)
5ABD: 5F         LD           E,A
5ABE: C6 0A      ADD         $0A
5AC0: EA 00 D6   LD           ($D600),A
5AC3: 16 00      LD           D,$00
5AC5: 19         ADD         HL,DE
5AC6: F0 CF      LD           A,($CF)
5AC8: 22         LD           (HLI),A
5AC9: F0 D0      LD           A,($D0)
5ACB: 22         LD           (HLI),A
5ACC: 3E 81      LD           A,$81
5ACE: 22         LD           (HLI),A
5ACF: 3E 5A      LD           A,$5A
5AD1: 22         LD           (HLI),A
5AD2: 3E 7F      LD           A,$7F
5AD4: 22         LD           (HLI),A
5AD5: F0 CF      LD           A,($CF)
5AD7: 22         LD           (HLI),A
5AD8: F0 D0      LD           A,($D0)
5ADA: 3C         INC         A
5ADB: 22         LD           (HLI),A
5ADC: 3E 81      LD           A,$81
5ADE: 22         LD           (HLI),A
5ADF: 3E 7F      LD           A,$7F
5AE1: 22         LD           (HLI),A
5AE2: 3E 5A      LD           A,$5A
5AE4: 22         LD           (HLI),A
5AE5: 3E 00      LD           A,$00
5AE7: 22         LD           (HLI),A
5AE8: C9         RET
5AE9: F0 F6      LD           A,($F6)
5AEB: FE 75      CP           $75
5AED: 28 0C      JR           Z,$5AFB
5AEF: FE 07      CP           $07
5AF1: 28 08      JR           Z,$5AFB
5AF3: FE AA      CP           $AA
5AF5: 28 04      JR           Z,$5AFB
5AF7: FE 4A      CP           $4A
5AF9: 20 6E      JR           NZ,$5B69
5AFB: 21 11 D7   LD           HL,$D711
5AFE: 19         ADD         HL,DE
5AFF: E5         PUSH       HL
5B00: F0 F6      LD           A,($F6)
5B02: 5F         LD           E,A
5B03: 16 00      LD           D,$00
5B05: 21 00 D8   LD           HL,$D800
5B08: 19         ADD         HL,DE
5B09: CB E6      SET         1,E
5B0B: E1         POP         HL
5B0C: 36 C6      LD           (HL),$C6
5B0E: CD 39 28   CALL       $2839
5B11: 21 01 D6   LD           HL,$D601
5B14: FA 00 D6   LD           A,($D600)
5B17: 5F         LD           E,A
5B18: C6 0A      ADD         $0A
5B1A: EA 00 D6   LD           ($D600),A
5B1D: 16 00      LD           D,$00
5B1F: 19         ADD         HL,DE
5B20: F0 CF      LD           A,($CF)
5B22: 22         LD           (HLI),A
5B23: F0 D0      LD           A,($D0)
5B25: 22         LD           (HLI),A
5B26: 3E 81      LD           A,$81
5B28: 22         LD           (HLI),A
5B29: 3E 68      LD           A,$68
5B2B: 22         LD           (HLI),A
5B2C: 3E 77      LD           A,$77
5B2E: 22         LD           (HLI),A
5B2F: F0 CF      LD           A,($CF)
5B31: 22         LD           (HLI),A
5B32: F0 D0      LD           A,($D0)
5B34: 3C         INC         A
5B35: 22         LD           (HLI),A
5B36: 3E 81      LD           A,$81
5B38: 22         LD           (HLI),A
5B39: 3E 69      LD           A,$69
5B3B: 22         LD           (HLI),A
5B3C: 3E 4B      LD           A,$4B
5B3E: 22         LD           (HLI),A
5B3F: 36 00      LD           (HL),$00
5B41: 3E 01      LD           A,$01
5B43: E0 AC      LDFF00   ($AC),A
5B45: F0 CD      LD           A,($CD)
5B47: E6 F0      AND         $F0
5B49: C6 10      ADD         $10
5B4B: E0 AE      LDFF00   ($AE),A
5B4D: F0 CE      LD           A,($CE)
5B4F: E6 F0      AND         $F0
5B51: C6 08      ADD         $08
5B53: E0 AD      LDFF00   ($AD),A
5B55: F0 CE      LD           A,($CE)
5B57: CB 37      SWAP        1,E
5B59: E6 0F      AND         $0F
5B5B: 5F         LD           E,A
5B5C: F0 CD      LD           A,($CD)
5B5E: E6 F0      AND         $F0
5B60: B3         OR           E
5B61: EA 16 D4   LD           ($D416),A
5B64: 3E 02      LD           A,$02
5B66: E0 F2      LDFF00   ($F2),A
5B68: C9         RET
5B69: 21 11 D7   LD           HL,$D711
5B6C: 19         ADD         HL,DE
5B6D: 36 E8      LD           (HL),$E8
5B6F: CD 39 28   CALL       $2839
5B72: 21 01 D6   LD           HL,$D601
5B75: FA 00 D6   LD           A,($D600)
5B78: 5F         LD           E,A
5B79: C6 0A      ADD         $0A
5B7B: EA 00 D6   LD           ($D600),A
5B7E: 16 00      LD           D,$00
5B80: 19         ADD         HL,DE
5B81: F0 CF      LD           A,($CF)
5B83: 22         LD           (HLI),A
5B84: F0 D0      LD           A,($D0)
5B86: 22         LD           (HLI),A
5B87: 3E 81      LD           A,$81
5B89: 22         LD           (HLI),A
5B8A: 3E 68      LD           A,$68
5B8C: 22         LD           (HLI),A
5B8D: 3E 78      LD           A,$78
5B8F: 22         LD           (HLI),A
5B90: F0 CF      LD           A,($CF)
5B92: 22         LD           (HLI),A
5B93: F0 D0      LD           A,($D0)
5B95: 3C         INC         A
5B96: 22         LD           (HLI),A
5B97: 3E 81      LD           A,$81
5B99: 22         LD           (HLI),A
5B9A: 3E 69      LD           A,$69
5B9C: 22         LD           (HLI),A
5B9D: 3E 79      LD           A,$79
5B9F: 22         LD           (HLI),A
5BA0: 36 00      LD           (HL),$00
5BA2: C9         RET
5BA3: FF         RST         0X38
5BA4: FF         RST         0X38
5BA5: FF         RST         0X38
5BA6: FF         RST         0X38
5BA7: FF         RST         0X38
5BA8: FF         RST         0X38
5BA9: FF         RST         0X38
5BAA: FF         RST         0X38
5BAB: FF         RST         0X38
5BAC: FF         RST         0X38
5BAD: FF         RST         0X38
5BAE: FF         RST         0X38
5BAF: FF         RST         0X38
5BB0: FF         RST         0X38
5BB1: FF         RST         0X38
5BB2: FF         RST         0X38
5BB3: FF         RST         0X38
5BB4: FF         RST         0X38
5BB5: FF         RST         0X38
5BB6: FF         RST         0X38
5BB7: FF         RST         0X38
5BB8: FF         RST         0X38
5BB9: FF         RST         0X38
5BBA: FF         RST         0X38
5BBB: FF         RST         0X38
5BBC: FF         RST         0X38
5BBD: FF         RST         0X38
5BBE: FF         RST         0X38
5BBF: FF         RST         0X38
5BC0: FF         RST         0X38
5BC1: FF         RST         0X38
5BC2: FF         RST         0X38
5BC3: FF         RST         0X38
5BC4: FF         RST         0X38
5BC5: FF         RST         0X38
5BC6: FF         RST         0X38
5BC7: FF         RST         0X38
5BC8: FF         RST         0X38
5BC9: FF         RST         0X38
5BCA: FF         RST         0X38
5BCB: FF         RST         0X38
5BCC: FF         RST         0X38
5BCD: FF         RST         0X38
5BCE: FF         RST         0X38
5BCF: FF         RST         0X38
5BD0: FF         RST         0X38
5BD1: FF         RST         0X38
5BD2: FF         RST         0X38
5BD3: FF         RST         0X38
5BD4: FF         RST         0X38
5BD5: FF         RST         0X38
5BD6: FF         RST         0X38
5BD7: FF         RST         0X38
5BD8: FF         RST         0X38
5BD9: FF         RST         0X38
5BDA: FF         RST         0X38
5BDB: FF         RST         0X38
5BDC: FF         RST         0X38
5BDD: FF         RST         0X38
5BDE: FF         RST         0X38
5BDF: FF         RST         0X38
5BE0: FF         RST         0X38
5BE1: FF         RST         0X38
5BE2: FF         RST         0X38
5BE3: FF         RST         0X38
5BE4: FF         RST         0X38
5BE5: FF         RST         0X38
5BE6: FF         RST         0X38
5BE7: FF         RST         0X38
5BE8: FF         RST         0X38
5BE9: FF         RST         0X38
5BEA: FF         RST         0X38
5BEB: FF         RST         0X38
5BEC: FF         RST         0X38
5BED: FF         RST         0X38
5BEE: FF         RST         0X38
5BEF: FF         RST         0X38
5BF0: FF         RST         0X38
5BF1: FF         RST         0X38
5BF2: FF         RST         0X38
5BF3: FF         RST         0X38
5BF4: FF         RST         0X38
5BF5: FF         RST         0X38
5BF6: FF         RST         0X38
5BF7: FF         RST         0X38
5BF8: FF         RST         0X38
5BF9: FF         RST         0X38
5BFA: FF         RST         0X38
5BFB: FF         RST         0X38
5BFC: FF         RST         0X38
5BFD: FF         RST         0X38
5BFE: FF         RST         0X38
5BFF: FF         RST         0X38
5C00: 57         LD           D,A
5C01: 68         LD           L,B
5C02: 6F         LD           L,A
5C03: 61         LD           H,C
5C04: 2C         INC         L
5C05: 20 62      JR           NZ,$5C69
5C07: 6F         LD           L,A
5C08: 79         LD           A,C
5C09: 21 20 57   LD           HL,$5720
5C0C: 68         LD           L,B
5C0D: 65         LD           H,L
5C0E: 72         LD           (HL),D
5C0F: 65         LD           H,L
5C10: 79         LD           A,C
5C11: 61         LD           H,C
5C12: 20 6F      JR           NZ,$5C83
5C14: 66         LD           H,(HL)
5C15: 66         LD           H,(HL)
5C16: 20 74      JR           NZ,$5C8C
5C18: 6F         LD           L,A
5C19: 20 69      JR           NZ,$5C84
5C1B: 6E         LD           L,(HL)
5C1C: 20 20      JR           NZ,$5C3E
5C1E: 20 20      JR           NZ,$5C40
5C20: 73         LD           (HL),E
5C21: 75         LD           (HL),L
5C22: 63         LD           H,E
5C23: 68         LD           L,B
5C24: 20 61      JR           NZ,$5C87
5C26: 20 68      JR           NZ,$5C90
5C28: 75         LD           (HL),L
5C29: 72         LD           (HL),D
5C2A: 72         LD           (HL),D
5C2B: 79         LD           A,C
5C2C: 3F         CCF
5C2D: 20 20      JR           NZ,$5C4F
5C2F: 20 53      JR           NZ,$5C84
5C31: 65         LD           H,L
5C32: 74         LD           (HL),H
5C33: 20 61      JR           NZ,$5C96
5C35: 20 73      JR           NZ,$5CAA
5C37: 70         LD           (HL),B
5C38: 65         LD           H,L
5C39: 6C         LD           L,H
5C3A: 6C         LD           L,H
5C3B: 2C         INC         L
5C3C: 20 49      JR           NZ,$5C87
5C3E: 20 20      JR           NZ,$5C60
5C40: 67         LD           H,A
5C41: 6F         LD           L,A
5C42: 74         LD           (HL),H
5C43: 20 73      JR           NZ,$5CB8
5C45: 6F         LD           L,A
5C46: 6D         LD           L,L
5C47: 65         LD           H,L
5C48: 74         LD           (HL),H
5C49: 68         LD           L,B
5C4A: 69         LD           L,C
5C4B: 6E         LD           L,(HL)
5C4C: 5E         LD           E,(HL)
5C4D: 20 74      JR           NZ,$5CC3
5C4F: 61         LD           H,C
5C50: 74         LD           (HL),H
5C51: 65         LD           H,L
5C52: 6C         LD           L,H
5C53: 6C         LD           L,H
5C54: 20 79      JR           NZ,$5CCF
5C56: 61         LD           H,C
5C57: 21 FF 57   LD           HL,$57FF
5C5A: 68         LD           L,B
5C5B: 61         LD           H,C
5C5C: 74         LD           (HL),H
5C5D: 20 61      JR           NZ,$5CC0
5C5F: 20 72      JR           NZ,$5CD3
5C61: 65         LD           H,L
5C62: 6C         LD           L,H
5C63: 69         LD           L,C
5C64: 65         LD           H,L
5C65: 66         LD           H,(HL)
5C66: 21 20 49   LD           HL,$4920
5C69: 74         LD           (HL),H
5C6A: 68         LD           L,B
5C6B: 6F         LD           L,A
5C6C: 75         LD           (HL),L
5C6D: 67         LD           H,A
5C6E: 68         LD           L,B
5C6F: 74         LD           (HL),H
5C70: 20 79      JR           NZ,$5CEB
5C72: 6F         LD           L,A
5C73: 75         LD           (HL),L
5C74: 5E         LD           E,(HL)
5C75: 64         LD           H,H
5C76: 20 20      JR           NZ,$5C98
5C78: 20 6E      JR           NZ,$5CE8
5C7A: 65         LD           H,L
5C7B: 76         HALT
5C7C: 65         LD           H,L
5C7D: 72         LD           (HL),D
5C7E: 20 77      JR           NZ,$5CF7
5C80: 61         LD           H,C
5C81: 6B         LD           L,E
5C82: 65         LD           H,L
5C83: 20 75      JR           NZ,$5CFA
5C85: 70         LD           (HL),B
5C86: 21 20 20   LD           HL,$2020
5C89: 59         LD           E,C
5C8A: 6F         LD           L,A
5C8B: 75         LD           (HL),L
5C8C: 20 77      JR           NZ,$5D05
5C8E: 65         LD           H,L
5C8F: 72         LD           (HL),D
5C90: 65         LD           H,L
5C91: 20 74      JR           NZ,$5D07
5C93: 6F         LD           L,A
5C94: 73         LD           (HL),E
5C95: 73         LD           (HL),E
5C96: 69         LD           L,C
5C97: 6E         LD           L,(HL)
5C98: 67         LD           H,A
5C99: 61         LD           H,C
5C9A: 6E         LD           L,(HL)
5C9B: 64         LD           H,H
5C9C: 20 74      JR           NZ,$5D12
5C9E: 75         LD           (HL),L
5C9F: 72         LD           (HL),D
5CA0: 6E         LD           L,(HL)
5CA1: 69         LD           L,C
5CA2: 6E         LD           L,(HL)
5CA3: 67         LD           H,A
5CA4: 2E 2E      LD           L,$2E
5CA6: 2E 20      LD           L,$20
5CA8: 20 57      JR           NZ,$5D01
5CAA: 68         LD           L,B
5CAB: 61         LD           H,C
5CAC: 74         LD           (HL),H
5CAD: 3F         CCF
5CAE: 20 20      JR           NZ,$5CD0
5CB0: 5A         LD           E,D
5CB1: 65         LD           H,L
5CB2: 6C         LD           L,H
5CB3: 64         LD           H,H
5CB4: 61         LD           H,C
5CB5: 3F         CCF
5CB6: 20 20      JR           NZ,$5CD8
5CB8: 20 4E      JR           NZ,$5D08
5CBA: 6F         LD           L,A
5CBB: 2C         INC         L
5CBC: 20 6D      JR           NZ,$5D2B
5CBE: 79         LD           A,C
5CBF: 20 6E      JR           NZ,$5D2F
5CC1: 61         LD           H,C
5CC2: 6D         LD           L,L
5CC3: 65         LD           H,L
5CC4: 5E         LD           E,(HL)
5CC5: 73         LD           (HL),E
5CC6: 20 20      JR           NZ,$5CE8
5CC8: 20 4D      JR           NZ,$5D17
5CCA: 61         LD           H,C
5CCB: 72         LD           (HL),D
5CCC: 69         LD           L,C
5CCD: 6E         LD           L,(HL)
5CCE: 21 20 20   LD           HL,$2020
5CD1: 59         LD           E,C
5CD2: 6F         LD           L,A
5CD3: 75         LD           (HL),L
5CD4: 20 6D      JR           NZ,$5D43
5CD6: 75         LD           (HL),L
5CD7: 73         LD           (HL),E
5CD8: 74         LD           (HL),H
5CD9: 73         LD           (HL),E
5CDA: 74         LD           (HL),H
5CDB: 69         LD           L,C
5CDC: 6C         LD           L,H
5CDD: 6C         LD           L,H
5CDE: 20 62      JR           NZ,$5D42
5CE0: 65         LD           H,L
5CE1: 20 66      JR           NZ,$5D49
5CE3: 65         LD           H,L
5CE4: 65         LD           H,L
5CE5: 6C         LD           L,H
5CE6: 69         LD           L,C
5CE7: 6E         LD           L,(HL)
5CE8: 67         LD           H,A
5CE9: 61         LD           H,C
5CEA: 20 6C      JR           NZ,$5D58
5CEC: 69         LD           L,C
5CED: 74         LD           (HL),H
5CEE: 74         LD           (HL),H
5CEF: 6C         LD           L,H
5CF0: 65         LD           H,L
5CF1: 20 77      JR           NZ,$5D6A
5CF3: 6F         LD           L,A
5CF4: 6F         LD           L,A
5CF5: 7A         LD           A,D
5CF6: 79         LD           A,C
5CF7: 2E 20      LD           L,$20
5CF9: 59         LD           E,C
5CFA: 6F         LD           L,A
5CFB: 75         LD           (HL),L
5CFC: 20 61      JR           NZ,$5D5F
5CFE: 72         LD           (HL),D
5CFF: 65         LD           H,L
5D00: 20 6F      JR           NZ,$5D71
5D02: 6E         LD           L,(HL)
5D03: 20 20      JR           NZ,$5D25
5D05: 20 20      JR           NZ,$5D27
5D07: 20 20      JR           NZ,$5D29
5D09: 4B         LD           C,E
5D0A: 6F         LD           L,A
5D0B: 68         LD           L,B
5D0C: 6F         LD           L,A
5D0D: 6C         LD           L,H
5D0E: 69         LD           L,C
5D0F: 6E         LD           L,(HL)
5D10: 74         LD           (HL),H
5D11: 20 49      JR           NZ,$5D5C
5D13: 73         LD           (HL),E
5D14: 6C         LD           L,H
5D15: 61         LD           H,C
5D16: 6E         LD           L,(HL)
5D17: 64         LD           H,H
5D18: 21 FF 46   LD           HL,$46FF
5D1B: 6F         LD           L,A
5D1C: 6C         LD           L,H
5D1D: 6C         LD           L,H
5D1E: 6F         LD           L,A
5D1F: 77         LD           (HL),A
5D20: 20 74      JR           NZ,$5D96
5D22: 68         LD           L,B
5D23: 65         LD           H,L
5D24: 20 6C      JR           NZ,$5D92
5D26: 61         LD           H,C
5D27: 6E         LD           L,(HL)
5D28: 65         LD           H,L
5D29: 20 73      JR           NZ,$5D9E
5D2B: 6F         LD           L,A
5D2C: 75         LD           (HL),L
5D2D: 74         LD           (HL),H
5D2E: 68         LD           L,B
5D2F: 20 74      JR           NZ,$5DA5
5D31: 6F         LD           L,A
5D32: 20 72      JR           NZ,$5DA6
5D34: 65         LD           H,L
5D35: 61         LD           H,C
5D36: 63         LD           H,E
5D37: 68         LD           L,B
5D38: 20 20      JR           NZ,$5D5A
5D3A: 74         LD           (HL),H
5D3B: 68         LD           L,B
5D3C: 65         LD           H,L
5D3D: 20 62      JR           NZ,$5DA1
5D3F: 65         LD           H,L
5D40: 61         LD           H,C
5D41: 63         LD           H,E
5D42: 68         LD           L,B
5D43: 20 77      JR           NZ,$5DBC
5D45: 68         LD           L,B
5D46: 65         LD           H,L
5D47: 72         LD           (HL),D
5D48: 65         LD           H,L
5D49: 20 49      JR           NZ,$5D94
5D4B: 20 66      JR           NZ,$5DB3
5D4D: 6F         LD           L,A
5D4E: 75         LD           (HL),L
5D4F: 6E         LD           L,(HL)
5D50: 64         LD           H,H
5D51: 20 79      JR           NZ,$5DCC
5D53: 6F         LD           L,A
5D54: 75         LD           (HL),L
5D55: 2E 20      LD           L,$20
5D57: 20 20      JR           NZ,$5D79
5D59: 20 53      JR           NZ,$5DAE
5D5B: 69         LD           L,C
5D5C: 6E         LD           L,(HL)
5D5D: 63         LD           H,E
5D5E: 65         LD           H,L
5D5F: 20 79      JR           NZ,$5DDA
5D61: 6F         LD           L,A
5D62: 75         LD           (HL),L
5D63: 20 77      JR           NZ,$5DDC
5D65: 61         LD           H,C
5D66: 73         LD           (HL),E
5D67: 68         LD           L,B
5D68: 65         LD           H,L
5D69: 64         LD           H,H
5D6A: 61         LD           H,C
5D6B: 73         LD           (HL),E
5D6C: 68         LD           L,B
5D6D: 6F         LD           L,A
5D6E: 72         LD           (HL),D
5D6F: 65         LD           H,L
5D70: 2C         INC         L
5D71: 20 6C      JR           NZ,$5DDF
5D73: 6F         LD           L,A
5D74: 74         LD           (HL),H
5D75: 73         LD           (HL),E
5D76: 20 6F      JR           NZ,$5DE7
5D78: 66         LD           H,(HL)
5D79: 20 6E      JR           NZ,$5DE9
5D7B: 61         LD           H,C
5D7C: 73         LD           (HL),E
5D7D: 74         LD           (HL),H
5D7E: 79         LD           A,C
5D7F: 20 6D      JR           NZ,$5DEE
5D81: 6F         LD           L,A
5D82: 6E         LD           L,(HL)
5D83: 73         LD           (HL),E
5D84: 74         LD           (HL),H
5D85: 65         LD           H,L
5D86: 72         LD           (HL),D
5D87: 73         LD           (HL),E
5D88: 20 20      JR           NZ,$5DAA
5D8A: 68         LD           L,B
5D8B: 61         LD           H,C
5D8C: 76         HALT
5D8D: 65         LD           H,L
5D8E: 20 62      JR           NZ,$5DF2
5D90: 65         LD           H,L
5D91: 65         LD           H,L
5D92: 6E         LD           L,(HL)
5D93: 20 69      JR           NZ,$5DFE
5D95: 6E         LD           L,(HL)
5D96: 20 74      JR           NZ,$5E0C
5D98: 68         LD           L,B
5D99: 65         LD           H,L
5D9A: 61         LD           H,C
5D9B: 72         LD           (HL),D
5D9C: 65         LD           H,L
5D9D: 61         LD           H,C
5D9E: 2C         INC         L
5D9F: 20 73      JR           NZ,$5E14
5DA1: 6F         LD           L,A
5DA2: 20 62      JR           NZ,$5E06
5DA4: 65         LD           H,L
5DA5: 20 20      JR           NZ,$5DC7
5DA7: 20 20      JR           NZ,$5DC9
5DA9: 20 63      JR           NZ,$5E0E
5DAB: 61         LD           H,C
5DAC: 72         LD           (HL),D
5DAD: 65         LD           H,L
5DAE: 66         LD           H,(HL)
5DAF: 75         LD           (HL),L
5DB0: 6C         LD           L,H
5DB1: 2C         INC         L
5DB2: 20 6F      JR           NZ,$5E23
5DB4: 6B         LD           L,E
5DB5: 61         LD           H,C
5DB6: 79         LD           A,C
5DB7: 3F         CCF
5DB8: FF         RST         0X38
5DB9: 48         LD           C,B
5DBA: 69         LD           L,C
5DBB: 21 20 20   LD           HL,$2020
5DBE: 54         LD           D,H
5DBF: 61         LD           H,C
5DC0: 72         LD           (HL),D
5DC1: 69         LD           L,C
5DC2: 6E         LD           L,(HL)
5DC3: 20 77      JR           NZ,$5E3C
5DC5: 65         LD           H,L
5DC6: 6E         LD           L,(HL)
5DC7: 74         LD           (HL),H
5DC8: 20 74      JR           NZ,$5E3E
5DCA: 6F         LD           L,A
5DCB: 20 74      JR           NZ,$5E41
5DCD: 68         LD           L,B
5DCE: 65         LD           H,L
5DCF: 20 66      JR           NZ,$5E37
5DD1: 6F         LD           L,A
5DD2: 72         LD           (HL),D
5DD3: 65         LD           H,L
5DD4: 73         LD           (HL),E
5DD5: 74         LD           (HL),H
5DD6: 20 74      JR           NZ,$5E4C
5DD8: 6F         LD           L,A
5DD9: 6C         LD           L,H
5DDA: 6F         LD           L,A
5DDB: 6F         LD           L,A
5DDC: 6B         LD           L,E
5DDD: 20 66      JR           NZ,$5E45
5DDF: 6F         LD           L,A
5DE0: 72         LD           (HL),D
5DE1: 20 74      JR           NZ,$5E57
5DE3: 6F         LD           L,A
5DE4: 61         LD           H,C
5DE5: 64         LD           H,H
5DE6: 2D         DEC         L
5DE7: 20 20      JR           NZ,$5E09
5DE9: 73         LD           (HL),E
5DEA: 74         LD           (HL),H
5DEB: 6F         LD           L,A
5DEC: 6F         LD           L,A
5DED: 6C         LD           L,H
5DEE: 73         LD           (HL),E
5DEF: 2C         INC         L
5DF0: 20 62      JR           NZ,$5E54
5DF2: 75         LD           (HL),L
5DF3: 74         LD           (HL),H
5DF4: 20 49      JR           NZ,$5E3F
5DF6: 5E         LD           E,(HL)
5DF7: 64         LD           H,H
5DF8: 20 72      JR           NZ,$5E6C
5DFA: 61         LD           H,C
5DFB: 74         LD           (HL),H
5DFC: 68         LD           L,B
5DFD: 65         LD           H,L
5DFE: 72         LD           (HL),D
5DFF: 20 73      JR           NZ,$5E74
5E01: 69         LD           L,C
5E02: 6E         LD           L,(HL)
5E03: 67         LD           H,A
5E04: 2E 20      LD           L,$20
5E06: 20 20      JR           NZ,$5E28
5E08: 20 4C      JR           NZ,$5E56
5E0A: 69         LD           L,C
5E0B: 73         LD           (HL),E
5E0C: 74         LD           (HL),H
5E0D: 65         LD           H,L
5E0E: 6E         LD           L,(HL)
5E0F: 20 74      JR           NZ,$5E85
5E11: 6F         LD           L,A
5E12: 20 74      JR           NZ,$5E88
5E14: 68         LD           L,B
5E15: 69         LD           L,C
5E16: 73         LD           (HL),E
5E17: 2C         INC         L
5E18: 20 69      JR           NZ,$5E83
5E1A: 74         LD           (HL),H
5E1B: 5E         LD           E,(HL)
5E1C: 73         LD           (HL),E
5E1D: 20 63      JR           NZ,$5E82
5E1F: 61         LD           H,C
5E20: 6C         LD           L,H
5E21: 6C         LD           L,H
5E22: 65         LD           H,L
5E23: 64         LD           H,H
5E24: 20 74      JR           NZ,$5E9A
5E26: 68         LD           L,B
5E27: 65         LD           H,L
5E28: 20 5E      JR           NZ,$5E88
5E2A: 42         LD           B,D
5E2B: 61         LD           H,C
5E2C: 6C         LD           L,H
5E2D: 6C         LD           L,H
5E2E: 61         LD           H,C
5E2F: 64         LD           H,H
5E30: 20 6F      JR           NZ,$5EA1
5E32: 66         LD           H,(HL)
5E33: 20 74      JR           NZ,$5EA9
5E35: 68         LD           L,B
5E36: 65         LD           H,L
5E37: 20 20      JR           NZ,$5E59
5E39: 57         LD           D,A
5E3A: 69         LD           L,C
5E3B: 6E         LD           L,(HL)
5E3C: 64         LD           H,H
5E3D: 20 46      JR           NZ,$5E85
5E3F: 69         LD           L,C
5E40: 73         LD           (HL),E
5E41: 68         LD           L,B
5E42: 2E 5E      LD           L,$5E
5E44: FF         RST         0X38
5E45: 48         LD           C,B
5E46: 65         LD           H,L
5E47: 79         LD           A,C
5E48: 21 20 20   LD           HL,$2020
5E4B: 54         LD           D,H
5E4C: 68         LD           L,B
5E4D: 61         LD           H,C
5E4E: 74         LD           (HL),H
5E4F: 5E         LD           E,(HL)
5E50: 73         LD           (HL),E
5E51: 20 61      JR           NZ,$5EB4
5E53: 20 20      JR           NZ,$5E75
5E55: 6E         LD           L,(HL)
5E56: 69         LD           L,C
5E57: 63         LD           H,E
5E58: 65         LD           H,L
5E59: 20 4F      JR           NZ,$5EAA
5E5B: 63         LD           H,E
5E5C: 61         LD           H,C
5E5D: 72         LD           (HL),D
5E5E: 69         LD           L,C
5E5F: 6E         LD           L,(HL)
5E60: 61         LD           H,C
5E61: 20 79      JR           NZ,$5EDC
5E63: 6F         LD           L,A
5E64: 75         LD           (HL),L
5E65: 68         LD           L,B
5E66: 61         LD           H,C
5E67: 76         HALT
5E68: 65         LD           H,L
5E69: 20 74      JR           NZ,$5EDF
5E6B: 68         LD           L,B
5E6C: 65         LD           H,L
5E6D: 72         LD           (HL),D
5E6E: 65         LD           H,L
5E6F: 21 20 57   LD           HL,$5720
5E72: 69         LD           L,C
5E73: 6C         LD           L,H
5E74: 6C         LD           L,H
5E75: 79         LD           A,C
5E76: 6F         LD           L,A
5E77: 75         LD           (HL),L
5E78: 20 61      JR           NZ,$5EDB
5E7A: 63         LD           H,E
5E7B: 63         LD           H,E
5E7C: 6F         LD           L,A
5E7D: 6D         LD           L,L
5E7E: 70         LD           (HL),B
5E7F: 61         LD           H,C
5E80: 6E         LD           L,(HL)
5E81: 79         LD           A,C
5E82: 20 20      JR           NZ,$5EA4
5E84: 20 6D      JR           NZ,$5EF3
5E86: 65         LD           H,L
5E87: 20 61      JR           NZ,$5EEA
5E89: 73         LD           (HL),E
5E8A: 20 49      JR           NZ,$5ED5
5E8C: 20 73      JR           NZ,$5F01
5E8E: 69         LD           L,C
5E8F: 6E         LD           L,(HL)
5E90: 67         LD           H,A
5E91: 3F         CCF
5E92: FF         RST         0X38
5E93: 49         LD           C,C
5E94: 20 6A      JR           NZ,$5F00
5E96: 75         LD           (HL),L
5E97: 73         LD           (HL),E
5E98: 74         LD           (HL),H
5E99: 20 6C      JR           NZ,$5F07
5E9B: 6F         LD           L,A
5E9C: 76         HALT
5E9D: 65         LD           H,L
5E9E: 20 74      JR           NZ,$5F14
5EA0: 6F         LD           L,A
5EA1: 20 20      JR           NZ,$5EC3
5EA3: 73         LD           (HL),E
5EA4: 69         LD           L,C
5EA5: 6E         LD           L,(HL)
5EA6: 67         LD           H,A
5EA7: 2D         DEC         L
5EA8: 2D         DEC         L
5EA9: 20 77      JR           NZ,$5F22
5EAB: 68         LD           L,B
5EAC: 61         LD           H,C
5EAD: 74         LD           (HL),H
5EAE: 20 63      JR           NZ,$5F13
5EB0: 61         LD           H,C
5EB1: 6E         LD           L,(HL)
5EB2: 20 49      JR           NZ,$5EFD
5EB4: 20 73      JR           NZ,$5F29
5EB6: 61         LD           H,C
5EB7: 79         LD           A,C
5EB8: 3F         CCF
5EB9: 20 20      JR           NZ,$5EDB
5EBB: 57         LD           D,A
5EBC: 68         LD           L,B
5EBD: 61         LD           H,C
5EBE: 74         LD           (HL),H
5EBF: 20 64      JR           NZ,$5F25
5EC1: 6F         LD           L,A
5EC2: 20 79      JR           NZ,$5F3D
5EC4: 6F         LD           L,A
5EC5: 75         LD           (HL),L
5EC6: 20 6C      JR           NZ,$5F34
5EC8: 69         LD           L,C
5EC9: 6B         LD           L,E
5ECA: 65         LD           H,L
5ECB: 20 74      JR           NZ,$5F41
5ECD: 6F         LD           L,A
5ECE: 20 64      JR           NZ,$5F34
5ED0: 6F         LD           L,A
5ED1: 2C         INC         L
5ED2: 20 23      JR           NZ,$5EF7
5ED4: 23         INC         HL
5ED5: 23         INC         HL
5ED6: 23         INC         HL
5ED7: 23         INC         HL
5ED8: 3F         CCF
5ED9: FF         RST         0X38
5EDA: 23         INC         HL
5EDB: 23         INC         HL
5EDC: 23         INC         HL
5EDD: 23         INC         HL
5EDE: 23         INC         HL
5EDF: 2C         INC         L
5EE0: 20 54      JR           NZ,$5F36
5EE2: 61         LD           H,C
5EE3: 72         LD           (HL),D
5EE4: 69         LD           L,C
5EE5: 6E         LD           L,(HL)
5EE6: 5E         LD           E,(HL)
5EE7: 73         LD           (HL),E
5EE8: 20 20      JR           NZ,$5F0A
5EEA: 74         LD           (HL),H
5EEB: 61         LD           H,C
5EEC: 6B         LD           L,E
5EED: 69         LD           L,C
5EEE: 6E         LD           L,(HL)
5EEF: 67         LD           H,A
5EF0: 20 61      JR           NZ,$5F53
5EF2: 20 6E      JR           NZ,$5F62
5EF4: 61         LD           H,C
5EF5: 70         LD           (HL),B
5EF6: 20 61      JR           NZ,$5F59
5EF8: 74         LD           (HL),H
5EF9: 20 68      JR           NZ,$5F63
5EFB: 6F         LD           L,A
5EFC: 6D         LD           L,L
5EFD: 65         LD           H,L
5EFE: 2E 20      LD           L,$20
5F00: 20 49      JR           NZ,$5F4B
5F02: 20 64      JR           NZ,$5F68
5F04: 6F         LD           L,A
5F05: 6E         LD           L,(HL)
5F06: 5E         LD           E,(HL)
5F07: 74         LD           (HL),H
5F08: 20 20      JR           NZ,$5F2A
5F0A: 6B         LD           L,E
5F0B: 6E         LD           L,(HL)
5F0C: 6F         LD           L,A
5F0D: 77         LD           (HL),A
5F0E: 20 68      JR           NZ,$5F78
5F10: 6F         LD           L,A
5F11: 77         LD           (HL),A
5F12: 20 68      JR           NZ,$5F7C
5F14: 65         LD           H,L
5F15: 20 63      JR           NZ,$5F7A
5F17: 61         LD           H,C
5F18: 6E         LD           L,(HL)
5F19: 20 73      JR           NZ,$5F8E
5F1B: 6C         LD           L,H
5F1C: 65         LD           H,L
5F1D: 65         LD           H,L
5F1E: 70         LD           (HL),B
5F1F: 20 6F      JR           NZ,$5F90
5F21: 6E         LD           L,(HL)
5F22: 20 73      JR           NZ,$5F97
5F24: 75         LD           (HL),L
5F25: 63         LD           H,E
5F26: 68         LD           L,B
5F27: 20 61      JR           NZ,$5F8A
5F29: 20 6E      JR           NZ,$5F99
5F2B: 69         LD           L,C
5F2C: 63         LD           H,E
5F2D: 65         LD           H,L
5F2E: 20 64      JR           NZ,$5F94
5F30: 61         LD           H,C
5F31: 79         LD           A,C
5F32: 21 20 20   LD           HL,$2020
5F35: 49         LD           C,C
5F36: 74         LD           (HL),H
5F37: 20 20      JR           NZ,$5F59
5F39: 20 6D      JR           NZ,$5FA8
5F3B: 61         LD           H,C
5F3C: 6B         LD           L,E
5F3D: 65         LD           H,L
5F3E: 73         LD           (HL),E
5F3F: 20 6D      JR           NZ,$5FAE
5F41: 65         LD           H,L
5F42: 20 77      JR           NZ,$5FBB
5F44: 61         LD           H,C
5F45: 6E         LD           L,(HL)
5F46: 74         LD           (HL),H
5F47: 20 74      JR           NZ,$5FBD
5F49: 6F         LD           L,A
5F4A: 73         LD           (HL),E
5F4B: 69         LD           L,C
5F4C: 6E         LD           L,(HL)
5F4D: 67         LD           H,A
5F4E: 20 61      JR           NZ,$5FB1
5F50: 20 73      JR           NZ,$5FC5
5F52: 6F         LD           L,A
5F53: 6E         LD           L,(HL)
5F54: 67         LD           H,A
5F55: 2E 2E      LD           L,$2E
5F57: 2E 20      LD           L,$20
5F59: 20 59      JR           NZ,$5FB4
5F5B: 65         LD           H,L
5F5C: 73         LD           (HL),E
5F5D: 2C         INC         L
5F5E: 20 74      JR           NZ,$5FD4
5F60: 68         LD           L,B
5F61: 65         LD           H,L
5F62: 20 73      JR           NZ,$5FD7
5F64: 6F         LD           L,A
5F65: 6E         LD           L,(HL)
5F66: 67         LD           H,A
5F67: 20 69      JR           NZ,$5FD2
5F69: 73         LD           (HL),E
5F6A: 5E         LD           E,(HL)
5F6B: 42         LD           B,D
5F6C: 61         LD           H,C
5F6D: 6C         LD           L,H
5F6E: 6C         LD           L,H
5F6F: 61         LD           H,C
5F70: 64         LD           H,H
5F71: 20 6F      JR           NZ,$5FE2
5F73: 66         LD           H,(HL)
5F74: 20 74      JR           NZ,$5FEA
5F76: 68         LD           L,B
5F77: 65         LD           H,L
5F78: 20 20      JR           NZ,$5F9A
5F7A: 57         LD           D,A
5F7B: 69         LD           L,C
5F7C: 6E         LD           L,(HL)
5F7D: 64         LD           H,H
5F7E: 20 46      JR           NZ,$5FC6
5F80: 69         LD           L,C
5F81: 73         LD           (HL),E
5F82: 68         LD           L,B
5F83: 21 5E FF   LD           HL,$FF5E
5F86: 45         LD           B,L
5F87: 68         LD           L,B
5F88: 3F         CCF
5F89: 20 49      JR           NZ,$5FD4
5F8B: 74         LD           (HL),H
5F8C: 5E         LD           E,(HL)
5F8D: 73         LD           (HL),E
5F8E: 20 6C      JR           NZ,$5FFC
5F90: 6F         LD           L,A
5F91: 63         LD           H,E
5F92: 6B         LD           L,E
5F93: 65         LD           H,L
5F94: 64         LD           H,H
5F95: 21 59 6F   LD           HL,$6F59
5F98: 75         LD           (HL),L
5F99: 20 63      JR           NZ,$5FFE
5F9B: 61         LD           H,C
5F9C: 6E         LD           L,(HL)
5F9D: 20 6F      JR           NZ,$600E
5F9F: 70         LD           (HL),B
5FA0: 65         LD           H,L
5FA1: 6E         LD           L,(HL)
5FA2: 20 74      JR           NZ,$6018
5FA4: 68         LD           L,B
5FA5: 65         LD           H,L
5FA6: 64         LD           H,H
5FA7: 6F         LD           L,A
5FA8: 6F         LD           L,A
5FA9: 72         LD           (HL),D
5FAA: 20 77      JR           NZ,$6023
5FAC: 69         LD           L,C
5FAD: 74         LD           (HL),H
5FAE: 68         LD           L,B
5FAF: 20 74      JR           NZ,$6025
5FB1: 68         LD           L,B
5FB2: 65         LD           H,L
5FB3: 20 20      JR           NZ,$5FD5
5FB5: 20 4E      JR           NZ,$6005
5FB7: 69         LD           L,C
5FB8: 67         LD           H,A
5FB9: 68         LD           L,B
5FBA: 74         LD           (HL),H
5FBB: 6D         LD           L,L
5FBC: 61         LD           H,C
5FBD: 72         LD           (HL),D
5FBE: 65         LD           H,L
5FBF: 20 4B      JR           NZ,$600C
5FC1: 65         LD           H,L
5FC2: 79         LD           A,C
5FC3: 2E FF      LD           L,$FF
5FC5: 59         LD           E,C
5FC6: 6F         LD           L,A
5FC7: 75         LD           (HL),L
5FC8: 20 67      JR           NZ,$6031
5FCA: 6F         LD           L,A
5FCB: 74         LD           (HL),H
5FCC: 20 61      JR           NZ,$602F
5FCE: 20 50      JR           NZ,$6020
5FD0: 69         LD           L,C
5FD1: 65         LD           H,L
5FD2: 63         LD           H,E
5FD3: 65         LD           H,L
5FD4: 20 6F      JR           NZ,$6045
5FD6: 66         LD           H,(HL)
5FD7: 20 50      JR           NZ,$6029
5FD9: 6F         LD           L,A
5FDA: 77         LD           (HL),A
5FDB: 65         LD           H,L
5FDC: 72         LD           (HL),D
5FDD: 21 20 20   LD           HL,$2020
5FE0: 59         LD           E,C
5FE1: 6F         LD           L,A
5FE2: 75         LD           (HL),L
5FE3: 20 20      JR           NZ,$6005
5FE5: 63         LD           H,E
5FE6: 61         LD           H,C
5FE7: 6E         LD           L,(HL)
5FE8: 20 66      JR           NZ,$6050
5FEA: 65         LD           H,L
5FEB: 65         LD           H,L
5FEC: 6C         LD           L,H
5FED: 20 74      JR           NZ,$6063
5FEF: 68         LD           L,B
5FF0: 65         LD           H,L
5FF1: 20 20      JR           NZ,$6013
5FF3: 20 20      JR           NZ,$6015
5FF5: 65         LD           H,L
5FF6: 6E         LD           L,(HL)
5FF7: 65         LD           H,L
5FF8: 72         LD           (HL),D
5FF9: 67         LD           H,A
5FFA: 79         LD           A,C
5FFB: 20 66      JR           NZ,$6063
5FFD: 6C         LD           L,H
5FFE: 6F         LD           L,A
5FFF: 77         LD           (HL),A
6000: 69         LD           L,C
6001: 6E         LD           L,(HL)
6002: 67         LD           H,A
6003: 20 20      JR           NZ,$6025
6005: 74         LD           (HL),H
6006: 68         LD           L,B
6007: 72         LD           (HL),D
6008: 6F         LD           L,A
6009: 75         LD           (HL),L
600A: 67         LD           H,A
600B: 68         LD           L,B
600C: 20 79      JR           NZ,$6087
600E: 6F         LD           L,A
600F: 75         LD           (HL),L
6010: 21 FF 41   LD           HL,$41FF
6013: 68         LD           L,B
6014: 68         LD           L,B
6015: 68         LD           L,B
6016: 2E 2E      LD           L,$2E
6018: 2E 20      LD           L,$20
601A: 49         LD           C,C
601B: 74         LD           (HL),H
601C: 20 68      JR           NZ,$6086
601E: 61         LD           H,C
601F: 73         LD           (HL),E
6020: 20 20      JR           NZ,$6042
6022: 74         LD           (HL),H
6023: 68         LD           L,B
6024: 65         LD           H,L
6025: 20 53      JR           NZ,$607A
6027: 6C         LD           L,H
6028: 65         LD           H,L
6029: 65         LD           H,L
602A: 70         LD           (HL),B
602B: 79         LD           A,C
602C: 20 54      JR           NZ,$6082
602E: 6F         LD           L,A
602F: 61         LD           H,C
6030: 64         LD           H,H
6031: 2D         DEC         L
6032: 73         LD           (HL),E
6033: 74         LD           (HL),H
6034: 6F         LD           L,A
6035: 6F         LD           L,A
6036: 6C         LD           L,H
6037: 2C         INC         L
6038: 20 69      JR           NZ,$60A3
603A: 74         LD           (HL),H
603B: 20 64      JR           NZ,$60A1
603D: 6F         LD           L,A
603E: 65         LD           H,L
603F: 73         LD           (HL),E
6040: 21 20 57   LD           HL,$5720
6043: 65         LD           H,L
6044: 5E         LD           E,(HL)
6045: 6C         LD           L,H
6046: 6C         LD           L,H
6047: 20 6D      JR           NZ,$60B6
6049: 69         LD           L,C
604A: 78         LD           A,B
604B: 20 69      JR           NZ,$60B6
604D: 74         LD           (HL),H
604E: 20 75      JR           NZ,$60C5
6050: 70         LD           (HL),B
6051: 20 73      JR           NZ,$60C6
6053: 6F         LD           L,A
6054: 6D         LD           L,L
6055: 65         LD           H,L
6056: 74         LD           (HL),H
6057: 68         LD           L,B
6058: 69         LD           L,C
6059: 6E         LD           L,(HL)
605A: 67         LD           H,A
605B: 20 69      JR           NZ,$60C6
605D: 6E         LD           L,(HL)
605E: 20 61      JR           NZ,$60C1
6060: 20 20      JR           NZ,$6082
6062: 6A         LD           L,D
6063: 69         LD           L,C
6064: 66         LD           H,(HL)
6065: 66         LD           H,(HL)
6066: 79         LD           A,C
6067: 2C         INC         L
6068: 20 77      JR           NZ,$60E1
606A: 65         LD           H,L
606B: 20 77      JR           NZ,$60E4
606D: 69         LD           L,C
606E: 6C         LD           L,H
606F: 6C         LD           L,H
6070: 21 FF 54   LD           HL,$54FF
6073: 68         LD           L,B
6074: 65         LD           H,L
6075: 20 6C      JR           NZ,$60E3
6077: 61         LD           H,C
6078: 73         LD           (HL),E
6079: 74         LD           (HL),H
607A: 20 74      JR           NZ,$60F0
607C: 68         LD           L,B
607D: 69         LD           L,C
607E: 6E         LD           L,(HL)
607F: 67         LD           H,A
6080: 20 49      JR           NZ,$60CB
6082: 6B         LD           L,E
6083: 69         LD           L,C
6084: 6E         LD           L,(HL)
6085: 20 72      JR           NZ,$60F9
6087: 65         LD           H,L
6088: 6D         LD           L,L
6089: 65         LD           H,L
608A: 6D         LD           L,L
608B: 62         LD           H,D
608C: 65         LD           H,L
608D: 72         LD           (HL),D
608E: 20 77      JR           NZ,$6107
6090: 61         LD           H,C
6091: 73         LD           (HL),E
6092: 62         LD           H,D
6093: 69         LD           L,C
6094: 74         LD           (HL),H
6095: 69         LD           L,C
6096: 6E         LD           L,(HL)
6097: 5E         LD           E,(HL)
6098: 20 69      JR           NZ,$6103
609A: 6E         LD           L,(HL)
609B: 74         LD           (HL),H
609C: 6F         LD           L,A
609D: 20 61      JR           NZ,$6100
609F: 20 20      JR           NZ,$60C1
60A1: 20 62      JR           NZ,$6105
60A3: 69         LD           L,C
60A4: 67         LD           H,A
60A5: 20 6A      JR           NZ,$6111
60A7: 75         LD           (HL),L
60A8: 69         LD           L,C
60A9: 63         LD           H,E
60AA: 79         LD           A,C
60AB: 20 74      JR           NZ,$6121
60AD: 6F         LD           L,A
60AE: 61         LD           H,C
60AF: 64         LD           H,H
60B0: 2D         DEC         L
60B1: 20 73      JR           NZ,$6126
60B3: 74         LD           (HL),H
60B4: 6F         LD           L,A
60B5: 6F         LD           L,A
60B6: 6C         LD           L,H
60B7: 2E 2E      LD           L,$2E
60B9: 2E 20      LD           L,$20
60BB: 54         LD           D,H
60BC: 68         LD           L,B
60BD: 65         LD           H,L
60BE: 6E         LD           L,(HL)
60BF: 2C         INC         L
60C0: 20 49      JR           NZ,$610B
60C2: 68         LD           L,B
60C3: 61         LD           H,C
60C4: 64         LD           H,H
60C5: 20 74      JR           NZ,$613B
60C7: 68         LD           L,B
60C8: 65         LD           H,L
60C9: 20 64      JR           NZ,$612F
60CB: 61         LD           H,C
60CC: 72         LD           (HL),D
60CD: 6E         LD           L,(HL)
60CE: 64         LD           H,H
60CF: 65         LD           H,L
60D0: 73         LD           (HL),E
60D1: 74         LD           (HL),H
60D2: 64         LD           H,H
60D3: 72         LD           (HL),D
60D4: 65         LD           H,L
60D5: 61         LD           H,C
60D6: 6D         LD           L,L
60D7: 2E 2E      LD           L,$2E
60D9: 2E 20      LD           L,$20
60DB: 49         LD           C,C
60DC: 20 77      JR           NZ,$6155
60DE: 61         LD           H,C
60DF: 73         LD           (HL),E
60E0: 20 61      JR           NZ,$6143
60E2: 72         LD           (HL),D
60E3: 61         LD           H,C
60E4: 63         LD           H,E
60E5: 63         LD           H,E
60E6: 6F         LD           L,A
60E7: 6F         LD           L,A
60E8: 6E         LD           L,(HL)
60E9: 21 20 20   LD           HL,$2020
60EC: 59         LD           E,C
60ED: 65         LD           H,L
60EE: 61         LD           H,C
60EF: 68         LD           L,B
60F0: 2C         INC         L
60F1: 20 73      JR           NZ,$6166
60F3: 6F         LD           L,A
60F4: 75         LD           (HL),L
60F5: 6E         LD           L,(HL)
60F6: 64         LD           H,H
60F7: 73         LD           (HL),E
60F8: 20 73      JR           NZ,$616D
60FA: 74         LD           (HL),H
60FB: 72         LD           (HL),D
60FC: 61         LD           H,C
60FD: 6E         LD           L,(HL)
60FE: 67         LD           H,A
60FF: 65         LD           H,L
6100: 2C         INC         L
6101: 20 62      JR           NZ,$6165
6103: 75         LD           (HL),L
6104: 74         LD           (HL),H
6105: 20 69      JR           NZ,$6170
6107: 74         LD           (HL),H
6108: 20 73      JR           NZ,$617D
610A: 75         LD           (HL),L
610B: 72         LD           (HL),D
610C: 65         LD           H,L
610D: 20 77      JR           NZ,$6186
610F: 61         LD           H,C
6110: 73         LD           (HL),E
6111: 20 66      JR           NZ,$6179
6113: 75         LD           (HL),L
6114: 6E         LD           L,(HL)
6115: 21 FF 49   LD           HL,$49FF
6118: 5E         LD           E,(HL)
6119: 6D         LD           L,L
611A: 20 61      JR           NZ,$617D
611C: 6C         LD           L,H
611D: 6C         LD           L,H
611E: 20 74      JR           NZ,$6194
6120: 75         LD           (HL),L
6121: 63         LD           H,E
6122: 6B         LD           L,E
6123: 65         LD           H,L
6124: 72         LD           (HL),D
6125: 5E         LD           E,(HL)
6126: 64         LD           H,H
6127: 6F         LD           L,A
6128: 75         LD           (HL),L
6129: 74         LD           (HL),H
612A: 2E 2E      LD           L,$2E
612C: 2E 20      LD           L,$20
612E: 20 49      JR           NZ,$6179
6130: 20 74      JR           NZ,$61A6
6132: 68         LD           L,B
6133: 69         LD           L,C
6134: 6E         LD           L,(HL)
6135: 6B         LD           L,E
6136: 20 49      JR           NZ,$6181
6138: 20 62      JR           NZ,$619C
613A: 65         LD           H,L
613B: 74         LD           (HL),H
613C: 74         LD           (HL),H
613D: 65         LD           H,L
613E: 72         LD           (HL),D
613F: 20 73      JR           NZ,$61B4
6141: 65         LD           H,L
6142: 74         LD           (HL),H
6143: 20 61      JR           NZ,$61A6
6145: 20 20      JR           NZ,$6167
6147: 73         LD           (HL),E
6148: 70         LD           (HL),B
6149: 65         LD           H,L
614A: 6C         LD           L,H
614B: 6C         LD           L,H
614C: 20 62      JR           NZ,$61B0
614E: 65         LD           H,L
614F: 66         LD           H,(HL)
6150: 6F         LD           L,A
6151: 72         LD           (HL),D
6152: 65         LD           H,L
6153: 20 49      JR           NZ,$619E
6155: 20 20      JR           NZ,$6177
6157: 68         LD           L,B
6158: 65         LD           H,L
6159: 61         LD           H,C
615A: 64         LD           H,H
615B: 20 68      JR           NZ,$61C5
615D: 6F         LD           L,A
615E: 6D         LD           L,L
615F: 65         LD           H,L
6160: 2E 2E      LD           L,$2E
6162: 2E FF      LD           L,$FF
6164: 44         LD           B,H
6165: 6F         LD           L,A
6166: 75         LD           (HL),L
6167: 62         LD           H,D
6168: 6C         LD           L,H
6169: 65         LD           H,L
616A: 20 64      JR           NZ,$61D0
616C: 6F         LD           L,A
616D: 75         LD           (HL),L
616E: 62         LD           H,D
616F: 6C         LD           L,H
6170: 65         LD           H,L
6171: 2C         INC         L
6172: 20 20      JR           NZ,$6194
6174: 74         LD           (HL),H
6175: 6F         LD           L,A
6176: 69         LD           L,C
6177: 6C         LD           L,H
6178: 20 61      JR           NZ,$61DB
617A: 6E         LD           L,(HL)
617B: 64         LD           H,H
617C: 20 74      JR           NZ,$61F2
617E: 72         LD           (HL),D
617F: 6F         LD           L,A
6180: 75         LD           (HL),L
6181: 62         LD           H,D
6182: 6C         LD           L,H
6183: 65         LD           H,L
6184: 61         LD           H,C
6185: 20 74      JR           NZ,$61FB
6187: 6F         LD           L,A
6188: 61         LD           H,C
6189: 64         LD           H,H
618A: 73         LD           (HL),E
618B: 74         LD           (HL),H
618C: 6F         LD           L,A
618D: 6F         LD           L,A
618E: 6C         LD           L,H
618F: 20 6D      JR           NZ,$61FE
6191: 69         LD           L,C
6192: 78         LD           A,B
6193: 20 6D      JR           NZ,$6202
6195: 61         LD           H,C
6196: 6B         LD           L,E
6197: 65         LD           H,L
6198: 73         LD           (HL),E
6199: 20 70      JR           NZ,$620B
619B: 6F         LD           L,A
619C: 77         LD           (HL),A
619D: 64         LD           H,H
619E: 65         LD           H,L
619F: 72         LD           (HL),D
61A0: 20 66      JR           NZ,$6208
61A2: 6F         LD           L,A
61A3: 72         LD           (HL),D
61A4: 74         LD           (HL),H
61A5: 72         LD           (HL),D
61A6: 69         LD           L,C
61A7: 63         LD           H,E
61A8: 6B         LD           L,E
61A9: 73         LD           (HL),E
61AA: 21 FF 41   LD           HL,$41FF
61AD: 73         LD           (HL),E
61AE: 20 61      JR           NZ,$6211
61B0: 20 72      JR           NZ,$6224
61B2: 61         LD           H,C
61B3: 63         LD           H,E
61B4: 63         LD           H,E
61B5: 6F         LD           L,A
61B6: 6F         LD           L,A
61B7: 6E         LD           L,(HL)
61B8: 2C         INC         L
61B9: 20 6D      JR           NZ,$6228
61BB: 79         LD           A,C
61BC: 6E         LD           L,(HL)
61BD: 6F         LD           L,A
61BE: 73         LD           (HL),E
61BF: 65         LD           H,L
61C0: 20 69      JR           NZ,$622B
61C2: 73         LD           (HL),E
61C3: 20 76      JR           NZ,$623B
61C5: 65         LD           H,L
61C6: 72         LD           (HL),D
61C7: 72         LD           (HL),D
61C8: 72         LD           (HL),D
61C9: 79         LD           A,C
61CA: 20 20      JR           NZ,$61EC
61CC: 73         LD           (HL),E
61CD: 65         LD           H,L
61CE: 6E         LD           L,(HL)
61CF: 73         LD           (HL),E
61D0: 69         LD           L,C
61D1: 74         LD           (HL),H
61D2: 69         LD           L,C
61D3: 76         HALT
61D4: 65         LD           H,L
61D5: 2C         INC         L
61D6: 20 74      JR           NZ,$624C
61D8: 61         LD           H,C
61D9: 20 20      JR           NZ,$61FB
61DB: 20 73      JR           NZ,$6250
61DD: 74         LD           (HL),H
61DE: 75         LD           (HL),L
61DF: 66         LD           H,(HL)
61E0: 66         LD           H,(HL)
61E1: 20 6C      JR           NZ,$624F
61E3: 69         LD           L,C
61E4: 6B         LD           L,E
61E5: 65         LD           H,L
61E6: 20 64      JR           NZ,$624C
61E8: 75         LD           (HL),L
61E9: 73         LD           (HL),E
61EA: 74         LD           (HL),H
61EB: 20 61      JR           NZ,$624E
61ED: 6E         LD           L,(HL)
61EE: 64         LD           H,H
61EF: 20 70      JR           NZ,$6261
61F1: 6F         LD           L,A
61F2: 77         LD           (HL),A
61F3: 64         LD           H,H
61F4: 65         LD           H,L
61F5: 72         LD           (HL),D
61F6: 2E 2E      LD           L,$2E
61F8: 2E FF      LD           L,$FF
61FA: 49         LD           C,C
61FB: 74         LD           (HL),H
61FC: 5E         LD           E,(HL)
61FD: 73         LD           (HL),E
61FE: 20 74      JR           NZ,$6274
6200: 68         LD           L,B
6201: 65         LD           H,L
6202: 20 74      JR           NZ,$6278
6204: 6F         LD           L,A
6205: 61         LD           H,C
6206: 64         LD           H,H
6207: 2D         DEC         L
6208: 20 20      JR           NZ,$622A
620A: 73         LD           (HL),E
620B: 74         LD           (HL),H
620C: 6F         LD           L,A
620D: 6F         LD           L,A
620E: 6C         LD           L,H
620F: 20 79      JR           NZ,$628A
6211: 6F         LD           L,A
6212: 75         LD           (HL),L
6213: 20 70      JR           NZ,$6285
6215: 69         LD           L,C
6216: 63         LD           H,E
6217: 6B         LD           L,E
6218: 65         LD           H,L
6219: 64         LD           H,H
621A: 69         LD           L,C
621B: 6E         LD           L,(HL)
621C: 20 74      JR           NZ,$6292
621E: 68         LD           L,B
621F: 65         LD           H,L
6220: 20 77      JR           NZ,$6299
6222: 6F         LD           L,A
6223: 6F         LD           L,A
6224: 64         LD           H,H
6225: 73         LD           (HL),E
6226: 2E 20      LD           L,$20
6228: 20 20      JR           NZ,$624A
622A: 57         LD           D,A
622B: 68         LD           L,B
622C: 61         LD           H,C
622D: 74         LD           (HL),H
622E: 20 69      JR           NZ,$6299
6230: 73         LD           (HL),E
6231: 20 69      JR           NZ,$629C
6233: 74         LD           (HL),H
6234: 20 66      JR           NZ,$629C
6236: 6F         LD           L,A
6237: 72         LD           (HL),D
6238: 3F         CCF
6239: 20 59      JR           NZ,$6294
623B: 6F         LD           L,A
623C: 75         LD           (HL),L
623D: 20 68      JR           NZ,$62A7
623F: 6F         LD           L,A
6240: 6C         LD           L,H
6241: 64         LD           H,H
6242: 20 69      JR           NZ,$62AD
6244: 74         LD           (HL),H
6245: 20 6F      JR           NZ,$62B6
6247: 76         HALT
6248: 65         LD           H,L
6249: 72         LD           (HL),D
624A: 79         LD           A,C
624B: 6F         LD           L,A
624C: 75         LD           (HL),L
624D: 72         LD           (HL),D
624E: 20 68      JR           NZ,$62B8
6250: 65         LD           H,L
6251: 61         LD           H,C
6252: 64         LD           H,H
6253: 20 61      JR           NZ,$62B6
6255: 6E         LD           L,(HL)
6256: 64         LD           H,H
6257: 20 61      JR           NZ,$62BA
6259: 20 6D      JR           NZ,$62C8
625B: 65         LD           H,L
625C: 6C         LD           L,H
625D: 6C         LD           L,H
625E: 6F         LD           L,A
625F: 77         LD           (HL),A
6260: 20 61      JR           NZ,$62C3
6262: 72         LD           (HL),D
6263: 6F         LD           L,A
6264: 6D         LD           L,L
6265: 61         LD           H,C
6266: 20 20      JR           NZ,$6288
6268: 20 20      JR           NZ,$628A
626A: 77         LD           (HL),A
626B: 61         LD           H,C
626C: 66         LD           H,(HL)
626D: 74         LD           (HL),H
626E: 73         LD           (HL),E
626F: 20 69      JR           NZ,$62DA
6271: 6E         LD           L,(HL)
6272: 74         LD           (HL),H
6273: 6F         LD           L,A
6274: 20 79      JR           NZ,$62EF
6276: 6F         LD           L,A
6277: 75         LD           (HL),L
6278: 72         LD           (HL),D
6279: 20 6E      JR           NZ,$62E9
627B: 6F         LD           L,A
627C: 73         LD           (HL),E
627D: 74         LD           (HL),H
627E: 72         LD           (HL),D
627F: 69         LD           L,C
6280: 6C         LD           L,H
6281: 73         LD           (HL),E
6282: 2E FF      LD           L,$FF
6284: 59         LD           E,C
6285: 6F         LD           L,A
6286: 75         LD           (HL),L
6287: 20 70      JR           NZ,$62F9
6289: 69         LD           L,C
628A: 63         LD           H,E
628B: 6B         LD           L,E
628C: 20 74      JR           NZ,$6302
628E: 68         LD           L,B
628F: 65         LD           H,L
6290: 20 20      JR           NZ,$62B2
6292: 20 20      JR           NZ,$62B4
6294: 74         LD           (HL),H
6295: 6F         LD           L,A
6296: 61         LD           H,C
6297: 64         LD           H,H
6298: 73         LD           (HL),E
6299: 74         LD           (HL),H
629A: 6F         LD           L,A
629B: 6F         LD           L,A
629C: 6C         LD           L,H
629D: 2E 2E      LD           L,$2E
629F: 2E 20      LD           L,$20
62A1: 41         LD           B,C
62A2: 73         LD           (HL),E
62A3: 20 79      JR           NZ,$631E
62A5: 6F         LD           L,A
62A6: 75         LD           (HL),L
62A7: 20 68      JR           NZ,$6311
62A9: 6F         LD           L,A
62AA: 6C         LD           L,H
62AB: 64         LD           H,H
62AC: 20 69      JR           NZ,$6317
62AE: 74         LD           (HL),H
62AF: 20 6F      JR           NZ,$6320
62B1: 76         HALT
62B2: 65         LD           H,L
62B3: 72         LD           (HL),D
62B4: 79         LD           A,C
62B5: 6F         LD           L,A
62B6: 75         LD           (HL),L
62B7: 72         LD           (HL),D
62B8: 20 68      JR           NZ,$6322
62BA: 65         LD           H,L
62BB: 61         LD           H,C
62BC: 64         LD           H,H
62BD: 2C         INC         L
62BE: 20 61      JR           NZ,$6321
62C0: 20 20      JR           NZ,$62E2
62C2: 20 20      JR           NZ,$62E4
62C4: 6D         LD           L,L
62C5: 65         LD           H,L
62C6: 6C         LD           L,H
62C7: 6C         LD           L,H
62C8: 6F         LD           L,A
62C9: 77         LD           (HL),A
62CA: 20 61      JR           NZ,$632D
62CC: 72         LD           (HL),D
62CD: 6F         LD           L,A
62CE: 6D         LD           L,L
62CF: 61         LD           H,C
62D0: 20 20      JR           NZ,$62F2
62D2: 20 20      JR           NZ,$62F4
62D4: 66         LD           H,(HL)
62D5: 6C         LD           L,H
62D6: 6F         LD           L,A
62D7: 77         LD           (HL),A
62D8: 73         LD           (HL),E
62D9: 20 69      JR           NZ,$6344
62DB: 6E         LD           L,(HL)
62DC: 74         LD           (HL),H
62DD: 6F         LD           L,A
62DE: 20 79      JR           NZ,$6359
62E0: 6F         LD           L,A
62E1: 75         LD           (HL),L
62E2: 72         LD           (HL),D
62E3: 20 6E      JR           NZ,$6353
62E5: 6F         LD           L,A
62E6: 73         LD           (HL),E
62E7: 74         LD           (HL),H
62E8: 72         LD           (HL),D
62E9: 69         LD           L,C
62EA: 6C         LD           L,H
62EB: 73         LD           (HL),E
62EC: 2E FF      LD           L,$FF
62EE: 48         LD           C,B
62EF: 72         LD           (HL),D
62F0: 72         LD           (HL),D
62F1: 72         LD           (HL),D
62F2: 6D         LD           L,L
62F3: 2E 2E      LD           L,$2E
62F5: 2E 53      LD           L,$53
62F7: 6E         LD           L,(HL)
62F8: 6F         LD           L,A
62F9: 72         LD           (HL),D
62FA: 65         LD           H,L
62FB: 2E 2E      LD           L,$2E
62FD: 2E 48      LD           L,$48
62FF: 75         LD           (HL),L
6300: 6E         LD           L,(HL)
6301: 68         LD           L,B
6302: 3F         CCF
6303: 2E 2E      LD           L,$2E
6305: 2E 20      LD           L,$20
6307: 49         LD           C,C
6308: 66         LD           H,(HL)
6309: 5E         LD           E,(HL)
630A: 6E         LD           L,(HL)
630B: 20 79      JR           NZ,$6386
630D: 61         LD           H,C
630E: 64         LD           H,H
630F: 6F         LD           L,A
6310: 6E         LD           L,(HL)
6311: 5E         LD           E,(HL)
6312: 20 6B      JR           NZ,$637F
6314: 6E         LD           L,(HL)
6315: 6F         LD           L,A
6316: 77         LD           (HL),A
6317: 2E 2E      LD           L,$2E
6319: 2E 63      LD           L,$63
631B: 61         LD           H,C
631C: 6C         LD           L,H
631D: 6C         LD           L,H
631E: 6F         LD           L,A
631F: 6C         LD           L,H
6320: 64         LD           H,H
6321: 20 6D      JR           NZ,$6390
6323: 61         LD           H,C
6324: 6E         LD           L,(HL)
6325: 20 55      JR           NZ,$637C
6327: 6C         LD           L,H
6328: 72         LD           (HL),D
6329: 69         LD           L,C
632A: 72         LD           (HL),D
632B: 61         LD           H,C
632C: 21 20 5A   LD           HL,$5A20
632F: 6F         LD           L,A
6330: 6E         LD           L,(HL)
6331: 6B         LD           L,E
6332: 2E 2E      LD           L,$2E
6334: 2E 53      LD           L,$53
6336: 6E         LD           L,(HL)
6337: 6F         LD           L,A
6338: 72         LD           (HL),D
6339: 65         LD           H,L
633A: 2E 2E      LD           L,$2E
633C: 2E FF      LD           L,$FF
633E: 49         LD           C,C
633F: 5E         LD           E,(HL)
6340: 6D         LD           L,L
6341: 20 74      JR           NZ,$63B7
6343: 69         LD           L,C
6344: 72         LD           (HL),D
6345: 65         LD           H,L
6346: 64         LD           H,H
6347: 2E 2E      LD           L,$2E
6349: 2E 20      LD           L,$20
634B: 49         LD           C,C
634C: 5E         LD           E,(HL)
634D: 6D         LD           L,L
634E: 67         LD           H,A
634F: 6F         LD           L,A
6350: 69         LD           L,C
6351: 6E         LD           L,(HL)
6352: 5E         LD           E,(HL)
6353: 20 74      JR           NZ,$63C9
6355: 61         LD           H,C
6356: 20 73      JR           NZ,$63CB
6358: 6C         LD           L,H
6359: 65         LD           H,L
635A: 65         LD           H,L
635B: 70         LD           (HL),B
635C: 20 20      JR           NZ,$637E
635E: 6E         LD           L,(HL)
635F: 6F         LD           L,A
6360: 77         LD           (HL),A
6361: 2E 2E      LD           L,$2E
6363: 2E 20      LD           L,$20
6365: 5A         LD           E,D
6366: 7A         LD           A,D
6367: 7A         LD           A,D
6368: 7A         LD           A,D
6369: 7A         LD           A,D
636A: 7A         LD           A,D
636B: 2E 2E      LD           L,$2E
636D: 2E FF      LD           L,$FF
636F: 57         LD           D,A
6370: 65         LD           H,L
6371: 6C         LD           L,H
6372: 6C         LD           L,H
6373: 20 74      JR           NZ,$63E9
6375: 68         LD           L,B
6376: 61         LD           H,C
6377: 74         LD           (HL),H
6378: 20 77      JR           NZ,$63F1
637A: 61         LD           H,C
637B: 73         LD           (HL),E
637C: 20 61      JR           NZ,$63DF
637E: 20 73      JR           NZ,$63F3
6380: 75         LD           (HL),L
6381: 72         LD           (HL),D
6382: 70         LD           (HL),B
6383: 72         LD           (HL),D
6384: 69         LD           L,C
6385: 73         LD           (HL),E
6386: 65         LD           H,L
6387: 21 20 20   LD           HL,$2020
638A: 48         LD           C,B
638B: 65         LD           H,L
638C: 79         LD           A,C
638D: 21 20 49   LD           HL,$4920
6390: 5E         LD           E,(HL)
6391: 6C         LD           L,H
6392: 6C         LD           L,H
6393: 20 74      JR           NZ,$6409
6395: 65         LD           H,L
6396: 6C         LD           L,H
6397: 6C         LD           L,H
6398: 20 79      JR           NZ,$6413
639A: 6F         LD           L,A
639B: 75         LD           (HL),L
639C: 20 61      JR           NZ,$63FF
639E: 20 73      JR           NZ,$6413
63A0: 65         LD           H,L
63A1: 63         LD           H,E
63A2: 72         LD           (HL),D
63A3: 65         LD           H,L
63A4: 74         LD           (HL),H
63A5: 21 20 55   LD           HL,$5520
63A8: 73         LD           (HL),E
63A9: 65         LD           H,L
63AA: 20 79      JR           NZ,$6425
63AC: 6F         LD           L,A
63AD: 75         LD           (HL),L
63AE: 72         LD           (HL),D
63AF: 73         LD           (HL),E
63B0: 77         LD           (HL),A
63B1: 6F         LD           L,A
63B2: 72         LD           (HL),D
63B3: 64         LD           H,H
63B4: 20 74      JR           NZ,$642A
63B6: 6F         LD           L,A
63B7: 20 70      JR           NZ,$6429
63B9: 6F         LD           L,A
63BA: 6B         LD           L,E
63BB: 65         LD           H,L
63BC: 20 61      JR           NZ,$641F
63BE: 74         LD           (HL),H
63BF: 64         LD           H,H
63C0: 75         LD           (HL),L
63C1: 6E         LD           L,(HL)
63C2: 67         LD           H,A
63C3: 65         LD           H,L
63C4: 6F         LD           L,A
63C5: 6E         LD           L,(HL)
63C6: 20 77      JR           NZ,$643F
63C8: 61         LD           H,C
63C9: 6C         LD           L,H
63CA: 6C         LD           L,H
63CB: 73         LD           (HL),E
63CC: 2E 2E      LD           L,$2E
63CE: 2E 49      LD           L,$49
63D0: 66         LD           H,(HL)
63D1: 20 79      JR           NZ,$644C
63D3: 6F         LD           L,A
63D4: 75         LD           (HL),L
63D5: 20 68      JR           NZ,$643F
63D7: 65         LD           H,L
63D8: 61         LD           H,C
63D9: 72         LD           (HL),D
63DA: 20 61      JR           NZ,$643D
63DC: 20 20      JR           NZ,$63FE
63DE: 20 68      JR           NZ,$6448
63E0: 6F         LD           L,A
63E1: 6C         LD           L,H
63E2: 6C         LD           L,H
63E3: 6F         LD           L,A
63E4: 77         LD           (HL),A
63E5: 20 63      JR           NZ,$644A
63E7: 6C         LD           L,H
63E8: 61         LD           H,C
63E9: 6E         LD           L,(HL)
63EA: 6B         LD           L,E
63EB: 2C         INC         L
63EC: 20 20      JR           NZ,$640E
63EE: 20 79      JR           NZ,$6469
63F0: 6F         LD           L,A
63F1: 75         LD           (HL),L
63F2: 20 63      JR           NZ,$6457
63F4: 61         LD           H,C
63F5: 6E         LD           L,(HL)
63F6: 20 62      JR           NZ,$645A
63F8: 72         LD           (HL),D
63F9: 65         LD           H,L
63FA: 61         LD           H,C
63FB: 6B         LD           L,E
63FC: 20 20      JR           NZ,$641E
63FE: 20 74      JR           NZ,$6474
6400: 68         LD           L,B
6401: 65         LD           H,L
6402: 20 77      JR           NZ,$647B
6404: 61         LD           H,C
6405: 6C         LD           L,H
6406: 6C         LD           L,H
6407: 20 77      JR           NZ,$6480
6409: 69         LD           L,C
640A: 74         LD           (HL),H
640B: 68         LD           L,B
640C: 20 61      JR           NZ,$646F
640E: 20 42      JR           NZ,$6452
6410: 6F         LD           L,A
6411: 6D         LD           L,L
6412: 62         LD           H,D
6413: 21 FF 59   LD           HL,$59FF
6416: 6F         LD           L,A
6417: 75         LD           (HL),L
6418: 5E         LD           E,(HL)
6419: 76         HALT
641A: 65         LD           H,L
641B: 20 6C      JR           NZ,$6489
641D: 65         LD           H,L
641E: 61         LD           H,C
641F: 72         LD           (HL),D
6420: 6E         LD           L,(HL)
6421: 65         LD           H,L
6422: 64         LD           H,H
6423: 20 20      JR           NZ,$6445
6425: 74         LD           (HL),H
6426: 68         LD           L,B
6427: 65         LD           H,L
6428: 20 5E      JR           NZ,$6488
642A: 42         LD           B,D
642B: 61         LD           H,C
642C: 6C         LD           L,H
642D: 6C         LD           L,H
642E: 61         LD           H,C
642F: 64         LD           H,H
6430: 20 6F      JR           NZ,$64A1
6432: 66         LD           H,(HL)
6433: 20 20      JR           NZ,$6455
6435: 74         LD           (HL),H
6436: 68         LD           L,B
6437: 65         LD           H,L
6438: 20 57      JR           NZ,$6491
643A: 69         LD           L,C
643B: 6E         LD           L,(HL)
643C: 64         LD           H,H
643D: 20 46      JR           NZ,$6485
643F: 69         LD           L,C
6440: 73         LD           (HL),E
6441: 68         LD           L,B
6442: 21 5E 20   LD           HL,$205E
6445: 54         LD           D,H
6446: 68         LD           L,B
6447: 69         LD           L,C
6448: 73         LD           (HL),E
6449: 20 73      JR           NZ,$64BE
644B: 6F         LD           L,A
644C: 6E         LD           L,(HL)
644D: 67         LD           H,A
644E: 20 77      JR           NZ,$64C7
6450: 69         LD           L,C
6451: 6C         LD           L,H
6452: 6C         LD           L,H
6453: 20 20      JR           NZ,$6475
6455: 61         LD           H,C
6456: 6C         LD           L,H
6457: 77         LD           (HL),A
6458: 61         LD           H,C
6459: 79         LD           A,C
645A: 73         LD           (HL),E
645B: 20 72      JR           NZ,$64CF
645D: 65         LD           H,L
645E: 6D         LD           L,L
645F: 61         LD           H,C
6460: 69         LD           L,C
6461: 6E         LD           L,(HL)
6462: 20 69      JR           NZ,$64CD
6464: 6E         LD           L,(HL)
6465: 79         LD           A,C
6466: 6F         LD           L,A
6467: 75         LD           (HL),L
6468: 72         LD           (HL),D
6469: 20 68      JR           NZ,$64D3
646B: 65         LD           H,L
646C: 61         LD           H,C
646D: 72         LD           (HL),D
646E: 74         LD           (HL),H
646F: 21 FF 50   LD           HL,$50FF
6472: 6C         LD           L,H
6473: 65         LD           H,L
6474: 61         LD           H,C
6475: 73         LD           (HL),E
6476: 65         LD           H,L
6477: 20 72      JR           NZ,$64EB
6479: 65         LD           H,L
647A: 6D         LD           L,L
647B: 65         LD           H,L
647C: 6D         LD           L,L
647D: 62         LD           H,D
647E: 65         LD           H,L
647F: 72         LD           (HL),D
6480: 20 74      JR           NZ,$64F6
6482: 68         LD           L,B
6483: 69         LD           L,C
6484: 73         LD           (HL),E
6485: 20 73      JR           NZ,$64FA
6487: 6F         LD           L,A
6488: 6E         LD           L,(HL)
6489: 67         LD           H,A
648A: 21 20 20   LD           HL,$2020
648D: 59         LD           E,C
648E: 6F         LD           L,A
648F: 75         LD           (HL),L
6490: 20 73      JR           NZ,$6505
6492: 68         LD           L,B
6493: 6F         LD           L,A
6494: 75         LD           (HL),L
6495: 6C         LD           L,H
6496: 64         LD           H,H
6497: 20 70      JR           NZ,$6509
6499: 6C         LD           L,H
649A: 61         LD           H,C
649B: 79         LD           A,C
649C: 20 69      JR           NZ,$6507
649E: 74         LD           (HL),H
649F: 20 20      JR           NZ,$64C1
64A1: 65         LD           H,L
64A2: 76         HALT
64A3: 65         LD           H,L
64A4: 72         LD           (HL),D
64A5: 79         LD           A,C
64A6: 20 6F      JR           NZ,$6517
64A8: 6E         LD           L,(HL)
64A9: 63         LD           H,E
64AA: 65         LD           H,L
64AB: 20 69      JR           NZ,$6516
64AD: 6E         LD           L,(HL)
64AE: 20 61      JR           NZ,$6511
64B0: 20 77      JR           NZ,$6529
64B2: 68         LD           L,B
64B3: 69         LD           L,C
64B4: 6C         LD           L,H
64B5: 65         LD           H,L
64B6: 20 74      JR           NZ,$652C
64B8: 6F         LD           L,A
64B9: 20 6B      JR           NZ,$6526
64BB: 65         LD           H,L
64BC: 65         LD           H,L
64BD: 70         LD           (HL),B
64BE: 20 69      JR           NZ,$6529
64C0: 74         LD           (HL),H
64C1: 66         LD           H,(HL)
64C2: 72         LD           (HL),D
64C3: 65         LD           H,L
64C4: 73         LD           (HL),E
64C5: 68         LD           L,B
64C6: 20 69      JR           NZ,$6531
64C8: 6E         LD           L,(HL)
64C9: 20 79      JR           NZ,$6544
64CB: 6F         LD           L,A
64CC: 75         LD           (HL),L
64CD: 72         LD           (HL),D
64CE: 20 20      JR           NZ,$64F0
64D0: 20 6D      JR           NZ,$653F
64D2: 69         LD           L,C
64D3: 6E         LD           L,(HL)
64D4: 64         LD           H,H
64D5: 21 FF 50   LD           HL,$50FF
64D8: 6C         LD           L,H
64D9: 65         LD           H,L
64DA: 61         LD           H,C
64DB: 73         LD           (HL),E
64DC: 65         LD           H,L
64DD: 21 20 20   LD           HL,$2020
64E0: 49         LD           C,C
64E1: 20 77      JR           NZ,$655A
64E3: 61         LD           H,C
64E4: 6E         LD           L,(HL)
64E5: 74         LD           (HL),H
64E6: 20 79      JR           NZ,$6561
64E8: 6F         LD           L,A
64E9: 75         LD           (HL),L
64EA: 20 74      JR           NZ,$6560
64EC: 6F         LD           L,A
64ED: 20 6C      JR           NZ,$655B
64EF: 65         LD           H,L
64F0: 61         LD           H,C
64F1: 72         LD           (HL),D
64F2: 6E         LD           L,(HL)
64F3: 20 69      JR           NZ,$655E
64F5: 74         LD           (HL),H
64F6: 21 54 68   LD           HL,$6854
64F9: 69         LD           L,C
64FA: 73         LD           (HL),E
64FB: 20 73      JR           NZ,$6570
64FD: 6F         LD           L,A
64FE: 6E         LD           L,(HL)
64FF: 67         LD           H,A
6500: 20 69      JR           NZ,$656B
6502: 73         LD           (HL),E
6503: 20 6D      JR           NZ,$6572
6505: 79         LD           A,C
6506: 20 66      JR           NZ,$656E
6508: 61         LD           H,C
6509: 76         HALT
650A: 6F         LD           L,A
650B: 72         LD           (HL),D
650C: 69         LD           L,C
650D: 74         LD           (HL),H
650E: 65         LD           H,L
650F: 21 FF 53   LD           HL,$53FF
6512: 6F         LD           L,A
6513: 2C         INC         L
6514: 20 68      JR           NZ,$657E
6516: 6F         LD           L,A
6517: 77         LD           (HL),A
6518: 20 64      JR           NZ,$657E
651A: 6F         LD           L,A
651B: 20 79      JR           NZ,$6596
651D: 6F         LD           L,A
651E: 75         LD           (HL),L
651F: 20 20      JR           NZ,$6541
6521: 6C         LD           L,H
6522: 69         LD           L,C
6523: 6B         LD           L,E
6524: 65         LD           H,L
6525: 20 69      JR           NZ,$6590
6527: 74         LD           (HL),H
6528: 3F         CCF
6529: 20 20      JR           NZ,$654B
652B: 49         LD           C,C
652C: 74         LD           (HL),H
652D: 5E         LD           E,(HL)
652E: 73         LD           (HL),E
652F: 20 20      JR           NZ,$6551
6531: 72         LD           (HL),D
6532: 65         LD           H,L
6533: 61         LD           H,C
6534: 6C         LD           L,H
6535: 6C         LD           L,H
6536: 79         LD           A,C
6537: 20 74      JR           NZ,$65AD
6539: 6F         LD           L,A
653A: 75         LD           (HL),L
653B: 63         LD           H,E
653C: 68         LD           L,B
653D: 69         LD           L,C
653E: 6E         LD           L,(HL)
653F: 67         LD           H,A
6540: 2C         INC         L
6541: 69         LD           L,C
6542: 73         LD           (HL),E
6543: 6E         LD           L,(HL)
6544: 5E         LD           E,(HL)
6545: 74         LD           (HL),H
6546: 20 69      JR           NZ,$65B1
6548: 74         LD           (HL),H
6549: 3F         CCF
654A: 20 20      JR           NZ,$656C
654C: 44         LD           B,H
654D: 6F         LD           L,A
654E: 65         LD           H,L
654F: 73         LD           (HL),E
6550: 20 69      JR           NZ,$65BB
6552: 74         LD           (HL),H
6553: 20 73      JR           NZ,$65C8
6555: 74         LD           (HL),H
6556: 69         LD           L,C
6557: 63         LD           H,E
6558: 6B         LD           L,E
6559: 20 69      JR           NZ,$65C4
655B: 6E         LD           L,(HL)
655C: 20 79      JR           NZ,$65D7
655E: 6F         LD           L,A
655F: 75         LD           (HL),L
6560: 72         LD           (HL),D
6561: 6D         LD           L,L
6562: 69         LD           L,C
6563: 6E         LD           L,(HL)
6564: 64         LD           H,H
6565: 3F         CCF
6566: 20 20      JR           NZ,$6588
6568: 20 20      JR           NZ,$658A
656A: 20 20      JR           NZ,$658C
656C: 20 20      JR           NZ,$658E
656E: 20 20      JR           NZ,$6590
6570: 20 20      JR           NZ,$6592
6572: 20 20      JR           NZ,$6594
6574: 20 59      JR           NZ,$65CF
6576: 65         LD           H,L
6577: 73         LD           (HL),E
6578: 20 20      JR           NZ,$659A
657A: 4E         LD           C,(HL)
657B: 6F         LD           L,A
657C: FE 48      CP           $48
657E: 69         LD           L,C
657F: 20 74      JR           NZ,$65F5
6581: 68         LD           L,B
6582: 65         LD           H,L
6583: 72         LD           (HL),D
6584: 65         LD           H,L
6585: 2C         INC         L
6586: 20 62      JR           NZ,$65EA
6588: 69         LD           L,C
6589: 67         LD           H,A
658A: 20 20      JR           NZ,$65AC
658C: 20 67      JR           NZ,$65F5
658E: 75         LD           (HL),L
658F: 79         LD           A,C
6590: 21 20 20   LD           HL,$2020
6593: 49         LD           C,C
6594: 5E         LD           E,(HL)
6595: 6D         LD           L,L
6596: 20 43      JR           NZ,$65DB
6598: 72         LD           (HL),D
6599: 61         LD           H,C
659A: 7A         LD           A,D
659B: 79         LD           A,C
659C: 20 54      JR           NZ,$65F2
659E: 72         LD           (HL),D
659F: 61         LD           H,C
65A0: 63         LD           H,E
65A1: 79         LD           A,C
65A2: 21 20 20   LD           HL,$2020
65A5: 49         LD           C,C
65A6: 5E         LD           E,(HL)
65A7: 76         HALT
65A8: 65         LD           H,L
65A9: 20 67      JR           NZ,$6612
65AB: 6F         LD           L,A
65AC: 74         LD           (HL),H
65AD: 61         LD           H,C
65AE: 20 6C      JR           NZ,$661C
65B0: 69         LD           L,C
65B1: 74         LD           (HL),H
65B2: 74         LD           (HL),H
65B3: 6C         LD           L,H
65B4: 65         LD           H,L
65B5: 20 73      JR           NZ,$662A
65B7: 65         LD           H,L
65B8: 63         LD           H,E
65B9: 72         LD           (HL),D
65BA: 65         LD           H,L
65BB: 74         LD           (HL),H
65BC: 20 66      JR           NZ,$6624
65BE: 6F         LD           L,A
65BF: 72         LD           (HL),D
65C0: 20 73      JR           NZ,$6635
65C2: 61         LD           H,C
65C3: 6C         LD           L,H
65C4: 65         LD           H,L
65C5: 20 74      JR           NZ,$663B
65C7: 68         LD           L,B
65C8: 61         LD           H,C
65C9: 74         LD           (HL),H
65CA: 5E         LD           E,(HL)
65CB: 6C         LD           L,H
65CC: 6C         LD           L,H
65CD: 70         LD           (HL),B
65CE: 75         LD           (HL),L
65CF: 6D         LD           L,L
65D0: 70         LD           (HL),B
65D1: 20 79      JR           NZ,$664C
65D3: 6F         LD           L,A
65D4: 75         LD           (HL),L
65D5: 20 75      JR           NZ,$664C
65D7: 70         LD           (HL),B
65D8: 21 FF 57   LD           HL,$57FF
65DB: 69         LD           L,C
65DC: 6C         LD           L,H
65DD: 6C         LD           L,H
65DE: 20 79      JR           NZ,$6659
65E0: 6F         LD           L,A
65E1: 75         LD           (HL),L
65E2: 20 67      JR           NZ,$664B
65E4: 69         LD           L,C
65E5: 76         HALT
65E6: 65         LD           H,L
65E7: 20 6D      JR           NZ,$6656
65E9: 65         LD           H,L
65EA: 32         LD           (HLD),A
65EB: 38 20      JR           C,$660D
65ED: 52         LD           D,D
65EE: 75         LD           (HL),L
65EF: 70         LD           (HL),B
65F0: 65         LD           H,L
65F1: 65         LD           H,L
65F2: 73         LD           (HL),E
65F3: 20 66      JR           NZ,$665B
65F5: 6F         LD           L,A
65F6: 72         LD           (HL),D
65F7: 20 6D      JR           NZ,$6666
65F9: 79         LD           A,C
65FA: 73         LD           (HL),E
65FB: 65         LD           H,L
65FC: 63         LD           H,E
65FD: 72         LD           (HL),D
65FE: 65         LD           H,L
65FF: 74         LD           (HL),H
6600: 3F         CCF
6601: 20 20      JR           NZ,$6623
6603: 20 20      JR           NZ,$6625
6605: 20 20      JR           NZ,$6627
6607: 20 20      JR           NZ,$6629
6609: 20 20      JR           NZ,$662B
660B: 20 20      JR           NZ,$662D
660D: 20 47      JR           NZ,$6656
660F: 69         LD           L,C
6610: 76         HALT
6611: 65         LD           H,L
6612: 20 44      JR           NZ,$6658
6614: 6F         LD           L,A
6615: 6E         LD           L,(HL)
6616: 5E         LD           E,(HL)
6617: 74         LD           (HL),H
6618: FE 48      CP           $48
661A: 6F         LD           L,A
661B: 77         LD           (HL),A
661C: 20 61      JR           NZ,$667F
661E: 62         LD           H,D
661F: 6F         LD           L,A
6620: 75         LD           (HL),L
6621: 74         LD           (HL),H
6622: 20 69      JR           NZ,$668D
6624: 74         LD           (HL),H
6625: 3F         CCF
6626: 20 20      JR           NZ,$6648
6628: 20 34      JR           NZ,$665E
662A: 32         LD           (HLD),A
662B: 20 52      JR           NZ,$667F
662D: 75         LD           (HL),L
662E: 70         LD           (HL),B
662F: 65         LD           H,L
6630: 65         LD           H,L
6631: 73         LD           (HL),E
6632: 20 66      JR           NZ,$669A
6634: 6F         LD           L,A
6635: 72         LD           (HL),D
6636: 20 6D      JR           NZ,$66A5
6638: 79         LD           A,C
6639: 6C         LD           L,H
663A: 69         LD           L,C
663B: 74         LD           (HL),H
663C: 74         LD           (HL),H
663D: 6C         LD           L,H
663E: 65         LD           H,L
663F: 20 73      JR           NZ,$66B4
6641: 65         LD           H,L
6642: 63         LD           H,E
6643: 72         LD           (HL),D
6644: 65         LD           H,L
6645: 74         LD           (HL),H
6646: 2E 2E      LD           L,$2E
6648: 2E 20      LD           L,$20
664A: 20 20      JR           NZ,$666C
664C: 20 47      JR           NZ,$6695
664E: 69         LD           L,C
664F: 76         HALT
6650: 65         LD           H,L
6651: 20 44      JR           NZ,$6697
6653: 6F         LD           L,A
6654: 6E         LD           L,(HL)
6655: 5E         LD           E,(HL)
6656: 74         LD           (HL),H
6657: FE 41      CP           $41
6659: 6C         LD           L,H
665A: 6C         LD           L,H
665B: 20 72      JR           NZ,$66CF
665D: 69         LD           L,C
665E: 67         LD           H,A
665F: 68         LD           L,B
6660: 74         LD           (HL),H
6661: 2C         INC         L
6662: 20 63      JR           NZ,$66C7
6664: 6F         LD           L,A
6665: 6D         LD           L,L
6666: 65         LD           H,L
6667: 20 68      JR           NZ,$66D1
6669: 65         LD           H,L
666A: 72         LD           (HL),D
666B: 65         LD           H,L
666C: 20 61      JR           NZ,$66CF
666E: 6E         LD           L,(HL)
666F: 64         LD           H,H
6670: 20 49      JR           NZ,$66BB
6672: 5E         LD           E,(HL)
6673: 6C         LD           L,H
6674: 6C         LD           L,H
6675: 20 20      JR           NZ,$6697
6677: 20 72      JR           NZ,$66EB
6679: 75         LD           (HL),L
667A: 62         LD           H,D
667B: 20 69      JR           NZ,$66E6
667D: 74         LD           (HL),H
667E: 20 6F      JR           NZ,$66EF
6680: 6E         LD           L,(HL)
6681: 20 79      JR           NZ,$66FC
6683: 6F         LD           L,A
6684: 75         LD           (HL),L
6685: 21 20 20   LD           HL,$2020
6688: 2E 2E      LD           L,$2E
668A: 2E 54      LD           L,$54
668C: 68         LD           L,B
668D: 65         LD           H,L
668E: 72         LD           (HL),D
668F: 65         LD           H,L
6690: 2E 2E      LD           L,$2E
6692: 2E 20      LD           L,$20
6694: 49         LD           C,C
6695: 5E         LD           E,(HL)
6696: 76         HALT
6697: 65         LD           H,L
6698: 61         LD           H,C
6699: 70         LD           (HL),B
669A: 70         LD           (HL),B
669B: 6C         LD           L,H
669C: 69         LD           L,C
669D: 65         LD           H,L
669E: 64         LD           H,H
669F: 20 6D      JR           NZ,$670E
66A1: 79         LD           A,C
66A2: 20 6F      JR           NZ,$6713
66A4: 77         LD           (HL),A
66A5: 6E         LD           L,(HL)
66A6: 20 20      JR           NZ,$66C8
66A8: 73         LD           (HL),E
66A9: 65         LD           H,L
66AA: 63         LD           H,E
66AB: 72         LD           (HL),D
66AC: 65         LD           H,L
66AD: 74         LD           (HL),H
66AE: 20 6D      JR           NZ,$671D
66B0: 65         LD           H,L
66B1: 64         LD           H,H
66B2: 69         LD           L,C
66B3: 63         LD           H,E
66B4: 69         LD           L,C
66B5: 6E         LD           L,(HL)
66B6: 65         LD           H,L
66B7: 21 49 74   LD           HL,$7449
66BA: 20 77      JR           NZ,$6733
66BC: 69         LD           L,C
66BD: 6C         LD           L,H
66BE: 6C         LD           L,H
66BF: 20 74      JR           NZ,$6735
66C1: 61         LD           H,C
66C2: 6B         LD           L,E
66C3: 65         LD           H,L
66C4: 20 20      JR           NZ,$66E6
66C6: 20 20      JR           NZ,$66E8
66C8: 65         LD           H,L
66C9: 66         LD           H,(HL)
66CA: 66         LD           H,(HL)
66CB: 65         LD           H,L
66CC: 63         LD           H,E
66CD: 74         LD           (HL),H
66CE: 20 77      JR           NZ,$6747
66D0: 68         LD           L,B
66D1: 65         LD           H,L
66D2: 6E         LD           L,(HL)
66D3: 20 79      JR           NZ,$674E
66D5: 6F         LD           L,A
66D6: 75         LD           (HL),L
66D7: 20 6C      JR           NZ,$6745
66D9: 6F         LD           L,A
66DA: 73         LD           (HL),E
66DB: 65         LD           H,L
66DC: 20 61      JR           NZ,$673F
66DE: 6C         LD           L,H
66DF: 6C         LD           L,H
66E0: 20 68      JR           NZ,$674A
66E2: 65         LD           H,L
66E3: 61         LD           H,C
66E4: 72         LD           (HL),D
66E5: 74         LD           (HL),H
66E6: 21 20 44   LD           HL,$4420
66E9: 72         LD           (HL),D
66EA: 6F         LD           L,A
66EB: 70         LD           (HL),B
66EC: 20 62      JR           NZ,$6750
66EE: 79         LD           A,C
66EF: 20 61      JR           NZ,$6752
66F1: 67         LD           H,A
66F2: 61         LD           H,C
66F3: 69         LD           L,C
66F4: 6E         LD           L,(HL)
66F5: 2C         INC         L
66F6: 20 20      JR           NZ,$6718
66F8: 62         LD           H,D
66F9: 69         LD           L,C
66FA: 67         LD           H,A
66FB: 20 67      JR           NZ,$6764
66FD: 75         LD           (HL),L
66FE: 79         LD           A,C
66FF: 21 FF 42   LD           HL,$42FF
6702: 65         LD           H,L
6703: 61         LD           H,C
6704: 74         LD           (HL),H
6705: 20 69      JR           NZ,$6770
6707: 74         LD           (HL),H
6708: 2C         INC         L
6709: 20 74      JR           NZ,$677F
670B: 68         LD           L,B
670C: 65         LD           H,L
670D: 6E         LD           L,(HL)
670E: 21 20 20   LD           HL,$2020
6711: 43         LD           B,E
6712: 6F         LD           L,A
6713: 6D         LD           L,L
6714: 65         LD           H,L
6715: 20 62      JR           NZ,$6779
6717: 61         LD           H,C
6718: 63         LD           H,E
6719: 6B         LD           L,E
671A: 20 77      JR           NZ,$6793
671C: 68         LD           L,B
671D: 65         LD           H,L
671E: 6E         LD           L,(HL)
671F: 20 20      JR           NZ,$6741
6721: 79         LD           A,C
6722: 6F         LD           L,A
6723: 75         LD           (HL),L
6724: 20 68      JR           NZ,$678E
6726: 61         LD           H,C
6727: 76         HALT
6728: 65         LD           H,L
6729: 20 73      JR           NZ,$679E
672B: 6F         LD           L,A
672C: 6D         LD           L,L
672D: 65         LD           H,L
672E: 20 20      JR           NZ,$6750
6730: 20 63      JR           NZ,$6795
6732: 61         LD           H,C
6733: 73         LD           (HL),E
6734: 68         LD           L,B
6735: 21 FF 2E   LD           HL,$2EFF
6738: 2E 2E      LD           L,$2E
673A: 20 2E      JR           NZ,$676A
673C: 2E 2E      LD           L,$2E
673E: 20 2E      JR           NZ,$676E
6740: 2E 2E      LD           L,$2E
6742: 20 2E      JR           NZ,$6772
6744: 2E 2E      LD           L,$2E
6746: 20 42      JR           NZ,$678A
6748: 75         LD           (HL),L
6749: 74         LD           (HL),H
674A: 20 49      JR           NZ,$6795
674C: 20 77      JR           NZ,$67C5
674E: 6F         LD           L,A
674F: 6E         LD           L,(HL)
6750: 5E         LD           E,(HL)
6751: 74         LD           (HL),H
6752: 20 73      JR           NZ,$67C7
6754: 65         LD           H,L
6755: 6C         LD           L,H
6756: 6C         LD           L,H
6757: 69         LD           L,C
6758: 74         LD           (HL),H
6759: 20 74      JR           NZ,$67CF
675B: 6F         LD           L,A
675C: 20 79      JR           NZ,$67D7
675E: 6F         LD           L,A
675F: 75         LD           (HL),L
6760: 21 FF 57   LD           HL,$57FF
6763: 65         LD           H,L
6764: 6C         LD           L,H
6765: 6C         LD           L,H
6766: 21 20 20   LD           HL,$2020
6769: 49         LD           C,C
676A: 5E         LD           E,(HL)
676B: 6D         LD           L,L
676C: 20 6F      JR           NZ,$67DD
676E: 6E         LD           L,(HL)
676F: 6C         LD           L,H
6770: 79         LD           A,C
6771: 20 6F      JR           NZ,$67E2
6773: 66         LD           H,(HL)
6774: 66         LD           H,(HL)
6775: 65         LD           H,L
6776: 72         LD           (HL),D
6777: 69         LD           L,C
6778: 6E         LD           L,(HL)
6779: 67         LD           H,A
677A: 20 79      JR           NZ,$67F5
677C: 6F         LD           L,A
677D: 75         LD           (HL),L
677E: 20 61      JR           NZ,$67E1
6780: 20 20      JR           NZ,$67A2
6782: 73         LD           (HL),E
6783: 65         LD           H,L
6784: 63         LD           H,E
6785: 72         LD           (HL),D
6786: 65         LD           H,L
6787: 74         LD           (HL),H
6788: 20 74      JR           NZ,$67FE
678A: 68         LD           L,B
678B: 61         LD           H,C
678C: 74         LD           (HL),H
678D: 20 77      JR           NZ,$6806
678F: 69         LD           L,C
6790: 6C         LD           L,H
6791: 6C         LD           L,H
6792: 6D         LD           L,L
6793: 61         LD           H,C
6794: 6B         LD           L,E
6795: 65         LD           H,L
6796: 20 79      JR           NZ,$6811
6798: 6F         LD           L,A
6799: 75         LD           (HL),L
679A: 20 73      JR           NZ,$680F
679C: 74         LD           (HL),H
679D: 72         LD           (HL),D
679E: 6F         LD           L,A
679F: 6E         LD           L,(HL)
67A0: 67         LD           H,A
67A1: 21 59 6F   LD           HL,$6F59
67A4: 75         LD           (HL),L
67A5: 5E         LD           E,(HL)
67A6: 72         LD           (HL),D
67A7: 65         LD           H,L
67A8: 20 73      JR           NZ,$681D
67AA: 75         LD           (HL),L
67AB: 63         LD           H,E
67AC: 68         LD           L,B
67AD: 20 61      JR           NZ,$6810
67AF: 20 20      JR           NZ,$67D1
67B1: 20 63      JR           NZ,$6816
67B3: 68         LD           L,B
67B4: 69         LD           L,C
67B5: 63         LD           H,E
67B6: 6B         LD           L,E
67B7: 65         LD           H,L
67B8: 6E         LD           L,(HL)
67B9: 21 21 FF   LD           HL,$FF21
67BC: 2E 2E      LD           L,$2E
67BE: 2E 59      LD           L,$59
67C0: 6F         LD           L,A
67C1: 75         LD           (HL),L
67C2: 5E         LD           E,(HL)
67C3: 72         LD           (HL),D
67C4: 65         LD           H,L
67C5: 20 73      JR           NZ,$683A
67C7: 6F         LD           L,A
67C8: 20 20      JR           NZ,$67EA
67CA: 20 20      JR           NZ,$67EC
67CC: 63         LD           H,E
67CD: 75         LD           (HL),L
67CE: 74         LD           (HL),H
67CF: 65         LD           H,L
67D0: 21 20 20   LD           HL,$2020
67D3: 49         LD           C,C
67D4: 5E         LD           E,(HL)
67D5: 6C         LD           L,H
67D6: 6C         LD           L,H
67D7: 20 67      JR           NZ,$6840
67D9: 69         LD           L,C
67DA: 76         HALT
67DB: 65         LD           H,L
67DC: 79         LD           A,C
67DD: 6F         LD           L,A
67DE: 75         LD           (HL),L
67DF: 20 61      JR           NZ,$6842
67E1: 20 37      JR           NZ,$681A
67E3: 20 52      JR           NZ,$6837
67E5: 75         LD           (HL),L
67E6: 70         LD           (HL),B
67E7: 65         LD           H,L
67E8: 65         LD           H,L
67E9: 20 20      JR           NZ,$680B
67EB: 20 64      JR           NZ,$6851
67ED: 69         LD           L,C
67EE: 73         LD           (HL),E
67EF: 63         LD           H,E
67F0: 6F         LD           L,A
67F1: 75         LD           (HL),L
67F2: 6E         LD           L,(HL)
67F3: 74         LD           (HL),H
67F4: 21 FF 59   LD           HL,$59FF
67F7: 6F         LD           L,A
67F8: 75         LD           (HL),L
67F9: 20 67      JR           NZ,$6862
67FB: 6F         LD           L,A
67FC: 74         LD           (HL),H
67FD: 20 4D      JR           NZ,$684C
67FF: 61         LD           H,C
6800: 72         LD           (HL),D
6801: 69         LD           L,C
6802: 6E         LD           L,(HL)
6803: 21 20 20   LD           HL,$2020
6806: 49         LD           C,C
6807: 73         LD           (HL),E
6808: 20 74      JR           NZ,$687E
680A: 68         LD           L,B
680B: 69         LD           L,C
680C: 73         LD           (HL),E
680D: 20 79      JR           NZ,$6888
680F: 6F         LD           L,A
6810: 75         LD           (HL),L
6811: 72         LD           (HL),D
6812: 20 62      JR           NZ,$6876
6814: 69         LD           L,C
6815: 67         LD           H,A
6816: 63         LD           H,E
6817: 68         LD           L,B
6818: 61         LD           H,C
6819: 6E         LD           L,(HL)
681A: 63         LD           H,E
681B: 65         LD           H,L
681C: 3F         CCF
681D: FF         RST         0X38
681E: 47         LD           B,A
681F: 52         LD           D,D
6820: 52         LD           D,D
6821: 52         LD           D,D
6822: 52         LD           D,D
6823: 2E 2E      LD           L,$2E
6825: 2E FF      LD           L,$FF
6827: 48         LD           C,B
6828: 65         LD           H,L
6829: 68         LD           L,B
682A: 20 68      JR           NZ,$6894
682C: 65         LD           H,L
682D: 68         LD           L,B
682E: 20 68      JR           NZ,$6898
6830: 65         LD           H,L
6831: 68         LD           L,B
6832: 20 68      JR           NZ,$689C
6834: 6F         LD           L,A
6835: 21 20 59   LD           HL,$5920
6838: 6F         LD           L,A
6839: 75         LD           (HL),L
683A: 5E         LD           E,(HL)
683B: 72         LD           (HL),D
683C: 65         LD           H,L
683D: 20 67      JR           NZ,$68A6
683F: 6F         LD           L,A
6840: 69         LD           L,C
6841: 6E         LD           L,(HL)
6842: 5E         LD           E,(HL)
6843: 20 74      JR           NZ,$68B9
6845: 61         LD           H,C
6846: 20 62      JR           NZ,$68AA
6848: 65         LD           H,L
6849: 20 6C      JR           NZ,$68B7
684B: 6F         LD           L,A
684C: 73         LD           (HL),E
684D: 74         LD           (HL),H
684E: 2C         INC         L
684F: 20 74      JR           NZ,$68C5
6851: 68         LD           L,B
6852: 61         LD           H,C
6853: 6E         LD           L,(HL)
6854: 6B         LD           L,E
6855: 73         LD           (HL),E
6856: 20 74      JR           NZ,$68CC
6858: 6F         LD           L,A
6859: 20 6D      JR           NZ,$68C8
685B: 65         LD           H,L
685C: 21 20 20   LD           HL,$2020
685F: 48         LD           C,B
6860: 65         LD           H,L
6861: 68         LD           L,B
6862: 20 68      JR           NZ,$68CC
6864: 65         LD           H,L
6865: 68         LD           L,B
6866: 21 FF 42   LD           HL,$42FF
6869: 4F         LD           C,A
686A: 57         LD           D,A
686B: 20 57      JR           NZ,$68C4
686D: 4F         LD           C,A
686E: 57         LD           D,A
686F: 21 20 20   LD           HL,$2020
6872: 20 20      JR           NZ,$6894
6874: 20 20      JR           NZ,$6896
6876: 20 20      JR           NZ,$6898
6878: 42         LD           B,D
6879: 4F         LD           C,A
687A: 57         LD           D,A
687B: 20 57      JR           NZ,$68D4
687D: 4F         LD           C,A
687E: 57         LD           D,A
687F: 21 FF 59   LD           HL,$59FF
6882: 49         LD           C,C
6883: 50         LD           D,B
6884: 20 59      JR           NZ,$68DF
6886: 49         LD           C,C
6887: 50         LD           D,B
6888: 21 20 20   LD           HL,$2020
688B: 20 20      JR           NZ,$68AD
688D: 20 20      JR           NZ,$68AF
688F: 20 20      JR           NZ,$68B1
6891: 59         LD           E,C
6892: 49         LD           C,C
6893: 50         LD           D,B
6894: 20 59      JR           NZ,$68EF
6896: 49         LD           C,C
6897: 50         LD           D,B
6898: 21 FF 4C   LD           HL,$4CFF
689B: 65         LD           H,L
689C: 74         LD           (HL),H
689D: 5E         LD           E,(HL)
689E: 73         LD           (HL),E
689F: 20 68      JR           NZ,$6909
68A1: 65         LD           H,L
68A2: 61         LD           H,C
68A3: 6C         LD           L,H
68A4: 20 79      JR           NZ,$691F
68A6: 6F         LD           L,A
68A7: 75         LD           (HL),L
68A8: 72         LD           (HL),D
68A9: 20 77      JR           NZ,$6922
68AB: 6F         LD           L,A
68AC: 75         LD           (HL),L
68AD: 6E         LD           L,(HL)
68AE: 64         LD           H,H
68AF: 73         LD           (HL),E
68B0: 20 61      JR           NZ,$6913
68B2: 6E         LD           L,(HL)
68B3: 64         LD           H,H
68B4: 20 67      JR           NZ,$691D
68B6: 65         LD           H,L
68B7: 74         LD           (HL),H
68B8: 20 20      JR           NZ,$68DA
68BA: 72         LD           (HL),D
68BB: 69         LD           L,C
68BC: 64         LD           H,H
68BD: 20 6F      JR           NZ,$692E
68BF: 66         LD           H,(HL)
68C0: 20 61      JR           NZ,$6923
68C2: 6C         LD           L,H
68C3: 6C         LD           L,H
68C4: 20 74      JR           NZ,$693A
68C6: 68         LD           L,B
68C7: 61         LD           H,C
68C8: 74         LD           (HL),H
68C9: 20 73      JR           NZ,$693E
68CB: 74         LD           (HL),H
68CC: 72         LD           (HL),D
68CD: 65         LD           H,L
68CE: 73         LD           (HL),E
68CF: 73         LD           (HL),E
68D0: 2E 2E      LD           L,$2E
68D2: 2E 20      LD           L,$20
68D4: 43         LD           B,E
68D5: 6C         LD           L,H
68D6: 6F         LD           L,A
68D7: 73         LD           (HL),E
68D8: 65         LD           H,L
68D9: 20 79      JR           NZ,$6954
68DB: 6F         LD           L,A
68DC: 75         LD           (HL),L
68DD: 72         LD           (HL),D
68DE: 20 65      JR           NZ,$6945
68E0: 79         LD           A,C
68E1: 65         LD           H,L
68E2: 73         LD           (HL),E
68E3: 20 61      JR           NZ,$6946
68E5: 6E         LD           L,(HL)
68E6: 64         LD           H,H
68E7: 20 20      JR           NZ,$6909
68E9: 20 72      JR           NZ,$695D
68EB: 65         LD           H,L
68EC: 6C         LD           L,H
68ED: 61         LD           H,C
68EE: 78         LD           A,B
68EF: 2E 2E      LD           L,$2E
68F1: 2E FF      LD           L,$FF
68F3: 59         LD           E,C
68F4: 6F         LD           L,A
68F5: 75         LD           (HL),L
68F6: 20 64      JR           NZ,$695C
68F8: 69         LD           L,C
68F9: 72         LD           (HL),D
68FA: 74         LD           (HL),H
68FB: 79         LD           A,C
68FC: 20 72      JR           NZ,$6970
68FE: 61         LD           H,C
68FF: 74         LD           (HL),H
6900: 21 20 20   LD           HL,$2020
6903: 59         LD           E,C
6904: 6F         LD           L,A
6905: 75         LD           (HL),L
6906: 20 6B      JR           NZ,$6973
6908: 2D         DEC         L
6909: 6B         LD           L,E
690A: 2D         DEC         L
690B: 6B         LD           L,E
690C: 2E 2E      LD           L,$2E
690E: 2E 62      LD           L,$62
6910: 65         LD           H,L
6911: 61         LD           H,C
6912: 74         LD           (HL),H
6913: 6D         LD           L,L
6914: 79         LD           A,C
6915: 20 62      JR           NZ,$6979
6917: 72         LD           (HL),D
6918: 6F         LD           L,A
6919: 74         LD           (HL),H
691A: 68         LD           L,B
691B: 65         LD           H,L
691C: 72         LD           (HL),D
691D: 73         LD           (HL),E
691E: 21 20 20   LD           HL,$2020
6921: 20 20      JR           NZ,$6943
6923: 59         LD           E,C
6924: 6F         LD           L,A
6925: 75         LD           (HL),L
6926: 5E         LD           E,(HL)
6927: 6C         LD           L,H
6928: 6C         LD           L,H
6929: 20 70      JR           NZ,$699B
692B: 61         LD           H,C
692C: 79         LD           A,C
692D: 21 21 20   LD           HL,$2021
6930: 20 20      JR           NZ,$6952
6932: 20 49      JR           NZ,$697D
6934: 5E         LD           E,(HL)
6935: 6C         LD           L,H
6936: 6C         LD           L,H
6937: 20 6E      JR           NZ,$69A7
6939: 65         LD           H,L
693A: 76         HALT
693B: 65         LD           H,L
693C: 72         LD           (HL),D
693D: 20 20      JR           NZ,$695F
693F: 20 20      JR           NZ,$6961
6941: 20 20      JR           NZ,$6963
6943: 66         LD           H,(HL)
6944: 6F         LD           L,A
6945: 72         LD           (HL),D
6946: 67         LD           H,A
6947: 65         LD           H,L
6948: 74         LD           (HL),H
6949: 20 79      JR           NZ,$69C4
694B: 6F         LD           L,A
694C: 75         LD           (HL),L
694D: 21 FF 48   LD           HL,$48FF
6950: 65         LD           H,L
6951: 79         LD           A,C
6952: 20 72      JR           NZ,$69C6
6954: 75         LD           (HL),L
6955: 6E         LD           L,(HL)
6956: 74         LD           (HL),H
6957: 21 20 20   LD           HL,$2020
695A: 59         LD           E,C
695B: 6F         LD           L,A
695C: 75         LD           (HL),L
695D: 20 20      JR           NZ,$697F
695F: 74         LD           (HL),H
6960: 68         LD           L,B
6961: 69         LD           L,C
6962: 6E         LD           L,(HL)
6963: 6B         LD           L,E
6964: 20 79      JR           NZ,$69DF
6966: 6F         LD           L,A
6967: 75         LD           (HL),L
6968: 20 63      JR           NZ,$69CD
696A: 61         LD           H,C
696B: 6E         LD           L,(HL)
696C: 20 20      JR           NZ,$698E
696E: 20 74      JR           NZ,$69E4
6970: 61         LD           H,C
6971: 6B         LD           L,E
6972: 65         LD           H,L
6973: 20 6D      JR           NZ,$69E2
6975: 65         LD           H,L
6976: 3F         CCF
6977: 21 20 20   LD           HL,$2020
697A: 41         LD           B,C
697B: 6C         LD           L,H
697C: 6C         LD           L,H
697D: 20 20      JR           NZ,$699F
697F: 72         LD           (HL),D
6980: 69         LD           L,C
6981: 67         LD           H,A
6982: 68         LD           L,B
6983: 74         LD           (HL),H
6984: 20 62      JR           NZ,$69E8
6986: 6F         LD           L,A
6987: 79         LD           A,C
6988: 73         LD           (HL),E
6989: 2C         INC         L
698A: 20 67      JR           NZ,$69F3
698C: 65         LD           H,L
698D: 74         LD           (HL),H
698E: 20 74      JR           NZ,$6A04
6990: 68         LD           L,B
6991: 69         LD           L,C
6992: 73         LD           (HL),E
6993: 20 70      JR           NZ,$6A05
6995: 75         LD           (HL),L
6996: 6E         LD           L,(HL)
6997: 6B         LD           L,E
6998: 20 6F      JR           NZ,$6A09
699A: 75         LD           (HL),L
699B: 74         LD           (HL),H
699C: 20 20      JR           NZ,$69BE
699E: 20 6F      JR           NZ,$6A0F
69A0: 66         LD           H,(HL)
69A1: 20 6D      JR           NZ,$6A10
69A3: 79         LD           A,C
69A4: 20 66      JR           NZ,$6A0C
69A6: 61         LD           H,C
69A7: 63         LD           H,E
69A8: 65         LD           H,L
69A9: 21 FF 59   LD           HL,$59FF
69AC: 65         LD           H,L
69AD: 70         LD           (HL),B
69AE: 21 20 20   LD           HL,$2020
69B1: 54         LD           D,H
69B2: 68         LD           L,B
69B3: 6F         LD           L,A
69B4: 73         LD           (HL),E
69B5: 65         LD           H,L
69B6: 5E         LD           E,(HL)
69B7: 72         LD           (HL),D
69B8: 65         LD           H,L
69B9: 20 20      JR           NZ,$69DB
69BB: 6D         LD           L,L
69BC: 79         LD           A,C
69BD: 20 62      JR           NZ,$6A21
69BF: 6F         LD           L,A
69C0: 79         LD           A,C
69C1: 73         LD           (HL),E
69C2: 21 20 20   LD           HL,$2020
69C5: 49         LD           C,C
69C6: 5E         LD           E,(HL)
69C7: 6D         LD           L,L
69C8: 20 20      JR           NZ,$69EA
69CA: 20 50      JR           NZ,$6A1C
69CC: 61         LD           H,C
69CD: 70         LD           (HL),B
69CE: 61         LD           H,C
69CF: 68         LD           L,B
69D0: 6C         LD           L,H
69D1: 2C         INC         L
69D2: 20 70      JR           NZ,$6A44
69D4: 6C         LD           L,H
69D5: 65         LD           H,L
69D6: 61         LD           H,C
69D7: 73         LD           (HL),E
69D8: 65         LD           H,L
69D9: 64         LD           H,H
69DA: 20 74      JR           NZ,$6A50
69DC: 61         LD           H,C
69DD: 20 6D      JR           NZ,$6A4C
69DF: 65         LD           H,L
69E0: 65         LD           H,L
69E1: 74         LD           (HL),H
69E2: 63         LD           H,E
69E3: 68         LD           L,B
69E4: 61         LD           H,C
69E5: 21 20 49   LD           HL,$4920
69E8: 5E         LD           E,(HL)
69E9: 6C         LD           L,H
69EA: 6C         LD           L,H
69EB: 62         LD           H,D
69EC: 65         LD           H,L
69ED: 20 6C      JR           NZ,$6A5B
69EF: 6F         LD           L,A
69F0: 73         LD           (HL),E
69F1: 74         LD           (HL),H
69F2: 20 69      JR           NZ,$6A5D
69F4: 6E         LD           L,(HL)
69F5: 20 74      JR           NZ,$6A6B
69F7: 68         LD           L,B
69F8: 65         LD           H,L
69F9: 20 20      JR           NZ,$6A1B
69FB: 68         LD           L,B
69FC: 69         LD           L,C
69FD: 6C         LD           L,H
69FE: 6C         LD           L,H
69FF: 73         LD           (HL),E
6A00: 20 6C      JR           NZ,$6A6E
6A02: 61         LD           H,C
6A03: 74         LD           (HL),H
6A04: 65         LD           H,L
6A05: 72         LD           (HL),D
6A06: 2C         INC         L
6A07: 20 73      JR           NZ,$6A7C
6A09: 6F         LD           L,A
6A0A: 20 6B      JR           NZ,$6A77
6A0C: 65         LD           H,L
6A0D: 65         LD           H,L
6A0E: 70         LD           (HL),B
6A0F: 20 61      JR           NZ,$6A72
6A11: 20 6C      JR           NZ,$6A7F
6A13: 6F         LD           L,A
6A14: 6F         LD           L,A
6A15: 6B         LD           L,E
6A16: 20 6F      JR           NZ,$6A87
6A18: 75         LD           (HL),L
6A19: 74         LD           (HL),H
6A1A: 20 66      JR           NZ,$6A82
6A1C: 6F         LD           L,A
6A1D: 72         LD           (HL),D
6A1E: 20 6D      JR           NZ,$6A8D
6A20: 65         LD           H,L
6A21: 2C         INC         L
6A22: 20 68      JR           NZ,$6A8C
6A24: 65         LD           H,L
6A25: 61         LD           H,C
6A26: 72         LD           (HL),D
6A27: 3F         CCF
6A28: FF         RST         0X38
6A29: 59         LD           E,C
6A2A: 65         LD           H,L
6A2B: 73         LD           (HL),E
6A2C: 21 21 20   LD           HL,$2021
6A2F: 20 59      JR           NZ,$6A8A
6A31: 65         LD           H,L
6A32: 73         LD           (HL),E
6A33: 21 21 20   LD           HL,$2021
6A36: 20 20      JR           NZ,$6A58
6A38: 20 42      JR           NZ,$6A7C
6A3A: 72         LD           (HL),D
6A3B: 65         LD           H,L
6A3C: 61         LD           H,C
6A3D: 6B         LD           L,E
6A3E: 20 74      JR           NZ,$6AB4
6A40: 68         LD           L,B
6A41: 65         LD           H,L
6A42: 6D         LD           L,L
6A43: 21 20 20   LD           HL,$2020
6A46: 20 20      JR           NZ,$6A68
6A48: 20 42      JR           NZ,$6A8C
6A4A: 72         LD           (HL),D
6A4B: 65         LD           H,L
6A4C: 61         LD           H,C
6A4D: 6B         LD           L,E
6A4E: 20 74      JR           NZ,$6AC4
6A50: 68         LD           L,B
6A51: 65         LD           H,L
6A52: 6D         LD           L,L
6A53: 20 61      JR           NZ,$6AB6
6A55: 6C         LD           L,H
6A56: 6C         LD           L,H
6A57: 21 20 2E   LD           HL,$2E20
6A5A: 2E 2E      LD           L,$2E
6A5C: 20 2E      JR           NZ,$6A8C
6A5E: 2E 2E      LD           L,$2E
6A60: 20 2E      JR           NZ,$6A90
6A62: 2E 2E      LD           L,$2E
6A64: 20 2E      JR           NZ,$6A94
6A66: 2E 2E      LD           L,$2E
6A68: 20 57      JR           NZ,$6AC1
6A6A: 68         LD           L,B
6A6B: 61         LD           H,C
6A6C: 74         LD           (HL),H
6A6D: 3F         CCF
6A6E: 20 20      JR           NZ,$6A90
6A70: 57         LD           D,A
6A71: 68         LD           L,B
6A72: 61         LD           H,C
6A73: 74         LD           (HL),H
6A74: 5E         LD           E,(HL)
6A75: 73         LD           (HL),E
6A76: 20 20      JR           NZ,$6A98
6A78: 20 77      JR           NZ,$6AF1
6A7A: 72         LD           (HL),D
6A7B: 6F         LD           L,A
6A7C: 6E         LD           L,(HL)
6A7D: 67         LD           H,A
6A7E: 3F         CCF
6A7F: FF         RST         0X38
6A80: 41         LD           B,C
6A81: 79         LD           A,C
6A82: 65         LD           H,L
6A83: 20 43      JR           NZ,$6AC8
6A85: 61         LD           H,C
6A86: 72         LD           (HL),D
6A87: 61         LD           H,C
6A88: 6D         LD           L,L
6A89: 62         LD           H,D
6A8A: 61         LD           H,C
6A8B: 21 20 20   LD           HL,$2020
6A8E: 20 20      JR           NZ,$6AB0
6A90: 4B         LD           C,E
6A91: 69         LD           L,C
6A92: 64         LD           H,H
6A93: 2C         INC         L
6A94: 20 79      JR           NZ,$6B0F
6A96: 6F         LD           L,A
6A97: 75         LD           (HL),L
6A98: 20 68      JR           NZ,$6B02
6A9A: 61         LD           H,C
6A9B: 76         HALT
6A9C: 65         LD           H,L
6A9D: 20 61      JR           NZ,$6B00
6A9F: 20 6C      JR           NZ,$6B0D
6AA1: 6F         LD           L,A
6AA2: 74         LD           (HL),H
6AA3: 20 74      JR           NZ,$6B19
6AA5: 6F         LD           L,A
6AA6: 20 6C      JR           NZ,$6B14
6AA8: 65         LD           H,L
6AA9: 61         LD           H,C
6AAA: 72         LD           (HL),D
6AAB: 6E         LD           L,(HL)
6AAC: 2C         INC         L
6AAD: 20 20      JR           NZ,$6ACF
6AAF: 20 74      JR           NZ,$6B25
6AB1: 72         LD           (HL),D
6AB2: 79         LD           A,C
6AB3: 69         LD           L,C
6AB4: 6E         LD           L,(HL)
6AB5: 67         LD           H,A
6AB6: 20 74      JR           NZ,$6B2C
6AB8: 6F         LD           L,A
6AB9: 20 62      JR           NZ,$6B1D
6ABB: 75         LD           (HL),L
6ABC: 79         LD           A,C
6ABD: 20 20      JR           NZ,$6ADF
6ABF: 20 73      JR           NZ,$6B34
6AC1: 6F         LD           L,A
6AC2: 6D         LD           L,L
6AC3: 65         LD           H,L
6AC4: 74         LD           (HL),H
6AC5: 68         LD           L,B
6AC6: 69         LD           L,C
6AC7: 6E         LD           L,(HL)
6AC8: 67         LD           H,A
6AC9: 20 79      JR           NZ,$6B44
6ACB: 6F         LD           L,A
6ACC: 75         LD           (HL),L
6ACD: 20 20      JR           NZ,$6AEF
6ACF: 20 68      JR           NZ,$6B39
6AD1: 61         LD           H,C
6AD2: 76         HALT
6AD3: 65         LD           H,L
6AD4: 20 6E      JR           NZ,$6B44
6AD6: 6F         LD           L,A
6AD7: 20 75      JR           NZ,$6B4E
6AD9: 73         LD           (HL),E
6ADA: 65         LD           H,L
6ADB: 20 66      JR           NZ,$6B43
6ADD: 6F         LD           L,A
6ADE: 72         LD           (HL),D
6ADF: 21 FF 59   LD           HL,$59FF
6AE2: 6F         LD           L,A
6AE3: 75         LD           (HL),L
6AE4: 5E         LD           E,(HL)
6AE5: 76         HALT
6AE6: 65         LD           H,L
6AE7: 20 67      JR           NZ,$6B50
6AE9: 6F         LD           L,A
6AEA: 74         LD           (HL),H
6AEB: 20 61      JR           NZ,$6B4E
6AED: 20 20      JR           NZ,$6B0F
6AEF: 20 20      JR           NZ,$6B11
6AF1: 48         LD           C,B
6AF2: 65         LD           H,L
6AF3: 61         LD           H,C
6AF4: 72         LD           (HL),D
6AF5: 74         LD           (HL),H
6AF6: 21 20 20   LD           HL,$2020
6AF9: 54         LD           D,H
6AFA: 68         LD           L,B
6AFB: 75         LD           (HL),L
6AFC: 6D         LD           L,L
6AFD: 70         LD           (HL),B
6AFE: 21 20 20   LD           HL,$2020
6B01: 4F         LD           C,A
6B02: 6E         LD           L,(HL)
6B03: 65         LD           H,L
6B04: 20 6F      JR           NZ,$6B75
6B06: 66         LD           H,(HL)
6B07: 20 79      JR           NZ,$6B82
6B09: 6F         LD           L,A
6B0A: 75         LD           (HL),L
6B0B: 72         LD           (HL),D
6B0C: 20 20      JR           NZ,$6B2E
6B0E: 20 20      JR           NZ,$6B30
6B10: 20 48      JR           NZ,$6B5A
6B12: 65         LD           H,L
6B13: 61         LD           H,C
6B14: 72         LD           (HL),D
6B15: 74         LD           (HL),H
6B16: 20 43      JR           NZ,$6B5B
6B18: 6F         LD           L,A
6B19: 6E         LD           L,(HL)
6B1A: 74         LD           (HL),H
6B1B: 61         LD           H,C
6B1C: 69         LD           L,C
6B1D: 6E         LD           L,(HL)
6B1E: 65         LD           H,L
6B1F: 72         LD           (HL),D
6B20: 73         LD           (HL),E
6B21: 69         LD           L,C
6B22: 73         LD           (HL),E
6B23: 20 66      JR           NZ,$6B8B
6B25: 69         LD           L,C
6B26: 6C         LD           L,H
6B27: 6C         LD           L,H
6B28: 65         LD           H,L
6B29: 64         LD           H,H
6B2A: 21 FF 42   LD           HL,$42FF
6B2D: 6F         LD           L,A
6B2E: 77         LD           (HL),A
6B2F: 20 26      JR           NZ,$6B57
6B31: 20 41      JR           NZ,$6B74
6B33: 72         LD           (HL),D
6B34: 72         LD           (HL),D
6B35: 6F         LD           L,A
6B36: 77         LD           (HL),A
6B37: 20 53      JR           NZ,$6B8C
6B39: 65         LD           H,L
6B3A: 74         LD           (HL),H
6B3B: 20 4F      JR           NZ,$6B8C
6B3D: 6E         LD           L,(HL)
6B3E: 6C         LD           L,H
6B3F: 79         LD           A,C
6B40: 20 39      JR           NZ,$6B7B
6B42: 38 30      JR           C,$6B74
6B44: 20 52      JR           NZ,$6B98
6B46: 75         LD           (HL),L
6B47: 70         LD           (HL),B
6B48: 65         LD           H,L
6B49: 65         LD           H,L
6B4A: 73         LD           (HL),E
6B4B: 21 20 20   LD           HL,$2020
6B4E: 20 20      JR           NZ,$6B70
6B50: 42         LD           B,D
6B51: 75         LD           (HL),L
6B52: 79         LD           A,C
6B53: 20 20      JR           NZ,$6B75
6B55: 4E         LD           C,(HL)
6B56: 6F         LD           L,A
6B57: 20 57      JR           NZ,$6BB0
6B59: 61         LD           H,C
6B5A: 79         LD           A,C
6B5B: FE 20      CP           $20
6B5D: 20 20      JR           NZ,$6B7F
6B5F: 31 30 20   LD           SP,$2030
6B62: 41         LD           B,C
6B63: 72         LD           (HL),D
6B64: 72         LD           (HL),D
6B65: 6F         LD           L,A
6B66: 77         LD           (HL),A
6B67: 73         LD           (HL),E
6B68: 20 20      JR           NZ,$6B8A
6B6A: 20 20      JR           NZ,$6B8C
6B6C: 20 20      JR           NZ,$6B8E
6B6E: 20 31      JR           NZ,$6BA1
6B70: 30 20      JR           NC,$6B92
6B72: 52         LD           D,D
6B73: 75         LD           (HL),L
6B74: 70         LD           (HL),B
6B75: 65         LD           H,L
6B76: 65         LD           H,L
6B77: 73         LD           (HL),E
6B78: 20 20      JR           NZ,$6B9A
6B7A: 20 20      JR           NZ,$6B9C
6B7C: 20 20      JR           NZ,$6B9E
6B7E: 20 20      JR           NZ,$6BA0
6B80: 42         LD           B,D
6B81: 75         LD           (HL),L
6B82: 79         LD           A,C
6B83: 20 20      JR           NZ,$6BA5
6B85: 44         LD           B,H
6B86: 6F         LD           L,A
6B87: 6E         LD           L,(HL)
6B88: 5E         LD           E,(HL)
6B89: 74         LD           (HL),H
6B8A: FE 48      CP           $48
6B8C: 65         LD           H,L
6B8D: 79         LD           A,C
6B8E: 21 20 20   LD           HL,$2020
6B91: 57         LD           D,A
6B92: 65         LD           H,L
6B93: 6C         LD           L,H
6B94: 63         LD           H,E
6B95: 6F         LD           L,A
6B96: 6D         LD           L,L
6B97: 65         LD           H,L
6B98: 21 20 20   LD           HL,$2020
6B9B: 53         LD           D,E
6B9C: 65         LD           H,L
6B9D: 65         LD           H,L
6B9E: 20 73      JR           NZ,$6C13
6BA0: 6F         LD           L,A
6BA1: 6D         LD           L,L
6BA2: 65         LD           H,L
6BA3: 74         LD           (HL),H
6BA4: 68         LD           L,B
6BA5: 69         LD           L,C
6BA6: 6E         LD           L,(HL)
6BA7: 67         LD           H,A
6BA8: 20 20      JR           NZ,$6BCA
6BAA: 20 79      JR           NZ,$6C25
6BAC: 6F         LD           L,A
6BAD: 75         LD           (HL),L
6BAE: 20 6C      JR           NZ,$6C1C
6BB0: 69         LD           L,C
6BB1: 6B         LD           L,E
6BB2: 65         LD           H,L
6BB3: 3F         CCF
6BB4: 21 20 20   LD           HL,$2020
6BB7: 4A         LD           C,D
6BB8: 75         LD           (HL),L
6BB9: 73         LD           (HL),E
6BBA: 74         LD           (HL),H
6BBB: 62         LD           H,D
6BBC: 72         LD           (HL),D
6BBD: 69         LD           L,C
6BBE: 6E         LD           L,(HL)
6BBF: 67         LD           H,A
6BC0: 20 69      JR           NZ,$6C2B
6BC2: 74         LD           (HL),H
6BC3: 20 68      JR           NZ,$6C2D
6BC5: 65         LD           H,L
6BC6: 72         LD           (HL),D
6BC7: 65         LD           H,L
6BC8: 21 FF 48   LD           HL,$48FF
6BCB: 65         LD           H,L
6BCC: 79         LD           A,C
6BCD: 21 20 59   LD           HL,$5920
6BD0: 6F         LD           L,A
6BD1: 75         LD           (HL),L
6BD2: 21 20 53   LD           HL,$5320
6BD5: 74         LD           (HL),H
6BD6: 6F         LD           L,A
6BD7: 70         LD           (HL),B
6BD8: 21 20 59   LD           HL,$5920
6BDB: 6F         LD           L,A
6BDC: 75         LD           (HL),L
6BDD: 20 67      JR           NZ,$6C46
6BDF: 6F         LD           L,A
6BE0: 74         LD           (HL),H
6BE1: 74         LD           (HL),H
6BE2: 61         LD           H,C
6BE3: 20 70      JR           NZ,$6C55
6BE5: 61         LD           H,C
6BE6: 79         LD           A,C
6BE7: 21 20 20   LD           HL,$2020
6BEA: 50         LD           D,B
6BEB: 75         LD           (HL),L
6BEC: 74         LD           (HL),H
6BED: 20 69      JR           NZ,$6C58
6BEF: 74         LD           (HL),H
6BF0: 20 62      JR           NZ,$6C54
6BF2: 61         LD           H,C
6BF3: 63         LD           H,E
6BF4: 6B         LD           L,E
6BF5: 21 FF 20   LD           HL,$20FF
6BF8: 20 44      JR           NZ,$6C3E
6BFA: 65         LD           H,L
6BFB: 6C         LD           L,H
6BFC: 75         LD           (HL),L
6BFD: 78         LD           A,B
6BFE: 65         LD           H,L
6BFF: 20 53      JR           NZ,$6C54
6C01: 68         LD           L,B
6C02: 6F         LD           L,A
6C03: 76         HALT
6C04: 65         LD           H,L
6C05: 6C         LD           L,H
6C06: 20 20      JR           NZ,$6C28
6C08: 20 20      JR           NZ,$6C2A
6C0A: 32         LD           (HLD),A
6C0B: 30 30      JR           NC,$6C3D
6C0D: 20 52      JR           NZ,$6C61
6C0F: 75         LD           (HL),L
6C10: 70         LD           (HL),B
6C11: 65         LD           H,L
6C12: 65         LD           H,L
6C13: 73         LD           (HL),E
6C14: 21 20 20   LD           HL,$2020
6C17: 53         LD           D,E
6C18: 65         LD           H,L
6C19: 65         LD           H,L
6C1A: 6D         LD           L,L
6C1B: 73         LD           (HL),E
6C1C: 20 65      JR           NZ,$6C83
6C1E: 78         LD           A,B
6C1F: 70         LD           (HL),B
6C20: 65         LD           H,L
6C21: 6E         LD           L,(HL)
6C22: 73         LD           (HL),E
6C23: 69         LD           L,C
6C24: 76         HALT
6C25: 65         LD           H,L
6C26: 21 20 20   LD           HL,$2020
6C29: 20 20      JR           NZ,$6C4B
6C2B: 42         LD           B,D
6C2C: 75         LD           (HL),L
6C2D: 79         LD           A,C
6C2E: 20 20      JR           NZ,$6C50
6C30: 4E         LD           C,(HL)
6C31: 6F         LD           L,A
6C32: 20 57      JR           NZ,$6C8B
6C34: 61         LD           H,C
6C35: 79         LD           A,C
6C36: 21 FE 20   LD           HL,$20FE
6C39: 20 20      JR           NZ,$6C5B
6C3B: 54         LD           D,H
6C3C: 68         LD           L,B
6C3D: 72         LD           (HL),D
6C3E: 65         LD           H,L
6C3F: 65         LD           H,L
6C40: 20 48      JR           NZ,$6C8A
6C42: 65         LD           H,L
6C43: 61         LD           H,C
6C44: 72         LD           (HL),D
6C45: 74         LD           (HL),H
6C46: 73         LD           (HL),E
6C47: 20 20      JR           NZ,$6C69
6C49: 20 20      JR           NZ,$6C6B
6C4B: 20 31      JR           NZ,$6C7E
6C4D: 30 20      JR           NC,$6C6F
6C4F: 52         LD           D,D
6C50: 75         LD           (HL),L
6C51: 70         LD           (HL),B
6C52: 65         LD           H,L
6C53: 65         LD           H,L
6C54: 73         LD           (HL),E
6C55: 21 20 20   LD           HL,$2020
6C58: 20 20      JR           NZ,$6C7A
6C5A: 20 20      JR           NZ,$6C7C
6C5C: 42         LD           B,D
6C5D: 75         LD           (HL),L
6C5E: 79         LD           A,C
6C5F: 20 20      JR           NZ,$6C81
6C61: 44         LD           B,H
6C62: 6F         LD           L,A
6C63: 6E         LD           L,(HL)
6C64: 5E         LD           E,(HL)
6C65: 74         LD           (HL),H
6C66: FE 20      CP           $20
6C68: 20 20      JR           NZ,$6C8A
6C6A: 20 20      JR           NZ,$6C8C
6C6C: 53         LD           D,E
6C6D: 68         LD           L,B
6C6E: 69         LD           L,C
6C6F: 65         LD           H,L
6C70: 6C         LD           L,H
6C71: 64         LD           H,H
6C72: 20 20      JR           NZ,$6C94
6C74: 20 20      JR           NZ,$6C96
6C76: 20 20      JR           NZ,$6C98
6C78: 20 20      JR           NZ,$6C9A
6C7A: 20 32      JR           NZ,$6CAE
6C7C: 30 20      JR           NC,$6C9E
6C7E: 52         LD           D,D
6C7F: 75         LD           (HL),L
6C80: 70         LD           (HL),B
6C81: 65         LD           H,L
6C82: 65         LD           H,L
6C83: 73         LD           (HL),E
6C84: 21 20 20   LD           HL,$2020
6C87: 20 20      JR           NZ,$6CA9
6C89: 20 20      JR           NZ,$6CAB
6C8B: 42         LD           B,D
6C8C: 75         LD           (HL),L
6C8D: 79         LD           A,C
6C8E: 20 20      JR           NZ,$6CB0
6C90: 44         LD           B,H
6C91: 6F         LD           L,A
6C92: 6E         LD           L,(HL)
6C93: 5E         LD           E,(HL)
6C94: 74         LD           (HL),H
6C95: FE 20      CP           $20
6C97: 20 20      JR           NZ,$6CB9
6C99: 20 54      JR           NZ,$6CEF
6C9B: 65         LD           H,L
6C9C: 6E         LD           L,(HL)
6C9D: 20 42      JR           NZ,$6CE1
6C9F: 6F         LD           L,A
6CA0: 6D         LD           L,L
6CA1: 62         LD           H,D
6CA2: 73         LD           (HL),E
6CA3: 20 20      JR           NZ,$6CC5
6CA5: 20 20      JR           NZ,$6CC7
6CA7: 20 20      JR           NZ,$6CC9
6CA9: 20 31      JR           NZ,$6CDC
6CAB: 30 20      JR           NC,$6CCD
6CAD: 52         LD           D,D
6CAE: 75         LD           (HL),L
6CAF: 70         LD           (HL),B
6CB0: 65         LD           H,L
6CB1: 65         LD           H,L
6CB2: 73         LD           (HL),E
6CB3: 20 20      JR           NZ,$6CD5
6CB5: 20 20      JR           NZ,$6CD7
6CB7: 20 20      JR           NZ,$6CD9
6CB9: 20 42      JR           NZ,$6CFD
6CBB: 75         LD           (HL),L
6CBC: 79         LD           A,C
6CBD: 20 20      JR           NZ,$6CDF
6CBF: 44         LD           B,H
6CC0: 6F         LD           L,A
6CC1: 6E         LD           L,(HL)
6CC2: 5E         LD           E,(HL)
6CC3: 74         LD           (HL),H
6CC4: FE 53      CP           $53
6CC6: 6F         LD           L,A
6CC7: 72         LD           (HL),D
6CC8: 72         LD           (HL),D
6CC9: 79         LD           A,C
6CCA: 2C         INC         L
6CCB: 20 6B      JR           NZ,$6D38
6CCD: 69         LD           L,C
6CCE: 64         LD           H,H
6CCF: 21 20 20   LD           HL,$2020
6CD2: 59         LD           E,C
6CD3: 6F         LD           L,A
6CD4: 75         LD           (HL),L
6CD5: 64         LD           H,H
6CD6: 6F         LD           L,A
6CD7: 6E         LD           L,(HL)
6CD8: 5E         LD           E,(HL)
6CD9: 74         LD           (HL),H
6CDA: 20 68      JR           NZ,$6D44
6CDC: 61         LD           H,C
6CDD: 76         HALT
6CDE: 65         LD           H,L
6CDF: 20 74      JR           NZ,$6D55
6CE1: 68         LD           L,B
6CE2: 65         LD           H,L
6CE3: 20 20      JR           NZ,$6D05
6CE5: 52         LD           D,D
6CE6: 75         LD           (HL),L
6CE7: 70         LD           (HL),B
6CE8: 65         LD           H,L
6CE9: 65         LD           H,L
6CEA: 73         LD           (HL),E
6CEB: 21 20 20   LD           HL,$2020
6CEE: 43         LD           B,E
6CEF: 6F         LD           L,A
6CF0: 6D         LD           L,L
6CF1: 65         LD           H,L
6CF2: 20 20      JR           NZ,$6D14
6CF4: 20 62      JR           NZ,$6D58
6CF6: 61         LD           H,C
6CF7: 63         LD           H,E
6CF8: 6B         LD           L,E
6CF9: 20 77      JR           NZ,$6D72
6CFB: 68         LD           L,B
6CFC: 65         LD           H,L
6CFD: 6E         LD           L,(HL)
6CFE: 20 79      JR           NZ,$6D79
6D00: 6F         LD           L,A
6D01: 75         LD           (HL),L
6D02: 20 20      JR           NZ,$6D24
6D04: 20 68      JR           NZ,$6D6E
6D06: 61         LD           H,C
6D07: 76         HALT
6D08: 65         LD           H,L
6D09: 20 74      JR           NZ,$6D7F
6D0B: 68         LD           L,B
6D0C: 65         LD           H,L
6D0D: 20 63      JR           NZ,$6D72
6D0F: 61         LD           H,C
6D10: 73         LD           (HL),E
6D11: 68         LD           L,B
6D12: 21 FF 54   LD           HL,$54FF
6D15: 68         LD           L,B
6D16: 61         LD           H,C
6D17: 6E         LD           L,(HL)
6D18: 6B         LD           L,E
6D19: 73         LD           (HL),E
6D1A: 20 61      JR           NZ,$6D7D
6D1C: 20 6C      JR           NZ,$6D8A
6D1E: 6F         LD           L,A
6D1F: 74         LD           (HL),H
6D20: 21 20 20   LD           HL,$2020
6D23: 20 41      JR           NZ,$6D66
6D25: 6E         LD           L,(HL)
6D26: 64         LD           H,H
6D27: 20 63      JR           NZ,$6D8C
6D29: 6F         LD           L,A
6D2A: 6D         LD           L,L
6D2B: 65         LD           H,L
6D2C: 20 61      JR           NZ,$6D8F
6D2E: 67         LD           H,A
6D2F: 61         LD           H,C
6D30: 69         LD           L,C
6D31: 6E         LD           L,(HL)
6D32: 21 FF 47   LD           HL,$47FF
6D35: 75         LD           (HL),L
6D36: 65         LD           H,L
6D37: 73         LD           (HL),E
6D38: 73         LD           (HL),E
6D39: 20 77      JR           NZ,$6DB2
6D3B: 68         LD           L,B
6D3C: 61         LD           H,C
6D3D: 74         LD           (HL),H
6D3E: 3F         CCF
6D3F: 20 20      JR           NZ,$6D61
6D41: 59         LD           E,C
6D42: 6F         LD           L,A
6D43: 75         LD           (HL),L
6D44: 67         LD           H,A
6D45: 6F         LD           L,A
6D46: 74         LD           (HL),H
6D47: 20 69      JR           NZ,$6DB2
6D49: 74         LD           (HL),H
6D4A: 20 66      JR           NZ,$6DB2
6D4C: 6F         LD           L,A
6D4D: 72         LD           (HL),D
6D4E: 20 66      JR           NZ,$6DB6
6D50: 72         LD           (HL),D
6D51: 65         LD           H,L
6D52: 65         LD           H,L
6D53: 2E 41      LD           L,$41
6D55: 72         LD           (HL),D
6D56: 65         LD           H,L
6D57: 20 79      JR           NZ,$6DD2
6D59: 6F         LD           L,A
6D5A: 75         LD           (HL),L
6D5B: 20 70      JR           NZ,$6DCD
6D5D: 72         LD           (HL),D
6D5E: 6F         LD           L,A
6D5F: 75         LD           (HL),L
6D60: 64         LD           H,H
6D61: 20 6F      JR           NZ,$6DD2
6D63: 66         LD           H,(HL)
6D64: 79         LD           A,C
6D65: 6F         LD           L,A
6D66: 75         LD           (HL),L
6D67: 72         LD           (HL),D
6D68: 73         LD           (HL),E
6D69: 65         LD           H,L
6D6A: 6C         LD           L,H
6D6B: 66         LD           H,(HL)
6D6C: 3F         CCF
6D6D: FF         RST         0X38
6D6E: 49         LD           C,C
6D6F: 20 77      JR           NZ,$6DE8
6D71: 61         LD           H,C
6D72: 73         LD           (HL),E
6D73: 6E         LD           L,(HL)
6D74: 5E         LD           E,(HL)
6D75: 74         LD           (HL),H
6D76: 20 6B      JR           NZ,$6DE3
6D78: 69         LD           L,C
6D79: 64         LD           H,H
6D7A: 64         LD           H,H
6D7B: 69         LD           L,C
6D7C: 6E         LD           L,(HL)
6D7D: 67         LD           H,A
6D7E: 77         LD           (HL),A
6D7F: 68         LD           L,B
6D80: 65         LD           H,L
6D81: 6E         LD           L,(HL)
6D82: 20 49      JR           NZ,$6DCD
6D84: 20 73      JR           NZ,$6DF9
6D86: 61         LD           H,C
6D87: 69         LD           L,C
6D88: 64         LD           H,H
6D89: 20 70      JR           NZ,$6DFB
6D8B: 61         LD           H,C
6D8C: 79         LD           A,C
6D8D: 21 4E 6F   LD           HL,$6F4E
6D90: 77         LD           (HL),A
6D91: 2C         INC         L
6D92: 20 79      JR           NZ,$6E0D
6D94: 6F         LD           L,A
6D95: 75         LD           (HL),L
6D96: 5E         LD           E,(HL)
6D97: 6C         LD           L,H
6D98: 6C         LD           L,H
6D99: 20 70      JR           NZ,$6E0B
6D9B: 61         LD           H,C
6D9C: 79         LD           A,C
6D9D: 20 74      JR           NZ,$6E13
6D9F: 68         LD           L,B
6DA0: 65         LD           H,L
6DA1: 20 75      JR           NZ,$6E18
6DA3: 6C         LD           L,H
6DA4: 74         LD           (HL),H
6DA5: 69         LD           L,C
6DA6: 6D         LD           L,L
6DA7: 61         LD           H,C
6DA8: 74         LD           (HL),H
6DA9: 65         LD           H,L
6DAA: 20 20      JR           NZ,$6DCC
6DAC: 20 20      JR           NZ,$6DCE
6DAE: 70         LD           (HL),B
6DAF: 72         LD           (HL),D
6DB0: 69         LD           L,C
6DB1: 63         LD           H,E
6DB2: 65         LD           H,L
6DB3: 21 21 FF   LD           HL,$FF21
6DB6: 48         LD           C,B
6DB7: 75         LD           (HL),L
6DB8: 6E         LD           L,(HL)
6DB9: 68         LD           L,B
6DBA: 3F         CCF
6DBB: 20 20      JR           NZ,$6DDD
6DBD: 49         LD           C,C
6DBE: 74         LD           (HL),H
6DBF: 20 73      JR           NZ,$6E34
6DC1: 6F         LD           L,A
6DC2: 75         LD           (HL),L
6DC3: 6E         LD           L,(HL)
6DC4: 64         LD           H,H
6DC5: 73         LD           (HL),E
6DC6: 6C         LD           L,H
6DC7: 69         LD           L,C
6DC8: 6B         LD           L,E
6DC9: 65         LD           H,L
6DCA: 20 74      JR           NZ,$6E40
6DCC: 68         LD           L,B
6DCD: 65         LD           H,L
6DCE: 20 63      JR           NZ,$6E33
6DD0: 61         LD           H,C
6DD1: 73         LD           (HL),E
6DD2: 74         LD           (HL),H
6DD3: 6C         LD           L,H
6DD4: 65         LD           H,L
6DD5: 20 67      JR           NZ,$6E3E
6DD7: 61         LD           H,C
6DD8: 74         LD           (HL),H
6DD9: 65         LD           H,L
6DDA: 20 6F      JR           NZ,$6E4B
6DDC: 70         LD           (HL),B
6DDD: 65         LD           H,L
6DDE: 6E         LD           L,(HL)
6DDF: 65         LD           H,L
6DE0: 64         LD           H,H
6DE1: 21 20 59   LD           HL,$5920
6DE4: 6F         LD           L,A
6DE5: 75         LD           (HL),L
6DE6: 63         LD           H,E
6DE7: 61         LD           H,C
6DE8: 6E         LD           L,(HL)
6DE9: 20 65      JR           NZ,$6E50
6DEB: 61         LD           H,C
6DEC: 73         LD           (HL),E
6DED: 69         LD           L,C
6DEE: 6C         LD           L,H
6DEF: 79         LD           A,C
6DF0: 20 6C      JR           NZ,$6E5E
6DF2: 65         LD           H,L
6DF3: 61         LD           H,C
6DF4: 76         HALT
6DF5: 65         LD           H,L
6DF6: 74         LD           (HL),H
6DF7: 68         LD           L,B
6DF8: 65         LD           H,L
6DF9: 20 63      JR           NZ,$6E5E
6DFB: 61         LD           H,C
6DFC: 73         LD           (HL),E
6DFD: 74         LD           (HL),H
6DFE: 6C         LD           L,H
6DFF: 65         LD           H,L
6E00: 20 6E      JR           NZ,$6E70
6E02: 6F         LD           L,A
6E03: 77         LD           (HL),A
6E04: 21 FF 20   LD           HL,$20FF
6E07: 20 54      JR           NZ,$6E5D
6E09: 52         LD           D,D
6E0A: 45         LD           B,L
6E0B: 4E         LD           C,(HL)
6E0C: 44         LD           B,H
6E0D: 59         LD           E,C
6E0E: 20 47      JR           NZ,$6E57
6E10: 41         LD           B,C
6E11: 4D         LD           C,L
6E12: 45         LD           B,L
6E13: 21 20 20   LD           HL,$2020
6E16: 20 4F      JR           NZ,$6E67
6E18: 6E         LD           L,(HL)
6E19: 65         LD           H,L
6E1A: 20 50      JR           NZ,$6E6C
6E1C: 6C         LD           L,H
6E1D: 61         LD           H,C
6E1E: 79         LD           A,C
6E1F: 20 31      JR           NZ,$6E52
6E21: 30 20      JR           NC,$6E43
6E23: 52         LD           D,D
6E24: 73         LD           (HL),E
6E25: 2E 20      LD           L,$20
6E27: 20 20      JR           NZ,$6E49
6E29: 20 50      JR           NZ,$6E7B
6E2B: 6C         LD           L,H
6E2C: 61         LD           H,C
6E2D: 79         LD           A,C
6E2E: 20 4E      JR           NZ,$6E7E
6E30: 6F         LD           L,A
6E31: FE 54      CP           $54
6E33: 68         LD           L,B
6E34: 65         LD           H,L
6E35: 20 41      JR           NZ,$6E78
6E37: 20 61      JR           NZ,$6E9A
6E39: 6E         LD           L,(HL)
6E3A: 64         LD           H,H
6E3B: 20 42      JR           NZ,$6E7F
6E3D: 20 20      JR           NZ,$6E5F
6E3F: 20 20      JR           NZ,$6E61
6E41: 20 42      JR           NZ,$6E85
6E43: 75         LD           (HL),L
6E44: 74         LD           (HL),H
6E45: 74         LD           (HL),H
6E46: 6F         LD           L,A
6E47: 6E         LD           L,(HL)
6E48: 73         LD           (HL),E
6E49: 20 6D      JR           NZ,$6EB8
6E4B: 6F         LD           L,A
6E4C: 76         HALT
6E4D: 65         LD           H,L
6E4E: 20 74      JR           NZ,$6EC4
6E50: 68         LD           L,B
6E51: 65         LD           H,L
6E52: 63         LD           H,E
6E53: 72         LD           (HL),D
6E54: 61         LD           H,C
6E55: 6E         LD           L,(HL)
6E56: 65         LD           H,L
6E57: 2E 2E      LD           L,$2E
6E59: 2E 54      LD           L,$54
6E5B: 68         LD           L,B
6E5C: 65         LD           H,L
6E5D: 20 72      JR           NZ,$6ED1
6E5F: 65         LD           H,L
6E60: 73         LD           (HL),E
6E61: 74         LD           (HL),H
6E62: 69         LD           L,C
6E63: 73         LD           (HL),E
6E64: 20 6A      JR           NZ,$6ED0
6E66: 75         LD           (HL),L
6E67: 73         LD           (HL),E
6E68: 74         LD           (HL),H
6E69: 20 74      JR           NZ,$6EDF
6E6B: 69         LD           L,C
6E6C: 6D         LD           L,L
6E6D: 69         LD           L,C
6E6E: 6E         LD           L,(HL)
6E6F: 67         LD           H,A
6E70: 21 20 47   LD           HL,$4720
6E73: 6F         LD           L,A
6E74: 20 6F      JR           NZ,$6EE5
6E76: 76         HALT
6E77: 65         LD           H,L
6E78: 72         LD           (HL),D
6E79: 20 74      JR           NZ,$6EEF
6E7B: 6F         LD           L,A
6E7C: 20 74      JR           NZ,$6EF2
6E7E: 68         LD           L,B
6E7F: 65         LD           H,L
6E80: 20 20      JR           NZ,$6EA2
6E82: 62         LD           H,D
6E83: 75         LD           (HL),L
6E84: 74         LD           (HL),H
6E85: 74         LD           (HL),H
6E86: 6F         LD           L,A
6E87: 6E         LD           L,(HL)
6E88: 73         LD           (HL),E
6E89: 20 74      JR           NZ,$6EFF
6E8B: 6F         LD           L,A
6E8C: 20 70      JR           NZ,$6EFE
6E8E: 6C         LD           L,H
6E8F: 61         LD           H,C
6E90: 79         LD           A,C
6E91: 21 47 6F   LD           HL,$6F47
6E94: 6F         LD           L,A
6E95: 64         LD           H,H
6E96: 20 4C      JR           NZ,$6EE4
6E98: 75         LD           (HL),L
6E99: 63         LD           H,E
6E9A: 6B         LD           L,E
6E9B: 21 FF 49   LD           HL,$49FF
6E9E: 74         LD           (HL),H
6E9F: 5E         LD           E,(HL)
6EA0: 73         LD           (HL),E
6EA1: 20 61      JR           NZ,$6F04
6EA3: 20 53      JR           NZ,$6EF8
6EA5: 68         LD           L,B
6EA6: 69         LD           L,C
6EA7: 65         LD           H,L
6EA8: 6C         LD           L,H
6EA9: 64         LD           H,H
6EAA: 21 20 20   LD           HL,$2020
6EAD: 54         LD           D,H
6EAE: 68         LD           L,B
6EAF: 65         LD           H,L
6EB0: 72         LD           (HL),D
6EB1: 65         LD           H,L
6EB2: 20 69      JR           NZ,$6F1D
6EB4: 73         LD           (HL),E
6EB5: 20 73      JR           NZ,$6F2A
6EB7: 70         LD           (HL),B
6EB8: 61         LD           H,C
6EB9: 63         LD           H,E
6EBA: 65         LD           H,L
6EBB: 20 20      JR           NZ,$6EDD
6EBD: 66         LD           H,(HL)
6EBE: 6F         LD           L,A
6EBF: 72         LD           (HL),D
6EC0: 20 79      JR           NZ,$6F3B
6EC2: 6F         LD           L,A
6EC3: 75         LD           (HL),L
6EC4: 72         LD           (HL),D
6EC5: 20 6E      JR           NZ,$6F35
6EC7: 61         LD           H,C
6EC8: 6D         LD           L,L
6EC9: 65         LD           H,L
6ECA: 21 FF 43   LD           HL,$43FF
6ECD: 68         LD           L,B
6ECE: 61         LD           H,C
6ECF: 6C         LD           L,H
6ED0: 6C         LD           L,H
6ED1: 65         LD           H,L
6ED2: 6E         LD           L,(HL)
6ED3: 67         LD           H,A
6ED4: 65         LD           H,L
6ED5: 20 41      JR           NZ,$6F18
6ED7: 67         LD           H,A
6ED8: 61         LD           H,C
6ED9: 69         LD           L,C
6EDA: 6E         LD           L,(HL)
6EDB: 3F         CCF
6EDC: 20 20      JR           NZ,$6EFE
6EDE: 20 20      JR           NZ,$6F00
6EE0: 50         LD           D,B
6EE1: 6C         LD           L,H
6EE2: 61         LD           H,C
6EE3: 79         LD           A,C
6EE4: 20 4E      JR           NZ,$6F34
6EE6: 6F         LD           L,A
6EE7: FE 47      CP           $47
6EE9: 6F         LD           L,A
6EEA: 6F         LD           L,A
6EEB: 64         LD           H,H
6EEC: 20 4C      JR           NZ,$6F3A
6EEE: 75         LD           (HL),L
6EEF: 63         LD           H,E
6EF0: 6B         LD           L,E
6EF1: 21 FF 57   LD           HL,$57FF
6EF4: 65         LD           H,L
6EF5: 5E         LD           E,(HL)
6EF6: 72         LD           (HL),D
6EF7: 65         LD           H,L
6EF8: 20 63      JR           NZ,$6F5D
6EFA: 6C         LD           L,H
6EFB: 6F         LD           L,A
6EFC: 73         LD           (HL),E
6EFD: 69         LD           L,C
6EFE: 6E         LD           L,(HL)
6EFF: 67         LD           H,A
6F00: 20 75      JR           NZ,$6F77
6F02: 70         LD           (HL),B
6F03: 66         LD           H,(HL)
6F04: 6F         LD           L,A
6F05: 72         LD           (HL),D
6F06: 20 74      JR           NZ,$6F7C
6F08: 6F         LD           L,A
6F09: 64         LD           H,H
6F0A: 61         LD           H,C
6F0B: 79         LD           A,C
6F0C: 21 20 20   LD           HL,$2020
6F0F: 43         LD           B,E
6F10: 6F         LD           L,A
6F11: 6D         LD           L,L
6F12: 65         LD           H,L
6F13: 61         LD           H,C
6F14: 67         LD           H,A
6F15: 61         LD           H,C
6F16: 69         LD           L,C
6F17: 6E         LD           L,(HL)
6F18: 2C         INC         L
6F19: 20 61      JR           NZ,$6F7C
6F1B: 6E         LD           L,(HL)
6F1C: 79         LD           A,C
6F1D: 74         LD           (HL),H
6F1E: 69         LD           L,C
6F1F: 6D         LD           L,L
6F20: 65         LD           H,L
6F21: 21 FF 59   LD           HL,$59FF
6F24: 6F         LD           L,A
6F25: 75         LD           (HL),L
6F26: 20 67      JR           NZ,$6F8F
6F28: 6F         LD           L,A
6F29: 74         LD           (HL),H
6F2A: 20 73      JR           NZ,$6F9F
6F2C: 6F         LD           L,A
6F2D: 6D         LD           L,L
6F2E: 65         LD           H,L
6F2F: 20 20      JR           NZ,$6F51
6F31: 20 20      JR           NZ,$6F53
6F33: 4D         LD           C,L
6F34: 61         LD           H,C
6F35: 67         LD           H,A
6F36: 69         LD           L,C
6F37: 63         LD           H,E
6F38: 20 50      JR           NZ,$6F8A
6F3A: 6F         LD           L,A
6F3B: 77         LD           (HL),A
6F3C: 64         LD           H,H
6F3D: 65         LD           H,L
6F3E: 72         LD           (HL),D
6F3F: 21 20 20   LD           HL,$2020
6F42: 20 54      JR           NZ,$6F98
6F44: 72         LD           (HL),D
6F45: 79         LD           A,C
6F46: 20 74      JR           NZ,$6FBC
6F48: 6F         LD           L,A
6F49: 20 73      JR           NZ,$6FBE
6F4B: 70         LD           (HL),B
6F4C: 72         LD           (HL),D
6F4D: 69         LD           L,C
6F4E: 6E         LD           L,(HL)
6F4F: 6B         LD           L,E
6F50: 6C         LD           L,H
6F51: 65         LD           H,L
6F52: 20 69      JR           NZ,$6FBD
6F54: 74         LD           (HL),H
6F55: 20 6F      JR           NZ,$6FC6
6F57: 6E         LD           L,(HL)
6F58: 20 6D      JR           NZ,$6FC7
6F5A: 61         LD           H,C
6F5B: 6E         LD           L,(HL)
6F5C: 79         LD           A,C
6F5D: 20 20      JR           NZ,$6F7F
6F5F: 20 20      JR           NZ,$6F81
6F61: 20 20      JR           NZ,$6F83
6F63: 74         LD           (HL),H
6F64: 68         LD           L,B
6F65: 69         LD           L,C
6F66: 6E         LD           L,(HL)
6F67: 67         LD           H,A
6F68: 73         LD           (HL),E
6F69: 21 FF 49   LD           HL,$49FF
6F6C: 74         LD           (HL),H
6F6D: 5E         LD           E,(HL)
6F6E: 73         LD           (HL),E
6F6F: 20 33      JR           NZ,$6FA4
6F71: 30 20      JR           NC,$6F93
6F73: 52         LD           D,D
6F74: 75         LD           (HL),L
6F75: 70         LD           (HL),B
6F76: 65         LD           H,L
6F77: 65         LD           H,L
6F78: 73         LD           (HL),E
6F79: 21 20 59   LD           HL,$5920
6F7C: 6F         LD           L,A
6F7D: 75         LD           (HL),L
6F7E: 20 63      JR           NZ,$6FE3
6F80: 61         LD           H,C
6F81: 6E         LD           L,(HL)
6F82: 20 70      JR           NZ,$6FF4
6F84: 6C         LD           L,H
6F85: 61         LD           H,C
6F86: 79         LD           A,C
6F87: 20 74      JR           NZ,$6FFD
6F89: 68         LD           L,B
6F8A: 65         LD           H,L
6F8B: 67         LD           H,A
6F8C: 61         LD           H,C
6F8D: 6D         LD           L,L
6F8E: 65         LD           H,L
6F8F: 20 74      JR           NZ,$7005
6F91: 68         LD           L,B
6F92: 72         LD           (HL),D
6F93: 65         LD           H,L
6F94: 65         LD           H,L
6F95: 20 6D      JR           NZ,$7004
6F97: 6F         LD           L,A
6F98: 72         LD           (HL),D
6F99: 65         LD           H,L
6F9A: 20 74      JR           NZ,$7010
6F9C: 69         LD           L,C
6F9D: 6D         LD           L,L
6F9E: 65         LD           H,L
6F9F: 73         LD           (HL),E
6FA0: 20 77      JR           NZ,$7019
6FA2: 69         LD           L,C
6FA3: 74         LD           (HL),H
6FA4: 68         LD           L,B
6FA5: 20 74      JR           NZ,$701B
6FA7: 68         LD           L,B
6FA8: 69         LD           L,C
6FA9: 73         LD           (HL),E
6FAA: 21 FF 43   LD           HL,$43FF
6FAD: 6F         LD           L,A
6FAE: 75         LD           (HL),L
6FAF: 67         LD           H,A
6FB0: 68         LD           L,B
6FB1: 20 43      JR           NZ,$6FF6
6FB3: 6F         LD           L,A
6FB4: 75         LD           (HL),L
6FB5: 67         LD           H,A
6FB6: 68         LD           L,B
6FB7: 2E 2E      LD           L,$2E
6FB9: 2E 20      LD           L,$20
6FBB: 20 44      JR           NZ,$7001
6FBD: 6F         LD           L,A
6FBE: 6E         LD           L,(HL)
6FBF: 5E         LD           E,(HL)
6FC0: 74         LD           (HL),H
6FC1: 20 73      JR           NZ,$7036
6FC3: 70         LD           (HL),B
6FC4: 72         LD           (HL),D
6FC5: 69         LD           L,C
6FC6: 6E         LD           L,(HL)
6FC7: 6B         LD           L,E
6FC8: 6C         LD           L,H
6FC9: 65         LD           H,L
6FCA: 20 20      JR           NZ,$6FEC
6FCC: 74         LD           (HL),H
6FCD: 68         LD           L,B
6FCE: 61         LD           H,C
6FCF: 74         LD           (HL),H
6FD0: 20 6F      JR           NZ,$7041
6FD2: 6E         LD           L,(HL)
6FD3: 20 6D      JR           NZ,$7042
6FD5: 65         LD           H,L
6FD6: 2E 2E      LD           L,$2E
6FD8: 2E 20      LD           L,$20
6FDA: 20 20      JR           NZ,$6FFC
6FDC: 2E 2E      LD           L,$2E
6FDE: 2E 49      LD           L,$49
6FE0: 5E         LD           E,(HL)
6FE1: 6C         LD           L,H
6FE2: 6C         LD           L,H
6FE3: 20 68      JR           NZ,$704D
6FE5: 61         LD           H,C
6FE6: 76         HALT
6FE7: 65         LD           H,L
6FE8: 20 74      JR           NZ,$705E
6FEA: 6F         LD           L,A
6FEB: 20 63      JR           NZ,$7050
6FED: 75         LD           (HL),L
6FEE: 72         LD           (HL),D
6FEF: 73         LD           (HL),E
6FF0: 65         LD           H,L
6FF1: 20 79      JR           NZ,$706C
6FF3: 6F         LD           L,A
6FF4: 75         LD           (HL),L
6FF5: 21 20 20   LD           HL,$2020
6FF8: 20 20      JR           NZ,$701A
6FFA: 20 20      JR           NZ,$701C
6FFC: 43         LD           B,E
6FFD: 6F         LD           L,A
6FFE: 75         LD           (HL),L
6FFF: 67         LD           H,A
7000: 68         LD           L,B
7001: 20 43      JR           NZ,$7046
7003: 6F         LD           L,A
7004: 75         LD           (HL),L
7005: 67         LD           H,A
7006: 68         LD           L,B
7007: 2E 2E      LD           L,$2E
7009: 2E FF      LD           L,$FF
700B: 59         LD           E,C
700C: 6F         LD           L,A
700D: 75         LD           (HL),L
700E: 20 67      JR           NZ,$7077
7010: 6F         LD           L,A
7011: 74         LD           (HL),H
7012: 20 61      JR           NZ,$7075
7014: 20 59      JR           NZ,$706F
7016: 6F         LD           L,A
7017: 73         LD           (HL),E
7018: 68         LD           L,B
7019: 69         LD           L,C
701A: 20 44      JR           NZ,$7060
701C: 6F         LD           L,A
701D: 6C         LD           L,H
701E: 6C         LD           L,H
701F: 21 20 20   LD           HL,$2020
7022: 52         LD           D,D
7023: 65         LD           H,L
7024: 63         LD           H,E
7025: 65         LD           H,L
7026: 6E         LD           L,(HL)
7027: 74         LD           (HL),H
7028: 6C         LD           L,H
7029: 79         LD           A,C
702A: 2C         INC         L
702B: 68         LD           L,B
702C: 65         LD           H,L
702D: 20 73      JR           NZ,$70A2
702F: 65         LD           H,L
7030: 65         LD           H,L
7031: 6D         LD           L,L
7032: 73         LD           (HL),E
7033: 20 74      JR           NZ,$70A9
7035: 6F         LD           L,A
7036: 20 62      JR           NZ,$709A
7038: 65         LD           H,L
7039: 20 20      JR           NZ,$705B
703B: 73         LD           (HL),E
703C: 68         LD           L,B
703D: 6F         LD           L,A
703E: 77         LD           (HL),A
703F: 69         LD           L,C
7040: 6E         LD           L,(HL)
7041: 67         LD           H,A
7042: 20 75      JR           NZ,$70B9
7044: 70         LD           (HL),B
7045: 20 69      JR           NZ,$70B0
7047: 6E         LD           L,(HL)
7048: 20 20      JR           NZ,$706A
704A: 20 6D      JR           NZ,$70B9
704C: 61         LD           H,C
704D: 6E         LD           L,(HL)
704E: 79         LD           A,C
704F: 20 67      JR           NZ,$70B8
7051: 61         LD           H,C
7052: 6D         LD           L,L
7053: 65         LD           H,L
7054: 73         LD           (HL),E
7055: 21 FF 48   LD           HL,$48FF
7058: 6F         LD           L,A
7059: 77         LD           (HL),A
705A: 20 61      JR           NZ,$70BD
705C: 62         LD           H,D
705D: 6F         LD           L,A
705E: 75         LD           (HL),L
705F: 74         LD           (HL),H
7060: 20 73      JR           NZ,$70D5
7062: 6F         LD           L,A
7063: 6D         LD           L,L
7064: 65         LD           H,L
7065: 20 20      JR           NZ,$7087
7067: 66         LD           H,(HL)
7068: 69         LD           L,C
7069: 73         LD           (HL),E
706A: 68         LD           L,B
706B: 69         LD           L,C
706C: 6E         LD           L,(HL)
706D: 67         LD           H,A
706E: 2C         INC         L
706F: 20 6C      JR           NZ,$70DD
7071: 69         LD           L,C
7072: 74         LD           (HL),H
7073: 74         LD           (HL),H
7074: 6C         LD           L,H
7075: 65         LD           H,L
7076: 20 62      JR           NZ,$70DA
7078: 75         LD           (HL),L
7079: 64         LD           H,H
707A: 64         LD           H,H
707B: 79         LD           A,C
707C: 3F         CCF
707D: 20 49      JR           NZ,$70C8
707F: 5E         LD           E,(HL)
7080: 6C         LD           L,H
7081: 6C         LD           L,H
7082: 20 6F      JR           NZ,$70F3
7084: 6E         LD           L,(HL)
7085: 6C         LD           L,H
7086: 79         LD           A,C
7087: 63         LD           H,E
7088: 68         LD           L,B
7089: 61         LD           H,C
708A: 72         LD           (HL),D
708B: 67         LD           H,A
708C: 65         LD           H,L
708D: 20 79      JR           NZ,$7108
708F: 6F         LD           L,A
7090: 75         LD           (HL),L
7091: 20 31      JR           NZ,$70C4
7093: 30 20      JR           NC,$70B5
7095: 20 20      JR           NZ,$70B7
7097: 52         LD           D,D
7098: 75         LD           (HL),L
7099: 70         LD           (HL),B
709A: 65         LD           H,L
709B: 65         LD           H,L
709C: 73         LD           (HL),E
709D: 2E 2E      LD           L,$2E
709F: 2E 20      LD           L,$20
70A1: 20 20      JR           NZ,$70C3
70A3: 20 20      JR           NZ,$70C5
70A5: 20 20      JR           NZ,$70C7
70A7: 20 20      JR           NZ,$70C9
70A9: 20 20      JR           NZ,$70CB
70AB: 46         LD           B,(HL)
70AC: 69         LD           L,C
70AD: 73         LD           (HL),E
70AE: 68         LD           L,B
70AF: 20 4E      JR           NZ,$70FF
70B1: 6F         LD           L,A
70B2: 74         LD           (HL),H
70B3: 20 4E      JR           NZ,$7103
70B5: 6F         LD           L,A
70B6: 77         LD           (HL),A
70B7: FE 59      CP           $59
70B9: 6F         LD           L,A
70BA: 75         LD           (HL),L
70BB: 20 68      JR           NZ,$7125
70BD: 61         LD           H,C
70BE: 76         HALT
70BF: 65         LD           H,L
70C0: 20 74      JR           NZ,$7136
70C2: 6F         LD           L,A
70C3: 20 68      JR           NZ,$712D
70C5: 61         LD           H,C
70C6: 76         HALT
70C7: 65         LD           H,L
70C8: 6D         LD           L,L
70C9: 6F         LD           L,A
70CA: 72         LD           (HL),D
70CB: 65         LD           H,L
70CC: 20 70      JR           NZ,$713E
70CE: 61         LD           H,C
70CF: 73         LD           (HL),E
70D0: 73         LD           (HL),E
70D1: 69         LD           L,C
70D2: 6F         LD           L,A
70D3: 6E         LD           L,(HL)
70D4: 21 20 20   LD           HL,$2020
70D7: 20 4C      JR           NZ,$7125
70D9: 69         LD           L,C
70DA: 76         HALT
70DB: 65         LD           H,L
70DC: 20 61      JR           NZ,$713F
70DE: 20 6C      JR           NZ,$714C
70E0: 69         LD           L,C
70E1: 74         LD           (HL),H
70E2: 74         LD           (HL),H
70E3: 6C         LD           L,H
70E4: 65         LD           H,L
70E5: 21 FF 4F   LD           HL,$4FFF
70E8: 6B         LD           L,E
70E9: 61         LD           H,C
70EA: 79         LD           A,C
70EB: 2C         INC         L
70EC: 20 68      JR           NZ,$7156
70EE: 65         LD           H,L
70EF: 72         LD           (HL),D
70F0: 65         LD           H,L
70F1: 5E         LD           E,(HL)
70F2: 73         LD           (HL),E
70F3: 20 68      JR           NZ,$715D
70F5: 6F         LD           L,A
70F6: 77         LD           (HL),A
70F7: 79         LD           A,C
70F8: 6F         LD           L,A
70F9: 75         LD           (HL),L
70FA: 20 64      JR           NZ,$7160
70FC: 6F         LD           L,A
70FD: 20 69      JR           NZ,$7168
70FF: 74         LD           (HL),H
7100: 2E 20      LD           L,$20
7102: 20 55      JR           NZ,$7159
7104: 73         LD           (HL),E
7105: 65         LD           H,L
7106: 20 F2      JR           NZ,$70FA
7108: 20 61      JR           NZ,$716B
710A: 6E         LD           L,(HL)
710B: 64         LD           H,H
710C: 20 F3      JR           NZ,$7101
710E: 20 6F      JR           NZ,$717F
7110: 6E         LD           L,(HL)
7111: 20 74      JR           NZ,$7187
7113: 68         LD           L,B
7114: 65         LD           H,L
7115: 20 EE      JR           NZ,$7105
7117: 74         LD           (HL),H
7118: 6F         LD           L,A
7119: 20 61      JR           NZ,$717C
711B: 69         LD           L,C
711C: 6D         LD           L,L
711D: 20 61      JR           NZ,$7180
711F: 20 63      JR           NZ,$7184
7121: 61         LD           H,C
7122: 73         LD           (HL),E
7123: 74         LD           (HL),H
7124: 2E 20      LD           L,$20
7126: 20 4F      JR           NZ,$7177
7128: 6E         LD           L,(HL)
7129: 63         LD           H,E
712A: 65         LD           H,L
712B: 20 79      JR           NZ,$71A6
712D: 6F         LD           L,A
712E: 75         LD           (HL),L
712F: 20 68      JR           NZ,$7199
7131: 6F         LD           L,A
7132: 6F         LD           L,A
7133: 6B         LD           L,E
7134: 20 61      JR           NZ,$7197
7136: 20 66      JR           NZ,$719E
7138: 69         LD           L,C
7139: 73         LD           (HL),E
713A: 68         LD           L,B
713B: 2C         INC         L
713C: 20 70      JR           NZ,$71AE
713E: 72         LD           (HL),D
713F: 65         LD           H,L
7140: 73         LD           (HL),E
7141: 73         LD           (HL),E
7142: 20 74      JR           NZ,$71B8
7144: 68         LD           L,B
7145: 65         LD           H,L
7146: 20 42      JR           NZ,$718A
7148: 75         LD           (HL),L
7149: 74         LD           (HL),H
714A: 74         LD           (HL),H
714B: 6F         LD           L,A
714C: 6E         LD           L,(HL)
714D: 20 72      JR           NZ,$71C1
714F: 61         LD           H,C
7150: 70         LD           (HL),B
7151: 69         LD           L,C
7152: 64         LD           H,H
7153: 6C         LD           L,H
7154: 79         LD           A,C
7155: 20 20      JR           NZ,$7177
7157: 74         LD           (HL),H
7158: 6F         LD           L,A
7159: 20 72      JR           NZ,$71CD
715B: 65         LD           H,L
715C: 65         LD           H,L
715D: 6C         LD           L,H
715E: 20 68      JR           NZ,$71C8
7160: 69         LD           L,C
7161: 6D         LD           L,L
7162: 20 69      JR           NZ,$71CD
7164: 6E         LD           L,(HL)
7165: 21 FF 57   LD           HL,$57FF
7168: 68         LD           L,B
7169: 79         LD           A,C
716A: 20 6E      JR           NZ,$71DA
716C: 6F         LD           L,A
716D: 74         LD           (HL),H
716E: 20 74      JR           NZ,$71E4
7170: 72         LD           (HL),D
7171: 79         LD           A,C
7172: 20 6F      JR           NZ,$71E3
7174: 6E         LD           L,(HL)
7175: 65         LD           H,L
7176: 20 6D      JR           NZ,$71E5
7178: 6F         LD           L,A
7179: 72         LD           (HL),D
717A: 65         LD           H,L
717B: 20 74      JR           NZ,$71F1
717D: 69         LD           L,C
717E: 6D         LD           L,L
717F: 65         LD           H,L
7180: 2C         INC         L
7181: 20 20      JR           NZ,$71A3
7183: 20 20      JR           NZ,$71A5
7185: 20 20      JR           NZ,$71A7
7187: 6C         LD           L,H
7188: 69         LD           L,C
7189: 74         LD           (HL),H
718A: 74         LD           (HL),H
718B: 6C         LD           L,H
718C: 65         LD           H,L
718D: 20 62      JR           NZ,$71F1
718F: 75         LD           (HL),L
7190: 64         LD           H,H
7191: 64         LD           H,H
7192: 79         LD           A,C
7193: 3F         CCF
7194: 20 20      JR           NZ,$71B6
7196: 20 20      JR           NZ,$71B8
7198: 20 20      JR           NZ,$71BA
719A: 20 43      JR           NZ,$71DF
719C: 61         LD           H,C
719D: 73         LD           (HL),E
719E: 74         LD           (HL),H
719F: 20 4E      JR           NZ,$71EF
71A1: 6F         LD           L,A
71A2: 74         LD           (HL),H
71A3: 20 4E      JR           NZ,$71F3
71A5: 6F         LD           L,A
71A6: 77         LD           (HL),A
71A7: FE 57      CP           $57
71A9: 6F         LD           L,A
71AA: 77         LD           (HL),A
71AB: 21 20 54   LD           HL,$5420
71AE: 68         LD           L,B
71AF: 61         LD           H,C
71B0: 74         LD           (HL),H
71B1: 20 6F      JR           NZ,$7222
71B3: 6E         LD           L,(HL)
71B4: 65         LD           H,L
71B5: 20 20      JR           NZ,$71D7
71B7: 20 67      JR           NZ,$7220
71B9: 6F         LD           L,A
71BA: 74         LD           (HL),H
71BB: 20 61      JR           NZ,$721E
71BD: 77         LD           (HL),A
71BE: 61         LD           H,C
71BF: 79         LD           A,C
71C0: 21 20 20   LD           HL,$2020
71C3: 57         LD           D,A
71C4: 61         LD           H,C
71C5: 6E         LD           L,(HL)
71C6: 74         LD           (HL),H
71C7: 20 74      JR           NZ,$723D
71C9: 6F         LD           L,A
71CA: 20 74      JR           NZ,$7240
71CC: 72         LD           (HL),D
71CD: 79         LD           A,C
71CE: 20 61      JR           NZ,$7231
71D0: 67         LD           H,A
71D1: 61         LD           H,C
71D2: 69         LD           L,C
71D3: 6E         LD           L,(HL)
71D4: 3F         CCF
71D5: 20 20      JR           NZ,$71F7
71D7: 20 20      JR           NZ,$71F9
71D9: 20 20      JR           NZ,$71FB
71DB: 20 43      JR           NZ,$7220
71DD: 61         LD           H,C
71DE: 73         LD           (HL),E
71DF: 74         LD           (HL),H
71E0: 20 4E      JR           NZ,$7230
71E2: 6F         LD           L,A
71E3: 74         LD           (HL),H
71E4: 20 4E      JR           NZ,$7234
71E6: 6F         LD           L,A
71E7: 77         LD           (HL),A
71E8: FE 57      CP           $57
71EA: 6F         LD           L,A
71EB: 77         LD           (HL),A
71EC: 21 20 4E   LD           HL,$4E20
71EF: 69         LD           L,C
71F0: 63         LD           H,E
71F1: 65         LD           H,L
71F2: 20 46      JR           NZ,$723A
71F4: 69         LD           L,C
71F5: 73         LD           (HL),E
71F6: 68         LD           L,B
71F7: 21 20 49   LD           HL,$4920
71FA: 74         LD           (HL),H
71FB: 5E         LD           E,(HL)
71FC: 73         LD           (HL),E
71FD: 20 61      JR           NZ,$7260
71FF: 20 6C      JR           NZ,$726D
7201: 75         LD           (HL),L
7202: 6E         LD           L,(HL)
7203: 6B         LD           L,E
7204: 65         LD           H,L
7205: 72         LD           (HL),D
7206: 21 21 20   LD           HL,$2021
7209: 49         LD           C,C
720A: 5E         LD           E,(HL)
720B: 6C         LD           L,H
720C: 6C         LD           L,H
720D: 20 67      JR           NZ,$7276
720F: 69         LD           L,C
7210: 76         HALT
7211: 65         LD           H,L
7212: 20 79      JR           NZ,$728D
7214: 6F         LD           L,A
7215: 75         LD           (HL),L
7216: 20 61      JR           NZ,$7279
7218: 20 32      JR           NZ,$724C
721A: 30 20      JR           NC,$723C
721C: 52         LD           D,D
721D: 75         LD           (HL),L
721E: 70         LD           (HL),B
721F: 65         LD           H,L
7220: 65         LD           H,L
7221: 20 70      JR           NZ,$7293
7223: 72         LD           (HL),D
7224: 69         LD           L,C
7225: 7A         LD           A,D
7226: 65         LD           H,L
7227: 21 20 54   LD           HL,$5420
722A: 72         LD           (HL),D
722B: 79         LD           A,C
722C: 20 61      JR           NZ,$728F
722E: 67         LD           H,A
722F: 61         LD           H,C
7230: 69         LD           L,C
7231: 6E         LD           L,(HL)
7232: 3F         CCF
7233: 20 20      JR           NZ,$7255
7235: 20 20      JR           NZ,$7257
7237: 20 20      JR           NZ,$7259
7239: 20 20      JR           NZ,$725B
723B: 20 20      JR           NZ,$725D
723D: 43         LD           B,E
723E: 61         LD           H,C
723F: 73         LD           (HL),E
7240: 74         LD           (HL),H
7241: 20 4E      JR           NZ,$7291
7243: 6F         LD           L,A
7244: 74         LD           (HL),H
7245: 20 4E      JR           NZ,$7295
7247: 6F         LD           L,A
7248: 77         LD           (HL),A
7249: FE 54      CP           $54
724B: 68         LD           L,B
724C: 69         LD           L,C
724D: 73         LD           (HL),E
724E: 20 70      JR           NZ,$72C0
7250: 6F         LD           L,A
7251: 6E         LD           L,(HL)
7252: 64         LD           H,H
7253: 5E         LD           E,(HL)
7254: 73         LD           (HL),E
7255: 20 61      JR           NZ,$72B8
7257: 6C         LD           L,H
7258: 6C         LD           L,H
7259: 20 66      JR           NZ,$72C1
725B: 69         LD           L,C
725C: 73         LD           (HL),E
725D: 68         LD           L,B
725E: 65         LD           H,L
725F: 64         LD           H,H
7260: 20 6F      JR           NZ,$72D1
7262: 75         LD           (HL),L
7263: 74         LD           (HL),H
7264: 2E 20      LD           L,$20
7266: 20 57      JR           NZ,$72BF
7268: 68         LD           L,B
7269: 79         LD           A,C
726A: 6E         LD           L,(HL)
726B: 6F         LD           L,A
726C: 74         LD           (HL),H
726D: 20 74      JR           NZ,$72E3
726F: 72         LD           (HL),D
7270: 79         LD           A,C
7271: 20 79      JR           NZ,$72EC
7273: 6F         LD           L,A
7274: 75         LD           (HL),L
7275: 72         LD           (HL),D
7276: 20 20      JR           NZ,$7298
7278: 20 20      JR           NZ,$729A
727A: 6C         LD           L,H
727B: 75         LD           (HL),L
727C: 63         LD           H,E
727D: 6B         LD           L,E
727E: 20 69      JR           NZ,$72E9
7280: 6E         LD           L,(HL)
7281: 20 74      JR           NZ,$72F7
7283: 68         LD           L,B
7284: 65         LD           H,L
7285: 20 73      JR           NZ,$72FA
7287: 65         LD           H,L
7288: 61         LD           H,C
7289: 3F         CCF
728A: 20 20      JR           NZ,$72AC
728C: 20 20      JR           NZ,$72AE
728E: 4F         LD           C,A
728F: 6B         LD           L,E
7290: 61         LD           H,C
7291: 79         LD           A,C
7292: 20 4E      JR           NZ,$72E2
7294: 6F         LD           L,A
7295: FE 44      CP           $44
7297: 69         LD           L,C
7298: 64         LD           H,H
7299: 20 49      JR           NZ,$72E4
729B: 20 73      JR           NZ,$7310
729D: 61         LD           H,C
729E: 79         LD           A,C
729F: 20 74      JR           NZ,$7315
72A1: 68         LD           L,B
72A2: 61         LD           H,C
72A3: 74         LD           (HL),H
72A4: 3F         CCF
72A5: 20 46      JR           NZ,$72ED
72A7: 6F         LD           L,A
72A8: 72         LD           (HL),D
72A9: 67         LD           H,A
72AA: 65         LD           H,L
72AB: 74         LD           (HL),H
72AC: 20 69      JR           NZ,$7317
72AE: 74         LD           (HL),H
72AF: 2C         INC         L
72B0: 20 6F      JR           NZ,$7321
72B2: 6B         LD           L,E
72B3: 61         LD           H,C
72B4: 79         LD           A,C
72B5: 3F         CCF
72B6: 52         LD           D,D
72B7: 75         LD           (HL),L
72B8: 6E         LD           L,(HL)
72B9: 20 61      JR           NZ,$731C
72BB: 6C         LD           L,H
72BC: 6F         LD           L,A
72BD: 6E         LD           L,(HL)
72BE: 67         LD           H,A
72BF: 20 6E      JR           NZ,$732F
72C1: 6F         LD           L,A
72C2: 77         LD           (HL),A
72C3: 2E 2E      LD           L,$2E
72C5: 2E FF      LD           L,$FF
72C7: 49         LD           C,C
72C8: 74         LD           (HL),H
72C9: 5E         LD           E,(HL)
72CA: 73         LD           (HL),E
72CB: 20 61      JR           NZ,$732E
72CD: 20 72      JR           NZ,$7341
72CF: 75         LD           (HL),L
72D0: 6E         LD           L,(HL)
72D1: 74         LD           (HL),H
72D2: 21 20 20   LD           HL,$2020
72D5: 20 20      JR           NZ,$72F7
72D7: 49         LD           C,C
72D8: 5E         LD           E,(HL)
72D9: 6C         LD           L,H
72DA: 6C         LD           L,H
72DB: 20 6F      JR           NZ,$734C
72DD: 6E         LD           L,(HL)
72DE: 6C         LD           L,H
72DF: 79         LD           A,C
72E0: 20 67      JR           NZ,$7349
72E2: 69         LD           L,C
72E3: 76         HALT
72E4: 65         LD           H,L
72E5: 20 20      JR           NZ,$7307
72E7: 79         LD           A,C
72E8: 6F         LD           L,A
72E9: 75         LD           (HL),L
72EA: 20 61      JR           NZ,$734D
72EC: 20 35      JR           NZ,$7323
72EE: 20 52      JR           NZ,$7342
72F0: 75         LD           (HL),L
72F1: 70         LD           (HL),B
72F2: 65         LD           H,L
72F3: 65         LD           H,L
72F4: 73         LD           (HL),E
72F5: 20 20      JR           NZ,$7317
72F7: 70         LD           (HL),B
72F8: 72         LD           (HL),D
72F9: 69         LD           L,C
72FA: 7A         LD           A,D
72FB: 65         LD           H,L
72FC: 20 66      JR           NZ,$7364
72FE: 6F         LD           L,A
72FF: 72         LD           (HL),D
7300: 20 74      JR           NZ,$7376
7302: 68         LD           L,B
7303: 61         LD           H,C
7304: 74         LD           (HL),H
7305: 2E 20      LD           L,$20
7307: 59         LD           E,C
7308: 6F         LD           L,A
7309: 75         LD           (HL),L
730A: 20 73      JR           NZ,$737F
730C: 68         LD           L,B
730D: 6F         LD           L,A
730E: 75         LD           (HL),L
730F: 6C         LD           L,H
7310: 64         LD           H,H
7311: 20 74      JR           NZ,$7387
7313: 72         LD           (HL),D
7314: 79         LD           A,C
7315: 20 20      JR           NZ,$7337
7317: 61         LD           H,C
7318: 67         LD           H,A
7319: 61         LD           H,C
731A: 69         LD           L,C
731B: 6E         LD           L,(HL)
731C: 21 20 20   LD           HL,$2020
731F: 20 20      JR           NZ,$7341
7321: 20 20      JR           NZ,$7343
7323: 20 20      JR           NZ,$7345
7325: 20 20      JR           NZ,$7347
7327: 20 20      JR           NZ,$7349
7329: 20 20      JR           NZ,$734B
732B: 4F         LD           C,A
732C: 6B         LD           L,E
732D: 61         LD           H,C
732E: 79         LD           A,C
732F: 20 4E      JR           NZ,$737F
7331: 6F         LD           L,A
7332: FE 59      CP           $59
7334: 6F         LD           L,A
7335: 75         LD           (HL),L
7336: 5E         LD           E,(HL)
7337: 72         LD           (HL),D
7338: 65         LD           H,L
7339: 20 73      JR           NZ,$73AE
733B: 68         LD           L,B
733C: 6F         LD           L,A
733D: 72         LD           (HL),D
733E: 74         LD           (HL),H
733F: 20 6F      JR           NZ,$73B0
7341: 66         LD           H,(HL)
7342: 20 52      JR           NZ,$7396
7344: 75         LD           (HL),L
7345: 70         LD           (HL),B
7346: 65         LD           H,L
7347: 65         LD           H,L
7348: 73         LD           (HL),E
7349: 3F         CCF
734A: 20 20      JR           NZ,$736C
734C: 44         LD           B,H
734D: 6F         LD           L,A
734E: 6E         LD           L,(HL)
734F: 5E         LD           E,(HL)
7350: 74         LD           (HL),H
7351: 20 20      JR           NZ,$7373
7353: 77         LD           (HL),A
7354: 6F         LD           L,A
7355: 72         LD           (HL),D
7356: 72         LD           (HL),D
7357: 79         LD           A,C
7358: 20 61      JR           NZ,$73BB
735A: 62         LD           H,D
735B: 6F         LD           L,A
735C: 75         LD           (HL),L
735D: 74         LD           (HL),H
735E: 20 69      JR           NZ,$73C9
7360: 74         LD           (HL),H
7361: 2E 20      LD           L,$20
7363: 59         LD           E,C
7364: 6F         LD           L,A
7365: 75         LD           (HL),L
7366: 20 6A      JR           NZ,$73D2
7368: 75         LD           (HL),L
7369: 73         LD           (HL),E
736A: 74         LD           (HL),H
736B: 20 63      JR           NZ,$73D0
736D: 6F         LD           L,A
736E: 6D         LD           L,L
736F: 65         LD           H,L
7370: 20 20      JR           NZ,$7392
7372: 20 62      JR           NZ,$73D6
7374: 61         LD           H,C
7375: 63         LD           H,E
7376: 6B         LD           L,E
7377: 20 77      JR           NZ,$73F0
7379: 68         LD           L,B
737A: 65         LD           H,L
737B: 6E         LD           L,(HL)
737C: 20 79      JR           NZ,$73F7
737E: 6F         LD           L,A
737F: 75         LD           (HL),L
7380: 20 20      JR           NZ,$73A2
7382: 20 68      JR           NZ,$73EC
7384: 61         LD           H,C
7385: 76         HALT
7386: 65         LD           H,L
7387: 20 6D      JR           NZ,$73F6
7389: 6F         LD           L,A
738A: 72         LD           (HL),D
738B: 65         LD           H,L
738C: 20 6D      JR           NZ,$73FB
738E: 6F         LD           L,A
738F: 6E         LD           L,(HL)
7390: 65         LD           H,L
7391: 79         LD           A,C
7392: 2C         INC         L
7393: 6C         LD           L,H
7394: 69         LD           L,C
7395: 74         LD           (HL),H
7396: 74         LD           (HL),H
7397: 6C         LD           L,H
7398: 65         LD           H,L
7399: 20 62      JR           NZ,$73FD
739B: 75         LD           (HL),L
739C: 64         LD           H,H
739D: 64         LD           H,H
739E: 79         LD           A,C
739F: 2E FF      LD           L,$FF
73A1: 59         LD           E,C
73A2: 6F         LD           L,A
73A3: 75         LD           (HL),L
73A4: 5E         LD           E,(HL)
73A5: 76         HALT
73A6: 65         LD           H,L
73A7: 20 67      JR           NZ,$7410
73A9: 6F         LD           L,A
73AA: 74         LD           (HL),H
73AB: 20 61      JR           NZ,$740E
73AD: 20 20      JR           NZ,$73CF
73AF: 20 20      JR           NZ,$73D1
73B1: 50         LD           D,B
73B2: 69         LD           L,C
73B3: 65         LD           H,L
73B4: 63         LD           H,E
73B5: 65         LD           H,L
73B6: 20 6F      JR           NZ,$7427
73B8: 66         LD           H,(HL)
73B9: 20 48      JR           NZ,$7403
73BB: 65         LD           H,L
73BC: 61         LD           H,C
73BD: 72         LD           (HL),D
73BE: 74         LD           (HL),H
73BF: 21 20 FF   LD           HL,$FF20
73C2: 59         LD           E,C
73C3: 6F         LD           L,A
73C4: 75         LD           (HL),L
73C5: 20 63      JR           NZ,$742A
73C7: 6F         LD           L,A
73C8: 6C         LD           L,H
73C9: 6C         LD           L,H
73CA: 65         LD           H,L
73CB: 63         LD           H,E
73CC: 74         LD           (HL),H
73CD: 65         LD           H,L
73CE: 64         LD           H,H
73CF: 20 20      JR           NZ,$73F1
73D1: 20 66      JR           NZ,$7439
73D3: 6F         LD           L,A
73D4: 75         LD           (HL),L
73D5: 72         LD           (HL),D
73D6: 20 50      JR           NZ,$7428
73D8: 69         LD           L,C
73D9: 65         LD           H,L
73DA: 63         LD           H,E
73DB: 65         LD           H,L
73DC: 73         LD           (HL),E
73DD: 20 6F      JR           NZ,$744E
73DF: 66         LD           H,(HL)
73E0: 20 20      JR           NZ,$7402
73E2: 48         LD           C,B
73E3: 65         LD           H,L
73E4: 61         LD           H,C
73E5: 72         LD           (HL),D
73E6: 74         LD           (HL),H
73E7: 2E 20      LD           L,$20
73E9: 20 4E      JR           NZ,$7439
73EB: 6F         LD           L,A
73EC: 77         LD           (HL),A
73ED: 2C         INC         L
73EE: 20 79      JR           NZ,$7469
73F0: 6F         LD           L,A
73F1: 75         LD           (HL),L
73F2: 68         LD           L,B
73F3: 61         LD           H,C
73F4: 76         HALT
73F5: 65         LD           H,L
73F6: 20 61      JR           NZ,$7459
73F8: 20 63      JR           NZ,$745D
73FA: 6F         LD           L,A
73FB: 6D         LD           L,L
73FC: 70         LD           (HL),B
73FD: 6C         LD           L,H
73FE: 65         LD           H,L
73FF: 74         LD           (HL),H
7400: 65         LD           H,L
7401: 20 48      JR           NZ,$744B
7403: 65         LD           H,L
7404: 61         LD           H,C
7405: 72         LD           (HL),D
7406: 74         LD           (HL),H
7407: 20 43      JR           NZ,$744C
7409: 6F         LD           L,A
740A: 6E         LD           L,(HL)
740B: 74         LD           (HL),H
740C: 61         LD           H,C
740D: 69         LD           L,C
740E: 6E         LD           L,(HL)
740F: 65         LD           H,L
7410: 72         LD           (HL),D
7411: 21 FF 42   LD           HL,$42FF
7414: 72         LD           (HL),D
7415: 72         LD           (HL),D
7416: 72         LD           (HL),D
7417: 72         LD           (HL),D
7418: 2E 2E      LD           L,$2E
741A: 2E 20      LD           L,$20
741C: 54         LD           D,H
741D: 68         LD           L,B
741E: 69         LD           L,C
741F: 73         LD           (HL),E
7420: 20 69      JR           NZ,$748B
7422: 73         LD           (HL),E
7423: 61         LD           H,C
7424: 20 62      JR           NZ,$7488
7426: 6C         LD           L,H
7427: 6F         LD           L,A
7428: 63         LD           H,E
7429: 6B         LD           L,E
742A: 20 6F      JR           NZ,$749B
742C: 66         LD           H,(HL)
742D: 20 73      JR           NZ,$74A2
742F: 6F         LD           L,A
7430: 6C         LD           L,H
7431: 69         LD           L,C
7432: 64         LD           H,H
7433: 69         LD           L,C
7434: 63         LD           H,E
7435: 65         LD           H,L
7436: 21 20 20   LD           HL,$2020
7439: 49         LD           C,C
743A: 74         LD           (HL),H
743B: 5E         LD           E,(HL)
743C: 73         LD           (HL),E
743D: 20 76      JR           NZ,$74B5
743F: 65         LD           H,L
7440: 72         LD           (HL),D
7441: 79         LD           A,C
7442: 20 63      JR           NZ,$74A7
7444: 6F         LD           L,A
7445: 6C         LD           L,H
7446: 64         LD           H,H
7447: 21 FF 4E   LD           HL,$4EFF
744A: 59         LD           E,C
744B: 41         LD           B,C
744C: 48         LD           C,B
744D: 20 4E      JR           NZ,$749D
744F: 59         LD           E,C
7450: 41         LD           B,C
7451: 48         LD           C,B
7452: 21 20 59   LD           HL,$5920
7455: 6F         LD           L,A
7456: 75         LD           (HL),L
7457: 20 20      JR           NZ,$7479
7459: 63         LD           H,E
745A: 61         LD           H,C
745B: 6E         LD           L,(HL)
745C: 5E         LD           E,(HL)
745D: 74         LD           (HL),H
745E: 20 68      JR           NZ,$74C8
7460: 75         LD           (HL),L
7461: 72         LD           (HL),D
7462: 74         LD           (HL),H
7463: 20 6D      JR           NZ,$74D2
7465: 65         LD           H,L
7466: 20 61      JR           NZ,$74C9
7468: 73         LD           (HL),E
7469: 6C         LD           L,H
746A: 6F         LD           L,A
746B: 6E         LD           L,(HL)
746C: 67         LD           H,A
746D: 20 61      JR           NZ,$74D0
746F: 73         LD           (HL),E
7470: 20 49      JR           NZ,$74BB
7472: 20 68      JR           NZ,$74DC
7474: 61         LD           H,C
7475: 76         HALT
7476: 65         LD           H,L
7477: 20 20      JR           NZ,$7499
7479: 6D         LD           L,L
747A: 79         LD           A,C
747B: 20 62      JR           NZ,$74DF
747D: 6F         LD           L,A
747E: 74         LD           (HL),H
747F: 74         LD           (HL),H
7480: 6C         LD           L,H
7481: 65         LD           H,L
7482: 21 FF 57   LD           HL,$57FF
7485: 61         LD           H,C
7486: 61         LD           H,C
7487: 61         LD           H,C
7488: 61         LD           H,C
7489: 68         LD           L,B
748A: 21 20 59   LD           HL,$5920
748D: 6F         LD           L,A
748E: 75         LD           (HL),L
748F: 2D         DEC         L
7490: 20 79      JR           NZ,$750B
7492: 6F         LD           L,A
7493: 75         LD           (HL),L
7494: 62         LD           H,D
7495: 72         LD           (HL),D
7496: 6F         LD           L,A
7497: 6B         LD           L,E
7498: 65         LD           H,L
7499: 20 6D      JR           NZ,$7508
749B: 79         LD           A,C
749C: 20 62      JR           NZ,$7500
749E: 6F         LD           L,A
749F: 74         LD           (HL),H
74A0: 74         LD           (HL),H
74A1: 6C         LD           L,H
74A2: 65         LD           H,L
74A3: 21 57 68   LD           HL,$6857
74A6: 79         LD           A,C
74A7: 2C         INC         L
74A8: 20 79      JR           NZ,$7523
74AA: 6F         LD           L,A
74AB: 75         LD           (HL),L
74AC: 2E 2E      LD           L,$2E
74AE: 2E 20      LD           L,$20
74B0: 59         LD           E,C
74B1: 6F         LD           L,A
74B2: 75         LD           (HL),L
74B3: 20 6D      JR           NZ,$7522
74B5: 61         LD           H,C
74B6: 6B         LD           L,E
74B7: 65         LD           H,L
74B8: 20 6D      JR           NZ,$7527
74BA: 65         LD           H,L
74BB: 20 68      JR           NZ,$7525
74BD: 6F         LD           L,A
74BE: 70         LD           (HL),B
74BF: 70         LD           (HL),B
74C0: 69         LD           L,C
74C1: 6E         LD           L,(HL)
74C2: 67         LD           H,A
74C3: 20 6D      JR           NZ,$7532
74C5: 61         LD           H,C
74C6: 64         LD           H,H
74C7: 21 21 21   LD           HL,$2121
74CA: FF         RST         0X38
74CB: 57         LD           D,A
74CC: 65         LD           H,L
74CD: 6C         LD           L,H
74CE: 6C         LD           L,H
74CF: 2C         INC         L
74D0: 20 23      JR           NZ,$74F5
74D2: 23         INC         HL
74D3: 23         INC         HL
74D4: 23         INC         HL
74D5: 23         INC         HL
74D6: 2C         INC         L
74D7: 20 79      JR           NZ,$7552
74D9: 61         LD           H,C
74DA: 20 66      JR           NZ,$7542
74DC: 69         LD           L,C
74DD: 6E         LD           L,(HL)
74DE: 61         LD           H,C
74DF: 6C         LD           L,H
74E0: 6C         LD           L,H
74E1: 79         LD           A,C
74E2: 20 73      JR           NZ,$7557
74E4: 6E         LD           L,(HL)
74E5: 61         LD           H,C
74E6: 70         LD           (HL),B
74E7: 70         LD           (HL),B
74E8: 65         LD           H,L
74E9: 64         LD           H,H
74EA: 20 6F      JR           NZ,$755B
74EC: 75         LD           (HL),L
74ED: 74         LD           (HL),H
74EE: 20 6F      JR           NZ,$755F
74F0: 66         LD           H,(HL)
74F1: 20 69      JR           NZ,$755C
74F3: 74         LD           (HL),H
74F4: 2E 2E      LD           L,$2E
74F6: 2E 20      LD           L,$20
74F8: 20 20      JR           NZ,$751A
74FA: 20 4E      JR           NZ,$754A
74FC: 61         LD           H,C
74FD: 6D         LD           L,L
74FE: 65         LD           H,L
74FF: 5E         LD           E,(HL)
7500: 73         LD           (HL),E
7501: 20 54      JR           NZ,$7557
7503: 61         LD           H,C
7504: 72         LD           (HL),D
7505: 69         LD           L,C
7506: 6E         LD           L,(HL)
7507: 2E 2E      LD           L,$2E
7509: 2E 20      LD           L,$20
750B: 48         LD           C,B
750C: 6F         LD           L,A
750D: 70         LD           (HL),B
750E: 65         LD           H,L
750F: 20 79      JR           NZ,$758A
7511: 65         LD           H,L
7512: 72         LD           (HL),D
7513: 20 66      JR           NZ,$757B
7515: 65         LD           H,L
7516: 65         LD           H,L
7517: 6C         LD           L,H
7518: 69         LD           L,C
7519: 6E         LD           L,(HL)
751A: 5E         LD           E,(HL)
751B: 62         LD           H,D
751C: 65         LD           H,L
751D: 74         LD           (HL),H
751E: 74         LD           (HL),H
751F: 65         LD           H,L
7520: 72         LD           (HL),D
7521: 2E 2E      LD           L,$2E
7523: 2E 20      LD           L,$20
7525: 20 57      JR           NZ,$757E
7527: 68         LD           L,B
7528: 61         LD           H,C
7529: 74         LD           (HL),H
752A: 3F         CCF
752B: 48         LD           C,B
752C: 6F         LD           L,A
752D: 77         LD           (HL),A
752E: 20 64      JR           NZ,$7594
7530: 69         LD           L,C
7531: 64         LD           H,H
7532: 20 49      JR           NZ,$757D
7534: 20 6B      JR           NZ,$75A1
7536: 6E         LD           L,(HL)
7537: 6F         LD           L,A
7538: 77         LD           (HL),A
7539: 20 20      JR           NZ,$755B
753B: 79         LD           A,C
753C: 6F         LD           L,A
753D: 75         LD           (HL),L
753E: 72         LD           (HL),D
753F: 20 6E      JR           NZ,$75AF
7541: 61         LD           H,C
7542: 6D         LD           L,L
7543: 65         LD           H,L
7544: 3F         CCF
7545: 20 20      JR           NZ,$7567
7547: 59         LD           E,C
7548: 6F         LD           L,A
7549: 75         LD           (HL),L
754A: 20 74      JR           NZ,$75C0
754C: 68         LD           L,B
754D: 69         LD           L,C
754E: 6E         LD           L,(HL)
754F: 6B         LD           L,E
7550: 20 69      JR           NZ,$75BB
7552: 74         LD           (HL),H
7553: 5E         LD           E,(HL)
7554: 73         LD           (HL),E
7555: 20 77      JR           NZ,$75CE
7557: 65         LD           H,L
7558: 69         LD           L,C
7559: 72         LD           (HL),D
755A: 64         LD           H,H
755B: 65         LD           H,L
755C: 68         LD           L,B
755D: 3F         CCF
755E: 20 20      JR           NZ,$7580
7560: 57         LD           D,A
7561: 65         LD           H,L
7562: 6C         LD           L,H
7563: 6C         LD           L,H
7564: 2C         INC         L
7565: 20 49      JR           NZ,$75B0
7567: 20 73      JR           NZ,$75DC
7569: 61         LD           H,C
756A: 77         LD           (HL),A
756B: 69         LD           L,C
756C: 74         LD           (HL),H
756D: 20 6F      JR           NZ,$75DE
756F: 6E         LD           L,(HL)
7570: 20 62      JR           NZ,$75D4
7572: 61         LD           H,C
7573: 63         LD           H,E
7574: 6B         LD           L,E
7575: 20 6F      JR           NZ,$75E6
7577: 66         LD           H,(HL)
7578: 20 20      JR           NZ,$759A
757A: 20 74      JR           NZ,$75F0
757C: 68         LD           L,B
757D: 69         LD           L,C
757E: 73         LD           (HL),E
757F: 20 73      JR           NZ,$75F4
7581: 68         LD           L,B
7582: 69         LD           L,C
7583: 65         LD           H,L
7584: 6C         LD           L,H
7585: 64         LD           H,H
7586: 21 FF 4F   LD           HL,$4FFF
7589: 68         LD           L,B
758A: 2C         INC         L
758B: 20 79      JR           NZ,$7606
758D: 65         LD           H,L
758E: 61         LD           H,C
758F: 68         LD           L,B
7590: 2E 2E      LD           L,$2E
7592: 2E 20      LD           L,$20
7594: 53         LD           D,E
7595: 6F         LD           L,A
7596: 6D         LD           L,L
7597: 65         LD           H,L
7598: 6F         LD           L,A
7599: 74         LD           (HL),H
759A: 68         LD           L,B
759B: 65         LD           H,L
759C: 72         LD           (HL),D
759D: 20 73      JR           NZ,$7612
759F: 74         LD           (HL),H
75A0: 75         LD           (HL),L
75A1: 66         LD           H,(HL)
75A2: 66         LD           H,(HL)
75A3: 20 6C      JR           NZ,$7611
75A5: 69         LD           L,C
75A6: 6B         LD           L,E
75A7: 65         LD           H,L
75A8: 74         LD           (HL),H
75A9: 68         LD           L,B
75AA: 69         LD           L,C
75AB: 73         LD           (HL),E
75AC: 20 77      JR           NZ,$7625
75AE: 61         LD           H,C
75AF: 73         LD           (HL),E
75B0: 68         LD           L,B
75B1: 65         LD           H,L
75B2: 64         LD           H,H
75B3: 20 75      JR           NZ,$762A
75B5: 70         LD           (HL),B
75B6: 20 20      JR           NZ,$75D8
75B8: 6F         LD           L,A
75B9: 6E         LD           L,(HL)
75BA: 20 74      JR           NZ,$7630
75BC: 68         LD           L,B
75BD: 65         LD           H,L
75BE: 20 62      JR           NZ,$7622
75C0: 65         LD           H,L
75C1: 61         LD           H,C
75C2: 63         LD           H,E
75C3: 68         LD           L,B
75C4: 2E 2E      LD           L,$2E
75C6: 2E 20      LD           L,$20
75C8: 49         LD           C,C
75C9: 66         LD           H,(HL)
75CA: 5E         LD           E,(HL)
75CB: 6E         LD           L,(HL)
75CC: 20 79      JR           NZ,$7647
75CE: 6F         LD           L,A
75CF: 75         LD           (HL),L
75D0: 20 67      JR           NZ,$7639
75D2: 6F         LD           L,A
75D3: 20 6C      JR           NZ,$7641
75D5: 6F         LD           L,A
75D6: 6F         LD           L,A
75D7: 6B         LD           L,E
75D8: 77         LD           (HL),A
75D9: 61         LD           H,C
75DA: 74         LD           (HL),H
75DB: 63         LD           H,E
75DC: 68         LD           L,B
75DD: 20 6F      JR           NZ,$764E
75DF: 75         LD           (HL),L
75E0: 74         LD           (HL),H
75E1: 20 66      JR           NZ,$7649
75E3: 6F         LD           L,A
75E4: 72         LD           (HL),D
75E5: 20 20      JR           NZ,$7607
75E7: 20 6D      JR           NZ,$7656
75E9: 6F         LD           L,A
75EA: 6E         LD           L,(HL)
75EB: 73         LD           (HL),E
75EC: 74         LD           (HL),H
75ED: 65         LD           H,L
75EE: 72         LD           (HL),D
75EF: 73         LD           (HL),E
75F0: 21 20 45   LD           HL,$4520
75F3: 76         HALT
75F4: 65         LD           H,L
75F5: 72         LD           (HL),D
75F6: 20 20      JR           NZ,$7618
75F8: 73         LD           (HL),E
75F9: 69         LD           L,C
75FA: 6E         LD           L,(HL)
75FB: 63         LD           H,E
75FC: 65         LD           H,L
75FD: 20 79      JR           NZ,$7678
75FF: 6F         LD           L,A
7600: 75         LD           (HL),L
7601: 20 73      JR           NZ,$7676
7603: 68         LD           L,B
7604: 6F         LD           L,A
7605: 77         LD           (HL),A
7606: 65         LD           H,L
7607: 64         LD           H,H
7608: 75         LD           (HL),L
7609: 70         LD           (HL),B
760A: 2C         INC         L
760B: 20 23      JR           NZ,$7630
760D: 23         INC         HL
760E: 23         INC         HL
760F: 23         INC         HL
7610: 23         INC         HL
7611: 2C         INC         L
7612: 20 49      JR           NZ,$765D
7614: 5E         LD           E,(HL)
7615: 76         HALT
7616: 65         LD           H,L
7617: 20 73      JR           NZ,$768C
7619: 65         LD           H,L
761A: 65         LD           H,L
761B: 6E         LD           L,(HL)
761C: 20 5E      JR           NZ,$767C
761E: 65         LD           H,L
761F: 6D         LD           L,L
7620: 20 61      JR           NZ,$7683
7622: 6C         LD           L,H
7623: 6C         LD           L,H
7624: 20 20      JR           NZ,$7646
7626: 20 20      JR           NZ,$7648
7628: 6F         LD           L,A
7629: 76         HALT
762A: 65         LD           H,L
762B: 72         LD           (HL),D
762C: 20 74      JR           NZ,$76A2
762E: 68         LD           L,B
762F: 65         LD           H,L
7630: 20 70      JR           NZ,$76A2
7632: 6C         LD           L,H
7633: 61         LD           H,C
7634: 63         LD           H,E
7635: 65         LD           H,L
7636: 21 FF 4C   LD           HL,$4CFF
7639: 65         LD           H,L
763A: 76         HALT
763B: 65         LD           H,L
763C: 6C         LD           L,H
763D: 20 31      JR           NZ,$7670
763F: 2D         DEC         L
7640: 2D         DEC         L
7641: 20 20      JR           NZ,$7663
7643: 20 20      JR           NZ,$7665
7645: 20 20      JR           NZ,$7667
7647: 20 20      JR           NZ,$7669
7649: 20 20      JR           NZ,$766B
764B: 20 20      JR           NZ,$766D
764D: 54         LD           D,H
764E: 61         LD           H,C
764F: 69         LD           L,C
7650: 6C         LD           L,H
7651: 20 43      JR           NZ,$7696
7653: 61         LD           H,C
7654: 76         HALT
7655: 65         LD           H,L
7656: FF         RST         0X38
7657: 4C         LD           C,H
7658: 65         LD           H,L
7659: 76         HALT
765A: 65         LD           H,L
765B: 6C         LD           L,H
765C: 20 32      JR           NZ,$7690
765E: 2D         DEC         L
765F: 2D         DEC         L
7660: 20 20      JR           NZ,$7682
7662: 20 20      JR           NZ,$7684
7664: 20 20      JR           NZ,$7686
7666: 20 20      JR           NZ,$7688
7668: 20 20      JR           NZ,$768A
766A: 42         LD           B,D
766B: 6F         LD           L,A
766C: 74         LD           (HL),H
766D: 74         LD           (HL),H
766E: 6C         LD           L,H
766F: 65         LD           H,L
7670: 20 47      JR           NZ,$76B9
7672: 72         LD           (HL),D
7673: 6F         LD           L,A
7674: 74         LD           (HL),H
7675: 74         LD           (HL),H
7676: 6F         LD           L,A
7677: FF         RST         0X38
7678: 4C         LD           C,H
7679: 65         LD           H,L
767A: 76         HALT
767B: 65         LD           H,L
767C: 6C         LD           L,H
767D: 20 33      JR           NZ,$76B2
767F: 2D         DEC         L
7680: 2D         DEC         L
7681: 20 20      JR           NZ,$76A3
7683: 20 20      JR           NZ,$76A5
7685: 20 20      JR           NZ,$76A7
7687: 20 20      JR           NZ,$76A9
7689: 20 20      JR           NZ,$76AB
768B: 20 20      JR           NZ,$76AD
768D: 20 4B      JR           NZ,$76DA
768F: 65         LD           H,L
7690: 79         LD           A,C
7691: 20 43      JR           NZ,$76D6
7693: 61         LD           H,C
7694: 76         HALT
7695: 65         LD           H,L
7696: 72         LD           (HL),D
7697: 6E         LD           L,(HL)
7698: FF         RST         0X38
7699: 4C         LD           C,H
769A: 65         LD           H,L
769B: 76         HALT
769C: 65         LD           H,L
769D: 6C         LD           L,H
769E: 20 34      JR           NZ,$76D4
76A0: 2D         DEC         L
76A1: 2D         DEC         L
76A2: 20 20      JR           NZ,$76C4
76A4: 20 20      JR           NZ,$76C6
76A6: 20 20      JR           NZ,$76C8
76A8: 20 20      JR           NZ,$76CA
76AA: 41         LD           B,C
76AB: 6E         LD           L,(HL)
76AC: 67         LD           H,A
76AD: 6C         LD           L,H
76AE: 65         LD           H,L
76AF: 72         LD           (HL),D
76B0: 5E         LD           E,(HL)
76B1: 73         LD           (HL),E
76B2: 20 54      JR           NZ,$7708
76B4: 75         LD           (HL),L
76B5: 6E         LD           L,(HL)
76B6: 6E         LD           L,(HL)
76B7: 65         LD           H,L
76B8: 6C         LD           L,H
76B9: FF         RST         0X38
76BA: 4C         LD           C,H
76BB: 65         LD           H,L
76BC: 76         HALT
76BD: 65         LD           H,L
76BE: 6C         LD           L,H
76BF: 20 35      JR           NZ,$76F6
76C1: 2D         DEC         L
76C2: 2D         DEC         L
76C3: 20 20      JR           NZ,$76E5
76C5: 20 20      JR           NZ,$76E7
76C7: 20 20      JR           NZ,$76E9
76C9: 20 20      JR           NZ,$76EB
76CB: 20 20      JR           NZ,$76ED
76CD: 43         LD           B,E
76CE: 61         LD           H,C
76CF: 74         LD           (HL),H
76D0: 66         LD           H,(HL)
76D1: 69         LD           L,C
76D2: 73         LD           (HL),E
76D3: 68         LD           L,B
76D4: 5E         LD           E,(HL)
76D5: 73         LD           (HL),E
76D6: 20 4D      JR           NZ,$7725
76D8: 61         LD           H,C
76D9: 77         LD           (HL),A
76DA: FF         RST         0X38
76DB: 4C         LD           C,H
76DC: 65         LD           H,L
76DD: 76         HALT
76DE: 65         LD           H,L
76DF: 6C         LD           L,H
76E0: 20 36      JR           NZ,$7718
76E2: 2D         DEC         L
76E3: 2D         DEC         L
76E4: 20 20      JR           NZ,$7706
76E6: 20 20      JR           NZ,$7708
76E8: 20 20      JR           NZ,$770A
76EA: 20 20      JR           NZ,$770C
76EC: 20 20      JR           NZ,$770E
76EE: 20 20      JR           NZ,$7710
76F0: 46         LD           B,(HL)
76F1: 61         LD           H,C
76F2: 63         LD           H,E
76F3: 65         LD           H,L
76F4: 20 53      JR           NZ,$7749
76F6: 68         LD           L,B
76F7: 72         LD           (HL),D
76F8: 69         LD           L,C
76F9: 6E         LD           L,(HL)
76FA: 65         LD           H,L
76FB: FF         RST         0X38
76FC: 4C         LD           C,H
76FD: 65         LD           H,L
76FE: 76         HALT
76FF: 65         LD           H,L
7700: 6C         LD           L,H
7701: 20 37      JR           NZ,$773A
7703: 2D         DEC         L
7704: 2D         DEC         L
7705: 20 20      JR           NZ,$7727
7707: 20 20      JR           NZ,$7729
7709: 20 20      JR           NZ,$772B
770B: 20 20      JR           NZ,$772D
770D: 20 20      JR           NZ,$772F
770F: 45         LD           B,L
7710: 61         LD           H,C
7711: 67         LD           H,A
7712: 6C         LD           L,H
7713: 65         LD           H,L
7714: 5E         LD           E,(HL)
7715: 73         LD           (HL),E
7716: 20 54      JR           NZ,$776C
7718: 6F         LD           L,A
7719: 77         LD           (HL),A
771A: 65         LD           H,L
771B: 72         LD           (HL),D
771C: FF         RST         0X38
771D: 4C         LD           C,H
771E: 65         LD           H,L
771F: 76         HALT
7720: 65         LD           H,L
7721: 6C         LD           L,H
7722: 20 38      JR           NZ,$775C
7724: 2D         DEC         L
7725: 2D         DEC         L
7726: 20 20      JR           NZ,$7748
7728: 20 20      JR           NZ,$774A
772A: 20 20      JR           NZ,$774C
772C: 20 20      JR           NZ,$774E
772E: 20 20      JR           NZ,$7750
7730: 20 20      JR           NZ,$7752
7732: 54         LD           D,H
7733: 75         LD           (HL),L
7734: 72         LD           (HL),D
7735: 74         LD           (HL),H
7736: 6C         LD           L,H
7737: 65         LD           H,L
7738: 20 52      JR           NZ,$778C
773A: 6F         LD           L,A
773B: 63         LD           H,E
773C: 6B         LD           L,E
773D: FF         RST         0X38
773E: 57         LD           D,A
773F: 69         LD           L,C
7740: 6E         LD           L,(HL)
7741: 64         LD           H,H
7742: 20 46      JR           NZ,$778A
7744: 69         LD           L,C
7745: 73         LD           (HL),E
7746: 68         LD           L,B
7747: 5E         LD           E,(HL)
7748: 73         LD           (HL),E
7749: 20 45      JR           NZ,$7790
774B: 67         LD           H,A
774C: 67         LD           H,A
774D: 20 FF      JR           NZ,$774E
774F: 4D         LD           C,L
7750: 6F         LD           L,A
7751: 75         LD           (HL),L
7752: 6E         LD           L,(HL)
7753: 74         LD           (HL),H
7754: 61         LD           H,C
7755: 69         LD           L,C
7756: 6E         LD           L,(HL)
7757: 20 42      JR           NZ,$779B
7759: 72         LD           (HL),D
775A: 69         LD           L,C
775B: 64         LD           H,H
775C: 67         LD           H,A
775D: 65         LD           H,L
775E: 20 FF      JR           NZ,$775F
7760: 53         LD           D,E
7761: 61         LD           H,C
7762: 6C         LD           L,H
7763: 65         LD           H,L
7764: 5E         LD           E,(HL)
7765: 73         LD           (HL),E
7766: 20 48      JR           NZ,$77B0
7768: 6F         LD           L,A
7769: 75         LD           (HL),L
776A: 73         LD           (HL),E
776B: 65         LD           H,L
776C: 20 4F      JR           NZ,$77BD
776E: 5E         LD           E,(HL)
776F: 20 20      JR           NZ,$7791
7771: 20 20      JR           NZ,$7793
7773: 20 42      JR           NZ,$77B7
7775: 61         LD           H,C
7776: 6E         LD           L,(HL)
7777: 61         LD           H,C
7778: 6E         LD           L,(HL)
7779: 61         LD           H,C
777A: 73         LD           (HL),E
777B: FF         RST         0X38
777C: 50         LD           D,B
777D: 6F         LD           L,A
777E: 74         LD           (HL),H
777F: 68         LD           L,B
7780: 6F         LD           L,A
7781: 6C         LD           L,H
7782: 65         LD           H,L
7783: 20 46      JR           NZ,$77CB
7785: 69         LD           L,C
7786: 65         LD           H,L
7787: 6C         LD           L,H
7788: 64         LD           H,H
7789: FF         RST         0X38
778A: 20 20      JR           NZ,$77AC
778C: 20 20      JR           NZ,$77AE
778E: 48         LD           C,B
778F: 6F         LD           L,A
7790: 75         LD           (HL),L
7791: 73         LD           (HL),E
7792: 65         LD           H,L
7793: 20 42      JR           NZ,$77D7
7795: 79         LD           A,C
7796: 20 20      JR           NZ,$77B8
7798: 20 20      JR           NZ,$77BA
779A: 20 20      JR           NZ,$77BC
779C: 20 20      JR           NZ,$77BE
779E: 20 54      JR           NZ,$77F4
77A0: 68         LD           L,B
77A1: 65         LD           H,L
77A2: 20 42      JR           NZ,$77E6
77A4: 61         LD           H,C
77A5: 79         LD           A,C
77A6: FF         RST         0X38
77A7: 20 20      JR           NZ,$77C9
77A9: 20 54      JR           NZ,$77FF
77AB: 72         LD           (HL),D
77AC: 65         LD           H,L
77AD: 6E         LD           L,(HL)
77AE: 64         LD           H,H
77AF: 79         LD           A,C
77B0: 20 47      JR           NZ,$77F9
77B2: 61         LD           H,C
77B3: 6D         LD           L,L
77B4: 65         LD           H,L
77B5: FF         RST         0X38
77B6: 20 20      JR           NZ,$77D8
77B8: 54         LD           D,H
77B9: 6F         LD           L,A
77BA: 77         LD           (HL),A
77BB: 6E         LD           L,(HL)
77BC: 20 54      JR           NZ,$7812
77BE: 6F         LD           L,A
77BF: 6F         LD           L,A
77C0: 6C         LD           L,H
77C1: 20 53      JR           NZ,$7816
77C3: 68         LD           L,B
77C4: 6F         LD           L,A
77C5: 70         LD           (HL),B
77C6: FF         RST         0X38
77C7: 4D         LD           C,L
77C8: 61         LD           H,C
77C9: 72         LD           (HL),D
77CA: 69         LD           L,C
77CB: 6E         LD           L,(HL)
77CC: 20 61      JR           NZ,$782F
77CE: 6E         LD           L,(HL)
77CF: 64         LD           H,H
77D0: 20 20      JR           NZ,$77F2
77D2: 20 20      JR           NZ,$77F4
77D4: 20 20      JR           NZ,$77F6
77D6: 20 20      JR           NZ,$77F8
77D8: 20 20      JR           NZ,$77FA
77DA: 54         LD           D,H
77DB: 61         LD           H,C
77DC: 72         LD           (HL),D
77DD: 69         LD           L,C
77DE: 6E         LD           L,(HL)
77DF: 5E         LD           E,(HL)
77E0: 73         LD           (HL),E
77E1: 20 48      JR           NZ,$782B
77E3: 6F         LD           L,A
77E4: 75         LD           (HL),L
77E5: 73         LD           (HL),E
77E6: 65         LD           H,L
77E7: FF         RST         0X38
77E8: 20 20      JR           NZ,$780A
77EA: 20 57      JR           NZ,$7843
77EC: 69         LD           L,C
77ED: 74         LD           (HL),H
77EE: 63         LD           H,E
77EF: 68         LD           L,B
77F0: 5E         LD           E,(HL)
77F1: 73         LD           (HL),E
77F2: 20 48      JR           NZ,$783C
77F4: 75         LD           (HL),L
77F5: 74         LD           (HL),H
77F6: FF         RST         0X38
77F7: 20 20      JR           NZ,$7819
77F9: 59         LD           E,C
77FA: 61         LD           H,C
77FB: 72         LD           (HL),D
77FC: 6E         LD           L,(HL)
77FD: 61         LD           H,C
77FE: 20 44      JR           NZ,$7844
7800: 65         LD           H,L
7801: 73         LD           (HL),E
7802: 65         LD           H,L
7803: 72         LD           (HL),D
7804: 74         LD           (HL),H
7805: FF         RST         0X38
7806: 20 20      JR           NZ,$7828
7808: 55         LD           D,L
7809: 6B         LD           L,E
780A: 75         LD           (HL),L
780B: 6B         LD           L,E
780C: 75         LD           (HL),L
780D: 20 50      JR           NZ,$785F
780F: 72         LD           (HL),D
7810: 61         LD           H,C
7811: 69         LD           L,C
7812: 72         LD           (HL),D
7813: 69         LD           L,C
7814: 65         LD           H,L
7815: FF         RST         0X38
7816: 4D         LD           C,L
7817: 79         LD           A,C
7818: 73         LD           (HL),E
7819: 74         LD           (HL),H
781A: 65         LD           H,L
781B: 72         LD           (HL),D
781C: 69         LD           L,C
781D: 6F         LD           L,A
781E: 75         LD           (HL),L
781F: 73         LD           (HL),E
7820: 20 57      JR           NZ,$7879
7822: 6F         LD           L,A
7823: 6F         LD           L,A
7824: 64         LD           H,H
7825: 73         LD           (HL),E
7826: FF         RST         0X38
7827: 20 20      JR           NZ,$7849
7829: 4D         LD           C,L
782A: 74         LD           (HL),H
782B: 2E 20      LD           L,$20
782D: 54         LD           D,H
782E: 61         LD           H,C
782F: 6D         LD           L,L
7830: 61         LD           H,C
7831: 72         LD           (HL),D
7832: 61         LD           H,C
7833: 6E         LD           L,(HL)
7834: 63         LD           H,E
7835: 68         LD           L,B
7836: 20 FF      JR           NZ,$7837
7838: 20 20      JR           NZ,$785A
783A: 20 20      JR           NZ,$785C
783C: 20 54      JR           NZ,$7892
783E: 61         LD           H,C
783F: 6C         LD           L,H
7840: 20 54      JR           NZ,$7896
7842: 61         LD           H,C
7843: 6C         LD           L,H
7844: 20 20      JR           NZ,$7866
7846: 20 20      JR           NZ,$7868
7848: 20 4D      JR           NZ,$7897
784A: 6F         LD           L,A
784B: 75         LD           (HL),L
784C: 6E         LD           L,(HL)
784D: 74         LD           (HL),H
784E: 61         LD           H,C
784F: 69         LD           L,C
7850: 6E         LD           L,(HL)
7851: 20 52      JR           NZ,$78A5
7853: 61         LD           H,C
7854: 6E         LD           L,(HL)
7855: 67         LD           H,A
7856: 65         LD           H,L
7857: 20 FF      JR           NZ,$7858
7859: 20 20      JR           NZ,$787B
785B: 53         LD           D,E
785C: 69         LD           L,C
785D: 67         LD           H,A
785E: 6E         LD           L,(HL)
785F: 70         LD           (HL),B
7860: 6F         LD           L,A
7861: 73         LD           (HL),E
7862: 74         LD           (HL),H
7863: 20 4D      JR           NZ,$78B2
7865: 61         LD           H,C
7866: 7A         LD           A,D
7867: 65         LD           H,L
7868: 20 FF      JR           NZ,$7869
786A: 20 20      JR           NZ,$788C
786C: 4D         LD           C,L
786D: 61         LD           H,C
786E: 62         LD           H,D
786F: 65         LD           H,L
7870: 20 56      JR           NZ,$78C8
7872: 69         LD           L,C
7873: 6C         LD           L,H
7874: 6C         LD           L,H
7875: 61         LD           H,C
7876: 67         LD           H,A
7877: 65         LD           H,L
7878: 20 20      JR           NZ,$789A
787A: FF         RST         0X38
787B: 20 41      JR           NZ,$78BE
787D: 6E         LD           L,(HL)
787E: 69         LD           L,C
787F: 6D         LD           L,L
7880: 61         LD           H,C
7881: 6C         LD           L,H
7882: 20 56      JR           NZ,$78DA
7884: 69         LD           L,C
7885: 6C         LD           L,H
7886: 6C         LD           L,H
7887: 61         LD           H,C
7888: 67         LD           H,A
7889: 65         LD           H,L
788A: 20 FF      JR           NZ,$788B
788C: 20 20      JR           NZ,$78AE
788E: 20 20      JR           NZ,$78B0
7890: 43         LD           B,E
7891: 65         LD           H,L
7892: 6D         LD           L,L
7893: 65         LD           H,L
7894: 74         LD           (HL),H
7895: 61         LD           H,C
7896: 72         LD           (HL),D
7897: 79         LD           A,C
7898: 20 20      JR           NZ,$78BA
789A: 20 20      JR           NZ,$78BC
789C: FF         RST         0X38
789D: 20 20      JR           NZ,$78BF
789F: 20 52      JR           NZ,$78F3
78A1: 61         LD           H,C
78A2: 70         LD           (HL),B
78A3: 69         LD           L,C
78A4: 64         LD           H,H
78A5: 73         LD           (HL),E
78A6: 20 52      JR           NZ,$78FA
78A8: 69         LD           L,C
78A9: 64         LD           H,H
78AA: 65         LD           H,L
78AB: 20 20      JR           NZ,$78CD
78AD: FF         RST         0X38
78AE: 4B         LD           C,E
78AF: 6F         LD           L,A
78B0: 68         LD           L,B
78B1: 6F         LD           L,A
78B2: 6C         LD           L,H
78B3: 69         LD           L,C
78B4: 6E         LD           L,(HL)
78B5: 74         LD           (HL),H
78B6: 20 50      JR           NZ,$7908
78B8: 72         LD           (HL),D
78B9: 61         LD           H,C
78BA: 69         LD           L,C
78BB: 72         LD           (HL),D
78BC: 69         LD           L,C
78BD: 65         LD           H,L
78BE: FF         RST         0X38
78BF: 20 54      JR           NZ,$7915
78C1: 6F         LD           L,A
78C2: 72         LD           (HL),D
78C3: 6F         LD           L,A
78C4: 6E         LD           L,(HL)
78C5: 62         LD           H,D
78C6: 6F         LD           L,A
78C7: 20 53      JR           NZ,$791C
78C9: 68         LD           L,B
78CA: 6F         LD           L,A
78CB: 72         LD           (HL),D
78CC: 65         LD           H,L
78CD: 73         LD           (HL),E
78CE: FF         RST         0X38
78CF: 20 20      JR           NZ,$78F1
78D1: 4D         LD           C,L
78D2: 61         LD           H,C
78D3: 72         LD           (HL),D
78D4: 74         LD           (HL),H
78D5: 68         LD           L,B
78D6: 61         LD           H,C
78D7: 5E         LD           E,(HL)
78D8: 73         LD           (HL),E
78D9: 20 42      JR           NZ,$791D
78DB: 61         LD           H,C
78DC: 79         LD           A,C
78DD: FF         RST         0X38
78DE: 45         LD           B,L
78DF: 61         LD           H,C
78E0: 73         LD           (HL),E
78E1: 74         LD           (HL),H
78E2: 20 6F      JR           NZ,$7953
78E4: 66         LD           H,(HL)
78E5: 20 74      JR           NZ,$795B
78E7: 68         LD           L,B
78E8: 65         LD           H,L
78E9: 20 42      JR           NZ,$792D
78EB: 61         LD           H,C
78EC: 79         LD           A,C
78ED: FF         RST         0X38
78EE: 20 20      JR           NZ,$7910
78F0: 47         LD           B,A
78F1: 6F         LD           L,A
78F2: 70         LD           (HL),B
78F3: 6F         LD           L,A
78F4: 6E         LD           L,(HL)
78F5: 67         LD           H,A
78F6: 61         LD           H,C
78F7: 20 53      JR           NZ,$794C
78F9: 77         LD           (HL),A
78FA: 61         LD           H,C
78FB: 6D         LD           L,L
78FC: 70         LD           (HL),B
78FD: FF         RST         0X38
78FE: 20 20      JR           NZ,$7920
7900: 20 46      JR           NZ,$7948
7902: 61         LD           H,C
7903: 63         LD           H,E
7904: 65         LD           H,L
7905: 20 53      JR           NZ,$795A
7907: 68         LD           L,B
7908: 72         LD           (HL),D
7909: 69         LD           L,C
790A: 6E         LD           L,(HL)
790B: 65         LD           H,L
790C: 20 FF      JR           NZ,$790D
790E: 20 4B      JR           NZ,$795B
7910: 61         LD           H,C
7911: 6E         LD           L,(HL)
7912: 61         LD           H,C
7913: 6C         LD           L,H
7914: 65         LD           H,L
7915: 74         LD           (HL),H
7916: 20 43      JR           NZ,$795B
7918: 61         LD           H,C
7919: 73         LD           (HL),E
791A: 74         LD           (HL),H
791B: 6C         LD           L,H
791C: 65         LD           H,L
791D: FF         RST         0X38
791E: 54         LD           D,H
791F: 61         LD           H,C
7920: 6C         LD           L,H
7921: 20 54      JR           NZ,$7977
7923: 61         LD           H,C
7924: 6C         LD           L,H
7925: 20 48      JR           NZ,$796F
7927: 65         LD           H,L
7928: 69         LD           L,C
7929: 67         LD           H,A
792A: 68         LD           L,B
792B: 74         LD           (HL),H
792C: 73         LD           (HL),E
792D: FF         RST         0X38
792E: 54         LD           D,H
792F: 61         LD           H,C
7930: 62         LD           H,D
7931: 61         LD           H,C
7932: 68         LD           L,B
7933: 6C         LD           L,H
7934: 20 57      JR           NZ,$798D
7936: 61         LD           H,C
7937: 73         LD           (HL),E
7938: 74         LD           (HL),H
7939: 65         LD           H,L
793A: 6C         LD           L,H
793B: 61         LD           H,C
793C: 6E         LD           L,(HL)
793D: 64         LD           H,H
793E: FF         RST         0X38
793F: 20 20      JR           NZ,$7961
7941: 53         LD           D,E
7942: 6F         LD           L,A
7943: 75         LD           (HL),L
7944: 74         LD           (HL),H
7945: 68         LD           L,B
7946: 20 6F      JR           NZ,$79B7
7948: 66         LD           H,(HL)
7949: 20 74      JR           NZ,$79BF
794B: 68         LD           L,B
794C: 65         LD           H,L
794D: 20 20      JR           NZ,$796F
794F: 20 20      JR           NZ,$7971
7951: 20 20      JR           NZ,$7973
7953: 56         LD           D,(HL)
7954: 69         LD           L,C
7955: 6C         LD           L,H
7956: 6C         LD           L,H
7957: 61         LD           H,C
7958: 67         LD           H,A
7959: 65         LD           H,L
795A: FF         RST         0X38
795B: 20 20      JR           NZ,$797D
795D: 46         LD           B,(HL)
795E: 69         LD           L,C
795F: 73         LD           (HL),E
7960: 68         LD           L,B
7961: 69         LD           L,C
7962: 6E         LD           L,(HL)
7963: 67         LD           H,A
7964: 20 50      JR           NZ,$79B6
7966: 6F         LD           L,A
7967: 6E         LD           L,(HL)
7968: 64         LD           H,H
7969: 20 20      JR           NZ,$798B
796B: FF         RST         0X38
796C: 4D         LD           C,L
796D: 61         LD           H,C
796E: 64         LD           H,H
796F: 61         LD           H,C
7970: 6D         LD           L,L
7971: 20 4D      JR           NZ,$79C0
7973: 65         LD           H,L
7974: 6F         LD           L,A
7975: 77         LD           (HL),A
7976: 4D         LD           C,L
7977: 65         LD           H,L
7978: 6F         LD           L,A
7979: 77         LD           (HL),A
797A: 5E         LD           E,(HL)
797B: 73         LD           (HL),E
797C: 20 20      JR           NZ,$799E
797E: 20 20      JR           NZ,$79A0
7980: 20 48      JR           NZ,$79CA
7982: 6F         LD           L,A
7983: 75         LD           (HL),L
7984: 73         LD           (HL),E
7985: 65         LD           H,L
7986: 20 20      JR           NZ,$79A8
7988: 20 20      JR           NZ,$79AA
798A: 20 20      JR           NZ,$79AC
798C: 20 42      JR           NZ,$79D0
798E: 65         LD           H,L
798F: 77         LD           (HL),A
7990: 61         LD           H,C
7991: 72         LD           (HL),D
7992: 65         LD           H,L
7993: 20 6F      JR           NZ,$7A04
7995: 66         LD           H,(HL)
7996: 20 44      JR           NZ,$79DC
7998: 6F         LD           L,A
7999: 67         LD           H,A
799A: 21 FF 4F   LD           HL,$4FFF
799D: 6C         LD           L,H
799E: 64         LD           H,H
799F: 20 4D      JR           NZ,$79EE
79A1: 61         LD           H,C
79A2: 6E         LD           L,(HL)
79A3: 20 55      JR           NZ,$79FA
79A5: 6C         LD           L,H
79A6: 72         LD           (HL),D
79A7: 69         LD           L,C
79A8: 72         LD           (HL),D
79A9: 61         LD           H,C
79AA: 5E         LD           E,(HL)
79AB: 73         LD           (HL),E
79AC: 20 20      JR           NZ,$79CE
79AE: 20 20      JR           NZ,$79D0
79B0: 20 48      JR           NZ,$79FA
79B2: 6F         LD           L,A
79B3: 75         LD           (HL),L
79B4: 73         LD           (HL),E
79B5: 65         LD           H,L
79B6: 20 20      JR           NZ,$79D8
79B8: 20 20      JR           NZ,$79DA
79BA: 20 20      JR           NZ,$79DC
79BC: FF         RST         0X38
79BD: 57         LD           D,A
79BE: 65         LD           H,L
79BF: 69         LD           L,C
79C0: 72         LD           (HL),D
79C1: 64         LD           H,H
79C2: 20 4D      JR           NZ,$7A11
79C4: 72         LD           (HL),D
79C5: 2E 20      LD           L,$20
79C7: 57         LD           D,A
79C8: 72         LD           (HL),D
79C9: 69         LD           L,C
79CA: 74         LD           (HL),H
79CB: 65         LD           H,L
79CC: 20 FF      JR           NZ,$79CD
79CE: FF         RST         0X38
79CF: FF         RST         0X38
79D0: FF         RST         0X38
79D1: FF         RST         0X38
79D2: FF         RST         0X38
79D3: FF         RST         0X38
79D4: FF         RST         0X38
79D5: FF         RST         0X38
79D6: FF         RST         0X38
79D7: FF         RST         0X38
79D8: FF         RST         0X38
79D9: FF         RST         0X38
79DA: FF         RST         0X38
79DB: FF         RST         0X38
79DC: FF         RST         0X38
79DD: FF         RST         0X38
79DE: FF         RST         0X38
79DF: FF         RST         0X38
79E0: FF         RST         0X38
79E1: FF         RST         0X38
79E2: FF         RST         0X38
79E3: FF         RST         0X38
79E4: FF         RST         0X38
79E5: FF         RST         0X38
79E6: FF         RST         0X38
79E7: FF         RST         0X38
79E8: FF         RST         0X38
79E9: FF         RST         0X38
79EA: FF         RST         0X38
79EB: FF         RST         0X38
79EC: FF         RST         0X38
79ED: FF         RST         0X38
79EE: FF         RST         0X38
79EF: FF         RST         0X38
79F0: FF         RST         0X38
79F1: FF         RST         0X38
79F2: FF         RST         0X38
79F3: FF         RST         0X38
79F4: FF         RST         0X38
79F5: FF         RST         0X38
79F6: FF         RST         0X38
79F7: FF         RST         0X38
79F8: FF         RST         0X38
79F9: FF         RST         0X38
79FA: FF         RST         0X38
79FB: FF         RST         0X38
79FC: FF         RST         0X38
79FD: FF         RST         0X38
79FE: FF         RST         0X38
79FF: FF         RST         0X38
7A00: FF         RST         0X38
7A01: FF         RST         0X38
7A02: FF         RST         0X38
7A03: FF         RST         0X38
7A04: FF         RST         0X38
7A05: FF         RST         0X38
7A06: FF         RST         0X38
7A07: FF         RST         0X38
7A08: FF         RST         0X38
7A09: FF         RST         0X38
7A0A: FF         RST         0X38
7A0B: FF         RST         0X38
7A0C: FF         RST         0X38
7A0D: FF         RST         0X38
7A0E: FF         RST         0X38
7A0F: FF         RST         0X38
7A10: FF         RST         0X38
7A11: FF         RST         0X38
7A12: FF         RST         0X38
7A13: FF         RST         0X38
7A14: FF         RST         0X38
7A15: FF         RST         0X38
7A16: FF         RST         0X38
7A17: FF         RST         0X38
7A18: FF         RST         0X38
7A19: FF         RST         0X38
7A1A: FF         RST         0X38
7A1B: FF         RST         0X38
7A1C: FF         RST         0X38
7A1D: FF         RST         0X38
7A1E: FF         RST         0X38
7A1F: FF         RST         0X38
7A20: FF         RST         0X38
7A21: FF         RST         0X38
7A22: FF         RST         0X38
7A23: FF         RST         0X38
7A24: FF         RST         0X38
7A25: FF         RST         0X38
7A26: FF         RST         0X38
7A27: FF         RST         0X38
7A28: FF         RST         0X38
7A29: FF         RST         0X38
7A2A: FF         RST         0X38
7A2B: FF         RST         0X38
7A2C: FF         RST         0X38
7A2D: FF         RST         0X38
7A2E: FF         RST         0X38
7A2F: FF         RST         0X38
7A30: FF         RST         0X38
7A31: FF         RST         0X38
7A32: FF         RST         0X38
7A33: FF         RST         0X38
7A34: FF         RST         0X38
7A35: FF         RST         0X38
7A36: FF         RST         0X38
7A37: FF         RST         0X38
7A38: FF         RST         0X38
7A39: FF         RST         0X38
7A3A: FF         RST         0X38
7A3B: FF         RST         0X38
7A3C: FF         RST         0X38
7A3D: FF         RST         0X38
7A3E: FF         RST         0X38
7A3F: FF         RST         0X38
7A40: FF         RST         0X38
7A41: FF         RST         0X38
7A42: FF         RST         0X38
7A43: FF         RST         0X38
7A44: FF         RST         0X38
7A45: FF         RST         0X38
7A46: FF         RST         0X38
7A47: FF         RST         0X38
7A48: FF         RST         0X38
7A49: FF         RST         0X38
7A4A: FF         RST         0X38
7A4B: FF         RST         0X38
7A4C: FF         RST         0X38
7A4D: FF         RST         0X38
7A4E: FF         RST         0X38
7A4F: FF         RST         0X38
7A50: FF         RST         0X38
7A51: FF         RST         0X38
7A52: FF         RST         0X38
7A53: FF         RST         0X38
7A54: FF         RST         0X38
7A55: FF         RST         0X38
7A56: FF         RST         0X38
7A57: FF         RST         0X38
7A58: FF         RST         0X38
7A59: FF         RST         0X38
7A5A: FF         RST         0X38
7A5B: FF         RST         0X38
7A5C: FF         RST         0X38
7A5D: FF         RST         0X38
7A5E: FF         RST         0X38
7A5F: FF         RST         0X38
7A60: FF         RST         0X38
7A61: FF         RST         0X38
7A62: FF         RST         0X38
7A63: FF         RST         0X38
7A64: FF         RST         0X38
7A65: FF         RST         0X38
7A66: FF         RST         0X38
7A67: FF         RST         0X38
7A68: FF         RST         0X38
7A69: FF         RST         0X38
7A6A: FF         RST         0X38
7A6B: FF         RST         0X38
7A6C: FF         RST         0X38
7A6D: FF         RST         0X38
7A6E: FF         RST         0X38
7A6F: FF         RST         0X38
7A70: FF         RST         0X38
7A71: FF         RST         0X38
7A72: FF         RST         0X38
7A73: FF         RST         0X38
7A74: FF         RST         0X38
7A75: FF         RST         0X38
7A76: FF         RST         0X38
7A77: FF         RST         0X38
7A78: FF         RST         0X38
7A79: FF         RST         0X38
7A7A: FF         RST         0X38
7A7B: FF         RST         0X38
7A7C: FF         RST         0X38
7A7D: FF         RST         0X38
7A7E: FF         RST         0X38
7A7F: FF         RST         0X38
7A80: FF         RST         0X38
7A81: FF         RST         0X38
7A82: FF         RST         0X38
7A83: FF         RST         0X38
7A84: FF         RST         0X38
7A85: FF         RST         0X38
7A86: FF         RST         0X38
7A87: FF         RST         0X38
7A88: FF         RST         0X38
7A89: FF         RST         0X38
7A8A: FF         RST         0X38
7A8B: FF         RST         0X38
7A8C: FF         RST         0X38
7A8D: FF         RST         0X38
7A8E: FF         RST         0X38
7A8F: FF         RST         0X38
7A90: FF         RST         0X38
7A91: FF         RST         0X38
7A92: FF         RST         0X38
7A93: FF         RST         0X38
7A94: FF         RST         0X38
7A95: FF         RST         0X38
7A96: FF         RST         0X38
7A97: FF         RST         0X38
7A98: FF         RST         0X38
7A99: FF         RST         0X38
7A9A: FF         RST         0X38
7A9B: FF         RST         0X38
7A9C: FF         RST         0X38
7A9D: FF         RST         0X38
7A9E: FF         RST         0X38
7A9F: FF         RST         0X38
7AA0: FF         RST         0X38
7AA1: FF         RST         0X38
7AA2: FF         RST         0X38
7AA3: FF         RST         0X38
7AA4: FF         RST         0X38
7AA5: FF         RST         0X38
7AA6: FF         RST         0X38
7AA7: FF         RST         0X38
7AA8: FF         RST         0X38
7AA9: FF         RST         0X38
7AAA: FF         RST         0X38
7AAB: FF         RST         0X38
7AAC: FF         RST         0X38
7AAD: FF         RST         0X38
7AAE: FF         RST         0X38
7AAF: FF         RST         0X38
7AB0: FF         RST         0X38
7AB1: FF         RST         0X38
7AB2: FF         RST         0X38
7AB3: FF         RST         0X38
7AB4: FF         RST         0X38
7AB5: FF         RST         0X38
7AB6: FF         RST         0X38
7AB7: FF         RST         0X38
7AB8: FF         RST         0X38
7AB9: FF         RST         0X38
7ABA: FF         RST         0X38
7ABB: FF         RST         0X38
7ABC: FF         RST         0X38
7ABD: FF         RST         0X38
7ABE: FF         RST         0X38
7ABF: FF         RST         0X38
7AC0: FF         RST         0X38
7AC1: FF         RST         0X38
7AC2: FF         RST         0X38
7AC3: FF         RST         0X38
7AC4: FF         RST         0X38
7AC5: FF         RST         0X38
7AC6: FF         RST         0X38
7AC7: FF         RST         0X38
7AC8: FF         RST         0X38
7AC9: FF         RST         0X38
7ACA: FF         RST         0X38
7ACB: FF         RST         0X38
7ACC: FF         RST         0X38
7ACD: FF         RST         0X38
7ACE: FF         RST         0X38
7ACF: FF         RST         0X38
7AD0: FF         RST         0X38
7AD1: FF         RST         0X38
7AD2: FF         RST         0X38
7AD3: FF         RST         0X38
7AD4: FF         RST         0X38
7AD5: FF         RST         0X38
7AD6: FF         RST         0X38
7AD7: FF         RST         0X38
7AD8: FF         RST         0X38
7AD9: FF         RST         0X38
7ADA: FF         RST         0X38
7ADB: FF         RST         0X38
7ADC: FF         RST         0X38
7ADD: FF         RST         0X38
7ADE: FF         RST         0X38
7ADF: FF         RST         0X38
7AE0: FF         RST         0X38
7AE1: FF         RST         0X38
7AE2: FF         RST         0X38
7AE3: FF         RST         0X38
7AE4: FF         RST         0X38
7AE5: FF         RST         0X38
7AE6: FF         RST         0X38
7AE7: FF         RST         0X38
7AE8: FF         RST         0X38
7AE9: FF         RST         0X38
7AEA: FF         RST         0X38
7AEB: FF         RST         0X38
7AEC: FF         RST         0X38
7AED: FF         RST         0X38
7AEE: FF         RST         0X38
7AEF: FF         RST         0X38
7AF0: FF         RST         0X38
7AF1: FF         RST         0X38
7AF2: FF         RST         0X38
7AF3: FF         RST         0X38
7AF4: FF         RST         0X38
7AF5: FF         RST         0X38
7AF6: FF         RST         0X38
7AF7: FF         RST         0X38
7AF8: FF         RST         0X38
7AF9: FF         RST         0X38
7AFA: FF         RST         0X38
7AFB: FF         RST         0X38
7AFC: FF         RST         0X38
7AFD: FF         RST         0X38
7AFE: FF         RST         0X38
7AFF: FF         RST         0X38
7B00: FF         RST         0X38
7B01: FF         RST         0X38
7B02: FF         RST         0X38
7B03: FF         RST         0X38
7B04: FF         RST         0X38
7B05: FF         RST         0X38
7B06: FF         RST         0X38
7B07: FF         RST         0X38
7B08: FF         RST         0X38
7B09: FF         RST         0X38
7B0A: FF         RST         0X38
7B0B: FF         RST         0X38
7B0C: FF         RST         0X38
7B0D: FF         RST         0X38
7B0E: FF         RST         0X38
7B0F: FF         RST         0X38
7B10: FF         RST         0X38
7B11: FF         RST         0X38
7B12: FF         RST         0X38
7B13: FF         RST         0X38
7B14: FF         RST         0X38
7B15: FF         RST         0X38
7B16: FF         RST         0X38
7B17: FF         RST         0X38
7B18: FF         RST         0X38
7B19: FF         RST         0X38
7B1A: FF         RST         0X38
7B1B: FF         RST         0X38
7B1C: FF         RST         0X38
7B1D: FF         RST         0X38
7B1E: FF         RST         0X38
7B1F: FF         RST         0X38
7B20: FF         RST         0X38
7B21: FF         RST         0X38
7B22: FF         RST         0X38
7B23: FF         RST         0X38
7B24: FF         RST         0X38
7B25: FF         RST         0X38
7B26: FF         RST         0X38
7B27: FF         RST         0X38
7B28: FF         RST         0X38
7B29: FF         RST         0X38
7B2A: FF         RST         0X38
7B2B: FF         RST         0X38
7B2C: FF         RST         0X38
7B2D: FF         RST         0X38
7B2E: FF         RST         0X38
7B2F: FF         RST         0X38
7B30: FF         RST         0X38
7B31: FF         RST         0X38
7B32: FF         RST         0X38
7B33: FF         RST         0X38
7B34: FF         RST         0X38
7B35: FF         RST         0X38
7B36: FF         RST         0X38
7B37: FF         RST         0X38
7B38: FF         RST         0X38
7B39: FF         RST         0X38
7B3A: FF         RST         0X38
7B3B: FF         RST         0X38
7B3C: FF         RST         0X38
7B3D: FF         RST         0X38
7B3E: FF         RST         0X38
7B3F: FF         RST         0X38
7B40: FF         RST         0X38
7B41: FF         RST         0X38
7B42: FF         RST         0X38
7B43: FF         RST         0X38
7B44: FF         RST         0X38
7B45: FF         RST         0X38
7B46: FF         RST         0X38
7B47: FF         RST         0X38
7B48: FF         RST         0X38
7B49: FF         RST         0X38
7B4A: FF         RST         0X38
7B4B: FF         RST         0X38
7B4C: FF         RST         0X38
7B4D: FF         RST         0X38
7B4E: FF         RST         0X38
7B4F: FF         RST         0X38
7B50: FF         RST         0X38
7B51: FF         RST         0X38
7B52: FF         RST         0X38
7B53: FF         RST         0X38
7B54: FF         RST         0X38
7B55: FF         RST         0X38
7B56: FF         RST         0X38
7B57: FF         RST         0X38
7B58: FF         RST         0X38
7B59: FF         RST         0X38
7B5A: FF         RST         0X38
7B5B: FF         RST         0X38
7B5C: FF         RST         0X38
7B5D: FF         RST         0X38
7B5E: FF         RST         0X38
7B5F: FF         RST         0X38
7B60: FF         RST         0X38
7B61: FF         RST         0X38
7B62: FF         RST         0X38
7B63: FF         RST         0X38
7B64: FF         RST         0X38
7B65: FF         RST         0X38
7B66: FF         RST         0X38
7B67: FF         RST         0X38
7B68: FF         RST         0X38
7B69: FF         RST         0X38
7B6A: FF         RST         0X38
7B6B: FF         RST         0X38
7B6C: FF         RST         0X38
7B6D: FF         RST         0X38
7B6E: FF         RST         0X38
7B6F: FF         RST         0X38
7B70: FF         RST         0X38
7B71: FF         RST         0X38
7B72: FF         RST         0X38
7B73: FF         RST         0X38
7B74: FF         RST         0X38
7B75: FF         RST         0X38
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