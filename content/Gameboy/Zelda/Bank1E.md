![Bank 1E](GBZelda.jpg)

# Bank 1E

>>> cpu Z80GB

>>> binary 4000:roms/zelda.gb[78000:7C000]

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: C3 09 40   JP           $4009
4003: C3 FA 4C   JP           $4CFA
4006: C3 1E 40   JP           $401E
4009: 21 00 D3   LD           HL,$D300
400C: 36 00      LD           (HL),$00
400E: 2C         INC         L
400F: 20 FB      JR           NZ,$400C
4011: 3E 80      LD           A,$80
4013: E0 26      LDFF00   ($26),A
4015: 3E 77      LD           A,$77
4017: E0 24      LDFF00   ($24),A
4019: 3E FF      LD           A,$FF
401B: E0 25      LDFF00   ($25),A
401D: C9         RET
401E: 21 68 D3   LD           HL,$D368
4021: 2A         LD           A,(HLI)
4022: A7         AND         A
4023: 20 14      JR           NZ,$4039
4025: CD 3F 40   CALL       $403F
4028: CD 7C 45   CALL       $457C
402B: AF         XOR         A
402C: EA 60 D3   LD           ($D360),A
402F: EA 68 D3   LD           ($D368),A
4032: EA 70 D3   LD           ($D370),A
4035: EA 78 D3   LD           ($D378),A
4038: C9         RET
4039: 77         LD           (HL),A
403A: CD 63 41   CALL       $4163
403D: 18 E9      JR           $4028
403F: 11 93 D3   LD           DE,$D393
4042: 21 78 D3   LD           HL,$D378
4045: 2A         LD           A,(HLI)
4046: FE 01      CP           $01
4048: 28 06      JR           Z,$4050
404A: 7E         LD           A,(HL)
404B: FE 01      CP           $01
404D: 28 0C      JR           Z,$405B
404F: C9         RET
4050: 3E 01      LD           A,$01
4052: EA 79 D3   LD           ($D379),A
4055: 21 68 40   LD           HL,$4068
4058: C3 72 40   JP           $4072
405B: 1A         LD           A,(DE)
405C: 3D         DEC         A
405D: 12         LD           (DE),A
405E: C0         RET         NZ
405F: AF         XOR         A
4060: EA 79 D3   LD           ($D379),A
4063: 21 6D 40   LD           HL,$406D
4066: 18 0A      JR           $4072
4068: 3B         DEC         SP
4069: 80         ADD         A,B
406A: 07         RLCA
406B: C0         RET         NZ
406C: 02         LD           (BC),A
406D: 00         NOP
406E: 42         LD           B,D
406F: 02         LD           (BC),A
4070: C0         RET         NZ
4071: 04         INC         B
4072: 06 04      LD           B,$04
4074: 0E 20      LD           C,$20
4076: 2A         LD           A,(HLI)
4077: E2         LDFF00   (C),A
4078: 0C         INC         C
4079: 05         DEC         B
407A: 20 FA      JR           NZ,$4076
407C: 7E         LD           A,(HL)
407D: 12         LD           (DE),A
407E: C9         RET
407F: 09         ADD         HL,BC
4080: 52         LD           D,D
4081: 56         LD           D,(HL)
4082: 56         LD           D,(HL)
4083: 6A         LD           L,D
4084: 5E         LD           E,(HL)
4085: 74         LD           (HL),H
4086: 59         LD           E,C
4087: AE         XOR         (HL)
4088: 5A         LD           E,D
4089: A7         AND         A
408A: 5C         LD           E,H
408B: B3         OR           E
408C: 5D         LD           E,L
408D: EE 5E      XOR         $5E
408F: 3C         INC         A
4090: 5F         LD           E,A
4091: 00         NOP
4092: 50         LD           D,B
4093: 64         LD           H,H
4094: 60         LD           H,B
4095: C2 60 23   JP           NZ,$2360
4098: 61         LD           H,C
4099: A9         XOR         C
409A: 62         LD           H,D
409B: 75         LD           (HL),L
409C: 64         LD           H,H
409D: A5         AND         L
409E: 72         LD           (HL),D
409F: 10 66      STOP       $66
40A1: 36 66      LD           (HL),$66
40A3: BF         CP           A
40A4: 52         LD           D,D
40A5: 62         LD           H,D
40A6: 66         LD           H,(HL)
40A7: A6         AND         (HL)
40A8: 7B         LD           A,E
40A9: 77         LD           (HL),A
40AA: 67         LD           H,A
40AB: 2E 4B      LD           L,$4B
40AD: F1         POP         AF
40AE: 72         LD           (HL),D
40AF: 3F         CCF
40B0: 73         LD           (HL),E
40B1: 9E         SBC         (HL)
40B2: 73         LD           (HL),E
40B3: 16 74      LD           D,$74
40B5: A8         XOR         B
40B6: 74         LD           (HL),H
40B7: 46         LD           B,(HL)
40B8: 75         LD           (HL),L
40B9: 92         SUB         D
40BA: 75         LD           (HL),L
40BB: 00         NOP
40BC: 76         HALT
40BD: 3D         DEC         A
40BE: 77         LD           (HL),A
40BF: 00         NOP
40C0: 70         LD           (HL),B
40C1: 2C         INC         L
40C2: 70         LD           (HL),B
40C3: F0 70      LD           A,($70)
40C5: 58         LD           E,B
40C6: 71         LD           (HL),C
40C7: A6         AND         (HL)
40C8: 71         LD           (HL),C
40C9: D4 71 3C   CALL       NC,$3C71
40CC: 72         LD           (HL),D
40CD: D3                              
40CE: 78         LD           A,B
40CF: 23         INC         HL
40D0: 4B         LD           C,E
40D1: 93         SUB         E
40D2: 76         HALT
40D3: 0E 63      LD           C,$63
40D5: 79         LD           A,C
40D6: 69         LD           L,C
40D7: DF         RST         0X18
40D8: 69         LD           L,C
40D9: 21 6A 09   LD           HL,$096A
40DC: 6C         LD           L,H
40DD: 33         INC         SP
40DE: 4C         LD           C,H
40DF: 6A         LD           L,D
40E0: 5E         LD           E,(HL)
40E1: 74         LD           (HL),H
40E2: 59         LD           E,C
40E3: B7         OR           A
40E4: 66         LD           H,(HL)
40E5: 80         ADD         A,B
40E6: 6C         LD           L,H
40E7: 05         DEC         B
40E8: 7A         LD           A,D
40E9: 5A         LD           E,D
40EA: 7A         LD           A,D
40EB: 28 7B      JR           Z,$4168
40ED: 7B         LD           A,E
40EE: 65         LD           H,L
40EF: 28 7C      JR           Z,$416D
40F1: C9         RET
40F2: 58         LD           E,B
40F3: 9C         SBC         H
40F4: 67         LD           H,A
40F5: 49         LD           C,C
40F6: 6C         LD           L,H
40F7: AC         XOR         H
40F8: 52         LD           D,D
40F9: FF         RST         0X38
40FA: 7C         LD           A,H
40FB: 4B         LD           C,E
40FC: 7D         LD           A,L
40FD: 04         INC         B
40FE: 7E         LD           A,(HL)
40FF: 1C         INC         E
4100: 3D         DEC         A
4101: CB 27      SLA         1,E
4103: 4F         LD           C,A
4104: 06 00      LD           B,$00
4106: 09         ADD         HL,BC
4107: 4E         LD           C,(HL)
4108: 23         INC         HL
4109: 46         LD           B,(HL)
410A: 69         LD           L,C
410B: 60         LD           H,B
410C: 7C         LD           A,H
410D: C9         RET
410E: C5         PUSH       BC
410F: 0E 30      LD           C,$30
4111: 2A         LD           A,(HLI)
4112: E2         LDFF00   (C),A
4113: 0C         INC         C
4114: 79         LD           A,C
4115: FE 40      CP           $40
4117: 20 F8      JR           NZ,$4111
4119: C1         POP         BC
411A: C9         RET
411B: AF         XOR         A
411C: EA 79 D3   LD           ($D379),A
411F: EA 4F D3   LD           ($D34F),A
4122: EA 98 D3   LD           ($D398),A
4125: EA 93 D3   LD           ($D393),A
4128: EA C9 D3   LD           ($D3C9),A
412B: EA A3 D3   LD           ($D3A3),A
412E: 3E 08      LD           A,$08
4130: E0 21      LDFF00   ($21),A
4132: 3E 80      LD           A,$80
4134: E0 23      LDFF00   ($23),A
4136: C9         RET
4137: FA 79 D3   LD           A,($D379)
413A: FE 05      CP           $05
413C: CA 18 4D   JP           Z,$4D18
413F: FE 0C      CP           $0C
4141: CA 18 4D   JP           Z,$4D18
4144: FE 1A      CP           $1A
4146: CA 18 4D   JP           Z,$4D18
4149: FE 24      CP           $24
414B: CA 18 4D   JP           Z,$4D18
414E: FE 2A      CP           $2A
4150: CA 18 4D   JP           Z,$4D18
4153: FE 2E      CP           $2E
4155: CA 18 4D   JP           Z,$4D18
4158: FE 3F      CP           $3F
415A: CA 18 4D   JP           Z,$4D18
415D: CD 1B 41   CALL       $411B
4160: C3 18 4D   JP           $4D18
4163: 47         LD           B,A
4164: FA CE D3   LD           A,($D3CE)
4167: A7         AND         A
4168: C2 2B 40   JP           NZ,$402B
416B: 78         LD           A,B
416C: FE FF      CP           $FF
416E: 28 C7      JR           Z,$4137
4170: FE 11      CP           $11
4172: 30 03      JR           NC,$4177
4174: C3 2B 40   JP           $402B
4177: FE 21      CP           $21
4179: 30 04      JR           NC,$417F
417B: C6 F0      ADD         $F0
417D: 18 0F      JR           $418E
417F: FE 31      CP           $31
4181: 30 04      JR           NC,$4187
4183: C6 F0      ADD         $F0
4185: 18 07      JR           $418E
4187: FE 41      CP           $41
4189: DA 2B 40   JP           C,$402B
418C: C6 E0      ADD         $E0
418E: 2B         DEC         HL
418F: 22         LD           (HLI),A
4190: 32         LD           (HLD),A
4191: FA CA D3   LD           A,($D3CA)
4194: EA CB D3   LD           ($D3CB),A
4197: 2A         LD           A,(HLI)
4198: EA CA D3   LD           ($D3CA),A
419B: 47         LD           B,A
419C: 21 7F 40   LD           HL,$407F
419F: E6 7F      AND         $7F
41A1: CD FF 40   CALL       $40FF
41A4: CD BB 43   CALL       $43BB
41A7: C3 54 43   JP           $4354
41AA: 01 00 FF   LD           BC,$FF00
41AD: FF         RST         0X38
41AE: 00         NOP
41AF: 00         NOP
41B0: 01 00 FF   LD           BC,$FF00
41B3: FF         RST         0X38
41B4: 00         NOP
41B5: 00         NOP
41B6: 01 00 FF   LD           BC,$FF00
41B9: FF         RST         0X38
41BA: 00         NOP
41BB: 00         NOP
41BC: 01 00 FF   LD           BC,$FF00
41BF: FF         RST         0X38
41C0: 00         NOP
41C1: 00         NOP
41C2: 01 00 FF   LD           BC,$FF00
41C5: FF         RST         0X38
41C6: 00         NOP
41C7: 00         NOP
41C8: 01 00 FF   LD           BC,$FF00
41CB: FF         RST         0X38
41CC: 00         NOP
41CD: 00         NOP
41CE: 01 00 FF   LD           BC,$FF00
41D1: FF         RST         0X38
41D2: 00         NOP
41D3: 00         NOP
41D4: 01 00 FF   LD           BC,$FF00
41D7: FF         RST         0X38
41D8: 00         NOP
41D9: 00         NOP
41DA: 01 00 FF   LD           BC,$FF00
41DD: FF         RST         0X38
41DE: 00         NOP
41DF: 00         NOP
41E0: 01 00 FF   LD           BC,$FF00
41E3: FF         RST         0X38
41E4: 00         NOP
41E5: 00         NOP
41E6: 01 00 FF   LD           BC,$FF00
41E9: FF         RST         0X38
41EA: 00         NOP
41EB: 00         NOP
41EC: 01 00 FF   LD           BC,$FF00
41EF: FF         RST         0X38
41F0: 00         NOP
41F1: 00         NOP
41F2: 01 00 FF   LD           BC,$FF00
41F5: FF         RST         0X38
41F6: 00         NOP
41F7: 00         NOP
41F8: 01 00 FF   LD           BC,$FF00
41FB: FF         RST         0X38
41FC: 00         NOP
41FD: 00         NOP
41FE: 01 00 FF   LD           BC,$FF00
4201: FF         RST         0X38
4202: 00         NOP
4203: 00         NOP
4204: 01 00 FF   LD           BC,$FF00
4207: FF         RST         0X38
4208: 00         NOP
4209: 00         NOP
420A: 01 00 FF   LD           BC,$FF00
420D: FF         RST         0X38
420E: 00         NOP
420F: 00         NOP
4210: 01 00 FF   LD           BC,$FF00
4213: FF         RST         0X38
4214: 00         NOP
4215: 00         NOP
4216: 01 00 FF   LD           BC,$FF00
4219: FF         RST         0X38
421A: 00         NOP
421B: 00         NOP
421C: 01 00 FF   LD           BC,$FF00
421F: FF         RST         0X38
4220: 00         NOP
4221: 00         NOP
4222: 01 00 FF   LD           BC,$FF00
4225: FF         RST         0X38
4226: 00         NOP
4227: 00         NOP
4228: 01 00 FF   LD           BC,$FF00
422B: FF         RST         0X38
422C: 00         NOP
422D: 00         NOP
422E: 01 00 FF   LD           BC,$FF00
4231: FF         RST         0X38
4232: 00         NOP
4233: 00         NOP
4234: 01 00 FF   LD           BC,$FF00
4237: FF         RST         0X38
4238: 00         NOP
4239: 00         NOP
423A: 01 00 FF   LD           BC,$FF00
423D: FF         RST         0X38
423E: 00         NOP
423F: 00         NOP
4240: 01 00 FF   LD           BC,$FF00
4243: FF         RST         0X38
4244: 00         NOP
4245: 00         NOP
4246: 01 00 FF   LD           BC,$FF00
4249: FF         RST         0X38
424A: 00         NOP
424B: 00         NOP
424C: 01 00 FF   LD           BC,$FF00
424F: FF         RST         0X38
4250: 00         NOP
4251: 00         NOP
4252: 01 00 FF   LD           BC,$FF00
4255: FF         RST         0X38
4256: 00         NOP
4257: 00         NOP
4258: 01 00 FF   LD           BC,$FF00
425B: FF         RST         0X38
425C: 00         NOP
425D: 00         NOP
425E: 01 00 FF   LD           BC,$FF00
4261: FF         RST         0X38
4262: 00         NOP
4263: 00         NOP
4264: 01 00 FF   LD           BC,$FF00
4267: FF         RST         0X38
4268: 00         NOP
4269: 00         NOP
426A: 01 00 FF   LD           BC,$FF00
426D: FF         RST         0X38
426E: 00         NOP
426F: 00         NOP
4270: 01 00 FF   LD           BC,$FF00
4273: FF         RST         0X38
4274: 00         NOP
4275: 00         NOP
4276: 01 00 FF   LD           BC,$FF00
4279: FF         RST         0X38
427A: 00         NOP
427B: 00         NOP
427C: 01 00 FF   LD           BC,$FF00
427F: FF         RST         0X38
4280: 00         NOP
4281: 00         NOP
4282: 01 00 FF   LD           BC,$FF00
4285: FF         RST         0X38
4286: 00         NOP
4287: 00         NOP
4288: 01 00 FF   LD           BC,$FF00
428B: FF         RST         0X38
428C: 00         NOP
428D: 00         NOP
428E: 01 00 FF   LD           BC,$FF00
4291: FF         RST         0X38
4292: 00         NOP
4293: 00         NOP
4294: 01 00 FF   LD           BC,$FF00
4297: FF         RST         0X38
4298: 00         NOP
4299: 00         NOP
429A: 01 00 FF   LD           BC,$FF00
429D: FF         RST         0X38
429E: 00         NOP
429F: 00         NOP
42A0: 01 00 FF   LD           BC,$FF00
42A3: FF         RST         0X38
42A4: 00         NOP
42A5: 00         NOP
42A6: 01 00 FF   LD           BC,$FF00
42A9: FF         RST         0X38
42AA: 00         NOP
42AB: 00         NOP
42AC: 01 00 FF   LD           BC,$FF00
42AF: FF         RST         0X38
42B0: 00         NOP
42B1: 00         NOP
42B2: 01 00 FF   LD           BC,$FF00
42B5: FF         RST         0X38
42B6: 00         NOP
42B7: 00         NOP
42B8: 01 00 FF   LD           BC,$FF00
42BB: FF         RST         0X38
42BC: 00         NOP
42BD: 00         NOP
42BE: 01 00 FF   LD           BC,$FF00
42C1: FF         RST         0X38
42C2: 00         NOP
42C3: 00         NOP
42C4: 01 00 FF   LD           BC,$FF00
42C7: FF         RST         0X38
42C8: 00         NOP
42C9: 00         NOP
42CA: 01 00 FF   LD           BC,$FF00
42CD: FF         RST         0X38
42CE: 00         NOP
42CF: 00         NOP
42D0: 01 00 FF   LD           BC,$FF00
42D3: FF         RST         0X38
42D4: 00         NOP
42D5: 00         NOP
42D6: 01 00 FF   LD           BC,$FF00
42D9: FF         RST         0X38
42DA: 00         NOP
42DB: 00         NOP
42DC: 01 00 FF   LD           BC,$FF00
42DF: FF         RST         0X38
42E0: 00         NOP
42E1: 00         NOP
42E2: 01 00 FF   LD           BC,$FF00
42E5: FF         RST         0X38
42E6: 00         NOP
42E7: 00         NOP
42E8: 01 00 FF   LD           BC,$FF00
42EB: FF         RST         0X38
42EC: 00         NOP
42ED: 00         NOP
42EE: 01 00 FF   LD           BC,$FF00
42F1: FF         RST         0X38
42F2: 00         NOP
42F3: 00         NOP
42F4: 01 00 FF   LD           BC,$FF00
42F7: FF         RST         0X38
42F8: 00         NOP
42F9: 00         NOP
42FA: 01 00 FF   LD           BC,$FF00
42FD: FF         RST         0X38
42FE: 00         NOP
42FF: 00         NOP
4300: 01 00 FF   LD           BC,$FF00
4303: FF         RST         0X38
4304: 00         NOP
4305: 00         NOP
4306: 01 00 FF   LD           BC,$FF00
4309: FF         RST         0X38
430A: 00         NOP
430B: 00         NOP
430C: 01 00 FF   LD           BC,$FF00
430F: FF         RST         0X38
4310: 00         NOP
4311: 00         NOP
4312: 01 00 FF   LD           BC,$FF00
4315: FF         RST         0X38
4316: 00         NOP
4317: 00         NOP
4318: 01 00 FF   LD           BC,$FF00
431B: FF         RST         0X38
431C: 00         NOP
431D: 00         NOP
431E: 01 00 FF   LD           BC,$FF00
4321: FF         RST         0X38
4322: 00         NOP
4323: 00         NOP
4324: 01 00 FF   LD           BC,$FF00
4327: FF         RST         0X38
4328: 00         NOP
4329: 00         NOP
432A: FA E7 D3   LD           A,($D3E7)
432D: A7         AND         A
432E: CA 3A 47   JP           Z,$473A
4331: AF         XOR         A
4332: E0 1A      LDFF00   ($1A),A
4334: EA E7 D3   LD           ($D3E7),A
4337: E5         PUSH       HL
4338: FA 36 D3   LD           A,($D336)
433B: 6F         LD           L,A
433C: FA 37 D3   LD           A,($D337)
433F: 67         LD           H,A
4340: C5         PUSH       BC
4341: 0E 30      LD           C,$30
4343: 2A         LD           A,(HLI)
4344: E2         LDFF00   (C),A
4345: 0C         INC         C
4346: 79         LD           A,C
4347: FE 40      CP           $40
4349: 20 F8      JR           NZ,$4343
434B: 3E 80      LD           A,$80
434D: E0 1A      LDFF00   ($1A),A
434F: C1         POP         BC
4350: E1         POP         HL
4351: C3 3A 47   JP           $473A
4354: FA 69 D3   LD           A,($D369)
4357: 21 AA 41   LD           HL,$41AA
435A: 3D         DEC         A
435B: 28 08      JR           Z,$4365
435D: 23         INC         HL
435E: 23         INC         HL
435F: 23         INC         HL
4360: 23         INC         HL
4361: 23         INC         HL
4362: 23         INC         HL
4363: 18 F5      JR           $435A
4365: 01 55 D3   LD           BC,$D355
4368: 2A         LD           A,(HLI)
4369: 02         LD           (BC),A
436A: 0C         INC         C
436B: AF         XOR         A
436C: 02         LD           (BC),A
436D: 0C         INC         C
436E: 2A         LD           A,(HLI)
436F: 02         LD           (BC),A
4370: 0C         INC         C
4371: AF         XOR         A
4372: 02         LD           (BC),A
4373: 0C         INC         C
4374: 2A         LD           A,(HLI)
4375: 02         LD           (BC),A
4376: E0 25      LDFF00   ($25),A
4378: 0C         INC         C
4379: 2A         LD           A,(HLI)
437A: 02         LD           (BC),A
437B: 0C         INC         C
437C: 2A         LD           A,(HLI)
437D: 02         LD           (BC),A
437E: 0C         INC         C
437F: 2A         LD           A,(HLI)
4380: 02         LD           (BC),A
4381: C9         RET
4382: 21 55 D3   LD           HL,$D355
4385: 2A         LD           A,(HLI)
4386: FE 01      CP           $01
4388: C8         RET         Z
4389: 34         INC         (HL)
438A: 2A         LD           A,(HLI)
438B: BE         CP           (HL)
438C: C0         RET         NZ
438D: 2D         DEC         L
438E: 36 00      LD           (HL),$00
4390: 2C         INC         L
4391: 2C         INC         L
4392: 34         INC         (HL)
4393: 2A         LD           A,(HLI)
4394: E6 03      AND         $03
4396: 4D         LD           C,L
4397: 44         LD           B,H
4398: A7         AND         A
4399: 28 0B      JR           Z,$43A6
439B: 0C         INC         C
439C: FE 01      CP           $01
439E: 28 06      JR           Z,$43A6
43A0: 0C         INC         C
43A1: FE 02      CP           $02
43A3: 28 01      JR           Z,$43A6
43A5: 0C         INC         C
43A6: 0A         LD           A,(BC)
43A7: E0 25      LDFF00   ($25),A
43A9: C9         RET
43AA: 2A         LD           A,(HLI)
43AB: 4F         LD           C,A
43AC: 7E         LD           A,(HL)
43AD: 47         LD           B,A
43AE: 0A         LD           A,(BC)
43AF: 12         LD           (DE),A
43B0: 1C         INC         E
43B1: 03         INC         BC
43B2: 0A         LD           A,(BC)
43B3: 12         LD           (DE),A
43B4: C9         RET
43B5: 2A         LD           A,(HLI)
43B6: 12         LD           (DE),A
43B7: 1C         INC         E
43B8: 2A         LD           A,(HLI)
43B9: 12         LD           (DE),A
43BA: C9         RET
43BB: FA 79 D3   LD           A,($D379)
43BE: FE 05      CP           $05
43C0: 28 1B      JR           Z,$43DD
43C2: FE 0C      CP           $0C
43C4: 28 17      JR           Z,$43DD
43C6: FE 1A      CP           $1A
43C8: 28 13      JR           Z,$43DD
43CA: FE 24      CP           $24
43CC: 28 0F      JR           Z,$43DD
43CE: FE 2A      CP           $2A
43D0: 28 0B      JR           Z,$43DD
43D2: FE 2E      CP           $2E
43D4: 28 07      JR           Z,$43DD
43D6: FE 3F      CP           $3F
43D8: 28 03      JR           Z,$43DD
43DA: CD 1B 41   CALL       $411B
43DD: CD 25 4D   CALL       $4D25
43E0: 11 00 D3   LD           DE,$D300
43E3: 06 00      LD           B,$00
43E5: 2A         LD           A,(HLI)
43E6: 12         LD           (DE),A
43E7: 1C         INC         E
43E8: CD B5 43   CALL       $43B5
43EB: 11 10 D3   LD           DE,$D310
43EE: CD B5 43   CALL       $43B5
43F1: 11 20 D3   LD           DE,$D320
43F4: CD B5 43   CALL       $43B5
43F7: 11 30 D3   LD           DE,$D330
43FA: CD B5 43   CALL       $43B5
43FD: 11 40 D3   LD           DE,$D340
4400: CD B5 43   CALL       $43B5
4403: 21 10 D3   LD           HL,$D310
4406: 11 14 D3   LD           DE,$D314
4409: CD AA 43   CALL       $43AA
440C: 21 20 D3   LD           HL,$D320
440F: 11 24 D3   LD           DE,$D324
4412: CD AA 43   CALL       $43AA
4415: 21 30 D3   LD           HL,$D330
4418: 11 34 D3   LD           DE,$D334
441B: CD AA 43   CALL       $43AA
441E: 21 40 D3   LD           HL,$D340
4421: 11 44 D3   LD           DE,$D344
4424: CD AA 43   CALL       $43AA
4427: 01 10 04   LD           BC,$0410
442A: 21 12 D3   LD           HL,$D312
442D: 36 01      LD           (HL),$01
442F: 79         LD           A,C
4430: 85         ADD         A,L
4431: 6F         LD           L,A
4432: 05         DEC         B
4433: 20 F8      JR           NZ,$442D
4435: AF         XOR         A
4436: EA 1E D3   LD           ($D31E),A
4439: EA 2E D3   LD           ($D32E),A
443C: EA 3E D3   LD           ($D33E),A
443F: C9         RET
4440: E5         PUSH       HL
4441: FA 71 D3   LD           A,($D371)
4444: A7         AND         A
4445: 20 08      JR           NZ,$444F
4447: AF         XOR         A
4448: E0 1A      LDFF00   ($1A),A
444A: 6B         LD           L,E
444B: 62         LD           H,D
444C: CD 0E 41   CALL       $410E
444F: E1         POP         HL
4450: 18 2A      JR           $447C
4452: CD 82 44   CALL       $4482
4455: CD 97 44   CALL       $4497
4458: 5F         LD           E,A
4459: CD 82 44   CALL       $4482
445C: CD 97 44   CALL       $4497
445F: 57         LD           D,A
4460: CD 82 44   CALL       $4482
4463: CD 97 44   CALL       $4497
4466: 4F         LD           C,A
4467: 2C         INC         L
4468: 2C         INC         L
4469: 73         LD           (HL),E
446A: 2C         INC         L
446B: 72         LD           (HL),D
446C: 2C         INC         L
446D: 71         LD           (HL),C
446E: 2D         DEC         L
446F: 2D         DEC         L
4470: 2D         DEC         L
4471: 2D         DEC         L
4472: E5         PUSH       HL
4473: 21 50 D3   LD           HL,$D350
4476: 7E         LD           A,(HL)
4477: E1         POP         HL
4478: FE 03      CP           $03
447A: 28 C4      JR           Z,$4440
447C: CD 82 44   CALL       $4482
447F: C3 A0 45   JP           $45A0
4482: D5         PUSH       DE
4483: 2A         LD           A,(HLI)
4484: 5F         LD           E,A
4485: 3A         LD           A,(HLD)
4486: 57         LD           D,A
4487: 13         INC         DE
4488: 7B         LD           A,E
4489: 22         LD           (HLI),A
448A: 7A         LD           A,D
448B: 32         LD           (HLD),A
448C: D1         POP         DE
448D: C9         RET
448E: D5         PUSH       DE
448F: 2A         LD           A,(HLI)
4490: 5F         LD           E,A
4491: 3A         LD           A,(HLD)
4492: 57         LD           D,A
4493: 13         INC         DE
4494: 13         INC         DE
4495: 18 F1      JR           $4488
4497: 2A         LD           A,(HLI)
4498: 4F         LD           C,A
4499: 3A         LD           A,(HLD)
449A: 47         LD           B,A
449B: 0A         LD           A,(BC)
449C: 47         LD           B,A
449D: C9         RET
449E: E1         POP         HL
449F: 18 31      JR           $44D2
44A1: FA 50 D3   LD           A,($D350)
44A4: FE 03      CP           $03
44A6: 20 10      JR           NZ,$44B8
44A8: FA 38 D3   LD           A,($D338)
44AB: CB 7F      BIT         1,E
44AD: 28 09      JR           Z,$44B8
44AF: 7E         LD           A,(HL)
44B0: FE 06      CP           $06
44B2: 20 04      JR           NZ,$44B8
44B4: 3E 40      LD           A,$40
44B6: E0 1C      LDFF00   ($1C),A
44B8: E5         PUSH       HL
44B9: 7D         LD           A,L
44BA: C6 09      ADD         $09
44BC: 6F         LD           L,A
44BD: 7E         LD           A,(HL)
44BE: A7         AND         A
44BF: 20 DD      JR           NZ,$449E
44C1: 7D         LD           A,L
44C2: C6 04      ADD         $04
44C4: 6F         LD           L,A
44C5: CB 7E      BIT         1,E
44C7: 20 D5      JR           NZ,$449E
44C9: E1         POP         HL
44CA: CD 6D 47   CALL       $476D
44CD: E5         PUSH       HL
44CE: CD F1 47   CALL       $47F1
44D1: E1         POP         HL
44D2: 2D         DEC         L
44D3: 2D         DEC         L
44D4: C3 4D 47   JP           $474D
44D7: 2D         DEC         L
44D8: 2D         DEC         L
44D9: 2D         DEC         L
44DA: 2D         DEC         L
44DB: CD 8E 44   CALL       $448E
44DE: 7D         LD           A,L
44DF: C6 04      ADD         $04
44E1: 5F         LD           E,A
44E2: 54         LD           D,H
44E3: CD AA 43   CALL       $43AA
44E6: FE 00      CP           $00
44E8: 28 1F      JR           Z,$4509
44EA: FE FF      CP           $FF
44EC: 28 04      JR           Z,$44F2
44EE: 2C         INC         L
44EF: C3 9E 45   JP           $459E
44F2: 2D         DEC         L
44F3: E5         PUSH       HL
44F4: CD 8E 44   CALL       $448E
44F7: CD 97 44   CALL       $4497
44FA: 5F         LD           E,A
44FB: CD 82 44   CALL       $4482
44FE: CD 97 44   CALL       $4497
4501: 57         LD           D,A
4502: E1         POP         HL
4503: 7B         LD           A,E
4504: 22         LD           (HLI),A
4505: 7A         LD           A,D
4506: 32         LD           (HLD),A
4507: 18 D5      JR           $44DE
4509: FA CA D3   LD           A,($D3CA)
450C: FE 15      CP           $15
450E: CA 4F 48   JP           Z,$484F
4511: 21 69 D3   LD           HL,$D369
4514: 36 00      LD           (HL),$00
4516: CD 37 41   CALL       $4137
4519: C9         RET
451A: CD 82 44   CALL       $4482
451D: CD 97 44   CALL       $4497
4520: EA 01 D3   LD           ($D301),A
4523: CD 82 44   CALL       $4482
4526: CD 97 44   CALL       $4497
4529: EA 02 D3   LD           ($D302),A
452C: 18 09      JR           $4537
452E: CD 82 44   CALL       $4482
4531: CD 97 44   CALL       $4497
4534: EA 00 D3   LD           ($D300),A
4537: CD 82 44   CALL       $4482
453A: 18 64      JR           $45A0
453C: CD 82 44   CALL       $4482
453F: CD 97 44   CALL       $4497
4542: E5         PUSH       HL
4543: 7D         LD           A,L
4544: C6 0B      ADD         $0B
4546: 6F         LD           L,A
4547: 4E         LD           C,(HL)
4548: 78         LD           A,B
4549: B1         OR           C
454A: 77         LD           (HL),A
454B: 44         LD           B,H
454C: 4D         LD           C,L
454D: 0D         DEC         C
454E: 0D         DEC         C
454F: E1         POP         HL
4550: 2A         LD           A,(HLI)
4551: 5F         LD           E,A
4552: 3A         LD           A,(HLD)
4553: 57         LD           D,A
4554: 13         INC         DE
4555: 7B         LD           A,E
4556: 22         LD           (HLI),A
4557: 7A         LD           A,D
4558: 32         LD           (HLD),A
4559: 7A         LD           A,D
455A: 02         LD           (BC),A
455B: 0D         DEC         C
455C: 7B         LD           A,E
455D: 02         LD           (BC),A
455E: 18 40      JR           $45A0
4560: E5         PUSH       HL
4561: 7D         LD           A,L
4562: C6 0B      ADD         $0B
4564: 6F         LD           L,A
4565: 7E         LD           A,(HL)
4566: 35         DEC         (HL)
4567: 7E         LD           A,(HL)
4568: E6 7F      AND         $7F
456A: 28 0D      JR           Z,$4579
456C: 44         LD           B,H
456D: 4D         LD           C,L
456E: 0D         DEC         C
456F: 0D         DEC         C
4570: 0D         DEC         C
4571: E1         POP         HL
4572: 0A         LD           A,(BC)
4573: 22         LD           (HLI),A
4574: 0C         INC         C
4575: 0A         LD           A,(BC)
4576: 32         LD           (HLD),A
4577: 18 27      JR           $45A0
4579: E1         POP         HL
457A: 18 BB      JR           $4537
457C: 21 69 D3   LD           HL,$D369
457F: 7E         LD           A,(HL)
4580: A7         AND         A
4581: C8         RET         Z
4582: FA CE D3   LD           A,($D3CE)
4585: A7         AND         A
4586: C2 2B 40   JP           NZ,$402B
4589: CD 82 43   CALL       $4382
458C: 3E 01      LD           A,$01
458E: EA 50 D3   LD           ($D350),A
4591: 21 10 D3   LD           HL,$D310
4594: 2C         INC         L
4595: 2A         LD           A,(HLI)
4596: A7         AND         A
4597: CA D2 44   JP           Z,$44D2
459A: 35         DEC         (HL)
459B: C2 A1 44   JP           NZ,$44A1
459E: 2C         INC         L
459F: 2C         INC         L
45A0: CD 97 44   CALL       $4497
45A3: FE 00      CP           $00
45A5: CA D7 44   JP           Z,$44D7
45A8: FE 9D      CP           $9D
45AA: CA 52 44   JP           Z,$4452
45AD: FE 9E      CP           $9E
45AF: CA 1A 45   JP           Z,$451A
45B2: FE 9F      CP           $9F
45B4: CA 2E 45   JP           Z,$452E
45B7: FE 9B      CP           $9B
45B9: CA 3C 45   JP           Z,$453C
45BC: FE 9C      CP           $9C
45BE: CA 60 45   JP           Z,$4560
45C1: FE 99      CP           $99
45C3: CA 69 48   JP           Z,$4869
45C6: FE 9A      CP           $9A
45C8: CA 74 48   JP           Z,$4874
45CB: FE 94      CP           $94
45CD: CA B3 48   JP           Z,$48B3
45D0: FE 97      CP           $97
45D2: CA E8 48   JP           Z,$48E8
45D5: FE 98      CP           $98
45D7: CA F7 48   JP           Z,$48F7
45DA: FE 96      CP           $96
45DC: CA 5B 48   JP           Z,$485B
45DF: FE 95      CP           $95
45E1: CA 66 48   JP           Z,$4866
45E4: E6 F0      AND         $F0
45E6: FE A0      CP           $A0
45E8: 20 4D      JR           NZ,$4637
45EA: 78         LD           A,B
45EB: E6 0F      AND         $0F
45ED: 4F         LD           C,A
45EE: 06 00      LD           B,$00
45F0: E5         PUSH       HL
45F1: 11 01 D3   LD           DE,$D301
45F4: 1A         LD           A,(DE)
45F5: 6F         LD           L,A
45F6: 1C         INC         E
45F7: 1A         LD           A,(DE)
45F8: 67         LD           H,A
45F9: 09         ADD         HL,BC
45FA: 7E         LD           A,(HL)
45FB: E1         POP         HL
45FC: E5         PUSH       HL
45FD: 57         LD           D,A
45FE: 2C         INC         L
45FF: 2C         INC         L
4600: 2C         INC         L
4601: 7E         LD           A,(HL)
4602: E6 F0      AND         $F0
4604: 20 03      JR           NZ,$4609
4606: 7A         LD           A,D
4607: 18 25      JR           $462E
4609: 5F         LD           E,A
460A: 7A         LD           A,D
460B: F5         PUSH       AF
460C: CB 3F      SRL         1,E
460E: CB 23      SLA         1,E
4610: 38 08      JR           C,$461A
4612: 57         LD           D,A
4613: CB 3F      SRL         1,E
4615: CB 23      SLA         1,E
4617: 38 01      JR           C,$461A
4619: 82         ADD         A,D
461A: 4F         LD           C,A
461B: A7         AND         A
461C: 20 02      JR           NZ,$4620
461E: 0E 02      LD           C,$02
4620: 11 50 D3   LD           DE,$D350
4623: 1A         LD           A,(DE)
4624: 3D         DEC         A
4625: 5F         LD           E,A
4626: 16 00      LD           D,$00
4628: 21 07 D3   LD           HL,$D307
462B: 19         ADD         HL,DE
462C: 71         LD           (HL),C
462D: F1         POP         AF
462E: E1         POP         HL
462F: 2D         DEC         L
4630: 22         LD           (HLI),A
4631: CD 82 44   CALL       $4482
4634: CD 97 44   CALL       $4497
4637: FA 50 D3   LD           A,($D350)
463A: FE 04      CP           $04
463C: 28 38      JR           Z,$4676
463E: D5         PUSH       DE
463F: 11 B0 D3   LD           DE,$D3B0
4642: CD 37 49   CALL       $4937
4645: AF         XOR         A
4646: 12         LD           (DE),A
4647: 1C         INC         E
4648: 12         LD           (DE),A
4649: 11 B6 D3   LD           DE,$D3B6
464C: CD 37 49   CALL       $4937
464F: 1C         INC         E
4650: AF         XOR         A
4651: 12         LD           (DE),A
4652: FA 50 D3   LD           A,($D350)
4655: FE 03      CP           $03
4657: 20 1C      JR           NZ,$4675
4659: 11 9E D3   LD           DE,$D39E
465C: 1A         LD           A,(DE)
465D: A7         AND         A
465E: 28 07      JR           Z,$4667
4660: 3E 01      LD           A,$01
4662: 12         LD           (DE),A
4663: AF         XOR         A
4664: EA 9F D3   LD           ($D39F),A
4667: 11 D9 D3   LD           DE,$D3D9
466A: 1A         LD           A,(DE)
466B: A7         AND         A
466C: 28 07      JR           Z,$4675
466E: 3E 01      LD           A,$01
4670: 12         LD           (DE),A
4671: AF         XOR         A
4672: EA DA D3   LD           ($D3DA),A
4675: D1         POP         DE
4676: 48         LD           C,B
4677: 06 00      LD           B,$00
4679: CD 82 44   CALL       $4482
467C: FA 50 D3   LD           A,($D350)
467F: FE 04      CP           $04
4681: CA B8 46   JP           Z,$46B8
4684: E5         PUSH       HL
4685: 7D         LD           A,L
4686: C6 05      ADD         $05
4688: 6F         LD           L,A
4689: 5D         LD           E,L
468A: 54         LD           D,H
468B: 2C         INC         L
468C: 2C         INC         L
468D: 79         LD           A,C
468E: FE 01      CP           $01
4690: 28 21      JR           Z,$46B3
4692: 36 00      LD           (HL),$00
4694: FA 00 D3   LD           A,($D300)
4697: A7         AND         A
4698: 28 0C      JR           Z,$46A6
469A: 6F         LD           L,A
469B: 26 00      LD           H,$00
469D: CB 7D      BIT         1,E
469F: 28 02      JR           Z,$46A3
46A1: 26 FF      LD           H,$FF
46A3: 09         ADD         HL,BC
46A4: 44         LD           B,H
46A5: 4D         LD           C,L
46A6: 21 BA 49   LD           HL,$49BA
46A9: 09         ADD         HL,BC
46AA: 2A         LD           A,(HLI)
46AB: 12         LD           (DE),A
46AC: 1C         INC         E
46AD: 7E         LD           A,(HL)
46AE: 12         LD           (DE),A
46AF: E1         POP         HL
46B0: C3 E9 46   JP           $46E9
46B3: 36 01      LD           (HL),$01
46B5: E1         POP         HL
46B6: 18 31      JR           $46E9
46B8: E5         PUSH       HL
46B9: 79         LD           A,C
46BA: FE FF      CP           $FF
46BC: 28 18      JR           Z,$46D6
46BE: 11 46 D3   LD           DE,$D346
46C1: 21 4C 4A   LD           HL,$4A4C
46C4: 09         ADD         HL,BC
46C5: 2A         LD           A,(HLI)
46C6: 12         LD           (DE),A
46C7: 1C         INC         E
46C8: 7B         LD           A,E
46C9: FE 4B      CP           $4B
46CB: 20 F8      JR           NZ,$46C5
46CD: 0E 20      LD           C,$20
46CF: 21 44 D3   LD           HL,$D344
46D2: 06 00      LD           B,$00
46D4: 18 41      JR           $4717
46D6: FA 4F D3   LD           A,($D34F)
46D9: CB 7F      BIT         1,E
46DB: C2 48 47   JP           NZ,$4748
46DE: 3E 01      LD           A,$01
46E0: EA 78 D3   LD           ($D378),A
46E3: CD 3F 40   CALL       $403F
46E6: C3 48 47   JP           $4748
46E9: E5         PUSH       HL
46EA: 06 00      LD           B,$00
46EC: FA 50 D3   LD           A,($D350)
46EF: FE 01      CP           $01
46F1: 28 21      JR           Z,$4714
46F3: FE 02      CP           $02
46F5: 28 19      JR           Z,$4710
46F7: 0E 1A      LD           C,$1A
46F9: FA 3F D3   LD           A,($D33F)
46FC: CB 7F      BIT         1,E
46FE: 20 05      JR           NZ,$4705
4700: AF         XOR         A
4701: E2         LDFF00   (C),A
4702: 3E 80      LD           A,$80
4704: E2         LDFF00   (C),A
4705: 0C         INC         C
4706: 2C         INC         L
4707: 2C         INC         L
4708: 2C         INC         L
4709: 2C         INC         L
470A: 2A         LD           A,(HLI)
470B: 5F         LD           E,A
470C: 16 00      LD           D,$00
470E: 18 0E      JR           $471E
4710: 0E 16      LD           C,$16
4712: 18 03      JR           $4717
4714: 0E 10      LD           C,$10
4716: 0C         INC         C
4717: 2C         INC         L
4718: 2C         INC         L
4719: 2A         LD           A,(HLI)
471A: 5F         LD           E,A
471B: 2C         INC         L
471C: 2A         LD           A,(HLI)
471D: 57         LD           D,A
471E: E5         PUSH       HL
471F: 2C         INC         L
4720: 2C         INC         L
4721: 2A         LD           A,(HLI)
4722: A7         AND         A
4723: 28 02      JR           Z,$4727
4725: 1E 08      LD           E,$08
4727: 2C         INC         L
4728: 2C         INC         L
4729: 36 00      LD           (HL),$00
472B: 2C         INC         L
472C: 7E         LD           A,(HL)
472D: E1         POP         HL
472E: CB 7F      BIT         1,E
4730: 20 16      JR           NZ,$4748
4732: FA 50 D3   LD           A,($D350)
4735: FE 03      CP           $03
4737: CA 2A 43   JP           Z,$432A
473A: 7A         LD           A,D
473B: B0         OR           B
473C: E2         LDFF00   (C),A
473D: 0C         INC         C
473E: 7B         LD           A,E
473F: E2         LDFF00   (C),A
4740: 0C         INC         C
4741: 2A         LD           A,(HLI)
4742: E2         LDFF00   (C),A
4743: 0C         INC         C
4744: 7E         LD           A,(HL)
4745: F6 80      OR           $80
4747: E2         LDFF00   (C),A
4748: E1         POP         HL
4749: 2D         DEC         L
474A: 3A         LD           A,(HLD)
474B: 32         LD           (HLD),A
474C: 2D         DEC         L
474D: 11 50 D3   LD           DE,$D350
4750: 1A         LD           A,(DE)
4751: FE 04      CP           $04
4753: 28 09      JR           Z,$475E
4755: 3C         INC         A
4756: 12         LD           (DE),A
4757: 3E 10      LD           A,$10
4759: 85         ADD         A,L
475A: 6F         LD           L,A
475B: C3 94 45   JP           $4594
475E: 21 1E D3   LD           HL,$D31E
4761: 34         INC         (HL)
4762: 21 2E D3   LD           HL,$D32E
4765: 34         INC         (HL)
4766: 21 3E D3   LD           HL,$D33E
4769: 34         INC         (HL)
476A: C9         RET
476B: E1         POP         HL
476C: C9         RET
476D: E5         PUSH       HL
476E: 7D         LD           A,L
476F: C6 06      ADD         $06
4771: 6F         LD           L,A
4772: 7E         LD           A,(HL)
4773: E6 0F      AND         $0F
4775: 28 18      JR           Z,$478F
4777: EA 51 D3   LD           ($D351),A
477A: FA 50 D3   LD           A,($D350)
477D: 0E 13      LD           C,$13
477F: FE 01      CP           $01
4781: 28 4E      JR           Z,$47D1
4783: 0E 18      LD           C,$18
4785: FE 02      CP           $02
4787: 28 48      JR           Z,$47D1
4789: 0E 1D      LD           C,$1D
478B: FE 03      CP           $03
478D: 28 42      JR           Z,$47D1
478F: FA 50 D3   LD           A,($D350)
4792: FE 04      CP           $04
4794: CA 6B 47   JP           Z,$476B
4797: 11 B6 D3   LD           DE,$D3B6
479A: CD 37 49   CALL       $4937
479D: 1A         LD           A,(DE)
479E: A7         AND         A
479F: CA B8 47   JP           Z,$47B8
47A2: FA 50 D3   LD           A,($D350)
47A5: 0E 13      LD           C,$13
47A7: FE 01      CP           $01
47A9: CA 00 49   JP           Z,$4900
47AC: 0E 18      LD           C,$18
47AE: FE 02      CP           $02
47B0: CA 00 49   JP           Z,$4900
47B3: 0E 1D      LD           C,$1D
47B5: C3 00 49   JP           $4900
47B8: FA 50 D3   LD           A,($D350)
47BB: FE 03      CP           $03
47BD: C2 6B 47   JP           NZ,$476B
47C0: FA 9E D3   LD           A,($D39E)
47C3: A7         AND         A
47C4: C2 7D 48   JP           NZ,$487D
47C7: FA D9 D3   LD           A,($D3D9)
47CA: A7         AND         A
47CB: C2 BE 48   JP           NZ,$48BE
47CE: C3 6B 47   JP           $476B
47D1: 2C         INC         L
47D2: 2A         LD           A,(HLI)
47D3: 5F         LD           E,A
47D4: 7E         LD           A,(HL)
47D5: E6 0F      AND         $0F
47D7: 57         LD           D,A
47D8: D5         PUSH       DE
47D9: 7D         LD           A,L
47DA: C6 04      ADD         $04
47DC: 6F         LD           L,A
47DD: 46         LD           B,(HL)
47DE: FA 51 D3   LD           A,($D351)
47E1: FE 01      CP           $01
47E3: CA 4D 49   JP           Z,$494D
47E6: 21 FF FF   LD           HL,$FFFF
47E9: D1         POP         DE
47EA: 19         ADD         HL,DE
47EB: CD 26 49   CALL       $4926
47EE: C3 8F 47   JP           $478F
47F1: FA 1B D3   LD           A,($D31B)
47F4: A7         AND         A
47F5: 20 21      JR           NZ,$4818
47F7: FA 17 D3   LD           A,($D317)
47FA: A7         AND         A
47FB: 28 1B      JR           Z,$4818
47FD: E6 0F      AND         $0F
47FF: 47         LD           B,A
4800: 21 07 D3   LD           HL,$D307
4803: FA 1E D3   LD           A,($D31E)
4806: BE         CP           (HL)
4807: 20 0F      JR           NZ,$4818
4809: 0E 12      LD           C,$12
480B: 11 1A D3   LD           DE,$D31A
480E: FA 1F D3   LD           A,($D31F)
4811: CB 7F      BIT         1,E
4813: 20 03      JR           NZ,$4818
4815: CD 3C 48   CALL       $483C
4818: FA 2B D3   LD           A,($D32B)
481B: A7         AND         A
481C: C0         RET         NZ
481D: FA 27 D3   LD           A,($D327)
4820: A7         AND         A
4821: C8         RET         Z
4822: E6 0F      AND         $0F
4824: 47         LD           B,A
4825: 21 08 D3   LD           HL,$D308
4828: FA 2E D3   LD           A,($D32E)
482B: BE         CP           (HL)
482C: C0         RET         NZ
482D: FA 2F D3   LD           A,($D32F)
4830: CB 7F      BIT         1,E
4832: C0         RET         NZ
4833: 0E 17      LD           C,$17
4835: 11 2A D3   LD           DE,$D32A
4838: CD 3C 48   CALL       $483C
483B: C9         RET
483C: C5         PUSH       BC
483D: 05         DEC         B
483E: 48         LD           C,B
483F: 06 00      LD           B,$00
4841: 21 10 4B   LD           HL,$4B10
4844: 09         ADD         HL,BC
4845: 7E         LD           A,(HL)
4846: C1         POP         BC
4847: E2         LDFF00   (C),A
4848: 0C         INC         C
4849: 0C         INC         C
484A: 1A         LD           A,(DE)
484B: F6 80      OR           $80
484D: E2         LDFF00   (C),A
484E: C9         RET
484F: AF         XOR         A
4850: EA CE D3   LD           ($D3CE),A
4853: F0 BF      LD           A,($BF)
4855: EA 68 D3   LD           ($D368),A
4858: C3 1E 40   JP           $401E
485B: 3E 01      LD           A,$01
485D: EA CD D3   LD           ($D3CD),A
4860: CD 82 44   CALL       $4482
4863: C3 A0 45   JP           $45A0
4866: AF         XOR         A
4867: 18 F4      JR           $485D
4869: 3E 01      LD           A,$01
486B: EA 9E D3   LD           ($D39E),A
486E: CD 82 44   CALL       $4482
4871: C3 A0 45   JP           $45A0
4874: AF         XOR         A
4875: EA D9 D3   LD           ($D3D9),A
4878: EA DA D3   LD           ($D3DA),A
487B: 18 EE      JR           $486B
487D: FE 02      CP           $02
487F: CA 6B 47   JP           Z,$476B
4882: 01 9F D3   LD           BC,$D39F
4885: CD AF 48   CALL       $48AF
4888: 0E 1C      LD           C,$1C
488A: 06 40      LD           B,$40
488C: FE 03      CP           $03
488E: 28 1A      JR           Z,$48AA
4890: 06 60      LD           B,$60
4892: FE 05      CP           $05
4894: 28 14      JR           Z,$48AA
4896: FE 0A      CP           $0A
4898: 28 10      JR           Z,$48AA
489A: 06 00      LD           B,$00
489C: FE 07      CP           $07
489E: 28 0A      JR           Z,$48AA
48A0: FE 0D      CP           $0D
48A2: C2 6B 47   JP           NZ,$476B
48A5: 3E 02      LD           A,$02
48A7: EA 9E D3   LD           ($D39E),A
48AA: 78         LD           A,B
48AB: E2         LDFF00   (C),A
48AC: C3 6B 47   JP           $476B
48AF: 0A         LD           A,(BC)
48B0: 3C         INC         A
48B1: 02         LD           (BC),A
48B2: C9         RET
48B3: 3E 01      LD           A,$01
48B5: EA D9 D3   LD           ($D3D9),A
48B8: CD 82 44   CALL       $4482
48BB: C3 A0 45   JP           $45A0
48BE: FE 02      CP           $02
48C0: CA 6B 47   JP           Z,$476B
48C3: 01 DA D3   LD           BC,$D3DA
48C6: CD AF 48   CALL       $48AF
48C9: 0E 1C      LD           C,$1C
48CB: 06 60      LD           B,$60
48CD: FE 03      CP           $03
48CF: CA AA 48   JP           Z,$48AA
48D2: 06 40      LD           B,$40
48D4: FE 05      CP           $05
48D6: CA AA 48   JP           Z,$48AA
48D9: 06 20      LD           B,$20
48DB: FE 06      CP           $06
48DD: C2 6B 47   JP           NZ,$476B
48E0: 3E 02      LD           A,$02
48E2: EA D9 D3   LD           ($D3D9),A
48E5: C3 AA 48   JP           $48AA
48E8: 11 B6 D3   LD           DE,$D3B6
48EB: CD 37 49   CALL       $4937
48EE: 3E 01      LD           A,$01
48F0: 12         LD           (DE),A
48F1: CD 82 44   CALL       $4482
48F4: C3 A0 45   JP           $45A0
48F7: 11 B6 D3   LD           DE,$D3B6
48FA: CD 37 49   CALL       $4937
48FD: AF         XOR         A
48FE: 18 F0      JR           $48F0
4900: 1C         INC         E
4901: 1A         LD           A,(DE)
4902: A7         AND         A
4903: 20 11      JR           NZ,$4916
4905: 3C         INC         A
4906: 12         LD           (DE),A
4907: E1         POP         HL
4908: E5         PUSH       HL
4909: CD 1B 49   CALL       $491B
490C: 21 9C FF   LD           HL,$FF9C
490F: 19         ADD         HL,DE
4910: CD 26 49   CALL       $4926
4913: C3 6B 47   JP           $476B
4916: CD 40 49   CALL       $4940
4919: 18 F1      JR           $490C
491B: 3E 07      LD           A,$07
491D: 85         ADD         A,L
491E: 6F         LD           L,A
491F: 2A         LD           A,(HLI)
4920: 5F         LD           E,A
4921: 7E         LD           A,(HL)
4922: E6 0F      AND         $0F
4924: 57         LD           D,A
4925: C9         RET
4926: 11 A4 D3   LD           DE,$D3A4
4929: CD 37 49   CALL       $4937
492C: 7D         LD           A,L
492D: E2         LDFF00   (C),A
492E: 12         LD           (DE),A
492F: 0C         INC         C
4930: 1C         INC         E
4931: 7C         LD           A,H
4932: E6 0F      AND         $0F
4934: E2         LDFF00   (C),A
4935: 12         LD           (DE),A
4936: C9         RET
4937: FA 50 D3   LD           A,($D350)
493A: 3D         DEC         A
493B: CB 27      SLA         1,E
493D: 83         ADD         A,E
493E: 5F         LD           E,A
493F: C9         RET
4940: 11 A4 D3   LD           DE,$D3A4
4943: CD 37 49   CALL       $4937
4946: 1A         LD           A,(DE)
4947: 6F         LD           L,A
4948: 1C         INC         E
4949: 1A         LD           A,(DE)
494A: 57         LD           D,A
494B: 5D         LD           E,L
494C: C9         RET
494D: D1         POP         DE
494E: 11 B0 D3   LD           DE,$D3B0
4951: CD 37 49   CALL       $4937
4954: 1A         LD           A,(DE)
4955: 3C         INC         A
4956: 12         LD           (DE),A
4957: 1C         INC         E
4958: FE 19      CP           $19
495A: 28 31      JR           Z,$498D
495C: FE 2D      CP           $2D
495E: 28 26      JR           Z,$4986
4960: 1A         LD           A,(DE)
4961: A7         AND         A
4962: CA 8F 47   JP           Z,$478F
4965: 1D         DEC         E
4966: 1A         LD           A,(DE)
4967: D6 19      SUB         $19
4969: CB 27      SLA         1,E
496B: 6F         LD           L,A
496C: 26 00      LD           H,$00
496E: 11 92 49   LD           DE,$4992
4971: 19         ADD         HL,DE
4972: 2A         LD           A,(HLI)
4973: 57         LD           D,A
4974: 7E         LD           A,(HL)
4975: 5F         LD           E,A
4976: E1         POP         HL
4977: E5         PUSH       HL
4978: D5         PUSH       DE
4979: CD 1B 49   CALL       $491B
497C: 62         LD           H,D
497D: 6B         LD           L,E
497E: D1         POP         DE
497F: 19         ADD         HL,DE
4980: CD 26 49   CALL       $4926
4983: C3 8F 47   JP           $478F
4986: 1D         DEC         E
4987: 3E 19      LD           A,$19
4989: 12         LD           (DE),A
498A: 1C         INC         E
498B: 18 D8      JR           $4965
498D: 3E 01      LD           A,$01
498F: 12         LD           (DE),A
4990: 18 D3      JR           $4965
4992: 00         NOP
4993: 00         NOP
4994: 00         NOP
4995: 00         NOP
4996: 00         NOP
4997: 01 00 01   LD           BC,$0100
499A: 00         NOP
499B: 02         LD           (BC),A
499C: 00         NOP
499D: 02         LD           (BC),A
499E: 00         NOP
499F: 00         NOP
49A0: 00         NOP
49A1: 00         NOP
49A2: FF         RST         0X38
49A3: FF         RST         0X38
49A4: FF         RST         0X38
49A5: FF         RST         0X38
49A6: FF         RST         0X38
49A7: FE FF      CP           $FF
49A9: FE 00      CP           $00
49AB: 00         NOP
49AC: 00         NOP
49AD: 01 00 02   LD           BC,$0200
49B0: 00         NOP
49B1: 01 00 00   LD           BC,$0000
49B4: FF         RST         0X38
49B5: FF         RST         0X38
49B6: FF         RST         0X38
49B7: FE FF      CP           $FF
49B9: FF         RST         0X38
49BA: 00         NOP
49BB: 0F         RRCA
49BC: 2C         INC         L
49BD: 00         NOP
49BE: 9C         SBC         H
49BF: 00         NOP
49C0: 06 01      LD           B,$01
49C2: 6B         LD           L,E
49C3: 01 C9 01   LD           BC,$01C9
49C6: 23         INC         HL
49C7: 02         LD           (BC),A
49C8: 77         LD           (HL),A
49C9: 02         LD           (BC),A
49CA: C6 02      ADD         $02
49CC: 12         LD           (DE),A
49CD: 03         INC         BC
49CE: 56         LD           D,(HL)
49CF: 03         INC         BC
49D0: 9B         SBC         E
49D1: 03         INC         BC
49D2: DA 03 16   JP           C,$1603
49D5: 04         INC         B
49D6: 4E         LD           C,(HL)
49D7: 04         INC         B
49D8: 83         ADD         A,E
49D9: 04         INC         B
49DA: B5         OR           L
49DB: 04         INC         B
49DC: E5         PUSH       HL
49DD: 04         INC         B
49DE: 11 05 3B   LD           DE,$3B05
49E1: 05         DEC         B
49E2: 63         LD           H,E
49E3: 05         DEC         B
49E4: 89         ADC         A,C
49E5: 05         DEC         B
49E6: AC         XOR         H
49E7: 05         DEC         B
49E8: CE 05      ADC         $05
49EA: ED                              
49EB: 05         DEC         B
49EC: 0A         LD           A,(BC)
49ED: 06 27      LD           B,$27
49EF: 06 42      LD           B,$42
49F1: 06 5B      LD           B,$5B
49F3: 06 72      LD           B,$72
49F5: 06 89      LD           B,$89
49F7: 06 9E      LD           B,$9E
49F9: 06 B2      LD           B,$B2
49FB: 06 C4      LD           B,$C4
49FD: 06 D6      LD           B,$D6
49FF: 06 E7      LD           B,$E7
4A01: 06 F7      LD           B,$F7
4A03: 06 06      LD           B,$06
4A05: 07         RLCA
4A06: 14         INC         D
4A07: 07         RLCA
4A08: 21 07 2D   LD           HL,$2D07
4A0B: 07         RLCA
4A0C: 39         ADD         HL,SP
4A0D: 07         RLCA
4A0E: 44         LD           B,H
4A0F: 07         RLCA
4A10: 4F         LD           C,A
4A11: 07         RLCA
4A12: 59         LD           E,C
4A13: 07         RLCA
4A14: 62         LD           H,D
4A15: 07         RLCA
4A16: 6B         LD           L,E
4A17: 07         RLCA
4A18: 74         LD           (HL),H
4A19: 07         RLCA
4A1A: 7B         LD           A,E
4A1B: 07         RLCA
4A1C: 83         ADD         A,E
4A1D: 07         RLCA
4A1E: 8A         ADC         A,D
4A1F: 07         RLCA
4A20: 90         SUB         B
4A21: 07         RLCA
4A22: 97         SUB         A
4A23: 07         RLCA
4A24: 9D         SBC         L
4A25: 07         RLCA
4A26: A2         AND         D
4A27: 07         RLCA
4A28: A7         AND         A
4A29: 07         RLCA
4A2A: AC         XOR         H
4A2B: 07         RLCA
4A2C: B1         OR           C
4A2D: 07         RLCA
4A2E: B6         OR           (HL)
4A2F: 07         RLCA
4A30: BA         CP           D
4A31: 07         RLCA
4A32: BE         CP           (HL)
4A33: 07         RLCA
4A34: C1         POP         BC
4A35: 07         RLCA
4A36: C5         PUSH       BC
4A37: 07         RLCA
4A38: C8         RET         Z
4A39: 07         RLCA
4A3A: CB 07      RLC         1,E
4A3C: CE 07      ADC         $07
4A3E: D1         POP         DE
4A3F: 07         RLCA
4A40: D4 07 D6   CALL       NC,$D607
4A43: 07         RLCA
4A44: D9         RETI
4A45: 07         RLCA
4A46: DB                              
4A47: 07         RLCA
4A48: DD                              
4A49: 07         RLCA
4A4A: DF         RST         0X18
4A4B: 07         RLCA
4A4C: 00         NOP
4A4D: 00         NOP
4A4E: 00         NOP
4A4F: 00         NOP
4A50: 00         NOP
4A51: C0         RET         NZ
4A52: 09         ADD         HL,BC
4A53: 00         NOP
4A54: 38 34      JR           C,$4A8A
4A56: C0         RET         NZ
4A57: 19         ADD         HL,DE
4A58: 00         NOP
4A59: 38 33      JR           C,$4A8E
4A5B: C0         RET         NZ
4A5C: 46         LD           B,(HL)
4A5D: 00         NOP
4A5E: 13         INC         DE
4A5F: 10 C0      STOP       $C0
4A61: 23         INC         HL
4A62: 00         NOP
4A63: 20 40      JR           NZ,$4AA5
4A65: 80         ADD         A,B
4A66: 51         LD           D,C
4A67: 00         NOP
4A68: 20 07      JR           NZ,$4A71
4A6A: 80         ADD         A,B
4A6B: A1         AND         C
4A6C: 00         NOP
4A6D: 00         NOP
4A6E: 18 80      JR           $49F0
4A70: F2                              
4A71: 00         NOP
4A72: 00         NOP
4A73: 18 80      JR           $49F5
4A75: 81         ADD         A,C
4A76: 00         NOP
4A77: 3A         LD           A,(HLD)
4A78: 10 C0      STOP       $C0
4A7A: 80         ADD         A,B
4A7B: 00         NOP
4A7C: 00         NOP
4A7D: 10 C0      STOP       $C0
4A7F: 57         LD           D,A
4A80: 00         NOP
4A81: 00         NOP
4A82: 60         LD           H,B
4A83: 80         ADD         A,B
4A84: 10 00      STOP       $00
4A86: 00         NOP
4A87: 10 80      STOP       $80
4A89: 01 02 04   LD           BC,$0402
4A8C: 08 10 20   LD           ($2010),SP
4A8F: 06 0C      LD           B,$0C
4A91: 18 01      JR           $4A94
4A93: 01 01 01   LD           BC,$0101
4A96: 01 30 01   LD           BC,$0130
4A99: 03         INC         BC
4A9A: 06 0C      LD           B,$0C
4A9C: 18 30      JR           $4ACE
4A9E: 09         ADD         HL,BC
4A9F: 12         LD           (DE),A
4AA0: 24         INC         H
4AA1: 02         LD           (BC),A
4AA2: 04         INC         B
4AA3: 08 01 01   LD           ($0101),SP
4AA6: 48         LD           C,B
4AA7: 02         LD           (BC),A
4AA8: 04         INC         B
4AA9: 08 10 20   LD           ($2010),SP
4AAC: 40         LD           B,B
4AAD: 0C         INC         C
4AAE: 18 30      JR           $4AE0
4AB0: 02         LD           (BC),A
4AB1: 05         DEC         B
4AB2: 03         INC         BC
4AB3: 01 01 60   LD           BC,$6001
4AB6: 03         INC         BC
4AB7: 05         DEC         B
4AB8: 0A         LD           A,(BC)
4AB9: 14         INC         D
4ABA: 28 50      JR           Z,$4B0C
4ABC: 0F         RRCA
4ABD: 1E 3C      LD           E,$3C
4ABF: 02         LD           (BC),A
4AC0: 08 10 02   LD           ($0210),SP
4AC3: 01 78 03   LD           BC,$0378
4AC6: 06 0C      LD           B,$0C
4AC8: 18 30      JR           $4AFA
4ACA: 60         LD           H,B
4ACB: 12         LD           (DE),A
4ACC: 24         INC         H
4ACD: 48         LD           C,B
4ACE: 03         INC         BC
4ACF: 08 10 02   LD           ($0210),SP
4AD2: 04         INC         B
4AD3: 90         SUB         B
4AD4: 03         INC         BC
4AD5: 07         RLCA
4AD6: 0E 1C      LD           C,$1C
4AD8: 38 70      JR           C,$4B4A
4ADA: 15         DEC         D
4ADB: 2A         LD           A,(HLI)
4ADC: 54         LD           D,H
4ADD: 04         INC         B
4ADE: 09         ADD         HL,BC
4ADF: 12         LD           (DE),A
4AE0: 02         LD           (BC),A
4AE1: 01 A8 04   LD           BC,$04A8
4AE4: 08 10 20   LD           ($2010),SP
4AE7: 40         LD           B,B
4AE8: 80         ADD         A,B
4AE9: 18 30      JR           $4B1B
4AEB: 60         LD           H,B
4AEC: 04         INC         B
4AED: 02         LD           (BC),A
4AEE: 01 01 00   LD           BC,$0001
4AF1: C0         RET         NZ
4AF2: 04         INC         B
4AF3: 09         ADD         HL,BC
4AF4: 12         LD           (DE),A
4AF5: 24         INC         H
4AF6: 48         LD           C,B
4AF7: 90         SUB         B
4AF8: 1B         DEC         DE
4AF9: 36 6C      LD           (HL),$6C
4AFB: 05         DEC         B
4AFC: 0C         INC         C
4AFD: 18 18      JR           $4B17
4AFF: 06 D8      LD           B,$D8
4B01: 05         DEC         B
4B02: 0A         LD           A,(BC)
4B03: 14         INC         D
4B04: 28 50      JR           Z,$4B56
4B06: A0         AND         B
4B07: 1E 3C      LD           E,$3C
4B09: 78         LD           A,B
4B0A: 05         DEC         B
4B0B: 01 01 01   LD           BC,$0101
4B0E: 01 F0 10   LD           BC,$10F0
4B11: 32         LD           (HLD),A
4B12: 22         LD           (HLI),A
4B13: 47         LD           B,A
4B14: 60         LD           H,B
4B15: 20 00      JR           NZ,$4B17
4B17: 1D         DEC         E
4B18: 4B         LD           C,E
4B19: FF         RST         0X38
4B1A: FF         RST         0X38
4B1B: 17         RLA
4B1C: 4B         LD           C,E
4B1D: 9B         SBC         E
4B1E: 20 AE      JR           NZ,$4ACE
4B20: 01 9C 00   LD           BC,$009C
4B23: 00         NOP
4B24: C5         PUSH       BC
4B25: 4A         LD           C,D
4B26: 3B         DEC         SP
4B27: 4B         LD           C,E
4B28: 43         LD           B,E
4B29: 4B         LD           C,E
4B2A: 4B         LD           C,E
4B2B: 4B         LD           C,E
4B2C: 53         LD           D,E
4B2D: 4B         LD           C,E
4B2E: 00         NOP
4B2F: C5         PUSH       BC
4B30: 4A         LD           C,D
4B31: 39         ADD         HL,SP
4B32: 4B         LD           C,E
4B33: 41         LD           B,C
4B34: 4B         LD           C,E
4B35: 49         LD           C,C
4B36: 4B         LD           C,E
4B37: 51         LD           D,C
4B38: 4B         LD           C,E
4B39: 59         LD           E,C
4B3A: 4B         LD           C,E
4B3B: 60         LD           H,B
4B3C: 4B         LD           C,E
4B3D: FF         RST         0X38
4B3E: FF         RST         0X38
4B3F: 3B         DEC         SP
4B40: 4B         LD           C,E
4B41: 82         ADD         A,D
4B42: 4B         LD           C,E
4B43: 92         SUB         D
4B44: 4B         LD           C,E
4B45: FF         RST         0X38
4B46: FF         RST         0X38
4B47: 43         LD           B,E
4B48: 4B         LD           C,E
4B49: 14         INC         D
4B4A: 4C         LD           C,H
4B4B: 19         ADD         HL,DE
4B4C: 4C         LD           C,H
4B4D: FF         RST         0X38
4B4E: FF         RST         0X38
4B4F: 4B         LD           C,E
4B50: 4B         LD           C,E
4B51: 25         DEC         H
4B52: 4C         LD           C,H
4B53: 2A         LD           A,(HLI)
4B54: 4C         LD           C,H
4B55: FF         RST         0X38
4B56: FF         RST         0X38
4B57: 53         LD           D,E
4B58: 4B         LD           C,E
4B59: A5         AND         L
4B5A: 01 A8 01   LD           BC,$01A8
4B5D: AA         XOR         D
4B5E: 01 00 9D   LD           BC,$9D00
4B61: 10 00      STOP       $00
4B63: 80         ADD         A,B
4B64: 9B         SBC         E
4B65: 04         INC         B
4B66: A1         AND         C
4B67: 7C         LD           A,H
4B68: 76         HALT
4B69: 6E         LD           L,(HL)
4B6A: 64         LD           H,H
4B6B: 9C         SBC         H
4B6C: 9B         SBC         E
4B6D: 04         INC         B
4B6E: 7E         LD           A,(HL)
4B6F: 78         LD           A,B
4B70: 70         LD           (HL),B
4B71: 66         LD           H,(HL)
4B72: 9C         SBC         H
4B73: 9B         SBC         E
4B74: 04         INC         B
4B75: 7C         LD           A,H
4B76: 76         HALT
4B77: 6E         LD           L,(HL)
4B78: 64         LD           H,H
4B79: 9C         SBC         H
4B7A: 9B         SBC         E
4B7B: 04         INC         B
4B7C: 78         LD           A,B
4B7D: 72         LD           (HL),D
4B7E: 6A         LD           L,D
4B7F: 60         LD           H,B
4B80: 9C         SBC         H
4B81: 00         NOP
4B82: 9D         SBC         L
4B83: 60         LD           H,B
4B84: 81         ADD         A,C
4B85: 41         LD           B,C
4B86: AA         XOR         D
4B87: 01 56 60   LD           BC,$6056
4B8A: 6A         LD           L,D
4B8B: 60         LD           H,B
4B8C: 66         LD           H,(HL)
4B8D: A5         AND         L
4B8E: 64         LD           H,H
4B8F: A3         AND         E
4B90: 01 00 9D   LD           BC,$9D00
4B93: 34         INC         (HL)
4B94: 00         NOP
4B95: 00         NOP
4B96: 9B         SBC         E
4B97: 03         INC         BC
4B98: A1         AND         C
4B99: 7C         LD           A,H
4B9A: 76         HALT
4B9B: 6E         LD           L,(HL)
4B9C: 64         LD           H,H
4B9D: 9C         SBC         H
4B9E: 9D         SBC         L
4B9F: 43         LD           B,E
4BA0: 00         NOP
4BA1: 00         NOP
4BA2: 7C         LD           A,H
4BA3: 76         HALT
4BA4: 6E         LD           L,(HL)
4BA5: 64         LD           H,H
4BA6: 9D         SBC         L
4BA7: 62         LD           H,D
4BA8: 00         NOP
4BA9: 00         NOP
4BAA: 7E         LD           A,(HL)
4BAB: 78         LD           A,B
4BAC: 70         LD           (HL),B
4BAD: 66         LD           H,(HL)
4BAE: 9D         SBC         L
4BAF: 43         LD           B,E
4BB0: 00         NOP
4BB1: 00         NOP
4BB2: 7E         LD           A,(HL)
4BB3: 78         LD           A,B
4BB4: 70         LD           (HL),B
4BB5: 66         LD           H,(HL)
4BB6: 9D         SBC         L
4BB7: 34         INC         (HL)
4BB8: 00         NOP
4BB9: 00         NOP
4BBA: 9B         SBC         E
4BBB: 02         LD           (BC),A
4BBC: 7E         LD           A,(HL)
4BBD: 78         LD           A,B
4BBE: 70         LD           (HL),B
4BBF: 66         LD           H,(HL)
4BC0: 9C         SBC         H
4BC1: 9B         SBC         E
4BC2: 02         LD           (BC),A
4BC3: 7C         LD           A,H
4BC4: 76         HALT
4BC5: 6E         LD           L,(HL)
4BC6: 64         LD           H,H
4BC7: 9C         SBC         H
4BC8: 9D         SBC         L
4BC9: 43         LD           B,E
4BCA: 00         NOP
4BCB: 00         NOP
4BCC: 7C         LD           A,H
4BCD: 76         HALT
4BCE: 6E         LD           L,(HL)
4BCF: 64         LD           H,H
4BD0: 9D         SBC         L
4BD1: 62         LD           H,D
4BD2: 00         NOP
4BD3: 00         NOP
4BD4: 7C         LD           A,H
4BD5: 76         HALT
4BD6: 6E         LD           L,(HL)
4BD7: 64         LD           H,H
4BD8: 9D         SBC         L
4BD9: 82         ADD         A,D
4BDA: 00         NOP
4BDB: 00         NOP
4BDC: 78         LD           A,B
4BDD: 72         LD           (HL),D
4BDE: 6A         LD           L,D
4BDF: 60         LD           H,B
4BE0: 9D         SBC         L
4BE1: 62         LD           H,D
4BE2: 00         NOP
4BE3: 00         NOP
4BE4: 78         LD           A,B
4BE5: 72         LD           (HL),D
4BE6: 6A         LD           L,D
4BE7: 60         LD           H,B
4BE8: 9D         SBC         L
4BE9: 43         LD           B,E
4BEA: 00         NOP
4BEB: 00         NOP
4BEC: 9B         SBC         E
4BED: 02         LD           (BC),A
4BEE: 78         LD           A,B
4BEF: 72         LD           (HL),D
4BF0: 6A         LD           L,D
4BF1: 60         LD           H,B
4BF2: 9C         SBC         H
4BF3: 00         NOP
4BF4: 66         LD           H,(HL)
4BF5: 66         LD           H,(HL)
4BF6: 66         LD           H,(HL)
4BF7: 66         LD           H,(HL)
4BF8: 00         NOP
4BF9: 00         NOP
4BFA: 00         NOP
4BFB: 00         NOP
4BFC: 66         LD           H,(HL)
4BFD: 66         LD           H,(HL)
4BFE: 66         LD           H,(HL)
4BFF: 66         LD           H,(HL)
4C00: 00         NOP
4C01: 00         NOP
4C02: 00         NOP
4C03: 00         NOP
4C04: 00         NOP
4C05: 22         LD           (HLI),A
4C06: 44         LD           B,H
4C07: 55         LD           D,L
4C08: 66         LD           H,(HL)
4C09: 66         LD           H,(HL)
4C0A: 88         ADC         A,B
4C0B: 88         ADC         A,B
4C0C: AA         XOR         D
4C0D: AA         XOR         D
4C0E: CC CC 04   CALL       Z,$04CC
4C11: 84         ADD         A,H
4C12: 04         INC         B
4C13: 84         ADD         A,H
4C14: A5         AND         L
4C15: 01 A8 01   LD           BC,$01A8
4C18: 00         NOP
4C19: 9D         SBC         L
4C1A: F4                              
4C1B: 4B         LD           C,E
4C1C: 20 99      JR           NZ,$4BB7
4C1E: 9B         SBC         E
4C1F: 20 A2      JR           NZ,$4BC3
4C21: 04         INC         B
4C22: 1C         INC         E
4C23: 9C         SBC         H
4C24: 00         NOP
4C25: A5         AND         L
4C26: 01 A8 01   LD           BC,$01A8
4C29: 00         NOP
4C2A: 9B         SBC         E
4C2B: 20 A2      JR           NZ,$4BCF
4C2D: 1A         LD           A,(DE)
4C2E: A1         AND         C
4C2F: 1A         LD           A,(DE)
4C30: 1A         LD           A,(DE)
4C31: 9C         SBC         H
4C32: 00         NOP
4C33: 02         LD           (BC),A
4C34: B6         OR           (HL)
4C35: 4A         LD           C,D
4C36: 3E 4C      LD           A,$4C
4C38: 4C         LD           C,H
4C39: 4C         LD           C,H
4C3A: 60         LD           H,B
4C3B: 4C         LD           C,H
4C3C: 66         LD           H,(HL)
4C3D: 4C         LD           C,H
4C3E: 6C         LD           L,H
4C3F: 4C         LD           C,H
4C40: 82         ADD         A,D
4C41: 4C         LD           C,H
4C42: 94         SUB         H
4C43: 4C         LD           C,H
4C44: A6         AND         (HL)
4C45: 4C         LD           C,H
4C46: 94         SUB         H
4C47: 4C         LD           C,H
4C48: FF         RST         0X38
4C49: FF         RST         0X38
4C4A: 40         LD           B,B
4C4B: 4C         LD           C,H
4C4C: 73         LD           (HL),E
4C4D: 4C         LD           C,H
4C4E: 82         ADD         A,D
4C4F: 4C         LD           C,H
4C50: 78         LD           A,B
4C51: 4C         LD           C,H
4C52: 94         SUB         H
4C53: 4C         LD           C,H
4C54: 7D         LD           A,L
4C55: 4C         LD           C,H
4C56: A6         AND         (HL)
4C57: 4C         LD           C,H
4C58: 78         LD           A,B
4C59: 4C         LD           C,H
4C5A: 94         SUB         H
4C5B: 4C         LD           C,H
4C5C: FF         RST         0X38
4C5D: FF         RST         0X38
4C5E: 4C         LD           C,H
4C5F: 4C         LD           C,H
4C60: B8         CP           B
4C61: 4C         LD           C,H
4C62: FF         RST         0X38
4C63: FF         RST         0X38
4C64: 60         LD           H,B
4C65: 4C         LD           C,H
4C66: EB                              
4C67: 4C         LD           C,H
4C68: FF         RST         0X38
4C69: FF         RST         0X38
4C6A: 66         LD           H,(HL)
4C6B: 4C         LD           C,H
4C6C: 9D         SBC         L
4C6D: 43         LD           B,E
4C6E: 00         NOP
4C6F: 03         INC         BC
4C70: A0         AND         B
4C71: 01 00 9D   LD           BC,$9D00
4C74: 43         LD           B,E
4C75: 00         NOP
4C76: 00         NOP
4C77: 00         NOP
4C78: 9D         SBC         L
4C79: 71         LD           (HL),C
4C7A: 00         NOP
4C7B: 00         NOP
4C7C: 00         NOP
4C7D: 9D         SBC         L
4C7E: 91         SUB         C
4C7F: 00         NOP
4C80: 00         NOP
4C81: 00         NOP
4C82: 9B         SBC         E
4C83: 02         LD           (BC),A
4C84: A1         AND         C
4C85: 48         LD           C,B
4C86: 4C         LD           C,H
4C87: 4E         LD           C,(HL)
4C88: A6         AND         (HL)
4C89: 5C         LD           E,H
4C8A: A1         AND         C
4C8B: 48         LD           C,B
4C8C: 4C         LD           C,H
4C8D: 4E         LD           C,(HL)
4C8E: A6         AND         (HL)
4C8F: 5A         LD           E,D
4C90: A3         AND         E
4C91: 01 9C 00   LD           BC,$009C
4C94: 9B         SBC         E
4C95: 02         LD           (BC),A
4C96: A1         AND         C
4C97: 4C         LD           C,H
4C98: 50         LD           D,B
4C99: 52         LD           D,D
4C9A: A6         AND         (HL)
4C9B: 60         LD           H,B
4C9C: A1         AND         C
4C9D: 4C         LD           C,H
4C9E: 50         LD           D,B
4C9F: 52         LD           D,D
4CA0: A6         AND         (HL)
4CA1: 5E         LD           E,(HL)
4CA2: A3         AND         E
4CA3: 01 9C 00   LD           BC,$009C
4CA6: 9B         SBC         E
4CA7: 02         LD           (BC),A
4CA8: A1         AND         C
4CA9: 50         LD           D,B
4CAA: 54         LD           D,H
4CAB: 56         LD           D,(HL)
4CAC: A6         AND         (HL)
4CAD: 64         LD           H,H
4CAE: A1         AND         C
4CAF: 50         LD           D,B
4CB0: 54         LD           D,H
4CB1: 56         LD           D,(HL)
4CB2: A6         AND         (HL)
4CB3: 62         LD           H,D
4CB4: A3         AND         E
4CB5: 01 9C 00   LD           BC,$009C
4CB8: 9D         SBC         L
4CB9: 04         INC         B
4CBA: 4C         LD           C,H
4CBB: 20 99      JR           NZ,$4C56
4CBD: 9B         SBC         E
4CBE: 02         LD           (BC),A
4CBF: A2         AND         D
4CC0: 30 18      JR           NC,$4CDA
4CC2: 18 30      JR           $4CF4
4CC4: 18 18      JR           $4CDE
4CC6: 30 18      JR           NC,$4CE0
4CC8: 9C         SBC         H
4CC9: 9B         SBC         E
4CCA: 02         LD           (BC),A
4CCB: 34         INC         (HL)
4CCC: 1C         INC         E
4CCD: 1C         INC         E
4CCE: 34         INC         (HL)
4CCF: 1C         INC         E
4CD0: 1C         INC         E
4CD1: 34         INC         (HL)
4CD2: 1C         INC         E
4CD3: 9C         SBC         H
4CD4: 9B         SBC         E
4CD5: 02         LD           (BC),A
4CD6: 38 20      JR           C,$4CF8
4CD8: 20 38      JR           NZ,$4D12
4CDA: 20 20      JR           NZ,$4CFC
4CDC: 38 20      JR           C,$4CFE
4CDE: 9C         SBC         H
4CDF: 9B         SBC         E
4CE0: 02         LD           (BC),A
4CE1: 34         INC         (HL)
4CE2: 1C         INC         E
4CE3: 1C         INC         E
4CE4: 34         INC         (HL)
4CE5: 1C         INC         E
4CE6: 1C         INC         E
4CE7: 34         INC         (HL)
4CE8: 1C         INC         E
4CE9: 9C         SBC         H
4CEA: 00         NOP
4CEB: 9B         SBC         E
4CEC: 02         LD           (BC),A
4CED: A1         AND         C
4CEE: 1A         LD           A,(DE)
4CEF: 1A         LD           A,(DE)
4CF0: 1A         LD           A,(DE)
4CF1: A6         AND         (HL)
4CF2: 1A         LD           A,(DE)
4CF3: 9C         SBC         H
4CF4: A1         AND         C
4CF5: 1A         LD           A,(DE)
4CF6: 15         DEC         D
4CF7: 15         DEC         D
4CF8: 15         DEC         D
4CF9: 00         NOP
4CFA: AF         XOR         A
4CFB: EA 79 D3   LD           ($D379),A
4CFE: EA 4F D3   LD           ($D34F),A
4D01: EA 98 D3   LD           ($D398),A
4D04: EA 93 D3   LD           ($D393),A
4D07: EA C9 D3   LD           ($D3C9),A
4D0A: EA A3 D3   LD           ($D3A3),A
4D0D: EA E5 D3   LD           ($D3E5),A
4D10: 3E 08      LD           A,$08
4D12: E0 21      LDFF00   ($21),A
4D14: 3E 80      LD           A,$80
4D16: E0 23      LDFF00   ($23),A
4D18: 3E FF      LD           A,$FF
4D1A: E0 25      LDFF00   ($25),A
4D1C: 3E 03      LD           A,$03
4D1E: EA 55 D3   LD           ($D355),A
4D21: AF         XOR         A
4D22: EA 69 D3   LD           ($D369),A
4D25: AF         XOR         A
4D26: EA 61 D3   LD           ($D361),A
4D29: EA 71 D3   LD           ($D371),A
4D2C: EA 1F D3   LD           ($D31F),A
4D2F: EA 2F D3   LD           ($D32F),A
4D32: EA 3F D3   LD           ($D33F),A
4D35: EA 9E D3   LD           ($D39E),A
4D38: EA 9F D3   LD           ($D39F),A
4D3B: EA D9 D3   LD           ($D3D9),A
4D3E: EA DA D3   LD           ($D3DA),A
4D41: EA B6 D3   LD           ($D3B6),A
4D44: EA B7 D3   LD           ($D3B7),A
4D47: EA B8 D3   LD           ($D3B8),A
4D4A: EA B9 D3   LD           ($D3B9),A
4D4D: EA BA D3   LD           ($D3BA),A
4D50: EA BB D3   LD           ($D3BB),A
4D53: EA 94 D3   LD           ($D394),A
4D56: EA 95 D3   LD           ($D395),A
4D59: EA 96 D3   LD           ($D396),A
4D5C: EA 90 D3   LD           ($D390),A
4D5F: EA 91 D3   LD           ($D391),A
4D62: EA 92 D3   LD           ($D392),A
4D65: EA C6 D3   LD           ($D3C6),A
4D68: EA C7 D3   LD           ($D3C7),A
4D6B: EA C8 D3   LD           ($D3C8),A
4D6E: EA A0 D3   LD           ($D3A0),A
4D71: EA A1 D3   LD           ($D3A1),A
4D74: EA A2 D3   LD           ($D3A2),A
4D77: EA CD D3   LD           ($D3CD),A
4D7A: EA D6 D3   LD           ($D3D6),A
4D7D: EA D7 D3   LD           ($D3D7),A
4D80: EA D8 D3   LD           ($D3D8),A
4D83: EA DC D3   LD           ($D3DC),A
4D86: EA E7 D3   LD           ($D3E7),A
4D89: EA E2 D3   LD           ($D3E2),A
4D8C: EA E3 D3   LD           ($D3E3),A
4D8F: EA E4 D3   LD           ($D3E4),A
4D92: 3E 08      LD           A,$08
4D94: E0 12      LDFF00   ($12),A
4D96: E0 17      LDFF00   ($17),A
4D98: 3E 80      LD           A,$80
4D9A: E0 14      LDFF00   ($14),A
4D9C: E0 19      LDFF00   ($19),A
4D9E: AF         XOR         A
4D9F: E0 10      LDFF00   ($10),A
4DA1: E0 1A      LDFF00   ($1A),A
4DA3: C9         RET
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
5000: 00         NOP
5001: E3                              
5002: 4A         LD           C,D
5003: 0B         DEC         BC
5004: 50         LD           D,B
5005: 2F         CPL
5006: 50         LD           D,B
5007: 53         LD           D,E
5008: 50         LD           D,B
5009: 00         NOP
500A: 00         NOP
500B: 13         INC         DE
500C: 6E         LD           L,(HL)
500D: 6F         LD           L,A
500E: 50         LD           D,B
500F: AC         XOR         H
5010: 6E         LD           L,(HL)
5011: A1         AND         C
5012: 50         LD           D,B
5013: A8         XOR         B
5014: 6E         LD           L,(HL)
5015: 22         LD           (HLI),A
5016: 6E         LD           L,(HL)
5017: A8         XOR         B
5018: 50         LD           D,B
5019: 09         ADD         HL,BC
501A: 6E         LD           L,(HL)
501B: 2A         LD           A,(HLI)
501C: 6D         LD           L,L
501D: 47         LD           B,A
501E: 51         LD           D,C
501F: 47         LD           B,A
5020: 51         LD           D,C
5021: 15         DEC         D
5022: 6D         LD           L,L
5023: B0         OR           B
5024: 6E         LD           L,(HL)
5025: 10 6D      STOP       $6D
5027: 09         ADD         HL,BC
5028: 6E         LD           L,(HL)
5029: 51         LD           D,C
502A: 51         LD           D,C
502B: E3                              
502C: 51         LD           D,C
502D: 00         NOP
502E: 00         NOP
502F: B7         OR           A
5030: 50         LD           D,B
5031: AC         XOR         H
5032: 6E         LD           L,(HL)
5033: FF         RST         0X38
5034: 6D         LD           L,L
5035: ED                              
5036: 50         LD           D,B
5037: A8         XOR         B
5038: 6E         LD           L,(HL)
5039: F2                              
503A: 50         LD           D,B
503B: CD 6D 47   CALL       $476D
503E: 51         LD           D,C
503F: 09         ADD         HL,BC
5040: 6E         LD           L,(HL)
5041: 47         LD           B,A
5042: 51         LD           D,C
5043: 15         DEC         D
5044: 6D         LD           L,L
5045: B0         OR           B
5046: 6E         LD           L,(HL)
5047: BE         CP           (HL)
5048: 6D         LD           L,L
5049: 51         LD           D,C
504A: 51         LD           D,C
504B: 2D         DEC         L
504C: 6D         LD           L,L
504D: 18 6E      JR           $50BD
504F: E3                              
5050: 51         LD           D,C
5051: 00         NOP
5052: 00         NOP
5053: 63         LD           H,E
5054: 6E         LD           L,(HL)
5055: 00         NOP
5056: 51         LD           D,C
5057: AC         XOR         H
5058: 6E         LD           L,(HL)
5059: 31 51 A8   LD           SP,$A851
505C: 6E         LD           L,(HL)
505D: 54         LD           D,H
505E: 6E         LD           L,(HL)
505F: 38 51      JR           C,$50B2
5061: 72         LD           (HL),D
5062: 6E         LD           L,(HL)
5063: 27         DAA
5064: 6D         LD           L,L
5065: 47         LD           B,A
5066: 51         LD           D,C
5067: 77         LD           (HL),A
5068: 6E         LD           L,(HL)
5069: 47         LD           B,A
506A: 51         LD           D,C
506B: FF         RST         0X38
506C: FF         RST         0X38
506D: 30 6D      JR           NC,$50DC
506F: 9B         SBC         E
5070: 02         LD           (BC),A
5071: A2         AND         D
5072: 12         LD           (DE),A
5073: 2A         LD           A,(HLI)
5074: 12         LD           (DE),A
5075: 18 30      JR           $50A7
5077: 9C         SBC         H
5078: 16 2E      LD           D,$2E
507A: 16 1C      LD           D,$1C
507C: 34         INC         (HL)
507D: 16 2E      LD           D,$2E
507F: 14         INC         D
5080: 2C         INC         L
5081: 9B         SBC         E
5082: 02         LD           (BC),A
5083: A2         AND         D
5084: 12         LD           (DE),A
5085: 2A         LD           A,(HLI)
5086: 12         LD           (DE),A
5087: 18 30      JR           $50B9
5089: 9C         SBC         H
508A: 1A         LD           A,(DE)
508B: 32         LD           (HLD),A
508C: 1A         LD           A,(DE)
508D: 20 38      JR           NZ,$50C7
508F: 1A         LD           A,(DE)
5090: 32         LD           (HLD),A
5091: 18 30      JR           $50C3
5093: 9B         SBC         E
5094: 02         LD           (BC),A
5095: 16 2E      LD           D,$2E
5097: 16 1C      LD           D,$1C
5099: 34         INC         (HL)
509A: 9C         SBC         H
509B: 22         LD           (HLI),A
509C: 3A         LD           A,(HLD)
509D: 22         LD           (HLI),A
509E: 28 40      JR           Z,$50E0
50A0: 00         NOP
50A1: A2         AND         D
50A2: 16 2E      LD           D,$2E
50A4: 16 1C      LD           D,$1C
50A6: 34         INC         (HL)
50A7: 00         NOP
50A8: A2         AND         D
50A9: 22         LD           (HLI),A
50AA: 3A         LD           A,(HLD)
50AB: 22         LD           (HLI),A
50AC: 28 40      JR           Z,$50EE
50AE: A2         AND         D
50AF: 2E 46      LD           L,$46
50B1: 2E 34      LD           L,$34
50B3: 4C         LD           C,H
50B4: A5         AND         L
50B5: 01 00 9D   LD           BC,$9D00
50B8: 97         SUB         A
50B9: 86         ADD         A,(HL)
50BA: 80         ADD         A,B
50BB: A7         AND         A
50BC: 42         LD           B,D
50BD: A4         AND         H
50BE: 34         INC         (HL)
50BF: A6         AND         (HL)
50C0: 01 A1 38   LD           BC,$38A1
50C3: 3A         LD           A,(HLD)
50C4: 3E A3      LD           A,$A3
50C6: 40         LD           B,B
50C7: A4         AND         H
50C8: 58         LD           E,B
50C9: A7         AND         A
50CA: 01 42 A4   LD           BC,$A442
50CD: 34         INC         (HL)
50CE: A6         AND         (HL)
50CF: 01 A1 38   LD           BC,$38A1
50D2: 3A         LD           A,(HLD)
50D3: 4C         LD           C,H
50D4: A3         AND         E
50D5: 4A         LD           C,D
50D6: A4         AND         H
50D7: 48         LD           C,B
50D8: A7         AND         A
50D9: 01 9D B7   LD           BC,$B79D
50DC: 86         ADD         A,(HL)
50DD: 80         ADD         A,B
50DE: A7         AND         A
50DF: 46         LD           B,(HL)
50E0: A4         AND         H
50E1: 38 A6      JR           C,$5089
50E3: 01 A1 3E   LD           BC,$3EA1
50E6: 40         LD           B,B
50E7: 42         LD           B,D
50E8: A3         AND         E
50E9: 44         LD           B,H
50EA: A7         AND         A
50EB: 5C         LD           E,H
50EC: 00         NOP
50ED: A3         AND         E
50EE: 32         LD           (HLD),A
50EF: A7         AND         A
50F0: 4A         LD           C,D
50F1: 00         NOP
50F2: 9D         SBC         L
50F3: 89         ADC         A,C
50F4: 86         ADD         A,(HL)
50F5: 81         ADD         A,C
50F6: A3         AND         E
50F7: 48         LD           C,B
50F8: A7         AND         A
50F9: 60         LD           H,B
50FA: A8         XOR         B
50FB: 80         ADD         A,B
50FC: 01 A2 01   LD           BC,$01A2
50FF: 00         NOP
5100: 9B         SBC         E
5101: 02         LD           (BC),A
5102: A2         AND         D
5103: 04         INC         B
5104: 1C         INC         E
5105: 04         INC         B
5106: 0A         LD           A,(BC)
5107: 22         LD           (HLI),A
5108: 9C         SBC         H
5109: 08 20 08   LD           ($0820),SP
510C: 0E 26      LD           C,$26
510E: 08 20 06   LD           ($0620),SP
5111: 1E 9B      LD           E,$9B
5113: 02         LD           (BC),A
5114: 04         INC         B
5115: 1C         INC         E
5116: 04         INC         B
5117: 0A         LD           A,(BC)
5118: 22         LD           (HLI),A
5119: 9C         SBC         H
511A: 0C         INC         C
511B: 24         INC         H
511C: 0C         INC         C
511D: 12         LD           (DE),A
511E: 2A         LD           A,(HLI)
511F: 0C         INC         C
5120: 24         INC         H
5121: 0A         LD           A,(BC)
5122: 22         LD           (HLI),A
5123: 9B         SBC         E
5124: 02         LD           (BC),A
5125: 08 20 08   LD           ($0820),SP
5128: 0E 26      LD           C,$26
512A: 9C         SBC         H
512B: 14         INC         D
512C: 2C         INC         L
512D: 14         INC         D
512E: 1A         LD           A,(DE)
512F: 32         LD           (HLD),A
5130: 00         NOP
5131: A2         AND         D
5132: 08 20 08   LD           ($0820),SP
5135: 0E 26      LD           C,$26
5137: 00         NOP
5138: A2         AND         D
5139: 14         INC         D
513A: 2C         INC         L
513B: 14         INC         D
513C: 1A         LD           A,(DE)
513D: 32         LD           (HLD),A
513E: A2         AND         D
513F: 20 38      JR           NZ,$5179
5141: 20 26      JR           NZ,$5169
5143: 3E A5      LD           A,$A5
5145: 01 00 A1   LD           BC,$A100
5148: 48         LD           C,B
5149: 50         LD           D,B
514A: 54         LD           D,H
514B: 5C         LD           E,H
514C: 60         LD           H,B
514D: 68         LD           L,B
514E: 6C         LD           L,H
514F: 74         LD           (HL),H
5150: 00         NOP
5151: A3         AND         E
5152: 3C         INC         A
5153: 2E 01      LD           L,$01
5155: A1         AND         C
5156: 2E 32      LD           L,$32
5158: 36 38      LD           (HL),$38
515A: A3         AND         E
515B: 01 38 2A   LD           BC,$2A38
515E: A1         AND         C
515F: 2A         LD           A,(HLI)
5160: 2E 32      LD           L,$32
5162: 36 A2      LD           (HL),$A2
5164: 01 6C 5E   LD           BC,$5E6C
5167: 24         INC         H
5168: 16 5E      LD           D,$5E
516A: A1         AND         C
516B: 5E         LD           E,(HL)
516C: 62         LD           H,D
516D: 66         LD           H,(HL)
516E: A6         AND         (HL)
516F: 68         LD           L,B
5170: A2         AND         D
5171: 68         LD           L,B
5172: 5A         LD           E,D
5173: 20 12      JR           NZ,$5187
5175: 5A         LD           E,D
5176: A1         AND         C
5177: 5A         LD           E,D
5178: 5E         LD           E,(HL)
5179: 62         LD           H,D
517A: 66         LD           H,(HL)
517B: A2         AND         D
517C: 01 84 76   LD           BC,$7684
517F: 3C         INC         A
5180: 2E 76      LD           L,$76
5182: A1         AND         C
5183: 76         HALT
5184: 7A         LD           A,D
5185: 7E         LD           A,(HL)
5186: A6         AND         (HL)
5187: 80         ADD         A,B
5188: A2         AND         D
5189: 80         ADD         A,B
518A: 72         LD           (HL),D
518B: 38 2A      JR           C,$51B7
518D: 72         LD           (HL),D
518E: A1         AND         C
518F: 72         LD           (HL),D
5190: 76         HALT
5191: 7A         LD           A,D
5192: 7E         LD           A,(HL)
5193: A2         AND         D
5194: 38 66      JR           C,$51FC
5196: 58         LD           E,B
5197: 38 20      JR           C,$51B9
5199: 58         LD           E,B
519A: A1         AND         C
519B: 58         LD           E,B
519C: 5C         LD           E,H
519D: 5E         LD           E,(HL)
519E: 62         LD           H,D
519F: A2         AND         D
51A0: 36 62      LD           (HL),$62
51A2: 54         LD           D,H
51A3: 6C         LD           L,H
51A4: A1         AND         C
51A5: 36 3C      LD           (HL),$3C
51A7: 44         LD           B,H
51A8: 4A         LD           C,D
51A9: 4E         LD           C,(HL)
51AA: 54         LD           D,H
51AB: 5C         LD           E,H
51AC: 62         LD           H,D
51AD: A2         AND         D
51AE: 32         LD           (HLD),A
51AF: 5E         LD           E,(HL)
51B0: 50         LD           D,B
51B1: 32         LD           (HLD),A
51B2: 4A         LD           C,D
51B3: 50         LD           D,B
51B4: A1         AND         C
51B5: 50         LD           D,B
51B6: 54         LD           D,H
51B7: 58         LD           E,B
51B8: 5C         LD           E,H
51B9: A2         AND         D
51BA: 2E 5C      LD           L,$5C
51BC: 4E         LD           C,(HL)
51BD: 66         LD           H,(HL)
51BE: A1         AND         C
51BF: 2E 36      LD           L,$36
51C1: 3C         INC         A
51C2: 44         LD           B,H
51C3: 46         LD           B,(HL)
51C4: 4E         LD           C,(HL)
51C5: 54         LD           D,H
51C6: 5C         LD           E,H
51C7: A2         AND         D
51C8: 2A         LD           A,(HLI)
51C9: 58         LD           E,B
51CA: A1         AND         C
51CB: 4A         LD           C,D
51CC: 50         LD           D,B
51CD: 58         LD           E,B
51CE: 62         LD           H,D
51CF: A2         AND         D
51D0: 26 54      LD           H,$54
51D2: A1         AND         C
51D3: 46         LD           B,(HL)
51D4: A0         AND         B
51D5: 01 A1 4C   LD           BC,$4CA1
51D8: A0         AND         B
51D9: 01 A1 54   LD           BC,$54A1
51DC: A0         AND         B
51DD: 01 A1 5E   LD           BC,$5EA1
51E0: A4         AND         H
51E1: 01 00 9E   LD           BC,$9E00
51E4: D4 4A A1   CALL       NC,$A14A
51E7: 32         LD           (HLD),A
51E8: 3C         INC         A
51E9: 46         LD           B,(HL)
51EA: 9B         SBC         E
51EB: 02         LD           (BC),A
51EC: 0C         INC         C
51ED: 01 01 9C   LD           BC,$9C01
51F0: 3C         INC         A
51F1: 40         LD           B,B
51F2: 44         LD           B,H
51F3: 46         LD           B,(HL)
51F4: 4A         LD           C,D
51F5: 01 0C 3C   LD           BC,$3C0C
51F8: 46         LD           B,(HL)
51F9: 50         LD           D,B
51FA: 0C         INC         C
51FB: 01 01 0C   LD           BC,$0C01
51FE: 01 46 50   LD           BC,$5046
5201: 5A         LD           E,D
5202: 01 0C 0C   LD           BC,$0C0C
5205: 01 0C 01   LD           BC,$010C
5208: 00         NOP
5209: 00         NOP
520A: D4 4A 14   CALL       NC,$144A
520D: 52         LD           D,D
520E: 1E 52      LD           E,$52
5210: 26 52      LD           H,$52
5212: 2E 52      LD           L,$52
5214: 15         DEC         D
5215: 6D         LD           L,L
5216: E1         POP         HL
5217: 6D         LD           L,L
5218: 53         LD           D,E
5219: 52         LD           D,D
521A: FF         RST         0X38
521B: FF         RST         0X38
521C: 16 52      LD           D,$52
521E: 31 6E 34   LD           SP,$346E
5221: 52         LD           D,D
5222: FF         RST         0X38
5223: FF         RST         0X38
5224: 1E 52      LD           E,$52
5226: 63         LD           H,E
5227: 6E         LD           L,(HL)
5228: 74         LD           (HL),H
5229: 52         LD           D,D
522A: FF         RST         0X38
522B: FF         RST         0X38
522C: 26 52      LD           H,$52
522E: 93         SUB         E
522F: 52         LD           D,D
5230: FF         RST         0X38
5231: FF         RST         0X38
5232: 2E 52      LD           L,$52
5234: A2         AND         D
5235: 46         LD           B,(HL)
5236: 01 A7 3C   LD           BC,$3CA7
5239: A1         AND         C
523A: 46         LD           B,(HL)
523B: 01 46 4A   LD           BC,$4A46
523E: 4E         LD           C,(HL)
523F: 50         LD           D,B
5240: A4         AND         H
5241: 54         LD           D,H
5242: 01 A2 5E   LD           BC,$5EA2
5245: 01 A7 54   LD           BC,$54A7
5248: A1         AND         C
5249: 5E         LD           E,(HL)
524A: 01 5E 62   LD           BC,$625E
524D: 66         LD           H,(HL)
524E: 68         LD           L,B
524F: A4         AND         H
5250: 6C         LD           L,H
5251: 01 00 A2   LD           BC,$A200
5254: 2A         LD           A,(HLI)
5255: 01 A7 20   LD           BC,$20A7
5258: A1         AND         C
5259: 2A         LD           A,(HLI)
525A: 01 2A 2E   LD           BC,$2E2A
525D: 32         LD           (HLD),A
525E: 38 3E      JR           C,$529E
5260: A6         AND         (HL)
5261: 01 A5 01   LD           BC,$01A5
5264: A2         AND         D
5265: 42         LD           B,D
5266: 01 A3 38   LD           BC,$38A3
5269: A1         AND         C
526A: 42         LD           B,D
526B: 38 32      JR           C,$529F
526D: 2A         LD           A,(HLI)
526E: 2E A6      LD           L,$A6
5270: 01 A8 01   LD           BC,$01A8
5273: 00         NOP
5274: 9B         SBC         E
5275: 02         LD           (BC),A
5276: 99         SBC         C
5277: A2         AND         D
5278: 16 16      LD           D,$16
527A: 01 16 9C   LD           BC,$9C16
527D: 9B         SBC         E
527E: 02         LD           (BC),A
527F: 12         LD           (DE),A
5280: 12         LD           (DE),A
5281: 01 12 9C   LD           BC,$9C12
5284: 9B         SBC         E
5285: 02         LD           (BC),A
5286: 0E 0E      LD           C,$0E
5288: 01 0E 9C   LD           BC,$9C0E
528B: 9B         SBC         E
528C: 02         LD           (BC),A
528D: 12         LD           (DE),A
528E: 12         LD           (DE),A
528F: 01 12 9C   LD           BC,$9C12
5292: 00         NOP
5293: 9B         SBC         E
5294: 07         RLCA
5295: A2         AND         D
5296: 1A         LD           A,(DE)
5297: A1         AND         C
5298: 1A         LD           A,(DE)
5299: 1A         LD           A,(DE)
529A: 9C         SBC         H
529B: 9B         SBC         E
529C: 04         INC         B
529D: 1A         LD           A,(DE)
529E: 9C         SBC         H
529F: 9B         SBC         E
52A0: 06 A2      LD           B,$A2
52A2: 1A         LD           A,(DE)
52A3: A1         AND         C
52A4: 1A         LD           A,(DE)
52A5: 1A         LD           A,(DE)
52A6: 9C         SBC         H
52A7: 9B         SBC         E
52A8: 08 1A 9C   LD           ($9C1A),SP
52AB: 00         NOP
52AC: 00         NOP
52AD: E3                              
52AE: 4A         LD           C,D
52AF: 17         RLA
52B0: 4B         LD           C,E
52B1: B7         OR           A
52B2: 52         LD           D,D
52B3: 17         RLA
52B4: 4B         LD           C,E
52B5: 00         NOP
52B6: 00         NOP
52B7: 2C         INC         L
52B8: 6E         LD           L,(HL)
52B9: DA 53 FF   JP           C,$FF53
52BC: FF         RST         0X38
52BD: B7         OR           A
52BE: 52         LD           D,D
52BF: 00         NOP
52C0: A7         AND         A
52C1: 4A         LD           C,D
52C2: F0 52      LD           A,($52)
52C4: CA 52 9A   JP           Z,$9A52
52C7: 53         LD           D,E
52C8: BE         CP           (HL)
52C9: 53         LD           D,E
52CA: E1         POP         HL
52CB: 6D         LD           L,L
52CC: CE 53      ADC         $53
52CE: A0         AND         B
52CF: 6E         LD           L,(HL)
52D0: 15         DEC         D
52D1: 6D         LD           L,L
52D2: AC         XOR         H
52D3: 6E         LD           L,(HL)
52D4: 27         DAA
52D5: 6D         LD           L,L
52D6: EB                              
52D7: 6D         LD           L,L
52D8: 98         SBC         B
52D9: 54         LD           D,H
52DA: D7         RST         0X10
52DB: 54         LD           D,H
52DC: D7         RST         0X10
52DD: 54         LD           D,H
52DE: D7         RST         0X10
52DF: 54         LD           D,H
52E0: DE 54      SBC         $54
52E2: 98         SBC         B
52E3: 54         LD           D,H
52E4: D7         RST         0X10
52E5: 54         LD           D,H
52E6: D7         RST         0X10
52E7: 54         LD           D,H
52E8: D7         RST         0X10
52E9: 54         LD           D,H
52EA: DE 54      SBC         $54
52EC: FF         RST         0X38
52ED: FF         RST         0X38
52EE: 3B         DEC         SP
52EF: 55         LD           D,L
52F0: 7C         LD           A,H
52F1: 6E         LD           L,(HL)
52F2: D2 6D 11   JP           NC,$116D
52F5: 54         LD           D,H
52F6: A0         AND         B
52F7: 6E         LD           L,(HL)
52F8: 15         DEC         D
52F9: 6D         LD           L,L
52FA: AC         XOR         H
52FB: 6E         LD           L,(HL)
52FC: 27         DAA
52FD: 6D         LD           L,L
52FE: 40         LD           B,B
52FF: 6E         LD           L,(HL)
5300: 2A         LD           A,(HLI)
5301: 54         LD           D,H
5302: 3B         DEC         SP
5303: 54         LD           D,H
5304: 2A         LD           A,(HLI)
5305: 6D         LD           L,L
5306: 3B         DEC         SP
5307: 54         LD           D,H
5308: 40         LD           B,B
5309: 6E         LD           L,(HL)
530A: 50         LD           D,B
530B: 54         LD           D,H
530C: 3B         DEC         SP
530D: 54         LD           D,H
530E: 40         LD           B,B
530F: 6E         LD           L,(HL)
5310: 61         LD           H,C
5311: 54         LD           D,H
5312: 3B         DEC         SP
5313: 54         LD           D,H
5314: 40         LD           B,B
5315: 6E         LD           L,(HL)
5316: 2A         LD           A,(HLI)
5317: 54         LD           D,H
5318: 3B         DEC         SP
5319: 54         LD           D,H
531A: 2A         LD           A,(HLI)
531B: 6D         LD           L,L
531C: 3B         DEC         SP
531D: 54         LD           D,H
531E: 40         LD           B,B
531F: 6E         LD           L,(HL)
5320: 50         LD           D,B
5321: 54         LD           D,H
5322: 3B         DEC         SP
5323: 54         LD           D,H
5324: 40         LD           B,B
5325: 6E         LD           L,(HL)
5326: 61         LD           H,C
5327: 54         LD           D,H
5328: 3B         DEC         SP
5329: 54         LD           D,H
532A: 91         SUB         C
532B: 6E         LD           L,(HL)
532C: 40         LD           B,B
532D: 6E         LD           L,(HL)
532E: 72         LD           (HL),D
532F: 54         LD           D,H
5330: 3B         DEC         SP
5331: 54         LD           D,H
5332: 2A         LD           A,(HLI)
5333: 6D         LD           L,L
5334: 3B         DEC         SP
5335: 54         LD           D,H
5336: F0 6D      LD           A,($6D)
5338: 7C         LD           A,H
5339: 6E         LD           L,(HL)
533A: AB         XOR         E
533B: 54         LD           D,H
533C: 94         SUB         H
533D: 6E         LD           L,(HL)
533E: AB         XOR         E
533F: 54         LD           D,H
5340: 8E         ADC         A,(HL)
5341: 6E         LD           L,(HL)
5342: BA         CP           D
5343: 54         LD           D,H
5344: 7C         LD           A,H
5345: 6E         LD           L,(HL)
5346: F0 6D      LD           A,($6D)
5348: C2 54 40   JP           NZ,$4054
534B: 6E         LD           L,(HL)
534C: 2A         LD           A,(HLI)
534D: 54         LD           D,H
534E: 3B         DEC         SP
534F: 54         LD           D,H
5350: 2A         LD           A,(HLI)
5351: 6D         LD           L,L
5352: 3B         DEC         SP
5353: 54         LD           D,H
5354: 40         LD           B,B
5355: 6E         LD           L,(HL)
5356: 50         LD           D,B
5357: 54         LD           D,H
5358: 3B         DEC         SP
5359: 54         LD           D,H
535A: 40         LD           B,B
535B: 6E         LD           L,(HL)
535C: 61         LD           H,C
535D: 54         LD           D,H
535E: 3B         DEC         SP
535F: 54         LD           D,H
5360: 40         LD           B,B
5361: 6E         LD           L,(HL)
5362: 2A         LD           A,(HLI)
5363: 54         LD           D,H
5364: 3B         DEC         SP
5365: 54         LD           D,H
5366: 2A         LD           A,(HLI)
5367: 6D         LD           L,L
5368: 3B         DEC         SP
5369: 54         LD           D,H
536A: 40         LD           B,B
536B: 6E         LD           L,(HL)
536C: 50         LD           D,B
536D: 54         LD           D,H
536E: 3B         DEC         SP
536F: 54         LD           D,H
5370: 40         LD           B,B
5371: 6E         LD           L,(HL)
5372: 61         LD           H,C
5373: 54         LD           D,H
5374: 3B         DEC         SP
5375: 54         LD           D,H
5376: 91         SUB         C
5377: 6E         LD           L,(HL)
5378: 40         LD           B,B
5379: 6E         LD           L,(HL)
537A: 72         LD           (HL),D
537B: 54         LD           D,H
537C: 3B         DEC         SP
537D: 54         LD           D,H
537E: 2A         LD           A,(HLI)
537F: 6D         LD           L,L
5380: 3B         DEC         SP
5381: 54         LD           D,H
5382: F0 6D      LD           A,($6D)
5384: 7C         LD           A,H
5385: 6E         LD           L,(HL)
5386: AB         XOR         E
5387: 54         LD           D,H
5388: 94         SUB         H
5389: 6E         LD           L,(HL)
538A: AB         XOR         E
538B: 54         LD           D,H
538C: 8E         ADC         A,(HL)
538D: 6E         LD           L,(HL)
538E: BA         CP           D
538F: 54         LD           D,H
5390: 7C         LD           A,H
5391: 6E         LD           L,(HL)
5392: E1         POP         HL
5393: 6D         LD           L,L
5394: C2 54 FF   JP           NZ,$FF54
5397: FF         RST         0X38
5398: 31 55 54   LD           SP,$5455
539B: 6E         LD           L,(HL)
539C: 1D         DEC         E
539D: 54         LD           D,H
539E: A0         AND         B
539F: 6E         LD           L,(HL)
53A0: 15         DEC         D
53A1: 6D         LD           L,L
53A2: AC         XOR         H
53A3: 6E         LD           L,(HL)
53A4: 27         DAA
53A5: 6D         LD           L,L
53A6: 59         LD           E,C
53A7: 6E         LD           L,(HL)
53A8: 82         ADD         A,D
53A9: 54         LD           D,H
53AA: F3         DI
53AB: 54         LD           D,H
53AC: 54         LD           D,H
53AD: 6E         LD           L,(HL)
53AE: 08 55 59   LD           ($5955),SP
53B1: 6E         LD           L,(HL)
53B2: 82         ADD         A,D
53B3: 54         LD           D,H
53B4: F3         DI
53B5: 54         LD           D,H
53B6: 54         LD           D,H
53B7: 6E         LD           L,(HL)
53B8: 08 55 FF   LD           ($FF55),SP
53BB: FF         RST         0X38
53BC: 45         LD           B,L
53BD: 55         LD           D,L
53BE: 18 55      JR           $5415
53C0: A0         AND         B
53C1: 6E         LD           L,(HL)
53C2: 2D         DEC         L
53C3: 60         LD           H,B
53C4: AC         XOR         H
53C5: 6E         LD           L,(HL)
53C6: 1D         DEC         E
53C7: 55         LD           D,L
53C8: 20 55      JR           NZ,$541F
53CA: FF         RST         0X38
53CB: FF         RST         0X38
53CC: C8         RET         Z
53CD: 53         LD           D,E
53CE: A2         AND         D
53CF: 4E         LD           C,(HL)
53D0: 4C         LD           C,H
53D1: 4A         LD           C,D
53D2: 48         LD           C,B
53D3: 4E         LD           C,(HL)
53D4: 50         LD           D,B
53D5: 52         LD           D,D
53D6: 54         LD           D,H
53D7: A3         AND         E
53D8: 01 00 9B   LD           BC,$9B00
53DB: 06 A0      LD           B,$A0
53DD: 48         LD           C,B
53DE: 46         LD           B,(HL)
53DF: 9C         SBC         H
53E0: 9B         SBC         E
53E1: 0A         LD           A,(BC)
53E2: 46         LD           B,(HL)
53E3: 44         LD           B,H
53E4: 9C         SBC         H
53E5: 9D         SBC         L
53E6: 68         LD           L,B
53E7: 00         NOP
53E8: 81         ADD         A,C
53E9: 9B         SBC         E
53EA: 06 44      LD           B,$44
53EC: 42         LD           B,D
53ED: 9C         SBC         H
53EE: 9B         SBC         E
53EF: 0A         LD           A,(BC)
53F0: 42         LD           B,D
53F1: 40         LD           B,B
53F2: 9C         SBC         H
53F3: 9D         SBC         L
53F4: A8         XOR         B
53F5: 00         NOP
53F6: 81         ADD         A,C
53F7: 9B         SBC         E
53F8: 06 A0      LD           B,$A0
53FA: 4C         LD           C,H
53FB: 4A         LD           C,D
53FC: 9C         SBC         H
53FD: 9B         SBC         E
53FE: 0A         LD           A,(BC)
53FF: 4A         LD           C,D
5400: 48         LD           C,B
5401: 9C         SBC         H
5402: 9D         SBC         L
5403: 78         LD           A,B
5404: 00         NOP
5405: 81         ADD         A,C
5406: 9B         SBC         E
5407: 06 48      LD           B,$48
5409: 46         LD           B,(HL)
540A: 9C         SBC         H
540B: 9B         SBC         E
540C: 0A         LD           A,(BC)
540D: 46         LD           B,(HL)
540E: 44         LD           B,H
540F: 9C         SBC         H
5410: 00         NOP
5411: A2         AND         D
5412: 54         LD           D,H
5413: 52         LD           D,D
5414: 50         LD           D,B
5415: 4E         LD           C,(HL)
5416: 54         LD           D,H
5417: 56         LD           D,(HL)
5418: 58         LD           E,B
5419: 5A         LD           E,D
541A: A3         AND         E
541B: 01 00 99   LD           BC,$9900
541E: A2         AND         D
541F: 5A         LD           E,D
5420: 58         LD           E,B
5421: 56         LD           D,(HL)
5422: 54         LD           D,H
5423: 5A         LD           E,D
5424: 5C         LD           E,H
5425: 5E         LD           E,(HL)
5426: 60         LD           H,B
5427: A3         AND         E
5428: 01 00 A1   LD           BC,$A100
542B: 40         LD           B,B
542C: 44         LD           B,H
542D: 01 A5 46   LD           BC,$46A5
5430: A7         AND         A
5431: 01 A1 40   LD           BC,$40A1
5434: 44         LD           B,H
5435: 01 46 A2   LD           BC,$A246
5438: 01 4C 00   LD           BC,$004C
543B: 9D         SBC         L
543C: 92         SUB         D
543D: 00         NOP
543E: C0         RET         NZ
543F: A1         AND         C
5440: 10 01      STOP       $01
5442: 10 28      STOP       $28
5444: 01 1A 1C   LD           BC,$1C1A
5447: 01 10 01   LD           BC,$0110
544A: 12         LD           (DE),A
544B: 01 12 04   LD           BC,$0412
544E: 01 00 A1   LD           BC,$A100
5451: 01 A2 5E   LD           BC,$5EA2
5454: A1         AND         C
5455: 01 5E 01   LD           BC,$015E
5458: A9         XOR         C
5459: 5E         LD           E,(HL)
545A: A0         AND         B
545B: 01 A4 5E   LD           BC,$5EA4
545E: A2         AND         D
545F: 01 00 A1   LD           BC,$A100
5462: 01 A2 64   LD           BC,$64A2
5465: A1         AND         C
5466: 01 64 01   LD           BC,$0164
5469: A9         XOR         C
546A: 64         LD           H,H
546B: A0         AND         B
546C: 01 A4 64   LD           BC,$64A4
546F: A2         AND         D
5470: 01 00 A1   LD           BC,$A100
5473: 40         LD           B,B
5474: 44         LD           B,H
5475: 01 A5 46   LD           BC,$46A5
5478: A4         AND         H
5479: 01 A1 01   LD           BC,$01A1
547C: 40         LD           B,B
547D: 44         LD           B,H
547E: 46         LD           B,(HL)
547F: 50         LD           D,B
5480: 4E         LD           C,(HL)
5481: 00         NOP
5482: 9B         SBC         E
5483: 14         INC         D
5484: 99         SBC         C
5485: A1         AND         C
5486: 32         LD           (HLD),A
5487: 32         LD           (HLD),A
5488: 01 32 4A   LD           BC,$4A32
548B: 01 3C 3E   LD           BC,$3E3C
548E: 01 32 01   LD           BC,$0132
5491: 34         INC         (HL)
5492: 01 34 26   LD           BC,$2634
5495: 01 9C 00   LD           BC,$009C
5498: A1         AND         C
5499: 04         INC         B
549A: 9B         SBC         E
549B: 7F         LD           A,A
549C: 02         LD           (BC),A
549D: 9C         SBC         H
549E: A1         AND         C
549F: 04         INC         B
54A0: 9B         SBC         E
54A1: 7F         LD           A,A
54A2: 02         LD           (BC),A
54A3: 9C         SBC         H
54A4: A1         AND         C
54A5: 04         INC         B
54A6: 9B         SBC         E
54A7: 3F         CCF
54A8: 02         LD           (BC),A
54A9: 9C         SBC         H
54AA: 00         NOP
54AB: A1         AND         C
54AC: 52         LD           D,D
54AD: 52         LD           D,D
54AE: 52         LD           D,D
54AF: 50         LD           D,B
54B0: A3         AND         E
54B1: 01 A1 4E   LD           BC,$4EA1
54B4: 01 01 4C   LD           BC,$4C01
54B7: A3         AND         E
54B8: 01 00 A1   LD           BC,$A100
54BB: 52         LD           D,D
54BC: 52         LD           D,D
54BD: 52         LD           D,D
54BE: 50         LD           D,B
54BF: A8         XOR         B
54C0: 01 00 A1   LD           BC,$A100
54C3: 46         LD           B,(HL)
54C4: 46         LD           B,(HL)
54C5: 01 46 01   LD           BC,$0146
54C8: 46         LD           B,(HL)
54C9: 01 50 01   LD           BC,$0150
54CC: 50         LD           D,B
54CD: A2         AND         D
54CE: 50         LD           D,B
54CF: 97         SUB         A
54D0: A1         AND         C
54D1: 01 36 2C   LD           BC,$2C36
54D4: 24         INC         H
54D5: 98         SBC         B
54D6: 00         NOP
54D7: A1         AND         C
54D8: 10 9B      STOP       $9B
54DA: 0F         RRCA
54DB: 0E 9C      LD           C,$9C
54DD: 00         NOP
54DE: A1         AND         C
54DF: 3C         INC         A
54E0: 3C         INC         A
54E1: 01 3C 01   LD           BC,$013C
54E4: 3C         INC         A
54E5: 01 3C 01   LD           BC,$013C
54E8: 46         LD           B,(HL)
54E9: A2         AND         D
54EA: 46         LD           B,(HL)
54EB: 97         SUB         A
54EC: A1         AND         C
54ED: 01 2C 24   LD           BC,$242C
54F0: 1E 98      LD           E,$98
54F2: 00         NOP
54F3: 9B         SBC         E
54F4: 03         INC         BC
54F5: A1         AND         C
54F6: 3E 3E      LD           A,$3E
54F8: 01 3E 56   LD           BC,$563E
54FB: 01 48 4A   LD           BC,$4A48
54FE: 01 3E 01   LD           BC,$013E
5501: 40         LD           B,B
5502: 01 40 32   LD           BC,$3240
5505: 01 9C 00   LD           BC,$009C
5508: A1         AND         C
5509: 32         LD           (HLD),A
550A: 32         LD           (HLD),A
550B: 01 32 01   LD           BC,$0132
550E: 32         LD           (HLD),A
550F: 01 3C 01   LD           BC,$013C
5512: 3C         INC         A
5513: 3C         INC         A
5514: 01 A3 01   LD           BC,$01A3
5517: 00         NOP
5518: A5         AND         L
5519: 01 A3 01   LD           BC,$01A3
551C: 00         NOP
551D: A6         AND         (HL)
551E: 01 00 9B   LD           BC,$9B00
5521: 02         LD           (BC),A
5522: A1         AND         C
5523: 1A         LD           A,(DE)
5524: 1A         LD           A,(DE)
5525: 1A         LD           A,(DE)
5526: 15         DEC         D
5527: 9C         SBC         H
5528: 1A         LD           A,(DE)
5529: 1A         LD           A,(DE)
552A: 15         DEC         D
552B: 1A         LD           A,(DE)
552C: 1A         LD           A,(DE)
552D: 1A         LD           A,(DE)
552E: 1A         LD           A,(DE)
552F: 1A         LD           A,(DE)
5530: 00         NOP
5531: 51         LD           D,C
5532: 55         LD           D,L
5533: 51         LD           D,C
5534: 55         LD           D,L
5535: 61         LD           H,C
5536: 55         LD           D,L
5537: FF         RST         0X38
5538: FF         RST         0X38
5539: FE 52      CP           $52
553B: 7C         LD           A,H
553C: 55         LD           D,L
553D: 7C         LD           A,H
553E: 55         LD           D,L
553F: A8         XOR         B
5540: 55         LD           D,L
5541: FF         RST         0X38
5542: FF         RST         0X38
5543: D6 52      SUB         $52
5545: 59         LD           E,C
5546: 6E         LD           L,(HL)
5547: EC                              
5548: 55         LD           D,L
5549: EC                              
554A: 55         LD           D,L
554B: 15         DEC         D
554C: 56         LD           D,(HL)
554D: FF         RST         0X38
554E: FF         RST         0X38
554F: A6         AND         (HL)
5550: 53         LD           D,E
5551: 9D         SBC         L
5552: C4 83 80   CALL       NZ,$8083
5555: A1         AND         C
5556: 04         INC         B
5557: 9B         SBC         E
5558: 1F         RRA
5559: 02         LD           (BC),A
555A: 9C         SBC         H
555B: 0A         LD           A,(BC)
555C: 9B         SBC         E
555D: 1F         RRA
555E: 08 9C 00   LD           ($009C),SP
5561: A1         AND         C
5562: 10 9B      STOP       $9B
5564: 0D         DEC         C
5565: 0E 9C      LD           C,$9C
5567: 10 12      STOP       $12
5569: 9B         SBC         E
556A: 0F         RRCA
556B: 14         INC         D
556C: 9C         SBC         H
556D: 10 9B      STOP       $9B
556F: 0E 0E      LD           C,$0E
5571: 9C         SBC         H
5572: 10 12      STOP       $12
5574: 9B         SBC         E
5575: 07         RLCA
5576: 14         INC         D
5577: 9C         SBC         H
5578: 16 A4      LD           D,$A4
557A: 01 00 9D   LD           BC,$9D00
557D: 84         ADD         A,H
557E: 86         ADD         A,(HL)
557F: 80         ADD         A,B
5580: 9B         SBC         E
5581: 02         LD           (BC),A
5582: A1         AND         C
5583: 10 10      STOP       $10
5585: 01 10 28   LD           BC,$2810
5588: 01 1A 1C   LD           BC,$1C1A
558B: 01 10 01   LD           BC,$0110
558E: 12         LD           (DE),A
558F: 01 12 04   LD           BC,$0412
5592: 01 9C 9B   LD           BC,$9B9C
5595: 02         LD           (BC),A
5596: 16 16      LD           D,$16
5598: 01 16 2E   LD           BC,$2E16
559B: 01 20 22   LD           BC,$2220
559E: 01 16 01   LD           BC,$0116
55A1: 18 01      JR           $55A4
55A3: 18 0C      JR           $55B1
55A5: 01 9C 00   LD           BC,$009C
55A8: A1         AND         C
55A9: 1C         INC         E
55AA: 1C         INC         E
55AB: 01 1C 34   LD           BC,$341C
55AE: 01 26 2A   LD           BC,$2A26
55B1: 01 1C 9B   LD           BC,$9B1C
55B4: 02         LD           (BC),A
55B5: 01 1E 9C   LD           BC,$9C1E
55B8: 12         LD           (DE),A
55B9: 01 22 22   LD           BC,$2222
55BC: 01 22 3A   LD           BC,$3A22
55BF: 01 2C 2E   LD           BC,$2E2C
55C2: 01 22 9B   LD           BC,$9B22
55C5: 02         LD           (BC),A
55C6: 01 24 9C   LD           BC,$9C24
55C9: 18 01      JR           $55CC
55CB: 1C         INC         E
55CC: 1C         INC         E
55CD: 01 1C 34   LD           BC,$341C
55D0: 01 26 2A   LD           BC,$2A26
55D3: 01 1C 9B   LD           BC,$9B1C
55D6: 02         LD           (BC),A
55D7: 01 1E 9C   LD           BC,$9C1E
55DA: 12         LD           (DE),A
55DB: 01 A2 22   LD           BC,$22A2
55DE: 22         LD           (HLI),A
55DF: 3A         LD           A,(HLD)
55E0: A1         AND         C
55E1: 24         INC         H
55E2: 26 01      LD           H,$01
55E4: 26 A6      LD           H,$A6
55E6: 3E A1      LD           A,$A1
55E8: 26 0E      LD           H,$0E
55EA: 26 00      LD           H,$00
55EC: 9B         SBC         E
55ED: 02         LD           (BC),A
55EE: 99         SBC         C
55EF: A1         AND         C
55F0: 32         LD           (HLD),A
55F1: 32         LD           (HLD),A
55F2: 01 32 4A   LD           BC,$4A32
55F5: 01 3C 3E   LD           BC,$3E3C
55F8: 01 32 01   LD           BC,$0132
55FB: 34         INC         (HL)
55FC: 01 34 26   LD           BC,$2634
55FF: 01 9C 9B   LD           BC,$9B9C
5602: 02         LD           (BC),A
5603: 38 38      JR           C,$563D
5605: 01 38 50   LD           BC,$5038
5608: 01 42 44   LD           BC,$4442
560B: 01 38 01   LD           BC,$0138
560E: 3A         LD           A,(HLD)
560F: 01 3A 2E   LD           BC,$2E3A
5612: 01 9C 00   LD           BC,$009C
5615: A1         AND         C
5616: 3E 3E      LD           A,$3E
5618: 01 3E 56   LD           BC,$563E
561B: 01 48 4C   LD           BC,$4C48
561E: 01 3E 01   LD           BC,$013E
5621: 40         LD           B,B
5622: 01 40 34   LD           BC,$3440
5625: 01 44 44   LD           BC,$4444
5628: 01 44 5C   LD           BC,$5C44
562B: 01 4E 50   LD           BC,$504E
562E: 01 44 01   LD           BC,$0144
5631: 46         LD           B,(HL)
5632: 01 46 3A   LD           BC,$3A46
5635: 01 3E 3E   LD           BC,$3E3E
5638: 01 3E 56   LD           BC,$563E
563B: 01 48 4C   LD           BC,$4C48
563E: 01 3E 01   LD           BC,$013E
5641: 40         LD           B,B
5642: 01 40 34   LD           BC,$3440
5645: 01 A2 44   LD           BC,$44A2
5648: 44         LD           B,H
5649: 5C         LD           E,H
564A: A1         AND         C
564B: 46         LD           B,(HL)
564C: 48         LD           C,B
564D: 01 48 A6   LD           BC,$A648
5650: 60         LD           H,B
5651: A1         AND         C
5652: 48         LD           C,B
5653: 30 48      JR           NC,$569D
5655: 00         NOP
5656: 00         NOP
5657: F2                              
5658: 4A         LD           C,D
5659: 61         LD           H,C
565A: 56         LD           D,(HL)
565B: 6D         LD           L,L
565C: 56         LD           D,(HL)
565D: 93         SUB         E
565E: 56         LD           D,(HL)
565F: 00         NOP
5660: 00         NOP
5661: E1         POP         HL
5662: 6D         LD           L,L
5663: A7         AND         A
5664: 56         LD           D,(HL)
5665: 20 6D      JR           NZ,$56D4
5667: 20 6D      JR           NZ,$56D6
5669: FF         RST         0X38
566A: FF         RST         0X38
566B: 45         LD           B,L
566C: 57         LD           D,A
566D: 9B         SBC         E
566E: 6D         LD           L,L
566F: BC         CP           H
5670: 56         LD           D,(HL)
5671: 45         LD           B,L
5672: 6E         LD           L,(HL)
5673: C7         RST         0X00
5674: 56         LD           D,(HL)
5675: 9B         SBC         E
5676: 6D         LD           L,L
5677: D2 56 BC   JP           NC,$BC56
567A: 56         LD           D,(HL)
567B: 45         LD           B,L
567C: 6E         LD           L,(HL)
567D: C7         RST         0X00
567E: 56         LD           D,(HL)
567F: 9B         SBC         E
5680: 6D         LD           L,L
5681: D2 56 27   JP           NC,$2756
5684: 6E         LD           L,(HL)
5685: E3                              
5686: 56         LD           D,(HL)
5687: 9B         SBC         E
5688: 6D         LD           L,L
5689: D2 56 82   JP           NC,$8256
568C: 6D         LD           L,L
568D: ED                              
568E: 56         LD           D,(HL)
568F: FF         RST         0X38
5690: FF         RST         0X38
5691: 5F         LD           E,A
5692: 57         LD           D,A
5693: 59         LD           E,C
5694: 6E         LD           L,(HL)
5695: F9         LD           SP,HL
5696: 56         LD           D,(HL)
5697: F9         LD           SP,HL
5698: 56         LD           D,(HL)
5699: 54         LD           D,H
569A: 6E         LD           L,(HL)
569B: 35         DEC         (HL)
569C: 57         LD           D,A
569D: 59         LD           E,C
569E: 6E         LD           L,(HL)
569F: 24         INC         H
56A0: 57         LD           D,A
56A1: 24         INC         H
56A2: 57         LD           D,A
56A3: FF         RST         0X38
56A4: FF         RST         0X38
56A5: 91         SUB         C
56A6: 57         LD           D,A
56A7: 9B         SBC         E
56A8: 10 A5      STOP       $A5
56AA: 01 9C A3   LD           BC,$A39C
56AD: 01 A1 0C   LD           BC,$0CA1
56B0: 18 24      JR           $56D6
56B2: 30 3C      JR           NC,$56F0
56B4: 48         LD           C,B
56B5: 54         LD           D,H
56B6: 60         LD           H,B
56B7: A5         AND         L
56B8: 01 A3 01   LD           BC,$01A3
56BB: 00         NOP
56BC: 9B         SBC         E
56BD: 02         LD           (BC),A
56BE: A2         AND         D
56BF: 6A         LD           L,D
56C0: 70         LD           (HL),B
56C1: 6E         LD           L,(HL)
56C2: 74         LD           (HL),H
56C3: AE         XOR         (HL)
56C4: 01 9C 00   LD           BC,$009C
56C7: A1         AND         C
56C8: 3A         LD           A,(HLD)
56C9: 40         LD           B,B
56CA: 3E 44      LD           A,$44
56CC: A4         AND         H
56CD: 50         LD           D,B
56CE: 01 A8 01   LD           BC,$01A8
56D1: 00         NOP
56D2: A8         XOR         B
56D3: 01 A2 01   LD           BC,$01A2
56D6: A1         AND         C
56D7: 78         LD           A,B
56D8: 76         HALT
56D9: 9B         SBC         E
56DA: 0D         DEC         C
56DB: A0         AND         B
56DC: 78         LD           A,B
56DD: 76         HALT
56DE: 9C         SBC         H
56DF: 78         LD           A,B
56E0: A3         AND         E
56E1: 01 00 A1   LD           BC,$A100
56E4: 6A         LD           L,D
56E5: 70         LD           (HL),B
56E6: 78         LD           A,B
56E7: 76         HALT
56E8: A5         AND         L
56E9: 7E         LD           A,(HL)
56EA: A8         XOR         B
56EB: 01 00 A3   LD           BC,$A300
56EE: 01 9B 0D   LD           BC,$0D9B
56F1: A0         AND         B
56F2: 78         LD           A,B
56F3: 76         HALT
56F4: 9C         SBC         H
56F5: 78         LD           A,B
56F6: A5         AND         L
56F7: 01 00 99   LD           BC,$9900
56FA: A2         AND         D
56FB: 0A         LD           A,(BC)
56FC: 01 A4 01   LD           BC,$01A4
56FF: A6         AND         (HL)
5700: 01 A1 0A   LD           BC,$0AA1
5703: 0A         LD           A,(BC)
5704: A6         AND         (HL)
5705: 01 A8 01   LD           BC,$01A8
5708: A2         AND         D
5709: 0A         LD           A,(BC)
570A: 0A         LD           A,(BC)
570B: A4         AND         H
570C: 01 A6 01   LD           BC,$01A6
570F: A1         AND         C
5710: 0A         LD           A,(BC)
5711: A2         AND         D
5712: 0A         LD           A,(BC)
5713: 01 A8 01   LD           BC,$01A8
5716: A2         AND         D
5717: 0A         LD           A,(BC)
5718: 01 A4 01   LD           BC,$01A4
571B: A6         AND         (HL)
571C: 01 A1 0A   LD           BC,$0AA1
571F: A2         AND         D
5720: 0A         LD           A,(BC)
5721: 01 A8 01   LD           BC,$01A8
5724: 99         SBC         C
5725: A2         AND         D
5726: 0A         LD           A,(BC)
5727: 0A         LD           A,(BC)
5728: A4         AND         H
5729: 01 A6 01   LD           BC,$01A6
572C: A1         AND         C
572D: 0A         LD           A,(BC)
572E: 0A         LD           A,(BC)
572F: 0A         LD           A,(BC)
5730: A8         XOR         B
5731: 01 A2 0A   LD           BC,$0AA2
5734: 00         NOP
5735: 9A         SBC         D
5736: A1         AND         C
5737: 0A         LD           A,(BC)
5738: 10 18      STOP       $18
573A: 16 A5      LD           D,$A5
573C: 1E A4      LD           E,$A4
573E: 01 A1 20   LD           BC,$20A1
5741: 18 10      JR           $5753
5743: 0A         LD           A,(BC)
5744: 00         NOP
5745: 36 6E      LD           (HL),$6E
5747: B1         OR           C
5748: 57         LD           D,A
5749: 40         LD           B,B
574A: 6E         LD           L,(HL)
574B: DB                              
574C: 57         LD           D,A
574D: 9B         SBC         E
574E: 6D         LD           L,L
574F: B4         OR           H
5750: 6E         LD           L,(HL)
5751: 08 58 E1   LD           ($E158),SP
5754: 6D         LD           L,L
5755: A7         AND         A
5756: 56         LD           D,(HL)
5757: 20 6D      JR           NZ,$57C6
5759: 20 6D      JR           NZ,$57C8
575B: FF         RST         0X38
575C: FF         RST         0X38
575D: 61         LD           H,C
575E: 56         LD           D,(HL)
575F: 36 6E      LD           (HL),$6E
5761: 14         INC         D
5762: 58         LD           E,B
5763: 40         LD           B,B
5764: 6E         LD           L,(HL)
5765: 3E 58      LD           A,$58
5767: B4         OR           H
5768: 6E         LD           L,(HL)
5769: 15         DEC         D
576A: 6D         LD           L,L
576B: 9B         SBC         E
576C: 6D         LD           L,L
576D: BC         CP           H
576E: 56         LD           D,(HL)
576F: 45         LD           B,L
5770: 6E         LD           L,(HL)
5771: C7         RST         0X00
5772: 56         LD           D,(HL)
5773: 9B         SBC         E
5774: 6D         LD           L,L
5775: D2 56 BC   JP           NC,$BC56
5778: 56         LD           D,(HL)
5779: 45         LD           B,L
577A: 6E         LD           L,(HL)
577B: C7         RST         0X00
577C: 56         LD           D,(HL)
577D: 9B         SBC         E
577E: 6D         LD           L,L
577F: D2 56 27   JP           NC,$2756
5782: 6E         LD           L,(HL)
5783: E3                              
5784: 56         LD           D,(HL)
5785: 9B         SBC         E
5786: 6D         LD           L,L
5787: D2 56 82   JP           NC,$8256
578A: 6D         LD           L,L
578B: ED                              
578C: 56         LD           D,(HL)
578D: FF         RST         0X38
578E: FF         RST         0X38
578F: 6D         LD           L,L
5790: 56         LD           D,(HL)
5791: 63         LD           H,E
5792: 6E         LD           L,(HL)
5793: 6B         LD           L,E
5794: 58         LD           E,B
5795: 54         LD           D,H
5796: 6E         LD           L,(HL)
5797: 9B         SBC         E
5798: 58         LD           E,B
5799: B4         OR           H
579A: 6E         LD           L,(HL)
579B: 15         DEC         D
579C: 6D         LD           L,L
579D: 59         LD           E,C
579E: 6E         LD           L,(HL)
579F: F9         LD           SP,HL
57A0: 56         LD           D,(HL)
57A1: F9         LD           SP,HL
57A2: 56         LD           D,(HL)
57A3: 54         LD           D,H
57A4: 6E         LD           L,(HL)
57A5: 35         DEC         (HL)
57A6: 57         LD           D,A
57A7: 59         LD           E,C
57A8: 6E         LD           L,(HL)
57A9: 24         INC         H
57AA: 57         LD           D,A
57AB: 24         INC         H
57AC: 57         LD           D,A
57AD: FF         RST         0X38
57AE: FF         RST         0X38
57AF: 93         SUB         E
57B0: 56         LD           D,(HL)
57B1: A2         AND         D
57B2: 18 1C      JR           $57D0
57B4: A4         AND         H
57B5: 1E A3      LD           E,$A3
57B7: 01 A2 18   LD           BC,$18A2
57BA: 1C         INC         E
57BB: A7         AND         A
57BC: 1E A2      LD           E,$A2
57BE: 28 26      JR           Z,$57E6
57C0: 18 A4      JR           $5766
57C2: 1C         INC         E
57C3: AE         XOR         (HL)
57C4: 01 A2 18   LD           BC,$18A2
57C7: 1C         INC         E
57C8: A4         AND         H
57C9: 1E A3      LD           E,$A3
57CB: 01 A2 18   LD           BC,$18A2
57CE: 1C         INC         E
57CF: A7         AND         A
57D0: 1E A2      LD           E,$A2
57D2: 26 30      LD           H,$30
57D4: 2E A4      LD           L,$A4
57D6: 2E 01      LD           L,$01
57D8: A5         AND         L
57D9: 01 00 A1   LD           BC,$A100
57DC: 30 32      JR           NC,$5810
57DE: A4         AND         H
57DF: 34         INC         (HL)
57E0: A2         AND         D
57E1: 01 A1 30   LD           BC,$30A1
57E4: 32         LD           (HLD),A
57E5: 34         INC         (HL)
57E6: A6         AND         (HL)
57E7: 01 A3 40   LD           BC,$40A3
57EA: A1         AND         C
57EB: 3E 3C      LD           A,$3C
57ED: 48         LD           C,B
57EE: 4A         LD           C,D
57EF: A4         AND         H
57F0: 4C         LD           C,H
57F1: A1         AND         C
57F2: 4E         LD           C,(HL)
57F3: 01 48 4A   LD           BC,$4A48
57F6: 4C         LD           C,H
57F7: 4E         LD           C,(HL)
57F8: A2         AND         D
57F9: 01 A3 58   LD           BC,$58A3
57FC: A1         AND         C
57FD: 56         LD           D,(HL)
57FE: 54         LD           D,H
57FF: 52         LD           D,D
5800: 54         LD           D,H
5801: 56         LD           D,(HL)
5802: 48         LD           C,B
5803: 4A         LD           C,D
5804: 01 A7 01   LD           BC,$01A7
5807: 00         NOP
5808: A7         AND         A
5809: 01 A1 78   LD           BC,$78A1
580C: 76         HALT
580D: 9B         SBC         E
580E: 09         ADD         HL,BC
580F: A0         AND         B
5810: 78         LD           A,B
5811: 76         HALT
5812: 9C         SBC         H
5813: 00         NOP
5814: A2         AND         D
5815: 22         LD           (HLI),A
5816: 26 A4      LD           H,$A4
5818: 28 A3      JR           Z,$57BD
581A: 01 A2 22   LD           BC,$22A2
581D: 26 A7      LD           H,$A7
581F: 28 A2      JR           Z,$57C3
5821: 32         LD           (HLD),A
5822: 30 22      JR           NC,$5846
5824: A4         AND         H
5825: 24         INC         H
5826: AE         XOR         (HL)
5827: 01 A2 22   LD           BC,$22A2
582A: 26 A4      LD           H,$A4
582C: 28 A3      JR           Z,$57D1
582E: 01 A2 22   LD           BC,$22A2
5831: 26 A7      LD           H,$A7
5833: 28 A2      JR           Z,$57D7
5835: 30 3A      JR           NC,$5871
5837: 38 A4      JR           C,$57DD
5839: 36 01      LD           (HL),$01
583B: A5         AND         L
583C: 01 00 A1   LD           BC,$A100
583F: 3A         LD           A,(HLD)
5840: 3C         INC         A
5841: A4         AND         H
5842: 3E A2      LD           A,$A2
5844: 01 A1 3A   LD           BC,$3AA1
5847: 3C         INC         A
5848: 3E A6      LD           A,$A6
584A: 01 A3 4A   LD           BC,$4AA3
584D: A1         AND         C
584E: 48         LD           C,B
584F: 46         LD           B,(HL)
5850: 52         LD           D,D
5851: 54         LD           D,H
5852: A4         AND         H
5853: 56         LD           D,(HL)
5854: A1         AND         C
5855: 58         LD           E,B
5856: 01 52 54   LD           BC,$5452
5859: 56         LD           D,(HL)
585A: 58         LD           E,B
585B: A2         AND         D
585C: 01 A3 4A   LD           BC,$4AA3
585F: A1         AND         C
5860: 60         LD           H,B
5861: 5E         LD           E,(HL)
5862: 6A         LD           L,D
5863: 6C         LD           L,H
5864: 6E         LD           L,(HL)
5865: 60         LD           H,B
5866: 62         LD           H,D
5867: 01 A7 01   LD           BC,$01A7
586A: 00         NOP
586B: 9B         SBC         E
586C: 02         LD           (BC),A
586D: 99         SBC         C
586E: A2         AND         D
586F: 0A         LD           A,(BC)
5870: 0A         LD           A,(BC)
5871: A8         XOR         B
5872: 01 9C 9B   LD           BC,$9B9C
5875: 02         LD           (BC),A
5876: A2         AND         D
5877: 06 06      LD           B,$06
5879: A8         XOR         B
587A: 01 9C 9B   LD           BC,$9B9C
587D: 02         LD           (BC),A
587E: A2         AND         D
587F: 0A         LD           A,(BC)
5880: 0A         LD           A,(BC)
5881: 01 0A 01   LD           BC,$010A
5884: 0A         LD           A,(BC)
5885: A1         AND         C
5886: 0A         LD           A,(BC)
5887: 0A         LD           A,(BC)
5888: 0A         LD           A,(BC)
5889: 0A         LD           A,(BC)
588A: 9C         SBC         H
588B: 9B         SBC         E
588C: 02         LD           (BC),A
588D: A2         AND         D
588E: 1A         LD           A,(DE)
588F: 1A         LD           A,(DE)
5890: 01 1A 01   LD           BC,$011A
5893: 1A         LD           A,(DE)
5894: A1         AND         C
5895: 1A         LD           A,(DE)
5896: 1A         LD           A,(DE)
5897: 1A         LD           A,(DE)
5898: 1A         LD           A,(DE)
5899: 9C         SBC         H
589A: 00         NOP
589B: 9B         SBC         E
589C: 04         INC         B
589D: A1         AND         C
589E: 0A         LD           A,(BC)
589F: 9C         SBC         H
58A0: 22         LD           (HLI),A
58A1: 9B         SBC         E
58A2: 07         RLCA
58A3: 0A         LD           A,(BC)
58A4: 9C         SBC         H
58A5: 9B         SBC         E
58A6: 04         INC         B
58A7: 0A         LD           A,(BC)
58A8: 9C         SBC         H
58A9: 22         LD           (HLI),A
58AA: 9B         SBC         E
58AB: 07         RLCA
58AC: 0A         LD           A,(BC)
58AD: 9C         SBC         H
58AE: 9B         SBC         E
58AF: 04         INC         B
58B0: 0A         LD           A,(BC)
58B1: 9C         SBC         H
58B2: 22         LD           (HLI),A
58B3: 9B         SBC         E
58B4: 07         RLCA
58B5: 0A         LD           A,(BC)
58B6: 9C         SBC         H
58B7: 9B         SBC         E
58B8: 04         INC         B
58B9: 0A         LD           A,(BC)
58BA: 9C         SBC         H
58BB: 22         LD           (HLI),A
58BC: 9B         SBC         E
58BD: 07         RLCA
58BE: 0A         LD           A,(BC)
58BF: 9C         SBC         H
58C0: 22         LD           (HLI),A
58C1: 24         INC         H
58C2: 26 18      LD           H,$18
58C4: 1A         LD           A,(DE)
58C5: 01 A7 01   LD           BC,$01A7
58C8: 00         NOP
58C9: 00         NOP
58CA: C5         PUSH       BC
58CB: 4A         LD           C,D
58CC: D4 58 EE   CALL       NC,$EE58
58CF: 58         LD           E,B
58D0: 0C         INC         C
58D1: 59         LD           E,C
58D2: 00         NOP
58D3: 00         NOP
58D4: 27         DAA
58D5: 6D         LD           L,L
58D6: 78         LD           A,B
58D7: 6D         LD           L,L
58D8: 18 59      JR           $5933
58DA: 21 59 18   LD           HL,$1859
58DD: 59         LD           E,C
58DE: 09         ADD         HL,BC
58DF: 6E         LD           L,(HL)
58E0: 29         ADD         HL,HL
58E1: 59         LD           E,C
58E2: 31 59 31   LD           SP,$3159
58E5: 59         LD           E,C
58E6: 31 59 31   LD           SP,$3159
58E9: 59         LD           E,C
58EA: FF         RST         0X38
58EB: FF         RST         0X38
58EC: D6 58      SUB         $58
58EE: 09         ADD         HL,BC
58EF: 6E         LD           L,(HL)
58F0: 18 59      JR           $594B
58F2: 21 59 C3   LD           HL,$C359
58F5: 6D         LD           L,L
58F6: 18 59      JR           $5951
58F8: 29         ADD         HL,HL
58F9: 59         LD           E,C
58FA: A5         AND         L
58FB: 6D         LD           L,L
58FC: 31 59 31   LD           SP,$3159
58FF: 59         LD           E,C
5900: C3 6D 31   JP           $316D
5903: 59         LD           E,C
5904: 09         ADD         HL,BC
5905: 6E         LD           L,(HL)
5906: 31 59 FF   LD           SP,$FF59
5909: FF         RST         0X38
590A: EE 58      XOR         $58
590C: 54         LD           D,H
590D: 6E         LD           L,(HL)
590E: 6E         LD           L,(HL)
590F: 59         LD           E,C
5910: 39         ADD         HL,SP
5911: 59         LD           E,C
5912: 61         LD           H,C
5913: 59         LD           E,C
5914: FF         RST         0X38
5915: FF         RST         0X38
5916: 0C         INC         C
5917: 59         LD           E,C
5918: 9B         SBC         E
5919: 04         INC         B
591A: A2         AND         D
591B: 48         LD           C,B
591C: 4C         LD           C,H
591D: 54         LD           D,H
591E: 58         LD           E,B
591F: 9C         SBC         H
5920: 00         NOP
5921: 9B         SBC         E
5922: 04         INC         B
5923: 44         LD           B,H
5924: 48         LD           C,B
5925: 50         LD           D,B
5926: 54         LD           D,H
5927: 9C         SBC         H
5928: 00         NOP
5929: 9B         SBC         E
592A: 04         INC         B
592B: 4A         LD           C,D
592C: 4E         LD           C,(HL)
592D: 56         LD           D,(HL)
592E: 5A         LD           E,D
592F: 9C         SBC         H
5930: 00         NOP
5931: 9B         SBC         E
5932: 02         LD           (BC),A
5933: 4C         LD           C,H
5934: 50         LD           D,B
5935: 56         LD           D,(HL)
5936: 5C         LD           E,H
5937: 9C         SBC         H
5938: 00         NOP
5939: 99         SBC         C
593A: A7         AND         A
593B: 18 A2      JR           $58DF
593D: 18 A5      JR           $58E4
593F: 01 A7 01   LD           BC,$01A7
5942: A2         AND         D
5943: 16 A7      LD           D,$A7
5945: 14         INC         D
5946: A2         AND         D
5947: 14         INC         D
5948: A5         AND         L
5949: 01 A7 01   LD           BC,$01A7
594C: A2         AND         D
594D: 14         INC         D
594E: A7         AND         A
594F: 0A         LD           A,(BC)
5950: A2         AND         D
5951: 0A         LD           A,(BC)
5952: A5         AND         L
5953: 01 A7 01   LD           BC,$01A7
5956: A2         AND         D
5957: 0A         LD           A,(BC)
5958: 02         LD           (BC),A
5959: 02         LD           (BC),A
595A: 01 02 A5   LD           BC,$A502
595D: 01 A7 01   LD           BC,$01A7
5960: 00         NOP
5961: 9B         SBC         E
5962: 04         INC         B
5963: A2         AND         D
5964: 04         INC         B
5965: 9C         SBC         H
5966: AE         XOR         (HL)
5967: 01 01 A4   LD           BC,$A401
596A: 01 A2 18   LD           BC,$18A2
596D: 00         NOP
596E: 9B         SBC         E
596F: 0C         INC         C
5970: A5         AND         L
5971: 01 9C 00   LD           BC,$009C
5974: 00         NOP
5975: B6         OR           (HL)
5976: 4A         LD           C,D
5977: 17         RLA
5978: 4B         LD           C,E
5979: 7F         LD           A,A
597A: 59         LD           E,C
597B: 2F         CPL
597C: 5A         LD           E,D
597D: 00         NOP
597E: 00         NOP
597F: 13         INC         DE
5980: 6E         LD           L,(HL)
5981: 7C         LD           A,H
5982: 6E         LD           L,(HL)
5983: 47         LD           B,A
5984: 5A         LD           E,D
5985: 51         LD           D,C
5986: 5A         LD           E,D
5987: 1D         DEC         E
5988: 6E         LD           L,(HL)
5989: 94         SUB         H
598A: 6E         LD           L,(HL)
598B: 47         LD           B,A
598C: 5A         LD           E,D
598D: 51         LD           D,C
598E: 5A         LD           E,D
598F: FA 6D 8B   LD           A,($8B6D)
5992: 6E         LD           L,(HL)
5993: 47         LD           B,A
5994: 5A         LD           E,D
5995: 88         ADC         A,B
5996: 6E         LD           L,(HL)
5997: 47         LD           B,A
5998: 5A         LD           E,D
5999: E6 6D      AND         $6D
599B: 85         ADD         A,L
599C: 6E         LD           L,(HL)
599D: 47         LD           B,A
599E: 5A         LD           E,D
599F: 20 6D      JR           NZ,$5A0E
59A1: 7C         LD           A,H
59A2: 6E         LD           L,(HL)
59A3: 13         INC         DE
59A4: 6E         LD           L,(HL)
59A5: 7C         LD           A,H
59A6: 6E         LD           L,(HL)
59A7: 47         LD           B,A
59A8: 5A         LD           E,D
59A9: 51         LD           D,C
59AA: 5A         LD           E,D
59AB: 1D         DEC         E
59AC: 6E         LD           L,(HL)
59AD: 94         SUB         H
59AE: 6E         LD           L,(HL)
59AF: 47         LD           B,A
59B0: 5A         LD           E,D
59B1: 51         LD           D,C
59B2: 5A         LD           E,D
59B3: FA 6D 8B   LD           A,($8B6D)
59B6: 6E         LD           L,(HL)
59B7: 47         LD           B,A
59B8: 5A         LD           E,D
59B9: 88         ADC         A,B
59BA: 6E         LD           L,(HL)
59BB: 47         LD           B,A
59BC: 5A         LD           E,D
59BD: E6 6D      AND         $6D
59BF: 85         ADD         A,L
59C0: 6E         LD           L,(HL)
59C1: 47         LD           B,A
59C2: 5A         LD           E,D
59C3: 20 6D      JR           NZ,$5A32
59C5: 7C         LD           A,H
59C6: 6E         LD           L,(HL)
59C7: 9B         SBC         E
59C8: 6D         LD           L,L
59C9: 77         LD           (HL),A
59CA: 5A         LD           E,D
59CB: 8C         ADC         A,H
59CC: 6D         LD           L,L
59CD: 7E         LD           A,(HL)
59CE: 5A         LD           E,D
59CF: 91         SUB         C
59D0: 6D         LD           L,L
59D1: 84         ADD         A,H
59D2: 5A         LD           E,D
59D3: 9B         SBC         E
59D4: 6D         LD           L,L
59D5: 84         ADD         A,H
59D6: 5A         LD           E,D
59D7: 84         ADD         A,H
59D8: 5A         LD           E,D
59D9: 82         ADD         A,D
59DA: 6D         LD           L,L
59DB: 84         ADD         A,H
59DC: 5A         LD           E,D
59DD: 9B         SBC         E
59DE: 6D         LD           L,L
59DF: 8A         ADC         A,D
59E0: 5A         LD           E,D
59E1: 8C         ADC         A,H
59E2: 6D         LD           L,L
59E3: 90         SUB         B
59E4: 5A         LD           E,D
59E5: 91         SUB         C
59E6: 6D         LD           L,L
59E7: 84         ADD         A,H
59E8: 5A         LD           E,D
59E9: 9B         SBC         E
59EA: 6D         LD           L,L
59EB: 84         ADD         A,H
59EC: 5A         LD           E,D
59ED: 84         ADD         A,H
59EE: 5A         LD           E,D
59EF: 82         ADD         A,D
59F0: 6D         LD           L,L
59F1: 84         ADD         A,H
59F2: 5A         LD           E,D
59F3: 94         SUB         H
59F4: 6E         LD           L,(HL)
59F5: 9B         SBC         E
59F6: 6D         LD           L,L
59F7: 77         LD           (HL),A
59F8: 5A         LD           E,D
59F9: 8C         ADC         A,H
59FA: 6D         LD           L,L
59FB: 7E         LD           A,(HL)
59FC: 5A         LD           E,D
59FD: 91         SUB         C
59FE: 6D         LD           L,L
59FF: 84         ADD         A,H
5A00: 5A         LD           E,D
5A01: 9B         SBC         E
5A02: 6D         LD           L,L
5A03: 84         ADD         A,H
5A04: 5A         LD           E,D
5A05: 84         ADD         A,H
5A06: 5A         LD           E,D
5A07: 82         ADD         A,D
5A08: 6D         LD           L,L
5A09: 84         ADD         A,H
5A0A: 5A         LD           E,D
5A0B: 9B         SBC         E
5A0C: 6D         LD           L,L
5A0D: 8A         ADC         A,D
5A0E: 5A         LD           E,D
5A0F: 8C         ADC         A,H
5A10: 6D         LD           L,L
5A11: 90         SUB         B
5A12: 5A         LD           E,D
5A13: 91         SUB         C
5A14: 6D         LD           L,L
5A15: 84         ADD         A,H
5A16: 5A         LD           E,D
5A17: 9B         SBC         E
5A18: 6D         LD           L,L
5A19: 84         ADD         A,H
5A1A: 5A         LD           E,D
5A1B: 84         ADD         A,H
5A1C: 5A         LD           E,D
5A1D: 82         ADD         A,D
5A1E: 6D         LD           L,L
5A1F: 84         ADD         A,H
5A20: 5A         LD           E,D
5A21: 7C         LD           A,H
5A22: 6E         LD           L,(HL)
5A23: B9         CP           C
5A24: 6D         LD           L,L
5A25: 3F         CCF
5A26: 5A         LD           E,D
5A27: 27         DAA
5A28: 6E         LD           L,(HL)
5A29: 96         SUB         (HL)
5A2A: 5A         LD           E,D
5A2B: FF         RST         0X38
5A2C: FF         RST         0X38
5A2D: 7F         LD           A,A
5A2E: 59         LD           E,C
5A2F: 5E         LD           E,(HL)
5A30: 6E         LD           L,(HL)
5A31: 6A         LD           L,D
5A32: 5A         LD           E,D
5A33: 9F         SBC         A
5A34: 5A         LD           E,D
5A35: 59         LD           E,C
5A36: 6E         LD           L,(HL)
5A37: 3F         CCF
5A38: 5A         LD           E,D
5A39: 96         SUB         (HL)
5A3A: 5A         LD           E,D
5A3B: FF         RST         0X38
5A3C: FF         RST         0X38
5A3D: 2F         CPL
5A3E: 5A         LD           E,D
5A3F: A2         AND         D
5A40: 18 1C      JR           $5A5E
5A42: 1E 14      LD           E,$14
5A44: 18 1A      JR           $5A60
5A46: 00         NOP
5A47: A3         AND         E
5A48: 30 34      JR           NC,$5A7E
5A4A: 36 A4      LD           (HL),$A4
5A4C: 44         LD           B,H
5A4D: 18 A3      JR           $59F2
5A4F: 01 00 30   LD           BC,$3000
5A52: 34         INC         (HL)
5A53: 36 A4      LD           (HL),$A4
5A55: 42         LD           B,D
5A56: 18 A3      JR           $59FB
5A58: 01 30 34   LD           BC,$3430
5A5B: 36 A4      LD           (HL),$A4
5A5D: 40         LD           B,B
5A5E: 18 A3      JR           $5A03
5A60: 01 30 34   LD           BC,$3430
5A63: 36 A4      LD           (HL),$A4
5A65: 42         LD           B,D
5A66: 18 A3      JR           $5A0B
5A68: 01 00 9B   LD           BC,$9B00
5A6B: 18 99      JR           $5A06
5A6D: A3         AND         E
5A6E: 18 18      JR           $5A88
5A70: A5         AND         L
5A71: 01 A3 01   LD           BC,$01A3
5A74: 18 9C      JR           $5A12
5A76: 00         NOP
5A77: 9B         SBC         E
5A78: 0C         INC         C
5A79: A1         AND         C
5A7A: 24         INC         H
5A7B: 2C         INC         L
5A7C: 9C         SBC         H
5A7D: 00         NOP
5A7E: 9B         SBC         E
5A7F: 04         INC         B
5A80: 24         INC         H
5A81: 2C         INC         L
5A82: 9C         SBC         H
5A83: 00         NOP
5A84: 9B         SBC         E
5A85: 04         INC         B
5A86: 22         LD           (HLI),A
5A87: 2A         LD           A,(HLI)
5A88: 9C         SBC         H
5A89: 00         NOP
5A8A: 9B         SBC         E
5A8B: 0C         INC         C
5A8C: 20 28      JR           NZ,$5AB6
5A8E: 9C         SBC         H
5A8F: 00         NOP
5A90: 9B         SBC         E
5A91: 04         INC         B
5A92: 20 28      JR           NZ,$5ABC
5A94: 9C         SBC         H
5A95: 00         NOP
5A96: A2         AND         D
5A97: 01 AE 0C   LD           BC,$0CAE
5A9A: A5         AND         L
5A9B: 01 A7 01   LD           BC,$01A7
5A9E: 00         NOP
5A9F: 9B         SBC         E
5AA0: 08 99 A3   LD           ($A399),SP
5AA3: 18 18      JR           $5ABD
5AA5: 01 18 01   LD           BC,$0118
5AA8: A4         AND         H
5AA9: 30 A3      JR           NC,$5A4E
5AAB: 18 9C      JR           $5A49
5AAD: 00         NOP
5AAE: 00         NOP
5AAF: B6         OR           (HL)
5AB0: 4A         LD           C,D
5AB1: B9         CP           C
5AB2: 5A         LD           E,D
5AB3: D5         PUSH       DE
5AB4: 5A         LD           E,D
5AB5: B1         OR           C
5AB6: 5B         LD           E,E
5AB7: 00         NOP
5AB8: 00         NOP
5AB9: 82         ADD         A,D
5ABA: 6D         LD           L,L
5ABB: DF         RST         0X18
5ABC: 5B         LD           E,E
5ABD: 9B         SBC         E
5ABE: 6D         LD           L,L
5ABF: DF         RST         0X18
5AC0: 5B         LD           E,E
5AC1: DF         RST         0X18
5AC2: 5B         LD           E,E
5AC3: 00         NOP
5AC4: 5C         LD           E,H
5AC5: 8C         ADC         A,H
5AC6: 6D         LD           L,L
5AC7: 0B         DEC         BC
5AC8: 5C         LD           E,H
5AC9: 0B         DEC         BC
5ACA: 5C         LD           E,H
5ACB: 0B         DEC         BC
5ACC: 5C         LD           E,H
5ACD: 7C         LD           A,H
5ACE: 6E         LD           L,(HL)
5ACF: 0B         DEC         BC
5AD0: 5C         LD           E,H
5AD1: FF         RST         0X38
5AD2: FF         RST         0X38
5AD3: B9         CP           C
5AD4: 5A         LD           E,D
5AD5: 82         ADD         A,D
5AD6: 6D         LD           L,L
5AD7: 2F         CPL
5AD8: 5C         LD           E,H
5AD9: 2F         CPL
5ADA: 5C         LD           E,H
5ADB: 9B         SBC         E
5ADC: 6D         LD           L,L
5ADD: 2F         CPL
5ADE: 5C         LD           E,H
5ADF: 82         ADD         A,D
5AE0: 6D         LD           L,L
5AE1: 2F         CPL
5AE2: 5C         LD           E,H
5AE3: 82         ADD         A,D
5AE4: 6D         LD           L,L
5AE5: 35         DEC         (HL)
5AE6: 5C         LD           E,H
5AE7: 35         DEC         (HL)
5AE8: 5C         LD           E,H
5AE9: 9B         SBC         E
5AEA: 6D         LD           L,L
5AEB: 35         DEC         (HL)
5AEC: 5C         LD           E,H
5AED: 82         ADD         A,D
5AEE: 6D         LD           L,L
5AEF: 35         DEC         (HL)
5AF0: 5C         LD           E,H
5AF1: 82         ADD         A,D
5AF2: 6D         LD           L,L
5AF3: 3A         LD           A,(HLD)
5AF4: 5C         LD           E,H
5AF5: 3A         LD           A,(HLD)
5AF6: 5C         LD           E,H
5AF7: 9B         SBC         E
5AF8: 6D         LD           L,L
5AF9: 3A         LD           A,(HLD)
5AFA: 5C         LD           E,H
5AFB: 82         ADD         A,D
5AFC: 6D         LD           L,L
5AFD: 3A         LD           A,(HLD)
5AFE: 5C         LD           E,H
5AFF: 82         ADD         A,D
5B00: 6D         LD           L,L
5B01: 3F         CCF
5B02: 5C         LD           E,H
5B03: 3F         CCF
5B04: 5C         LD           E,H
5B05: 9B         SBC         E
5B06: 6D         LD           L,L
5B07: 3F         CCF
5B08: 5C         LD           E,H
5B09: 82         ADD         A,D
5B0A: 6D         LD           L,L
5B0B: 3F         CCF
5B0C: 5C         LD           E,H
5B0D: 82         ADD         A,D
5B0E: 6D         LD           L,L
5B0F: 2F         CPL
5B10: 5C         LD           E,H
5B11: 9B         SBC         E
5B12: 6D         LD           L,L
5B13: 2F         CPL
5B14: 5C         LD           E,H
5B15: 8C         ADC         A,H
5B16: 6D         LD           L,L
5B17: 2F         CPL
5B18: 5C         LD           E,H
5B19: 82         ADD         A,D
5B1A: 6D         LD           L,L
5B1B: 2F         CPL
5B1C: 5C         LD           E,H
5B1D: 82         ADD         A,D
5B1E: 6D         LD           L,L
5B1F: 35         DEC         (HL)
5B20: 5C         LD           E,H
5B21: 9B         SBC         E
5B22: 6D         LD           L,L
5B23: 35         DEC         (HL)
5B24: 5C         LD           E,H
5B25: 8C         ADC         A,H
5B26: 6D         LD           L,L
5B27: 35         DEC         (HL)
5B28: 5C         LD           E,H
5B29: 82         ADD         A,D
5B2A: 6D         LD           L,L
5B2B: 35         DEC         (HL)
5B2C: 5C         LD           E,H
5B2D: 82         ADD         A,D
5B2E: 6D         LD           L,L
5B2F: 3A         LD           A,(HLD)
5B30: 5C         LD           E,H
5B31: 9B         SBC         E
5B32: 6D         LD           L,L
5B33: 3A         LD           A,(HLD)
5B34: 5C         LD           E,H
5B35: 8C         ADC         A,H
5B36: 6D         LD           L,L
5B37: 3A         LD           A,(HLD)
5B38: 5C         LD           E,H
5B39: 82         ADD         A,D
5B3A: 6D         LD           L,L
5B3B: 3A         LD           A,(HLD)
5B3C: 5C         LD           E,H
5B3D: 82         ADD         A,D
5B3E: 6D         LD           L,L
5B3F: 3F         CCF
5B40: 5C         LD           E,H
5B41: 9B         SBC         E
5B42: 6D         LD           L,L
5B43: 3F         CCF
5B44: 5C         LD           E,H
5B45: 8C         ADC         A,H
5B46: 6D         LD           L,L
5B47: 3F         CCF
5B48: 5C         LD           E,H
5B49: 82         ADD         A,D
5B4A: 6D         LD           L,L
5B4B: 3F         CCF
5B4C: 5C         LD           E,H
5B4D: 82         ADD         A,D
5B4E: 6D         LD           L,L
5B4F: 2F         CPL
5B50: 5C         LD           E,H
5B51: 9B         SBC         E
5B52: 6D         LD           L,L
5B53: 2F         CPL
5B54: 5C         LD           E,H
5B55: 8C         ADC         A,H
5B56: 6D         LD           L,L
5B57: 2F         CPL
5B58: 5C         LD           E,H
5B59: 82         ADD         A,D
5B5A: 6D         LD           L,L
5B5B: 2F         CPL
5B5C: 5C         LD           E,H
5B5D: 82         ADD         A,D
5B5E: 6D         LD           L,L
5B5F: 35         DEC         (HL)
5B60: 5C         LD           E,H
5B61: 9B         SBC         E
5B62: 6D         LD           L,L
5B63: 35         DEC         (HL)
5B64: 5C         LD           E,H
5B65: 8C         ADC         A,H
5B66: 6D         LD           L,L
5B67: 35         DEC         (HL)
5B68: 5C         LD           E,H
5B69: 82         ADD         A,D
5B6A: 6D         LD           L,L
5B6B: 35         DEC         (HL)
5B6C: 5C         LD           E,H
5B6D: 82         ADD         A,D
5B6E: 6D         LD           L,L
5B6F: 3A         LD           A,(HLD)
5B70: 5C         LD           E,H
5B71: 9B         SBC         E
5B72: 6D         LD           L,L
5B73: 3A         LD           A,(HLD)
5B74: 5C         LD           E,H
5B75: 8C         ADC         A,H
5B76: 6D         LD           L,L
5B77: 3A         LD           A,(HLD)
5B78: 5C         LD           E,H
5B79: 82         ADD         A,D
5B7A: 6D         LD           L,L
5B7B: 3A         LD           A,(HLD)
5B7C: 5C         LD           E,H
5B7D: 82         ADD         A,D
5B7E: 6D         LD           L,L
5B7F: 3F         CCF
5B80: 5C         LD           E,H
5B81: 9B         SBC         E
5B82: 6D         LD           L,L
5B83: 3F         CCF
5B84: 5C         LD           E,H
5B85: 8C         ADC         A,H
5B86: 6D         LD           L,L
5B87: 3F         CCF
5B88: 5C         LD           E,H
5B89: 82         ADD         A,D
5B8A: 6D         LD           L,L
5B8B: 3F         CCF
5B8C: 5C         LD           E,H
5B8D: 82         ADD         A,D
5B8E: 6D         LD           L,L
5B8F: 44         LD           B,H
5B90: 5C         LD           E,H
5B91: 8C         ADC         A,H
5B92: 6D         LD           L,L
5B93: 44         LD           B,H
5B94: 5C         LD           E,H
5B95: 9B         SBC         E
5B96: 6D         LD           L,L
5B97: 49         LD           C,C
5B98: 5C         LD           E,H
5B99: 8C         ADC         A,H
5B9A: 6D         LD           L,L
5B9B: 49         LD           C,C
5B9C: 5C         LD           E,H
5B9D: 20 6D      JR           NZ,$5C0C
5B9F: 20 6D      JR           NZ,$5C0E
5BA1: 9B         SBC         E
5BA2: 6D         LD           L,L
5BA3: 4E         LD           C,(HL)
5BA4: 5C         LD           E,H
5BA5: 94         SUB         H
5BA6: 6E         LD           L,(HL)
5BA7: 4E         LD           C,(HL)
5BA8: 5C         LD           E,H
5BA9: 20 6D      JR           NZ,$5C18
5BAB: 20 6D      JR           NZ,$5C1A
5BAD: FF         RST         0X38
5BAE: FF         RST         0X38
5BAF: D5         PUSH       DE
5BB0: 5A         LD           E,D
5BB1: 67         LD           H,A
5BB2: 5D         LD           E,L
5BB3: 15         DEC         D
5BB4: 6D         LD           L,L
5BB5: 20 6D      JR           NZ,$5C24
5BB7: 20 6D      JR           NZ,$5C26
5BB9: 20 6D      JR           NZ,$5C28
5BBB: 63         LD           H,E
5BBC: 6E         LD           L,(HL)
5BBD: 5E         LD           E,(HL)
5BBE: 5C         LD           E,H
5BBF: 72         LD           (HL),D
5BC0: 6E         LD           L,(HL)
5BC1: 8D         ADC         A,L
5BC2: 5C         LD           E,H
5BC3: 6D         LD           L,L
5BC4: 6E         LD           L,(HL)
5BC5: A1         AND         C
5BC6: 5C         LD           E,H
5BC7: 72         LD           (HL),D
5BC8: 6E         LD           L,(HL)
5BC9: 8D         ADC         A,L
5BCA: 5C         LD           E,H
5BCB: 6D         LD           L,L
5BCC: 6E         LD           L,(HL)
5BCD: A1         AND         C
5BCE: 5C         LD           E,H
5BCF: 18 6D      JR           $5C3E
5BD1: 6D         LD           L,L
5BD2: 6E         LD           L,(HL)
5BD3: 96         SUB         (HL)
5BD4: 5C         LD           E,H
5BD5: 77         LD           (HL),A
5BD6: 6E         LD           L,(HL)
5BD7: A1         AND         C
5BD8: 5C         LD           E,H
5BD9: 18 6D      JR           $5C48
5BDB: FF         RST         0X38
5BDC: FF         RST         0X38
5BDD: B1         OR           C
5BDE: 5B         LD           E,E
5BDF: A5         AND         L
5BE0: 01 A3 01   LD           BC,$01A3
5BE3: 9B         SBC         E
5BE4: 04         INC         B
5BE5: A2         AND         D
5BE6: 54         LD           D,H
5BE7: 9C         SBC         H
5BE8: AE         XOR         (HL)
5BE9: 01 9B 04   LD           BC,$049B
5BEC: A2         AND         D
5BED: 52         LD           D,D
5BEE: 9C         SBC         H
5BEF: AE         XOR         (HL)
5BF0: 01 9B 04   LD           BC,$049B
5BF3: A2         AND         D
5BF4: 58         LD           E,B
5BF5: 9C         SBC         H
5BF6: AE         XOR         (HL)
5BF7: 01 9B 04   LD           BC,$049B
5BFA: A2         AND         D
5BFB: 56         LD           D,(HL)
5BFC: 9C         SBC         H
5BFD: A3         AND         E
5BFE: 01 00 A8   LD           BC,$A800
5C01: 01 A2 01   LD           BC,$01A2
5C04: 5E         LD           E,(HL)
5C05: A8         XOR         B
5C06: 01 A2 01   LD           BC,$01A2
5C09: 60         LD           H,B
5C0A: 00         NOP
5C0B: 9B         SBC         E
5C0C: 03         INC         BC
5C0D: A2         AND         D
5C0E: 02         LD           (BC),A
5C0F: 08 04 0C   LD           ($0C04),SP
5C12: 9C         SBC         H
5C13: 9D         SBC         L
5C14: A2         AND         D
5C15: 83         ADD         A,E
5C16: C0         RET         NZ
5C17: 02         LD           (BC),A
5C18: 08 04 0C   LD           ($0C04),SP
5C1B: 9D         SBC         L
5C1C: C2 83 C0   JP           NZ,$C083
5C1F: 02         LD           (BC),A
5C20: 08 04 0C   LD           ($0C04),SP
5C23: 9D         SBC         L
5C24: 81         ADD         A,C
5C25: 83         ADD         A,E
5C26: C0         RET         NZ
5C27: 9B         SBC         E
5C28: 03         INC         BC
5C29: 02         LD           (BC),A
5C2A: 08 04 0C   LD           ($0C04),SP
5C2D: 9C         SBC         H
5C2E: 00         NOP
5C2F: 9B         SBC         E
5C30: 04         INC         B
5C31: A2         AND         D
5C32: 60         LD           H,B
5C33: 9C         SBC         H
5C34: 00         NOP
5C35: 9B         SBC         E
5C36: 04         INC         B
5C37: 5E         LD           E,(HL)
5C38: 9C         SBC         H
5C39: 00         NOP
5C3A: 9B         SBC         E
5C3B: 04         INC         B
5C3C: 64         LD           H,H
5C3D: 9C         SBC         H
5C3E: 00         NOP
5C3F: 9B         SBC         E
5C40: 04         INC         B
5C41: 62         LD           H,D
5C42: 9C         SBC         H
5C43: 00         NOP
5C44: 9B         SBC         E
5C45: 04         INC         B
5C46: 6A         LD           L,D
5C47: 9C         SBC         H
5C48: 00         NOP
5C49: 9B         SBC         E
5C4A: 04         INC         B
5C4B: 6C         LD           L,H
5C4C: 9C         SBC         H
5C4D: 00         NOP
5C4E: A2         AND         D
5C4F: 30 34      JR           NC,$5C85
5C51: 36 44      LD           (HL),$44
5C53: A5         AND         L
5C54: 01 A2 01   LD           BC,$01A2
5C57: 42         LD           B,D
5C58: 34         INC         (HL)
5C59: 42         LD           B,D
5C5A: A5         AND         L
5C5B: 01 01 00   LD           BC,$0001
5C5E: 99         SBC         C
5C5F: A2         AND         D
5C60: 18 1C      JR           $5C7E
5C62: 1E 2C      LD           E,$2C
5C64: AE         XOR         (HL)
5C65: 01 A2 18   LD           BC,$18A2
5C68: 1C         INC         E
5C69: 1E 2A      LD           E,$2A
5C6B: AE         XOR         (HL)
5C6C: 01 A2 1C   LD           BC,$1CA2
5C6F: 20 22      JR           NZ,$5C93
5C71: 30 AE      JR           NC,$5C21
5C73: 01 A2 1C   LD           BC,$1CA2
5C76: 20 22      JR           NZ,$5C9A
5C78: 2E AE      LD           L,$AE
5C7A: 01 A2 26   LD           BC,$26A2
5C7D: 2A         LD           A,(HLI)
5C7E: 2C         INC         L
5C7F: 3A         LD           A,(HLD)
5C80: A4         AND         H
5C81: 01 A2 28   LD           BC,$28A2
5C84: 2C         INC         L
5C85: 2E 3C      LD           L,$3C
5C87: 9B         SBC         E
5C88: 09         ADD         HL,BC
5C89: A4         AND         H
5C8A: 01 9C 00   LD           BC,$009C
5C8D: A3         AND         E
5C8E: 01 A2 60   LD           BC,$60A2
5C91: 64         LD           H,H
5C92: 66         LD           H,(HL)
5C93: 74         LD           (HL),H
5C94: A3         AND         E
5C95: 01 A5 01   LD           BC,$01A5
5C98: 9B         SBC         E
5C99: 03         INC         BC
5C9A: A2         AND         D
5C9B: 5A         LD           E,D
5C9C: 60         LD           H,B
5C9D: 5E         LD           E,(HL)
5C9E: 62         LD           H,D
5C9F: 9C         SBC         H
5CA0: 00         NOP
5CA1: A2         AND         D
5CA2: 5A         LD           E,D
5CA3: 60         LD           H,B
5CA4: 5E         LD           E,(HL)
5CA5: 62         LD           H,D
5CA6: 00         NOP
5CA7: 00         NOP
5CA8: D4 4A B2   CALL       NC,$B24A
5CAB: 5C         LD           E,H
5CAC: 00         NOP
5CAD: 5D         LD           E,L
5CAE: 2C         INC         L
5CAF: 5D         LD           E,L
5CB0: 00         NOP
5CB1: 00         NOP
5CB2: 09         ADD         HL,BC
5CB3: 6E         LD           L,(HL)
5CB4: 6D         LD           L,L
5CB5: 5D         LD           E,L
5CB6: 13         INC         DE
5CB7: 6E         LD           L,(HL)
5CB8: 6D         LD           L,L
5CB9: 5D         LD           E,L
5CBA: CD 6D 6D   CALL       $6D6D
5CBD: 5D         LD           E,L
5CBE: 13         INC         DE
5CBF: 6E         LD           L,(HL)
5CC0: 6D         LD           L,L
5CC1: 5D         LD           E,L
5CC2: 87         ADD         A,A
5CC3: 6D         LD           L,L
5CC4: 75         LD           (HL),L
5CC5: 5D         LD           E,L
5CC6: 09         ADD         HL,BC
5CC7: 6E         LD           L,(HL)
5CC8: 6D         LD           L,L
5CC9: 5D         LD           E,L
5CCA: 6D         LD           L,L
5CCB: 5D         LD           E,L
5CCC: 18 6D      JR           $5D3B
5CCE: 24         INC         H
5CCF: 6D         LD           L,L
5CD0: 24         INC         H
5CD1: 6D         LD           L,L
5CD2: 2D         DEC         L
5CD3: 6D         LD           L,L
5CD4: 09         ADD         HL,BC
5CD5: 6E         LD           L,(HL)
5CD6: 6D         LD           L,L
5CD7: 5D         LD           E,L
5CD8: 13         INC         DE
5CD9: 6E         LD           L,(HL)
5CDA: 6D         LD           L,L
5CDB: 5D         LD           E,L
5CDC: CD 6D 6D   CALL       $6D6D
5CDF: 5D         LD           E,L
5CE0: 13         INC         DE
5CE1: 6E         LD           L,(HL)
5CE2: 6D         LD           L,L
5CE3: 5D         LD           E,L
5CE4: 87         ADD         A,A
5CE5: 6D         LD           L,L
5CE6: 86         ADD         A,(HL)
5CE7: 5D         LD           E,L
5CE8: 0E 6E      LD           C,$6E
5CEA: 6D         LD           L,L
5CEB: 5D         LD           E,L
5CEC: 13         INC         DE
5CED: 6E         LD           L,(HL)
5CEE: 6D         LD           L,L
5CEF: 5D         LD           E,L
5CF0: CD 6D 6D   CALL       $6D6D
5CF3: 5D         LD           E,L
5CF4: 24         INC         H
5CF5: 6D         LD           L,L
5CF6: 24         INC         H
5CF7: 6D         LD           L,L
5CF8: 0E 6E      LD           C,$6E
5CFA: 98         SBC         B
5CFB: 5D         LD           E,L
5CFC: FF         RST         0X38
5CFD: FF         RST         0X38
5CFE: B2         OR           D
5CFF: 5C         LD           E,H
5D00: 45         LD           B,L
5D01: 6E         LD           L,(HL)
5D02: 36 5D      LD           (HL),$5D
5D04: 13         INC         DE
5D05: 6E         LD           L,(HL)
5D06: 4D         LD           C,L
5D07: 5D         LD           E,L
5D08: 09         ADD         HL,BC
5D09: 6E         LD           L,(HL)
5D0A: 6D         LD           L,L
5D0B: 5D         LD           E,L
5D0C: 13         INC         DE
5D0D: 6E         LD           L,(HL)
5D0E: 6D         LD           L,L
5D0F: 5D         LD           E,L
5D10: 09         ADD         HL,BC
5D11: 6E         LD           L,(HL)
5D12: 6D         LD           L,L
5D13: 5D         LD           E,L
5D14: 2D         DEC         L
5D15: 6D         LD           L,L
5D16: 2D         DEC         L
5D17: 6D         LD           L,L
5D18: 09         ADD         HL,BC
5D19: 6E         LD           L,(HL)
5D1A: 6D         LD           L,L
5D1B: 5D         LD           E,L
5D1C: 0E 6E      LD           C,$6E
5D1E: 6D         LD           L,L
5D1F: 5D         LD           E,L
5D20: 13         INC         DE
5D21: 6E         LD           L,(HL)
5D22: 6D         LD           L,L
5D23: 5D         LD           E,L
5D24: 2D         DEC         L
5D25: 6D         LD           L,L
5D26: 2D         DEC         L
5D27: 6D         LD           L,L
5D28: FF         RST         0X38
5D29: FF         RST         0X38
5D2A: 00         NOP
5D2B: 5D         LD           E,L
5D2C: 5E         LD           E,(HL)
5D2D: 6E         LD           L,(HL)
5D2E: 36 5D      LD           (HL),$5D
5D30: 67         LD           H,A
5D31: 5D         LD           E,L
5D32: FF         RST         0X38
5D33: FF         RST         0X38
5D34: 2C         INC         L
5D35: 5D         LD           E,L
5D36: A4         AND         H
5D37: 18 A3      JR           $5CDC
5D39: 1C         INC         E
5D3A: 1E A5      LD           E,$A5
5D3C: 16 9B      LD           D,$9B
5D3E: 04         INC         B
5D3F: 01 9C A4   LD           BC,$A49C
5D42: 18 A3      JR           $5CE7
5D44: 1C         INC         E
5D45: 1E A5      LD           E,$A5
5D47: 24         INC         H
5D48: 9B         SBC         E
5D49: 04         INC         B
5D4A: 01 9C 00   LD           BC,$009C
5D4D: A4         AND         H
5D4E: 60         LD           H,B
5D4F: A3         AND         E
5D50: 64         LD           H,H
5D51: 66         LD           H,(HL)
5D52: A4         AND         H
5D53: 74         LD           (HL),H
5D54: 5E         LD           E,(HL)
5D55: A3         AND         E
5D56: 62         LD           H,D
5D57: 64         LD           H,H
5D58: A4         AND         H
5D59: 72         LD           (HL),D
5D5A: 6E         LD           L,(HL)
5D5B: A3         AND         E
5D5C: 72         LD           (HL),D
5D5D: 74         LD           (HL),H
5D5E: A4         AND         H
5D5F: 82         ADD         A,D
5D60: 70         LD           (HL),B
5D61: A3         AND         E
5D62: 74         LD           (HL),H
5D63: 76         HALT
5D64: A4         AND         H
5D65: 84         ADD         A,H
5D66: 00         NOP
5D67: 9B         SBC         E
5D68: 09         ADD         HL,BC
5D69: A5         AND         L
5D6A: 01 9C 00   LD           BC,$009C
5D6D: AA         XOR         D
5D6E: 48         LD           C,B
5D6F: 54         LD           D,H
5D70: 56         LD           D,(HL)
5D71: 60         LD           H,B
5D72: 56         LD           D,(HL)
5D73: 54         LD           D,H
5D74: 00         NOP
5D75: A1         AND         C
5D76: 01 AD 01   LD           BC,$01AD
5D79: A3         AND         E
5D7A: 01 74 72   LD           BC,$7274
5D7D: 01 74 72   LD           BC,$7274
5D80: A4         AND         H
5D81: 01 A2 74   LD           BC,$74A2
5D84: 72         LD           (HL),D
5D85: 00         NOP
5D86: A1         AND         C
5D87: 01 AD 01   LD           BC,$01AD
5D8A: 01 A3 01   LD           BC,$01A3
5D8D: 7A         LD           A,D
5D8E: 78         LD           A,B
5D8F: 01 7A 78   LD           BC,$787A
5D92: A4         AND         H
5D93: 01 A2 7A   LD           BC,$7AA2
5D96: 78         LD           A,B
5D97: 00         NOP
5D98: A0         AND         B
5D99: 01 01 9B   LD           BC,$9B01
5D9C: 03         INC         BC
5D9D: A3         AND         E
5D9E: 48         LD           C,B
5D9F: 3C         INC         A
5DA0: 9C         SBC         H
5DA1: 9B         SBC         E
5DA2: 03         INC         BC
5DA3: 46         LD           B,(HL)
5DA4: 3A         LD           A,(HLD)
5DA5: 9C         SBC         H
5DA6: 9B         SBC         E
5DA7: 03         INC         BC
5DA8: 3E 32      LD           A,$32
5DAA: 9C         SBC         H
5DAB: 9B         SBC         E
5DAC: 06 40      LD           B,$40
5DAE: 34         INC         (HL)
5DAF: 9C         SBC         H
5DB0: AE         XOR         (HL)
5DB1: 01 00 00   LD           BC,$0000
5DB4: B6         OR           (HL)
5DB5: 4A         LD           C,D
5DB6: BE         CP           (HL)
5DB7: 5D         LD           E,L
5DB8: C6 5D      ADD         $5D
5DBA: 17         RLA
5DBB: 4B         LD           C,E
5DBC: 00         NOP
5DBD: 00         NOP
5DBE: 09         ADD         HL,BC
5DBF: 6E         LD           L,(HL)
5DC0: D6 5D      SUB         $5D
5DC2: FF         RST         0X38
5DC3: FF         RST         0X38
5DC4: BE         CP           (HL)
5DC5: 5D         LD           E,L
5DC6: 0E 6E      LD           C,$6E
5DC8: 20 5E      JR           NZ,$5E28
5DCA: 13         INC         DE
5DCB: 6E         LD           L,(HL)
5DCC: 4D         LD           C,L
5DCD: 5E         LD           E,(HL)
5DCE: CD 6D 5F   CALL       $5F6D
5DD1: 5E         LD           E,(HL)
5DD2: FF         RST         0X38
5DD3: FF         RST         0X38
5DD4: C6 5D      ADD         $5D
5DD6: A3         AND         E
5DD7: 01 A2 48   LD           BC,$48A2
5DDA: 4C         LD           C,H
5DDB: 4E         LD           C,(HL)
5DDC: 5C         LD           E,H
5DDD: 01 6C 6C   LD           BC,$6C6C
5DE0: A4         AND         H
5DE1: 01 A2 01   LD           BC,$01A2
5DE4: 48         LD           C,B
5DE5: 4C         LD           C,H
5DE6: 4E         LD           C,(HL)
5DE7: 5A         LD           E,D
5DE8: 01 6A 6A   LD           BC,$6A6A
5DEB: A4         AND         H
5DEC: 01 A2 01   LD           BC,$01A2
5DEF: 4C         LD           C,H
5DF0: 50         LD           D,B
5DF1: 52         LD           D,D
5DF2: 60         LD           H,B
5DF3: 01 70 70   LD           BC,$7070
5DF6: A4         AND         H
5DF7: 01 A2 01   LD           BC,$01A2
5DFA: 4C         LD           C,H
5DFB: 50         LD           D,B
5DFC: 52         LD           D,D
5DFD: 5E         LD           E,(HL)
5DFE: 01 6E 6E   LD           BC,$6E6E
5E01: A4         AND         H
5E02: 01 A2 01   LD           BC,$01A2
5E05: 56         LD           D,(HL)
5E06: 5A         LD           E,D
5E07: 5C         LD           E,H
5E08: 6A         LD           L,D
5E09: 01 76 A3   LD           BC,$A376
5E0C: 01 A2 58   LD           BC,$58A2
5E0F: 5C         LD           E,H
5E10: 5E         LD           E,(HL)
5E11: 6C         LD           L,H
5E12: 01 78 A3   LD           BC,$A378
5E15: 01 A2 60   LD           BC,$60A2
5E18: 64         LD           H,H
5E19: 84         ADD         A,H
5E1A: 82         ADD         A,D
5E1B: 80         ADD         A,B
5E1C: 7E         LD           A,(HL)
5E1D: AE         XOR         (HL)
5E1E: 01 00 A2   LD           BC,$A200
5E21: 48         LD           C,B
5E22: 4C         LD           C,H
5E23: 4E         LD           C,(HL)
5E24: 5C         LD           E,H
5E25: A7         AND         A
5E26: 01 A2 78   LD           BC,$78A2
5E29: A4         AND         H
5E2A: 78         LD           A,B
5E2B: A2         AND         D
5E2C: 48         LD           C,B
5E2D: 4C         LD           C,H
5E2E: 4E         LD           C,(HL)
5E2F: 5A         LD           E,D
5E30: A7         AND         A
5E31: 01 A2 76   LD           BC,$76A2
5E34: A4         AND         H
5E35: 76         HALT
5E36: A2         AND         D
5E37: 4C         LD           C,H
5E38: 50         LD           D,B
5E39: 52         LD           D,D
5E3A: 60         LD           H,B
5E3B: A7         AND         A
5E3C: 01 A2 7C   LD           BC,$7CA2
5E3F: A4         AND         H
5E40: 7C         LD           A,H
5E41: A2         AND         D
5E42: 4C         LD           C,H
5E43: 50         LD           D,B
5E44: 52         LD           D,D
5E45: 5E         LD           E,(HL)
5E46: A7         AND         A
5E47: 01 A2 7A   LD           BC,$7AA2
5E4A: A4         AND         H
5E4B: 7A         LD           A,D
5E4C: 00         NOP
5E4D: A2         AND         D
5E4E: 56         LD           D,(HL)
5E4F: 5A         LD           E,D
5E50: 5C         LD           E,H
5E51: 6A         LD           L,D
5E52: A7         AND         A
5E53: 01 A2 82   LD           BC,$82A2
5E56: 58         LD           E,B
5E57: 5C         LD           E,H
5E58: 5E         LD           E,(HL)
5E59: 6C         LD           L,H
5E5A: A7         AND         A
5E5B: 01 A2 84   LD           BC,$84A2
5E5E: 00         NOP
5E5F: 60         LD           H,B
5E60: 64         LD           H,H
5E61: 66         LD           H,(HL)
5E62: 8C         ADC         A,H
5E63: 8A         ADC         A,D
5E64: 88         ADC         A,B
5E65: 86         ADD         A,(HL)
5E66: 84         ADD         A,H
5E67: AE         XOR         (HL)
5E68: 01 00 00   LD           BC,$0000
5E6B: E3                              
5E6C: 4A         LD           C,D
5E6D: 89         ADC         A,C
5E6E: 5E         LD           E,(HL)
5E6F: 75         LD           (HL),L
5E70: 5E         LD           E,(HL)
5E71: 93         SUB         E
5E72: 5E         LD           E,(HL)
5E73: 00         NOP
5E74: 00         NOP
5E75: AA         XOR         D
5E76: 6D         LD           L,L
5E77: 9B         SBC         E
5E78: 5E         LD           E,(HL)
5E79: AF         XOR         A
5E7A: 6D         LD           L,L
5E7B: AD         XOR         L
5E7C: 5E         LD           E,(HL)
5E7D: B4         OR           H
5E7E: 6D         LD           L,L
5E7F: BE         CP           (HL)
5E80: 5E         LD           E,(HL)
5E81: AF         XOR         A
5E82: 6D         LD           L,L
5E83: CF         RST         0X08
5E84: 5E         LD           E,(HL)
5E85: FF         RST         0X38
5E86: FF         RST         0X38
5E87: 75         LD           (HL),L
5E88: 5E         LD           E,(HL)
5E89: 10 6D      STOP       $6D
5E8B: 7D         LD           A,L
5E8C: 6D         LD           L,L
5E8D: 9B         SBC         E
5E8E: 5E         LD           E,(HL)
5E8F: FF         RST         0X38
5E90: FF         RST         0X38
5E91: 8B         ADC         A,E
5E92: 5E         LD           E,(HL)
5E93: 54         LD           D,H
5E94: 6E         LD           L,(HL)
5E95: E0 5E      LDFF00   ($5E),A
5E97: FF         RST         0X38
5E98: FF         RST         0X38
5E99: 93         SUB         E
5E9A: 5E         LD           E,(HL)
5E9B: A2         AND         D
5E9C: 2C         INC         L
5E9D: 26 20      LD           H,$20
5E9F: 1A         LD           A,(DE)
5EA0: 14         INC         D
5EA1: 0E 08      LD           C,$08
5EA3: 04         INC         B
5EA4: 02         LD           (BC),A
5EA5: 08 0E 14   LD           ($140E),SP
5EA8: 1A         LD           A,(DE)
5EA9: 20 26      JR           NZ,$5ED1
5EAB: 2C         INC         L
5EAC: 00         NOP
5EAD: 2E 26      LD           L,$26
5EAF: 20 1A      JR           NZ,$5ECB
5EB1: 16 0E      LD           D,$0E
5EB3: 08 04 02   LD           ($0204),SP
5EB6: 08 0E 16   LD           ($160E),SP
5EB9: 1A         LD           A,(DE)
5EBA: 20 26      JR           NZ,$5EE2
5EBC: 2E 00      LD           L,$00
5EBE: 30 26      JR           NC,$5EE6
5EC0: 20 1A      JR           NZ,$5EDC
5EC2: 18 0E      JR           $5ED2
5EC4: 08 04 02   LD           ($0204),SP
5EC7: 08 0E 18   LD           ($180E),SP
5ECA: 1A         LD           A,(DE)
5ECB: 20 26      JR           NZ,$5EF3
5ECD: 30 00      JR           NC,$5ECF
5ECF: 2E 26      LD           L,$26
5ED1: 20 1A      JR           NZ,$5EED
5ED3: 16 0E      LD           D,$0E
5ED5: 08 04 02   LD           ($0204),SP
5ED8: 08 0E 16   LD           ($160E),SP
5EDB: 1A         LD           A,(DE)
5EDC: 20 26      JR           NZ,$5F04
5EDE: 2E 00      LD           L,$00
5EE0: 99         SBC         C
5EE1: A8         XOR         B
5EE2: 01 A2 01   LD           BC,$01A2
5EE5: 02         LD           (BC),A
5EE6: 02         LD           (BC),A
5EE7: 01 A8 01   LD           BC,$01A8
5EEA: A5         AND         L
5EEB: 01 01 00   LD           BC,$0001
5EEE: 00         NOP
5EEF: D4 4A F9   CALL       NC,$F94A
5EF2: 5E         LD           E,(HL)
5EF3: 05         DEC         B
5EF4: 5F         LD           E,A
5EF5: 00         NOP
5EF6: 00         NOP
5EF7: 00         NOP
5EF8: 00         NOP
5EF9: 10 6D      STOP       $6D
5EFB: 7D         LD           A,L
5EFC: 6D         LD           L,L
5EFD: 19         ADD         HL,DE
5EFE: 5F         LD           E,A
5EFF: 19         ADD         HL,DE
5F00: 5F         LD           E,A
5F01: FF         RST         0X38
5F02: FF         RST         0X38
5F03: FB         EI
5F04: 5E         LD           E,(HL)
5F05: 09         ADD         HL,BC
5F06: 6E         LD           L,(HL)
5F07: 19         ADD         HL,DE
5F08: 5F         LD           E,A
5F09: 0E 6E      LD           C,$6E
5F0B: 2B         DEC         HL
5F0C: 5F         LD           E,A
5F0D: 13         INC         DE
5F0E: 6E         LD           L,(HL)
5F0F: 19         ADD         HL,DE
5F10: 5F         LD           E,A
5F11: 22         LD           (HLI),A
5F12: 6E         LD           L,(HL)
5F13: 2B         DEC         HL
5F14: 5F         LD           E,A
5F15: FF         RST         0X38
5F16: FF         RST         0X38
5F17: 0D         DEC         C
5F18: 5F         LD           E,A
5F19: A1         AND         C
5F1A: 48         LD           C,B
5F1B: 44         LD           B,H
5F1C: 3E 38      LD           A,$38
5F1E: 30 2C      JR           NC,$5F4C
5F20: 26 20      LD           H,$20
5F22: 18 20      JR           $5F44
5F24: 26 2C      LD           H,$2C
5F26: 30 38      JR           NC,$5F60
5F28: 3E 44      LD           A,$44
5F2A: 00         NOP
5F2B: 4C         LD           C,H
5F2C: 48         LD           C,B
5F2D: 44         LD           B,H
5F2E: 3E 38      LD           A,$38
5F30: 30 2C      JR           NC,$5F5E
5F32: 26 20      LD           H,$20
5F34: 26 2C      LD           H,$2C
5F36: 34         INC         (HL)
5F37: 3E 44      LD           A,$44
5F39: 4C         LD           C,H
5F3A: 50         LD           D,B
5F3B: 00         NOP
5F3C: 00         NOP
5F3D: 98         SBC         B
5F3E: 4A         LD           C,D
5F3F: 47         LD           B,A
5F40: 5F         LD           E,A
5F41: 5D         LD           E,L
5F42: 5F         LD           E,A
5F43: 77         LD           (HL),A
5F44: 5F         LD           E,A
5F45: 8B         ADC         A,E
5F46: 5F         LD           E,A
5F47: 4F         LD           C,A
5F48: 6E         LD           L,(HL)
5F49: 03         INC         BC
5F4A: 60         LD           H,B
5F4B: C8         RET         Z
5F4C: 6D         LD           L,L
5F4D: 9D         SBC         L
5F4E: 5F         LD           E,A
5F4F: 27         DAA
5F50: 6E         LD           L,(HL)
5F51: BC         CP           H
5F52: 5F         LD           E,A
5F53: C8         RET         Z
5F54: 6D         LD           L,L
5F55: 9D         SBC         L
5F56: 5F         LD           E,A
5F57: 20 6D      JR           NZ,$5FC6
5F59: FF         RST         0X38
5F5A: FF         RST         0X38
5F5B: 47         LD           B,A
5F5C: 5F         LD           E,A
5F5D: 4F         LD           C,A
5F5E: 6E         LD           L,(HL)
5F5F: F1         POP         AF
5F60: 5F         LD           E,A
5F61: C8         RET         Z
5F62: 6D         LD           L,L
5F63: C7         RST         0X00
5F64: 5F         LD           E,A
5F65: 27         DAA
5F66: 6E         LD           L,(HL)
5F67: E6 5F      AND         $5F
5F69: 8E         ADC         A,(HL)
5F6A: 6E         LD           L,(HL)
5F6B: C8         RET         Z
5F6C: 6D         LD           L,L
5F6D: C7         RST         0X00
5F6E: 5F         LD           E,A
5F6F: 20 6D      JR           NZ,$5FDE
5F71: 7C         LD           A,H
5F72: 6E         LD           L,(HL)
5F73: FF         RST         0X38
5F74: FF         RST         0X38
5F75: 5D         LD           E,L
5F76: 5F         LD           E,A
5F77: 15         DEC         D
5F78: 6D         LD           L,L
5F79: 5E         LD           E,(HL)
5F7A: 6E         LD           L,(HL)
5F7B: 15         DEC         D
5F7C: 60         LD           H,B
5F7D: 59         LD           E,C
5F7E: 6E         LD           L,(HL)
5F7F: 22         LD           (HLI),A
5F80: 60         LD           H,B
5F81: 5E         LD           E,(HL)
5F82: 6E         LD           L,(HL)
5F83: 15         DEC         D
5F84: 60         LD           H,B
5F85: 20 6D      JR           NZ,$5FF4
5F87: FF         RST         0X38
5F88: FF         RST         0X38
5F89: 77         LD           (HL),A
5F8A: 5F         LD           E,A
5F8B: 2D         DEC         L
5F8C: 60         LD           H,B
5F8D: 30 60      JR           NC,$5FEF
5F8F: 30 60      JR           NC,$5FF1
5F91: 48         LD           C,B
5F92: 60         LD           H,B
5F93: 30 60      JR           NC,$5FF5
5F95: 30 60      JR           NC,$5FF7
5F97: 53         LD           D,E
5F98: 60         LD           H,B
5F99: FF         RST         0X38
5F9A: FF         RST         0X38
5F9B: 8B         ADC         A,E
5F9C: 5F         LD           E,A
5F9D: 9B         SBC         E
5F9E: 02         LD           (BC),A
5F9F: A2         AND         D
5FA0: 22         LD           (HLI),A
5FA1: 22         LD           (HLI),A
5FA2: 22         LD           (HLI),A
5FA3: 20 A4      JR           NZ,$5F49
5FA5: 01 A7 1E   LD           BC,$1EA7
5FA8: 1C         INC         E
5FA9: A3         AND         E
5FAA: 01 9C 9B   LD           BC,$9B9C
5FAD: 02         LD           (BC),A
5FAE: A2         AND         D
5FAF: 26 26      LD           H,$26
5FB1: 26 24      LD           H,$24
5FB3: A4         AND         H
5FB4: 01 A7 22   LD           BC,$22A7
5FB7: 20 A3      JR           NZ,$5F5C
5FB9: 01 9C 00   LD           BC,$009C
5FBC: A7         AND         A
5FBD: 48         LD           C,B
5FBE: 46         LD           B,(HL)
5FBF: A2         AND         D
5FC0: 48         LD           C,B
5FC1: 4A         LD           C,D
5FC2: 4C         LD           C,H
5FC3: A1         AND         C
5FC4: 4E         LD           C,(HL)
5FC5: 01 00 9B   LD           BC,$9B00
5FC8: 02         LD           (BC),A
5FC9: A2         AND         D
5FCA: 30 30      JR           NC,$5FFC
5FCC: 30 2E      JR           NC,$5FFC
5FCE: A4         AND         H
5FCF: 01 A7 2C   LD           BC,$2CA7
5FD2: 2A         LD           A,(HLI)
5FD3: A3         AND         E
5FD4: 01 9C 9B   LD           BC,$9B9C
5FD7: 02         LD           (BC),A
5FD8: A2         AND         D
5FD9: 34         INC         (HL)
5FDA: 34         INC         (HL)
5FDB: 34         INC         (HL)
5FDC: 32         LD           (HLD),A
5FDD: A4         AND         H
5FDE: 01 A7 30   LD           BC,$30A7
5FE1: 2E A3      LD           L,$A3
5FE3: 01 9C 00   LD           BC,$009C
5FE6: A7         AND         A
5FE7: 52         LD           D,D
5FE8: 50         LD           D,B
5FE9: A2         AND         D
5FEA: 52         LD           D,D
5FEB: 54         LD           D,H
5FEC: 56         LD           D,(HL)
5FED: A1         AND         C
5FEE: 58         LD           E,B
5FEF: 01 00 A1   LD           BC,$A100
5FF2: 6C         LD           L,H
5FF3: 6A         LD           L,D
5FF4: 68         LD           L,B
5FF5: 66         LD           H,(HL)
5FF6: 64         LD           H,H
5FF7: 62         LD           H,D
5FF8: 60         LD           H,B
5FF9: 5E         LD           E,(HL)
5FFA: 5C         LD           E,H
5FFB: 5A         LD           E,D
5FFC: 58         LD           E,B
5FFD: 56         LD           D,(HL)
5FFE: 54         LD           D,H
5FFF: 52         LD           D,D
6000: 50         LD           D,B
6001: 4E         LD           C,(HL)
6002: 00         NOP
6003: A1         AND         C
6004: 66         LD           H,(HL)
6005: 64         LD           H,H
6006: 62         LD           H,D
6007: 60         LD           H,B
6008: 5E         LD           E,(HL)
6009: 5C         LD           E,H
600A: 5A         LD           E,D
600B: 58         LD           E,B
600C: 56         LD           D,(HL)
600D: 54         LD           D,H
600E: 52         LD           D,D
600F: 50         LD           D,B
6010: 4E         LD           C,(HL)
6011: 4C         LD           C,H
6012: 4A         LD           C,D
6013: 48         LD           C,B
6014: 00         NOP
6015: 9B         SBC         E
6016: 10 99      STOP       $99
6018: A2         AND         D
6019: 18 0E      JR           $6029
601B: 9C         SBC         H
601C: 9B         SBC         E
601D: 10 04      STOP       $04
601F: 1C         INC         E
6020: 9C         SBC         H
6021: 00         NOP
6022: 9A         SBC         D
6023: A7         AND         A
6024: 32         LD           (HLD),A
6025: 30 A2      JR           NC,$5FC9
6027: 32         LD           (HLD),A
6028: 34         INC         (HL)
6029: 36 99      LD           (HL),$99
602B: 38 00      JR           C,$602D
602D: A5         AND         L
602E: 01 00 9B   LD           BC,$9B00
6031: 04         INC         B
6032: A2         AND         D
6033: 15         DEC         D
6034: 15         DEC         D
6035: FF         RST         0X38
6036: 01 9C 9B   LD           BC,$9B9C
6039: 02         LD           (BC),A
603A: 15         DEC         D
603B: 15         DEC         D
603C: FF         RST         0X38
603D: 15         DEC         D
603E: 9C         SBC         H
603F: 1A         LD           A,(DE)
6040: FF         RST         0X38
6041: 15         DEC         D
6042: FF         RST         0X38
6043: 9B         SBC         E
6044: 04         INC         B
6045: FF         RST         0X38
6046: 9C         SBC         H
6047: 00         NOP
6048: 9B         SBC         E
6049: 02         LD           (BC),A
604A: FF         RST         0X38
604B: 1A         LD           A,(DE)
604C: 1A         LD           A,(DE)
604D: 9C         SBC         H
604E: 9B         SBC         E
604F: 04         INC         B
6050: FF         RST         0X38
6051: 9C         SBC         H
6052: 00         NOP
6053: 1A         LD           A,(DE)
6054: 1A         LD           A,(DE)
6055: 01 15 15   LD           BC,$1515
6058: 01 FF FF   LD           BC,$FFFF
605B: 9B         SBC         E
605C: 04         INC         B
605D: 15         DEC         D
605E: 9C         SBC         H
605F: 9B         SBC         E
6060: 04         INC         B
6061: 1A         LD           A,(DE)
6062: 9C         SBC         H
6063: 00         NOP
6064: 00         NOP
6065: A7         AND         A
6066: 4A         LD           C,D
6067: 6F         LD           L,A
6068: 60         LD           H,B
6069: 79         LD           A,C
606A: 60         LD           H,B
606B: 7F         LD           A,A
606C: 60         LD           H,B
606D: 00         NOP
606E: 00         NOP
606F: 09         ADD         HL,BC
6070: 6E         LD           L,(HL)
6071: 24         INC         H
6072: 6D         LD           L,L
6073: 27         DAA
6074: 6D         LD           L,L
6075: 87         ADD         A,A
6076: 60         LD           H,B
6077: 00         NOP
6078: 00         NOP
6079: CD 6D 87   CALL       $876D
607C: 60         LD           H,B
607D: 00         NOP
607E: 00         NOP
607F: 77         LD           (HL),A
6080: 6E         LD           L,(HL)
6081: 27         DAA
6082: 6D         LD           L,L
6083: 87         ADD         A,A
6084: 60         LD           H,B
6085: 00         NOP
6086: 00         NOP
6087: 9B         SBC         E
6088: 02         LD           (BC),A
6089: A1         AND         C
608A: 90         SUB         B
608B: 8A         ADC         A,D
608C: 82         ADD         A,D
608D: 7C         LD           A,H
608E: 78         LD           A,B
608F: 72         LD           (HL),D
6090: 6A         LD           L,D
6091: 64         LD           H,H
6092: 60         LD           H,B
6093: 5A         LD           E,D
6094: 52         LD           D,D
6095: 4C         LD           C,H
6096: 48         LD           C,B
6097: 42         LD           B,D
6098: 3A         LD           A,(HLD)
6099: 34         INC         (HL)
609A: 8E         ADC         A,(HL)
609B: 88         ADC         A,B
609C: 82         ADD         A,D
609D: 7A         LD           A,D
609E: 76         HALT
609F: 70         LD           (HL),B
60A0: 6A         LD           L,D
60A1: 62         LD           H,D
60A2: 5E         LD           E,(HL)
60A3: 58         LD           E,B
60A4: 52         LD           D,D
60A5: 4A         LD           C,D
60A6: 46         LD           B,(HL)
60A7: 40         LD           B,B
60A8: 3A         LD           A,(HLD)
60A9: 32         LD           (HLD),A
60AA: 9C         SBC         H
60AB: 2E 28      LD           L,$28
60AD: 22         LD           (HLI),A
60AE: 1A         LD           A,(DE)
60AF: 16 10      LD           D,$10
60B1: 0A         LD           A,(BC)
60B2: 02         LD           (BC),A
60B3: A6         AND         (HL)
60B4: 48         LD           C,B
60B5: 56         LD           D,(HL)
60B6: 5C         LD           E,H
60B7: 64         LD           H,H
60B8: 01 A2 60   LD           BC,$60A2
60BB: A1         AND         C
60BC: 68         LD           L,B
60BD: 6E         LD           L,(HL)
60BE: A5         AND         L
60BF: 78         LD           A,B
60C0: 01 00 00   LD           BC,$0000
60C3: C5         PUSH       BC
60C4: 4A         LD           C,D
60C5: CD 60 D9   CALL       $D960
60C8: 60         LD           H,B
60C9: 17         RLA
60CA: 4B         LD           C,E
60CB: 00         NOP
60CC: 00         NOP
60CD: 09         ADD         HL,BC
60CE: 6E         LD           L,(HL)
60CF: 03         INC         BC
60D0: 60         LD           H,B
60D1: 10 6D      STOP       $6D
60D3: E3                              
60D4: 60         LD           H,B
60D5: FF         RST         0X38
60D6: FF         RST         0X38
60D7: D3                              
60D8: 60         LD           H,B
60D9: 09         ADD         HL,BC
60DA: 6E         LD           L,(HL)
60DB: 9D         SBC         L
60DC: 6E         LD           L,(HL)
60DD: F1         POP         AF
60DE: 5F         LD           E,A
60DF: FF         RST         0X38
60E0: FF         RST         0X38
60E1: D3                              
60E2: 60         LD           H,B
60E3: A2         AND         D
60E4: 28 30      JR           Z,$6116
60E6: 36 3E      LD           (HL),$3E
60E8: A3         AND         E
60E9: 6E         LD           L,(HL)
60EA: 01 A2 60   LD           BC,$60A2
60ED: 28 30      JR           Z,$611F
60EF: 36 60      LD           (HL),$60
60F1: 64         LD           H,H
60F2: 66         LD           H,(HL)
60F3: 6A         LD           L,D
60F4: 26 34      LD           H,$34
60F6: A3         AND         E
60F7: 6A         LD           L,D
60F8: 5C         LD           E,H
60F9: 74         LD           (HL),H
60FA: A2         AND         D
60FB: 52         LD           D,D
60FC: 4C         LD           C,H
60FD: 44         LD           B,H
60FE: 3E 3A      LD           A,$3A
6100: 34         INC         (HL)
6101: 2C         INC         L
6102: 26 22      LD           H,$22
6104: 28 30      JR           Z,$6136
6106: 36 A3      LD           (HL),$A3
6108: 66         LD           H,(HL)
6109: 01 A2 58   LD           BC,$58A2
610C: 22         LD           (HLI),A
610D: 28 30      JR           Z,$613F
610F: 58         LD           E,B
6110: 5C         LD           E,H
6111: 60         LD           H,B
6112: 64         LD           H,H
6113: 1E 2C      LD           E,$2C
6115: A3         AND         E
6116: 64         LD           H,H
6117: 56         LD           D,(HL)
6118: 6E         LD           L,(HL)
6119: A2         AND         D
611A: 4C         LD           C,H
611B: 44         LD           B,H
611C: 3E 36      LD           A,$36
611E: 34         INC         (HL)
611F: 2C         INC         L
6120: 26 1E      LD           H,$1E
6122: 00         NOP
6123: 00         NOP
6124: A7         AND         A
6125: 4A         LD           C,D
6126: 2E 61      LD           L,$61
6128: 34         INC         (HL)
6129: 61         LD           H,C
612A: 48         LD           C,B
612B: 61         LD           H,C
612C: 00         NOP
612D: 00         NOP
612E: 54         LD           D,H
612F: 61         LD           H,C
6130: FF         RST         0X38
6131: FF         RST         0X38
6132: 2E 61      LD           L,$61
6134: 8F         ADC         A,A
6135: 61         LD           H,C
6136: E3                              
6137: 60         LD           H,B
6138: 7C         LD           A,H
6139: 6E         LD           L,(HL)
613A: 9D         SBC         L
613B: 61         LD           H,C
613C: 96         SUB         (HL)
613D: 61         LD           H,C
613E: E2         LDFF00   (C),A
613F: 61         LD           H,C
6140: 7C         LD           A,H
6141: 6E         LD           L,(HL)
6142: 26 62      LD           H,$62
6144: FF         RST         0X38
6145: FF         RST         0X38
6146: 34         INC         (HL)
6147: 61         LD           H,C
6148: 68         LD           L,B
6149: 6E         LD           L,(HL)
614A: 67         LD           H,A
614B: 62         LD           H,D
614C: 6D         LD           L,L
614D: 6E         LD           L,(HL)
614E: 67         LD           H,A
614F: 62         LD           H,D
6150: FF         RST         0X38
6151: FF         RST         0X38
6152: 48         LD           C,B
6153: 61         LD           H,C
6154: 9D         SBC         L
6155: 32         LD           (HLD),A
6156: 83         ADD         A,E
6157: 80         ADD         A,B
6158: 9B         SBC         E
6159: 04         INC         B
615A: A2         AND         D
615B: 48         LD           C,B
615C: 01 48 48   LD           BC,$4848
615F: 9C         SBC         H
6160: 9B         SBC         E
6161: 04         INC         B
6162: 44         LD           B,H
6163: 01 44 44   LD           BC,$4444
6166: 9C         SBC         H
6167: 9B         SBC         E
6168: 04         INC         B
6169: 40         LD           B,B
616A: 01 40 40   LD           BC,$4040
616D: 9C         SBC         H
616E: 9B         SBC         E
616F: 04         INC         B
6170: 3E 01      LD           A,$01
6172: 3E 3E      LD           A,$3E
6174: 9C         SBC         H
6175: 9B         SBC         E
6176: 04         INC         B
6177: 30 01      JR           NC,$617A
6179: 30 30      JR           NC,$61AB
617B: 9C         SBC         H
617C: 9B         SBC         E
617D: 04         INC         B
617E: 2C         INC         L
617F: 01 2C 2C   LD           BC,$2C2C
6182: 9C         SBC         H
6183: 9B         SBC         E
6184: 07         RLCA
6185: 2E 01      LD           L,$01
6187: 2E 2E      LD           L,$2E
6189: 9C         SBC         H
618A: 2C         INC         L
618B: 01 2C 2C   LD           BC,$2C2C
618E: 00         NOP
618F: 9D         SBC         L
6190: 67         LD           H,A
6191: 86         ADD         A,(HL)
6192: 80         ADD         A,B
6193: 9F         SBC         A
6194: E8 00      ADD         SP,$00
6196: 9D         SBC         L
6197: 47         LD           B,A
6198: 86         ADD         A,(HL)
6199: 80         ADD         A,B
619A: 9F         SBC         A
619B: E8 00      ADD         SP,$00
619D: A2         AND         D
619E: 10 18      STOP       $18
61A0: 1E 26      LD           E,$26
61A2: A3         AND         E
61A3: 56         LD           D,(HL)
61A4: A2         AND         D
61A5: 58         LD           E,B
61A6: 5C         LD           E,H
61A7: A3         AND         E
61A8: 60         LD           H,B
61A9: A2         AND         D
61AA: 10 1E      STOP       $1E
61AC: 28 30      JR           Z,$61DE
61AE: 5C         LD           E,H
61AF: 58         LD           E,B
61B0: 5C         LD           E,H
61B1: 06 1E      LD           B,$1E
61B3: 58         LD           E,B
61B4: A3         AND         E
61B5: 56         LD           D,(HL)
61B6: A2         AND         D
61B7: 52         LD           D,D
61B8: 4E         LD           C,(HL)
61B9: 06 0E      LD           B,$0E
61BB: 14         INC         D
61BC: 1E A4      LD           E,$A4
61BE: 4E         LD           C,(HL)
61BF: A2         AND         D
61C0: 0C         INC         C
61C1: 16 1A      LD           D,$1A
61C3: 1E 54      LD           E,$54
61C5: 5E         LD           E,(HL)
61C6: 62         LD           H,D
61C7: A3         AND         E
61C8: 66         LD           H,(HL)
61C9: A2         AND         D
61CA: 16 0C      LD           D,$0C
61CC: 24         INC         H
61CD: 2E 3C      LD           L,$3C
61CF: 62         LD           H,D
61D0: 5E         LD           E,(HL)
61D1: A7         AND         A
61D2: 62         LD           H,D
61D3: A2         AND         D
61D4: 70         LD           (HL),B
61D5: 0A         LD           A,(BC)
61D6: 16 1A      LD           D,$1A
61D8: 28 A7      JR           Z,$6181
61DA: 6E         LD           L,(HL)
61DB: A2         AND         D
61DC: 7A         LD           A,D
61DD: 08 14 1A   LD           ($1A14),SP
61E0: 26 00      LD           H,$00
61E2: A2         AND         D
61E3: 28 30      JR           Z,$6215
61E5: 36 3E      LD           (HL),$3E
61E7: A3         AND         E
61E8: 6E         LD           L,(HL)
61E9: 01 A2 60   LD           BC,$60A2
61EC: 28 30      JR           Z,$621E
61EE: 36 01      LD           (HL),$01
61F0: 86         ADD         A,(HL)
61F1: 78         LD           A,B
61F2: 90         SUB         B
61F3: A2         AND         D
61F4: 8C         ADC         A,H
61F5: 4C         LD           C,H
61F6: 4E         LD           C,(HL)
61F7: 52         LD           D,D
61F8: A3         AND         E
61F9: 56         LD           D,(HL)
61FA: A2         AND         D
61FB: 58         LD           E,B
61FC: A4         AND         H
61FD: 5C         LD           E,H
61FE: A2         AND         D
61FF: 3E 3A      LD           A,$3A
6201: 34         INC         (HL)
6202: 3E 44      LD           A,$44
6204: 3A         LD           A,(HLD)
6205: 40         LD           B,B
6206: 48         LD           C,B
6207: 4E         LD           C,(HL)
6208: A3         AND         E
6209: 4E         LD           C,(HL)
620A: 01 A2 40   LD           BC,$40A2
620D: 22         LD           (HLI),A
620E: 28 30      JR           Z,$6240
6210: 40         LD           B,B
6211: 44         LD           B,H
6212: 48         LD           C,B
6213: 4C         LD           C,H
6214: 30 34      JR           NC,$624A
6216: 36 3E      LD           (HL),$3E
6218: A3         AND         E
6219: 4E         LD           C,(HL)
621A: A2         AND         D
621B: 52         LD           D,D
621C: A7         AND         A
621D: 56         LD           D,(HL)
621E: A2         AND         D
621F: 01 48 4E   LD           BC,$4E48
6222: 56         LD           D,(HL)
6223: 58         LD           E,B
6224: 5C         LD           E,H
6225: 00         NOP
6226: A4         AND         H
6227: 48         LD           C,B
6228: A2         AND         D
6229: 10 18      STOP       $18
622B: 1E 26      LD           E,$26
622D: 28 30      JR           Z,$625F
622F: 36 3E      LD           (HL),$3E
6231: 48         LD           C,B
6232: 4C         LD           C,H
6233: 4E         LD           C,(HL)
6234: 52         LD           D,D
6235: A7         AND         A
6236: 44         LD           B,H
6237: A2         AND         D
6238: 5C         LD           E,H
6239: 26 2C      LD           H,$2C
623B: 30 34      JR           NC,$6271
623D: 36 6E      LD           (HL),$6E
623F: 66         LD           H,(HL)
6240: 74         LD           (HL),H
6241: 8C         ADC         A,H
6242: 26 2C      LD           H,$2C
6244: 36 A7      LD           (HL),$A7
6246: 76         HALT
6247: A2         AND         D
6248: 8E         ADC         A,(HL)
6249: 3C         INC         A
624A: 46         LD           B,(HL)
624B: 4A         LD           C,D
624C: A3         AND         E
624D: 4E         LD           C,(HL)
624E: A2         AND         D
624F: 16 0C      LD           D,$0C
6251: 24         INC         H
6252: 2E 3C      LD           L,$3C
6254: 4A         LD           C,D
6255: 46         LD           B,(HL)
6256: A7         AND         A
6257: 4A         LD           C,D
6258: A2         AND         D
6259: 58         LD           E,B
625A: 22         LD           (HLI),A
625B: 24         INC         H
625C: 28 2E      JR           Z,$628C
625E: A7         AND         A
625F: 56         LD           D,(HL)
6260: A2         AND         D
6261: 62         LD           H,D
6262: 38 3E      JR           C,$62A2
6264: 44         LD           B,H
6265: 4A         LD           C,D
6266: 00         NOP
6267: 9B         SBC         E
6268: 04         INC         B
6269: 99         SBC         C
626A: A2         AND         D
626B: 40         LD           B,B
626C: 01 40 40   LD           BC,$4040
626F: 9C         SBC         H
6270: 9B         SBC         E
6271: 04         INC         B
6272: 3E 01      LD           A,$01
6274: 3E 3E      LD           A,$3E
6276: 9C         SBC         H
6277: 9B         SBC         E
6278: 04         INC         B
6279: 3A         LD           A,(HLD)
627A: 01 3A 3A   LD           BC,$3A3A
627D: 9C         SBC         H
627E: 9B         SBC         E
627F: 04         INC         B
6280: 30 01      JR           NC,$6283
6282: 30 30      JR           NC,$62B4
6284: 9C         SBC         H
6285: 9B         SBC         E
6286: 04         INC         B
6287: 28 01      JR           Z,$628A
6289: 28 28      JR           Z,$62B3
628B: 9C         SBC         H
628C: 9B         SBC         E
628D: 04         INC         B
628E: 26 01      LD           H,$01
6290: 26 26      LD           H,$26
6292: 9C         SBC         H
6293: 9B         SBC         E
6294: 04         INC         B
6295: 24         INC         H
6296: 01 24 24   LD           BC,$2424
6299: 9C         SBC         H
629A: 9B         SBC         E
629B: 02         LD           (BC),A
629C: 22         LD           (HLI),A
629D: 01 22 22   LD           BC,$2222
62A0: 9C         SBC         H
62A1: 9B         SBC         E
62A2: 02         LD           (BC),A
62A3: 20 01      JR           NZ,$62A6
62A5: 20 20      JR           NZ,$62C7
62A7: 9C         SBC         H
62A8: 00         NOP
62A9: 00         NOP
62AA: B6         OR           (HL)
62AB: 4A         LD           C,D
62AC: B4         OR           H
62AD: 62         LD           H,D
62AE: D0         RET         NC
62AF: 62         LD           H,D
62B0: 17         RLA
62B1: 4B         LD           C,E
62B2: 00         NOP
62B3: 00         NOP
62B4: 7D         LD           A,L
62B5: 6D         LD           L,L
62B6: 10 6D      STOP       $6D
62B8: F2                              
62B9: 62         LD           H,D
62BA: 09         ADD         HL,BC
62BB: 6E         LD           L,(HL)
62BC: F2                              
62BD: 62         LD           H,D
62BE: 04         INC         B
62BF: 63         LD           H,E
62C0: 2D         DEC         L
62C1: 6D         LD           L,L
62C2: A8         XOR         B
62C3: 6E         LD           L,(HL)
62C4: 7D         LD           A,L
62C5: 6D         LD           L,L
62C6: 47         LD           B,A
62C7: 51         LD           D,C
62C8: 47         LD           B,A
62C9: 51         LD           D,C
62CA: 47         LD           B,A
62CB: 51         LD           D,C
62CC: 20 6D      JR           NZ,$633B
62CE: 00         NOP
62CF: 00         NOP
62D0: F0 6D      LD           A,($6D)
62D2: F2                              
62D3: 62         LD           H,D
62D4: E1         POP         HL
62D5: 6D         LD           L,L
62D6: 94         SUB         H
62D7: 6E         LD           L,(HL)
62D8: F2                              
62D9: 62         LD           H,D
62DA: 13         INC         DE
62DB: 6E         LD           L,(HL)
62DC: 7C         LD           A,H
62DD: 6E         LD           L,(HL)
62DE: 04         INC         B
62DF: 63         LD           H,E
62E0: 22         LD           (HLI),A
62E1: 6E         LD           L,(HL)
62E2: A8         XOR         B
62E3: 6E         LD           L,(HL)
62E4: 47         LD           B,A
62E5: 51         LD           D,C
62E6: CD 6D 47   CALL       $476D
62E9: 51         LD           D,C
62EA: 0E 6E      LD           C,$6E
62EC: 47         LD           B,A
62ED: 51         LD           D,C
62EE: 20 6D      JR           NZ,$635D
62F0: 00         NOP
62F1: 00         NOP
62F2: A1         AND         C
62F3: 2E 34      LD           L,$34
62F5: 3C         INC         A
62F6: 44         LD           B,H
62F7: 46         LD           B,(HL)
62F8: 4C         LD           C,H
62F9: 54         LD           D,H
62FA: 5C         LD           E,H
62FB: 2C         INC         L
62FC: 32         LD           (HLD),A
62FD: 3A         LD           A,(HLD)
62FE: 42         LD           B,D
62FF: 44         LD           B,H
6300: 42         LD           B,D
6301: 3A         LD           A,(HLD)
6302: 32         LD           (HLD),A
6303: 00         NOP
6304: A1         AND         C
6305: 38 3E      JR           C,$6345
6307: 46         LD           B,(HL)
6308: 4E         LD           C,(HL)
6309: 50         LD           D,B
630A: 56         LD           D,(HL)
630B: 5E         LD           E,(HL)
630C: 66         LD           H,(HL)
630D: 00         NOP
630E: 00         NOP
630F: D4 4A 19   CALL       NC,$194A
6312: 63         LD           H,E
6313: 29         ADD         HL,HL
6314: 63         LD           H,E
6315: 55         LD           D,L
6316: 63         LD           H,E
6317: 00         NOP
6318: 00         NOP
6319: A0         AND         B
631A: 6D         LD           L,L
631B: C7         RST         0X00
631C: 63         LD           H,E
631D: 3B         DEC         SP
631E: 6E         LD           L,(HL)
631F: E7         RST         0X20
6320: 63         LD           H,E
6321: A0         AND         B
6322: 6D         LD           L,L
6323: 18 64      JR           $6389
6325: FF         RST         0X38
6326: FF         RST         0X38
6327: 19         ADD         HL,DE
6328: 63         LD           H,E
6329: AA         XOR         D
632A: 6D         LD           L,L
632B: 65         LD           H,L
632C: 63         LD           H,E
632D: AA         XOR         D
632E: 6D         LD           L,L
632F: 65         LD           H,L
6330: 63         LD           H,E
6331: AA         XOR         D
6332: 6D         LD           L,L
6333: 8B         ADC         A,E
6334: 63         LD           H,E
6335: AA         XOR         D
6336: 6D         LD           L,L
6337: 65         LD           H,L
6338: 63         LD           H,E
6339: AA         XOR         D
633A: 6D         LD           L,L
633B: 65         LD           H,L
633C: 63         LD           H,E
633D: AA         XOR         D
633E: 6D         LD           L,L
633F: 65         LD           H,L
6340: 63         LD           H,E
6341: AA         XOR         D
6342: 6D         LD           L,L
6343: 8B         ADC         A,E
6344: 63         LD           H,E
6345: AF         XOR         A
6346: 6D         LD           L,L
6347: A9         XOR         C
6348: 63         LD           H,E
6349: AA         XOR         D
634A: 6D         LD           L,L
634B: 8B         ADC         A,E
634C: 63         LD           H,E
634D: AF         XOR         A
634E: 6D         LD           L,L
634F: A9         XOR         C
6350: 63         LD           H,E
6351: FF         RST         0X38
6352: FF         RST         0X38
6353: 29         ADD         HL,HL
6354: 63         LD           H,E
6355: 6D         LD           L,L
6356: 6E         LD           L,(HL)
6357: 33         INC         SP
6358: 64         LD           H,H
6359: 6D         LD           L,L
635A: 6E         LD           L,(HL)
635B: 54         LD           D,H
635C: 64         LD           H,H
635D: 6D         LD           L,L
635E: 6E         LD           L,(HL)
635F: 5A         LD           E,D
6360: 64         LD           H,H
6361: FF         RST         0X38
6362: FF         RST         0X38
6363: 55         LD           D,L
6364: 63         LD           H,E
6365: A2         AND         D
6366: 02         LD           (BC),A
6367: 0E 04      LD           C,$04
6369: 0C         INC         C
636A: 01 04 9D   LD           BC,$9D04
636D: 92         SUB         D
636E: 00         NOP
636F: C0         RET         NZ
6370: 02         LD           (BC),A
6371: 0E 04      LD           C,$04
6373: 0C         INC         C
6374: 01 04 9D   LD           BC,$9D04
6377: B2         OR           D
6378: 00         NOP
6379: C0         RET         NZ
637A: 02         LD           (BC),A
637B: 0E 04      LD           C,$04
637D: 0C         INC         C
637E: 01 04 9D   LD           BC,$9D04
6381: 92         SUB         D
6382: 00         NOP
6383: C0         RET         NZ
6384: 02         LD           (BC),A
6385: 0E 04      LD           C,$04
6387: 0C         INC         C
6388: 01 04 00   LD           BC,$0004
638B: 9B         SBC         E
638C: 02         LD           (BC),A
638D: 02         LD           (BC),A
638E: 0E 04      LD           C,$04
6390: 0C         INC         C
6391: 01 04 9C   LD           BC,$9C04
6394: 9D         SBC         L
6395: 92         SUB         D
6396: 00         NOP
6397: C0         RET         NZ
6398: 02         LD           (BC),A
6399: 0E 04      LD           C,$04
639B: 0C         INC         C
639C: 01 04 9D   LD           BC,$9D04
639F: B2         OR           D
63A0: 00         NOP
63A1: C0         RET         NZ
63A2: 02         LD           (BC),A
63A3: 0E 04      LD           C,$04
63A5: 0C         INC         C
63A6: 01 04 00   LD           BC,$0004
63A9: 02         LD           (BC),A
63AA: 0E 04      LD           C,$04
63AC: 0C         INC         C
63AD: 01 04 9D   LD           BC,$9D04
63B0: 92         SUB         D
63B1: 00         NOP
63B2: C0         RET         NZ
63B3: 02         LD           (BC),A
63B4: 0E 04      LD           C,$04
63B6: 0C         INC         C
63B7: 01 04 9D   LD           BC,$9D04
63BA: 62         LD           H,D
63BB: 00         NOP
63BC: C0         RET         NZ
63BD: 9B         SBC         E
63BE: 02         LD           (BC),A
63BF: 02         LD           (BC),A
63C0: 0E 04      LD           C,$04
63C2: 0C         INC         C
63C3: 01 04 9C   LD           BC,$9C04
63C6: 00         NOP
63C7: AE         XOR         (HL)
63C8: 01 01 9B   LD           BC,$9B01
63CB: 02         LD           (BC),A
63CC: A1         AND         C
63CD: 32         LD           (HLD),A
63CE: 32         LD           (HLD),A
63CF: 32         LD           (HLD),A
63D0: 32         LD           (HLD),A
63D1: 34         INC         (HL)
63D2: 32         LD           (HLD),A
63D3: A2         AND         D
63D4: 32         LD           (HLD),A
63D5: AE         XOR         (HL)
63D6: 01 A8 01   LD           BC,$01A8
63D9: A2         AND         D
63DA: 01 4A A1   LD           BC,$A14A
63DD: 32         LD           (HLD),A
63DE: 32         LD           (HLD),A
63DF: A7         AND         A
63E0: 01 A5 01   LD           BC,$01A5
63E3: AE         XOR         (HL)
63E4: 01 9C 00   LD           BC,$009C
63E7: A1         AND         C
63E8: 01 50 54   LD           BC,$5450
63EB: 56         LD           D,(HL)
63EC: 64         LD           H,H
63ED: A3         AND         E
63EE: 5E         LD           E,(HL)
63EF: A1         AND         C
63F0: 5E         LD           E,(HL)
63F1: 62         LD           H,D
63F2: 01 AE 01   LD           BC,$01AE
63F5: A4         AND         H
63F6: 01 A1 68   LD           BC,$68A1
63F9: 62         LD           H,D
63FA: 5E         LD           E,(HL)
63FB: 5C         LD           E,H
63FC: AE         XOR         (HL)
63FD: 01 A9 2C   LD           BC,$2CA9
6400: A0         AND         B
6401: 01 A1 2C   LD           BC,$2CA1
6404: A7         AND         A
6405: 01 A5 01   LD           BC,$01A5
6408: A1         AND         C
6409: 62         LD           H,D
640A: 5E         LD           E,(HL)
640B: 52         LD           D,D
640C: 50         LD           D,B
640D: A5         AND         L
640E: 01 01 A4   LD           BC,$A401
6411: 01 A2 30   LD           BC,$30A2
6414: A1         AND         C
6415: 32         LD           (HLD),A
6416: 01 00 A1   LD           BC,$A100
6419: 2C         INC         L
641A: 2C         INC         L
641B: 2C         INC         L
641C: 2C         INC         L
641D: 2E 2C      LD           L,$2C
641F: A2         AND         D
6420: 2C         INC         L
6421: AE         XOR         (HL)
6422: 01 A5 01   LD           BC,$01A5
6425: A1         AND         C
6426: 22         LD           (HLI),A
6427: 22         LD           (HLI),A
6428: 22         LD           (HLI),A
6429: 22         LD           (HLI),A
642A: 24         INC         H
642B: 22         LD           (HLI),A
642C: A2         AND         D
642D: 22         LD           (HLI),A
642E: A5         AND         L
642F: 01 AE 01   LD           BC,$01AE
6432: 00         NOP
6433: 99         SBC         C
6434: AE         XOR         (HL)
6435: 01 01 9B   LD           BC,$9B01
6438: 02         LD           (BC),A
6439: A1         AND         C
643A: 2E 2E      LD           L,$2E
643C: 2E 2E      LD           L,$2E
643E: 30 2E      JR           NC,$646E
6440: A2         AND         D
6441: 2E AE      LD           L,$AE
6443: 01 A8 01   LD           BC,$01A8
6446: A2         AND         D
6447: 01 46 A1   LD           BC,$A146
644A: 2E 2E      LD           L,$2E
644C: A7         AND         A
644D: 01 AE 01   LD           BC,$01AE
6450: A5         AND         L
6451: 01 9C 00   LD           BC,$009C
6454: 9B         SBC         E
6455: 0C         INC         C
6456: A8         XOR         B
6457: 01 9C 00   LD           BC,$009C
645A: A1         AND         C
645B: 24         INC         H
645C: 24         INC         H
645D: 24         INC         H
645E: 24         INC         H
645F: 26 24      LD           H,$24
6461: 24         INC         H
6462: 01 A5 01   LD           BC,$01A5
6465: AE         XOR         (HL)
6466: 01 A1 1A   LD           BC,$1AA1
6469: 1A         LD           A,(DE)
646A: 1A         LD           A,(DE)
646B: 1A         LD           A,(DE)
646C: 34         INC         (HL)
646D: 1A         LD           A,(DE)
646E: 1A         LD           A,(DE)
646F: 01 A5 01   LD           BC,$01A5
6472: AE         XOR         (HL)
6473: 01 00 00   LD           BC,$0000
6476: B6         OR           (HL)
6477: 4A         LD           C,D
6478: 80         ADD         A,B
6479: 64         LD           H,H
647A: B4         OR           H
647B: 64         LD           H,H
647C: 17         RLA
647D: 4B         LD           C,E
647E: 17         RLA
647F: 4B         LD           C,E
6480: 7F         LD           A,A
6481: 6E         LD           L,(HL)
6482: 0E 6E      LD           C,$6E
6484: C0         RET         NZ
6485: 64         LD           H,H
6486: C0         RET         NZ
6487: 64         LD           H,H
6488: 13         INC         DE
6489: 6E         LD           L,(HL)
648A: C0         RET         NZ
648B: 64         LD           H,H
648C: D7         RST         0X10
648D: 64         LD           H,H
648E: E0 64      LDFF00   ($64),A
6490: E9         JP           (HL)
6491: 64         LD           H,H
6492: 0E 6E      LD           C,$6E
6494: F2                              
6495: 64         LD           H,H
6496: 13         INC         DE
6497: 6E         LD           L,(HL)
6498: FB         EI
6499: 64         LD           H,H
649A: 1D         DEC         E
649B: 6E         LD           L,(HL)
649C: 04         INC         B
649D: 65         LD           H,L
649E: 13         INC         DE
649F: 6E         LD           L,(HL)
64A0: 0D         DEC         C
64A1: 65         LD           H,L
64A2: 0E 6E      LD           C,$6E
64A4: 16 65      LD           D,$65
64A6: 13         INC         DE
64A7: 6E         LD           L,(HL)
64A8: 1F         RRA
64A9: 65         LD           H,L
64AA: 1D         DEC         E
64AB: 6E         LD           L,(HL)
64AC: 28 65      JR           Z,$6513
64AE: 42         LD           B,D
64AF: 65         LD           H,L
64B0: FF         RST         0X38
64B1: FF         RST         0X38
64B2: 88         ADC         A,B
64B3: 64         LD           H,H
64B4: 20 6D      JR           NZ,$6523
64B6: 20 6D      JR           NZ,$6525
64B8: 2C         INC         L
64B9: 6E         LD           L,(HL)
64BA: 4B         LD           C,E
64BB: 65         LD           H,L
64BC: FF         RST         0X38
64BD: FF         RST         0X38
64BE: B8         CP           B
64BF: 64         LD           H,H
64C0: A3         AND         E
64C1: 28 32      JR           Z,$64F5
64C3: 30 32      JR           NC,$64F7
64C5: 38 32      JR           C,$64F9
64C7: 30 32      JR           NC,$64FB
64C9: 00         NOP
64CA: 9B         SBC         E
64CB: 02         LD           (BC),A
64CC: A2         AND         D
64CD: 28 32      JR           Z,$6501
64CF: 30 32      JR           NC,$6503
64D1: 38 32      JR           C,$6505
64D3: 30 32      JR           NC,$6507
64D5: 9C         SBC         H
64D6: 00         NOP
64D7: 2A         LD           A,(HLI)
64D8: 32         LD           (HLD),A
64D9: 30 32      JR           NC,$650D
64DB: 38 32      JR           C,$650F
64DD: 30 32      JR           NC,$6511
64DF: 00         NOP
64E0: 2A         LD           A,(HLI)
64E1: 36 32      LD           (HL),$32
64E3: 36 3C      LD           (HL),$3C
64E5: 36 32      LD           (HL),$32
64E7: 36 00      LD           (HL),$00
64E9: 28 38      JR           Z,$6523
64EB: 36 38      LD           (HL),$38
64ED: 40         LD           B,B
64EE: 38 36      JR           C,$6526
64F0: 38 00      JR           C,$64F2
64F2: 32         LD           (HLD),A
64F3: 38 36      JR           C,$652B
64F5: 38 42      JR           C,$6539
64F7: 38 36      JR           C,$652F
64F9: 38 00      JR           C,$64FB
64FB: 2A         LD           A,(HLI)
64FC: 36 32      LD           (HL),$32
64FE: 36 3C      LD           (HL),$3C
6500: 36 32      LD           (HL),$32
6502: 36 00      LD           (HL),$00
6504: 2E 36      LD           L,$36
6506: 32         LD           (HLD),A
6507: 36 3C      LD           (HL),$3C
6509: 36 32      LD           (HL),$32
650B: 36 00      LD           (HL),$00
650D: 2E 38      LD           L,$38
650F: 36 38      LD           (HL),$38
6511: 40         LD           B,B
6512: 38 36      JR           C,$654A
6514: 38 00      JR           C,$6516
6516: 2A         LD           A,(HLI)
6517: 38 36      JR           C,$654F
6519: 38 42      JR           C,$655D
651B: 38 36      JR           C,$6553
651D: 38 00      JR           C,$651F
651F: 2C         INC         L
6520: 36 32      LD           (HL),$32
6522: 36 3E      LD           (HL),$3E
6524: 36 32      LD           (HL),$32
6526: 36 00      LD           (HL),$00
6528: 28 36      JR           Z,$6560
652A: 32         LD           (HLD),A
652B: 36 40      LD           (HL),$40
652D: 36 32      LD           (HL),$32
652F: 36 00      LD           (HL),$00
6531: 30 36      JR           NC,$6569
6533: 3C         INC         A
6534: 42         LD           B,D
6535: 48         LD           C,B
6536: 4E         LD           C,(HL)
6537: 54         LD           D,H
6538: 5A         LD           E,D
6539: 58         LD           E,B
653A: 54         LD           D,H
653B: 4E         LD           C,(HL)
653C: 48         LD           C,B
653D: 40         LD           B,B
653E: 3C         INC         A
653F: 36 30      LD           (HL),$30
6541: 00         NOP
6542: 30 36      JR           NC,$657A
6544: 3C         INC         A
6545: 42         LD           B,D
6546: 48         LD           C,B
6547: 4E         LD           C,(HL)
6548: 54         LD           D,H
6549: 5A         LD           E,D
654A: 00         NOP
654B: 9B         SBC         E
654C: 02         LD           (BC),A
654D: A3         AND         E
654E: 4A         LD           C,D
654F: 4E         LD           C,(HL)
6550: AE         XOR         (HL)
6551: 50         LD           D,B
6552: 9C         SBC         H
6553: A5         AND         L
6554: 4E         LD           C,(HL)
6555: 48         LD           C,B
6556: AE         XOR         (HL)
6557: 4A         LD           C,D
6558: A4         AND         H
6559: 01 A3 4A   LD           BC,$4AA3
655C: 4E         LD           C,(HL)
655D: AE         XOR         (HL)
655E: 50         LD           D,B
655F: A3         AND         E
6560: 4E         LD           C,(HL)
6561: 50         LD           D,B
6562: A5         AND         L
6563: 54         LD           D,H
6564: A4         AND         H
6565: 01 A3 46   LD           BC,$46A3
6568: 4E         LD           C,(HL)
6569: A5         AND         L
656A: 54         LD           D,H
656B: A4         AND         H
656C: 5A         LD           E,D
656D: AE         XOR         (HL)
656E: 58         LD           E,B
656F: A4         AND         H
6570: 01 A5 54   LD           BC,$54A5
6573: 54         LD           D,H
6574: 56         LD           D,(HL)
6575: 56         LD           D,(HL)
6576: 58         LD           E,B
6577: 58         LD           E,B
6578: 01 01 00   LD           BC,$0001
657B: 00         NOP
657C: E3                              
657D: 4A         LD           C,D
657E: 86         ADD         A,(HL)
657F: 65         LD           H,L
6580: BA         CP           D
6581: 65         LD           H,L
6582: 17         RLA
6583: 4B         LD           C,E
6584: 00         NOP
6585: 00         NOP
6586: 24         INC         H
6587: 6D         LD           L,L
6588: 7D         LD           A,L
6589: 6D         LD           L,L
658A: CA 64 D7   JP           Z,$D764
658D: 64         LD           H,H
658E: D7         RST         0X10
658F: 64         LD           H,H
6590: E0 64      LDFF00   ($64),A
6592: E0 64      LDFF00   ($64),A
6594: E9         JP           (HL)
6595: 64         LD           H,H
6596: E9         JP           (HL)
6597: 64         LD           H,H
6598: F2                              
6599: 64         LD           H,H
659A: F2                              
659B: 64         LD           H,H
659C: FB         EI
659D: 64         LD           H,H
659E: FB         EI
659F: 64         LD           H,H
65A0: 04         INC         B
65A1: 65         LD           H,L
65A2: 04         INC         B
65A3: 65         LD           H,L
65A4: 0D         DEC         C
65A5: 65         LD           H,L
65A6: 0D         DEC         C
65A7: 65         LD           H,L
65A8: 16 65      LD           D,$65
65AA: 16 65      LD           D,$65
65AC: 1F         RRA
65AD: 65         LD           H,L
65AE: 1F         RRA
65AF: 65         LD           H,L
65B0: 28 65      JR           Z,$6617
65B2: 28 65      JR           Z,$6619
65B4: 31 65 FF   LD           SP,$FF65
65B7: FF         RST         0X38
65B8: 88         ADC         A,B
65B9: 65         LD           H,L
65BA: 0E 6E      LD           C,$6E
65BC: CA 64 D7   JP           Z,$D764
65BF: 64         LD           H,H
65C0: 13         INC         DE
65C1: 6E         LD           L,(HL)
65C2: D7         RST         0X10
65C3: 64         LD           H,H
65C4: CD 6D E0   CALL       $E06D
65C7: 64         LD           H,H
65C8: FA 6D E0   LD           A,($E06D)
65CB: 64         LD           H,H
65CC: 13         INC         DE
65CD: 6E         LD           L,(HL)
65CE: E9         JP           (HL)
65CF: 64         LD           H,H
65D0: 0E 6E      LD           C,$6E
65D2: E9         JP           (HL)
65D3: 64         LD           H,H
65D4: F2                              
65D5: 64         LD           H,H
65D6: 13         INC         DE
65D7: 6E         LD           L,(HL)
65D8: F2                              
65D9: 64         LD           H,H
65DA: CD 6D FB   CALL       $FB6D
65DD: 64         LD           H,H
65DE: 0E 6E      LD           C,$6E
65E0: FB         EI
65E1: 64         LD           H,H
65E2: 09         ADD         HL,BC
65E3: 6E         LD           L,(HL)
65E4: 04         INC         B
65E5: 65         LD           H,L
65E6: 0E 6E      LD           C,$6E
65E8: 04         INC         B
65E9: 65         LD           H,L
65EA: 13         INC         DE
65EB: 6E         LD           L,(HL)
65EC: 0D         DEC         C
65ED: 65         LD           H,L
65EE: 09         ADD         HL,BC
65EF: 6E         LD           L,(HL)
65F0: 0D         DEC         C
65F1: 65         LD           H,L
65F2: 0E 6E      LD           C,$6E
65F4: 16 65      LD           D,$65
65F6: 13         INC         DE
65F7: 6E         LD           L,(HL)
65F8: 16 65      LD           D,$65
65FA: CD 6D 1F   CALL       $1F6D
65FD: 65         LD           H,L
65FE: FA 6D 1F   LD           A,($1F6D)
6601: 65         LD           H,L
6602: 28 65      JR           Z,$6669
6604: E6 6D      AND         $6D
6606: 28 65      JR           Z,$666D
6608: CD 6D 31   CALL       $316D
660B: 65         LD           H,L
660C: FF         RST         0X38
660D: FF         RST         0X38
660E: BA         CP           D
660F: 65         LD           H,L
6610: 00         NOP
6611: E3                              
6612: 4A         LD           C,D
6613: 17         RLA
6614: 4B         LD           C,E
6615: 1B         DEC         DE
6616: 66         LD           H,(HL)
6617: 17         RLA
6618: 4B         LD           C,E
6619: 00         NOP
661A: 00         NOP
661B: F5         PUSH       AF
661C: 6D         LD           L,L
661D: 25         DEC         H
661E: 66         LD           H,(HL)
661F: 20 6D      JR           NZ,$668E
6621: FF         RST         0X38
6622: FF         RST         0X38
6623: 1B         DEC         DE
6624: 66         LD           H,(HL)
6625: A2         AND         D
6626: 02         LD           (BC),A
6627: 0E 0C      LD           C,$0C
6629: A7         AND         A
662A: 01 A6 01   LD           BC,$01A6
662D: A1         AND         C
662E: 02         LD           (BC),A
662F: A2         AND         D
6630: 02         LD           (BC),A
6631: 0E A1      LD           C,$A1
6633: 0C         INC         C
6634: 18 00      JR           $6636
6636: 00         NOP
6637: B6         OR           (HL)
6638: 4A         LD           C,D
6639: 41         LD           B,C
663A: 66         LD           H,(HL)
663B: 4D         LD           C,L
663C: 66         LD           H,(HL)
663D: 17         RLA
663E: 4B         LD           C,E
663F: 00         NOP
6640: 00         NOP
6641: 09         ADD         HL,BC
6642: 6E         LD           L,(HL)
6643: 24         INC         H
6644: 6D         LD           L,L
6645: 10 6D      STOP       $6D
6647: 53         LD           D,E
6648: 66         LD           H,(HL)
6649: FF         RST         0X38
664A: FF         RST         0X38
664B: 47         LD           B,A
664C: 66         LD           H,(HL)
664D: CD 6D FF   CALL       $FF6D
6650: FF         RST         0X38
6651: 47         LD           B,A
6652: 66         LD           H,(HL)
6653: A3         AND         E
6654: 32         LD           (HLD),A
6655: 46         LD           B,(HL)
6656: 58         LD           E,B
6657: 66         LD           H,(HL)
6658: 70         LD           (HL),B
6659: 01 A3 2E   LD           BC,$2EA3
665C: 42         LD           B,D
665D: 54         LD           D,H
665E: 62         LD           H,D
665F: 6C         LD           L,H
6660: 01 00 00   LD           BC,$0000
6663: C5         PUSH       BC
6664: 4A         LD           C,D
6665: 6D         LD           L,L
6666: 66         LD           H,(HL)
6667: 7B         LD           A,E
6668: 66         LD           H,(HL)
6669: 17         RLA
666A: 4B         LD           C,E
666B: 00         NOP
666C: 00         NOP
666D: 09         ADD         HL,BC
666E: 6E         LD           L,(HL)
666F: 10 6D      STOP       $6D
6671: 85         ADD         A,L
6672: 66         LD           H,(HL)
6673: 9B         SBC         E
6674: 66         LD           H,(HL)
6675: AB         XOR         E
6676: 66         LD           H,(HL)
6677: FF         RST         0X38
6678: FF         RST         0X38
6679: 75         LD           (HL),L
667A: 66         LD           H,(HL)
667B: 0E 6E      LD           C,$6E
667D: 85         ADD         A,L
667E: 66         LD           H,(HL)
667F: 8F         ADC         A,A
6680: 66         LD           H,(HL)
6681: FF         RST         0X38
6682: FF         RST         0X38
6683: 7F         LD           A,A
6684: 66         LD           H,(HL)
6685: A1         AND         C
6686: 8E         ADC         A,(HL)
6687: 8C         ADC         A,H
6688: 84         ADD         A,H
6689: 7C         LD           A,H
668A: 76         HALT
668B: 74         LD           (HL),H
668C: 6C         LD           L,H
668D: 64         LD           H,H
668E: 00         NOP
668F: 9B         SBC         E
6690: 03         INC         BC
6691: A7         AND         A
6692: 74         LD           (HL),H
6693: 01 9C A2   LD           BC,$A29C
6696: 74         LD           (HL),H
6697: 74         LD           (HL),H
6698: A4         AND         H
6699: 01 00 A4   LD           BC,$A400
669C: 01 A6 01   LD           BC,$01A6
669F: 9B         SBC         E
66A0: 02         LD           (BC),A
66A1: A7         AND         A
66A2: 54         LD           D,H
66A3: 01 9C A2   LD           BC,$A29C
66A6: 54         LD           D,H
66A7: 54         LD           D,H
66A8: A4         AND         H
66A9: 01 00 9B   LD           BC,$9B00
66AC: 03         INC         BC
66AD: A7         AND         A
66AE: 54         LD           D,H
66AF: 01 9C A2   LD           BC,$A29C
66B2: 54         LD           D,H
66B3: 54         LD           D,H
66B4: A4         AND         H
66B5: 01 00 00   LD           BC,$0000
66B8: C5         PUSH       BC
66B9: 4A         LD           C,D
66BA: C2 66 D4   JP           NZ,$D466
66BD: 66         LD           H,(HL)
66BE: E6 66      AND         $66
66C0: 00         NOP
66C1: 00         NOP
66C2: 7D         LD           A,L
66C3: 6D         LD           L,L
66C4: 10 6D      STOP       $6D
66C6: F6 66      OR           $66
66C8: A4         AND         H
66C9: 6E         LD           L,(HL)
66CA: 09         ADD         HL,BC
66CB: 6E         LD           L,(HL)
66CC: 45         LD           B,L
66CD: 67         LD           H,A
66CE: A8         XOR         B
66CF: 6E         LD           L,(HL)
66D0: FF         RST         0X38
66D1: FF         RST         0X38
66D2: C2 66 A0   JP           NZ,$A066
66D5: 6D         LD           L,L
66D6: F6 66      OR           $66
66D8: 10 6D      STOP       $6D
66DA: A4         AND         H
66DB: 6E         LD           L,(HL)
66DC: BE         CP           (HL)
66DD: 6D         LD           L,L
66DE: 19         ADD         HL,DE
66DF: 67         LD           H,A
66E0: A8         XOR         B
66E1: 6E         LD           L,(HL)
66E2: FF         RST         0X38
66E3: FF         RST         0X38
66E4: D4 66 10   CALL       NC,$1066
66E7: 6D         LD           L,L
66E8: 18 6D      JR           $6757
66EA: A4         AND         H
66EB: 6E         LD           L,(HL)
66EC: 68         LD           L,B
66ED: 6E         LD           L,(HL)
66EE: 00         NOP
66EF: 67         LD           H,A
66F0: A8         XOR         B
66F1: 6E         LD           L,(HL)
66F2: FF         RST         0X38
66F3: FF         RST         0X38
66F4: E6 66      AND         $66
66F6: A1         AND         C
66F7: 8E         ADC         A,(HL)
66F8: 8C         ADC         A,H
66F9: 84         ADD         A,H
66FA: 7C         LD           A,H
66FB: 76         HALT
66FC: 74         LD           (HL),H
66FD: 6C         LD           L,H
66FE: 64         LD           H,H
66FF: 00         NOP
6700: 9B         SBC         E
6701: 02         LD           (BC),A
6702: A3         AND         E
6703: 01 A6 88   LD           BC,$88A6
6706: A1         AND         C
6707: 01 AE 01   LD           BC,$01AE
670A: 01 01 A5   LD           BC,$A501
670D: 01 9C A3   LD           BC,$A39C
6710: 01 A6 88   LD           BC,$88A6
6713: A1         AND         C
6714: 01 AE 01   LD           BC,$01AE
6717: 01 00 9D   LD           BC,$9D00
671A: 61         LD           H,C
671B: 86         ADD         A,(HL)
671C: 80         ADD         A,B
671D: 9B         SBC         E
671E: 02         LD           (BC),A
671F: A3         AND         E
6720: 64         LD           H,H
6721: 68         LD           L,B
6722: 6A         LD           L,D
6723: 82         ADD         A,D
6724: A5         AND         L
6725: 01 A3 01   LD           BC,$01A3
6728: 80         ADD         A,B
6729: 7C         LD           A,H
672A: 6A         LD           L,D
672B: A5         AND         L
672C: 01 9C A3   LD           BC,$A39C
672F: 64         LD           H,H
6730: 68         LD           L,B
6731: 6A         LD           L,D
6732: 01 01 68   LD           BC,$6801
6735: 64         LD           H,H
6736: 58         LD           E,B
6737: 5E         LD           E,(HL)
6738: 64         LD           H,H
6739: A8         XOR         B
673A: 01 A3 68   LD           BC,$68A3
673D: 6A         LD           L,D
673E: 6E         LD           L,(HL)
673F: 70         LD           (HL),B
6740: 88         ADC         A,B
6741: AE         XOR         (HL)
6742: 01 01 00   LD           BC,$0001
6745: 9B         SBC         E
6746: 04         INC         B
6747: A2         AND         D
6748: 54         LD           D,H
6749: 5C         LD           E,H
674A: 4C         LD           C,H
674B: 52         LD           D,D
674C: 54         LD           D,H
674D: 52         LD           D,D
674E: 4C         LD           C,H
674F: 44         LD           B,H
6750: 9C         SBC         H
6751: 9B         SBC         E
6752: 04         INC         B
6753: 52         LD           D,D
6754: 58         LD           E,B
6755: 48         LD           C,B
6756: 50         LD           D,B
6757: 52         LD           D,D
6758: 58         LD           E,B
6759: 60         LD           H,B
675A: 68         LD           L,B
675B: 9C         SBC         H
675C: 9B         SBC         E
675D: 04         INC         B
675E: 50         LD           D,B
675F: 58         LD           E,B
6760: 46         LD           B,(HL)
6761: 4C         LD           C,H
6762: 50         LD           D,B
6763: 4C         LD           C,H
6764: 46         LD           B,(HL)
6765: 40         LD           B,B
6766: 9C         SBC         H
6767: 9B         SBC         E
6768: 03         INC         BC
6769: 52         LD           D,D
676A: 58         LD           E,B
676B: 48         LD           C,B
676C: 50         LD           D,B
676D: 52         LD           D,D
676E: 58         LD           E,B
676F: 60         LD           H,B
6770: 68         LD           L,B
6771: 9C         SBC         H
6772: 52         LD           D,D
6773: 58         LD           E,B
6774: 48         LD           C,B
6775: 50         LD           D,B
6776: 00         NOP
6777: 00         NOP
6778: C5         PUSH       BC
6779: 4A         LD           C,D
677A: 82         ADD         A,D
677B: 67         LD           H,A
677C: 8A         ADC         A,D
677D: 67         LD           H,A
677E: 17         RLA
677F: 4B         LD           C,E
6780: 00         NOP
6781: 00         NOP
6782: 09         ADD         HL,BC
6783: 6E         LD           L,(HL)
6784: D6 5D      SUB         $5D
6786: FF         RST         0X38
6787: FF         RST         0X38
6788: 82         ADD         A,D
6789: 67         LD           H,A
678A: 13         INC         DE
678B: 6E         LD           L,(HL)
678C: 9A         SBC         D
678D: 6E         LD           L,(HL)
678E: FF         RST         0X38
678F: FF         RST         0X38
6790: 92         SUB         D
6791: 67         LD           H,A
6792: 20 5E      JR           NZ,$67F2
6794: 4D         LD           C,L
6795: 5E         LD           E,(HL)
6796: 5F         LD           E,A
6797: 5E         LD           E,(HL)
6798: FF         RST         0X38
6799: FF         RST         0X38
679A: 92         SUB         D
679B: 67         LD           H,A
679C: 00         NOP
679D: D4 4A A7   CALL       NC,$A74A
67A0: 67         LD           H,A
67A1: FD                              
67A2: 67         LD           H,A
67A3: D3                              
67A4: 67         LD           H,A
67A5: 00         NOP
67A6: 00         NOP
67A7: 10 6D      STOP       $6D
67A9: 78         LD           A,B
67AA: 6D         LD           L,L
67AB: DB                              
67AC: 68         LD           L,B
67AD: DB                              
67AE: 68         LD           L,B
67AF: DB                              
67B0: 68         LD           L,B
67B1: DB                              
67B2: 68         LD           L,B
67B3: DB                              
67B4: 68         LD           L,B
67B5: DB                              
67B6: 68         LD           L,B
67B7: 78         LD           A,B
67B8: 6D         LD           L,L
67B9: DB                              
67BA: 68         LD           L,B
67BB: DB                              
67BC: 68         LD           L,B
67BD: 7D         LD           A,L
67BE: 6D         LD           L,L
67BF: 97         SUB         A
67C0: 68         LD           L,B
67C1: 78         LD           A,B
67C2: 6D         LD           L,L
67C3: DB                              
67C4: 68         LD           L,B
67C5: C4 68 20   CALL       NZ,$2068
67C8: 6D         LD           L,L
67C9: 20 6D      JR           NZ,$6838
67CB: 20 6D      JR           NZ,$683A
67CD: 20 6D      JR           NZ,$683C
67CF: FF         RST         0X38
67D0: FF         RST         0X38
67D1: A9         XOR         C
67D2: 67         LD           H,A
67D3: 73         LD           (HL),E
67D4: 69         LD           L,C
67D5: 68         LD           L,B
67D6: 6E         LD           L,(HL)
67D7: 56         LD           D,(HL)
67D8: 68         LD           L,B
67D9: 6D         LD           L,L
67DA: 6E         LD           L,(HL)
67DB: 56         LD           D,(HL)
67DC: 68         LD           L,B
67DD: 68         LD           L,B
67DE: 6E         LD           L,(HL)
67DF: 25         DEC         H
67E0: 68         LD           L,B
67E1: 77         LD           (HL),A
67E2: 6E         LD           L,(HL)
67E3: 25         DEC         H
67E4: 68         LD           L,B
67E5: 68         LD           L,B
67E6: 6E         LD           L,(HL)
67E7: 39         ADD         HL,SP
67E8: 68         LD           L,B
67E9: 6D         LD           L,L
67EA: 6E         LD           L,(HL)
67EB: 66         LD           H,(HL)
67EC: 68         LD           L,B
67ED: 68         LD           L,B
67EE: 6E         LD           L,(HL)
67EF: 73         LD           (HL),E
67F0: 68         LD           L,B
67F1: 6D         LD           L,L
67F2: 6E         LD           L,(HL)
67F3: 7F         LD           A,A
67F4: 68         LD           L,B
67F5: 77         LD           (HL),A
67F6: 6E         LD           L,(HL)
67F7: 8B         ADC         A,E
67F8: 68         LD           L,B
67F9: FF         RST         0X38
67FA: FF         RST         0X38
67FB: D3                              
67FC: 67         LD           H,A
67FD: 09         ADD         HL,BC
67FE: 6E         LD           L,(HL)
67FF: FC                              
6800: 68         LD           L,B
6801: FC                              
6802: 68         LD           L,B
6803: FC                              
6804: 68         LD           L,B
6805: FC                              
6806: 68         LD           L,B
6807: FC                              
6808: 68         LD           L,B
6809: FC                              
680A: 68         LD           L,B
680B: 09         ADD         HL,BC
680C: 6E         LD           L,(HL)
680D: FC                              
680E: 68         LD           L,B
680F: FC                              
6810: 68         LD           L,B
6811: 97         SUB         A
6812: 68         LD           L,B
6813: FC                              
6814: 68         LD           L,B
6815: 0E 6E      LD           C,$6E
6817: C4 68 09   CALL       NZ,$0968
681A: 6E         LD           L,(HL)
681B: 35         DEC         (HL)
681C: 69         LD           L,C
681D: 78         LD           A,B
681E: 6D         LD           L,L
681F: 65         LD           H,L
6820: 69         LD           L,C
6821: FF         RST         0X38
6822: FF         RST         0X38
6823: FD                              
6824: 67         LD           H,A
6825: A3         AND         E
6826: 50         LD           D,B
6827: 64         LD           H,H
6828: 62         LD           H,D
6829: 6E         LD           L,(HL)
682A: A4         AND         H
682B: 01 A2 01   LD           BC,$01A2
682E: 64         LD           H,H
682F: 62         LD           H,D
6830: 50         LD           D,B
6831: A3         AND         E
6832: 4E         LD           C,(HL)
6833: 60         LD           H,B
6834: 5E         LD           E,(HL)
6835: 6C         LD           L,H
6836: A5         AND         L
6837: 01 00 A3   LD           BC,$A300
683A: 4C         LD           C,H
683B: 5C         LD           E,H
683C: 5A         LD           E,D
683D: 6A         LD           L,D
683E: A5         AND         L
683F: 01 A3 4A   LD           BC,$4AA3
6842: 5A         LD           E,D
6843: 58         LD           E,B
6844: 68         LD           L,B
6845: A5         AND         L
6846: 01 A3 48   LD           BC,$48A3
6849: 58         LD           E,B
684A: 56         LD           D,(HL)
684B: 66         LD           H,(HL)
684C: A5         AND         L
684D: 01 A3 4A   LD           BC,$4AA3
6850: 5A         LD           E,D
6851: 58         LD           E,B
6852: 68         LD           L,B
6853: A5         AND         L
6854: 01 00 99   LD           BC,$9900
6857: A3         AND         E
6858: 4C         LD           C,H
6859: 5C         LD           E,H
685A: 5A         LD           E,D
685B: 6A         LD           L,D
685C: A5         AND         L
685D: 01 A3 4A   LD           BC,$4AA3
6860: 5A         LD           E,D
6861: 58         LD           E,B
6862: 68         LD           L,B
6863: A5         AND         L
6864: 01 00 9A   LD           BC,$9A00
6867: A2         AND         D
6868: 30 34      JR           NC,$689E
686A: 36 44      LD           (HL),$44
686C: 48         LD           C,B
686D: 4C         LD           C,H
686E: 4E         LD           C,(HL)
686F: 5C         LD           E,H
6870: A5         AND         L
6871: 01 00 A2   LD           BC,$A200
6874: 30 34      JR           NC,$68AA
6876: 36 42      LD           (HL),$42
6878: 48         LD           C,B
6879: 4C         LD           C,H
687A: 4E         LD           C,(HL)
687B: 5A         LD           E,D
687C: A5         AND         L
687D: 01 00 A2   LD           BC,$A200
6880: 34         INC         (HL)
6881: 38 3A      JR           C,$68BD
6883: 48         LD           C,B
6884: 4C         LD           C,H
6885: 50         LD           D,B
6886: 52         LD           D,D
6887: 60         LD           H,B
6888: A5         AND         L
6889: 01 00 A2   LD           BC,$A200
688C: 34         INC         (HL)
688D: 38 3A      JR           C,$68C9
688F: 46         LD           B,(HL)
6890: 4C         LD           C,H
6891: 50         LD           D,B
6892: 52         LD           D,D
6893: 5E         LD           E,(HL)
6894: A5         AND         L
6895: 01 00 9B   LD           BC,$9B00
6898: 02         LD           (BC),A
6899: A2         AND         D
689A: 01 38 3C   LD           BC,$3C38
689D: 38 3C      JR           C,$68DB
689F: A7         AND         A
68A0: 01 9C 9B   LD           BC,$9B9C
68A3: 02         LD           (BC),A
68A4: A2         AND         D
68A5: 01 36 3C   LD           BC,$3C36
68A8: 36 3C      LD           (HL),$3C
68AA: A7         AND         A
68AB: 01 9C 9B   LD           BC,$9B9C
68AE: 02         LD           (BC),A
68AF: A2         AND         D
68B0: 01 38 3C   LD           BC,$3C38
68B3: 3E 46      LD           A,$46
68B5: A7         AND         A
68B6: 01 9C 9B   LD           BC,$9B9C
68B9: 02         LD           (BC),A
68BA: A2         AND         D
68BB: 01 36 3C   LD           BC,$3C36
68BE: 3E 4E      LD           A,$4E
68C0: A7         AND         A
68C1: 01 9C 00   LD           BC,$009C
68C4: 9B         SBC         E
68C5: 02         LD           (BC),A
68C6: 3E 36      LD           A,$36
68C8: 3E 40      LD           A,$40
68CA: 46         LD           B,(HL)
68CB: 48         LD           C,B
68CC: 46         LD           B,(HL)
68CD: 44         LD           B,H
68CE: 9C         SBC         H
68CF: 9B         SBC         E
68D0: 02         LD           (BC),A
68D1: 32         LD           (HLD),A
68D2: 38 40      JR           C,$6914
68D4: 42         LD           B,D
68D5: 48         LD           C,B
68D6: 4A         LD           C,D
68D7: 48         LD           C,B
68D8: 42         LD           B,D
68D9: 9C         SBC         H
68DA: 00         NOP
68DB: A2         AND         D
68DC: 44         LD           B,H
68DD: 4C         LD           C,H
68DE: 4A         LD           C,D
68DF: 4C         LD           C,H
68E0: 9D         SBC         L
68E1: 20 00      JR           NZ,$68E3
68E3: 80         ADD         A,B
68E4: 9B         SBC         E
68E5: 03         INC         BC
68E6: A2         AND         D
68E7: 44         LD           B,H
68E8: 4C         LD           C,H
68E9: 4A         LD           C,D
68EA: 4C         LD           C,H
68EB: 9C         SBC         H
68EC: 9B         SBC         E
68ED: 03         INC         BC
68EE: 42         LD           B,D
68EF: 48         LD           C,B
68F0: 4A         LD           C,D
68F1: 48         LD           C,B
68F2: 9C         SBC         H
68F3: 9D         SBC         L
68F4: 10 00      STOP       $00
68F6: 80         ADD         A,B
68F7: 42         LD           B,D
68F8: 48         LD           C,B
68F9: 4A         LD           C,D
68FA: 48         LD           C,B
68FB: 00         NOP
68FC: A2         AND         D
68FD: 44         LD           B,H
68FE: 4C         LD           C,H
68FF: 4A         LD           C,D
6900: 4C         LD           C,H
6901: 9D         SBC         L
6902: 37         SCF
6903: 00         NOP
6904: 80         ADD         A,B
6905: 44         LD           B,H
6906: 4C         LD           C,H
6907: 4A         LD           C,D
6908: 4C         LD           C,H
6909: 9D         SBC         L
690A: 53         LD           D,E
690B: 00         NOP
690C: 80         ADD         A,B
690D: 44         LD           B,H
690E: 4C         LD           C,H
690F: 4A         LD           C,D
6910: 4C         LD           C,H
6911: 9D         SBC         L
6912: 64         LD           H,H
6913: 00         NOP
6914: 80         ADD         A,B
6915: 44         LD           B,H
6916: 4C         LD           C,H
6917: 4A         LD           C,D
6918: 4C         LD           C,H
6919: 9D         SBC         L
691A: 53         LD           D,E
691B: 00         NOP
691C: 80         ADD         A,B
691D: 42         LD           B,D
691E: 48         LD           C,B
691F: 4A         LD           C,D
6920: 48         LD           C,B
6921: 9D         SBC         L
6922: 37         SCF
6923: 00         NOP
6924: 80         ADD         A,B
6925: 42         LD           B,D
6926: 48         LD           C,B
6927: 4A         LD           C,D
6928: 48         LD           C,B
6929: 9D         SBC         L
692A: 27         DAA
692B: 00         NOP
692C: 80         ADD         A,B
692D: 9B         SBC         E
692E: 02         LD           (BC),A
692F: 42         LD           B,D
6930: 48         LD           C,B
6931: 4A         LD           C,D
6932: 48         LD           C,B
6933: 9C         SBC         H
6934: 00         NOP
6935: A2         AND         D
6936: 01 30 34   LD           BC,$3430
6939: 36 44      LD           (HL),$44
693B: 48         LD           C,B
693C: 4C         LD           C,H
693D: 4E         LD           C,(HL)
693E: 60         LD           H,B
693F: 64         LD           H,H
6940: 66         LD           H,(HL)
6941: 74         LD           (HL),H
6942: A4         AND         H
6943: 01 A2 01   LD           BC,$01A2
6946: 30 34      JR           NC,$697C
6948: 36 42      LD           (HL),$42
694A: 48         LD           C,B
694B: 4C         LD           C,H
694C: 4E         LD           C,(HL)
694D: 60         LD           H,B
694E: 64         LD           H,H
694F: 66         LD           H,(HL)
6950: 72         LD           (HL),D
6951: A4         AND         H
6952: 01 A2 01   LD           BC,$01A2
6955: 34         INC         (HL)
6956: 38 3A      JR           C,$6992
6958: 48         LD           C,B
6959: 4C         LD           C,H
695A: 50         LD           D,B
695B: 52         LD           D,D
695C: 64         LD           H,H
695D: 68         LD           L,B
695E: 6A         LD           L,D
695F: 78         LD           A,B
6960: A4         AND         H
6961: 01 A2 01   LD           BC,$01A2
6964: 00         NOP
6965: 34         INC         (HL)
6966: 38 3A      JR           C,$69A2
6968: 46         LD           B,(HL)
6969: 4C         LD           C,H
696A: 50         LD           D,B
696B: 52         LD           D,D
696C: 64         LD           H,H
696D: 68         LD           L,B
696E: 6A         LD           L,D
696F: 76         HALT
6970: A4         AND         H
6971: 01 00 9B   LD           BC,$9B00
6974: 18 A5      JR           $691B
6976: 01 9C 00   LD           BC,$009C
6979: 00         NOP
697A: D4 4A 84   CALL       NC,$844A
697D: 69         LD           L,C
697E: 8E         ADC         A,(HL)
697F: 69         LD           L,C
6980: 98         SBC         B
6981: 69         LD           L,C
6982: 00         NOP
6983: 00         NOP
6984: FF         RST         0X38
6985: 6D         LD           L,L
6986: A2         AND         D
6987: 69         LD           L,C
6988: 4A         LD           C,D
6989: 6E         LD           L,(HL)
698A: B4         OR           H
698B: 69         LD           L,C
698C: 00         NOP
698D: 00         NOP
698E: FF         RST         0X38
698F: 6D         LD           L,L
6990: B7         OR           A
6991: 69         LD           L,C
6992: 4A         LD           C,D
6993: 6E         LD           L,(HL)
6994: C9         RET
6995: 69         LD           L,C
6996: 00         NOP
6997: 00         NOP
6998: 54         LD           D,H
6999: 6E         LD           L,(HL)
699A: CC 69 59   CALL       Z,$5969
699D: 6E         LD           L,(HL)
699E: DA 69 00   JP           C,$0069
69A1: 00         NOP
69A2: A1         AND         C
69A3: 01 A4 01   LD           BC,$01A4
69A6: A3         AND         E
69A7: 1C         INC         E
69A8: 20 A8      JR           NZ,$6952
69AA: 22         LD           (HLI),A
69AB: A3         AND         E
69AC: 01 22 26   LD           BC,$2622
69AF: A7         AND         A
69B0: 2A         LD           A,(HLI)
69B1: A2         AND         D
69B2: 2E 00      LD           L,$00
69B4: AE         XOR         (HL)
69B5: 1A         LD           A,(DE)
69B6: 00         NOP
69B7: A1         AND         C
69B8: 01 A4 01   LD           BC,$01A4
69BB: A3         AND         E
69BC: 2E 30      LD           L,$30
69BE: A8         XOR         B
69BF: 34         INC         (HL)
69C0: A3         AND         E
69C1: 01 34 38   LD           BC,$3834
69C4: A7         AND         A
69C5: 3A         LD           A,(HLD)
69C6: A2         AND         D
69C7: 3E 00      LD           A,$00
69C9: AE         XOR         (HL)
69CA: 42         LD           B,D
69CB: 00         NOP
69CC: 9B         SBC         E
69CD: 02         LD           (BC),A
69CE: 99         SBC         C
69CF: A1         AND         C
69D0: 0E 9A      LD           C,$9A
69D2: A5         AND         L
69D3: 0E A3      LD           C,$A3
69D5: 0E A6      LD           C,$A6
69D7: 01 9C 00   LD           BC,$009C
69DA: A1         AND         C
69DB: 01 AE 14   LD           BC,$14AE
69DE: 00         NOP
69DF: 00         NOP
69E0: E3                              
69E1: 4A         LD           C,D
69E2: EA 69 F4   LD           ($F469),A
69E5: 69         LD           L,C
69E6: FE 69      CP           $69
69E8: 00         NOP
69E9: 00         NOP
69EA: 7D         LD           A,L
69EB: 6D         LD           L,L
69EC: 10 6D      STOP       $6D
69EE: 08 6A FF   LD           ($FF6A),SP
69F1: FF         RST         0X38
69F2: F8 69      LDHL       SP,$69
69F4: 87         ADD         A,A
69F5: 6D         LD           L,L
69F6: 08 6A 12   LD           ($126A),SP
69F9: 6A         LD           L,D
69FA: FF         RST         0X38
69FB: FF         RST         0X38
69FC: 30 6D      JR           NC,$6A6B
69FE: 18 6D      JR           $6A6D
6A00: 77         LD           (HL),A
6A01: 6E         LD           L,(HL)
6A02: 1C         INC         E
6A03: 6A         LD           L,D
6A04: FF         RST         0X38
6A05: FF         RST         0X38
6A06: 30 6D      JR           NC,$6A75
6A08: A1         AND         C
6A09: 80         ADD         A,B
6A0A: 78         LD           A,B
6A0B: 72         LD           (HL),D
6A0C: 6A         LD           L,D
6A0D: 68         LD           L,B
6A0E: 60         LD           H,B
6A0F: 5A         LD           E,D
6A10: 50         LD           D,B
6A11: 00         NOP
6A12: A1         AND         C
6A13: 54         LD           D,H
6A14: 5C         LD           E,H
6A15: 62         LD           H,D
6A16: 6A         LD           L,D
6A17: 6C         LD           L,H
6A18: 74         LD           (HL),H
6A19: 7A         LD           A,D
6A1A: 82         ADD         A,D
6A1B: 00         NOP
6A1C: 99         SBC         C
6A1D: A2         AND         D
6A1E: 54         LD           D,H
6A1F: 54         LD           D,H
6A20: 00         NOP
6A21: 00         NOP
6A22: D4 4A 54   CALL       NC,$544A
6A25: 6A         LD           L,D
6A26: 2C         INC         L
6A27: 6A         LD           L,D
6A28: 7C         LD           A,H
6A29: 6A         LD           L,D
6A2A: 00         NOP
6A2B: 00         NOP
6A2C: A0         AND         B
6A2D: 6D         LD           L,L
6A2E: 9B         SBC         E
6A2F: 6A         LD           L,D
6A30: A5         AND         L
6A31: 6A         LD           L,D
6A32: B0         OR           B
6A33: 6E         LD           L,(HL)
6A34: 96         SUB         (HL)
6A35: 6D         LD           L,L
6A36: A8         XOR         B
6A37: 6A         LD           L,D
6A38: 10 6D      STOP       $6D
6A3A: 7D         LD           A,L
6A3B: 6D         LD           L,L
6A3C: 08 6A 24   LD           ($246A),SP
6A3F: 6D         LD           L,L
6A40: 2D         DEC         L
6A41: 6D         LD           L,L
6A42: 96         SUB         (HL)
6A43: 6A         LD           L,D
6A44: 78         LD           A,B
6A45: 6B         LD           L,E
6A46: A0         AND         B
6A47: 6D         LD           L,L
6A48: 28 6B      JR           Z,$6AB5
6A4A: 09         ADD         HL,BC
6A4B: 6E         LD           L,(HL)
6A4C: 40         LD           B,B
6A4D: 6B         LD           L,E
6A4E: 27         DAA
6A4F: 6D         LD           L,L
6A50: FF         RST         0X38
6A51: FF         RST         0X38
6A52: 32         LD           (HLD),A
6A53: 6A         LD           L,D
6A54: 7D         LD           A,L
6A55: 6D         LD           L,L
6A56: 10 6D      STOP       $6D
6A58: 9B         SBC         E
6A59: 6A         LD           L,D
6A5A: 2D         DEC         L
6A5B: 6D         LD           L,L
6A5C: B0         OR           B
6A5D: 6E         LD           L,(HL)
6A5E: 22         LD           (HLI),A
6A5F: 6B         LD           L,E
6A60: 87         ADD         A,A
6A61: 6D         LD           L,L
6A62: 08 6A 20   LD           ($206A),SP
6A65: 6D         LD           L,L
6A66: 20 6D      JR           NZ,$6AD5
6A68: 20 6D      JR           NZ,$6AD7
6A6A: 20 6D      JR           NZ,$6AD9
6A6C: 10 6D      STOP       $6D
6A6E: 7D         LD           A,L
6A6F: 6D         LD           L,L
6A70: 28 6B      JR           Z,$6ADD
6A72: 27         DAA
6A73: 6D         LD           L,L
6A74: 2D         DEC         L
6A75: 6D         LD           L,L
6A76: 10 6D      STOP       $6D
6A78: FF         RST         0X38
6A79: FF         RST         0X38
6A7A: 5C         LD           E,H
6A7B: 6A         LD           L,D
6A7C: 18 6D      JR           $6AEB
6A7E: 24         INC         H
6A7F: 6D         LD           L,L
6A80: 6D         LD           L,L
6A81: 6E         LD           L,(HL)
6A82: B0         OR           B
6A83: 6E         LD           L,(HL)
6A84: 10 6D      STOP       $6D
6A86: 67         LD           H,A
6A87: 5D         LD           E,L
6A88: 46         LD           B,(HL)
6A89: 6B         LD           L,E
6A8A: 15         DEC         D
6A8B: 6D         LD           L,L
6A8C: 2D         DEC         L
6A8D: 6D         LD           L,L
6A8E: 18 6D      JR           $6AFD
6A90: 24         INC         H
6A91: 6D         LD           L,L
6A92: FF         RST         0X38
6A93: FF         RST         0X38
6A94: 80         ADD         A,B
6A95: 6A         LD           L,D
6A96: 9D         SBC         L
6A97: C2 83 C0   JP           NZ,$C083
6A9A: 00         NOP
6A9B: A1         AND         C
6A9C: 44         LD           B,H
6A9D: 48         LD           C,B
6A9E: 4C         LD           C,H
6A9F: 50         LD           D,B
6AA0: 56         LD           D,(HL)
6AA1: 5C         LD           E,H
6AA2: 60         LD           H,B
6AA3: 64         LD           H,H
6AA4: 00         NOP
6AA5: 68         LD           L,B
6AA6: 6E         LD           L,(HL)
6AA7: 00         NOP
6AA8: 9D         SBC         L
6AA9: B1         OR           C
6AAA: 83         ADD         A,E
6AAB: 80         ADD         A,B
6AAC: A6         AND         (HL)
6AAD: 01 64 68   LD           BC,$6864
6AB0: 6A         LD           L,D
6AB1: 9D         SBC         L
6AB2: 81         ADD         A,C
6AB3: 83         ADD         A,E
6AB4: 80         ADD         A,B
6AB5: A2         AND         D
6AB6: 3E 42      LD           A,$42
6AB8: 44         LD           B,H
6AB9: 4C         LD           C,H
6ABA: 52         LD           D,D
6ABB: A1         AND         C
6ABC: 01 9D B1   LD           BC,$B19D
6ABF: 83         ADD         A,E
6AC0: 80         ADD         A,B
6AC1: A6         AND         (HL)
6AC2: 64         LD           H,H
6AC3: 68         LD           L,B
6AC4: 6A         LD           L,D
6AC5: 9D         SBC         L
6AC6: 81         ADD         A,C
6AC7: 83         ADD         A,E
6AC8: 80         ADD         A,B
6AC9: A2         AND         D
6ACA: 30 3E      JR           NC,$6B0A
6ACC: 44         LD           B,H
6ACD: 4C         LD           C,H
6ACE: 50         LD           D,B
6ACF: 9D         SBC         L
6AD0: B1         OR           C
6AD1: 83         ADD         A,E
6AD2: 80         ADD         A,B
6AD3: 68         LD           L,B
6AD4: 64         LD           H,H
6AD5: 5A         LD           E,D
6AD6: 60         LD           H,B
6AD7: 9D         SBC         L
6AD8: 81         ADD         A,C
6AD9: 83         ADD         A,E
6ADA: 80         ADD         A,B
6ADB: 3A         LD           A,(HLD)
6ADC: 42         LD           B,D
6ADD: 64         LD           H,H
6ADE: 50         LD           D,B
6ADF: A7         AND         A
6AE0: 01 A2 34   LD           BC,$34A2
6AE3: 3C         INC         A
6AE4: 42         LD           B,D
6AE5: 48         LD           C,B
6AE6: 4C         LD           C,H
6AE7: 9D         SBC         L
6AE8: B1         OR           C
6AE9: 83         ADD         A,E
6AEA: 80         ADD         A,B
6AEB: 64         LD           H,H
6AEC: 68         LD           L,B
6AED: 6A         LD           L,D
6AEE: 9D         SBC         L
6AEF: 81         ADD         A,C
6AF0: 83         ADD         A,E
6AF1: 80         ADD         A,B
6AF2: A2         AND         D
6AF3: 3E 42      LD           A,$42
6AF5: 44         LD           B,H
6AF6: 4C         LD           C,H
6AF7: 52         LD           D,D
6AF8: 9D         SBC         L
6AF9: B1         OR           C
6AFA: 83         ADD         A,E
6AFB: 80         ADD         A,B
6AFC: 60         LD           H,B
6AFD: 6A         LD           L,D
6AFE: 74         LD           (HL),H
6AFF: 9D         SBC         L
6B00: 81         ADD         A,C
6B01: 83         ADD         A,E
6B02: 80         ADD         A,B
6B03: A2         AND         D
6B04: 30 3E      JR           NC,$6B44
6B06: 44         LD           B,H
6B07: 4C         LD           C,H
6B08: 56         LD           D,(HL)
6B09: 9D         SBC         L
6B0A: B1         OR           C
6B0B: 83         ADD         A,E
6B0C: 80         ADD         A,B
6B0D: 72         LD           (HL),D
6B0E: 6E         LD           L,(HL)
6B0F: 72         LD           (HL),D
6B10: 9D         SBC         L
6B11: 81         ADD         A,C
6B12: 83         ADD         A,E
6B13: 80         ADD         A,B
6B14: A2         AND         D
6B15: 3A         LD           A,(HLD)
6B16: 42         LD           B,D
6B17: 48         LD           C,B
6B18: 50         LD           D,B
6B19: 52         LD           D,D
6B1A: 5A         LD           E,D
6B1B: 60         LD           H,B
6B1C: 68         LD           L,B
6B1D: 78         LD           A,B
6B1E: 01 90 01   LD           BC,$0190
6B21: 00         NOP
6B22: 9B         SBC         E
6B23: 11 A4 01   LD           DE,$01A4
6B26: 9C         SBC         H
6B27: 00         NOP
6B28: A1         AND         C
6B29: 1C         INC         E
6B2A: 22         LD           (HLI),A
6B2B: 2A         LD           A,(HLI)
6B2C: 30 38      JR           NC,$6B66
6B2E: 3A         LD           A,(HLD)
6B2F: 42         LD           B,D
6B30: 48         LD           C,B
6B31: 50         LD           D,B
6B32: 48         LD           C,B
6B33: 42         LD           B,D
6B34: 3A         LD           A,(HLD)
6B35: 38 30      JR           C,$6B67
6B37: 2A         LD           A,(HLI)
6B38: 22         LD           (HLI),A
6B39: 18 26      JR           $6B61
6B3B: 2C         INC         L
6B3C: 34         INC         (HL)
6B3D: 3E 44      LD           A,$44
6B3F: 00         NOP
6B40: 4C         LD           C,H
6B41: 56         LD           D,(HL)
6B42: 60         LD           H,B
6B43: A9         XOR         C
6B44: 01 00 A9   LD           BC,$A900
6B47: 01 A3 01   LD           BC,$01A3
6B4A: A3         AND         E
6B4B: 80         ADD         A,B
6B4C: 7C         LD           A,H
6B4D: 72         LD           (HL),D
6B4E: A7         AND         A
6B4F: 72         LD           (HL),D
6B50: A4         AND         H
6B51: 74         LD           (HL),H
6B52: A7         AND         A
6B53: 01 A3 86   LD           BC,$86A3
6B56: 82         ADD         A,D
6B57: 72         LD           (HL),D
6B58: A7         AND         A
6B59: 72         LD           (HL),D
6B5A: A3         AND         E
6B5B: 74         LD           (HL),H
6B5C: A2         AND         D
6B5D: 01 A3 74   LD           BC,$74A3
6B60: A3         AND         E
6B61: 78         LD           A,B
6B62: 01 A2 66   LD           BC,$66A2
6B65: 6C         LD           L,H
6B66: 78         LD           A,B
6B67: A4         AND         H
6B68: 72         LD           (HL),D
6B69: A7         AND         A
6B6A: 01 A2 6A   LD           BC,$6AA2
6B6D: A4         AND         H
6B6E: 7C         LD           A,H
6B6F: 01 A2 01   LD           BC,$01A2
6B72: A7         AND         A
6B73: 7A         LD           A,D
6B74: 8C         ADC         A,H
6B75: A3         AND         E
6B76: 8A         ADC         A,D
6B77: 00         NOP
6B78: 9D         SBC         L
6B79: C2 83 C0   JP           NZ,$C083
6B7C: A3         AND         E
6B7D: 80         ADD         A,B
6B7E: 7C         LD           A,H
6B7F: 72         LD           (HL),D
6B80: A2         AND         D
6B81: 72         LD           (HL),D
6B82: 9D         SBC         L
6B83: 72         LD           (HL),D
6B84: 00         NOP
6B85: 80         ADD         A,B
6B86: 26 34      LD           H,$34
6B88: 9D         SBC         L
6B89: C2 83 C0   JP           NZ,$C083
6B8C: 74         LD           (HL),H
6B8D: 9D         SBC         L
6B8E: 72         LD           (HL),D
6B8F: 00         NOP
6B90: 80         ADD         A,B
6B91: A1         AND         C
6B92: 3E 42      LD           A,$42
6B94: 44         LD           B,H
6B95: 4C         LD           C,H
6B96: 56         LD           D,(HL)
6B97: 5A         LD           E,D
6B98: 5C         LD           E,H
6B99: 6A         LD           L,D
6B9A: 34         INC         (HL)
6B9B: 42         LD           B,D
6B9C: 50         LD           D,B
6B9D: 60         LD           H,B
6B9E: 9D         SBC         L
6B9F: C2 83 C0   JP           NZ,$C083
6BA2: A3         AND         E
6BA3: 86         ADD         A,(HL)
6BA4: 82         ADD         A,D
6BA5: 72         LD           (HL),D
6BA6: A2         AND         D
6BA7: 72         LD           (HL),D
6BA8: 9D         SBC         L
6BA9: 72         LD           (HL),D
6BAA: 00         NOP
6BAB: 80         ADD         A,B
6BAC: 3E 4C      LD           A,$4C
6BAE: 9D         SBC         L
6BAF: C2 83 C0   JP           NZ,$C083
6BB2: 74         LD           (HL),H
6BB3: 9D         SBC         L
6BB4: 72         LD           (HL),D
6BB5: 00         NOP
6BB6: 80         ADD         A,B
6BB7: A1         AND         C
6BB8: 56         LD           D,(HL)
6BB9: 5A         LD           E,D
6BBA: 5C         LD           E,H
6BBB: 64         LD           H,H
6BBC: 9D         SBC         L
6BBD: C2 83 C0   JP           NZ,$C083
6BC0: A3         AND         E
6BC1: 74         LD           (HL),H
6BC2: 78         LD           A,B
6BC3: 9D         SBC         L
6BC4: 72         LD           (HL),D
6BC5: 00         NOP
6BC6: 80         ADD         A,B
6BC7: A1         AND         C
6BC8: 4E         LD           C,(HL)
6BC9: 54         LD           D,H
6BCA: 5A         LD           E,D
6BCB: 60         LD           H,B
6BCC: 9D         SBC         L
6BCD: C2 83 C0   JP           NZ,$C083
6BD0: A2         AND         D
6BD1: 66         LD           H,(HL)
6BD2: 6C         LD           L,H
6BD3: 78         LD           A,B
6BD4: 72         LD           (HL),D
6BD5: 9D         SBC         L
6BD6: 72         LD           (HL),D
6BD7: 00         NOP
6BD8: 80         ADD         A,B
6BD9: A1         AND         C
6BDA: 01 52 5A   LD           BC,$5A52
6BDD: 60         LD           H,B
6BDE: 6A         LD           L,D
6BDF: 72         LD           (HL),D
6BE0: 78         LD           A,B
6BE1: 7E         LD           A,(HL)
6BE2: A3         AND         E
6BE3: 82         ADD         A,D
6BE4: 9D         SBC         L
6BE5: C2 83 C0   JP           NZ,$C083
6BE8: A2         AND         D
6BE9: 6A         LD           L,D
6BEA: 7C         LD           A,H
6BEB: 9D         SBC         L
6BEC: 72         LD           (HL),D
6BED: 00         NOP
6BEE: 80         ADD         A,B
6BEF: A1         AND         C
6BF0: 2C         INC         L
6BF1: 34         INC         (HL)
6BF2: 3A         LD           A,(HLD)
6BF3: 42         LD           B,D
6BF4: 44         LD           B,H
6BF5: 4C         LD           C,H
6BF6: 52         LD           D,D
6BF7: 5A         LD           E,D
6BF8: 4C         LD           C,H
6BF9: 52         LD           D,D
6BFA: 5A         LD           E,D
6BFB: 5C         LD           E,H
6BFC: 52         LD           D,D
6BFD: 5A         LD           E,D
6BFE: 5C         LD           E,H
6BFF: 64         LD           H,H
6C00: 9D         SBC         L
6C01: C2 83 C0   JP           NZ,$C083
6C04: A7         AND         A
6C05: 7A         LD           A,D
6C06: 8C         ADC         A,H
6C07: A3         AND         E
6C08: 8A         ADC         A,D
6C09: 00         NOP
6C0A: C5         PUSH       BC
6C0B: 4A         LD           C,D
6C0C: 14         INC         D
6C0D: 6C         LD           L,H
6C0E: 1E 6C      LD           E,$6C
6C10: 26 6C      LD           H,$6C
6C12: 00         NOP
6C13: 00         NOP
6C14: 9B         SBC         E
6C15: 6D         LD           L,L
6C16: 40         LD           B,B
6C17: 6C         LD           L,H
6C18: 2A         LD           A,(HLI)
6C19: 6D         LD           L,L
6C1A: FF         RST         0X38
6C1B: FF         RST         0X38
6C1C: 22         LD           (HLI),A
6C1D: 6C         LD           L,H
6C1E: B9         CP           C
6C1F: 6D         LD           L,L
6C20: 2E 6C      LD           L,$6C
6C22: 38 6C      JR           C,$6C90
6C24: 00         NOP
6C25: 00         NOP
6C26: 6D         LD           L,L
6C27: 6E         LD           L,(HL)
6C28: 10 6D      STOP       $6D
6C2A: FF         RST         0X38
6C2B: FF         RST         0X38
6C2C: 20 6C      JR           NZ,$6C9A
6C2E: A1         AND         C
6C2F: 52         LD           D,D
6C30: 5A         LD           E,D
6C31: 60         LD           H,B
6C32: 68         LD           L,B
6C33: 6A         LD           L,D
6C34: 72         LD           (HL),D
6C35: 78         LD           A,B
6C36: 80         ADD         A,B
6C37: 00         NOP
6C38: A3         AND         E
6C39: 01 A1 8A   LD           BC,$8AA1
6C3C: 90         SUB         B
6C3D: 01 01 00   LD           BC,$0001
6C40: 9B         SBC         E
6C41: 02         LD           (BC),A
6C42: A1         AND         C
6C43: 3A         LD           A,(HLD)
6C44: 42         LD           B,D
6C45: 48         LD           C,B
6C46: 42         LD           B,D
6C47: 9C         SBC         H
6C48: 00         NOP
6C49: 00         NOP
6C4A: B6         OR           (HL)
6C4B: 4A         LD           C,D
6C4C: 54         LD           D,H
6C4D: 6C         LD           L,H
6C4E: 66         LD           H,(HL)
6C4F: 6C         LD           L,H
6C50: 17         RLA
6C51: 4B         LD           C,E
6C52: 00         NOP
6C53: 00         NOP
6C54: E1         POP         HL
6C55: 6D         LD           L,L
6C56: 03         INC         BC
6C57: 6D         LD           L,L
6C58: F0 6D      LD           A,($6D)
6C5A: 03         INC         BC
6C5B: 6D         LD           L,L
6C5C: 03         INC         BC
6C5D: 6D         LD           L,L
6C5E: E1         POP         HL
6C5F: 6D         LD           L,L
6C60: 03         INC         BC
6C61: 6D         LD           L,L
6C62: FF         RST         0X38
6C63: FF         RST         0X38
6C64: 54         LD           D,H
6C65: 6C         LD           L,H
6C66: 9B         SBC         E
6C67: 6D         LD           L,L
6C68: E9         JP           (HL)
6C69: 6C         LD           L,H
6C6A: 8C         ADC         A,H
6C6B: 6D         LD           L,L
6C6C: 9D         SBC         L
6C6D: 6E         LD           L,(HL)
6C6E: E9         JP           (HL)
6C6F: 6C         LD           L,H
6C70: 94         SUB         H
6C71: 6E         LD           L,(HL)
6C72: E9         JP           (HL)
6C73: 6C         LD           L,H
6C74: 9B         SBC         E
6C75: 6D         LD           L,L
6C76: 97         SUB         A
6C77: 6E         LD           L,(HL)
6C78: E9         JP           (HL)
6C79: 6C         LD           L,H
6C7A: 7C         LD           A,H
6C7B: 6E         LD           L,(HL)
6C7C: FF         RST         0X38
6C7D: FF         RST         0X38
6C7E: 66         LD           H,(HL)
6C7F: 6C         LD           L,H
6C80: 00         NOP
6C81: B6         OR           (HL)
6C82: 4A         LD           C,D
6C83: 8B         ADC         A,E
6C84: 6C         LD           L,H
6C85: A5         AND         L
6C86: 6C         LD           L,H
6C87: D3                              
6C88: 6C         LD           L,H
6C89: E1         POP         HL
6C8A: 6C         LD           L,H
6C8B: E1         POP         HL
6C8C: 6D         LD           L,L
6C8D: 03         INC         BC
6C8E: 6D         LD           L,L
6C8F: F0 6D      LD           A,($6D)
6C91: 03         INC         BC
6C92: 6D         LD           L,L
6C93: FF         RST         0X38
6C94: 6D         LD           L,L
6C95: 03         INC         BC
6C96: 6D         LD           L,L
6C97: 03         INC         BC
6C98: 6D         LD           L,L
6C99: 03         INC         BC
6C9A: 6D         LD           L,L
6C9B: 03         INC         BC
6C9C: 6D         LD           L,L
6C9D: 03         INC         BC
6C9E: 6D         LD           L,L
6C9F: A0         AND         B
6CA0: 6E         LD           L,(HL)
6CA1: FF         RST         0X38
6CA2: FF         RST         0X38
6CA3: 47         LD           B,A
6CA4: 5F         LD           E,A
6CA5: 9B         SBC         E
6CA6: 6D         LD           L,L
6CA7: E9         JP           (HL)
6CA8: 6C         LD           L,H
6CA9: 8C         ADC         A,H
6CAA: 6D         LD           L,L
6CAB: 9D         SBC         L
6CAC: 6E         LD           L,(HL)
6CAD: E9         JP           (HL)
6CAE: 6C         LD           L,H
6CAF: EB                              
6CB0: 6D         LD           L,L
6CB1: 94         SUB         H
6CB2: 6E         LD           L,(HL)
6CB3: E9         JP           (HL)
6CB4: 6C         LD           L,H
6CB5: 97         SUB         A
6CB6: 6E         LD           L,(HL)
6CB7: E9         JP           (HL)
6CB8: 6C         LD           L,H
6CB9: 8C         ADC         A,H
6CBA: 6D         LD           L,L
6CBB: 7C         LD           A,H
6CBC: 6E         LD           L,(HL)
6CBD: F6 6C      OR           $6C
6CBF: B9         CP           C
6CC0: 6D         LD           L,L
6CC1: 9D         SBC         L
6CC2: 6E         LD           L,(HL)
6CC3: F6 6C      OR           $6C
6CC5: EB                              
6CC6: 6D         LD           L,L
6CC7: 94         SUB         H
6CC8: 6E         LD           L,(HL)
6CC9: F6 6C      OR           $6C
6CCB: 7C         LD           A,H
6CCC: 6E         LD           L,(HL)
6CCD: A0         AND         B
6CCE: 6E         LD           L,(HL)
6CCF: FF         RST         0X38
6CD0: FF         RST         0X38
6CD1: 5D         LD           E,L
6CD2: 5F         LD           E,A
6CD3: 20 6D      JR           NZ,$6D42
6CD5: 20 6D      JR           NZ,$6D44
6CD7: 20 6D      JR           NZ,$6D46
6CD9: 15         DEC         D
6CDA: 6D         LD           L,L
6CDB: A0         AND         B
6CDC: 6E         LD           L,(HL)
6CDD: FF         RST         0X38
6CDE: FF         RST         0X38
6CDF: 77         LD           (HL),A
6CE0: 5F         LD           E,A
6CE1: 0A         LD           A,(BC)
6CE2: 6D         LD           L,L
6CE3: A0         AND         B
6CE4: 6E         LD           L,(HL)
6CE5: FF         RST         0X38
6CE6: FF         RST         0X38
6CE7: 8B         ADC         A,E
6CE8: 5F         LD           E,A
6CE9: 9B         SBC         E
6CEA: 02         LD           (BC),A
6CEB: A1         AND         C
6CEC: 06 0C      LD           B,$0C
6CEE: 12         LD           (DE),A
6CEF: 1A         LD           A,(DE)
6CF0: 1E 24      LD           E,$24
6CF2: 2A         LD           A,(HLI)
6CF3: 32         LD           (HLD),A
6CF4: 9C         SBC         H
6CF5: 00         NOP
6CF6: 9B         SBC         E
6CF7: 02         LD           (BC),A
6CF8: A1         AND         C
6CF9: 1E 24      LD           E,$24
6CFB: 2A         LD           A,(HLI)
6CFC: 32         LD           (HLD),A
6CFD: 36 3C      LD           (HL),$3C
6CFF: 42         LD           B,D
6D00: 4A         LD           C,D
6D01: 9C         SBC         H
6D02: 00         NOP
6D03: 99         SBC         C
6D04: A2         AND         D
6D05: 06 06      LD           B,$06
6D07: A8         XOR         B
6D08: 01 00 9B   LD           BC,$9B00
6D0B: 07         RLCA
6D0C: A5         AND         L
6D0D: 01 9C 00   LD           BC,$009C
6D10: A1         AND         C
6D11: 01 A9 01   LD           BC,$01A9
6D14: 00         NOP
6D15: A5         AND         L
6D16: 01 00 A4   LD           BC,$A400
6D19: 01 00 A5   LD           BC,$A500
6D1C: 01 A8 01   LD           BC,$01A8
6D1F: 00         NOP
6D20: A5         AND         L
6D21: 01 01 00   LD           BC,$0001
6D24: A2         AND         D
6D25: 01 00 A6   LD           BC,$A600
6D28: 01 00 A1   LD           BC,$A100
6D2B: 01 00 A0   LD           BC,$A000
6D2E: 01 00 15   LD           BC,$1500
6D31: 6D         LD           L,L
6D32: FF         RST         0X38
6D33: FF         RST         0X38
6D34: 30 6D      JR           NC,$6DA3
6D36: 99         SBC         C
6D37: 00         NOP
6D38: FF         RST         0X38
6D39: FF         RST         0X38
6D3A: FF         RST         0X38
6D3B: FF         RST         0X38
6D3C: 00         NOP
6D3D: 00         NOP
6D3E: 00         NOP
6D3F: 00         NOP
6D40: FF         RST         0X38
6D41: FF         RST         0X38
6D42: FF         RST         0X38
6D43: FF         RST         0X38
6D44: 00         NOP
6D45: 00         NOP
6D46: 00         NOP
6D47: 00         NOP
6D48: FF         RST         0X38
6D49: FF         RST         0X38
6D4A: 00         NOP
6D4B: 00         NOP
6D4C: 00         NOP
6D4D: 00         NOP
6D4E: 00         NOP
6D4F: 00         NOP
6D50: 00         NOP
6D51: 00         NOP
6D52: 00         NOP
6D53: 00         NOP
6D54: 00         NOP
6D55: 00         NOP
6D56: 00         NOP
6D57: 00         NOP
6D58: 99         SBC         C
6D59: 99         SBC         C
6D5A: 99         SBC         C
6D5B: 99         SBC         C
6D5C: 00         NOP
6D5D: 00         NOP
6D5E: 00         NOP
6D5F: 00         NOP
6D60: 99         SBC         C
6D61: 99         SBC         C
6D62: 99         SBC         C
6D63: 99         SBC         C
6D64: 00         NOP
6D65: 00         NOP
6D66: 00         NOP
6D67: 00         NOP
6D68: 44         LD           B,H
6D69: 44         LD           B,H
6D6A: 44         LD           B,H
6D6B: 44         LD           B,H
6D6C: 00         NOP
6D6D: 00         NOP
6D6E: 00         NOP
6D6F: 00         NOP
6D70: 44         LD           B,H
6D71: 44         LD           B,H
6D72: 44         LD           B,H
6D73: 44         LD           B,H
6D74: 00         NOP
6D75: 00         NOP
6D76: 00         NOP
6D77: 00         NOP
6D78: 9D         SBC         L
6D79: 10 00      STOP       $00
6D7B: 80         ADD         A,B
6D7C: 00         NOP
6D7D: 9D         SBC         L
6D7E: 20 00      JR           NZ,$6D80
6D80: 80         ADD         A,B
6D81: 00         NOP
6D82: 9D         SBC         L
6D83: 24         INC         H
6D84: 83         ADD         A,E
6D85: C0         RET         NZ
6D86: 00         NOP
6D87: 9D         SBC         L
6D88: 46         LD           B,(HL)
6D89: 86         ADD         A,(HL)
6D8A: 80         ADD         A,B
6D8B: 00         NOP
6D8C: 9D         SBC         L
6D8D: 81         ADD         A,C
6D8E: 83         ADD         A,E
6D8F: C0         RET         NZ
6D90: 00         NOP
6D91: 9D         SBC         L
6D92: A2         AND         D
6D93: 83         ADD         A,E
6D94: C0         RET         NZ
6D95: 00         NOP
6D96: 9D         SBC         L
6D97: 91         SUB         C
6D98: 83         ADD         A,E
6D99: 80         ADD         A,B
6D9A: 00         NOP
6D9B: 9D         SBC         L
6D9C: 52         LD           D,D
6D9D: 83         ADD         A,E
6D9E: C0         RET         NZ
6D9F: 00         NOP
6DA0: 9D         SBC         L
6DA1: 62         LD           H,D
6DA2: 00         NOP
6DA3: 80         ADD         A,B
6DA4: 00         NOP
6DA5: 9D         SBC         L
6DA6: 82         ADD         A,D
6DA7: 00         NOP
6DA8: 80         ADD         A,B
6DA9: 00         NOP
6DAA: 9D         SBC         L
6DAB: 62         LD           H,D
6DAC: 00         NOP
6DAD: C0         RET         NZ
6DAE: 00         NOP
6DAF: 9D         SBC         L
6DB0: 92         SUB         D
6DB1: 00         NOP
6DB2: C0         RET         NZ
6DB3: 00         NOP
6DB4: 9D         SBC         L
6DB5: B2         OR           D
6DB6: 00         NOP
6DB7: C0         RET         NZ
6DB8: 00         NOP
6DB9: 9D         SBC         L
6DBA: C1         POP         BC
6DBB: 83         ADD         A,E
6DBC: 00         NOP
6DBD: 00         NOP
6DBE: 9D         SBC         L
6DBF: 45         LD           B,L
6DC0: 00         NOP
6DC1: 80         ADD         A,B
6DC2: 00         NOP
6DC3: 9D         SBC         L
6DC4: 53         LD           D,E
6DC5: 00         NOP
6DC6: 80         ADD         A,B
6DC7: 00         NOP
6DC8: 9D         SBC         L
6DC9: 93         SUB         E
6DCA: 00         NOP
6DCB: 00         NOP
6DCC: 00         NOP
6DCD: 9D         SBC         L
6DCE: 64         LD           H,H
6DCF: 00         NOP
6DD0: 80         ADD         A,B
6DD1: 00         NOP
6DD2: 9D         SBC         L
6DD3: 84         ADD         A,H
6DD4: 86         ADD         A,(HL)
6DD5: 80         ADD         A,B
6DD6: 00         NOP
6DD7: 9D         SBC         L
6DD8: B4         OR           H
6DD9: 86         ADD         A,(HL)
6DDA: 80         ADD         A,B
6DDB: 00         NOP
6DDC: 9D         SBC         L
6DDD: E4                              
6DDE: 86         ADD         A,(HL)
6DDF: 80         ADD         A,B
6DE0: 00         NOP
6DE1: 9D         SBC         L
6DE2: 75         LD           (HL),L
6DE3: 86         ADD         A,(HL)
6DE4: 80         ADD         A,B
6DE5: 00         NOP
6DE6: 9D         SBC         L
6DE7: A5         AND         L
6DE8: 00         NOP
6DE9: 80         ADD         A,B
6DEA: 00         NOP
6DEB: 9D         SBC         L
6DEC: F5         PUSH       AF
6DED: 86         ADD         A,(HL)
6DEE: 80         ADD         A,B
6DEF: 00         NOP
6DF0: 9D         SBC         L
6DF1: A5         AND         L
6DF2: 86         ADD         A,(HL)
6DF3: 80         ADD         A,B
6DF4: 00         NOP
6DF5: 9D         SBC         L
6DF6: A5         AND         L
6DF7: 46         LD           B,(HL)
6DF8: 80         ADD         A,B
6DF9: 00         NOP
6DFA: 9D         SBC         L
6DFB: 85         ADD         A,L
6DFC: 00         NOP
6DFD: 80         ADD         A,B
6DFE: 00         NOP
6DFF: 9D         SBC         L
6E00: E7         RST         0X20
6E01: 86         ADD         A,(HL)
6E02: 80         ADD         A,B
6E03: 00         NOP
6E04: 9D         SBC         L
6E05: 17         RLA
6E06: 00         NOP
6E07: 80         ADD         A,B
6E08: 00         NOP
6E09: 9D         SBC         L
6E0A: 27         DAA
6E0B: 00         NOP
6E0C: 80         ADD         A,B
6E0D: 00         NOP
6E0E: 9D         SBC         L
6E0F: 37         SCF
6E10: 00         NOP
6E11: 80         ADD         A,B
6E12: 00         NOP
6E13: 9D         SBC         L
6E14: 47         LD           B,A
6E15: 00         NOP
6E16: 80         ADD         A,B
6E17: 00         NOP
6E18: 9D         SBC         L
6E19: 86         ADD         A,(HL)
6E1A: 00         NOP
6E1B: C0         RET         NZ
6E1C: 00         NOP
6E1D: 9D         SBC         L
6E1E: 66         LD           H,(HL)
6E1F: 00         NOP
6E20: 80         ADD         A,B
6E21: 00         NOP
6E22: 9D         SBC         L
6E23: 87         ADD         A,A
6E24: 00         NOP
6E25: 80         ADD         A,B
6E26: 00         NOP
6E27: 9D         SBC         L
6E28: 48         LD           C,B
6E29: 00         NOP
6E2A: 80         ADD         A,B
6E2B: 00         NOP
6E2C: 9D         SBC         L
6E2D: 38 00      JR           C,$6E2F
6E2F: 81         ADD         A,C
6E30: 00         NOP
6E31: 9D         SBC         L
6E32: 48         LD           C,B
6E33: 86         ADD         A,(HL)
6E34: 80         ADD         A,B
6E35: 00         NOP
6E36: 9D         SBC         L
6E37: 48         LD           C,B
6E38: 00         NOP
6E39: 00         NOP
6E3A: 00         NOP
6E3B: 9D         SBC         L
6E3C: 58         LD           E,B
6E3D: 00         NOP
6E3E: 00         NOP
6E3F: 00         NOP
6E40: 9D         SBC         L
6E41: A8         XOR         B
6E42: 86         ADD         A,(HL)
6E43: C0         RET         NZ
6E44: 00         NOP
6E45: 9D         SBC         L
6E46: 88         ADC         A,B
6E47: 00         NOP
6E48: 00         NOP
6E49: 00         NOP
6E4A: 9D         SBC         L
6E4B: 1F         RRA
6E4C: 00         NOP
6E4D: 00         NOP
6E4E: 00         NOP
6E4F: 9D         SBC         L
6E50: 5F         LD           E,A
6E51: 00         NOP
6E52: 80         ADD         A,B
6E53: 00         NOP
6E54: 9D         SBC         L
6E55: 38 6D      JR           C,$6EC4
6E57: 20 00      JR           NZ,$6E59
6E59: 9D         SBC         L
6E5A: 48         LD           C,B
6E5B: 6D         LD           L,L
6E5C: 20 00      JR           NZ,$6E5E
6E5E: 9D         SBC         L
6E5F: 48         LD           C,B
6E60: 6D         LD           L,L
6E61: 40         LD           B,B
6E62: 00         NOP
6E63: 9D         SBC         L
6E64: 58         LD           E,B
6E65: 6D         LD           L,L
6E66: 20 00      JR           NZ,$6E68
6E68: 9D         SBC         L
6E69: 58         LD           E,B
6E6A: 6D         LD           L,L
6E6B: 40         LD           B,B
6E6C: 00         NOP
6E6D: 9D         SBC         L
6E6E: 58         LD           E,B
6E6F: 6D         LD           L,L
6E70: 60         LD           H,B
6E71: 00         NOP
6E72: 9D         SBC         L
6E73: 68         LD           L,B
6E74: 6D         LD           L,L
6E75: 40         LD           B,B
6E76: 00         NOP
6E77: 9D         SBC         L
6E78: 68         LD           L,B
6E79: 6D         LD           L,L
6E7A: 60         LD           H,B
6E7B: 00         NOP
6E7C: 9F         SBC         A
6E7D: 00         NOP
6E7E: 00         NOP
6E7F: 9F         SBC         A
6E80: 18 00      JR           $6E82
6E82: 9F         SBC         A
6E83: 16 00      LD           D,$00
6E85: 9F         SBC         A
6E86: 0E 00      LD           C,$00
6E88: 9F         SBC         A
6E89: 0C         INC         C
6E8A: 00         NOP
6E8B: 9F         SBC         A
6E8C: 0A         LD           A,(BC)
6E8D: 00         NOP
6E8E: 9F         SBC         A
6E8F: 08 00 9F   LD           ($9F00),SP
6E92: 06 00      LD           B,$00
6E94: 9F         SBC         A
6E95: 04         INC         B
6E96: 00         NOP
6E97: 9F         SBC         A
6E98: 02         LD           (BC),A
6E99: 00         NOP
6E9A: 9F         SBC         A
6E9B: D0         RET         NC
6E9C: 00         NOP
6E9D: 9F         SBC         A
6E9E: FE 00      CP           $00
6EA0: 9E         SBC         (HL)
6EA1: 98         SBC         B
6EA2: 4A         LD           C,D
6EA3: 00         NOP
6EA4: 9E         SBC         (HL)
6EA5: A7         AND         A
6EA6: 4A         LD           C,D
6EA7: 00         NOP
6EA8: 9E         SBC         (HL)
6EA9: C5         PUSH       BC
6EAA: 4A         LD           C,D
6EAB: 00         NOP
6EAC: 9E         SBC         (HL)
6EAD: D4 4A 00   CALL       NC,$004A
6EB0: 9E         SBC         (HL)
6EB1: E3                              
6EB2: 4A         LD           C,D
6EB3: 00         NOP
6EB4: 9E         SBC         (HL)
6EB5: F2                              
6EB6: 4A         LD           C,D
6EB7: 00         NOP
6EB8: FF         RST         0X38
6EB9: FF         RST         0X38
6EBA: FF         RST         0X38
6EBB: FF         RST         0X38
6EBC: FF         RST         0X38
6EBD: FF         RST         0X38
6EBE: FF         RST         0X38
6EBF: FF         RST         0X38
6EC0: FF         RST         0X38
6EC1: FF         RST         0X38
6EC2: FF         RST         0X38
6EC3: FF         RST         0X38
6EC4: FF         RST         0X38
6EC5: FF         RST         0X38
6EC6: FF         RST         0X38
6EC7: FF         RST         0X38
6EC8: FF         RST         0X38
6EC9: FF         RST         0X38
6ECA: FF         RST         0X38
6ECB: FF         RST         0X38
6ECC: FF         RST         0X38
6ECD: FF         RST         0X38
6ECE: FF         RST         0X38
6ECF: FF         RST         0X38
6ED0: FF         RST         0X38
6ED1: FF         RST         0X38
6ED2: FF         RST         0X38
6ED3: FF         RST         0X38
6ED4: FF         RST         0X38
6ED5: FF         RST         0X38
6ED6: FF         RST         0X38
6ED7: FF         RST         0X38
6ED8: FF         RST         0X38
6ED9: FF         RST         0X38
6EDA: FF         RST         0X38
6EDB: FF         RST         0X38
6EDC: FF         RST         0X38
6EDD: FF         RST         0X38
6EDE: FF         RST         0X38
6EDF: FF         RST         0X38
6EE0: FF         RST         0X38
6EE1: FF         RST         0X38
6EE2: FF         RST         0X38
6EE3: FF         RST         0X38
6EE4: FF         RST         0X38
6EE5: FF         RST         0X38
6EE6: FF         RST         0X38
6EE7: FF         RST         0X38
6EE8: FF         RST         0X38
6EE9: FF         RST         0X38
6EEA: FF         RST         0X38
6EEB: FF         RST         0X38
6EEC: FF         RST         0X38
6EED: FF         RST         0X38
6EEE: FF         RST         0X38
6EEF: FF         RST         0X38
6EF0: FF         RST         0X38
6EF1: FF         RST         0X38
6EF2: FF         RST         0X38
6EF3: FF         RST         0X38
6EF4: FF         RST         0X38
6EF5: FF         RST         0X38
6EF6: FF         RST         0X38
6EF7: FF         RST         0X38
6EF8: FF         RST         0X38
6EF9: FF         RST         0X38
6EFA: FF         RST         0X38
6EFB: FF         RST         0X38
6EFC: FF         RST         0X38
6EFD: FF         RST         0X38
6EFE: FF         RST         0X38
6EFF: FF         RST         0X38
6F00: FF         RST         0X38
6F01: FF         RST         0X38
6F02: FF         RST         0X38
6F03: FF         RST         0X38
6F04: FF         RST         0X38
6F05: FF         RST         0X38
6F06: FF         RST         0X38
6F07: FF         RST         0X38
6F08: FF         RST         0X38
6F09: FF         RST         0X38
6F0A: FF         RST         0X38
6F0B: FF         RST         0X38
6F0C: FF         RST         0X38
6F0D: FF         RST         0X38
6F0E: FF         RST         0X38
6F0F: FF         RST         0X38
6F10: FF         RST         0X38
6F11: FF         RST         0X38
6F12: FF         RST         0X38
6F13: FF         RST         0X38
6F14: FF         RST         0X38
6F15: FF         RST         0X38
6F16: FF         RST         0X38
6F17: FF         RST         0X38
6F18: FF         RST         0X38
6F19: FF         RST         0X38
6F1A: FF         RST         0X38
6F1B: FF         RST         0X38
6F1C: FF         RST         0X38
6F1D: FF         RST         0X38
6F1E: FF         RST         0X38
6F1F: FF         RST         0X38
6F20: FF         RST         0X38
6F21: FF         RST         0X38
6F22: FF         RST         0X38
6F23: FF         RST         0X38
6F24: FF         RST         0X38
6F25: FF         RST         0X38
6F26: FF         RST         0X38
6F27: FF         RST         0X38
6F28: FF         RST         0X38
6F29: FF         RST         0X38
6F2A: FF         RST         0X38
6F2B: FF         RST         0X38
6F2C: FF         RST         0X38
6F2D: FF         RST         0X38
6F2E: FF         RST         0X38
6F2F: FF         RST         0X38
6F30: FF         RST         0X38
6F31: FF         RST         0X38
6F32: FF         RST         0X38
6F33: FF         RST         0X38
6F34: FF         RST         0X38
6F35: FF         RST         0X38
6F36: FF         RST         0X38
6F37: FF         RST         0X38
6F38: FF         RST         0X38
6F39: FF         RST         0X38
6F3A: FF         RST         0X38
6F3B: FF         RST         0X38
6F3C: FF         RST         0X38
6F3D: FF         RST         0X38
6F3E: FF         RST         0X38
6F3F: FF         RST         0X38
6F40: FF         RST         0X38
6F41: FF         RST         0X38
6F42: FF         RST         0X38
6F43: FF         RST         0X38
6F44: FF         RST         0X38
6F45: FF         RST         0X38
6F46: FF         RST         0X38
6F47: FF         RST         0X38
6F48: FF         RST         0X38
6F49: FF         RST         0X38
6F4A: FF         RST         0X38
6F4B: FF         RST         0X38
6F4C: FF         RST         0X38
6F4D: FF         RST         0X38
6F4E: FF         RST         0X38
6F4F: FF         RST         0X38
6F50: FF         RST         0X38
6F51: FF         RST         0X38
6F52: FF         RST         0X38
6F53: FF         RST         0X38
6F54: FF         RST         0X38
6F55: FF         RST         0X38
6F56: FF         RST         0X38
6F57: FF         RST         0X38
6F58: FF         RST         0X38
6F59: FF         RST         0X38
6F5A: FF         RST         0X38
6F5B: FF         RST         0X38
6F5C: FF         RST         0X38
6F5D: FF         RST         0X38
6F5E: FF         RST         0X38
6F5F: FF         RST         0X38
6F60: FF         RST         0X38
6F61: FF         RST         0X38
6F62: FF         RST         0X38
6F63: FF         RST         0X38
6F64: FF         RST         0X38
6F65: FF         RST         0X38
6F66: FF         RST         0X38
6F67: FF         RST         0X38
6F68: FF         RST         0X38
6F69: FF         RST         0X38
6F6A: FF         RST         0X38
6F6B: FF         RST         0X38
6F6C: FF         RST         0X38
6F6D: FF         RST         0X38
6F6E: FF         RST         0X38
6F6F: FF         RST         0X38
6F70: FF         RST         0X38
6F71: FF         RST         0X38
6F72: FF         RST         0X38
6F73: FF         RST         0X38
6F74: FF         RST         0X38
6F75: FF         RST         0X38
6F76: FF         RST         0X38
6F77: FF         RST         0X38
6F78: FF         RST         0X38
6F79: FF         RST         0X38
6F7A: FF         RST         0X38
6F7B: FF         RST         0X38
6F7C: FF         RST         0X38
6F7D: FF         RST         0X38
6F7E: FF         RST         0X38
6F7F: FF         RST         0X38
6F80: FF         RST         0X38
6F81: FF         RST         0X38
6F82: FF         RST         0X38
6F83: FF         RST         0X38
6F84: FF         RST         0X38
6F85: FF         RST         0X38
6F86: FF         RST         0X38
6F87: FF         RST         0X38
6F88: FF         RST         0X38
6F89: FF         RST         0X38
6F8A: FF         RST         0X38
6F8B: FF         RST         0X38
6F8C: FF         RST         0X38
6F8D: FF         RST         0X38
6F8E: FF         RST         0X38
6F8F: FF         RST         0X38
6F90: FF         RST         0X38
6F91: FF         RST         0X38
6F92: FF         RST         0X38
6F93: FF         RST         0X38
6F94: FF         RST         0X38
6F95: FF         RST         0X38
6F96: FF         RST         0X38
6F97: FF         RST         0X38
6F98: FF         RST         0X38
6F99: FF         RST         0X38
6F9A: FF         RST         0X38
6F9B: FF         RST         0X38
6F9C: FF         RST         0X38
6F9D: FF         RST         0X38
6F9E: FF         RST         0X38
6F9F: FF         RST         0X38
6FA0: FF         RST         0X38
6FA1: FF         RST         0X38
6FA2: FF         RST         0X38
6FA3: FF         RST         0X38
6FA4: FF         RST         0X38
6FA5: FF         RST         0X38
6FA6: FF         RST         0X38
6FA7: FF         RST         0X38
6FA8: FF         RST         0X38
6FA9: FF         RST         0X38
6FAA: FF         RST         0X38
6FAB: FF         RST         0X38
6FAC: FF         RST         0X38
6FAD: FF         RST         0X38
6FAE: FF         RST         0X38
6FAF: FF         RST         0X38
6FB0: FF         RST         0X38
6FB1: FF         RST         0X38
6FB2: FF         RST         0X38
6FB3: FF         RST         0X38
6FB4: FF         RST         0X38
6FB5: FF         RST         0X38
6FB6: FF         RST         0X38
6FB7: FF         RST         0X38
6FB8: FF         RST         0X38
6FB9: FF         RST         0X38
6FBA: FF         RST         0X38
6FBB: FF         RST         0X38
6FBC: FF         RST         0X38
6FBD: FF         RST         0X38
6FBE: FF         RST         0X38
6FBF: FF         RST         0X38
6FC0: FF         RST         0X38
6FC1: FF         RST         0X38
6FC2: FF         RST         0X38
6FC3: FF         RST         0X38
6FC4: FF         RST         0X38
6FC5: FF         RST         0X38
6FC6: FF         RST         0X38
6FC7: FF         RST         0X38
6FC8: FF         RST         0X38
6FC9: FF         RST         0X38
6FCA: FF         RST         0X38
6FCB: FF         RST         0X38
6FCC: FF         RST         0X38
6FCD: FF         RST         0X38
6FCE: FF         RST         0X38
6FCF: FF         RST         0X38
6FD0: FF         RST         0X38
6FD1: FF         RST         0X38
6FD2: FF         RST         0X38
6FD3: FF         RST         0X38
6FD4: FF         RST         0X38
6FD5: FF         RST         0X38
6FD6: FF         RST         0X38
6FD7: FF         RST         0X38
6FD8: FF         RST         0X38
6FD9: FF         RST         0X38
6FDA: FF         RST         0X38
6FDB: FF         RST         0X38
6FDC: FF         RST         0X38
6FDD: FF         RST         0X38
6FDE: FF         RST         0X38
6FDF: FF         RST         0X38
6FE0: FF         RST         0X38
6FE1: FF         RST         0X38
6FE2: FF         RST         0X38
6FE3: FF         RST         0X38
6FE4: FF         RST         0X38
6FE5: FF         RST         0X38
6FE6: FF         RST         0X38
6FE7: FF         RST         0X38
6FE8: FF         RST         0X38
6FE9: FF         RST         0X38
6FEA: FF         RST         0X38
6FEB: FF         RST         0X38
6FEC: FF         RST         0X38
6FED: FF         RST         0X38
6FEE: FF         RST         0X38
6FEF: FF         RST         0X38
6FF0: FF         RST         0X38
6FF1: FF         RST         0X38
6FF2: FF         RST         0X38
6FF3: FF         RST         0X38
6FF4: FF         RST         0X38
6FF5: FF         RST         0X38
6FF6: FF         RST         0X38
6FF7: FF         RST         0X38
6FF8: FF         RST         0X38
6FF9: FF         RST         0X38
6FFA: FF         RST         0X38
6FFB: FF         RST         0X38
6FFC: FF         RST         0X38
6FFD: FF         RST         0X38
6FFE: FF         RST         0X38
6FFF: FF         RST         0X38
7000: 00         NOP
7001: D4 4A 0B   CALL       NC,$0B4A
7004: 70         LD           (HL),B
7005: 17         RLA
7006: 4B         LD           C,E
7007: 13         INC         DE
7008: 70         LD           (HL),B
7009: 00         NOP
700A: 00         NOP
700B: 1D         DEC         E
700C: 70         LD           (HL),B
700D: 97         SUB         A
700E: 70         LD           (HL),B
700F: C0         RET         NZ
7010: 70         LD           (HL),B
7011: 00         NOP
7012: 00         NOP
7013: 26 70      LD           H,$70
7015: 97         SUB         A
7016: 70         LD           (HL),B
7017: 91         SUB         C
7018: 70         LD           (HL),B
7019: C0         RET         NZ
701A: 70         LD           (HL),B
701B: 00         NOP
701C: 00         NOP
701D: 9D         SBC         L
701E: 20 00      JR           NZ,$7020
7020: 81         ADD         A,C
7021: A2         AND         D
7022: 01 A9 01   LD           BC,$01A9
7025: 00         NOP
7026: 9D         SBC         L
7027: 0F         RRCA
7028: 73         LD           (HL),E
7029: 01 94 00   LD           BC,$0094
702C: 00         NOP
702D: D4 4A 37   CALL       NC,$374A
7030: 70         LD           (HL),B
7031: 3F         CCF
7032: 70         LD           (HL),B
7033: 43         LD           B,E
7034: 70         LD           (HL),B
7035: 00         NOP
7036: 00         NOP
7037: 4D         LD           C,L
7038: 70         LD           (HL),B
7039: 97         SUB         A
703A: 70         LD           (HL),B
703B: C0         RET         NZ
703C: 70         LD           (HL),B
703D: 00         NOP
703E: 00         NOP
703F: 58         LD           E,B
7040: 70         LD           (HL),B
7041: 00         NOP
7042: 00         NOP
7043: 89         ADC         A,C
7044: 70         LD           (HL),B
7045: 97         SUB         A
7046: 70         LD           (HL),B
7047: 91         SUB         C
7048: 70         LD           (HL),B
7049: C0         RET         NZ
704A: 70         LD           (HL),B
704B: 00         NOP
704C: 00         NOP
704D: 9D         SBC         L
704E: 20 00      JR           NZ,$7050
7050: 81         ADD         A,C
7051: A2         AND         D
7052: 01 A9 01   LD           BC,$01A9
7055: AE         XOR         (HL)
7056: 01 00 9D   LD           BC,$9D00
7059: 47         LD           B,A
705A: 00         NOP
705B: 80         ADD         A,B
705C: 96         SUB         (HL)
705D: 9B         SBC         E
705E: 0A         LD           A,(BC)
705F: A3         AND         E
7060: 74         LD           (HL),H
7061: 66         LD           H,(HL)
7062: 6A         LD           L,D
7063: 78         LD           A,B
7064: 9C         SBC         H
7065: 9B         SBC         E
7066: 02         LD           (BC),A
7067: 6E         LD           L,(HL)
7068: 60         LD           H,B
7069: 66         LD           H,(HL)
706A: 6E         LD           L,(HL)
706B: 70         LD           (HL),B
706C: 60         LD           H,B
706D: 6A         LD           L,D
706E: 70         LD           (HL),B
706F: 9C         SBC         H
7070: 74         LD           (HL),H
7071: 62         LD           H,D
7072: 6A         LD           L,D
7073: 74         LD           (HL),H
7074: 7A         LD           A,D
7075: 68         LD           L,B
7076: 6E         LD           L,(HL)
7077: 74         LD           (HL),H
7078: 70         LD           (HL),B
7079: 60         LD           H,B
707A: 66         LD           H,(HL)
707B: 70         LD           (HL),B
707C: 6A         LD           L,D
707D: 5E         LD           E,(HL)
707E: 64         LD           H,H
707F: 76         HALT
7080: 9B         SBC         E
7081: 02         LD           (BC),A
7082: 74         LD           (HL),H
7083: 66         LD           H,(HL)
7084: 6A         LD           L,D
7085: 78         LD           A,B
7086: 9C         SBC         H
7087: 95         SUB         L
7088: 00         NOP
7089: 9D         SBC         L
708A: 0F         RRCA
708B: 73         LD           (HL),E
708C: 01 AE 01   LD           BC,$01AE
708F: 94         SUB         H
7090: 00         NOP
7091: 9D         SBC         L
7092: E1         POP         HL
7093: 72         LD           (HL),D
7094: 01 94 00   LD           BC,$0094
7097: 96         SUB         (HL)
7098: A2         AND         D
7099: 01 30 34   LD           BC,$3430
709C: A8         XOR         B
709D: 36 A2      LD           (HL),$A2
709F: 30 34      JR           NC,$70D5
70A1: A8         XOR         B
70A2: 36 A2      LD           (HL),$A2
70A4: 34         INC         (HL)
70A5: 30 26      JR           NC,$70CD
70A7: A7         AND         A
70A8: 2C         INC         L
70A9: A5         AND         L
70AA: 30 A3      JR           NC,$704F
70AC: 01 A2 30   LD           BC,$30A2
70AF: 34         INC         (HL)
70B0: A8         XOR         B
70B1: 36 A2      LD           (HL),$A2
70B3: 2C         INC         L
70B4: 36 A8      LD           (HL),$A8
70B6: 40         LD           B,B
70B7: A2         AND         D
70B8: 3E 3A      LD           A,$3A
70BA: A5         AND         L
70BB: 3E 01      LD           A,$01
70BD: A2         AND         D
70BE: 01 00 A3   LD           BC,$A300
70C1: 01 64 60   LD           BC,$6064
70C4: 56         LD           D,(HL)
70C5: A7         AND         A
70C6: 56         LD           D,(HL)
70C7: A5         AND         L
70C8: 58         LD           E,B
70C9: A2         AND         D
70CA: 6A         LD           L,D
70CB: 66         LD           H,(HL)
70CC: 64         LD           H,H
70CD: 60         LD           H,B
70CE: 56         LD           D,(HL)
70CF: 52         LD           D,D
70D0: 56         LD           D,(HL)
70D1: 60         LD           H,B
70D2: A7         AND         A
70D3: 58         LD           E,B
70D4: A2         AND         D
70D5: 58         LD           E,B
70D6: A4         AND         H
70D7: 5C         LD           E,H
70D8: A2         AND         D
70D9: 01 4A 52   LD           BC,$524A
70DC: 5C         LD           E,H
70DD: A8         XOR         B
70DE: 56         LD           D,(HL)
70DF: A2         AND         D
70E0: 01 4E A8   LD           BC,$A84E
70E3: 60         LD           H,B
70E4: A7         AND         A
70E5: 01 5E 70   LD           BC,$705E
70E8: 6E         LD           L,(HL)
70E9: 01 A4 01   LD           BC,$01A4
70EC: A5         AND         L
70ED: 01 95 00   LD           BC,$0095
70F0: 00         NOP
70F1: D4 4A 3F   CALL       NC,$3F4A
70F4: 70         LD           (HL),B
70F5: FB         EI
70F6: 70         LD           (HL),B
70F7: 43         LD           B,E
70F8: 70         LD           (HL),B
70F9: 00         NOP
70FA: 00         NOP
70FB: 07         RLCA
70FC: 71         LD           (HL),C
70FD: 14         INC         D
70FE: 71         LD           (HL),C
70FF: 23         INC         HL
7100: 71         LD           (HL),C
7101: 23         INC         HL
7102: 71         LD           (HL),C
7103: 33         INC         SP
7104: 71         LD           (HL),C
7105: 00         NOP
7106: 00         NOP
7107: 9D         SBC         L
7108: 71         LD           (HL),C
7109: 82         ADD         A,D
710A: 80         ADD         A,B
710B: 96         SUB         (HL)
710C: 9B         SBC         E
710D: 04         INC         B
710E: A2         AND         D
710F: 4E         LD           C,(HL)
7110: 56         LD           D,(HL)
7111: 64         LD           H,H
7112: 5C         LD           E,H
7113: 9C         SBC         H
7114: 9B         SBC         E
7115: 04         INC         B
7116: 52         LD           D,D
7117: 58         LD           E,B
7118: 66         LD           H,(HL)
7119: 60         LD           H,B
711A: 9C         SBC         H
711B: 9B         SBC         E
711C: 04         INC         B
711D: 4E         LD           C,(HL)
711E: 56         LD           D,(HL)
711F: 64         LD           H,H
7120: 60         LD           H,B
7121: 9C         SBC         H
7122: 00         NOP
7123: 9B         SBC         E
7124: 02         LD           (BC),A
7125: A2         AND         D
7126: 48         LD           C,B
7127: 4E         LD           C,(HL)
7128: 60         LD           H,B
7129: 56         LD           D,(HL)
712A: 9C         SBC         H
712B: 9B         SBC         E
712C: 02         LD           (BC),A
712D: 48         LD           C,B
712E: 52         LD           D,D
712F: 60         LD           H,B
7130: 58         LD           E,B
7131: 9C         SBC         H
7132: 00         NOP
7133: 9B         SBC         E
7134: 02         LD           (BC),A
7135: 44         LD           B,H
7136: 4A         LD           C,D
7137: 58         LD           E,B
7138: 52         LD           D,D
7139: 9C         SBC         H
713A: 9B         SBC         E
713B: 02         LD           (BC),A
713C: 44         LD           B,H
713D: 4A         LD           C,D
713E: 56         LD           D,(HL)
713F: 50         LD           D,B
7140: 9C         SBC         H
7141: 9B         SBC         E
7142: 02         LD           (BC),A
7143: 40         LD           B,B
7144: 48         LD           C,B
7145: 56         LD           D,(HL)
7146: 4E         LD           C,(HL)
7147: 9C         SBC         H
7148: 9B         SBC         E
7149: 02         LD           (BC),A
714A: 40         LD           B,B
714B: 46         LD           B,(HL)
714C: 52         LD           D,D
714D: 4C         LD           C,H
714E: 9C         SBC         H
714F: 9B         SBC         E
7150: 04         INC         B
7151: 4E         LD           C,(HL)
7152: 56         LD           D,(HL)
7153: 64         LD           H,H
7154: 5C         LD           E,H
7155: 9C         SBC         H
7156: 95         SUB         L
7157: 00         NOP
7158: 00         NOP
7159: D4 4A 63   CALL       NC,$634A
715C: 71         LD           (HL),C
715D: FB         EI
715E: 70         LD           (HL),B
715F: 43         LD           B,E
7160: 70         LD           (HL),B
7161: 00         NOP
7162: 00         NOP
7163: 6D         LD           L,L
7164: 71         LD           (HL),C
7165: 76         HALT
7166: 71         LD           (HL),C
7167: 76         HALT
7168: 71         LD           (HL),C
7169: 8A         ADC         A,D
716A: 71         LD           (HL),C
716B: 00         NOP
716C: 00         NOP
716D: 9D         SBC         L
716E: 87         ADD         A,A
716F: 00         NOP
7170: 80         ADD         A,B
7171: 96         SUB         (HL)
7172: A5         AND         L
7173: 8C         ADC         A,H
7174: 8C         ADC         A,H
7175: 00         NOP
7176: 9D         SBC         L
7177: 87         ADD         A,A
7178: 00         NOP
7179: 80         ADD         A,B
717A: A5         AND         L
717B: 8C         ADC         A,H
717C: 8C         ADC         A,H
717D: 9D         SBC         L
717E: 37         SCF
717F: 00         NOP
7180: 80         ADD         A,B
7181: 9B         SBC         E
7182: 02         LD           (BC),A
7183: A3         AND         E
7184: 74         LD           (HL),H
7185: 66         LD           H,(HL)
7186: 6A         LD           L,D
7187: 78         LD           A,B
7188: 9C         SBC         H
7189: 00         NOP
718A: 9D         SBC         L
718B: 76         HALT
718C: 00         NOP
718D: 80         ADD         A,B
718E: 9B         SBC         E
718F: 02         LD           (BC),A
7190: A4         AND         H
7191: 90         SUB         B
7192: 86         ADD         A,(HL)
7193: 90         SUB         B
7194: 88         ADC         A,B
7195: 9C         SBC         H
7196: 8C         ADC         A,H
7197: 88         ADC         A,B
7198: 86         ADD         A,(HL)
7199: 8C         ADC         A,H
719A: 90         SUB         B
719B: 88         ADC         A,B
719C: 8E         ADC         A,(HL)
719D: 88         ADC         A,B
719E: 9D         SBC         L
719F: 87         ADD         A,A
71A0: 00         NOP
71A1: 80         ADD         A,B
71A2: A5         AND         L
71A3: 8C         ADC         A,H
71A4: 8C         ADC         A,H
71A5: 00         NOP
71A6: 00         NOP
71A7: D4 4A 63   CALL       NC,$634A
71AA: 71         LD           (HL),C
71AB: FB         EI
71AC: 70         LD           (HL),B
71AD: 43         LD           B,E
71AE: 70         LD           (HL),B
71AF: B1         OR           C
71B0: 71         LD           (HL),C
71B1: B5         OR           L
71B2: 71         LD           (HL),C
71B3: 00         NOP
71B4: 00         NOP
71B5: 9B         SBC         E
71B6: 0A         LD           A,(BC)
71B7: A1         AND         C
71B8: 1F         RRA
71B9: 1F         RRA
71BA: 1F         RRA
71BB: 1F         RRA
71BC: A2         AND         D
71BD: 1F         RRA
71BE: A3         AND         E
71BF: 24         INC         H
71C0: A2         AND         D
71C1: 1F         RRA
71C2: A3         AND         E
71C3: 24         INC         H
71C4: A1         AND         C
71C5: 1F         RRA
71C6: 1F         RRA
71C7: 1F         RRA
71C8: 1F         RRA
71C9: A3         AND         E
71CA: 24         INC         H
71CB: A1         AND         C
71CC: 1F         RRA
71CD: 1F         RRA
71CE: 1F         RRA
71CF: 1F         RRA
71D0: A3         AND         E
71D1: 24         INC         H
71D2: 9C         SBC         H
71D3: 00         NOP
71D4: 00         NOP
71D5: D4 4A DF   CALL       NC,$DF4A
71D8: 71         LD           (HL),C
71D9: EF         RST         0X28
71DA: 71         LD           (HL),C
71DB: 43         LD           B,E
71DC: 70         LD           (HL),B
71DD: B1         OR           C
71DE: 71         LD           (HL),C
71DF: 6D         LD           L,L
71E0: 71         LD           (HL),C
71E1: 76         HALT
71E2: 71         LD           (HL),C
71E3: 76         HALT
71E4: 71         LD           (HL),C
71E5: 37         SCF
71E6: 72         LD           (HL),D
71E7: 23         INC         HL
71E8: 71         LD           (HL),C
71E9: 23         INC         HL
71EA: 71         LD           (HL),C
71EB: 33         INC         SP
71EC: 71         LD           (HL),C
71ED: 00         NOP
71EE: 00         NOP
71EF: F7         RST         0X30
71F0: 71         LD           (HL),C
71F1: 04         INC         B
71F2: 72         LD           (HL),D
71F3: 13         INC         DE
71F4: 72         LD           (HL),D
71F5: 00         NOP
71F6: 00         NOP
71F7: 9D         SBC         L
71F8: 19         ADD         HL,DE
71F9: 45         LD           B,L
71FA: 40         LD           B,B
71FB: 96         SUB         (HL)
71FC: 9B         SBC         E
71FD: 02         LD           (BC),A
71FE: A3         AND         E
71FF: 1E 2C      LD           E,$2C
7201: 26 2C      LD           H,$2C
7203: 9C         SBC         H
7204: 9B         SBC         E
7205: 02         LD           (BC),A
7206: 22         LD           (HLI),A
7207: 30 28      JR           NC,$7231
7209: 30 9C      JR           NC,$71A7
720B: 9B         SBC         E
720C: 02         LD           (BC),A
720D: 1E 2C      LD           E,$2C
720F: 26 2C      LD           H,$2C
7211: 9C         SBC         H
7212: 00         NOP
7213: 9B         SBC         E
7214: 02         LD           (BC),A
7215: A3         AND         E
7216: 18 26      JR           $723E
7218: 1E 26      LD           E,$26
721A: 18 28      JR           $7244
721C: 22         LD           (HLI),A
721D: 28 9C      JR           Z,$71BB
721F: 2C         INC         L
7220: 22         LD           (HLI),A
7221: 1A         LD           A,(DE)
7222: 22         LD           (HLI),A
7223: 2C         INC         L
7224: 20 1A      JR           NZ,$7240
7226: 20 28      JR           NZ,$7250
7228: 1E 18      LD           E,$18
722A: 1E 28      LD           E,$28
722C: 1C         INC         E
722D: 16 1C      LD           D,$1C
722F: 9B         SBC         E
7230: 02         LD           (BC),A
7231: 1E 2C      LD           E,$2C
7233: 26 2C      LD           H,$2C
7235: 9C         SBC         H
7236: 00         NOP
7237: 9D         SBC         L
7238: 61         LD           H,C
7239: 82         ADD         A,D
723A: 80         ADD         A,B
723B: 00         NOP
723C: 00         NOP
723D: D4 4A FB   CALL       NC,$FB4A
7240: 70         LD           (HL),B
7241: 47         LD           B,A
7242: 72         LD           (HL),D
7243: 43         LD           B,E
7244: 70         LD           (HL),B
7245: 53         LD           D,E
7246: 72         LD           (HL),D
7247: 6D         LD           L,L
7248: 71         LD           (HL),C
7249: 76         HALT
724A: 71         LD           (HL),C
724B: 76         HALT
724C: 71         LD           (HL),C
724D: 7D         LD           A,L
724E: 72         LD           (HL),D
724F: 13         INC         DE
7250: 72         LD           (HL),D
7251: 00         NOP
7252: 00         NOP
7253: 82         ADD         A,D
7254: 72         LD           (HL),D
7255: 82         ADD         A,D
7256: 72         LD           (HL),D
7257: 82         ADD         A,D
7258: 72         LD           (HL),D
7259: 82         ADD         A,D
725A: 72         LD           (HL),D
725B: 82         ADD         A,D
725C: 72         LD           (HL),D
725D: 82         ADD         A,D
725E: 72         LD           (HL),D
725F: 82         ADD         A,D
7260: 72         LD           (HL),D
7261: 82         ADD         A,D
7262: 72         LD           (HL),D
7263: 82         ADD         A,D
7264: 72         LD           (HL),D
7265: 82         ADD         A,D
7266: 72         LD           (HL),D
7267: 95         SUB         L
7268: 72         LD           (HL),D
7269: 82         ADD         A,D
726A: 72         LD           (HL),D
726B: 95         SUB         L
726C: 72         LD           (HL),D
726D: 82         ADD         A,D
726E: 72         LD           (HL),D
726F: 82         ADD         A,D
7270: 72         LD           (HL),D
7271: 82         ADD         A,D
7272: 72         LD           (HL),D
7273: 82         ADD         A,D
7274: 72         LD           (HL),D
7275: 82         ADD         A,D
7276: 72         LD           (HL),D
7277: 82         ADD         A,D
7278: 72         LD           (HL),D
7279: 82         ADD         A,D
727A: 72         LD           (HL),D
727B: 00         NOP
727C: 00         NOP
727D: 9D         SBC         L
727E: 19         ADD         HL,DE
727F: 45         LD           B,L
7280: 40         LD           B,B
7281: 00         NOP
7282: 9B         SBC         E
7283: 03         INC         BC
7284: A2         AND         D
7285: 1A         LD           A,(DE)
7286: A9         XOR         C
7287: 15         DEC         D
7288: AD         XOR         L
7289: 01 A9 15   LD           BC,$15A9
728C: AD         XOR         L
728D: 01 A9 15   LD           BC,$15A9
7290: 9C         SBC         H
7291: A2         AND         D
7292: 1A         LD           A,(DE)
7293: 1A         LD           A,(DE)
7294: 00         NOP
7295: 9B         SBC         E
7296: 02         LD           (BC),A
7297: A1         AND         C
7298: 1F         RRA
7299: 1F         RRA
729A: 1F         RRA
729B: 1F         RRA
729C: A2         AND         D
729D: 1F         RRA
729E: A3         AND         E
729F: 24         INC         H
72A0: A2         AND         D
72A1: 1F         RRA
72A2: A3         AND         E
72A3: 24         INC         H
72A4: 00         NOP
72A5: 00         NOP
72A6: E3                              
72A7: 4A         LD           C,D
72A8: 17         RLA
72A9: 4B         LD           C,E
72AA: B0         OR           B
72AB: 72         LD           (HL),D
72AC: B6         OR           (HL)
72AD: 72         LD           (HL),D
72AE: 00         NOP
72AF: 00         NOP
72B0: BA         CP           D
72B1: 72         LD           (HL),D
72B2: C8         RET         Z
72B3: 72         LD           (HL),D
72B4: 00         NOP
72B5: 00         NOP
72B6: C3 72 00   JP           $0072
72B9: 00         NOP
72BA: 9D         SBC         L
72BB: 20 00      JR           NZ,$72BD
72BD: 41         LD           B,C
72BE: A1         AND         C
72BF: 01 A0 01   LD           BC,$01A0
72C2: 00         NOP
72C3: 9D         SBC         L
72C4: E1         POP         HL
72C5: 72         LD           (HL),D
72C6: 01 94 A2   LD           BC,$A294
72C9: 60         LD           H,B
72CA: 64         LD           H,H
72CB: A8         XOR         B
72CC: 66         LD           H,(HL)
72CD: A2         AND         D
72CE: 60         LD           H,B
72CF: 64         LD           H,H
72D0: A4         AND         H
72D1: 66         LD           H,(HL)
72D2: A2         AND         D
72D3: 64         LD           H,H
72D4: A6         AND         (HL)
72D5: 60         LD           H,B
72D6: A3         AND         E
72D7: 56         LD           D,(HL)
72D8: AE         XOR         (HL)
72D9: 6E         LD           L,(HL)
72DA: 9A         SBC         D
72DB: 9B         SBC         E
72DC: 20 A5      JR           NZ,$7283
72DE: 01 9C 00   LD           BC,$009C
72E1: 01 35 66   LD           BC,$6635
72E4: 53         LD           D,E
72E5: 10 02      STOP       $02
72E7: 46         LD           B,(HL)
72E8: 8A         ADC         A,D
72E9: 01 35 66   LD           BC,$6635
72EC: 53         LD           D,E
72ED: 10 02      STOP       $02
72EF: 46         LD           B,(HL)
72F0: 8A         ADC         A,D
72F1: 00         NOP
72F2: F2                              
72F3: 4A         LD           C,D
72F4: 17         RLA
72F5: 4B         LD           C,E
72F6: FC                              
72F7: 72         LD           (HL),D
72F8: 02         LD           (BC),A
72F9: 73         LD           (HL),E
72FA: 00         NOP
72FB: 00         NOP
72FC: 06 73      LD           B,$73
72FE: 24         INC         H
72FF: 73         LD           (HL),E
7300: 00         NOP
7301: 00         NOP
7302: 1F         RRA
7303: 73         LD           (HL),E
7304: 00         NOP
7305: 00         NOP
7306: 9D         SBC         L
7307: 20 00      JR           NZ,$7309
7309: 41         LD           B,C
730A: A1         AND         C
730B: 01 A0 01   LD           BC,$01A0
730E: 00         NOP
730F: 06 9B      LD           B,$9B
7311: CD DE EE   CALL       $EEDE
7314: FF         RST         0X38
7315: FF         RST         0X38
7316: FE 06      CP           $06
7318: 9B         SBC         E
7319: CD DE EE   CALL       $EEDE
731C: FF         RST         0X38
731D: FF         RST         0X38
731E: FE 9D      CP           $9D
7320: 0F         RRCA
7321: 73         LD           (HL),E
7322: 01 94 A1   LD           BC,$A194
7325: 30 34      JR           NC,$735B
7327: A4         AND         H
7328: 36 A3      LD           (HL),$A3
732A: 01 A1 30   LD           BC,$30A1
732D: 34         INC         (HL)
732E: A2         AND         D
732F: 36 34      LD           (HL),$34
7331: A6         AND         (HL)
7332: 30 A3      JR           NC,$72D7
7334: 26 A2      LD           H,$A2
7336: 01 A5 3E   LD           BC,$3EA5
7339: 9B         SBC         E
733A: 20 AE      JR           NZ,$72EA
733C: 01 9C 00   LD           BC,$009C
733F: 00         NOP
7340: D4 4A 17   CALL       NC,$174A
7343: 4B         LD           C,E
7344: 4A         LD           C,D
7345: 73         LD           (HL),E
7346: 54         LD           D,H
7347: 73         LD           (HL),E
7348: 00         NOP
7349: 00         NOP
734A: 5A         LD           E,D
734B: 73         LD           (HL),E
734C: 5A         LD           E,D
734D: 73         LD           (HL),E
734E: 6A         LD           L,D
734F: 73         LD           (HL),E
7350: FF         RST         0X38
7351: FF         RST         0X38
7352: BB         CP           E
7353: 78         LD           A,B
7354: 80         ADD         A,B
7355: 73         LD           (HL),E
7356: FF         RST         0X38
7357: FF         RST         0X38
7358: BB         CP           E
7359: 78         LD           A,B
735A: 9D         SBC         L
735B: 81         ADD         A,C
735C: 00         NOP
735D: 80         ADD         A,B
735E: A1         AND         C
735F: 74         LD           (HL),H
7360: 66         LD           H,(HL)
7361: 6A         LD           L,D
7362: 78         LD           A,B
7363: 9D         SBC         L
7364: A6         AND         (HL)
7365: 00         NOP
7366: 80         ADD         A,B
7367: A4         AND         H
7368: 74         LD           (HL),H
7369: 00         NOP
736A: 9D         SBC         L
736B: 82         ADD         A,D
736C: 00         NOP
736D: 80         ADD         A,B
736E: A2         AND         D
736F: 74         LD           (HL),H
7370: 66         LD           H,(HL)
7371: A6         AND         (HL)
7372: 6A         LD           L,D
7373: 9D         SBC         L
7374: 85         ADD         A,L
7375: 00         NOP
7376: 80         ADD         A,B
7377: A3         AND         E
7378: 78         LD           A,B
7379: 9D         SBC         L
737A: A6         AND         (HL)
737B: 00         NOP
737C: 80         ADD         A,B
737D: AE         XOR         (HL)
737E: 74         LD           (HL),H
737F: 00         NOP
7380: 9D         SBC         L
7381: 0C         INC         C
7382: 75         LD           (HL),L
7383: 23         INC         HL
7384: 99         SBC         C
7385: 9B         SBC         E
7386: 02         LD           (BC),A
7387: A1         AND         C
7388: 6A         LD           L,D
7389: 5C         LD           E,H
738A: 60         LD           H,B
738B: 6E         LD           L,(HL)
738C: A4         AND         H
738D: 6A         LD           L,D
738E: 9C         SBC         H
738F: A2         AND         D
7390: 6A         LD           L,D
7391: 5C         LD           E,H
7392: A6         AND         (HL)
7393: 60         LD           H,B
7394: A3         AND         E
7395: 6E         LD           L,(HL)
7396: AE         XOR         (HL)
7397: 6A         LD           L,D
7398: 9B         SBC         E
7399: 20 AE      JR           NZ,$7349
739B: 01 9C 00   LD           BC,$009C
739E: 18 98      JR           $7338
73A0: 4A         LD           C,D
73A1: 17         RLA
73A2: 4B         LD           C,E
73A3: A9         XOR         C
73A4: 73         LD           (HL),E
73A5: AF         XOR         A
73A6: 73         LD           (HL),E
73A7: 00         NOP
73A8: 00         NOP
73A9: B3         OR           E
73AA: 73         LD           (HL),E
73AB: D1         POP         DE
73AC: 73         LD           (HL),E
73AD: 00         NOP
73AE: 00         NOP
73AF: CC 73 00   CALL       Z,$0073
73B2: 00         NOP
73B3: 9D         SBC         L
73B4: 10 00      STOP       $00
73B6: 80         ADD         A,B
73B7: A3         AND         E
73B8: 01 A1 01   LD           BC,$01A1
73BB: 00         NOP
73BC: 46         LD           B,(HL)
73BD: 79         LD           A,C
73BE: 98         SBC         B
73BF: 64         LD           H,H
73C0: 43         LD           B,E
73C1: 10 01      STOP       $01
73C3: 34         INC         (HL)
73C4: 46         LD           B,(HL)
73C5: 79         LD           A,C
73C6: 98         SBC         B
73C7: 64         LD           H,H
73C8: 43         LD           B,E
73C9: 10 01      STOP       $01
73CB: 34         INC         (HL)
73CC: 9D         SBC         L
73CD: BC         CP           H
73CE: 73         LD           (HL),E
73CF: 20 99      JR           NZ,$736A
73D1: A3         AND         E
73D2: 62         LD           H,D
73D3: 60         LD           H,B
73D4: 58         LD           E,B
73D5: 52         LD           D,D
73D6: A6         AND         (HL)
73D7: 4A         LD           C,D
73D8: 48         LD           C,B
73D9: 4A         LD           C,D
73DA: 52         LD           D,D
73DB: 58         LD           E,B
73DC: AB         XOR         E
73DD: 60         LD           H,B
73DE: 58         LD           E,B
73DF: 52         LD           D,D
73E0: 4A         LD           C,D
73E1: A2         AND         D
73E2: 48         LD           C,B
73E3: 4A         LD           C,D
73E4: 52         LD           D,D
73E5: 58         LD           E,B
73E6: 60         LD           H,B
73E7: 58         LD           E,B
73E8: 52         LD           D,D
73E9: 4A         LD           C,D
73EA: 48         LD           C,B
73EB: 4A         LD           C,D
73EC: 52         LD           D,D
73ED: 58         LD           E,B
73EE: 9B         SBC         E
73EF: 02         LD           (BC),A
73F0: 5E         LD           E,(HL)
73F1: 56         LD           D,(HL)
73F2: 50         LD           D,B
73F3: 48         LD           C,B
73F4: 46         LD           B,(HL)
73F5: 48         LD           C,B
73F6: 50         LD           D,B
73F7: 56         LD           D,(HL)
73F8: 9C         SBC         H
73F9: 58         LD           E,B
73FA: 50         LD           D,B
73FB: 4A         LD           C,D
73FC: 42         LD           B,D
73FD: 40         LD           B,B
73FE: 42         LD           B,D
73FF: 4A         LD           C,D
7400: 50         LD           D,B
7401: AB         XOR         E
7402: 54         LD           D,H
7403: 4C         LD           C,H
7404: 46         LD           B,(HL)
7405: 3E A6      LD           A,$A6
7407: 3C         INC         A
7408: 3E A3      LD           A,$A3
740A: 46         LD           B,(HL)
740B: 4C         LD           C,H
740C: AA         XOR         D
740D: 01 A2 50   LD           BC,$50A2
7410: 9B         SBC         E
7411: 20 AE      JR           NZ,$73C1
7413: 01 9C 00   LD           BC,$009C
7416: 00         NOP
7417: B6         OR           (HL)
7418: 4A         LD           C,D
7419: 21 74 27   LD           HL,$2774
741C: 74         LD           (HL),H
741D: 2D         DEC         L
741E: 74         LD           (HL),H
741F: 00         NOP
7420: 00         NOP
7421: 33         INC         SP
7422: 74         LD           (HL),H
7423: FF         RST         0X38
7424: FF         RST         0X38
7425: BB         CP           E
7426: 78         LD           A,B
7427: 58         LD           E,B
7428: 74         LD           (HL),H
7429: FF         RST         0X38
742A: FF         RST         0X38
742B: BB         CP           E
742C: 78         LD           A,B
742D: 8C         ADC         A,H
742E: 74         LD           (HL),H
742F: FF         RST         0X38
7430: FF         RST         0X38
7431: BB         CP           E
7432: 78         LD           A,B
7433: 9D         SBC         L
7434: 81         ADD         A,C
7435: 00         NOP
7436: 80         ADD         A,B
7437: A1         AND         C
7438: 01 A2 6E   LD           BC,$6EA2
743B: 9D         SBC         L
743C: C1         POP         BC
743D: 00         NOP
743E: 80         ADD         A,B
743F: A2         AND         D
7440: 6E         LD           L,(HL)
7441: A6         AND         (HL)
7442: 01 A4 01   LD           BC,$01A4
7445: 9D         SBC         L
7446: A2         AND         D
7447: 00         NOP
7448: 80         ADD         A,B
7449: A2         AND         D
744A: 01 A3 64   LD           BC,$64A3
744D: 6A         LD           L,D
744E: 74         LD           (HL),H
744F: 6A         LD           L,D
7450: 78         LD           A,B
7451: 9D         SBC         L
7452: A7         AND         A
7453: 00         NOP
7454: 80         ADD         A,B
7455: AE         XOR         (HL)
7456: 8C         ADC         A,H
7457: 00         NOP
7458: 9D         SBC         L
7459: 61         LD           H,C
745A: 00         NOP
745B: 80         ADD         A,B
745C: A2         AND         D
745D: 6E         LD           L,(HL)
745E: 9D         SBC         L
745F: A1         AND         C
7460: 00         NOP
7461: 80         ADD         A,B
7462: A2         AND         D
7463: 6E         LD           L,(HL)
7464: 9D         SBC         L
7465: E5         PUSH       HL
7466: 00         NOP
7467: 80         ADD         A,B
7468: A8         XOR         B
7469: 6E         LD           L,(HL)
746A: 9D         SBC         L
746B: A2         AND         D
746C: 00         NOP
746D: 80         ADD         A,B
746E: A3         AND         E
746F: 60         LD           H,B
7470: 66         LD           H,(HL)
7471: 6E         LD           L,(HL)
7472: 72         LD           (HL),D
7473: 6E         LD           L,(HL)
7474: 82         ADD         A,D
7475: 9D         SBC         L
7476: A7         AND         A
7477: 00         NOP
7478: 80         ADD         A,B
7479: AE         XOR         (HL)
747A: 86         ADD         A,(HL)
747B: 00         NOP
747C: 66         LD           H,(HL)
747D: 00         NOP
747E: 66         LD           H,(HL)
747F: 00         NOP
7480: 66         LD           H,(HL)
7481: 00         NOP
7482: 66         LD           H,(HL)
7483: 00         NOP
7484: 66         LD           H,(HL)
7485: 00         NOP
7486: 66         LD           H,(HL)
7487: 00         NOP
7488: 66         LD           H,(HL)
7489: 00         NOP
748A: 66         LD           H,(HL)
748B: 00         NOP
748C: 9D         SBC         L
748D: 7C         LD           A,H
748E: 74         LD           (HL),H
748F: 23         INC         HL
7490: 99         SBC         C
7491: A1         AND         C
7492: 64         LD           H,H
7493: 64         LD           H,H
7494: 64         LD           H,H
7495: 64         LD           H,H
7496: A8         XOR         B
7497: 64         LD           H,H
7498: A2         AND         D
7499: 56         LD           D,(HL)
749A: 5A         LD           E,D
749B: 5C         LD           E,H
749C: 78         LD           A,B
749D: 64         LD           H,H
749E: 6A         LD           L,D
749F: 68         LD           L,B
74A0: 60         LD           H,B
74A1: 64         LD           H,H
74A2: 6E         LD           L,(HL)
74A3: 78         LD           A,B
74A4: 82         ADD         A,D
74A5: AE         XOR         (HL)
74A6: 7C         LD           A,H
74A7: 00         NOP
74A8: 00         NOP
74A9: C5         PUSH       BC
74AA: 4A         LD           C,D
74AB: 17         RLA
74AC: 4B         LD           C,E
74AD: B3         OR           E
74AE: 74         LD           (HL),H
74AF: CF         RST         0X08
74B0: 74         LD           (HL),H
74B1: 00         NOP
74B2: 00         NOP
74B3: D3                              
74B4: 74         LD           (HL),H
74B5: EC                              
74B6: 74         LD           (HL),H
74B7: D3                              
74B8: 74         LD           (HL),H
74B9: FE 74      CP           $74
74BB: D3                              
74BC: 74         LD           (HL),H
74BD: FE 74      CP           $74
74BF: D3                              
74C0: 74         LD           (HL),H
74C1: EC                              
74C2: 74         LD           (HL),H
74C3: D3                              
74C4: 74         LD           (HL),H
74C5: FE 74      CP           $74
74C7: D3                              
74C8: 74         LD           (HL),H
74C9: 05         DEC         B
74CA: 75         LD           (HL),L
74CB: 40         LD           B,B
74CC: 75         LD           (HL),L
74CD: 00         NOP
74CE: 00         NOP
74CF: 1C         INC         E
74D0: 75         LD           (HL),L
74D1: 00         NOP
74D2: 00         NOP
74D3: 9D         SBC         L
74D4: 21 00 80   LD           HL,$8000
74D7: A1         AND         C
74D8: 78         LD           A,B
74D9: 9D         SBC         L
74DA: 41         LD           B,C
74DB: 00         NOP
74DC: 80         ADD         A,B
74DD: A1         AND         C
74DE: 78         LD           A,B
74DF: 9D         SBC         L
74E0: 71         LD           (HL),C
74E1: 00         NOP
74E2: 80         ADD         A,B
74E3: A1         AND         C
74E4: 78         LD           A,B
74E5: 9D         SBC         L
74E6: A1         AND         C
74E7: 00         NOP
74E8: 80         ADD         A,B
74E9: A1         AND         C
74EA: 78         LD           A,B
74EB: 00         NOP
74EC: 9D         SBC         L
74ED: A1         AND         C
74EE: 00         NOP
74EF: 80         ADD         A,B
74F0: A2         AND         D
74F1: 78         LD           A,B
74F2: 9D         SBC         L
74F3: C3 00 80   JP           $8000
74F6: A3         AND         E
74F7: 78         LD           A,B
74F8: 9D         SBC         L
74F9: 82         ADD         A,D
74FA: 00         NOP
74FB: 80         ADD         A,B
74FC: A2         AND         D
74FD: 78         LD           A,B
74FE: 9D         SBC         L
74FF: D2 00 80   JP           NC,$8000
7502: A3         AND         E
7503: 78         LD           A,B
7504: 00         NOP
7505: 9D         SBC         L
7506: E3                              
7507: 00         NOP
7508: 80         ADD         A,B
7509: AE         XOR         (HL)
750A: 78         LD           A,B
750B: 00         NOP
750C: 00         NOP
750D: 0C         INC         C
750E: 00         NOP
750F: 0C         INC         C
7510: 00         NOP
7511: 0C         INC         C
7512: 00         NOP
7513: 0C         INC         C
7514: 06 06      LD           B,$06
7516: 06 06      LD           B,$06
7518: 06 06      LD           B,$06
751A: 06 06      LD           B,$06
751C: 9D         SBC         L
751D: 0C         INC         C
751E: 75         LD           (HL),L
751F: 20 99      JR           NZ,$74BA
7521: 9B         SBC         E
7522: 02         LD           (BC),A
7523: A1         AND         C
7524: 86         ADD         A,(HL)
7525: 86         ADD         A,(HL)
7526: 86         ADD         A,(HL)
7527: 86         ADD         A,(HL)
7528: A2         AND         D
7529: 86         ADD         A,(HL)
752A: A3         AND         E
752B: 86         ADD         A,(HL)
752C: A2         AND         D
752D: 86         ADD         A,(HL)
752E: A3         AND         E
752F: 86         ADD         A,(HL)
7530: A1         AND         C
7531: 86         ADD         A,(HL)
7532: 86         ADD         A,(HL)
7533: 86         ADD         A,(HL)
7534: 86         ADD         A,(HL)
7535: A3         AND         E
7536: 86         ADD         A,(HL)
7537: A1         AND         C
7538: 86         ADD         A,(HL)
7539: 86         ADD         A,(HL)
753A: 86         ADD         A,(HL)
753B: 86         ADD         A,(HL)
753C: A3         AND         E
753D: 86         ADD         A,(HL)
753E: 9C         SBC         H
753F: 9A         SBC         D
7540: 9B         SBC         E
7541: 20 AE      JR           NZ,$74F1
7543: 01 9C 00   LD           BC,$009C
7546: 00         NOP
7547: E3                              
7548: 4A         LD           C,D
7549: 17         RLA
754A: 4B         LD           C,E
754B: 51         LD           D,C
754C: 75         LD           (HL),L
754D: 59         LD           E,C
754E: 75         LD           (HL),L
754F: 00         NOP
7550: 00         NOP
7551: 5F         LD           E,A
7552: 75         LD           (HL),L
7553: 7D         LD           A,L
7554: 75         LD           (HL),L
7555: FF         RST         0X38
7556: FF         RST         0X38
7557: BB         CP           E
7558: 78         LD           A,B
7559: 78         LD           A,B
755A: 75         LD           (HL),L
755B: FF         RST         0X38
755C: FF         RST         0X38
755D: BB         CP           E
755E: 78         LD           A,B
755F: 9D         SBC         L
7560: 20 00      JR           NZ,$7562
7562: 80         ADD         A,B
7563: A2         AND         D
7564: 01 A9 01   LD           BC,$01A9
7567: 00         NOP
7568: 88         ADC         A,B
7569: 88         ADC         A,B
756A: 88         ADC         A,B
756B: 84         ADD         A,H
756C: 00         NOP
756D: 00         NOP
756E: 00         NOP
756F: 00         NOP
7570: 88         ADC         A,B
7571: 88         ADC         A,B
7572: 88         ADC         A,B
7573: 84         ADD         A,H
7574: 00         NOP
7575: 00         NOP
7576: 00         NOP
7577: 00         NOP
7578: 9D         SBC         L
7579: 68         LD           L,B
757A: 75         LD           (HL),L
757B: 00         NOP
757C: 94         SUB         H
757D: A2         AND         D
757E: 48         LD           C,B
757F: 4C         LD           C,H
7580: A8         XOR         B
7581: 4E         LD           C,(HL)
7582: A2         AND         D
7583: 48         LD           C,B
7584: 4C         LD           C,H
7585: A3         AND         E
7586: 4E         LD           C,(HL)
7587: 4C         LD           C,H
7588: 48         LD           C,B
7589: A0         AND         B
758A: 01 A3 3E   LD           BC,$3EA3
758D: A1         AND         C
758E: 01 A5 56   LD           BC,$56A5
7591: 00         NOP
7592: 00         NOP
7593: D4 4A 17   CALL       NC,$174A
7596: 4B         LD           C,E
7597: 9D         SBC         L
7598: 75         LD           (HL),L
7599: 17         RLA
759A: 4B         LD           C,E
759B: AD         XOR         L
759C: 75         LD           (HL),L
759D: B5         OR           L
759E: 75         LD           (HL),L
759F: B5         OR           L
75A0: 75         LD           (HL),L
75A1: CB 75      BIT         1,E
75A3: B5         OR           L
75A4: 75         LD           (HL),L
75A5: B5         OR           L
75A6: 75         LD           (HL),L
75A7: CB 75      BIT         1,E
75A9: FF         RST         0X38
75AA: FF         RST         0X38
75AB: BB         CP           E
75AC: 78         LD           A,B
75AD: E2         LDFF00   (C),A
75AE: 75         LD           (HL),L
75AF: E2         LDFF00   (C),A
75B0: 75         LD           (HL),L
75B1: FA 75 00   LD           A,($0075)
75B4: 00         NOP
75B5: 9D         SBC         L
75B6: A1         AND         C
75B7: 00         NOP
75B8: 80         ADD         A,B
75B9: 97         SUB         A
75BA: A2         AND         D
75BB: 36 9D      LD           (HL),$9D
75BD: 61         LD           H,C
75BE: 00         NOP
75BF: 80         ADD         A,B
75C0: A9         XOR         C
75C1: 2C         INC         L
75C2: AD         XOR         L
75C3: 01 A9 2C   LD           BC,$2CA9
75C6: AD         XOR         L
75C7: 01 A9 2C   LD           BC,$2CA9
75CA: 00         NOP
75CB: A1         AND         C
75CC: 2C         INC         L
75CD: 9D         SBC         L
75CE: A1         AND         C
75CF: 00         NOP
75D0: 80         ADD         A,B
75D1: A1         AND         C
75D2: 36 9D      LD           (HL),$9D
75D4: 61         LD           H,C
75D5: 00         NOP
75D6: 80         ADD         A,B
75D7: A1         AND         C
75D8: 2C         INC         L
75D9: 2C         INC         L
75DA: 9D         SBC         L
75DB: A1         AND         C
75DC: 00         NOP
75DD: 80         ADD         A,B
75DE: A2         AND         D
75DF: 36 36      LD           (HL),$36
75E1: 00         NOP
75E2: 9B         SBC         E
75E3: 02         LD           (BC),A
75E4: A2         AND         D
75E5: FF         RST         0X38
75E6: A9         XOR         C
75E7: 15         DEC         D
75E8: AD         XOR         L
75E9: 01 A9 15   LD           BC,$15A9
75EC: AD         XOR         L
75ED: 01 A9 15   LD           BC,$15A9
75F0: 9C         SBC         H
75F1: A1         AND         C
75F2: 15         DEC         D
75F3: FF         RST         0X38
75F4: 15         DEC         D
75F5: 15         DEC         D
75F6: A2         AND         D
75F7: FF         RST         0X38
75F8: FF         RST         0X38
75F9: 00         NOP
75FA: 9B         SBC         E
75FB: 20 AE      JR           NZ,$75AB
75FD: 01 9C 00   LD           BC,$009C
7600: 00         NOP
7601: D4 4A 0B   CALL       NC,$0B4A
7604: 76         HALT
7605: 17         RLA
7606: 76         HALT
7607: 21 76 00   LD           HL,$0076
760A: 00         NOP
760B: 27         DAA
760C: 76         HALT
760D: 34         INC         (HL)
760E: 76         HALT
760F: 4A         LD           C,D
7610: 76         HALT
7611: 5D         LD           E,L
7612: 76         HALT
7613: FF         RST         0X38
7614: FF         RST         0X38
7615: 0D         DEC         C
7616: 76         HALT
7617: 30 76      JR           NC,$768F
7619: 4A         LD           C,D
761A: 76         HALT
761B: 5D         LD           E,L
761C: 76         HALT
761D: FF         RST         0X38
761E: FF         RST         0X38
761F: 17         RLA
7620: 76         HALT
7621: 8A         ADC         A,D
7622: 76         HALT
7623: FF         RST         0X38
7624: FF         RST         0X38
7625: 0D         DEC         C
7626: 76         HALT
7627: 9D         SBC         L
7628: 20 00      JR           NZ,$762A
762A: 80         ADD         A,B
762B: A1         AND         C
762C: 01 A9 01   LD           BC,$01A9
762F: 00         NOP
7630: 9D         SBC         L
7631: 60         LD           H,B
7632: 21 80 A2   LD           HL,$A280
7635: 01 60 64   LD           BC,$6460
7638: A8         XOR         B
7639: 66         LD           H,(HL)
763A: A2         AND         D
763B: 60         LD           H,B
763C: 64         LD           H,H
763D: A8         XOR         B
763E: 66         LD           H,(HL)
763F: A2         AND         D
7640: 64         LD           H,H
7641: 60         LD           H,B
7642: 56         LD           D,(HL)
7643: A7         AND         A
7644: 5C         LD           E,H
7645: A5         AND         L
7646: 60         LD           H,B
7647: A3         AND         E
7648: 01 00 A2   LD           BC,$A200
764B: 60         LD           H,B
764C: 64         LD           H,H
764D: A8         XOR         B
764E: 66         LD           H,(HL)
764F: A2         AND         D
7650: 5C         LD           E,H
7651: 66         LD           H,(HL)
7652: A8         XOR         B
7653: 70         LD           (HL),B
7654: A2         AND         D
7655: 6E         LD           L,(HL)
7656: 6A         LD           L,D
7657: A5         AND         L
7658: 6E         LD           L,(HL)
7659: 01 A7 01   LD           BC,$01A7
765C: 00         NOP
765D: A3         AND         E
765E: 7C         LD           A,H
765F: 78         LD           A,B
7660: 6E         LD           L,(HL)
7661: A7         AND         A
7662: 6E         LD           L,(HL)
7663: A5         AND         L
7664: 70         LD           (HL),B
7665: A2         AND         D
7666: 82         ADD         A,D
7667: 7E         LD           A,(HL)
7668: 7C         LD           A,H
7669: 78         LD           A,B
766A: 6E         LD           L,(HL)
766B: 6A         LD           L,D
766C: 6E         LD           L,(HL)
766D: 78         LD           A,B
766E: A7         AND         A
766F: 70         LD           (HL),B
7670: A2         AND         D
7671: 70         LD           (HL),B
7672: A4         AND         H
7673: 74         LD           (HL),H
7674: A2         AND         D
7675: 01 62 6A   LD           BC,$6A62
7678: 74         LD           (HL),H
7679: A8         XOR         B
767A: 6E         LD           L,(HL)
767B: A2         AND         D
767C: 01 66 A5   LD           BC,$A566
767F: 78         LD           A,B
7680: A2         AND         D
7681: 01 A7 76   LD           BC,$76A7
7684: 88         ADC         A,B
7685: 86         ADD         A,(HL)
7686: 01 A5 01   LD           BC,$01A5
7689: 00         NOP
768A: 9D         SBC         L
768B: 68         LD           L,B
768C: 6D         LD           L,L
768D: 60         LD           H,B
768E: A3         AND         E
768F: 01 A1 01   LD           BC,$01A1
7692: 00         NOP
7693: 00         NOP
7694: D4 4A 9E   CALL       NC,$9E4A
7697: 76         HALT
7698: AE         XOR         (HL)
7699: 76         HALT
769A: B8         CP           B
769B: 76         HALT
769C: 00         NOP
769D: 00         NOP
769E: BE         CP           (HL)
769F: 76         HALT
76A0: 14         INC         D
76A1: 71         LD           (HL),C
76A2: 14         INC         D
76A3: 71         LD           (HL),C
76A4: 23         INC         HL
76A5: 71         LD           (HL),C
76A6: 23         INC         HL
76A7: 71         LD           (HL),C
76A8: 33         INC         SP
76A9: 71         LD           (HL),C
76AA: FF         RST         0X38
76AB: FF         RST         0X38
76AC: A0         AND         B
76AD: 76         HALT
76AE: 30 76      JR           NC,$7726
76B0: C7         RST         0X00
76B1: 76         HALT
76B2: 5D         LD           E,L
76B3: 76         HALT
76B4: FF         RST         0X38
76B5: FF         RST         0X38
76B6: AE         XOR         (HL)
76B7: 76         HALT
76B8: EB                              
76B9: 76         HALT
76BA: FF         RST         0X38
76BB: FF         RST         0X38
76BC: B8         CP           B
76BD: 76         HALT
76BE: 9D         SBC         L
76BF: 19         ADD         HL,DE
76C0: 42         LD           B,D
76C1: 40         LD           B,B
76C2: A7         AND         A
76C3: 01 A2 01   LD           BC,$01A2
76C6: 00         NOP
76C7: A2         AND         D
76C8: 30 34      JR           NC,$76FE
76CA: A8         XOR         B
76CB: 36 A2      LD           (HL),$A2
76CD: 2C         INC         L
76CE: 36 A8      LD           (HL),$A8
76D0: 40         LD           B,B
76D1: A2         AND         D
76D2: 3E 3A      LD           A,$3A
76D4: AE         XOR         (HL)
76D5: 3E A4      LD           A,$A4
76D7: 01 A7 01   LD           BC,$01A7
76DA: 00         NOP
76DB: 01 37 9A   LD           BC,$9A37
76DE: BB         CP           E
76DF: BB         CP           E
76E0: BB         CP           E
76E1: A6         AND         (HL)
76E2: 21 01 37   LD           HL,$3701
76E5: 9A         SBC         D
76E6: BB         CP           E
76E7: BB         CP           E
76E8: BB         CP           E
76E9: A6         AND         (HL)
76EA: 21 9D DB   LD           HL,$DB9D
76ED: 76         HALT
76EE: 40         LD           B,B
76EF: 9B         SBC         E
76F0: 08 A5 01   LD           ($01A5),SP
76F3: 9C         SBC         H
76F4: A8         XOR         B
76F5: 01 A3 6A   LD           BC,$6AA3
76F8: 66         LD           H,(HL)
76F9: A6         AND         (HL)
76FA: 5C         LD           E,H
76FB: A1         AND         C
76FC: 01 A7 5C   LD           BC,$5CA7
76FF: A8         XOR         B
7700: 60         LD           H,B
7701: A3         AND         E
7702: 01 A1 70   LD           BC,$70A1
7705: 01 6E 01   LD           BC,$016E
7708: 6A         LD           L,D
7709: 01 66 01   LD           BC,$0166
770C: 5C         LD           E,H
770D: 01 58 01   LD           BC,$0158
7710: 5C         LD           E,H
7711: 01 66 01   LD           BC,$0166
7714: A6         AND         (HL)
7715: 60         LD           H,B
7716: 01 A2 60   LD           BC,$60A2
7719: A7         AND         A
771A: 62         LD           H,D
771B: A3         AND         E
771C: 01 A1 52   LD           BC,$52A1
771F: 01 58 01   LD           BC,$0158
7722: 62         LD           H,D
7723: 01 A4 5C   LD           BC,$5CA4
7726: A7         AND         A
7727: 01 A2 56   LD           BC,$56A2
772A: A8         XOR         B
772B: 66         LD           H,(HL)
772C: A7         AND         A
772D: 01 A3 64   LD           BC,$64A3
7730: A2         AND         D
7731: 01 A3 5E   LD           BC,$5EA3
7734: A2         AND         D
7735: 01 A3 5C   LD           BC,$5CA3
7738: A4         AND         H
7739: 01 A5 01   LD           BC,$01A5
773C: 00         NOP
773D: 00         NOP
773E: 01 4B 48   LD           BC,$484B
7741: 77         LD           (HL),A
7742: 4C         LD           C,H
7743: 77         LD           (HL),A
7744: 50         LD           D,B
7745: 77         LD           (HL),A
7746: 54         LD           D,H
7747: 77         LD           (HL),A
7748: 58         LD           E,B
7749: 77         LD           (HL),A
774A: 00         NOP
774B: 00         NOP
774C: A3         AND         E
774D: 77         LD           (HL),A
774E: 00         NOP
774F: 00         NOP
7750: 27         DAA
7751: 78         LD           A,B
7752: 00         NOP
7753: 00         NOP
7754: 8C         ADC         A,H
7755: 78         LD           A,B
7756: 00         NOP
7757: 00         NOP
7758: 9D         SBC         L
7759: 62         LD           H,D
775A: 00         NOP
775B: 00         NOP
775C: A1         AND         C
775D: 1E 22      LD           E,$22
775F: 24         INC         H
7760: A6         AND         (HL)
7761: 26 A1      LD           H,$A1
7763: 26 28      LD           H,$28
7765: 2A         LD           A,(HLI)
7766: A6         AND         (HL)
7767: 2C         INC         L
7768: A1         AND         C
7769: 2C         INC         L
776A: 30 32      JR           NC,$779E
776C: 34         INC         (HL)
776D: A3         AND         E
776E: 36 97      LD           (HL),$97
7770: 3C         INC         A
7771: 98         SBC         B
7772: 9D         SBC         L
7773: 41         LD           B,C
7774: 00         NOP
7775: 80         ADD         A,B
7776: 9B         SBC         E
7777: 06 A2      LD           B,$A2
7779: 78         LD           A,B
777A: A1         AND         C
777B: 7E         LD           A,(HL)
777C: A2         AND         D
777D: 74         LD           (HL),H
777E: 7E         LD           A,(HL)
777F: 78         LD           A,B
7780: 7E         LD           A,(HL)
7781: A1         AND         C
7782: 78         LD           A,B
7783: A2         AND         D
7784: 74         LD           (HL),H
7785: 7E         LD           A,(HL)
7786: 9C         SBC         H
7787: 9D         SBC         L
7788: 61         LD           H,C
7789: 00         NOP
778A: 40         LD           B,B
778B: A6         AND         (HL)
778C: 70         LD           (HL),B
778D: A1         AND         C
778E: 70         LD           (HL),B
778F: 6C         LD           L,H
7790: A2         AND         D
7791: 74         LD           (HL),H
7792: 70         LD           (HL),B
7793: 70         LD           (HL),B
7794: A1         AND         C
7795: 70         LD           (HL),B
7796: A2         AND         D
7797: 6C         LD           L,H
7798: 74         LD           (HL),H
7799: 88         ADC         A,B
779A: 88         ADC         A,B
779B: 84         ADD         A,H
779C: A7         AND         A
779D: 88         ADC         A,B
779E: 97         SUB         A
779F: A3         AND         E
77A0: 2C         INC         L
77A1: 98         SBC         B
77A2: 00         NOP
77A3: 9D         SBC         L
77A4: 81         ADD         A,C
77A5: 00         NOP
77A6: 40         LD           B,B
77A7: A1         AND         C
77A8: 3E 40      LD           A,$40
77AA: 42         LD           B,D
77AB: A6         AND         (HL)
77AC: 44         LD           B,H
77AD: A1         AND         C
77AE: 44         LD           B,H
77AF: 46         LD           B,(HL)
77B0: 48         LD           C,B
77B1: A6         AND         (HL)
77B2: 4A         LD           C,D
77B3: A1         AND         C
77B4: 4A         LD           C,D
77B5: 4E         LD           C,(HL)
77B6: 52         LD           D,D
77B7: 54         LD           D,H
77B8: A4         AND         H
77B9: 56         LD           D,(HL)
77BA: AE         XOR         (HL)
77BB: 01 97 A1   LD           BC,$A197
77BE: 01 A2 4A   LD           BC,$4AA2
77C1: A1         AND         C
77C2: 4A         LD           C,D
77C3: A2         AND         D
77C4: 40         LD           B,B
77C5: A1         AND         C
77C6: 30 30      JR           NC,$77F8
77C8: 98         SBC         B
77C9: A6         AND         (HL)
77CA: 30 A1      JR           NC,$776D
77CC: 30 2C      JR           NC,$77FA
77CE: A2         AND         D
77CF: 32         LD           (HLD),A
77D0: 30 30      JR           NC,$7802
77D2: A1         AND         C
77D3: 30 A2      JR           NC,$7777
77D5: 2C         INC         L
77D6: 32         LD           (HLD),A
77D7: A6         AND         (HL)
77D8: 30 A1      JR           NC,$777B
77DA: 30 2C      JR           NC,$7808
77DC: A2         AND         D
77DD: 32         LD           (HLD),A
77DE: A2         AND         D
77DF: 30 97      JR           NC,$7778
77E1: 4A         LD           C,D
77E2: A1         AND         C
77E3: 4A         LD           C,D
77E4: A2         AND         D
77E5: 40         LD           B,B
77E6: A1         AND         C
77E7: 30 30      JR           NC,$7819
77E9: 98         SBC         B
77EA: A6         AND         (HL)
77EB: 36 A1      LD           (HL),$A1
77ED: 36 32      LD           (HL),$32
77EF: A2         AND         D
77F0: 3A         LD           A,(HLD)
77F1: 36 36      LD           (HL),$36
77F3: A1         AND         C
77F4: 36 A2      LD           (HL),$A2
77F6: 32         LD           (HLD),A
77F7: 3A         LD           A,(HLD)
77F8: A6         AND         (HL)
77F9: 36 A1      LD           (HL),$A1
77FB: 36 32      LD           (HL),$32
77FD: A2         AND         D
77FE: 3A         LD           A,(HLD)
77FF: A2         AND         D
7800: 36 97      LD           (HL),$97
7802: 4A         LD           C,D
7803: A1         AND         C
7804: 4A         LD           C,D
7805: A2         AND         D
7806: 40         LD           B,B
7807: A1         AND         C
7808: 30 30      JR           NC,$783A
780A: 98         SBC         B
780B: A6         AND         (HL)
780C: 10 A1      STOP       $A1
780E: 10 0C      STOP       $0C
7810: A2         AND         D
7811: 14         INC         D
7812: 10 10      STOP       $10
7814: A1         AND         C
7815: 10 A2      STOP       $A2
7817: 0C         INC         C
7818: 14         INC         D
7819: 10 10      STOP       $10
781B: 0C         INC         C
781C: A7         AND         A
781D: 10 9D      STOP       $9D
781F: A1         AND         C
7820: 00         NOP
7821: 80         ADD         A,B
7822: 97         SUB         A
7823: A3         AND         E
7824: 3C         INC         A
7825: 98         SBC         B
7826: 00         NOP
7827: 9D         SBC         L
7828: 0F         RRCA
7829: 73         LD           (HL),E
782A: 20 99      JR           NZ,$77C5
782C: A1         AND         C
782D: 4E         LD           C,(HL)
782E: 52         LD           D,D
782F: 54         LD           D,H
7830: A6         AND         (HL)
7831: 56         LD           D,(HL)
7832: A1         AND         C
7833: 56         LD           D,(HL)
7834: 58         LD           E,B
7835: 5A         LD           E,D
7836: A6         AND         (HL)
7837: 5C         LD           E,H
7838: A1         AND         C
7839: 5C         LD           E,H
783A: 60         LD           H,B
783B: 62         LD           H,D
783C: 64         LD           H,H
783D: A4         AND         H
783E: 66         LD           H,(HL)
783F: 9B         SBC         E
7840: 02         LD           (BC),A
7841: A6         AND         (HL)
7842: 28 A1      JR           Z,$77E5
7844: 28 24      JR           Z,$786A
7846: A2         AND         D
7847: 2C         INC         L
7848: 28 28      JR           Z,$7872
784A: A1         AND         C
784B: 28 A2      JR           Z,$77EF
784D: 24         INC         H
784E: 2C         INC         L
784F: A6         AND         (HL)
7850: 28 A1      JR           Z,$77F3
7852: 28 24      JR           Z,$7878
7854: A2         AND         D
7855: 2C         INC         L
7856: 28 A6      JR           Z,$77FE
7858: 01 A3 01   LD           BC,$01A3
785B: 9C         SBC         H
785C: A6         AND         (HL)
785D: 30 A1      JR           NC,$7800
785F: 30 2C      JR           NC,$788D
7861: A2         AND         D
7862: 32         LD           (HLD),A
7863: 30 30      JR           NC,$7895
7865: A1         AND         C
7866: 30 A2      JR           NC,$780A
7868: 2C         INC         L
7869: 32         LD           (HLD),A
786A: A6         AND         (HL)
786B: 30 A1      JR           NC,$780E
786D: 30 2C      JR           NC,$789B
786F: A2         AND         D
7870: 32         LD           (HLD),A
7871: 30 A6      JR           NC,$7819
7873: 01 A3 01   LD           BC,$01A3
7876: A6         AND         (HL)
7877: 40         LD           B,B
7878: A1         AND         C
7879: 40         LD           B,B
787A: 3C         INC         A
787B: A2         AND         D
787C: 44         LD           B,H
787D: 40         LD           B,B
787E: 40         LD           B,B
787F: A1         AND         C
7880: 40         LD           B,B
7881: A2         AND         D
7882: 3C         INC         A
7883: 44         LD           B,H
7884: 40         LD           B,B
7885: 40         LD           B,B
7886: 3C         INC         A
7887: A7         AND         A
7888: 40         LD           B,B
7889: A3         AND         E
788A: 01 00 A5   LD           BC,$A500
788D: 01 A3 01   LD           BC,$01A3
7890: FF         RST         0X38
7891: 9B         SBC         E
7892: 06 A1      LD           B,$A1
7894: 1A         LD           A,(DE)
7895: 15         DEC         D
7896: 15         DEC         D
7897: 1A         LD           A,(DE)
7898: 15         DEC         D
7899: 15         DEC         D
789A: FF         RST         0X38
789B: 1A         LD           A,(DE)
789C: 1A         LD           A,(DE)
789D: 15         DEC         D
789E: 15         DEC         D
789F: 1A         LD           A,(DE)
78A0: 15         DEC         D
78A1: 15         DEC         D
78A2: FF         RST         0X38
78A3: FF         RST         0X38
78A4: 9C         SBC         H
78A5: A6         AND         (HL)
78A6: FF         RST         0X38
78A7: A1         AND         C
78A8: FF         RST         0X38
78A9: FF         RST         0X38
78AA: A2         AND         D
78AB: FF         RST         0X38
78AC: FF         RST         0X38
78AD: FF         RST         0X38
78AE: A1         AND         C
78AF: FF         RST         0X38
78B0: A2         AND         D
78B1: FF         RST         0X38
78B2: FF         RST         0X38
78B3: FF         RST         0X38
78B4: FF         RST         0X38
78B5: FF         RST         0X38
78B6: A7         AND         A
78B7: FF         RST         0X38
78B8: A3         AND         E
78B9: FF         RST         0X38
78BA: 00         NOP
78BB: C1         POP         BC
78BC: 78         LD           A,B
78BD: FF         RST         0X38
78BE: FF         RST         0X38
78BF: BB         CP           E
78C0: 78         LD           A,B
78C1: 9B         SBC         E
78C2: 20 AE      JR           NZ,$7872
78C4: 01 9C 00   LD           BC,$009C
78C7: CD 78 FF   CALL       $FF78
78CA: FF         RST         0X38
78CB: C7         RST         0X00
78CC: 78         LD           A,B
78CD: 9B         SBC         E
78CE: 20 AE      JR           NZ,$787E
78D0: 01 9C 00   LD           BC,$009C
78D3: 00         NOP
78D4: D4 4A DE   CALL       NC,$DE4A
78D7: 78         LD           A,B
78D8: E4                              
78D9: 78         LD           A,B
78DA: EA 78 00   LD           ($0078),A
78DD: 00         NOP
78DE: F2                              
78DF: 78         LD           A,B
78E0: FF         RST         0X38
78E1: FF         RST         0X38
78E2: DE 78      SBC         $78
78E4: 60         LD           H,B
78E5: 79         LD           A,C
78E6: FF         RST         0X38
78E7: FF         RST         0X38
78E8: E4                              
78E9: 78         LD           A,B
78EA: B7         OR           A
78EB: 79         LD           A,C
78EC: BE         CP           (HL)
78ED: 79         LD           A,C
78EE: FF         RST         0X38
78EF: FF         RST         0X38
78F0: EC                              
78F1: 78         LD           A,B
78F2: 9D         SBC         L
78F3: 42         LD           B,D
78F4: 82         ADD         A,D
78F5: 80         ADD         A,B
78F6: 9B         SBC         E
78F7: 02         LD           (BC),A
78F8: A2         AND         D
78F9: 40         LD           B,B
78FA: 4E         LD           C,(HL)
78FB: 5C         LD           E,H
78FC: 60         LD           H,B
78FD: A4         AND         H
78FE: 01 A2 40   LD           BC,$40A2
7901: 52         LD           D,D
7902: 60         LD           H,B
7903: 62         LD           H,D
7904: A4         AND         H
7905: 01 9C A2   LD           BC,$A29C
7908: 40         LD           B,B
7909: 4E         LD           C,(HL)
790A: 5C         LD           E,H
790B: 60         LD           H,B
790C: A4         AND         H
790D: 01 A2 40   LD           BC,$40A2
7910: 4C         LD           C,H
7911: 5C         LD           E,H
7912: 5E         LD           E,(HL)
7913: A4         AND         H
7914: 01 A2 44   LD           BC,$44A2
7917: 52         LD           D,D
7918: 60         LD           H,B
7919: 62         LD           H,D
791A: A4         AND         H
791B: 01 A2 42   LD           BC,$42A2
791E: 48         LD           C,B
791F: 4E         LD           C,(HL)
7920: 54         LD           D,H
7921: 52         LD           D,D
7922: A7         AND         A
7923: 01 A2 44   LD           BC,$44A2
7926: 4C         LD           C,H
7927: 52         LD           D,D
7928: 58         LD           E,B
7929: A4         AND         H
792A: 01 A2 4A   LD           BC,$4AA2
792D: 50         LD           D,B
792E: 56         LD           D,(HL)
792F: 5C         LD           E,H
7930: A4         AND         H
7931: 01 A2 48   LD           BC,$48A2
7934: 4E         LD           C,(HL)
7935: 56         LD           D,(HL)
7936: 5C         LD           E,H
7937: A4         AND         H
7938: 01 A2 48   LD           BC,$48A2
793B: 4E         LD           C,(HL)
793C: 56         LD           D,(HL)
793D: 58         LD           E,B
793E: A4         AND         H
793F: 01 A2 44   LD           BC,$44A2
7942: 4A         LD           C,D
7943: 52         LD           D,D
7944: 58         LD           E,B
7945: A4         AND         H
7946: 01 A2 44   LD           BC,$44A2
7949: 4C         LD           C,H
794A: 52         LD           D,D
794B: 58         LD           E,B
794C: A4         AND         H
794D: 01 A2 48   LD           BC,$48A2
7950: 4E         LD           C,(HL)
7951: 56         LD           D,(HL)
7952: 4E         LD           C,(HL)
7953: 46         LD           B,(HL)
7954: 4C         LD           C,H
7955: 52         LD           D,D
7956: 4C         LD           C,H
7957: 44         LD           B,H
7958: 4A         LD           C,D
7959: 52         LD           D,D
795A: 4A         LD           C,D
795B: 44         LD           B,H
795C: 4A         LD           C,D
795D: 50         LD           D,B
795E: 4A         LD           C,D
795F: 00         NOP
7960: 9D         SBC         L
7961: 50         LD           D,B
7962: 44         LD           B,H
7963: 80         ADD         A,B
7964: 9B         SBC         E
7965: 02         LD           (BC),A
7966: A4         AND         H
7967: 66         LD           H,(HL)
7968: 58         LD           E,B
7969: 5C         LD           E,H
796A: A3         AND         E
796B: 01 A2 60   LD           BC,$60A2
796E: 62         LD           H,D
796F: 9C         SBC         H
7970: A3         AND         E
7971: 60         LD           H,B
7972: 66         LD           H,(HL)
7973: A4         AND         H
7974: 74         LD           (HL),H
7975: A3         AND         E
7976: 01 70 74   LD           BC,$7470
7979: 70         LD           (HL),B
797A: 66         LD           H,(HL)
797B: A2         AND         D
797C: 62         LD           H,D
797D: 60         LD           H,B
797E: A4         AND         H
797F: 5C         LD           E,H
7980: 01 A2 01   LD           BC,$01A2
7983: 60         LD           H,B
7984: 62         LD           H,D
7985: 66         LD           H,(HL)
7986: A4         AND         H
7987: 6A         LD           L,D
7988: 58         LD           E,B
7989: 56         LD           D,(HL)
798A: A3         AND         E
798B: 01 A2 5C   LD           BC,$5CA2
798E: 6A         LD           L,D
798F: A4         AND         H
7990: 66         LD           H,(HL)
7991: 56         LD           D,(HL)
7992: 58         LD           E,B
7993: A3         AND         E
7994: 01 A2 58   LD           BC,$58A2
7997: 56         LD           D,(HL)
7998: A3         AND         E
7999: 52         LD           D,D
799A: 58         LD           E,B
799B: A4         AND         H
799C: 60         LD           H,B
799D: A3         AND         E
799E: 01 5C 58   LD           BC,$585C
79A1: 50         LD           D,B
79A2: A4         AND         H
79A3: 4E         LD           C,(HL)
79A4: AE         XOR         (HL)
79A5: 01 00 11   LD           BC,$1100
79A8: 11 11 10   LD           DE,$1011
79AB: 00         NOP
79AC: 00         NOP
79AD: 00         NOP
79AE: 00         NOP
79AF: 11 11 11   LD           DE,$1111
79B2: 10 00      STOP       $00
79B4: 00         NOP
79B5: 00         NOP
79B6: 00         NOP
79B7: 9D         SBC         L
79B8: A7         AND         A
79B9: 79         LD           A,C
79BA: 20 A2      JR           NZ,$795E
79BC: 01 00 9B   LD           BC,$9B00
79BF: 02         LD           (BC),A
79C0: A4         AND         H
79C1: 66         LD           H,(HL)
79C2: 58         LD           E,B
79C3: 5C         LD           E,H
79C4: A3         AND         E
79C5: 01 A2 60   LD           BC,$60A2
79C8: 62         LD           H,D
79C9: 9C         SBC         H
79CA: A3         AND         E
79CB: 60         LD           H,B
79CC: 66         LD           H,(HL)
79CD: A7         AND         A
79CE: 74         LD           (HL),H
79CF: 01 A3 70   LD           BC,$70A3
79D2: 74         LD           (HL),H
79D3: 70         LD           (HL),B
79D4: 66         LD           H,(HL)
79D5: A2         AND         D
79D6: 62         LD           H,D
79D7: 60         LD           H,B
79D8: A7         AND         A
79D9: 5C         LD           E,H
79DA: A4         AND         H
79DB: 01 A2 01   LD           BC,$01A2
79DE: 01 60 62   LD           BC,$6260
79E1: 66         LD           H,(HL)
79E2: A4         AND         H
79E3: 6A         LD           L,D
79E4: 58         LD           E,B
79E5: A7         AND         A
79E6: 56         LD           D,(HL)
79E7: 01 A2 5C   LD           BC,$5CA2
79EA: 6A         LD           L,D
79EB: A4         AND         H
79EC: 66         LD           H,(HL)
79ED: 56         LD           D,(HL)
79EE: A7         AND         A
79EF: 58         LD           E,B
79F0: 01 A2 58   LD           BC,$58A2
79F3: 56         LD           D,(HL)
79F4: A3         AND         E
79F5: 52         LD           D,D
79F6: 58         LD           E,B
79F7: A7         AND         A
79F8: 60         LD           H,B
79F9: 01 A3 5C   LD           BC,$5CA3
79FC: 58         LD           E,B
79FD: 50         LD           D,B
79FE: A7         AND         A
79FF: 4E         LD           C,(HL)
7A00: A2         AND         D
7A01: 01 AE 01   LD           BC,$01AE
7A04: 00         NOP
7A05: 00         NOP
7A06: C5         PUSH       BC
7A07: 4A         LD           C,D
7A08: 10 7A      STOP       $7A
7A0A: 24         INC         H
7A0B: 7A         LD           A,D
7A0C: 2A         LD           A,(HLI)
7A0D: 7A         LD           A,D
7A0E: 00         NOP
7A0F: 00         NOP
7A10: 3E 7A      LD           A,$7A
7A12: 32         LD           (HLD),A
7A13: 7A         LD           A,D
7A14: 43         LD           B,E
7A15: 7A         LD           A,D
7A16: 32         LD           (HLD),A
7A17: 7A         LD           A,D
7A18: 48         LD           C,B
7A19: 7A         LD           A,D
7A1A: 32         LD           (HLD),A
7A1B: 7A         LD           A,D
7A1C: 43         LD           B,E
7A1D: 7A         LD           A,D
7A1E: 32         LD           (HLD),A
7A1F: 7A         LD           A,D
7A20: FF         RST         0X38
7A21: FF         RST         0X38
7A22: 10 7A      STOP       $7A
7A24: 4D         LD           C,L
7A25: 7A         LD           A,D
7A26: FF         RST         0X38
7A27: FF         RST         0X38
7A28: 24         INC         H
7A29: 7A         LD           A,D
7A2A: B7         OR           A
7A2B: 79         LD           A,C
7A2C: 51         LD           D,C
7A2D: 7A         LD           A,D
7A2E: FF         RST         0X38
7A2F: FF         RST         0X38
7A30: 2C         INC         L
7A31: 7A         LD           A,D
7A32: 9B         SBC         E
7A33: 02         LD           (BC),A
7A34: AC         XOR         H
7A35: 7C         LD           A,H
7A36: 7E         LD           A,(HL)
7A37: 9C         SBC         H
7A38: 9B         SBC         E
7A39: 02         LD           (BC),A
7A3A: 82         ADD         A,D
7A3B: 84         ADD         A,H
7A3C: 9C         SBC         H
7A3D: 00         NOP
7A3E: 9D         SBC         L
7A3F: 10 00      STOP       $00
7A41: 00         NOP
7A42: 00         NOP
7A43: 9D         SBC         L
7A44: 20 00      JR           NZ,$7A46
7A46: 00         NOP
7A47: 00         NOP
7A48: 9D         SBC         L
7A49: 30 00      JR           NC,$7A4B
7A4B: 00         NOP
7A4C: 00         NOP
7A4D: 9D         SBC         L
7A4E: 1A         LD           A,(DE)
7A4F: 81         ADD         A,C
7A50: 40         LD           B,B
7A51: 9B         SBC         E
7A52: 20 A2      JR           NZ,$79F6
7A54: 62         LD           H,D
7A55: 6C         LD           L,H
7A56: 76         HALT
7A57: 78         LD           A,B
7A58: 9C         SBC         H
7A59: 00         NOP
7A5A: 00         NOP
7A5B: F2                              
7A5C: 4A         LD           C,D
7A5D: 65         LD           H,L
7A5E: 7A         LD           A,D
7A5F: 71         LD           (HL),C
7A60: 7A         LD           A,D
7A61: 17         RLA
7A62: 4B         LD           C,E
7A63: 00         NOP
7A64: 00         NOP
7A65: 7B         LD           A,E
7A66: 7A         LD           A,D
7A67: 87         ADD         A,A
7A68: 7A         LD           A,D
7A69: 16 7B      LD           D,$7B
7A6B: 1F         RRA
7A6C: 7B         LD           A,E
7A6D: FF         RST         0X38
7A6E: FF         RST         0X38
7A6F: 69         LD           L,C
7A70: 7A         LD           A,D
7A71: 82         ADD         A,D
7A72: 7A         LD           A,D
7A73: 87         ADD         A,A
7A74: 7A         LD           A,D
7A75: 1B         DEC         DE
7A76: 7B         LD           A,E
7A77: FF         RST         0X38
7A78: FF         RST         0X38
7A79: 75         LD           (HL),L
7A7A: 7A         LD           A,D
7A7B: 9D         SBC         L
7A7C: 42         LD           B,D
7A7D: 00         NOP
7A7E: 80         ADD         A,B
7A7F: A1         AND         C
7A80: 01 00 9D   LD           BC,$9D00
7A83: 81         ADD         A,C
7A84: 00         NOP
7A85: 80         ADD         A,B
7A86: 00         NOP
7A87: A5         AND         L
7A88: 01 A2 01   LD           BC,$01A2
7A8B: 97         SUB         A
7A8C: A0         AND         B
7A8D: 2E 30      LD           L,$30
7A8F: 3E 40      LD           A,$40
7A91: 46         LD           B,(HL)
7A92: 40         LD           B,B
7A93: 38 30      JR           C,$7AC5
7A95: 32         LD           (HLD),A
7A96: 34         INC         (HL)
7A97: 3C         INC         A
7A98: 44         LD           B,H
7A99: 4A         LD           C,D
7A9A: 44         LD           B,H
7A9B: 3C         INC         A
7A9C: 34         INC         (HL)
7A9D: 36 38      LD           (HL),$38
7A9F: 40         LD           B,B
7AA0: 48         LD           C,B
7AA1: 4E         LD           C,(HL)
7AA2: 48         LD           C,B
7AA3: 40         LD           B,B
7AA4: 38 3A      JR           C,$7AE0
7AA6: 3C         INC         A
7AA7: 44         LD           B,H
7AA8: 4C         LD           C,H
7AA9: 52         LD           D,D
7AAA: 4C         LD           C,H
7AAB: 44         LD           B,H
7AAC: 3C         INC         A
7AAD: 3E 40      LD           A,$40
7AAF: 48         LD           C,B
7AB0: 50         LD           D,B
7AB1: 56         LD           D,(HL)
7AB2: 50         LD           D,B
7AB3: 48         LD           C,B
7AB4: 40         LD           B,B
7AB5: 42         LD           B,D
7AB6: 44         LD           B,H
7AB7: 4C         LD           C,H
7AB8: 54         LD           D,H
7AB9: 5A         LD           E,D
7ABA: 54         LD           D,H
7ABB: 4C         LD           C,H
7ABC: 44         LD           B,H
7ABD: 46         LD           B,(HL)
7ABE: 48         LD           C,B
7ABF: 50         LD           D,B
7AC0: 58         LD           E,B
7AC1: 5E         LD           E,(HL)
7AC2: 58         LD           E,B
7AC3: 50         LD           D,B
7AC4: 48         LD           C,B
7AC5: 4A         LD           C,D
7AC6: 4C         LD           C,H
7AC7: 54         LD           D,H
7AC8: 5C         LD           E,H
7AC9: 62         LD           H,D
7ACA: 5C         LD           E,H
7ACB: 54         LD           D,H
7ACC: 4C         LD           C,H
7ACD: 4E         LD           C,(HL)
7ACE: 50         LD           D,B
7ACF: 58         LD           E,B
7AD0: 60         LD           H,B
7AD1: 66         LD           H,(HL)
7AD2: 60         LD           H,B
7AD3: 58         LD           E,B
7AD4: 50         LD           D,B
7AD5: 52         LD           D,D
7AD6: 54         LD           D,H
7AD7: 5C         LD           E,H
7AD8: 64         LD           H,H
7AD9: 6A         LD           L,D
7ADA: 64         LD           H,H
7ADB: 5C         LD           E,H
7ADC: 54         LD           D,H
7ADD: 9B         SBC         E
7ADE: 02         LD           (BC),A
7ADF: 56         LD           D,(HL)
7AE0: 58         LD           E,B
7AE1: 60         LD           H,B
7AE2: 68         LD           L,B
7AE3: 6E         LD           L,(HL)
7AE4: 68         LD           L,B
7AE5: 60         LD           H,B
7AE6: 58         LD           E,B
7AE7: 56         LD           D,(HL)
7AE8: 50         LD           D,B
7AE9: 48         LD           C,B
7AEA: 40         LD           B,B
7AEB: 48         LD           C,B
7AEC: 50         LD           D,B
7AED: 9C         SBC         H
7AEE: 56         LD           D,(HL)
7AEF: 58         LD           E,B
7AF0: 60         LD           H,B
7AF1: 68         LD           L,B
7AF2: 6E         LD           L,(HL)
7AF3: 68         LD           L,B
7AF4: 60         LD           H,B
7AF5: 58         LD           E,B
7AF6: 68         LD           L,B
7AF7: 60         LD           H,B
7AF8: 58         LD           E,B
7AF9: 56         LD           D,(HL)
7AFA: 60         LD           H,B
7AFB: 58         LD           E,B
7AFC: 56         LD           D,(HL)
7AFD: 50         LD           D,B
7AFE: 58         LD           E,B
7AFF: 56         LD           D,(HL)
7B00: 50         LD           D,B
7B01: 48         LD           C,B
7B02: 56         LD           D,(HL)
7B03: 50         LD           D,B
7B04: 48         LD           C,B
7B05: 40         LD           B,B
7B06: 50         LD           D,B
7B07: 48         LD           C,B
7B08: 40         LD           B,B
7B09: 38 48      JR           C,$7B53
7B0B: 40         LD           B,B
7B0C: 3E 38      LD           A,$38
7B0E: 40         LD           B,B
7B0F: 3E 38      LD           A,$38
7B11: 30 A5      JR           NC,$7AB8
7B13: 28 98      JR           Z,$7AAD
7B15: 00         NOP
7B16: 9D         SBC         L
7B17: 10 00      STOP       $00
7B19: 80         ADD         A,B
7B1A: 00         NOP
7B1B: 9D         SBC         L
7B1C: 1A         LD           A,(DE)
7B1D: 81         ADD         A,C
7B1E: 40         LD           B,B
7B1F: 9B         SBC         E
7B20: 20 AA      JR           NZ,$7ACC
7B22: 62         LD           H,D
7B23: 6C         LD           L,H
7B24: 76         HALT
7B25: 78         LD           A,B
7B26: 9C         SBC         H
7B27: 00         NOP
7B28: 0E B6      LD           C,$B6
7B2A: 4A         LD           C,D
7B2B: 33         INC         SP
7B2C: 7B         LD           A,E
7B2D: 39         ADD         HL,SP
7B2E: 7B         LD           A,E
7B2F: 3F         CCF
7B30: 7B         LD           A,E
7B31: 00         NOP
7B32: 00         NOP
7B33: 45         LD           B,L
7B34: 7B         LD           A,E
7B35: FF         RST         0X38
7B36: FF         RST         0X38
7B37: 33         INC         SP
7B38: 7B         LD           A,E
7B39: 61         LD           H,C
7B3A: 7B         LD           A,E
7B3B: FF         RST         0X38
7B3C: FF         RST         0X38
7B3D: 39         ADD         HL,SP
7B3E: 7B         LD           A,E
7B3F: 90         SUB         B
7B40: 7B         LD           A,E
7B41: FF         RST         0X38
7B42: FF         RST         0X38
7B43: 3F         CCF
7B44: 7B         LD           A,E
7B45: 9D         SBC         L
7B46: 62         LD           H,D
7B47: 00         NOP
7B48: 40         LD           B,B
7B49: 9B         SBC         E
7B4A: 20 A3      JR           NZ,$7AEF
7B4C: 32         LD           (HLD),A
7B4D: A2         AND         D
7B4E: 3A         LD           A,(HLD)
7B4F: A3         AND         E
7B50: 40         LD           B,B
7B51: A2         AND         D
7B52: 48         LD           C,B
7B53: A8         XOR         B
7B54: 44         LD           B,H
7B55: A3         AND         E
7B56: 2C         INC         L
7B57: A2         AND         D
7B58: 36 A3      LD           (HL),$A3
7B5A: 3C         INC         A
7B5B: A2         AND         D
7B5C: 44         LD           B,H
7B5D: A8         XOR         B
7B5E: 40         LD           B,B
7B5F: 9C         SBC         H
7B60: 00         NOP
7B61: 9D         SBC         L
7B62: 50         LD           D,B
7B63: 21 80 AE   LD           HL,$AE80
7B66: 01 01 A8   LD           BC,$A801
7B69: 58         LD           E,B
7B6A: A3         AND         E
7B6B: 01 A2 4E   LD           BC,$4EA2
7B6E: A3         AND         E
7B6F: 52         LD           D,D
7B70: A2         AND         D
7B71: 40         LD           B,B
7B72: A5         AND         L
7B73: 44         LD           B,H
7B74: A2         AND         D
7B75: 01 A3 52   LD           BC,$52A3
7B78: A2         AND         D
7B79: 5C         LD           E,H
7B7A: A8         XOR         B
7B7B: 58         LD           E,B
7B7C: A3         AND         E
7B7D: 01 A2 4E   LD           BC,$4EA2
7B80: A3         AND         E
7B81: 52         LD           D,D
7B82: A2         AND         D
7B83: 40         LD           B,B
7B84: A5         AND         L
7B85: 44         LD           B,H
7B86: A2         AND         D
7B87: 01 A3 40   LD           BC,$40A3
7B8A: A2         AND         D
7B8B: 52         LD           D,D
7B8C: AE         XOR         (HL)
7B8D: 4A         LD           C,D
7B8E: 01 00 9D   LD           BC,$9D00
7B91: F4                              
7B92: 4B         LD           C,E
7B93: 40         LD           B,B
7B94: 9B         SBC         E
7B95: 20 A5      JR           NZ,$7B3C
7B97: 01 A1 5C   LD           BC,$5CA1
7B9A: 01 A7 74   LD           BC,$74A7
7B9D: A5         AND         L
7B9E: 01 A1 58   LD           BC,$58A1
7BA1: 01 A7 70   LD           BC,$70A7
7BA4: 9C         SBC         H
7BA5: 00         NOP
7BA6: 00         NOP
7BA7: E3                              
7BA8: 4A         LD           C,D
7BA9: B1         OR           C
7BAA: 7B         LD           A,E
7BAB: B7         OR           A
7BAC: 7B         LD           A,E
7BAD: BD         CP           L
7BAE: 7B         LD           A,E
7BAF: C3 7B C9   JP           $C97B
7BB2: 7B         LD           A,E
7BB3: FF         RST         0X38
7BB4: FF         RST         0X38
7BB5: F9         LD           SP,HL
7BB6: 5E         LD           E,(HL)
7BB7: E0 7B      LDFF00   ($7B),A
7BB9: FF         RST         0X38
7BBA: FF         RST         0X38
7BBB: 05         DEC         B
7BBC: 5F         LD           E,A
7BBD: 06 7C      LD           B,$7C
7BBF: FF         RST         0X38
7BC0: FF         RST         0X38
7BC1: BB         CP           E
7BC2: 78         LD           A,B
7BC3: 1A         LD           A,(DE)
7BC4: 7C         LD           A,H
7BC5: FF         RST         0X38
7BC6: FF         RST         0X38
7BC7: C7         RST         0X00
7BC8: 78         LD           A,B
7BC9: 9D         SBC         L
7BCA: 80         ADD         A,B
7BCB: 81         ADD         A,C
7BCC: 00         NOP
7BCD: 96         SUB         (HL)
7BCE: A1         AND         C
7BCF: 52         LD           D,D
7BD0: 5C         LD           E,H
7BD1: 66         LD           H,(HL)
7BD2: 60         LD           H,B
7BD3: 6A         LD           L,D
7BD4: 74         LD           (HL),H
7BD5: 9D         SBC         L
7BD6: 80         ADD         A,B
7BD7: 00         NOP
7BD8: 00         NOP
7BD9: A4         AND         H
7BDA: 6E         LD           L,(HL)
7BDB: 01 9E D4   LD           BC,$D49E
7BDE: 4A         LD           C,D
7BDF: 00         NOP
7BE0: 9D         SBC         L
7BE1: 40         LD           B,B
7BE2: 81         ADD         A,C
7BE3: 40         LD           B,B
7BE4: A1         AND         C
7BE5: 42         LD           B,D
7BE6: 4C         LD           C,H
7BE7: 56         LD           D,(HL)
7BE8: 50         LD           D,B
7BE9: 5A         LD           E,D
7BEA: 64         LD           H,H
7BEB: 9D         SBC         L
7BEC: 40         LD           B,B
7BED: 00         NOP
7BEE: 40         LD           B,B
7BEF: A4         AND         H
7BF0: 5E         LD           E,(HL)
7BF1: 01 9E D4   LD           BC,$D49E
7BF4: 4A         LD           C,D
7BF5: 00         NOP
7BF6: AA         XOR         D
7BF7: AA         XOR         D
7BF8: AA         XOR         D
7BF9: A8         XOR         B
7BFA: 00         NOP
7BFB: 00         NOP
7BFC: 00         NOP
7BFD: 00         NOP
7BFE: AA         XOR         D
7BFF: AA         XOR         D
7C00: AA         XOR         D
7C01: A8         XOR         B
7C02: 00         NOP
7C03: 00         NOP
7C04: 00         NOP
7C05: 00         NOP
7C06: 9D         SBC         L
7C07: F6 7B      OR           $7B
7C09: 20 99      JR           NZ,$7BA4
7C0B: A1         AND         C
7C0C: 30 3A      JR           NC,$7C48
7C0E: 44         LD           B,H
7C0F: 3E 48      LD           A,$48
7C11: 52         LD           D,D
7C12: 9A         SBC         D
7C13: A4         AND         H
7C14: 4C         LD           C,H
7C15: 01 9E D4   LD           BC,$D49E
7C18: 4A         LD           C,D
7C19: 00         NOP
7C1A: 9B         SBC         E
7C1B: 06 A1      LD           B,$A1
7C1D: 1A         LD           A,(DE)
7C1E: 9C         SBC         H
7C1F: 9B         SBC         E
7C20: 10 A0      STOP       $A0
7C22: 15         DEC         D
7C23: 9C         SBC         H
7C24: 9E         SBC         (HL)
7C25: D4 4A 00   CALL       NC,$004A
7C28: 00         NOP
7C29: C5         PUSH       BC
7C2A: 4A         LD           C,D
7C2B: 33         INC         SP
7C2C: 7C         LD           A,H
7C2D: 3B         DEC         SP
7C2E: 7C         LD           A,H
7C2F: 17         RLA
7C30: 4B         LD           C,E
7C31: 41         LD           B,C
7C32: 7C         LD           A,H
7C33: 47         LD           B,A
7C34: 7C         LD           A,H
7C35: 4E         LD           C,(HL)
7C36: 7C         LD           A,H
7C37: FF         RST         0X38
7C38: FF         RST         0X38
7C39: 35         DEC         (HL)
7C3A: 7C         LD           A,H
7C3B: 93         SUB         E
7C3C: 7C         LD           A,H
7C3D: FF         RST         0X38
7C3E: FF         RST         0X38
7C3F: 3B         DEC         SP
7C40: 7C         LD           A,H
7C41: F9         LD           SP,HL
7C42: 7C         LD           A,H
7C43: FF         RST         0X38
7C44: FF         RST         0X38
7C45: 41         LD           B,C
7C46: 7C         LD           A,H
7C47: 9D         SBC         L
7C48: 10 00      STOP       $00
7C4A: 80         ADD         A,B
7C4B: A1         AND         C
7C4C: 01 00 AC   LD           BC,$AC00
7C4F: 90         SUB         B
7C50: 86         ADD         A,(HL)
7C51: 8E         ADC         A,(HL)
7C52: 84         ADD         A,H
7C53: 8C         ADC         A,H
7C54: 82         ADD         A,D
7C55: 8A         ADC         A,D
7C56: 80         ADD         A,B
7C57: 88         ADC         A,B
7C58: 7E         LD           A,(HL)
7C59: 86         ADD         A,(HL)
7C5A: 78         LD           A,B
7C5B: 84         ADD         A,H
7C5C: 76         HALT
7C5D: 82         ADD         A,D
7C5E: 74         LD           (HL),H
7C5F: 80         ADD         A,B
7C60: 72         LD           (HL),D
7C61: AC         XOR         H
7C62: 86         ADD         A,(HL)
7C63: 78         LD           A,B
7C64: 84         ADD         A,H
7C65: 76         HALT
7C66: 82         ADD         A,D
7C67: 74         LD           (HL),H
7C68: 80         ADD         A,B
7C69: 72         LD           (HL),D
7C6A: AD         XOR         L
7C6B: 7C         LD           A,H
7C6C: 7A         LD           A,D
7C6D: 72         LD           (HL),D
7C6E: 6C         LD           L,H
7C6F: 68         LD           L,B
7C70: 64         LD           H,H
7C71: 62         LD           H,D
7C72: 5A         LD           E,D
7C73: 54         LD           D,H
7C74: 50         LD           D,B
7C75: AD         XOR         L
7C76: 64         LD           H,H
7C77: 62         LD           H,D
7C78: 5A         LD           E,D
7C79: 54         LD           D,H
7C7A: 50         LD           D,B
7C7B: AE         XOR         (HL)
7C7C: 01 AD 7A   LD           BC,$7AAD
7C7F: 72         LD           (HL),D
7C80: AD         XOR         L
7C81: 7A         LD           A,D
7C82: 72         LD           (HL),D
7C83: A5         AND         L
7C84: 01 01 AD   LD           BC,$AD01
7C87: 62         LD           H,D
7C88: 64         LD           H,H
7C89: 72         LD           (HL),D
7C8A: 6C         LD           L,H
7C8B: 62         LD           H,D
7C8C: 64         LD           H,H
7C8D: 72         LD           (HL),D
7C8E: 6C         LD           L,H
7C8F: A5         AND         L
7C90: 01 01 00   LD           BC,$0001
7C93: 9D         SBC         L
7C94: 39         ADD         HL,SP
7C95: 00         NOP
7C96: 00         NOP
7C97: AC         XOR         H
7C98: 90         SUB         B
7C99: 86         ADD         A,(HL)
7C9A: 8E         ADC         A,(HL)
7C9B: 84         ADD         A,H
7C9C: 8C         ADC         A,H
7C9D: 82         ADD         A,D
7C9E: 8A         ADC         A,D
7C9F: 80         ADD         A,B
7CA0: 88         ADC         A,B
7CA1: 7E         LD           A,(HL)
7CA2: 86         ADD         A,(HL)
7CA3: 78         LD           A,B
7CA4: 84         ADD         A,H
7CA5: 76         HALT
7CA6: 82         ADD         A,D
7CA7: 74         LD           (HL),H
7CA8: 80         ADD         A,B
7CA9: 72         LD           (HL),D
7CAA: 9D         SBC         L
7CAB: 20 00      JR           NZ,$7CAD
7CAD: 40         LD           B,B
7CAE: AC         XOR         H
7CAF: 86         ADD         A,(HL)
7CB0: 78         LD           A,B
7CB1: 84         ADD         A,H
7CB2: 76         HALT
7CB3: 82         ADD         A,D
7CB4: 74         LD           (HL),H
7CB5: 80         ADD         A,B
7CB6: 72         LD           (HL),D
7CB7: 9D         SBC         L
7CB8: 29         ADD         HL,HL
7CB9: 00         NOP
7CBA: 00         NOP
7CBB: AD         XOR         L
7CBC: 7C         LD           A,H
7CBD: 7A         LD           A,D
7CBE: 72         LD           (HL),D
7CBF: 6C         LD           L,H
7CC0: 68         LD           L,B
7CC1: 64         LD           H,H
7CC2: 62         LD           H,D
7CC3: 5A         LD           E,D
7CC4: 54         LD           D,H
7CC5: 50         LD           D,B
7CC6: 9D         SBC         L
7CC7: 20 00      JR           NZ,$7CC9
7CC9: 40         LD           B,B
7CCA: AD         XOR         L
7CCB: 64         LD           H,H
7CCC: 62         LD           H,D
7CCD: 5A         LD           E,D
7CCE: 54         LD           D,H
7CCF: 50         LD           D,B
7CD0: AE         XOR         (HL)
7CD1: 01 9D 29   LD           BC,$299D
7CD4: 00         NOP
7CD5: 00         NOP
7CD6: AD         XOR         L
7CD7: 7A         LD           A,D
7CD8: 72         LD           (HL),D
7CD9: 9D         SBC         L
7CDA: 20 00      JR           NZ,$7CDC
7CDC: 40         LD           B,B
7CDD: AD         XOR         L
7CDE: 7A         LD           A,D
7CDF: 72         LD           (HL),D
7CE0: A5         AND         L
7CE1: 01 01 9D   LD           BC,$9D01
7CE4: 29         ADD         HL,HL
7CE5: 00         NOP
7CE6: 00         NOP
7CE7: AD         XOR         L
7CE8: 62         LD           H,D
7CE9: 64         LD           H,H
7CEA: 72         LD           (HL),D
7CEB: 6C         LD           L,H
7CEC: 9D         SBC         L
7CED: 20 00      JR           NZ,$7CEF
7CEF: 40         LD           B,B
7CF0: AD         XOR         L
7CF1: 62         LD           H,D
7CF2: 64         LD           H,H
7CF3: 72         LD           (HL),D
7CF4: 6C         LD           L,H
7CF5: A5         AND         L
7CF6: 01 01 00   LD           BC,$0001
7CF9: 9B         SBC         E
7CFA: 20 A3      JR           NZ,$7C9F
7CFC: 38 9C      JR           C,$7C9A
7CFE: 00         NOP
7CFF: 00         NOP
7D00: C5         PUSH       BC
7D01: 4A         LD           C,D
7D02: 0A         LD           A,(BC)
7D03: 7D         LD           A,L
7D04: 12         LD           (DE),A
7D05: 7D         LD           A,L
7D06: 17         RLA
7D07: 4B         LD           C,E
7D08: 00         NOP
7D09: 00         NOP
7D0A: 28 7D      JR           Z,$7D89
7D0C: 36 7D      LD           (HL),$7D
7D0E: FF         RST         0X38
7D0F: FF         RST         0X38
7D10: 0C         INC         C
7D11: 7D         LD           A,L
7D12: 33         INC         SP
7D13: 7D         LD           A,L
7D14: 3C         INC         A
7D15: 7D         LD           A,L
7D16: 36 7D      LD           (HL),$7D
7D18: 41         LD           B,C
7D19: 7D         LD           A,L
7D1A: 36 7D      LD           (HL),$7D
7D1C: 46         LD           B,(HL)
7D1D: 7D         LD           A,L
7D1E: 36 7D      LD           (HL),$7D
7D20: 41         LD           B,C
7D21: 7D         LD           A,L
7D22: 36 7D      LD           (HL),$7D
7D24: FF         RST         0X38
7D25: FF         RST         0X38
7D26: 14         INC         D
7D27: 7D         LD           A,L
7D28: 9D         SBC         L
7D29: 20 00      JR           NZ,$7D2B
7D2B: 43         LD           B,E
7D2C: A7         AND         A
7D2D: 01 A1 01   LD           BC,$01A1
7D30: A0         AND         B
7D31: 01 00 A7   LD           BC,$A700
7D34: 01 00 A1   LD           BC,$A100
7D37: 20 22      JR           NZ,$7D5B
7D39: 20 22      JR           NZ,$7D5D
7D3B: 00         NOP
7D3C: 9D         SBC         L
7D3D: 20 00      JR           NZ,$7D3F
7D3F: 40         LD           B,B
7D40: 00         NOP
7D41: 9D         SBC         L
7D42: 30 00      JR           NC,$7D44
7D44: 40         LD           B,B
7D45: 00         NOP
7D46: 9D         SBC         L
7D47: 40         LD           B,B
7D48: 00         NOP
7D49: 40         LD           B,B
7D4A: 00         NOP
7D4B: 00         NOP
7D4C: A7         AND         A
7D4D: 4A         LD           C,D
7D4E: 56         LD           D,(HL)
7D4F: 7D         LD           A,L
7D50: 5E         LD           E,(HL)
7D51: 7D         LD           A,L
7D52: 66         LD           H,(HL)
7D53: 7D         LD           A,L
7D54: 00         NOP
7D55: 00         NOP
7D56: 6E         LD           L,(HL)
7D57: 7D         LD           A,L
7D58: 84         ADD         A,H
7D59: 7D         LD           A,L
7D5A: FF         RST         0X38
7D5B: FF         RST         0X38
7D5C: 58         LD           E,B
7D5D: 7D         LD           A,L
7D5E: 7A         LD           A,D
7D5F: 7D         LD           A,L
7D60: 84         ADD         A,H
7D61: 7D         LD           A,L
7D62: FF         RST         0X38
7D63: FF         RST         0X38
7D64: 60         LD           H,B
7D65: 7D         LD           A,L
7D66: F8 7D      LDHL       SP,$7D
7D68: 84         ADD         A,H
7D69: 7D         LD           A,L
7D6A: FF         RST         0X38
7D6B: FF         RST         0X38
7D6C: 68         LD           L,B
7D6D: 7D         LD           A,L
7D6E: 9D         SBC         L
7D6F: 10 00      STOP       $00
7D71: 40         LD           B,B
7D72: A5         AND         L
7D73: 01 01 A8   LD           BC,$A801
7D76: 01 AA 01   LD           BC,$01AA
7D79: 00         NOP
7D7A: 9D         SBC         L
7D7B: 20 00      JR           NZ,$7D7D
7D7D: 00         NOP
7D7E: A5         AND         L
7D7F: 01 01 A8   LD           BC,$A801
7D82: 01 00 A1   LD           BC,$A100
7D85: 8E         ADC         A,(HL)
7D86: 8A         ADC         A,D
7D87: 88         ADC         A,B
7D88: 80         ADD         A,B
7D89: 7A         LD           A,D
7D8A: 76         HALT
7D8B: 72         LD           (HL),D
7D8C: 70         LD           (HL),B
7D8D: 68         LD           L,B
7D8E: 62         LD           H,D
7D8F: 5E         LD           E,(HL)
7D90: 5A         LD           E,D
7D91: 58         LD           E,B
7D92: 50         LD           D,B
7D93: 4A         LD           C,D
7D94: 46         LD           B,(HL)
7D95: 42         LD           B,D
7D96: 40         LD           B,B
7D97: 38 32      JR           C,$7DCB
7D99: 2E 2A      LD           L,$2A
7D9B: 2E 32      LD           L,$32
7D9D: 38 40      JR           C,$7DDF
7D9F: 42         LD           B,D
7DA0: 46         LD           B,(HL)
7DA1: 4A         LD           C,D
7DA2: 50         LD           D,B
7DA3: 58         LD           E,B
7DA4: 5A         LD           E,D
7DA5: 5E         LD           E,(HL)
7DA6: 62         LD           H,D
7DA7: 68         LD           L,B
7DA8: 70         LD           (HL),B
7DA9: 72         LD           (HL),D
7DAA: 76         HALT
7DAB: 7A         LD           A,D
7DAC: 80         ADD         A,B
7DAD: 88         ADC         A,B
7DAE: 8A         ADC         A,D
7DAF: 8E         ADC         A,(HL)
7DB0: 8A         ADC         A,D
7DB1: 86         ADD         A,(HL)
7DB2: 80         ADD         A,B
7DB3: 78         LD           A,B
7DB4: 76         HALT
7DB5: 72         LD           (HL),D
7DB6: 6E         LD           L,(HL)
7DB7: 68         LD           L,B
7DB8: 60         LD           H,B
7DB9: 5E         LD           E,(HL)
7DBA: 5A         LD           E,D
7DBB: 56         LD           D,(HL)
7DBC: 50         LD           D,B
7DBD: 48         LD           C,B
7DBE: 46         LD           B,(HL)
7DBF: 42         LD           B,D
7DC0: 3E 38      LD           A,$38
7DC2: 30 34      JR           NC,$7DF8
7DC4: 38 3E      JR           C,$7E04
7DC6: 42         LD           B,D
7DC7: 46         LD           B,(HL)
7DC8: 48         LD           C,B
7DC9: 34         INC         (HL)
7DCA: 50         LD           D,B
7DCB: 56         LD           D,(HL)
7DCC: 5A         LD           E,D
7DCD: 5E         LD           E,(HL)
7DCE: 60         LD           H,B
7DCF: 34         INC         (HL)
7DD0: 68         LD           L,B
7DD1: 6E         LD           L,(HL)
7DD2: 72         LD           (HL),D
7DD3: 76         HALT
7DD4: 76         HALT
7DD5: 72         LD           (HL),D
7DD6: 6C         LD           L,H
7DD7: 64         LD           H,H
7DD8: 62         LD           H,D
7DD9: 5E         LD           E,(HL)
7DDA: 5A         LD           E,D
7DDB: 54         LD           D,H
7DDC: 4C         LD           C,H
7DDD: 4A         LD           C,D
7DDE: 46         LD           B,(HL)
7DDF: 42         LD           B,D
7DE0: 3C         INC         A
7DE1: 34         INC         (HL)
7DE2: 32         LD           (HLD),A
7DE3: 2E 32      LD           L,$32
7DE5: 34         INC         (HL)
7DE6: 3C         INC         A
7DE7: 42         LD           B,D
7DE8: 46         LD           B,(HL)
7DE9: 4A         LD           C,D
7DEA: 4C         LD           C,H
7DEB: 54         LD           D,H
7DEC: 5A         LD           E,D
7DED: 5E         LD           E,(HL)
7DEE: 62         LD           H,D
7DEF: 64         LD           H,H
7DF0: 6C         LD           L,H
7DF1: 72         LD           (HL),D
7DF2: 76         HALT
7DF3: 7A         LD           A,D
7DF4: 7C         LD           A,H
7DF5: 84         ADD         A,H
7DF6: 8A         ADC         A,D
7DF7: 00         NOP
7DF8: 9D         SBC         L
7DF9: A7         AND         A
7DFA: 79         LD           A,C
7DFB: 20 A5      JR           NZ,$7DA2
7DFD: 01 01 A8   LD           BC,$A801
7E00: 01 A3 01   LD           BC,$01A3
7E03: 00         NOP
7E04: 00         NOP
7E05: D4 4A 0F   CALL       NC,$0F4A
7E08: 7E         LD           A,(HL)
7E09: 17         RLA
7E0A: 7E         LD           A,(HL)
7E0B: 1F         RRA
7E0C: 7E         LD           A,(HL)
7E0D: 27         DAA
7E0E: 7E         LD           A,(HL)
7E0F: 2F         CPL
7E10: 7E         LD           A,(HL)
7E11: 70         LD           (HL),B
7E12: 7E         LD           A,(HL)
7E13: FF         RST         0X38
7E14: FF         RST         0X38
7E15: 11 7E 3A   LD           DE,$3A7E
7E18: 7E         LD           A,(HL)
7E19: 96         SUB         (HL)
7E1A: 7E         LD           A,(HL)
7E1B: FF         RST         0X38
7E1C: FF         RST         0X38
7E1D: 19         ADD         HL,DE
7E1E: 7E         LD           A,(HL)
7E1F: 55         LD           D,L
7E20: 7E         LD           A,(HL)
7E21: FE 7E      CP           $7E
7E23: FF         RST         0X38
7E24: FF         RST         0X38
7E25: 21 7E 60   LD           HL,$607E
7E28: 7E         LD           A,(HL)
7E29: 76         HALT
7E2A: 7F         LD           A,A
7E2B: FF         RST         0X38
7E2C: FF         RST         0X38
7E2D: 29         ADD         HL,HL
7E2E: 7E         LD           A,(HL)
7E2F: 9D         SBC         L
7E30: 60         LD           H,B
7E31: 00         NOP
7E32: 41         LD           B,C
7E33: A7         AND         A
7E34: 01 AA 4E   LD           BC,$4EAA
7E37: AE         XOR         (HL)
7E38: 50         LD           D,B
7E39: 00         NOP
7E3A: 9D         SBC         L
7E3B: 40         LD           B,B
7E3C: 00         NOP
7E3D: 01 A7 01   LD           BC,$01A7
7E40: AA         XOR         D
7E41: 64         LD           H,H
7E42: AE         XOR         (HL)
7E43: 66         LD           H,(HL)
7E44: 00         NOP
7E45: 8A         ADC         A,D
7E46: DF         RST         0X18
7E47: DA 86 31   JP           C,$3186
7E4A: 01 36 86   LD           BC,$8636
7E4D: 8A         ADC         A,D
7E4E: DF         RST         0X18
7E4F: DA 86 31   JP           C,$3186
7E52: 01 36 86   LD           BC,$8636
7E55: 9D         SBC         L
7E56: 45         LD           B,L
7E57: 7E         LD           A,(HL)
7E58: 20 A7      JR           NZ,$7E01
7E5A: 01 AA 5A   LD           BC,$5AAA
7E5D: AE         XOR         (HL)
7E5E: 5C         LD           E,H
7E5F: 00         NOP
7E60: A7         AND         A
7E61: 01 AA 01   LD           BC,$01AA
7E64: A5         AND         L
7E65: 01 A1 FF   LD           BC,$FFA1
7E68: A2         AND         D
7E69: FF         RST         0X38
7E6A: FF         RST         0X38
7E6B: A1         AND         C
7E6C: FF         RST         0X38
7E6D: A2         AND         D
7E6E: FF         RST         0X38
7E6F: 00         NOP
7E70: 9D         SBC         L
7E71: 41         LD           B,C
7E72: 00         NOP
7E73: 80         ADD         A,B
7E74: 9B         SBC         E
7E75: 07         RLCA
7E76: A6         AND         (HL)
7E77: 82         ADD         A,D
7E78: 82         ADD         A,D
7E79: A3         AND         E
7E7A: 82         ADD         A,D
7E7B: A2         AND         D
7E7C: 82         ADD         A,D
7E7D: A3         AND         E
7E7E: 82         ADD         A,D
7E7F: 9C         SBC         H
7E80: 9D         SBC         L
7E81: 61         LD           H,C
7E82: 00         NOP
7E83: 80         ADD         A,B
7E84: 97         SUB         A
7E85: A2         AND         D
7E86: 44         LD           B,H
7E87: A6         AND         (HL)
7E88: 44         LD           B,H
7E89: A1         AND         C
7E8A: 44         LD           B,H
7E8B: 44         LD           B,H
7E8C: A3         AND         E
7E8D: 44         LD           B,H
7E8E: A2         AND         D
7E8F: 44         LD           B,H
7E90: A1         AND         C
7E91: 44         LD           B,H
7E92: A2         AND         D
7E93: 44         LD           B,H
7E94: 98         SBC         B
7E95: 00         NOP
7E96: 9D         SBC         L
7E97: 60         LD           H,B
7E98: 21 41 A3   LD           HL,$A341
7E9B: 46         LD           B,(HL)
7E9C: A7         AND         A
7E9D: 3C         INC         A
7E9E: A1         AND         C
7E9F: 01 46 46   LD           BC,$4646
7EA2: 4A         LD           C,D
7EA3: 4C         LD           C,H
7EA4: 50         LD           D,B
7EA5: A8         XOR         B
7EA6: 54         LD           D,H
7EA7: AA         XOR         D
7EA8: 54         LD           D,H
7EA9: 56         LD           D,(HL)
7EAA: 5A         LD           E,D
7EAB: AD         XOR         L
7EAC: 01 A8 5E   LD           BC,$5EA8
7EAF: AA         XOR         D
7EB0: 5E         LD           E,(HL)
7EB1: 5A         LD           E,D
7EB2: 56         LD           D,(HL)
7EB3: AD         XOR         L
7EB4: 01 A6 5A   LD           BC,$5AA6
7EB7: A1         AND         C
7EB8: 56         LD           D,(HL)
7EB9: A4         AND         H
7EBA: 54         LD           D,H
7EBB: A3         AND         E
7EBC: 54         LD           D,H
7EBD: A2         AND         D
7EBE: 50         LD           D,B
7EBF: A1         AND         C
7EC0: 50         LD           D,B
7EC1: 54         LD           D,H
7EC2: A4         AND         H
7EC3: 56         LD           D,(HL)
7EC4: A2         AND         D
7EC5: 54         LD           D,H
7EC6: 50         LD           D,B
7EC7: A2         AND         D
7EC8: 4C         LD           C,H
7EC9: A1         AND         C
7ECA: 4C         LD           C,H
7ECB: 50         LD           D,B
7ECC: A4         AND         H
7ECD: 54         LD           D,H
7ECE: A2         AND         D
7ECF: 50         LD           D,B
7ED0: 4C         LD           C,H
7ED1: A2         AND         D
7ED2: 4A         LD           C,D
7ED3: A1         AND         C
7ED4: 4A         LD           C,D
7ED5: 4E         LD           C,(HL)
7ED6: A4         AND         H
7ED7: 52         LD           D,D
7ED8: A3         AND         E
7ED9: 58         LD           E,B
7EDA: 9D         SBC         L
7EDB: 62         LD           H,D
7EDC: 00         NOP
7EDD: 40         LD           B,B
7EDE: A2         AND         D
7EDF: 54         LD           D,H
7EE0: A6         AND         (HL)
7EE1: 54         LD           D,H
7EE2: A1         AND         C
7EE3: 54         LD           D,H
7EE4: 54         LD           D,H
7EE5: A3         AND         E
7EE6: 54         LD           D,H
7EE7: A2         AND         D
7EE8: 54         LD           D,H
7EE9: A1         AND         C
7EEA: 54         LD           D,H
7EEB: A2         AND         D
7EEC: 54         LD           D,H
7EED: 00         NOP
7EEE: 00         NOP
7EEF: 11 22 33   LD           DE,$3322
7EF2: 44         LD           B,H
7EF3: 55         LD           D,L
7EF4: 67         LD           H,A
7EF5: 89         ADC         A,C
7EF6: 00         NOP
7EF7: 00         NOP
7EF8: 00         NOP
7EF9: 05         DEC         B
7EFA: 00         NOP
7EFB: 00         NOP
7EFC: 00         NOP
7EFD: 05         DEC         B
7EFE: 9D         SBC         L
7EFF: EE 7E      XOR         $7E
7F01: 20 99      JR           NZ,$7E9C
7F03: A2         AND         D
7F04: 5E         LD           E,(HL)
7F05: A1         AND         C
7F06: 4C         LD           C,H
7F07: A2         AND         D
7F08: 54         LD           D,H
7F09: 5E         LD           E,(HL)
7F0A: 5C         LD           E,H
7F0B: 4C         LD           C,H
7F0C: 54         LD           D,H
7F0D: 5C         LD           E,H
7F0E: A1         AND         C
7F0F: 4C         LD           C,H
7F10: A2         AND         D
7F11: 5A         LD           E,D
7F12: A1         AND         C
7F13: 4C         LD           C,H
7F14: A2         AND         D
7F15: 54         LD           D,H
7F16: 5A         LD           E,D
7F17: 58         LD           E,B
7F18: 4C         LD           C,H
7F19: 54         LD           D,H
7F1A: 58         LD           E,B
7F1B: A1         AND         C
7F1C: 4C         LD           C,H
7F1D: A2         AND         D
7F1E: 56         LD           D,(HL)
7F1F: A1         AND         C
7F20: 46         LD           B,(HL)
7F21: A2         AND         D
7F22: 4C         LD           C,H
7F23: 56         LD           D,(HL)
7F24: 5A         LD           E,D
7F25: 4A         LD           C,D
7F26: 50         LD           D,B
7F27: 5A         LD           E,D
7F28: A1         AND         C
7F29: 4A         LD           C,D
7F2A: A2         AND         D
7F2B: 5A         LD           E,D
7F2C: A1         AND         C
7F2D: 4C         LD           C,H
7F2E: A2         AND         D
7F2F: 54         LD           D,H
7F30: 5A         LD           E,D
7F31: 5A         LD           E,D
7F32: A1         AND         C
7F33: 4C         LD           C,H
7F34: 54         LD           D,H
7F35: A2         AND         D
7F36: 5A         LD           E,D
7F37: A1         AND         C
7F38: 4C         LD           C,H
7F39: 54         LD           D,H
7F3A: 5A         LD           E,D
7F3B: A2         AND         D
7F3C: 56         LD           D,(HL)
7F3D: A1         AND         C
7F3E: 48         LD           C,B
7F3F: A2         AND         D
7F40: 50         LD           D,B
7F41: 56         LD           D,(HL)
7F42: 50         LD           D,B
7F43: 3E 48      LD           A,$48
7F45: 50         LD           D,B
7F46: A1         AND         C
7F47: 52         LD           D,D
7F48: A2         AND         D
7F49: 54         LD           D,H
7F4A: A1         AND         C
7F4B: 46         LD           B,(HL)
7F4C: A2         AND         D
7F4D: 4C         LD           C,H
7F4E: 54         LD           D,H
7F4F: 5E         LD           E,(HL)
7F50: A1         AND         C
7F51: 4C         LD           C,H
7F52: 54         LD           D,H
7F53: A2         AND         D
7F54: 5E         LD           E,(HL)
7F55: A1         AND         C
7F56: 5C         LD           E,H
7F57: 5E         LD           E,(HL)
7F58: 60         LD           H,B
7F59: A2         AND         D
7F5A: 62         LD           H,D
7F5B: A1         AND         C
7F5C: 52         LD           D,D
7F5D: A2         AND         D
7F5E: 58         LD           E,B
7F5F: 62         LD           H,D
7F60: 5E         LD           E,(HL)
7F61: 52         LD           D,D
7F62: 58         LD           E,B
7F63: 5E         LD           E,(HL)
7F64: A1         AND         C
7F65: 58         LD           E,B
7F66: A2         AND         D
7F67: 5C         LD           E,H
7F68: A6         AND         (HL)
7F69: 5C         LD           E,H
7F6A: A1         AND         C
7F6B: 5C         LD           E,H
7F6C: 5C         LD           E,H
7F6D: A3         AND         E
7F6E: 5C         LD           E,H
7F6F: A2         AND         D
7F70: 5C         LD           E,H
7F71: A1         AND         C
7F72: 5C         LD           E,H
7F73: A2         AND         D
7F74: 5C         LD           E,H
7F75: 00         NOP
7F76: 9B         SBC         E
7F77: 07         RLCA
7F78: A1         AND         C
7F79: 15         DEC         D
7F7A: 15         DEC         D
7F7B: 1A         LD           A,(DE)
7F7C: 15         DEC         D
7F7D: 15         DEC         D
7F7E: 15         DEC         D
7F7F: FF         RST         0X38
7F80: 15         DEC         D
7F81: 15         DEC         D
7F82: 15         DEC         D
7F83: 1A         LD           A,(DE)
7F84: 15         DEC         D
7F85: 15         DEC         D
7F86: 15         DEC         D
7F87: 1A         LD           A,(DE)
7F88: FF         RST         0X38
7F89: 9C         SBC         H
7F8A: A2         AND         D
7F8B: FF         RST         0X38
7F8C: A6         AND         (HL)
7F8D: FF         RST         0X38
7F8E: A1         AND         C
7F8F: FF         RST         0X38
7F90: FF         RST         0X38
7F91: A3         AND         E
7F92: FF         RST         0X38
7F93: A2         AND         D
7F94: FF         RST         0X38
7F95: A1         AND         C
7F96: FF         RST         0X38
7F97: A2         AND         D
7F98: FF         RST         0X38
7F99: 00         NOP
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
