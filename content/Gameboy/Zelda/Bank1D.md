![Bank 1D](GBZelda.jpg)

# Bank 1D

>>> cpu Z80GB

>>> binary 4000:zelda.gb[74000:78000]

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: 4D         LD           C,L
4001: 61         LD           H,C
4002: 6B         LD           L,E
4003: 65         LD           H,L
4004: 2D         DEC         L
4005: 75         LD           (HL),L
4006: 70         LD           (HL),B
4007: 21 20 4A   LD           HL,$4A20
400A: 65         LD           H,L
400B: 77         LD           (HL),A
400C: 65         LD           H,L
400D: 6C         LD           L,H
400E: 73         LD           (HL),E
400F: 21 44 72   LD           HL,$7244
4012: 65         LD           H,L
4013: 73         LD           (HL),E
4014: 73         LD           (HL),E
4015: 65         LD           H,L
4016: 73         LD           (HL),E
4017: 21 20 20   LD           HL,$2020
401A: 49         LD           C,C
401B: 20 77      JR           NZ,$4094
401D: 61         LD           H,C
401E: 6E         LD           L,(HL)
401F: 74         LD           (HL),H
4020: 69         LD           L,C
4021: 74         LD           (HL),H
4022: 20 61      JR           NZ,$4085
4024: 6C         LD           L,H
4025: 6C         LD           L,H
4026: 21 20 20   LD           HL,$2020
4029: 53         LD           D,E
402A: 69         LD           L,C
402B: 67         LD           H,A
402C: 68         LD           L,B
402D: 2E 2E      LD           L,$2E
402F: 2E 41      LD           L,$41
4031: 6E         LD           L,(HL)
4032: 64         LD           H,H
4033: 20 73      JR           NZ,$40A8
4035: 6F         LD           L,A
4036: 6D         LD           L,L
4037: 65         LD           H,L
4038: 20 6E      JR           NZ,$40A8
403A: 65         LD           H,L
403B: 77         LD           (HL),A
403C: 20 20      JR           NZ,$405E
403E: 20 20      JR           NZ,$4060
4040: 61         LD           H,C
4041: 63         LD           H,E
4042: 63         LD           H,E
4043: 65         LD           H,L
4044: 73         LD           (HL),E
4045: 73         LD           (HL),E
4046: 6F         LD           L,A
4047: 72         LD           (HL),D
4048: 69         LD           L,C
4049: 65         LD           H,L
404A: 73         LD           (HL),E
404B: 20 20      JR           NZ,$406D
404D: 20 20      JR           NZ,$406F
404F: 20 77      JR           NZ,$40C8
4051: 6F         LD           L,A
4052: 75         LD           (HL),L
4053: 6C         LD           L,H
4054: 64         LD           H,H
4055: 20 62      JR           NZ,$40B9
4057: 65         LD           H,L
4058: 20 6E      JR           NZ,$40C8
405A: 69         LD           L,C
405B: 63         LD           H,E
405C: 65         LD           H,L
405D: 2E 2E      LD           L,$2E
405F: 2E FF      LD           L,$FF
4061: 4D         LD           C,L
4062: 61         LD           H,C
4063: 6B         LD           L,E
4064: 65         LD           H,L
4065: 2D         DEC         L
4066: 75         LD           (HL),L
4067: 70         LD           (HL),B
4068: 21 20 4A   LD           HL,$4A20
406B: 65         LD           H,L
406C: 77         LD           (HL),A
406D: 65         LD           H,L
406E: 6C         LD           L,H
406F: 73         LD           (HL),E
4070: 21 44 72   LD           HL,$7244
4073: 65         LD           H,L
4074: 73         LD           (HL),E
4075: 73         LD           (HL),E
4076: 65         LD           H,L
4077: 73         LD           (HL),E
4078: 21 20 20   LD           HL,$2020
407B: 49         LD           C,C
407C: 20 77      JR           NZ,$40F5
407E: 61         LD           H,C
407F: 6E         LD           L,(HL)
4080: 74         LD           (HL),H
4081: 69         LD           L,C
4082: 74         LD           (HL),H
4083: 20 61      JR           NZ,$40E6
4085: 6C         LD           L,H
4086: 6C         LD           L,H
4087: 21 20 20   LD           HL,$2020
408A: 53         LD           D,E
408B: 69         LD           L,C
408C: 67         LD           H,A
408D: 68         LD           L,B
408E: 2E 2E      LD           L,$2E
4090: 2E 41      LD           L,$41
4092: 6E         LD           L,(HL)
4093: 64         LD           H,H
4094: 20 73      JR           NZ,$4109
4096: 6F         LD           L,A
4097: 6D         LD           L,L
4098: 65         LD           H,L
4099: 20 6E      JR           NZ,$4109
409B: 65         LD           H,L
409C: 77         LD           (HL),A
409D: 20 20      JR           NZ,$40BF
409F: 20 20      JR           NZ,$40C1
40A1: 61         LD           H,C
40A2: 63         LD           H,E
40A3: 63         LD           H,E
40A4: 65         LD           H,L
40A5: 73         LD           (HL),E
40A6: 73         LD           (HL),E
40A7: 6F         LD           L,A
40A8: 72         LD           (HL),D
40A9: 69         LD           L,C
40AA: 65         LD           H,L
40AB: 73         LD           (HL),E
40AC: 20 20      JR           NZ,$40CE
40AE: 20 20      JR           NZ,$40D0
40B0: 20 77      JR           NZ,$4129
40B2: 6F         LD           L,A
40B3: 75         LD           (HL),L
40B4: 6C         LD           L,H
40B5: 64         LD           H,H
40B6: 20 62      JR           NZ,$411A
40B8: 65         LD           H,L
40B9: 20 6E      JR           NZ,$4129
40BB: 69         LD           L,C
40BC: 63         LD           H,E
40BD: 65         LD           H,L
40BE: 2E 2E      LD           L,$2E
40C0: 2E 4F      LD           L,$4F
40C2: 68         LD           L,B
40C3: 21 20 54   LD           HL,$5420
40C6: 68         LD           L,B
40C7: 61         LD           H,C
40C8: 74         LD           (HL),H
40C9: 20 52      JR           NZ,$411D
40CB: 69         LD           L,C
40CC: 62         LD           H,D
40CD: 62         LD           H,D
40CE: 6F         LD           L,A
40CF: 6E         LD           L,(HL)
40D0: 21 49 20   LD           HL,$2049
40D3: 6E         LD           L,(HL)
40D4: 65         LD           H,L
40D5: 65         LD           H,L
40D6: 64         LD           H,H
40D7: 20 69      JR           NZ,$4142
40D9: 74         LD           (HL),H
40DA: 21 20 20   LD           HL,$2020
40DD: 57         LD           D,A
40DE: 69         LD           L,C
40DF: 6C         LD           L,H
40E0: 6C         LD           L,H
40E1: 79         LD           A,C
40E2: 6F         LD           L,A
40E3: 75         LD           (HL),L
40E4: 20 74      JR           NZ,$415A
40E6: 72         LD           (HL),D
40E7: 61         LD           H,C
40E8: 64         LD           H,H
40E9: 65         LD           H,L
40EA: 20 66      JR           NZ,$4152
40EC: 6F         LD           L,A
40ED: 72         LD           (HL),D
40EE: 20 6D      JR           NZ,$415D
40F0: 79         LD           A,C
40F1: 64         LD           H,H
40F2: 6F         LD           L,A
40F3: 67         LD           H,A
40F4: 20 66      JR           NZ,$415C
40F6: 6F         LD           L,A
40F7: 6F         LD           L,A
40F8: 64         LD           H,H
40F9: 3F         CCF
40FA: 20 20      JR           NZ,$411C
40FC: 20 20      JR           NZ,$411E
40FE: 20 20      JR           NZ,$4120
4100: 20 20      JR           NZ,$4122
4102: 20 20      JR           NZ,$4124
4104: 20 59      JR           NZ,$415F
4106: 65         LD           H,L
4107: 73         LD           (HL),E
4108: 20 20      JR           NZ,$412A
410A: 4E         LD           C,(HL)
410B: 6F         LD           L,A
410C: 21 FE 59   LD           HL,$59FE
410F: 6F         LD           L,A
4110: 75         LD           (HL),L
4111: 20 65      JR           NZ,$4178
4113: 78         LD           A,B
4114: 63         LD           H,E
4115: 68         LD           L,B
4116: 61         LD           H,C
4117: 6E         LD           L,(HL)
4118: 67         LD           H,A
4119: 65         LD           H,L
411A: 64         LD           H,H
411B: 20 E1      JR           NZ,$40FE
411D: 20 66      JR           NZ,$4185
411F: 6F         LD           L,A
4120: 72         LD           (HL),D
4121: 20 E2      JR           NZ,$4105
4123: 21 20 49   LD           HL,$4920
4126: 74         LD           (HL),H
4127: 5E         LD           E,(HL)
4128: 73         LD           (HL),E
4129: 20 66      JR           NZ,$4191
412B: 75         LD           (HL),L
412C: 6C         LD           L,H
412D: 6C         LD           L,H
412E: 6F         LD           L,A
412F: 66         LD           H,(HL)
4130: 20 6A      JR           NZ,$419C
4132: 75         LD           (HL),L
4133: 69         LD           L,C
4134: 63         LD           H,E
4135: 79         LD           A,C
4136: 20 62      JR           NZ,$419A
4138: 65         LD           H,L
4139: 65         LD           H,L
413A: 66         LD           H,(HL)
413B: 21 FF 4C   LD           HL,$4CFF
413E: 75         LD           (HL),L
413F: 63         LD           H,E
4140: 6B         LD           L,E
4141: 79         LD           A,C
4142: 21 20 20   LD           HL,$2020
4145: 54         LD           D,H
4146: 68         LD           L,B
4147: 61         LD           H,C
4148: 6E         LD           L,(HL)
4149: 6B         LD           L,E
414A: 73         LD           (HL),E
414B: 21 20 57   LD           HL,$5720
414E: 65         LD           H,L
414F: 6C         LD           L,H
4150: 6C         LD           L,H
4151: 2C         INC         L
4152: 20 68      JR           NZ,$41BC
4154: 65         LD           H,L
4155: 72         LD           (HL),D
4156: 65         LD           H,L
4157: 5E         LD           E,(HL)
4158: 73         LD           (HL),E
4159: 20 20      JR           NZ,$417B
415B: 20 20      JR           NZ,$417D
415D: 79         LD           A,C
415E: 6F         LD           L,A
415F: 75         LD           (HL),L
4160: 72         LD           (HL),D
4161: 20 E2      JR           NZ,$4145
4163: 21 FF 45   LD           HL,$45FF
4166: 68         LD           L,B
4167: 3F         CCF
4168: 21 20 20   LD           HL,$2020
416B: 49         LD           C,C
416C: 20 63      JR           NZ,$41D1
416E: 61         LD           H,C
416F: 6E         LD           L,(HL)
4170: 5E         LD           E,(HL)
4171: 74         LD           (HL),H
4172: 20 20      JR           NZ,$4194
4174: 20 62      JR           NZ,$41D8
4176: 65         LD           H,L
4177: 6C         LD           L,H
4178: 69         LD           L,C
4179: 65         LD           H,L
417A: 76         HALT
417B: 65         LD           H,L
417C: 20 69      JR           NZ,$41E7
417E: 74         LD           (HL),H
417F: 21 20 20   LD           HL,$2020
4182: 59         LD           E,C
4183: 6F         LD           L,A
4184: 75         LD           (HL),L
4185: 61         LD           H,C
4186: 72         LD           (HL),D
4187: 65         LD           H,L
4188: 20 74      JR           NZ,$41FE
418A: 68         LD           L,B
418B: 65         LD           H,L
418C: 20 77      JR           NZ,$4205
418E: 6F         LD           L,A
418F: 72         LD           (HL),D
4190: 73         LD           (HL),E
4191: 74         LD           (HL),H
4192: 21 21 FF   LD           HL,$FF21
4195: 49         LD           C,C
4196: 20 61      JR           NZ,$41F9
4198: 6D         LD           L,L
4199: 20 4D      JR           NZ,$41E8
419B: 61         LD           H,C
419C: 6E         LD           L,(HL)
419D: 62         LD           H,D
419E: 6F         LD           L,A
419F: 2C         INC         L
41A0: 20 20      JR           NZ,$41C2
41A2: 20 20      JR           NZ,$41C4
41A4: 20 63      JR           NZ,$4209
41A6: 68         LD           L,B
41A7: 69         LD           L,C
41A8: 6C         LD           L,H
41A9: 64         LD           H,H
41AA: 20 6F      JR           NZ,$421B
41AC: 66         LD           H,(HL)
41AD: 20 74      JR           NZ,$4223
41AF: 68         LD           L,B
41B0: 65         LD           H,L
41B1: 20 53      JR           NZ,$4206
41B3: 75         LD           (HL),L
41B4: 6E         LD           L,(HL)
41B5: 46         LD           B,(HL)
41B6: 69         LD           L,C
41B7: 73         LD           (HL),E
41B8: 68         LD           L,B
41B9: 21 20 20   LD           HL,$2020
41BC: 48         LD           C,B
41BD: 61         LD           H,C
41BE: 76         HALT
41BF: 65         LD           H,L
41C0: 20 79      JR           NZ,$423B
41C2: 6F         LD           L,A
41C3: 75         LD           (HL),L
41C4: 20 67      JR           NZ,$422D
41C6: 6F         LD           L,A
41C7: 74         LD           (HL),H
41C8: 20 61      JR           NZ,$422B
41CA: 6E         LD           L,(HL)
41CB: 20 4F      JR           NZ,$421C
41CD: 63         LD           H,E
41CE: 61         LD           H,C
41CF: 72         LD           (HL),D
41D0: 69         LD           L,C
41D1: 6E         LD           L,(HL)
41D2: 61         LD           H,C
41D3: 3F         CCF
41D4: 20 20      JR           NZ,$41F6
41D6: 20 20      JR           NZ,$41F8
41D8: 20 59      JR           NZ,$4233
41DA: 65         LD           H,L
41DB: 73         LD           (HL),E
41DC: 20 20      JR           NZ,$41FE
41DE: 4E         LD           C,(HL)
41DF: 6F         LD           L,A
41E0: FE 56      CP           $56
41E2: 65         LD           H,L
41E3: 72         LD           (HL),D
41E4: 79         LD           A,C
41E5: 20 77      JR           NZ,$425E
41E7: 65         LD           H,L
41E8: 6C         LD           L,H
41E9: 6C         LD           L,H
41EA: 2E 2E      LD           L,$2E
41EC: 2E 20      LD           L,$20
41EE: 20 20      JR           NZ,$4210
41F0: 20 47      JR           NZ,$4239
41F2: 6C         LD           L,H
41F3: 75         LD           (HL),L
41F4: 62         LD           H,D
41F5: 20 42      JR           NZ,$4239
41F7: 6C         LD           L,H
41F8: 75         LD           (HL),L
41F9: 62         LD           H,D
41FA: 20 42      JR           NZ,$423E
41FC: 6C         LD           L,H
41FD: 6F         LD           L,A
41FE: 6F         LD           L,A
41FF: 70         LD           (HL),B
4200: 21 FF 41   LD           HL,$41FF
4203: 68         LD           L,B
4204: 61         LD           H,C
4205: 68         LD           L,B
4206: 61         LD           H,C
4207: 21 20 20   LD           HL,$2020
420A: 54         LD           D,H
420B: 68         LD           L,B
420C: 65         LD           H,L
420D: 6E         LD           L,(HL)
420E: 20 49      JR           NZ,$4259
4210: 20 20      JR           NZ,$4232
4212: 63         LD           H,E
4213: 61         LD           H,C
4214: 6E         LD           L,(HL)
4215: 20 74      JR           NZ,$428B
4217: 65         LD           H,L
4218: 61         LD           H,C
4219: 63         LD           H,E
421A: 68         LD           L,B
421B: 20 79      JR           NZ,$4296
421D: 6F         LD           L,A
421E: 75         LD           (HL),L
421F: 20 6D      JR           NZ,$428E
4221: 79         LD           A,C
4222: 73         LD           (HL),E
4223: 6F         LD           L,A
4224: 6E         LD           L,(HL)
4225: 67         LD           H,A
4226: 21 20 42   LD           HL,$4220
4229: 6C         LD           L,H
422A: 6F         LD           L,A
422B: 6F         LD           L,A
422C: 70         LD           (HL),B
422D: 21 FF 59   LD           HL,$59FF
4230: 6F         LD           L,A
4231: 75         LD           (HL),L
4232: 5E         LD           E,(HL)
4233: 76         HALT
4234: 65         LD           H,L
4235: 20 6C      JR           NZ,$42A3
4237: 65         LD           H,L
4238: 61         LD           H,C
4239: 72         LD           (HL),D
423A: 6E         LD           L,(HL)
423B: 65         LD           H,L
423C: 64         LD           H,H
423D: 20 20      JR           NZ,$425F
423F: 4D         LD           C,L
4240: 61         LD           H,C
4241: 6E         LD           L,(HL)
4242: 62         LD           H,D
4243: 6F         LD           L,A
4244: 5E         LD           E,(HL)
4245: 73         LD           (HL),E
4246: 20 4D      JR           NZ,$4295
4248: 61         LD           H,C
4249: 6D         LD           L,L
424A: 62         LD           H,D
424B: 6F         LD           L,A
424C: 21 20 20   LD           HL,$2020
424F: 57         LD           D,A
4250: 68         LD           L,B
4251: 65         LD           H,L
4252: 6E         LD           L,(HL)
4253: 20 79      JR           NZ,$42CE
4255: 6F         LD           L,A
4256: 75         LD           (HL),L
4257: 20 67      JR           NZ,$42C0
4259: 65         LD           H,L
425A: 74         LD           (HL),H
425B: 20 6F      JR           NZ,$42CC
425D: 75         LD           (HL),L
425E: 74         LD           (HL),H
425F: 6F         LD           L,A
4260: 66         LD           H,(HL)
4261: 20 74      JR           NZ,$42D7
4263: 68         LD           L,B
4264: 65         LD           H,L
4265: 20 77      JR           NZ,$42DE
4267: 61         LD           H,C
4268: 74         LD           (HL),H
4269: 65         LD           H,L
426A: 72         LD           (HL),D
426B: 2C         INC         L
426C: 20 20      JR           NZ,$428E
426E: 20 70      JR           NZ,$42E0
4270: 6C         LD           L,H
4271: 61         LD           H,C
4272: 79         LD           A,C
4273: 20 69      JR           NZ,$42DE
4275: 74         LD           (HL),H
4276: 21 FF 49   LD           HL,$49FF
4279: 20 61      JR           NZ,$42DC
427B: 6D         LD           L,L
427C: 20 4D      JR           NZ,$42CB
427E: 61         LD           H,C
427F: 6E         LD           L,(HL)
4280: 62         LD           H,D
4281: 6F         LD           L,A
4282: 2C         INC         L
4283: 20 20      JR           NZ,$42A5
4285: 20 20      JR           NZ,$42A7
4287: 20 63      JR           NZ,$42EC
4289: 68         LD           L,B
428A: 69         LD           L,C
428B: 6C         LD           L,H
428C: 64         LD           H,H
428D: 20 6F      JR           NZ,$42FE
428F: 66         LD           H,(HL)
4290: 20 74      JR           NZ,$4306
4292: 68         LD           L,B
4293: 65         LD           H,L
4294: 20 53      JR           NZ,$42E9
4296: 75         LD           (HL),L
4297: 6E         LD           L,(HL)
4298: 46         LD           B,(HL)
4299: 69         LD           L,C
429A: 73         LD           (HL),E
429B: 68         LD           L,B
429C: 21 20 20   LD           HL,$2020
429F: 57         LD           D,A
42A0: 68         LD           L,B
42A1: 65         LD           H,L
42A2: 6E         LD           L,(HL)
42A3: 20 79      JR           NZ,$431E
42A5: 6F         LD           L,A
42A6: 75         LD           (HL),L
42A7: 20 70      JR           NZ,$4319
42A9: 6C         LD           L,H
42AA: 61         LD           H,C
42AB: 79         LD           A,C
42AC: 20 6D      JR           NZ,$431B
42AE: 79         LD           A,C
42AF: 20 4D      JR           NZ,$42FE
42B1: 61         LD           H,C
42B2: 6D         LD           L,L
42B3: 62         LD           H,D
42B4: 6F         LD           L,A
42B5: 2C         INC         L
42B6: 20 20      JR           NZ,$42D8
42B8: 79         LD           A,C
42B9: 6F         LD           L,A
42BA: 75         LD           (HL),L
42BB: 20 63      JR           NZ,$4320
42BD: 61         LD           H,C
42BE: 6E         LD           L,(HL)
42BF: 20 77      JR           NZ,$4338
42C1: 61         LD           H,C
42C2: 72         LD           (HL),D
42C3: 70         LD           (HL),B
42C4: 20 74      JR           NZ,$433A
42C6: 6F         LD           L,A
42C7: 20 4D      JR           NZ,$4316
42C9: 61         LD           H,C
42CA: 6E         LD           L,(HL)
42CB: 62         LD           H,D
42CC: 6F         LD           L,A
42CD: 20 50      JR           NZ,$431F
42CF: 6F         LD           L,A
42D0: 6E         LD           L,(HL)
42D1: 64         LD           H,H
42D2: 21 20 20   LD           HL,$2020
42D5: 54         LD           D,H
42D6: 72         LD           (HL),D
42D7: 79         LD           A,C
42D8: 74         LD           (HL),H
42D9: 68         LD           L,B
42DA: 69         LD           L,C
42DB: 73         LD           (HL),E
42DC: 20 74      JR           NZ,$4352
42DE: 75         LD           (HL),L
42DF: 6E         LD           L,(HL)
42E0: 65         LD           H,L
42E1: 20 69      JR           NZ,$434C
42E3: 6E         LD           L,(HL)
42E4: 20 74      JR           NZ,$435A
42E6: 68         LD           L,B
42E7: 65         LD           H,L
42E8: 64         LD           H,H
42E9: 75         LD           (HL),L
42EA: 6E         LD           L,(HL)
42EB: 67         LD           H,A
42EC: 65         LD           H,L
42ED: 6F         LD           L,A
42EE: 6E         LD           L,(HL)
42EF: 73         LD           (HL),E
42F0: 2C         INC         L
42F1: 20 74      JR           NZ,$4367
42F3: 6F         LD           L,A
42F4: 6F         LD           L,A
42F5: 21 20 20   LD           HL,$2020
42F8: 43         LD           B,E
42F9: 68         LD           L,B
42FA: 61         LD           H,C
42FB: 2D         DEC         L
42FC: 63         LD           H,E
42FD: 68         LD           L,B
42FE: 61         LD           H,C
42FF: 2D         DEC         L
4300: 63         LD           H,E
4301: 68         LD           L,B
4302: 61         LD           H,C
4303: 21 FF 41   LD           HL,$41FF
4306: 68         LD           L,B
4307: 61         LD           H,C
4308: 2E 2E      LD           L,$2E
430A: 2E 20      LD           L,$20
430C: 59         LD           E,C
430D: 6F         LD           L,A
430E: 75         LD           (HL),L
430F: 20 64      JR           NZ,$4375
4311: 6F         LD           L,A
4312: 6E         LD           L,(HL)
4313: 5E         LD           E,(HL)
4314: 74         LD           (HL),H
4315: 68         LD           L,B
4316: 61         LD           H,C
4317: 76         HALT
4318: 65         LD           H,L
4319: 20 61      JR           NZ,$437C
431B: 6E         LD           L,(HL)
431C: 20 4F      JR           NZ,$436D
431E: 63         LD           H,E
431F: 61         LD           H,C
4320: 72         LD           (HL),D
4321: 69         LD           L,C
4322: 6E         LD           L,(HL)
4323: 61         LD           H,C
4324: 2C         INC         L
4325: 73         LD           (HL),E
4326: 6F         LD           L,A
4327: 2E 2E      LD           L,$2E
4329: 2E 47      LD           L,$47
432B: 6C         LD           L,H
432C: 75         LD           (HL),L
432D: 62         LD           H,D
432E: 20 67      JR           NZ,$4397
4330: 6C         LD           L,H
4331: 75         LD           (HL),L
4332: 62         LD           H,D
4333: 21 FF 43   LD           HL,$43FF
4336: 68         LD           L,B
4337: 69         LD           L,C
4338: 63         LD           H,E
4339: 6B         LD           L,E
433A: 65         LD           H,L
433B: 6E         LD           L,(HL)
433C: 73         LD           (HL),E
433D: 20 74      JR           NZ,$43B3
433F: 68         LD           L,B
4340: 65         LD           H,L
4341: 73         LD           (HL),E
4342: 65         LD           H,L
4343: 20 20      JR           NZ,$4365
4345: 64         LD           H,H
4346: 61         LD           H,C
4347: 79         LD           A,C
4348: 73         LD           (HL),E
4349: 20 64      JR           NZ,$43AF
434B: 6F         LD           L,A
434C: 6E         LD           L,(HL)
434D: 5E         LD           E,(HL)
434E: 74         LD           (HL),H
434F: 20 68      JR           NZ,$43B9
4351: 61         LD           H,C
4352: 76         HALT
4353: 65         LD           H,L
4354: 20 74      JR           NZ,$43CA
4356: 68         LD           L,B
4357: 65         LD           H,L
4358: 20 66      JR           NZ,$43C0
435A: 69         LD           L,C
435B: 67         LD           H,A
435C: 68         LD           L,B
435D: 74         LD           (HL),H
435E: 69         LD           L,C
435F: 6E         LD           L,(HL)
4360: 67         LD           H,A
4361: 20 20      JR           NZ,$4383
4363: 20 20      JR           NZ,$4385
4365: 73         LD           (HL),E
4366: 70         LD           (HL),B
4367: 69         LD           L,C
4368: 72         LD           (HL),D
4369: 69         LD           L,C
436A: 74         LD           (HL),H
436B: 20 74      JR           NZ,$43E1
436D: 68         LD           L,B
436E: 65         LD           H,L
436F: 79         LD           A,C
4370: 20 75      JR           NZ,$43E7
4372: 73         LD           (HL),E
4373: 65         LD           H,L
4374: 64         LD           H,H
4375: 74         LD           (HL),H
4376: 6F         LD           L,A
4377: 21 20 20   LD           HL,$2020
437A: 49         LD           C,C
437B: 6E         LD           L,(HL)
437C: 20 74      JR           NZ,$43F2
437E: 68         LD           L,B
437F: 65         LD           H,L
4380: 20 6F      JR           NZ,$43F1
4382: 6C         LD           L,H
4383: 64         LD           H,H
4384: 20 64      JR           NZ,$43EA
4386: 61         LD           H,C
4387: 79         LD           A,C
4388: 73         LD           (HL),E
4389: 2C         INC         L
438A: 20 74      JR           NZ,$4400
438C: 68         LD           L,B
438D: 65         LD           H,L
438E: 79         LD           A,C
438F: 20 63      JR           NZ,$43F4
4391: 6F         LD           L,A
4392: 75         LD           (HL),L
4393: 6C         LD           L,H
4394: 64         LD           H,H
4395: 66         LD           H,(HL)
4396: 6C         LD           L,H
4397: 79         LD           A,C
4398: 2C         INC         L
4399: 20 66      JR           NZ,$4401
439B: 6C         LD           L,H
439C: 61         LD           H,C
439D: 70         LD           (HL),B
439E: 20 66      JR           NZ,$4406
43A0: 6C         LD           L,H
43A1: 61         LD           H,C
43A2: 70         LD           (HL),B
43A3: 21 20 42   LD           HL,$4220
43A6: 75         LD           (HL),L
43A7: 74         LD           (HL),H
43A8: 20 6E      JR           NZ,$4418
43AA: 6F         LD           L,A
43AB: 77         LD           (HL),A
43AC: 2C         INC         L
43AD: 20 73      JR           NZ,$4422
43AF: 65         LD           H,L
43B0: 65         LD           H,L
43B1: 3F         CCF
43B2: 20 20      JR           NZ,$43D4
43B4: 20 43      JR           NZ,$43F9
43B6: 6C         LD           L,H
43B7: 75         LD           (HL),L
43B8: 63         LD           H,E
43B9: 6B         LD           L,E
43BA: 20 63      JR           NZ,$441F
43BC: 6C         LD           L,H
43BD: 75         LD           (HL),L
43BE: 63         LD           H,E
43BF: 6B         LD           L,E
43C0: 21 FF 57   LD           HL,$57FF
43C3: 6F         LD           L,A
43C4: 77         LD           (HL),A
43C5: 21 20 20   LD           HL,$2020
43C8: 41         LD           B,C
43C9: 6D         LD           L,L
43CA: 61         LD           H,C
43CB: 7A         LD           A,D
43CC: 69         LD           L,C
43CD: 6E         LD           L,(HL)
43CE: 67         LD           H,A
43CF: 21 20 20   LD           HL,$2020
43D2: 54         LD           D,H
43D3: 68         LD           L,B
43D4: 61         LD           H,C
43D5: 74         LD           (HL),H
43D6: 20 72      JR           NZ,$444A
43D8: 6F         LD           L,A
43D9: 6F         LD           L,A
43DA: 73         LD           (HL),E
43DB: 74         LD           (HL),H
43DC: 65         LD           H,L
43DD: 72         LD           (HL),D
43DE: 20 69      JR           NZ,$4449
43E0: 73         LD           (HL),E
43E1: 20 61      JR           NZ,$4444
43E3: 63         LD           H,E
43E4: 74         LD           (HL),H
43E5: 75         LD           (HL),L
43E6: 61         LD           H,C
43E7: 6C         LD           L,H
43E8: 6C         LD           L,H
43E9: 79         LD           A,C
43EA: 20 66      JR           NZ,$4452
43EC: 6C         LD           L,H
43ED: 79         LD           A,C
43EE: 69         LD           L,C
43EF: 6E         LD           L,(HL)
43F0: 67         LD           H,A
43F1: 21 49 74   LD           HL,$7449
43F4: 5E         LD           E,(HL)
43F5: 73         LD           (HL),E
43F6: 20 6A      JR           NZ,$4462
43F8: 75         LD           (HL),L
43F9: 73         LD           (HL),E
43FA: 74         LD           (HL),H
43FB: 20 6C      JR           NZ,$4469
43FD: 69         LD           L,C
43FE: 6B         LD           L,E
43FF: 65         LD           H,L
4400: 20 49      JR           NZ,$444B
4402: 73         LD           (HL),E
4403: 61         LD           H,C
4404: 69         LD           L,C
4405: 64         LD           H,H
4406: 2C         INC         L
4407: 20 65      JR           NZ,$446E
4409: 68         LD           L,B
440A: 3F         CCF
440B: 20 20      JR           NZ,$442D
440D: 48         LD           C,B
440E: 61         LD           H,C
440F: 76         HALT
4410: 65         LD           H,L
4411: 20 79      JR           NZ,$448C
4413: 6F         LD           L,A
4414: 75         LD           (HL),L
4415: 20 74      JR           NZ,$448B
4417: 72         LD           (HL),D
4418: 69         LD           L,C
4419: 65         LD           H,L
441A: 64         LD           H,H
441B: 20 74      JR           NZ,$4491
441D: 6F         LD           L,A
441E: 20 20      JR           NZ,$4440
4420: 20 20      JR           NZ,$4442
4422: 68         LD           L,B
4423: 6F         LD           L,A
4424: 6C         LD           L,H
4425: 64         LD           H,H
4426: 20 68      JR           NZ,$4490
4428: 69         LD           L,C
4429: 6D         LD           L,L
442A: 20 6F      JR           NZ,$449B
442C: 76         HALT
442D: 65         LD           H,L
442E: 72         LD           (HL),D
442F: 20 20      JR           NZ,$4451
4431: 20 79      JR           NZ,$44AC
4433: 6F         LD           L,A
4434: 75         LD           (HL),L
4435: 72         LD           (HL),D
4436: 20 68      JR           NZ,$44A0
4438: 65         LD           H,L
4439: 61         LD           H,C
443A: 64         LD           H,H
443B: 3F         CCF
443C: 20 43      JR           NZ,$4481
443E: 6C         LD           L,H
443F: 75         LD           (HL),L
4440: 63         LD           H,E
4441: 6B         LD           L,E
4442: 43         LD           B,E
4443: 6C         LD           L,H
4444: 75         LD           (HL),L
4445: 63         LD           H,E
4446: 6B         LD           L,E
4447: 21 FF 57   LD           HL,$57FF
444A: 6F         LD           L,A
444B: 6F         LD           L,A
444C: 6F         LD           L,A
444D: 21 20 20   LD           HL,$2020
4450: 46         LD           B,(HL)
4451: 69         LD           L,C
4452: 6E         LD           L,(HL)
4453: 61         LD           H,C
4454: 6C         LD           L,H
4455: 6C         LD           L,H
4456: 79         LD           A,C
4457: 21 20 54   LD           HL,$5420
445A: 68         LD           L,B
445B: 69         LD           L,C
445C: 73         LD           (HL),E
445D: 20 66      JR           NZ,$44C5
445F: 6C         LD           L,H
4460: 79         LD           A,C
4461: 69         LD           L,C
4462: 6E         LD           L,(HL)
4463: 67         LD           H,A
4464: 20 20      JR           NZ,$4486
4466: 20 20      JR           NZ,$4488
4468: 20 72      JR           NZ,$44DC
446A: 6F         LD           L,A
446B: 6F         LD           L,A
446C: 73         LD           (HL),E
446D: 74         LD           (HL),H
446E: 65         LD           H,L
446F: 72         LD           (HL),D
4470: 20 69      JR           NZ,$44DB
4472: 73         LD           (HL),E
4473: 20 74      JR           NZ,$44E9
4475: 68         LD           L,B
4476: 65         LD           H,L
4477: 20 20      JR           NZ,$4499
4479: 67         LD           H,A
447A: 72         LD           (HL),D
447B: 65         LD           H,L
447C: 61         LD           H,C
447D: 74         LD           (HL),H
447E: 65         LD           H,L
447F: 73         LD           (HL),E
4480: 74         LD           (HL),H
4481: 21 FF 20   LD           HL,$20FF
4484: 48         LD           C,B
4485: 65         LD           H,L
4486: 72         LD           (HL),D
4487: 65         LD           H,L
4488: 20 53      JR           NZ,$44DD
448A: 6C         LD           L,H
448B: 65         LD           H,L
448C: 65         LD           H,L
448D: 70         LD           (HL),B
448E: 73         LD           (HL),E
448F: 20 54      JR           NZ,$44E5
4491: 68         LD           L,B
4492: 65         LD           H,L
4493: 20 46      JR           NZ,$44DB
4495: 6C         LD           L,H
4496: 79         LD           A,C
4497: 69         LD           L,C
4498: 6E         LD           L,(HL)
4499: 67         LD           H,A
449A: 20 52      JR           NZ,$44EE
449C: 6F         LD           L,A
449D: 6F         LD           L,A
449E: 73         LD           (HL),E
449F: 74         LD           (HL),H
44A0: 65         LD           H,L
44A1: 72         LD           (HL),D
44A2: FF         RST         0X38
44A3: 45         LD           B,L
44A4: 6E         LD           L,(HL)
44A5: 6E         LD           L,(HL)
44A6: 68         LD           L,B
44A7: 3F         CCF
44A8: 20 20      JR           NZ,$44CA
44AA: 57         LD           D,A
44AB: 68         LD           L,B
44AC: 6F         LD           L,A
44AD: 5E         LD           E,(HL)
44AE: 73         LD           (HL),E
44AF: 20 20      JR           NZ,$44D1
44B1: 20 20      JR           NZ,$44D3
44B3: 74         LD           (HL),H
44B4: 68         LD           L,B
44B5: 69         LD           L,C
44B6: 73         LD           (HL),E
44B7: 20 73      JR           NZ,$452C
44B9: 75         LD           (HL),L
44BA: 73         LD           (HL),E
44BB: 70         LD           (HL),B
44BC: 69         LD           L,C
44BD: 63         LD           H,E
44BE: 69         LD           L,C
44BF: 6F         LD           L,A
44C0: 75         LD           (HL),L
44C1: 73         LD           (HL),E
44C2: 2D         DEC         L
44C3: 6C         LD           L,H
44C4: 6F         LD           L,A
44C5: 6F         LD           L,A
44C6: 6B         LD           L,E
44C7: 69         LD           L,C
44C8: 6E         LD           L,(HL)
44C9: 67         LD           H,A
44CA: 20 72      JR           NZ,$453E
44CC: 75         LD           (HL),L
44CD: 6E         LD           L,(HL)
44CE: 74         LD           (HL),H
44CF: 3F         CCF
44D0: 21 20 20   LD           HL,$2020
44D3: 4F         LD           C,A
44D4: 6B         LD           L,E
44D5: 61         LD           H,C
44D6: 79         LD           A,C
44D7: 20 62      JR           NZ,$453B
44D9: 6F         LD           L,A
44DA: 79         LD           A,C
44DB: 73         LD           (HL),E
44DC: 2C         INC         L
44DD: 20 6C      JR           NZ,$454B
44DF: 65         LD           H,L
44E0: 74         LD           (HL),H
44E1: 5E         LD           E,(HL)
44E2: 73         LD           (HL),E
44E3: 67         LD           H,A
44E4: 65         LD           H,L
44E5: 74         LD           (HL),H
44E6: 20 72      JR           NZ,$455A
44E8: 69         LD           L,C
44E9: 64         LD           H,H
44EA: 64         LD           H,H
44EB: 61         LD           H,C
44EC: 20 68      JR           NZ,$4556
44EE: 69         LD           L,C
44EF: 6D         LD           L,L
44F0: 21 FF 59   LD           HL,$59FF
44F3: 6F         LD           L,A
44F4: 75         LD           (HL),L
44F5: 20 6D      JR           NZ,$4564
44F7: 75         LD           (HL),L
44F8: 73         LD           (HL),E
44F9: 74         LD           (HL),H
44FA: 20 62      JR           NZ,$455E
44FC: 65         LD           H,L
44FD: 20 61      JR           NZ,$4560
44FF: 6E         LD           L,(HL)
4500: 20 20      JR           NZ,$4522
4502: 61         LD           H,C
4503: 73         LD           (HL),E
4504: 73         LD           (HL),E
4505: 61         LD           H,C
4506: 73         LD           (HL),E
4507: 73         LD           (HL),E
4508: 69         LD           L,C
4509: 6E         LD           L,(HL)
450A: 20 73      JR           NZ,$457F
450C: 65         LD           H,L
450D: 6E         LD           L,(HL)
450E: 74         LD           (HL),H
450F: 20 62      JR           NZ,$4573
4511: 79         LD           A,C
4512: 4D         LD           C,L
4513: 61         LD           H,C
4514: 64         LD           H,H
4515: 61         LD           H,C
4516: 6D         LD           L,L
4517: 20 4D      JR           NZ,$4566
4519: 65         LD           H,L
451A: 6F         LD           L,A
451B: 77         LD           (HL),A
451C: 4D         LD           C,L
451D: 65         LD           H,L
451E: 6F         LD           L,A
451F: 77         LD           (HL),A
4520: 20 20      JR           NZ,$4542
4522: 74         LD           (HL),H
4523: 6F         LD           L,A
4524: 20 72      JR           NZ,$4598
4526: 65         LD           H,L
4527: 73         LD           (HL),E
4528: 63         LD           H,E
4529: 75         LD           (HL),L
452A: 65         LD           H,L
452B: 20 74      JR           NZ,$45A1
452D: 68         LD           L,B
452E: 65         LD           H,L
452F: 20 20      JR           NZ,$4551
4531: 20 6D      JR           NZ,$45A0
4533: 75         LD           (HL),L
4534: 74         LD           (HL),H
4535: 74         LD           (HL),H
4536: 21 20 20   LD           HL,$2020
4539: 59         LD           E,C
453A: 6F         LD           L,A
453B: 75         LD           (HL),L
453C: 20 63      JR           NZ,$45A1
453E: 61         LD           H,C
453F: 6D         LD           L,L
4540: 65         LD           H,L
4541: 20 68      JR           NZ,$45AB
4543: 65         LD           H,L
4544: 72         LD           (HL),D
4545: 65         LD           H,L
4546: 20 74      JR           NZ,$45BC
4548: 6F         LD           L,A
4549: 20 67      JR           NZ,$45B2
454B: 65         LD           H,L
454C: 74         LD           (HL),H
454D: 20 6D      JR           NZ,$45BC
454F: 65         LD           H,L
4550: 2C         INC         L
4551: 20 62      JR           NZ,$45B5
4553: 75         LD           (HL),L
4554: 74         LD           (HL),H
4555: 20 69      JR           NZ,$45C0
4557: 74         LD           (HL),H
4558: 20 69      JR           NZ,$45C3
455A: 73         LD           (HL),E
455B: 20 49      JR           NZ,$45A6
455D: 20 77      JR           NZ,$45D6
455F: 68         LD           L,B
4560: 6F         LD           L,A
4561: 20 77      JR           NZ,$45DA
4563: 69         LD           L,C
4564: 6C         LD           L,H
4565: 6C         LD           L,H
4566: 20 67      JR           NZ,$45CF
4568: 65         LD           H,L
4569: 74         LD           (HL),H
456A: 20 79      JR           NZ,$45E5
456C: 6F         LD           L,A
456D: 75         LD           (HL),L
456E: 21 21 FF   LD           HL,$FF21
4571: 4F         LD           C,A
4572: 68         LD           L,B
4573: 2C         INC         L
4574: 20 23      JR           NZ,$4599
4576: 23         INC         HL
4577: 23         INC         HL
4578: 23         INC         HL
4579: 23         INC         HL
457A: 2E 20      LD           L,$20
457C: 20 49      JR           NZ,$45C7
457E: 20 20      JR           NZ,$45A0
4580: 20 6F      JR           NZ,$45F1
4582: 66         LD           H,(HL)
4583: 74         LD           (HL),H
4584: 65         LD           H,L
4585: 6E         LD           L,(HL)
4586: 20 63      JR           NZ,$45EB
4588: 6F         LD           L,A
4589: 6D         LD           L,L
458A: 65         LD           H,L
458B: 20 74      JR           NZ,$4601
458D: 6F         LD           L,A
458E: 20 20      JR           NZ,$45B0
4590: 20 74      JR           NZ,$4606
4592: 68         LD           L,B
4593: 69         LD           L,C
4594: 73         LD           (HL),E
4595: 20 76      JR           NZ,$460D
4597: 69         LD           L,C
4598: 6C         LD           L,H
4599: 6C         LD           L,H
459A: 61         LD           H,C
459B: 67         LD           H,A
459C: 65         LD           H,L
459D: 20 74      JR           NZ,$4613
459F: 6F         LD           L,A
45A0: 20 73      JR           NZ,$4615
45A2: 69         LD           L,C
45A3: 6E         LD           L,(HL)
45A4: 67         LD           H,A
45A5: 2C         INC         L
45A6: 20 74      JR           NZ,$461C
45A8: 6F         LD           L,A
45A9: 6F         LD           L,A
45AA: 21 20 20   LD           HL,$2020
45AD: 49         LD           C,C
45AE: 74         LD           (HL),H
45AF: 20 20      JR           NZ,$45D1
45B1: 73         LD           (HL),E
45B2: 65         LD           H,L
45B3: 65         LD           H,L
45B4: 6D         LD           L,L
45B5: 73         LD           (HL),E
45B6: 20 74      JR           NZ,$462C
45B8: 68         LD           L,B
45B9: 61         LD           H,C
45BA: 74         LD           (HL),H
45BB: 20 6A      JR           NZ,$4627
45BD: 75         LD           (HL),L
45BE: 73         LD           (HL),E
45BF: 74         LD           (HL),H
45C0: 20 61      JR           NZ,$4623
45C2: 62         LD           H,D
45C3: 6F         LD           L,A
45C4: 75         LD           (HL),L
45C5: 74         LD           (HL),H
45C6: 20 65      JR           NZ,$462D
45C8: 76         HALT
45C9: 65         LD           H,L
45CA: 72         LD           (HL),D
45CB: 79         LD           A,C
45CC: 6F         LD           L,A
45CD: 6E         LD           L,(HL)
45CE: 65         LD           H,L
45CF: 20 20      JR           NZ,$45F1
45D1: 6C         LD           L,H
45D2: 6F         LD           L,A
45D3: 76         HALT
45D4: 65         LD           H,L
45D5: 73         LD           (HL),E
45D6: 20 6D      JR           NZ,$4645
45D8: 79         LD           A,C
45D9: 20 5E      JR           NZ,$4639
45DB: 42         LD           B,D
45DC: 61         LD           H,C
45DD: 6C         LD           L,H
45DE: 6C         LD           L,H
45DF: 61         LD           H,C
45E0: 64         LD           H,H
45E1: 6F         LD           L,A
45E2: 66         LD           H,(HL)
45E3: 20 74      JR           NZ,$4659
45E5: 68         LD           L,B
45E6: 65         LD           H,L
45E7: 20 57      JR           NZ,$4640
45E9: 69         LD           L,C
45EA: 6E         LD           L,(HL)
45EB: 64         LD           H,H
45EC: 20 20      JR           NZ,$460E
45EE: 20 20      JR           NZ,$4610
45F0: 20 46      JR           NZ,$4638
45F2: 69         LD           L,C
45F3: 73         LD           (HL),E
45F4: 68         LD           L,B
45F5: 21 5E 20   LD           HL,$205E
45F8: 20 23      JR           NZ,$461D
45FA: 23         INC         HL
45FB: 23         INC         HL
45FC: 23         INC         HL
45FD: 23         INC         HL
45FE: 2C         INC         L
45FF: 20 20      JR           NZ,$4621
4601: 77         LD           (HL),A
4602: 68         LD           L,B
4603: 61         LD           H,C
4604: 74         LD           (HL),H
4605: 20 69      JR           NZ,$4670
4607: 73         LD           (HL),E
4608: 20 79      JR           NZ,$4683
460A: 6F         LD           L,A
460B: 75         LD           (HL),L
460C: 72         LD           (HL),D
460D: 20 20      JR           NZ,$462F
460F: 20 20      JR           NZ,$4631
4611: 66         LD           H,(HL)
4612: 61         LD           H,C
4613: 76         HALT
4614: 6F         LD           L,A
4615: 72         LD           (HL),D
4616: 69         LD           L,C
4617: 74         LD           (HL),H
4618: 65         LD           H,L
4619: 20 73      JR           NZ,$468E
461B: 6F         LD           L,A
461C: 6E         LD           L,(HL)
461D: 67         LD           H,A
461E: 3F         CCF
461F: FF         RST         0X38
4620: 50         LD           D,B
4621: 6C         LD           L,H
4622: 65         LD           H,L
4623: 61         LD           H,C
4624: 73         LD           (HL),E
4625: 65         LD           H,L
4626: 2C         INC         L
4627: 20 64      JR           NZ,$468D
4629: 6F         LD           L,A
462A: 6E         LD           L,(HL)
462B: 5E         LD           E,(HL)
462C: 74         LD           (HL),H
462D: 20 20      JR           NZ,$464F
462F: 20 65      JR           NZ,$4696
4631: 76         HALT
4632: 65         LD           H,L
4633: 72         LD           (HL),D
4634: 20 66      JR           NZ,$469C
4636: 6F         LD           L,A
4637: 72         LD           (HL),D
4638: 67         LD           H,A
4639: 65         LD           H,L
463A: 74         LD           (HL),H
463B: 20 74      JR           NZ,$46B1
463D: 68         LD           L,B
463E: 69         LD           L,C
463F: 73         LD           (HL),E
4640: 73         LD           (HL),E
4641: 6F         LD           L,A
4642: 6E         LD           L,(HL)
4643: 67         LD           H,A
4644: 2E 2E      LD           L,$2E
4646: 2E 6F      LD           L,$6F
4648: 72         LD           (HL),D
4649: 20 6D      JR           NZ,$46B8
464B: 65         LD           H,L
464C: 2E 2E      LD           L,$2E
464E: 2E FF      LD           L,$FF
4650: 54         LD           D,H
4651: 68         LD           L,B
4652: 61         LD           H,C
4653: 6E         LD           L,(HL)
4654: 6B         LD           L,E
4655: 20 79      JR           NZ,$46D0
4657: 6F         LD           L,A
4658: 75         LD           (HL),L
4659: 20 66      JR           NZ,$46C1
465B: 6F         LD           L,A
465C: 72         LD           (HL),D
465D: 20 20      JR           NZ,$467F
465F: 20 65      JR           NZ,$46C6
4661: 76         HALT
4662: 65         LD           H,L
4663: 72         LD           (HL),D
4664: 79         LD           A,C
4665: 74         LD           (HL),H
4666: 68         LD           L,B
4667: 69         LD           L,C
4668: 6E         LD           L,(HL)
4669: 67         LD           H,A
466A: 21 20 20   LD           HL,$2020
466D: 20 20      JR           NZ,$468F
466F: 20 23      JR           NZ,$4694
4671: 23         INC         HL
4672: 23         INC         HL
4673: 23         INC         HL
4674: 23         INC         HL
4675: 2C         INC         L
4676: 20 79      JR           NZ,$46F1
4678: 6F         LD           L,A
4679: 75         LD           (HL),L
467A: 20 61      JR           NZ,$46DD
467C: 72         LD           (HL),D
467D: 65         LD           H,L
467E: 20 20      JR           NZ,$46A0
4680: 74         LD           (HL),H
4681: 68         LD           L,B
4682: 65         LD           H,L
4683: 20 6B      JR           NZ,$46F0
4685: 69         LD           L,C
4686: 6E         LD           L,(HL)
4687: 64         LD           H,H
4688: 65         LD           H,L
4689: 73         LD           (HL),E
468A: 74         LD           (HL),H
468B: 20 62      JR           NZ,$46EF
468D: 6F         LD           L,A
468E: 79         LD           A,C
468F: 20 49      JR           NZ,$46DA
4691: 20 6B      JR           NZ,$46FE
4693: 6E         LD           L,(HL)
4694: 6F         LD           L,A
4695: 77         LD           (HL),A
4696: 2E 20      LD           L,$20
4698: 20 4F      JR           NZ,$46E9
469A: 6E         LD           L,(HL)
469B: 65         LD           H,L
469C: 20 64      JR           NZ,$4702
469E: 61         LD           H,C
469F: 79         LD           A,C
46A0: 49         LD           C,C
46A1: 20 6D      JR           NZ,$4710
46A3: 61         LD           H,C
46A4: 64         LD           H,H
46A5: 65         LD           H,L
46A6: 20 61      JR           NZ,$4709
46A8: 20 77      JR           NZ,$4721
46AA: 69         LD           L,C
46AB: 73         LD           (HL),E
46AC: 68         LD           L,B
46AD: 20 74      JR           NZ,$4723
46AF: 6F         LD           L,A
46B0: 74         LD           (HL),H
46B1: 68         LD           L,B
46B2: 65         LD           H,L
46B3: 20 57      JR           NZ,$470C
46B5: 69         LD           L,C
46B6: 6E         LD           L,(HL)
46B7: 64         LD           H,H
46B8: 20 46      JR           NZ,$4700
46BA: 69         LD           L,C
46BB: 73         LD           (HL),E
46BC: 68         LD           L,B
46BD: 2E 2E      LD           L,$2E
46BF: 2E 57      LD           L,$57
46C1: 68         LD           L,B
46C2: 61         LD           H,C
46C3: 74         LD           (HL),H
46C4: 20 77      JR           NZ,$473D
46C6: 61         LD           H,C
46C7: 73         LD           (HL),E
46C8: 20 74      JR           NZ,$473E
46CA: 68         LD           L,B
46CB: 65         LD           H,L
46CC: 20 20      JR           NZ,$46EE
46CE: 20 20      JR           NZ,$46F0
46D0: 77         LD           (HL),A
46D1: 69         LD           L,C
46D2: 73         LD           (HL),E
46D3: 68         LD           L,B
46D4: 3F         CCF
46D5: 20 20      JR           NZ,$46F7
46D7: 49         LD           C,C
46D8: 74         LD           (HL),H
46D9: 20 77      JR           NZ,$4752
46DB: 61         LD           H,C
46DC: 73         LD           (HL),E
46DD: 2E 2E      LD           L,$2E
46DF: 2E 4E      LD           L,$4E
46E1: 6F         LD           L,A
46E2: 2C         INC         L
46E3: 20 69      JR           NZ,$474E
46E5: 74         LD           (HL),H
46E6: 5E         LD           E,(HL)
46E7: 73         LD           (HL),E
46E8: 20 73      JR           NZ,$475D
46EA: 65         LD           H,L
46EB: 63         LD           H,E
46EC: 72         LD           (HL),D
46ED: 65         LD           H,L
46EE: 74         LD           (HL),H
46EF: 21 FF 23   LD           HL,$23FF
46F2: 23         INC         HL
46F3: 23         INC         HL
46F4: 23         INC         HL
46F5: 23         INC         HL
46F6: 2C         INC         L
46F7: 20 73      JR           NZ,$476C
46F9: 6F         LD           L,A
46FA: 6D         LD           L,L
46FB: 65         LD           H,L
46FC: 20 64      JR           NZ,$4762
46FE: 61         LD           H,C
46FF: 79         LD           A,C
4700: 20 79      JR           NZ,$477B
4702: 6F         LD           L,A
4703: 75         LD           (HL),L
4704: 20 77      JR           NZ,$477D
4706: 69         LD           L,C
4707: 6C         LD           L,H
4708: 6C         LD           L,H
4709: 20 6C      JR           NZ,$4777
470B: 65         LD           H,L
470C: 61         LD           H,C
470D: 76         HALT
470E: 65         LD           H,L
470F: 20 20      JR           NZ,$4731
4711: 74         LD           (HL),H
4712: 68         LD           L,B
4713: 69         LD           L,C
4714: 73         LD           (HL),E
4715: 20 69      JR           NZ,$4780
4717: 73         LD           (HL),E
4718: 6C         LD           L,H
4719: 61         LD           H,C
471A: 6E         LD           L,(HL)
471B: 64         LD           H,H
471C: 2E 2E      LD           L,$2E
471E: 2E 20      LD           L,$20
4720: 20 49      JR           NZ,$476B
4722: 20 6A      JR           NZ,$478E
4724: 75         LD           (HL),L
4725: 73         LD           (HL),E
4726: 74         LD           (HL),H
4727: 20 6B      JR           NZ,$4794
4729: 6E         LD           L,(HL)
472A: 6F         LD           L,A
472B: 77         LD           (HL),A
472C: 20 69      JR           NZ,$4797
472E: 74         LD           (HL),H
472F: 20 20      JR           NZ,$4751
4731: 69         LD           L,C
4732: 6E         LD           L,(HL)
4733: 20 6D      JR           NZ,$47A2
4735: 79         LD           A,C
4736: 20 68      JR           NZ,$47A0
4738: 65         LD           H,L
4739: 61         LD           H,C
473A: 72         LD           (HL),D
473B: 74         LD           (HL),H
473C: 2E 2E      LD           L,$2E
473E: 2E 20      LD           L,$20
4740: 20 2E      JR           NZ,$4770
4742: 2E 2E      LD           L,$2E
4744: 44         LD           B,H
4745: 6F         LD           L,A
4746: 6E         LD           L,(HL)
4747: 5E         LD           E,(HL)
4748: 74         LD           (HL),H
4749: 20 65      JR           NZ,$47B0
474B: 76         HALT
474C: 65         LD           H,L
474D: 72         LD           (HL),D
474E: 20 20      JR           NZ,$4770
4750: 20 66      JR           NZ,$47B8
4752: 6F         LD           L,A
4753: 72         LD           (HL),D
4754: 67         LD           H,A
4755: 65         LD           H,L
4756: 74         LD           (HL),H
4757: 20 6D      JR           NZ,$47C6
4759: 65         LD           H,L
475A: 2E 2E      LD           L,$2E
475C: 2E 20      LD           L,$20
475E: 49         LD           C,C
475F: 66         LD           H,(HL)
4760: 20 79      JR           NZ,$47DB
4762: 6F         LD           L,A
4763: 75         LD           (HL),L
4764: 20 64      JR           NZ,$47CA
4766: 6F         LD           L,A
4767: 2C         INC         L
4768: 20 49      JR           NZ,$47B3
476A: 5E         LD           E,(HL)
476B: 6C         LD           L,H
476C: 6C         LD           L,H
476D: 20 20      JR           NZ,$478F
476F: 20 20      JR           NZ,$4791
4771: 6E         LD           L,(HL)
4772: 65         LD           H,L
4773: 76         HALT
4774: 65         LD           H,L
4775: 72         LD           (HL),D
4776: 20 66      JR           NZ,$47DE
4778: 6F         LD           L,A
4779: 72         LD           (HL),D
477A: 67         LD           H,A
477B: 69         LD           L,C
477C: 76         HALT
477D: 65         LD           H,L
477E: 20 20      JR           NZ,$47A0
4780: 20 79      JR           NZ,$47FB
4782: 6F         LD           L,A
4783: 75         LD           (HL),L
4784: 21 FF 2E   LD           HL,$2EFF
4787: 2E 2E      LD           L,$2E
4789: 20 2E      JR           NZ,$47B9
478B: 2E 2E      LD           L,$2E
478D: 20 2E      JR           NZ,$47BD
478F: 2E 2E      LD           L,$2E
4791: 20 2E      JR           NZ,$47C1
4793: 2E 2E      LD           L,$2E
4795: 20 49      JR           NZ,$47E0
4797: 74         LD           (HL),H
4798: 20 73      JR           NZ,$480D
479A: 65         LD           H,L
479B: 65         LD           H,L
479C: 6D         LD           L,L
479D: 73         LD           (HL),E
479E: 20 74      JR           NZ,$4814
47A0: 6F         LD           L,A
47A1: 20 62      JR           NZ,$4805
47A3: 65         LD           H,L
47A4: 20 20      JR           NZ,$47C6
47A6: 74         LD           (HL),H
47A7: 6F         LD           L,A
47A8: 74         LD           (HL),H
47A9: 61         LD           H,C
47AA: 6C         LD           L,H
47AB: 6C         LD           L,H
47AC: 79         LD           A,C
47AD: 20 61      JR           NZ,$4810
47AF: 62         LD           H,D
47B0: 73         LD           (HL),E
47B1: 6F         LD           L,A
47B2: 72         LD           (HL),D
47B3: 62         LD           H,D
47B4: 65         LD           H,L
47B5: 64         LD           H,H
47B6: 69         LD           L,C
47B7: 6E         LD           L,(HL)
47B8: 20 4D      JR           NZ,$4807
47BA: 61         LD           H,C
47BB: 72         LD           (HL),D
47BC: 69         LD           L,C
47BD: 6E         LD           L,(HL)
47BE: 5E         LD           E,(HL)
47BF: 73         LD           (HL),E
47C0: 20 73      JR           NZ,$4835
47C2: 6F         LD           L,A
47C3: 6E         LD           L,(HL)
47C4: 67         LD           H,A
47C5: 21 FF 54   LD           HL,$54FF
47C8: 68         LD           L,B
47C9: 65         LD           H,L
47CA: 79         LD           A,C
47CB: 20 73      JR           NZ,$4840
47CD: 61         LD           H,C
47CE: 79         LD           A,C
47CF: 20 74      JR           NZ,$4845
47D1: 68         LD           L,B
47D2: 65         LD           H,L
47D3: 20 20      JR           NZ,$47F5
47D5: 20 20      JR           NZ,$47F7
47D7: 5E         LD           E,(HL)
47D8: 42         LD           B,D
47D9: 61         LD           H,C
47DA: 6C         LD           L,H
47DB: 6C         LD           L,H
47DC: 61         LD           H,C
47DD: 64         LD           H,H
47DE: 20 6F      JR           NZ,$484F
47E0: 66         LD           H,(HL)
47E1: 20 74      JR           NZ,$4857
47E3: 68         LD           L,B
47E4: 65         LD           H,L
47E5: 20 20      JR           NZ,$4807
47E7: 57         LD           D,A
47E8: 69         LD           L,C
47E9: 6E         LD           L,(HL)
47EA: 64         LD           H,H
47EB: 20 46      JR           NZ,$4833
47ED: 69         LD           L,C
47EE: 73         LD           (HL),E
47EF: 68         LD           L,B
47F0: 5E         LD           E,(HL)
47F1: 20 69      JR           NZ,$485C
47F3: 73         LD           (HL),E
47F4: 20 61      JR           NZ,$4857
47F6: 20 73      JR           NZ,$486B
47F8: 6F         LD           L,A
47F9: 6E         LD           L,(HL)
47FA: 67         LD           H,A
47FB: 20 6F      JR           NZ,$486C
47FD: 66         LD           H,(HL)
47FE: 20 61      JR           NZ,$4861
4800: 77         LD           (HL),A
4801: 61         LD           H,C
4802: 6B         LD           L,E
4803: 65         LD           H,L
4804: 6E         LD           L,(HL)
4805: 2D         DEC         L
4806: 20 69      JR           NZ,$4871
4808: 6E         LD           L,(HL)
4809: 67         LD           H,A
480A: 2E 20      LD           L,$20
480C: 20 49      JR           NZ,$4857
480E: 20 77      JR           NZ,$4887
4810: 6F         LD           L,A
4811: 6E         LD           L,(HL)
4812: 64         LD           H,H
4813: 65         LD           H,L
4814: 72         LD           (HL),D
4815: 2C         INC         L
4816: 20 69      JR           NZ,$4881
4818: 66         LD           H,(HL)
4819: 20 74      JR           NZ,$488F
481B: 68         LD           L,B
481C: 65         LD           H,L
481D: 20 57      JR           NZ,$4876
481F: 69         LD           L,C
4820: 6E         LD           L,(HL)
4821: 64         LD           H,H
4822: 20 46      JR           NZ,$486A
4824: 69         LD           L,C
4825: 73         LD           (HL),E
4826: 68         LD           L,B
4827: 77         LD           (HL),A
4828: 61         LD           H,C
4829: 6B         LD           L,E
482A: 65         LD           H,L
482B: 73         LD           (HL),E
482C: 20 75      JR           NZ,$48A3
482E: 70         LD           (HL),B
482F: 2C         INC         L
4830: 20 77      JR           NZ,$48A9
4832: 69         LD           L,C
4833: 6C         LD           L,H
4834: 6C         LD           L,H
4835: 20 20      JR           NZ,$4857
4837: 68         LD           L,B
4838: 65         LD           H,L
4839: 20 6D      JR           NZ,$48A8
483B: 61         LD           H,C
483C: 6B         LD           L,E
483D: 65         LD           H,L
483E: 20 6D      JR           NZ,$48AD
4840: 79         LD           A,C
4841: 20 77      JR           NZ,$48BA
4843: 69         LD           L,C
4844: 73         LD           (HL),E
4845: 68         LD           L,B
4846: 20 63      JR           NZ,$48AB
4848: 6F         LD           L,A
4849: 6D         LD           L,L
484A: 65         LD           H,L
484B: 20 74      JR           NZ,$48C1
484D: 72         LD           (HL),D
484E: 75         LD           (HL),L
484F: 65         LD           H,L
4850: 3F         CCF
4851: FF         RST         0X38
4852: 45         LD           B,L
4853: 68         LD           L,B
4854: 3F         CCF
4855: 20 20      JR           NZ,$4877
4857: 59         LD           E,C
4858: 6F         LD           L,A
4859: 75         LD           (HL),L
485A: 20 77      JR           NZ,$48D3
485C: 61         LD           H,C
485D: 6E         LD           L,(HL)
485E: 74         LD           (HL),H
485F: 20 6D      JR           NZ,$48CE
4861: 65         LD           H,L
4862: 74         LD           (HL),H
4863: 6F         LD           L,A
4864: 20 67      JR           NZ,$48CD
4866: 6F         LD           L,A
4867: 20 69      JR           NZ,$48D2
4869: 6E         LD           L,(HL)
486A: 20 74      JR           NZ,$48E0
486C: 68         LD           L,B
486D: 65         LD           H,L
486E: 72         LD           (HL),D
486F: 65         LD           H,L
4870: 3F         CCF
4871: 20 4E      JR           NZ,$48C1
4873: 6F         LD           L,A
4874: 2C         INC         L
4875: 20 49      JR           NZ,$48C0
4877: 20 74      JR           NZ,$48ED
4879: 68         LD           L,B
487A: 69         LD           L,C
487B: 6E         LD           L,(HL)
487C: 6B         LD           L,E
487D: 20 49      JR           NZ,$48C8
487F: 5E         LD           E,(HL)
4880: 6C         LD           L,H
4881: 6C         LD           L,H
4882: 77         LD           (HL),A
4883: 61         LD           H,C
4884: 69         LD           L,C
4885: 74         LD           (HL),H
4886: 20 6F      JR           NZ,$48F7
4888: 75         LD           (HL),L
4889: 74         LD           (HL),H
488A: 20 68      JR           NZ,$48F4
488C: 65         LD           H,L
488D: 72         LD           (HL),D
488E: 65         LD           H,L
488F: 2E 2E      LD           L,$2E
4891: 2E 54      LD           L,$54
4893: 61         LD           H,C
4894: 6B         LD           L,E
4895: 65         LD           H,L
4896: 20 63      JR           NZ,$48FB
4898: 61         LD           H,C
4899: 72         LD           (HL),D
489A: 65         LD           H,L
489B: 20 6F      JR           NZ,$490C
489D: 66         LD           H,(HL)
489E: 20 20      JR           NZ,$48C0
48A0: 20 20      JR           NZ,$48C2
48A2: 79         LD           A,C
48A3: 6F         LD           L,A
48A4: 75         LD           (HL),L
48A5: 72         LD           (HL),D
48A6: 73         LD           (HL),E
48A7: 65         LD           H,L
48A8: 6C         LD           L,H
48A9: 66         LD           H,(HL)
48AA: 2C         INC         L
48AB: 20 23      JR           NZ,$48D0
48AD: 23         INC         HL
48AE: 23         INC         HL
48AF: 23         INC         HL
48B0: 23         INC         HL
48B1: 21 FF 41   LD           HL,$41FF
48B4: 68         LD           L,B
48B5: 68         LD           L,B
48B6: 68         LD           L,B
48B7: 21 20 20   LD           HL,$2020
48BA: 41         LD           B,C
48BB: 68         LD           L,B
48BC: 68         LD           L,B
48BD: 68         LD           L,B
48BE: 2C         INC         L
48BF: 20 79      JR           NZ,$493A
48C1: 6F         LD           L,A
48C2: 75         LD           (HL),L
48C3: 61         LD           H,C
48C4: 72         LD           (HL),D
48C5: 65         LD           H,L
48C6: 20 61      JR           NZ,$4929
48C8: 20 62      JR           NZ,$492C
48CA: 61         LD           H,C
48CB: 64         LD           H,H
48CC: 20 62      JR           NZ,$4930
48CE: 6F         LD           L,A
48CF: 79         LD           A,C
48D0: 2C         INC         L
48D1: 20 20      JR           NZ,$48F3
48D3: 23         INC         HL
48D4: 23         INC         HL
48D5: 23         INC         HL
48D6: 23         INC         HL
48D7: 23         INC         HL
48D8: 21 FF 48   LD           HL,$48FF
48DB: 65         LD           H,L
48DC: 72         LD           (HL),D
48DD: 65         LD           H,L
48DE: 5E         LD           E,(HL)
48DF: 73         LD           (HL),E
48E0: 20 73      JR           NZ,$4955
48E2: 6F         LD           L,A
48E3: 6D         LD           L,L
48E4: 65         LD           H,L
48E5: 20 20      JR           NZ,$4907
48E7: 20 20      JR           NZ,$4909
48E9: 20 62      JR           NZ,$494D
48EB: 6F         LD           L,A
48EC: 6E         LD           L,(HL)
48ED: 75         LD           (HL),L
48EE: 73         LD           (HL),E
48EF: 20 74      JR           NZ,$4965
48F1: 72         LD           (HL),D
48F2: 65         LD           H,L
48F3: 61         LD           H,C
48F4: 74         LD           (HL),H
48F5: 6D         LD           L,L
48F6: 65         LD           H,L
48F7: 6E         LD           L,(HL)
48F8: 74         LD           (HL),H
48F9: 21 42 65   LD           HL,$6542
48FC: 68         LD           L,B
48FD: 6F         LD           L,A
48FE: 6C         LD           L,H
48FF: 64         LD           H,H
4900: 21 20 20   LD           HL,$2020
4903: 59         LD           E,C
4904: 6F         LD           L,A
4905: 75         LD           (HL),L
4906: 72         LD           (HL),D
4907: 20 20      JR           NZ,$4929
4909: 20 48      JR           NZ,$4953
490B: 65         LD           H,L
490C: 61         LD           H,C
490D: 72         LD           (HL),D
490E: 74         LD           (HL),H
490F: 73         LD           (HL),E
4910: 20 61      JR           NZ,$4973
4912: 72         LD           (HL),D
4913: 65         LD           H,L
4914: 20 66      JR           NZ,$497C
4916: 75         LD           (HL),L
4917: 6C         LD           L,H
4918: 6C         LD           L,H
4919: 21 FF 59   LD           HL,$59FF
491C: 61         LD           H,C
491D: 2C         INC         L
491E: 20 49      JR           NZ,$4969
4920: 20 61      JR           NZ,$4983
4922: 6D         LD           L,L
4923: 20 53      JR           NZ,$4978
4925: 63         LD           H,E
4926: 68         LD           L,B
4927: 75         LD           (HL),L
4928: 6C         LD           L,H
4929: 65         LD           H,L
492A: 20 44      JR           NZ,$4970
492C: 6F         LD           L,A
492D: 6E         LD           L,(HL)
492E: 61         LD           H,C
492F: 76         HALT
4930: 69         LD           L,C
4931: 74         LD           (HL),H
4932: 63         LD           H,E
4933: 68         LD           L,B
4934: 21 20 20   LD           HL,$2020
4937: 5A         LD           E,D
4938: 65         LD           H,L
4939: 65         LD           H,L
493A: 20 6D      JR           NZ,$49A9
493C: 65         LD           H,L
493D: 72         LD           (HL),D
493E: 6D         LD           L,L
493F: 61         LD           H,C
4940: 69         LD           L,C
4941: 64         LD           H,H
4942: 20 73      JR           NZ,$49B7
4944: 74         LD           (HL),H
4945: 61         LD           H,C
4946: 74         LD           (HL),H
4947: 75         LD           (HL),L
4948: 65         LD           H,L
4949: 20 20      JR           NZ,$496B
494B: 62         LD           H,D
494C: 79         LD           A,C
494D: 20 7A      JR           NZ,$49C9
494F: 65         LD           H,L
4950: 65         LD           H,L
4951: 20 62      JR           NZ,$49B5
4953: 61         LD           H,C
4954: 79         LD           A,C
4955: 20 69      JR           NZ,$49C0
4957: 7A         LD           A,D
4958: 20 6D      JR           NZ,$49C7
495A: 79         LD           A,C
495B: 6D         LD           L,L
495C: 61         LD           H,C
495D: 73         LD           (HL),E
495E: 74         LD           (HL),H
495F: 65         LD           H,L
4960: 72         LD           (HL),D
4961: 70         LD           (HL),B
4962: 69         LD           L,C
4963: 65         LD           H,L
4964: 63         LD           H,E
4965: 65         LD           H,L
4966: 21 20 2E   LD           HL,$2E20
4969: 2E 2E      LD           L,$2E
496B: 54         LD           D,H
496C: 6F         LD           L,A
496D: 20 74      JR           NZ,$49E3
496F: 65         LD           H,L
4970: 6C         LD           L,H
4971: 6C         LD           L,H
4972: 20 79      JR           NZ,$49ED
4974: 6F         LD           L,A
4975: 75         LD           (HL),L
4976: 20 7A      JR           NZ,$49F2
4978: 65         LD           H,L
4979: 65         LD           H,L
497A: 20 74      JR           NZ,$49F0
497C: 72         LD           (HL),D
497D: 75         LD           (HL),L
497E: 74         LD           (HL),H
497F: 68         LD           L,B
4980: 2C         INC         L
4981: 20 7A      JR           NZ,$49FD
4983: 69         LD           L,C
4984: 73         LD           (HL),E
4985: 20 77      JR           NZ,$49FE
4987: 65         LD           H,L
4988: 72         LD           (HL),D
4989: 6B         LD           L,E
498A: 20 69      JR           NZ,$49F5
498C: 7A         LD           A,D
498D: 20 6E      JR           NZ,$49FD
498F: 6F         LD           L,A
4990: 74         LD           (HL),H
4991: 20 63      JR           NZ,$49F6
4993: 6F         LD           L,A
4994: 6D         LD           L,L
4995: 70         LD           (HL),B
4996: 6C         LD           L,H
4997: 65         LD           H,L
4998: 74         LD           (HL),H
4999: 65         LD           H,L
499A: 21 5A 65   LD           HL,$655A
499D: 65         LD           H,L
499E: 20 61      JR           NZ,$4A01
49A0: 72         LD           (HL),D
49A1: 74         LD           (HL),H
49A2: 2C         INC         L
49A3: 20 69      JR           NZ,$4A0E
49A5: 74         LD           (HL),H
49A6: 5E         LD           E,(HL)
49A7: 7A         LD           A,D
49A8: 2E 2E      LD           L,$2E
49AA: 2E 64      LD           L,$64
49AC: 69         LD           L,C
49AD: 66         LD           H,(HL)
49AE: 66         LD           H,(HL)
49AF: 69         LD           L,C
49B0: 63         LD           H,E
49B1: 75         LD           (HL),L
49B2: 6C         LD           L,H
49B3: 74         LD           (HL),H
49B4: 20 66      JR           NZ,$4A1C
49B6: 6F         LD           L,A
49B7: 72         LD           (HL),D
49B8: 20 20      JR           NZ,$49DA
49BA: 20 79      JR           NZ,$4A35
49BC: 6F         LD           L,A
49BD: 75         LD           (HL),L
49BE: 20 74      JR           NZ,$4A34
49C0: 6F         LD           L,A
49C1: 20 67      JR           NZ,$4A2A
49C3: 72         LD           (HL),D
49C4: 61         LD           H,C
49C5: 73         LD           (HL),E
49C6: 70         LD           (HL),B
49C7: 2C         INC         L
49C8: 20 69      JR           NZ,$4A33
49CA: 7A         LD           A,D
49CB: 69         LD           L,C
49CC: 74         LD           (HL),H
49CD: 20 6E      JR           NZ,$4A3D
49CF: 6F         LD           L,A
49D0: 74         LD           (HL),H
49D1: 3F         CCF
49D2: FF         RST         0X38
49D3: 20 20      JR           NZ,$49F5
49D5: 54         LD           D,H
49D6: 48         LD           C,B
49D7: 45         LD           B,L
49D8: 20 4D      JR           NZ,$4A27
49DA: 4F         LD           C,A
49DB: 55         LD           D,L
49DC: 52         LD           D,D
49DD: 4E         LD           C,(HL)
49DE: 49         LD           C,C
49DF: 4E         LD           C,(HL)
49E0: 47         LD           B,A
49E1: 20 20      JR           NZ,$4A03
49E3: 20 20      JR           NZ,$4A05
49E5: 20 20      JR           NZ,$4A07
49E7: 20 4D      JR           NZ,$4A36
49E9: 45         LD           B,L
49EA: 52         LD           D,D
49EB: 4D         LD           C,L
49EC: 41         LD           B,C
49ED: 49         LD           C,C
49EE: 44         LD           B,H
49EF: 20 20      JR           NZ,$4A11
49F1: 20 20      JR           NZ,$4A13
49F3: 20 20      JR           NZ,$4A15
49F5: 20 20      JR           NZ,$4A17
49F7: 42         LD           B,D
49F8: 79         LD           A,C
49F9: 20 53      JR           NZ,$4A4E
49FB: 43         LD           B,E
49FC: 48         LD           C,B
49FD: 55         LD           D,L
49FE: 4C         LD           C,H
49FF: 45         LD           B,L
4A00: 20 20      JR           NZ,$4A22
4A02: 20 3F      JR           NZ,$4A43
4A04: 20 2E      JR           NZ,$4A34
4A06: 2E 2E      LD           L,$2E
4A08: 41         LD           B,C
4A09: 20 73      JR           NZ,$4A7E
4A0B: 63         LD           H,E
4A0C: 61         LD           H,C
4A0D: 6C         LD           L,H
4A0E: 65         LD           H,L
4A0F: 20 69      JR           NZ,$4A7A
4A11: 73         LD           (HL),E
4A12: 20 6D      JR           NZ,$4A81
4A14: 69         LD           L,C
4A15: 73         LD           (HL),E
4A16: 73         LD           (HL),E
4A17: 69         LD           L,C
4A18: 6E         LD           L,(HL)
4A19: 67         LD           H,A
4A1A: 2E 2E      LD           L,$2E
4A1C: 2E FF      LD           L,$FF
4A1E: 53         LD           D,E
4A1F: 65         LD           H,L
4A20: 61         LD           H,C
4A21: 73         LD           (HL),E
4A22: 68         LD           L,B
4A23: 65         LD           H,L
4A24: 6C         LD           L,H
4A25: 6C         LD           L,H
4A26: 20 4D      JR           NZ,$4A75
4A28: 61         LD           H,C
4A29: 6E         LD           L,(HL)
4A2A: 73         LD           (HL),E
4A2B: 69         LD           L,C
4A2C: 6F         LD           L,A
4A2D: 6E         LD           L,(HL)
4A2E: FF         RST         0X38
4A2F: 45         LD           B,L
4A30: 6E         LD           L,(HL)
4A31: 74         LD           (HL),H
4A32: 72         LD           (HL),D
4A33: 61         LD           H,C
4A34: 6E         LD           L,(HL)
4A35: 63         LD           H,E
4A36: 65         LD           H,L
4A37: 20 74      JR           NZ,$4AAD
4A39: 6F         LD           L,A
4A3A: 20 20      JR           NZ,$4A5C
4A3C: 20 20      JR           NZ,$4A5E
4A3E: 20 20      JR           NZ,$4A60
4A40: 20 59      JR           NZ,$4A9B
4A42: 61         LD           H,C
4A43: 72         LD           (HL),D
4A44: 6E         LD           L,(HL)
4A45: 61         LD           H,C
4A46: 20 44      JR           NZ,$4A8C
4A48: 65         LD           H,L
4A49: 73         LD           (HL),E
4A4A: 65         LD           H,L
4A4B: 72         LD           (HL),D
4A4C: 74         LD           (HL),H
4A4D: 20 F3      JR           NZ,$4A42
4A4F: FF         RST         0X38
4A50: 20 20      JR           NZ,$4A72
4A52: 20 4D      JR           NZ,$4AA1
4A54: 79         LD           A,C
4A55: 73         LD           (HL),E
4A56: 74         LD           (HL),H
4A57: 65         LD           H,L
4A58: 72         LD           (HL),D
4A59: 69         LD           L,C
4A5A: 6F         LD           L,A
4A5B: 75         LD           (HL),L
4A5C: 73         LD           (HL),E
4A5D: 20 20      JR           NZ,$4A7F
4A5F: 20 20      JR           NZ,$4A81
4A61: 20 20      JR           NZ,$4A83
4A63: 20 20      JR           NZ,$4A85
4A65: 46         LD           B,(HL)
4A66: 6F         LD           L,A
4A67: 72         LD           (HL),D
4A68: 65         LD           H,L
4A69: 73         LD           (HL),E
4A6A: 74         LD           (HL),H
4A6B: 20 20      JR           NZ,$4A8D
4A6D: 20 20      JR           NZ,$4A8F
4A6F: 20 20      JR           NZ,$4A91
4A71: 28 49      JR           Z,$4ABC
4A73: 74         LD           (HL),H
4A74: 5E         LD           E,(HL)
4A75: 73         LD           (HL),E
4A76: 20 61      JR           NZ,$4AD9
4A78: 20 6C      JR           NZ,$4AE6
4A7A: 69         LD           L,C
4A7B: 74         LD           (HL),H
4A7C: 74         LD           (HL),H
4A7D: 6C         LD           L,H
4A7E: 65         LD           H,L
4A7F: 20 20      JR           NZ,$4AA1
4A81: 62         LD           H,D
4A82: 69         LD           L,C
4A83: 74         LD           (HL),H
4A84: 20 6D      JR           NZ,$4AF3
4A86: 79         LD           A,C
4A87: 73         LD           (HL),E
4A88: 74         LD           (HL),H
4A89: 65         LD           H,L
4A8A: 72         LD           (HL),D
4A8B: 69         LD           L,C
4A8C: 6F         LD           L,A
4A8D: 75         LD           (HL),L
4A8E: 73         LD           (HL),E
4A8F: 29         ADD         HL,HL
4A90: FF         RST         0X38
4A91: 44         LD           B,H
4A92: 6F         LD           L,A
4A93: 20 79      JR           NZ,$4B0E
4A95: 6F         LD           L,A
4A96: 75         LD           (HL),L
4A97: 20 77      JR           NZ,$4B10
4A99: 61         LD           H,C
4A9A: 6E         LD           L,(HL)
4A9B: 74         LD           (HL),H
4A9C: 20 74      JR           NZ,$4B12
4A9E: 6F         LD           L,A
4A9F: 20 20      JR           NZ,$4AC1
4AA1: 63         LD           H,E
4AA2: 68         LD           L,B
4AA3: 61         LD           H,C
4AA4: 6C         LD           L,H
4AA5: 6C         LD           L,H
4AA6: 65         LD           H,L
4AA7: 6E         LD           L,(HL)
4AA8: 67         LD           H,A
4AA9: 65         LD           H,L
4AAA: 20 74      JR           NZ,$4B20
4AAC: 68         LD           L,B
4AAD: 65         LD           H,L
4AAE: 20 20      JR           NZ,$4AD0
4AB0: 20 72      JR           NZ,$4B24
4AB2: 69         LD           L,C
4AB3: 76         HALT
4AB4: 65         LD           H,L
4AB5: 72         LD           (HL),D
4AB6: 20 72      JR           NZ,$4B2A
4AB8: 61         LD           H,C
4AB9: 70         LD           (HL),B
4ABA: 69         LD           L,C
4ABB: 64         LD           H,H
4ABC: 73         LD           (HL),E
4ABD: 20 6F      JR           NZ,$4B2E
4ABF: 6E         LD           L,(HL)
4AC0: 20 61      JR           NZ,$4B23
4AC2: 20 72      JR           NZ,$4B36
4AC4: 61         LD           H,C
4AC5: 66         LD           H,(HL)
4AC6: 74         LD           (HL),H
4AC7: 3F         CCF
4AC8: 20 20      JR           NZ,$4AEA
4ACA: 50         LD           D,B
4ACB: 72         LD           (HL),D
4ACC: 6F         LD           L,A
4ACD: 63         LD           H,E
4ACE: 65         LD           H,L
4ACF: 65         LD           H,L
4AD0: 64         LD           H,H
4AD1: 74         LD           (HL),H
4AD2: 6F         LD           L,A
4AD3: 20 74      JR           NZ,$4B49
4AD5: 68         LD           L,B
4AD6: 65         LD           H,L
4AD7: 20 6F      JR           NZ,$4B48
4AD9: 66         LD           H,(HL)
4ADA: 66         LD           H,(HL)
4ADB: 69         LD           L,C
4ADC: 63         LD           H,E
4ADD: 65         LD           H,L
4ADE: 20 61      JR           NZ,$4B41
4AE0: 74         LD           (HL),H
4AE1: 6F         LD           L,A
4AE2: 6E         LD           L,(HL)
4AE3: 63         LD           H,E
4AE4: 65         LD           H,L
4AE5: 2C         INC         L
4AE6: 20 70      JR           NZ,$4B58
4AE8: 6C         LD           L,H
4AE9: 65         LD           H,L
4AEA: 61         LD           H,C
4AEB: 73         LD           (HL),E
4AEC: 65         LD           H,L
4AED: 21 FF 45   LD           HL,$45FF
4AF0: 61         LD           H,C
4AF1: 73         LD           (HL),E
4AF2: 74         LD           (HL),H
4AF3: 20 F3      JR           NZ,$4AE8
4AF5: 20 55      JR           NZ,$4B4C
4AF7: 6B         LD           L,E
4AF8: 75         LD           (HL),L
4AF9: 6B         LD           L,E
4AFA: 75         LD           (HL),L
4AFB: 20 20      JR           NZ,$4B1D
4AFD: 20 20      JR           NZ,$4B1F
4AFF: 20 20      JR           NZ,$4B21
4B01: 20 20      JR           NZ,$4B23
4B03: 20 20      JR           NZ,$4B25
4B05: 20 50      JR           NZ,$4B57
4B07: 72         LD           (HL),D
4B08: 61         LD           H,C
4B09: 69         LD           L,C
4B0A: 72         LD           (HL),D
4B0B: 69         LD           L,C
4B0C: 65         LD           H,L
4B0D: 20 20      JR           NZ,$4B2F
4B0F: 46         LD           B,(HL)
4B10: 61         LD           H,C
4B11: 72         LD           (HL),D
4B12: 74         LD           (HL),H
4B13: 68         LD           L,B
4B14: 65         LD           H,L
4B15: 72         LD           (HL),D
4B16: 20 45      JR           NZ,$4B5D
4B18: 61         LD           H,C
4B19: 73         LD           (HL),E
4B1A: 74         LD           (HL),H
4B1B: 20 20      JR           NZ,$4B3D
4B1D: 20 20      JR           NZ,$4B3F
4B1F: 20 20      JR           NZ,$4B41
4B21: 41         LD           B,C
4B22: 6E         LD           L,(HL)
4B23: 69         LD           L,C
4B24: 6D         LD           L,L
4B25: 61         LD           H,C
4B26: 6C         LD           L,H
4B27: 20 56      JR           NZ,$4B7F
4B29: 69         LD           L,C
4B2A: 6C         LD           L,H
4B2B: 6C         LD           L,H
4B2C: 61         LD           H,C
4B2D: 67         LD           H,A
4B2E: 65         LD           H,L
4B2F: FF         RST         0X38
4B30: 4D         LD           C,L
4B31: 74         LD           (HL),H
4B32: 2E 20      LD           L,$20
4B34: 54         LD           D,H
4B35: 61         LD           H,C
4B36: 6D         LD           L,L
4B37: 61         LD           H,C
4B38: 72         LD           (HL),D
4B39: 61         LD           H,C
4B3A: 6E         LD           L,(HL)
4B3B: 63         LD           H,E
4B3C: 68         LD           L,B
4B3D: 20 20      JR           NZ,$4B5F
4B3F: 20 FF      JR           NZ,$4B40
4B41: F3         DI
4B42: 20 54      JR           NZ,$4B98
4B44: 61         LD           H,C
4B45: 69         LD           L,C
4B46: 6C         LD           L,H
4B47: 20 43      JR           NZ,$4B8C
4B49: 61         LD           H,C
4B4A: 76         HALT
4B4B: 65         LD           H,L
4B4C: 20 20      JR           NZ,$4B6E
4B4E: 20 20      JR           NZ,$4B70
4B50: 20 F1      JR           NZ,$4B43
4B52: 20 54      JR           NZ,$4BA8
4B54: 6F         LD           L,A
4B55: 72         LD           (HL),D
4B56: 6F         LD           L,A
4B57: 6E         LD           L,(HL)
4B58: 62         LD           H,D
4B59: 6F         LD           L,A
4B5A: 20 53      JR           NZ,$4BAF
4B5C: 68         LD           L,B
4B5D: 6F         LD           L,A
4B5E: 72         LD           (HL),D
4B5F: 65         LD           H,L
4B60: 73         LD           (HL),E
4B61: FF         RST         0X38
4B62: F3         DI
4B63: 20 47      JR           NZ,$4BAC
4B65: 6F         LD           L,A
4B66: 70         LD           (HL),B
4B67: 6F         LD           L,A
4B68: 6E         LD           L,(HL)
4B69: 67         LD           H,A
4B6A: 6F         LD           L,A
4B6B: 20 53      JR           NZ,$4BC0
4B6D: 77         LD           (HL),A
4B6E: 61         LD           H,C
4B6F: 6D         LD           L,L
4B70: 70         LD           (HL),B
4B71: 20 F1      JR           NZ,$4B64
4B73: 20 4D      JR           NZ,$4BC2
4B75: 79         LD           A,C
4B76: 73         LD           (HL),E
4B77: 74         LD           (HL),H
4B78: 65         LD           H,L
4B79: 72         LD           (HL),D
4B7A: 69         LD           L,C
4B7B: 6F         LD           L,A
4B7C: 75         LD           (HL),L
4B7D: 73         LD           (HL),E
4B7E: 20 20      JR           NZ,$4BA0
4B80: 20 20      JR           NZ,$4BA2
4B82: 20 20      JR           NZ,$4BA4
4B84: 46         LD           B,(HL)
4B85: 6F         LD           L,A
4B86: 72         LD           (HL),D
4B87: 65         LD           H,L
4B88: 73         LD           (HL),E
4B89: 74         LD           (HL),H
4B8A: FF         RST         0X38
4B8B: 42         LD           B,D
4B8C: 65         LD           H,L
4B8D: 77         LD           (HL),A
4B8E: 61         LD           H,C
4B8F: 72         LD           (HL),D
4B90: 65         LD           H,L
4B91: 20 6F      JR           NZ,$4C02
4B93: 66         LD           H,(HL)
4B94: 20 66      JR           NZ,$4BFC
4B96: 6C         LD           L,H
4B97: 6F         LD           L,A
4B98: 6F         LD           L,A
4B99: 72         LD           (HL),D
4B9A: 73         LD           (HL),E
4B9B: 77         LD           (HL),A
4B9C: 69         LD           L,C
4B9D: 74         LD           (HL),H
4B9E: 68         LD           L,B
4B9F: 20 63      JR           NZ,$4C04
4BA1: 72         LD           (HL),D
4BA2: 61         LD           H,C
4BA3: 63         LD           H,E
4BA4: 6B         LD           L,E
4BA5: 73         LD           (HL),E
4BA6: 21 20 20   LD           HL,$2020
4BA9: 41         LD           B,C
4BAA: 20 68      JR           NZ,$4C14
4BAC: 65         LD           H,L
4BAD: 61         LD           H,C
4BAE: 76         HALT
4BAF: 79         LD           A,C
4BB0: 20 70      JR           NZ,$4C22
4BB2: 65         LD           H,L
4BB3: 72         LD           (HL),D
4BB4: 73         LD           (HL),E
4BB5: 6F         LD           L,A
4BB6: 6E         LD           L,(HL)
4BB7: 20 20      JR           NZ,$4BD9
4BB9: 20 20      JR           NZ,$4BDB
4BBB: 73         LD           (HL),E
4BBC: 68         LD           L,B
4BBD: 6F         LD           L,A
4BBE: 75         LD           (HL),L
4BBF: 6C         LD           L,H
4BC0: 64         LD           H,H
4BC1: 20 6E      JR           NZ,$4C31
4BC3: 6F         LD           L,A
4BC4: 74         LD           (HL),H
4BC5: 20 73      JR           NZ,$4C3A
4BC7: 74         LD           (HL),H
4BC8: 61         LD           H,C
4BC9: 6E         LD           L,(HL)
4BCA: 64         LD           H,H
4BCB: 6F         LD           L,A
4BCC: 6E         LD           L,(HL)
4BCD: 20 74      JR           NZ,$4C43
4BCF: 68         LD           L,B
4BD0: 65         LD           H,L
4BD1: 6D         LD           L,L
4BD2: 21 FF 54   LD           HL,$54FF
4BD5: 65         LD           H,L
4BD6: 6C         LD           L,H
4BD7: 65         LD           H,L
4BD8: 70         LD           (HL),B
4BD9: 68         LD           L,B
4BDA: 6F         LD           L,A
4BDB: 6E         LD           L,(HL)
4BDC: 65         LD           H,L
4BDD: 20 42      JR           NZ,$4C21
4BDF: 6F         LD           L,A
4BE0: 6F         LD           L,A
4BE1: 74         LD           (HL),H
4BE2: 68         LD           L,B
4BE3: 20 FF      JR           NZ,$4BE4
4BE5: 20 20      JR           NZ,$4C07
4BE7: 20 20      JR           NZ,$4C09
4BE9: 20 44      JR           NZ,$4C2F
4BEB: 41         LD           B,C
4BEC: 4E         LD           C,(HL)
4BED: 47         LD           B,A
4BEE: 45         LD           B,L
4BEF: 52         LD           D,D
4BF0: 21 20 20   LD           HL,$2020
4BF3: 20 20      JR           NZ,$4C15
4BF5: 20 20      JR           NZ,$4C17
4BF7: 20 20      JR           NZ,$4C19
4BF9: 4B         LD           C,E
4BFA: 65         LD           H,L
4BFB: 65         LD           H,L
4BFC: 70         LD           (HL),B
4BFD: 20 6F      JR           NZ,$4C6E
4BFF: 75         LD           (HL),L
4C00: 74         LD           (HL),H
4C01: 21 20 20   LD           HL,$2020
4C04: 20 28      JR           NZ,$4C2E
4C06: 45         LD           B,L
4C07: 78         LD           A,B
4C08: 63         LD           H,E
4C09: 65         LD           H,L
4C0A: 70         LD           (HL),B
4C0B: 74         LD           (HL),H
4C0C: 20 42      JR           NZ,$4C50
4C0E: 6F         LD           L,A
4C0F: 77         LD           (HL),A
4C10: 57         LD           D,A
4C11: 6F         LD           L,A
4C12: 77         LD           (HL),A
4C13: 29         ADD         HL,HL
4C14: FF         RST         0X38
4C15: F1         POP         AF
4C16: 20 47      JR           NZ,$4C5F
4C18: 4F         LD           C,A
4C19: 20 54      JR           NZ,$4C6F
4C1B: 48         LD           C,B
4C1C: 49         LD           C,C
4C1D: 53         LD           D,E
4C1E: 20 57      JR           NZ,$4C77
4C20: 41         LD           B,C
4C21: 59         LD           E,C
4C22: FF         RST         0X38
4C23: F0 20      LD           A,($20)
4C25: 47         LD           B,A
4C26: 4F         LD           C,A
4C27: 20 54      JR           NZ,$4C7D
4C29: 48         LD           C,B
4C2A: 49         LD           C,C
4C2B: 53         LD           D,E
4C2C: 20 57      JR           NZ,$4C85
4C2E: 41         LD           B,C
4C2F: 59         LD           E,C
4C30: FF         RST         0X38
4C31: F3         DI
4C32: 20 47      JR           NZ,$4C7B
4C34: 4F         LD           C,A
4C35: 20 54      JR           NZ,$4C8B
4C37: 48         LD           C,B
4C38: 49         LD           C,C
4C39: 53         LD           D,E
4C3A: 20 57      JR           NZ,$4C93
4C3C: 41         LD           B,C
4C3D: 59         LD           E,C
4C3E: FF         RST         0X38
4C3F: F2                              
4C40: 20 47      JR           NZ,$4C89
4C42: 4F         LD           C,A
4C43: 20 54      JR           NZ,$4C99
4C45: 48         LD           C,B
4C46: 49         LD           C,C
4C47: 53         LD           D,E
4C48: 20 57      JR           NZ,$4CA1
4C4A: 41         LD           B,C
4C4B: 59         LD           E,C
4C4C: FF         RST         0X38
4C4D: 20 54      JR           NZ,$4CA3
4C4F: 52         LD           D,D
4C50: 59         LD           E,C
4C51: 20 41      JR           NZ,$4C94
4C53: 47         LD           B,A
4C54: 41         LD           B,C
4C55: 49         LD           C,C
4C56: 4E         LD           C,(HL)
4C57: 20 46      JR           NZ,$4C9F
4C59: 52         LD           D,D
4C5A: 4F         LD           C,A
4C5B: 4D         LD           C,L
4C5C: 20 20      JR           NZ,$4C7E
4C5E: 20 20      JR           NZ,$4C80
4C60: 54         LD           D,H
4C61: 48         LD           C,B
4C62: 45         LD           B,L
4C63: 20 53      JR           NZ,$4CB8
4C65: 54         LD           D,H
4C66: 41         LD           B,C
4C67: 52         LD           D,D
4C68: 54         LD           D,H
4C69: FF         RST         0X38
4C6A: 47         LD           B,A
4C6B: 52         LD           D,D
4C6C: 45         LD           B,L
4C6D: 41         LD           B,C
4C6E: 54         LD           D,H
4C6F: 21 20 20   LD           HL,$2020
4C72: 59         LD           E,C
4C73: 4F         LD           C,A
4C74: 55         LD           D,L
4C75: 20 44      JR           NZ,$4CBB
4C77: 49         LD           C,C
4C78: 44         LD           B,H
4C79: 20 49      JR           NZ,$4CC4
4C7B: 54         LD           D,H
4C7C: 21 20 20   LD           HL,$2020
4C7F: 59         LD           E,C
4C80: 4F         LD           C,A
4C81: 55         LD           D,L
4C82: 52         LD           D,D
4C83: 20 52      JR           NZ,$4CD7
4C85: 45         LD           B,L
4C86: 57         LD           D,A
4C87: 41         LD           B,C
4C88: 52         LD           D,D
4C89: 44         LD           B,H
4C8A: 49         LD           C,C
4C8B: 53         LD           D,E
4C8C: 20 F3      JR           NZ,$4C81
4C8E: 20 54      JR           NZ,$4CE4
4C90: 48         LD           C,B
4C91: 49         LD           C,C
4C92: 53         LD           D,E
4C93: 20 57      JR           NZ,$4CEC
4C95: 41         LD           B,C
4C96: 59         LD           E,C
4C97: 21 FF 47   LD           HL,$47FF
4C9A: 4F         LD           C,A
4C9B: 4E         LD           C,(HL)
4C9C: 45         LD           B,L
4C9D: 20 4F      JR           NZ,$4CEE
4C9F: 4E         LD           C,(HL)
4CA0: 20 54      JR           NZ,$4CF6
4CA2: 4F         LD           C,A
4CA3: 55         LD           D,L
4CA4: 52         LD           D,D
4CA5: 20 20      JR           NZ,$4CC7
4CA7: 20 20      JR           NZ,$4CC9
4CA9: 20 20      JR           NZ,$4CCB
4CAB: 20 20      JR           NZ,$4CCD
4CAD: 20 20      JR           NZ,$4CCF
4CAF: 20 20      JR           NZ,$4CD1
4CB1: 20 4D      JR           NZ,$4D00
4CB3: 41         LD           B,C
4CB4: 4D         LD           C,L
4CB5: 55         LD           D,L
4CB6: FF         RST         0X38
4CB7: F3         DI
4CB8: 20 43      JR           NZ,$4CFD
4CBA: 72         LD           (HL),D
4CBB: 61         LD           H,C
4CBC: 7A         LD           A,D
4CBD: 79         LD           A,C
4CBE: 20 54      JR           NZ,$4D14
4CC0: 72         LD           (HL),D
4CC1: 61         LD           H,C
4CC2: 63         LD           H,E
4CC3: 79         LD           A,C
4CC4: 20 20      JR           NZ,$4CE6
4CC6: 20 F1      JR           NZ,$4CB9
4CC8: 20 4D      JR           NZ,$4D17
4CCA: 61         LD           H,C
4CCB: 6E         LD           L,(HL)
4CCC: 62         LD           H,D
4CCD: 6F         LD           L,A
4CCE: 5E         LD           E,(HL)
4CCF: 73         LD           (HL),E
4CD0: 20 50      JR           NZ,$4D22
4CD2: 6F         LD           L,A
4CD3: 6E         LD           L,(HL)
4CD4: 64         LD           H,H
4CD5: FF         RST         0X38
4CD6: F3         DI
4CD7: 20 41      JR           NZ,$4D1A
4CD9: 6E         LD           L,(HL)
4CDA: 69         LD           L,C
4CDB: 6D         LD           L,L
4CDC: 61         LD           H,C
4CDD: 6C         LD           L,H
4CDE: 20 56      JR           NZ,$4D36
4CE0: 69         LD           L,C
4CE1: 6C         LD           L,H
4CE2: 6C         LD           L,H
4CE3: 61         LD           H,C
4CE4: 67         LD           H,A
4CE5: 65         LD           H,L
4CE6: F1         POP         AF
4CE7: 20 4D      JR           NZ,$4D36
4CE9: 61         LD           H,C
4CEA: 72         LD           (HL),D
4CEB: 74         LD           (HL),H
4CEC: 68         LD           L,B
4CED: 61         LD           H,C
4CEE: 5E         LD           E,(HL)
4CEF: 73         LD           (HL),E
4CF0: 20 42      JR           NZ,$4D34
4CF2: 61         LD           H,C
4CF3: 79         LD           A,C
4CF4: FF         RST         0X38
4CF5: F3         DI
4CF6: 20 57      JR           NZ,$4D4F
4CF8: 65         LD           H,L
4CF9: 6C         LD           L,H
4CFA: 63         LD           H,E
4CFB: 6F         LD           L,A
4CFC: 6D         LD           L,L
4CFD: 65         LD           H,L
4CFE: 20 74      JR           NZ,$4D74
4D00: 6F         LD           L,A
4D01: 20 74      JR           NZ,$4D77
4D03: 68         LD           L,B
4D04: 65         LD           H,L
4D05: 20 41      JR           NZ,$4D48
4D07: 6E         LD           L,(HL)
4D08: 69         LD           L,C
4D09: 6D         LD           L,L
4D0A: 61         LD           H,C
4D0B: 6C         LD           L,H
4D0C: 20 56      JR           NZ,$4D64
4D0E: 69         LD           L,C
4D0F: 6C         LD           L,H
4D10: 6C         LD           L,H
4D11: 61         LD           H,C
4D12: 67         LD           H,A
4D13: 65         LD           H,L
4D14: 21 FF F3   LD           HL,$F3FF
4D17: 20 43      JR           NZ,$4D5C
4D19: 65         LD           H,L
4D1A: 6D         LD           L,L
4D1B: 65         LD           H,L
4D1C: 74         LD           (HL),H
4D1D: 61         LD           H,C
4D1E: 72         LD           (HL),D
4D1F: 79         LD           A,C
4D20: 20 20      JR           NZ,$4D42
4D22: 20 20      JR           NZ,$4D44
4D24: 20 20      JR           NZ,$4D46
4D26: F1         POP         AF
4D27: 20 55      JR           NZ,$4D7E
4D29: 6B         LD           L,E
4D2A: 75         LD           (HL),L
4D2B: 6B         LD           L,E
4D2C: 75         LD           (HL),L
4D2D: 20 50      JR           NZ,$4D7F
4D2F: 72         LD           (HL),D
4D30: 61         LD           H,C
4D31: 69         LD           L,C
4D32: 72         LD           (HL),D
4D33: 69         LD           L,C
4D34: 65         LD           H,L
4D35: 20 FF      JR           NZ,$4D36
4D37: 54         LD           D,H
4D38: 61         LD           H,C
4D39: 6C         LD           L,H
4D3A: 20 54      JR           NZ,$4D90
4D3C: 61         LD           H,C
4D3D: 6C         LD           L,H
4D3E: 20 48      JR           NZ,$4D88
4D40: 65         LD           H,L
4D41: 69         LD           L,C
4D42: 67         LD           H,A
4D43: 68         LD           L,B
4D44: 74         LD           (HL),H
4D45: 73         LD           (HL),E
4D46: FF         RST         0X38
4D47: F3         DI
4D48: 20 54      JR           NZ,$4D9E
4D4A: 61         LD           H,C
4D4B: 6D         LD           L,L
4D4C: 61         LD           H,C
4D4D: 72         LD           (HL),D
4D4E: 61         LD           H,C
4D4F: 6E         LD           L,(HL)
4D50: 63         LD           H,E
4D51: 68         LD           L,B
4D52: 20 4D      JR           NZ,$4DA1
4D54: 74         LD           (HL),H
4D55: 2E 20      LD           L,$20
4D57: F2                              
4D58: 20 47      JR           NZ,$4DA1
4D5A: 6F         LD           L,A
4D5B: 70         LD           (HL),B
4D5C: 6F         LD           L,A
4D5D: 6E         LD           L,(HL)
4D5E: 67         LD           H,A
4D5F: 61         LD           H,C
4D60: 20 53      JR           NZ,$4DB5
4D62: 77         LD           (HL),A
4D63: 61         LD           H,C
4D64: 6D         LD           L,L
4D65: 70         LD           (HL),B
4D66: 20 FF      JR           NZ,$4D67
4D68: 4D         LD           C,L
4D69: 55         LD           D,L
4D6A: 53         LD           D,E
4D6B: 49         LD           C,C
4D6C: 43         LD           B,E
4D6D: 2C         INC         L
4D6E: 20 54      JR           NZ,$4DC4
4D70: 48         LD           C,B
4D71: 45         LD           B,L
4D72: 20 46      JR           NZ,$4DBA
4D74: 49         LD           C,C
4D75: 53         LD           D,E
4D76: 48         LD           C,B
4D77: 20 53      JR           NZ,$4DCC
4D79: 54         LD           D,H
4D7A: 49         LD           C,C
4D7B: 52         LD           D,D
4D7C: 53         LD           D,E
4D7D: 20 49      JR           NZ,$4DC8
4D7F: 4E         LD           C,(HL)
4D80: 20 54      JR           NZ,$4DD6
4D82: 48         LD           C,B
4D83: 45         LD           B,L
4D84: 20 45      JR           NZ,$4DCB
4D86: 47         LD           B,A
4D87: 47         LD           B,A
4D88: 59         LD           E,C
4D89: 4F         LD           C,A
4D8A: 55         LD           D,L
4D8B: 20 41      JR           NZ,$4DCE
4D8D: 52         LD           D,D
4D8E: 45         LD           B,L
4D8F: 20 54      JR           NZ,$4DE5
4D91: 48         LD           C,B
4D92: 45         LD           B,L
4D93: 52         LD           D,D
4D94: 45         LD           B,L
4D95: 2E 2E      LD           L,$2E
4D97: 2E FF      LD           L,$FF
4D99: 54         LD           D,H
4D9A: 48         LD           C,B
4D9B: 45         LD           B,L
4D9C: 20 57      JR           NZ,$4DF5
4D9E: 49         LD           C,C
4D9F: 4E         LD           C,(HL)
4DA0: 44         LD           B,H
4DA1: 20 46      JR           NZ,$4DE9
4DA3: 49         LD           C,C
4DA4: 53         LD           D,E
4DA5: 48         LD           C,B
4DA6: 20 49      JR           NZ,$4DF1
4DA8: 4E         LD           C,(HL)
4DA9: 4E         LD           C,(HL)
4DAA: 41         LD           B,C
4DAB: 4D         LD           C,L
4DAC: 45         LD           B,L
4DAD: 20 4F      JR           NZ,$4DFE
4DAF: 4E         LD           C,(HL)
4DB0: 4C         LD           C,H
4DB1: 59         LD           E,C
4DB2: 2C         INC         L
4DB3: 20 46      JR           NZ,$4DFB
4DB5: 4F         LD           C,A
4DB6: 52         LD           D,D
4DB7: 20 20      JR           NZ,$4DD9
4DB9: 49         LD           C,C
4DBA: 54         LD           D,H
4DBB: 20 49      JR           NZ,$4E06
4DBD: 53         LD           D,E
4DBE: 20 4E      JR           NZ,$4E0E
4DC0: 45         LD           B,L
4DC1: 49         LD           C,C
4DC2: 54         LD           D,H
4DC3: 48         LD           C,B
4DC4: 45         LD           B,L
4DC5: 52         LD           D,D
4DC6: 2E FF      LD           L,$FF
4DC8: 49         LD           C,C
4DC9: 4E         LD           C,(HL)
4DCA: 20 53      JR           NZ,$4E1F
4DCC: 4F         LD           C,A
4DCD: 49         LD           C,C
4DCE: 4C         LD           C,H
4DCF: 20 53      JR           NZ,$4E24
4DD1: 4C         LD           C,H
4DD2: 45         LD           B,L
4DD3: 45         LD           B,L
4DD4: 50         LD           D,B
4DD5: 53         LD           D,E
4DD6: 20 20      JR           NZ,$4DF8
4DD8: 53         LD           D,E
4DD9: 45         LD           B,L
4DDA: 43         LD           B,E
4DDB: 52         LD           D,D
4DDC: 45         LD           B,L
4DDD: 54         LD           D,H
4DDE: 53         LD           D,E
4DDF: 2C         INC         L
4DE0: 20 42      JR           NZ,$4E24
4DE2: 45         LD           B,L
4DE3: 4E         LD           C,(HL)
4DE4: 45         LD           B,L
4DE5: 41         LD           B,C
4DE6: 54         LD           D,H
4DE7: 48         LD           C,B
4DE8: 59         LD           E,C
4DE9: 4F         LD           C,A
4DEA: 55         LD           D,L
4DEB: 52         LD           D,D
4DEC: 20 53      JR           NZ,$4E41
4DEE: 4F         LD           C,A
4DEF: 4C         LD           C,H
4DF0: 45         LD           B,L
4DF1: 53         LD           D,E
4DF2: 2E 2E      LD           L,$2E
4DF4: 2E FF      LD           L,$FF
4DF6: 49         LD           C,C
4DF7: 4E         LD           C,(HL)
4DF8: 20 53      JR           NZ,$4E4D
4DFA: 4F         LD           C,A
4DFB: 49         LD           C,C
4DFC: 4C         LD           C,H
4DFD: 20 53      JR           NZ,$4E52
4DFF: 4C         LD           C,H
4E00: 45         LD           B,L
4E01: 45         LD           B,L
4E02: 50         LD           D,B
4E03: 53         LD           D,E
4E04: 20 20      JR           NZ,$4E26
4E06: 53         LD           D,E
4E07: 45         LD           B,L
4E08: 43         LD           B,E
4E09: 52         LD           D,D
4E0A: 45         LD           B,L
4E0B: 54         LD           D,H
4E0C: 53         LD           D,E
4E0D: 2C         INC         L
4E0E: 20 42      JR           NZ,$4E52
4E10: 45         LD           B,L
4E11: 4E         LD           C,(HL)
4E12: 45         LD           B,L
4E13: 41         LD           B,C
4E14: 54         LD           D,H
4E15: 48         LD           C,B
4E16: 59         LD           E,C
4E17: 4F         LD           C,A
4E18: 55         LD           D,L
4E19: 52         LD           D,D
4E1A: 20 53      JR           NZ,$4E6F
4E1C: 4F         LD           C,A
4E1D: 4C         LD           C,H
4E1E: 45         LD           B,L
4E1F: 53         LD           D,E
4E20: 2E 2E      LD           L,$2E
4E22: 2E FF      LD           L,$FF
4E24: 41         LD           B,C
4E25: 52         LD           D,D
4E26: 4F         LD           C,A
4E27: 55         LD           D,L
4E28: 4E         LD           C,(HL)
4E29: 44         LD           B,H
4E2A: 20 48      JR           NZ,$4E74
4E2C: 45         LD           B,L
4E2D: 52         LD           D,D
4E2E: 45         LD           B,L
4E2F: 2C         INC         L
4E30: 20 20      JR           NZ,$4E52
4E32: 20 20      JR           NZ,$4E54
4E34: 53         LD           D,E
4E35: 45         LD           B,L
4E36: 43         LD           B,E
4E37: 52         LD           D,D
4E38: 45         LD           B,L
4E39: 54         LD           D,H
4E3A: 53         LD           D,E
4E3B: 20 41      JR           NZ,$4E7E
4E3D: 52         LD           D,D
4E3E: 45         LD           B,L
4E3F: 20 4E      JR           NZ,$4E8F
4E41: 49         LD           C,C
4E42: 47         LD           B,A
4E43: 48         LD           C,B
4E44: FF         RST         0X38
4E45: 53         LD           D,E
4E46: 45         LD           B,L
4E47: 43         LD           B,E
4E48: 52         LD           D,D
4E49: 45         LD           B,L
4E4A: 54         LD           D,H
4E4B: 53         LD           D,E
4E4C: 20 41      JR           NZ,$4E8F
4E4E: 52         LD           D,D
4E4F: 45         LD           B,L
4E50: 20 4C      JR           NZ,$4E9E
4E52: 49         LD           C,C
4E53: 4B         LD           C,E
4E54: 45         LD           B,L
4E55: 57         LD           D,A
4E56: 41         LD           B,C
4E57: 54         LD           D,H
4E58: 45         LD           B,L
4E59: 52         LD           D,D
4E5A: 20 57      JR           NZ,$4EB3
4E5C: 48         LD           C,B
4E5D: 45         LD           B,L
4E5E: 4E         LD           C,(HL)
4E5F: 20 49      JR           NZ,$4EAA
4E61: 54         LD           D,H
4E62: 20 20      JR           NZ,$4E84
4E64: 20 43      JR           NZ,$4EA9
4E66: 4F         LD           C,A
4E67: 4D         LD           C,L
4E68: 45         LD           B,L
4E69: 53         LD           D,E
4E6A: 20 54      JR           NZ,$4EC0
4E6C: 4F         LD           C,A
4E6D: 20 42      JR           NZ,$4EB1
4E6F: 52         LD           D,D
4E70: 49         LD           C,C
4E71: 44         LD           B,H
4E72: 47         LD           B,A
4E73: 45         LD           B,L
4E74: 53         LD           D,E
4E75: FF         RST         0X38
4E76: 4E         LD           C,(HL)
4E77: 4F         LD           C,A
4E78: 57         LD           D,A
4E79: 20 59      JR           NZ,$4ED4
4E7B: 4F         LD           C,A
4E7C: 55         LD           D,L
4E7D: 20 4E      JR           NZ,$4ECD
4E7F: 45         LD           B,L
4E80: 45         LD           B,L
4E81: 44         LD           B,H
4E82: 20 20      JR           NZ,$4EA4
4E84: 20 20      JR           NZ,$4EA6
4E86: 4C         LD           C,H
4E87: 4F         LD           C,A
4E88: 4F         LD           C,A
4E89: 4B         LD           C,E
4E8A: 20 46      JR           NZ,$4ED2
4E8C: 41         LD           B,C
4E8D: 52         LD           D,D
4E8E: 20 46      JR           NZ,$4ED6
4E90: 4F         LD           C,A
4E91: 52         LD           D,D
4E92: 20 20      JR           NZ,$4EB4
4E94: 20 20      JR           NZ,$4EB6
4E96: 41         LD           B,C
4E97: 20 53      JR           NZ,$4EEC
4E99: 45         LD           B,L
4E9A: 43         LD           B,E
4E9B: 52         LD           D,D
4E9C: 45         LD           B,L
4E9D: 54         LD           D,H
4E9E: 2E 2E      LD           L,$2E
4EA0: 2E FF      LD           L,$FF
4EA2: 54         LD           D,H
4EA3: 48         LD           C,B
4EA4: 45         LD           B,L
4EA5: 20 57      JR           NZ,$4EFE
4EA7: 49         LD           C,C
4EA8: 4E         LD           C,(HL)
4EA9: 44         LD           B,H
4EAA: 20 46      JR           NZ,$4EF2
4EAC: 49         LD           C,C
4EAD: 53         LD           D,E
4EAE: 48         LD           C,B
4EAF: 20 20      JR           NZ,$4ED1
4EB1: 20 53      JR           NZ,$4F06
4EB3: 4C         LD           C,H
4EB4: 55         LD           D,L
4EB5: 4D         LD           C,L
4EB6: 42         LD           B,D
4EB7: 45         LD           B,L
4EB8: 52         LD           D,D
4EB9: 53         LD           D,E
4EBA: 20 4C      JR           NZ,$4F08
4EBC: 4F         LD           C,A
4EBD: 4E         LD           C,(HL)
4EBE: 47         LD           B,A
4EBF: 2E 2E      LD           L,$2E
4EC1: 2E 54      LD           L,$54
4EC3: 48         LD           C,B
4EC4: 45         LD           B,L
4EC5: 20 48      JR           NZ,$4F0F
4EC7: 45         LD           B,L
4EC8: 52         LD           D,D
4EC9: 4F         LD           C,A
4ECA: 5E         LD           E,(HL)
4ECB: 53         LD           D,E
4ECC: 20 4C      JR           NZ,$4F1A
4ECE: 49         LD           C,C
4ECF: 46         LD           B,(HL)
4ED0: 45         LD           B,L
4ED1: 20 47      JR           NZ,$4F1A
4ED3: 4F         LD           C,A
4ED4: 4E         LD           C,(HL)
4ED5: 45         LD           B,L
4ED6: 2E 2E      LD           L,$2E
4ED8: 2E FF      LD           L,$FF
4EDA: 53         LD           D,E
4EDB: 45         LD           B,L
4EDC: 41         LD           B,C
4EDD: 20 42      JR           NZ,$4F21
4EDF: 45         LD           B,L
4EE0: 41         LD           B,C
4EE1: 52         LD           D,D
4EE2: 53         LD           D,E
4EE3: 20 46      JR           NZ,$4F2B
4EE5: 4F         LD           C,A
4EE6: 41         LD           B,C
4EE7: 4D         LD           C,L
4EE8: 2C         INC         L
4EE9: 20 53      JR           NZ,$4F3E
4EEB: 4C         LD           C,H
4EEC: 45         LD           B,L
4EED: 45         LD           B,L
4EEE: 50         LD           D,B
4EEF: 20 42      JR           NZ,$4F33
4EF1: 45         LD           B,L
4EF2: 41         LD           B,C
4EF3: 52         LD           D,D
4EF4: 53         LD           D,E
4EF5: 20 20      JR           NZ,$4F17
4EF7: 20 20      JR           NZ,$4F19
4EF9: 20 44      JR           NZ,$4F3F
4EFB: 52         LD           D,D
4EFC: 45         LD           B,L
4EFD: 41         LD           B,C
4EFE: 4D         LD           C,L
4EFF: 53         LD           D,E
4F00: 2E 20      LD           L,$20
4F02: 42         LD           B,D
4F03: 4F         LD           C,A
4F04: 54         LD           D,H
4F05: 48         LD           C,B
4F06: 20 45      JR           NZ,$4F4D
4F08: 4E         LD           C,(HL)
4F09: 44         LD           B,H
4F0A: 49         LD           C,C
4F0B: 4E         LD           C,(HL)
4F0C: 20 54      JR           NZ,$4F62
4F0E: 48         LD           C,B
4F0F: 45         LD           B,L
4F10: 20 53      JR           NZ,$4F65
4F12: 41         LD           B,C
4F13: 4D         LD           C,L
4F14: 45         LD           B,L
4F15: 20 57      JR           NZ,$4F6E
4F17: 41         LD           B,C
4F18: 59         LD           E,C
4F19: 20 43      JR           NZ,$4F5E
4F1B: 52         LD           D,D
4F1C: 41         LD           B,C
4F1D: 53         LD           D,E
4F1E: 53         LD           D,E
4F1F: 53         LD           D,E
4F20: 48         LD           C,B
4F21: 21 FF 4F   LD           HL,$4FFF
4F24: 68         LD           L,B
4F25: 3F         CCF
4F26: 21 20 20   LD           HL,$2020
4F29: 23         INC         HL
4F2A: 23         INC         HL
4F2B: 23         INC         HL
4F2C: 23         INC         HL
4F2D: 23         INC         HL
4F2E: 2C         INC         L
4F2F: 20 49      JR           NZ,$4F7A
4F31: 20 20      JR           NZ,$4F53
4F33: 73         LD           (HL),E
4F34: 65         LD           H,L
4F35: 65         LD           H,L
4F36: 20 79      JR           NZ,$4FB1
4F38: 61         LD           H,C
4F39: 20 68      JR           NZ,$4FA3
4F3B: 61         LD           H,C
4F3C: 76         HALT
4F3D: 65         LD           H,L
4F3E: 20 61      JR           NZ,$4FA1
4F40: 20 20      JR           NZ,$4F62
4F42: 20 6E      JR           NZ,$4FB2
4F44: 69         LD           L,C
4F45: 63         LD           H,E
4F46: 65         LD           H,L
4F47: 20 73      JR           NZ,$4FBC
4F49: 74         LD           (HL),H
4F4A: 69         LD           L,C
4F4B: 63         LD           H,E
4F4C: 6B         LD           L,E
4F4D: 2E 2E      LD           L,$2E
4F4F: 2E 20      LD           L,$20
4F51: 20 20      JR           NZ,$4F73
4F53: 43         LD           B,E
4F54: 61         LD           H,C
4F55: 6E         LD           L,(HL)
4F56: 20 49      JR           NZ,$4FA1
4F58: 20 62      JR           NZ,$4FBC
4F5A: 6F         LD           L,A
4F5B: 72         LD           (HL),D
4F5C: 72         LD           (HL),D
4F5D: 6F         LD           L,A
4F5E: 77         LD           (HL),A
4F5F: 20 69      JR           NZ,$4FCA
4F61: 74         LD           (HL),H
4F62: 20 66      JR           NZ,$4FCA
4F64: 6F         LD           L,A
4F65: 72         LD           (HL),D
4F66: 20 61      JR           NZ,$4FC9
4F68: 20 73      JR           NZ,$4FDD
4F6A: 65         LD           H,L
4F6B: 63         LD           H,E
4F6C: 6F         LD           L,A
4F6D: 6E         LD           L,(HL)
4F6E: 64         LD           H,H
4F6F: 3F         CCF
4F70: 20 20      JR           NZ,$4F92
4F72: 20 20      JR           NZ,$4F94
4F74: 20 20      JR           NZ,$4F96
4F76: 20 43      JR           NZ,$4FBB
4F78: 61         LD           H,C
4F79: 6E         LD           L,(HL)
4F7A: 20 20      JR           NZ,$4F9C
4F7C: 43         LD           B,E
4F7D: 61         LD           H,C
4F7E: 6E         LD           L,(HL)
4F7F: 5E         LD           E,(HL)
4F80: 74         LD           (HL),H
4F81: FE E4      CP           $E4
4F83: 20 62      JR           NZ,$4FE7
4F85: 65         LD           H,L
4F86: 63         LD           H,E
4F87: 61         LD           H,C
4F88: 6D         LD           L,L
4F89: 65         LD           H,L
4F8A: 20 74      JR           NZ,$5000
4F8C: 68         LD           L,B
4F8D: 65         LD           H,L
4F8E: 20 20      JR           NZ,$4FB0
4F90: 20 20      JR           NZ,$4FB2
4F92: 68         LD           L,B
4F93: 6F         LD           L,A
4F94: 6E         LD           L,(HL)
4F95: 65         LD           H,L
4F96: 79         LD           A,C
4F97: 63         LD           H,E
4F98: 6F         LD           L,A
4F99: 6D         LD           L,L
4F9A: 62         LD           H,D
4F9B: 20 E5      JR           NZ,$4F82
4F9D: 21 20 20   LD           HL,$2020
4FA0: 20 20      JR           NZ,$4FC2
4FA2: 59         LD           E,C
4FA3: 6F         LD           L,A
4FA4: 75         LD           (HL),L
4FA5: 5E         LD           E,(HL)
4FA6: 72         LD           (HL),D
4FA7: 65         LD           H,L
4FA8: 20 6E      JR           NZ,$5018
4FAA: 6F         LD           L,A
4FAB: 74         LD           (HL),H
4FAC: 20 73      JR           NZ,$5021
4FAE: 75         LD           (HL),L
4FAF: 72         LD           (HL),D
4FB0: 65         LD           H,L
4FB1: 20 68      JR           NZ,$501B
4FB3: 6F         LD           L,A
4FB4: 77         LD           (HL),A
4FB5: 20 69      JR           NZ,$5020
4FB7: 74         LD           (HL),H
4FB8: 20 68      JR           NZ,$5022
4FBA: 61         LD           H,C
4FBB: 70         LD           (HL),B
4FBC: 70         LD           (HL),B
4FBD: 65         LD           H,L
4FBE: 6E         LD           L,(HL)
4FBF: 65         LD           H,L
4FC0: 64         LD           H,H
4FC1: 2C         INC         L
4FC2: 62         LD           H,D
4FC3: 75         LD           (HL),L
4FC4: 74         LD           (HL),H
4FC5: 20 74      JR           NZ,$503B
4FC7: 61         LD           H,C
4FC8: 6B         LD           L,E
4FC9: 65         LD           H,L
4FCA: 20 69      JR           NZ,$5035
4FCC: 74         LD           (HL),H
4FCD: 21 FF 48   LD           HL,$48FF
4FD0: 6D         LD           L,L
4FD1: 6D         LD           L,L
4FD2: 6D         LD           L,L
4FD3: 2C         INC         L
4FD4: 20 23      JR           NZ,$4FF9
4FD6: 23         INC         HL
4FD7: 23         INC         HL
4FD8: 23         INC         HL
4FD9: 23         INC         HL
4FDA: 2C         INC         L
4FDB: 20 79      JR           NZ,$5056
4FDD: 6F         LD           L,A
4FDE: 75         LD           (HL),L
4FDF: 61         LD           H,C
4FE0: 72         LD           (HL),D
4FE1: 65         LD           H,L
4FE2: 20 6D      JR           NZ,$5051
4FE4: 65         LD           H,L
4FE5: 61         LD           H,C
4FE6: 6E         LD           L,(HL)
4FE7: 21 FF 42   LD           HL,$42FF
4FEA: 65         LD           H,L
4FEB: 77         LD           (HL),A
4FEC: 61         LD           H,C
4FED: 72         LD           (HL),D
4FEE: 65         LD           H,L
4FEF: 20 6F      JR           NZ,$5060
4FF1: 66         LD           H,(HL)
4FF2: 20 53      JR           NZ,$5047
4FF4: 65         LD           H,L
4FF5: 61         LD           H,C
4FF6: 20 20      JR           NZ,$5018
4FF8: 20 55      JR           NZ,$504F
4FFA: 72         LD           (HL),D
4FFB: 63         LD           H,E
4FFC: 68         LD           L,B
4FFD: 69         LD           L,C
4FFE: 6E         LD           L,(HL)
4FFF: 73         LD           (HL),E
5000: 21 20 20   LD           HL,$2020
5003: 44         LD           B,H
5004: 6F         LD           L,A
5005: 6E         LD           L,(HL)
5006: 5E         LD           E,(HL)
5007: 74         LD           (HL),H
5008: 20 74      JR           NZ,$507E
500A: 6F         LD           L,A
500B: 75         LD           (HL),L
500C: 63         LD           H,E
500D: 68         LD           L,B
500E: 20 74      JR           NZ,$5084
5010: 68         LD           L,B
5011: 65         LD           H,L
5012: 6D         LD           L,L
5013: 20 77      JR           NZ,$508C
5015: 69         LD           L,C
5016: 74         LD           (HL),H
5017: 68         LD           L,B
5018: 20 79      JR           NZ,$5093
501A: 6F         LD           L,A
501B: 75         LD           (HL),L
501C: 72         LD           (HL),D
501D: 20 62      JR           NZ,$5081
501F: 61         LD           H,C
5020: 72         LD           (HL),D
5021: 65         LD           H,L
5022: 20 68      JR           NZ,$508C
5024: 61         LD           H,C
5025: 6E         LD           L,(HL)
5026: 64         LD           H,H
5027: 73         LD           (HL),E
5028: 21 FF 49   LD           HL,$49FF
502B: 20 77      JR           NZ,$50A4
502D: 61         LD           H,C
502E: 73         LD           (HL),E
502F: 20 68      JR           NZ,$5099
5031: 75         LD           (HL),L
5032: 6E         LD           L,(HL)
5033: 67         LD           H,A
5034: 72         LD           (HL),D
5035: 79         LD           A,C
5036: 20 20      JR           NZ,$5058
5038: 20 20      JR           NZ,$505A
503A: 73         LD           (HL),E
503B: 6F         LD           L,A
503C: 6D         LD           L,L
503D: 65         LD           H,L
503E: 74         LD           (HL),H
503F: 68         LD           L,B
5040: 69         LD           L,C
5041: 6E         LD           L,(HL)
5042: 5E         LD           E,(HL)
5043: 20 66      JR           NZ,$50AB
5045: 69         LD           L,C
5046: 65         LD           H,L
5047: 72         LD           (HL),D
5048: 63         LD           H,E
5049: 65         LD           H,L
504A: 73         LD           (HL),E
504B: 6F         LD           L,A
504C: 20 49      JR           NZ,$5097
504E: 20 77      JR           NZ,$50C7
5050: 65         LD           H,L
5051: 6E         LD           L,(HL)
5052: 74         LD           (HL),H
5053: 20 61      JR           NZ,$50B6
5055: 6E         LD           L,(HL)
5056: 64         LD           H,H
5057: 20 20      JR           NZ,$5079
5059: 20 67      JR           NZ,$50C2
505B: 6F         LD           L,A
505C: 74         LD           (HL),H
505D: 20 62      JR           NZ,$50C1
505F: 61         LD           H,C
5060: 6E         LD           L,(HL)
5061: 61         LD           H,C
5062: 6E         LD           L,(HL)
5063: 61         LD           H,C
5064: 73         LD           (HL),E
5065: 20 61      JR           NZ,$50C8
5067: 74         LD           (HL),H
5068: 20 20      JR           NZ,$508A
506A: 74         LD           (HL),H
506B: 68         LD           L,B
506C: 65         LD           H,L
506D: 20 62      JR           NZ,$50D1
506F: 65         LD           H,L
5070: 61         LD           H,C
5071: 63         LD           H,E
5072: 68         LD           L,B
5073: 2E 2E      LD           L,$2E
5075: 2E 20      LD           L,$20
5077: 20 20      JR           NZ,$5099
5079: 20 23      JR           NZ,$509E
507B: 23         INC         HL
507C: 23         INC         HL
507D: 23         INC         HL
507E: 23         INC         HL
507F: 2C         INC         L
5080: 20 69      JR           NZ,$50EB
5082: 66         LD           H,(HL)
5083: 20 79      JR           NZ,$50FE
5085: 6F         LD           L,A
5086: 75         LD           (HL),L
5087: 20 20      JR           NZ,$50A9
5089: 20 77      JR           NZ,$5102
508B: 61         LD           H,C
508C: 6E         LD           L,(HL)
508D: 74         LD           (HL),H
508E: 20 73      JR           NZ,$5103
5090: 6F         LD           L,A
5091: 6D         LD           L,L
5092: 65         LD           H,L
5093: 2C         INC         L
5094: 20 79      JR           NZ,$510F
5096: 6F         LD           L,A
5097: 75         LD           (HL),L
5098: 20 20      JR           NZ,$50BA
509A: 73         LD           (HL),E
509B: 68         LD           L,B
509C: 6F         LD           L,A
509D: 75         LD           (HL),L
509E: 6C         LD           L,H
509F: 64         LD           H,H
50A0: 20 67      JR           NZ,$5109
50A2: 6F         LD           L,A
50A3: 20 61      JR           NZ,$5106
50A5: 6E         LD           L,(HL)
50A6: 64         LD           H,H
50A7: 20 20      JR           NZ,$50C9
50A9: 20 67      JR           NZ,$5112
50AB: 65         LD           H,L
50AC: 74         LD           (HL),H
50AD: 20 73      JR           NZ,$5122
50AF: 6F         LD           L,A
50B0: 6D         LD           L,L
50B1: 65         LD           H,L
50B2: 21 FF 57   LD           HL,$57FF
50B5: 65         LD           H,L
50B6: 6C         LD           L,H
50B7: 63         LD           H,E
50B8: 6F         LD           L,A
50B9: 6D         LD           L,L
50BA: 65         LD           H,L
50BB: 20 74      JR           NZ,$5131
50BD: 6F         LD           L,A
50BE: 20 20      JR           NZ,$50E0
50C0: 20 20      JR           NZ,$50E2
50C2: 20 20      JR           NZ,$50E4
50C4: 53         LD           D,E
50C5: 61         LD           H,C
50C6: 6C         LD           L,H
50C7: 65         LD           H,L
50C8: 5E         LD           E,(HL)
50C9: 73         LD           (HL),E
50CA: 20 48      JR           NZ,$5114
50CC: 6F         LD           L,A
50CD: 75         LD           (HL),L
50CE: 73         LD           (HL),E
50CF: 65         LD           H,L
50D0: 20 4F      JR           NZ,$5121
50D2: 5E         LD           E,(HL)
50D3: 20 42      JR           NZ,$5117
50D5: 61         LD           H,C
50D6: 6E         LD           L,(HL)
50D7: 61         LD           H,C
50D8: 6E         LD           L,(HL)
50D9: 61         LD           H,C
50DA: 73         LD           (HL),E
50DB: 21 20 20   LD           HL,$2020
50DE: 49         LD           C,C
50DF: 5E         LD           E,(HL)
50E0: 6D         LD           L,L
50E1: 20 20      JR           NZ,$5103
50E3: 20 53      JR           NZ,$5138
50E5: 61         LD           H,C
50E6: 6C         LD           L,H
50E7: 65         LD           H,L
50E8: 2C         INC         L
50E9: 20 74      JR           NZ,$515F
50EB: 68         LD           L,B
50EC: 69         LD           L,C
50ED: 73         LD           (HL),E
50EE: 20 69      JR           NZ,$5159
50F0: 73         LD           (HL),E
50F1: 20 6D      JR           NZ,$5160
50F3: 79         LD           A,C
50F4: 68         LD           L,B
50F5: 6F         LD           L,A
50F6: 75         LD           (HL),L
50F7: 73         LD           (HL),E
50F8: 65         LD           H,L
50F9: 21 20 41   LD           HL,$4120
50FC: 63         LD           H,E
50FD: 74         LD           (HL),H
50FE: 75         LD           (HL),L
50FF: 61         LD           H,C
5100: 6C         LD           L,H
5101: 6C         LD           L,H
5102: 79         LD           A,C
5103: 2C         INC         L
5104: 6D         LD           L,L
5105: 79         LD           A,C
5106: 20 68      JR           NZ,$5170
5108: 6F         LD           L,A
5109: 62         LD           H,D
510A: 62         LD           H,D
510B: 79         LD           A,C
510C: 20 69      JR           NZ,$5177
510E: 73         LD           (HL),E
510F: 20 63      JR           NZ,$5174
5111: 6F         LD           L,A
5112: 6C         LD           L,H
5113: 2D         DEC         L
5114: 6C         LD           L,H
5115: 65         LD           H,L
5116: 63         LD           H,E
5117: 74         LD           (HL),H
5118: 69         LD           L,C
5119: 6E         LD           L,(HL)
511A: 67         LD           H,A
511B: 20 72      JR           NZ,$518F
511D: 61         LD           H,C
511E: 72         LD           (HL),D
511F: 65         LD           H,L
5120: 20 61      JR           NZ,$5183
5122: 6E         LD           L,(HL)
5123: 64         LD           H,H
5124: 75         LD           (HL),L
5125: 6E         LD           L,(HL)
5126: 75         LD           (HL),L
5127: 73         LD           (HL),E
5128: 75         LD           (HL),L
5129: 61         LD           H,C
512A: 6C         LD           L,H
512B: 20 63      JR           NZ,$5190
512D: 61         LD           H,C
512E: 6E         LD           L,(HL)
512F: 6E         LD           L,(HL)
5130: 65         LD           H,L
5131: 64         LD           H,H
5132: 20 20      JR           NZ,$5154
5134: 66         LD           H,(HL)
5135: 6F         LD           L,A
5136: 6F         LD           L,A
5137: 64         LD           H,H
5138: 2E 20      LD           L,$20
513A: 4D         LD           C,L
513B: 79         LD           A,C
513C: 20 62      JR           NZ,$51A0
513E: 72         LD           (HL),D
513F: 6F         LD           L,A
5140: 74         LD           (HL),H
5141: 68         LD           L,B
5142: 65         LD           H,L
5143: 72         LD           (HL),D
5144: 69         LD           L,C
5145: 73         LD           (HL),E
5146: 20 61      JR           NZ,$51A9
5148: 6E         LD           L,(HL)
5149: 20 61      JR           NZ,$51AC
514B: 72         LD           (HL),D
514C: 74         LD           (HL),H
514D: 69         LD           L,C
514E: 73         LD           (HL),E
514F: 74         LD           (HL),H
5150: 2C         INC         L
5151: 20 73      JR           NZ,$51C6
5153: 6F         LD           L,A
5154: 49         LD           C,C
5155: 20 67      JR           NZ,$51BE
5157: 75         LD           (HL),L
5158: 65         LD           H,L
5159: 73         LD           (HL),E
515A: 73         LD           (HL),E
515B: 20 73      JR           NZ,$51D0
515D: 74         LD           (HL),H
515E: 72         LD           (HL),D
515F: 61         LD           H,C
5160: 6E         LD           L,(HL)
5161: 67         LD           H,A
5162: 65         LD           H,L
5163: 20 68      JR           NZ,$51CD
5165: 6F         LD           L,A
5166: 62         LD           H,D
5167: 62         LD           H,D
5168: 69         LD           L,C
5169: 65         LD           H,L
516A: 73         LD           (HL),E
516B: 20 72      JR           NZ,$51DF
516D: 75         LD           (HL),L
516E: 6E         LD           L,(HL)
516F: 20 69      JR           NZ,$51DA
5171: 6E         LD           L,(HL)
5172: 20 20      JR           NZ,$5194
5174: 74         LD           (HL),H
5175: 68         LD           L,B
5176: 65         LD           H,L
5177: 20 66      JR           NZ,$51DF
5179: 61         LD           H,C
517A: 6D         LD           L,L
517B: 69         LD           L,C
517C: 6C         LD           L,H
517D: 79         LD           A,C
517E: 21 FF 57   LD           HL,$57FF
5181: 68         LD           L,B
5182: 61         LD           H,C
5183: 74         LD           (HL),H
5184: 5E         LD           E,(HL)
5185: 73         LD           (HL),E
5186: 20 74      JR           NZ,$51FC
5188: 68         LD           L,B
5189: 61         LD           H,C
518A: 74         LD           (HL),H
518B: 20 79      JR           NZ,$5206
518D: 6F         LD           L,A
518E: 75         LD           (HL),L
518F: 20 68      JR           NZ,$51F9
5191: 61         LD           H,C
5192: 76         HALT
5193: 65         LD           H,L
5194: 3F         CCF
5195: 21 20 20   LD           HL,$2020
5198: 49         LD           C,C
5199: 74         LD           (HL),H
519A: 5E         LD           E,(HL)
519B: 73         LD           (HL),E
519C: 20 20      JR           NZ,$51BE
519E: 20 20      JR           NZ,$51C0
51A0: 63         LD           H,E
51A1: 61         LD           H,C
51A2: 6E         LD           L,(HL)
51A3: 6E         LD           L,(HL)
51A4: 65         LD           H,L
51A5: 64         LD           H,H
51A6: 20 66      JR           NZ,$520E
51A8: 6F         LD           L,A
51A9: 6F         LD           L,A
51AA: 64         LD           H,H
51AB: 21 20 46   LD           HL,$4620
51AE: 6F         LD           L,A
51AF: 72         LD           (HL),D
51B0: 68         LD           L,B
51B1: 65         LD           H,L
51B2: 61         LD           H,C
51B3: 76         HALT
51B4: 65         LD           H,L
51B5: 6E         LD           L,(HL)
51B6: 5E         LD           E,(HL)
51B7: 73         LD           (HL),E
51B8: 20 73      JR           NZ,$522D
51BA: 61         LD           H,C
51BB: 6B         LD           L,E
51BC: 65         LD           H,L
51BD: 2C         INC         L
51BE: 20 20      JR           NZ,$51E0
51C0: 6D         LD           L,L
51C1: 61         LD           H,C
51C2: 6E         LD           L,(HL)
51C3: 2C         INC         L
51C4: 20 67      JR           NZ,$522D
51C6: 69         LD           L,C
51C7: 76         HALT
51C8: 65         LD           H,L
51C9: 20 74      JR           NZ,$523F
51CB: 68         LD           L,B
51CC: 61         LD           H,C
51CD: 74         LD           (HL),H
51CE: 20 E2      JR           NZ,$51B2
51D0: 74         LD           (HL),H
51D1: 6F         LD           L,A
51D2: 20 4D      JR           NZ,$5221
51D4: 45         LD           B,L
51D5: 21 21 20   LD           HL,$2021
51D8: 20 50      JR           NZ,$522A
51DA: 4C         LD           C,H
51DB: 45         LD           B,L
51DC: 41         LD           B,C
51DD: 53         LD           D,E
51DE: 45         LD           B,L
51DF: 21 48 65   LD           HL,$6548
51E2: 5E         LD           E,(HL)
51E3: 73         LD           (HL),E
51E4: 20 68      JR           NZ,$524E
51E6: 79         LD           A,C
51E7: 73         LD           (HL),E
51E8: 74         LD           (HL),H
51E9: 65         LD           H,L
51EA: 72         LD           (HL),D
51EB: 69         LD           L,C
51EC: 63         LD           H,E
51ED: 61         LD           H,C
51EE: 6C         LD           L,H
51EF: 21 57 68   LD           HL,$6857
51F2: 61         LD           H,C
51F3: 74         LD           (HL),H
51F4: 20 64      JR           NZ,$525A
51F6: 6F         LD           L,A
51F7: 20 79      JR           NZ,$5272
51F9: 6F         LD           L,A
51FA: 75         LD           (HL),L
51FB: 20 64      JR           NZ,$5261
51FD: 6F         LD           L,A
51FE: 3F         CCF
51FF: 20 20      JR           NZ,$5221
5201: 20 20      JR           NZ,$5223
5203: 20 47      JR           NZ,$524C
5205: 69         LD           L,C
5206: 76         HALT
5207: 65         LD           H,L
5208: 20 44      JR           NZ,$524E
520A: 6F         LD           L,A
520B: 6E         LD           L,(HL)
520C: 5E         LD           E,(HL)
520D: 74         LD           (HL),H
520E: FE 4F      CP           $4F
5210: 68         LD           L,B
5211: 20 74      JR           NZ,$5287
5213: 68         LD           L,B
5214: 61         LD           H,C
5215: 6E         LD           L,(HL)
5216: 6B         LD           L,E
5217: 20 79      JR           NZ,$5292
5219: 6F         LD           L,A
521A: 75         LD           (HL),L
521B: 21 20 20   LD           HL,$2020
521E: 20 49      JR           NZ,$5269
5220: 5E         LD           E,(HL)
5221: 6C         LD           L,H
5222: 6C         LD           L,H
5223: 20 74      JR           NZ,$5299
5225: 61         LD           H,C
5226: 6B         LD           L,E
5227: 65         LD           H,L
5228: 20 74      JR           NZ,$529E
522A: 68         LD           L,B
522B: 61         LD           H,C
522C: 74         LD           (HL),H
522D: 21 FF 49   LD           HL,$49FF
5230: 20 64      JR           NZ,$5296
5232: 6F         LD           L,A
5233: 6E         LD           L,(HL)
5234: 5E         LD           E,(HL)
5235: 74         LD           (HL),H
5236: 20 73      JR           NZ,$52AB
5238: 75         LD           (HL),L
5239: 70         LD           (HL),B
523A: 70         LD           (HL),B
523B: 6F         LD           L,A
523C: 73         LD           (HL),E
523D: 65         LD           H,L
523E: 20 69      JR           NZ,$52A9
5240: 74         LD           (HL),H
5241: 20 77      JR           NZ,$52BA
5243: 6F         LD           L,A
5244: 75         LD           (HL),L
5245: 6C         LD           L,H
5246: 64         LD           H,H
5247: 20 64      JR           NZ,$52AD
5249: 6F         LD           L,A
524A: 20 61      JR           NZ,$52AD
524C: 6E         LD           L,(HL)
524D: 79         LD           A,C
524E: 20 67      JR           NZ,$52B7
5250: 6F         LD           L,A
5251: 6F         LD           L,A
5252: 64         LD           H,H
5253: 20 74      JR           NZ,$52C9
5255: 6F         LD           L,A
5256: 20 62      JR           NZ,$52BA
5258: 65         LD           H,L
5259: 67         LD           H,A
525A: 3F         CCF
525B: 20 20      JR           NZ,$527D
525D: 20 20      JR           NZ,$527F
525F: 57         LD           D,A
5260: 65         LD           H,L
5261: 6C         LD           L,H
5262: 6C         LD           L,H
5263: 2C         INC         L
5264: 20 69      JR           NZ,$52CF
5266: 66         LD           H,(HL)
5267: 20 79      JR           NZ,$52E2
5269: 6F         LD           L,A
526A: 75         LD           (HL),L
526B: 20 20      JR           NZ,$528D
526D: 20 20      JR           NZ,$528F
526F: 63         LD           H,E
5270: 68         LD           L,B
5271: 61         LD           H,C
5272: 6E         LD           L,(HL)
5273: 67         LD           H,A
5274: 65         LD           H,L
5275: 20 79      JR           NZ,$52F0
5277: 6F         LD           L,A
5278: 75         LD           (HL),L
5279: 72         LD           (HL),D
527A: 20 20      JR           NZ,$529C
527C: 20 20      JR           NZ,$529E
527E: 20 6D      JR           NZ,$52ED
5280: 69         LD           L,C
5281: 6E         LD           L,(HL)
5282: 64         LD           H,H
5283: 2C         INC         L
5284: 20 74      JR           NZ,$52FA
5286: 65         LD           H,L
5287: 6C         LD           L,H
5288: 6C         LD           L,H
5289: 20 6D      JR           NZ,$52F8
528B: 65         LD           H,L
528C: 2E FF      LD           L,$FF
528E: 20 20      JR           NZ,$52B0
5290: 4D         LD           C,L
5291: 55         LD           D,L
5292: 4E         LD           C,(HL)
5293: 43         LD           B,E
5294: 48         LD           C,B
5295: 20 4D      JR           NZ,$52E4
5297: 55         LD           D,L
5298: 4E         LD           C,(HL)
5299: 43         LD           B,E
529A: 48         LD           C,B
529B: 21 21 20   LD           HL,$2021
529E: 2E 2E      LD           L,$2E
52A0: 2E 20      LD           L,$20
52A2: 2E 2E      LD           L,$2E
52A4: 2E 20      LD           L,$20
52A6: 2E 2E      LD           L,$2E
52A8: 2E 20      LD           L,$20
52AA: 2E 2E      LD           L,$2E
52AC: 2E 20      LD           L,$20
52AE: 54         LD           D,H
52AF: 68         LD           L,B
52B0: 61         LD           H,C
52B1: 74         LD           (HL),H
52B2: 20 77      JR           NZ,$532B
52B4: 61         LD           H,C
52B5: 73         LD           (HL),E
52B6: 20 67      JR           NZ,$531F
52B8: 72         LD           (HL),D
52B9: 65         LD           H,L
52BA: 61         LD           H,C
52BB: 74         LD           (HL),H
52BC: 21 20 49   LD           HL,$4920
52BF: 20 6B      JR           NZ,$532C
52C1: 6E         LD           L,(HL)
52C2: 6F         LD           L,A
52C3: 77         LD           (HL),A
52C4: 20 69      JR           NZ,$532F
52C6: 74         LD           (HL),H
52C7: 5E         LD           E,(HL)
52C8: 73         LD           (HL),E
52C9: 20 6E      JR           NZ,$5339
52CB: 6F         LD           L,A
52CC: 74         LD           (HL),H
52CD: 20 61      JR           NZ,$5330
52CF: 20 66      JR           NZ,$5337
52D1: 61         LD           H,C
52D2: 69         LD           L,C
52D3: 72         LD           (HL),D
52D4: 20 74      JR           NZ,$534A
52D6: 72         LD           (HL),D
52D7: 61         LD           H,C
52D8: 64         LD           H,H
52D9: 65         LD           H,L
52DA: 2C         INC         L
52DB: 20 20      JR           NZ,$52FD
52DD: 20 62      JR           NZ,$5341
52DF: 75         LD           (HL),L
52E0: 74         LD           (HL),H
52E1: 20 68      JR           NZ,$534B
52E3: 65         LD           H,L
52E4: 72         LD           (HL),D
52E5: 65         LD           H,L
52E6: 5E         LD           E,(HL)
52E7: 73         LD           (HL),E
52E8: 20 73      JR           NZ,$535D
52EA: 6F         LD           L,A
52EB: 6D         LD           L,L
52EC: 65         LD           H,L
52ED: 20 62      JR           NZ,$5351
52EF: 61         LD           H,C
52F0: 6E         LD           L,(HL)
52F1: 61         LD           H,C
52F2: 6E         LD           L,(HL)
52F3: 61         LD           H,C
52F4: 73         LD           (HL),E
52F5: 21 20 59   LD           HL,$5920
52F8: 55         LD           D,L
52F9: 4D         LD           C,L
52FA: 2E 2E      LD           L,$2E
52FC: 2E FF      LD           L,$FF
52FE: 59         LD           E,C
52FF: 6F         LD           L,A
5300: 75         LD           (HL),L
5301: 20 67      JR           NZ,$536A
5303: 61         LD           H,C
5304: 76         HALT
5305: 65         LD           H,L
5306: 20 68      JR           NZ,$5370
5308: 69         LD           L,C
5309: 6D         LD           L,L
530A: 20 E2      JR           NZ,$52EE
530C: 20 20      JR           NZ,$532E
530E: 61         LD           H,C
530F: 6E         LD           L,(HL)
5310: 64         LD           H,H
5311: 20 67      JR           NZ,$537A
5313: 6F         LD           L,A
5314: 74         LD           (HL),H
5315: 20 62      JR           NZ,$5379
5317: 61         LD           H,C
5318: 6E         LD           L,(HL)
5319: 61         LD           H,C
531A: 6E         LD           L,(HL)
531B: 61         LD           H,C
531C: 73         LD           (HL),E
531D: 20 E3      JR           NZ,$5302
531F: 20 69      JR           NZ,$538A
5321: 6E         LD           L,(HL)
5322: 20 72      JR           NZ,$5396
5324: 65         LD           H,L
5325: 74         LD           (HL),H
5326: 75         LD           (HL),L
5327: 72         LD           (HL),D
5328: 6E         LD           L,(HL)
5329: 21 20 20   LD           HL,$2020
532C: 20 20      JR           NZ,$534E
532E: 47         LD           B,A
532F: 6F         LD           L,A
5330: 6F         LD           L,A
5331: 64         LD           H,H
5332: 20 64      JR           NZ,$5398
5334: 65         LD           H,L
5335: 61         LD           H,C
5336: 6C         LD           L,H
5337: 21 FF 54   LD           HL,$54FF
533A: 68         LD           L,B
533B: 61         LD           H,C
533C: 6E         LD           L,(HL)
533D: 6B         LD           L,E
533E: 20 79      JR           NZ,$53B9
5340: 6F         LD           L,A
5341: 75         LD           (HL),L
5342: 20 61      JR           NZ,$53A5
5344: 67         LD           H,A
5345: 61         LD           H,C
5346: 69         LD           L,C
5347: 6E         LD           L,(HL)
5348: 21 54 68   LD           HL,$6854
534B: 61         LD           H,C
534C: 74         LD           (HL),H
534D: 20 77      JR           NZ,$53C6
534F: 61         LD           H,C
5350: 73         LD           (HL),E
5351: 20 79      JR           NZ,$53CC
5353: 75         LD           (HL),L
5354: 6D         LD           L,L
5355: 6D         LD           L,L
5356: 79         LD           A,C
5357: 21 FF 48   LD           HL,$48FF
535A: 65         LD           H,L
535B: 79         LD           A,C
535C: 20 66      JR           NZ,$53C4
535E: 72         LD           (HL),D
535F: 69         LD           L,C
5360: 65         LD           H,L
5361: 6E         LD           L,(HL)
5362: 64         LD           H,H
5363: 21 20 48   LD           HL,$4820
5366: 61         LD           H,C
5367: 76         HALT
5368: 65         LD           H,L
5369: 79         LD           A,C
536A: 6F         LD           L,A
536B: 75         LD           (HL),L
536C: 20 65      JR           NZ,$53D3
536E: 76         HALT
536F: 65         LD           H,L
5370: 72         LD           (HL),D
5371: 20 72      JR           NZ,$53E5
5373: 69         LD           L,C
5374: 64         LD           H,H
5375: 64         LD           H,H
5376: 65         LD           H,L
5377: 6E         LD           L,(HL)
5378: 20 74      JR           NZ,$53EE
537A: 68         LD           L,B
537B: 65         LD           H,L
537C: 20 72      JR           NZ,$53F0
537E: 61         LD           H,C
537F: 70         LD           (HL),B
5380: 69         LD           L,C
5381: 64         LD           H,H
5382: 73         LD           (HL),E
5383: 20 6F      JR           NZ,$53F4
5385: 6E         LD           L,(HL)
5386: 20 61      JR           NZ,$53E9
5388: 20 72      JR           NZ,$53FC
538A: 61         LD           H,C
538B: 66         LD           H,(HL)
538C: 74         LD           (HL),H
538D: 3F         CCF
538E: 20 20      JR           NZ,$53B0
5390: 59         LD           E,C
5391: 6F         LD           L,A
5392: 75         LD           (HL),L
5393: 20 63      JR           NZ,$53F8
5395: 61         LD           H,C
5396: 6E         LD           L,(HL)
5397: 2C         INC         L
5398: 20 6E      JR           NZ,$5408
539A: 65         LD           H,L
539B: 61         LD           H,C
539C: 72         LD           (HL),D
539D: 20 54      JR           NZ,$53F3
539F: 61         LD           H,C
53A0: 6C         LD           L,H
53A1: 20 54      JR           NZ,$53F7
53A3: 61         LD           H,C
53A4: 6C         LD           L,H
53A5: 20 20      JR           NZ,$53C7
53A7: 20 20      JR           NZ,$53C9
53A9: 48         LD           C,B
53AA: 65         LD           H,L
53AB: 69         LD           L,C
53AC: 67         LD           H,A
53AD: 68         LD           L,B
53AE: 74         LD           (HL),H
53AF: 73         LD           (HL),E
53B0: 21 20 20   LD           HL,$2020
53B3: 59         LD           E,C
53B4: 6F         LD           L,A
53B5: 75         LD           (HL),L
53B6: 20 20      JR           NZ,$53D8
53B8: 20 6F      JR           NZ,$5429
53BA: 75         LD           (HL),L
53BB: 67         LD           H,A
53BC: 68         LD           L,B
53BD: 74         LD           (HL),H
53BE: 20 74      JR           NZ,$5434
53C0: 6F         LD           L,A
53C1: 20 74      JR           NZ,$5437
53C3: 72         LD           (HL),D
53C4: 79         LD           A,C
53C5: 20 69      JR           NZ,$5430
53C7: 74         LD           (HL),H
53C8: 21 FF 52   LD           HL,$52FF
53CB: 69         LD           L,C
53CC: 6B         LD           L,E
53CD: 5E         LD           E,(HL)
53CE: 6D         LD           L,L
53CF: 20 72      JR           NZ,$5443
53D1: 61         LD           H,C
53D2: 6B         LD           L,E
53D3: 5E         LD           E,(HL)
53D4: 6D         LD           L,L
53D5: 21 20 49   LD           HL,$4920
53D8: 20 20      JR           NZ,$53FA
53DA: 72         LD           (HL),D
53DB: 61         LD           H,C
53DC: 6E         LD           L,(HL)
53DD: 20 6F      JR           NZ,$544E
53DF: 75         LD           (HL),L
53E0: 74         LD           (HL),H
53E1: 20 6F      JR           NZ,$5452
53E3: 66         LD           H,(HL)
53E4: 20 20      JR           NZ,$5406
53E6: 20 20      JR           NZ,$5408
53E8: 20 20      JR           NZ,$540A
53EA: 69         LD           L,C
53EB: 6E         LD           L,(HL)
53EC: 67         LD           H,A
53ED: 72         LD           (HL),D
53EE: 65         LD           H,L
53EF: 64         LD           H,H
53F0: 69         LD           L,C
53F1: 65         LD           H,L
53F2: 6E         LD           L,(HL)
53F3: 74         LD           (HL),H
53F4: 73         LD           (HL),E
53F5: 21 20 20   LD           HL,$2020
53F8: 49         LD           C,C
53F9: 66         LD           H,(HL)
53FA: 49         LD           C,C
53FB: 20 68      JR           NZ,$5465
53FD: 61         LD           H,C
53FE: 64         LD           H,H
53FF: 20 68      JR           NZ,$5469
5401: 6F         LD           L,A
5402: 6E         LD           L,(HL)
5403: 65         LD           H,L
5404: 79         LD           A,C
5405: 2C         INC         L
5406: 20 49      JR           NZ,$5451
5408: 20 20      JR           NZ,$542A
540A: 63         LD           H,E
540B: 6F         LD           L,A
540C: 75         LD           (HL),L
540D: 6C         LD           L,H
540E: 64         LD           H,H
540F: 20 6D      JR           NZ,$547E
5411: 61         LD           H,C
5412: 6B         LD           L,E
5413: 65         LD           H,L
5414: 20 74      JR           NZ,$548A
5416: 68         LD           L,B
5417: 69         LD           L,C
5418: 73         LD           (HL),E
5419: 20 66      JR           NZ,$5481
541B: 69         LD           L,C
541C: 74         LD           (HL),H
541D: 20 66      JR           NZ,$5485
541F: 6F         LD           L,A
5420: 72         LD           (HL),D
5421: 20 61      JR           NZ,$5484
5423: 20 6B      JR           NZ,$5490
5425: 69         LD           L,C
5426: 6E         LD           L,(HL)
5427: 67         LD           H,A
5428: 21 FF 48   LD           HL,$48FF
542B: 69         LD           L,C
542C: 20 68      JR           NZ,$5496
542E: 6F         LD           L,A
542F: 21 20 48   LD           HL,$4820
5432: 65         LD           H,L
5433: 79         LD           A,C
5434: 20 79      JR           NZ,$54AF
5436: 6F         LD           L,A
5437: 75         LD           (HL),L
5438: 21 20 49   LD           HL,$4920
543B: 73         LD           (HL),E
543C: 20 74      JR           NZ,$54B2
543E: 68         LD           L,B
543F: 61         LD           H,C
5440: 74         LD           (HL),H
5441: 20 70      JR           NZ,$54B3
5443: 6F         LD           L,A
5444: 73         LD           (HL),E
5445: 73         LD           (HL),E
5446: 69         LD           L,C
5447: 62         LD           H,D
5448: 6C         LD           L,H
5449: 79         LD           A,C
544A: 61         LD           H,C
544B: 20 E5      JR           NZ,$5432
544D: 20 79      JR           NZ,$54C8
544F: 6F         LD           L,A
5450: 75         LD           (HL),L
5451: 20 68      JR           NZ,$54BB
5453: 61         LD           H,C
5454: 76         HALT
5455: 65         LD           H,L
5456: 3F         CCF
5457: 20 20      JR           NZ,$5479
5459: 20 49      JR           NZ,$54A4
545B: 20 6A      JR           NZ,$54C7
545D: 75         LD           (HL),L
545E: 73         LD           (HL),E
545F: 74         LD           (HL),H
5460: 20 72      JR           NZ,$54D4
5462: 61         LD           H,C
5463: 6E         LD           L,(HL)
5464: 20 6F      JR           NZ,$54D5
5466: 75         LD           (HL),L
5467: 74         LD           (HL),H
5468: 21 20 57   LD           HL,$5720
546B: 69         LD           L,C
546C: 6C         LD           L,H
546D: 6C         LD           L,H
546E: 20 79      JR           NZ,$54E9
5470: 6F         LD           L,A
5471: 75         LD           (HL),L
5472: 20 73      JR           NZ,$54E7
5474: 77         LD           (HL),A
5475: 61         LD           H,C
5476: 70         LD           (HL),B
5477: 20 69      JR           NZ,$54E2
5479: 74         LD           (HL),H
547A: 66         LD           H,(HL)
547B: 6F         LD           L,A
547C: 72         LD           (HL),D
547D: 20 61      JR           NZ,$54E0
547F: 20 70      JR           NZ,$54F1
5481: 69         LD           L,C
5482: 6E         LD           L,(HL)
5483: 65         LD           H,L
5484: 61         LD           H,C
5485: 70         LD           (HL),B
5486: 70         LD           (HL),B
5487: 6C         LD           L,H
5488: 65         LD           H,L
5489: 3F         CCF
548A: 20 20      JR           NZ,$54AC
548C: 20 20      JR           NZ,$54AE
548E: 59         LD           E,C
548F: 65         LD           H,L
5490: 73         LD           (HL),E
5491: 20 20      JR           NZ,$54B3
5493: 4E         LD           C,(HL)
5494: 6F         LD           L,A
5495: FE 59      CP           $59
5497: 6F         LD           L,A
5498: 75         LD           (HL),L
5499: 20 65      JR           NZ,$5500
549B: 78         LD           A,B
549C: 63         LD           H,E
549D: 68         LD           L,B
549E: 61         LD           H,C
549F: 6E         LD           L,(HL)
54A0: 67         LD           H,A
54A1: 65         LD           H,L
54A2: 64         LD           H,H
54A3: 20 E5      JR           NZ,$548A
54A5: 20 66      JR           NZ,$550D
54A7: 6F         LD           L,A
54A8: 72         LD           (HL),D
54A9: 20 E6      JR           NZ,$5491
54AB: 21 20 20   LD           HL,$2020
54AE: 49         LD           C,C
54AF: 74         LD           (HL),H
54B0: 5E         LD           E,(HL)
54B1: 73         LD           (HL),E
54B2: 20 6E      JR           NZ,$5522
54B4: 6F         LD           L,A
54B5: 74         LD           (HL),H
54B6: 61         LD           H,C
54B7: 73         LD           (HL),E
54B8: 20 73      JR           NZ,$552D
54BA: 77         LD           (HL),A
54BB: 65         LD           H,L
54BC: 65         LD           H,L
54BD: 74         LD           (HL),H
54BE: 2C         INC         L
54BF: 20 62      JR           NZ,$5523
54C1: 75         LD           (HL),L
54C2: 74         LD           (HL),H
54C3: 20 69      JR           NZ,$552E
54C5: 74         LD           (HL),H
54C6: 69         LD           L,C
54C7: 73         LD           (HL),E
54C8: 20 64      JR           NZ,$552E
54CA: 65         LD           H,L
54CB: 6C         LD           L,H
54CC: 69         LD           L,C
54CD: 63         LD           H,E
54CE: 69         LD           L,C
54CF: 6F         LD           L,A
54D0: 75         LD           (HL),L
54D1: 73         LD           (HL),E
54D2: 21 20 20   LD           HL,$2020
54D5: 20 FF      JR           NZ,$54D6
54D7: 54         LD           D,H
54D8: 68         LD           L,B
54D9: 61         LD           H,C
54DA: 74         LD           (HL),H
54DB: 5E         LD           E,(HL)
54DC: 73         LD           (HL),E
54DD: 20 61      JR           NZ,$5540
54DF: 20 63      JR           NZ,$5544
54E1: 72         LD           (HL),D
54E2: 79         LD           A,C
54E3: 69         LD           L,C
54E4: 6E         LD           L,(HL)
54E5: 67         LD           H,A
54E6: 20 73      JR           NZ,$555B
54E8: 68         LD           L,B
54E9: 61         LD           H,C
54EA: 6D         LD           L,L
54EB: 65         LD           H,L
54EC: 2C         INC         L
54ED: 20 62      JR           NZ,$5551
54EF: 75         LD           (HL),L
54F0: 74         LD           (HL),H
54F1: 20 49      JR           NZ,$553C
54F3: 20 20      JR           NZ,$5515
54F5: 20 20      JR           NZ,$5517
54F7: 72         LD           (HL),D
54F8: 65         LD           H,L
54F9: 61         LD           H,C
54FA: 6C         LD           L,H
54FB: 69         LD           L,C
54FC: 7A         LD           A,D
54FD: 65         LD           H,L
54FE: 20 74      JR           NZ,$5574
5500: 68         LD           L,B
5501: 6F         LD           L,A
5502: 73         LD           (HL),E
5503: 65         LD           H,L
5504: 20 20      JR           NZ,$5526
5506: 20 61      JR           NZ,$5569
5508: 72         LD           (HL),D
5509: 65         LD           H,L
550A: 20 61      JR           NZ,$556D
550C: 20 72      JR           NZ,$5580
550E: 61         LD           H,C
550F: 72         LD           (HL),D
5510: 65         LD           H,L
5511: 20 20      JR           NZ,$5533
5513: 20 20      JR           NZ,$5535
5515: 20 20      JR           NZ,$5537
5517: 64         LD           H,H
5518: 65         LD           H,L
5519: 6C         LD           L,H
551A: 69         LD           L,C
551B: 63         LD           H,E
551C: 61         LD           H,C
551D: 63         LD           H,E
551E: 79         LD           A,C
551F: 21 FF 48   LD           HL,$48FF
5522: 69         LD           L,C
5523: 20 68      JR           NZ,$558D
5525: 6F         LD           L,A
5526: 21 20 59   LD           HL,$5920
5529: 65         LD           H,L
552A: 61         LD           H,C
552B: 68         LD           L,B
552C: 2C         INC         L
552D: 20 49      JR           NZ,$5578
552F: 20 20      JR           NZ,$5551
5531: 6B         LD           L,E
5532: 6E         LD           L,(HL)
5533: 6F         LD           L,A
5534: 77         LD           (HL),A
5535: 2C         INC         L
5536: 20 74      JR           NZ,$55AC
5538: 68         LD           L,B
5539: 61         LD           H,C
553A: 74         LD           (HL),H
553B: 20 74      JR           NZ,$55B1
553D: 75         LD           (HL),L
553E: 62         LD           H,D
553F: 20 20      JR           NZ,$5561
5541: 6F         LD           L,A
5542: 66         LD           H,(HL)
5543: 20 67      JR           NZ,$55AC
5545: 6F         LD           L,A
5546: 6F         LD           L,A
5547: 20 69      JR           NZ,$55B2
5549: 73         LD           (HL),E
554A: 20 61      JR           NZ,$55AD
554C: 73         LD           (HL),E
554D: 6C         LD           L,H
554E: 65         LD           H,L
554F: 65         LD           H,L
5550: 70         LD           (HL),B
5551: 72         LD           (HL),D
5552: 69         LD           L,C
5553: 67         LD           H,A
5554: 68         LD           L,B
5555: 74         LD           (HL),H
5556: 20 69      JR           NZ,$55C1
5558: 6E         LD           L,(HL)
5559: 20 74      JR           NZ,$55CF
555B: 68         LD           L,B
555C: 65         LD           H,L
555D: 20 77      JR           NZ,$55D6
555F: 61         LD           H,C
5560: 79         LD           A,C
5561: 74         LD           (HL),H
5562: 6F         LD           L,A
5563: 20 59      JR           NZ,$55BE
5565: 61         LD           H,C
5566: 72         LD           (HL),D
5567: 6E         LD           L,(HL)
5568: 61         LD           H,C
5569: 20 44      JR           NZ,$55AF
556B: 65         LD           H,L
556C: 73         LD           (HL),E
556D: 65         LD           H,L
556E: 72         LD           (HL),D
556F: 74         LD           (HL),H
5570: 21 4F 6E   LD           HL,$6E4F
5573: 63         LD           H,E
5574: 65         LD           H,L
5575: 20 68      JR           NZ,$55DF
5577: 65         LD           H,L
5578: 5E         LD           E,(HL)
5579: 73         LD           (HL),E
557A: 20 61      JR           NZ,$55DD
557C: 73         LD           (HL),E
557D: 6C         LD           L,H
557E: 65         LD           H,L
557F: 65         LD           H,L
5580: 70         LD           (HL),B
5581: 68         LD           L,B
5582: 65         LD           H,L
5583: 20 77      JR           NZ,$55FC
5585: 6F         LD           L,A
5586: 6E         LD           L,(HL)
5587: 5E         LD           E,(HL)
5588: 74         LD           (HL),H
5589: 20 62      JR           NZ,$55ED
558B: 75         LD           (HL),L
558C: 64         LD           H,H
558D: 67         LD           H,A
558E: 65         LD           H,L
558F: 20 20      JR           NZ,$55B1
5591: 66         LD           H,(HL)
5592: 6F         LD           L,A
5593: 72         LD           (HL),D
5594: 20 61      JR           NZ,$55F7
5596: 20 6C      JR           NZ,$5604
5598: 6F         LD           L,A
5599: 6F         LD           L,A
559A: 6F         LD           L,A
559B: 6F         LD           L,A
559C: 6F         LD           L,A
559D: 6F         LD           L,A
559E: 6E         LD           L,(HL)
559F: 6E         LD           L,(HL)
55A0: 67         LD           H,A
55A1: 74         LD           (HL),H
55A2: 69         LD           L,C
55A3: 6D         LD           L,L
55A4: 65         LD           H,L
55A5: 2E 20      LD           L,$20
55A7: 20 42      JR           NZ,$55EB
55A9: 75         LD           (HL),L
55AA: 74         LD           (HL),H
55AB: 20 68      JR           NZ,$5615
55AD: 65         LD           H,L
55AE: 79         LD           A,C
55AF: 21 20 54   LD           HL,$5420
55B2: 61         LD           H,C
55B3: 6B         LD           L,E
55B4: 65         LD           H,L
55B5: 20 4C      JR           NZ,$5603
55B7: 69         LD           L,C
55B8: 74         LD           (HL),H
55B9: 74         LD           (HL),H
55BA: 6C         LD           L,H
55BB: 65         LD           H,L
55BC: 20 20      JR           NZ,$55DE
55BE: 20 20      JR           NZ,$55E0
55C0: 20 4D      JR           NZ,$560F
55C2: 61         LD           H,C
55C3: 72         LD           (HL),D
55C4: 69         LD           L,C
55C5: 6E         LD           L,(HL)
55C6: 20 61      JR           NZ,$5629
55C8: 6E         LD           L,(HL)
55C9: 64         LD           H,H
55CA: 20 77      JR           NZ,$5643
55CC: 61         LD           H,C
55CD: 6B         LD           L,E
55CE: 65         LD           H,L
55CF: 20 20      JR           NZ,$55F1
55D1: 68         LD           L,B
55D2: 69         LD           L,C
55D3: 6D         LD           L,L
55D4: 20 75      JR           NZ,$564B
55D6: 70         LD           (HL),B
55D7: 20 77      JR           NZ,$5650
55D9: 69         LD           L,C
55DA: 74         LD           (HL),H
55DB: 68         LD           L,B
55DC: 20 68      JR           NZ,$5646
55DE: 65         LD           H,L
55DF: 72         LD           (HL),D
55E0: 20 73      JR           NZ,$5655
55E2: 6F         LD           L,A
55E3: 6E         LD           L,(HL)
55E4: 67         LD           H,A
55E5: 21 20 20   LD           HL,$2020
55E8: 54         LD           D,H
55E9: 68         LD           L,B
55EA: 61         LD           H,C
55EB: 74         LD           (HL),H
55EC: 20 73      JR           NZ,$5661
55EE: 6C         LD           L,H
55EF: 6F         LD           L,A
55F0: 62         LD           H,D
55F1: 77         LD           (HL),A
55F2: 6F         LD           L,A
55F3: 75         LD           (HL),L
55F4: 6C         LD           L,H
55F5: 64         LD           H,H
55F6: 20 77      JR           NZ,$566F
55F8: 61         LD           H,C
55F9: 6B         LD           L,E
55FA: 65         LD           H,L
55FB: 20 75      JR           NZ,$5672
55FD: 70         LD           (HL),B
55FE: 20 20      JR           NZ,$5620
5600: 20 77      JR           NZ,$5679
5602: 69         LD           L,C
5603: 74         LD           (HL),H
5604: 68         LD           L,B
5605: 20 61      JR           NZ,$5668
5607: 20 6A      JR           NZ,$5673
5609: 75         LD           (HL),L
560A: 6D         LD           L,L
560B: 70         LD           (HL),B
560C: 20 69      JR           NZ,$5677
560E: 66         LD           H,(HL)
560F: 20 20      JR           NZ,$5631
5611: 68         LD           L,B
5612: 65         LD           H,L
5613: 20 68      JR           NZ,$567D
5615: 65         LD           H,L
5616: 61         LD           H,C
5617: 72         LD           (HL),D
5618: 64         LD           H,H
5619: 20 68      JR           NZ,$5683
561B: 65         LD           H,L
561C: 72         LD           (HL),D
561D: 20 20      JR           NZ,$563F
561F: 20 20      JR           NZ,$5641
5621: 73         LD           (HL),E
5622: 69         LD           L,C
5623: 6E         LD           L,(HL)
5624: 67         LD           H,A
5625: 2C         INC         L
5626: 20 66      JR           NZ,$568E
5628: 6F         LD           L,A
5629: 72         LD           (HL),D
562A: 20 73      JR           NZ,$569F
562C: 75         LD           (HL),L
562D: 72         LD           (HL),D
562E: 65         LD           H,L
562F: 21 20 48   LD           HL,$4820
5632: 65         LD           H,L
5633: 68         LD           L,B
5634: 20 68      JR           NZ,$569E
5636: 65         LD           H,L
5637: 68         LD           L,B
5638: 20 68      JR           NZ,$56A2
563A: 65         LD           H,L
563B: 68         LD           L,B
563C: 21 FF 4D   LD           HL,$4DFF
563F: 79         LD           A,C
5640: 20 75      JR           NZ,$56B7
5642: 6C         LD           L,H
5643: 74         LD           (HL),H
5644: 69         LD           L,C
5645: 6D         LD           L,L
5646: 61         LD           H,C
5647: 74         LD           (HL),H
5648: 65         LD           H,L
5649: 20 70      JR           NZ,$56BB
564B: 6C         LD           L,H
564C: 61         LD           H,C
564D: 6E         LD           L,(HL)
564E: 69         LD           L,C
564F: 73         LD           (HL),E
5650: 20 74      JR           NZ,$56C6
5652: 6F         LD           L,A
5653: 20 6F      JR           NZ,$56C4
5655: 70         LD           (HL),B
5656: 65         LD           H,L
5657: 6E         LD           L,(HL)
5658: 20 61      JR           NZ,$56BB
565A: 20 20      JR           NZ,$567C
565C: 20 20      JR           NZ,$567E
565E: 62         LD           H,D
565F: 72         LD           (HL),D
5660: 61         LD           H,C
5661: 6E         LD           L,(HL)
5662: 63         LD           H,E
5663: 68         LD           L,B
5664: 20 69      JR           NZ,$56CF
5666: 6E         LD           L,(HL)
5667: 20 4D      JR           NZ,$56B6
5669: 61         LD           H,C
566A: 62         LD           H,D
566B: 65         LD           H,L
566C: 20 20      JR           NZ,$568E
566E: 56         LD           D,(HL)
566F: 69         LD           L,C
5670: 6C         LD           L,H
5671: 6C         LD           L,H
5672: 61         LD           H,C
5673: 67         LD           H,A
5674: 65         LD           H,L
5675: 21 FF 48   LD           HL,$48FF
5678: 49         LD           C,C
5679: 20 48      JR           NZ,$56C3
567B: 4F         LD           C,A
567C: 21 20 20   LD           HL,$2020
567F: 4C         LD           C,H
5680: 69         LD           L,C
5681: 74         LD           (HL),H
5682: 74         LD           (HL),H
5683: 6C         LD           L,H
5684: 65         LD           H,L
5685: 20 20      JR           NZ,$56A7
5687: 4D         LD           C,L
5688: 61         LD           H,C
5689: 72         LD           (HL),D
568A: 69         LD           L,C
568B: 6E         LD           L,(HL)
568C: 21 20 20   LD           HL,$2020
568F: 57         LD           D,A
5690: 65         LD           H,L
5691: 6C         LD           L,H
5692: 63         LD           H,E
5693: 6F         LD           L,A
5694: 6D         LD           L,L
5695: 65         LD           H,L
5696: 21 2E 2E   LD           HL,$2E2E
5699: 2E 20      LD           L,$20
569B: 2E 2E      LD           L,$2E
569D: 2E 20      LD           L,$20
569F: 2E 2E      LD           L,$2E
56A1: 2E 20      LD           L,$20
56A3: 2E 2E      LD           L,$2E
56A5: 2E 20      LD           L,$20
56A7: 4F         LD           C,A
56A8: 68         LD           L,B
56A9: 2C         INC         L
56AA: 20 73      JR           NZ,$571F
56AC: 68         LD           L,B
56AD: 75         LD           (HL),L
56AE: 63         LD           H,E
56AF: 6B         LD           L,E
56B0: 73         LD           (HL),E
56B1: 21 20 20   LD           HL,$2020
56B4: 59         LD           E,C
56B5: 6F         LD           L,A
56B6: 75         LD           (HL),L
56B7: 61         LD           H,C
56B8: 72         LD           (HL),D
56B9: 65         LD           H,L
56BA: 20 68      JR           NZ,$5724
56BC: 65         LD           H,L
56BD: 72         LD           (HL),D
56BE: 65         LD           H,L
56BF: 20 74      JR           NZ,$5735
56C1: 6F         LD           L,A
56C2: 6F         LD           L,A
56C3: 2E 2E      LD           L,$2E
56C5: 2E 20      LD           L,$20
56C7: 53         LD           D,E
56C8: 6F         LD           L,A
56C9: 72         LD           (HL),D
56CA: 72         LD           (HL),D
56CB: 79         LD           A,C
56CC: 2E 2E      LD           L,$2E
56CE: 2E FF      LD           L,$FF
56D0: 4F         LD           C,A
56D1: 68         LD           L,B
56D2: 2C         INC         L
56D3: 20 23      JR           NZ,$56F8
56D5: 23         INC         HL
56D6: 23         INC         HL
56D7: 23         INC         HL
56D8: 23         INC         HL
56D9: 2C         INC         L
56DA: 20 49      JR           NZ,$5725
56DC: 5E         LD           E,(HL)
56DD: 6D         LD           L,L
56DE: 20 20      JR           NZ,$5700
56E0: 67         LD           H,A
56E1: 6C         LD           L,H
56E2: 61         LD           H,C
56E3: 64         LD           H,H
56E4: 20 79      JR           NZ,$575F
56E6: 6F         LD           L,A
56E7: 75         LD           (HL),L
56E8: 20 66      JR           NZ,$5750
56EA: 6F         LD           L,A
56EB: 75         LD           (HL),L
56EC: 6E         LD           L,(HL)
56ED: 64         LD           H,H
56EE: 20 20      JR           NZ,$5710
56F0: 74         LD           (HL),H
56F1: 68         LD           L,B
56F2: 69         LD           L,C
56F3: 73         LD           (HL),E
56F4: 20 70      JR           NZ,$5766
56F6: 6C         LD           L,H
56F7: 61         LD           H,C
56F8: 63         LD           H,E
56F9: 65         LD           H,L
56FA: 2E 20      LD           L,$20
56FC: 20 20      JR           NZ,$571E
56FE: 20 20      JR           NZ,$5720
5700: 57         LD           D,A
5701: 69         LD           L,C
5702: 6C         LD           L,H
5703: 6C         LD           L,H
5704: 20 79      JR           NZ,$577F
5706: 6F         LD           L,A
5707: 75         LD           (HL),L
5708: 20 73      JR           NZ,$577D
570A: 74         LD           (HL),H
570B: 61         LD           H,C
570C: 79         LD           A,C
570D: 20 20      JR           NZ,$572F
570F: 20 61      JR           NZ,$5772
5711: 6E         LD           L,(HL)
5712: 64         LD           H,H
5713: 20 74      JR           NZ,$5789
5715: 61         LD           H,C
5716: 6C         LD           L,H
5717: 6B         LD           L,E
5718: 20 74      JR           NZ,$578E
571A: 6F         LD           L,A
571B: 20 6D      JR           NZ,$578A
571D: 65         LD           H,L
571E: 20 20      JR           NZ,$5740
5720: 66         LD           H,(HL)
5721: 6F         LD           L,A
5722: 72         LD           (HL),D
5723: 20 61      JR           NZ,$5786
5725: 20 77      JR           NZ,$579E
5727: 68         LD           L,B
5728: 69         LD           L,C
5729: 6C         LD           L,H
572A: 65         LD           H,L
572B: 3F         CCF
572C: 20 20      JR           NZ,$574E
572E: 20 20      JR           NZ,$5750
5730: 20 20      JR           NZ,$5752
5732: 20 20      JR           NZ,$5754
5734: 59         LD           E,C
5735: 65         LD           H,L
5736: 73         LD           (HL),E
5737: 21 20 4E   LD           HL,$4E20
573A: 6F         LD           L,A
573B: 2E 2E      LD           L,$2E
573D: 2E FE      LD           L,$FE
573F: 4F         LD           C,A
5740: 6B         LD           L,E
5741: 61         LD           H,C
5742: 79         LD           A,C
5743: 2C         INC         L
5744: 20 49      JR           NZ,$578F
5746: 5E         LD           E,(HL)
5747: 6C         LD           L,H
5748: 6C         LD           L,H
5749: 20 6A      JR           NZ,$57B5
574B: 75         LD           (HL),L
574C: 73         LD           (HL),E
574D: 74         LD           (HL),H
574E: 20 77      JR           NZ,$57C7
5750: 61         LD           H,C
5751: 74         LD           (HL),H
5752: 63         LD           H,E
5753: 68         LD           L,B
5754: 20 74      JR           NZ,$57CA
5756: 68         LD           L,B
5757: 65         LD           H,L
5758: 20 77      JR           NZ,$57D1
575A: 61         LD           H,C
575B: 76         HALT
575C: 65         LD           H,L
575D: 73         LD           (HL),E
575E: 20 66      JR           NZ,$57C6
5760: 6F         LD           L,A
5761: 72         LD           (HL),D
5762: 20 61      JR           NZ,$57C5
5764: 20 77      JR           NZ,$57DD
5766: 68         LD           L,B
5767: 69         LD           L,C
5768: 6C         LD           L,H
5769: 65         LD           H,L
576A: 2E 2E      LD           L,$2E
576C: 2E FF      LD           L,$FF
576E: 41         LD           B,C
576F: 74         LD           (HL),H
5770: 20 74      JR           NZ,$57E6
5772: 68         LD           L,B
5773: 65         LD           H,L
5774: 20 62      JR           NZ,$57D8
5776: 65         LD           H,L
5777: 61         LD           H,C
5778: 63         LD           H,E
5779: 68         LD           L,B
577A: 2E 2E      LD           L,$2E
577C: 2E 20      LD           L,$20
577E: 20 4D      JR           NZ,$57CD
5780: 61         LD           H,C
5781: 72         LD           (HL),D
5782: 69         LD           L,C
5783: 6E         LD           L,(HL)
5784: 20 20      JR           NZ,$57A6
5786: DE FF      SBC         $FF
5788: 49         LD           C,C
5789: 20 77      JR           NZ,$5802
578B: 6F         LD           L,A
578C: 6E         LD           L,(HL)
578D: 64         LD           H,H
578E: 65         LD           H,L
578F: 72         LD           (HL),D
5790: 20 77      JR           NZ,$5809
5792: 68         LD           L,B
5793: 65         LD           H,L
5794: 72         LD           (HL),D
5795: 65         LD           H,L
5796: 20 20      JR           NZ,$57B8
5798: 74         LD           (HL),H
5799: 68         LD           L,B
579A: 65         LD           H,L
579B: 73         LD           (HL),E
579C: 65         LD           H,L
579D: 20 63      JR           NZ,$5802
579F: 6F         LD           L,A
57A0: 63         LD           H,E
57A1: 6F         LD           L,A
57A2: 6E         LD           L,(HL)
57A3: 75         LD           (HL),L
57A4: 74         LD           (HL),H
57A5: 20 20      JR           NZ,$57C7
57A7: 20 74      JR           NZ,$581D
57A9: 72         LD           (HL),D
57AA: 65         LD           H,L
57AB: 65         LD           H,L
57AC: 73         LD           (HL),E
57AD: 20 63      JR           NZ,$5812
57AF: 6F         LD           L,A
57B0: 6D         LD           L,L
57B1: 65         LD           H,L
57B2: 20 66      JR           NZ,$581A
57B4: 72         LD           (HL),D
57B5: 6F         LD           L,A
57B6: 6D         LD           L,L
57B7: 3F         CCF
57B8: 2E 2E      LD           L,$2E
57BA: 2E 54      LD           L,$54
57BC: 61         LD           H,C
57BD: 72         LD           (HL),D
57BE: 69         LD           L,C
57BF: 6E         LD           L,(HL)
57C0: 20 73      JR           NZ,$5835
57C2: 61         LD           H,C
57C3: 79         LD           A,C
57C4: 73         LD           (HL),E
57C5: 20 20      JR           NZ,$57E7
57C7: 20 74      JR           NZ,$583D
57C9: 68         LD           L,B
57CA: 65         LD           H,L
57CB: 72         LD           (HL),D
57CC: 65         LD           H,L
57CD: 20 69      JR           NZ,$5838
57CF: 73         LD           (HL),E
57D0: 20 6E      JR           NZ,$5840
57D2: 6F         LD           L,A
57D3: 74         LD           (HL),H
57D4: 68         LD           L,B
57D5: 69         LD           L,C
57D6: 6E         LD           L,(HL)
57D7: 67         LD           H,A
57D8: 62         LD           H,D
57D9: 65         LD           H,L
57DA: 79         LD           A,C
57DB: 6F         LD           L,A
57DC: 6E         LD           L,(HL)
57DD: 64         LD           H,H
57DE: 20 74      JR           NZ,$5854
57E0: 68         LD           L,B
57E1: 65         LD           H,L
57E2: 20 73      JR           NZ,$5857
57E4: 65         LD           H,L
57E5: 61         LD           H,C
57E6: 2C         INC         L
57E7: 20 62      JR           NZ,$584B
57E9: 75         LD           (HL),L
57EA: 74         LD           (HL),H
57EB: 20 49      JR           NZ,$5836
57ED: 20 62      JR           NZ,$5851
57EF: 65         LD           H,L
57F0: 6C         LD           L,H
57F1: 69         LD           L,C
57F2: 65         LD           H,L
57F3: 76         HALT
57F4: 65         LD           H,L
57F5: 20 20      JR           NZ,$5817
57F7: 20 74      JR           NZ,$586D
57F9: 68         LD           L,B
57FA: 65         LD           H,L
57FB: 72         LD           (HL),D
57FC: 65         LD           H,L
57FD: 20 6D      JR           NZ,$586C
57FF: 75         LD           (HL),L
5800: 73         LD           (HL),E
5801: 74         LD           (HL),H
5802: 20 62      JR           NZ,$5866
5804: 65         LD           H,L
5805: 20 20      JR           NZ,$5827
5807: 20 73      JR           NZ,$587C
5809: 6F         LD           L,A
580A: 6D         LD           L,L
580B: 65         LD           H,L
580C: 74         LD           (HL),H
580D: 68         LD           L,B
580E: 69         LD           L,C
580F: 6E         LD           L,(HL)
5810: 67         LD           H,A
5811: 20 6F      JR           NZ,$5882
5813: 76         HALT
5814: 65         LD           H,L
5815: 72         LD           (HL),D
5816: 20 20      JR           NZ,$5838
5818: 74         LD           (HL),H
5819: 68         LD           L,B
581A: 65         LD           H,L
581B: 72         LD           (HL),D
581C: 65         LD           H,L
581D: 2E 2E      LD           L,$2E
581F: 2E 20      LD           L,$20
5821: 20 57      JR           NZ,$587A
5823: 68         LD           L,B
5824: 65         LD           H,L
5825: 6E         LD           L,(HL)
5826: 20 49      JR           NZ,$5871
5828: 64         LD           H,H
5829: 69         LD           L,C
582A: 73         LD           (HL),E
582B: 63         LD           H,E
582C: 6F         LD           L,A
582D: 76         HALT
582E: 65         LD           H,L
582F: 72         LD           (HL),D
5830: 65         LD           H,L
5831: 64         LD           H,H
5832: 20 79      JR           NZ,$58AD
5834: 6F         LD           L,A
5835: 75         LD           (HL),L
5836: 2C         INC         L
5837: 20 23      JR           NZ,$585C
5839: 23         INC         HL
583A: 23         INC         HL
583B: 23         INC         HL
583C: 23         INC         HL
583D: 2C         INC         L
583E: 20 6D      JR           NZ,$58AD
5840: 79         LD           A,C
5841: 20 68      JR           NZ,$58AB
5843: 65         LD           H,L
5844: 61         LD           H,C
5845: 72         LD           (HL),D
5846: 74         LD           (HL),H
5847: 20 73      JR           NZ,$58BC
5849: 6B         LD           L,E
584A: 69         LD           L,C
584B: 70         LD           (HL),B
584C: 70         LD           (HL),B
584D: 65         LD           H,L
584E: 64         LD           H,H
584F: 20 61      JR           NZ,$58B2
5851: 20 62      JR           NZ,$58B5
5853: 65         LD           H,L
5854: 61         LD           H,C
5855: 74         LD           (HL),H
5856: 21 20 49   LD           HL,$4920
5859: 20 74      JR           NZ,$58CF
585B: 68         LD           L,B
585C: 6F         LD           L,A
585D: 75         LD           (HL),L
585E: 67         LD           H,A
585F: 68         LD           L,B
5860: 74         LD           (HL),H
5861: 2C         INC         L
5862: 20 74      JR           NZ,$58D8
5864: 68         LD           L,B
5865: 69         LD           L,C
5866: 73         LD           (HL),E
5867: 20 70      JR           NZ,$58D9
5869: 65         LD           H,L
586A: 72         LD           (HL),D
586B: 73         LD           (HL),E
586C: 6F         LD           L,A
586D: 6E         LD           L,(HL)
586E: 20 68      JR           NZ,$58D8
5870: 61         LD           H,C
5871: 73         LD           (HL),E
5872: 20 63      JR           NZ,$58D7
5874: 6F         LD           L,A
5875: 6D         LD           L,L
5876: 65         LD           H,L
5877: 20 74      JR           NZ,$58ED
5879: 6F         LD           L,A
587A: 20 67      JR           NZ,$58E3
587C: 69         LD           L,C
587D: 76         HALT
587E: 65         LD           H,L
587F: 20 75      JR           NZ,$58F6
5881: 73         LD           (HL),E
5882: 20 61      JR           NZ,$58E5
5884: 20 20      JR           NZ,$58A6
5886: 20 20      JR           NZ,$58A8
5888: 6D         LD           L,L
5889: 65         LD           H,L
588A: 73         LD           (HL),E
588B: 73         LD           (HL),E
588C: 61         LD           H,C
588D: 67         LD           H,A
588E: 65         LD           H,L
588F: 2E 2E      LD           L,$2E
5891: 2E FF      LD           L,$FF
5893: 2E 2E      LD           L,$2E
5895: 2E 20      LD           L,$20
5897: 2E 2E      LD           L,$2E
5899: 2E 20      LD           L,$20
589B: 2E 2E      LD           L,$2E
589D: 2E 20      LD           L,$20
589F: 2E 2E      LD           L,$2E
58A1: 2E 20      LD           L,$20
58A3: 2E 2E      LD           L,$2E
58A5: 2E 20      LD           L,$20
58A7: 2E 2E      LD           L,$2E
58A9: 2E 20      LD           L,$20
58AB: 2E 2E      LD           L,$2E
58AD: 2E 20      LD           L,$20
58AF: 2E 2E      LD           L,$2E
58B1: 2E 20      LD           L,$20
58B3: 49         LD           C,C
58B4: 66         LD           H,(HL)
58B5: 20 49      JR           NZ,$5900
58B7: 20 77      JR           NZ,$5930
58B9: 61         LD           H,C
58BA: 73         LD           (HL),E
58BB: 20 61      JR           NZ,$591E
58BD: 20 73      JR           NZ,$5932
58BF: 65         LD           H,L
58C0: 61         LD           H,C
58C1: 20 20      JR           NZ,$58E3
58C3: 67         LD           H,A
58C4: 75         LD           (HL),L
58C5: 6C         LD           L,H
58C6: 6C         LD           L,H
58C7: 2C         INC         L
58C8: 20 49      JR           NZ,$5913
58CA: 20 77      JR           NZ,$5943
58CC: 6F         LD           L,A
58CD: 75         LD           (HL),L
58CE: 6C         LD           L,H
58CF: 64         LD           H,H
58D0: 20 20      JR           NZ,$58F2
58D2: 20 66      JR           NZ,$593A
58D4: 6C         LD           L,H
58D5: 79         LD           A,C
58D6: 20 61      JR           NZ,$5939
58D8: 73         LD           (HL),E
58D9: 20 66      JR           NZ,$5941
58DB: 61         LD           H,C
58DC: 72         LD           (HL),D
58DD: 20 61      JR           NZ,$5940
58DF: 73         LD           (HL),E
58E0: 20 49      JR           NZ,$592B
58E2: 20 63      JR           NZ,$5947
58E4: 6F         LD           L,A
58E5: 75         LD           (HL),L
58E6: 6C         LD           L,H
58E7: 64         LD           H,H
58E8: 21 20 20   LD           HL,$2020
58EB: 49         LD           C,C
58EC: 20 77      JR           NZ,$5965
58EE: 6F         LD           L,A
58EF: 75         LD           (HL),L
58F0: 6C         LD           L,H
58F1: 64         LD           H,H
58F2: 20 66      JR           NZ,$595A
58F4: 6C         LD           L,H
58F5: 79         LD           A,C
58F6: 20 74      JR           NZ,$596C
58F8: 6F         LD           L,A
58F9: 20 66      JR           NZ,$5961
58FB: 61         LD           H,C
58FC: 72         LD           (HL),D
58FD: 20 61      JR           NZ,$5960
58FF: 77         LD           (HL),A
5900: 61         LD           H,C
5901: 79         LD           A,C
5902: 20 70      JR           NZ,$5974
5904: 6C         LD           L,H
5905: 61         LD           H,C
5906: 63         LD           H,E
5907: 65         LD           H,L
5908: 73         LD           (HL),E
5909: 20 61      JR           NZ,$596C
590B: 6E         LD           L,(HL)
590C: 64         LD           H,H
590D: 20 73      JR           NZ,$5982
590F: 69         LD           L,C
5910: 6E         LD           L,(HL)
5911: 67         LD           H,A
5912: 20 66      JR           NZ,$597A
5914: 6F         LD           L,A
5915: 72         LD           (HL),D
5916: 20 6D      JR           NZ,$5985
5918: 61         LD           H,C
5919: 6E         LD           L,(HL)
591A: 79         LD           A,C
591B: 20 70      JR           NZ,$598D
591D: 65         LD           H,L
591E: 6F         LD           L,A
591F: 70         LD           (HL),B
5920: 6C         LD           L,H
5921: 65         LD           H,L
5922: 21 2E 2E   LD           HL,$2E2E
5925: 2E 49      LD           L,$49
5927: 66         LD           H,(HL)
5928: 20 49      JR           NZ,$5973
592A: 20 77      JR           NZ,$59A3
592C: 69         LD           L,C
592D: 73         LD           (HL),E
592E: 68         LD           L,B
592F: 20 74      JR           NZ,$59A5
5931: 6F         LD           L,A
5932: 20 74      JR           NZ,$59A8
5934: 68         LD           L,B
5935: 65         LD           H,L
5936: 20 57      JR           NZ,$598F
5938: 69         LD           L,C
5939: 6E         LD           L,(HL)
593A: 64         LD           H,H
593B: 20 46      JR           NZ,$5983
593D: 69         LD           L,C
593E: 73         LD           (HL),E
593F: 68         LD           L,B
5940: 2C         INC         L
5941: 20 20      JR           NZ,$5963
5943: 49         LD           C,C
5944: 20 77      JR           NZ,$59BD
5946: 6F         LD           L,A
5947: 6E         LD           L,(HL)
5948: 64         LD           H,H
5949: 65         LD           H,L
594A: 72         LD           (HL),D
594B: 20 69      JR           NZ,$59B6
594D: 66         LD           H,(HL)
594E: 20 6D      JR           NZ,$59BD
5950: 79         LD           A,C
5951: 20 20      JR           NZ,$5973
5953: 64         LD           H,H
5954: 72         LD           (HL),D
5955: 65         LD           H,L
5956: 61         LD           H,C
5957: 6D         LD           L,L
5958: 20 77      JR           NZ,$59D1
595A: 69         LD           L,C
595B: 6C         LD           L,H
595C: 6C         LD           L,H
595D: 20 63      JR           NZ,$59C2
595F: 6F         LD           L,A
5960: 6D         LD           L,L
5961: 65         LD           H,L
5962: 20 74      JR           NZ,$59D8
5964: 72         LD           (HL),D
5965: 75         LD           (HL),L
5966: 65         LD           H,L
5967: 2E 2E      LD           L,$2E
5969: 2E 20      LD           L,$20
596B: 2E 2E      LD           L,$2E
596D: 2E 20      LD           L,$20
596F: 2E 2E      LD           L,$2E
5971: 2E FF      LD           L,$FF
5973: 48         LD           C,B
5974: 65         LD           H,L
5975: 79         LD           A,C
5976: 21 20 20   LD           HL,$2020
5979: 41         LD           B,C
597A: 72         LD           (HL),D
597B: 65         LD           H,L
597C: 20 79      JR           NZ,$59F7
597E: 6F         LD           L,A
597F: 75         LD           (HL),L
5980: 20 20      JR           NZ,$59A2
5982: 20 6C      JR           NZ,$59F0
5984: 69         LD           L,C
5985: 73         LD           (HL),E
5986: 74         LD           (HL),H
5987: 65         LD           H,L
5988: 6E         LD           L,(HL)
5989: 69         LD           L,C
598A: 6E         LD           L,(HL)
598B: 67         LD           H,A
598C: 3F         CCF
598D: 20 20      JR           NZ,$59AF
598F: 20 20      JR           NZ,$59B1
5991: 20 20      JR           NZ,$59B3
5993: 23         INC         HL
5994: 23         INC         HL
5995: 23         INC         HL
5996: 23         INC         HL
5997: 23         INC         HL
5998: 2C         INC         L
5999: 20 61      JR           NZ,$59FC
599B: 72         LD           (HL),D
599C: 65         LD           H,L
599D: 20 79      JR           NZ,$5A18
599F: 6F         LD           L,A
59A0: 75         LD           (HL),L
59A1: 20 20      JR           NZ,$59C3
59A3: 6C         LD           L,H
59A4: 69         LD           L,C
59A5: 73         LD           (HL),E
59A6: 74         LD           (HL),H
59A7: 65         LD           H,L
59A8: 6E         LD           L,(HL)
59A9: 69         LD           L,C
59AA: 6E         LD           L,(HL)
59AB: 67         LD           H,A
59AC: 20 74      JR           NZ,$5A22
59AE: 6F         LD           L,A
59AF: 20 6D      JR           NZ,$5A1E
59B1: 65         LD           H,L
59B2: 3F         CCF
59B3: 20 20      JR           NZ,$59D5
59B5: 20 20      JR           NZ,$59D7
59B7: 59         LD           E,C
59B8: 65         LD           H,L
59B9: 61         LD           H,C
59BA: 68         LD           L,B
59BB: 20 4E      JR           NZ,$5A0B
59BD: 6F         LD           L,A
59BE: 2E 2E      LD           L,$2E
59C0: 2E FE      LD           L,$FE
59C2: 49         LD           C,C
59C3: 20 77      JR           NZ,$5A3C
59C5: 61         LD           H,C
59C6: 6E         LD           L,(HL)
59C7: 74         LD           (HL),H
59C8: 20 74      JR           NZ,$5A3E
59CA: 6F         LD           L,A
59CB: 20 6B      JR           NZ,$5A38
59CD: 6E         LD           L,(HL)
59CE: 6F         LD           L,A
59CF: 77         LD           (HL),A
59D0: 20 20      JR           NZ,$59F2
59D2: 65         LD           H,L
59D3: 76         HALT
59D4: 65         LD           H,L
59D5: 72         LD           (HL),D
59D6: 79         LD           A,C
59D7: 74         LD           (HL),H
59D8: 68         LD           L,B
59D9: 69         LD           L,C
59DA: 6E         LD           L,(HL)
59DB: 67         LD           H,A
59DC: 20 61      JR           NZ,$5A3F
59DE: 62         LD           H,D
59DF: 6F         LD           L,A
59E0: 75         LD           (HL),L
59E1: 74         LD           (HL),H
59E2: 79         LD           A,C
59E3: 6F         LD           L,A
59E4: 75         LD           (HL),L
59E5: 2E 2E      LD           L,$2E
59E7: 2E 45      LD           L,$45
59E9: 72         LD           (HL),D
59EA: 72         LD           (HL),D
59EB: 2E 2E      LD           L,$2E
59ED: 2E 55      LD           L,$55
59EF: 68         LD           L,B
59F0: 68         LD           L,B
59F1: 2C         INC         L
59F2: 48         LD           C,B
59F3: 61         LD           H,C
59F4: 20 68      JR           NZ,$5A5E
59F6: 61         LD           H,C
59F7: 20 68      JR           NZ,$5A61
59F9: 61         LD           H,C
59FA: 20 68      JR           NZ,$5A64
59FC: 61         LD           H,C
59FD: 21 FF 48   LD           HL,$48FF
5A00: 75         LD           (HL),L
5A01: 6E         LD           L,(HL)
5A02: 68         LD           L,B
5A03: 3F         CCF
5A04: 20 54      JR           NZ,$5A5A
5A06: 68         LD           L,B
5A07: 65         LD           H,L
5A08: 20 77      JR           NZ,$5A81
5A0A: 61         LD           H,C
5A0B: 6C         LD           L,H
5A0C: 72         LD           (HL),D
5A0D: 75         LD           (HL),L
5A0E: 73         LD           (HL),E
5A0F: 77         LD           (HL),A
5A10: 61         LD           H,C
5A11: 6E         LD           L,(HL)
5A12: 74         LD           (HL),H
5A13: 73         LD           (HL),E
5A14: 20 6D      JR           NZ,$5A83
5A16: 65         LD           H,L
5A17: 20 74      JR           NZ,$5A8D
5A19: 6F         LD           L,A
5A1A: 20 67      JR           NZ,$5A83
5A1C: 6F         LD           L,A
5A1D: 20 20      JR           NZ,$5A3F
5A1F: 74         LD           (HL),H
5A20: 6F         LD           L,A
5A21: 20 68      JR           NZ,$5A8B
5A23: 69         LD           L,C
5A24: 6D         LD           L,L
5A25: 3F         CCF
5A26: 20 20      JR           NZ,$5A48
5A28: 49         LD           C,C
5A29: 74         LD           (HL),H
5A2A: 20 20      JR           NZ,$5A4C
5A2C: 20 20      JR           NZ,$5A4E
5A2E: 20 64      JR           NZ,$5A94
5A30: 6F         LD           L,A
5A31: 65         LD           H,L
5A32: 73         LD           (HL),E
5A33: 6E         LD           L,(HL)
5A34: 5E         LD           E,(HL)
5A35: 74         LD           (HL),H
5A36: 20 6D      JR           NZ,$5AA5
5A38: 61         LD           H,C
5A39: 74         LD           (HL),H
5A3A: 74         LD           (HL),H
5A3B: 65         LD           H,L
5A3C: 72         LD           (HL),D
5A3D: 2C         INC         L
5A3E: 20 49      JR           NZ,$5A89
5A40: 20 77      JR           NZ,$5AB9
5A42: 69         LD           L,C
5A43: 6C         LD           L,H
5A44: 6C         LD           L,H
5A45: 20 67      JR           NZ,$5AAE
5A47: 6F         LD           L,A
5A48: 20 77      JR           NZ,$5AC1
5A4A: 69         LD           L,C
5A4B: 74         LD           (HL),H
5A4C: 68         LD           L,B
5A4D: 20 20      JR           NZ,$5A6F
5A4F: 79         LD           A,C
5A50: 6F         LD           L,A
5A51: 75         LD           (HL),L
5A52: 20 74      JR           NZ,$5AC8
5A54: 6F         LD           L,A
5A55: 20 68      JR           NZ,$5ABF
5A57: 69         LD           L,C
5A58: 6D         LD           L,L
5A59: 2E 2E      LD           L,$2E
5A5B: 2E FF      LD           L,$FF
5A5D: 55         LD           D,L
5A5E: 6E         LD           L,(HL)
5A5F: 6E         LD           L,(HL)
5A60: 6E         LD           L,(HL)
5A61: 6E         LD           L,(HL)
5A62: 67         LD           H,A
5A63: 68         LD           L,B
5A64: 21 20 4F   LD           HL,$4F20
5A67: 77         LD           (HL),A
5A68: 77         LD           (HL),A
5A69: 77         LD           (HL),A
5A6A: 77         LD           (HL),A
5A6B: 77         LD           (HL),A
5A6C: 21 2E 2E   LD           HL,$2E2E
5A6F: 2E 20      LD           L,$20
5A71: 2E 2E      LD           L,$2E
5A73: 2E 20      LD           L,$20
5A75: 2E 2E      LD           L,$2E
5A77: 2E 20      LD           L,$20
5A79: 2E 2E      LD           L,$2E
5A7B: 2E 20      LD           L,$20
5A7D: 49         LD           C,C
5A7E: 5E         LD           E,(HL)
5A7F: 76         HALT
5A80: 65         LD           H,L
5A81: 20 73      JR           NZ,$5AF6
5A83: 75         LD           (HL),L
5A84: 72         LD           (HL),D
5A85: 65         LD           H,L
5A86: 20 6C      JR           NZ,$5AF4
5A88: 6F         LD           L,A
5A89: 73         LD           (HL),E
5A8A: 74         LD           (HL),H
5A8B: 20 20      JR           NZ,$5AAD
5A8D: 6D         LD           L,L
5A8E: 79         LD           A,C
5A8F: 20 74      JR           NZ,$5B05
5A91: 61         LD           H,C
5A92: 73         LD           (HL),E
5A93: 74         LD           (HL),H
5A94: 65         LD           H,L
5A95: 20 66      JR           NZ,$5AFD
5A97: 6F         LD           L,A
5A98: 72         LD           (HL),D
5A99: 20 20      JR           NZ,$5ABB
5A9B: 20 20      JR           NZ,$5ABD
5A9D: 68         LD           L,B
5A9E: 6F         LD           L,A
5A9F: 6E         LD           L,(HL)
5AA0: 65         LD           H,L
5AA1: 79         LD           A,C
5AA2: 21 FF 48   LD           HL,$48FF
5AA5: 75         LD           (HL),L
5AA6: 6D         LD           L,L
5AA7: 70         LD           (HL),B
5AA8: 68         LD           L,B
5AA9: 21 20 59   LD           HL,$5920
5AAC: 6F         LD           L,A
5AAD: 75         LD           (HL),L
5AAE: 72         LD           (HL),D
5AAF: 20 68      JR           NZ,$5B19
5AB1: 65         LD           H,L
5AB2: 61         LD           H,C
5AB3: 64         LD           H,H
5AB4: 69         LD           L,C
5AB5: 73         LD           (HL),E
5AB6: 20 61      JR           NZ,$5B19
5AB8: 6C         LD           L,H
5AB9: 77         LD           (HL),A
5ABA: 61         LD           H,C
5ABB: 79         LD           A,C
5ABC: 73         LD           (HL),E
5ABD: 20 69      JR           NZ,$5B28
5ABF: 6E         LD           L,(HL)
5AC0: 20 74      JR           NZ,$5B36
5AC2: 68         LD           L,B
5AC3: 65         LD           H,L
5AC4: 63         LD           H,E
5AC5: 6C         LD           L,H
5AC6: 6F         LD           L,A
5AC7: 75         LD           (HL),L
5AC8: 64         LD           H,H
5AC9: 73         LD           (HL),E
5ACA: 21 20 57   LD           HL,$5720
5ACD: 69         LD           L,C
5ACE: 6C         LD           L,H
5ACF: 6C         LD           L,H
5AD0: 20 79      JR           NZ,$5B4B
5AD2: 6F         LD           L,A
5AD3: 75         LD           (HL),L
5AD4: 70         LD           (HL),B
5AD5: 6C         LD           L,H
5AD6: 65         LD           H,L
5AD7: 61         LD           H,C
5AD8: 73         LD           (HL),E
5AD9: 65         LD           H,L
5ADA: 20 6C      JR           NZ,$5B48
5ADC: 69         LD           L,C
5ADD: 73         LD           (HL),E
5ADE: 74         LD           (HL),H
5ADF: 65         LD           H,L
5AE0: 6E         LD           L,(HL)
5AE1: 20 74      JR           NZ,$5B57
5AE3: 6F         LD           L,A
5AE4: 6D         LD           L,L
5AE5: 65         LD           H,L
5AE6: 20 6E      JR           NZ,$5B56
5AE8: 65         LD           H,L
5AE9: 78         LD           A,B
5AEA: 74         LD           (HL),H
5AEB: 20 74      JR           NZ,$5B61
5AED: 69         LD           L,C
5AEE: 6D         LD           L,L
5AEF: 65         LD           H,L
5AF0: 3F         CCF
5AF1: 21 FF 5A   LD           HL,$5AFF
5AF4: 5A         LD           E,D
5AF5: 5A         LD           E,D
5AF6: 20 5A      JR           NZ,$5B52
5AF8: 5A         LD           E,D
5AF9: 5A         LD           E,D
5AFA: 20 5A      JR           NZ,$5B56
5AFC: 5A         LD           E,D
5AFD: 5A         LD           E,D
5AFE: 20 5A      JR           NZ,$5B5A
5B00: 5A         LD           E,D
5B01: 5A         LD           E,D
5B02: 20 20      JR           NZ,$5B24
5B04: 2E 2E      LD           L,$2E
5B06: 2E 20      LD           L,$20
5B08: DE 20      SBC         $20
5B0A: 2E 2E      LD           L,$2E
5B0C: 2E 20      LD           L,$20
5B0E: DE 20      SBC         $20
5B10: 2E 2E      LD           L,$2E
5B12: 2E FF      LD           L,$FF
5B14: 59         LD           E,C
5B15: 65         LD           H,L
5B16: 73         LD           (HL),E
5B17: 2C         INC         L
5B18: 20 69      JR           NZ,$5B83
5B1A: 74         LD           (HL),H
5B1B: 5E         LD           E,(HL)
5B1C: 73         LD           (HL),E
5B1D: 20 74      JR           NZ,$5B93
5B1F: 68         LD           L,B
5B20: 61         LD           H,C
5B21: 74         LD           (HL),H
5B22: 20 20      JR           NZ,$5B44
5B24: 6C         LD           L,H
5B25: 61         LD           H,C
5B26: 7A         LD           A,D
5B27: 79         LD           A,C
5B28: 20 77      JR           NZ,$5BA1
5B2A: 61         LD           H,C
5B2B: 6C         LD           L,H
5B2C: 72         LD           (HL),D
5B2D: 75         LD           (HL),L
5B2E: 73         LD           (HL),E
5B2F: 21 20 20   LD           HL,$2020
5B32: 20 20      JR           NZ,$5B54
5B34: 53         LD           D,E
5B35: 68         LD           L,B
5B36: 61         LD           H,C
5B37: 6C         LD           L,H
5B38: 6C         LD           L,H
5B39: 20 77      JR           NZ,$5BB2
5B3B: 65         LD           H,L
5B3C: 20 67      JR           NZ,$5BA5
5B3E: 69         LD           L,C
5B3F: 76         HALT
5B40: 65         LD           H,L
5B41: 20 20      JR           NZ,$5B63
5B43: 20 68      JR           NZ,$5BAD
5B45: 69         LD           L,C
5B46: 6D         LD           L,L
5B47: 20 61      JR           NZ,$5BAA
5B49: 20 6C      JR           NZ,$5BB7
5B4B: 69         LD           L,C
5B4C: 74         LD           (HL),H
5B4D: 74         LD           (HL),H
5B4E: 6C         LD           L,H
5B4F: 65         LD           H,L
5B50: 20 20      JR           NZ,$5B72
5B52: 20 20      JR           NZ,$5B74
5B54: 73         LD           (HL),E
5B55: 75         LD           (HL),L
5B56: 72         LD           (HL),D
5B57: 70         LD           (HL),B
5B58: 72         LD           (HL),D
5B59: 69         LD           L,C
5B5A: 73         LD           (HL),E
5B5B: 65         LD           H,L
5B5C: 3F         CCF
5B5D: 20 20      JR           NZ,$5B7F
5B5F: 20 20      JR           NZ,$5B81
5B61: 20 20      JR           NZ,$5B83
5B63: 20 20      JR           NZ,$5B85
5B65: 20 20      JR           NZ,$5B87
5B67: 20 59      JR           NZ,$5BC2
5B69: 65         LD           H,L
5B6A: 73         LD           (HL),E
5B6B: 20 20      JR           NZ,$5B8D
5B6D: 4E         LD           C,(HL)
5B6E: 6F         LD           L,A
5B6F: 2E 2E      LD           L,$2E
5B71: 2E FE      LD           L,$FE
5B73: 41         LD           B,C
5B74: 68         LD           L,B
5B75: 61         LD           H,C
5B76: 20 68      JR           NZ,$5BE0
5B78: 61         LD           H,C
5B79: 20 68      JR           NZ,$5BE3
5B7B: 61         LD           H,C
5B7C: 21 20 20   LD           HL,$2020
5B7F: 57         LD           D,A
5B80: 6F         LD           L,A
5B81: 77         LD           (HL),A
5B82: 21 48 65   LD           HL,$6548
5B85: 20 63      JR           NZ,$5BEA
5B87: 65         LD           H,L
5B88: 72         LD           (HL),D
5B89: 74         LD           (HL),H
5B8A: 61         LD           H,C
5B8B: 69         LD           L,C
5B8C: 6E         LD           L,(HL)
5B8D: 6C         LD           L,H
5B8E: 79         LD           A,C
5B8F: 20 20      JR           NZ,$5BB1
5B91: 20 20      JR           NZ,$5BB3
5B93: 77         LD           (HL),A
5B94: 6F         LD           L,A
5B95: 6B         LD           L,E
5B96: 65         LD           H,L
5B97: 20 77      JR           NZ,$5C10
5B99: 69         LD           L,C
5B9A: 74         LD           (HL),H
5B9B: 68         LD           L,B
5B9C: 20 61      JR           NZ,$5BFF
5B9E: 20 20      JR           NZ,$5BC0
5BA0: 20 20      JR           NZ,$5BC2
5BA2: 20 73      JR           NZ,$5C17
5BA4: 74         LD           (HL),H
5BA5: 61         LD           H,C
5BA6: 72         LD           (HL),D
5BA7: 74         LD           (HL),H
5BA8: 21 FF 48   LD           HL,$48FF
5BAB: 75         LD           (HL),L
5BAC: 6E         LD           L,(HL)
5BAD: 68         LD           L,B
5BAE: 3F         CCF
5BAF: 20 20      JR           NZ,$5BD1
5BB1: 4F         LD           C,A
5BB2: 68         LD           L,B
5BB3: 2C         INC         L
5BB4: 20 68      JR           NZ,$5C1E
5BB6: 65         LD           H,L
5BB7: 5E         LD           E,(HL)
5BB8: 73         LD           (HL),E
5BB9: 20 63      JR           NZ,$5C1E
5BBB: 61         LD           H,C
5BBC: 6C         LD           L,H
5BBD: 6C         LD           L,H
5BBE: 69         LD           L,C
5BBF: 6E         LD           L,(HL)
5BC0: 67         LD           H,A
5BC1: 20 6D      JR           NZ,$5C30
5BC3: 65         LD           H,L
5BC4: 2E 2E      LD           L,$2E
5BC6: 2E 20      LD           L,$20
5BC8: 20 20      JR           NZ,$5BEA
5BCA: 49         LD           C,C
5BCB: 74         LD           (HL),H
5BCC: 5E         LD           E,(HL)
5BCD: 73         LD           (HL),E
5BCE: 20 74      JR           NZ,$5C44
5BD0: 68         LD           L,B
5BD1: 65         LD           H,L
5BD2: 20 73      JR           NZ,$5C47
5BD4: 61         LD           H,C
5BD5: 6D         LD           L,L
5BD6: 65         LD           H,L
5BD7: 20 61      JR           NZ,$5C3A
5BD9: 73         LD           (HL),E
5BDA: 61         LD           H,C
5BDB: 6C         LD           L,H
5BDC: 77         LD           (HL),A
5BDD: 61         LD           H,C
5BDE: 79         LD           A,C
5BDF: 73         LD           (HL),E
5BE0: 2E 2E      LD           L,$2E
5BE2: 2E 20      LD           L,$20
5BE4: 48         LD           C,B
5BE5: 61         LD           H,C
5BE6: 20 68      JR           NZ,$5C50
5BE8: 61         LD           H,C
5BE9: 21 FF 59   LD           HL,$59FF
5BEC: 6F         LD           L,A
5BED: 75         LD           (HL),L
5BEE: 5E         LD           E,(HL)
5BEF: 72         LD           (HL),D
5BF0: 65         LD           H,L
5BF1: 20 72      JR           NZ,$5C65
5BF3: 69         LD           L,C
5BF4: 67         LD           H,A
5BF5: 68         LD           L,B
5BF6: 74         LD           (HL),H
5BF7: 2C         INC         L
5BF8: 20 69      JR           NZ,$5C63
5BFA: 74         LD           (HL),H
5BFB: 77         LD           (HL),A
5BFC: 6F         LD           L,A
5BFD: 75         LD           (HL),L
5BFE: 6C         LD           L,H
5BFF: 64         LD           H,H
5C00: 20 62      JR           NZ,$5C64
5C02: 65         LD           H,L
5C03: 20 6D      JR           NZ,$5C72
5C05: 65         LD           H,L
5C06: 61         LD           H,C
5C07: 6E         LD           L,(HL)
5C08: 20 74      JR           NZ,$5C7E
5C0A: 6F         LD           L,A
5C0B: 77         LD           (HL),A
5C0C: 61         LD           H,C
5C0D: 6B         LD           L,E
5C0E: 65         LD           H,L
5C0F: 20 68      JR           NZ,$5C79
5C11: 69         LD           L,C
5C12: 6D         LD           L,L
5C13: 20 75      JR           NZ,$5C8A
5C15: 70         LD           (HL),B
5C16: 20 6E      JR           NZ,$5C86
5C18: 6F         LD           L,A
5C19: 77         LD           (HL),A
5C1A: 21 4C 65   LD           HL,$654C
5C1D: 74         LD           (HL),H
5C1E: 5E         LD           E,(HL)
5C1F: 73         LD           (HL),E
5C20: 20 6C      JR           NZ,$5C8E
5C22: 65         LD           H,L
5C23: 74         LD           (HL),H
5C24: 20 68      JR           NZ,$5C8E
5C26: 69         LD           L,C
5C27: 6D         LD           L,L
5C28: 20 20      JR           NZ,$5C4A
5C2A: 20 73      JR           NZ,$5C9F
5C2C: 6C         LD           L,H
5C2D: 65         LD           H,L
5C2E: 65         LD           H,L
5C2F: 70         LD           (HL),B
5C30: 20 73      JR           NZ,$5CA5
5C32: 6F         LD           L,A
5C33: 6D         LD           L,L
5C34: 65         LD           H,L
5C35: 20 6D      JR           NZ,$5CA4
5C37: 6F         LD           L,A
5C38: 72         LD           (HL),D
5C39: 65         LD           H,L
5C3A: 21 FF 23   LD           HL,$23FF
5C3D: 23         INC         HL
5C3E: 23         INC         HL
5C3F: 23         INC         HL
5C40: 23         INC         HL
5C41: 2C         INC         L
5C42: 20 49      JR           NZ,$5C8D
5C44: 5E         LD           E,(HL)
5C45: 6D         LD           L,L
5C46: 20 67      JR           NZ,$5CAF
5C48: 6F         LD           L,A
5C49: 69         LD           L,C
5C4A: 6E         LD           L,(HL)
5C4B: 67         LD           H,A
5C4C: 74         LD           (HL),H
5C4D: 6F         LD           L,A
5C4E: 20 74      JR           NZ,$5CC4
5C50: 68         LD           L,B
5C51: 65         LD           H,L
5C52: 20 41      JR           NZ,$5C95
5C54: 6E         LD           L,(HL)
5C55: 69         LD           L,C
5C56: 6D         LD           L,L
5C57: 61         LD           H,C
5C58: 6C         LD           L,H
5C59: 20 20      JR           NZ,$5C7B
5C5B: 20 56      JR           NZ,$5CB3
5C5D: 69         LD           L,C
5C5E: 6C         LD           L,H
5C5F: 6C         LD           L,H
5C60: 61         LD           H,C
5C61: 67         LD           H,A
5C62: 65         LD           H,L
5C63: 21 20 20   LD           HL,$2020
5C66: 50         LD           D,B
5C67: 6C         LD           L,H
5C68: 65         LD           H,L
5C69: 61         LD           H,C
5C6A: 73         LD           (HL),E
5C6B: 65         LD           H,L
5C6C: 64         LD           H,H
5C6D: 72         LD           (HL),D
5C6E: 6F         LD           L,A
5C6F: 70         LD           (HL),B
5C70: 20 62      JR           NZ,$5CD4
5C72: 79         LD           A,C
5C73: 2C         INC         L
5C74: 20 6F      JR           NZ,$5CE5
5C76: 6B         LD           L,E
5C77: 61         LD           H,C
5C78: 79         LD           A,C
5C79: 3F         CCF
5C7A: FF         RST         0X38
5C7B: 41         LD           B,C
5C7C: 72         LD           (HL),D
5C7D: 66         LD           H,(HL)
5C7E: 68         LD           L,B
5C7F: 21 20 41   LD           HL,$4120
5C82: 72         LD           (HL),D
5C83: 66         LD           H,(HL)
5C84: 68         LD           L,B
5C85: 21 20 41   LD           HL,$4120
5C88: 72         LD           (HL),D
5C89: 66         LD           H,(HL)
5C8A: 21 20 DE   LD           HL,$DE20
5C8D: 20 20      JR           NZ,$5CAF
5C8F: DE 21      SBC         $21
5C91: 20 20      JR           NZ,$5CB3
5C93: DE 20      SBC         $20
5C95: 20 20      JR           NZ,$5CB7
5C97: DE 21      SBC         $21
5C99: 20 20      JR           NZ,$5CBB
5C9B: 2E 2E      LD           L,$2E
5C9D: 2E 2E      LD           L,$2E
5C9F: 2E 20      LD           L,$20
5CA1: DD                              
5CA2: 3F         CCF
5CA3: 3F         CCF
5CA4: 20 FF      JR           NZ,$5CA5
5CA6: 49         LD           C,C
5CA7: 74         LD           (HL),H
5CA8: 5E         LD           E,(HL)
5CA9: 73         LD           (HL),E
5CAA: 20 6E      JR           NZ,$5D1A
5CAC: 6F         LD           L,A
5CAD: 20 75      JR           NZ,$5D24
5CAF: 73         LD           (HL),E
5CB0: 65         LD           H,L
5CB1: 2C         INC         L
5CB2: 20 20      JR           NZ,$5CD4
5CB4: 20 20      JR           NZ,$5CD6
5CB6: 6C         LD           L,H
5CB7: 69         LD           L,C
5CB8: 74         LD           (HL),H
5CB9: 74         LD           (HL),H
5CBA: 6C         LD           L,H
5CBB: 65         LD           H,L
5CBC: 20 62      JR           NZ,$5D20
5CBE: 75         LD           (HL),L
5CBF: 64         LD           H,H
5CC0: 64         LD           H,H
5CC1: 79         LD           A,C
5CC2: 21 20 20   LD           HL,$2020
5CC5: 41         LD           B,C
5CC6: 66         LD           H,(HL)
5CC7: 69         LD           L,C
5CC8: 73         LD           (HL),E
5CC9: 68         LD           L,B
5CCA: 20 74      JR           NZ,$5D40
5CCC: 6F         LD           L,A
5CCD: 6F         LD           L,A
5CCE: 6B         LD           L,E
5CCF: 20 6D      JR           NZ,$5D3E
5CD1: 79         LD           A,C
5CD2: 20 20      JR           NZ,$5CF4
5CD4: 20 20      JR           NZ,$5CF6
5CD6: 68         LD           L,B
5CD7: 6F         LD           L,A
5CD8: 6F         LD           L,A
5CD9: 6B         LD           L,E
5CDA: 2E 2E      LD           L,$2E
5CDC: 2E 20      LD           L,$20
5CDE: 49         LD           C,C
5CDF: 20 6B      JR           NZ,$5D4C
5CE1: 65         LD           H,L
5CE2: 65         LD           H,L
5CE3: 70         LD           (HL),B
5CE4: 20 20      JR           NZ,$5D06
5CE6: 63         LD           H,E
5CE7: 61         LD           H,C
5CE8: 73         LD           (HL),E
5CE9: 74         LD           (HL),H
5CEA: 69         LD           L,C
5CEB: 6E         LD           L,(HL)
5CEC: 67         LD           H,A
5CED: 20 6D      JR           NZ,$5D5C
5CEF: 79         LD           A,C
5CF0: 20 6C      JR           NZ,$5D5E
5CF2: 69         LD           L,C
5CF3: 6E         LD           L,(HL)
5CF4: 65         LD           H,L
5CF5: 20 69      JR           NZ,$5D60
5CF7: 6E         LD           L,(HL)
5CF8: 74         LD           (HL),H
5CF9: 6F         LD           L,A
5CFA: 20 74      JR           NZ,$5D70
5CFC: 68         LD           L,B
5CFD: 65         LD           H,L
5CFE: 20 77      JR           NZ,$5D77
5D00: 61         LD           H,C
5D01: 74         LD           (HL),H
5D02: 65         LD           H,L
5D03: 72         LD           (HL),D
5D04: 2C         INC         L
5D05: 20 62      JR           NZ,$5D69
5D07: 75         LD           (HL),L
5D08: 74         LD           (HL),H
5D09: 20 49      JR           NZ,$5D54
5D0B: 20 68      JR           NZ,$5D75
5D0D: 61         LD           H,C
5D0E: 76         HALT
5D0F: 65         LD           H,L
5D10: 6E         LD           L,(HL)
5D11: 5E         LD           E,(HL)
5D12: 74         LD           (HL),H
5D13: 20 20      JR           NZ,$5D35
5D15: 20 67      JR           NZ,$5D7E
5D17: 6F         LD           L,A
5D18: 74         LD           (HL),H
5D19: 20 61      JR           NZ,$5D7C
5D1B: 20 62      JR           NZ,$5D7F
5D1D: 69         LD           L,C
5D1E: 74         LD           (HL),H
5D1F: 65         LD           H,L
5D20: 2E 2E      LD           L,$2E
5D22: 2E 20      LD           L,$20
5D24: 49         LD           C,C
5D25: 20 74      JR           NZ,$5D9B
5D27: 68         LD           L,B
5D28: 6F         LD           L,A
5D29: 75         LD           (HL),L
5D2A: 67         LD           H,A
5D2B: 68         LD           L,B
5D2C: 74         LD           (HL),H
5D2D: 20 74      JR           NZ,$5DA3
5D2F: 68         LD           L,B
5D30: 69         LD           L,C
5D31: 73         LD           (HL),E
5D32: 20 20      JR           NZ,$5D54
5D34: 20 20      JR           NZ,$5D56
5D36: 77         LD           (HL),A
5D37: 6F         LD           L,A
5D38: 75         LD           (HL),L
5D39: 6C         LD           L,H
5D3A: 64         LD           H,H
5D3B: 20 68      JR           NZ,$5DA5
5D3D: 61         LD           H,C
5D3E: 70         LD           (HL),B
5D3F: 70         LD           (HL),B
5D40: 65         LD           H,L
5D41: 6E         LD           L,(HL)
5D42: 2E 2E      LD           L,$2E
5D44: 2E FF      LD           L,$FF
5D46: 4F         LD           C,A
5D47: 68         LD           L,B
5D48: 21 20 57   LD           HL,$5720
5D4B: 68         LD           L,B
5D4C: 61         LD           H,C
5D4D: 74         LD           (HL),H
5D4E: 20 69      JR           NZ,$5DB9
5D50: 73         LD           (HL),E
5D51: 20 74      JR           NZ,$5DC7
5D53: 68         LD           L,B
5D54: 61         LD           H,C
5D55: 74         LD           (HL),H
5D56: 79         LD           A,C
5D57: 6F         LD           L,A
5D58: 75         LD           (HL),L
5D59: 20 68      JR           NZ,$5DC3
5D5B: 61         LD           H,C
5D5C: 76         HALT
5D5D: 65         LD           H,L
5D5E: 20 69      JR           NZ,$5DC9
5D60: 6E         LD           L,(HL)
5D61: 20 79      JR           NZ,$5DDC
5D63: 6F         LD           L,A
5D64: 75         LD           (HL),L
5D65: 72         LD           (HL),D
5D66: 68         LD           L,B
5D67: 61         LD           H,C
5D68: 6E         LD           L,(HL)
5D69: 64         LD           H,H
5D6A: 3F         CCF
5D6B: 20 20      JR           NZ,$5D8D
5D6D: 49         LD           C,C
5D6E: 74         LD           (HL),H
5D6F: 5E         LD           E,(HL)
5D70: 73         LD           (HL),E
5D71: 20 6E      JR           NZ,$5DE1
5D73: 6F         LD           L,A
5D74: 74         LD           (HL),H
5D75: 20 61      JR           NZ,$5DD8
5D77: 20 66      JR           NZ,$5DDF
5D79: 69         LD           L,C
5D7A: 73         LD           (HL),E
5D7B: 68         LD           L,B
5D7C: 69         LD           L,C
5D7D: 6E         LD           L,(HL)
5D7E: 67         LD           H,A
5D7F: 20 68      JR           NZ,$5DE9
5D81: 6F         LD           L,A
5D82: 6F         LD           L,A
5D83: 6B         LD           L,E
5D84: 2C         INC         L
5D85: 20 69      JR           NZ,$5DF0
5D87: 73         LD           (HL),E
5D88: 20 69      JR           NZ,$5DF3
5D8A: 74         LD           (HL),H
5D8B: 3F         CCF
5D8C: 20 20      JR           NZ,$5DAE
5D8E: 59         LD           E,C
5D8F: 6F         LD           L,A
5D90: 75         LD           (HL),L
5D91: 20 68      JR           NZ,$5DFB
5D93: 61         LD           H,C
5D94: 64         LD           H,H
5D95: 20 62      JR           NZ,$5DF9
5D97: 65         LD           H,L
5D98: 74         LD           (HL),H
5D99: 74         LD           (HL),H
5D9A: 65         LD           H,L
5D9B: 72         LD           (HL),D
5D9C: 20 6C      JR           NZ,$5E0A
5D9E: 65         LD           H,L
5D9F: 74         LD           (HL),H
5DA0: 20 6D      JR           NZ,$5E0F
5DA2: 65         LD           H,L
5DA3: 20 20      JR           NZ,$5DC5
5DA5: 20 68      JR           NZ,$5E0F
5DA7: 61         LD           H,C
5DA8: 76         HALT
5DA9: 65         LD           H,L
5DAA: 20 69      JR           NZ,$5E15
5DAC: 74         LD           (HL),H
5DAD: 2E 20      LD           L,$20
5DAF: 20 49      JR           NZ,$5DFA
5DB1: 5E         LD           E,(HL)
5DB2: 6C         LD           L,H
5DB3: 6C         LD           L,H
5DB4: 20 20      JR           NZ,$5DD6
5DB6: 67         LD           H,A
5DB7: 69         LD           L,C
5DB8: 76         HALT
5DB9: 65         LD           H,L
5DBA: 20 79      JR           NZ,$5E35
5DBC: 6F         LD           L,A
5DBD: 75         LD           (HL),L
5DBE: 20 6D      JR           NZ,$5E2D
5DC0: 79         LD           A,C
5DC1: 20 6E      JR           NZ,$5E31
5DC3: 65         LD           H,L
5DC4: 78         LD           A,B
5DC5: 74         LD           (HL),H
5DC6: 63         LD           H,E
5DC7: 61         LD           H,C
5DC8: 74         LD           (HL),H
5DC9: 63         LD           H,E
5DCA: 68         LD           L,B
5DCB: 20 69      JR           NZ,$5E36
5DCD: 66         LD           H,(HL)
5DCE: 20 79      JR           NZ,$5E49
5DD0: 6F         LD           L,A
5DD1: 75         LD           (HL),L
5DD2: 20 6C      JR           NZ,$5E40
5DD4: 65         LD           H,L
5DD5: 74         LD           (HL),H
5DD6: 6D         LD           L,L
5DD7: 65         LD           H,L
5DD8: 20 68      JR           NZ,$5E42
5DDA: 61         LD           H,C
5DDB: 76         HALT
5DDC: 65         LD           H,L
5DDD: 20 69      JR           NZ,$5E48
5DDF: 74         LD           (HL),H
5DE0: 2E 2E      LD           L,$2E
5DE2: 2E 20      LD           L,$20
5DE4: 20 20      JR           NZ,$5E06
5DE6: 20 20      JR           NZ,$5E08
5DE8: 20 20      JR           NZ,$5E0A
5DEA: 4F         LD           C,A
5DEB: 6B         LD           L,E
5DEC: 61         LD           H,C
5DED: 79         LD           A,C
5DEE: 20 4E      JR           NZ,$5E3E
5DF0: 6F         LD           L,A
5DF1: FE 41      CP           $41
5DF3: 6C         LD           L,H
5DF4: 6C         LD           L,H
5DF5: 20 72      JR           NZ,$5E69
5DF7: 69         LD           L,C
5DF8: 67         LD           H,A
5DF9: 68         LD           L,B
5DFA: 74         LD           (HL),H
5DFB: 2C         INC         L
5DFC: 20 62      JR           NZ,$5E60
5DFE: 6F         LD           L,A
5DFF: 79         LD           A,C
5E00: 2C         INC         L
5E01: 20 66      JR           NZ,$5E69
5E03: 65         LD           H,L
5E04: 61         LD           H,C
5E05: 73         LD           (HL),E
5E06: 74         LD           (HL),H
5E07: 20 79      JR           NZ,$5E82
5E09: 6F         LD           L,A
5E0A: 75         LD           (HL),L
5E0B: 72         LD           (HL),D
5E0C: 20 65      JR           NZ,$5E73
5E0E: 79         LD           A,C
5E0F: 65         LD           H,L
5E10: 73         LD           (HL),E
5E11: 20 6F      JR           NZ,$5E82
5E13: 6E         LD           L,(HL)
5E14: 20 61      JR           NZ,$5E77
5E16: 20 64      JR           NZ,$5E7C
5E18: 69         LD           L,C
5E19: 73         LD           (HL),E
5E1A: 70         LD           (HL),B
5E1B: 6C         LD           L,H
5E1C: 61         LD           H,C
5E1D: 79         LD           A,C
5E1E: 20 6F      JR           NZ,$5E8F
5E20: 66         LD           H,(HL)
5E21: 20 66      JR           NZ,$5E89
5E23: 69         LD           L,C
5E24: 73         LD           (HL),E
5E25: 68         LD           L,B
5E26: 69         LD           L,C
5E27: 6E         LD           L,(HL)
5E28: 67         LD           H,A
5E29: 20 73      JR           NZ,$5E9E
5E2B: 6B         LD           L,E
5E2C: 69         LD           L,C
5E2D: 6C         LD           L,H
5E2E: 6C         LD           L,H
5E2F: 21 FF 59   LD           HL,$59FF
5E32: 6F         LD           L,A
5E33: 75         LD           (HL),L
5E34: 20 73      JR           NZ,$5EA9
5E36: 68         LD           L,B
5E37: 6F         LD           L,A
5E38: 75         LD           (HL),L
5E39: 6C         LD           L,H
5E3A: 64         LD           H,H
5E3B: 20 62      JR           NZ,$5E9F
5E3D: 65         LD           H,L
5E3E: 20 20      JR           NZ,$5E60
5E40: 20 6D      JR           NZ,$5EAF
5E42: 6F         LD           L,A
5E43: 72         LD           (HL),D
5E44: 65         LD           H,L
5E45: 20 6B      JR           NZ,$5EB2
5E47: 69         LD           L,C
5E48: 6E         LD           L,(HL)
5E49: 64         LD           H,H
5E4A: 20 74      JR           NZ,$5EC0
5E4C: 6F         LD           L,A
5E4D: 20 6D      JR           NZ,$5EBC
5E4F: 65         LD           H,L
5E50: 21 49 20   LD           HL,$2049
5E53: 74         LD           (HL),H
5E54: 68         LD           L,B
5E55: 6F         LD           L,A
5E56: 75         LD           (HL),L
5E57: 67         LD           H,A
5E58: 68         LD           L,B
5E59: 74         LD           (HL),H
5E5A: 20 77      JR           NZ,$5ED3
5E5C: 65         LD           H,L
5E5D: 20 20      JR           NZ,$5E7F
5E5F: 20 20      JR           NZ,$5E81
5E61: 77         LD           (HL),A
5E62: 65         LD           H,L
5E63: 72         LD           (HL),D
5E64: 65         LD           H,L
5E65: 20 62      JR           NZ,$5EC9
5E67: 75         LD           (HL),L
5E68: 64         LD           H,H
5E69: 64         LD           H,H
5E6A: 69         LD           L,C
5E6B: 65         LD           H,L
5E6C: 73         LD           (HL),E
5E6D: 21 FF 57   LD           HL,$57FF
5E70: 68         LD           L,B
5E71: 6F         LD           L,A
5E72: 6F         LD           L,A
5E73: 6F         LD           L,A
5E74: 61         LD           H,C
5E75: 68         LD           L,B
5E76: 20 6E      JR           NZ,$5EE6
5E78: 65         LD           H,L
5E79: 6C         LD           L,H
5E7A: 6C         LD           L,H
5E7B: 69         LD           L,C
5E7C: 65         LD           H,L
5E7D: 21 21 49   LD           HL,$4921
5E80: 74         LD           (HL),H
5E81: 5E         LD           E,(HL)
5E82: 73         LD           (HL),E
5E83: 20 61      JR           NZ,$5EE6
5E85: 20 62      JR           NZ,$5EE9
5E87: 69         LD           L,C
5E88: 67         LD           H,A
5E89: 20 6F      JR           NZ,$5EFA
5E8B: 6E         LD           L,(HL)
5E8C: 65         LD           H,L
5E8D: 21 21 42   LD           HL,$4221
5E90: 69         LD           L,C
5E91: 67         LD           H,A
5E92: 21 20 42   LD           HL,$4220
5E95: 69         LD           L,C
5E96: 67         LD           H,A
5E97: 21 20 59   LD           HL,$5920
5E9A: 61         LD           H,C
5E9B: 61         LD           H,C
5E9C: 61         LD           H,C
5E9D: 68         LD           L,B
5E9E: 21 FF 54   LD           HL,$54FF
5EA1: 68         LD           L,B
5EA2: 65         LD           H,L
5EA3: 20 E9      JR           NZ,$5E8E
5EA5: 20 62      JR           NZ,$5F09
5EA7: 65         LD           H,L
5EA8: 63         LD           H,E
5EA9: 61         LD           H,C
5EAA: 6D         LD           L,L
5EAB: 65         LD           H,L
5EAC: 20 61      JR           NZ,$5F0F
5EAE: 20 20      JR           NZ,$5ED0
5EB0: 6E         LD           L,(HL)
5EB1: 65         LD           H,L
5EB2: 63         LD           H,E
5EB3: 6B         LD           L,E
5EB4: 6C         LD           L,H
5EB5: 61         LD           H,C
5EB6: 63         LD           H,E
5EB7: 65         LD           H,L
5EB8: 20 EA      JR           NZ,$5EA4
5EBA: 21 20 20   LD           HL,$2020
5EBD: 20 20      JR           NZ,$5EDF
5EBF: 20 4C      JR           NZ,$5F0D
5EC1: 2D         DEC         L
5EC2: 6C         LD           L,H
5EC3: 2D         DEC         L
5EC4: 6C         LD           L,H
5EC5: 75         LD           (HL),L
5EC6: 63         LD           H,E
5EC7: 6B         LD           L,E
5EC8: 79         LD           A,C
5EC9: 21 FF 49   LD           HL,$49FF
5ECC: 20 63      JR           NZ,$5F31
5ECE: 61         LD           H,C
5ECF: 6E         LD           L,(HL)
5ED0: 5E         LD           E,(HL)
5ED1: 74         LD           (HL),H
5ED2: 20 77      JR           NZ,$5F4B
5ED4: 61         LD           H,C
5ED5: 69         LD           L,C
5ED6: 74         LD           (HL),H
5ED7: 20 74      JR           NZ,$5F4D
5ED9: 6F         LD           L,A
5EDA: 20 73      JR           NZ,$5F4F
5EDC: 65         LD           H,L
5EDD: 65         LD           H,L
5EDE: 20 77      JR           NZ,$5F57
5EE0: 68         LD           L,B
5EE1: 61         LD           H,C
5EE2: 74         LD           (HL),H
5EE3: 20 49      JR           NZ,$5F2E
5EE5: 5E         LD           E,(HL)
5EE6: 6C         LD           L,H
5EE7: 6C         LD           L,H
5EE8: 20 20      JR           NZ,$5F0A
5EEA: 20 63      JR           NZ,$5F4F
5EEC: 61         LD           H,C
5EED: 74         LD           (HL),H
5EEE: 63         LD           H,E
5EEF: 68         LD           L,B
5EF0: 20 6E      JR           NZ,$5F60
5EF2: 65         LD           H,L
5EF3: 78         LD           A,B
5EF4: 74         LD           (HL),H
5EF5: 21 FF 57   LD           HL,$57FF
5EF8: 68         LD           L,B
5EF9: 65         LD           H,L
5EFA: 6E         LD           L,(HL)
5EFB: 20 49      JR           NZ,$5F46
5EFD: 20 77      JR           NZ,$5F76
5EFF: 61         LD           H,C
5F00: 73         LD           (HL),E
5F01: 20 73      JR           NZ,$5F76
5F03: 77         LD           (HL),A
5F04: 69         LD           L,C
5F05: 6D         LD           L,L
5F06: 2D         DEC         L
5F07: 6D         LD           L,L
5F08: 69         LD           L,C
5F09: 6E         LD           L,(HL)
5F0A: 67         LD           H,A
5F0B: 20 69      JR           NZ,$5F76
5F0D: 6E         LD           L,(HL)
5F0E: 20 74      JR           NZ,$5F84
5F10: 68         LD           L,B
5F11: 65         LD           H,L
5F12: 20 62      JR           NZ,$5F76
5F14: 61         LD           H,C
5F15: 79         LD           A,C
5F16: 2C         INC         L
5F17: 74         LD           (HL),H
5F18: 68         LD           L,B
5F19: 65         LD           H,L
5F1A: 20 77      JR           NZ,$5F93
5F1C: 61         LD           H,C
5F1D: 76         HALT
5F1E: 65         LD           H,L
5F1F: 73         LD           (HL),E
5F20: 20 74      JR           NZ,$5F96
5F22: 6F         LD           L,A
5F23: 6F         LD           L,A
5F24: 6B         LD           L,E
5F25: 20 61      JR           NZ,$5F88
5F27: 76         HALT
5F28: 65         LD           H,L
5F29: 72         LD           (HL),D
5F2A: 79         LD           A,C
5F2B: 20 69      JR           NZ,$5F96
5F2D: 6D         LD           L,L
5F2E: 70         LD           (HL),B
5F2F: 6F         LD           L,A
5F30: 72         LD           (HL),D
5F31: 74         LD           (HL),H
5F32: 61         LD           H,C
5F33: 6E         LD           L,(HL)
5F34: 74         LD           (HL),H
5F35: 20 20      JR           NZ,$5F57
5F37: 6E         LD           L,(HL)
5F38: 65         LD           H,L
5F39: 63         LD           H,E
5F3A: 6B         LD           L,E
5F3B: 6C         LD           L,H
5F3C: 61         LD           H,C
5F3D: 63         LD           H,E
5F3E: 65         LD           H,L
5F3F: 20 66      JR           NZ,$5FA7
5F41: 72         LD           (HL),D
5F42: 6F         LD           L,A
5F43: 6D         LD           L,L
5F44: 20 20      JR           NZ,$5F66
5F46: 20 61      JR           NZ,$5FA9
5F48: 72         LD           (HL),D
5F49: 6F         LD           L,A
5F4A: 75         LD           (HL),L
5F4B: 6E         LD           L,(HL)
5F4C: 64         LD           H,H
5F4D: 20 6D      JR           NZ,$5FBC
5F4F: 79         LD           A,C
5F50: 20 6E      JR           NZ,$5FC0
5F52: 65         LD           H,L
5F53: 63         LD           H,E
5F54: 6B         LD           L,E
5F55: 21 20 49   LD           HL,$4920
5F58: 66         LD           H,(HL)
5F59: 20 79      JR           NZ,$5FD4
5F5B: 6F         LD           L,A
5F5C: 75         LD           (HL),L
5F5D: 20 66      JR           NZ,$5FC5
5F5F: 69         LD           L,C
5F60: 6E         LD           L,(HL)
5F61: 64         LD           H,H
5F62: 20 69      JR           NZ,$5FCD
5F64: 74         LD           (HL),H
5F65: 2C         INC         L
5F66: 20 49      JR           NZ,$5FB1
5F68: 20 77      JR           NZ,$5FE1
5F6A: 69         LD           L,C
5F6B: 6C         LD           L,H
5F6C: 6C         LD           L,H
5F6D: 20 6C      JR           NZ,$5FDB
5F6F: 65         LD           H,L
5F70: 74         LD           (HL),H
5F71: 20 79      JR           NZ,$5FEC
5F73: 6F         LD           L,A
5F74: 75         LD           (HL),L
5F75: 20 20      JR           NZ,$5F97
5F77: 74         LD           (HL),H
5F78: 61         LD           H,C
5F79: 6B         LD           L,E
5F7A: 65         LD           H,L
5F7B: 20 61      JR           NZ,$5FDE
5F7D: 20 73      JR           NZ,$5FF2
5F7F: 63         LD           H,E
5F80: 61         LD           H,C
5F81: 6C         LD           L,H
5F82: 65         LD           H,L
5F83: 20 20      JR           NZ,$5FA5
5F85: 20 20      JR           NZ,$5FA7
5F87: 66         LD           H,(HL)
5F88: 72         LD           (HL),D
5F89: 6F         LD           L,A
5F8A: 6D         LD           L,L
5F8B: 20 6D      JR           NZ,$5FFA
5F8D: 79         LD           A,C
5F8E: 20 74      JR           NZ,$6004
5F90: 61         LD           H,C
5F91: 69         LD           L,C
5F92: 6C         LD           L,H
5F93: 21 20 20   LD           HL,$2020
5F96: 20 FF      JR           NZ,$5F97
5F98: 49         LD           C,C
5F99: 20 68      JR           NZ,$6003
5F9B: 61         LD           H,C
5F9C: 76         HALT
5F9D: 65         LD           H,L
5F9E: 20 61      JR           NZ,$6001
5FA0: 6C         LD           L,H
5FA1: 72         LD           (HL),D
5FA2: 65         LD           H,L
5FA3: 61         LD           H,C
5FA4: 64         LD           H,H
5FA5: 79         LD           A,C
5FA6: 20 20      JR           NZ,$5FC8
5FA8: 6C         LD           L,H
5FA9: 6F         LD           L,A
5FAA: 6F         LD           L,A
5FAB: 6B         LD           L,E
5FAC: 65         LD           H,L
5FAD: 64         LD           H,H
5FAE: 20 61      JR           NZ,$6011
5FB0: 72         LD           (HL),D
5FB1: 6F         LD           L,A
5FB2: 75         LD           (HL),L
5FB3: 6E         LD           L,(HL)
5FB4: 64         LD           H,H
5FB5: 20 20      JR           NZ,$5FD7
5FB7: 20 68      JR           NZ,$6021
5FB9: 65         LD           H,L
5FBA: 72         LD           (HL),D
5FBB: 65         LD           H,L
5FBC: 21 FF 41   LD           HL,$41FF
5FBF: 68         LD           L,B
5FC0: 68         LD           L,B
5FC1: 21 20 20   LD           HL,$2020
5FC4: 54         LD           D,H
5FC5: 68         LD           L,B
5FC6: 61         LD           H,C
5FC7: 74         LD           (HL),H
5FC8: 5E         LD           E,(HL)
5FC9: 73         LD           (HL),E
5FCA: 20 69      JR           NZ,$6035
5FCC: 74         LD           (HL),H
5FCD: 21 54 68   LD           HL,$6854
5FD0: 61         LD           H,C
5FD1: 74         LD           (HL),H
5FD2: 5E         LD           E,(HL)
5FD3: 73         LD           (HL),E
5FD4: 20 6D      JR           NZ,$6043
5FD6: 79         LD           A,C
5FD7: 20 6E      JR           NZ,$6047
5FD9: 65         LD           H,L
5FDA: 63         LD           H,E
5FDB: 6B         LD           L,E
5FDC: 2D         DEC         L
5FDD: 20 6C      JR           NZ,$604B
5FDF: 61         LD           H,C
5FE0: 63         LD           H,E
5FE1: 65         LD           H,L
5FE2: 21 20 20   LD           HL,$2020
5FE5: 47         LD           B,A
5FE6: 69         LD           L,C
5FE7: 76         HALT
5FE8: 65         LD           H,L
5FE9: 20 69      JR           NZ,$6054
5FEB: 74         LD           (HL),H
5FEC: 21 20 47   LD           HL,$4720
5FEF: 69         LD           L,C
5FF0: 76         HALT
5FF1: 65         LD           H,L
5FF2: 20 69      JR           NZ,$605D
5FF4: 74         LD           (HL),H
5FF5: 20 62      JR           NZ,$6059
5FF7: 61         LD           H,C
5FF8: 63         LD           H,E
5FF9: 6B         LD           L,E
5FFA: 21 20 20   LD           HL,$2020
5FFD: 49         LD           C,C
5FFE: 77         LD           (HL),A
5FFF: 69         LD           L,C
6000: 6C         LD           L,H
6001: 6C         LD           L,H
6002: 20 67      JR           NZ,$606B
6004: 69         LD           L,C
6005: 76         HALT
6006: 65         LD           H,L
6007: 20 79      JR           NZ,$6082
6009: 6F         LD           L,A
600A: 75         LD           (HL),L
600B: 20 61      JR           NZ,$606E
600D: 20 73      JR           NZ,$6082
600F: 63         LD           H,E
6010: 61         LD           H,C
6011: 6C         LD           L,H
6012: 65         LD           H,L
6013: 20 61      JR           NZ,$6076
6015: 73         LD           (HL),E
6016: 20 49      JR           NZ,$6061
6018: 20 73      JR           NZ,$608D
601A: 61         LD           H,C
601B: 69         LD           L,C
601C: 64         LD           H,H
601D: 21 20 20   LD           HL,$2020
6020: 20 20      JR           NZ,$6042
6022: 47         LD           B,A
6023: 69         LD           L,C
6024: 76         HALT
6025: 65         LD           H,L
6026: 20 4B      JR           NZ,$6073
6028: 65         LD           H,L
6029: 65         LD           H,L
602A: 70         LD           (HL),B
602B: FE 50      CP           $50
602D: 72         LD           (HL),D
602E: 6F         LD           L,A
602F: 6D         LD           L,L
6030: 69         LD           L,C
6031: 73         LD           (HL),E
6032: 65         LD           H,L
6033: 21 20 20   LD           HL,$2020
6036: 59         LD           E,C
6037: 6F         LD           L,A
6038: 75         LD           (HL),L
6039: 5E         LD           E,(HL)
603A: 6C         LD           L,H
603B: 6C         LD           L,H
603C: 6F         LD           L,A
603D: 6E         LD           L,(HL)
603E: 6C         LD           L,H
603F: 79         LD           A,C
6040: 20 74      JR           NZ,$60B6
6042: 61         LD           H,C
6043: 6B         LD           L,E
6044: 65         LD           H,L
6045: 20 6F      JR           NZ,$60B6
6047: 6E         LD           L,(HL)
6048: 65         LD           H,L
6049: 21 FF 59   LD           HL,$59FF
604C: 6F         LD           L,A
604D: 75         LD           (HL),L
604E: 20 61      JR           NZ,$60B1
6050: 72         LD           (HL),D
6051: 65         LD           H,L
6052: 20 68      JR           NZ,$60BC
6054: 65         LD           H,L
6055: 61         LD           H,C
6056: 72         LD           (HL),D
6057: 74         LD           (HL),H
6058: 2D         DEC         L
6059: 20 20      JR           NZ,$607B
605B: 6C         LD           L,H
605C: 65         LD           H,L
605D: 73         LD           (HL),E
605E: 73         LD           (HL),E
605F: 20 61      JR           NZ,$60C2
6061: 6E         LD           L,(HL)
6062: 64         LD           H,H
6063: 20 63      JR           NZ,$60C8
6065: 72         LD           (HL),D
6066: 75         LD           (HL),L
6067: 65         LD           H,L
6068: 6C         LD           L,H
6069: 21 FF 59   LD           HL,$59FF
606C: 6F         LD           L,A
606D: 75         LD           (HL),L
606E: 20 72      JR           NZ,$60E2
6070: 65         LD           H,L
6071: 74         LD           (HL),H
6072: 75         LD           (HL),L
6073: 72         LD           (HL),D
6074: 6E         LD           L,(HL)
6075: 65         LD           H,L
6076: 64         LD           H,H
6077: 20 74      JR           NZ,$60ED
6079: 68         LD           L,B
607A: 65         LD           H,L
607B: 6E         LD           L,(HL)
607C: 65         LD           H,L
607D: 63         LD           H,E
607E: 6B         LD           L,E
607F: 6C         LD           L,H
6080: 61         LD           H,C
6081: 63         LD           H,E
6082: 65         LD           H,L
6083: 20 EA      JR           NZ,$606F
6085: 20 61      JR           NZ,$60E8
6087: 6E         LD           L,(HL)
6088: 64         LD           H,H
6089: 20 20      JR           NZ,$60AB
608B: 67         LD           H,A
608C: 6F         LD           L,A
608D: 74         LD           (HL),H
608E: 20 61      JR           NZ,$60F1
6090: 20 73      JR           NZ,$6105
6092: 63         LD           H,E
6093: 61         LD           H,C
6094: 6C         LD           L,H
6095: 65         LD           H,L
6096: 20 EB      JR           NZ,$6083
6098: 20 6F      JR           NZ,$6109
609A: 66         LD           H,(HL)
609B: 74         LD           (HL),H
609C: 68         LD           L,B
609D: 65         LD           H,L
609E: 20 6D      JR           NZ,$610D
60A0: 65         LD           H,L
60A1: 72         LD           (HL),D
60A2: 6D         LD           L,L
60A3: 61         LD           H,C
60A4: 69         LD           L,C
60A5: 64         LD           H,H
60A6: 5E         LD           E,(HL)
60A7: 73         LD           (HL),E
60A8: 20 20      JR           NZ,$60CA
60AA: 20 74      JR           NZ,$6120
60AC: 61         LD           H,C
60AD: 69         LD           L,C
60AE: 6C         LD           L,H
60AF: 2E 20      LD           L,$20
60B1: 20 48      JR           NZ,$60FB
60B3: 6F         LD           L,A
60B4: 77         LD           (HL),A
60B5: 20 77      JR           NZ,$612E
60B7: 69         LD           L,C
60B8: 6C         LD           L,H
60B9: 6C         LD           L,H
60BA: 20 79      JR           NZ,$6135
60BC: 6F         LD           L,A
60BD: 75         LD           (HL),L
60BE: 20 75      JR           NZ,$6135
60C0: 73         LD           (HL),E
60C1: 65         LD           H,L
60C2: 20 74      JR           NZ,$6138
60C4: 68         LD           L,B
60C5: 69         LD           L,C
60C6: 73         LD           (HL),E
60C7: 3F         CCF
60C8: FF         RST         0X38
60C9: 41         LD           B,C
60CA: 6E         LD           L,(HL)
60CB: 20 61      JR           NZ,$612E
60CD: 72         LD           (HL),D
60CE: 74         LD           (HL),H
60CF: 69         LD           L,C
60D0: 73         LD           (HL),E
60D1: 74         LD           (HL),H
60D2: 20 6F      JR           NZ,$6143
60D4: 6E         LD           L,(HL)
60D5: 63         LD           H,E
60D6: 65         LD           H,L
60D7: 20 20      JR           NZ,$60F9
60D9: 61         LD           H,C
60DA: 73         LD           (HL),E
60DB: 6B         LD           L,E
60DC: 65         LD           H,L
60DD: 64         LD           H,H
60DE: 20 6D      JR           NZ,$614D
60E0: 65         LD           H,L
60E1: 20 74      JR           NZ,$6157
60E3: 6F         LD           L,A
60E4: 20 70      JR           NZ,$6156
60E6: 6F         LD           L,A
60E7: 73         LD           (HL),E
60E8: 65         LD           H,L
60E9: 66         LD           H,(HL)
60EA: 6F         LD           L,A
60EB: 72         LD           (HL),D
60EC: 20 68      JR           NZ,$6156
60EE: 69         LD           L,C
60EF: 6D         LD           L,L
60F0: 2C         INC         L
60F1: 20 61      JR           NZ,$6154
60F3: 6E         LD           L,(HL)
60F4: 64         LD           H,H
60F5: 20 68      JR           NZ,$615F
60F7: 65         LD           H,L
60F8: 20 77      JR           NZ,$6171
60FA: 61         LD           H,C
60FB: 6E         LD           L,(HL)
60FC: 74         LD           (HL),H
60FD: 65         LD           H,L
60FE: 64         LD           H,H
60FF: 20 61      JR           NZ,$6162
6101: 20 73      JR           NZ,$6176
6103: 63         LD           H,E
6104: 61         LD           H,C
6105: 6C         LD           L,H
6106: 65         LD           H,L
6107: 2C         INC         L
6108: 20 74      JR           NZ,$617E
610A: 6F         LD           L,A
610B: 6F         LD           L,A
610C: 2E 2E      LD           L,$2E
610E: 2E 20      LD           L,$20
6110: 20 43      JR           NZ,$6155
6112: 61         LD           H,C
6113: 6E         LD           L,(HL)
6114: 20 74      JR           NZ,$618A
6116: 68         LD           L,B
6117: 65         LD           H,L
6118: 20 6C      JR           NZ,$6186
611A: 65         LD           H,L
611B: 67         LD           H,A
611C: 65         LD           H,L
611D: 6E         LD           L,(HL)
611E: 64         LD           H,H
611F: 20 6F      JR           NZ,$6190
6121: 66         LD           H,(HL)
6122: 20 74      JR           NZ,$6198
6124: 68         LD           L,B
6125: 65         LD           H,L
6126: 20 20      JR           NZ,$6148
6128: 20 4D      JR           NZ,$6177
612A: 61         LD           H,C
612B: 67         LD           H,A
612C: 6E         LD           L,(HL)
612D: 69         LD           L,C
612E: 66         LD           H,(HL)
612F: 79         LD           A,C
6130: 69         LD           L,C
6131: 6E         LD           L,(HL)
6132: 67         LD           H,A
6133: 20 4C      JR           NZ,$6181
6135: 65         LD           H,L
6136: 6E         LD           L,(HL)
6137: 73         LD           (HL),E
6138: 20 62      JR           NZ,$619C
613A: 65         LD           H,L
613B: 20 74      JR           NZ,$61B1
613D: 72         LD           (HL),D
613E: 75         LD           (HL),L
613F: 65         LD           H,L
6140: 2E 2E      LD           L,$2E
6142: 2E 3F      LD           L,$3F
6144: FF         RST         0X38
6145: 52         LD           D,D
6146: 69         LD           L,C
6147: 63         LD           H,E
6148: 68         LD           L,B
6149: 61         LD           H,C
614A: 72         LD           (HL),D
614B: 64         LD           H,H
614C: 5E         LD           E,(HL)
614D: 73         LD           (HL),E
614E: 20 56      JR           NZ,$61A6
6150: 69         LD           L,C
6151: 6C         LD           L,H
6152: 6C         LD           L,H
6153: 61         LD           H,C
6154: 20 FF      JR           NZ,$6155
6156: 4B         LD           C,E
6157: 61         LD           H,C
6158: 6E         LD           L,(HL)
6159: 61         LD           H,C
615A: 6C         LD           L,H
615B: 65         LD           H,L
615C: 74         LD           (HL),H
615D: 20 43      JR           NZ,$61A2
615F: 61         LD           H,C
6160: 73         LD           (HL),E
6161: 74         LD           (HL),H
6162: 6C         LD           L,H
6163: 65         LD           H,L
6164: 20 20      JR           NZ,$6186
6166: 31 30 20   LD           SP,$2030
6169: 4D         LD           C,L
616A: 69         LD           L,C
616B: 6E         LD           L,(HL)
616C: 2E 20      LD           L,$20
616E: F3         DI
616F: 20 F0      JR           NZ,$6161
6171: FF         RST         0X38
6172: 4B         LD           C,E
6173: 61         LD           H,C
6174: 6E         LD           L,(HL)
6175: 61         LD           H,C
6176: 6C         LD           L,H
6177: 65         LD           H,L
6178: 74         LD           (HL),H
6179: 20 43      JR           NZ,$61BE
617B: 61         LD           H,C
617C: 73         LD           (HL),E
617D: 74         LD           (HL),H
617E: 6C         LD           L,H
617F: 65         LD           H,L
6180: 20 20      JR           NZ,$61A2
6182: 35         DEC         (HL)
6183: 20 4D      JR           NZ,$61D2
6185: 69         LD           L,C
6186: 6E         LD           L,(HL)
6187: 2E 20      LD           L,$20
6189: F3         DI
618A: FF         RST         0X38
618B: 4B         LD           C,E
618C: 61         LD           H,C
618D: 6E         LD           L,(HL)
618E: 61         LD           H,C
618F: 6C         LD           L,H
6190: 65         LD           H,L
6191: 74         LD           (HL),H
6192: 20 43      JR           NZ,$61D7
6194: 61         LD           H,C
6195: 73         LD           (HL),E
6196: 74         LD           (HL),H
6197: 6C         LD           L,H
6198: 65         LD           H,L
6199: 20 20      JR           NZ,$61BB
619B: 35         DEC         (HL)
619C: 30 20      JR           NC,$61BE
619E: 50         LD           D,B
619F: 61         LD           H,C
61A0: 63         LD           H,E
61A1: 65         LD           H,L
61A2: 73         LD           (HL),E
61A3: 20 F0      JR           NZ,$6195
61A5: FF         RST         0X38
61A6: 5E         LD           E,(HL)
61A7: 42         LD           B,D
61A8: 52         LD           D,D
61A9: 52         LD           D,D
61AA: 49         LD           C,C
61AB: 4E         LD           C,(HL)
61AC: 47         LD           B,A
61AD: 21 20 42   LD           HL,$4220
61B0: 52         LD           D,D
61B1: 52         LD           D,D
61B2: 49         LD           C,C
61B3: 4E         LD           C,(HL)
61B4: 47         LD           B,A
61B5: 21 20 42   LD           HL,$4220
61B8: 52         LD           D,D
61B9: 52         LD           D,D
61BA: 49         LD           C,C
61BB: 4E         LD           C,(HL)
61BC: 47         LD           B,A
61BD: 21 20 43   LD           HL,$4320
61C0: 4C         LD           C,H
61C1: 49         LD           C,C
61C2: 43         LD           B,E
61C3: 4B         LD           C,E
61C4: 21 20 59   LD           HL,$5920
61C7: 65         LD           H,L
61C8: 65         LD           H,L
61C9: 65         LD           H,L
61CA: 73         LD           (HL),E
61CB: 21 20 20   LD           HL,$2020
61CE: 49         LD           C,C
61CF: 74         LD           (HL),H
61D0: 5E         LD           E,(HL)
61D1: 73         LD           (HL),E
61D2: 20 74      JR           NZ,$6248
61D4: 68         LD           L,B
61D5: 65         LD           H,L
61D6: 42         LD           B,D
61D7: 75         LD           (HL),L
61D8: 63         LD           H,E
61D9: 6B         LD           L,E
61DA: 65         LD           H,L
61DB: 74         LD           (HL),H
61DC: 20 4D      JR           NZ,$622B
61DE: 6F         LD           L,A
61DF: 75         LD           (HL),L
61E0: 73         LD           (HL),E
61E1: 65         LD           H,L
61E2: 21 20 20   LD           HL,$2020
61E5: 20 54      JR           NZ,$623B
61E7: 68         LD           L,B
61E8: 61         LD           H,C
61E9: 6E         LD           L,(HL)
61EA: 6B         LD           L,E
61EB: 73         LD           (HL),E
61EC: 20 66      JR           NZ,$6254
61EE: 6F         LD           L,A
61EF: 72         LD           (HL),D
61F0: 20 63      JR           NZ,$6255
61F2: 61         LD           H,C
61F3: 6C         LD           L,H
61F4: 6C         LD           L,H
61F5: 2D         DEC         L
61F6: 69         LD           L,C
61F7: 6E         LD           L,(HL)
61F8: 67         LD           H,A
61F9: 21 20 2E   LD           HL,$2E20
61FC: 2E 2E      LD           L,$2E
61FE: 57         LD           D,A
61FF: 65         LD           H,L
6200: 6C         LD           L,H
6201: 6C         LD           L,H
6202: 2E 2E      LD           L,$2E
6204: 2E 20      LD           L,$20
6206: 43         LD           B,E
6207: 4C         LD           C,H
6208: 49         LD           C,C
6209: 43         LD           B,E
620A: 4B         LD           C,E
620B: 21 5E 20   LD           HL,$205E
620E: 20 3F      JR           NZ,$624F
6210: 3F         CCF
6211: 3F         CCF
6212: 20 2E      JR           NZ,$6242
6214: 2E 2E      LD           L,$2E
6216: 59         LD           E,C
6217: 6F         LD           L,A
6218: 75         LD           (HL),L
6219: 20 6D      JR           NZ,$6288
621B: 75         LD           (HL),L
621C: 73         LD           (HL),E
621D: 74         LD           (HL),H
621E: 20 68      JR           NZ,$6288
6220: 61         LD           H,C
6221: 76         HALT
6222: 65         LD           H,L
6223: 20 20      JR           NZ,$6245
6225: 20 64      JR           NZ,$628B
6227: 69         LD           L,C
6228: 61         LD           H,C
6229: 6C         LD           L,H
622A: 65         LD           H,L
622B: 64         LD           H,H
622C: 20 61      JR           NZ,$628F
622E: 20 77      JR           NZ,$62A7
6230: 72         LD           (HL),D
6231: 6F         LD           L,A
6232: 6E         LD           L,(HL)
6233: 67         LD           H,A
6234: 20 20      JR           NZ,$6256
6236: 6E         LD           L,(HL)
6237: 75         LD           (HL),L
6238: 6D         LD           L,L
6239: 62         LD           H,D
623A: 65         LD           H,L
623B: 72         LD           (HL),D
623C: 2E 2E      LD           L,$2E
623E: 2E FF      LD           L,$FF
6240: 4F         LD           C,A
6241: 68         LD           L,B
6242: 21 20 20   LD           HL,$2020
6245: 49         LD           C,C
6246: 74         LD           (HL),H
6247: 5E         LD           E,(HL)
6248: 73         LD           (HL),E
6249: 20 61      JR           NZ,$62AC
624B: 20 62      JR           NZ,$62AF
624D: 69         LD           L,C
624E: 67         LD           H,A
624F: 20 6F      JR           NZ,$62C0
6251: 6E         LD           L,(HL)
6252: 65         LD           H,L
6253: 21 20 20   LD           HL,$2020
6256: 41         LD           B,C
6257: 6E         LD           L,(HL)
6258: 64         LD           H,H
6259: 20 69      JR           NZ,$62C4
625B: 74         LD           (HL),H
625C: 20 68      JR           NZ,$62C6
625E: 61         LD           H,C
625F: 73         LD           (HL),E
6260: 61         LD           H,C
6261: 20 50      JR           NZ,$62B3
6263: 69         LD           L,C
6264: 65         LD           H,L
6265: 63         LD           H,E
6266: 65         LD           H,L
6267: 20 6F      JR           NZ,$62D8
6269: 66         LD           H,(HL)
626A: 20 20      JR           NZ,$628C
626C: 20 20      JR           NZ,$628E
626E: 20 20      JR           NZ,$6290
6270: 48         LD           C,B
6271: 65         LD           H,L
6272: 61         LD           H,C
6273: 72         LD           (HL),D
6274: 74         LD           (HL),H
6275: 2C         INC         L
6276: 20 74      JR           NZ,$62EC
6278: 6F         LD           L,A
6279: 6F         LD           L,A
627A: 21 20 20   LD           HL,$2020
627D: 59         LD           E,C
627E: 6F         LD           L,A
627F: 75         LD           (HL),L
6280: 67         LD           H,A
6281: 65         LD           H,L
6282: 74         LD           (HL),H
6283: 20 61      JR           NZ,$62E6
6285: 20 32      JR           NZ,$62B9
6287: 30 20      JR           NC,$62A9
6289: 52         LD           D,D
628A: 75         LD           (HL),L
628B: 70         LD           (HL),B
628C: 65         LD           H,L
628D: 65         LD           H,L
628E: 20 20      JR           NZ,$62B0
6290: 70         LD           (HL),B
6291: 72         LD           (HL),D
6292: 69         LD           L,C
6293: 7A         LD           A,D
6294: 65         LD           H,L
6295: 20 6F      JR           NZ,$6306
6297: 6E         LD           L,(HL)
6298: 20 74      JR           NZ,$630E
629A: 6F         LD           L,A
629B: 70         LD           (HL),B
629C: 20 6F      JR           NZ,$630D
629E: 66         LD           H,(HL)
629F: 20 74      JR           NZ,$6315
62A1: 68         LD           L,B
62A2: 61         LD           H,C
62A3: 74         LD           (HL),H
62A4: 21 20 54   LD           HL,$5420
62A7: 72         LD           (HL),D
62A8: 79         LD           A,C
62A9: 20 61      JR           NZ,$630C
62AB: 67         LD           H,A
62AC: 61         LD           H,C
62AD: 69         LD           L,C
62AE: 6E         LD           L,(HL)
62AF: 3F         CCF
62B0: 20 20      JR           NZ,$62D2
62B2: 20 20      JR           NZ,$62D4
62B4: 59         LD           E,C
62B5: 65         LD           H,L
62B6: 73         LD           (HL),E
62B7: 20 20      JR           NZ,$62D9
62B9: 4E         LD           C,(HL)
62BA: 6F         LD           L,A
62BB: FE 4F      CP           $4F
62BD: 68         LD           L,B
62BE: 21 20 20   LD           HL,$2020
62C1: 49         LD           C,C
62C2: 74         LD           (HL),H
62C3: 5E         LD           E,(HL)
62C4: 73         LD           (HL),E
62C5: 20 61      JR           NZ,$6328
62C7: 20 62      JR           NZ,$632B
62C9: 69         LD           L,C
62CA: 67         LD           H,A
62CB: 20 6F      JR           NZ,$633C
62CD: 6E         LD           L,(HL)
62CE: 65         LD           H,L
62CF: 21 20 20   LD           HL,$2020
62D2: 41         LD           B,C
62D3: 6E         LD           L,(HL)
62D4: 64         LD           H,H
62D5: 20 69      JR           NZ,$6340
62D7: 74         LD           (HL),H
62D8: 20 68      JR           NZ,$6342
62DA: 61         LD           H,C
62DB: 73         LD           (HL),E
62DC: 61         LD           H,C
62DD: 20 50      JR           NZ,$632F
62DF: 69         LD           L,C
62E0: 65         LD           H,L
62E1: 63         LD           H,E
62E2: 65         LD           H,L
62E3: 20 6F      JR           NZ,$6354
62E5: 66         LD           H,(HL)
62E6: 20 20      JR           NZ,$6308
62E8: 20 20      JR           NZ,$630A
62EA: 20 20      JR           NZ,$630C
62EC: 48         LD           C,B
62ED: 65         LD           H,L
62EE: 61         LD           H,C
62EF: 72         LD           (HL),D
62F0: 74         LD           (HL),H
62F1: 2C         INC         L
62F2: 20 74      JR           NZ,$6368
62F4: 6F         LD           L,A
62F5: 6F         LD           L,A
62F6: 21 20 20   LD           HL,$2020
62F9: 59         LD           E,C
62FA: 6F         LD           L,A
62FB: 75         LD           (HL),L
62FC: 68         LD           L,B
62FD: 61         LD           H,C
62FE: 76         HALT
62FF: 65         LD           H,L
6300: 20 63      JR           NZ,$6365
6302: 6F         LD           L,A
6303: 6D         LD           L,L
6304: 70         LD           (HL),B
6305: 6C         LD           L,H
6306: 65         LD           H,L
6307: 74         LD           (HL),H
6308: 65         LD           H,L
6309: 64         LD           H,H
630A: 20 20      JR           NZ,$632C
630C: 61         LD           H,C
630D: 6E         LD           L,(HL)
630E: 6F         LD           L,A
630F: 74         LD           (HL),H
6310: 68         LD           L,B
6311: 65         LD           H,L
6312: 72         LD           (HL),D
6313: 20 48      JR           NZ,$635D
6315: 65         LD           H,L
6316: 61         LD           H,C
6317: 72         LD           (HL),D
6318: 74         LD           (HL),H
6319: 20 20      JR           NZ,$633B
631B: 20 43      JR           NZ,$6360
631D: 6F         LD           L,A
631E: 6E         LD           L,(HL)
631F: 74         LD           (HL),H
6320: 61         LD           H,C
6321: 69         LD           L,C
6322: 6E         LD           L,(HL)
6323: 65         LD           H,L
6324: 72         LD           (HL),D
6325: 21 20 20   LD           HL,$2020
6328: 4F         LD           C,A
6329: 6E         LD           L,(HL)
632A: 20 20      JR           NZ,$634C
632C: 74         LD           (HL),H
632D: 6F         LD           L,A
632E: 70         LD           (HL),B
632F: 20 6F      JR           NZ,$63A0
6331: 66         LD           H,(HL)
6332: 20 74      JR           NZ,$63A8
6334: 68         LD           L,B
6335: 61         LD           H,C
6336: 74         LD           (HL),H
6337: 2C         INC         L
6338: 20 79      JR           NZ,$63B3
633A: 6F         LD           L,A
633B: 75         LD           (HL),L
633C: 67         LD           H,A
633D: 65         LD           H,L
633E: 74         LD           (HL),H
633F: 20 61      JR           NZ,$63A2
6341: 20 32      JR           NZ,$6375
6343: 30 20      JR           NC,$6365
6345: 52         LD           D,D
6346: 75         LD           (HL),L
6347: 70         LD           (HL),B
6348: 65         LD           H,L
6349: 65         LD           H,L
634A: 20 20      JR           NZ,$636C
634C: 70         LD           (HL),B
634D: 72         LD           (HL),D
634E: 69         LD           L,C
634F: 7A         LD           A,D
6350: 65         LD           H,L
6351: 21 20 57   LD           HL,$5720
6354: 61         LD           H,C
6355: 6E         LD           L,(HL)
6356: 74         LD           (HL),H
6357: 20 74      JR           NZ,$63CD
6359: 6F         LD           L,A
635A: 20 20      JR           NZ,$637C
635C: 74         LD           (HL),H
635D: 72         LD           (HL),D
635E: 79         LD           A,C
635F: 20 61      JR           NZ,$63C2
6361: 67         LD           H,A
6362: 61         LD           H,C
6363: 69         LD           L,C
6364: 6E         LD           L,(HL)
6365: 3F         CCF
6366: 20 20      JR           NZ,$6388
6368: 20 20      JR           NZ,$638A
636A: 20 20      JR           NZ,$638C
636C: 20 20      JR           NZ,$638E
636E: 20 20      JR           NZ,$6390
6370: 59         LD           E,C
6371: 65         LD           H,L
6372: 73         LD           (HL),E
6373: 20 20      JR           NZ,$6395
6375: 4E         LD           C,(HL)
6376: 6F         LD           L,A
6377: FE 20      CP           $20
6379: 5E         LD           E,(HL)
637A: 48         LD           C,B
637B: 6F         LD           L,A
637C: 77         LD           (HL),A
637D: 20 54      JR           NZ,$63D3
637F: 6F         LD           L,A
6380: 20 48      JR           NZ,$63CA
6382: 61         LD           H,C
6383: 6E         LD           L,(HL)
6384: 64         LD           H,H
6385: 6C         LD           L,H
6386: 65         LD           H,L
6387: 20 20      JR           NZ,$63A9
6389: 20 20      JR           NZ,$63AB
638B: 59         LD           E,C
638C: 6F         LD           L,A
638D: 75         LD           (HL),L
638E: 72         LD           (HL),D
638F: 20 53      JR           NZ,$63E4
6391: 68         LD           L,B
6392: 69         LD           L,C
6393: 65         LD           H,L
6394: 6C         LD           L,H
6395: 64         LD           H,H
6396: 20 20      JR           NZ,$63B8
6398: 20 20      JR           NZ,$63BA
639A: 20 4C      JR           NZ,$63E8
639C: 69         LD           L,C
639D: 6B         LD           L,E
639E: 65         LD           H,L
639F: 20 41      JR           NZ,$63E2
63A1: 20 50      JR           NZ,$63F3
63A3: 72         LD           (HL),D
63A4: 6F         LD           L,A
63A5: 21 5E 20   LD           HL,$205E
63A8: 52         LD           D,D
63A9: 65         LD           H,L
63AA: 61         LD           H,C
63AB: 64         LD           H,H
63AC: 20 74      JR           NZ,$6422
63AE: 68         LD           L,B
63AF: 69         LD           L,C
63B0: 73         LD           (HL),E
63B1: 20 62      JR           NZ,$6415
63B3: 6F         LD           L,A
63B4: 6F         LD           L,A
63B5: 6B         LD           L,E
63B6: 3F         CCF
63B7: 20 20      JR           NZ,$63D9
63B9: 20 20      JR           NZ,$63DB
63BB: 20 52      JR           NZ,$640F
63BD: 65         LD           H,L
63BE: 61         LD           H,C
63BF: 64         LD           H,H
63C0: 20 44      JR           NZ,$6406
63C2: 6F         LD           L,A
63C3: 6E         LD           L,(HL)
63C4: 5E         LD           E,(HL)
63C5: 74         LD           (HL),H
63C6: FE 5E      CP           $5E
63C8: 49         LD           C,C
63C9: 66         LD           H,(HL)
63CA: 20 79      JR           NZ,$6445
63CC: 6F         LD           L,A
63CD: 75         LD           (HL),L
63CE: 20 68      JR           NZ,$6438
63D0: 6F         LD           L,A
63D1: 6C         LD           L,H
63D2: 64         LD           H,H
63D3: 20 74      JR           NZ,$6449
63D5: 68         LD           L,B
63D6: 65         LD           H,L
63D7: 42         LD           B,D
63D8: 75         LD           (HL),L
63D9: 74         LD           (HL),H
63DA: 74         LD           (HL),H
63DB: 6F         LD           L,A
63DC: 6E         LD           L,(HL)
63DD: 20 64      JR           NZ,$6443
63DF: 6F         LD           L,A
63E0: 77         LD           (HL),A
63E1: 6E         LD           L,(HL)
63E2: 2C         INC         L
63E3: 20 79      JR           NZ,$645E
63E5: 6F         LD           L,A
63E6: 75         LD           (HL),L
63E7: 63         LD           H,E
63E8: 61         LD           H,C
63E9: 6E         LD           L,(HL)
63EA: 20 64      JR           NZ,$6450
63EC: 65         LD           H,L
63ED: 66         LD           H,(HL)
63EE: 65         LD           H,L
63EF: 6E         LD           L,(HL)
63F0: 64         LD           H,H
63F1: 20 79      JR           NZ,$646C
63F3: 6F         LD           L,A
63F4: 75         LD           (HL),L
63F5: 72         LD           (HL),D
63F6: 2D         DEC         L
63F7: 73         LD           (HL),E
63F8: 65         LD           H,L
63F9: 6C         LD           L,H
63FA: 66         LD           H,(HL)
63FB: 20 66      JR           NZ,$6463
63FD: 72         LD           (HL),D
63FE: 6F         LD           L,A
63FF: 6D         LD           L,L
6400: 20 65      JR           NZ,$6467
6402: 6E         LD           L,(HL)
6403: 65         LD           H,L
6404: 6D         LD           L,L
6405: 79         LD           A,C
6406: 20 61      JR           NZ,$6469
6408: 74         LD           (HL),H
6409: 74         LD           (HL),H
640A: 61         LD           H,C
640B: 63         LD           H,E
640C: 6B         LD           L,E
640D: 73         LD           (HL),E
640E: 2C         INC         L
640F: 20 61      JR           NZ,$6472
6411: 6E         LD           L,(HL)
6412: 64         LD           H,H
6413: 20 79      JR           NZ,$648E
6415: 6F         LD           L,A
6416: 75         LD           (HL),L
6417: 63         LD           H,E
6418: 61         LD           H,C
6419: 6E         LD           L,(HL)
641A: 20 66      JR           NZ,$6482
641C: 69         LD           L,C
641D: 6C         LD           L,H
641E: 6C         LD           L,H
641F: 69         LD           L,C
6420: 70         LD           (HL),B
6421: 20 73      JR           NZ,$6496
6423: 6F         LD           L,A
6424: 6D         LD           L,L
6425: 65         LD           H,L
6426: 20 65      JR           NZ,$648D
6428: 6E         LD           L,(HL)
6429: 65         LD           H,L
642A: 6D         LD           L,L
642B: 69         LD           L,C
642C: 65         LD           H,L
642D: 73         LD           (HL),E
642E: 2C         INC         L
642F: 20 74      JR           NZ,$64A5
6431: 6F         LD           L,A
6432: 6F         LD           L,A
6433: 2E 2E      LD           L,$2E
6435: 2E 20      LD           L,$20
6437: 42         LD           B,D
6438: 65         LD           H,L
6439: 73         LD           (HL),E
643A: 69         LD           L,C
643B: 64         LD           H,H
643C: 65         LD           H,L
643D: 73         LD           (HL),E
643E: 20 74      JR           NZ,$64B4
6440: 68         LD           L,B
6441: 65         LD           H,L
6442: 20 20      JR           NZ,$6464
6444: 20 20      JR           NZ,$6466
6446: 20 73      JR           NZ,$64BB
6448: 74         LD           (HL),H
6449: 61         LD           H,C
644A: 6E         LD           L,(HL)
644B: 64         LD           H,H
644C: 61         LD           H,C
644D: 72         LD           (HL),D
644E: 64         LD           H,H
644F: 20 73      JR           NZ,$64C4
6451: 68         LD           L,B
6452: 69         LD           L,C
6453: 65         LD           H,L
6454: 6C         LD           L,H
6455: 64         LD           H,H
6456: 20 74      JR           NZ,$64CC
6458: 68         LD           L,B
6459: 65         LD           H,L
645A: 72         LD           (HL),D
645B: 65         LD           H,L
645C: 20 69      JR           NZ,$64C7
645E: 73         LD           (HL),E
645F: 20 61      JR           NZ,$64C2
6461: 6C         LD           L,H
6462: 73         LD           (HL),E
6463: 6F         LD           L,A
6464: 20 61      JR           NZ,$64C7
6466: 20 6D      JR           NZ,$64D5
6468: 69         LD           L,C
6469: 72         LD           (HL),D
646A: 72         LD           (HL),D
646B: 6F         LD           L,A
646C: 72         LD           (HL),D
646D: 65         LD           H,L
646E: 64         LD           H,H
646F: 20 76      JR           NZ,$64E7
6471: 61         LD           H,C
6472: 72         LD           (HL),D
6473: 69         LD           L,C
6474: 65         LD           H,L
6475: 74         LD           (HL),H
6476: 79         LD           A,C
6477: 77         LD           (HL),A
6478: 68         LD           L,B
6479: 69         LD           L,C
647A: 63         LD           H,E
647B: 68         LD           L,B
647C: 20 63      JR           NZ,$64E1
647E: 61         LD           H,C
647F: 6E         LD           L,(HL)
6480: 20 64      JR           NZ,$64E6
6482: 65         LD           H,L
6483: 66         LD           H,(HL)
6484: 65         LD           H,L
6485: 6E         LD           L,(HL)
6486: 64         LD           H,H
6487: 61         LD           H,C
6488: 67         LD           H,A
6489: 61         LD           H,C
648A: 69         LD           L,C
648B: 6E         LD           L,(HL)
648C: 73         LD           (HL),E
648D: 74         LD           (HL),H
648E: 20 62      JR           NZ,$64F2
6490: 65         LD           H,L
6491: 61         LD           H,C
6492: 6D         LD           L,L
6493: 73         LD           (HL),E
6494: 21 5E FF   LD           HL,$FF5E
6497: 20 5E      JR           NZ,$64F7
6499: 53         LD           D,E
649A: 65         LD           H,L
649B: 6C         LD           L,H
649C: 65         LD           H,L
649D: 63         LD           H,E
649E: 74         LD           (HL),H
649F: 69         LD           L,C
64A0: 6E         LD           L,(HL)
64A1: 67         LD           H,A
64A2: 20 54      JR           NZ,$64F8
64A4: 68         LD           L,B
64A5: 65         LD           H,L
64A6: 20 20      JR           NZ,$64C8
64A8: 20 20      JR           NZ,$64CA
64AA: 49         LD           C,C
64AB: 74         LD           (HL),H
64AC: 65         LD           H,L
64AD: 6D         LD           L,L
64AE: 20 54      JR           NZ,$6504
64B0: 68         LD           L,B
64B1: 61         LD           H,C
64B2: 74         LD           (HL),H
64B3: 5E         LD           E,(HL)
64B4: 73         LD           (HL),E
64B5: 20 20      JR           NZ,$64D7
64B7: 20 20      JR           NZ,$64D9
64B9: 52         LD           D,D
64BA: 69         LD           L,C
64BB: 67         LD           H,A
64BC: 68         LD           L,B
64BD: 74         LD           (HL),H
64BE: 20 46      JR           NZ,$6506
64C0: 6F         LD           L,A
64C1: 72         LD           (HL),D
64C2: 20 59      JR           NZ,$651D
64C4: 6F         LD           L,A
64C5: 75         LD           (HL),L
64C6: 5E         LD           E,(HL)
64C7: 52         LD           D,D
64C8: 65         LD           H,L
64C9: 61         LD           H,C
64CA: 64         LD           H,H
64CB: 20 74      JR           NZ,$6541
64CD: 68         LD           L,B
64CE: 69         LD           L,C
64CF: 73         LD           (HL),E
64D0: 20 62      JR           NZ,$6534
64D2: 6F         LD           L,A
64D3: 6F         LD           L,A
64D4: 6B         LD           L,E
64D5: 3F         CCF
64D6: 20 20      JR           NZ,$64F8
64D8: 20 20      JR           NZ,$64FA
64DA: 20 52      JR           NZ,$652E
64DC: 65         LD           H,L
64DD: 61         LD           H,C
64DE: 64         LD           H,H
64DF: 20 44      JR           NZ,$6525
64E1: 6F         LD           L,A
64E2: 6E         LD           L,(HL)
64E3: 5E         LD           E,(HL)
64E4: 74         LD           (HL),H
64E5: FE 5E      CP           $5E
64E7: 59         LD           E,C
64E8: 6F         LD           L,A
64E9: 75         LD           (HL),L
64EA: 20 63      JR           NZ,$654F
64EC: 61         LD           H,C
64ED: 6E         LD           L,(HL)
64EE: 20 73      JR           NZ,$6563
64F0: 65         LD           H,L
64F1: 6C         LD           L,H
64F2: 65         LD           H,L
64F3: 63         LD           H,E
64F4: 74         LD           (HL),H
64F5: 20 79      JR           NZ,$6570
64F7: 6F         LD           L,A
64F8: 75         LD           (HL),L
64F9: 72         LD           (HL),D
64FA: 20 66      JR           NZ,$6562
64FC: 61         LD           H,C
64FD: 76         HALT
64FE: 6F         LD           L,A
64FF: 72         LD           (HL),D
6500: 69         LD           L,C
6501: 74         LD           (HL),H
6502: 65         LD           H,L
6503: 20 20      JR           NZ,$6525
6505: 20 69      JR           NZ,$6570
6507: 74         LD           (HL),H
6508: 65         LD           H,L
6509: 6D         LD           L,L
650A: 20 66      JR           NZ,$6572
650C: 6F         LD           L,A
650D: 72         LD           (HL),D
650E: 20 74      JR           NZ,$6584
6510: 68         LD           L,B
6511: 65         LD           H,L
6512: 20 41      JR           NZ,$6555
6514: 20 20      JR           NZ,$6536
6516: 61         LD           H,C
6517: 6E         LD           L,(HL)
6518: 64         LD           H,H
6519: 20 42      JR           NZ,$655D
651B: 20 42      JR           NZ,$655F
651D: 75         LD           (HL),L
651E: 74         LD           (HL),H
651F: 74         LD           (HL),H
6520: 6F         LD           L,A
6521: 6E         LD           L,(HL)
6522: 73         LD           (HL),E
6523: 20 6F      JR           NZ,$6594
6525: 6E         LD           L,(HL)
6526: 74         LD           (HL),H
6527: 68         LD           L,B
6528: 65         LD           H,L
6529: 20 53      JR           NZ,$657E
652B: 75         LD           (HL),L
652C: 62         LD           H,D
652D: 2D         DEC         L
652E: 53         LD           D,E
652F: 63         LD           H,E
6530: 72         LD           (HL),D
6531: 65         LD           H,L
6532: 65         LD           H,L
6533: 6E         LD           L,(HL)
6534: 2E 20      LD           L,$20
6536: 55         LD           D,L
6537: 73         LD           (HL),E
6538: 69         LD           L,C
6539: 6E         LD           L,(HL)
653A: 67         LD           H,A
653B: 20 64      JR           NZ,$65A1
653D: 69         LD           L,C
653E: 66         LD           H,(HL)
653F: 66         LD           H,(HL)
6540: 65         LD           H,L
6541: 72         LD           (HL),D
6542: 65         LD           H,L
6543: 6E         LD           L,(HL)
6544: 74         LD           (HL),H
6545: 20 69      JR           NZ,$65B0
6547: 74         LD           (HL),H
6548: 65         LD           H,L
6549: 6D         LD           L,L
654A: 73         LD           (HL),E
654B: 2C         INC         L
654C: 20 79      JR           NZ,$65C7
654E: 6F         LD           L,A
654F: 75         LD           (HL),L
6550: 20 63      JR           NZ,$65B5
6552: 61         LD           H,C
6553: 6E         LD           L,(HL)
6554: 20 20      JR           NZ,$6576
6556: 66         LD           H,(HL)
6557: 69         LD           L,C
6558: 67         LD           H,A
6559: 68         LD           L,B
655A: 74         LD           (HL),H
655B: 20 77      JR           NZ,$65D4
655D: 69         LD           L,C
655E: 74         LD           (HL),H
655F: 68         LD           L,B
6560: 6F         LD           L,A
6561: 75         LD           (HL),L
6562: 74         LD           (HL),H
6563: 20 61      JR           NZ,$65C6
6565: 20 73      JR           NZ,$65DA
6567: 77         LD           (HL),A
6568: 6F         LD           L,A
6569: 72         LD           (HL),D
656A: 64         LD           H,H
656B: 21 20 20   LD           HL,$2020
656E: 54         LD           D,H
656F: 72         LD           (HL),D
6570: 79         LD           A,C
6571: 20 6D      JR           NZ,$65E0
6573: 61         LD           H,C
6574: 6E         LD           L,(HL)
6575: 79         LD           A,C
6576: 64         LD           H,H
6577: 69         LD           L,C
6578: 66         LD           H,(HL)
6579: 66         LD           H,(HL)
657A: 65         LD           H,L
657B: 72         LD           (HL),D
657C: 65         LD           H,L
657D: 6E         LD           L,(HL)
657E: 74         LD           (HL),H
657F: 20 74      JR           NZ,$65F5
6581: 68         LD           L,B
6582: 69         LD           L,C
6583: 6E         LD           L,(HL)
6584: 67         LD           H,A
6585: 73         LD           (HL),E
6586: 74         LD           (HL),H
6587: 6F         LD           L,A
6588: 20 66      JR           NZ,$65F0
658A: 69         LD           L,C
658B: 6E         LD           L,(HL)
658C: 64         LD           H,H
658D: 20 77      JR           NZ,$6606
658F: 68         LD           L,B
6590: 61         LD           H,C
6591: 74         LD           (HL),H
6592: 5E         LD           E,(HL)
6593: 73         LD           (HL),E
6594: 20 20      JR           NZ,$65B6
6596: 72         LD           (HL),D
6597: 69         LD           L,C
6598: 67         LD           H,A
6599: 68         LD           L,B
659A: 74         LD           (HL),H
659B: 20 66      JR           NZ,$6603
659D: 6F         LD           L,A
659E: 72         LD           (HL),D
659F: 20 79      JR           NZ,$661A
65A1: 6F         LD           L,A
65A2: 75         LD           (HL),L
65A3: 21 5E FF   LD           HL,$FF5E
65A6: 20 5E      JR           NZ,$6606
65A8: 41         LD           B,C
65A9: 75         LD           (HL),L
65AA: 74         LD           (HL),H
65AB: 6F         LD           L,A
65AC: 20 4D      JR           NZ,$65FB
65AE: 61         LD           H,C
65AF: 70         LD           (HL),B
65B0: 20 61      JR           NZ,$6613
65B2: 6E         LD           L,(HL)
65B3: 64         LD           H,H
65B4: 20 20      JR           NZ,$65D6
65B6: 4D         LD           C,L
65B7: 65         LD           H,L
65B8: 6D         LD           L,L
65B9: 6F         LD           L,A
65BA: 20 47      JR           NZ,$6603
65BC: 75         LD           (HL),L
65BD: 69         LD           L,C
65BE: 64         LD           H,H
65BF: 65         LD           H,L
65C0: 20 42      JR           NZ,$6604
65C2: 6F         LD           L,A
65C3: 6F         LD           L,A
65C4: 6B         LD           L,E
65C5: 5E         LD           E,(HL)
65C6: 52         LD           D,D
65C7: 65         LD           H,L
65C8: 61         LD           H,C
65C9: 64         LD           H,H
65CA: 20 74      JR           NZ,$6640
65CC: 68         LD           L,B
65CD: 69         LD           L,C
65CE: 73         LD           (HL),E
65CF: 20 62      JR           NZ,$6633
65D1: 6F         LD           L,A
65D2: 6F         LD           L,A
65D3: 6B         LD           L,E
65D4: 3F         CCF
65D5: 20 20      JR           NZ,$65F7
65D7: 20 20      JR           NZ,$65F9
65D9: 20 52      JR           NZ,$662D
65DB: 65         LD           H,L
65DC: 61         LD           H,C
65DD: 64         LD           H,H
65DE: 20 44      JR           NZ,$6624
65E0: 6F         LD           L,A
65E1: 6E         LD           L,(HL)
65E2: 5E         LD           E,(HL)
65E3: 74         LD           (HL),H
65E4: FE 5E      CP           $5E
65E6: 59         LD           E,C
65E7: 6F         LD           L,A
65E8: 75         LD           (HL),L
65E9: 20 63      JR           NZ,$664E
65EB: 61         LD           H,C
65EC: 6E         LD           L,(HL)
65ED: 20 73      JR           NZ,$6662
65EF: 65         LD           H,L
65F0: 65         LD           H,L
65F1: 20 61      JR           NZ,$6654
65F3: 6E         LD           L,(HL)
65F4: 20 69      JR           NZ,$665F
65F6: 73         LD           (HL),E
65F7: 6C         LD           L,H
65F8: 61         LD           H,C
65F9: 6E         LD           L,(HL)
65FA: 64         LD           H,H
65FB: 20 6D      JR           NZ,$666A
65FD: 61         LD           H,C
65FE: 70         LD           (HL),B
65FF: 20 62      JR           NZ,$6663
6601: 79         LD           A,C
6602: 20 20      JR           NZ,$6624
6604: 20 70      JR           NZ,$6676
6606: 72         LD           (HL),D
6607: 65         LD           H,L
6608: 73         LD           (HL),E
6609: 73         LD           (HL),E
660A: 69         LD           L,C
660B: 6E         LD           L,(HL)
660C: 67         LD           H,A
660D: 20 74      JR           NZ,$6683
660F: 68         LD           L,B
6610: 65         LD           H,L
6611: 20 20      JR           NZ,$6633
6613: 20 20      JR           NZ,$6635
6615: 53         LD           D,E
6616: 45         LD           B,L
6617: 4C         LD           C,H
6618: 45         LD           B,L
6619: 43         LD           B,E
661A: 54         LD           D,H
661B: 20 42      JR           NZ,$665F
661D: 75         LD           (HL),L
661E: 74         LD           (HL),H
661F: 74         LD           (HL),H
6620: 6F         LD           L,A
6621: 6E         LD           L,(HL)
6622: 2E 20      LD           L,$20
6624: 20 54      JR           NZ,$667A
6626: 68         LD           L,B
6627: 65         LD           H,L
6628: 20 64      JR           NZ,$668E
662A: 61         LD           H,C
662B: 72         LD           (HL),D
662C: 6B         LD           L,E
662D: 20 70      JR           NZ,$669F
662F: 61         LD           H,C
6630: 72         LD           (HL),D
6631: 74         LD           (HL),H
6632: 73         LD           (HL),E
6633: 20 20      JR           NZ,$6655
6635: 6F         LD           L,A
6636: 66         LD           H,(HL)
6637: 20 74      JR           NZ,$66AD
6639: 68         LD           L,B
663A: 65         LD           H,L
663B: 20 6D      JR           NZ,$66AA
663D: 61         LD           H,C
663E: 70         LD           (HL),B
663F: 20 61      JR           NZ,$66A2
6641: 72         LD           (HL),D
6642: 65         LD           H,L
6643: 20 20      JR           NZ,$6665
6645: 70         LD           (HL),B
6646: 6C         LD           L,H
6647: 61         LD           H,C
6648: 63         LD           H,E
6649: 65         LD           H,L
664A: 73         LD           (HL),E
664B: 20 79      JR           NZ,$66C6
664D: 6F         LD           L,A
664E: 75         LD           (HL),L
664F: 20 68      JR           NZ,$66B9
6651: 61         LD           H,C
6652: 76         HALT
6653: 65         LD           H,L
6654: 20 6E      JR           NZ,$66C4
6656: 6F         LD           L,A
6657: 74         LD           (HL),H
6658: 20 79      JR           NZ,$66D3
665A: 65         LD           H,L
665B: 74         LD           (HL),H
665C: 20 76      JR           NZ,$66D4
665E: 69         LD           L,C
665F: 73         LD           (HL),E
6660: 69         LD           L,C
6661: 74         LD           (HL),H
6662: 65         LD           H,L
6663: 64         LD           H,H
6664: 2E 4D      LD           L,$4D
6666: 6F         LD           L,A
6667: 76         HALT
6668: 65         LD           H,L
6669: 20 74      JR           NZ,$66DF
666B: 68         LD           L,B
666C: 65         LD           H,L
666D: 20 63      JR           NZ,$66D2
666F: 75         LD           (HL),L
6670: 72         LD           (HL),D
6671: 73         LD           (HL),E
6672: 6F         LD           L,A
6673: 72         LD           (HL),D
6674: 20 61      JR           NZ,$66D7
6676: 6E         LD           L,(HL)
6677: 64         LD           H,H
6678: 20 70      JR           NZ,$66EA
667A: 72         LD           (HL),D
667B: 65         LD           H,L
667C: 73         LD           (HL),E
667D: 73         LD           (HL),E
667E: 20 74      JR           NZ,$66F4
6680: 68         LD           L,B
6681: 65         LD           H,L
6682: 20 41      JR           NZ,$66C5
6684: 20 42      JR           NZ,$66C8
6686: 75         LD           (HL),L
6687: 74         LD           (HL),H
6688: 74         LD           (HL),H
6689: 6F         LD           L,A
668A: 6E         LD           L,(HL)
668B: 20 74      JR           NZ,$6701
668D: 6F         LD           L,A
668E: 20 67      JR           NZ,$66F7
6690: 65         LD           H,L
6691: 74         LD           (HL),H
6692: 20 20      JR           NZ,$66B4
6694: 20 6D      JR           NZ,$6703
6696: 6F         LD           L,A
6697: 72         LD           (HL),D
6698: 65         LD           H,L
6699: 20 69      JR           NZ,$6704
669B: 6E         LD           L,(HL)
669C: 66         LD           H,(HL)
669D: 6F         LD           L,A
669E: 72         LD           (HL),D
669F: 6D         LD           L,L
66A0: 61         LD           H,C
66A1: 74         LD           (HL),H
66A2: 69         LD           L,C
66A3: 6F         LD           L,A
66A4: 6E         LD           L,(HL)
66A5: 61         LD           H,C
66A6: 62         LD           H,D
66A7: 6F         LD           L,A
66A8: 75         LD           (HL),L
66A9: 74         LD           (HL),H
66AA: 20 61      JR           NZ,$670D
66AC: 6E         LD           L,(HL)
66AD: 20 61      JR           NZ,$6710
66AF: 72         LD           (HL),D
66B0: 65         LD           H,L
66B1: 61         LD           H,C
66B2: 2C         INC         L
66B3: 20 20      JR           NZ,$66D5
66B5: 6F         LD           L,A
66B6: 72         LD           (HL),D
66B7: 20 74      JR           NZ,$672D
66B9: 6F         LD           L,A
66BA: 20 72      JR           NZ,$672E
66BC: 65         LD           H,L
66BD: 70         LD           (HL),B
66BE: 6C         LD           L,H
66BF: 61         LD           H,C
66C0: 79         LD           A,C
66C1: 20 74      JR           NZ,$6737
66C3: 68         LD           L,B
66C4: 65         LD           H,L
66C5: 6D         LD           L,L
66C6: 65         LD           H,L
66C7: 73         LD           (HL),E
66C8: 73         LD           (HL),E
66C9: 61         LD           H,C
66CA: 67         LD           H,A
66CB: 65         LD           H,L
66CC: 20 79      JR           NZ,$6747
66CE: 6F         LD           L,A
66CF: 75         LD           (HL),L
66D0: 20 67      JR           NZ,$6739
66D2: 6F         LD           L,A
66D3: 74         LD           (HL),H
66D4: 20 74      JR           NZ,$674A
66D6: 68         LD           L,B
66D7: 65         LD           H,L
66D8: 72         LD           (HL),D
66D9: 65         LD           H,L
66DA: 2E 2E      LD           L,$2E
66DC: 2E 5E      LD           L,$5E
66DE: 20 20      JR           NZ,$6700
66E0: 41         LD           B,C
66E1: 68         LD           L,B
66E2: 68         LD           L,B
66E3: 68         LD           L,B
66E4: 21 48 6F   LD           HL,$6F48
66E7: 77         LD           (HL),A
66E8: 20 63      JR           NZ,$674D
66EA: 6F         LD           L,A
66EB: 6E         LD           L,(HL)
66EC: 76         HALT
66ED: 65         LD           H,L
66EE: 6E         LD           L,(HL)
66EF: 69         LD           L,C
66F0: 65         LD           H,L
66F1: 6E         LD           L,(HL)
66F2: 74         LD           (HL),H
66F3: 21 FF 20   LD           HL,$20FF
66F6: 5E         LD           E,(HL)
66F7: 53         LD           D,E
66F8: 65         LD           H,L
66F9: 63         LD           H,E
66FA: 72         LD           (HL),D
66FB: 65         LD           H,L
66FC: 74         LD           (HL),H
66FD: 73         LD           (HL),E
66FE: 20 4F      JR           NZ,$674F
6700: 66         LD           H,(HL)
6701: 20 54      JR           NZ,$6757
6703: 68         LD           L,B
6704: 65         LD           H,L
6705: 20 57      JR           NZ,$675E
6707: 68         LD           L,B
6708: 69         LD           L,C
6709: 72         LD           (HL),D
670A: 6C         LD           L,H
670B: 69         LD           L,C
670C: 6E         LD           L,(HL)
670D: 67         LD           H,A
670E: 20 42      JR           NZ,$6752
6710: 6C         LD           L,H
6711: 61         LD           H,C
6712: 64         LD           H,H
6713: 65         LD           H,L
6714: 5E         LD           E,(HL)
6715: 52         LD           D,D
6716: 65         LD           H,L
6717: 61         LD           H,C
6718: 64         LD           H,H
6719: 20 74      JR           NZ,$678F
671B: 68         LD           L,B
671C: 69         LD           L,C
671D: 73         LD           (HL),E
671E: 20 62      JR           NZ,$6782
6720: 6F         LD           L,A
6721: 6F         LD           L,A
6722: 6B         LD           L,E
6723: 3F         CCF
6724: 20 20      JR           NZ,$6746
6726: 20 20      JR           NZ,$6748
6728: 20 52      JR           NZ,$677C
672A: 65         LD           H,L
672B: 61         LD           H,C
672C: 64         LD           H,H
672D: 20 44      JR           NZ,$6773
672F: 6F         LD           L,A
6730: 6E         LD           L,(HL)
6731: 5E         LD           E,(HL)
6732: 74         LD           (HL),H
6733: FE 5E      CP           $5E
6735: 54         LD           D,H
6736: 68         LD           L,B
6737: 65         LD           H,L
6738: 20 57      JR           NZ,$6791
673A: 68         LD           L,B
673B: 69         LD           L,C
673C: 72         LD           (HL),D
673D: 6C         LD           L,H
673E: 69         LD           L,C
673F: 6E         LD           L,(HL)
6740: 67         LD           H,A
6741: 20 20      JR           NZ,$6763
6743: 20 42      JR           NZ,$6787
6745: 6C         LD           L,H
6746: 61         LD           H,C
6747: 64         LD           H,H
6748: 65         LD           H,L
6749: 20 74      JR           NZ,$67BF
674B: 65         LD           H,L
674C: 63         LD           H,E
674D: 68         LD           L,B
674E: 6E         LD           L,(HL)
674F: 69         LD           L,C
6750: 71         LD           (HL),C
6751: 75         LD           (HL),L
6752: 65         LD           H,L
6753: 20 68      JR           NZ,$67BD
6755: 61         LD           H,C
6756: 73         LD           (HL),E
6757: 20 62      JR           NZ,$67BB
6759: 65         LD           H,L
675A: 65         LD           H,L
675B: 6E         LD           L,(HL)
675C: 20 68      JR           NZ,$67C6
675E: 61         LD           H,C
675F: 6E         LD           L,(HL)
6760: 64         LD           H,H
6761: 65         LD           H,L
6762: 64         LD           H,H
6763: 20 64      JR           NZ,$67C9
6765: 6F         LD           L,A
6766: 77         LD           (HL),A
6767: 6E         LD           L,(HL)
6768: 20 66      JR           NZ,$67D0
676A: 72         LD           (HL),D
676B: 6F         LD           L,A
676C: 6D         LD           L,L
676D: 20 67      JR           NZ,$67D6
676F: 65         LD           H,L
6770: 6E         LD           L,(HL)
6771: 65         LD           H,L
6772: 72         LD           (HL),D
6773: 2D         DEC         L
6774: 61         LD           H,C
6775: 74         LD           (HL),H
6776: 69         LD           L,C
6777: 6F         LD           L,A
6778: 6E         LD           L,(HL)
6779: 20 74      JR           NZ,$67EF
677B: 6F         LD           L,A
677C: 20 67      JR           NZ,$67E5
677E: 65         LD           H,L
677F: 6E         LD           L,(HL)
6780: 65         LD           H,L
6781: 72         LD           (HL),D
6782: 2D         DEC         L
6783: 20 61      JR           NZ,$67E6
6785: 74         LD           (HL),H
6786: 69         LD           L,C
6787: 6F         LD           L,A
6788: 6E         LD           L,(HL)
6789: 20 62      JR           NZ,$67ED
678B: 79         LD           A,C
678C: 20 74      JR           NZ,$6802
678E: 68         LD           L,B
678F: 65         LD           H,L
6790: 20 20      JR           NZ,$67B2
6792: 20 20      JR           NZ,$67B4
6794: 66         LD           H,(HL)
6795: 61         LD           H,C
6796: 6D         LD           L,L
6797: 69         LD           L,C
6798: 6C         LD           L,H
6799: 79         LD           A,C
679A: 20 6F      JR           NZ,$680B
679C: 66         LD           H,(HL)
679D: 20 74      JR           NZ,$6813
679F: 68         LD           L,B
67A0: 65         LD           H,L
67A1: 20 20      JR           NZ,$67C3
67A3: 20 68      JR           NZ,$680D
67A5: 65         LD           H,L
67A6: 72         LD           (HL),D
67A7: 6F         LD           L,A
67A8: 2E 20      LD           L,$20
67AA: 54         LD           D,H
67AB: 6F         LD           L,A
67AC: 20 75      JR           NZ,$6823
67AE: 73         LD           (HL),E
67AF: 65         LD           H,L
67B0: 20 69      JR           NZ,$681B
67B2: 74         LD           (HL),H
67B3: 2C         INC         L
67B4: 68         LD           L,B
67B5: 6F         LD           L,A
67B6: 6C         LD           L,H
67B7: 64         LD           H,H
67B8: 20 64      JR           NZ,$681E
67BA: 6F         LD           L,A
67BB: 77         LD           (HL),A
67BC: 6E         LD           L,(HL)
67BD: 20 74      JR           NZ,$6833
67BF: 68         LD           L,B
67C0: 65         LD           H,L
67C1: 20 20      JR           NZ,$67E3
67C3: 20 53      JR           NZ,$6818
67C5: 77         LD           (HL),A
67C6: 6F         LD           L,A
67C7: 72         LD           (HL),D
67C8: 64         LD           H,H
67C9: 20 42      JR           NZ,$680D
67CB: 75         LD           (HL),L
67CC: 74         LD           (HL),H
67CD: 74         LD           (HL),H
67CE: 6F         LD           L,A
67CF: 6E         LD           L,(HL)
67D0: 20 61      JR           NZ,$6833
67D2: 6E         LD           L,(HL)
67D3: 64         LD           H,H
67D4: 62         LD           H,D
67D5: 75         LD           (HL),L
67D6: 69         LD           L,C
67D7: 6C         LD           L,H
67D8: 64         LD           H,H
67D9: 20 75      JR           NZ,$6850
67DB: 70         LD           (HL),B
67DC: 20 79      JR           NZ,$6857
67DE: 6F         LD           L,A
67DF: 75         LD           (HL),L
67E0: 72         LD           (HL),D
67E1: 20 20      JR           NZ,$6803
67E3: 20 70      JR           NZ,$6855
67E5: 6F         LD           L,A
67E6: 77         LD           (HL),A
67E7: 65         LD           H,L
67E8: 72         LD           (HL),D
67E9: 2E 20      LD           L,$20
67EB: 20 57      JR           NZ,$6844
67ED: 68         LD           L,B
67EE: 65         LD           H,L
67EF: 6E         LD           L,(HL)
67F0: 20 79      JR           NZ,$686B
67F2: 6F         LD           L,A
67F3: 75         LD           (HL),L
67F4: 68         LD           L,B
67F5: 61         LD           H,C
67F6: 76         HALT
67F7: 65         LD           H,L
67F8: 20 65      JR           NZ,$685F
67FA: 6E         LD           L,(HL)
67FB: 6F         LD           L,A
67FC: 75         LD           (HL),L
67FD: 67         LD           H,A
67FE: 68         LD           L,B
67FF: 2C         INC         L
6800: 20 79      JR           NZ,$687B
6802: 6F         LD           L,A
6803: 75         LD           (HL),L
6804: 63         LD           H,E
6805: 61         LD           H,C
6806: 6E         LD           L,(HL)
6807: 20 72      JR           NZ,$687B
6809: 65         LD           H,L
680A: 6C         LD           L,H
680B: 65         LD           H,L
680C: 61         LD           H,C
680D: 73         LD           (HL),E
680E: 65         LD           H,L
680F: 20 74      JR           NZ,$6885
6811: 68         LD           L,B
6812: 65         LD           H,L
6813: 20 42      JR           NZ,$6857
6815: 75         LD           (HL),L
6816: 74         LD           (HL),H
6817: 74         LD           (HL),H
6818: 6F         LD           L,A
6819: 6E         LD           L,(HL)
681A: 21 20 20   LD           HL,$2020
681D: 43         LD           B,E
681E: 61         LD           H,C
681F: 6E         LD           L,(HL)
6820: 20 79      JR           NZ,$689B
6822: 6F         LD           L,A
6823: 75         LD           (HL),L
6824: 6D         LD           L,L
6825: 61         LD           H,C
6826: 73         LD           (HL),E
6827: 74         LD           (HL),H
6828: 65         LD           H,L
6829: 72         LD           (HL),D
682A: 20 74      JR           NZ,$68A0
682C: 68         LD           L,B
682D: 69         LD           L,C
682E: 73         LD           (HL),E
682F: 3F         CCF
6830: 5E         LD           E,(HL)
6831: FF         RST         0X38
6832: 5E         LD           E,(HL)
6833: 54         LD           D,H
6834: 68         LD           L,B
6835: 65         LD           H,L
6836: 20 50      JR           NZ,$6888
6838: 72         LD           (HL),D
6839: 6F         LD           L,A
683A: 70         LD           (HL),B
683B: 65         LD           H,L
683C: 72         LD           (HL),D
683D: 74         LD           (HL),H
683E: 69         LD           L,C
683F: 65         LD           H,L
6840: 73         LD           (HL),E
6841: 20 20      JR           NZ,$6863
6843: 20 4F      JR           NZ,$6894
6845: 66         LD           H,(HL)
6846: 20 57      JR           NZ,$689F
6848: 61         LD           H,C
6849: 72         LD           (HL),D
684A: 70         LD           (HL),B
684B: 20 48      JR           NZ,$6895
684D: 6F         LD           L,A
684E: 6C         LD           L,H
684F: 65         LD           H,L
6850: 73         LD           (HL),E
6851: 5E         LD           E,(HL)
6852: 52         LD           D,D
6853: 65         LD           H,L
6854: 61         LD           H,C
6855: 64         LD           H,H
6856: 20 74      JR           NZ,$68CC
6858: 68         LD           L,B
6859: 69         LD           L,C
685A: 73         LD           (HL),E
685B: 20 62      JR           NZ,$68BF
685D: 6F         LD           L,A
685E: 6F         LD           L,A
685F: 6B         LD           L,E
6860: 3F         CCF
6861: 20 20      JR           NZ,$6883
6863: 20 20      JR           NZ,$6885
6865: 20 52      JR           NZ,$68B9
6867: 65         LD           H,L
6868: 61         LD           H,C
6869: 64         LD           H,H
686A: 20 44      JR           NZ,$68B0
686C: 6F         LD           L,A
686D: 6E         LD           L,(HL)
686E: 5E         LD           E,(HL)
686F: 74         LD           (HL),H
6870: FE 5E      CP           $5E
6872: 54         LD           D,H
6873: 68         LD           L,B
6874: 65         LD           H,L
6875: 72         LD           (HL),D
6876: 65         LD           H,L
6877: 20 61      JR           NZ,$68DA
6879: 72         LD           (HL),D
687A: 65         LD           H,L
687B: 20 73      JR           NZ,$68F0
687D: 6F         LD           L,A
687E: 6D         LD           L,L
687F: 65         LD           H,L
6880: 20 57      JR           NZ,$68D9
6882: 61         LD           H,C
6883: 72         LD           (HL),D
6884: 70         LD           (HL),B
6885: 20 48      JR           NZ,$68CF
6887: 6F         LD           L,A
6888: 6C         LD           L,H
6889: 65         LD           H,L
688A: 73         LD           (HL),E
688B: 20 6F      JR           NZ,$68FC
688D: 6E         LD           L,(HL)
688E: 20 20      JR           NZ,$68B0
6890: 20 4B      JR           NZ,$68DD
6892: 6F         LD           L,A
6893: 68         LD           L,B
6894: 6F         LD           L,A
6895: 6C         LD           L,H
6896: 69         LD           L,C
6897: 6E         LD           L,(HL)
6898: 74         LD           (HL),H
6899: 20 49      JR           NZ,$68E4
689B: 73         LD           (HL),E
689C: 6C         LD           L,H
689D: 61         LD           H,C
689E: 6E         LD           L,(HL)
689F: 64         LD           H,H
68A0: 2E 59      LD           L,$59
68A2: 6F         LD           L,A
68A3: 75         LD           (HL),L
68A4: 20 63      JR           NZ,$6909
68A6: 61         LD           H,C
68A7: 6E         LD           L,(HL)
68A8: 20 77      JR           NZ,$6921
68AA: 61         LD           H,C
68AB: 72         LD           (HL),D
68AC: 70         LD           (HL),B
68AD: 20 74      JR           NZ,$6923
68AF: 6F         LD           L,A
68B0: 20 61      JR           NZ,$6913
68B2: 6E         LD           L,(HL)
68B3: 64         LD           H,H
68B4: 20 66      JR           NZ,$691C
68B6: 72         LD           (HL),D
68B7: 6F         LD           L,A
68B8: 20 75      JR           NZ,$692F
68BA: 73         LD           (HL),E
68BB: 69         LD           L,C
68BC: 6E         LD           L,(HL)
68BD: 67         LD           H,A
68BE: 20 20      JR           NZ,$68E0
68C0: 20 74      JR           NZ,$6936
68C2: 68         LD           L,B
68C3: 65         LD           H,L
68C4: 73         LD           (HL),E
68C5: 65         LD           H,L
68C6: 20 68      JR           NZ,$6930
68C8: 6F         LD           L,A
68C9: 6C         LD           L,H
68CA: 65         LD           H,L
68CB: 73         LD           (HL),E
68CC: 2E 20      LD           L,$20
68CE: 20 49      JR           NZ,$6919
68D0: 66         LD           H,(HL)
68D1: 79         LD           A,C
68D2: 6F         LD           L,A
68D3: 75         LD           (HL),L
68D4: 20 6A      JR           NZ,$6940
68D6: 75         LD           (HL),L
68D7: 6D         LD           L,L
68D8: 70         LD           (HL),B
68D9: 20 69      JR           NZ,$6944
68DB: 6E         LD           L,(HL)
68DC: 74         LD           (HL),H
68DD: 6F         LD           L,A
68DE: 20 20      JR           NZ,$6900
68E0: 20 74      JR           NZ,$6956
68E2: 68         LD           L,B
68E3: 65         LD           H,L
68E4: 20 57      JR           NZ,$693D
68E6: 61         LD           H,C
68E7: 72         LD           (HL),D
68E8: 70         LD           (HL),B
68E9: 20 48      JR           NZ,$6933
68EB: 6F         LD           L,A
68EC: 6C         LD           L,H
68ED: 65         LD           H,L
68EE: 20 20      JR           NZ,$6910
68F0: 20 61      JR           NZ,$6953
68F2: 74         LD           (HL),H
68F3: 20 77      JR           NZ,$696C
68F5: 68         LD           L,B
68F6: 69         LD           L,C
68F7: 63         LD           H,E
68F8: 68         LD           L,B
68F9: 20 79      JR           NZ,$6974
68FB: 6F         LD           L,A
68FC: 75         LD           (HL),L
68FD: 20 20      JR           NZ,$691F
68FF: 20 20      JR           NZ,$6921
6901: 61         LD           H,C
6902: 72         LD           (HL),D
6903: 72         LD           (HL),D
6904: 69         LD           L,C
6905: 76         HALT
6906: 65         LD           H,L
6907: 64         LD           H,H
6908: 2C         INC         L
6909: 20 79      JR           NZ,$6984
690B: 6F         LD           L,A
690C: 75         LD           (HL),L
690D: 20 20      JR           NZ,$692F
690F: 20 20      JR           NZ,$6931
6911: 77         LD           (HL),A
6912: 69         LD           L,C
6913: 6C         LD           L,H
6914: 6C         LD           L,H
6915: 20 67      JR           NZ,$697E
6917: 6F         LD           L,A
6918: 20 74      JR           NZ,$698E
691A: 6F         LD           L,A
691B: 20 74      JR           NZ,$6991
691D: 68         LD           L,B
691E: 65         LD           H,L
691F: 20 20      JR           NZ,$6941
6921: 6E         LD           L,(HL)
6922: 65         LD           H,L
6923: 78         LD           A,B
6924: 74         LD           (HL),H
6925: 20 6F      JR           NZ,$6996
6927: 6E         LD           L,(HL)
6928: 65         LD           H,L
6929: 20 69      JR           NZ,$6994
692B: 6E         LD           L,(HL)
692C: 20 74      JR           NZ,$69A2
692E: 68         LD           L,B
692F: 65         LD           H,L
6930: 20 73      JR           NZ,$69A5
6932: 65         LD           H,L
6933: 71         LD           (HL),C
6934: 75         LD           (HL),L
6935: 65         LD           H,L
6936: 6E         LD           L,(HL)
6937: 63         LD           H,E
6938: 65         LD           H,L
6939: 2E 20      LD           L,$20
693B: 20 59      JR           NZ,$6996
693D: 6F         LD           L,A
693E: 75         LD           (HL),L
693F: 20 20      JR           NZ,$6961
6941: 63         LD           H,E
6942: 61         LD           H,C
6943: 6E         LD           L,(HL)
6944: 20 6F      JR           NZ,$69B5
6946: 6E         LD           L,(HL)
6947: 6C         LD           L,H
6948: 79         LD           A,C
6949: 20 77      JR           NZ,$69C2
694B: 61         LD           H,C
694C: 72         LD           (HL),D
694D: 70         LD           (HL),B
694E: 20 74      JR           NZ,$69C4
6950: 6F         LD           L,A
6951: 61         LD           H,C
6952: 20 68      JR           NZ,$69BC
6954: 6F         LD           L,A
6955: 6C         LD           L,H
6956: 65         LD           H,L
6957: 20 79      JR           NZ,$69D2
6959: 6F         LD           L,A
695A: 75         LD           (HL),L
695B: 20 68      JR           NZ,$69C5
695D: 61         LD           H,C
695E: 76         HALT
695F: 65         LD           H,L
6960: 20 73      JR           NZ,$69D5
6962: 65         LD           H,L
6963: 65         LD           H,L
6964: 6E         LD           L,(HL)
6965: 20 77      JR           NZ,$69DE
6967: 69         LD           L,C
6968: 74         LD           (HL),H
6969: 68         LD           L,B
696A: 20 79      JR           NZ,$69E5
696C: 6F         LD           L,A
696D: 75         LD           (HL),L
696E: 72         LD           (HL),D
696F: 20 20      JR           NZ,$6991
6971: 6F         LD           L,A
6972: 77         LD           (HL),A
6973: 6E         LD           L,(HL)
6974: 20 65      JR           NZ,$69DB
6976: 79         LD           A,C
6977: 65         LD           H,L
6978: 73         LD           (HL),E
6979: 2E 2E      LD           L,$2E
697B: 2E 5E      LD           L,$5E
697D: FF         RST         0X38
697E: 5E         LD           E,(HL)
697F: 46         LD           B,(HL)
6980: 75         LD           (HL),L
6981: 6E         LD           L,(HL)
6982: 20 57      JR           NZ,$69DB
6984: 69         LD           L,C
6985: 74         LD           (HL),H
6986: 68         LD           L,B
6987: 20 42      JR           NZ,$69CB
6989: 6F         LD           L,A
698A: 6D         LD           L,L
698B: 62         LD           H,D
698C: 73         LD           (HL),E
698D: 5E         LD           E,(HL)
698E: 52         LD           D,D
698F: 65         LD           H,L
6990: 61         LD           H,C
6991: 64         LD           H,H
6992: 20 74      JR           NZ,$6A08
6994: 68         LD           L,B
6995: 69         LD           L,C
6996: 73         LD           (HL),E
6997: 20 62      JR           NZ,$69FB
6999: 6F         LD           L,A
699A: 6F         LD           L,A
699B: 6B         LD           L,E
699C: 3F         CCF
699D: 20 20      JR           NZ,$69BF
699F: 20 20      JR           NZ,$69C1
69A1: 20 52      JR           NZ,$69F5
69A3: 65         LD           H,L
69A4: 61         LD           H,C
69A5: 64         LD           H,H
69A6: 20 44      JR           NZ,$69EC
69A8: 6F         LD           L,A
69A9: 6E         LD           L,(HL)
69AA: 5E         LD           E,(HL)
69AB: 74         LD           (HL),H
69AC: FE 5E      CP           $5E
69AE: 41         LD           B,C
69AF: 66         LD           H,(HL)
69B0: 74         LD           (HL),H
69B1: 65         LD           H,L
69B2: 72         LD           (HL),D
69B3: 20 79      JR           NZ,$6A2E
69B5: 6F         LD           L,A
69B6: 75         LD           (HL),L
69B7: 20 70      JR           NZ,$6A29
69B9: 75         LD           (HL),L
69BA: 74         LD           (HL),H
69BB: 20 61      JR           NZ,$6A1E
69BD: 42         LD           B,D
69BE: 6F         LD           L,A
69BF: 6D         LD           L,L
69C0: 62         LD           H,D
69C1: 20 64      JR           NZ,$6A27
69C3: 6F         LD           L,A
69C4: 77         LD           (HL),A
69C5: 6E         LD           L,(HL)
69C6: 2C         INC         L
69C7: 20 79      JR           NZ,$6A42
69C9: 6F         LD           L,A
69CA: 75         LD           (HL),L
69CB: 20 20      JR           NZ,$69ED
69CD: 63         LD           H,E
69CE: 61         LD           H,C
69CF: 6E         LD           L,(HL)
69D0: 20 70      JR           NZ,$6A42
69D2: 69         LD           L,C
69D3: 63         LD           H,E
69D4: 6B         LD           L,E
69D5: 20 69      JR           NZ,$6A40
69D7: 74         LD           (HL),H
69D8: 20 75      JR           NZ,$6A4F
69DA: 70         LD           (HL),B
69DB: 20 20      JR           NZ,$69FD
69DD: 62         LD           H,D
69DE: 79         LD           A,C
69DF: 20 70      JR           NZ,$6A51
69E1: 72         LD           (HL),D
69E2: 65         LD           H,L
69E3: 73         LD           (HL),E
69E4: 73         LD           (HL),E
69E5: 69         LD           L,C
69E6: 6E         LD           L,(HL)
69E7: 67         LD           H,A
69E8: 20 74      JR           NZ,$6A5E
69EA: 68         LD           L,B
69EB: 65         LD           H,L
69EC: 20 42      JR           NZ,$6A30
69EE: 75         LD           (HL),L
69EF: 74         LD           (HL),H
69F0: 74         LD           (HL),H
69F1: 6F         LD           L,A
69F2: 6E         LD           L,(HL)
69F3: 20 61      JR           NZ,$6A56
69F5: 67         LD           H,A
69F6: 61         LD           H,C
69F7: 69         LD           L,C
69F8: 6E         LD           L,(HL)
69F9: 2E 20      LD           L,$20
69FB: 20 20      JR           NZ,$6A1D
69FD: 59         LD           E,C
69FE: 6F         LD           L,A
69FF: 75         LD           (HL),L
6A00: 20 63      JR           NZ,$6A65
6A02: 61         LD           H,C
6A03: 6E         LD           L,(HL)
6A04: 20 74      JR           NZ,$6A7A
6A06: 68         LD           L,B
6A07: 65         LD           H,L
6A08: 6E         LD           L,(HL)
6A09: 20 20      JR           NZ,$6A2B
6A0B: 20 20      JR           NZ,$6A2D
6A0D: 74         LD           (HL),H
6A0E: 68         LD           L,B
6A0F: 72         LD           (HL),D
6A10: 6F         LD           L,A
6A11: 77         LD           (HL),A
6A12: 20 69      JR           NZ,$6A7D
6A14: 74         LD           (HL),H
6A15: 20 62      JR           NZ,$6A79
6A17: 79         LD           A,C
6A18: 20 20      JR           NZ,$6A3A
6A1A: 20 20      JR           NZ,$6A3C
6A1C: 20 70      JR           NZ,$6A8E
6A1E: 75         LD           (HL),L
6A1F: 73         LD           (HL),E
6A20: 68         LD           L,B
6A21: 69         LD           L,C
6A22: 6E         LD           L,(HL)
6A23: 67         LD           H,A
6A24: 20 74      JR           NZ,$6A9A
6A26: 68         LD           L,B
6A27: 65         LD           H,L
6A28: 20 20      JR           NZ,$6A4A
6A2A: 20 20      JR           NZ,$6A4C
6A2C: 20 42      JR           NZ,$6A70
6A2E: 75         LD           (HL),L
6A2F: 74         LD           (HL),H
6A30: 74         LD           (HL),H
6A31: 6F         LD           L,A
6A32: 6E         LD           L,(HL)
6A33: 20 6F      JR           NZ,$6AA4
6A35: 6E         LD           L,(HL)
6A36: 65         LD           H,L
6A37: 20 6D      JR           NZ,$6AA6
6A39: 6F         LD           L,A
6A3A: 72         LD           (HL),D
6A3B: 65         LD           H,L
6A3C: 20 74      JR           NZ,$6AB2
6A3E: 69         LD           L,C
6A3F: 6D         LD           L,L
6A40: 65         LD           H,L
6A41: 2E 20      LD           L,$20
6A43: 20 44      JR           NZ,$6A89
6A45: 69         LD           L,C
6A46: 64         LD           H,H
6A47: 20 79      JR           NZ,$6AC2
6A49: 6F         LD           L,A
6A4A: 75         LD           (HL),L
6A4B: 20 20      JR           NZ,$6A6D
6A4D: 6B         LD           L,E
6A4E: 6E         LD           L,(HL)
6A4F: 6F         LD           L,A
6A50: 77         LD           (HL),A
6A51: 20 74      JR           NZ,$6AC7
6A53: 68         LD           L,B
6A54: 61         LD           H,C
6A55: 74         LD           (HL),H
6A56: 3F         CCF
6A57: 5E         LD           E,(HL)
6A58: FF         RST         0X38
6A59: 20 20      JR           NZ,$6A7B
6A5B: 20 5E      JR           NZ,$6ABB
6A5D: 41         LD           B,C
6A5E: 74         LD           (HL),H
6A5F: 6C         LD           L,H
6A60: 61         LD           H,C
6A61: 73         LD           (HL),E
6A62: 20 4F      JR           NZ,$6AB3
6A64: 66         LD           H,(HL)
6A65: 20 20      JR           NZ,$6A87
6A67: 20 20      JR           NZ,$6A89
6A69: 4B         LD           C,E
6A6A: 6F         LD           L,A
6A6B: 68         LD           L,B
6A6C: 6F         LD           L,A
6A6D: 6C         LD           L,H
6A6E: 69         LD           L,C
6A6F: 6E         LD           L,(HL)
6A70: 74         LD           (HL),H
6A71: 20 49      JR           NZ,$6ABC
6A73: 73         LD           (HL),E
6A74: 6C         LD           L,H
6A75: 61         LD           H,C
6A76: 6E         LD           L,(HL)
6A77: 64         LD           H,H
6A78: 5E         LD           E,(HL)
6A79: 59         LD           E,C
6A7A: 6F         LD           L,A
6A7B: 75         LD           (HL),L
6A7C: 20 63      JR           NZ,$6AE1
6A7E: 61         LD           H,C
6A7F: 6E         LD           L,(HL)
6A80: 20 6D      JR           NZ,$6AEF
6A82: 6F         LD           L,A
6A83: 76         HALT
6A84: 65         LD           H,L
6A85: 20 74      JR           NZ,$6AFB
6A87: 68         LD           L,B
6A88: 65         LD           H,L
6A89: 63         LD           H,E
6A8A: 75         LD           (HL),L
6A8B: 72         LD           (HL),D
6A8C: 73         LD           (HL),E
6A8D: 6F         LD           L,A
6A8E: 72         LD           (HL),D
6A8F: 20 61      JR           NZ,$6AF2
6A91: 6E         LD           L,(HL)
6A92: 64         LD           H,H
6A93: 20 6C      JR           NZ,$6B01
6A95: 6F         LD           L,A
6A96: 6F         LD           L,A
6A97: 6B         LD           L,E
6A98: 20 75      JR           NZ,$6B0F
6A9A: 70         LD           (HL),B
6A9B: 20 74      JR           NZ,$6B11
6A9D: 68         LD           L,B
6A9E: 65         LD           H,L
6A9F: 20 6E      JR           NZ,$6B0F
6AA1: 61         LD           H,C
6AA2: 6D         LD           L,L
6AA3: 65         LD           H,L
6AA4: 20 6F      JR           NZ,$6B15
6AA6: 66         LD           H,(HL)
6AA7: 20 61      JR           NZ,$6B0A
6AA9: 70         LD           (HL),B
6AAA: 6C         LD           L,H
6AAB: 61         LD           H,C
6AAC: 63         LD           H,E
6AAD: 65         LD           H,L
6AAE: 2E 2E      LD           L,$2E
6AB0: 2E 20      LD           L,$20
6AB2: 20 44      JR           NZ,$6AF8
6AB4: 6F         LD           L,A
6AB5: 20 79      JR           NZ,$6B30
6AB7: 6F         LD           L,A
6AB8: 75         LD           (HL),L
6AB9: 77         LD           (HL),A
6ABA: 61         LD           H,C
6ABB: 6E         LD           L,(HL)
6ABC: 74         LD           (HL),H
6ABD: 20 74      JR           NZ,$6B33
6ABF: 6F         LD           L,A
6AC0: 20 6C      JR           NZ,$6B2E
6AC2: 6F         LD           L,A
6AC3: 6F         LD           L,A
6AC4: 6B         LD           L,E
6AC5: 20 61      JR           NZ,$6B28
6AC7: 74         LD           (HL),H
6AC8: 20 74      JR           NZ,$6B3E
6ACA: 68         LD           L,B
6ACB: 69         LD           L,C
6ACC: 73         LD           (HL),E
6ACD: 20 6D      JR           NZ,$6B3C
6ACF: 61         LD           H,C
6AD0: 70         LD           (HL),B
6AD1: 3F         CCF
6AD2: 20 20      JR           NZ,$6AF4
6AD4: 20 20      JR           NZ,$6AF6
6AD6: 20 20      JR           NZ,$6AF8
6AD8: 20 20      JR           NZ,$6AFA
6ADA: 20 20      JR           NZ,$6AFC
6ADC: 20 4C      JR           NZ,$6B2A
6ADE: 6F         LD           L,A
6ADF: 6F         LD           L,A
6AE0: 6B         LD           L,E
6AE1: 20 44      JR           NZ,$6B27
6AE3: 6F         LD           L,A
6AE4: 6E         LD           L,(HL)
6AE5: 5E         LD           E,(HL)
6AE6: 74         LD           (HL),H
6AE7: FE 20      CP           $20
6AE9: 5E         LD           E,(HL)
6AEA: 44         LD           B,H
6AEB: 61         LD           H,C
6AEC: 72         LD           (HL),D
6AED: 6B         LD           L,E
6AEE: 20 53      JR           NZ,$6B43
6AF0: 65         LD           H,L
6AF1: 63         LD           H,E
6AF2: 72         LD           (HL),D
6AF3: 65         LD           H,L
6AF4: 74         LD           (HL),H
6AF5: 73         LD           (HL),E
6AF6: 20 20      JR           NZ,$6B18
6AF8: 20 20      JR           NZ,$6B1A
6AFA: 41         LD           B,C
6AFB: 6E         LD           L,(HL)
6AFC: 64         LD           H,H
6AFD: 20 4D      JR           NZ,$6B4C
6AFF: 79         LD           A,C
6B00: 73         LD           (HL),E
6B01: 74         LD           (HL),H
6B02: 65         LD           H,L
6B03: 72         LD           (HL),D
6B04: 69         LD           L,C
6B05: 65         LD           H,L
6B06: 73         LD           (HL),E
6B07: 20 20      JR           NZ,$6B29
6B09: 20 20      JR           NZ,$6B2B
6B0B: 4F         LD           C,A
6B0C: 66         LD           H,(HL)
6B0D: 20 4B      JR           NZ,$6B5A
6B0F: 6F         LD           L,A
6B10: 68         LD           L,B
6B11: 6F         LD           L,A
6B12: 6C         LD           L,H
6B13: 69         LD           L,C
6B14: 6E         LD           L,(HL)
6B15: 74         LD           (HL),H
6B16: 5E         LD           E,(HL)
6B17: 20 44      JR           NZ,$6B5D
6B19: 6F         LD           L,A
6B1A: 20 79      JR           NZ,$6B95
6B1C: 6F         LD           L,A
6B1D: 75         LD           (HL),L
6B1E: 20 72      JR           NZ,$6B92
6B20: 65         LD           H,L
6B21: 61         LD           H,C
6B22: 6C         LD           L,H
6B23: 6C         LD           L,H
6B24: 79         LD           A,C
6B25: 20 20      JR           NZ,$6B47
6B27: 20 77      JR           NZ,$6BA0
6B29: 61         LD           H,C
6B2A: 6E         LD           L,(HL)
6B2B: 74         LD           (HL),H
6B2C: 20 74      JR           NZ,$6BA2
6B2E: 6F         LD           L,A
6B2F: 20 72      JR           NZ,$6BA3
6B31: 65         LD           H,L
6B32: 61         LD           H,C
6B33: 64         LD           H,H
6B34: 20 69      JR           NZ,$6B9F
6B36: 74         LD           (HL),H
6B37: 3F         CCF
6B38: 20 20      JR           NZ,$6B5A
6B3A: 20 20      JR           NZ,$6B5C
6B3C: 59         LD           E,C
6B3D: 65         LD           H,L
6B3E: 73         LD           (HL),E
6B3F: 21 20 4E   LD           HL,$4E20
6B42: 2D         DEC         L
6B43: 4E         LD           C,(HL)
6B44: 6F         LD           L,A
6B45: FE 47      CP           $47
6B47: 61         LD           H,C
6B48: 73         LD           (HL),E
6B49: 70         LD           (HL),B
6B4A: 21 20 57   LD           HL,$5720
6B4D: 68         LD           L,B
6B4E: 61         LD           H,C
6B4F: 2D         DEC         L
6B50: 57         LD           D,A
6B51: 68         LD           L,B
6B52: 61         LD           H,C
6B53: 74         LD           (HL),H
6B54: 5E         LD           E,(HL)
6B55: 73         LD           (HL),E
6B56: 74         LD           (HL),H
6B57: 68         LD           L,B
6B58: 69         LD           L,C
6B59: 73         LD           (HL),E
6B5A: 21 20 2E   LD           HL,$2E20
6B5D: 2E 2E      LD           L,$2E
6B5F: 20 2E      JR           NZ,$6B8F
6B61: 2E 2E      LD           L,$2E
6B63: 20 20      JR           NZ,$6B85
6B65: 20 59      JR           NZ,$6BC0
6B67: 6F         LD           L,A
6B68: 75         LD           (HL),L
6B69: 20 63      JR           NZ,$6BCE
6B6B: 61         LD           H,C
6B6C: 6E         LD           L,(HL)
6B6D: 5E         LD           E,(HL)
6B6E: 74         LD           (HL),H
6B6F: 20 72      JR           NZ,$6BE3
6B71: 65         LD           H,L
6B72: 61         LD           H,C
6B73: 64         LD           H,H
6B74: 20 20      JR           NZ,$6B96
6B76: 74         LD           (HL),H
6B77: 68         LD           L,B
6B78: 65         LD           H,L
6B79: 20 74      JR           NZ,$6BEF
6B7B: 69         LD           L,C
6B7C: 6E         LD           L,(HL)
6B7D: 79         LD           A,C
6B7E: 20 70      JR           NZ,$6BF0
6B80: 72         LD           (HL),D
6B81: 69         LD           L,C
6B82: 6E         LD           L,(HL)
6B83: 74         LD           (HL),H
6B84: 20 20      JR           NZ,$6BA6
6B86: 77         LD           (HL),A
6B87: 69         LD           L,C
6B88: 74         LD           (HL),H
6B89: 68         LD           L,B
6B8A: 6F         LD           L,A
6B8B: 75         LD           (HL),L
6B8C: 74         LD           (HL),H
6B8D: 20 74      JR           NZ,$6C03
6B8F: 68         LD           L,B
6B90: 65         LD           H,L
6B91: 20 61      JR           NZ,$6BF4
6B93: 69         LD           L,C
6B94: 64         LD           H,H
6B95: 20 6F      JR           NZ,$6C06
6B97: 66         LD           H,(HL)
6B98: 20 61      JR           NZ,$6BFB
6B9A: 20 6D      JR           NZ,$6C09
6B9C: 61         LD           H,C
6B9D: 67         LD           H,A
6B9E: 6E         LD           L,(HL)
6B9F: 69         LD           L,C
6BA0: 66         LD           H,(HL)
6BA1: 79         LD           A,C
6BA2: 69         LD           L,C
6BA3: 6E         LD           L,(HL)
6BA4: 67         LD           H,A
6BA5: 20 67      JR           NZ,$6C0E
6BA7: 6C         LD           L,H
6BA8: 61         LD           H,C
6BA9: 73         LD           (HL),E
6BAA: 73         LD           (HL),E
6BAB: 2E 2E      LD           L,$2E
6BAD: 2E FF      LD           L,$FF
6BAF: 2E 2E      LD           L,$2E
6BB1: 2E 6D      LD           L,$6D
6BB3: 79         LD           A,C
6BB4: 20 67      JR           NZ,$6C1D
6BB6: 72         LD           (HL),D
6BB7: 61         LD           H,C
6BB8: 76         HALT
6BB9: 65         LD           H,L
6BBA: 2E 2E      LD           L,$2E
6BBC: 2E 20      LD           L,$20
6BBE: 20 2E      JR           NZ,$6BEE
6BC0: 2E 2E      LD           L,$2E
6BC2: 74         LD           (HL),H
6BC3: 61         LD           H,C
6BC4: 6B         LD           L,E
6BC5: 65         LD           H,L
6BC6: 20 6D      JR           NZ,$6C35
6BC8: 65         LD           H,L
6BC9: 2E 2E      LD           L,$2E
6BCB: 2E 20      LD           L,$20
6BCD: 20 20      JR           NZ,$6BEF
6BCF: 2E 2E      LD           L,$2E
6BD1: 2E 6D      LD           L,$6D
6BD3: 79         LD           A,C
6BD4: 20 67      JR           NZ,$6C3D
6BD6: 72         LD           (HL),D
6BD7: 61         LD           H,C
6BD8: 76         HALT
6BD9: 65         LD           H,L
6BDA: 2E 2E      LD           L,$2E
6BDC: 2E FF      LD           L,$FF
6BDE: 2E 2E      LD           L,$2E
6BE0: 2E 74      LD           L,$74
6BE2: 68         LD           L,B
6BE3: 65         LD           H,L
6BE4: 20 68      JR           NZ,$6C4E
6BE6: 6F         LD           L,A
6BE7: 75         LD           (HL),L
6BE8: 73         LD           (HL),E
6BE9: 65         LD           H,L
6BEA: 2E 2E      LD           L,$2E
6BEC: 2E 20      LD           L,$20
6BEE: 20 2E      JR           NZ,$6C1E
6BF0: 2E 2E      LD           L,$2E
6BF2: 74         LD           (HL),H
6BF3: 61         LD           H,C
6BF4: 6B         LD           L,E
6BF5: 65         LD           H,L
6BF6: 20 6D      JR           NZ,$6C65
6BF8: 65         LD           H,L
6BF9: 2E 2E      LD           L,$2E
6BFB: 2E 20      LD           L,$20
6BFD: 20 2E      JR           NZ,$6C2D
6BFF: 2E 2E      LD           L,$2E
6C01: 74         LD           (HL),H
6C02: 68         LD           L,B
6C03: 65         LD           H,L
6C04: 20 68      JR           NZ,$6C6E
6C06: 6F         LD           L,A
6C07: 75         LD           (HL),L
6C08: 73         LD           (HL),E
6C09: 65         LD           H,L
6C0A: 2E 2E      LD           L,$2E
6C0C: 2E 20      LD           L,$20
6C0E: 2E 2E      LD           L,$2E
6C10: 2E 61      LD           L,$61
6C12: 74         LD           (HL),H
6C13: 20 74      JR           NZ,$6C89
6C15: 68         LD           L,B
6C16: 65         LD           H,L
6C17: 20 62      JR           NZ,$6C7B
6C19: 61         LD           H,C
6C1A: 79         LD           A,C
6C1B: 2E 2E      LD           L,$2E
6C1D: 2E FF      LD           L,$FF
6C1F: 2E 2E      LD           L,$2E
6C21: 2E 4E      LD           L,$4E
6C23: 2D         DEC         L
6C24: 4E         LD           C,(HL)
6C25: 2D         DEC         L
6C26: 4E         LD           C,(HL)
6C27: 6F         LD           L,A
6C28: 21 2E 2E   LD           HL,$2E2E
6C2B: 2E 20      LD           L,$20
6C2D: 20 20      JR           NZ,$6C4F
6C2F: 2E 2E      LD           L,$2E
6C31: 2E 4E      LD           L,$4E
6C33: 2D         DEC         L
6C34: 6E         LD           L,(HL)
6C35: 6F         LD           L,A
6C36: 74         LD           (HL),H
6C37: 20 74      JR           NZ,$6CAD
6C39: 68         LD           L,B
6C3A: 65         LD           H,L
6C3B: 72         LD           (HL),D
6C3C: 65         LD           H,L
6C3D: 21 FF 20   LD           HL,$20FF
6C40: 20 20      JR           NZ,$6C62
6C42: 2E 2E      LD           L,$2E
6C44: 2E 48      LD           L,$48
6C46: 65         LD           H,L
6C47: 72         LD           (HL),D
6C48: 65         LD           H,L
6C49: 21 2E 2E   LD           HL,$2E2E
6C4C: 2E 20      LD           L,$20
6C4E: 20 20      JR           NZ,$6C70
6C50: 20 20      JR           NZ,$6C72
6C52: 2E 2E      LD           L,$2E
6C54: 2E 65      LD           L,$65
6C56: 6E         LD           L,(HL)
6C57: 74         LD           (HL),H
6C58: 65         LD           H,L
6C59: 72         LD           (HL),D
6C5A: 2E 2E      LD           L,$2E
6C5C: 2E 20      LD           L,$20
6C5E: 20 20      JR           NZ,$6C80
6C60: 2E 2E      LD           L,$2E
6C62: 2E 6D      LD           L,$6D
6C64: 79         LD           A,C
6C65: 20 68      JR           NZ,$6CCF
6C67: 6F         LD           L,A
6C68: 75         LD           (HL),L
6C69: 73         LD           (HL),E
6C6A: 65         LD           H,L
6C6B: 2E 2E      LD           L,$2E
6C6D: 2E FF      LD           L,$FF
6C6F: 20 2E      JR           NZ,$6C9F
6C71: 2E 2E      LD           L,$2E
6C73: 4E         LD           C,(HL)
6C74: 6F         LD           L,A
6C75: 73         LD           (HL),E
6C76: 74         LD           (HL),H
6C77: 61         LD           H,C
6C78: 6C         LD           L,H
6C79: 67         LD           H,A
6C7A: 69         LD           L,C
6C7B: 61         LD           H,C
6C7C: 2E 2E      LD           L,$2E
6C7E: 2E 20      LD           L,$20
6C80: 2E 2E      LD           L,$2E
6C82: 2E 75      LD           L,$75
6C84: 6E         LD           L,(HL)
6C85: 63         LD           H,E
6C86: 68         LD           L,B
6C87: 61         LD           H,C
6C88: 6E         LD           L,(HL)
6C89: 67         LD           H,A
6C8A: 65         LD           H,L
6C8B: 64         LD           H,H
6C8C: 2E 2E      LD           L,$2E
6C8E: 2E 20      LD           L,$20
6C90: 2E 2E      LD           L,$2E
6C92: 2E 62      LD           L,$62
6C94: 6F         LD           L,A
6C95: 6F         LD           L,A
6C96: 20 68      JR           NZ,$6D00
6C98: 6F         LD           L,A
6C99: 6F         LD           L,A
6C9A: 2E 2E      LD           L,$2E
6C9C: 2E FF      LD           L,$FF
6C9E: 20 20      JR           NZ,$6CC0
6CA0: 2E 2E      LD           L,$2E
6CA2: 2E 45      LD           L,$45
6CA4: 6E         LD           L,(HL)
6CA5: 6F         LD           L,A
6CA6: 75         LD           (HL),L
6CA7: 67         LD           H,A
6CA8: 68         LD           L,B
6CA9: 2E 2E      LD           L,$2E
6CAB: 2E 20      LD           L,$20
6CAD: 20 20      JR           NZ,$6CCF
6CAF: 2E 2E      LD           L,$2E
6CB1: 2E 63      LD           L,$63
6CB3: 65         LD           H,L
6CB4: 6D         LD           L,L
6CB5: 65         LD           H,L
6CB6: 74         LD           (HL),H
6CB7: 61         LD           H,C
6CB8: 72         LD           (HL),D
6CB9: 79         LD           A,C
6CBA: 2E 2E      LD           L,$2E
6CBC: 2E 20      LD           L,$20
6CBE: 20 20      JR           NZ,$6CE0
6CC0: 2E 2E      LD           L,$2E
6CC2: 2E 74      LD           L,$74
6CC4: 61         LD           H,C
6CC5: 6B         LD           L,E
6CC6: 65         LD           H,L
6CC7: 20 6D      JR           NZ,$6D36
6CC9: 65         LD           H,L
6CCA: 2E 2E      LD           L,$2E
6CCC: 2E 20      LD           L,$20
6CCE: 20 2E      JR           NZ,$6CFE
6CD0: 2E 2E      LD           L,$2E
6CD2: 6D         LD           L,L
6CD3: 79         LD           A,C
6CD4: 20 67      JR           NZ,$6D3D
6CD6: 72         LD           (HL),D
6CD7: 61         LD           H,C
6CD8: 76         HALT
6CD9: 65         LD           H,L
6CDA: 2E 2E      LD           L,$2E
6CDC: 2E FF      LD           L,$FF
6CDE: 2E 2E      LD           L,$2E
6CE0: 2E 54      LD           L,$54
6CE2: 68         LD           L,B
6CE3: 61         LD           H,C
6CE4: 6E         LD           L,(HL)
6CE5: 6B         LD           L,E
6CE6: 20 79      JR           NZ,$6D61
6CE8: 6F         LD           L,A
6CE9: 75         LD           (HL),L
6CEA: 2E 2E      LD           L,$2E
6CEC: 2E 20      LD           L,$20
6CEE: 20 2E      JR           NZ,$6D1E
6CF0: 2E 2E      LD           L,$2E
6CF2: 61         LD           H,C
6CF3: 20 6A      JR           NZ,$6D5F
6CF5: 61         LD           H,C
6CF6: 72         LD           (HL),D
6CF7: 2E 2E      LD           L,$2E
6CF9: 2E 20      LD           L,$20
6CFB: 20 20      JR           NZ,$6D1D
6CFD: 20 2E      JR           NZ,$6D2D
6CFF: 2E 2E      LD           L,$2E
6D01: 69         LD           L,C
6D02: 6E         LD           L,(HL)
6D03: 20 6D      JR           NZ,$6D72
6D05: 79         LD           A,C
6D06: 20 68      JR           NZ,$6D70
6D08: 6F         LD           L,A
6D09: 6D         LD           L,L
6D0A: 65         LD           H,L
6D0B: 2E 2E      LD           L,$2E
6D0D: 2E 2E      LD           L,$2E
6D0F: 2E 2E      LD           L,$2E
6D11: 6C         LD           L,H
6D12: 6F         LD           L,A
6D13: 6F         LD           L,A
6D14: 6B         LD           L,E
6D15: 20 69      JR           NZ,$6D80
6D17: 6E         LD           L,(HL)
6D18: 73         LD           (HL),E
6D19: 69         LD           L,C
6D1A: 64         LD           H,H
6D1B: 65         LD           H,L
6D1C: 2E 2E      LD           L,$2E
6D1E: 2E 2E      LD           L,$2E
6D20: 2E 62      LD           L,$62
6D22: 79         LD           A,C
6D23: 65         LD           H,L
6D24: 2E 2E      LD           L,$2E
6D26: 2E 62      LD           L,$62
6D28: 79         LD           A,C
6D29: 65         LD           H,L
6D2A: 2E 2E      LD           L,$2E
6D2C: 2E FF      LD           L,$FF
6D2E: 52         LD           D,D
6D2F: 6F         LD           L,A
6D30: 75         LD           (HL),L
6D31: 6E         LD           L,(HL)
6D32: 64         LD           H,H
6D33: 20 61      JR           NZ,$6D96
6D35: 6E         LD           L,(HL)
6D36: 64         LD           H,H
6D37: 20 72      JR           NZ,$6DAB
6D39: 6F         LD           L,A
6D3A: 75         LD           (HL),L
6D3B: 6E         LD           L,(HL)
6D3C: 64         LD           H,H
6D3D: 2C         INC         L
6D3E: 74         LD           (HL),H
6D3F: 68         LD           L,B
6D40: 65         LD           H,L
6D41: 20 70      JR           NZ,$6DB3
6D43: 61         LD           H,C
6D44: 73         LD           (HL),E
6D45: 73         LD           (HL),E
6D46: 61         LD           H,C
6D47: 67         LD           H,A
6D48: 65         LD           H,L
6D49: 77         LD           (HL),A
6D4A: 61         LD           H,C
6D4B: 79         LD           A,C
6D4C: 73         LD           (HL),E
6D4D: 20 6F      JR           NZ,$6DBE
6D4F: 66         LD           H,(HL)
6D50: 20 74      JR           NZ,$6DC6
6D52: 68         LD           L,B
6D53: 65         LD           H,L
6D54: 20 45      JR           NZ,$6D9B
6D56: 67         LD           H,A
6D57: 67         LD           H,A
6D58: 2E 2E      LD           L,$2E
6D5A: 2E 20      LD           L,$20
6D5C: 20 20      JR           NZ,$6D7E
6D5E: F2                              
6D5F: 20 F2      JR           NZ,$6D53
6D61: 20 F0      JR           NZ,$6D53
6D63: 20 F3      JR           NZ,$6D58
6D65: 20 F3      JR           NZ,$6D5A
6D67: 20 F0      JR           NZ,$6D59
6D69: 20 F2      JR           NZ,$6D5D
6D6B: 20 F0      JR           NZ,$6D5D
6D6D: 20 3F      JR           NZ,$6DAE
6D6F: 3F         CCF
6D70: 20 20      JR           NZ,$6D92
6D72: 2E 2E      LD           L,$2E
6D74: 2E 48      LD           L,$48
6D76: 6D         LD           L,L
6D77: 6D         LD           L,L
6D78: 6D         LD           L,L
6D79: 6D         LD           L,L
6D7A: 6D         LD           L,L
6D7B: 6D         LD           L,L
6D7C: 2C         INC         L
6D7D: 20 74      JR           NZ,$6DF3
6D7F: 68         LD           L,B
6D80: 69         LD           L,C
6D81: 73         LD           (HL),E
6D82: 20 62      JR           NZ,$6DE6
6D84: 6F         LD           L,A
6D85: 6F         LD           L,A
6D86: 6B         LD           L,E
6D87: 20 72      JR           NZ,$6DFB
6D89: 65         LD           H,L
6D8A: 65         LD           H,L
6D8B: 6B         LD           L,E
6D8C: 73         LD           (HL),E
6D8D: 20 6F      JR           NZ,$6DFE
6D8F: 66         LD           H,(HL)
6D90: 20 73      JR           NZ,$6E05
6D92: 65         LD           H,L
6D93: 63         LD           H,E
6D94: 72         LD           (HL),D
6D95: 65         LD           H,L
6D96: 74         LD           (HL),H
6D97: 73         LD           (HL),E
6D98: 2E 2E      LD           L,$2E
6D9A: 2E FF      LD           L,$FF
6D9C: 52         LD           D,D
6D9D: 6F         LD           L,A
6D9E: 75         LD           (HL),L
6D9F: 6E         LD           L,(HL)
6DA0: 64         LD           H,H
6DA1: 20 61      JR           NZ,$6E04
6DA3: 6E         LD           L,(HL)
6DA4: 64         LD           H,H
6DA5: 20 72      JR           NZ,$6E19
6DA7: 6F         LD           L,A
6DA8: 75         LD           (HL),L
6DA9: 6E         LD           L,(HL)
6DAA: 64         LD           H,H
6DAB: 2C         INC         L
6DAC: 74         LD           (HL),H
6DAD: 68         LD           L,B
6DAE: 65         LD           H,L
6DAF: 20 70      JR           NZ,$6E21
6DB1: 61         LD           H,C
6DB2: 73         LD           (HL),E
6DB3: 73         LD           (HL),E
6DB4: 61         LD           H,C
6DB5: 67         LD           H,A
6DB6: 65         LD           H,L
6DB7: 77         LD           (HL),A
6DB8: 61         LD           H,C
6DB9: 79         LD           A,C
6DBA: 73         LD           (HL),E
6DBB: 20 6F      JR           NZ,$6E2C
6DBD: 66         LD           H,(HL)
6DBE: 20 74      JR           NZ,$6E34
6DC0: 68         LD           L,B
6DC1: 65         LD           H,L
6DC2: 20 45      JR           NZ,$6E09
6DC4: 67         LD           H,A
6DC5: 67         LD           H,A
6DC6: 2E 2E      LD           L,$2E
6DC8: 2E 20      LD           L,$20
6DCA: 20 20      JR           NZ,$6DEC
6DCC: F3         DI
6DCD: 20 F0      JR           NZ,$6DBF
6DCF: 20 F0      JR           NZ,$6DC1
6DD1: 20 F3      JR           NZ,$6DC6
6DD3: 20 F0      JR           NZ,$6DC5
6DD5: 20 F0      JR           NZ,$6DC7
6DD7: 20 F3      JR           NZ,$6DCC
6DD9: 20 F0      JR           NZ,$6DCB
6DDB: 20 3F      JR           NZ,$6E1C
6DDD: 3F         CCF
6DDE: 20 20      JR           NZ,$6E00
6DE0: 2E 2E      LD           L,$2E
6DE2: 2E 48      LD           L,$48
6DE4: 6D         LD           L,L
6DE5: 6D         LD           L,L
6DE6: 6D         LD           L,L
6DE7: 6D         LD           L,L
6DE8: 6D         LD           L,L
6DE9: 6D         LD           L,L
6DEA: 2C         INC         L
6DEB: 20 74      JR           NZ,$6E61
6DED: 68         LD           L,B
6DEE: 69         LD           L,C
6DEF: 73         LD           (HL),E
6DF0: 20 62      JR           NZ,$6E54
6DF2: 6F         LD           L,A
6DF3: 6F         LD           L,A
6DF4: 6B         LD           L,E
6DF5: 20 72      JR           NZ,$6E69
6DF7: 65         LD           H,L
6DF8: 65         LD           H,L
6DF9: 6B         LD           L,E
6DFA: 73         LD           (HL),E
6DFB: 20 6F      JR           NZ,$6E6C
6DFD: 66         LD           H,(HL)
6DFE: 20 73      JR           NZ,$6E73
6E00: 65         LD           H,L
6E01: 63         LD           H,E
6E02: 72         LD           (HL),D
6E03: 65         LD           H,L
6E04: 74         LD           (HL),H
6E05: 73         LD           (HL),E
6E06: 2E 2E      LD           L,$2E
6E08: 2E FF      LD           L,$FF
6E0A: 52         LD           D,D
6E0B: 6F         LD           L,A
6E0C: 75         LD           (HL),L
6E0D: 6E         LD           L,(HL)
6E0E: 64         LD           H,H
6E0F: 20 61      JR           NZ,$6E72
6E11: 6E         LD           L,(HL)
6E12: 64         LD           H,H
6E13: 20 72      JR           NZ,$6E87
6E15: 6F         LD           L,A
6E16: 75         LD           (HL),L
6E17: 6E         LD           L,(HL)
6E18: 64         LD           H,H
6E19: 2C         INC         L
6E1A: 74         LD           (HL),H
6E1B: 68         LD           L,B
6E1C: 65         LD           H,L
6E1D: 20 70      JR           NZ,$6E8F
6E1F: 61         LD           H,C
6E20: 73         LD           (HL),E
6E21: 73         LD           (HL),E
6E22: 61         LD           H,C
6E23: 67         LD           H,A
6E24: 65         LD           H,L
6E25: 77         LD           (HL),A
6E26: 61         LD           H,C
6E27: 79         LD           A,C
6E28: 73         LD           (HL),E
6E29: 20 6F      JR           NZ,$6E9A
6E2B: 66         LD           H,(HL)
6E2C: 20 74      JR           NZ,$6EA2
6E2E: 68         LD           L,B
6E2F: 65         LD           H,L
6E30: 20 45      JR           NZ,$6E77
6E32: 67         LD           H,A
6E33: 67         LD           H,A
6E34: 2E 2E      LD           L,$2E
6E36: 2E 20      LD           L,$20
6E38: 20 20      JR           NZ,$6E5A
6E3A: F2                              
6E3B: 20 F0      JR           NZ,$6E2D
6E3D: 20 F3      JR           NZ,$6E32
6E3F: 20 F0      JR           NZ,$6E31
6E41: 20 F2      JR           NZ,$6E35
6E43: 20 F0      JR           NZ,$6E35
6E45: 20 F3      JR           NZ,$6E3A
6E47: 20 F0      JR           NZ,$6E39
6E49: 20 3F      JR           NZ,$6E8A
6E4B: 3F         CCF
6E4C: 20 20      JR           NZ,$6E6E
6E4E: 2E 2E      LD           L,$2E
6E50: 2E 48      LD           L,$48
6E52: 6D         LD           L,L
6E53: 6D         LD           L,L
6E54: 6D         LD           L,L
6E55: 6D         LD           L,L
6E56: 6D         LD           L,L
6E57: 6D         LD           L,L
6E58: 2C         INC         L
6E59: 20 74      JR           NZ,$6ECF
6E5B: 68         LD           L,B
6E5C: 69         LD           L,C
6E5D: 73         LD           (HL),E
6E5E: 20 62      JR           NZ,$6EC2
6E60: 6F         LD           L,A
6E61: 6F         LD           L,A
6E62: 6B         LD           L,E
6E63: 20 72      JR           NZ,$6ED7
6E65: 65         LD           H,L
6E66: 65         LD           H,L
6E67: 6B         LD           L,E
6E68: 73         LD           (HL),E
6E69: 20 6F      JR           NZ,$6EDA
6E6B: 66         LD           H,(HL)
6E6C: 20 73      JR           NZ,$6EE1
6E6E: 65         LD           H,L
6E6F: 63         LD           H,E
6E70: 72         LD           (HL),D
6E71: 65         LD           H,L
6E72: 74         LD           (HL),H
6E73: 73         LD           (HL),E
6E74: 2E 2E      LD           L,$2E
6E76: 2E FF      LD           L,$FF
6E78: 52         LD           D,D
6E79: 6F         LD           L,A
6E7A: 75         LD           (HL),L
6E7B: 6E         LD           L,(HL)
6E7C: 64         LD           H,H
6E7D: 20 61      JR           NZ,$6EE0
6E7F: 6E         LD           L,(HL)
6E80: 64         LD           H,H
6E81: 20 72      JR           NZ,$6EF5
6E83: 6F         LD           L,A
6E84: 75         LD           (HL),L
6E85: 6E         LD           L,(HL)
6E86: 64         LD           H,H
6E87: 2C         INC         L
6E88: 74         LD           (HL),H
6E89: 68         LD           L,B
6E8A: 65         LD           H,L
6E8B: 20 70      JR           NZ,$6EFD
6E8D: 61         LD           H,C
6E8E: 73         LD           (HL),E
6E8F: 73         LD           (HL),E
6E90: 61         LD           H,C
6E91: 67         LD           H,A
6E92: 65         LD           H,L
6E93: 77         LD           (HL),A
6E94: 61         LD           H,C
6E95: 79         LD           A,C
6E96: 73         LD           (HL),E
6E97: 20 6F      JR           NZ,$6F08
6E99: 66         LD           H,(HL)
6E9A: 20 74      JR           NZ,$6F10
6E9C: 68         LD           L,B
6E9D: 65         LD           H,L
6E9E: 20 45      JR           NZ,$6EE5
6EA0: 67         LD           H,A
6EA1: 67         LD           H,A
6EA2: 2E 2E      LD           L,$2E
6EA4: 2E 20      LD           L,$20
6EA6: 20 20      JR           NZ,$6EC8
6EA8: F3         DI
6EA9: 20 F3      JR           NZ,$6E9E
6EAB: 20 F3      JR           NZ,$6EA0
6EAD: 20 F3      JR           NZ,$6EA2
6EAF: 20 F0      JR           NZ,$6EA1
6EB1: 20 F0      JR           NZ,$6EA3
6EB3: 20 F0      JR           NZ,$6EA5
6EB5: 20 F0      JR           NZ,$6EA7
6EB7: 20 3F      JR           NZ,$6EF8
6EB9: 3F         CCF
6EBA: 20 20      JR           NZ,$6EDC
6EBC: 2E 2E      LD           L,$2E
6EBE: 2E 48      LD           L,$48
6EC0: 6D         LD           L,L
6EC1: 6D         LD           L,L
6EC2: 6D         LD           L,L
6EC3: 6D         LD           L,L
6EC4: 6D         LD           L,L
6EC5: 6D         LD           L,L
6EC6: 2C         INC         L
6EC7: 20 74      JR           NZ,$6F3D
6EC9: 68         LD           L,B
6ECA: 69         LD           L,C
6ECB: 73         LD           (HL),E
6ECC: 20 62      JR           NZ,$6F30
6ECE: 6F         LD           L,A
6ECF: 6F         LD           L,A
6ED0: 6B         LD           L,E
6ED1: 20 72      JR           NZ,$6F45
6ED3: 65         LD           H,L
6ED4: 65         LD           H,L
6ED5: 6B         LD           L,E
6ED6: 73         LD           (HL),E
6ED7: 20 6F      JR           NZ,$6F48
6ED9: 66         LD           H,(HL)
6EDA: 20 73      JR           NZ,$6F4F
6EDC: 65         LD           H,L
6EDD: 63         LD           H,E
6EDE: 72         LD           (HL),D
6EDF: 65         LD           H,L
6EE0: 74         LD           (HL),H
6EE1: 73         LD           (HL),E
6EE2: 2E 2E      LD           L,$2E
6EE4: 2E FF      LD           L,$FF
6EE6: 2E 2E      LD           L,$2E
6EE8: 2E 59      LD           L,$59
6EEA: 6F         LD           L,A
6EEB: 75         LD           (HL),L
6EEC: 5E         LD           E,(HL)
6EED: 72         LD           (HL),D
6EEE: 65         LD           H,L
6EEF: 20 6C      JR           NZ,$6F5D
6EF1: 61         LD           H,C
6EF2: 74         LD           (HL),H
6EF3: 65         LD           H,L
6EF4: 21 20 49   LD           HL,$4920
6EF7: 20 74      JR           NZ,$6F6D
6EF9: 68         LD           L,B
6EFA: 6F         LD           L,A
6EFB: 75         LD           (HL),L
6EFC: 67         LD           H,A
6EFD: 68         LD           L,B
6EFE: 74         LD           (HL),H
6EFF: 20 79      JR           NZ,$6F7A
6F01: 6F         LD           L,A
6F02: 75         LD           (HL),L
6F03: 5E         LD           E,(HL)
6F04: 64         LD           H,H
6F05: 20 6E      JR           NZ,$6F75
6F07: 65         LD           H,L
6F08: 76         HALT
6F09: 65         LD           H,L
6F0A: 72         LD           (HL),D
6F0B: 20 63      JR           NZ,$6F70
6F0D: 6F         LD           L,A
6F0E: 6D         LD           L,L
6F0F: 65         LD           H,L
6F10: 20 62      JR           NZ,$6F74
6F12: 61         LD           H,C
6F13: 63         LD           H,E
6F14: 6B         LD           L,E
6F15: 21 FF 2E   LD           HL,$2EFF
6F18: 2E 2E      LD           L,$2E
6F1A: 45         LD           B,L
6F1B: 45         LD           B,L
6F1C: 45         LD           B,L
6F1D: 4B         LD           C,E
6F1E: 21 20 20   LD           HL,$2020
6F21: 59         LD           E,C
6F22: 6F         LD           L,A
6F23: 75         LD           (HL),L
6F24: 5E         LD           E,(HL)
6F25: 72         LD           (HL),D
6F26: 65         LD           H,L
6F27: 68         LD           L,B
6F28: 75         LD           (HL),L
6F29: 72         LD           (HL),D
6F2A: 74         LD           (HL),H
6F2B: 21 20 20   LD           HL,$2020
6F2E: 41         LD           B,C
6F2F: 72         LD           (HL),D
6F30: 72         LD           (HL),D
6F31: 72         LD           (HL),D
6F32: 67         LD           H,A
6F33: 68         LD           L,B
6F34: 21 20 20   LD           HL,$2020
6F37: 44         LD           B,H
6F38: 6F         LD           L,A
6F39: 6E         LD           L,(HL)
6F3A: 5E         LD           E,(HL)
6F3B: 74         LD           (HL),H
6F3C: 20 62      JR           NZ,$6FA0
6F3E: 65         LD           H,L
6F3F: 20 73      JR           NZ,$6FB4
6F41: 6F         LD           L,A
6F42: 20 20      JR           NZ,$6F64
6F44: 20 20      JR           NZ,$6F66
6F46: 20 72      JR           NZ,$6FBA
6F48: 65         LD           H,L
6F49: 63         LD           H,E
6F4A: 6B         LD           L,E
6F4B: 6C         LD           L,H
6F4C: 65         LD           H,L
6F4D: 73         LD           (HL),E
6F4E: 73         LD           (HL),E
6F4F: 21 FF 23   LD           HL,$23FF
6F52: 23         INC         HL
6F53: 23         INC         HL
6F54: 23         INC         HL
6F55: 23         INC         HL
6F56: 21 20 59   LD           HL,$5920
6F59: 6F         LD           L,A
6F5A: 75         LD           (HL),L
6F5B: 5E         LD           E,(HL)
6F5C: 72         LD           (HL),D
6F5D: 65         LD           H,L
6F5E: 20 20      JR           NZ,$6F80
6F60: 20 62      JR           NZ,$6FC4
6F62: 61         LD           H,C
6F63: 63         LD           H,E
6F64: 6B         LD           L,E
6F65: 21 20 20   LD           HL,$2020
6F68: 41         LD           B,C
6F69: 72         LD           (HL),D
6F6A: 65         LD           H,L
6F6B: 20 79      JR           NZ,$6FE6
6F6D: 6F         LD           L,A
6F6E: 75         LD           (HL),L
6F6F: 20 20      JR           NZ,$6F91
6F71: 68         LD           L,B
6F72: 75         LD           (HL),L
6F73: 72         LD           (HL),D
6F74: 74         LD           (HL),H
6F75: 3F         CCF
6F76: FF         RST         0X38
6F77: 2E 2E      LD           L,$2E
6F79: 2E 59      LD           L,$59
6F7B: 6F         LD           L,A
6F7C: 75         LD           (HL),L
6F7D: 20 69      JR           NZ,$6FE8
6F7F: 64         LD           H,H
6F80: 69         LD           L,C
6F81: 6F         LD           L,A
6F82: 74         LD           (HL),H
6F83: 21 20 20   LD           HL,$2020
6F86: 20 49      JR           NZ,$6FD1
6F88: 20 74      JR           NZ,$6FFE
6F8A: 6F         LD           L,A
6F8B: 6C         LD           L,H
6F8C: 64         LD           H,H
6F8D: 20 79      JR           NZ,$7008
6F8F: 6F         LD           L,A
6F90: 75         LD           (HL),L
6F91: 20 74      JR           NZ,$7007
6F93: 68         LD           L,B
6F94: 69         LD           L,C
6F95: 73         LD           (HL),E
6F96: 20 77      JR           NZ,$700F
6F98: 6F         LD           L,A
6F99: 75         LD           (HL),L
6F9A: 6C         LD           L,H
6F9B: 64         LD           H,H
6F9C: 20 68      JR           NZ,$7006
6F9E: 61         LD           H,C
6F9F: 70         LD           (HL),B
6FA0: 70         LD           (HL),B
6FA1: 65         LD           H,L
6FA2: 6E         LD           L,(HL)
6FA3: 2E 2E      LD           L,$2E
6FA5: 2E 20      LD           L,$20
6FA7: 45         LD           B,L
6FA8: 68         LD           L,B
6FA9: 3F         CCF
6FAA: 21 20 20   LD           HL,$2020
6FAD: 57         LD           D,A
6FAE: 68         LD           L,B
6FAF: 61         LD           H,C
6FB0: 74         LD           (HL),H
6FB1: 3F         CCF
6FB2: 20 20      JR           NZ,$6FD4
6FB4: 49         LD           C,C
6FB5: 20 20      JR           NZ,$6FD7
6FB7: 64         LD           H,H
6FB8: 69         LD           L,C
6FB9: 64         LD           H,H
6FBA: 6E         LD           L,(HL)
6FBB: 5E         LD           E,(HL)
6FBC: 74         LD           (HL),H
6FBD: 20 73      JR           NZ,$7032
6FBF: 61         LD           H,C
6FC0: 79         LD           A,C
6FC1: 20 61      JR           NZ,$7024
6FC3: 6E         LD           L,(HL)
6FC4: 79         LD           A,C
6FC5: 2D         DEC         L
6FC6: 20 74      JR           NZ,$703C
6FC8: 68         LD           L,B
6FC9: 69         LD           L,C
6FCA: 6E         LD           L,(HL)
6FCB: 67         LD           H,A
6FCC: 2C         INC         L
6FCD: 20 72      JR           NZ,$7041
6FCF: 65         LD           H,L
6FD0: 61         LD           H,C
6FD1: 6C         LD           L,H
6FD2: 6C         LD           L,H
6FD3: 79         LD           A,C
6FD4: 21 FF 48   LD           HL,$48FF
6FD7: 65         LD           H,L
6FD8: 79         LD           A,C
6FD9: 20 62      JR           NZ,$703D
6FDB: 75         LD           (HL),L
6FDC: 64         LD           H,H
6FDD: 64         LD           H,H
6FDE: 79         LD           A,C
6FDF: 21 20 20   LD           HL,$2020
6FE2: 49         LD           C,C
6FE3: 74         LD           (HL),H
6FE4: 5E         LD           E,(HL)
6FE5: 73         LD           (HL),E
6FE6: 73         LD           (HL),E
6FE7: 65         LD           H,L
6FE8: 72         LD           (HL),D
6FE9: 69         LD           L,C
6FEA: 6F         LD           L,A
6FEB: 75         LD           (HL),L
6FEC: 73         LD           (HL),E
6FED: 21 20 20   LD           HL,$2020
6FF0: 59         LD           E,C
6FF1: 65         LD           H,L
6FF2: 61         LD           H,C
6FF3: 68         LD           L,B
6FF4: 2C         INC         L
6FF5: 20 72      JR           NZ,$7069
6FF7: 65         LD           H,L
6FF8: 61         LD           H,C
6FF9: 6C         LD           L,H
6FFA: 6C         LD           L,H
6FFB: 79         LD           A,C
6FFC: 20 73      JR           NZ,$7071
6FFE: 65         LD           H,L
6FFF: 72         LD           (HL),D
7000: 69         LD           L,C
7001: 6F         LD           L,A
7002: 75         LD           (HL),L
7003: 73         LD           (HL),E
7004: 21 21 59   LD           HL,$5921
7007: 65         LD           H,L
7008: 61         LD           H,C
7009: 68         LD           L,B
700A: 2C         INC         L
700B: 20 69      JR           NZ,$7076
700D: 74         LD           (HL),H
700E: 20 69      JR           NZ,$7079
7010: 73         LD           (HL),E
7011: 21 20 20   LD           HL,$2020
7014: 20 20      JR           NZ,$7036
7016: 54         LD           D,H
7017: 68         LD           L,B
7018: 65         LD           H,L
7019: 20 4D      JR           NZ,$7068
701B: 6F         LD           L,A
701C: 62         LD           H,D
701D: 6C         LD           L,H
701E: 69         LD           L,C
701F: 6E         LD           L,(HL)
7020: 73         LD           (HL),E
7021: 20 63      JR           NZ,$7086
7023: 61         LD           H,C
7024: 6D         LD           L,L
7025: 65         LD           H,L
7026: 74         LD           (HL),H
7027: 6F         LD           L,A
7028: 20 74      JR           NZ,$709E
702A: 68         LD           L,B
702B: 65         LD           H,L
702C: 20 76      JR           NZ,$70A4
702E: 69         LD           L,C
702F: 6C         LD           L,H
7030: 6C         LD           L,H
7031: 61         LD           H,C
7032: 67         LD           H,A
7033: 65         LD           H,L
7034: 21 20 59   LD           HL,$5920
7037: 65         LD           H,L
7038: 61         LD           H,C
7039: 68         LD           L,B
703A: 2C         INC         L
703B: 20 74      JR           NZ,$70B1
703D: 68         LD           L,B
703E: 61         LD           H,C
703F: 74         LD           (HL),H
7040: 5E         LD           E,(HL)
7041: 73         LD           (HL),E
7042: 20 20      JR           NZ,$7064
7044: 20 20      JR           NZ,$7066
7046: 72         LD           (HL),D
7047: 69         LD           L,C
7048: 67         LD           H,A
7049: 68         LD           L,B
704A: 74         LD           (HL),H
704B: 21 20 20   LD           HL,$2020
704E: 41         LD           B,C
704F: 20 77      JR           NZ,$70C8
7051: 68         LD           L,B
7052: 6F         LD           L,A
7053: 6C         LD           L,H
7054: 65         LD           H,L
7055: 20 67      JR           NZ,$70BE
7057: 61         LD           H,C
7058: 6E         LD           L,(HL)
7059: 67         LD           H,A
705A: 20 6F      JR           NZ,$70CB
705C: 66         LD           H,(HL)
705D: 20 4D      JR           NZ,$70AC
705F: 6F         LD           L,A
7060: 62         LD           H,D
7061: 6C         LD           L,H
7062: 69         LD           L,C
7063: 6E         LD           L,(HL)
7064: 73         LD           (HL),E
7065: 21 54 68   LD           HL,$6854
7068: 65         LD           H,L
7069: 6E         LD           L,(HL)
706A: 2E 2E      LD           L,$2E
706C: 2E 20      LD           L,$20
706E: 49         LD           C,C
706F: 74         LD           (HL),H
7070: 5E         LD           E,(HL)
7071: 73         LD           (HL),E
7072: 20 66      JR           NZ,$70DA
7074: 6F         LD           L,A
7075: 72         LD           (HL),D
7076: 72         LD           (HL),D
7077: 65         LD           H,L
7078: 61         LD           H,C
7079: 6C         LD           L,H
707A: 21 20 20   LD           HL,$2020
707D: 54         LD           D,H
707E: 68         LD           L,B
707F: 65         LD           H,L
7080: 79         LD           A,C
7081: 20 61      JR           NZ,$70E4
7083: 6C         LD           L,H
7084: 6C         LD           L,H
7085: 20 77      JR           NZ,$70FE
7087: 65         LD           H,L
7088: 6E         LD           L,(HL)
7089: 74         LD           (HL),H
708A: 20 74      JR           NZ,$7100
708C: 6F         LD           L,A
708D: 20 74      JR           NZ,$7103
708F: 68         LD           L,B
7090: 65         LD           H,L
7091: 20 20      JR           NZ,$70B3
7093: 20 20      JR           NZ,$70B5
7095: 20 68      JR           NZ,$70FF
7097: 6F         LD           L,A
7098: 75         LD           (HL),L
7099: 73         LD           (HL),E
709A: 65         LD           H,L
709B: 2E 2E      LD           L,$2E
709D: 2E 20      LD           L,$20
709F: 20 59      JR           NZ,$70FA
70A1: 65         LD           H,L
70A2: 61         LD           H,C
70A3: 68         LD           L,B
70A4: 2C         INC         L
70A5: 20 74      JR           NZ,$711B
70A7: 68         LD           L,B
70A8: 61         LD           H,C
70A9: 74         LD           (HL),H
70AA: 20 68      JR           NZ,$7114
70AC: 6F         LD           L,A
70AD: 75         LD           (HL),L
70AE: 73         LD           (HL),E
70AF: 65         LD           H,L
70B0: 2C         INC         L
70B1: 20 61      JR           NZ,$7114
70B3: 6E         LD           L,(HL)
70B4: 64         LD           H,H
70B5: 20 74      JR           NZ,$712B
70B7: 68         LD           L,B
70B8: 65         LD           H,L
70B9: 6E         LD           L,(HL)
70BA: 20 74      JR           NZ,$7130
70BC: 68         LD           L,B
70BD: 65         LD           H,L
70BE: 79         LD           A,C
70BF: 20 64      JR           NZ,$7125
70C1: 69         LD           L,C
70C2: 64         LD           H,H
70C3: 20 20      JR           NZ,$70E5
70C5: 20 73      JR           NZ,$713A
70C7: 6F         LD           L,A
70C8: 6D         LD           L,L
70C9: 65         LD           H,L
70CA: 74         LD           (HL),H
70CB: 68         LD           L,B
70CC: 69         LD           L,C
70CD: 6E         LD           L,(HL)
70CE: 67         LD           H,A
70CF: 20 61      JR           NZ,$7132
70D1: 74         LD           (HL),H
70D2: 20 42      JR           NZ,$7116
70D4: 6F         LD           L,A
70D5: 77         LD           (HL),A
70D6: 57         LD           D,A
70D7: 6F         LD           L,A
70D8: 77         LD           (HL),A
70D9: 5E         LD           E,(HL)
70DA: 73         LD           (HL),E
70DB: 20 68      JR           NZ,$7145
70DD: 6F         LD           L,A
70DE: 75         LD           (HL),L
70DF: 73         LD           (HL),E
70E0: 65         LD           H,L
70E1: 21 21 20   LD           HL,$2021
70E4: 20 20      JR           NZ,$7106
70E6: 49         LD           C,C
70E7: 74         LD           (HL),H
70E8: 20 77      JR           NZ,$7161
70EA: 61         LD           H,C
70EB: 73         LD           (HL),E
70EC: 20 61      JR           NZ,$714F
70EE: 20 72      JR           NZ,$7162
70F0: 65         LD           H,L
70F1: 61         LD           H,C
70F2: 6C         LD           L,H
70F3: 6C         LD           L,H
70F4: 79         LD           A,C
70F5: 20 62      JR           NZ,$7159
70F7: 61         LD           H,C
70F8: 64         LD           H,H
70F9: 20 73      JR           NZ,$716E
70FB: 63         LD           H,E
70FC: 65         LD           H,L
70FD: 6E         LD           L,(HL)
70FE: 65         LD           H,L
70FF: 2C         INC         L
7100: 20 77      JR           NZ,$7179
7102: 69         LD           L,C
7103: 74         LD           (HL),H
7104: 68         LD           L,B
7105: 20 74      JR           NZ,$717B
7107: 68         LD           L,B
7108: 65         LD           H,L
7109: 20 4D      JR           NZ,$7158
710B: 2D         DEC         L
710C: 6D         LD           L,L
710D: 2D         DEC         L
710E: 6D         LD           L,L
710F: 6F         LD           L,A
7110: 62         LD           H,D
7111: 6C         LD           L,H
7112: 69         LD           L,C
7113: 6E         LD           L,(HL)
7114: 73         LD           (HL),E
7115: 21 53 6F   LD           HL,$6F53
7118: 2C         INC         L
7119: 20 49      JR           NZ,$7164
711B: 20 6D      JR           NZ,$718A
711D: 65         LD           H,L
711E: 61         LD           H,C
711F: 6E         LD           L,(HL)
7120: 2C         INC         L
7121: 20 61      JR           NZ,$7184
7123: 68         LD           L,B
7124: 68         LD           L,B
7125: 21 2E 2E   LD           HL,$2E2E
7128: 2E 20      LD           L,$20
712A: 2E 2E      LD           L,$2E
712C: 2E 20      LD           L,$20
712E: 2E 2E      LD           L,$2E
7130: 2E 20      LD           L,$20
7132: 2E 2E      LD           L,$2E
7134: 2E 20      LD           L,$20
7136: 2E 2E      LD           L,$2E
7138: 2E 20      LD           L,$20
713A: 2E 2E      LD           L,$2E
713C: 2E 20      LD           L,$20
713E: 2E 2E      LD           L,$2E
7140: 2E 20      LD           L,$20
7142: 2E 2E      LD           L,$2E
7144: 2E 20      LD           L,$20
7146: 49         LD           C,C
7147: 74         LD           (HL),H
7148: 20 6D      JR           NZ,$71B7
714A: 69         LD           L,C
714B: 67         LD           H,A
714C: 68         LD           L,B
714D: 74         LD           (HL),H
714E: 20 62      JR           NZ,$71B2
7150: 65         LD           H,L
7151: 20 20      JR           NZ,$7173
7153: 20 20      JR           NZ,$7175
7155: 20 66      JR           NZ,$71BD
7157: 61         LD           H,C
7158: 73         LD           (HL),E
7159: 74         LD           (HL),H
715A: 65         LD           H,L
715B: 72         LD           (HL),D
715C: 20 74      JR           NZ,$71D2
715E: 6F         LD           L,A
715F: 20 66      JR           NZ,$71C7
7161: 69         LD           L,C
7162: 6E         LD           L,(HL)
7163: 64         LD           H,H
7164: 20 20      JR           NZ,$7186
7166: 6F         LD           L,A
7167: 75         LD           (HL),L
7168: 74         LD           (HL),H
7169: 20 66      JR           NZ,$71D1
716B: 6F         LD           L,A
716C: 72         LD           (HL),D
716D: 20 79      JR           NZ,$71E8
716F: 6F         LD           L,A
7170: 75         LD           (HL),L
7171: 72         LD           (HL),D
7172: 73         LD           (HL),E
7173: 65         LD           H,L
7174: 6C         LD           L,H
7175: 66         LD           H,(HL)
7176: 77         LD           (HL),A
7177: 68         LD           L,B
7178: 61         LD           H,C
7179: 74         LD           (HL),H
717A: 20 68      JR           NZ,$71E4
717C: 61         LD           H,C
717D: 70         LD           (HL),B
717E: 70         LD           (HL),B
717F: 65         LD           H,L
7180: 6E         LD           L,(HL)
7181: 65         LD           H,L
7182: 64         LD           H,H
7183: 21 FF 49   LD           HL,$49FF
7186: 20 66      JR           NZ,$71EE
7188: 6F         LD           L,A
7189: 75         LD           (HL),L
718A: 6E         LD           L,(HL)
718B: 64         LD           H,H
718C: 20 61      JR           NZ,$71EF
718E: 20 67      JR           NZ,$71F7
7190: 6F         LD           L,A
7191: 6F         LD           L,A
7192: 64         LD           H,H
7193: 20 20      JR           NZ,$71B5
7195: 69         LD           L,C
7196: 74         LD           (HL),H
7197: 65         LD           H,L
7198: 6D         LD           L,L
7199: 20 77      JR           NZ,$7212
719B: 61         LD           H,C
719C: 73         LD           (HL),E
719D: 68         LD           L,B
719E: 65         LD           H,L
719F: 64         LD           H,H
71A0: 20 75      JR           NZ,$7217
71A2: 70         LD           (HL),B
71A3: 20 20      JR           NZ,$71C5
71A5: 6F         LD           L,A
71A6: 6E         LD           L,(HL)
71A7: 20 74      JR           NZ,$721D
71A9: 68         LD           L,B
71AA: 65         LD           H,L
71AB: 20 62      JR           NZ,$720F
71AD: 65         LD           H,L
71AE: 61         LD           H,C
71AF: 63         LD           H,E
71B0: 68         LD           L,B
71B1: 2E 2E      LD           L,$2E
71B3: 2E 20      LD           L,$20
71B5: 49         LD           C,C
71B6: 5E         LD           E,(HL)
71B7: 6C         LD           L,H
71B8: 6C         LD           L,H
71B9: 20 74      JR           NZ,$722F
71BB: 72         LD           (HL),D
71BC: 61         LD           H,C
71BD: 64         LD           H,H
71BE: 65         LD           H,L
71BF: 20 69      JR           NZ,$722A
71C1: 74         LD           (HL),H
71C2: 20 74      JR           NZ,$7238
71C4: 6F         LD           L,A
71C5: 79         LD           A,C
71C6: 6F         LD           L,A
71C7: 75         LD           (HL),L
71C8: 20 66      JR           NZ,$7230
71CA: 6F         LD           L,A
71CB: 72         LD           (HL),D
71CC: 20 77      JR           NZ,$7245
71CE: 68         LD           L,B
71CF: 61         LD           H,C
71D0: 74         LD           (HL),H
71D1: 20 79      JR           NZ,$724C
71D3: 6F         LD           L,A
71D4: 75         LD           (HL),L
71D5: 68         LD           L,B
71D6: 61         LD           H,C
71D7: 76         HALT
71D8: 65         LD           H,L
71D9: 20 69      JR           NZ,$7244
71DB: 6E         LD           L,(HL)
71DC: 20 79      JR           NZ,$7257
71DE: 6F         LD           L,A
71DF: 75         LD           (HL),L
71E0: 72         LD           (HL),D
71E1: 20 42      JR           NZ,$7225
71E3: 20 20      JR           NZ,$7205
71E5: 42         LD           B,D
71E6: 75         LD           (HL),L
71E7: 74         LD           (HL),H
71E8: 74         LD           (HL),H
71E9: 6F         LD           L,A
71EA: 6E         LD           L,(HL)
71EB: 2E 2E      LD           L,$2E
71ED: 2E 20      LD           L,$20
71EF: 20 20      JR           NZ,$7211
71F1: 20 20      JR           NZ,$7213
71F3: 20 20      JR           NZ,$7215
71F5: 20 20      JR           NZ,$7217
71F7: 20 20      JR           NZ,$7219
71F9: 4F         LD           C,A
71FA: 6B         LD           L,E
71FB: 61         LD           H,C
71FC: 79         LD           A,C
71FD: 20 4E      JR           NZ,$724D
71FF: 6F         LD           L,A
7200: FE 4F      CP           $4F
7202: 6B         LD           L,E
7203: 61         LD           H,C
7204: 79         LD           A,C
7205: 2C         INC         L
7206: 20 6C      JR           NZ,$7274
7208: 65         LD           H,L
7209: 74         LD           (HL),H
720A: 5E         LD           E,(HL)
720B: 73         LD           (HL),E
720C: 20 64      JR           NZ,$7272
720E: 6F         LD           L,A
720F: 20 20      JR           NZ,$7231
7211: 69         LD           L,C
7212: 74         LD           (HL),H
7213: 21 20 20   LD           HL,$2020
7216: 57         LD           D,A
7217: 68         LD           L,B
7218: 65         LD           H,L
7219: 6E         LD           L,(HL)
721A: 20 79      JR           NZ,$7295
721C: 6F         LD           L,A
721D: 75         LD           (HL),L
721E: 20 20      JR           NZ,$7240
7220: 20 64      JR           NZ,$7286
7222: 6F         LD           L,A
7223: 6E         LD           L,(HL)
7224: 5E         LD           E,(HL)
7225: 74         LD           (HL),H
7226: 20 77      JR           NZ,$729F
7228: 61         LD           H,C
7229: 6E         LD           L,(HL)
722A: 74         LD           (HL),H
722B: 20 74      JR           NZ,$72A1
722D: 68         LD           L,B
722E: 65         LD           H,L
722F: 20 20      JR           NZ,$7251
7231: 42         LD           B,D
7232: 6F         LD           L,A
7233: 6F         LD           L,A
7234: 6D         LD           L,L
7235: 65         LD           H,L
7236: 72         LD           (HL),D
7237: 61         LD           H,C
7238: 6E         LD           L,(HL)
7239: 67         LD           H,A
723A: 20 61      JR           NZ,$729D
723C: 6E         LD           L,(HL)
723D: 79         LD           A,C
723E: 20 20      JR           NZ,$7260
7240: 20 6D      JR           NZ,$72AF
7242: 6F         LD           L,A
7243: 72         LD           (HL),D
7244: 65         LD           H,L
7245: 2C         INC         L
7246: 20 63      JR           NZ,$72AB
7248: 6F         LD           L,A
7249: 6D         LD           L,L
724A: 65         LD           H,L
724B: 20 62      JR           NZ,$72AF
724D: 61         LD           H,C
724E: 63         LD           H,E
724F: 6B         LD           L,E
7250: 21 FF 4F   LD           HL,$4FFF
7253: 68         LD           L,B
7254: 2C         INC         L
7255: 20 79      JR           NZ,$72D0
7257: 65         LD           H,L
7258: 61         LD           H,C
7259: 68         LD           L,B
725A: 2C         INC         L
725B: 20 75      JR           NZ,$72D2
725D: 68         LD           L,B
725E: 2E 2E      LD           L,$2E
7260: 2E 20      LD           L,$20
7262: 6F         LD           L,A
7263: 6B         LD           L,E
7264: 61         LD           H,C
7265: 79         LD           A,C
7266: 2C         INC         L
7267: 20 77      JR           NZ,$72E0
7269: 68         LD           L,B
726A: 61         LD           H,C
726B: 74         LD           (HL),H
726C: 65         LD           H,L
726D: 76         HALT
726E: 65         LD           H,L
726F: 72         LD           (HL),D
7270: 2E FF      LD           L,$FF
7272: 59         LD           E,C
7273: 6F         LD           L,A
7274: 75         LD           (HL),L
7275: 20 67      JR           NZ,$72DE
7277: 6F         LD           L,A
7278: 74         LD           (HL),H
7279: 20 74      JR           NZ,$72EF
727B: 68         LD           L,B
727C: 65         LD           H,L
727D: 20 20      JR           NZ,$729F
727F: 20 20      JR           NZ,$72A1
7281: 20 42      JR           NZ,$72C5
7283: 6F         LD           L,A
7284: 6F         LD           L,A
7285: 6D         LD           L,L
7286: 65         LD           H,L
7287: 72         LD           (HL),D
7288: 61         LD           H,C
7289: 6E         LD           L,(HL)
728A: 67         LD           H,A
728B: 20 69      JR           NZ,$72F6
728D: 6E         LD           L,(HL)
728E: 20 20      JR           NZ,$72B0
7290: 20 20      JR           NZ,$72B2
7292: 65         LD           H,L
7293: 78         LD           A,B
7294: 63         LD           H,E
7295: 68         LD           L,B
7296: 61         LD           H,C
7297: 6E         LD           L,(HL)
7298: 67         LD           H,A
7299: 65         LD           H,L
729A: 20 66      JR           NZ,$7302
729C: 6F         LD           L,A
729D: 72         LD           (HL),D
729E: 20 74      JR           NZ,$7314
72A0: 68         LD           L,B
72A1: 65         LD           H,L
72A2: 69         LD           L,C
72A3: 74         LD           (HL),H
72A4: 65         LD           H,L
72A5: 6D         LD           L,L
72A6: 20 79      JR           NZ,$7321
72A8: 6F         LD           L,A
72A9: 75         LD           (HL),L
72AA: 20 68      JR           NZ,$7314
72AC: 61         LD           H,C
72AD: 64         LD           H,H
72AE: 2E FF      LD           L,$FF
72B0: 47         LD           B,A
72B1: 69         LD           L,C
72B2: 76         HALT
72B3: 65         LD           H,L
72B4: 20 6D      JR           NZ,$7323
72B6: 65         LD           H,L
72B7: 20 62      JR           NZ,$731B
72B9: 61         LD           H,C
72BA: 63         LD           H,E
72BB: 6B         LD           L,E
72BC: 20 74      JR           NZ,$7332
72BE: 68         LD           L,B
72BF: 65         LD           H,L
72C0: 42         LD           B,D
72C1: 6F         LD           L,A
72C2: 6F         LD           L,A
72C3: 6D         LD           L,L
72C4: 65         LD           H,L
72C5: 72         LD           (HL),D
72C6: 61         LD           H,C
72C7: 6E         LD           L,(HL)
72C8: 67         LD           H,A
72C9: 2C         INC         L
72CA: 20 49      JR           NZ,$7315
72CC: 20 62      JR           NZ,$7330
72CE: 65         LD           H,L
72CF: 67         LD           H,A
72D0: 79         LD           A,C
72D1: 6F         LD           L,A
72D2: 75         LD           (HL),L
72D3: 21 20 49   LD           HL,$4920
72D6: 5E         LD           E,(HL)
72D7: 6C         LD           L,H
72D8: 6C         LD           L,H
72D9: 20 72      JR           NZ,$734D
72DB: 65         LD           H,L
72DC: 74         LD           (HL),H
72DD: 75         LD           (HL),L
72DE: 72         LD           (HL),D
72DF: 6E         LD           L,(HL)
72E0: 74         LD           (HL),H
72E1: 68         LD           L,B
72E2: 65         LD           H,L
72E3: 20 69      JR           NZ,$734E
72E5: 74         LD           (HL),H
72E6: 65         LD           H,L
72E7: 6D         LD           L,L
72E8: 20 79      JR           NZ,$7363
72EA: 6F         LD           L,A
72EB: 75         LD           (HL),L
72EC: 20 20      JR           NZ,$730E
72EE: 20 20      JR           NZ,$7310
72F0: 67         LD           H,A
72F1: 61         LD           H,C
72F2: 76         HALT
72F3: 65         LD           H,L
72F4: 20 74      JR           NZ,$736A
72F6: 6F         LD           L,A
72F7: 20 6D      JR           NZ,$7366
72F9: 65         LD           H,L
72FA: 21 20 20   LD           HL,$2020
72FD: 20 20      JR           NZ,$731F
72FF: 20 20      JR           NZ,$7321
7301: 20 20      JR           NZ,$7323
7303: 20 4F      JR           NZ,$7354
7305: 6B         LD           L,E
7306: 61         LD           H,C
7307: 79         LD           A,C
7308: 20 4E      JR           NZ,$7358
730A: 6F         LD           L,A
730B: 74         LD           (HL),H
730C: 20 4E      JR           NZ,$735C
730E: 6F         LD           L,A
730F: 77         LD           (HL),A
7310: FE 54      CP           $54
7312: 68         LD           L,B
7313: 65         LD           H,L
7314: 20 69      JR           NZ,$737F
7316: 74         LD           (HL),H
7317: 65         LD           H,L
7318: 6D         LD           L,L
7319: 20 63      JR           NZ,$737E
731B: 61         LD           H,C
731C: 6D         LD           L,L
731D: 65         LD           H,L
731E: 20 20      JR           NZ,$7340
7320: 20 62      JR           NZ,$7384
7322: 61         LD           H,C
7323: 63         LD           H,E
7324: 6B         LD           L,E
7325: 20 74      JR           NZ,$739B
7327: 6F         LD           L,A
7328: 20 79      JR           NZ,$73A3
732A: 6F         LD           L,A
732B: 75         LD           (HL),L
732C: 2E 20      LD           L,$20
732E: 59         LD           E,C
732F: 6F         LD           L,A
7330: 75         LD           (HL),L
7331: 72         LD           (HL),D
7332: 65         LD           H,L
7333: 74         LD           (HL),H
7334: 75         LD           (HL),L
7335: 72         LD           (HL),D
7336: 6E         LD           L,(HL)
7337: 65         LD           H,L
7338: 64         LD           H,H
7339: 20 74      JR           NZ,$73AF
733B: 68         LD           L,B
733C: 65         LD           H,L
733D: 20 20      JR           NZ,$735F
733F: 20 20      JR           NZ,$7361
7341: 42         LD           B,D
7342: 6F         LD           L,A
7343: 6F         LD           L,A
7344: 6D         LD           L,L
7345: 65         LD           H,L
7346: 72         LD           (HL),D
7347: 61         LD           H,C
7348: 6E         LD           L,(HL)
7349: 67         LD           H,A
734A: 2E FF      LD           L,$FF
734C: 41         LD           B,C
734D: 68         LD           L,B
734E: 2E 2E      LD           L,$2E
7350: 2E 20      LD           L,$20
7352: 44         LD           B,H
7353: 6F         LD           L,A
7354: 6E         LD           L,(HL)
7355: 5E         LD           E,(HL)
7356: 74         LD           (HL),H
7357: 20 67      JR           NZ,$73C0
7359: 69         LD           L,C
735A: 76         HALT
735B: 65         LD           H,L
735C: 6D         LD           L,L
735D: 65         LD           H,L
735E: 20 74      JR           NZ,$73D4
7360: 68         LD           L,B
7361: 61         LD           H,C
7362: 74         LD           (HL),H
7363: 20 69      JR           NZ,$73CE
7365: 74         LD           (HL),H
7366: 65         LD           H,L
7367: 6D         LD           L,L
7368: 2E 2E      LD           L,$2E
736A: 2E 20      LD           L,$20
736C: 48         LD           C,B
736D: 6F         LD           L,A
736E: 77         LD           (HL),A
736F: 20 61      JR           NZ,$73D2
7371: 62         LD           H,D
7372: 6F         LD           L,A
7373: 75         LD           (HL),L
7374: 74         LD           (HL),H
7375: 20 73      JR           NZ,$73EA
7377: 6F         LD           L,A
7378: 6D         LD           L,L
7379: 65         LD           H,L
737A: 2D         DEC         L
737B: 20 74      JR           NZ,$73F1
737D: 68         LD           L,B
737E: 69         LD           L,C
737F: 6E         LD           L,(HL)
7380: 67         LD           H,A
7381: 20 65      JR           NZ,$73E8
7383: 6C         LD           L,H
7384: 73         LD           (HL),E
7385: 65         LD           H,L
7386: 3F         CCF
7387: FF         RST         0X38
7388: 48         LD           C,B
7389: 75         LD           (HL),L
738A: 6E         LD           L,(HL)
738B: 68         LD           L,B
738C: 3F         CCF
738D: 20 20      JR           NZ,$73AF
738F: 41         LD           B,C
7390: 20 6B      JR           NZ,$73FD
7392: 65         LD           H,L
7393: 79         LD           A,C
7394: 68         LD           L,B
7395: 6F         LD           L,A
7396: 6C         LD           L,H
7397: 65         LD           H,L
7398: 68         LD           L,B
7399: 65         LD           H,L
739A: 72         LD           (HL),D
739B: 65         LD           H,L
739C: 3F         CCF
739D: 20 20      JR           NZ,$73BF
739F: 49         LD           C,C
73A0: 74         LD           (HL),H
73A1: 20 73      JR           NZ,$7416
73A3: 61         LD           H,C
73A4: 79         LD           A,C
73A5: 73         LD           (HL),E
73A6: 2C         INC         L
73A7: 20 5E      JR           NZ,$7407
73A9: 54         LD           D,H
73AA: 61         LD           H,C
73AB: 6C         LD           L,H
73AC: 65         LD           H,L
73AD: 20 4B      JR           NZ,$73FA
73AF: 65         LD           H,L
73B0: 79         LD           A,C
73B1: 68         LD           L,B
73B2: 6F         LD           L,A
73B3: 6C         LD           L,H
73B4: 65         LD           H,L
73B5: 5E         LD           E,(HL)
73B6: FF         RST         0X38
73B7: 48         LD           C,B
73B8: 75         LD           (HL),L
73B9: 6E         LD           L,(HL)
73BA: 68         LD           L,B
73BB: 3F         CCF
73BC: 20 20      JR           NZ,$73DE
73BE: 41         LD           B,C
73BF: 20 6B      JR           NZ,$742C
73C1: 65         LD           H,L
73C2: 79         LD           A,C
73C3: 68         LD           L,B
73C4: 6F         LD           L,A
73C5: 6C         LD           L,H
73C6: 65         LD           H,L
73C7: 68         LD           L,B
73C8: 65         LD           H,L
73C9: 72         LD           (HL),D
73CA: 65         LD           H,L
73CB: 3F         CCF
73CC: 20 20      JR           NZ,$73EE
73CE: 49         LD           C,C
73CF: 74         LD           (HL),H
73D0: 20 73      JR           NZ,$7445
73D2: 61         LD           H,C
73D3: 79         LD           A,C
73D4: 73         LD           (HL),E
73D5: 2C         INC         L
73D6: 20 5E      JR           NZ,$7436
73D8: 53         LD           D,E
73D9: 6C         LD           L,H
73DA: 69         LD           L,C
73DB: 6D         LD           L,L
73DC: 65         LD           H,L
73DD: 20 4B      JR           NZ,$742A
73DF: 65         LD           H,L
73E0: 79         LD           A,C
73E1: 68         LD           L,B
73E2: 6F         LD           L,A
73E3: 6C         LD           L,H
73E4: 65         LD           H,L
73E5: 5E         LD           E,(HL)
73E6: FF         RST         0X38
73E7: 48         LD           C,B
73E8: 75         LD           (HL),L
73E9: 6E         LD           L,(HL)
73EA: 68         LD           L,B
73EB: 3F         CCF
73EC: 20 20      JR           NZ,$740E
73EE: 41         LD           B,C
73EF: 20 6B      JR           NZ,$745C
73F1: 65         LD           H,L
73F2: 79         LD           A,C
73F3: 68         LD           L,B
73F4: 6F         LD           L,A
73F5: 6C         LD           L,H
73F6: 65         LD           H,L
73F7: 68         LD           L,B
73F8: 65         LD           H,L
73F9: 72         LD           (HL),D
73FA: 65         LD           H,L
73FB: 3F         CCF
73FC: 20 20      JR           NZ,$741E
73FE: 49         LD           C,C
73FF: 74         LD           (HL),H
7400: 20 73      JR           NZ,$7475
7402: 61         LD           H,C
7403: 79         LD           A,C
7404: 73         LD           (HL),E
7405: 2C         INC         L
7406: 20 5E      JR           NZ,$7466
7408: 41         LD           B,C
7409: 6E         LD           L,(HL)
740A: 67         LD           H,A
740B: 6C         LD           L,H
740C: 65         LD           H,L
740D: 72         LD           (HL),D
740E: 20 4B      JR           NZ,$745B
7410: 65         LD           H,L
7411: 79         LD           A,C
7412: 68         LD           L,B
7413: 6F         LD           L,A
7414: 6C         LD           L,H
7415: 65         LD           H,L
7416: 5E         LD           E,(HL)
7417: FF         RST         0X38
7418: 48         LD           C,B
7419: 75         LD           (HL),L
741A: 6E         LD           L,(HL)
741B: 68         LD           L,B
741C: 3F         CCF
741D: 20 20      JR           NZ,$743F
741F: 41         LD           B,C
7420: 20 6B      JR           NZ,$748D
7422: 65         LD           H,L
7423: 79         LD           A,C
7424: 68         LD           L,B
7425: 6F         LD           L,A
7426: 6C         LD           L,H
7427: 65         LD           H,L
7428: 68         LD           L,B
7429: 65         LD           H,L
742A: 72         LD           (HL),D
742B: 65         LD           H,L
742C: 3F         CCF
742D: 20 20      JR           NZ,$744F
742F: 49         LD           C,C
7430: 74         LD           (HL),H
7431: 20 73      JR           NZ,$74A6
7433: 61         LD           H,C
7434: 79         LD           A,C
7435: 73         LD           (HL),E
7436: 2C         INC         L
7437: 20 5E      JR           NZ,$7497
7439: 42         LD           B,D
743A: 69         LD           L,C
743B: 72         LD           (HL),D
743C: 64         LD           H,H
743D: 20 4B      JR           NZ,$748A
743F: 65         LD           H,L
7440: 79         LD           A,C
7441: 68         LD           L,B
7442: 6F         LD           L,A
7443: 6C         LD           L,H
7444: 65         LD           H,L
7445: 5E         LD           E,(HL)
7446: FF         RST         0X38
7447: 48         LD           C,B
7448: 75         LD           (HL),L
7449: 6E         LD           L,(HL)
744A: 68         LD           L,B
744B: 3F         CCF
744C: 20 20      JR           NZ,$746E
744E: 41         LD           B,C
744F: 20 6B      JR           NZ,$74BC
7451: 65         LD           H,L
7452: 79         LD           A,C
7453: 68         LD           L,B
7454: 6F         LD           L,A
7455: 6C         LD           L,H
7456: 65         LD           H,L
7457: 68         LD           L,B
7458: 65         LD           H,L
7459: 72         LD           (HL),D
745A: 65         LD           H,L
745B: 3F         CCF
745C: 20 20      JR           NZ,$747E
745E: 49         LD           C,C
745F: 74         LD           (HL),H
7460: 20 73      JR           NZ,$74D5
7462: 61         LD           H,C
7463: 79         LD           A,C
7464: 73         LD           (HL),E
7465: 2C         INC         L
7466: 20 5E      JR           NZ,$74C6
7468: 46         LD           B,(HL)
7469: 61         LD           H,C
746A: 63         LD           H,E
746B: 65         LD           H,L
746C: 20 4B      JR           NZ,$74B9
746E: 65         LD           H,L
746F: 79         LD           A,C
7470: 68         LD           L,B
7471: 6F         LD           L,A
7472: 6C         LD           L,H
7473: 65         LD           H,L
7474: 5E         LD           E,(HL)
7475: FF         RST         0X38
7476: 53         LD           D,E
7477: 6F         LD           L,A
7478: 6D         LD           L,L
7479: 65         LD           H,L
747A: 62         LD           H,D
747B: 6F         LD           L,A
747C: 64         LD           H,H
747D: 79         LD           A,C
747E: 2C         INC         L
747F: 20 48      JR           NZ,$74C9
7481: 45         LD           B,L
7482: 4C         LD           C,H
7483: 50         LD           D,B
7484: 21 FF 48   LD           HL,$48FF
7487: 65         LD           H,L
7488: 79         LD           A,C
7489: 21 20 20   LD           HL,$2020
748C: 23         INC         HL
748D: 23         INC         HL
748E: 23         INC         HL
748F: 23         INC         HL
7490: 23         INC         HL
7491: 21 20 20   LD           HL,$2020
7494: 20 20      JR           NZ,$74B6
7496: 53         LD           D,E
7497: 6F         LD           L,A
7498: 6D         LD           L,L
7499: 65         LD           H,L
749A: 20 6D      JR           NZ,$7509
749C: 6F         LD           L,A
749D: 6E         LD           L,(HL)
749E: 73         LD           (HL),E
749F: 74         LD           (HL),H
74A0: 65         LD           H,L
74A1: 72         LD           (HL),D
74A2: 73         LD           (HL),E
74A3: 20 20      JR           NZ,$74C5
74A5: 20 70      JR           NZ,$7517
74A7: 75         LD           (HL),L
74A8: 74         LD           (HL),H
74A9: 20 6D      JR           NZ,$7518
74AB: 65         LD           H,L
74AC: 20 75      JR           NZ,$7523
74AE: 70         LD           (HL),B
74AF: 20 68      JR           NZ,$7519
74B1: 65         LD           H,L
74B2: 72         LD           (HL),D
74B3: 65         LD           H,L
74B4: 21 20 57   LD           HL,$5720
74B7: 68         LD           L,B
74B8: 61         LD           H,C
74B9: 74         LD           (HL),H
74BA: 20 73      JR           NZ,$752F
74BC: 68         LD           L,B
74BD: 6F         LD           L,A
74BE: 75         LD           (HL),L
74BF: 6C         LD           L,H
74C0: 64         LD           H,H
74C1: 20 49      JR           NZ,$750C
74C3: 20 20      JR           NZ,$74E5
74C5: 20 64      JR           NZ,$752B
74C7: 6F         LD           L,A
74C8: 3F         CCF
74C9: 21 20 20   LD           HL,$2020
74CC: 49         LD           C,C
74CD: 5E         LD           E,(HL)
74CE: 6D         LD           L,L
74CF: 20 61      JR           NZ,$7532
74D1: 66         LD           H,(HL)
74D2: 72         LD           (HL),D
74D3: 61         LD           H,C
74D4: 69         LD           L,C
74D5: 64         LD           H,H
74D6: 6F         LD           L,A
74D7: 66         LD           H,(HL)
74D8: 20 68      JR           NZ,$7542
74DA: 65         LD           H,L
74DB: 69         LD           L,C
74DC: 67         LD           H,A
74DD: 68         LD           L,B
74DE: 74         LD           (HL),H
74DF: 73         LD           (HL),E
74E0: 21 21 FF   LD           HL,$FF21
74E3: 59         LD           E,C
74E4: 6F         LD           L,A
74E5: 77         LD           (HL),A
74E6: 21 20 20   LD           HL,$2020
74E9: 54         LD           D,H
74EA: 68         LD           L,B
74EB: 61         LD           H,C
74EC: 74         LD           (HL),H
74ED: 20 77      JR           NZ,$7566
74EF: 61         LD           H,C
74F0: 73         LD           (HL),E
74F1: 20 61      JR           NZ,$7554
74F3: 73         LD           (HL),E
74F4: 75         LD           (HL),L
74F5: 72         LD           (HL),D
74F6: 70         LD           (HL),B
74F7: 72         LD           (HL),D
74F8: 69         LD           L,C
74F9: 73         LD           (HL),E
74FA: 65         LD           H,L
74FB: 21 20 23   LD           HL,$2320
74FE: 23         INC         HL
74FF: 23         INC         HL
7500: 23         INC         HL
7501: 23         INC         HL
7502: 2C         INC         L
7503: 74         LD           (HL),H
7504: 68         LD           L,B
7505: 61         LD           H,C
7506: 6E         LD           L,(HL)
7507: 6B         LD           L,E
7508: 20 79      JR           NZ,$7583
750A: 6F         LD           L,A
750B: 75         LD           (HL),L
750C: 21 FF 2E   LD           HL,$2EFF
750F: 2E 2E      LD           L,$2E
7511: 20 2E      JR           NZ,$7541
7513: 2E 2E      LD           L,$2E
7515: 20 2E      JR           NZ,$7545
7517: 2E 2E      LD           L,$2E
7519: 20 2E      JR           NZ,$7549
751B: 2E 2E      LD           L,$2E
751D: 20 2E      JR           NZ,$754D
751F: 2E 2E      LD           L,$2E
7521: 20 2E      JR           NZ,$7551
7523: 2E 2E      LD           L,$2E
7525: 20 2E      JR           NZ,$7555
7527: 2E 2E      LD           L,$2E
7529: 20 2E      JR           NZ,$7559
752B: 2E 2E      LD           L,$2E
752D: 20 53      JR           NZ,$7582
752F: 61         LD           H,C
7530: 79         LD           A,C
7531: 2E 2E      LD           L,$2E
7533: 2E 20      LD           L,$20
7535: 23         INC         HL
7536: 23         INC         HL
7537: 23         INC         HL
7538: 23         INC         HL
7539: 23         INC         HL
753A: 2E 2E      LD           L,$2E
753C: 2E 20      LD           L,$20
753E: FF         RST         0X38
753F: 55         LD           D,L
7540: 68         LD           L,B
7541: 68         LD           L,B
7542: 2E 2E      LD           L,$2E
7544: 2E 20      LD           L,$20
7546: 49         LD           C,C
7547: 20 64      JR           NZ,$75AD
7549: 6F         LD           L,A
754A: 6E         LD           L,(HL)
754B: 5E         LD           E,(HL)
754C: 74         LD           (HL),H
754D: 20 20      JR           NZ,$756F
754F: 6B         LD           L,E
7550: 6E         LD           L,(HL)
7551: 6F         LD           L,A
7552: 77         LD           (HL),A
7553: 20 68      JR           NZ,$75BD
7555: 6F         LD           L,A
7556: 77         LD           (HL),A
7557: 20 74      JR           NZ,$75CD
7559: 6F         LD           L,A
755A: 20 73      JR           NZ,$75CF
755C: 61         LD           H,C
755D: 79         LD           A,C
755E: 20 74      JR           NZ,$75D4
7560: 68         LD           L,B
7561: 69         LD           L,C
7562: 73         LD           (HL),E
7563: 2E 2E      LD           L,$2E
7565: 2E 20      LD           L,$20
7567: 62         LD           H,D
7568: 75         LD           (HL),L
7569: 74         LD           (HL),H
756A: 2E 2E      LD           L,$2E
756C: 2E FF      LD           L,$FF
756E: 48         LD           C,B
756F: 75         LD           (HL),L
7570: 6E         LD           L,(HL)
7571: 68         LD           L,B
7572: 3F         CCF
7573: 21 20 20   LD           HL,$2020
7576: 54         LD           D,H
7577: 61         LD           H,C
7578: 72         LD           (HL),D
7579: 69         LD           L,C
757A: 6E         LD           L,(HL)
757B: 3F         CCF
757C: 3F         CCF
757D: 21 2E 2E   LD           HL,$2E2E
7580: 2E 20      LD           L,$20
7582: 2E 2E      LD           L,$2E
7584: 2E 20      LD           L,$20
7586: 2E 2E      LD           L,$2E
7588: 2E 20      LD           L,$20
758A: 2E 2E      LD           L,$2E
758C: 2E 20      LD           L,$20
758E: 55         LD           D,L
758F: 68         LD           L,B
7590: 2E 2E      LD           L,$2E
7592: 2E 20      LD           L,$20
7594: 4E         LD           C,(HL)
7595: 65         LD           H,L
7596: 76         HALT
7597: 65         LD           H,L
7598: 72         LD           (HL),D
7599: 6D         LD           L,L
759A: 69         LD           L,C
759B: 6E         LD           L,(HL)
759C: 64         LD           H,H
759D: 2C         INC         L
759E: 49         LD           C,C
759F: 2E 2E      LD           L,$2E
75A1: 2E 20      LD           L,$20
75A3: 49         LD           C,C
75A4: 20 67      JR           NZ,$760D
75A6: 6F         LD           L,A
75A7: 74         LD           (HL),H
75A8: 74         LD           (HL),H
75A9: 61         LD           H,C
75AA: 20 67      JR           NZ,$7613
75AC: 6F         LD           L,A
75AD: 21 FF 4D   LD           HL,$4DFF
75B0: 41         LD           B,C
75B1: 41         LD           B,C
75B2: 41         LD           B,C
75B3: 41         LD           B,C
75B4: 41         LD           B,C
75B5: 41         LD           B,C
75B6: 41         LD           B,C
75B7: 52         LD           D,D
75B8: 49         LD           C,C
75B9: 4E         LD           C,(HL)
75BA: 4E         LD           C,(HL)
75BB: 4E         LD           C,(HL)
75BC: 4E         LD           C,(HL)
75BD: 21 21 FF   LD           HL,$FF21
75C0: 5E         LD           E,(HL)
75C1: 42         LD           B,D
75C2: 52         LD           D,D
75C3: 52         LD           D,D
75C4: 49         LD           C,C
75C5: 4E         LD           C,(HL)
75C6: 47         LD           B,A
75C7: 21 20 42   LD           HL,$4220
75CA: 52         LD           D,D
75CB: 52         LD           D,D
75CC: 49         LD           C,C
75CD: 4E         LD           C,(HL)
75CE: 47         LD           B,A
75CF: 21 54 68   LD           HL,$6854
75D2: 69         LD           L,C
75D3: 73         LD           (HL),E
75D4: 20 69      JR           NZ,$763F
75D6: 73         LD           (HL),E
75D7: 20 55      JR           NZ,$762E
75D9: 6C         LD           L,H
75DA: 72         LD           (HL),D
75DB: 69         LD           L,C
75DC: 72         LD           (HL),D
75DD: 61         LD           H,C
75DE: 21 20 4F   LD           HL,$4F20
75E1: 68         LD           L,B
75E2: 2C         INC         L
75E3: 20 49      JR           NZ,$762E
75E5: 20 68      JR           NZ,$764F
75E7: 65         LD           H,L
75E8: 61         LD           H,C
75E9: 72         LD           (HL),D
75EA: 64         LD           H,H
75EB: 20 66      JR           NZ,$7653
75ED: 72         LD           (HL),D
75EE: 6F         LD           L,A
75EF: 6D         LD           L,L
75F0: 67         LD           H,A
75F1: 72         LD           (HL),D
75F2: 61         LD           H,C
75F3: 6E         LD           L,(HL)
75F4: 64         LD           H,H
75F5: 6D         LD           L,L
75F6: 61         LD           H,C
75F7: 20 74      JR           NZ,$766D
75F9: 68         LD           L,B
75FA: 61         LD           H,C
75FB: 74         LD           (HL),H
75FC: 20 20      JR           NZ,$761E
75FE: 20 20      JR           NZ,$7620
7600: 74         LD           (HL),H
7601: 68         LD           L,B
7602: 65         LD           H,L
7603: 72         LD           (HL),D
7604: 65         LD           H,L
7605: 20 69      JR           NZ,$7670
7607: 73         LD           (HL),E
7608: 20 73      JR           NZ,$767D
760A: 6F         LD           L,A
760B: 6D         LD           L,L
760C: 65         LD           H,L
760D: 2D         DEC         L
760E: 20 20      JR           NZ,$7630
7610: 74         LD           (HL),H
7611: 68         LD           L,B
7612: 69         LD           L,C
7613: 6E         LD           L,(HL)
7614: 67         LD           H,A
7615: 20 68      JR           NZ,$767F
7617: 69         LD           L,C
7618: 64         LD           H,H
7619: 64         LD           H,H
761A: 65         LD           H,L
761B: 6E         LD           L,(HL)
761C: 20 20      JR           NZ,$763E
761E: 20 20      JR           NZ,$7640
7620: 62         LD           H,D
7621: 65         LD           H,L
7622: 68         LD           L,B
7623: 69         LD           L,C
7624: 6E         LD           L,(HL)
7625: 64         LD           H,H
7626: 20 74      JR           NZ,$769C
7628: 68         LD           L,B
7629: 65         LD           H,L
762A: 20 66      JR           NZ,$7692
762C: 61         LD           H,C
762D: 6C         LD           L,H
762E: 6C         LD           L,H
762F: 73         LD           (HL),E
7630: 69         LD           L,C
7631: 6E         LD           L,(HL)
7632: 20 74      JR           NZ,$76A8
7634: 68         LD           L,B
7635: 65         LD           H,L
7636: 20 54      JR           NZ,$768C
7638: 61         LD           H,C
7639: 6C         LD           L,H
763A: 20 54      JR           NZ,$7690
763C: 61         LD           H,C
763D: 6C         LD           L,H
763E: 20 20      JR           NZ,$7660
7640: 4D         LD           C,L
7641: 6F         LD           L,A
7642: 75         LD           (HL),L
7643: 6E         LD           L,(HL)
7644: 74         LD           (HL),H
7645: 61         LD           H,C
7646: 69         LD           L,C
7647: 6E         LD           L,(HL)
7648: 73         LD           (HL),E
7649: 2E 20      LD           L,$20
764B: 20 44      JR           NZ,$7691
764D: 6F         LD           L,A
764E: 65         LD           H,L
764F: 73         LD           (HL),E
7650: 74         LD           (HL),H
7651: 68         LD           L,B
7652: 61         LD           H,C
7653: 74         LD           (HL),H
7654: 20 68      JR           NZ,$76BE
7656: 65         LD           H,L
7657: 6C         LD           L,H
7658: 70         LD           (HL),B
7659: 3F         CCF
765A: 20 20      JR           NZ,$767C
765C: 42         LD           B,D
765D: 79         LD           A,C
765E: 65         LD           H,L
765F: 21 43 4C   LD           HL,$4C43
7662: 49         LD           C,C
7663: 43         LD           B,E
7664: 4B         LD           C,E
7665: 21 5E FF   LD           HL,$FF5E
7668: 5E         LD           E,(HL)
7669: 42         LD           B,D
766A: 52         LD           D,D
766B: 52         LD           D,D
766C: 49         LD           C,C
766D: 4E         LD           C,(HL)
766E: 47         LD           B,A
766F: 21 20 42   LD           HL,$4220
7672: 52         LD           D,D
7673: 52         LD           D,D
7674: 49         LD           C,C
7675: 4E         LD           C,(HL)
7676: 47         LD           B,A
7677: 21 55 6C   LD           HL,$6C55
767A: 72         LD           (HL),D
767B: 69         LD           L,C
767C: 72         LD           (HL),D
767D: 61         LD           H,C
767E: 20 68      JR           NZ,$76E8
7680: 65         LD           H,L
7681: 72         LD           (HL),D
7682: 65         LD           H,L
7683: 2E 2E      LD           L,$2E
7685: 2E 20      LD           L,$20
7687: 20 59      JR           NZ,$76E2
7689: 65         LD           H,L
768A: 73         LD           (HL),E
768B: 2C         INC         L
768C: 20 77      JR           NZ,$7705
768E: 68         LD           L,B
768F: 65         LD           H,L
7690: 6E         LD           L,(HL)
7691: 20 49      JR           NZ,$76DC
7693: 20 77      JR           NZ,$770C
7695: 61         LD           H,C
7696: 73         LD           (HL),E
7697: 20 6A      JR           NZ,$7703
7699: 75         LD           (HL),L
769A: 73         LD           (HL),E
769B: 74         LD           (HL),H
769C: 20 61      JR           NZ,$76FF
769E: 20 6C      JR           NZ,$770C
76A0: 61         LD           H,C
76A1: 64         LD           H,H
76A2: 2C         INC         L
76A3: 20 49      JR           NZ,$76EE
76A5: 20 20      JR           NZ,$76C7
76A7: 20 72      JR           NZ,$771B
76A9: 65         LD           H,L
76AA: 63         LD           H,E
76AB: 61         LD           H,C
76AC: 6C         LD           L,H
76AD: 6C         LD           L,H
76AE: 20 73      JR           NZ,$7723
76B0: 65         LD           H,L
76B1: 65         LD           H,L
76B2: 69         LD           L,C
76B3: 6E         LD           L,(HL)
76B4: 67         LD           H,A
76B5: 20 61      JR           NZ,$7718
76B7: 20 68      JR           NZ,$7721
76B9: 69         LD           L,C
76BA: 67         LD           H,A
76BB: 68         LD           L,B
76BC: 20 74      JR           NZ,$7732
76BE: 6F         LD           L,A
76BF: 77         LD           (HL),A
76C0: 65         LD           H,L
76C1: 72         LD           (HL),D
76C2: 20 69      JR           NZ,$772D
76C4: 6E         LD           L,(HL)
76C5: 20 20      JR           NZ,$76E7
76C7: 20 74      JR           NZ,$773D
76C9: 68         LD           L,B
76CA: 65         LD           H,L
76CB: 20 6D      JR           NZ,$773A
76CD: 6F         LD           L,A
76CE: 75         LD           (HL),L
76CF: 6E         LD           L,(HL)
76D0: 74         LD           (HL),H
76D1: 61         LD           H,C
76D2: 69         LD           L,C
76D3: 6E         LD           L,(HL)
76D4: 73         LD           (HL),E
76D5: 21 20 20   LD           HL,$2020
76D8: 59         LD           E,C
76D9: 6F         LD           L,A
76DA: 75         LD           (HL),L
76DB: 20 73      JR           NZ,$7750
76DD: 68         LD           L,B
76DE: 6F         LD           L,A
76DF: 75         LD           (HL),L
76E0: 6C         LD           L,H
76E1: 64         LD           H,H
76E2: 20 67      JR           NZ,$774B
76E4: 6F         LD           L,A
76E5: 20 20      JR           NZ,$7707
76E7: 20 74      JR           NZ,$775D
76E9: 68         LD           L,B
76EA: 65         LD           H,L
76EB: 72         LD           (HL),D
76EC: 65         LD           H,L
76ED: 21 20 20   LD           HL,$2020
76F0: 49         LD           C,C
76F1: 73         LD           (HL),E
76F2: 20 74      JR           NZ,$7768
76F4: 68         LD           L,B
76F5: 61         LD           H,C
76F6: 74         LD           (HL),H
76F7: 20 68      JR           NZ,$7761
76F9: 65         LD           H,L
76FA: 6C         LD           L,H
76FB: 70         LD           (HL),B
76FC: 66         LD           H,(HL)
76FD: 75         LD           (HL),L
76FE: 6C         LD           L,H
76FF: 20 66      JR           NZ,$7767
7701: 6F         LD           L,A
7702: 72         LD           (HL),D
7703: 20 79      JR           NZ,$777E
7705: 6F         LD           L,A
7706: 75         LD           (HL),L
7707: 3F         CCF
7708: 42         LD           B,D
7709: 79         LD           A,C
770A: 65         LD           H,L
770B: 21 20 43   LD           HL,$4320
770E: 4C         LD           C,H
770F: 49         LD           C,C
7710: 43         LD           B,E
7711: 4B         LD           C,E
7712: 21 5E FF   LD           HL,$FF5E
7715: 5E         LD           E,(HL)
7716: 42         LD           B,D
7717: 52         LD           D,D
7718: 52         LD           D,D
7719: 49         LD           C,C
771A: 4E         LD           C,(HL)
771B: 47         LD           B,A
771C: 21 20 42   LD           HL,$4220
771F: 52         LD           D,D
7720: 52         LD           D,D
7721: 49         LD           C,C
7722: 4E         LD           C,(HL)
7723: 47         LD           B,A
7724: 21 48 65   LD           HL,$6548
7727: 6C         LD           L,H
7728: 6C         LD           L,H
7729: 6F         LD           L,A
772A: 2C         INC         L
772B: 20 74      JR           NZ,$77A1
772D: 68         LD           L,B
772E: 69         LD           L,C
772F: 73         LD           (HL),E
7730: 20 69      JR           NZ,$779B
7732: 73         LD           (HL),E
7733: 20 20      JR           NZ,$7755
7735: 55         LD           D,L
7736: 6C         LD           L,H
7737: 72         LD           (HL),D
7738: 69         LD           L,C
7739: 72         LD           (HL),D
773A: 61         LD           H,C
773B: 20 73      JR           NZ,$77B0
773D: 70         LD           (HL),B
773E: 65         LD           H,L
773F: 61         LD           H,C
7740: 6B         LD           L,E
7741: 69         LD           L,C
7742: 6E         LD           L,(HL)
7743: 67         LD           H,A
7744: 21 23 23   LD           HL,$2323
7747: 23         INC         HL
7748: 23         INC         HL
7749: 23         INC         HL
774A: 2C         INC         L
774B: 20 69      JR           NZ,$77B6
774D: 74         LD           (HL),H
774E: 5E         LD           E,(HL)
774F: 73         LD           (HL),E
7750: 20 74      JR           NZ,$77C6
7752: 69         LD           L,C
7753: 6D         LD           L,L
7754: 65         LD           H,L
7755: 66         LD           H,(HL)
7756: 6F         LD           L,A
7757: 72         LD           (HL),D
7758: 20 79      JR           NZ,$77D3
775A: 6F         LD           L,A
775B: 75         LD           (HL),L
775C: 20 74      JR           NZ,$77D2
775E: 6F         LD           L,A
775F: 20 66      JR           NZ,$77C7
7761: 61         LD           H,C
7762: 63         LD           H,E
7763: 65         LD           H,L
7764: 20 74      JR           NZ,$77DA
7766: 68         LD           L,B
7767: 65         LD           H,L
7768: 20 45      JR           NZ,$77AF
776A: 67         LD           H,A
776B: 67         LD           H,A
776C: 20 6F      JR           NZ,$77DD
776E: 6E         LD           L,(HL)
776F: 20 4D      JR           NZ,$77BE
7771: 74         LD           (HL),H
7772: 2E 20      LD           L,$20
7774: 20 54      JR           NZ,$77CA
7776: 61         LD           H,C
7777: 6D         LD           L,L
7778: 61         LD           H,C
7779: 72         LD           (HL),D
777A: 61         LD           H,C
777B: 6E         LD           L,(HL)
777C: 63         LD           H,E
777D: 68         LD           L,B
777E: 21 20 20   LD           HL,$2020
7781: 42         LD           B,D
7782: 65         LD           H,L
7783: 20 20      JR           NZ,$77A5
7785: 63         LD           H,E
7786: 61         LD           H,C
7787: 72         LD           (HL),D
7788: 65         LD           H,L
7789: 66         LD           H,(HL)
778A: 75         LD           (HL),L
778B: 6C         LD           L,H
778C: 2C         INC         L
778D: 20 23      JR           NZ,$77B2
778F: 23         INC         HL
7790: 23         INC         HL
7791: 23         INC         HL
7792: 23         INC         HL
7793: 21 20 42   LD           HL,$4220
7796: 79         LD           A,C
7797: 65         LD           H,L
7798: 21 20 20   LD           HL,$2020
779B: 43         LD           B,E
779C: 4C         LD           C,H
779D: 49         LD           C,C
779E: 43         LD           B,E
779F: 4B         LD           C,E
77A0: 21 5E FF   LD           HL,$FF5E
77A3: 5E         LD           E,(HL)
77A4: 42         LD           B,D
77A5: 52         LD           D,D
77A6: 52         LD           D,D
77A7: 49         LD           C,C
77A8: 4E         LD           C,(HL)
77A9: 47         LD           B,A
77AA: 21 20 42   LD           HL,$4220
77AD: 52         LD           D,D
77AE: 52         LD           D,D
77AF: 49         LD           C,C
77B0: 4E         LD           C,(HL)
77B1: 47         LD           B,A
77B2: 21 54 68   LD           HL,$6854
77B5: 69         LD           L,C
77B6: 73         LD           (HL),E
77B7: 20 69      JR           NZ,$7822
77B9: 73         LD           (HL),E
77BA: 20 55      JR           NZ,$7811
77BC: 6C         LD           L,H
77BD: 72         LD           (HL),D
77BE: 69         LD           L,C
77BF: 72         LD           (HL),D
77C0: 61         LD           H,C
77C1: 21 20 59   LD           HL,$5920
77C4: 6F         LD           L,A
77C5: 75         LD           (HL),L
77C6: 5E         LD           E,(HL)
77C7: 72         LD           (HL),D
77C8: 65         LD           H,L
77C9: 20 6C      JR           NZ,$7837
77CB: 6F         LD           L,A
77CC: 73         LD           (HL),E
77CD: 74         LD           (HL),H
77CE: 20 69      JR           NZ,$7839
77D0: 6E         LD           L,(HL)
77D1: 20 20      JR           NZ,$77F3
77D3: 74         LD           (HL),H
77D4: 68         LD           L,B
77D5: 65         LD           H,L
77D6: 20 45      JR           NZ,$781D
77D8: 67         LD           H,A
77D9: 67         LD           H,A
77DA: 3F         CCF
77DB: 20 20      JR           NZ,$77FD
77DD: 48         LD           C,B
77DE: 6D         LD           L,L
77DF: 6D         LD           L,L
77E0: 6D         LD           L,L
77E1: 6D         LD           L,L
77E2: 2E 4E      LD           L,$4E
77E4: 6F         LD           L,A
77E5: 20 73      JR           NZ,$785A
77E7: 69         LD           L,C
77E8: 72         LD           (HL),D
77E9: 2C         INC         L
77EA: 20 49      JR           NZ,$7835
77EC: 20 63      JR           NZ,$7851
77EE: 61         LD           H,C
77EF: 6E         LD           L,(HL)
77F0: 5E         LD           E,(HL)
77F1: 74         LD           (HL),H
77F2: 20 68      JR           NZ,$785C
77F4: 65         LD           H,L
77F5: 6C         LD           L,H
77F6: 70         LD           (HL),B
77F7: 20 79      JR           NZ,$7872
77F9: 6F         LD           L,A
77FA: 75         LD           (HL),L
77FB: 20 6F      JR           NZ,$786C
77FD: 6E         LD           L,(HL)
77FE: 20 74      JR           NZ,$7874
7800: 68         LD           L,B
7801: 61         LD           H,C
7802: 74         LD           (HL),H
7803: 6F         LD           L,A
7804: 6E         LD           L,(HL)
7805: 65         LD           H,L
7806: 2E 20      LD           L,$20
7808: 20 48      JR           NZ,$7852
780A: 6F         LD           L,A
780B: 77         LD           (HL),A
780C: 20 61      JR           NZ,$786F
780E: 62         LD           H,D
780F: 6F         LD           L,A
7810: 75         LD           (HL),L
7811: 74         LD           (HL),H
7812: 20 74      JR           NZ,$7888
7814: 68         LD           L,B
7815: 65         LD           H,L
7816: 20 6C      JR           NZ,$7884
7818: 69         LD           L,C
7819: 62         LD           H,D
781A: 72         LD           (HL),D
781B: 61         LD           H,C
781C: 72         LD           (HL),D
781D: 79         LD           A,C
781E: 3F         CCF
781F: 20 20      JR           NZ,$7841
7821: 20 20      JR           NZ,$7843
7823: 41         LD           B,C
7824: 6E         LD           L,(HL)
7825: 64         LD           H,H
7826: 20 68      JR           NZ,$7890
7828: 65         LD           H,L
7829: 79         LD           A,C
782A: 2C         INC         L
782B: 20 64      JR           NZ,$7891
782D: 6F         LD           L,A
782E: 6E         LD           L,(HL)
782F: 5E         LD           E,(HL)
7830: 74         LD           (HL),H
7831: 20 20      JR           NZ,$7853
7833: 73         LD           (HL),E
7834: 74         LD           (HL),H
7835: 6F         LD           L,A
7836: 70         LD           (HL),B
7837: 20 63      JR           NZ,$789C
7839: 61         LD           H,C
783A: 6C         LD           L,H
783B: 6C         LD           L,H
783C: 69         LD           L,C
783D: 6E         LD           L,(HL)
783E: 67         LD           H,A
783F: 20 6D      JR           NZ,$78AE
7841: 65         LD           H,L
7842: 20 62      JR           NZ,$78A6
7844: 65         LD           H,L
7845: 63         LD           H,E
7846: 61         LD           H,C
7847: 75         LD           (HL),L
7848: 73         LD           (HL),E
7849: 65         LD           H,L
784A: 20 49      JR           NZ,$7895
784C: 20 64      JR           NZ,$78B2
784E: 69         LD           L,C
784F: 64         LD           H,H
7850: 6E         LD           L,(HL)
7851: 5E         LD           E,(HL)
7852: 74         LD           (HL),H
7853: 6B         LD           L,E
7854: 6E         LD           L,(HL)
7855: 6F         LD           L,A
7856: 77         LD           (HL),A
7857: 20 6F      JR           NZ,$78C8
7859: 6E         LD           L,(HL)
785A: 65         LD           H,L
785B: 20 6C      JR           NZ,$78C9
785D: 69         LD           L,C
785E: 74         LD           (HL),H
785F: 74         LD           (HL),H
7860: 6C         LD           L,H
7861: 65         LD           H,L
7862: 20 61      JR           NZ,$78C5
7864: 6E         LD           L,(HL)
7865: 73         LD           (HL),E
7866: 77         LD           (HL),A
7867: 65         LD           H,L
7868: 72         LD           (HL),D
7869: 21 20 20   LD           HL,$2020
786C: 43         LD           B,E
786D: 4C         LD           C,H
786E: 49         LD           C,C
786F: 43         LD           B,E
7870: 4B         LD           C,E
7871: 21 5E FF   LD           HL,$FF5E
7874: 5E         LD           E,(HL)
7875: 42         LD           B,D
7876: 52         LD           D,D
7877: 52         LD           D,D
7878: 49         LD           C,C
7879: 4E         LD           C,(HL)
787A: 47         LD           B,A
787B: 21 20 42   LD           HL,$4220
787E: 52         LD           D,D
787F: 52         LD           D,D
7880: 49         LD           C,C
7881: 4E         LD           C,(HL)
7882: 47         LD           B,A
7883: 21 55 6C   LD           HL,$6C55
7886: 72         LD           (HL),D
7887: 69         LD           L,C
7888: 72         LD           (HL),D
7889: 61         LD           H,C
788A: 20 61      JR           NZ,$78ED
788C: 74         LD           (HL),H
788D: 20 79      JR           NZ,$7908
788F: 6F         LD           L,A
7890: 75         LD           (HL),L
7891: 72         LD           (HL),D
7892: 20 20      JR           NZ,$78B4
7894: 73         LD           (HL),E
7895: 65         LD           H,L
7896: 72         LD           (HL),D
7897: 76         HALT
7898: 69         LD           L,C
7899: 63         LD           H,E
789A: 65         LD           H,L
789B: 21 20 20   LD           HL,$2020
789E: 4F         LD           C,A
789F: 68         LD           L,B
78A0: 3F         CCF
78A1: 20 20      JR           NZ,$78C3
78A3: 20 59      JR           NZ,$78FE
78A5: 6F         LD           L,A
78A6: 75         LD           (HL),L
78A7: 20 73      JR           NZ,$791C
78A9: 68         LD           L,B
78AA: 6F         LD           L,A
78AB: 75         LD           (HL),L
78AC: 6C         LD           L,H
78AD: 64         LD           H,H
78AE: 20 74      JR           NZ,$7924
78B0: 61         LD           H,C
78B1: 6B         LD           L,E
78B2: 65         LD           H,L
78B3: 20 42      JR           NZ,$78F7
78B5: 6F         LD           L,A
78B6: 77         LD           (HL),A
78B7: 57         LD           D,A
78B8: 6F         LD           L,A
78B9: 77         LD           (HL),A
78BA: 20 68      JR           NZ,$7924
78BC: 6F         LD           L,A
78BD: 6D         LD           L,L
78BE: 65         LD           H,L
78BF: 20 6E      JR           NZ,$792F
78C1: 6F         LD           L,A
78C2: 77         LD           (HL),A
78C3: 2C         INC         L
78C4: 4D         LD           C,L
78C5: 61         LD           H,C
78C6: 64         LD           H,H
78C7: 61         LD           H,C
78C8: 6D         LD           L,L
78C9: 20 4D      JR           NZ,$7918
78CB: 65         LD           H,L
78CC: 6F         LD           L,A
78CD: 77         LD           (HL),A
78CE: 4D         LD           C,L
78CF: 65         LD           H,L
78D0: 6F         LD           L,A
78D1: 77         LD           (HL),A
78D2: 20 20      JR           NZ,$78F4
78D4: 77         LD           (HL),A
78D5: 6F         LD           L,A
78D6: 75         LD           (HL),L
78D7: 6C         LD           L,H
78D8: 64         LD           H,H
78D9: 20 61      JR           NZ,$793C
78DB: 70         LD           (HL),B
78DC: 70         LD           (HL),B
78DD: 72         LD           (HL),D
78DE: 65         LD           H,L
78DF: 63         LD           H,E
78E0: 69         LD           L,C
78E1: 61         LD           H,C
78E2: 74         LD           (HL),H
78E3: 65         LD           H,L
78E4: 69         LD           L,C
78E5: 74         LD           (HL),H
78E6: 21 20 42   LD           HL,$4220
78E9: 79         LD           A,C
78EA: 65         LD           H,L
78EB: 21 20 43   LD           HL,$4320
78EE: 4C         LD           C,H
78EF: 49         LD           C,C
78F0: 43         LD           B,E
78F1: 4B         LD           C,E
78F2: 21 5E FF   LD           HL,$FF5E
78F5: 5E         LD           E,(HL)
78F6: 42         LD           B,D
78F7: 52         LD           D,D
78F8: 52         LD           D,D
78F9: 49         LD           C,C
78FA: 4E         LD           C,(HL)
78FB: 47         LD           B,A
78FC: 21 20 42   LD           HL,$4220
78FF: 52         LD           D,D
7900: 52         LD           D,D
7901: 49         LD           C,C
7902: 4E         LD           C,(HL)
7903: 47         LD           B,A
7904: 21 59 65   LD           HL,$6559
7907: 61         LD           H,C
7908: 68         LD           L,B
7909: 2C         INC         L
790A: 20 74      JR           NZ,$7980
790C: 68         LD           L,B
790D: 69         LD           L,C
790E: 73         LD           (HL),E
790F: 20 69      JR           NZ,$797A
7911: 73         LD           (HL),E
7912: 20 20      JR           NZ,$7934
7914: 20 55      JR           NZ,$796B
7916: 6C         LD           L,H
7917: 72         LD           (HL),D
7918: 69         LD           L,C
7919: 72         LD           (HL),D
791A: 61         LD           H,C
791B: 21 20 20   LD           HL,$2020
791E: 59         LD           E,C
791F: 6F         LD           L,A
7920: 75         LD           (HL),L
7921: 20 61      JR           NZ,$7984
7923: 72         LD           (HL),D
7924: 65         LD           H,L
7925: 73         LD           (HL),E
7926: 74         LD           (HL),H
7927: 61         LD           H,C
7928: 72         LD           (HL),D
7929: 74         LD           (HL),H
792A: 69         LD           L,C
792B: 6E         LD           L,(HL)
792C: 67         LD           H,A
792D: 20 74      JR           NZ,$79A3
792F: 6F         LD           L,A
7930: 20 6C      JR           NZ,$799E
7932: 69         LD           L,C
7933: 6B         LD           L,E
7934: 65         LD           H,L
7935: 74         LD           (HL),H
7936: 6F         LD           L,A
7937: 20 6D      JR           NZ,$79A6
7939: 75         LD           (HL),L
793A: 73         LD           (HL),E
793B: 69         LD           L,C
793C: 63         LD           H,E
793D: 2C         INC         L
793E: 20 65      JR           NZ,$79A5
7940: 68         LD           L,B
7941: 3F         CCF
7942: 20 20      JR           NZ,$7964
7944: 20 57      JR           NZ,$799D
7946: 65         LD           H,L
7947: 6C         LD           L,H
7948: 6C         LD           L,H
7949: 2C         INC         L
794A: 20 61      JR           NZ,$79AD
794C: 20 66      JR           NZ,$79B4
794E: 72         LD           (HL),D
794F: 6F         LD           L,A
7950: 67         LD           H,A
7951: 20 20      JR           NZ,$7973
7953: 20 20      JR           NZ,$7975
7955: 6E         LD           L,(HL)
7956: 61         LD           H,C
7957: 6D         LD           L,L
7958: 65         LD           H,L
7959: 64         LD           H,H
795A: 20 4D      JR           NZ,$79A9
795C: 61         LD           H,C
795D: 6D         LD           L,L
795E: 75         LD           (HL),L
795F: 2C         INC         L
7960: 20 77      JR           NZ,$79D9
7962: 68         LD           L,B
7963: 6F         LD           L,A
7964: 20 6C      JR           NZ,$79D2
7966: 69         LD           L,C
7967: 76         HALT
7968: 65         LD           H,L
7969: 73         LD           (HL),E
796A: 20 69      JR           NZ,$79D5
796C: 6E         LD           L,(HL)
796D: 20 74      JR           NZ,$79E3
796F: 68         LD           L,B
7970: 65         LD           H,L
7971: 20 20      JR           NZ,$7993
7973: 20 20      JR           NZ,$7995
7975: 53         LD           D,E
7976: 69         LD           L,C
7977: 67         LD           H,A
7978: 6E         LD           L,(HL)
7979: 70         LD           (HL),B
797A: 6F         LD           L,A
797B: 73         LD           (HL),E
797C: 74         LD           (HL),H
797D: 20 4D      JR           NZ,$79CC
797F: 61         LD           H,C
7980: 7A         LD           A,D
7981: 65         LD           H,L
7982: 2C         INC         L
7983: 20 20      JR           NZ,$79A5
7985: 6D         LD           L,L
7986: 69         LD           L,C
7987: 67         LD           H,A
7988: 68         LD           L,B
7989: 74         LD           (HL),H
798A: 20 6B      JR           NZ,$79F7
798C: 6E         LD           L,(HL)
798D: 6F         LD           L,A
798E: 77         LD           (HL),A
798F: 20 73      JR           NZ,$7A04
7991: 6F         LD           L,A
7992: 6D         LD           L,L
7993: 65         LD           H,L
7994: 20 6E      JR           NZ,$7A04
7996: 65         LD           H,L
7997: 77         LD           (HL),A
7998: 20 73      JR           NZ,$7A0D
799A: 6F         LD           L,A
799B: 6E         LD           L,(HL)
799C: 67         LD           H,A
799D: 73         LD           (HL),E
799E: 2C         INC         L
799F: 20 62      JR           NZ,$7A03
79A1: 75         LD           (HL),L
79A2: 74         LD           (HL),H
79A3: 20 20      JR           NZ,$79C5
79A5: 68         LD           L,B
79A6: 65         LD           H,L
79A7: 20 63      JR           NZ,$7A0C
79A9: 68         LD           L,B
79AA: 61         LD           H,C
79AB: 72         LD           (HL),D
79AC: 67         LD           H,A
79AD: 65         LD           H,L
79AE: 73         LD           (HL),E
79AF: 20 61      JR           NZ,$7A12
79B1: 20 6C      JR           NZ,$7A1F
79B3: 6F         LD           L,A
79B4: 74         LD           (HL),H
79B5: 74         LD           (HL),H
79B6: 6F         LD           L,A
79B7: 20 70      JR           NZ,$7A29
79B9: 6C         LD           L,H
79BA: 61         LD           H,C
79BB: 79         LD           A,C
79BC: 20 74      JR           NZ,$7A32
79BE: 68         LD           L,B
79BF: 65         LD           H,L
79C0: 6D         LD           L,L
79C1: 21 20 20   LD           HL,$2020
79C4: 20 42      JR           NZ,$7A08
79C6: 79         LD           A,C
79C7: 65         LD           H,L
79C8: 21 20 20   LD           HL,$2020
79CB: 43         LD           B,E
79CC: 4C         LD           C,H
79CD: 49         LD           C,C
79CE: 43         LD           B,E
79CF: 4B         LD           C,E
79D0: 21 5E FF   LD           HL,$FF5E
79D3: 5E         LD           E,(HL)
79D4: 42         LD           B,D
79D5: 52         LD           D,D
79D6: 52         LD           D,D
79D7: 49         LD           C,C
79D8: 4E         LD           C,(HL)
79D9: 47         LD           B,A
79DA: 21 20 42   LD           HL,$4220
79DD: 52         LD           D,D
79DE: 52         LD           D,D
79DF: 49         LD           C,C
79E0: 4E         LD           C,(HL)
79E1: 47         LD           B,A
79E2: 21 48 69   LD           HL,$6948
79E5: 2C         INC         L
79E6: 20 69      JR           NZ,$7A51
79E8: 74         LD           (HL),H
79E9: 5E         LD           E,(HL)
79EA: 73         LD           (HL),E
79EB: 20 55      JR           NZ,$7A42
79ED: 6C         LD           L,H
79EE: 72         LD           (HL),D
79EF: 69         LD           L,C
79F0: 72         LD           (HL),D
79F1: 61         LD           H,C
79F2: 21 59 6F   LD           HL,$6F59
79F5: 75         LD           (HL),L
79F6: 20 61      JR           NZ,$7A59
79F8: 72         LD           (HL),D
79F9: 65         LD           H,L
79FA: 20 64      JR           NZ,$7A60
79FC: 6F         LD           L,A
79FD: 69         LD           L,C
79FE: 6E         LD           L,(HL)
79FF: 67         LD           H,A
7A00: 20 20      JR           NZ,$7A22
7A02: 20 67      JR           NZ,$7A6B
7A04: 72         LD           (HL),D
7A05: 65         LD           H,L
7A06: 61         LD           H,C
7A07: 74         LD           (HL),H
7A08: 21 20 20   LD           HL,$2020
7A0B: 59         LD           E,C
7A0C: 6F         LD           L,A
7A0D: 75         LD           (HL),L
7A0E: 72         LD           (HL),D
7A0F: 20 20      JR           NZ,$7A31
7A11: 20 20      JR           NZ,$7A33
7A13: 65         LD           H,L
7A14: 66         LD           H,(HL)
7A15: 66         LD           H,(HL)
7A16: 6F         LD           L,A
7A17: 72         LD           (HL),D
7A18: 74         LD           (HL),H
7A19: 73         LD           (HL),E
7A1A: 20 77      JR           NZ,$7A93
7A1C: 69         LD           L,C
7A1D: 6C         LD           L,H
7A1E: 6C         LD           L,H
7A1F: 20 65      JR           NZ,$7A86
7A21: 6E         LD           L,(HL)
7A22: 64         LD           H,H
7A23: 73         LD           (HL),E
7A24: 6F         LD           L,A
7A25: 6F         LD           L,A
7A26: 6E         LD           L,(HL)
7A27: 2E 2E      LD           L,$2E
7A29: 2E 20      LD           L,$20
7A2B: 42         LD           B,D
7A2C: 79         LD           A,C
7A2D: 20 74      JR           NZ,$7AA3
7A2F: 68         LD           L,B
7A30: 65         LD           H,L
7A31: 20 20      JR           NZ,$7A53
7A33: 77         LD           (HL),A
7A34: 61         LD           H,C
7A35: 79         LD           A,C
7A36: 2C         INC         L
7A37: 20 68      JR           NZ,$7AA1
7A39: 61         LD           H,C
7A3A: 76         HALT
7A3B: 65         LD           H,L
7A3C: 20 79      JR           NZ,$7AB7
7A3E: 6F         LD           L,A
7A3F: 75         LD           (HL),L
7A40: 20 20      JR           NZ,$7A62
7A42: 20 76      JR           NZ,$7ABA
7A44: 69         LD           L,C
7A45: 73         LD           (HL),E
7A46: 69         LD           L,C
7A47: 74         LD           (HL),H
7A48: 65         LD           H,L
7A49: 64         LD           H,H
7A4A: 20 74      JR           NZ,$7AC0
7A4C: 68         LD           L,B
7A4D: 65         LD           H,L
7A4E: 20 48      JR           NZ,$7A98
7A50: 65         LD           H,L
7A51: 6E         LD           L,(HL)
7A52: 20 48      JR           NZ,$7A9C
7A54: 6F         LD           L,A
7A55: 75         LD           (HL),L
7A56: 73         LD           (HL),E
7A57: 65         LD           H,L
7A58: 20 6F      JR           NZ,$7AC9
7A5A: 6E         LD           L,(HL)
7A5B: 20 74      JR           NZ,$7AD1
7A5D: 68         LD           L,B
7A5E: 65         LD           H,L
7A5F: 20 20      JR           NZ,$7A81
7A61: 20 20      JR           NZ,$7A83
7A63: 6D         LD           L,L
7A64: 6F         LD           L,A
7A65: 75         LD           (HL),L
7A66: 6E         LD           L,(HL)
7A67: 74         LD           (HL),H
7A68: 61         LD           H,C
7A69: 69         LD           L,C
7A6A: 6E         LD           L,(HL)
7A6B: 3F         CCF
7A6C: 20 20      JR           NZ,$7A8E
7A6E: 54         LD           D,H
7A6F: 68         LD           L,B
7A70: 65         LD           H,L
7A71: 72         LD           (HL),D
7A72: 65         LD           H,L
7A73: 69         LD           L,C
7A74: 73         LD           (HL),E
7A75: 20 61      JR           NZ,$7AD8
7A77: 20 63      JR           NZ,$7ADC
7A79: 61         LD           H,C
7A7A: 76         HALT
7A7B: 65         LD           H,L
7A7C: 20 6E      JR           NZ,$7AEC
7A7E: 65         LD           H,L
7A7F: 61         LD           H,C
7A80: 72         LD           (HL),D
7A81: 62         LD           H,D
7A82: 79         LD           A,C
7A83: 77         LD           (HL),A
7A84: 69         LD           L,C
7A85: 74         LD           (HL),H
7A86: 68         LD           L,B
7A87: 20 73      JR           NZ,$7AFC
7A89: 6F         LD           L,A
7A8A: 6D         LD           L,L
7A8B: 65         LD           H,L
7A8C: 74         LD           (HL),H
7A8D: 68         LD           L,B
7A8E: 69         LD           L,C
7A8F: 6E         LD           L,(HL)
7A90: 67         LD           H,A
7A91: 20 20      JR           NZ,$7AB3
7A93: 69         LD           L,C
7A94: 6D         LD           L,L
7A95: 70         LD           (HL),B
7A96: 6F         LD           L,A
7A97: 72         LD           (HL),D
7A98: 74         LD           (HL),H
7A99: 61         LD           H,C
7A9A: 6E         LD           L,(HL)
7A9B: 74         LD           (HL),H
7A9C: 20 69      JR           NZ,$7B07
7A9E: 6E         LD           L,(HL)
7A9F: 20 69      JR           NZ,$7B0A
7AA1: 74         LD           (HL),H
7AA2: 2E 42      LD           L,$42
7AA4: 79         LD           A,C
7AA5: 65         LD           H,L
7AA6: 21 20 20   LD           HL,$2020
7AA9: 43         LD           B,E
7AAA: 4C         LD           C,H
7AAB: 49         LD           C,C
7AAC: 43         LD           B,E
7AAD: 4B         LD           C,E
7AAE: 21 5E FF   LD           HL,$FF5E
7AB1: 5E         LD           E,(HL)
7AB2: 42         LD           B,D
7AB3: 52         LD           D,D
7AB4: 52         LD           D,D
7AB5: 49         LD           C,C
7AB6: 4E         LD           C,(HL)
7AB7: 47         LD           B,A
7AB8: 21 20 42   LD           HL,$4220
7ABB: 52         LD           D,D
7ABC: 52         LD           D,D
7ABD: 49         LD           C,C
7ABE: 4E         LD           C,(HL)
7ABF: 47         LD           B,A
7AC0: 21 55 6C   LD           HL,$6C55
7AC3: 72         LD           (HL),D
7AC4: 69         LD           L,C
7AC5: 72         LD           (HL),D
7AC6: 61         LD           H,C
7AC7: 20 73      JR           NZ,$7B3C
7AC9: 70         LD           (HL),B
7ACA: 65         LD           H,L
7ACB: 61         LD           H,C
7ACC: 6B         LD           L,E
7ACD: 69         LD           L,C
7ACE: 6E         LD           L,(HL)
7ACF: 67         LD           H,A
7AD0: 21 41 72   LD           HL,$7241
7AD3: 65         LD           H,L
7AD4: 20 79      JR           NZ,$7B4F
7AD6: 6F         LD           L,A
7AD7: 75         LD           (HL),L
7AD8: 72         LD           (HL),D
7AD9: 20 65      JR           NZ,$7B40
7ADB: 6E         LD           L,(HL)
7ADC: 65         LD           H,L
7ADD: 6D         LD           L,L
7ADE: 69         LD           L,C
7ADF: 65         LD           H,L
7AE0: 73         LD           (HL),E
7AE1: 74         LD           (HL),H
7AE2: 6F         LD           L,A
7AE3: 6F         LD           L,A
7AE4: 20 73      JR           NZ,$7B59
7AE6: 74         LD           (HL),H
7AE7: 72         LD           (HL),D
7AE8: 6F         LD           L,A
7AE9: 6E         LD           L,(HL)
7AEA: 67         LD           H,A
7AEB: 20 66      JR           NZ,$7B53
7AED: 6F         LD           L,A
7AEE: 72         LD           (HL),D
7AEF: 20 20      JR           NZ,$7B11
7AF1: 79         LD           A,C
7AF2: 6F         LD           L,A
7AF3: 75         LD           (HL),L
7AF4: 3F         CCF
7AF5: 20 20      JR           NZ,$7B17
7AF7: 49         LD           C,C
7AF8: 6E         LD           L,(HL)
7AF9: 20 74      JR           NZ,$7B6F
7AFB: 68         LD           L,B
7AFC: 61         LD           H,C
7AFD: 74         LD           (HL),H
7AFE: 20 20      JR           NZ,$7B20
7B00: 20 63      JR           NZ,$7B65
7B02: 61         LD           H,C
7B03: 73         LD           (HL),E
7B04: 65         LD           H,L
7B05: 2C         INC         L
7B06: 20 79      JR           NZ,$7B81
7B08: 6F         LD           L,A
7B09: 75         LD           (HL),L
7B0A: 20 62      JR           NZ,$7B6E
7B0C: 65         LD           H,L
7B0D: 74         LD           (HL),H
7B0E: 74         LD           (HL),H
7B0F: 65         LD           H,L
7B10: 72         LD           (HL),D
7B11: 63         LD           H,E
7B12: 6F         LD           L,A
7B13: 6C         LD           L,H
7B14: 6C         LD           L,H
7B15: 65         LD           H,L
7B16: 63         LD           H,E
7B17: 74         LD           (HL),H
7B18: 20 61      JR           NZ,$7B7B
7B1A: 6C         LD           L,H
7B1B: 6C         LD           L,H
7B1C: 20 74      JR           NZ,$7B92
7B1E: 68         LD           L,B
7B1F: 65         LD           H,L
7B20: 20 53      JR           NZ,$7B75
7B22: 65         LD           H,L
7B23: 61         LD           H,C
7B24: 73         LD           (HL),E
7B25: 68         LD           L,B
7B26: 65         LD           H,L
7B27: 6C         LD           L,H
7B28: 6C         LD           L,H
7B29: 73         LD           (HL),E
7B2A: 2E 2E      LD           L,$2E
7B2C: 2E 4A      LD           L,$4A
7B2E: 75         LD           (HL),L
7B2F: 73         LD           (HL),E
7B30: 74         LD           (HL),H
7B31: 62         LD           H,D
7B32: 65         LD           H,L
7B33: 6C         LD           L,H
7B34: 69         LD           L,C
7B35: 65         LD           H,L
7B36: 76         HALT
7B37: 65         LD           H,L
7B38: 20 69      JR           NZ,$7BA3
7B3A: 6E         LD           L,(HL)
7B3B: 20 79      JR           NZ,$7BB6
7B3D: 6F         LD           L,A
7B3E: 75         LD           (HL),L
7B3F: 72         LD           (HL),D
7B40: 2D         DEC         L
7B41: 73         LD           (HL),E
7B42: 65         LD           H,L
7B43: 6C         LD           L,H
7B44: 66         LD           H,(HL)
7B45: 20 61      JR           NZ,$7BA8
7B47: 6E         LD           L,(HL)
7B48: 64         LD           H,H
7B49: 20 64      JR           NZ,$7BAF
7B4B: 6F         LD           L,A
7B4C: 20 79      JR           NZ,$7BC7
7B4E: 6F         LD           L,A
7B4F: 75         LD           (HL),L
7B50: 72         LD           (HL),D
7B51: 62         LD           H,D
7B52: 65         LD           H,L
7B53: 73         LD           (HL),E
7B54: 74         LD           (HL),H
7B55: 21 20 20   LD           HL,$2020
7B58: 43         LD           B,E
7B59: 4C         LD           C,H
7B5A: 49         LD           C,C
7B5B: 43         LD           B,E
7B5C: 4B         LD           C,E
7B5D: 21 5E FF   LD           HL,$FF5E
7B60: 5E         LD           E,(HL)
7B61: 42         LD           B,D
7B62: 52         LD           D,D
7B63: 52         LD           D,D
7B64: 49         LD           C,C
7B65: 4E         LD           C,(HL)
7B66: 47         LD           B,A
7B67: 21 20 42   LD           HL,$4220
7B6A: 52         LD           D,D
7B6B: 52         LD           D,D
7B6C: 49         LD           C,C
7B6D: 4E         LD           C,(HL)
7B6E: 47         LD           B,A
7B6F: 21 55 6C   LD           HL,$6C55
7B72: 72         LD           (HL),D
7B73: 69         LD           L,C
7B74: 72         LD           (HL),D
7B75: 61         LD           H,C
7B76: 20 68      JR           NZ,$7BE0
7B78: 65         LD           H,L
7B79: 72         LD           (HL),D
7B7A: 65         LD           H,L
7B7B: 21 20 2E   LD           HL,$2E20
7B7E: 2E 2E      LD           L,$2E
7B80: 47         LD           B,A
7B81: 6F         LD           L,A
7B82: 20 66      JR           NZ,$7BEA
7B84: 6F         LD           L,A
7B85: 72         LD           (HL),D
7B86: 20 69      JR           NZ,$7BF1
7B88: 74         LD           (HL),H
7B89: 21 20 20   LD           HL,$2020
7B8C: 20 20      JR           NZ,$7BAE
7B8E: 20 20      JR           NZ,$7BB0
7B90: 59         LD           E,C
7B91: 6F         LD           L,A
7B92: 75         LD           (HL),L
7B93: 5E         LD           E,(HL)
7B94: 72         LD           (HL),D
7B95: 65         LD           H,L
7B96: 20 61      JR           NZ,$7BF9
7B98: 6C         LD           L,H
7B99: 6D         LD           L,L
7B9A: 6F         LD           L,A
7B9B: 73         LD           (HL),E
7B9C: 74         LD           (HL),H
7B9D: 20 20      JR           NZ,$7BBF
7B9F: 20 74      JR           NZ,$7C15
7BA1: 68         LD           L,B
7BA2: 65         LD           H,L
7BA3: 72         LD           (HL),D
7BA4: 65         LD           H,L
7BA5: 21 20 49   LD           HL,$4920
7BA8: 5E         LD           E,(HL)
7BA9: 6D         LD           L,L
7BAA: 20 70      JR           NZ,$7C1C
7BAC: 75         LD           (HL),L
7BAD: 6C         LD           L,H
7BAE: 6C         LD           L,H
7BAF: 2D         DEC         L
7BB0: 69         LD           L,C
7BB1: 6E         LD           L,(HL)
7BB2: 67         LD           H,A
7BB3: 20 66      JR           NZ,$7C1B
7BB5: 6F         LD           L,A
7BB6: 72         LD           (HL),D
7BB7: 20 79      JR           NZ,$7C32
7BB9: 6F         LD           L,A
7BBA: 75         LD           (HL),L
7BBB: 21 20 20   LD           HL,$2020
7BBE: 20 20      JR           NZ,$7BE0
7BC0: 42         LD           B,D
7BC1: 79         LD           A,C
7BC2: 65         LD           H,L
7BC3: 21 20 20   LD           HL,$2020
7BC6: 43         LD           B,E
7BC7: 4C         LD           C,H
7BC8: 49         LD           C,C
7BC9: 43         LD           B,E
7BCA: 4B         LD           C,E
7BCB: 21 5E FF   LD           HL,$FF5E
7BCE: 59         LD           E,C
7BCF: 61         LD           H,C
7BD0: 72         LD           (HL),D
7BD1: 6E         LD           L,(HL)
7BD2: 61         LD           H,C
7BD3: 20 44      JR           NZ,$7C19
7BD5: 65         LD           H,L
7BD6: 73         LD           (HL),E
7BD7: 65         LD           H,L
7BD8: 72         LD           (HL),D
7BD9: 74         LD           (HL),H
7BDA: 3F         CCF
7BDB: 20 20      JR           NZ,$7BFD
7BDD: 20 54      JR           NZ,$7C33
7BDF: 68         LD           L,B
7BE0: 65         LD           H,L
7BE1: 72         LD           (HL),D
7BE2: 65         LD           H,L
7BE3: 5E         LD           E,(HL)
7BE4: 73         LD           (HL),E
7BE5: 20 61      JR           NZ,$7C48
7BE7: 20 77      JR           NZ,$7C60
7BE9: 61         LD           H,C
7BEA: 79         LD           A,C
7BEB: 20 74      JR           NZ,$7C61
7BED: 6F         LD           L,A
7BEE: 67         LD           H,A
7BEF: 65         LD           H,L
7BF0: 74         LD           (HL),H
7BF1: 20 74      JR           NZ,$7C67
7BF3: 68         LD           L,B
7BF4: 65         LD           H,L
7BF5: 72         LD           (HL),D
7BF6: 65         LD           H,L
7BF7: 20 74      JR           NZ,$7C6D
7BF9: 6F         LD           L,A
7BFA: 20 74      JR           NZ,$7C70
7BFC: 68         LD           L,B
7BFD: 65         LD           H,L
7BFE: 73         LD           (HL),E
7BFF: 6F         LD           L,A
7C00: 75         LD           (HL),L
7C01: 74         LD           (HL),H
7C02: 68         LD           L,B
7C03: 2C         INC         L
7C04: 20 62      JR           NZ,$7C68
7C06: 75         LD           (HL),L
7C07: 74         LD           (HL),H
7C08: 20 79      JR           NZ,$7C83
7C0A: 6F         LD           L,A
7C0B: 75         LD           (HL),L
7C0C: 20 20      JR           NZ,$7C2E
7C0E: 6D         LD           L,L
7C0F: 69         LD           L,C
7C10: 67         LD           H,A
7C11: 68         LD           L,B
7C12: 74         LD           (HL),H
7C13: 20 6E      JR           NZ,$7C83
7C15: 6F         LD           L,A
7C16: 74         LD           (HL),H
7C17: 20 62      JR           NZ,$7C7B
7C19: 65         LD           H,L
7C1A: 20 20      JR           NZ,$7C3C
7C1C: 20 20      JR           NZ,$7C3E
7C1E: 61         LD           H,C
7C1F: 62         LD           H,D
7C20: 6C         LD           L,H
7C21: 65         LD           H,L
7C22: 20 74      JR           NZ,$7C98
7C24: 6F         LD           L,A
7C25: 20 67      JR           NZ,$7C8E
7C27: 65         LD           H,L
7C28: 74         LD           (HL),H
7C29: 20 20      JR           NZ,$7C4B
7C2B: 20 20      JR           NZ,$7C4D
7C2D: 20 74      JR           NZ,$7CA3
7C2F: 68         LD           L,B
7C30: 72         LD           (HL),D
7C31: 6F         LD           L,A
7C32: 75         LD           (HL),L
7C33: 67         LD           H,A
7C34: 68         LD           L,B
7C35: 20 69      JR           NZ,$7CA0
7C37: 66         LD           H,(HL)
7C38: 20 74      JR           NZ,$7CAE
7C3A: 68         LD           L,B
7C3B: 61         LD           H,C
7C3C: 74         LD           (HL),H
7C3D: 20 6C      JR           NZ,$7CAB
7C3F: 61         LD           H,C
7C40: 7A         LD           A,D
7C41: 79         LD           A,C
7C42: 20 77      JR           NZ,$7CBB
7C44: 61         LD           H,C
7C45: 6C         LD           L,H
7C46: 72         LD           (HL),D
7C47: 75         LD           (HL),L
7C48: 73         LD           (HL),E
7C49: 20 69      JR           NZ,$7CB4
7C4B: 73         LD           (HL),E
7C4C: 20 20      JR           NZ,$7C6E
7C4E: 69         LD           L,C
7C4F: 6E         LD           L,(HL)
7C50: 20 74      JR           NZ,$7CC6
7C52: 68         LD           L,B
7C53: 65         LD           H,L
7C54: 20 77      JR           NZ,$7CCD
7C56: 61         LD           H,C
7C57: 79         LD           A,C
7C58: 21 FF 41   LD           HL,$41FF
7C5B: 68         LD           L,B
7C5C: 68         LD           L,B
7C5D: 68         LD           L,B
7C5E: 2E 2E      LD           L,$2E
7C60: 2E 20      LD           L,$20
7C62: 53         LD           D,E
7C63: 69         LD           L,C
7C64: 67         LD           H,A
7C65: 68         LD           L,B
7C66: 2E 2E      LD           L,$2E
7C68: 2E 20      LD           L,$20
7C6A: 4F         LD           C,A
7C6B: 6E         LD           L,(HL)
7C6C: 20 73      JR           NZ,$7CE1
7C6E: 75         LD           (HL),L
7C6F: 63         LD           H,E
7C70: 68         LD           L,B
7C71: 20 61      JR           NZ,$7CD4
7C73: 20 6E      JR           NZ,$7CE3
7C75: 69         LD           L,C
7C76: 63         LD           H,E
7C77: 65         LD           H,L
7C78: 20 20      JR           NZ,$7C9A
7C7A: 64         LD           H,H
7C7B: 61         LD           H,C
7C7C: 79         LD           A,C
7C7D: 2C         INC         L
7C7E: 20 77      JR           NZ,$7CF7
7C80: 65         LD           H,L
7C81: 20 6E      JR           NZ,$7CF1
7C83: 65         LD           H,L
7C84: 65         LD           H,L
7C85: 64         LD           H,H
7C86: 20 61      JR           NZ,$7CE9
7C88: 20 20      JR           NZ,$7CAA
7C8A: 73         LD           (HL),E
7C8B: 6F         LD           L,A
7C8C: 6E         LD           L,(HL)
7C8D: 67         LD           H,A
7C8E: 20 66      JR           NZ,$7CF6
7C90: 72         LD           (HL),D
7C91: 6F         LD           L,A
7C92: 6D         LD           L,L
7C93: 20 4D      JR           NZ,$7CE2
7C95: 61         LD           H,C
7C96: 72         LD           (HL),D
7C97: 69         LD           L,C
7C98: 6E         LD           L,(HL)
7C99: 21 FF 48   LD           HL,$48FF
7C9C: 65         LD           H,L
7C9D: 79         LD           A,C
7C9E: 21 20 44   LD           HL,$4420
7CA1: 69         LD           L,C
7CA2: 64         LD           H,H
7CA3: 20 79      JR           NZ,$7D1E
7CA5: 61         LD           H,C
7CA6: 20 6B      JR           NZ,$7D13
7CA8: 6E         LD           L,(HL)
7CA9: 6F         LD           L,A
7CAA: 77         LD           (HL),A
7CAB: 41         LD           B,C
7CAC: 6E         LD           L,(HL)
7CAD: 69         LD           L,C
7CAE: 6D         LD           L,L
7CAF: 61         LD           H,C
7CB0: 6C         LD           L,H
7CB1: 20 56      JR           NZ,$7D09
7CB3: 69         LD           L,C
7CB4: 6C         LD           L,H
7CB5: 6C         LD           L,H
7CB6: 61         LD           H,C
7CB7: 67         LD           H,A
7CB8: 65         LD           H,L
7CB9: 20 20      JR           NZ,$7CDB
7CBB: 61         LD           H,C
7CBC: 6E         LD           L,(HL)
7CBD: 64         LD           H,H
7CBE: 20 4D      JR           NZ,$7D0D
7CC0: 61         LD           H,C
7CC1: 62         LD           H,D
7CC2: 65         LD           H,L
7CC3: 20 56      JR           NZ,$7D1B
7CC5: 69         LD           L,C
7CC6: 6C         LD           L,H
7CC7: 6C         LD           L,H
7CC8: 61         LD           H,C
7CC9: 67         LD           H,A
7CCA: 65         LD           H,L
7CCB: 61         LD           H,C
7CCC: 72         LD           (HL),D
7CCD: 65         LD           H,L
7CCE: 20 73      JR           NZ,$7D43
7CD0: 69         LD           L,C
7CD1: 73         LD           (HL),E
7CD2: 74         LD           (HL),H
7CD3: 65         LD           H,L
7CD4: 72         LD           (HL),D
7CD5: 20 20      JR           NZ,$7CF7
7CD7: 20 20      JR           NZ,$7CF9
7CD9: 20 20      JR           NZ,$7CFB
7CDB: 63         LD           H,E
7CDC: 69         LD           L,C
7CDD: 74         LD           (HL),H
7CDE: 69         LD           L,C
7CDF: 65         LD           H,L
7CE0: 73         LD           (HL),E
7CE1: 3F         CCF
7CE2: 20 20      JR           NZ,$7D04
7CE4: 59         LD           E,C
7CE5: 65         LD           H,L
7CE6: 73         LD           (HL),E
7CE7: 2C         INC         L
7CE8: 20 20      JR           NZ,$7D0A
7CEA: 20 65      JR           NZ,$7D51
7CEC: 76         HALT
7CED: 65         LD           H,L
7CEE: 6E         LD           L,(HL)
7CEF: 20 74      JR           NZ,$7D65
7CF1: 68         LD           L,B
7CF2: 6F         LD           L,A
7CF3: 75         LD           (HL),L
7CF4: 67         LD           H,A
7CF5: 68         LD           L,B
7CF6: 20 74      JR           NZ,$7D6C
7CF8: 68         LD           L,B
7CF9: 65         LD           H,L
7CFA: 79         LD           A,C
7CFB: 61         LD           H,C
7CFC: 72         LD           (HL),D
7CFD: 65         LD           H,L
7CFE: 6E         LD           L,(HL)
7CFF: 5E         LD           E,(HL)
7D00: 74         LD           (HL),H
7D01: 20 6C      JR           NZ,$7D6F
7D03: 61         LD           H,C
7D04: 72         LD           (HL),D
7D05: 67         LD           H,A
7D06: 65         LD           H,L
7D07: 20 20      JR           NZ,$7D29
7D09: 20 20      JR           NZ,$7D2B
7D0B: 65         LD           H,L
7D0C: 6E         LD           L,(HL)
7D0D: 6F         LD           L,A
7D0E: 75         LD           (HL),L
7D0F: 67         LD           H,A
7D10: 68         LD           L,B
7D11: 20 74      JR           NZ,$7D87
7D13: 6F         LD           L,A
7D14: 20 62      JR           NZ,$7D78
7D16: 65         LD           H,L
7D17: 20 20      JR           NZ,$7D39
7D19: 20 20      JR           NZ,$7D3B
7D1B: 63         LD           H,E
7D1C: 61         LD           H,C
7D1D: 6C         LD           L,H
7D1E: 6C         LD           L,H
7D1F: 65         LD           H,L
7D20: 64         LD           H,H
7D21: 20 63      JR           NZ,$7D86
7D23: 69         LD           L,C
7D24: 74         LD           (HL),H
7D25: 69         LD           L,C
7D26: 65         LD           H,L
7D27: 73         LD           (HL),E
7D28: 2E 2E      LD           L,$2E
7D2A: 2E 41      LD           L,$41
7D2C: 6E         LD           L,(HL)
7D2D: 79         LD           A,C
7D2E: 77         LD           (HL),A
7D2F: 61         LD           H,C
7D30: 79         LD           A,C
7D31: 2C         INC         L
7D32: 20 49      JR           NZ,$7D7D
7D34: 20 68      JR           NZ,$7D9E
7D36: 65         LD           H,L
7D37: 61         LD           H,C
7D38: 72         LD           (HL),D
7D39: 64         LD           H,H
7D3A: 20 66      JR           NZ,$7DA2
7D3C: 72         LD           (HL),D
7D3D: 6F         LD           L,A
7D3E: 6D         LD           L,L
7D3F: 20 61      JR           NZ,$7DA2
7D41: 20 76      JR           NZ,$7DB9
7D43: 65         LD           H,L
7D44: 72         LD           (HL),D
7D45: 79         LD           A,C
7D46: 20 67      JR           NZ,$7DAF
7D48: 6F         LD           L,A
7D49: 6F         LD           L,A
7D4A: 64         LD           H,H
7D4B: 73         LD           (HL),E
7D4C: 6F         LD           L,A
7D4D: 75         LD           (HL),L
7D4E: 72         LD           (HL),D
7D4F: 63         LD           H,E
7D50: 65         LD           H,L
7D51: 20 74      JR           NZ,$7DC7
7D53: 68         LD           L,B
7D54: 61         LD           H,C
7D55: 74         LD           (HL),H
7D56: 20 74      JR           NZ,$7DCC
7D58: 68         LD           L,B
7D59: 65         LD           H,L
7D5A: 79         LD           A,C
7D5B: 68         LD           L,B
7D5C: 61         LD           H,C
7D5D: 76         HALT
7D5E: 65         LD           H,L
7D5F: 20 61      JR           NZ,$7DC2
7D61: 20 44      JR           NZ,$7DA7
7D63: 72         LD           (HL),D
7D64: 65         LD           H,L
7D65: 61         LD           H,C
7D66: 6D         LD           L,L
7D67: 20 20      JR           NZ,$7D89
7D69: 20 20      JR           NZ,$7D8B
7D6B: 53         LD           D,E
7D6C: 68         LD           L,B
7D6D: 72         LD           (HL),D
7D6E: 69         LD           L,C
7D6F: 6E         LD           L,(HL)
7D70: 65         LD           H,L
7D71: 20 69      JR           NZ,$7DDC
7D73: 6E         LD           L,(HL)
7D74: 20 4D      JR           NZ,$7DC3
7D76: 61         LD           H,C
7D77: 62         LD           H,D
7D78: 65         LD           H,L
7D79: 2C         INC         L
7D7A: 20 61      JR           NZ,$7DDD
7D7C: 6E         LD           L,(HL)
7D7D: 64         LD           H,H
7D7E: 20 74      JR           NZ,$7DF4
7D80: 68         LD           L,B
7D81: 61         LD           H,C
7D82: 74         LD           (HL),H
7D83: 20 69      JR           NZ,$7DEE
7D85: 74         LD           (HL),H
7D86: 20 68      JR           NZ,$7DF0
7D88: 61         LD           H,C
7D89: 73         LD           (HL),E
7D8A: 20 73      JR           NZ,$7DFF
7D8C: 6F         LD           L,A
7D8D: 6D         LD           L,L
7D8E: 65         LD           H,L
7D8F: 74         LD           (HL),H
7D90: 68         LD           L,B
7D91: 69         LD           L,C
7D92: 6E         LD           L,(HL)
7D93: 67         LD           H,A
7D94: 20 67      JR           NZ,$7DFD
7D96: 6F         LD           L,A
7D97: 6F         LD           L,A
7D98: 64         LD           H,H
7D99: 20 20      JR           NZ,$7DBB
7D9B: 69         LD           L,C
7D9C: 6E         LD           L,(HL)
7D9D: 73         LD           (HL),E
7D9E: 69         LD           L,C
7D9F: 64         LD           H,H
7DA0: 65         LD           H,L
7DA1: 2E 2E      LD           L,$2E
7DA3: 2E 20      LD           L,$20
7DA5: 20 49      JR           NZ,$7DF0
7DA7: 73         LD           (HL),E
7DA8: 20 20      JR           NZ,$7DCA
7DAA: 20 74      JR           NZ,$7E20
7DAC: 68         LD           L,B
7DAD: 61         LD           H,C
7DAE: 74         LD           (HL),H
7DAF: 20 74      JR           NZ,$7E25
7DB1: 72         LD           (HL),D
7DB2: 75         LD           (HL),L
7DB3: 65         LD           H,L
7DB4: 3F         CCF
7DB5: FF         RST         0X38
7DB6: 4C         LD           C,H
7DB7: 61         LD           H,C
7DB8: 74         LD           (HL),H
7DB9: 65         LD           H,L
7DBA: 6C         LD           L,H
7DBB: 79         LD           A,C
7DBC: 20 74      JR           NZ,$7E32
7DBE: 68         LD           L,B
7DBF: 65         LD           H,L
7DC0: 72         LD           (HL),D
7DC1: 65         LD           H,L
7DC2: 20 20      JR           NZ,$7DE4
7DC4: 20 20      JR           NZ,$7DE6
7DC6: 68         LD           L,B
7DC7: 61         LD           H,C
7DC8: 76         HALT
7DC9: 65         LD           H,L
7DCA: 20 62      JR           NZ,$7E2E
7DCC: 65         LD           H,L
7DCD: 65         LD           H,L
7DCE: 6E         LD           L,(HL)
7DCF: 20 61      JR           NZ,$7E32
7DD1: 20 6C      JR           NZ,$7E3F
7DD3: 6F         LD           L,A
7DD4: 74         LD           (HL),H
7DD5: 20 6F      JR           NZ,$7E46
7DD7: 66         LD           H,(HL)
7DD8: 20 6D      JR           NZ,$7E47
7DDA: 6F         LD           L,A
7DDB: 6E         LD           L,(HL)
7DDC: 73         LD           (HL),E
7DDD: 74         LD           (HL),H
7DDE: 65         LD           H,L
7DDF: 72         LD           (HL),D
7DE0: 73         LD           (HL),E
7DE1: 20 69      JR           NZ,$7E4C
7DE3: 6E         LD           L,(HL)
7DE4: 20 20      JR           NZ,$7E06
7DE6: 74         LD           (HL),H
7DE7: 68         LD           L,B
7DE8: 65         LD           H,L
7DE9: 20 61      JR           NZ,$7E4C
7DEB: 72         LD           (HL),D
7DEC: 65         LD           H,L
7DED: 61         LD           H,C
7DEE: 2C         INC         L
7DEF: 20 73      JR           NZ,$7E64
7DF1: 6F         LD           L,A
7DF2: 20 77      JR           NZ,$7E6B
7DF4: 65         LD           H,L
7DF5: 20 63      JR           NZ,$7E5A
7DF7: 61         LD           H,C
7DF8: 6E         LD           L,(HL)
7DF9: 5E         LD           E,(HL)
7DFA: 74         LD           (HL),H
7DFB: 20 67      JR           NZ,$7E64
7DFD: 6F         LD           L,A
7DFE: 20 74      JR           NZ,$7E74
7E00: 6F         LD           L,A
7E01: 20 4D      JR           NZ,$7E50
7E03: 61         LD           H,C
7E04: 62         LD           H,D
7E05: 65         LD           H,L
7E06: 56         LD           D,(HL)
7E07: 69         LD           L,C
7E08: 6C         LD           L,H
7E09: 6C         LD           L,H
7E0A: 61         LD           H,C
7E0B: 67         LD           H,A
7E0C: 65         LD           H,L
7E0D: 2E 2E      LD           L,$2E
7E0F: 2E 20      LD           L,$20
7E11: 20 49      JR           NZ,$7E5C
7E13: 20 20      JR           NZ,$7E35
7E15: 20 77      JR           NZ,$7E8E
7E17: 6F         LD           L,A
7E18: 6E         LD           L,(HL)
7E19: 64         LD           H,H
7E1A: 65         LD           H,L
7E1B: 72         LD           (HL),D
7E1C: 20 68      JR           NZ,$7E86
7E1E: 6F         LD           L,A
7E1F: 77         LD           (HL),A
7E20: 20 4D      JR           NZ,$7E6F
7E22: 61         LD           H,C
7E23: 72         LD           (HL),D
7E24: 69         LD           L,C
7E25: 6E         LD           L,(HL)
7E26: 69         LD           L,C
7E27: 73         LD           (HL),E
7E28: 20 64      JR           NZ,$7E8E
7E2A: 6F         LD           L,A
7E2B: 69         LD           L,C
7E2C: 6E         LD           L,(HL)
7E2D: 67         LD           H,A
7E2E: 3F         CCF
7E2F: FF         RST         0X38
7E30: 48         LD           C,B
7E31: 61         LD           H,C
7E32: 76         HALT
7E33: 65         LD           H,L
7E34: 20 79      JR           NZ,$7EAF
7E36: 6F         LD           L,A
7E37: 75         LD           (HL),L
7E38: 20 68      JR           NZ,$7EA2
7E3A: 65         LD           H,L
7E3B: 61         LD           H,C
7E3C: 72         LD           (HL),D
7E3D: 64         LD           H,H
7E3E: 20 20      JR           NZ,$7E60
7E40: 6F         LD           L,A
7E41: 66         LD           H,(HL)
7E42: 20 74      JR           NZ,$7EB8
7E44: 68         LD           L,B
7E45: 65         LD           H,L
7E46: 20 46      JR           NZ,$7E8E
7E48: 6C         LD           L,H
7E49: 79         LD           A,C
7E4A: 69         LD           L,C
7E4B: 6E         LD           L,(HL)
7E4C: 67         LD           H,A
7E4D: 20 20      JR           NZ,$7E6F
7E4F: 20 52      JR           NZ,$7EA3
7E51: 6F         LD           L,A
7E52: 6F         LD           L,A
7E53: 73         LD           (HL),E
7E54: 74         LD           (HL),H
7E55: 65         LD           H,L
7E56: 72         LD           (HL),D
7E57: 3F         CCF
7E58: 20 20      JR           NZ,$7E7A
7E5A: 54         LD           D,H
7E5B: 68         LD           L,B
7E5C: 65         LD           H,L
7E5D: 79         LD           A,C
7E5E: 20 20      JR           NZ,$7E80
7E60: 73         LD           (HL),E
7E61: 61         LD           H,C
7E62: 79         LD           A,C
7E63: 20 69      JR           NZ,$7ECE
7E65: 74         LD           (HL),H
7E66: 20 6C      JR           NZ,$7ED4
7E68: 69         LD           L,C
7E69: 76         HALT
7E6A: 65         LD           H,L
7E6B: 64         LD           H,H
7E6C: 20 69      JR           NZ,$7ED7
7E6E: 6E         LD           L,(HL)
7E6F: 20 4D      JR           NZ,$7EBE
7E71: 61         LD           H,C
7E72: 62         LD           H,D
7E73: 65         LD           H,L
7E74: 20 56      JR           NZ,$7ECC
7E76: 69         LD           L,C
7E77: 6C         LD           L,H
7E78: 6C         LD           L,H
7E79: 61         LD           H,C
7E7A: 67         LD           H,A
7E7B: 65         LD           H,L
7E7C: 20 61      JR           NZ,$7EDF
7E7E: 20 20      JR           NZ,$7EA0
7E80: 6C         LD           L,H
7E81: 6F         LD           L,A
7E82: 6E         LD           L,(HL)
7E83: 67         LD           H,A
7E84: 20 74      JR           NZ,$7EFA
7E86: 69         LD           L,C
7E87: 6D         LD           L,L
7E88: 65         LD           H,L
7E89: 20 61      JR           NZ,$7EEC
7E8B: 67         LD           H,A
7E8C: 6F         LD           L,A
7E8D: 2E 2E      LD           L,$2E
7E8F: 2E 49      LD           L,$49
7E91: 20 77      JR           NZ,$7F0A
7E93: 6F         LD           L,A
7E94: 6E         LD           L,(HL)
7E95: 64         LD           H,H
7E96: 65         LD           H,L
7E97: 72         LD           (HL),D
7E98: 20 69      JR           NZ,$7F03
7E9A: 66         LD           H,(HL)
7E9B: 20 69      JR           NZ,$7F06
7E9D: 74         LD           (HL),H
7E9E: 5E         LD           E,(HL)
7E9F: 73         LD           (HL),E
7EA0: 74         LD           (HL),H
7EA1: 72         LD           (HL),D
7EA2: 75         LD           (HL),L
7EA3: 65         LD           H,L
7EA4: 2E 2E      LD           L,$2E
7EA6: 2E FF      LD           L,$FF
7EA8: 41         LD           B,C
7EA9: 61         LD           H,C
7EAA: 61         LD           H,C
7EAB: 61         LD           H,C
7EAC: 68         LD           L,B
7EAD: 2C         INC         L
7EAE: 20 4C      JR           NZ,$7EFC
7EB0: 69         LD           L,C
7EB1: 74         LD           (HL),H
7EB2: 74         LD           (HL),H
7EB3: 6C         LD           L,H
7EB4: 65         LD           H,L
7EB5: 20 20      JR           NZ,$7ED7
7EB7: 20 4D      JR           NZ,$7F06
7EB9: 61         LD           H,C
7EBA: 72         LD           (HL),D
7EBB: 69         LD           L,C
7EBC: 6E         LD           L,(HL)
7EBD: 2E 2E      LD           L,$2E
7EBF: 2E 20      LD           L,$20
7EC1: 49         LD           C,C
7EC2: 20 77      JR           NZ,$7F3B
7EC4: 61         LD           H,C
7EC5: 6E         LD           L,(HL)
7EC6: 74         LD           (HL),H
7EC7: 20 68      JR           NZ,$7F31
7EC9: 65         LD           H,L
7ECA: 72         LD           (HL),D
7ECB: 20 74      JR           NZ,$7F41
7ECD: 6F         LD           L,A
7ECE: 20 63      JR           NZ,$7F33
7ED0: 6F         LD           L,A
7ED1: 6D         LD           L,L
7ED2: 65         LD           H,L
7ED3: 20 62      JR           NZ,$7F37
7ED5: 61         LD           H,C
7ED6: 63         LD           H,E
7ED7: 6B         LD           L,E
7ED8: 61         LD           H,C
7ED9: 67         LD           H,A
7EDA: 61         LD           H,C
7EDB: 69         LD           L,C
7EDC: 6E         LD           L,(HL)
7EDD: 2E 2E      LD           L,$2E
7EDF: 2E 48      LD           L,$48
7EE1: 65         LD           H,L
7EE2: 72         LD           (HL),D
7EE3: 20 73      JR           NZ,$7F58
7EE5: 6F         LD           L,A
7EE6: 6E         LD           L,(HL)
7EE7: 67         LD           H,A
7EE8: 69         LD           L,C
7EE9: 73         LD           (HL),E
7EEA: 20 74      JR           NZ,$7F60
7EEC: 68         LD           L,B
7EED: 65         LD           H,L
7EEE: 20 62      JR           NZ,$7F52
7EF0: 65         LD           H,L
7EF1: 73         LD           (HL),E
7EF2: 74         LD           (HL),H
7EF3: 2E 2E      LD           L,$2E
7EF5: 2E FF      LD           L,$FF
7EF7: 49         LD           C,C
7EF8: 20 64      JR           NZ,$7F5E
7EFA: 72         LD           (HL),D
7EFB: 65         LD           H,L
7EFC: 61         LD           H,C
7EFD: 6D         LD           L,L
7EFE: 65         LD           H,L
7EFF: 64         LD           H,H
7F00: 20 74      JR           NZ,$7F76
7F02: 68         LD           L,B
7F03: 61         LD           H,C
7F04: 74         LD           (HL),H
7F05: 20 20      JR           NZ,$7F27
7F07: 49         LD           C,C
7F08: 20 74      JR           NZ,$7F7E
7F0A: 75         LD           (HL),L
7F0B: 72         LD           (HL),D
7F0C: 6E         LD           L,(HL)
7F0D: 65         LD           H,L
7F0E: 64         LD           H,H
7F0F: 20 69      JR           NZ,$7F7A
7F11: 6E         LD           L,(HL)
7F12: 74         LD           (HL),H
7F13: 6F         LD           L,A
7F14: 20 61      JR           NZ,$7F77
7F16: 20 63      JR           NZ,$7F7B
7F18: 61         LD           H,C
7F19: 72         LD           (HL),D
7F1A: 72         LD           (HL),D
7F1B: 6F         LD           L,A
7F1C: 74         LD           (HL),H
7F1D: 20 6C      JR           NZ,$7F8B
7F1F: 61         LD           H,C
7F20: 73         LD           (HL),E
7F21: 74         LD           (HL),H
7F22: 20 20      JR           NZ,$7F44
7F24: 20 20      JR           NZ,$7F46
7F26: 20 6E      JR           NZ,$7F96
7F28: 69         LD           L,C
7F29: 67         LD           H,A
7F2A: 68         LD           L,B
7F2B: 74         LD           (HL),H
7F2C: 2E 2E      LD           L,$2E
7F2E: 2E 20      LD           L,$20
7F30: 20 57      JR           NZ,$7F89
7F32: 68         LD           L,B
7F33: 61         LD           H,C
7F34: 74         LD           (HL),H
7F35: 20 20      JR           NZ,$7F57
7F37: 61         LD           H,C
7F38: 6E         LD           L,(HL)
7F39: 20 6F      JR           NZ,$7FAA
7F3B: 64         LD           H,H
7F3C: 64         LD           H,H
7F3D: 20 64      JR           NZ,$7FA3
7F3F: 72         LD           (HL),D
7F40: 65         LD           H,L
7F41: 61         LD           H,C
7F42: 6D         LD           L,L
7F43: 2E 2E      LD           L,$2E
7F45: 2E FF      LD           L,$FF
7F47: 45         LD           B,L
7F48: 68         LD           L,B
7F49: 3F         CCF
7F4A: 20 20      JR           NZ,$7F6C
7F4C: 48         LD           C,B
7F4D: 6F         LD           L,A
7F4E: 77         LD           (HL),A
7F4F: 20 63      JR           NZ,$7FB4
7F51: 61         LD           H,C
7F52: 6E         LD           L,(HL)
7F53: 20 61      JR           NZ,$7FB6
7F55: 6E         LD           L,(HL)
7F56: 20 61      JR           NZ,$7FB9
7F58: 6E         LD           L,(HL)
7F59: 69         LD           L,C
7F5A: 6D         LD           L,L
7F5B: 61         LD           H,C
7F5C: 6C         LD           L,H
7F5D: 20 74      JR           NZ,$7FD3
7F5F: 61         LD           H,C
7F60: 6C         LD           L,H
7F61: 6B         LD           L,E
7F62: 3F         CCF
7F63: 20 20      JR           NZ,$7F85
7F65: 20 20      JR           NZ,$7F87
7F67: 48         LD           C,B
7F68: 6F         LD           L,A
7F69: 77         LD           (HL),A
7F6A: 3F         CCF
7F6B: 20 20      JR           NZ,$7F8D
7F6D: 48         LD           C,B
7F6E: 65         LD           H,L
7F6F: 79         LD           A,C
7F70: 2C         INC         L
7F71: 20 49      JR           NZ,$7FBC
7F73: 5E         LD           E,(HL)
7F74: 6D         LD           L,L
7F75: 20 20      JR           NZ,$7F97
7F77: 6A         LD           L,D
7F78: 75         LD           (HL),L
7F79: 73         LD           (HL),E
7F7A: 74         LD           (HL),H
7F7B: 20 61      JR           NZ,$7FDE
7F7D: 20 72      JR           NZ,$7FF1
7F7F: 61         LD           H,C
7F80: 62         LD           H,D
7F81: 62         LD           H,D
7F82: 69         LD           L,C
7F83: 74         LD           (HL),H
7F84: 2C         INC         L
7F85: 20 20      JR           NZ,$7FA7
7F87: 73         LD           (HL),E
7F88: 6F         LD           L,A
7F89: 20 49      JR           NZ,$7FD4
7F8B: 20 64      JR           NZ,$7FF1
7F8D: 6F         LD           L,A
7F8E: 6E         LD           L,(HL)
7F8F: 5E         LD           E,(HL)
7F90: 74         LD           (HL),H
7F91: 20 6B      JR           NZ,$7FFE
7F93: 6E         LD           L,(HL)
7F94: 6F         LD           L,A
7F95: 77         LD           (HL),A
7F96: 21 FF 41   LD           HL,$41FF
7F99: 68         LD           L,B
7F9A: 68         LD           L,B
7F9B: 68         LD           L,B
7F9C: 21 20 20   LD           HL,$2020
7F9F: 49         LD           C,C
7FA0: 74         LD           (HL),H
7FA1: 5E         LD           E,(HL)
7FA2: 73         LD           (HL),E
7FA3: 20 68      JR           NZ,$800D
7FA5: 65         LD           H,L
7FA6: 72         LD           (HL),D
7FA7: 21 4C 69   LD           HL,$694C
7FAA: 74         LD           (HL),H
7FAB: 74         LD           (HL),H
7FAC: 6C         LD           L,H
7FAD: 65         LD           H,L
7FAE: 20 4D      JR           NZ,$7FFD
7FB0: 61         LD           H,C
7FB1: 72         LD           (HL),D
7FB2: 69         LD           L,C
7FB3: 6E         LD           L,(HL)
7FB4: 21 21 FF   LD           HL,$FF21
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
