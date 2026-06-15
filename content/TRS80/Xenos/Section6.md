![Xenos](Xenos.png)

# Xenos SECTION6.DAT

>>> cpu Z80

>>> binary 5200:roms/section6.bin

```code
5200: 00 87 96                      ; List ID: 0x00, Length: 0x0796

5203: 81 19 00                      ; room=81_6_??81??, Length: 0x0019, Data: 0x00
;
5206:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5208:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5209:    04 13                      ;   Section COMMANDS, Length: 0x0013
520B:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
520E:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
520F:          02                   ;       ELSE go to: 0x5212
5210:             00 82             ;         MOVE AND LOOK, room=82_6_??82??
5212:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5213:          02                   ;       ELSE go to: 0x5216
5214:             00 83             ;         MOVE AND LOOK, room=83_6_??83??
5216:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5217:          02                   ;       ELSE go to: 0x521A
5218:             00 A8             ;         MOVE AND LOOK, room=A8_6_??A8??
521A:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
521B:          02                   ;       ELSE go to: 0x521E
521C:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

521E: 82 19 00                      ; room=82_6_??82??, Length: 0x0019, Data: 0x00
;
5221:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5223:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5224:    04 13                      ;   Section COMMANDS, Length: 0x0013
5226:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5229:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
522A:          02                   ;       ELSE go to: 0x522D
522B:             00 83             ;         MOVE AND LOOK, room=83_6_??83??
522D:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
522E:          02                   ;       ELSE go to: 0x5231
522F:             00 81             ;         MOVE AND LOOK, room=81_6_??81??
5231:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5232:          02                   ;       ELSE go to: 0x5235
5233:             00 A9             ;         MOVE AND LOOK, room=A9_6_??A9??
5235:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5236:          02                   ;       ELSE go to: 0x5239
5237:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

5239: 83 19 00                      ; room=83_6_??83??, Length: 0x0019, Data: 0x00
;
523C:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
523E:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
523F:    04 13                      ;   Section COMMANDS, Length: 0x0013
5241:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5244:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5245:          02                   ;       ELSE go to: 0x5248
5246:             00 84             ;         MOVE AND LOOK, room=84_6_??84??
5248:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5249:          02                   ;       ELSE go to: 0x524C
524A:             00 82             ;         MOVE AND LOOK, room=82_6_??82??
524C:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
524D:          02                   ;       ELSE go to: 0x5250
524E:             00 AA             ;         MOVE AND LOOK, room=AA_6_??AA??
5250:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5251:          02                   ;       ELSE go to: 0x5254
5252:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

5254: 84 19 00                      ; room=84_6_??84??, Length: 0x0019, Data: 0x00
;
5257:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5259:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
525A:    04 13                      ;   Section COMMANDS, Length: 0x0013
525C:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
525F:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5260:          02                   ;       ELSE go to: 0x5263
5261:             00 85             ;         MOVE AND LOOK, room=85_6_??85??
5263:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5264:          02                   ;       ELSE go to: 0x5267
5265:             00 83             ;         MOVE AND LOOK, room=83_6_??83??
5267:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5268:          02                   ;       ELSE go to: 0x526B
5269:             00 AB             ;         MOVE AND LOOK, room=AB_6_??AB??
526B:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
526C:          02                   ;       ELSE go to: 0x526F
526D:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

526F: 85 19 00                      ; room=85_6_??85??, Length: 0x0019, Data: 0x00
;
5272:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5274:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5275:    04 13                      ;   Section COMMANDS, Length: 0x0013
5277:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
527A:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
527B:          02                   ;       ELSE go to: 0x527E
527C:             00 86             ;         MOVE AND LOOK, room=86_6_??86??
527E:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
527F:          02                   ;       ELSE go to: 0x5282
5280:             00 84             ;         MOVE AND LOOK, room=84_6_??84??
5282:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5283:          02                   ;       ELSE go to: 0x5286
5284:             00 AC             ;         MOVE AND LOOK, room=AC_6_??AC??
5286:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5287:          02                   ;       ELSE go to: 0x528A
5288:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

528A: 86 19 00                      ; room=86_6_??86??, Length: 0x0019, Data: 0x00
;
528D:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
528F:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5290:    04 13                      ;   Section COMMANDS, Length: 0x0013
5292:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5295:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5296:          02                   ;       ELSE go to: 0x5299
5297:             00 87             ;         MOVE AND LOOK, room=87_6_??87??
5299:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
529A:          02                   ;       ELSE go to: 0x529D
529B:             00 85             ;         MOVE AND LOOK, room=85_6_??85??
529D:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
529E:          02                   ;       ELSE go to: 0x52A1
529F:             00 AD             ;         MOVE AND LOOK, room=AD_6_??AD??
52A1:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
52A2:          02                   ;       ELSE go to: 0x52A5
52A3:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

52A5: 87 19 00                      ; room=87_6_??87??, Length: 0x0019, Data: 0x00
;
52A8:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
52AA:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
52AB:    04 13                      ;   Section COMMANDS, Length: 0x0013
52AD:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
52B0:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
52B1:          02                   ;       ELSE go to: 0x52B4
52B2:             00 88             ;         MOVE AND LOOK, room=88_6_??88??
52B4:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
52B5:          02                   ;       ELSE go to: 0x52B8
52B6:             00 86             ;         MOVE AND LOOK, room=86_6_??86??
52B8:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
52B9:          02                   ;       ELSE go to: 0x52BC
52BA:             00 AE             ;         MOVE AND LOOK, room=AE_6_??AE??
52BC:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
52BD:          02                   ;       ELSE go to: 0x52C0
52BE:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

52C0: 88 19 00                      ; room=88_6_??88??, Length: 0x0019, Data: 0x00
;
52C3:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
52C5:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
52C6:    04 13                      ;   Section COMMANDS, Length: 0x0013
52C8:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
52CB:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
52CC:          02                   ;       ELSE go to: 0x52CF
52CD:             00 89             ;         MOVE AND LOOK, room=89_6_??89??
52CF:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
52D0:          02                   ;       ELSE go to: 0x52D3
52D1:             00 87             ;         MOVE AND LOOK, room=87_6_??87??
52D3:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
52D4:          02                   ;       ELSE go to: 0x52D7
52D5:             00 AF             ;         MOVE AND LOOK, room=AF_6_??AF??
52D7:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
52D8:          02                   ;       ELSE go to: 0x52DB
52D9:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

52DB: 89 19 00                      ; room=89_6_??89??, Length: 0x0019, Data: 0x00
;
52DE:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
52E0:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
52E1:    04 13                      ;   Section COMMANDS, Length: 0x0013
52E3:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
52E6:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
52E7:          02                   ;       ELSE go to: 0x52EA
52E8:             00 8A             ;         MOVE AND LOOK, room=8A_6_??8A??
52EA:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
52EB:          02                   ;       ELSE go to: 0x52EE
52EC:             00 88             ;         MOVE AND LOOK, room=88_6_??88??
52EE:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
52EF:          02                   ;       ELSE go to: 0x52F2
52F0:             00 B0             ;         MOVE AND LOOK, room=B0_6_SMALL_OASIS
52F2:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
52F3:          02                   ;       ELSE go to: 0x52F6
52F4:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

52F6: 8A 19 00                      ; room=8A_6_??8A??, Length: 0x0019, Data: 0x00
;
52F9:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
52FB:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
52FC:    04 13                      ;   Section COMMANDS, Length: 0x0013
52FE:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5301:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5302:          02                   ;       ELSE go to: 0x5305
5303:             00 8B             ;         MOVE AND LOOK, room=8B_6_??8B??
5305:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5306:          02                   ;       ELSE go to: 0x5309
5307:             00 89             ;         MOVE AND LOOK, room=89_6_??89??
5309:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
530A:          02                   ;       ELSE go to: 0x530D
530B:             00 B1             ;         MOVE AND LOOK, room=B1_6_??B1??
530D:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
530E:          02                   ;       ELSE go to: 0x5311
530F:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

5311: 8B 19 00                      ; room=8B_6_??8B??, Length: 0x0019, Data: 0x00
;
5314:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5316:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5317:    04 13                      ;   Section COMMANDS, Length: 0x0013
5319:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
531C:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
531D:          02                   ;       ELSE go to: 0x5320
531E:             00 89             ;         MOVE AND LOOK, room=89_6_??89??
5320:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5321:          02                   ;       ELSE go to: 0x5324
5322:             00 8A             ;         MOVE AND LOOK, room=8A_6_??8A??
5324:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5325:          02                   ;       ELSE go to: 0x5328
5326:             00 8C             ;         MOVE AND LOOK, room=8C_6_??8C??
5328:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5329:          02                   ;       ELSE go to: 0x532C
532A:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??

532C: 8C 19 00                      ; room=8C_6_??8C??, Length: 0x0019, Data: 0x00
;
532F:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5331:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5332:    04 13                      ;   Section COMMANDS, Length: 0x0013
5334:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5337:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5338:          02                   ;       ELSE go to: 0x533B
5339:             00 AF             ;         MOVE AND LOOK, room=AF_6_??AF??
533B:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
533C:          02                   ;       ELSE go to: 0x533F
533D:             00 B1             ;         MOVE AND LOOK, room=B1_6_??B1??
533F:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5340:          02                   ;       ELSE go to: 0x5343
5341:             00 8D             ;         MOVE AND LOOK, room=8D_6_??8D??
5343:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5344:          02                   ;       ELSE go to: 0x5347
5345:             00 8B             ;         MOVE AND LOOK, room=8B_6_??8B??

5347: 8D 19 00                      ; room=8D_6_??8D??, Length: 0x0019, Data: 0x00
;
534A:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
534C:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
534D:    04 13                      ;   Section COMMANDS, Length: 0x0013
534F:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5352:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5353:          02                   ;       ELSE go to: 0x5356
5354:             00 CC             ;         MOVE AND LOOK, room=CC_6_??CC??
5356:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5357:          02                   ;       ELSE go to: 0x535A
5358:             00 B2             ;         MOVE AND LOOK, room=B2_6_??B2??
535A:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
535B:          02                   ;       ELSE go to: 0x535E
535C:             00 8E             ;         MOVE AND LOOK, room=8E_6_??8E??
535E:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
535F:          02                   ;       ELSE go to: 0x5362
5360:             00 8C             ;         MOVE AND LOOK, room=8C_6_??8C??

5362: 8E 19 00                      ; room=8E_6_??8E??, Length: 0x0019, Data: 0x00
;
5365:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5367:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5368:    04 13                      ;   Section COMMANDS, Length: 0x0013
536A:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
536D:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
536E:          02                   ;       ELSE go to: 0x5371
536F:             00 CD             ;         MOVE AND LOOK, room=CD_6_??CD??
5371:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5372:          02                   ;       ELSE go to: 0x5375
5373:             00 B3             ;         MOVE AND LOOK, room=B3_6_??B3??
5375:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5376:          02                   ;       ELSE go to: 0x5379
5377:             00 8F             ;         MOVE AND LOOK, room=8F_6_??8F??
5379:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
537A:          02                   ;       ELSE go to: 0x537D
537B:             00 8D             ;         MOVE AND LOOK, room=8D_6_??8D??

537D: 8F 1C 00                      ; room=8F_6_??8F??, Length: 0x001C, Data: 0x00
;
5380:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5382:       0D 02                   ;     WHILE PASS, Length: 0x0002
5384:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
5385:          9B                   ;       ROUTINE 0x9B PRINT_EMPTY_HIGHWAY
;
5386:    04 13                      ;   Section COMMANDS, Length: 0x0013
5388:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
538B:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
538C:          02                   ;       ELSE go to: 0x538F
538D:             00 CE             ;         MOVE AND LOOK, room=CE_6_??CE??
538F:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5390:          02                   ;       ELSE go to: 0x5393
5391:             00 B4             ;         MOVE AND LOOK, room=B4_6_??B4??
5393:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5394:          02                   ;       ELSE go to: 0x5397
5395:             00 90             ;         MOVE AND LOOK, room=90_6_??90??
5397:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5398:          02                   ;       ELSE go to: 0x539B
5399:             00 8E             ;         MOVE AND LOOK, room=8E_6_??8E??

539B: 90 19 00                      ; room=90_6_??90??, Length: 0x0019, Data: 0x00
;
539E:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
53A0:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
53A1:    04 13                      ;   Section COMMANDS, Length: 0x0013
53A3:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
53A6:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
53A7:          02                   ;       ELSE go to: 0x53AA
53A8:             00 CF             ;         MOVE AND LOOK, room=CF_6_??CF??
53AA:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
53AB:          02                   ;       ELSE go to: 0x53AE
53AC:             00 B5             ;         MOVE AND LOOK, room=B5_6_??B5??
53AE:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
53AF:          02                   ;       ELSE go to: 0x53B2
53B0:             00 91             ;         MOVE AND LOOK, room=91_6_??91??
53B2:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
53B3:          02                   ;       ELSE go to: 0x53B6
53B4:             00 8F             ;         MOVE AND LOOK, room=8F_6_??8F??

53B6: 91 19 00                      ; room=91_6_??91??, Length: 0x0019, Data: 0x00
;
53B9:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
53BB:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
53BC:    04 13                      ;   Section COMMANDS, Length: 0x0013
53BE:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
53C1:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
53C2:          02                   ;       ELSE go to: 0x53C5
53C3:             00 D0             ;         MOVE AND LOOK, room=D0_6_??D0??
53C5:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
53C6:          02                   ;       ELSE go to: 0x53C9
53C7:             00 B6             ;         MOVE AND LOOK, room=B6_6_??B6??
53C9:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
53CA:          02                   ;       ELSE go to: 0x53CD
53CB:             00 92             ;         MOVE AND LOOK, room=92_6_??92??
53CD:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
53CE:          02                   ;       ELSE go to: 0x53D1
53CF:             00 90             ;         MOVE AND LOOK, room=90_6_??90??

53D1: 92 19 00                      ; room=92_6_??92??, Length: 0x0019, Data: 0x00
;
53D4:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
53D6:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
53D7:    04 13                      ;   Section COMMANDS, Length: 0x0013
53D9:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
53DC:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
53DD:          02                   ;       ELSE go to: 0x53E0
53DE:             00 D1             ;         MOVE AND LOOK, room=D1_6_??D1??
53E0:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
53E1:          02                   ;       ELSE go to: 0x53E4
53E2:             00 B7             ;         MOVE AND LOOK, room=B7_6_??B7??
53E4:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
53E5:          02                   ;       ELSE go to: 0x53E8
53E6:             00 93             ;         MOVE AND LOOK, room=93_6_??93??
53E8:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
53E9:          02                   ;       ELSE go to: 0x53EC
53EA:             00 91             ;         MOVE AND LOOK, room=91_6_??91??

53EC: 93 1C 00                      ; room=93_6_??93??, Length: 0x001C, Data: 0x00
;
53EF:    03 05                      ;   Section DESCRIPTION, Length: 0x0005
53F1:       0D 03                   ;     WHILE PASS, Length: 0x0003
53F3:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
53F4:          96                   ;       ROUTINE 0x96 PRINT_VAST_CANYON
53F5:          98                   ;       ROUTINE 0x98 PRINT_LAKE
;
53F6:    04 12                      ;   Section COMMANDS, Length: 0x0012
53F8:       0B 10 0A                ;     SWITCH, Length: 0x0010, Function to call: COM_0A_is_input_phrase(phrase_num)
53FB:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
53FC:          02                   ;       ELSE go to: 0x53FF
53FD:             00 B8             ;         MOVE AND LOOK, room=B8_6_??B8??
53FF:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5400:          02                   ;       ELSE go to: 0x5403
5401:             00 94             ;         MOVE AND LOOK, room=94_6_??94??
5403:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5404:          01                   ;       ELSE go to: 0x5406
5405:             97                ;         ROUTINE 0x97 PRINT_CERTAIN_DEATH
5406:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5407:          02                   ;       ELSE go to: 0x540A
5408:             00 92             ;         MOVE AND LOOK, room=92_6_??92??

540A: 94 1C 00                      ; room=94_6_??94??, Length: 0x001C, Data: 0x00
;
540D:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
540F:       0D 02                   ;     WHILE PASS, Length: 0x0002
5411:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
5412:          98                   ;       ROUTINE 0x98 PRINT_LAKE
;
5413:    04 13                      ;   Section COMMANDS, Length: 0x0013
5415:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5418:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5419:          02                   ;       ELSE go to: 0x541C
541A:             00 93             ;         MOVE AND LOOK, room=93_6_??93??
541C:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
541D:          02                   ;       ELSE go to: 0x5420
541E:             00 B8             ;         MOVE AND LOOK, room=B8_6_??B8??
5420:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5421:          02                   ;       ELSE go to: 0x5424
5422:             00 95             ;         MOVE AND LOOK, room=95_6_??95??
5424:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5425:          02                   ;       ELSE go to: 0x5428
5426:             00 B7             ;         MOVE AND LOOK, room=B7_6_??B7??

5428: 95 1B 00                      ; room=95_6_??95??, Length: 0x001B, Data: 0x00
;
542B:    03 05                      ;   Section DESCRIPTION, Length: 0x0005
542D:       0D 03                   ;     WHILE PASS, Length: 0x0003
542F:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
5430:          96                   ;       ROUTINE 0x96 PRINT_VAST_CANYON
5431:          98                   ;       ROUTINE 0x98 PRINT_LAKE
;
5432:    04 11                      ;   Section COMMANDS, Length: 0x0011
5434:       0B 0F 0A                ;     SWITCH, Length: 0x000F, Function to call: COM_0A_is_input_phrase(phrase_num)
5437:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5438:          01                   ;       ELSE go to: 0x543A
5439:             97                ;         ROUTINE 0x97 PRINT_CERTAIN_DEATH
543A:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
543B:          02                   ;       ELSE go to: 0x543E
543C:             00 96             ;         MOVE AND LOOK, room=96_6_??96??
543E:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
543F:          01                   ;       ELSE go to: 0x5441
5440:             97                ;         ROUTINE 0x97 PRINT_CERTAIN_DEATH
5441:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5442:          02                   ;       ELSE go to: 0x5445
5443:             00 94             ;         MOVE AND LOOK, room=94_6_??94??

5445: 96 1C 00                      ; room=96_6_??96??, Length: 0x001C, Data: 0x00
;
5448:    03 05                      ;   Section DESCRIPTION, Length: 0x0005
544A:       0D 03                   ;     WHILE PASS, Length: 0x0003
544C:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
544D:          96                   ;       ROUTINE 0x96 PRINT_VAST_CANYON
544E:          98                   ;       ROUTINE 0x98 PRINT_LAKE
;
544F:    04 12                      ;   Section COMMANDS, Length: 0x0012
5451:       0B 10 0A                ;     SWITCH, Length: 0x0010, Function to call: COM_0A_is_input_phrase(phrase_num)
5454:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5455:          02                   ;       ELSE go to: 0x5458
5456:             00 95             ;         MOVE AND LOOK, room=95_6_??95??
5458:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5459:          02                   ;       ELSE go to: 0x545C
545A:             00 B9             ;         MOVE AND LOOK, room=B9_6_??B9??
545C:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
545D:          01                   ;       ELSE go to: 0x545F
545E:             97                ;         ROUTINE 0x97 PRINT_CERTAIN_DEATH
545F:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5460:          02                   ;       ELSE go to: 0x5463
5461:             00 B8             ;         MOVE AND LOOK, room=B8_6_??B8??

5463: 97 1E 00                      ; room=97_6_??97??, Length: 0x001E, Data: 0x00
;
5466:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5468:       0D 02                   ;     WHILE PASS, Length: 0x0002
546A:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
546B:          96                   ;       ROUTINE 0x96 PRINT_VAST_CANYON
;
546C:    04 15                      ;   Section COMMANDS, Length: 0x0015
546E:       0B 13 0A                ;     SWITCH, Length: 0x0013, Function to call: COM_0A_is_input_phrase(phrase_num)
5471:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5472:          01                   ;       ELSE go to: 0x5474
5473:             97                ;         ROUTINE 0x97 PRINT_CERTAIN_DEATH
5474:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5475:          06                   ;       ELSE go to: 0x547C
5476:             0D 04             ;         WHILE PASS, Length: 0x0004
5478:                30 98          ;           SET CURRENT ROOM, room=98_5_??98??
547A:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
547C:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
547D:          01                   ;       ELSE go to: 0x547F
547E:             97                ;         ROUTINE 0x97 PRINT_CERTAIN_DEATH
547F:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5480:          02                   ;       ELSE go to: 0x5483
5481:             00 B9             ;         MOVE AND LOOK, room=B9_6_??B9??

5483: A7 20 00                      ; room=A7_6_??A7??, Length: 0x0020, Data: 0x00
;
5486:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5488:       0D 02                   ;     WHILE PASS, Length: 0x0002
548A:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
548B:          9B                   ;       ROUTINE 0x9B PRINT_EMPTY_HIGHWAY
;
548C:    04 17                      ;   Section COMMANDS, Length: 0x0017
548E:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
5491:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5492:          02                   ;       ELSE go to: 0x5495
5493:             00 C5             ;         MOVE AND LOOK, room=C5_6_??C5??
5495:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5496:          02                   ;       ELSE go to: 0x5499
5497:             00 A7             ;         MOVE AND LOOK, room=A7_6_??A7??
5499:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
549A:          06                   ;       ELSE go to: 0x54A1
549B:             0D 04             ;         WHILE PASS, Length: 0x0004
549D:                30 A6          ;           SET CURRENT ROOM, room=A6_5_??A6??
549F:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
54A1:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
54A2:          02                   ;       ELSE go to: 0x54A5
54A3:             00 A8             ;         MOVE AND LOOK, room=A8_6_??A8??

54A5: A8 19 00                      ; room=A8_6_??A8??, Length: 0x0019, Data: 0x00
;
54A8:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
54AA:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
54AB:    04 13                      ;   Section COMMANDS, Length: 0x0013
54AD:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
54B0:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
54B1:          02                   ;       ELSE go to: 0x54B4
54B2:             00 A9             ;         MOVE AND LOOK, room=A9_6_??A9??
54B4:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
54B5:          02                   ;       ELSE go to: 0x54B8
54B6:             00 84             ;         MOVE AND LOOK, room=84_6_??84??
54B8:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
54B9:          02                   ;       ELSE go to: 0x54BC
54BA:             00 A7             ;         MOVE AND LOOK, room=A7_6_??A7??
54BC:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
54BD:          02                   ;       ELSE go to: 0x54C0
54BE:             00 81             ;         MOVE AND LOOK, room=81_6_??81??

54C0: A9 19 00                      ; room=A9_6_??A9??, Length: 0x0019, Data: 0x00
;
54C3:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
54C5:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
54C6:    04 13                      ;   Section COMMANDS, Length: 0x0013
54C8:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
54CB:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
54CC:          02                   ;       ELSE go to: 0x54CF
54CD:             00 AA             ;         MOVE AND LOOK, room=AA_6_??AA??
54CF:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
54D0:          02                   ;       ELSE go to: 0x54D3
54D1:             00 A8             ;         MOVE AND LOOK, room=A8_6_??A8??
54D3:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
54D4:          02                   ;       ELSE go to: 0x54D7
54D5:             00 C5             ;         MOVE AND LOOK, room=C5_6_??C5??
54D7:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
54D8:          02                   ;       ELSE go to: 0x54DB
54D9:             00 82             ;         MOVE AND LOOK, room=82_6_??82??

54DB: AA 19 00                      ; room=AA_6_??AA??, Length: 0x0019, Data: 0x00
;
54DE:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
54E0:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
54E1:    04 13                      ;   Section COMMANDS, Length: 0x0013
54E3:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
54E6:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
54E7:          02                   ;       ELSE go to: 0x54EA
54E8:             00 AB             ;         MOVE AND LOOK, room=AB_6_??AB??
54EA:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
54EB:          02                   ;       ELSE go to: 0x54EE
54EC:             00 A9             ;         MOVE AND LOOK, room=A9_6_??A9??
54EE:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
54EF:          02                   ;       ELSE go to: 0x54F2
54F0:             00 C6             ;         MOVE AND LOOK, room=C6_6_HIGHWAY_TURNS
54F2:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
54F3:          02                   ;       ELSE go to: 0x54F6
54F4:             00 83             ;         MOVE AND LOOK, room=83_6_??83??

54F6: AB 19 00                      ; room=AB_6_??AB??, Length: 0x0019, Data: 0x00
;
54F9:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
54FB:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
54FC:    04 13                      ;   Section COMMANDS, Length: 0x0013
54FE:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5501:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5502:          02                   ;       ELSE go to: 0x5505
5503:             00 AC             ;         MOVE AND LOOK, room=AC_6_??AC??
5505:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5506:          02                   ;       ELSE go to: 0x5509
5507:             00 AA             ;         MOVE AND LOOK, room=AA_6_??AA??
5509:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
550A:          02                   ;       ELSE go to: 0x550D
550B:             00 C7             ;         MOVE AND LOOK, room=C7_6_??C7??
550D:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
550E:          02                   ;       ELSE go to: 0x5511
550F:             00 84             ;         MOVE AND LOOK, room=84_6_??84??

5511: AC 19 00                      ; room=AC_6_??AC??, Length: 0x0019, Data: 0x00
;
5514:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5516:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5517:    04 13                      ;   Section COMMANDS, Length: 0x0013
5519:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
551C:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
551D:          02                   ;       ELSE go to: 0x5520
551E:             00 AD             ;         MOVE AND LOOK, room=AD_6_??AD??
5520:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5521:          02                   ;       ELSE go to: 0x5524
5522:             00 AB             ;         MOVE AND LOOK, room=AB_6_??AB??
5524:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5525:          02                   ;       ELSE go to: 0x5528
5526:             00 C8             ;         MOVE AND LOOK, room=C8_6_??C8??
5528:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5529:          02                   ;       ELSE go to: 0x552C
552A:             00 85             ;         MOVE AND LOOK, room=85_6_??85??

552C: AD 19 00                      ; room=AD_6_??AD??, Length: 0x0019, Data: 0x00
;
552F:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5531:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5532:    04 13                      ;   Section COMMANDS, Length: 0x0013
5534:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5537:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5538:          02                   ;       ELSE go to: 0x553B
5539:             00 AE             ;         MOVE AND LOOK, room=AE_6_??AE??
553B:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
553C:          02                   ;       ELSE go to: 0x553F
553D:             00 AC             ;         MOVE AND LOOK, room=AC_6_??AC??
553F:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5540:          02                   ;       ELSE go to: 0x5543
5541:             00 C9             ;         MOVE AND LOOK, room=C9_6_??C9??
5543:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5544:          02                   ;       ELSE go to: 0x5547
5545:             00 86             ;         MOVE AND LOOK, room=86_6_??86??

5547: AE 19 00                      ; room=AE_6_??AE??, Length: 0x0019, Data: 0x00
;
554A:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
554C:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
554D:    04 13                      ;   Section COMMANDS, Length: 0x0013
554F:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5552:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5553:          02                   ;       ELSE go to: 0x5556
5554:             00 AF             ;         MOVE AND LOOK, room=AF_6_??AF??
5556:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5557:          02                   ;       ELSE go to: 0x555A
5558:             00 AD             ;         MOVE AND LOOK, room=AD_6_??AD??
555A:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
555B:          02                   ;       ELSE go to: 0x555E
555C:             00 CA             ;         MOVE AND LOOK, room=CA_6_??CA??
555E:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
555F:          02                   ;       ELSE go to: 0x5562
5560:             00 87             ;         MOVE AND LOOK, room=87_6_??87??

5562: AF 19 00                      ; room=AF_6_??AF??, Length: 0x0019, Data: 0x00
;
5565:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5567:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5568:    04 13                      ;   Section COMMANDS, Length: 0x0013
556A:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
556D:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
556E:          02                   ;       ELSE go to: 0x5571
556F:             00 B0             ;         MOVE AND LOOK, room=B0_6_SMALL_OASIS
5571:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5572:          02                   ;       ELSE go to: 0x5575
5573:             00 AE             ;         MOVE AND LOOK, room=AE_6_??AE??
5575:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5576:          02                   ;       ELSE go to: 0x5579
5577:             00 CB             ;         MOVE AND LOOK, room=CB_6_??CB??
5579:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
557A:          02                   ;       ELSE go to: 0x557D
557B:             00 88             ;         MOVE AND LOOK, room=88_6_??88??

557D: B0 43 00                      ; room=B0_6_SMALL_OASIS, Length: 0x0043, Data: 0x00
;
5580:    03 2B                      ;   Section DESCRIPTION, Length: 0x002B
5582:       0D 29                   ;     WHILE PASS, Length: 0x0029
5584:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
5585:          04 26                ;       PRINT, Length: 0x0026
5587:             5F BE 5B B1 4B 7B 55 45 8E 91 11 8A 5B 49 CA B5 ; 
5597:             2F 62 44 F4 96 C6 8E 14 6E 49 D6 15 9B 15 C6 B5 ; 
55A7:             07 B2 17 58 AB A2 ; 
;
;                 THERE IS A SMALL OASIS HERE. BUT, ALAS, IT HAS DRIED UP! 
;
;
55AD:    04 13                      ;   Section COMMANDS, Length: 0x0013
55AF:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
55B2:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
55B3:          02                   ;       ELSE go to: 0x55B6
55B4:             00 B1             ;         MOVE AND LOOK, room=B1_6_??B1??
55B6:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
55B7:          02                   ;       ELSE go to: 0x55BA
55B8:             00 AF             ;         MOVE AND LOOK, room=AF_6_??AF??
55BA:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
55BB:          02                   ;       ELSE go to: 0x55BE
55BC:             00 CC             ;         MOVE AND LOOK, room=CC_6_??CC??
55BE:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
55BF:          02                   ;       ELSE go to: 0x55C2
55C0:             00 89             ;         MOVE AND LOOK, room=89_6_??89??

55C2: B1 19 00                      ; room=B1_6_??B1??, Length: 0x0019, Data: 0x00
;
55C5:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
55C7:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
55C8:    04 13                      ;   Section COMMANDS, Length: 0x0013
55CA:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
55CD:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
55CE:          02                   ;       ELSE go to: 0x55D1
55CF:             00 8C             ;         MOVE AND LOOK, room=8C_6_??8C??
55D1:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
55D2:          02                   ;       ELSE go to: 0x55D5
55D3:             00 B0             ;         MOVE AND LOOK, room=B0_6_SMALL_OASIS
55D5:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
55D6:          02                   ;       ELSE go to: 0x55D9
55D7:             00 B2             ;         MOVE AND LOOK, room=B2_6_??B2??
55D9:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
55DA:          02                   ;       ELSE go to: 0x55DD
55DB:             00 8A             ;         MOVE AND LOOK, room=8A_6_??8A??

55DD: B2 19 00                      ; room=B2_6_??B2??, Length: 0x0019, Data: 0x00
;
55E0:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
55E2:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
55E3:    04 13                      ;   Section COMMANDS, Length: 0x0013
55E5:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
55E8:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
55E9:          02                   ;       ELSE go to: 0x55EC
55EA:             00 8D             ;         MOVE AND LOOK, room=8D_6_??8D??
55EC:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
55ED:          02                   ;       ELSE go to: 0x55F0
55EE:             00 CC             ;         MOVE AND LOOK, room=CC_6_??CC??
55F0:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
55F1:          02                   ;       ELSE go to: 0x55F4
55F2:             00 B3             ;         MOVE AND LOOK, room=B3_6_??B3??
55F4:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
55F5:          02                   ;       ELSE go to: 0x55F8
55F6:             00 B1             ;         MOVE AND LOOK, room=B1_6_??B1??

55F8: B3 19 00                      ; room=B3_6_??B3??, Length: 0x0019, Data: 0x00
;
55FB:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
55FD:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
55FE:    04 13                      ;   Section COMMANDS, Length: 0x0013
5600:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5603:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5604:          02                   ;       ELSE go to: 0x5607
5605:             00 8E             ;         MOVE AND LOOK, room=8E_6_??8E??
5607:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5608:          02                   ;       ELSE go to: 0x560B
5609:             00 CD             ;         MOVE AND LOOK, room=CD_6_??CD??
560B:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
560C:          02                   ;       ELSE go to: 0x560F
560D:             00 B4             ;         MOVE AND LOOK, room=B4_6_??B4??
560F:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5610:          02                   ;       ELSE go to: 0x5613
5611:             00 B2             ;         MOVE AND LOOK, room=B2_6_??B2??

5613: B4 1C 00                      ; room=B4_6_??B4??, Length: 0x001C, Data: 0x00
;
5616:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5618:       0D 02                   ;     WHILE PASS, Length: 0x0002
561A:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
561B:          9B                   ;       ROUTINE 0x9B PRINT_EMPTY_HIGHWAY
;
561C:    04 13                      ;   Section COMMANDS, Length: 0x0013
561E:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5621:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5622:          02                   ;       ELSE go to: 0x5625
5623:             00 8F             ;         MOVE AND LOOK, room=8F_6_??8F??
5625:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5626:          02                   ;       ELSE go to: 0x5629
5627:             00 CE             ;         MOVE AND LOOK, room=CE_6_??CE??
5629:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
562A:          02                   ;       ELSE go to: 0x562D
562B:             00 B5             ;         MOVE AND LOOK, room=B5_6_??B5??
562D:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
562E:          02                   ;       ELSE go to: 0x5631
562F:             00 B3             ;         MOVE AND LOOK, room=B3_6_??B3??

5631: B5 19 00                      ; room=B5_6_??B5??, Length: 0x0019, Data: 0x00
;
5634:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5636:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5637:    04 13                      ;   Section COMMANDS, Length: 0x0013
5639:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
563C:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
563D:          02                   ;       ELSE go to: 0x5640
563E:             00 90             ;         MOVE AND LOOK, room=90_6_??90??
5640:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5641:          02                   ;       ELSE go to: 0x5644
5642:             00 CF             ;         MOVE AND LOOK, room=CF_6_??CF??
5644:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5645:          02                   ;       ELSE go to: 0x5648
5646:             00 B6             ;         MOVE AND LOOK, room=B6_6_??B6??
5648:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5649:          02                   ;       ELSE go to: 0x564C
564A:             00 B4             ;         MOVE AND LOOK, room=B4_6_??B4??

564C: B6 19 00                      ; room=B6_6_??B6??, Length: 0x0019, Data: 0x00
;
564F:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5651:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5652:    04 13                      ;   Section COMMANDS, Length: 0x0013
5654:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5657:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5658:          02                   ;       ELSE go to: 0x565B
5659:             00 91             ;         MOVE AND LOOK, room=91_6_??91??
565B:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
565C:          02                   ;       ELSE go to: 0x565F
565D:             00 D0             ;         MOVE AND LOOK, room=D0_6_??D0??
565F:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5660:          02                   ;       ELSE go to: 0x5663
5661:             00 B7             ;         MOVE AND LOOK, room=B7_6_??B7??
5663:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5664:          02                   ;       ELSE go to: 0x5667
5665:             00 B5             ;         MOVE AND LOOK, room=B5_6_??B5??

5667: B7 1C 00                      ; room=B7_6_??B7??, Length: 0x001C, Data: 0x00
;
566A:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
566C:       0D 02                   ;     WHILE PASS, Length: 0x0002
566E:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
566F:          98                   ;       ROUTINE 0x98 PRINT_LAKE
;
5670:    04 13                      ;   Section COMMANDS, Length: 0x0013
5672:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5675:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5676:          02                   ;       ELSE go to: 0x5679
5677:             00 92             ;         MOVE AND LOOK, room=92_6_??92??
5679:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
567A:          02                   ;       ELSE go to: 0x567D
567B:             00 D1             ;         MOVE AND LOOK, room=D1_6_??D1??
567D:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
567E:          02                   ;       ELSE go to: 0x5681
567F:             00 94             ;         MOVE AND LOOK, room=94_6_??94??
5681:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5682:          02                   ;       ELSE go to: 0x5685
5683:             00 B6             ;         MOVE AND LOOK, room=B6_6_??B6??

5685: B8 1C 00                      ; room=B8_6_??B8??, Length: 0x001C, Data: 0x00
;
5688:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
568A:       0D 02                   ;     WHILE PASS, Length: 0x0002
568C:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
568D:          98                   ;       ROUTINE 0x98 PRINT_LAKE
;
568E:    04 13                      ;   Section COMMANDS, Length: 0x0013
5690:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5693:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5694:          02                   ;       ELSE go to: 0x5697
5695:             00 94             ;         MOVE AND LOOK, room=94_6_??94??
5697:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5698:          02                   ;       ELSE go to: 0x569B
5699:             00 D2             ;         MOVE AND LOOK, room=D2_6_??D2??
569B:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
569C:          02                   ;       ELSE go to: 0x569F
569D:             00 96             ;         MOVE AND LOOK, room=96_6_??96??
569F:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
56A0:          02                   ;       ELSE go to: 0x56A3
56A1:             00 D1             ;         MOVE AND LOOK, room=D1_6_??D1??

56A3: B9 20 00                      ; room=B9_6_??B9??, Length: 0x0020, Data: 0x00
;
56A6:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
56A8:       0D 02                   ;     WHILE PASS, Length: 0x0002
56AA:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
56AB:          98                   ;       ROUTINE 0x98 PRINT_LAKE
;
56AC:    04 17                      ;   Section COMMANDS, Length: 0x0017
56AE:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
56B1:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
56B2:          02                   ;       ELSE go to: 0x56B5
56B3:             00 96             ;         MOVE AND LOOK, room=96_6_??96??
56B5:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
56B6:          06                   ;       ELSE go to: 0x56BD
56B7:             0D 04             ;         WHILE PASS, Length: 0x0004
56B9:                30 BA          ;           SET CURRENT ROOM, room=BA_5_??BA??
56BB:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
56BD:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
56BE:          02                   ;       ELSE go to: 0x56C1
56BF:             00 97             ;         MOVE AND LOOK, room=97_6_??97??
56C1:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
56C2:          02                   ;       ELSE go to: 0x56C5
56C3:             00 D2             ;         MOVE AND LOOK, room=D2_6_??D2??

56C5: C5 20 00                      ; room=C5_6_??C5??, Length: 0x0020, Data: 0x00
;
56C8:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
56CA:       0D 02                   ;     WHILE PASS, Length: 0x0002
56CC:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
56CD:          9B                   ;       ROUTINE 0x9B PRINT_EMPTY_HIGHWAY
;
56CE:    04 17                      ;   Section COMMANDS, Length: 0x0017
56D0:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
56D3:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
56D4:          02                   ;       ELSE go to: 0x56D7
56D5:             00 C6             ;         MOVE AND LOOK, room=C6_6_HIGHWAY_TURNS
56D7:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
56D8:          02                   ;       ELSE go to: 0x56DB
56D9:             00 A7             ;         MOVE AND LOOK, room=A7_6_??A7??
56DB:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
56DC:          06                   ;       ELSE go to: 0x56E3
56DD:             0D 04             ;         WHILE PASS, Length: 0x0004
56DF:                30 C4          ;           SET CURRENT ROOM, room=C4_5_??C4??
56E1:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
56E3:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
56E4:          02                   ;       ELSE go to: 0x56E7
56E5:             00 A9             ;         MOVE AND LOOK, room=A9_6_??A9??

56E7: C6 43 00                      ; room=C6_6_HIGHWAY_TURNS, Length: 0x0043, Data: 0x00
;
56EA:    03 27                      ;   Section DESCRIPTION, Length: 0x0027
56EC:       0D 25                   ;     WHILE PASS, Length: 0x0025
56EE:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
56EF:          04 22                ;       PRINT, Length: 0x0022
56F1:             5F BE A3 15 31 6D 3B 4A 74 C0 8B 9A 3B 6E AB 98 ; 
5701:             79 68 56 90 DB 72 04 9A 53 BE 6B BF 5F BE F7 17 ; 
5711:             17 BA             ; 
;
;                 THE HIGHWAY TURNS GOING FROM THE NORTH TO THE WEST.
;
;
5713:    04 17                      ;   Section COMMANDS, Length: 0x0017
5715:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
5718:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5719:          02                   ;       ELSE go to: 0x571C
571A:             00 C7             ;         MOVE AND LOOK, room=C7_6_??C7??
571C:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
571D:          02                   ;       ELSE go to: 0x5720
571E:             00 C5             ;         MOVE AND LOOK, room=C5_6_??C5??
5720:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5721:          06                   ;       ELSE go to: 0x5728
5722:             0D 04             ;         WHILE PASS, Length: 0x0004
5724:                30 DE          ;           SET CURRENT ROOM, room=DE_5_HIGHWAY_LEADS
5726:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
5728:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5729:          02                   ;       ELSE go to: 0x572C
572A:             00 AA             ;         MOVE AND LOOK, room=AA_6_??AA??

572C: C7 1D 00                      ; room=C7_6_??C7??, Length: 0x001D, Data: 0x00
;
572F:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5731:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5732:    04 17                      ;   Section COMMANDS, Length: 0x0017
5734:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
5737:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5738:          02                   ;       ELSE go to: 0x573B
5739:             00 C8             ;         MOVE AND LOOK, room=C8_6_??C8??
573B:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
573C:          02                   ;       ELSE go to: 0x573F
573D:             00 C6             ;         MOVE AND LOOK, room=C6_6_HIGHWAY_TURNS
573F:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5740:          06                   ;       ELSE go to: 0x5747
5741:             0D 04             ;         WHILE PASS, Length: 0x0004
5743:                30 DF          ;           SET CURRENT ROOM, room=DF_5_??DF??
5745:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
5747:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5748:          02                   ;       ELSE go to: 0x574B
5749:             00 AB             ;         MOVE AND LOOK, room=AB_6_??AB??

574B: C8 1D 00                      ; room=C8_6_??C8??, Length: 0x001D, Data: 0x00
;
574E:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5750:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5751:    04 17                      ;   Section COMMANDS, Length: 0x0017
5753:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
5756:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5757:          02                   ;       ELSE go to: 0x575A
5758:             00 C9             ;         MOVE AND LOOK, room=C9_6_??C9??
575A:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
575B:          02                   ;       ELSE go to: 0x575E
575C:             00 C7             ;         MOVE AND LOOK, room=C7_6_??C7??
575E:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
575F:          06                   ;       ELSE go to: 0x5766
5760:             0D 04             ;         WHILE PASS, Length: 0x0004
5762:                30 E0          ;           SET CURRENT ROOM, room=E0_5_??E0??
5764:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
5766:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5767:          02                   ;       ELSE go to: 0x576A
5768:             00 AC             ;         MOVE AND LOOK, room=AC_6_??AC??

576A: C9 1D 00                      ; room=C9_6_??C9??, Length: 0x001D, Data: 0x00
;
576D:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
576F:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5770:    04 17                      ;   Section COMMANDS, Length: 0x0017
5772:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
5775:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5776:          02                   ;       ELSE go to: 0x5779
5777:             00 CA             ;         MOVE AND LOOK, room=CA_6_??CA??
5779:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
577A:          02                   ;       ELSE go to: 0x577D
577B:             00 C8             ;         MOVE AND LOOK, room=C8_6_??C8??
577D:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
577E:          06                   ;       ELSE go to: 0x5785
577F:             0D 04             ;         WHILE PASS, Length: 0x0004
5781:                30 E1          ;           SET CURRENT ROOM, room=E1_5_??E1??
5783:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
5785:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5786:          02                   ;       ELSE go to: 0x5789
5787:             00 AD             ;         MOVE AND LOOK, room=AD_6_??AD??

5789: CA 1D 00                      ; room=CA_6_??CA??, Length: 0x001D, Data: 0x00
;
578C:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
578E:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
578F:    04 17                      ;   Section COMMANDS, Length: 0x0017
5791:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
5794:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5795:          02                   ;       ELSE go to: 0x5798
5796:             00 CB             ;         MOVE AND LOOK, room=CB_6_??CB??
5798:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5799:          02                   ;       ELSE go to: 0x579C
579A:             00 C9             ;         MOVE AND LOOK, room=C9_6_??C9??
579C:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
579D:          06                   ;       ELSE go to: 0x57A4
579E:             0D 04             ;         WHILE PASS, Length: 0x0004
57A0:                30 E2          ;           SET CURRENT ROOM, room=E2_5_??E2??
57A2:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
57A4:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
57A5:          02                   ;       ELSE go to: 0x57A8
57A6:             00 AE             ;         MOVE AND LOOK, room=AE_6_??AE??

57A8: CB 19 00                      ; room=CB_6_??CB??, Length: 0x0019, Data: 0x00
;
57AB:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
57AD:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
57AE:    04 13                      ;   Section COMMANDS, Length: 0x0013
57B0:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
57B3:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
57B4:          02                   ;       ELSE go to: 0x57B7
57B5:             00 CC             ;         MOVE AND LOOK, room=CC_6_??CC??
57B7:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
57B8:          02                   ;       ELSE go to: 0x57BB
57B9:             00 CA             ;         MOVE AND LOOK, room=CA_6_??CA??
57BB:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
57BC:          02                   ;       ELSE go to: 0x57BF
57BD:             00 E3             ;         MOVE AND LOOK, room=E3_6_??E3??
57BF:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
57C0:          02                   ;       ELSE go to: 0x57C3
57C1:             00 AF             ;         MOVE AND LOOK, room=AF_6_??AF??

57C3: CC 19 00                      ; room=CC_6_??CC??, Length: 0x0019, Data: 0x00
;
57C6:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
57C8:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
57C9:    04 13                      ;   Section COMMANDS, Length: 0x0013
57CB:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
57CE:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
57CF:          02                   ;       ELSE go to: 0x57D2
57D0:             00 B2             ;         MOVE AND LOOK, room=B2_6_??B2??
57D2:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
57D3:          02                   ;       ELSE go to: 0x57D6
57D4:             00 CB             ;         MOVE AND LOOK, room=CB_6_??CB??
57D6:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
57D7:          02                   ;       ELSE go to: 0x57DA
57D8:             00 CD             ;         MOVE AND LOOK, room=CD_6_??CD??
57DA:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
57DB:          02                   ;       ELSE go to: 0x57DE
57DC:             00 B0             ;         MOVE AND LOOK, room=B0_6_SMALL_OASIS

57DE: CD 19 00                      ; room=CD_6_??CD??, Length: 0x0019, Data: 0x00
;
57E1:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
57E3:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
57E4:    04 13                      ;   Section COMMANDS, Length: 0x0013
57E6:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
57E9:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
57EA:          02                   ;       ELSE go to: 0x57ED
57EB:             00 B3             ;         MOVE AND LOOK, room=B3_6_??B3??
57ED:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
57EE:          02                   ;       ELSE go to: 0x57F1
57EF:             00 E3             ;         MOVE AND LOOK, room=E3_6_??E3??
57F1:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
57F2:          02                   ;       ELSE go to: 0x57F5
57F3:             00 CE             ;         MOVE AND LOOK, room=CE_6_??CE??
57F5:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
57F6:          02                   ;       ELSE go to: 0x57F9
57F7:             00 CC             ;         MOVE AND LOOK, room=CC_6_??CC??

57F9: CE 1C 00                      ; room=CE_6_??CE??, Length: 0x001C, Data: 0x00
;
57FC:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
57FE:       0D 02                   ;     WHILE PASS, Length: 0x0002
5800:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
5801:          9B                   ;       ROUTINE 0x9B PRINT_EMPTY_HIGHWAY
;
5802:    04 13                      ;   Section COMMANDS, Length: 0x0013
5804:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5807:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5808:          02                   ;       ELSE go to: 0x580B
5809:             00 B4             ;         MOVE AND LOOK, room=B4_6_??B4??
580B:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
580C:          02                   ;       ELSE go to: 0x580F
580D:             00 E4             ;         MOVE AND LOOK, room=E4_6_??E4??
580F:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5810:          02                   ;       ELSE go to: 0x5813
5811:             00 CF             ;         MOVE AND LOOK, room=CF_6_??CF??
5813:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5814:          02                   ;       ELSE go to: 0x5817
5815:             00 CD             ;         MOVE AND LOOK, room=CD_6_??CD??

5817: CF 19 00                      ; room=CF_6_??CF??, Length: 0x0019, Data: 0x00
;
581A:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
581C:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
581D:    04 13                      ;   Section COMMANDS, Length: 0x0013
581F:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5822:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5823:          02                   ;       ELSE go to: 0x5826
5824:             00 B5             ;         MOVE AND LOOK, room=B5_6_??B5??
5826:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5827:          02                   ;       ELSE go to: 0x582A
5828:             00 E5             ;         MOVE AND LOOK, room=E5_6_??E5??
582A:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
582B:          02                   ;       ELSE go to: 0x582E
582C:             00 D0             ;         MOVE AND LOOK, room=D0_6_??D0??
582E:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
582F:          02                   ;       ELSE go to: 0x5832
5830:             00 CE             ;         MOVE AND LOOK, room=CE_6_??CE??

5832: D0 19 00                      ; room=D0_6_??D0??, Length: 0x0019, Data: 0x00
;
5835:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5837:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5838:    04 13                      ;   Section COMMANDS, Length: 0x0013
583A:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
583D:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
583E:          02                   ;       ELSE go to: 0x5841
583F:             00 B6             ;         MOVE AND LOOK, room=B6_6_??B6??
5841:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5842:          02                   ;       ELSE go to: 0x5845
5843:             00 E6             ;         MOVE AND LOOK, room=E6_6_??E6??
5845:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5846:          02                   ;       ELSE go to: 0x5849
5847:             00 D1             ;         MOVE AND LOOK, room=D1_6_??D1??
5849:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
584A:          02                   ;       ELSE go to: 0x584D
584B:             00 CF             ;         MOVE AND LOOK, room=CF_6_??CF??

584D: D1 19 00                      ; room=D1_6_??D1??, Length: 0x0019, Data: 0x00
;
5850:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5852:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5853:    04 13                      ;   Section COMMANDS, Length: 0x0013
5855:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5858:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5859:          02                   ;       ELSE go to: 0x585C
585A:             00 B7             ;         MOVE AND LOOK, room=B7_6_??B7??
585C:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
585D:          02                   ;       ELSE go to: 0x5860
585E:             00 E7             ;         MOVE AND LOOK, room=E7_6_??E7??
5860:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5861:          02                   ;       ELSE go to: 0x5864
5862:             00 B8             ;         MOVE AND LOOK, room=B8_6_??B8??
5864:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5865:          02                   ;       ELSE go to: 0x5868
5866:             00 D0             ;         MOVE AND LOOK, room=D0_6_??D0??

5868: D2 1D 00                      ; room=D2_6_??D2??, Length: 0x001D, Data: 0x00
;
586B:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
586D:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
586E:    04 17                      ;   Section COMMANDS, Length: 0x0017
5870:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
5873:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5874:          02                   ;       ELSE go to: 0x5877
5875:             00 B8             ;         MOVE AND LOOK, room=B8_6_??B8??
5877:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5878:          06                   ;       ELSE go to: 0x587F
5879:             0D 04             ;         WHILE PASS, Length: 0x0004
587B:                30 D3          ;           SET CURRENT ROOM, room=D3_5_??D3??
587D:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
587F:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5880:          02                   ;       ELSE go to: 0x5883
5881:             00 B9             ;         MOVE AND LOOK, room=B9_6_??B9??
5883:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5884:          02                   ;       ELSE go to: 0x5887
5885:             00 E7             ;         MOVE AND LOOK, room=E7_6_??E7??

5887: E3 1D 00                      ; room=E3_6_??E3??, Length: 0x001D, Data: 0x00
;
588A:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
588C:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
588D:    04 17                      ;   Section COMMANDS, Length: 0x0017
588F:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
5892:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5893:          02                   ;       ELSE go to: 0x5896
5894:             00 CD             ;         MOVE AND LOOK, room=CD_6_??CD??
5896:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5897:          06                   ;       ELSE go to: 0x589E
5898:             0D 04             ;         WHILE PASS, Length: 0x0004
589A:                30 E2          ;           SET CURRENT ROOM, room=E2_5_??E2??
589C:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
589E:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
589F:          02                   ;       ELSE go to: 0x58A2
58A0:             00 E4             ;         MOVE AND LOOK, room=E4_6_??E4??
58A2:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
58A3:          02                   ;       ELSE go to: 0x58A6
58A4:             00 CB             ;         MOVE AND LOOK, room=CB_6_??CB??

58A6: E4 20 00                      ; room=E4_6_??E4??, Length: 0x0020, Data: 0x00
;
58A9:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
58AB:       0D 02                   ;     WHILE PASS, Length: 0x0002
58AD:          AB                   ;       ROUTINE 0xAB PRINT_STILL_IN_DESERT
58AE:          9B                   ;       ROUTINE 0x9B PRINT_EMPTY_HIGHWAY
;
58AF:    04 17                      ;   Section COMMANDS, Length: 0x0017
58B1:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
58B4:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
58B5:          02                   ;       ELSE go to: 0x58B8
58B6:             00 CE             ;         MOVE AND LOOK, room=CE_6_??CE??
58B8:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
58B9:          06                   ;       ELSE go to: 0x58C0
58BA:             0D 04             ;         WHILE PASS, Length: 0x0004
58BC:                30 F0          ;           SET CURRENT ROOM, room=F0_5_??F0??
58BE:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
58C0:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
58C1:          02                   ;       ELSE go to: 0x58C4
58C2:             00 E5             ;         MOVE AND LOOK, room=E5_6_??E5??
58C4:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
58C5:          02                   ;       ELSE go to: 0x58C8
58C6:             00 E3             ;         MOVE AND LOOK, room=E3_6_??E3??

58C8: E5 1D 00                      ; room=E5_6_??E5??, Length: 0x001D, Data: 0x00
;
58CB:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
58CD:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
58CE:    04 17                      ;   Section COMMANDS, Length: 0x0017
58D0:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
58D3:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
58D4:          02                   ;       ELSE go to: 0x58D7
58D5:             00 CF             ;         MOVE AND LOOK, room=CF_6_??CF??
58D7:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
58D8:          06                   ;       ELSE go to: 0x58DF
58D9:             0D 04             ;         WHILE PASS, Length: 0x0004
58DB:                30 F1          ;           SET CURRENT ROOM, room=F1_5_SMALL_TRAIL1
58DD:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
58DF:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
58E0:          02                   ;       ELSE go to: 0x58E3
58E1:             00 E6             ;         MOVE AND LOOK, room=E6_6_??E6??
58E3:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
58E4:          02                   ;       ELSE go to: 0x58E7
58E5:             00 E4             ;         MOVE AND LOOK, room=E4_6_??E4??

58E7: E6 1D 00                      ; room=E6_6_??E6??, Length: 0x001D, Data: 0x00
;
58EA:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
58EC:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
58ED:    04 17                      ;   Section COMMANDS, Length: 0x0017
58EF:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
58F2:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
58F3:          02                   ;       ELSE go to: 0x58F6
58F4:             00 D0             ;         MOVE AND LOOK, room=D0_6_??D0??
58F6:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
58F7:          06                   ;       ELSE go to: 0x58FE
58F8:             0D 04             ;         WHILE PASS, Length: 0x0004
58FA:                30 F2          ;           SET CURRENT ROOM, room=F2_5_TWISTY_TRAIL
58FC:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
58FE:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
58FF:          02                   ;       ELSE go to: 0x5902
5900:             00 E7             ;         MOVE AND LOOK, room=E7_6_??E7??
5902:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5903:          02                   ;       ELSE go to: 0x5906
5904:             00 E5             ;         MOVE AND LOOK, room=E5_6_??E5??

5906: E7 1D 00                      ; room=E7_6_??E7??, Length: 0x001D, Data: 0x00
;
5909:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
590B:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
590C:    04 17                      ;   Section COMMANDS, Length: 0x0017
590E:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: COM_0A_is_input_phrase(phrase_num)
5911:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5912:          02                   ;       ELSE go to: 0x5915
5913:             00 D1             ;         MOVE AND LOOK, room=D1_6_??D1??
5915:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5916:          06                   ;       ELSE go to: 0x591D
5917:             0D 04             ;         WHILE PASS, Length: 0x0004
5919:                30 E8          ;           SET CURRENT ROOM, room=E8_5_??E8??
591B:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
591D:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
591E:          02                   ;       ELSE go to: 0x5921
591F:             00 D2             ;         MOVE AND LOOK, room=D2_6_??D2??
5921:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5922:          02                   ;       ELSE go to: 0x5925
5923:             00 E6             ;         MOVE AND LOOK, room=E6_6_??E6??

5925: F7 19 00                      ; room=F7_6_??F7??, Length: 0x0019, Data: 0x00
;
5928:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
592A:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
592B:    04 13                      ;   Section COMMANDS, Length: 0x0013
592D:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5930:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5931:          02                   ;       ELSE go to: 0x5934
5932:             00 FA             ;         MOVE AND LOOK, room=FA_6_??FA??
5934:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5935:          02                   ;       ELSE go to: 0x5938
5936:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??
5938:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5939:          02                   ;       ELSE go to: 0x593C
593A:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??
593C:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
593D:          02                   ;       ELSE go to: 0x5940
593E:             00 F8             ;         MOVE AND LOOK, room=F8_6_??F8??

5940: F8 19 00                      ; room=F8_6_??F8??, Length: 0x0019, Data: 0x00
;
5943:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5945:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5946:    04 13                      ;   Section COMMANDS, Length: 0x0013
5948:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
594B:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
594C:          02                   ;       ELSE go to: 0x594F
594D:             00 F8             ;         MOVE AND LOOK, room=F8_6_??F8??
594F:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5950:          02                   ;       ELSE go to: 0x5953
5951:             00 F9             ;         MOVE AND LOOK, room=F9_6_??F9??
5953:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5954:          02                   ;       ELSE go to: 0x5957
5955:             00 F8             ;         MOVE AND LOOK, room=F8_6_??F8??
5957:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5958:          02                   ;       ELSE go to: 0x595B
5959:             00 F8             ;         MOVE AND LOOK, room=F8_6_??F8??

595B: F9 21 00                      ; room=F9_6_??F9??, Length: 0x0021, Data: 0x00
;
595E:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5960:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5961:    04 1B                      ;   Section COMMANDS, Length: 0x001B
5963:       0B 19 0A                ;     SWITCH, Length: 0x0019, Function to call: COM_0A_is_input_phrase(phrase_num)
5966:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
5967:          0A                   ;       ELSE go to: 0x5972
5968:             0E 08             ;         WHILE FAIL, Length: 0x0008
596A:                0D 04          ;           WHILE PASS, Length: 0x0004
596C:                   05 3E       ;             IS LESS OR EQUAL TO LAST RANDOM, Value: 0x3E
596E:                   00 86       ;             MOVE AND LOOK, room=86_6_??86??
5970:                00 F9          ;           MOVE AND LOOK, room=F9_6_??F9??
5972:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
5973:          02                   ;       ELSE go to: 0x5976
5974:             00 F8             ;         MOVE AND LOOK, room=F8_6_??F8??
5976:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5977:          02                   ;       ELSE go to: 0x597A
5978:             00 FA             ;         MOVE AND LOOK, room=FA_6_??FA??
597A:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
597B:          02                   ;       ELSE go to: 0x597E
597C:             00 F9             ;         MOVE AND LOOK, room=F9_6_??F9??

597E: FA 19 00                      ; room=FA_6_??FA??, Length: 0x0019, Data: 0x00
;
5981:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5983:       AB                      ;     ROUTINE 0xAB PRINT_STILL_IN_DESERT
;
5984:    04 13                      ;   Section COMMANDS, Length: 0x0013
5986:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: COM_0A_is_input_phrase(phrase_num)
5989:          03                   ;       COM_0A_is_input_phrase(03: "EAST     *          *           *")
598A:          02                   ;       ELSE go to: 0x598D
598B:             00 FA             ;         MOVE AND LOOK, room=FA_6_??FA??
598D:          04                   ;       COM_0A_is_input_phrase(04: "WEST     *          *           *")
598E:          02                   ;       ELSE go to: 0x5991
598F:             00 F7             ;         MOVE AND LOOK, room=F7_6_??F7??
5991:          01                   ;       COM_0A_is_input_phrase(01: "NORTH    *          *           *")
5992:          02                   ;       ELSE go to: 0x5995
5993:             00 FA             ;         MOVE AND LOOK, room=FA_6_??FA??
5995:          02                   ;       COM_0A_is_input_phrase(02: "SOUTH    *          *           *")
5996:          02                   ;       ELSE go to: 0x5999
5997:             00 F9             ;         MOVE AND LOOK, room=F9_6_??F9??
```

```code
5999: 06 E8 1D 00 03 01 AB 04 17 0B 15 0A 03 06 0D 04 ; ................
59A9: 30 E7 2F 06 04 02 00 E9 01 02 00 D3 02 02 00 F2 ; 0./.............
59B9: E9 1C 00 03 04 0D 02 AB 95 04 13 0B 11 0A 03 02 ; ................
59C9: 00 D4 04 02 00 F3 01 02 00 EA 02 02 00 E8 EA 19 ; ................
59D9: 00 03 01 AB 04 13 0B 11 0A 03 02 00 E9 04 02 00 ; ................
59E9: EB 01 02 00 D7 02 02 00 F4 EB 1C 00 03 04 0D 02 ; ................
59F9: AB 95 04 13 0B 11 0A 03 02 00 EC 04 02 00 D8 01 ; ................
5A09: 02 00 EA 02 02 00 DA EC 1C 00 03 04 0D 02 AB 95 ; ................
5A19: 04 13 0B 11 0A 03 02 00 F4 04 02 00 EB 01 02 00 ; ................
5A29: EA 02 02 00 DC ED 19 00 03 01 AB 04 13 0B 11 0A ; ................
5A39: 03 02 00 F5 04 02 00 DC 01 02 00 EC 02 02 00 EE ; ................
5A49: EE 1C 00 03 04 0D 02 AB 9B 04 13 0B 11 0A 03 02 ; ................
5A59: 00 EF 04 02 00 DD 01 02 00 ED 02 02 00 DF EF 24 ; ...............$
5A69: 00 03 04 0D 02 AB 9B 04 1B 0B 19 0A 03 0A 0D 08 ; ................
5A79: C8 30 80 17 9D 00 2F 01 04 02 00 EE 01 02 00 F5 ; .0..../.........
5A89: 02 02 00 E0 F0 28 00 03 04 0D 02 9B AB 04 1F 0B ; .....(..........
5A99: 1D 0A 03 06 0D 04 30 E4 2F 06 04 0A 0D 08 C8 30 ; ......0./......0
5AA9: B4 17 9D 00 2F 04 01 02 00 F1 02 02 00 E2 F1 3F ; ..../..........?
5AB9: 00 03 23 0D 21 AB 04 1E 55 45 8E 91 16 8A CB B0 ; ..#.!...UE......
5AC9: 0E 8A 86 5F D9 B5 66 62 90 14 10 58 BE A0 08 71 ; ..._..fb...X...q
5AD9: FF B2 9F 15 7F B1 04 17 0B 15 0A 03 06 0D 04 30 ; ...............0
5AE9: E5 2F 06 04 02 00 F6 01 02 00 F2 02 02 00 F0 F2 ; ./..............
5AF9: 41 00 03 25 0D 23 AB 04 20 55 45 8E 91 16 8A 55 ; A..%.#.. UE....U
5B09: D1 FB C0 EB BF 33 7A E3 8B 0B 5C B5 D0 03 BC 33 ; .....3z...\....3
5B19: 98 47 B9 53 BE F4 72 DB 63 04 17 0B 15 0A 03 06 ; .G.S..r.c.......
5B29: 0D 04 30 E6 2F 06 04 02 00 F3 01 02 00 E8 02 02 ; ..0./...........
5B39: 00 F1 F3 35 00 03 1D 0D 1B AB 95 04 17 5F BE 8C ; ...5........._..
5B49: 17 CE 47 8E 14 2B B9 04 68 CB 87 6B BF 5F BE 61 ; ..G..+..h..k._.a
5B59: 17 82 C6 2E 04 13 0B 11 0A 03 02 00 E9 04 02 00 ; ................
5B69: F4 01 02 00 EA 02 02 00 F1 F4 1C 00 03 04 0D 02 ; ................
5B79: AB 95 04 13 0B 11 0A 03 02 00 F3 04 02 00 EC 01 ; ................
5B89: 02 00 EA 02 02 00 F5 F5 19 00 03 01 AB 04 13 0B ; ................
5B99: 11 0A 03 02 00 F6 04 02 00 ED 01 02 00 F4 02 02 ; ................
5BA9: 00 EF F6 45 00 03 25 0D 23 AB 04 20 55 45 8E 91 ; ...E..%.#.. UE..
5BB9: 16 8A CB B0 0E 8A 86 5F C8 B5 FF B2 82 17 55 5E ; ......._......U^
5BC9: 36 A1 16 71 D6 9C DB 72 95 5F 9B C1 04 1B 0B 19 ; 6..q...r._......
5BD9: 0A 03 02 00 F1 04 02 00 F5 01 02 00 F3 02 0A 0D ; ................
5BE9: 08 C8 30 B7 17 9D 00 2F 02 F7 19 00 03 01 AB 04 ; ..0..../........
5BF9: 13 0B 11 0A 03 02 00 FA 04 02 00 F7 01 02 00 F7 ; ................
5C09: 02 02 00 F8 F8 19 00 03 01 AB 04 13 0B 11 0A 03 ; ................
5C19: 02 00 F8 04 02 00 F9 01 02 00 F8 02 02 00 F8 F9 ; ................
5C29: 21 00 03 01 AB 04 1B 0B 19 0A 03 0A 0E 08 0D 04 ; !...............
5C39: 05 3E 00 86 00 F9 04 02 00 F8 01 02 00 FA 02 02 ; .>..............
5C49: 00 F9 FA 19 00 03 01 AB 04 13 0B 11 0A 03 02 00 ; ................
5C59: FA 04 02 00 F7 01 02 00 FA 02 02 00 F9 4C 41 54 ; .............LAT
5C69: 22 05 53 50 41 52 45 23 04 42 4C 55 45 0D 06 4D ; ".SPARE#.BLUE..M
5C79: 41 53 53 49 56 3F 04 42 41 4E 4B 40 06 53 41 4C ; ASSIV?.BANK@.SAL
5C89: 4F 4F 4E 41 06 53 48 45 52 49 46 42 06 4F 46 46 ; OONA.SHERIFB.OFF
5C99: 49 43 45 42 06 53 4C 49 4D 27 53 43 05 53 4C 49 ; ICEB.SLIM'SC.SLI
5CA9: 4D 53 43 05 42 4F 42 27 53 44 04 42 4F 42 53 44 ; MSC.BOB'SD.BOBSD
5CB9: 06 44 4F 55 42 4C 45 45 05 48 4F 54 45 4C 47 06 ; .DOUBLEE.HOTELG.
5CC9: 53 57 49 4E 47 49 46 04 54 53 4F 4D 6B 04 43 4F ; SWINGIF.TSOMk.CO
5CD9: 4F 4C 72 05 43 4C 45 41 52 74 05 42 52 4F 57 4E ; OLr.CLEARt.BROWN
5CE9: 73 00 02 54 4F 01 04 57 49 54 48 02 05 55 53 49 ; s..TO..WITH..USI
5CF9: 4E 47 02 02 41 54 03 05 
```

