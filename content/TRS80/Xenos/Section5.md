![Xenos](Xenos.png)

# Xenos SECTION5.DAT

>>> cpu Z80

>>> binary 5200:roms/section5.bin

```code
5200: 00 8A 63                      ; List ID: 0x00, Length: 0x0A63

5203: 98 1D 00                      ; Room Number: 0x98, Length: 0x001D, Data: 0x00
;
5206:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5208:       AB                      ;     COMMAND 0xAB
;
5209:    04 17                      ;   Section COMMANDS, Length: 0x0017
520B:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
520E:          03                   ;       Phrase number: 0x03
520F:          06                   ;       ELSE go to: 0x5216
5210:             0D 04             ;         WHILE PASS, Length: 0x0004
5212:                30 97          ;           UNKNOWN1, Data: 0x97
5214:                2F 06          ;           UNKNOWN2 Data: 0x06
5216:          04                   ;       Phrase number: 0x04
5217:          02                   ;       ELSE go to: 0x521A
5218:             00 BB             ;         MOVE AND LOOK, Destination room: 0xBB
521A:          01                   ;       Phrase number: 0x01
521B:          02                   ;       ELSE go to: 0x521E
521C:             00 99             ;         MOVE AND LOOK, Destination room: 0x99
521E:          02                   ;       Phrase number: 0x02
521F:          02                   ;       ELSE go to: 0x5222
5220:             00 BA             ;         MOVE AND LOOK, Destination room: 0xBA

5222: 99 1A 00                      ; Room Number: 0x99, Length: 0x001A, Data: 0x00
;
5225:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5227:       0D 02                   ;     WHILE PASS, Length: 0x0002
5229:          AB                   ;       COMMAND 0xAB
522A:          96                   ;       COMMAND 0x96
;
522B:    04 11                      ;   Section COMMANDS, Length: 0x0011
522D:       0B 0F 0A                ;     SWITCH, Length: 0x000F, Function to call: 0x0A
5230:          03                   ;       Phrase number: 0x03
5231:          01                   ;       ELSE go to: 0x5233
5232:             97                ;         COMMAND 0x97
5233:          04                   ;       Phrase number: 0x04
5234:          02                   ;       ELSE go to: 0x5237
5235:             00 9A             ;         MOVE AND LOOK, Destination room: 0x9A
5237:          01                   ;       Phrase number: 0x01
5238:          01                   ;       ELSE go to: 0x523A
5239:             97                ;         COMMAND 0x97
523A:          02                   ;       Phrase number: 0x02
523B:          02                   ;       ELSE go to: 0x523E
523C:             00 98             ;         MOVE AND LOOK, Destination room: 0x98

523E: 9A 1A 00                      ; Room Number: 0x9A, Length: 0x001A, Data: 0x00
;
5241:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5243:       0D 02                   ;     WHILE PASS, Length: 0x0002
5245:          AB                   ;       COMMAND 0xAB
5246:          96                   ;       COMMAND 0x96
;
5247:    04 11                      ;   Section COMMANDS, Length: 0x0011
5249:       0B 0F 0A                ;     SWITCH, Length: 0x000F, Function to call: 0x0A
524C:          03                   ;       Phrase number: 0x03
524D:          02                   ;       ELSE go to: 0x5250
524E:             00 99             ;         MOVE AND LOOK, Destination room: 0x99
5250:          04                   ;       Phrase number: 0x04
5251:          01                   ;       ELSE go to: 0x5253
5252:             97                ;         COMMAND 0x97
5253:          01                   ;       Phrase number: 0x01
5254:          01                   ;       ELSE go to: 0x5256
5255:             97                ;         COMMAND 0x97
5256:          02                   ;       Phrase number: 0x02
5257:          02                   ;       ELSE go to: 0x525A
5258:             00 BB             ;         MOVE AND LOOK, Destination room: 0xBB

525A: 9B 62 00                      ; Room Number: 0x9B, Length: 0x0062, Data: 0x00
;
525D:    03 45                      ;   Section DESCRIPTION, Length: 0x0045
525F:       04 43                   ;     PRINT, Length: 0x0043
;
; YOU ARE ON A NARROW PATH THAT LEADS DOWN THE FACE OF THE CLIFF TO THE NORTH. IT IS VERY TREACHEROUS!
;
5261:          C7 DE 94 14 51 5E 83 96 8B 16 79 B3 D2 CE 82 49 ; 
5271:          82 17 73 49 E3 8B 0B 5C 89 5B 96 96 DB 72 C5 65 ; 
5281:          51 5E 96 64 DB 72 C3 54 83 66 6B BF 5F BE 99 16 ; 
5291:          C2 B3 4B F4 0B BC D8 B5 43 62 8C 17 85 5F F4 72 ; 
52A1:          35 A1 21             ; 
;
52A4:    04 18                      ;   Section COMMANDS, Length: 0x0018
52A6:       0B 16 0A                ;     SWITCH, Length: 0x0016, Function to call: 0x0A
52A9:          03                   ;       Phrase number: 0x03
52AA:          01                   ;       ELSE go to: 0x52AC
52AB:             99                ;         COMMAND 0x99
52AC:          04                   ;       Phrase number: 0x04
52AD:          01                   ;       ELSE go to: 0x52AF
52AE:             99                ;         COMMAND 0x99
52AF:          01                   ;       Phrase number: 0x01
52B0:          09                   ;       ELSE go to: 0x52BA
52B1:             0E 07             ;         WHILE FAIL, Length: 0x0007
52B3:                0D 04          ;           WHILE PASS, Length: 0x0004
52B5:                   05 F0       ;             IS LESS OR EQUAL TO LAST RANDOM, Value: 0xF0
52B7:                   00 9C       ;             MOVE AND LOOK, Destination room: 0x9C
52B9:                99             ;           COMMAND 0x99
52BA:          02                   ;       Phrase number: 0x02
52BB:          02                   ;       ELSE go to: 0x52BE
52BC:             00 BC             ;         MOVE AND LOOK, Destination room: 0xBC

52BE: 9C 68 00                      ; Room Number: 0x9C, Length: 0x0068, Data: 0x00
;
52C1:    03 52                      ;   Section DESCRIPTION, Length: 0x0052
52C3:       04 50                   ;     PRINT, Length: 0x0050
;
; YOU ARE NOW ON THE CANYON FLOOR. TO THE WEST YOU CAN SEE A LARGE CRATER WITH A CYLINDRICAL METALIC OBJECT RESTING IN IT.
;
52C5:          C7 DE 94 14 50 5E 6B A1 03 A0 5F BE D3 14 91 9B ; 
52D5:          88 96 81 8D 1B B5 6B BF 5F BE F7 17 F3 B9 C7 DE ; 
52E5:          D3 14 95 96 1B 60 4E 45 31 49 45 5E D6 B0 23 62 ; 
52F5:          56 D1 03 71 EB 14 90 8C F3 5B 0E 53 67 16 4E BD ; 
5305:          CB 78 34 9E E6 5F 2F 17 03 BA AB 98 83 7A 97 7B ; 
;
5315:    04 11                      ;   Section COMMANDS, Length: 0x0011
5317:       0B 0F 0A                ;     SWITCH, Length: 0x000F, Function to call: 0x0A
531A:          03                   ;       Phrase number: 0x03
531B:          01                   ;       ELSE go to: 0x531D
531C:             9A                ;         COMMAND 0x9A
531D:          04                   ;       Phrase number: 0x04
531E:          02                   ;       ELSE go to: 0x5321
531F:             00 9D             ;         MOVE AND LOOK, Destination room: 0x9D
5321:          01                   ;       Phrase number: 0x01
5322:          01                   ;       ELSE go to: 0x5324
5323:             9A                ;         COMMAND 0x9A
5324:          02                   ;       Phrase number: 0x02
5325:          02                   ;       ELSE go to: 0x5328
5326:             00 9B             ;         MOVE AND LOOK, Destination room: 0x9B

5328: 9D 80 B3 00                   ; Room Number: 0x9D, Length: 0x00B3, Data: 0x00
;
532C:    03 37                      ;   Section DESCRIPTION, Length: 0x0037
532E:       04 35                   ;     PRINT, Length: 0x0035
;
; YOU ARE NOW IN THE CRATER WHERE A UFO HAS LANDED! THE CRATER OPENS TO THE EAST.
;
5330:          C7 DE 94 14 50 5E 6B A1 83 7A 5F BE E4 14 7F 49 ; 
5340:          99 AF F4 72 43 5E A8 17 CA 9C 4B 49 50 8B E6 59 ; 
5350:          D6 06 DB 72 AB 55 F4 BD C2 16 9D 61 89 17 82 17 ; 
5360:          47 5E 66 49 2E       ; 
;
5365:    04 77                      ;   Section COMMANDS, Length: 0x0077
5367:       0B 75 0A                ;     SWITCH, Length: 0x0075, Function to call: 0x0A
536A:          04                   ;       Phrase number: 0x04
536B:          2D                   ;       ELSE go to: 0x5399
536C:             0E 2B             ;         WHILE FAIL, Length: 0x002B
536E:                0D 20          ;           WHILE PASS, Length: 0x0020
5370:                   01 4E       ;             IS IN PACK OR CURRENT ROOM, Object number: 0x4E
5372:                   04 1C       ;             PRINT, Length: 0x001C
;
; THE BOULDER BLOCKS PASSAGE INTO THE SHIP. 
;
5374:                      5F BE B9 14 3E C5 23 62 89 4E A5 54 DB 16 D3 B9 ; 
5384:                      9B 6C 9E 7A D6 9C DB 72 23 B8 9B A8 ; 
5390:                0D 07          ;           WHILE PASS, Length: 0x0007
5392:                   30 80       ;             UNKNOWN1, Data: 0x80
5394:                   17 9D 00    ;             MOVE TO, Object number: 0x9D, Destination room: 0x00
5397:                   2F 07       ;             UNKNOWN2 Data: 0x07
5399:          36                   ;       Phrase number: 0x36
539A:          39                   ;       ELSE go to: 0x53D4
539B:             0E 37             ;         WHILE FAIL, Length: 0x0037
539D:                0D 26          ;           WHILE PASS, Length: 0x0026
539F:                   0E 04       ;             WHILE FAIL, Length: 0x0004
53A1:                      09 00    ;               COMPARE TO SECOND NOUN, Word number: 0x00
53A3:                      09 99    ;               COMPARE TO SECOND NOUN, Word number: 0x99
53A5:                   01 4E       ;             IS IN PACK OR CURRENT ROOM, Object number: 0x4E
53A7:                   04 1C       ;             PRINT, Length: 0x001C
;
; THE BOULDER BLOCKS PASSAGE INTO THE SHIP. 
;
53A9:                      5F BE B9 14 3E C5 23 62 89 4E A5 54 DB 16 D3 B9 ; 
53B9:                      9B 6C 9E 7A D6 9C DB 72 23 B8 9B A8 ; 
53C5:                0D 0D          ;           WHILE PASS, Length: 0x000D
53C7:                   0E 04       ;             WHILE FAIL, Length: 0x0004
53C9:                      09 00    ;               COMPARE TO SECOND NOUN, Word number: 0x00
53CB:                      09 99    ;               COMPARE TO SECOND NOUN, Word number: 0x99
53CD:                   30 80       ;             UNKNOWN1, Data: 0x80
53CF:                   17 9D 00    ;             MOVE TO, Object number: 0x9D, Destination room: 0x00
53D2:                   2F 07       ;             UNKNOWN2 Data: 0x07
53D4:          01                   ;       Phrase number: 0x01
53D5:          01                   ;       ELSE go to: 0x53D7
53D6:             9A                ;         COMMAND 0x9A
53D7:          02                   ;       Phrase number: 0x02
53D8:          01                   ;       ELSE go to: 0x53DA
53D9:             9A                ;         COMMAND 0x9A
53DA:          03                   ;       Phrase number: 0x03
53DB:          02                   ;       ELSE go to: 0x53DE
53DC:             00 9C             ;         MOVE AND LOOK, Destination room: 0x9C

53DE: 9E 59 00                      ; Room Number: 0x9E, Length: 0x0059, Data: 0x00
;
53E1:    03 42                      ;   Section DESCRIPTION, Length: 0x0042
53E3:       0D 40                   ;     WHILE PASS, Length: 0x0040
53E5:          AB                   ;       COMMAND 0xAB
53E6:          96                   ;       COMMAND 0x96
53E7:          04 3C                ;       PRINT, Length: 0x003C
;
; STRANGE FOOTPRINTS LEAD SOUTH FROM HERE. THEY SEEM TO ORIGINATE AT THE EDGE OF THE CANYON.
;
53E9:             0C BA 91 48 48 5E 46 A0 F3 A6 CD 9A 3F 16 F3 46 ; 
53F9:             47 B9 53 BE 79 68 4A 90 2F 62 56 F4 FB 72 57 17 ; 
5409:             5B 61 6B BF B3 A0 50 6D 7F 49 96 14 82 17 47 5E ; 
5419:             37 5A B8 16 82 17 45 5E A3 48 27 A0 ; 
;
5425:    04 12                      ;   Section COMMANDS, Length: 0x0012
5427:       0B 10 0A                ;     SWITCH, Length: 0x0010, Function to call: 0x0A
542A:          03                   ;       Phrase number: 0x03
542B:          02                   ;       ELSE go to: 0x542E
542C:             00 BC             ;         MOVE AND LOOK, Destination room: 0xBC
542E:          04                   ;       Phrase number: 0x04
542F:          02                   ;       ELSE go to: 0x5432
5430:             00 9F             ;         MOVE AND LOOK, Destination room: 0x9F
5432:          01                   ;       Phrase number: 0x01
5433:          01                   ;       ELSE go to: 0x5435
5434:             97                ;         COMMAND 0x97
5435:          02                   ;       Phrase number: 0x02
5436:          02                   ;       ELSE go to: 0x5439
5437:             00 BD             ;         MOVE AND LOOK, Destination room: 0xBD

5439: 9F 1A 00                      ; Room Number: 0x9F, Length: 0x001A, Data: 0x00
;
543C:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
543E:       0D 02                   ;     WHILE PASS, Length: 0x0002
5440:          AB                   ;       COMMAND 0xAB
5441:          96                   ;       COMMAND 0x96
;
5442:    04 11                      ;   Section COMMANDS, Length: 0x0011
5444:       0B 0F 0A                ;     SWITCH, Length: 0x000F, Function to call: 0x0A
5447:          03                   ;       Phrase number: 0x03
5448:          02                   ;       ELSE go to: 0x544B
5449:             00 9E             ;         MOVE AND LOOK, Destination room: 0x9E
544B:          04                   ;       Phrase number: 0x04
544C:          01                   ;       ELSE go to: 0x544E
544D:             97                ;         COMMAND 0x97
544E:          01                   ;       Phrase number: 0x01
544F:          01                   ;       ELSE go to: 0x5451
5450:             97                ;         COMMAND 0x97
5451:          02                   ;       Phrase number: 0x02
5452:          02                   ;       ELSE go to: 0x5455
5453:             00 BE             ;         MOVE AND LOOK, Destination room: 0xBE

5455: A0 44 00                      ; Room Number: 0xA0, Length: 0x0044, Data: 0x00
;
5458:    03 2E                      ;   Section DESCRIPTION, Length: 0x002E
545A:       0D 2C                   ;     WHILE PASS, Length: 0x002C
545C:          AB                   ;       COMMAND 0xAB
545D:          96                   ;       COMMAND 0x96
545E:          04 28                ;       PRINT, Length: 0x0028
;
; SOMEWHAT ERRATIC FOOTPRINTS LEAD FROM THE EAST TO THE SOUTH.
;
5460:             3F B9 FA 62 73 49 3C 62 83 49 C8 51 46 A0 F3 A6 ; 
5470:             CD 9A 3F 16 F3 46 79 68 56 90 DB 72 95 5F 16 BC ; 
5480:             D6 9C DB 72 47 B9 77 BE ; 
;
5488:    04 11                      ;   Section COMMANDS, Length: 0x0011
548A:       0B 0F 0A                ;     SWITCH, Length: 0x000F, Function to call: 0x0A
548D:          03                   ;       Phrase number: 0x03
548E:          02                   ;       ELSE go to: 0x5491
548F:             00 BE             ;         MOVE AND LOOK, Destination room: 0xBE
5491:          04                   ;       Phrase number: 0x04
5492:          01                   ;       ELSE go to: 0x5494
5493:             97                ;         COMMAND 0x97
5494:          01                   ;       Phrase number: 0x01
5495:          01                   ;       ELSE go to: 0x5497
5496:             97                ;         COMMAND 0x97
5497:          02                   ;       Phrase number: 0x02
5498:          02                   ;       ELSE go to: 0x549B
5499:             00 BF             ;         MOVE AND LOOK, Destination room: 0xBF

549B: A1 3F 00                      ; Room Number: 0xA1, Length: 0x003F, Data: 0x00
;
549E:    03 28                      ;   Section DESCRIPTION, Length: 0x0028
54A0:       0D 26                   ;     WHILE PASS, Length: 0x0026
54A2:          AB                   ;       COMMAND 0xAB
54A3:          96                   ;       COMMAND 0x96
54A4:          04 22                ;       PRINT, Length: 0x0022
;
; WEAVING FOOTPRINTS LEAD FROM THE EAST TO THE SOUTH.
;
54A6:             A3 D0 10 CB C8 6A 46 A0 F3 A6 CD 9A 3F 16 F3 46 ; 
54B6:             79 68 56 90 DB 72 95 5F 16 BC D6 9C DB 72 47 B9 ; 
54C6:             77 BE             ; 
;
54C8:    04 12                      ;   Section COMMANDS, Length: 0x0012
54CA:       0B 10 0A                ;     SWITCH, Length: 0x0010, Function to call: 0x0A
54CD:          03                   ;       Phrase number: 0x03
54CE:          02                   ;       ELSE go to: 0x54D1
54CF:             00 BF             ;         MOVE AND LOOK, Destination room: 0xBF
54D1:          04                   ;       Phrase number: 0x04
54D2:          02                   ;       ELSE go to: 0x54D5
54D3:             00 A3             ;         MOVE AND LOOK, Destination room: 0xA3
54D5:          01                   ;       Phrase number: 0x01
54D6:          01                   ;       ELSE go to: 0x54D8
54D7:             97                ;         COMMAND 0x97
54D8:          02                   ;       Phrase number: 0x02
54D9:          02                   ;       ELSE go to: 0x54DC
54DA:             00 A2             ;         MOVE AND LOOK, Destination room: 0xA2

54DC: A2 40 00                      ; Room Number: 0xA2, Length: 0x0040, Data: 0x00
;
54DF:    03 28                      ;   Section DESCRIPTION, Length: 0x0028
54E1:       0D 26                   ;     WHILE PASS, Length: 0x0026
54E3:          AB                   ;       COMMAND 0xAB
54E4:          04 23                ;       PRINT, Length: 0x0023
;
; STRANGE FOOTPRINTS WEAVE FROM THE NORTH TO THE EAST.
;
54E6:             0C BA 91 48 48 5E 46 A0 F3 A6 CD 9A F7 17 CF 49 ; 
54F6:             5C 15 DB 9F 5F BE 99 16 C2 B3 89 17 82 17 47 5E ; 
5506:             66 49 2E          ; 
;
5509:    04 13                      ;   Section COMMANDS, Length: 0x0013
550B:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
550E:          03                   ;       Phrase number: 0x03
550F:          02                   ;       ELSE go to: 0x5512
5510:             00 C0             ;         MOVE AND LOOK, Destination room: 0xC0
5512:          04                   ;       Phrase number: 0x04
5513:          02                   ;       ELSE go to: 0x5516
5514:             00 A4             ;         MOVE AND LOOK, Destination room: 0xA4
5516:          01                   ;       Phrase number: 0x01
5517:          02                   ;       ELSE go to: 0x551A
5518:             00 A1             ;         MOVE AND LOOK, Destination room: 0xA1
551A:          02                   ;       Phrase number: 0x02
551B:          02                   ;       ELSE go to: 0x551E
551C:             00 A3             ;         MOVE AND LOOK, Destination room: 0xA3

551E: A3 19 00                      ; Room Number: 0xA3, Length: 0x0019, Data: 0x00
;
5521:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5523:       AB                      ;     COMMAND 0xAB
;
5524:    04 13                      ;   Section COMMANDS, Length: 0x0013
5526:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5529:          03                   ;       Phrase number: 0x03
552A:          02                   ;       ELSE go to: 0x552D
552B:             00 C1             ;         MOVE AND LOOK, Destination room: 0xC1
552D:          04                   ;       Phrase number: 0x04
552E:          02                   ;       ELSE go to: 0x5531
552F:             00 C3             ;         MOVE AND LOOK, Destination room: 0xC3
5531:          01                   ;       Phrase number: 0x01
5532:          02                   ;       ELSE go to: 0x5535
5533:             00 A2             ;         MOVE AND LOOK, Destination room: 0xA2
5535:          02                   ;       Phrase number: 0x02
5536:          02                   ;       ELSE go to: 0x5539
5537:             00 A4             ;         MOVE AND LOOK, Destination room: 0xA4

5539: A4 19 00                      ; Room Number: 0xA4, Length: 0x0019, Data: 0x00
;
553C:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
553E:       AB                      ;     COMMAND 0xAB
;
553F:    04 13                      ;   Section COMMANDS, Length: 0x0013
5541:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5544:          03                   ;       Phrase number: 0x03
5545:          02                   ;       ELSE go to: 0x5548
5546:             00 C2             ;         MOVE AND LOOK, Destination room: 0xC2
5548:          04                   ;       Phrase number: 0x04
5549:          02                   ;       ELSE go to: 0x554C
554A:             00 C4             ;         MOVE AND LOOK, Destination room: 0xC4
554C:          01                   ;       Phrase number: 0x01
554D:          02                   ;       ELSE go to: 0x5550
554E:             00 A3             ;         MOVE AND LOOK, Destination room: 0xA3
5550:          02                   ;       Phrase number: 0x02
5551:          02                   ;       ELSE go to: 0x5554
5552:             00 A5             ;         MOVE AND LOOK, Destination room: 0xA5

5554: A5 19 00                      ; Room Number: 0xA5, Length: 0x0019, Data: 0x00
;
5557:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5559:       AB                      ;     COMMAND 0xAB
;
555A:    04 13                      ;   Section COMMANDS, Length: 0x0013
555C:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
555F:          03                   ;       Phrase number: 0x03
5560:          02                   ;       ELSE go to: 0x5563
5561:             00 C3             ;         MOVE AND LOOK, Destination room: 0xC3
5563:          04                   ;       Phrase number: 0x04
5564:          02                   ;       ELSE go to: 0x5567
5565:             00 C2             ;         MOVE AND LOOK, Destination room: 0xC2
5567:          01                   ;       Phrase number: 0x01
5568:          02                   ;       ELSE go to: 0x556B
5569:             00 A4             ;         MOVE AND LOOK, Destination room: 0xA4
556B:          02                   ;       Phrase number: 0x02
556C:          02                   ;       ELSE go to: 0x556F
556D:             00 A6             ;         MOVE AND LOOK, Destination room: 0xA6

556F: A6 1D 00                      ; Room Number: 0xA6, Length: 0x001D, Data: 0x00
;
5572:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5574:       AB                      ;     COMMAND 0xAB
;
5575:    04 17                      ;   Section COMMANDS, Length: 0x0017
5577:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
557A:          03                   ;       Phrase number: 0x03
557B:          02                   ;       ELSE go to: 0x557E
557C:             00 C4             ;         MOVE AND LOOK, Destination room: 0xC4
557E:          04                   ;       Phrase number: 0x04
557F:          02                   ;       ELSE go to: 0x5582
5580:             00 C3             ;         MOVE AND LOOK, Destination room: 0xC3
5582:          01                   ;       Phrase number: 0x01
5583:          02                   ;       ELSE go to: 0x5586
5584:             00 A5             ;         MOVE AND LOOK, Destination room: 0xA5
5586:          02                   ;       Phrase number: 0x02
5587:          06                   ;       ELSE go to: 0x558E
5588:             0D 04             ;         WHILE PASS, Length: 0x0004
558A:                30 A7          ;           UNKNOWN1, Data: 0xA7
558C:                2F 06          ;           UNKNOWN2 Data: 0x06

558E: BA 1D 00                      ; Room Number: 0xBA, Length: 0x001D, Data: 0x00
;
5591:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5593:       AB                      ;     COMMAND 0xAB
;
5594:    04 17                      ;   Section COMMANDS, Length: 0x0017
5596:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
5599:          03                   ;       Phrase number: 0x03
559A:          06                   ;       ELSE go to: 0x55A1
559B:             0D 04             ;         WHILE PASS, Length: 0x0004
559D:                30 B9          ;           UNKNOWN1, Data: 0xB9
559F:                2F 06          ;           UNKNOWN2 Data: 0x06
55A1:          04                   ;       Phrase number: 0x04
55A2:          02                   ;       ELSE go to: 0x55A5
55A3:             00 D5             ;         MOVE AND LOOK, Destination room: 0xD5
55A5:          01                   ;       Phrase number: 0x01
55A6:          02                   ;       ELSE go to: 0x55A9
55A7:             00 98             ;         MOVE AND LOOK, Destination room: 0x98
55A9:          02                   ;       Phrase number: 0x02
55AA:          02                   ;       ELSE go to: 0x55AD
55AB:             00 D3             ;         MOVE AND LOOK, Destination room: 0xD3

55AD: BB 19 00                      ; Room Number: 0xBB, Length: 0x0019, Data: 0x00
;
55B0:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
55B2:       AB                      ;     COMMAND 0xAB
;
55B3:    04 13                      ;   Section COMMANDS, Length: 0x0013
55B5:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
55B8:          03                   ;       Phrase number: 0x03
55B9:          02                   ;       ELSE go to: 0x55BC
55BA:             00 98             ;         MOVE AND LOOK, Destination room: 0x98
55BC:          04                   ;       Phrase number: 0x04
55BD:          02                   ;       ELSE go to: 0x55C0
55BE:             00 BC             ;         MOVE AND LOOK, Destination room: 0xBC
55C0:          01                   ;       Phrase number: 0x01
55C1:          02                   ;       ELSE go to: 0x55C4
55C2:             00 9A             ;         MOVE AND LOOK, Destination room: 0x9A
55C4:          02                   ;       Phrase number: 0x02
55C5:          02                   ;       ELSE go to: 0x55C8
55C6:             00 D5             ;         MOVE AND LOOK, Destination room: 0xD5

55C8: BC 19 00                      ; Room Number: 0xBC, Length: 0x0019, Data: 0x00
;
55CB:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
55CD:       AB                      ;     COMMAND 0xAB
;
55CE:    04 13                      ;   Section COMMANDS, Length: 0x0013
55D0:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
55D3:          03                   ;       Phrase number: 0x03
55D4:          02                   ;       ELSE go to: 0x55D7
55D5:             00 BB             ;         MOVE AND LOOK, Destination room: 0xBB
55D7:          04                   ;       Phrase number: 0x04
55D8:          02                   ;       ELSE go to: 0x55DB
55D9:             00 9E             ;         MOVE AND LOOK, Destination room: 0x9E
55DB:          01                   ;       Phrase number: 0x01
55DC:          02                   ;       ELSE go to: 0x55DF
55DD:             00 9B             ;         MOVE AND LOOK, Destination room: 0x9B
55DF:          02                   ;       Phrase number: 0x02
55E0:          02                   ;       ELSE go to: 0x55E3
55E1:             00 D6             ;         MOVE AND LOOK, Destination room: 0xD6

55E3: BD 35 00                      ; Room Number: 0xBD, Length: 0x0035, Data: 0x00
;
55E6:    03 1D                      ;   Section DESCRIPTION, Length: 0x001D
55E8:       0D 1B                   ;     WHILE PASS, Length: 0x001B
55EA:          AB                   ;       COMMAND 0xAB
55EB:          04 18                ;       PRINT, Length: 0x0018
;
; FOOTPRINTS LEAD FROM NORTH TO WEST. 
;
55ED:             01 68 AC BF 9E 7A CE B5 86 5F 5C 15 DB 9F 04 9A ; 
55FD:             53 BE 6B BF B5 D0 9B C1 ; 
;
5605:    04 13                      ;   Section COMMANDS, Length: 0x0013
5607:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
560A:          03                   ;       Phrase number: 0x03
560B:          02                   ;       ELSE go to: 0x560E
560C:             00 D6             ;         MOVE AND LOOK, Destination room: 0xD6
560E:          04                   ;       Phrase number: 0x04
560F:          02                   ;       ELSE go to: 0x5612
5610:             00 BE             ;         MOVE AND LOOK, Destination room: 0xBE
5612:          01                   ;       Phrase number: 0x01
5613:          02                   ;       ELSE go to: 0x5616
5614:             00 9E             ;         MOVE AND LOOK, Destination room: 0x9E
5616:          02                   ;       Phrase number: 0x02
5617:          02                   ;       ELSE go to: 0x561A
5618:             00 D8             ;         MOVE AND LOOK, Destination room: 0xD8

561A: BE 3F 00                      ; Room Number: 0xBE, Length: 0x003F, Data: 0x00
;
561D:    03 27                      ;   Section DESCRIPTION, Length: 0x0027
561F:       0D 25                   ;     WHILE PASS, Length: 0x0025
5621:          AB                   ;       COMMAND 0xAB
5622:          04 22                ;       PRINT, Length: 0x0022
;
; STRANGE FOOTPRINTS LEAD FROM THE EAST TO THE WEST. 
;
5624:             0C BA 91 48 48 5E 46 A0 F3 A6 CD 9A 3F 16 F3 46 ; 
5634:             79 68 56 90 DB 72 95 5F 16 BC D6 9C DB 72 B5 D0 ; 
5644:             9B C1             ; 
;
5646:    04 13                      ;   Section COMMANDS, Length: 0x0013
5648:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
564B:          03                   ;       Phrase number: 0x03
564C:          02                   ;       ELSE go to: 0x564F
564D:             00 BD             ;         MOVE AND LOOK, Destination room: 0xBD
564F:          04                   ;       Phrase number: 0x04
5650:          02                   ;       ELSE go to: 0x5653
5651:             00 A0             ;         MOVE AND LOOK, Destination room: 0xA0
5653:          01                   ;       Phrase number: 0x01
5654:          02                   ;       ELSE go to: 0x5657
5655:             00 9F             ;         MOVE AND LOOK, Destination room: 0x9F
5657:          02                   ;       Phrase number: 0x02
5658:          02                   ;       ELSE go to: 0x565B
5659:             00 D9             ;         MOVE AND LOOK, Destination room: 0xD9

565B: BF 3D 00                      ; Room Number: 0xBF, Length: 0x003D, Data: 0x00
;
565E:    03 25                      ;   Section DESCRIPTION, Length: 0x0025
5660:       0D 23                   ;     WHILE PASS, Length: 0x0023
5662:          AB                   ;       COMMAND 0xAB
5663:          04 20                ;       PRINT, Length: 0x0020
;
; WEARY FOOTPRINTS GO FROM THE NORTH TO THE WEST. 
;
5665:             A3 D0 7B B4 01 68 AC BF 9E 7A C9 B5 C8 9C FF B2 ; 
5675:             82 17 50 5E BE A0 16 71 D6 9C DB 72 B5 D0 9B C1 ; 
;
5685:    04 13                      ;   Section COMMANDS, Length: 0x0013
5687:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
568A:          03                   ;       Phrase number: 0x03
568B:          02                   ;       ELSE go to: 0x568E
568C:             00 D9             ;         MOVE AND LOOK, Destination room: 0xD9
568E:          04                   ;       Phrase number: 0x04
568F:          02                   ;       ELSE go to: 0x5692
5690:             00 A1             ;         MOVE AND LOOK, Destination room: 0xA1
5692:          01                   ;       Phrase number: 0x01
5693:          02                   ;       ELSE go to: 0x5696
5694:             00 A0             ;         MOVE AND LOOK, Destination room: 0xA0
5696:          02                   ;       Phrase number: 0x02
5697:          02                   ;       ELSE go to: 0x569A
5698:             00 C0             ;         MOVE AND LOOK, Destination room: 0xC0

569A: C0 41 00                      ; Room Number: 0xC0, Length: 0x0041, Data: 0x00
;
569D:    03 29                      ;   Section DESCRIPTION, Length: 0x0029
569F:       0D 27                   ;     WHILE PASS, Length: 0x0027
56A1:          AB                   ;       COMMAND 0xAB
56A2:          04 24                ;       PRINT, Length: 0x0024
;
; STAGGERING FOOTPRINTS LEAD FROM THE WEST TO THE SOUTH.
;
56A4:             FB B9 F7 6C 10 B2 C8 6A 46 A0 F3 A6 CD 9A 3F 16 ; 
56B4:             F3 46 79 68 56 90 DB 72 B5 D0 16 BC D6 9C DB 72 ; 
56C4:             47 B9 77 BE       ; 
;
56C8:    04 13                      ;   Section COMMANDS, Length: 0x0013
56CA:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
56CD:          03                   ;       Phrase number: 0x03
56CE:          02                   ;       ELSE go to: 0x56D1
56CF:             00 DA             ;         MOVE AND LOOK, Destination room: 0xDA
56D1:          04                   ;       Phrase number: 0x04
56D2:          02                   ;       ELSE go to: 0x56D5
56D3:             00 A2             ;         MOVE AND LOOK, Destination room: 0xA2
56D5:          01                   ;       Phrase number: 0x01
56D6:          02                   ;       ELSE go to: 0x56D9
56D7:             00 BF             ;         MOVE AND LOOK, Destination room: 0xBF
56D9:          02                   ;       Phrase number: 0x02
56DA:          02                   ;       ELSE go to: 0x56DD
56DB:             00 C1             ;         MOVE AND LOOK, Destination room: 0xC1

56DD: C1 47 00                      ; Room Number: 0xC1, Length: 0x0047, Data: 0x00
;
56E0:    03 2F                      ;   Section DESCRIPTION, Length: 0x002F
56E2:       0D 2D                   ;     WHILE PASS, Length: 0x002D
56E4:          AB                   ;       COMMAND 0xAB
56E5:          04 2A                ;       PRINT, Length: 0x002A
;
; CRAWL MARKS LEAD FROM THE NORTH TO THE EAST. THEY LOOK RECENT. 
;
56E7:             AB 55 B3 D1 94 91 CB 87 E3 8B 08 58 FF B2 82 17 ; 
56F7:             50 5E BE A0 16 71 D6 9C DB 72 95 5F 9B C1 5F BE ; 
5707:             4E DB 3D A0 2F 17 B0 53 9B C1 ; 
;
5711:    04 13                      ;   Section COMMANDS, Length: 0x0013
5713:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5716:          03                   ;       Phrase number: 0x03
5717:          02                   ;       ELSE go to: 0x571A
5718:             00 DB             ;         MOVE AND LOOK, Destination room: 0xDB
571A:          04                   ;       Phrase number: 0x04
571B:          02                   ;       ELSE go to: 0x571E
571C:             00 A3             ;         MOVE AND LOOK, Destination room: 0xA3
571E:          01                   ;       Phrase number: 0x01
571F:          02                   ;       ELSE go to: 0x5722
5720:             00 C0             ;         MOVE AND LOOK, Destination room: 0xC0
5722:          02                   ;       Phrase number: 0x02
5723:          02                   ;       ELSE go to: 0x5726
5724:             00 C2             ;         MOVE AND LOOK, Destination room: 0xC2

5726: C2 19 00                      ; Room Number: 0xC2, Length: 0x0019, Data: 0x00
;
5729:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
572B:       AB                      ;     COMMAND 0xAB
;
572C:    04 13                      ;   Section COMMANDS, Length: 0x0013
572E:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5731:          03                   ;       Phrase number: 0x03
5732:          02                   ;       ELSE go to: 0x5735
5733:             00 DC             ;         MOVE AND LOOK, Destination room: 0xDC
5735:          04                   ;       Phrase number: 0x04
5736:          02                   ;       ELSE go to: 0x5739
5737:             00 A4             ;         MOVE AND LOOK, Destination room: 0xA4
5739:          01                   ;       Phrase number: 0x01
573A:          02                   ;       ELSE go to: 0x573D
573B:             00 C1             ;         MOVE AND LOOK, Destination room: 0xC1
573D:          02                   ;       Phrase number: 0x02
573E:          02                   ;       ELSE go to: 0x5741
573F:             00 C3             ;         MOVE AND LOOK, Destination room: 0xC3

5741: C3 19 00                      ; Room Number: 0xC3, Length: 0x0019, Data: 0x00
;
5744:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5746:       AB                      ;     COMMAND 0xAB
;
5747:    04 13                      ;   Section COMMANDS, Length: 0x0013
5749:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
574C:          03                   ;       Phrase number: 0x03
574D:          02                   ;       ELSE go to: 0x5750
574E:             00 DD             ;         MOVE AND LOOK, Destination room: 0xDD
5750:          04                   ;       Phrase number: 0x04
5751:          02                   ;       ELSE go to: 0x5754
5752:             00 A5             ;         MOVE AND LOOK, Destination room: 0xA5
5754:          01                   ;       Phrase number: 0x01
5755:          02                   ;       ELSE go to: 0x5758
5756:             00 C2             ;         MOVE AND LOOK, Destination room: 0xC2
5758:          02                   ;       Phrase number: 0x02
5759:          02                   ;       ELSE go to: 0x575C
575A:             00 C4             ;         MOVE AND LOOK, Destination room: 0xC4

575C: C4 1D 00                      ; Room Number: 0xC4, Length: 0x001D, Data: 0x00
;
575F:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5761:       AB                      ;     COMMAND 0xAB
;
5762:    04 17                      ;   Section COMMANDS, Length: 0x0017
5764:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
5767:          03                   ;       Phrase number: 0x03
5768:          02                   ;       ELSE go to: 0x576B
5769:             00 DE             ;         MOVE AND LOOK, Destination room: 0xDE
576B:          04                   ;       Phrase number: 0x04
576C:          02                   ;       ELSE go to: 0x576F
576D:             00 A6             ;         MOVE AND LOOK, Destination room: 0xA6
576F:          01                   ;       Phrase number: 0x01
5770:          02                   ;       ELSE go to: 0x5773
5771:             00 C3             ;         MOVE AND LOOK, Destination room: 0xC3
5773:          02                   ;       Phrase number: 0x02
5774:          06                   ;       ELSE go to: 0x577B
5775:             0D 04             ;         WHILE PASS, Length: 0x0004
5777:                30 C5          ;           UNKNOWN1, Data: 0xC5
5779:                2F 06          ;           UNKNOWN2 Data: 0x06

577B: D3 1D 00                      ; Room Number: 0xD3, Length: 0x001D, Data: 0x00
;
577E:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5780:       AB                      ;     COMMAND 0xAB
;
5781:    04 17                      ;   Section COMMANDS, Length: 0x0017
5783:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
5786:          03                   ;       Phrase number: 0x03
5787:          06                   ;       ELSE go to: 0x578E
5788:             0D 04             ;         WHILE PASS, Length: 0x0004
578A:                30 D2          ;           UNKNOWN1, Data: 0xD2
578C:                2F 06          ;           UNKNOWN2 Data: 0x06
578E:          04                   ;       Phrase number: 0x04
578F:          02                   ;       ELSE go to: 0x5792
5790:             00 D4             ;         MOVE AND LOOK, Destination room: 0xD4
5792:          01                   ;       Phrase number: 0x01
5793:          02                   ;       ELSE go to: 0x5796
5794:             00 BA             ;         MOVE AND LOOK, Destination room: 0xBA
5796:          02                   ;       Phrase number: 0x02
5797:          02                   ;       ELSE go to: 0x579A
5798:             00 E8             ;         MOVE AND LOOK, Destination room: 0xE8

579A: D4 1C 00                      ; Room Number: 0xD4, Length: 0x001C, Data: 0x00
;
579D:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
579F:       0D 02                   ;     WHILE PASS, Length: 0x0002
57A1:          AB                   ;       COMMAND 0xAB
57A2:          95                   ;       COMMAND 0x95
;
57A3:    04 13                      ;   Section COMMANDS, Length: 0x0013
57A5:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
57A8:          03                   ;       Phrase number: 0x03
57A9:          02                   ;       ELSE go to: 0x57AC
57AA:             00 D7             ;         MOVE AND LOOK, Destination room: 0xD7
57AC:          04                   ;       Phrase number: 0x04
57AD:          02                   ;       ELSE go to: 0x57B0
57AE:             00 E9             ;         MOVE AND LOOK, Destination room: 0xE9
57B0:          01                   ;       Phrase number: 0x01
57B1:          02                   ;       ELSE go to: 0x57B4
57B2:             00 EA             ;         MOVE AND LOOK, Destination room: 0xEA
57B4:          02                   ;       Phrase number: 0x02
57B5:          02                   ;       ELSE go to: 0x57B8
57B6:             00 BA             ;         MOVE AND LOOK, Destination room: 0xBA

57B8: D5 19 00                      ; Room Number: 0xD5, Length: 0x0019, Data: 0x00
;
57BB:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
57BD:       AB                      ;     COMMAND 0xAB
;
57BE:    04 13                      ;   Section COMMANDS, Length: 0x0013
57C0:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
57C3:          03                   ;       Phrase number: 0x03
57C4:          02                   ;       ELSE go to: 0x57C7
57C5:             00 BA             ;         MOVE AND LOOK, Destination room: 0xBA
57C7:          04                   ;       Phrase number: 0x04
57C8:          02                   ;       ELSE go to: 0x57CB
57C9:             00 D6             ;         MOVE AND LOOK, Destination room: 0xD6
57CB:          01                   ;       Phrase number: 0x01
57CC:          02                   ;       ELSE go to: 0x57CF
57CD:             00 BB             ;         MOVE AND LOOK, Destination room: 0xBB
57CF:          02                   ;       Phrase number: 0x02
57D0:          02                   ;       ELSE go to: 0x57D3
57D1:             00 D4             ;         MOVE AND LOOK, Destination room: 0xD4

57D3: D6 19 00                      ; Room Number: 0xD6, Length: 0x0019, Data: 0x00
;
57D6:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
57D8:       AB                      ;     COMMAND 0xAB
;
57D9:    04 13                      ;   Section COMMANDS, Length: 0x0013
57DB:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
57DE:          03                   ;       Phrase number: 0x03
57DF:          02                   ;       ELSE go to: 0x57E2
57E0:             00 D5             ;         MOVE AND LOOK, Destination room: 0xD5
57E2:          04                   ;       Phrase number: 0x04
57E3:          02                   ;       ELSE go to: 0x57E6
57E4:             00 BD             ;         MOVE AND LOOK, Destination room: 0xBD
57E6:          01                   ;       Phrase number: 0x01
57E7:          02                   ;       ELSE go to: 0x57EA
57E8:             00 BC             ;         MOVE AND LOOK, Destination room: 0xBC
57EA:          02                   ;       Phrase number: 0x02
57EB:          02                   ;       ELSE go to: 0x57EE
57EC:             00 D7             ;         MOVE AND LOOK, Destination room: 0xD7

57EE: D7 1C 00                      ; Room Number: 0xD7, Length: 0x001C, Data: 0x00
;
57F1:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
57F3:       0D 02                   ;     WHILE PASS, Length: 0x0002
57F5:          AB                   ;       COMMAND 0xAB
57F6:          95                   ;       COMMAND 0x95
;
57F7:    04 13                      ;   Section COMMANDS, Length: 0x0013
57F9:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
57FC:          03                   ;       Phrase number: 0x03
57FD:          02                   ;       ELSE go to: 0x5800
57FE:             00 D8             ;         MOVE AND LOOK, Destination room: 0xD8
5800:          04                   ;       Phrase number: 0x04
5801:          02                   ;       ELSE go to: 0x5804
5802:             00 D4             ;         MOVE AND LOOK, Destination room: 0xD4
5804:          01                   ;       Phrase number: 0x01
5805:          02                   ;       ELSE go to: 0x5808
5806:             00 EA             ;         MOVE AND LOOK, Destination room: 0xEA
5808:          02                   ;       Phrase number: 0x02
5809:          02                   ;       ELSE go to: 0x580C
580A:             00 D6             ;         MOVE AND LOOK, Destination room: 0xD6

580C: D8 1C 00                      ; Room Number: 0xD8, Length: 0x001C, Data: 0x00
;
580F:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5811:       0D 02                   ;     WHILE PASS, Length: 0x0002
5813:          AB                   ;       COMMAND 0xAB
5814:          95                   ;       COMMAND 0x95
;
5815:    04 13                      ;   Section COMMANDS, Length: 0x0013
5817:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
581A:          03                   ;       Phrase number: 0x03
581B:          02                   ;       ELSE go to: 0x581E
581C:             00 EB             ;         MOVE AND LOOK, Destination room: 0xEB
581E:          04                   ;       Phrase number: 0x04
581F:          02                   ;       ELSE go to: 0x5822
5820:             00 D7             ;         MOVE AND LOOK, Destination room: 0xD7
5822:          01                   ;       Phrase number: 0x01
5823:          02                   ;       ELSE go to: 0x5826
5824:             00 EA             ;         MOVE AND LOOK, Destination room: 0xEA
5826:          02                   ;       Phrase number: 0x02
5827:          02                   ;       ELSE go to: 0x582A
5828:             00 BE             ;         MOVE AND LOOK, Destination room: 0xBE

582A: D9 19 00                      ; Room Number: 0xD9, Length: 0x0019, Data: 0x00
;
582D:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
582F:       AB                      ;     COMMAND 0xAB
;
5830:    04 13                      ;   Section COMMANDS, Length: 0x0013
5832:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5835:          03                   ;       Phrase number: 0x03
5836:          02                   ;       ELSE go to: 0x5839
5837:             00 D8             ;         MOVE AND LOOK, Destination room: 0xD8
5839:          04                   ;       Phrase number: 0x04
583A:          02                   ;       ELSE go to: 0x583D
583B:             00 BF             ;         MOVE AND LOOK, Destination room: 0xBF
583D:          01                   ;       Phrase number: 0x01
583E:          02                   ;       ELSE go to: 0x5841
583F:             00 BE             ;         MOVE AND LOOK, Destination room: 0xBE
5841:          02                   ;       Phrase number: 0x02
5842:          02                   ;       ELSE go to: 0x5845
5843:             00 DA             ;         MOVE AND LOOK, Destination room: 0xDA

5845: DA 19 00                      ; Room Number: 0xDA, Length: 0x0019, Data: 0x00
;
5848:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
584A:       AB                      ;     COMMAND 0xAB
;
584B:    04 13                      ;   Section COMMANDS, Length: 0x0013
584D:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5850:          03                   ;       Phrase number: 0x03
5851:          02                   ;       ELSE go to: 0x5854
5852:             00 EB             ;         MOVE AND LOOK, Destination room: 0xEB
5854:          04                   ;       Phrase number: 0x04
5855:          02                   ;       ELSE go to: 0x5858
5856:             00 C0             ;         MOVE AND LOOK, Destination room: 0xC0
5858:          01                   ;       Phrase number: 0x01
5859:          02                   ;       ELSE go to: 0x585C
585A:             00 D9             ;         MOVE AND LOOK, Destination room: 0xD9
585C:          02                   ;       Phrase number: 0x02
585D:          02                   ;       ELSE go to: 0x5860
585E:             00 DB             ;         MOVE AND LOOK, Destination room: 0xDB

5860: DB 19 00                      ; Room Number: 0xDB, Length: 0x0019, Data: 0x00
;
5863:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5865:       AB                      ;     COMMAND 0xAB
;
5866:    04 13                      ;   Section COMMANDS, Length: 0x0013
5868:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
586B:          03                   ;       Phrase number: 0x03
586C:          02                   ;       ELSE go to: 0x586F
586D:             00 EC             ;         MOVE AND LOOK, Destination room: 0xEC
586F:          04                   ;       Phrase number: 0x04
5870:          02                   ;       ELSE go to: 0x5873
5871:             00 C1             ;         MOVE AND LOOK, Destination room: 0xC1
5873:          01                   ;       Phrase number: 0x01
5874:          02                   ;       ELSE go to: 0x5877
5875:             00 DA             ;         MOVE AND LOOK, Destination room: 0xDA
5877:          02                   ;       Phrase number: 0x02
5878:          02                   ;       ELSE go to: 0x587B
5879:             00 DC             ;         MOVE AND LOOK, Destination room: 0xDC

587B: DC 19 00                      ; Room Number: 0xDC, Length: 0x0019, Data: 0x00
;
587E:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5880:       AB                      ;     COMMAND 0xAB
;
5881:    04 13                      ;   Section COMMANDS, Length: 0x0013
5883:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5886:          03                   ;       Phrase number: 0x03
5887:          02                   ;       ELSE go to: 0x588A
5888:             00 ED             ;         MOVE AND LOOK, Destination room: 0xED
588A:          04                   ;       Phrase number: 0x04
588B:          02                   ;       ELSE go to: 0x588E
588C:             00 C2             ;         MOVE AND LOOK, Destination room: 0xC2
588E:          01                   ;       Phrase number: 0x01
588F:          02                   ;       ELSE go to: 0x5892
5890:             00 DB             ;         MOVE AND LOOK, Destination room: 0xDB
5892:          02                   ;       Phrase number: 0x02
5893:          02                   ;       ELSE go to: 0x5896
5894:             00 DD             ;         MOVE AND LOOK, Destination room: 0xDD

5896: DD 40 00                      ; Room Number: 0xDD, Length: 0x0040, Data: 0x00
;
5899:    03 28                      ;   Section DESCRIPTION, Length: 0x0028
589B:       0D 26                   ;     WHILE PASS, Length: 0x0026
589D:          AB                   ;       COMMAND 0xAB
589E:          04 23                ;       PRINT, Length: 0x0023
;
; THE HIGHWAY CURVES HERE, LEADING DUE EAST AND SOUTH.
;
58A0:             5F BE A3 15 31 6D 3B 4A 34 56 75 CA 9F 15 7E B1 ; 
58B0:             3F 16 03 47 AB 98 67 5C 23 15 F3 B9 8E 48 61 17 ; 
58C0:             82 C6 2E          ; 
;
58C3:    04 13                      ;   Section COMMANDS, Length: 0x0013
58C5:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
58C8:          03                   ;       Phrase number: 0x03
58C9:          02                   ;       ELSE go to: 0x58CC
58CA:             00 EE             ;         MOVE AND LOOK, Destination room: 0xEE
58CC:          04                   ;       Phrase number: 0x04
58CD:          02                   ;       ELSE go to: 0x58D0
58CE:             00 C3             ;         MOVE AND LOOK, Destination room: 0xC3
58D0:          01                   ;       Phrase number: 0x01
58D1:          02                   ;       ELSE go to: 0x58D4
58D2:             00 DC             ;         MOVE AND LOOK, Destination room: 0xDC
58D4:          02                   ;       Phrase number: 0x02
58D5:          02                   ;       ELSE go to: 0x58D8
58D6:             00 DE             ;         MOVE AND LOOK, Destination room: 0xDE

58D8: DE 38 00                      ; Room Number: 0xDE, Length: 0x0038, Data: 0x00
;
58DB:    03 1C                      ;   Section DESCRIPTION, Length: 0x001C
58DD:       0D 1A                   ;     WHILE PASS, Length: 0x001A
58DF:          AB                   ;       COMMAND 0xAB
58E0:          04 17                ;       PRINT, Length: 0x0017
;
; THE HIGHWAY LEADS NORTH AND SOUTH.
;
58E2:             5F BE A3 15 31 6D 3B 4A E3 8B 0B 5C 04 9A 53 BE ; 
58F2:             8E 48 61 17 82 C6 2E ; 
;
58F9:    04 17                      ;   Section COMMANDS, Length: 0x0017
58FB:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
58FE:          03                   ;       Phrase number: 0x03
58FF:          02                   ;       ELSE go to: 0x5902
5900:             00 DF             ;         MOVE AND LOOK, Destination room: 0xDF
5902:          04                   ;       Phrase number: 0x04
5903:          02                   ;       ELSE go to: 0x5906
5904:             00 C4             ;         MOVE AND LOOK, Destination room: 0xC4
5906:          01                   ;       Phrase number: 0x01
5907:          02                   ;       ELSE go to: 0x590A
5908:             00 DD             ;         MOVE AND LOOK, Destination room: 0xDD
590A:          02                   ;       Phrase number: 0x02
590B:          06                   ;       ELSE go to: 0x5912
590C:             0D 04             ;         WHILE PASS, Length: 0x0004
590E:                30 C6          ;           UNKNOWN1, Data: 0xC6
5910:                2F 06          ;           UNKNOWN2 Data: 0x06

5912: DF 1D 00                      ; Room Number: 0xDF, Length: 0x001D, Data: 0x00
;
5915:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5917:       AB                      ;     COMMAND 0xAB
;
5918:    04 17                      ;   Section COMMANDS, Length: 0x0017
591A:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
591D:          03                   ;       Phrase number: 0x03
591E:          02                   ;       ELSE go to: 0x5921
591F:             00 E0             ;         MOVE AND LOOK, Destination room: 0xE0
5921:          04                   ;       Phrase number: 0x04
5922:          02                   ;       ELSE go to: 0x5925
5923:             00 DE             ;         MOVE AND LOOK, Destination room: 0xDE
5925:          01                   ;       Phrase number: 0x01
5926:          02                   ;       ELSE go to: 0x5929
5927:             00 EE             ;         MOVE AND LOOK, Destination room: 0xEE
5929:          02                   ;       Phrase number: 0x02
592A:          06                   ;       ELSE go to: 0x5931
592B:             0D 04             ;         WHILE PASS, Length: 0x0004
592D:                30 C7          ;           UNKNOWN1, Data: 0xC7
592F:                2F 06          ;           UNKNOWN2 Data: 0x06

5931: E0 1D 00                      ; Room Number: 0xE0, Length: 0x001D, Data: 0x00
;
5934:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5936:       AB                      ;     COMMAND 0xAB
;
5937:    04 17                      ;   Section COMMANDS, Length: 0x0017
5939:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
593C:          03                   ;       Phrase number: 0x03
593D:          02                   ;       ELSE go to: 0x5940
593E:             00 E1             ;         MOVE AND LOOK, Destination room: 0xE1
5940:          04                   ;       Phrase number: 0x04
5941:          02                   ;       ELSE go to: 0x5944
5942:             00 DF             ;         MOVE AND LOOK, Destination room: 0xDF
5944:          01                   ;       Phrase number: 0x01
5945:          02                   ;       ELSE go to: 0x5948
5946:             00 EF             ;         MOVE AND LOOK, Destination room: 0xEF
5948:          02                   ;       Phrase number: 0x02
5949:          06                   ;       ELSE go to: 0x5950
594A:             0D 04             ;         WHILE PASS, Length: 0x0004
594C:                30 C8          ;           UNKNOWN1, Data: 0xC8
594E:                2F 06          ;           UNKNOWN2 Data: 0x06

5950: E1 25 00                      ; Room Number: 0xE1, Length: 0x0025, Data: 0x00
;
5953:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5955:       AB                      ;     COMMAND 0xAB
;
5956:    04 1F                      ;   Section COMMANDS, Length: 0x001F
5958:       0B 1D 0A                ;     SWITCH, Length: 0x001D, Function to call: 0x0A
595B:          03                   ;       Phrase number: 0x03
595C:          02                   ;       ELSE go to: 0x595F
595D:             00 E2             ;         MOVE AND LOOK, Destination room: 0xE2
595F:          04                   ;       Phrase number: 0x04
5960:          02                   ;       ELSE go to: 0x5963
5961:             00 E0             ;         MOVE AND LOOK, Destination room: 0xE0
5963:          01                   ;       Phrase number: 0x01
5964:          0A                   ;       ELSE go to: 0x596F
5965:             0D 08             ;         WHILE PASS, Length: 0x0008
5967:                C8             ;           COMMAND 0xC8
5968:                30 B3          ;           UNKNOWN1, Data: 0xB3
596A:                17 9D 00       ;           MOVE TO, Object number: 0x9D, Destination room: 0x00
596D:                2F 03          ;           UNKNOWN2 Data: 0x03
596F:          02                   ;       Phrase number: 0x02
5970:          06                   ;       ELSE go to: 0x5977
5971:             0D 04             ;         WHILE PASS, Length: 0x0004
5973:                30 C9          ;           UNKNOWN1, Data: 0xC9
5975:                2F 06          ;           UNKNOWN2 Data: 0x06

5977: E2 21 00                      ; Room Number: 0xE2, Length: 0x0021, Data: 0x00
;
597A:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
597C:       AB                      ;     COMMAND 0xAB
;
597D:    04 1B                      ;   Section COMMANDS, Length: 0x001B
597F:       0B 19 0A                ;     SWITCH, Length: 0x0019, Function to call: 0x0A
5982:          03                   ;       Phrase number: 0x03
5983:          06                   ;       ELSE go to: 0x598A
5984:             0D 04             ;         WHILE PASS, Length: 0x0004
5986:                30 E3          ;           UNKNOWN1, Data: 0xE3
5988:                2F 06          ;           UNKNOWN2 Data: 0x06
598A:          04                   ;       Phrase number: 0x04
598B:          02                   ;       ELSE go to: 0x598E
598C:             00 E1             ;         MOVE AND LOOK, Destination room: 0xE1
598E:          01                   ;       Phrase number: 0x01
598F:          02                   ;       ELSE go to: 0x5992
5990:             00 F0             ;         MOVE AND LOOK, Destination room: 0xF0
5992:          02                   ;       Phrase number: 0x02
5993:          06                   ;       ELSE go to: 0x599A
5994:             0D 04             ;         WHILE PASS, Length: 0x0004
5996:                30 CA          ;           UNKNOWN1, Data: 0xCA
5998:                2F 06          ;           UNKNOWN2 Data: 0x06

599A: E8 1D 00                      ; Room Number: 0xE8, Length: 0x001D, Data: 0x00
;
599D:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
599F:       AB                      ;     COMMAND 0xAB
;
59A0:    04 17                      ;   Section COMMANDS, Length: 0x0017
59A2:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
59A5:          03                   ;       Phrase number: 0x03
59A6:          06                   ;       ELSE go to: 0x59AD
59A7:             0D 04             ;         WHILE PASS, Length: 0x0004
59A9:                30 E7          ;           UNKNOWN1, Data: 0xE7
59AB:                2F 06          ;           UNKNOWN2 Data: 0x06
59AD:          04                   ;       Phrase number: 0x04
59AE:          02                   ;       ELSE go to: 0x59B1
59AF:             00 E9             ;         MOVE AND LOOK, Destination room: 0xE9
59B1:          01                   ;       Phrase number: 0x01
59B2:          02                   ;       ELSE go to: 0x59B5
59B3:             00 D3             ;         MOVE AND LOOK, Destination room: 0xD3
59B5:          02                   ;       Phrase number: 0x02
59B6:          02                   ;       ELSE go to: 0x59B9
59B7:             00 F2             ;         MOVE AND LOOK, Destination room: 0xF2

59B9: E9 1C 00                      ; Room Number: 0xE9, Length: 0x001C, Data: 0x00
;
59BC:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
59BE:       0D 02                   ;     WHILE PASS, Length: 0x0002
59C0:          AB                   ;       COMMAND 0xAB
59C1:          95                   ;       COMMAND 0x95
;
59C2:    04 13                      ;   Section COMMANDS, Length: 0x0013
59C4:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
59C7:          03                   ;       Phrase number: 0x03
59C8:          02                   ;       ELSE go to: 0x59CB
59C9:             00 D4             ;         MOVE AND LOOK, Destination room: 0xD4
59CB:          04                   ;       Phrase number: 0x04
59CC:          02                   ;       ELSE go to: 0x59CF
59CD:             00 F3             ;         MOVE AND LOOK, Destination room: 0xF3
59CF:          01                   ;       Phrase number: 0x01
59D0:          02                   ;       ELSE go to: 0x59D3
59D1:             00 EA             ;         MOVE AND LOOK, Destination room: 0xEA
59D3:          02                   ;       Phrase number: 0x02
59D4:          02                   ;       ELSE go to: 0x59D7
59D5:             00 E8             ;         MOVE AND LOOK, Destination room: 0xE8

59D7: EA 19 00                      ; Room Number: 0xEA, Length: 0x0019, Data: 0x00
;
59DA:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
59DC:       AB                      ;     COMMAND 0xAB
;
59DD:    04 13                      ;   Section COMMANDS, Length: 0x0013
59DF:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
59E2:          03                   ;       Phrase number: 0x03
59E3:          02                   ;       ELSE go to: 0x59E6
59E4:             00 E9             ;         MOVE AND LOOK, Destination room: 0xE9
59E6:          04                   ;       Phrase number: 0x04
59E7:          02                   ;       ELSE go to: 0x59EA
59E8:             00 EB             ;         MOVE AND LOOK, Destination room: 0xEB
59EA:          01                   ;       Phrase number: 0x01
59EB:          02                   ;       ELSE go to: 0x59EE
59EC:             00 D7             ;         MOVE AND LOOK, Destination room: 0xD7
59EE:          02                   ;       Phrase number: 0x02
59EF:          02                   ;       ELSE go to: 0x59F2
59F0:             00 F4             ;         MOVE AND LOOK, Destination room: 0xF4

59F2: EB 1C 00                      ; Room Number: 0xEB, Length: 0x001C, Data: 0x00
;
59F5:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
59F7:       0D 02                   ;     WHILE PASS, Length: 0x0002
59F9:          AB                   ;       COMMAND 0xAB
59FA:          95                   ;       COMMAND 0x95
;
59FB:    04 13                      ;   Section COMMANDS, Length: 0x0013
59FD:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5A00:          03                   ;       Phrase number: 0x03
5A01:          02                   ;       ELSE go to: 0x5A04
5A02:             00 EC             ;         MOVE AND LOOK, Destination room: 0xEC
5A04:          04                   ;       Phrase number: 0x04
5A05:          02                   ;       ELSE go to: 0x5A08
5A06:             00 D8             ;         MOVE AND LOOK, Destination room: 0xD8
5A08:          01                   ;       Phrase number: 0x01
5A09:          02                   ;       ELSE go to: 0x5A0C
5A0A:             00 EA             ;         MOVE AND LOOK, Destination room: 0xEA
5A0C:          02                   ;       Phrase number: 0x02
5A0D:          02                   ;       ELSE go to: 0x5A10
5A0E:             00 DA             ;         MOVE AND LOOK, Destination room: 0xDA

5A10: EC 1C 00                      ; Room Number: 0xEC, Length: 0x001C, Data: 0x00
;
5A13:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5A15:       0D 02                   ;     WHILE PASS, Length: 0x0002
5A17:          AB                   ;       COMMAND 0xAB
5A18:          95                   ;       COMMAND 0x95
;
5A19:    04 13                      ;   Section COMMANDS, Length: 0x0013
5A1B:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5A1E:          03                   ;       Phrase number: 0x03
5A1F:          02                   ;       ELSE go to: 0x5A22
5A20:             00 F4             ;         MOVE AND LOOK, Destination room: 0xF4
5A22:          04                   ;       Phrase number: 0x04
5A23:          02                   ;       ELSE go to: 0x5A26
5A24:             00 EB             ;         MOVE AND LOOK, Destination room: 0xEB
5A26:          01                   ;       Phrase number: 0x01
5A27:          02                   ;       ELSE go to: 0x5A2A
5A28:             00 EA             ;         MOVE AND LOOK, Destination room: 0xEA
5A2A:          02                   ;       Phrase number: 0x02
5A2B:          02                   ;       ELSE go to: 0x5A2E
5A2C:             00 DC             ;         MOVE AND LOOK, Destination room: 0xDC

5A2E: ED 19 00                      ; Room Number: 0xED, Length: 0x0019, Data: 0x00
;
5A31:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5A33:       AB                      ;     COMMAND 0xAB
;
5A34:    04 13                      ;   Section COMMANDS, Length: 0x0013
5A36:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5A39:          03                   ;       Phrase number: 0x03
5A3A:          02                   ;       ELSE go to: 0x5A3D
5A3B:             00 F5             ;         MOVE AND LOOK, Destination room: 0xF5
5A3D:          04                   ;       Phrase number: 0x04
5A3E:          02                   ;       ELSE go to: 0x5A41
5A3F:             00 DC             ;         MOVE AND LOOK, Destination room: 0xDC
5A41:          01                   ;       Phrase number: 0x01
5A42:          02                   ;       ELSE go to: 0x5A45
5A43:             00 EC             ;         MOVE AND LOOK, Destination room: 0xEC
5A45:          02                   ;       Phrase number: 0x02
5A46:          02                   ;       ELSE go to: 0x5A49
5A47:             00 EE             ;         MOVE AND LOOK, Destination room: 0xEE

5A49: EE 1C 00                      ; Room Number: 0xEE, Length: 0x001C, Data: 0x00
;
5A4C:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5A4E:       0D 02                   ;     WHILE PASS, Length: 0x0002
5A50:          AB                   ;       COMMAND 0xAB
5A51:          9B                   ;       COMMAND 0x9B
;
5A52:    04 13                      ;   Section COMMANDS, Length: 0x0013
5A54:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5A57:          03                   ;       Phrase number: 0x03
5A58:          02                   ;       ELSE go to: 0x5A5B
5A59:             00 EF             ;         MOVE AND LOOK, Destination room: 0xEF
5A5B:          04                   ;       Phrase number: 0x04
5A5C:          02                   ;       ELSE go to: 0x5A5F
5A5D:             00 DD             ;         MOVE AND LOOK, Destination room: 0xDD
5A5F:          01                   ;       Phrase number: 0x01
5A60:          02                   ;       ELSE go to: 0x5A63
5A61:             00 ED             ;         MOVE AND LOOK, Destination room: 0xED
5A63:          02                   ;       Phrase number: 0x02
5A64:          02                   ;       ELSE go to: 0x5A67
5A65:             00 DF             ;         MOVE AND LOOK, Destination room: 0xDF

5A67: EF 24 00                      ; Room Number: 0xEF, Length: 0x0024, Data: 0x00
;
5A6A:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5A6C:       0D 02                   ;     WHILE PASS, Length: 0x0002
5A6E:          AB                   ;       COMMAND 0xAB
5A6F:          9B                   ;       COMMAND 0x9B
;
5A70:    04 1B                      ;   Section COMMANDS, Length: 0x001B
5A72:       0B 19 0A                ;     SWITCH, Length: 0x0019, Function to call: 0x0A
5A75:          03                   ;       Phrase number: 0x03
5A76:          0A                   ;       ELSE go to: 0x5A81
5A77:             0D 08             ;         WHILE PASS, Length: 0x0008
5A79:                C8             ;           COMMAND 0xC8
5A7A:                30 80          ;           UNKNOWN1, Data: 0x80
5A7C:                17 9D 00       ;           MOVE TO, Object number: 0x9D, Destination room: 0x00
5A7F:                2F 01          ;           UNKNOWN2 Data: 0x01
5A81:          04                   ;       Phrase number: 0x04
5A82:          02                   ;       ELSE go to: 0x5A85
5A83:             00 EE             ;         MOVE AND LOOK, Destination room: 0xEE
5A85:          01                   ;       Phrase number: 0x01
5A86:          02                   ;       ELSE go to: 0x5A89
5A87:             00 F5             ;         MOVE AND LOOK, Destination room: 0xF5
5A89:          02                   ;       Phrase number: 0x02
5A8A:          02                   ;       ELSE go to: 0x5A8D
5A8B:             00 E0             ;         MOVE AND LOOK, Destination room: 0xE0

5A8D: F0 28 00                      ; Room Number: 0xF0, Length: 0x0028, Data: 0x00
;
5A90:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5A92:       0D 02                   ;     WHILE PASS, Length: 0x0002
5A94:          9B                   ;       COMMAND 0x9B
5A95:          AB                   ;       COMMAND 0xAB
;
5A96:    04 1F                      ;   Section COMMANDS, Length: 0x001F
5A98:       0B 1D 0A                ;     SWITCH, Length: 0x001D, Function to call: 0x0A
5A9B:          03                   ;       Phrase number: 0x03
5A9C:          06                   ;       ELSE go to: 0x5AA3
5A9D:             0D 04             ;         WHILE PASS, Length: 0x0004
5A9F:                30 E4          ;           UNKNOWN1, Data: 0xE4
5AA1:                2F 06          ;           UNKNOWN2 Data: 0x06
5AA3:          04                   ;       Phrase number: 0x04
5AA4:          0A                   ;       ELSE go to: 0x5AAF
5AA5:             0D 08             ;         WHILE PASS, Length: 0x0008
5AA7:                C8             ;           COMMAND 0xC8
5AA8:                30 B4          ;           UNKNOWN1, Data: 0xB4
5AAA:                17 9D 00       ;           MOVE TO, Object number: 0x9D, Destination room: 0x00
5AAD:                2F 04          ;           UNKNOWN2 Data: 0x04
5AAF:          01                   ;       Phrase number: 0x01
5AB0:          02                   ;       ELSE go to: 0x5AB3
5AB1:             00 F1             ;         MOVE AND LOOK, Destination room: 0xF1
5AB3:          02                   ;       Phrase number: 0x02
5AB4:          02                   ;       ELSE go to: 0x5AB7
5AB5:             00 E2             ;         MOVE AND LOOK, Destination room: 0xE2

5AB7: F1 3F 00                      ; Room Number: 0xF1, Length: 0x003F, Data: 0x00
;
5ABA:    03 23                      ;   Section DESCRIPTION, Length: 0x0023
5ABC:       0D 21                   ;     WHILE PASS, Length: 0x0021
5ABE:          AB                   ;       COMMAND 0xAB
5ABF:          04 1E                ;       PRINT, Length: 0x001E
;
; A SMALL TRAIL LEADS WEST AND NORTH FROM HERE.
;
5AC1:             55 45 8E 91 16 8A CB B0 0E 8A 86 5F D9 B5 66 62 ; 
5AD1:             90 14 10 58 BE A0 08 71 FF B2 9F 15 7F B1 ; 
;
5ADF:    04 17                      ;   Section COMMANDS, Length: 0x0017
5AE1:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
5AE4:          03                   ;       Phrase number: 0x03
5AE5:          06                   ;       ELSE go to: 0x5AEC
5AE6:             0D 04             ;         WHILE PASS, Length: 0x0004
5AE8:                30 E5          ;           UNKNOWN1, Data: 0xE5
5AEA:                2F 06          ;           UNKNOWN2 Data: 0x06
5AEC:          04                   ;       Phrase number: 0x04
5AED:          02                   ;       ELSE go to: 0x5AF0
5AEE:             00 F6             ;         MOVE AND LOOK, Destination room: 0xF6
5AF0:          01                   ;       Phrase number: 0x01
5AF1:          02                   ;       ELSE go to: 0x5AF4
5AF2:             00 F2             ;         MOVE AND LOOK, Destination room: 0xF2
5AF4:          02                   ;       Phrase number: 0x02
5AF5:          02                   ;       ELSE go to: 0x5AF8
5AF6:             00 F0             ;         MOVE AND LOOK, Destination room: 0xF0

5AF8: F2 41 00                      ; Room Number: 0xF2, Length: 0x0041, Data: 0x00
;
5AFB:    03 25                      ;   Section DESCRIPTION, Length: 0x0025
5AFD:       0D 23                   ;     WHILE PASS, Length: 0x0023
5AFF:          AB                   ;       COMMAND 0xAB
5B00:          04 20                ;       PRINT, Length: 0x0020
;
; A SMALL TWISTY TRAIL LEADS WEST AND SOUTH HERE. 
;
5B02:             55 45 8E 91 16 8A 55 D1 FB C0 EB BF 33 7A E3 8B ; 
5B12:             0B 5C B5 D0 03 BC 33 98 47 B9 53 BE F4 72 DB 63 ; 
;
5B22:    04 17                      ;   Section COMMANDS, Length: 0x0017
5B24:       0B 15 0A                ;     SWITCH, Length: 0x0015, Function to call: 0x0A
5B27:          03                   ;       Phrase number: 0x03
5B28:          06                   ;       ELSE go to: 0x5B2F
5B29:             0D 04             ;         WHILE PASS, Length: 0x0004
5B2B:                30 E6          ;           UNKNOWN1, Data: 0xE6
5B2D:                2F 06          ;           UNKNOWN2 Data: 0x06
5B2F:          04                   ;       Phrase number: 0x04
5B30:          02                   ;       ELSE go to: 0x5B33
5B31:             00 F3             ;         MOVE AND LOOK, Destination room: 0xF3
5B33:          01                   ;       Phrase number: 0x01
5B34:          02                   ;       ELSE go to: 0x5B37
5B35:             00 E8             ;         MOVE AND LOOK, Destination room: 0xE8
5B37:          02                   ;       Phrase number: 0x02
5B38:          02                   ;       ELSE go to: 0x5B3B
5B39:             00 F1             ;         MOVE AND LOOK, Destination room: 0xF1

5B3B: F3 35 00                      ; Room Number: 0xF3, Length: 0x0035, Data: 0x00
;
5B3E:    03 1D                      ;   Section DESCRIPTION, Length: 0x001D
5B40:       0D 1B                   ;     WHILE PASS, Length: 0x001B
5B42:          AB                   ;       COMMAND 0xAB
5B43:          95                   ;       COMMAND 0x95
5B44:          04 17                ;       PRINT, Length: 0x0017
;
; THE TRAIL ALSO FORKS TO THE SOUTH.
;
5B46:             5F BE 8C 17 CE 47 8E 14 2B B9 04 68 CB 87 6B BF ; 
5B56:             5F BE 61 17 82 C6 2E ; 
;
5B5D:    04 13                      ;   Section COMMANDS, Length: 0x0013
5B5F:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5B62:          03                   ;       Phrase number: 0x03
5B63:          02                   ;       ELSE go to: 0x5B66
5B64:             00 E9             ;         MOVE AND LOOK, Destination room: 0xE9
5B66:          04                   ;       Phrase number: 0x04
5B67:          02                   ;       ELSE go to: 0x5B6A
5B68:             00 F4             ;         MOVE AND LOOK, Destination room: 0xF4
5B6A:          01                   ;       Phrase number: 0x01
5B6B:          02                   ;       ELSE go to: 0x5B6E
5B6C:             00 EA             ;         MOVE AND LOOK, Destination room: 0xEA
5B6E:          02                   ;       Phrase number: 0x02
5B6F:          02                   ;       ELSE go to: 0x5B72
5B70:             00 F1             ;         MOVE AND LOOK, Destination room: 0xF1

5B72: F4 1C 00                      ; Room Number: 0xF4, Length: 0x001C, Data: 0x00
;
5B75:    03 04                      ;   Section DESCRIPTION, Length: 0x0004
5B77:       0D 02                   ;     WHILE PASS, Length: 0x0002
5B79:          AB                   ;       COMMAND 0xAB
5B7A:          95                   ;       COMMAND 0x95
;
5B7B:    04 13                      ;   Section COMMANDS, Length: 0x0013
5B7D:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5B80:          03                   ;       Phrase number: 0x03
5B81:          02                   ;       ELSE go to: 0x5B84
5B82:             00 F3             ;         MOVE AND LOOK, Destination room: 0xF3
5B84:          04                   ;       Phrase number: 0x04
5B85:          02                   ;       ELSE go to: 0x5B88
5B86:             00 EC             ;         MOVE AND LOOK, Destination room: 0xEC
5B88:          01                   ;       Phrase number: 0x01
5B89:          02                   ;       ELSE go to: 0x5B8C
5B8A:             00 EA             ;         MOVE AND LOOK, Destination room: 0xEA
5B8C:          02                   ;       Phrase number: 0x02
5B8D:          02                   ;       ELSE go to: 0x5B90
5B8E:             00 F5             ;         MOVE AND LOOK, Destination room: 0xF5

5B90: F5 19 00                      ; Room Number: 0xF5, Length: 0x0019, Data: 0x00
;
5B93:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5B95:       AB                      ;     COMMAND 0xAB
;
5B96:    04 13                      ;   Section COMMANDS, Length: 0x0013
5B98:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5B9B:          03                   ;       Phrase number: 0x03
5B9C:          02                   ;       ELSE go to: 0x5B9F
5B9D:             00 F6             ;         MOVE AND LOOK, Destination room: 0xF6
5B9F:          04                   ;       Phrase number: 0x04
5BA0:          02                   ;       ELSE go to: 0x5BA3
5BA1:             00 ED             ;         MOVE AND LOOK, Destination room: 0xED
5BA3:          01                   ;       Phrase number: 0x01
5BA4:          02                   ;       ELSE go to: 0x5BA7
5BA5:             00 F4             ;         MOVE AND LOOK, Destination room: 0xF4
5BA7:          02                   ;       Phrase number: 0x02
5BA8:          02                   ;       ELSE go to: 0x5BAB
5BA9:             00 EF             ;         MOVE AND LOOK, Destination room: 0xEF

5BAB: F6 45 00                      ; Room Number: 0xF6, Length: 0x0045, Data: 0x00
;
5BAE:    03 25                      ;   Section DESCRIPTION, Length: 0x0025
5BB0:       0D 23                   ;     WHILE PASS, Length: 0x0023
5BB2:          AB                   ;       COMMAND 0xAB
5BB3:          04 20                ;       PRINT, Length: 0x0020
;
; A SMALL TRAIL LEADS FROM THE SOUTH TO THE EAST. 
;
5BB5:             55 45 8E 91 16 8A CB B0 0E 8A 86 5F C8 B5 FF B2 ; 
5BC5:             82 17 55 5E 36 A1 16 71 D6 9C DB 72 95 5F 9B C1 ; 
;
5BD5:    04 1B                      ;   Section COMMANDS, Length: 0x001B
5BD7:       0B 19 0A                ;     SWITCH, Length: 0x0019, Function to call: 0x0A
5BDA:          03                   ;       Phrase number: 0x03
5BDB:          02                   ;       ELSE go to: 0x5BDE
5BDC:             00 F1             ;         MOVE AND LOOK, Destination room: 0xF1
5BDE:          04                   ;       Phrase number: 0x04
5BDF:          02                   ;       ELSE go to: 0x5BE2
5BE0:             00 F5             ;         MOVE AND LOOK, Destination room: 0xF5
5BE2:          01                   ;       Phrase number: 0x01
5BE3:          02                   ;       ELSE go to: 0x5BE6
5BE4:             00 F3             ;         MOVE AND LOOK, Destination room: 0xF3
5BE6:          02                   ;       Phrase number: 0x02
5BE7:          0A                   ;       ELSE go to: 0x5BF2
5BE8:             0D 08             ;         WHILE PASS, Length: 0x0008
5BEA:                C8             ;           COMMAND 0xC8
5BEB:                30 B7          ;           UNKNOWN1, Data: 0xB7
5BED:                17 9D 00       ;           MOVE TO, Object number: 0x9D, Destination room: 0x00
5BF0:                2F 02          ;           UNKNOWN2 Data: 0x02

5BF2: F7 19 00                      ; Room Number: 0xF7, Length: 0x0019, Data: 0x00
;
5BF5:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5BF7:       AB                      ;     COMMAND 0xAB
;
5BF8:    04 13                      ;   Section COMMANDS, Length: 0x0013
5BFA:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5BFD:          03                   ;       Phrase number: 0x03
5BFE:          02                   ;       ELSE go to: 0x5C01
5BFF:             00 FA             ;         MOVE AND LOOK, Destination room: 0xFA
5C01:          04                   ;       Phrase number: 0x04
5C02:          02                   ;       ELSE go to: 0x5C05
5C03:             00 F7             ;         MOVE AND LOOK, Destination room: 0xF7
5C05:          01                   ;       Phrase number: 0x01
5C06:          02                   ;       ELSE go to: 0x5C09
5C07:             00 F7             ;         MOVE AND LOOK, Destination room: 0xF7
5C09:          02                   ;       Phrase number: 0x02
5C0A:          02                   ;       ELSE go to: 0x5C0D
5C0B:             00 F8             ;         MOVE AND LOOK, Destination room: 0xF8

5C0D: F8 19 00                      ; Room Number: 0xF8, Length: 0x0019, Data: 0x00
;
5C10:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5C12:       AB                      ;     COMMAND 0xAB
;
5C13:    04 13                      ;   Section COMMANDS, Length: 0x0013
5C15:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5C18:          03                   ;       Phrase number: 0x03
5C19:          02                   ;       ELSE go to: 0x5C1C
5C1A:             00 F8             ;         MOVE AND LOOK, Destination room: 0xF8
5C1C:          04                   ;       Phrase number: 0x04
5C1D:          02                   ;       ELSE go to: 0x5C20
5C1E:             00 F9             ;         MOVE AND LOOK, Destination room: 0xF9
5C20:          01                   ;       Phrase number: 0x01
5C21:          02                   ;       ELSE go to: 0x5C24
5C22:             00 F8             ;         MOVE AND LOOK, Destination room: 0xF8
5C24:          02                   ;       Phrase number: 0x02
5C25:          02                   ;       ELSE go to: 0x5C28
5C26:             00 F8             ;         MOVE AND LOOK, Destination room: 0xF8

5C28: F9 21 00                      ; Room Number: 0xF9, Length: 0x0021, Data: 0x00
;
5C2B:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5C2D:       AB                      ;     COMMAND 0xAB
;
5C2E:    04 1B                      ;   Section COMMANDS, Length: 0x001B
5C30:       0B 19 0A                ;     SWITCH, Length: 0x0019, Function to call: 0x0A
5C33:          03                   ;       Phrase number: 0x03
5C34:          0A                   ;       ELSE go to: 0x5C3F
5C35:             0E 08             ;         WHILE FAIL, Length: 0x0008
5C37:                0D 04          ;           WHILE PASS, Length: 0x0004
5C39:                   05 3E       ;             IS LESS OR EQUAL TO LAST RANDOM, Value: 0x3E
5C3B:                   00 86       ;             MOVE AND LOOK, Destination room: 0x86
5C3D:                00 F9          ;           MOVE AND LOOK, Destination room: 0xF9
5C3F:          04                   ;       Phrase number: 0x04
5C40:          02                   ;       ELSE go to: 0x5C43
5C41:             00 F8             ;         MOVE AND LOOK, Destination room: 0xF8
5C43:          01                   ;       Phrase number: 0x01
5C44:          02                   ;       ELSE go to: 0x5C47
5C45:             00 FA             ;         MOVE AND LOOK, Destination room: 0xFA
5C47:          02                   ;       Phrase number: 0x02
5C48:          02                   ;       ELSE go to: 0x5C4B
5C49:             00 F9             ;         MOVE AND LOOK, Destination room: 0xF9

5C4B: FA 19 00                      ; Room Number: 0xFA, Length: 0x0019, Data: 0x00
;
5C4E:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5C50:       AB                      ;     COMMAND 0xAB
;
5C51:    04 13                      ;   Section COMMANDS, Length: 0x0013
5C53:       0B 11 0A                ;     SWITCH, Length: 0x0011, Function to call: 0x0A
5C56:          03                   ;       Phrase number: 0x03
5C57:          02                   ;       ELSE go to: 0x5C5A
5C58:             00 FA             ;         MOVE AND LOOK, Destination room: 0xFA
5C5A:          04                   ;       Phrase number: 0x04
5C5B:          02                   ;       ELSE go to: 0x5C5E
5C5C:             00 F7             ;         MOVE AND LOOK, Destination room: 0xF7
5C5E:          01                   ;       Phrase number: 0x01
5C5F:          02                   ;       ELSE go to: 0x5C62
5C60:             00 FA             ;         MOVE AND LOOK, Destination room: 0xFA
5C62:          02                   ;       Phrase number: 0x02
5C63:          02                   ;       ELSE go to: 0x5C66
5C64:             00 F9             ;         MOVE AND LOOK, Destination room: 0xF9


5C66: 4C 41 54 22 05 53 50 41 52 45 23 04 42 4C 55 45 ; LAT".SPARE#.BLUE
5C76: 0D 06 4D 41 53 53 49 56 3F 04 42 41 4E 4B 40 06 ; ..MASSIV?.BANK@.
5C86: 53 41 4C 4F 4F 4E 41 06 53 48 45 52 49 46 42 06 ; SALOONA.SHERIFB.
5C96: 4F 46 46 49 43 45 42 06 53 4C 49 4D 27 53 43 05 ; OFFICEB.SLIM'SC.
5CA6: 53 4C 49 4D 53 43 05 42 4F 42 27 53 44 04 42 4F ; SLIMSC.BOB'SD.BO
5CB6: 42 53 44 06 44 4F 55 42 4C 45 45 05 48 4F 54 45 ; BSD.DOUBLEE.HOTE
5CC6: 4C 47 06 53 57 49 4E 47 49 46 04 54 53 4F 4D 6B ; LG.SWINGIF.TSOMk
5CD6: 04 43 4F 4F 4C 72 05 43 4C 45 41 52 74 05 42 52 ; .COOLr.CLEARt.BR
5CE6: 4F 57 4E 73 00 02 54 4F 01 04 57 49 54 48 02 05 ; OWNs..TO..WITH..
5CF6: 55 53 49 4E 47 02 02 41 54 03 05 
```

