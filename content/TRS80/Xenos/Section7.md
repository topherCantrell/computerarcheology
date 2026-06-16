![Xenos](Xenos.png)

# Xenos SECTION7.DAT

>>> cpu Z80

>>> binary 5200:roms/section7.bin

```code
5200: 00 87 7C                           ; List_ID=0x00, length=0x077C

5203: 80 49 00                           ; ----- Room RM_7_??80??, Length: 0x0049, Data: 0x00
;
5206:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5208:       9D                           ;     FN_9D_??
;
5209:    04 43                           ;   ---- Section SECTION_04_COMMANDS length=0x0043
520B:       0B 41 0A                     ;     COM_0B_switch length=0x0041, function=COM_0A_is_input_phrase(phrase_num)
520E:          37                        ;       COM_0A_is_input_phrase("CLIMB * OUT *")
520F:          09                        ;       ELSE goto=0x5219
5210:             0D 07                  ;         COM_0D_while_pass length=0x0007
5212:                30 9D               ;           COM_30_set_current_room(room=RM_5_UFO_CRATER)
5214:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5217:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5219:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
521A:          09                        ;       ELSE goto=0x5224
521B:             0D 07                  ;         COM_0D_while_pass length=0x0007
521D:                30 9D               ;           COM_30_set_current_room(room=RM_5_UFO_CRATER)
521F:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5222:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5224:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
5225:          16                        ;       ELSE goto=0x523C
5226:             0E 14                  ;         COM_0E_while_fail length=0x0014
5228:                0D 11               ;           COM_0D_while_pass length=0x0011
522A:                   14               ;             COM_14_execute_and_reverse_status next command
522B:                   03 67 81         ;             COM_03_is_located(owner=OBJ_67_HOLE, obj=OBJ_81_GREEN_CUBE)
522E:                   04 0B            ;             COM_04_print_command length=0x000B
5230:                      06 9A 90 73 CA 6A EA 48 9D 61 2E ; 
;
;                          NOTHING HAPPENS.
;
523B:                9F                  ;           FN_9F_??
523C:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
523D:          10                        ;       ELSE goto=0x524E
523E:             0D 0E                  ;         COM_0D_while_pass length=0x000E
5240:                C0                  ;           FN_C0_??
5241:                0E 0B               ;           COM_0E_while_fail length=0x000B
5243:                   AE               ;             FN_AE_??
5244:                   14               ;             COM_14_execute_and_reverse_status next command
5245:                   0B 06 03         ;             COM_0B_switch length=0x0006, function=COM_03_is_located(room_num, obj_num)
5248:                      3F 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_3F_YELLOW_BUTTON, obj_num=OBJ_3E_??
524A:                      02            ;               ELSE goto=0x524D
524B:                         00 82      ;                 COM_00_move_and_look(room=RM_7_??82??)
524D:                   9E               ;             FN_9E_??

524E: 82 80 E0 00                        ; ----- Room RM_7_??82??, Length: 0x00E0, Data: 0x00
;
5252:    03 80 AF                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00AF
5255:       0D 80 AC                     ;     COM_0D_while_pass length=0x00AC
5258:          04 07                     ;       COM_04_print_command length=0x0007
525A:             AF B9 94 61 37 49 41   ; 
;
;                 SREENJARMA
;
5261:          0E 07                     ;       COM_0E_while_fail length=0x0007
5263:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
5264:             04 04                  ;         COM_04_print_command length=0x0004
5266:                87 8D B7 98         ; 
;
;                    LOUNGE
;
526A:          8B                        ;       FN_8B_PRINT_PERIOD
526B:          04 80 96                  ;       COM_04_print_command length=0x0096
526E:             51 18 43 C2 5B B1 09 9A D0 15 7B 14 54 8B 9B 6C ; 
527E:             65 B1 50 BD 2E 6F 23 49 01 B3 DB 95 83 48 34 60 ; 
528E:             1B 79 C8 93 91 7A E3 16 0F 56 5B B1 C5 65 4B 62 ; 
529E:             C7 DE 51 F4 96 96 DB 72 0E D0 04 8A A3 60 33 98 ; 
52AE:             C7 DE 82 17 2F 62 94 14 56 5E EF 74 44 5E 8E C6 ; 
52BE:             1D A0 11 EE 5B 98 66 B1 11 EE 5B 98 8F 4E B3 63 ; 
52CE:             8E 48 C0 16 5B 5E 46 61 8F A1 82 17 3B 63 2F 49 ; 
52DE:             94 14 D0 B0 A6 6C A9 15 1C B2 1E A0 46 48 B3 E0 ; 
52EE:             56 D1 16 71 DB 72 66 B1 BF 14 49 C0 91 96 96 96 ; 
52FE:             DB 72 09 B2 57 75      ; 
;
;                  YOU ARE NOW IN A LARGE RECTANGULAR ROOM. AN EERIE MOVING
;                 PICTURE FACES YOU. ON THE WALL BEHIND YOU THERE ARE THREE
;                 BUTTONS, ONE RED, ONE BLUE, AND ONE YELLOW. THEY ARE
;                 ARRANGED HORIZONTALLY, WITH THE RED BUTTON ON THE RIGHT.
;
;
5304:    04 2B                           ;   ---- Section SECTION_04_COMMANDS length=0x002B
5306:       0B 29 0A                     ;     COM_0B_switch length=0x0029, function=COM_0A_is_input_phrase(phrase_num)
5309:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
530A:          05                        ;       ELSE goto=0x5310
530B:             0E 03                  ;         COM_0E_while_fail length=0x0003
530D:                A0                  ;           FN_A0_??
530E:                A1                  ;           FN_A1_??
530F:                9F                  ;           FN_9F_??
5310:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
5311:          1F                        ;       ELSE goto=0x5331
5312:             0D 1D                  ;         COM_0D_while_pass length=0x001D
5314:                C0                  ;           FN_C0_??
5315:                0E 1A               ;           COM_0E_while_fail length=0x001A
5317:                   AE               ;             FN_AE_??
5318:                   14               ;             COM_14_execute_and_reverse_status next command
5319:                   0B 15 03         ;             COM_0B_switch length=0x0015, function=COM_03_is_located(room_num, obj_num)
531C:                      3F 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_3F_YELLOW_BUTTON, obj_num=OBJ_3E_??
531E:                      02            ;               ELSE goto=0x5321
531F:                         00 80      ;                 COM_00_move_and_look(room=RM_7_??80??)
5321:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
5323:                      02            ;               ELSE goto=0x5326
5324:                         00 83      ;                 COM_00_move_and_look(room=RM_7_??83??)
5326:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
5328:                      07            ;               ELSE goto=0x5330
5329:                         0D 05      ;                 COM_0D_while_pass length=0x0005
532B:                            9E      ;                   FN_9E_??
532C:                            30 84   ;                   COM_30_set_current_room(room=RM_8_??84??)
532E:                            2F 08   ;                   COM_2F_load_section_from_disk(section=8)
5330:                   9E               ;             FN_9E_??

5331: 83 2C 00                           ; ----- Room RM_7_??83??, Length: 0x002C, Data: 0x00
;
5334:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5336:       B0                           ;     FN_B0_??
;
5337:    04 26                           ;   ---- Section SECTION_04_COMMANDS length=0x0026
5339:       0B 24 0A                     ;     COM_0B_switch length=0x0024, function=COM_0A_is_input_phrase(phrase_num)
533C:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
533D:          05                        ;       ELSE goto=0x5343
533E:             0E 03                  ;         COM_0E_while_fail length=0x0003
5340:                9F                  ;           FN_9F_??
5341:                A0                  ;           FN_A0_??
5342:                A1                  ;           FN_A1_??
5343:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
5344:          1A                        ;       ELSE goto=0x535F
5345:             0D 18                  ;         COM_0D_while_pass length=0x0018
5347:                C0                  ;           FN_C0_??
5348:                0E 15               ;           COM_0E_while_fail length=0x0015
534A:                   AE               ;             FN_AE_??
534B:                   14               ;             COM_14_execute_and_reverse_status next command
534C:                   0B 10 03         ;             COM_0B_switch length=0x0010, function=COM_03_is_located(room_num, obj_num)
534F:                      3F 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_3F_YELLOW_BUTTON, obj_num=OBJ_3E_??
5351:                      02            ;               ELSE goto=0x5354
5352:                         00 93      ;                 COM_00_move_and_look(room=RM_7_??93??)
5354:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
5356:                      02            ;               ELSE goto=0x5359
5357:                         00 85      ;                 COM_00_move_and_look(room=RM_7_??85??)
5359:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
535B:                      02            ;               ELSE goto=0x535E
535C:                         00 82      ;                 COM_00_move_and_look(room=RM_7_??82??)
535E:                   9E               ;             FN_9E_??

535F: 85 80 D2 00                        ; ----- Room RM_7_??85??, Length: 0x00D2, Data: 0x00
;
5363:    03 80 AC                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00AC
5366:       0D 80 A9                     ;     COM_0D_while_pass length=0x00A9
5369:          04 07                     ;       COM_04_print_command length=0x0007
536B:             74 A7 7F 4E B6 5F 45   ; 
;
;                 PURBLEEBLE
;
5372:          0E 09                     ;       COM_0E_while_fail length=0x0009
5374:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
5375:             04 06                  ;         COM_04_print_command length=0x0006
5377:                BF B8 E3 61 AB 98   ; 
;
;                    SLEEPING 
;
537D:          8B                        ;       FN_8B_PRINT_PERIOD
537E:          04 80 91                  ;       COM_04_print_command length=0x0091
5381:             C7 DE 99 16 C8 CE 8E 7A 51 18 3D C6 40 61 D0 15 ; 
5391:             7B 14 8F 5A FB 8E 96 8C E7 14 05 4E FF 8B 82 17 ; 
53A1:             2F 62 D5 15 7B 14 CE 56 8E 7A 23 62 56 D1 03 71 ; 
53B1:             7E 15 65 49 43 16 03 58 0B 6C A6 9A C0 16 59 5E ; 
53C1:             46 48 44 F4 A3 60 33 98 C7 DE 51 18 46 C2 55 7B ; 
53D1:             4F A1 96 AF DB 72 0E D0 0A 8A 4B 49 C1 C0 BF 14 ; 
53E1:             49 C0 8B 9A 03 A0 96 7B 7B 14 66 B1 BF 14 49 C0 ; 
53F1:             83 96 33 98 44 45 67 8E BF 14 49 C0 F3 9B 3C 49 ; 
5401:             91 48 F3 5F 79 68 4E 90 5E 60 89 17 33 17 2E 6D ; 
5411:             2E                     ; 
;
;                 YOU NOW FIND YOURSELF IN A DIMLY LIT CUBICLE. THERE IS A
;                 CYLINDER WITH A GLASS LID AGAINST ONE WALL. BEHIND YOU YOU
;                 DISCOVER THE WALL HAS TWO BUTTONS ON IT, A RED BUTTON AND A
;                 BLUE BUTTON, ARRANGED FROM LEFT TO RIGHT.
;
;
5412:    04 20                           ;   ---- Section SECTION_04_COMMANDS length=0x0020
5414:       0B 1E 0A                     ;     COM_0B_switch length=0x001E, function=COM_0A_is_input_phrase(phrase_num)
5417:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
5418:          04                        ;       ELSE goto=0x541D
5419:             0E 02                  ;         COM_0E_while_fail length=0x0002
541B:                A0                  ;           FN_A0_??
541C:                A1                  ;           FN_A1_??
541D:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
541E:          15                        ;       ELSE goto=0x5434
541F:             0D 13                  ;         COM_0D_while_pass length=0x0013
5421:                C0                  ;           FN_C0_??
5422:                0E 10               ;           COM_0E_while_fail length=0x0010
5424:                   AE               ;             FN_AE_??
5425:                   14               ;             COM_14_execute_and_reverse_status next command
5426:                   0B 0B 03         ;             COM_0B_switch length=0x000B, function=COM_03_is_located(room_num, obj_num)
5429:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
542B:                      02            ;               ELSE goto=0x542E
542C:                         00 87      ;                 COM_00_move_and_look(room=RM_7_??87??)
542E:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
5430:                      02            ;               ELSE goto=0x5433
5431:                         00 83      ;                 COM_00_move_and_look(room=RM_7_??83??)
5433:                   9E               ;             FN_9E_??

5434: 87 26 00                           ; ----- Room RM_7_??87??, Length: 0x0026, Data: 0x00
;
5437:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5439:       9C                           ;     FN_9C_??
;
543A:    04 20                           ;   ---- Section SECTION_04_COMMANDS length=0x0020
543C:       0B 1E 0A                     ;     COM_0B_switch length=0x001E, function=COM_0A_is_input_phrase(phrase_num)
543F:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
5440:          04                        ;       ELSE goto=0x5445
5441:             0E 02                  ;         COM_0E_while_fail length=0x0002
5443:                A0                  ;           FN_A0_??
5444:                A1                  ;           FN_A1_??
5445:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
5446:          15                        ;       ELSE goto=0x545C
5447:             0D 13                  ;         COM_0D_while_pass length=0x0013
5449:                C0                  ;           FN_C0_??
544A:                0E 10               ;           COM_0E_while_fail length=0x0010
544C:                   AE               ;             FN_AE_??
544D:                   14               ;             COM_14_execute_and_reverse_status next command
544E:                   0B 0B 03         ;             COM_0B_switch length=0x000B, function=COM_03_is_located(room_num, obj_num)
5451:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
5453:                      02            ;               ELSE goto=0x5456
5454:                         00 89      ;                 COM_00_move_and_look(room=RM_7_??89??)
5456:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
5458:                      02            ;               ELSE goto=0x545B
5459:                         00 85      ;                 COM_00_move_and_look(room=RM_7_??85??)
545B:                   9E               ;             FN_9E_??

545C: 89 80 C9 00                        ; ----- Room RM_7_??89??, Length: 0x00C9, Data: 0x00
;
5460:    03 80 A3                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00A3
5463:       0D 80 A0                     ;     COM_0D_while_pass length=0x00A0
5466:          04 04                     ;       COM_04_print_command length=0x0004
5468:             8B 91 01 86            ; 
;
;                 MAIKGO
;
546C:          0E 08                     ;       COM_0E_while_fail length=0x0008
546E:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
546F:             04 05                  ;         COM_04_print_command length=0x0005
5471:                40 55 F9 BF 4C      ; 
;
;                    CONTROL
;
5476:          8B                        ;       FN_8B_PRINT_PERIOD
5477:          04 80 8C                  ;       COM_04_print_command length=0x008C
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
5506:    04 20                           ;   ---- Section SECTION_04_COMMANDS length=0x0020
5508:       0B 1E 0A                     ;     COM_0B_switch length=0x001E, function=COM_0A_is_input_phrase(phrase_num)
550B:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
550C:          04                        ;       ELSE goto=0x5511
550D:             0E 02                  ;         COM_0E_while_fail length=0x0002
550F:                A0                  ;           FN_A0_??
5510:                A1                  ;           FN_A1_??
5511:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
5512:          15                        ;       ELSE goto=0x5528
5513:             0D 13                  ;         COM_0D_while_pass length=0x0013
5515:                C0                  ;           FN_C0_??
5516:                0E 10               ;           COM_0E_while_fail length=0x0010
5518:                   AE               ;             FN_AE_??
5519:                   14               ;             COM_14_execute_and_reverse_status next command
551A:                   0B 0B 03         ;             COM_0B_switch length=0x000B, function=COM_03_is_located(room_num, obj_num)
551D:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
551F:                      02            ;               ELSE goto=0x5522
5520:                         00 8B      ;                 COM_00_move_and_look(room=RM_7_??8B??)
5522:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
5524:                      02            ;               ELSE goto=0x5527
5525:                         00 87      ;                 COM_00_move_and_look(room=RM_7_??87??)
5527:                   9E               ;             FN_9E_??

5528: 8B 26 00                           ; ----- Room RM_7_??8B??, Length: 0x0026, Data: 0x00
;
552B:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
552D:       9C                           ;     FN_9C_??
;
552E:    04 20                           ;   ---- Section SECTION_04_COMMANDS length=0x0020
5530:       0B 1E 0A                     ;     COM_0B_switch length=0x001E, function=COM_0A_is_input_phrase(phrase_num)
5533:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
5534:          04                        ;       ELSE goto=0x5539
5535:             0E 02                  ;         COM_0E_while_fail length=0x0002
5537:                A0                  ;           FN_A0_??
5538:                A1                  ;           FN_A1_??
5539:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
553A:          15                        ;       ELSE goto=0x5550
553B:             0D 13                  ;         COM_0D_while_pass length=0x0013
553D:                C0                  ;           FN_C0_??
553E:                0E 10               ;           COM_0E_while_fail length=0x0010
5540:                   AE               ;             FN_AE_??
5541:                   14               ;             COM_14_execute_and_reverse_status next command
5542:                   0B 0B 03         ;             COM_0B_switch length=0x000B, function=COM_03_is_located(room_num, obj_num)
5545:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
5547:                      02            ;               ELSE goto=0x554A
5548:                         00 8D      ;                 COM_00_move_and_look(room=RM_7_??8D??)
554A:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
554C:                      02            ;               ELSE goto=0x554F
554D:                         00 89      ;                 COM_00_move_and_look(room=RM_7_??89??)
554F:                   9E               ;             FN_9E_??

5550: 8D 80 DE 00                        ; ----- Room RM_7_??8D??, Length: 0x00DE, Data: 0x00
;
5554:    03 80 C0                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00C0
5557:       0D 80 BD                     ;     COM_0D_while_pass length=0x00BD
555A:          04 05                     ;       COM_04_print_command length=0x0005
555C:             CA 97 66 8E 4A         ; 
;
;                 NAHLUDJ
;
5561:          0E 08                     ;       COM_0E_while_fail length=0x0008
5563:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
5564:             04 05                  ;         COM_04_print_command length=0x0005
5566:                84 8C D4 B0 59      ; 
;
;                    LIBRARY
;
556B:          8B                        ;       FN_8B_PRINT_PERIOD
556C:          04 80 A8                  ;       COM_04_print_command length=0x00A8
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
5617:    04 18                           ;   ---- Section SECTION_04_COMMANDS length=0x0018
5619:       0B 16 0A                     ;     COM_0B_switch length=0x0016, function=COM_0A_is_input_phrase(phrase_num)
561C:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
561D:          01                        ;       ELSE goto=0x561F
561E:             A1                     ;         FN_A1_??
561F:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
5620:          10                        ;       ELSE goto=0x5631
5621:             0D 0E                  ;         COM_0D_while_pass length=0x000E
5623:                C0                  ;           FN_C0_??
5624:                0E 0B               ;           COM_0E_while_fail length=0x000B
5626:                   AE               ;             FN_AE_??
5627:                   14               ;             COM_14_execute_and_reverse_status next command
5628:                   0B 06 03         ;             COM_0B_switch length=0x0006, function=COM_03_is_located(room_num, obj_num)
562B:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
562D:                      02            ;               ELSE goto=0x5630
562E:                         00 8B      ;                 COM_00_move_and_look(room=RM_7_??8B??)
5630:                   9E               ;             FN_9E_??

5631: 93 2C 00                           ; ----- Room RM_7_??93??, Length: 0x002C, Data: 0x00
;
5634:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5636:       B0                           ;     FN_B0_??
;
5637:    04 26                           ;   ---- Section SECTION_04_COMMANDS length=0x0026
5639:       0B 24 0A                     ;     COM_0B_switch length=0x0024, function=COM_0A_is_input_phrase(phrase_num)
563C:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
563D:          05                        ;       ELSE goto=0x5643
563E:             0E 03                  ;         COM_0E_while_fail length=0x0003
5640:                A0                  ;           FN_A0_??
5641:                A1                  ;           FN_A1_??
5642:                9F                  ;           FN_9F_??
5643:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
5644:          1A                        ;       ELSE goto=0x565F
5645:             0D 18                  ;         COM_0D_while_pass length=0x0018
5647:                C0                  ;           FN_C0_??
5648:                0E 15               ;           COM_0E_while_fail length=0x0015
564A:                   AE               ;             FN_AE_??
564B:                   14               ;             COM_14_execute_and_reverse_status next command
564C:                   0B 10 03         ;             COM_0B_switch length=0x0010, function=COM_03_is_located(room_num, obj_num)
564F:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
5651:                      02            ;               ELSE goto=0x5654
5652:                         00 95      ;                 COM_00_move_and_look(room=RM_7_??95??)
5654:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
5656:                      02            ;               ELSE goto=0x5659
5657:                         00 94      ;                 COM_00_move_and_look(room=RM_7_??94??)
5659:                      3F 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_3F_YELLOW_BUTTON, obj_num=OBJ_3E_??
565B:                      02            ;               ELSE goto=0x565E
565C:                         00 83      ;                 COM_00_move_and_look(room=RM_7_??83??)
565E:                   9E               ;             FN_9E_??

565F: 94 80 A9 00                        ; ----- Room RM_7_??94??, Length: 0x00A9, Data: 0x00
;
5663:    03 80 8B                        ;   ---- Section SECTION_03_DESCRIPTION length=0x008B
5666:       0D 80 88                     ;     COM_0D_while_pass length=0x0088
5669:          04 05                     ;       COM_04_print_command length=0x0005
566B:             7A 63 F0 B3 4A         ; 
;
;                 EZPRUNJ
;
5670:          0E 07                     ;       COM_0E_while_fail length=0x0007
5672:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
5673:             04 04                  ;         COM_04_print_command length=0x0004
5675:                FF 4E 8B 4F         ; 
;
;                    BOMBS 
;
5679:          8B                        ;       FN_8B_PRINT_PERIOD
567A:          04 75                     ;       COM_04_print_command length=0x0075
567C:             C7 DE 94 14 4B 5E 83 96 49 16 CE 98 8B 16 79 B3 ; 
568C:             D4 CE 3F A0 82 17 73 49 4B 7B EE 68 11 8A 85 64 ; 
569C:             43 DE 3F 98 8B B3 5B BE 03 BC 5B B1 83 7A 55 45 ; 
56AC:             33 62 4B 62 C3 9E FB B9 A5 54 82 17 73 49 90 8C ; 
56BC:             56 5E DB 72 80 8D B4 6C F3 17 0D 8D 51 F4 96 96 ; 
56CC:             DB 72 29 B8 B3 B3 0E D0 04 8A A3 60 33 98 C7 DE ; 
56DC:             1B EE 1B A1 10 67 03 58 5B 17 BE 98 54 5E F3 5F ; 
56EC:             F6 4F 80 BF 2E         ; 
;
;                 YOU ARE IN A LONG, NARROW ROOM THAT IS FULL OF CYLINDERS
;                 THAT ARE IN A SERIES OF STACKS THAT LINE THE LONGER WALLS.
;                 ON THE SHORT WALL BEHIND YOU, YOU FIND A SINGLE RED BUTTON.
;
;
56F1:    04 18                           ;   ---- Section SECTION_04_COMMANDS length=0x0018
56F3:       0B 16 0A                     ;     COM_0B_switch length=0x0016, function=COM_0A_is_input_phrase(phrase_num)
56F6:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
56F7:          01                        ;       ELSE goto=0x56F9
56F8:             A0                     ;         FN_A0_??
56F9:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
56FA:          10                        ;       ELSE goto=0x570B
56FB:             0D 0E                  ;         COM_0D_while_pass length=0x000E
56FD:                C0                  ;           FN_C0_??
56FE:                0E 0B               ;           COM_0E_while_fail length=0x000B
5700:                   AE               ;             FN_AE_??
5701:                   14               ;             COM_14_execute_and_reverse_status next command
5702:                   0B 06 03         ;             COM_0B_switch length=0x0006, function=COM_03_is_located(room_num, obj_num)
5705:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
5707:                      02            ;               ELSE goto=0x570A
5708:                         00 93      ;                 COM_00_move_and_look(room=RM_7_??93??)
570A:                   9E               ;             FN_9E_??

570B: 95 80 D9 00                        ; ----- Room RM_7_??95??, Length: 0x00D9, Data: 0x00
;
570F:    03 80 B3                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00B3
5712:       0D 80 B0                     ;     COM_0D_while_pass length=0x00B0
5715:          04 06                     ;       COM_04_print_command length=0x0006
5717:             19 B9 9C A1 23 C6      ; 
;
;                 SNOOXBUR 
;
571D:          0E 05                     ;       COM_0E_while_fail length=0x0005
571F:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
5720:             04 02                  ;         COM_04_print_command length=0x0002
5722:                15 6C               ; 
;
;                    GAS
;
5724:          8B                        ;       FN_8B_PRINT_PERIOD
5725:          04 80 9D                  ;       COM_04_print_command length=0x009D
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
57C5:    04 20                           ;   ---- Section SECTION_04_COMMANDS length=0x0020
57C7:       0B 1E 0A                     ;     COM_0B_switch length=0x001E, function=COM_0A_is_input_phrase(phrase_num)
57CA:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
57CB:          04                        ;       ELSE goto=0x57D0
57CC:             0E 02                  ;         COM_0E_while_fail length=0x0002
57CE:                A0                  ;           FN_A0_??
57CF:                A1                  ;           FN_A1_??
57D0:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
57D1:          15                        ;       ELSE goto=0x57E7
57D2:             0D 13                  ;         COM_0D_while_pass length=0x0013
57D4:                C0                  ;           FN_C0_??
57D5:                0E 10               ;           COM_0E_while_fail length=0x0010
57D7:                   AE               ;             FN_AE_??
57D8:                   14               ;             COM_14_execute_and_reverse_status next command
57D9:                   0B 0B 03         ;             COM_0B_switch length=0x000B, function=COM_03_is_located(room_num, obj_num)
57DC:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
57DE:                      02            ;               ELSE goto=0x57E1
57DF:                         00 96      ;                 COM_00_move_and_look(room=RM_7_??96??)
57E1:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
57E3:                      02            ;               ELSE goto=0x57E6
57E4:                         00 93      ;                 COM_00_move_and_look(room=RM_7_??93??)
57E6:                   9E               ;             FN_9E_??

57E7: 96 26 00                           ; ----- Room RM_7_??96??, Length: 0x0026, Data: 0x00
;
57EA:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
57EC:       9C                           ;     FN_9C_??
;
57ED:    04 20                           ;   ---- Section SECTION_04_COMMANDS length=0x0020
57EF:       0B 1E 0A                     ;     COM_0B_switch length=0x001E, function=COM_0A_is_input_phrase(phrase_num)
57F2:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
57F3:          04                        ;       ELSE goto=0x57F8
57F4:             0E 02                  ;         COM_0E_while_fail length=0x0002
57F6:                A0                  ;           FN_A0_??
57F7:                A1                  ;           FN_A1_??
57F8:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
57F9:          15                        ;       ELSE goto=0x580F
57FA:             0D 13                  ;         COM_0D_while_pass length=0x0013
57FC:                C0                  ;           FN_C0_??
57FD:                0E 10               ;           COM_0E_while_fail length=0x0010
57FF:                   AE               ;             FN_AE_??
5800:                   14               ;             COM_14_execute_and_reverse_status next command
5801:                   0B 0B 03         ;             COM_0B_switch length=0x000B, function=COM_03_is_located(room_num, obj_num)
5804:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
5806:                      02            ;               ELSE goto=0x5809
5807:                         00 97      ;                 COM_00_move_and_look(room=RM_7_??97??)
5809:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
580B:                      02            ;               ELSE goto=0x580E
580C:                         00 95      ;                 COM_00_move_and_look(room=RM_7_??95??)
580E:                   9E               ;             FN_9E_??

580F: 97 80 AD 00                        ; ----- Room RM_7_??97??, Length: 0x00AD, Data: 0x00
;
5813:    03 80 87                        ;   ---- Section SECTION_03_DESCRIPTION length=0x0087
5816:       0D 80 84                     ;     COM_0D_while_pass length=0x0084
5819:          04 06                     ;       COM_04_print_command length=0x0006
581B:             E6 5F 36 9E 5F 49      ; 
;
;                 ECTOBLASM
;
5821:          0E 05                     ;       COM_0E_while_fail length=0x0005
5823:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
5824:             04 02                  ;         COM_04_print_command length=0x0002
5826:                11 4E               ; 
;
;                    BIO
;
5828:          8B                        ;       FN_8B_PRINT_PERIOD
5829:          04 72                     ;       COM_04_print_command length=0x0072
582B:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 39 17 FE 9F ; 
583B:             82 17 2F 62 94 14 55 5E CF 62 CE B0 B6 14 DD 46 ; 
584B:             7E 15 2F 9E CB B5 95 96 45 BD CB 87 73 47 9D 7A ; 
585B:             16 BC DB 72 0E D0 2F 8E C0 16 82 17 59 5E 46 48 ; 
586B:             AF 14 90 73 1B 58 3E A1 82 17 2F 62 D5 15 7B 14 ; 
587B:             66 B1 90 14 03 58 B6 14 1B C4 F6 4F 80 BF 94 14 ; 
588B:             D0 B0 A6 6C 5C 15 DB 9F E8 8B 16 BC D4 9C 7A 79 ; 
589B:             9B C1                  ; 
;
;                 YOU ARE IN A SMALL ROOM, THERE ARE SEVERAL BLACK GLOBES IN
;                 STACKS AGAINST THE WALLS. ON THE WALL BEHIND YOU, THERE IS
;                 A RED AND A BLUE BUTTON ARRANGED FROM LEFT TO RIGHT.
;
;
589D:    04 20                           ;   ---- Section SECTION_04_COMMANDS length=0x0020
589F:       0B 1E 0A                     ;     COM_0B_switch length=0x001E, function=COM_0A_is_input_phrase(phrase_num)
58A2:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
58A3:          04                        ;       ELSE goto=0x58A8
58A4:             0E 02                  ;         COM_0E_while_fail length=0x0002
58A6:                A0                  ;           FN_A0_??
58A7:                A1                  ;           FN_A1_??
58A8:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
58A9:          15                        ;       ELSE goto=0x58BF
58AA:             0D 13                  ;         COM_0D_while_pass length=0x0013
58AC:                C0                  ;           FN_C0_??
58AD:                0E 10               ;           COM_0E_while_fail length=0x0010
58AF:                   AE               ;             FN_AE_??
58B0:                   14               ;             COM_14_execute_and_reverse_status next command
58B1:                   0B 0B 03         ;             COM_0B_switch length=0x000B, function=COM_03_is_located(room_num, obj_num)
58B4:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
58B6:                      02            ;               ELSE goto=0x58B9
58B7:                         00 98      ;                 COM_00_move_and_look(room=RM_7_??98??)
58B9:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
58BB:                      02            ;               ELSE goto=0x58BE
58BC:                         00 96      ;                 COM_00_move_and_look(room=RM_7_??96??)
58BE:                   9E               ;             FN_9E_??

58BF: 98 26 00                           ; ----- Room RM_7_??98??, Length: 0x0026, Data: 0x00
;
58C2:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
58C4:       9C                           ;     FN_9C_??
;
58C5:    04 20                           ;   ---- Section SECTION_04_COMMANDS length=0x0020
58C7:       0B 1E 0A                     ;     COM_0B_switch length=0x001E, function=COM_0A_is_input_phrase(phrase_num)
58CA:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
58CB:          04                        ;       ELSE goto=0x58D0
58CC:             0E 02                  ;         COM_0E_while_fail length=0x0002
58CE:                A0                  ;           FN_A0_??
58CF:                A1                  ;           FN_A1_??
58D0:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
58D1:          15                        ;       ELSE goto=0x58E7
58D2:             0D 13                  ;         COM_0D_while_pass length=0x0013
58D4:                C0                  ;           FN_C0_??
58D5:                0E 10               ;           COM_0E_while_fail length=0x0010
58D7:                   AE               ;             FN_AE_??
58D8:                   14               ;             COM_14_execute_and_reverse_status next command
58D9:                   0B 0B 03         ;             COM_0B_switch length=0x000B, function=COM_03_is_located(room_num, obj_num)
58DC:                      40 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_40_RED_BUTTON, obj_num=OBJ_3E_??
58DE:                      02            ;               ELSE goto=0x58E1
58DF:                         00 99      ;                 COM_00_move_and_look(room=RM_7_??99??)
58E1:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
58E3:                      02            ;               ELSE goto=0x58E6
58E4:                         00 97      ;                 COM_00_move_and_look(room=RM_7_??97??)
58E6:                   9E               ;             FN_9E_??

58E7: 99 80 95 00                        ; ----- Room RM_7_??99??, Length: 0x0095, Data: 0x00
;
58EB:    03 78                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0078
58ED:       0D 76                        ;     COM_0D_while_pass length=0x0076
58EF:          04 06                     ;       COM_04_print_command length=0x0006
58F1:             A7 85 F3 A6 23 99      ; 
;
;                 KEEPRINJ 
;
58F7:          0E 08                     ;       COM_0E_while_fail length=0x0008
58F9:             C3                     ;         FN_C3_PLAYER_LACKS_WISDOM
58FA:             04 05                  ;         COM_04_print_command length=0x0005
58FC:                09 BA C9 B0 45      ; 
;
;                    STORAGE
;
5901:          8B                        ;       FN_8B_PRINT_PERIOD
5902:          04 61                     ;       COM_04_print_command length=0x0061
5904:             C7 DE 94 14 4B 5E 83 96 5F 17 46 48 39 17 FE 9F ; 
5914:             82 17 2F 62 94 14 55 5E CF 62 CE B0 EB 14 90 8C ; 
5924:             F4 59 D5 B5 84 BF F3 5F 83 7A 55 45 45 BD D1 83 ; 
5934:             A9 A6 56 B8 5B 5E 3F A1 89 17 82 17 55 5E FF 78 ; 
5944:             1B EE 1B A1 10 53 57 17 43 5E 61 17 96 8C 43 49 ; 
5954:             B6 14 1B C4 F6 4F 80 BF C0 16 82 17 59 5E 46 48 ; 
5964:             2E                     ; 
;
;                 YOU ARE IN A SMALL ROOM, THERE ARE SEVERAL CYLINDERS STORED
;                 IN A STACK OPPOSITE YOU. TO THE SIDE, YOU CAN SEE A
;                 SOLITARY BLUE BUTTON ON THE WALL.
;
;
5965:    04 18                           ;   ---- Section SECTION_04_COMMANDS length=0x0018
5967:       0B 16 0A                     ;     COM_0B_switch length=0x0016, function=COM_0A_is_input_phrase(phrase_num)
596A:          12                        ;       COM_0A_is_input_phrase("PULL u....... * *")
596B:          01                        ;       ELSE goto=0x596D
596C:             A1                     ;         FN_A1_??
596D:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
596E:          10                        ;       ELSE goto=0x597F
596F:             0D 0E                  ;         COM_0D_while_pass length=0x000E
5971:                C0                  ;           FN_C0_??
5972:                0E 0B               ;           COM_0E_while_fail length=0x000B
5974:                   AE               ;             FN_AE_??
5975:                   14               ;             COM_14_execute_and_reverse_status next command
5976:                   0B 06 03         ;             COM_0B_switch length=0x0006, function=COM_03_is_located(room_num, obj_num)
5979:                      41 3E         ;               COM_03_is_located(room_num, obj_num) room_num=OBJ_41_BLUE_BUTTON, obj_num=OBJ_3E_??
597B:                      02            ;               ELSE goto=0x597E
597C:                         00 98      ;                 COM_00_move_and_look(room=RM_7_??98??)
597E:                   9E               ;             FN_9E_??
```

# Unitialized data

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

