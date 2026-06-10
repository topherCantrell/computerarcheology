![Xenos](Xenos.png)

# Xenos SECTION7.DAT

>>> cpu Z80

>>> binary 5200:roms/section7.bin

```code
5200: 00 87 7C                      ; List ID: 0x00, Length: 0x077C

5203: 80 49 00                      ; room=80_7_??80??, Length: 0x0049, Data: 0x00
;
5206:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5208:       9D                      ;     ROUTINE 0x9D
;
5209:    04 43                      ;   Section COMMANDS, Length: 0x0043
520B:       0B 41 0A                ;     SWITCH, Length: 0x0041, Function to call: 0x0A
520E:          37                   ;       Phrase 0x37: "CLIMB    *          OUT         *"
520F:          09                   ;       ELSE go to: 0x5219
5210:             0D 07             ;         WHILE PASS, Length: 0x0007
5212:                30 9D          ;           SET CURRENT ROOM, room=9D_5_UFO_CRATER
5214:                17 9D 01       ;           MOVE TO, obj=9D_THIRST_TRACKER, room=01_PLAYER
5217:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
5219:          03                   ;       Phrase 0x03: "EAST     *          *           *"
521A:          09                   ;       ELSE go to: 0x5224
521B:             0D 07             ;         WHILE PASS, Length: 0x0007
521D:                30 9D          ;           SET CURRENT ROOM, room=9D_5_UFO_CRATER
521F:                17 9D 01       ;           MOVE TO, obj=9D_THIRST_TRACKER, room=01_PLAYER
5222:                2F 05          ;           LOAD SECTION FROM DISK, Section: 0x05
5224:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
5225:          16                   ;       ELSE go to: 0x523C
5226:             0E 14             ;         WHILE FAIL, Length: 0x0014
5228:                0D 11          ;           WHILE PASS, Length: 0x0011
522A:                   14          ;             EXECUTE AND REVERSE STATUS
522B:                   03 67 81    ;             IS LOCATED, room=obj_67, obj=??81??
522E:                   04 0B       ;             PRINT, Length: 0x000B
5230:                      06 9A 90 73 CA 6A EA 48 9D 61 2E ; 
;
;                          NOTHING HAPPENS.
;
523B:                9F             ;           ROUTINE 0x9F
523C:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
523D:          10                   ;       ELSE go to: 0x524E
523E:             0D 0E             ;         WHILE PASS, Length: 0x000E
5240:                C0             ;           ROUTINE 0xC0
5241:                0E 0B          ;           WHILE FAIL, Length: 0x000B
5243:                   AE          ;             ROUTINE 0xAE
5244:                   14          ;             EXECUTE AND REVERSE STATUS
5245:                   0B 06 03    ;             SWITCH, Length: 0x0006, Function to call: 0x03
5248:                      3F       ;               Phrase 0x3F: "SAVE     *          *           *"
5249:                      3E       ;               ELSE go to: 0x5288
524A:                         02 00 82 ;                 IS OWNED BY, A=0x82, obj=??00??
524D:                   9E          ;             ROUTINE 0x9E

524E: 82 80 E0 00                   ; room=82_7_SREENJARMA_LOUNGE, Length: 0x00E0, Data: 0x00
;
5252:    03 80 AF                   ;   Section DESCRIPTION, Length: 0x00AF
5255:       0D 80 AC                ;     WHILE PASS, Length: 0x00AC
5258:          04 07                ;       PRINT, Length: 0x0007
525A:             AF B9 94 61 37 49 41 ; 
;
;                 SREENJARMA
;
5261:          0E 07                ;       WHILE FAIL, Length: 0x0007
5263:             C3                ;         ROUTINE 0xC3
5264:             04 04             ;         PRINT, Length: 0x0004
5266:                87 8D B7 98    ; 
;
;                    LOUNGE
;
526A:          8B                   ;       ROUTINE 0x8B
526B:          04 80 96             ;       PRINT, Length: 0x0096
526E:             51 18 43 C2 5B B1 09 9A D0 15 7B 14 54 8B 9B 6C ; 
527E:             65 B1 50 BD 2E 6F 23 49 01 B3 DB 95 83 48 34 60 ; 
528E:             1B 79 C8 93 91 7A E3 16 0F 56 5B B1 C5 65 4B 62 ; 
529E:             C7 DE 51 F4 96 96 DB 72 0E D0 04 8A A3 60 33 98 ; 
52AE:             C7 DE 82 17 2F 62 94 14 56 5E EF 74 44 5E 8E C6 ; 
52BE:             1D A0 11 EE 5B 98 66 B1 11 EE 5B 98 8F 4E B3 63 ; 
52CE:             8E 48 C0 16 5B 5E 46 61 8F A1 82 17 3B 63 2F 49 ; 
52DE:             94 14 D0 B0 A6 6C A9 15 1C B2 1E A0 46 48 B3 E0 ; 
52EE:             56 D1 16 71 DB 72 66 B1 BF 14 49 C0 91 96 96 96 ; 
52FE:             DB 72 09 B2 57 75 ; 
;
;                  YOU ARE NOW IN A LARGE RECTANGULAR ROOM. AN EERIE MOVING
;                 PICTURE FACES YOU. ON THE WALL BEHIND YOU THERE ARE THREE
;                 BUTTONS, ONE RED, ONE BLUE, AND ONE YELLOW. THEY ARE
;                 ARRANGED HORIZONTALLY, WITH THE RED BUTTON ON THE RIGHT.
;
;
5304:    04 2B                      ;   Section COMMANDS, Length: 0x002B
5306:       0B 29 0A                ;     SWITCH, Length: 0x0029, Function to call: 0x0A
5309:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
530A:          05                   ;       ELSE go to: 0x5310
530B:             0E 03             ;         WHILE FAIL, Length: 0x0003
530D:                A0             ;           ROUTINE 0xA0
530E:                A1             ;           ROUTINE 0xA1
530F:                9F             ;           ROUTINE 0x9F
5310:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5311:          1F                   ;       ELSE go to: 0x5331
5312:             0D 1D             ;         WHILE PASS, Length: 0x001D
5314:                C0             ;           ROUTINE 0xC0
5315:                0E 1A          ;           WHILE FAIL, Length: 0x001A
5317:                   AE          ;             ROUTINE 0xAE
5318:                   14          ;             EXECUTE AND REVERSE STATUS
5319:                   0B 15 03    ;             SWITCH, Length: 0x0015, Function to call: 0x03
531C:                      3F       ;               Phrase 0x3F: "SAVE     *          *           *"
531D:                      3E       ;               ELSE go to: 0x535C
531E:                         02 00 80 ;                 IS OWNED BY, A=0x80, obj=??00??
5321:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5322:                      3E       ;               ELSE go to: 0x5361
5323:                         02 00 83 ;                 IS OWNED BY, A=0x83, obj=??00??
5326:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5327:                      3E       ;               ELSE go to: 0x5366
5328:                         07    ;                 PRINT ROOM DESCRIPTION
5329:                      0D       ;               Phrase 0x0D: "THROW    .vC.....   AT       ...P...."
532A:                      05       ;               ELSE go to: 0x5330
532B:                         9E    ;                 ROUTINE 0x9E
532C:                      30       ;               Phrase 0x30: "??30??"
532D:                      84 2F    ;               ELSE go to: 0x575E
532F:                         08 9E ;                 IS FIRST NOUN, Word number: 0x9E

5331: 83 2C 00                      ; room=83_7_??83??, Length: 0x002C, Data: 0x00
;
5334:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5336:       B0                      ;     ROUTINE 0xB0
;
5337:    04 26                      ;   Section COMMANDS, Length: 0x0026
5339:       0B 24 0A                ;     SWITCH, Length: 0x0024, Function to call: 0x0A
533C:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
533D:          05                   ;       ELSE go to: 0x5343
533E:             0E 03             ;         WHILE FAIL, Length: 0x0003
5340:                9F             ;           ROUTINE 0x9F
5341:                A0             ;           ROUTINE 0xA0
5342:                A1             ;           ROUTINE 0xA1
5343:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5344:          1A                   ;       ELSE go to: 0x535F
5345:             0D 18             ;         WHILE PASS, Length: 0x0018
5347:                C0             ;           ROUTINE 0xC0
5348:                0E 15          ;           WHILE FAIL, Length: 0x0015
534A:                   AE          ;             ROUTINE 0xAE
534B:                   14          ;             EXECUTE AND REVERSE STATUS
534C:                   0B 10 03    ;             SWITCH, Length: 0x0010, Function to call: 0x03
534F:                      3F       ;               Phrase 0x3F: "SAVE     *          *           *"
5350:                      3E       ;               ELSE go to: 0x538F
5351:                         02 00 93 ;                 IS OWNED BY, A=0x93, obj=??00??
5354:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5355:                      3E       ;               ELSE go to: 0x5394
5356:                         02 00 85 ;                 IS OWNED BY, A=0x85, obj=??00??
5359:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
535A:                      3E       ;               ELSE go to: 0x5399
535B:                         02 00 82 ;                 IS OWNED BY, A=0x82, obj=??00??
535E:                   9E          ;             ROUTINE 0x9E

535F: 85 80 D2 00                   ; room=85_7_PURBLEEBLE_SLEEPING, Length: 0x00D2, Data: 0x00
;
5363:    03 80 AC                   ;   Section DESCRIPTION, Length: 0x00AC
5366:       0D 80 A9                ;     WHILE PASS, Length: 0x00A9
5369:          04 07                ;       PRINT, Length: 0x0007
536B:             74 A7 7F 4E B6 5F 45 ; 
;
;                 PURBLEEBLE
;
5372:          0E 09                ;       WHILE FAIL, Length: 0x0009
5374:             C3                ;         ROUTINE 0xC3
5375:             04 06             ;         PRINT, Length: 0x0006
5377:                BF B8 E3 61 AB 98 ; 
;
;                    SLEEPING 
;
537D:          8B                   ;       ROUTINE 0x8B
537E:          04 80 91             ;       PRINT, Length: 0x0091
5381:             C7 DE 99 16 C8 CE 8E 7A 51 18 3D C6 40 61 D0 15 ; 
5391:             7B 14 8F 5A FB 8E 96 8C E7 14 05 4E FF 8B 82 17 ; 
53A1:             2F 62 D5 15 7B 14 CE 56 8E 7A 23 62 56 D1 03 71 ; 
53B1:             7E 15 65 49 43 16 03 58 0B 6C A6 9A C0 16 59 5E ; 
53C1:             46 48 44 F4 A3 60 33 98 C7 DE 51 18 46 C2 55 7B ; 
53D1:             4F A1 96 AF DB 72 0E D0 0A 8A 4B 49 C1 C0 BF 14 ; 
53E1:             49 C0 8B 9A 03 A0 96 7B 7B 14 66 B1 BF 14 49 C0 ; 
53F1:             83 96 33 98 44 45 67 8E BF 14 49 C0 F3 9B 3C 49 ; 
5401:             91 48 F3 5F 79 68 4E 90 5E 60 89 17 33 17 2E 6D ; 
5411:             2E                ; 
;
;                 YOU NOW FIND YOURSELF IN A DIMLY LIT CUBICLE. THERE IS A
;                 CYLINDER WITH A GLASS LID AGAINST ONE WALL. BEHIND YOU YOU
;                 DISCOVER THE WALL HAS TWO BUTTONS ON IT, A RED BUTTON AND A
;                 BLUE BUTTON, ARRANGED FROM LEFT TO RIGHT.
;
;
5412:    04 20                      ;   Section COMMANDS, Length: 0x0020
5414:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
5417:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
5418:          04                   ;       ELSE go to: 0x541D
5419:             0E 02             ;         WHILE FAIL, Length: 0x0002
541B:                A0             ;           ROUTINE 0xA0
541C:                A1             ;           ROUTINE 0xA1
541D:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
541E:          15                   ;       ELSE go to: 0x5434
541F:             0D 13             ;         WHILE PASS, Length: 0x0013
5421:                C0             ;           ROUTINE 0xC0
5422:                0E 10          ;           WHILE FAIL, Length: 0x0010
5424:                   AE          ;             ROUTINE 0xAE
5425:                   14          ;             EXECUTE AND REVERSE STATUS
5426:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
5429:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
542A:                      3E       ;               ELSE go to: 0x5469
542B:                         02 00 87 ;                 IS OWNED BY, A=0x87, obj=??00??
542E:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
542F:                      3E       ;               ELSE go to: 0x546E
5430:                         02 00 83 ;                 IS OWNED BY, A=0x83, obj=??00??
5433:                   9E          ;             ROUTINE 0x9E

5434: 87 26 00                      ; room=87_7_??87??, Length: 0x0026, Data: 0x00
;
5437:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5439:       9C                      ;     ROUTINE 0x9C
;
543A:    04 20                      ;   Section COMMANDS, Length: 0x0020
543C:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
543F:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
5440:          04                   ;       ELSE go to: 0x5445
5441:             0E 02             ;         WHILE FAIL, Length: 0x0002
5443:                A0             ;           ROUTINE 0xA0
5444:                A1             ;           ROUTINE 0xA1
5445:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5446:          15                   ;       ELSE go to: 0x545C
5447:             0D 13             ;         WHILE PASS, Length: 0x0013
5449:                C0             ;           ROUTINE 0xC0
544A:                0E 10          ;           WHILE FAIL, Length: 0x0010
544C:                   AE          ;             ROUTINE 0xAE
544D:                   14          ;             EXECUTE AND REVERSE STATUS
544E:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
5451:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5452:                      3E       ;               ELSE go to: 0x5491
5453:                         02 00 89 ;                 IS OWNED BY, A=0x89, obj=??00??
5456:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5457:                      3E       ;               ELSE go to: 0x5496
5458:                         02 00 85 ;                 IS OWNED BY, A=0x85, obj=??00??
545B:                   9E          ;             ROUTINE 0x9E

545C: 89 80 C9 00                   ; room=89_7_MAIKGO_CONTROL, Length: 0x00C9, Data: 0x00
;
5460:    03 80 A3                   ;   Section DESCRIPTION, Length: 0x00A3
5463:       0D 80 A0                ;     WHILE PASS, Length: 0x00A0
5466:          04 04                ;       PRINT, Length: 0x0004
5468:             8B 91 01 86       ; 
;
;                 MAIKGO
;
546C:          0E 08                ;       WHILE FAIL, Length: 0x0008
546E:             C3                ;         ROUTINE 0xC3
546F:             04 05             ;         PRINT, Length: 0x0005
5471:                40 55 F9 BF 4C ; 
;
;                    CONTROL
;
5476:          8B                   ;       ROUTINE 0x8B
5477:          04 80 8C             ;       PRINT, Length: 0x008C
547A:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 39 17 DB 9F ; 
548A:             56 D1 04 71 45 8B D9 83 46 48 5B BB 83 7A 5F BE ; 
549A:             D7 14 BF 9A 91 AF 96 64 DB 72 01 B3 4B 90 C3 B5 ; 
54AA:             5F 17 46 48 DA 14 D4 47 4B 15 50 54 C3 6A 5F 17 ; 
54BA:             46 48 E1 14 CC 9A B3 9F 50 A4 57 61 82 17 59 5E ; 
54CA:             46 48 AF 14 90 73 16 58 DB 72 1B 54 23 7B 55 72 ; 
54DA:             B2 17 03 A0 73 7B 52 45 D4 47 B8 16 7F 17 F2 8B ; 
54EA:             BE A0 33 48 F6 4F 80 BF 33 BB 0F A0 D5 15 2F 17 ; 
54FA:             03 58 33 98 0F A0 D5 15 B6 14 3F C4 ; 
;
;                 YOU ARE IN A SMALL ROOM WITH BLACK WALLS. IN THE CENTER OF
;                 THE ROOM IS A SMALL CHAIR FACING A SMALL CONTROL PANEL. THE
;                 WALL BEHIND THE CHAIR HAS UPON IT A PAIR OF TELEPORTAL
;                 BUTTONS, ONE IS RED AND ONE IS BLUE.
;
;
5506:    04 20                      ;   Section COMMANDS, Length: 0x0020
5508:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
550B:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
550C:          04                   ;       ELSE go to: 0x5511
550D:             0E 02             ;         WHILE FAIL, Length: 0x0002
550F:                A0             ;           ROUTINE 0xA0
5510:                A1             ;           ROUTINE 0xA1
5511:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5512:          15                   ;       ELSE go to: 0x5528
5513:             0D 13             ;         WHILE PASS, Length: 0x0013
5515:                C0             ;           ROUTINE 0xC0
5516:                0E 10          ;           WHILE FAIL, Length: 0x0010
5518:                   AE          ;             ROUTINE 0xAE
5519:                   14          ;             EXECUTE AND REVERSE STATUS
551A:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
551D:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
551E:                      3E       ;               ELSE go to: 0x555D
551F:                         02 00 8B ;                 IS OWNED BY, A=0x8B, obj=??00??
5522:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5523:                      3E       ;               ELSE go to: 0x5562
5524:                         02 00 87 ;                 IS OWNED BY, A=0x87, obj=??00??
5527:                   9E          ;             ROUTINE 0x9E

5528: 8B 26 00                      ; room=8B_7_??8B??, Length: 0x0026, Data: 0x00
;
552B:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
552D:       9C                      ;     ROUTINE 0x9C
;
552E:    04 20                      ;   Section COMMANDS, Length: 0x0020
5530:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
5533:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
5534:          04                   ;       ELSE go to: 0x5539
5535:             0E 02             ;         WHILE FAIL, Length: 0x0002
5537:                A0             ;           ROUTINE 0xA0
5538:                A1             ;           ROUTINE 0xA1
5539:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
553A:          15                   ;       ELSE go to: 0x5550
553B:             0D 13             ;         WHILE PASS, Length: 0x0013
553D:                C0             ;           ROUTINE 0xC0
553E:                0E 10          ;           WHILE FAIL, Length: 0x0010
5540:                   AE          ;             ROUTINE 0xAE
5541:                   14          ;             EXECUTE AND REVERSE STATUS
5542:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
5545:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5546:                      3E       ;               ELSE go to: 0x5585
5547:                         02 00 8D ;                 IS OWNED BY, A=0x8D, obj=??00??
554A:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
554B:                      3E       ;               ELSE go to: 0x558A
554C:                         02 00 89 ;                 IS OWNED BY, A=0x89, obj=??00??
554F:                   9E          ;             ROUTINE 0x9E

5550: 8D 80 DE 00                   ; room=8D_7_NAHLUDJ_LIBRARY, Length: 0x00DE, Data: 0x00
;
5554:    03 80 C0                   ;   Section DESCRIPTION, Length: 0x00C0
5557:       0D 80 BD                ;     WHILE PASS, Length: 0x00BD
555A:          04 05                ;       PRINT, Length: 0x0005
555C:             CA 97 66 8E 4A    ; 
;
;                 NAHLUDJ
;
5561:          0E 08                ;       WHILE FAIL, Length: 0x0008
5563:             C3                ;         ROUTINE 0xC3
5564:             04 05             ;         PRINT, Length: 0x0005
5566:                84 8C D4 B0 59 ; 
;
;                    LIBRARY
;
556B:          8B                   ;       ROUTINE 0x8B
556C:          04 80 A8             ;       PRINT, Length: 0x00A8
556F:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 2F 17 FB 55 ; 
557F:             C7 98 54 8B 39 17 FF 9F D0 15 82 17 45 5E 9E 61 ; 
558F:             23 62 C3 9E 5F BE 39 17 DB 9F 4B 7B 45 45 4B 72 ; 
559F:             F3 B4 23 D1 13 54 C5 65 4B 62 4E 45 31 49 45 5E ; 
55AF:             AF C3 56 F4 F4 72 4B 5E C3 B5 5F 17 46 48 63 17 ; 
55BF:             94 C3 4A 5E BF 9F 84 14 36 A1 91 17 CB 9C 1A 98 ; 
55CF:             4B 62 E7 59 0B A3 96 96 DB 72 82 BF B8 16 82 17 ; 
55DF:             45 5E AF C3 43 F4 E7 14 A1 B3 7B B4 9D 7A E5 A4 ; 
55EF:             91 BE 91 96 96 64 DB 72 01 B3 54 90 CF 62 4D 48 ; 
55FF:             7B 14 8F 4E 44 5E 8E C6 03 A0 03 A0 0F A0 B8 16 ; 
560F:             82 17 59 5E 46 48 5B BB ; 
;
;                 YOU ARE IN A SMALL RECTANGULAR ROOM. IN THE CENTER OF THE
;                 ROOM IS A CHAIR, WHICH FACES A LARGE CUBE. THERE IS A SMALL
;                 SQUARE HOLE ABOUT TWO INCHES DEEP IN THE TOP OF THE CUBE. A
;                 CURSORY INSPECTION OF THE ROOM REVEALS A BLUE BUTTON ON ONE
;                 OF THE WALLS.
;
;
5617:    04 18                      ;   Section COMMANDS, Length: 0x0018
5619:       0B 16 0A                ;     SWITCH, Length: 0x0016, Function to call: 0x0A
561C:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
561D:          01                   ;       ELSE go to: 0x561F
561E:             A1                ;         ROUTINE 0xA1
561F:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5620:          10                   ;       ELSE go to: 0x5631
5621:             0D 0E             ;         WHILE PASS, Length: 0x000E
5623:                C0             ;           ROUTINE 0xC0
5624:                0E 0B          ;           WHILE FAIL, Length: 0x000B
5626:                   AE          ;             ROUTINE 0xAE
5627:                   14          ;             EXECUTE AND REVERSE STATUS
5628:                   0B 06 03    ;             SWITCH, Length: 0x0006, Function to call: 0x03
562B:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
562C:                      3E       ;               ELSE go to: 0x566B
562D:                         02 00 8B ;                 IS OWNED BY, A=0x8B, obj=??00??
5630:                   9E          ;             ROUTINE 0x9E

5631: 93 2C 00                      ; room=93_7_??93??, Length: 0x002C, Data: 0x00
;
5634:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
5636:       B0                      ;     ROUTINE 0xB0
;
5637:    04 26                      ;   Section COMMANDS, Length: 0x0026
5639:       0B 24 0A                ;     SWITCH, Length: 0x0024, Function to call: 0x0A
563C:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
563D:          05                   ;       ELSE go to: 0x5643
563E:             0E 03             ;         WHILE FAIL, Length: 0x0003
5640:                A0             ;           ROUTINE 0xA0
5641:                A1             ;           ROUTINE 0xA1
5642:                9F             ;           ROUTINE 0x9F
5643:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
5644:          1A                   ;       ELSE go to: 0x565F
5645:             0D 18             ;         WHILE PASS, Length: 0x0018
5647:                C0             ;           ROUTINE 0xC0
5648:                0E 15          ;           WHILE FAIL, Length: 0x0015
564A:                   AE          ;             ROUTINE 0xAE
564B:                   14          ;             EXECUTE AND REVERSE STATUS
564C:                   0B 10 03    ;             SWITCH, Length: 0x0010, Function to call: 0x03
564F:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5650:                      3E       ;               ELSE go to: 0x568F
5651:                         02 00 95 ;                 IS OWNED BY, A=0x95, obj=??00??
5654:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
5655:                      3E       ;               ELSE go to: 0x5694
5656:                         02 00 94 ;                 IS OWNED BY, A=0x94, obj=??00??
5659:                      3F       ;               Phrase 0x3F: "SAVE     *          *           *"
565A:                      3E       ;               ELSE go to: 0x5699
565B:                         02 00 83 ;                 IS OWNED BY, A=0x83, obj=??00??
565E:                   9E          ;             ROUTINE 0x9E

565F: 94 80 A9 00                   ; room=94_7_EZPRUNJ_BOMBS, Length: 0x00A9, Data: 0x00
;
5663:    03 80 8B                   ;   Section DESCRIPTION, Length: 0x008B
5666:       0D 80 88                ;     WHILE PASS, Length: 0x0088
5669:          04 05                ;       PRINT, Length: 0x0005
566B:             7A 63 F0 B3 4A    ; 
;
;                 EZPRUNJ
;
5670:          0E 07                ;       WHILE FAIL, Length: 0x0007
5672:             C3                ;         ROUTINE 0xC3
5673:             04 04             ;         PRINT, Length: 0x0004
5675:                FF 4E 8B 4F    ; 
;
;                    BOMBS 
;
5679:          8B                   ;       ROUTINE 0x8B
567A:          04 75                ;       PRINT, Length: 0x0075
567C:             C7 DE 94 14 4B 5E 83 96 49 16 CE 98 8B 16 79 B3 ; 
568C:             D4 CE 3F A0 82 17 73 49 4B 7B EE 68 11 8A 85 64 ; 
569C:             43 DE 3F 98 8B B3 5B BE 03 BC 5B B1 83 7A 55 45 ; 
56AC:             33 62 4B 62 C3 9E FB B9 A5 54 82 17 73 49 90 8C ; 
56BC:             56 5E DB 72 80 8D B4 6C F3 17 0D 8D 51 F4 96 96 ; 
56CC:             DB 72 29 B8 B3 B3 0E D0 04 8A A3 60 33 98 C7 DE ; 
56DC:             1B EE 1B A1 10 67 03 58 5B 17 BE 98 54 5E F3 5F ; 
56EC:             F6 4F 80 BF 2E    ; 
;
;                 YOU ARE IN A LONG, NARROW ROOM THAT IS FULL OF CYLINDERS
;                 THAT ARE IN A SERIES OF STACKS THAT LINE THE LONGER WALLS.
;                 ON THE SHORT WALL BEHIND YOU, YOU FIND A SINGLE RED BUTTON.
;
;
56F1:    04 18                      ;   Section COMMANDS, Length: 0x0018
56F3:       0B 16 0A                ;     SWITCH, Length: 0x0016, Function to call: 0x0A
56F6:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
56F7:          01                   ;       ELSE go to: 0x56F9
56F8:             A0                ;         ROUTINE 0xA0
56F9:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
56FA:          10                   ;       ELSE go to: 0x570B
56FB:             0D 0E             ;         WHILE PASS, Length: 0x000E
56FD:                C0             ;           ROUTINE 0xC0
56FE:                0E 0B          ;           WHILE FAIL, Length: 0x000B
5700:                   AE          ;             ROUTINE 0xAE
5701:                   14          ;             EXECUTE AND REVERSE STATUS
5702:                   0B 06 03    ;             SWITCH, Length: 0x0006, Function to call: 0x03
5705:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5706:                      3E       ;               ELSE go to: 0x5745
5707:                         02 00 93 ;                 IS OWNED BY, A=0x93, obj=??00??
570A:                   9E          ;             ROUTINE 0x9E

570B: 95 80 D9 00                   ; room=95_7_SNOOXBUR_GAS, Length: 0x00D9, Data: 0x00
;
570F:    03 80 B3                   ;   Section DESCRIPTION, Length: 0x00B3
5712:       0D 80 B0                ;     WHILE PASS, Length: 0x00B0
5715:          04 06                ;       PRINT, Length: 0x0006
5717:             19 B9 9C A1 23 C6 ; 
;
;                 SNOOXBUR 
;
571D:          0E 05                ;       WHILE FAIL, Length: 0x0005
571F:             C3                ;         ROUTINE 0xC3
5720:             04 02             ;         PRINT, Length: 0x0002
5722:                15 6C          ; 
;
;                    GAS
;
5724:          8B                   ;       ROUTINE 0x8B
5725:          04 80 9D             ;       PRINT, Length: 0x009D
5728:             C7 DE 94 14 4B 5E 83 96 49 16 CE 98 8B 16 79 B3 ; 
5738:             D4 CE 3F A0 82 17 73 49 4B 7B EE 68 11 8A 85 64 ; 
5748:             43 DE 3F 98 8B B3 5B BE 03 BC 5B B1 83 7A 55 45 ; 
5758:             33 62 4B 62 C3 9E FB B9 A5 54 82 17 73 49 90 8C ; 
5768:             56 5E DB 72 80 8D B4 6C F3 17 0D 8D 51 F4 96 96 ; 
5778:             DB 72 29 B8 B3 B3 0E D0 04 8A A3 60 33 98 C7 DE ; 
5788:             16 EE F4 72 43 5E 5B B1 44 45 67 8E 90 14 03 58 ; 
5798:             2F 17 04 58 8E C6 03 A0 3C 49 91 48 F3 5F 84 74 ; 
57A8:             79 7C BB 9A 13 8D 81 15 91 7A 5C 15 DB 9F 5F BE ; 
57B8:             33 17 2E 6D 89 17 82 17 4E 5E 5E 60 2E ; 
;
;                 YOU ARE IN A LONG, NARROW ROOM THAT IS FULL OF CYLINDERS
;                 THAT ARE IN A SERIES OF STACKS THAT LINE THE LONGER WALLS.
;                 ON THE SHORT WALL BEHIND YOU, THERE ARE A BLUE AND A RED
;                 BUTTON ARRANGED HORIZONTALLY GOING FROM THE RIGHT TO THE
;                 LEFT.
;
;
57C5:    04 20                      ;   Section COMMANDS, Length: 0x0020
57C7:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
57CA:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
57CB:          04                   ;       ELSE go to: 0x57D0
57CC:             0E 02             ;         WHILE FAIL, Length: 0x0002
57CE:                A0             ;           ROUTINE 0xA0
57CF:                A1             ;           ROUTINE 0xA1
57D0:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
57D1:          15                   ;       ELSE go to: 0x57E7
57D2:             0D 13             ;         WHILE PASS, Length: 0x0013
57D4:                C0             ;           ROUTINE 0xC0
57D5:                0E 10          ;           WHILE FAIL, Length: 0x0010
57D7:                   AE          ;             ROUTINE 0xAE
57D8:                   14          ;             EXECUTE AND REVERSE STATUS
57D9:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
57DC:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
57DD:                      3E       ;               ELSE go to: 0x581C
57DE:                         02 00 96 ;                 IS OWNED BY, A=0x96, obj=??00??
57E1:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
57E2:                      3E       ;               ELSE go to: 0x5821
57E3:                         02 00 93 ;                 IS OWNED BY, A=0x93, obj=??00??
57E6:                   9E          ;             ROUTINE 0x9E

57E7: 96 26 00                      ; room=96_7_??96??, Length: 0x0026, Data: 0x00
;
57EA:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
57EC:       9C                      ;     ROUTINE 0x9C
;
57ED:    04 20                      ;   Section COMMANDS, Length: 0x0020
57EF:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
57F2:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
57F3:          04                   ;       ELSE go to: 0x57F8
57F4:             0E 02             ;         WHILE FAIL, Length: 0x0002
57F6:                A0             ;           ROUTINE 0xA0
57F7:                A1             ;           ROUTINE 0xA1
57F8:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
57F9:          15                   ;       ELSE go to: 0x580F
57FA:             0D 13             ;         WHILE PASS, Length: 0x0013
57FC:                C0             ;           ROUTINE 0xC0
57FD:                0E 10          ;           WHILE FAIL, Length: 0x0010
57FF:                   AE          ;             ROUTINE 0xAE
5800:                   14          ;             EXECUTE AND REVERSE STATUS
5801:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
5804:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
5805:                      3E       ;               ELSE go to: 0x5844
5806:                         02 00 97 ;                 IS OWNED BY, A=0x97, obj=??00??
5809:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
580A:                      3E       ;               ELSE go to: 0x5849
580B:                         02 00 95 ;                 IS OWNED BY, A=0x95, obj=??00??
580E:                   9E          ;             ROUTINE 0x9E

580F: 97 80 AD 00                   ; room=97_7_ECTOBLASM_BIO, Length: 0x00AD, Data: 0x00
;
5813:    03 80 87                   ;   Section DESCRIPTION, Length: 0x0087
5816:       0D 80 84                ;     WHILE PASS, Length: 0x0084
5819:          04 06                ;       PRINT, Length: 0x0006
581B:             E6 5F 36 9E 5F 49 ; 
;
;                 ECTOBLASM
;
5821:          0E 05                ;       WHILE FAIL, Length: 0x0005
5823:             C3                ;         ROUTINE 0xC3
5824:             04 02             ;         PRINT, Length: 0x0002
5826:                11 4E          ; 
;
;                    BIO
;
5828:          8B                   ;       ROUTINE 0x8B
5829:          04 72                ;       PRINT, Length: 0x0072
582B:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 39 17 FE 9F ; 
583B:             82 17 2F 62 94 14 55 5E CF 62 CE B0 B6 14 DD 46 ; 
584B:             7E 15 2F 9E CB B5 95 96 45 BD CB 87 73 47 9D 7A ; 
585B:             16 BC DB 72 0E D0 2F 8E C0 16 82 17 59 5E 46 48 ; 
586B:             AF 14 90 73 1B 58 3E A1 82 17 2F 62 D5 15 7B 14 ; 
587B:             66 B1 90 14 03 58 B6 14 1B C4 F6 4F 80 BF 94 14 ; 
588B:             D0 B0 A6 6C 5C 15 DB 9F E8 8B 16 BC D4 9C 7A 79 ; 
589B:             9B C1             ; 
;
;                 YOU ARE IN A SMALL ROOM, THERE ARE SEVERAL BLACK GLOBES IN
;                 STACKS AGAINST THE WALLS. ON THE WALL BEHIND YOU, THERE IS
;                 A RED AND A BLUE BUTTON ARRANGED FROM LEFT TO RIGHT.
;
;
589D:    04 20                      ;   Section COMMANDS, Length: 0x0020
589F:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
58A2:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
58A3:          04                   ;       ELSE go to: 0x58A8
58A4:             0E 02             ;         WHILE FAIL, Length: 0x0002
58A6:                A0             ;           ROUTINE 0xA0
58A7:                A1             ;           ROUTINE 0xA1
58A8:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
58A9:          15                   ;       ELSE go to: 0x58BF
58AA:             0D 13             ;         WHILE PASS, Length: 0x0013
58AC:                C0             ;           ROUTINE 0xC0
58AD:                0E 10          ;           WHILE FAIL, Length: 0x0010
58AF:                   AE          ;             ROUTINE 0xAE
58B0:                   14          ;             EXECUTE AND REVERSE STATUS
58B1:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
58B4:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
58B5:                      3E       ;               ELSE go to: 0x58F4
58B6:                         02 00 98 ;                 IS OWNED BY, A=0x98, obj=??00??
58B9:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
58BA:                      3E       ;               ELSE go to: 0x58F9
58BB:                         02 00 96 ;                 IS OWNED BY, A=0x96, obj=??00??
58BE:                   9E          ;             ROUTINE 0x9E

58BF: 98 26 00                      ; room=98_7_??98??, Length: 0x0026, Data: 0x00
;
58C2:    03 01                      ;   Section DESCRIPTION, Length: 0x0001
58C4:       9C                      ;     ROUTINE 0x9C
;
58C5:    04 20                      ;   Section COMMANDS, Length: 0x0020
58C7:       0B 1E 0A                ;     SWITCH, Length: 0x001E, Function to call: 0x0A
58CA:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
58CB:          04                   ;       ELSE go to: 0x58D0
58CC:             0E 02             ;         WHILE FAIL, Length: 0x0002
58CE:                A0             ;           ROUTINE 0xA0
58CF:                A1             ;           ROUTINE 0xA1
58D0:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
58D1:          15                   ;       ELSE go to: 0x58E7
58D2:             0D 13             ;         WHILE PASS, Length: 0x0013
58D4:                C0             ;           ROUTINE 0xC0
58D5:                0E 10          ;           WHILE FAIL, Length: 0x0010
58D7:                   AE          ;             ROUTINE 0xAE
58D8:                   14          ;             EXECUTE AND REVERSE STATUS
58D9:                   0B 0B 03    ;             SWITCH, Length: 0x000B, Function to call: 0x03
58DC:                      40       ;               Phrase 0x40: "CLOSE    ....A...   *           *"
58DD:                      3E       ;               ELSE go to: 0x591C
58DE:                         02 00 99 ;                 IS OWNED BY, A=0x99, obj=??00??
58E1:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
58E2:                      3E       ;               ELSE go to: 0x5921
58E3:                         02 00 97 ;                 IS OWNED BY, A=0x97, obj=??00??
58E6:                   9E          ;             ROUTINE 0x9E

58E7: 99 80 95 00                   ; room=99_7_KEEPRINJ_STORAGE, Length: 0x0095, Data: 0x00
;
58EB:    03 78                      ;   Section DESCRIPTION, Length: 0x0078
58ED:       0D 76                   ;     WHILE PASS, Length: 0x0076
58EF:          04 06                ;       PRINT, Length: 0x0006
58F1:             A7 85 F3 A6 23 99 ; 
;
;                 KEEPRINJ 
;
58F7:          0E 08                ;       WHILE FAIL, Length: 0x0008
58F9:             C3                ;         ROUTINE 0xC3
58FA:             04 05             ;         PRINT, Length: 0x0005
58FC:                09 BA C9 B0 45 ; 
;
;                    STORAGE
;
5901:          8B                   ;       ROUTINE 0x8B
5902:          04 61                ;       PRINT, Length: 0x0061
5904:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 39 17 FE 9F ; 
5914:             82 17 2F 62 94 14 55 5E CF 62 CE B0 EB 14 90 8C ; 
5924:             F4 59 D5 B5 84 BF F3 5F 83 7A 55 45 45 BD D1 83 ; 
5934:             A9 A6 56 B8 5B 5E 3F A1 89 17 82 17 55 5E FF 78 ; 
5944:             1B EE 1B A1 10 53 57 17 43 5E 61 17 96 8C 43 49 ; 
5954:             B6 14 1B C4 F6 4F 80 BF C0 16 82 17 59 5E 46 48 ; 
5964:             2E                ; 
;
;                 YOU ARE IN A SMALL ROOM, THERE ARE SEVERAL CYLINDERS STORED
;                 IN A STACK OPPOSITE YOU. TO THE SIDE, YOU CAN SEE A
;                 SOLITARY BLUE BUTTON ON THE WALL.
;
;
5965:    04 18                      ;   Section COMMANDS, Length: 0x0018
5967:       0B 16 0A                ;     SWITCH, Length: 0x0016, Function to call: 0x0A
596A:          12                   ;       Phrase 0x12: "PULL     u.......   *           *"
596B:          01                   ;       ELSE go to: 0x596D
596C:             A1                ;         ROUTINE 0xA1
596D:          36                   ;       Phrase 0x36: "ENTER    *          *           *"
596E:          10                   ;       ELSE go to: 0x597F
596F:             0D 0E             ;         WHILE PASS, Length: 0x000E
5971:                C0             ;           ROUTINE 0xC0
5972:                0E 0B          ;           WHILE FAIL, Length: 0x000B
5974:                   AE          ;             ROUTINE 0xAE
5975:                   14          ;             EXECUTE AND REVERSE STATUS
5976:                   0B 06 03    ;             SWITCH, Length: 0x0006, Function to call: 0x03
5979:                      41       ;               Phrase 0x41: "LOCK     ....A...   WITH     u......."
597A:                      3E       ;               ELSE go to: 0x59B9
597B:                         02 00 98 ;                 IS OWNED BY, A=0x98, obj=??00??
597E:                   9E          ;             ROUTINE 0x9E
```

```code
597F: 19 00 03 01 AB 04 13 0B 11 0A 03 02 00 FA 04 02 ; ................
598F: 00 F7 01 02 00 FA 02 02 00 F9 06 E8 1D 00 03 01 ; ................
599F: AB 04 17 0B 15 0A 03 06 0D 04 30 E7 2F 06 04 02 ; ..........0./...
59AF: 00 E9 01 02 00 D3 02 02 00 F2 E9 1C 00 03 04 0D ; ................
59BF: 02 AB 95 04 13 0B 11 0A 03 02 00 D4 04 02 00 F3 ; ................
59CF: 01 02 00 EA 02 02 00 E8 EA 19 00 03 01 AB 04 13 ; ................
59DF: 0B 11 0A 03 02 00 E9 04 02 00 EB 01 02 00 D7 02 ; ................
59EF: 02 00 F4 EB 1C 00 03 04 0D 02 AB 95 04 13 0B 11 ; ................
59FF: 0A 03 02 00 EC 04 02 00 D8 01 02 00 EA 02 02 00 ; ................
5A0F: DA EC 1C 00 03 04 0D 02 AB 95 04 13 0B 11 0A 03 ; ................
5A1F: 02 00 F4 04 02 00 EB 01 02 00 EA 02 02 00 DC ED ; ................
5A2F: 19 00 03 01 AB 04 13 0B 11 0A 03 02 00 F5 04 02 ; ................
5A3F: 00 DC 01 02 00 EC 02 02 00 EE EE 1C 00 03 04 0D ; ................
5A4F: 02 AB 9B 04 13 0B 11 0A 03 02 00 EF 04 02 00 DD ; ................
5A5F: 01 02 00 ED 02 02 00 DF EF 24 00 03 04 0D 02 AB ; .........$......
5A6F: 9B 04 1B 0B 19 0A 03 0A 0D 08 C8 30 80 17 9D 00 ; ...........0....
5A7F: 2F 01 04 02 00 EE 01 02 00 F5 02 02 00 E0 F0 28 ; /..............(
5A8F: 00 03 04 0D 02 9B AB 04 1F 0B 1D 0A 03 06 0D 04 ; ................
5A9F: 30 E4 2F 06 04 0A 0D 08 C8 30 B4 17 9D 00 2F 04 ; 0./......0..../.
5AAF: 01 02 00 F1 02 02 00 E2 F1 3F 00 03 23 0D 21 AB ; .........?..#.!.
5ABF: 04 1E 55 45 8E 91 16 8A CB B0 0E 8A 86 5F D9 B5 ; ..UE........._..
5ACF: 66 62 90 14 10 58 BE A0 08 71 FF B2 9F 15 7F B1 ; fb...X...q......
5ADF: 04 17 0B 15 0A 03 06 0D 04 30 E5 2F 06 04 02 00 ; .........0./....
5AEF: F6 01 02 00 F2 02 02 00 F0 F2 41 00 03 25 0D 23 ; ..........A..%.#
5AFF: AB 04 20 55 45 8E 91 16 8A 55 D1 FB C0 EB BF 33 ; .. UE....U.....3
5B0F: 7A E3 8B 0B 5C B5 D0 03 BC 33 98 47 B9 53 BE F4 ; z...\....3.G.S..
5B1F: 72 DB 63 04 17 0B 15 0A 03 06 0D 04 30 E6 2F 06 ; r.c.........0./.
5B2F: 04 02 00 F3 01 02 00 E8 02 02 00 F1 F3 35 00 03 ; .............5..
5B3F: 1D 0D 1B AB 95 04 17 5F BE 8C 17 CE 47 8E 14 2B ; ......._....G..+
5B4F: B9 04 68 CB 87 6B BF 5F BE 61 17 82 C6 2E 04 13 ; ..h..k._.a......
5B5F: 0B 11 0A 03 02 00 E9 04 02 00 F4 01 02 00 EA 02 ; ................
5B6F: 02 00 F1 F4 1C 00 03 04 0D 02 AB 95 04 13 0B 11 ; ................
5B7F: 0A 03 02 00 F3 04 02 00 EC 01 02 00 EA 02 02 00 ; ................
5B8F: F5 F5 19 00 03 01 AB 04 13 0B 11 0A 03 02 00 F6 ; ................
5B9F: 04 02 00 ED 01 02 00 F4 02 02 00 EF F6 45 00 03 ; .............E..
5BAF: 25 0D 23 AB 04 20 55 45 8E 91 16 8A CB B0 0E 8A ; %.#.. UE........
5BBF: 86 5F C8 B5 FF B2 82 17 55 5E 36 A1 16 71 D6 9C ; ._......U^6..q..
5BCF: DB 72 95 5F 9B C1 04 1B 0B 19 0A 03 02 00 F1 04 ; .r._............
5BDF: 02 00 F5 01 02 00 F3 02 0A 0D 08 C8 30 B7 17 9D ; ............0...
5BEF: 00 2F 02 F7 19 00 03 01 AB 04 13 0B 11 0A 03 02 ; ./..............
5BFF: 00 FA 04 02 00 F7 01 02 00 F7 02 02 00 F8 F8 19 ; ................
5C0F: 00 03 01 AB 04 13 0B 11 0A 03 02 00 F8 04 02 00 ; ................
5C1F: F9 01 02 00 F8 02 02 00 F8 F9 21 00 03 01 AB 04 ; ..........!.....
5C2F: 1B 0B 19 0A 03 0A 0E 08 0D 04 05 3E 00 86 00 F9 ; ...........>....
5C3F: 04 02 00 F8 01 02 00 FA 02 02 00 F9 FA 19 00 03 ; ................
5C4F: 01 AB 04 13 0B 11 0A 03 02 00 FA 04 02 00 F7 01 ; ................
5C5F: 02 00 FA 02 02 00 F9 4C 41 54 22 05 53 50 41 52 ; .......LAT".SPAR
5C6F: 45 23 04 42 4C 55 45 0D 06 4D 41 53 53 49 56 3F ; E#.BLUE..MASSIV?
5C7F: 04 42 41 4E 4B 40 06 53 41 4C 4F 4F 4E 41 06 53 ; .BANK@.SALOONA.S
5C8F: 48 45 52 49 46 42 06 4F 46 46 49 43 45 42 06 53 ; HERIFB.OFFICEB.S
5C9F: 4C 49 4D 27 53 43 05 53 4C 49 4D 53 43 05 42 4F ; LIM'SC.SLIMSC.BO
5CAF: 42 27 53 44 04 42 4F 42 53 44 06 44 4F 55 42 4C ; B'SD.BOBSD.DOUBL
5CBF: 45 45 05 48 4F 54 45 4C 47 06 53 57 49 4E 47 49 ; EE.HOTELG.SWINGI
5CCF: 46 04 54 53 4F 4D 6B 04 43 4F 4F 4C 72 05 43 4C ; F.TSOMk.COOLr.CL
5CDF: 45 41 52 74 05 42 52 4F 57 4E 73 00 02 54 4F 01 ; EARt.BROWNs..TO.
5CEF: 04 57 49 54 48 02 05 55 53 49 4E 47 02 02 41 54 ; .WITH..USING..AT
5CFF: 03 05 
```

