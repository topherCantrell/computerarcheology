![Xenos](Xenos.png)

# Xenos SECTION9.DAT

>>> cpu Z80

>>> binary 5200:roms/section9.bin

```code
5200: 00 89 BD                           ; List_ID=0x00, length=0x09BD (to 0x5BC0)

; --------------------------------------------------------------------------------------------------------------------
;
5203: 81 80 F3 00                        ; ----- Room 0x81 RM_9_SURFACE, Length: 0x00F3, Data: 0x00
;
5207:    03 80 DD                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00DD (to 0x52E7)
520A:       04 80 DA                     ;     COM_04_print_message length=0x00DA (to 0x52E7)
520D:          34 BA C5 65 DB 63 C7 DE 53 15 33 98 C7 DE 97 B3
521D:          03 8C FB B9 43 98 AB 98 83 7A 4E 45 31 49 45 5E
522D:          2D 7B DB 8B C3 9E 79 4F 03 D2 3B B9 03 8A 07 4F
523D:          16 BC EF 74 4A 5E 8E C5 66 B1 4F 15 73 62 83 7A
524D:          83 5A 36 92 47 62 C7 16 1B C0 DB 59 C3 9E 63 BE
525D:          C5 B5 2D 7B DB 8B 5F BE 84 15 30 A1 0B 58 C4 B5
526D:          38 C6 04 BC 45 8B 5B 89 50 72 50 6D CB 6A 96 96
527D:          DB 72 AB B8 D5 15 7B 14 43 6D B3 9A 66 B1 67 17
528D:          99 96 85 73 0B 71 D8 B5 43 62 BE 16 03 58 33 98
529D:          41 55 9B 8F 73 7B EA 48 94 5F D6 B5 C4 9C 4B 5E
52AD:          8B 96 65 BC 53 15 CE 97 66 17 77 47 C4 B5 59 60
52BD:          5B B1 3B 6E AB 98 08 9A DB 4A 4E 45 31 49 52 5E
52CD:          81 8D C4 97 3F 16 0D 47 61 17 3B B4 04 BC 49 61
52DD:          D6 CE DB 72 34 BA C5 65 DB 63
;
;              SURFACE. YOU FIND YOURSELF STANDING IN A LARGE CIRCLE OF
;              BROWN SOIL ABOUT THREE HUNDRED FEET IN DIAMETER. OUTSIDE OF
;              THIS CIRCLE THE GROUND IS BURNT BLACK. HANGING IN THE SKY
;              IS A GIANT RED SUN WHICH IS VERY OLD AND COOL. IT APPEARS
;              TO BE IN IT'S FINAL STAGES BEFORE GOING NOVA. A LARGE
;              PLOONAB LEADS SORWIT BELOW THE SURFACE.
;
;
52E7:    04 10                           ;   ---- Section SECTION_04_COMMANDS length=0x0010 (to 0x52F9)
52E9:       0B 0E 0A                     ;     COM_0B_switch length=0x000E (to 0x52FA), function=COM_0A_is_input_phrase(phrase_num)
52EC:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
52EE:             00 83                  ;         COM_00_move_and_look(room=RM_9_GRAND_CENTRAL)
;                                        ;       end case
52F0:          03 01                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0001
52F2:             BE                     ;         FN_BE_PRINT_FORCE_FIELD
;                                        ;       end case
52F3:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
52F5:             BE                     ;         FN_BE_PRINT_FORCE_FIELD
;                                        ;       end case
52F6:          04 01                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0001
52F8:             BE                     ;         FN_BE_PRINT_FORCE_FIELD
;                                        ;       end case
;                                        ;     end decode_switch at 0x52E9

; --------------------------------------------------------------------------------------------------------------------
;
52F9: 82 80 9A 00                        ; ----- Room 0x82 RM_9_CARNEGIE, Length: 0x009A, Data: 0x00
;
52FD:    03 80 8D                        ;   ---- Section SECTION_03_DESCRIPTION length=0x008D (to 0x538D)
5300:       04 80 8A                     ;     COM_04_print_message length=0x008A (to 0x538D)
5303:          14 53 69 98 1B 79 4E 72 9B 8F C7 DE 94 14 4B 5E
5313:          83 96 AF 15 9B 6C 01 B3 56 90 56 72 D5 15 53 15
5323:          FF 8C 19 58 82 7B 7B 14 0C BA 91 48 43 5E 33 98
5333:          3F 55 6E A7 58 B8 4F 5E 5B C6 5B 57 04 68 7B 14
5343:          73 4F 43 60 BF 93 9E 61 51 18 48 C2 2E 60 82 17
5353:          57 5E B7 B1 89 17 82 17 EF B3 51 18 23 C6 6F 68
5363:          3B 61 73 A8 F6 4F 82 17 73 49 4B 7B 72 7A E5 A0
5373:          B6 78 DB 63 5F BE C0 16 FB 8E 16 E4 4B 5E D6 B5
5383:          D6 9C DB 72 9F 61 BE B1 DB 63
;
;              CARNEGIE HALL. YOU ARE IN A HUGE ROOM THAT IS FILLED WITH A
;              STRANGE AND COMPULSIVE MUSIC. FOR A BRIEF MOMENT YOU FEEL
;              THE URGE TO THRUM YOUR FREELAP, BUT THAT IS IMPOSSIBLE. THE
;              ONLY ZITE IS TO THE ENURGLE.
;
;
538D:    04 07                           ;   ---- Section SECTION_04_COMMANDS length=0x0007 (to 0x5396)
538F:       0B 05 0A                     ;     COM_0B_switch length=0x0005 (to 0x5397), function=COM_0A_is_input_phrase(phrase_num)
5392:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5394:             00 83                  ;         COM_00_move_and_look(room=RM_9_GRAND_CENTRAL)
;                                        ;       end case
;                                        ;     end decode_switch at 0x538F

; --------------------------------------------------------------------------------------------------------------------
;
5396: 83 81 0E 00                        ; ----- Room 0x83 RM_9_GRAND_CENTRAL, Length: 0x010E, Data: 0x00
;
539A:    03 80 EF                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00EF (to 0x548C)
539D:       04 80 EC                     ;     COM_04_print_message length=0x00EC (to 0x548C)
53A0:          AB 6E 33 98 B0 53 EB BF 15 8A 56 BD C0 7A 5B F4
53B0:          1B A1 2F 49 D0 15 7B 14 69 75 51 5E F0 A4 D3 14
53C0:          74 CA 99 96 82 7B 57 17 74 CA 33 48 69 BE 53 C6
53D0:          33 98 43 48 9D 61 56 F4 FB 72 94 14 55 5E 34 56
53E0:          8B B4 AB 98 6C BE 29 A1 05 71 CF 49 D6 B5 D6 9C
53F0:          DB 72 9F 61 BE B1 43 5E 33 98 56 D1 44 B9 55 F4
5400:          E7 9F 89 74 8E 14 16 8A DB 72 EB BF 93 66 D5 51
5410:          2F 60 CE B5 E6 A0 D0 15 67 17 13 54 4E 45 31 49
5420:          54 5E 3F A0 4B F4 0B BC C3 B5 CB B5 8B 64 19 BC
5430:          2F 62 63 16 DB 59 04 68 63 16 7B 9B 8F BE 4B 62
5440:          C4 93 56 5E D7 9C BF B7 DB F9 5C 45 7F 7B 3F 16
5450:          0D 47 FB 17 21 C0 1B B5 83 48 60 62 33 61 E3 8B
5460:          0B 5C 9F 61 BE B1 DB 63 5F BE 3B 16 B7 B1 E6 16
5470:          40 A0 A3 46 40 55 90 BE 35 C4 61 17 3B B4 04 BC
5480:          49 61 D6 CE DB 72 34 BA C5 65 DB 63
;
;              GRAND CENTRAL STATION. YOU ARE IN A HUGE OPEN CAVERN WITH
;              SEVERAL THOUSAND ALIENS. THEY ARE SCURRYING THROUGH CAVES
;              TO THE ENURGLE AND WITSOR. SOMEHOW ALL THE TRAFFIC SEEMS
;              LOST IN SUCH A LARGE ROOM. IT IS AS IF IT WERE MADE FOR
;              MANY TIMES MORE TO USE... A ZITE LEADS WITSOR. AN ESNEL
;              LEADS ENURGLE. THE LARGE PLOONAB CONTINUES SORWIT BELOW THE
;              SURFACE.
;
;
548C:    04 19                           ;   ---- Section SECTION_04_COMMANDS length=0x0019 (to 0x54A7)
548E:       0B 17 0A                     ;     COM_0B_switch length=0x0017 (to 0x54A8), function=COM_0A_is_input_phrase(phrase_num)
5491:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5493:             00 81                  ;         COM_00_move_and_look(room=RM_9_SURFACE)
;                                        ;       end case
5495:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5497:             00 85                  ;         COM_00_move_and_look(room=RM_9_MUSEUM)
;                                        ;       end case
5499:          03 08                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0008
549B:             0E 06                  ;         COM_0E_group_OR length=0x0006 (to 0x54A3)
549D:                14                  ;           COM_14_reverse_status next command
549E:                1C 93               ;           COM_1C_set_var_object(obj=OBJ_93_DOOR_ESNEL)
54A0:                C7                  ;           FN_C7_IS_OBJECT_RIBULN
54A1:                00 84               ;           COM_00_move_and_look(room=RM_9_DISCO)
;                                        ;         end group_OR at 0x549B
;                                        ;       end case
54A3:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
54A5:             00 82                  ;         COM_00_move_and_look(room=RM_9_CARNEGIE)
;                                        ;       end case
;                                        ;     end decode_switch at 0x548E

; --------------------------------------------------------------------------------------------------------------------
;
54A7: 84 80 B6 00                        ; ----- Room 0x84 RM_9_DISCO, Length: 0x00B6, Data: 0x00
;
54AB:    03 80 A9                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00A9 (to 0x5557)
54AE:       04 80 A6                     ;     COM_04_print_message length=0x00A6 (to 0x5557)
54B1:          95 5A 4F 55 51 18 43 C2 5B B1 83 7A 4E 45 31 49
54C1:          54 5E 3F A0 82 17 73 49 4B 7B EE 68 11 8A 83 64
54D1:          87 8C 8B 9A F4 A4 04 68 D0 92 D6 6A DB 72 B4 53
54E1:          71 61 03 99 06 8A 8D 48 51 5E 88 64 B6 A0 42 A0
54F1:          43 F4 F3 8C 6C BE 1B 60 BA B7 4B 62 2F 49 2F 17
5501:          EF A6 B0 B7 E6 BD D0 15 23 15 13 54 F3 BF 5B A2
5511:          5F BE 5B B1 4B 7B 01 B3 48 90 A3 A0 F0 BD D1 B5
5521:          96 64 87 74 10 B7 2E 5C BF 14 11 BC 93 99 7B 14
5531:          79 66 AF 15 4C 98 F3 5F 2F 49 EC 16 57 62 D7 9A
5541:          82 17 51 5E 93 99 73 18 DB BD 4B 7B 6B BF 5F BE
5551:          FB 17 21 C0 1B B5        
;
;              DISCO. YOU ARE IN A LARGE ROOM THAT IS FULL OF ALIENS
;              PERFORMING THE CEREMONIAL DANCE OF FORLOOP. ALL THREE SEXES
;              ARE REPRESENTED IN EACH TRIO. THERE IS ROOM FOR TENS OF
;              THOUSANDS, BUT ONLY A FEW HUNDRED ARE PRESENT. THE ONLY
;              ZITE IS TO THE WITSOR.
;
;
5557:    04 07                           ;   ---- Section SECTION_04_COMMANDS length=0x0007 (to 0x5560)
5559:       0B 05 0A                     ;     COM_0B_switch length=0x0005 (to 0x5561), function=COM_0A_is_input_phrase(phrase_num)
555C:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
555E:             00 83                  ;         COM_00_move_and_look(room=RM_9_GRAND_CENTRAL)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5559

; --------------------------------------------------------------------------------------------------------------------
;
5560: 85 80 B3 00                        ; ----- Room 0x85 RM_9_MUSEUM, Length: 0x00B3, Data: 0x00
;
5564:    03 80 A2                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00A2 (to 0x5609)
5567:       04 80 9F                     ;     COM_04_print_message length=0x009F (to 0x5609)
556A:          B5 94 AF 62 5B F4 1B A1 2F 49 D0 15 7B 14 D5 C9
557A:          11 BC F0 A4 D3 14 74 CA 88 96 46 7A F3 5F 56 D1
558A:          07 71 86 D8 CB 78 85 91 90 73 4B 62 8E 48 FF 14
559A:          05 CB 6F 62 82 17 3B 63 2F 49 8E 14 06 8A 62 7B
55AA:          5B 8B F3 5F 5F A0 93 99 04 EE 73 C6 00 9A 55 5E
55BA:          2F 60 89 17 AF 14 FF 14 64 B7 AF 78 03 58 D6 B5
55CA:          C8 9C 8D C5 91 BE 91 96 92 AF 3A C6 D7 A0 56 F4
55DA:          DB 72 54 8B 9B 6C 09 A6 0B A0 85 4B 1E A0 9F 7A
55EA:          4B 62 44 B9 56 D1 50 F4 94 5F 82 17 47 5E F4 9A
55FA:          BF 6D 56 15 5F 49 D5 15 7B 14 62 B9 C2 A0 2E
;
;              MUSEUM. YOU ARE IN A VAST OPEN CAVERN FILLED WITH EXOTIC
;              MACHINES AND DEVICES. THEY ARE ALL DISPLAYED OPENLY, BUT
;              NONE SEEM TO BE DESCRIBED AS TO FUNCTION OR PURPOSE. THE
;              LARGE PLOONAB CONTINUES SORWIT. NEAR THE ENURGLE FLASM IS A
;              SPHORX.
;
;
5609:    04 0B                           ;   ---- Section SECTION_04_COMMANDS length=0x000B (to 0x5616)
560B:       0B 09 0A                     ;     COM_0B_switch length=0x0009 (to 0x5617), function=COM_0A_is_input_phrase(phrase_num)
560E:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5610:             00 83                  ;         COM_00_move_and_look(room=RM_9_GRAND_CENTRAL)
;                                        ;       end case
5612:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5614:             00 86                  ;         COM_00_move_and_look(room=RM_9_BIOLOGICAL)
;                                        ;       end case
;                                        ;     end decode_switch at 0x560B

; --------------------------------------------------------------------------------------------------------------------
;
5616: 86 80 E0 00                        ; ----- Room 0x86 RM_9_BIOLOGICAL, Length: 0x00E0, Data: 0x00
;
561A:    03 80 CF                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00CF (to 0x56EC)
561D:       04 80 CC                     ;     COM_04_print_message length=0x00CC (to 0x56EC)
5620:          11 4E 79 8D D3 78 0E 8A BD 46 5B F4 1B A1 2F 49
5630:          99 16 CB CE 83 96 83 96 C3 9A B2 B7 85 BE 14 EE
5640:          F3 5F 01 B3 DB 95 5F BE 5B B1 2F 49 57 17 74 CA
5650:          33 48 70 75 EF 5B 0E 58 A3 46 E5 BD 53 74 43 54
5660:          8B 9A 83 7A 5F BE 23 7B 66 B1 5F 17 5D 9E C5 B5
5670:          1D A0 50 BD 13 BF 57 17 13 B4 50 54 D6 6A DB 72
5680:          69 BE 53 C6 4D 98 B8 16 63 16 23 54 75 98 D0 15
5690:          82 17 54 5E 3F A0 56 F4 DB 72 85 91 90 73 4B 62
56A0:          40 55 4B BD 90 96 EB 62 11 4E 79 8D D3 78 05 8A
56B0:          63 B1 91 BE 8B 9A 23 D1 13 54 9B 91 C4 16 63 16
56C0:          50 DB F3 A0 F9 A6 5B CA 57 C6 EE 68 89 17 82 17
56D0:          45 5E C9 9F 9F 9B 82 17 52 5E 81 8D C4 97 3F 16
56E0:          0D 47 FF 14 DF 61 95 AF C1 A0 97 7B
;
;              BIOLOGICAL LABS. YOU ARE NOW IN AN ANTISEPTIC, RED ROOM.
;              THERE ARE SEVERAL HUNDRED LAB TECHNICIANS IN THEIR RED
;              SMOCKS CONSTANTLY SERVICING THE THOUSANDS OF MACHINES IN
;              THE ROOM. THE MACHINES CONTAIN NEW BIOLOGICAL CREATIONS
;              WHICH MAY OR MAY NOT PROVE USEFUL TO THE COLONY. THE
;              PLOONAB LEADS DEEPER SORWIT.
;
;
56EC:    04 0B                           ;   ---- Section SECTION_04_COMMANDS length=0x000B (to 0x56F9)
56EE:       0B 09 0A                     ;     COM_0B_switch length=0x0009 (to 0x56FA), function=COM_0A_is_input_phrase(phrase_num)
56F1:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
56F3:             00 85                  ;         COM_00_move_and_look(room=RM_9_MUSEUM)
;                                        ;       end case
56F5:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
56F7:             00 88                  ;         COM_00_move_and_look(room=RM_9_GREEN_HOUSE)
;                                        ;       end case
;                                        ;     end decode_switch at 0x56EE

; --------------------------------------------------------------------------------------------------------------------
;
56F9: 87 80 B5 00                        ; ----- Room 0x87 RM_9_NURSERY, Length: 0x00B5, Data: 0x00
;
56FD:    03 80 9E                        ;   ---- Section SECTION_03_DESCRIPTION length=0x009E (to 0x579E)
5700:       04 80 9B                     ;     COM_04_print_message length=0x009B (to 0x579E)
5703:          F4 9A B4 B7 DB E0 5F BE 39 17 DB 9F 5B BE 1B BC
5713:          1B A1 2F 49 99 16 D5 CE 50 BD 90 5A CB 6A 83 96
5723:          9F A6 3D 49 89 17 AF 14 7B 14 69 75 50 5E 3D C6
5733:          43 62 44 F4 73 C6 C7 DE AB 98 43 48 9D 61 94 14
5743:          58 5E 43 62 55 17 2D 49 DB 63 5F BE 39 17 DB 9F
5753:          47 55 B3 8B 50 72 FF 5A 57 17 74 CA 33 48 70 75
5763:          EF 5B 16 58 87 74 10 B7 03 58 03 BC 83 17 3E 92
5773:          90 14 16 58 75 75 57 17 75 61 2F 15 53 A7 90 14
5783:          06 58 5F 60 26 98 5C F4 7F 7B C3 B5 5B B1 9F 61
5793:          BE B1 43 5E 33 98 44 B9 56 D1 2E
;
;              NURSERY. THE ROOM THAT YOU ARE NOW STANDING IN APPEARS TO
;              BE A HUGE NURSERY. BUT YOUNG ALIENS ARE VERY SCARCE. THE
;              ROOM COULD HANDLE SEVERAL HUNDRED THOUSAND AT A TIME, AND
;              THUS SEEMS EMPTY AND DEFUNCT. ZITES ARE ENURGLE AND SORWIT.
;
;
579E:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011 (to 0x57B1)
57A0:       0B 0F 0A                     ;     COM_0B_switch length=0x000F (to 0x57B2), function=COM_0A_is_input_phrase(phrase_num)
57A3:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
57A5:             00 88                  ;         COM_00_move_and_look(room=RM_9_GREEN_HOUSE)
;                                        ;       end case
57A7:          02 08                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0008
57A9:             0E 06                  ;         COM_0E_group_OR length=0x0006 (to 0x57B1)
57AB:                14                  ;           COM_14_reverse_status next command
57AC:                1C 95               ;           COM_1C_set_var_object(obj=OBJ_95_DOOR_ESNEL)
57AE:                C7                  ;           FN_C7_IS_OBJECT_RIBULN
57AF:                00 8A               ;           COM_00_move_and_look(room=RM_9_GENERATOR)
;                                        ;         end group_OR at 0x57A9
;                                        ;       end case
;                                        ;     end decode_switch at 0x57A0

; --------------------------------------------------------------------------------------------------------------------
;
57B1: 88 80 FC 00                        ; ----- Room 0x88 RM_9_GREEN_HOUSE, Length: 0x00FC, Data: 0x00
;
57B5:    03 80 E7                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00E7 (to 0x589F)
57B8:       04 80 E4                     ;     COM_04_print_message length=0x00E4 (to 0x589F)
57BB:          AF 6E 83 61 87 74 BF B7 51 18 43 C2 5B B1 FB B9
57CB:          43 98 AB 98 83 7A 4E 45 31 49 45 5E CF 49 C3 B2
57DB:          23 D1 13 54 4B 7B EE 68 11 8A 96 64 AF C3 07 B3
57EB:          D4 B5 46 A0 5B BB 5F BE 5B B1 2F 49 09 15 70 E3
57FB:          D1 B5 99 64 B5 A0 3D 62 9A 13 40 49 66 62 91 7A
580B:          D6 1F F5 72 54 5E 46 A0 D9 B5 82 7B 3B 16 B7 B1
581B:          63 16 23 54 75 98 4F F4 DA C3 B8 16 82 17 54 5E
582B:          3F A0 D5 15 99 16 49 16 B7 98 92 AF F6 B2 E6 C3
583B:          CF 7B 03 EE 33 98 58 6D 4B 62 5F BE CF 15 EF A6
584B:          DB B9 03 A0 C3 9E 59 45 8E 7A 91 7A 09 15 03 D2
585B:          C3 9E F4 68 5F BE 92 AF F6 B2 E6 C3 C0 7A 56 F4
586B:          DB 72 09 A6 0B A0 95 4B C1 A0 73 7B 79 68 56 90
587B:          DB 72 34 BA C5 65 55 5E 82 BF CA B5 2F 62 5C F4
588B:          7F 7B CE B5 86 5F 30 15 31 C6 DB 8B 8E 48 FB 17
589B:          21 C0 1B B5              
;
;              GREEN HOUSE. YOU ARE STANDING IN A LARGE CAVERN WHICH IS
;              FULL OF TUBEROUS ROOTS. THERE ARE DOZENS OF WORKERS
;              'HARVESTING' THESE ROOTS WITH LARGE MACHINES. MUCH OF THE
;              ROOM IS NO LONGER PRODUCTIVE, AND GIVES THE IMPRESSION OF A
;              WINDING DOWN OF FURTHER PRODUCTION. THE PLOONAB SORWIT FROM
;              THE SURFACE STOPS HERE. ZITES LEAD ENURGLE AND WITSOR.
;
;
589F:    04 0F                           ;   ---- Section SECTION_04_COMMANDS length=0x000F (to 0x58B0)
58A1:       0B 0D 0A                     ;     COM_0B_switch length=0x000D (to 0x58B1), function=COM_0A_is_input_phrase(phrase_num)
58A4:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
58A6:             00 87                  ;         COM_00_move_and_look(room=RM_9_NURSERY)
;                                        ;       end case
58A8:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
58AA:             00 86                  ;         COM_00_move_and_look(room=RM_9_BIOLOGICAL)
;                                        ;       end case
58AC:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
58AE:             00 89                  ;         COM_00_move_and_look(room=RM_9_LIBRARY2)
;                                        ;       end case
;                                        ;     end decode_switch at 0x58A1

; --------------------------------------------------------------------------------------------------------------------
;
58B0: 89 80 B4 00                        ; ----- Room 0x89 RM_9_LIBRARY2, Length: 0x00B4, Data: 0x00
;
58B4:    03 80 9D                        ;   ---- Section SECTION_03_DESCRIPTION length=0x009D (to 0x5954)
58B7:       04 80 9A                     ;     COM_04_print_message length=0x009A (to 0x5954)
58BA:          84 8C D4 B0 DB E0 69 75 45 5E F2 9F 7F C6 84 AF
58CA:          95 48 C8 B5 46 7A 82 17 4B 7B 1B 54 AF 91 1B B5
58DA:          4A 45 8E 48 EE 68 B8 16 8E 14 30 79 C3 B5 5B B1
58EA:          16 D0 23 54 AB 98 56 45 EF 74 96 63 67 7A 9B 9A
58FA:          0B A0 06 8A 62 7B 5B 8B B8 16 61 17 36 92 90 73
590A:          D6 6A DB 9C 34 A1 3F 16 D7 68 82 17 59 5E 56 7B
591A:          DB 9F C3 9E 5F BE 89 14 4B 62 47 55 B3 8B 5B 4D
592A:          09 BA 66 B1 FB 17 63 BE 96 96 95 73 AF 15 9B 6C
593A:          85 91 90 73 DB 63 16 E4 4B 62 E3 8B 19 58 8D 7B
594A:          A3 A0 8E 48 61 17 3B B4 9B C1
;
;              LIBRARY. HUGE COMPUTER BANKS FILL THIS CHAMBER. A HANDFUL
;              OF ALIENS ARE WATCHING A THREE-DIMENSIONAL DISPLAY OF
;              SOMETHING TO YOUR LEFT. THE WISDOM OF THE AGES COULD BE
;              STORED WITHIN THIS HUGE MACHINE. ZITES LEAD WITSOR AND
;              SORWIT.
;
;
5954:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011 (to 0x5967)
5956:       0B 0F 0A                     ;     COM_0B_switch length=0x000F (to 0x5968), function=COM_0A_is_input_phrase(phrase_num)
5959:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
595B:             00 88                  ;         COM_00_move_and_look(room=RM_9_GREEN_HOUSE)
;                                        ;       end case
595D:          02 08                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0008
595F:             0E 06                  ;         COM_0E_group_OR length=0x0006 (to 0x5967)
5961:                14                  ;           COM_14_reverse_status next command
5962:                1C 96               ;           COM_1C_set_var_object(obj=OBJ_96_DOOR_ESNEL)
5964:                C7                  ;           FN_C7_IS_OBJECT_RIBULN
5965:                00 8C               ;           COM_00_move_and_look(room=RM_9_DETROIT)
;                                        ;         end group_OR at 0x595F
;                                        ;       end case
;                                        ;     end decode_switch at 0x5956

; --------------------------------------------------------------------------------------------------------------------
;
5967: 8A 80 C0 00                        ; ----- Room 0x8A RM_9_GENERATOR, Length: 0x00C0, Data: 0x00
;
596B:    03 80 AF                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00AF (to 0x5A1D)
596E:       04 80 AC                     ;     COM_04_print_message length=0x00AC (to 0x5A1D)
5971:          B0 6C 2B 62 84 BF 4A F4 77 C4 77 15 74 98 89 49
5981:          8B B3 0E 67 16 8A 95 73 39 17 FF 9F 82 17 3B 63
5991:          2F 49 82 17 52 5E 77 A1 95 AF EA C5 FB 8E C3 9E
59A1:          5F BE E1 14 80 8D DB E0 79 68 56 90 DB 72 AF 6E
59B1:          73 49 64 C0 4B 62 5B BE 0E BC 86 5F 82 17 07 B3
59C1:          13 6D 5F BE 56 15 44 A0 1B EE 1B A1 2F 49 4B 15
59D1:          36 7B 55 DB 2F C6 82 17 73 49 5F BE 23 7B 89 A6
59E1:          23 62 47 B9 17 B1 D5 15 82 17 4F 5E CE 9F 83 61
59F1:          44 55 51 5E 96 64 EB 72 91 AF 03 D2 FB A5 76 98
5A01:          5B F4 1B A1 10 53 81 15 30 15 31 C6 DB 8B 8E 48
5A11:          9F 16 BE B1 48 5E FF B2 9F 15 7F B1
;
;              GENERATOR. HUGE GENERATORS FILL THIS ROOM. THEY ARE THE
;              POWER SUPPLY OF THE COLONY. FROM THE GREAT TUBES THAT LEAD
;              THROUGH THE FLOOR, YOU ARE FAIRLY SURE THAT THEIR POWER
;              SOURCE IS THE MOLTEN CORE OF THEIR OWN PLANET. YOU CAN GO
;              ENURGLE AND NURGLE FROM HERE.
;
;
5A1D:    04 0B                           ;   ---- Section SECTION_04_COMMANDS length=0x000B (to 0x5A2A)
5A1F:       0B 09 0A                     ;     COM_0B_switch length=0x0009 (to 0x5A2B), function=COM_0A_is_input_phrase(phrase_num)
5A22:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5A24:             00 8B                  ;         COM_00_move_and_look(room=RM_9_PITTSBURG)
;                                        ;       end case
5A26:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5A28:             00 87                  ;         COM_00_move_and_look(room=RM_9_NURSERY)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5A1F

; --------------------------------------------------------------------------------------------------------------------
;
5A2A: 8B 80 E0 00                        ; ----- Room 0x8B RM_9_PITTSBURG, Length: 0x00E0, Data: 0x00
;
5A2E:    03 80 CF                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00CF (to 0x5B00)
5A31:       04 80 CC                     ;     COM_04_print_message length=0x00CC (to 0x5B00)
5A34:          96 A5 14 C0 31 C6 5B F4 1B A1 FB B9 5B B1 83 7A
5A44:          F7 49 96 14 7B 14 57 B7 5B 98 0C BA C9 47 33 75
5A54:          36 A1 B8 16 FB 14 BF 9A 0B B6 90 7A 38 62 5B A2
5A64:          69 75 55 5E 2E 92 F4 BD C3 B5 33 98 F4 68 C5 97
5A74:          4B 62 87 A6 8F AF CE 9F 83 61 36 92 4D 48 D0 15
5A84:          6B BF 15 53 0B C0 83 7A 55 45 7B 5F C3 9E 7B 67
5A94:          3F 92 38 15 83 61 6C BE 29 A1 16 71 DB 72 04 68
5AA4:          9B 53 07 67 B3 8B 5B BE 12 BC 06 B3 E6 5F DB B5
5AB4:          3E A1 51 18 45 C2 83 48 67 66 16 8A DB 72 E3 72
5AC4:          9B C1 83 48 9F 61 BE B1 A9 63 8D 7B A3 A0 16 E4
5AD4:          45 5E 1E A0 9F 7A 4B 62 79 68 4A 90 2F 62 56 F4
5AE4:          DB 72 8F 4E DF B2 4B 90 CE B5 53 9E E6 BD C3 14
5AF4:          82 17 55 5E C1 A0 73 7B 7B 67 FF B8
;
;              PITTSBURG. YOU STARE IN AWE AT A SCENE STRAIGHT OUT OF
;              DANTES' INFERNO. HUGE SMELTERS AND FURNACES POUR MOLTEN
;              METALS INTO CASTS IN A SEA OF FLAME. EVEN THROUGH THE FORCE
;              FIELD THAT PROTECTS YOU, YOU CAN FEEL THE HEAT. AN
;              ENURGLE-WITSOR ZITE CONTINUES FROM HERE. THE BLURNUM IS
;              LOCATED BY THE SORWIT FLASM.
;
;
5B00:    04 0B                           ;   ---- Section SECTION_04_COMMANDS length=0x000B (to 0x5B0D)
5B02:       0B 09 0A                     ;     COM_0B_switch length=0x0009 (to 0x5B0E), function=COM_0A_is_input_phrase(phrase_num)
5B05:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5B07:             00 8A                  ;         COM_00_move_and_look(room=RM_9_GENERATOR)
;                                        ;       end case
5B09:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5B0B:             00 8C                  ;         COM_00_move_and_look(room=RM_9_DETROIT)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5B02

; --------------------------------------------------------------------------------------------------------------------
;
5B0D: 8C 80 B0 00                        ; ----- Room 0x8C RM_9_DETROIT, Length: 0x00B0, Data: 0x00
;
5B11:    03 80 9F                        ;   ---- Section SECTION_03_DESCRIPTION length=0x009F (to 0x5BB3)
5B14:       04 80 9C                     ;     COM_04_print_message length=0x009C (to 0x5BB3)
5B17:          F6 59 FB B2 9B C1 69 75 43 5E D7 B9 B6 91 4E DB
5B27:          8F 7A C8 B5 46 7A 82 17 4B 7B 01 B3 B3 95 85 5F
5B37:          0F 71 9F 48 C5 65 74 C0 91 7A 61 17 1B 92 29 63
5B47:          85 BE 03 EE 87 8C 8F 96 DA 46 8F 7A 44 F4 51 63
5B57:          33 98 5F BE 5B 90 1B A1 10 53 57 17 43 5E 8F 16
5B67:          C1 C0 4B B2 C3 9E 70 C0 6E 98 D6 B5 56 72 57 17
5B77:          5B 61 6B BF 04 4F 47 5E 46 98 65 62 FB 8E 9E 7A
5B87:          D6 9C DB 72 09 BA 5B 98 C3 9E 63 BE D5 B5 EB BF
5B97:          B7 98 E6 16 8F 48 9B C1 16 E4 4B 62 E3 8B 10 58
5BA7:          31 C6 DB 8B 8E 48 FB 17 21 C0 1B B5
;
;              DETROIT. HUGE ASSEMBLY LINES FILL THIS ROOM, EACH
;              MANUFACTURING SOME EXOTIC, ALIEN MACHINE. BEYOND THEM YOU
;              CAN SEE A NETWORK OF TUNNELS THAT SEEM TO BORE ENDLESSLY
;              INTO THE STONE OF THIS STRANGE PLANET. ZITES LEAD NURGLE
;              AND WITSOR.
;
;
5BB3:    04 0B                           ;   ---- Section SECTION_04_COMMANDS length=0x000B (to 0x5BC0)
5BB5:       0B 09 0A                     ;     COM_0B_switch length=0x0009 (to 0x5BC1), function=COM_0A_is_input_phrase(phrase_num)
5BB8:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5BBA:             00 8B                  ;         COM_00_move_and_look(room=RM_9_PITTSBURG)
;                                        ;       end case
5BBC:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5BBE:             00 89                  ;         COM_00_move_and_look(room=RM_9_LIBRARY2)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5BB5
```

# Unitialized data

```code
5BC0: 5F C8 B5 FF B2 82 17 55 5E 36 A1 16 71 D6 9C DB ; _......U^6..q...
5BD0: 72 95 5F 9B C1 04 1B 0B 19 0A 03 02 00 F1 04 02 ; r._.............
5BE0: 00 F5 01 02 00 F3 02 0A 0D 08 C8 30 B7 17 9D 00 ; ...........0....
5BF0: 2F 02 F7 19 00 03 01 AB 04 13 0B 11 0A 03 02 00 ; /...............
5C00: FA 04 02 00 F7 01 02 00 F7 02 02 00 F8 F8 19 00 ; ................
5C10: 03 01 AB 04 13 0B 11 0A 03 02 00 F8 04 02 00 F9 ; ................
5C20: 01 02 00 F8 02 02 00 F8 F9 21 00 03 01 AB 04 1B ; .........!......
5C30: 0B 19 0A 03 0A 0E 08 0D 04 05 3E 00 86 00 F9 04 ; ..........>.....
5C40: 02 00 F8 01 02 00 FA 02 02 00 F9 FA 19 00 03 01 ; ................
5C50: AB 04 13 0B 11 0A 03 02 00 FA 04 02 00 F7 01 02 ; ................
5C60: 00 FA 02 02 00 F9 4C 41 54 22 05 53 50 41 52 45 ; ......LAT".SPARE
5C70: 23 04 42 4C 55 45 0D 06 4D 41 53 53 49 56 3F 04 ; #.BLUE..MASSIV?.
5C80: 42 41 4E 4B 40 06 53 41 4C 4F 4F 4E 41 06 53 48 ; BANK@.SALOONA.SH
5C90: 45 52 49 46 42 06 4F 46 46 49 43 45 42 06 53 4C ; ERIFB.OFFICEB.SL
5CA0: 49 4D 27 53 43 05 53 4C 49 4D 53 43 05 42 4F 42 ; IM'SC.SLIMSC.BOB
5CB0: 27 53 44 04 42 4F 42 53 44 06 44 4F 55 42 4C 45 ; 'SD.BOBSD.DOUBLE
5CC0: 45 05 48 4F 54 45 4C 47 06 53 57 49 4E 47 49 46 ; E.HOTELG.SWINGIF
5CD0: 04 54 53 4F 4D 6B 04 43 4F 4F 4C 72 05 43 4C 45 ; .TSOMk.COOLr.CLE
5CE0: 41 52 74 05 42 52 4F 57 4E 73 00 02 54 4F 01 04 ; ARt.BROWNs..TO..
5CF0: 57 49 54 48 02 05 55 53 49 4E 47 02 02 41 54 03 ; WITH..USING..AT.
5D00: 05 
```

