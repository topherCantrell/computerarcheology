![Xenos](Xenos.png)

# Xenos SECTION4.DAT

>>> cpu Z80

>>> binary 5200:roms/section4.bin

```code
5200: 00 8A 50                           ; List_ID=0x00, length=0x0A50

; --------------------------------------------------------------------------------------------------------------------
;
5203: 99 81 1C 00                        ; ----- Room 0x99 RM_4_MAIN_STREET_EAST, Length: 0x011C, Data: 0x00
;
5207:    03 80 F3                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00F3
520A:       04 80 F0                     ;     COM_04_print_command length=0x00F0
520D:          8B 91 95 96 EF BF 73 62 95 5F 9B C1 C7 DE 94 14 ; 
521D:          51 5E 8F 96 D0 47 66 17 67 B1 03 BC 16 BC DB 72 ; 
522D:          95 5F 07 BC 33 98 C3 9E 89 BF 1B 9C 03 A0 5F BE ; 
523D:          99 16 C2 B3 5B 17 DB 59 C3 9E 5F BE 66 17 67 B1 ; 
524D:          0B BC C3 B5 3B 16 B7 B1 01 18 7F 9E 84 96 CE C4 ; 
525D:          90 5A D6 6A 56 72 D5 15 63 16 57 B2 73 5D E9 1B ; 
526D:          EE BD 63 F4 03 A0 5F BE 61 17 82 C6 5B 17 DB 59 ; 
527D:          C3 9E 5F BE 66 17 67 B1 0B BC C3 B5 3B 16 B7 B1 ; 
528D:          BC 14 DD 78 BF 14 3E 7A 91 7A 82 17 73 49 4B 7B ; 
529D:          94 91 A6 85 FC ED D0 4C E3 83 83 7A 54 8B 9B 6C ; 
52AD:          F6 8B F4 BD D1 B5 83 96 01 18 7F 9E 95 96 80 79 ; 
52BD:          C7 16 08 BC 00 B3 9B C1 83 7A 5F BE FB 17 49 98 ; 
52CD:          D6 CE F4 72 4B 5E C3 B5 5F 17 46 48 DB 16 9E 7A ; 
52DD:          F3 5F 49 B8 96 96 56 72 2F 17 0D 47 FC ED 86 BF ; 
52ED:          33 48 65 49 8D 62 FF F9 5A F5 F1 EE 61 3E 5C 3E ; 
;
;              MAIN STREET EAST. YOU ARE ON MAIN STREET AT THE EAST END OF
;              TOWN. ON THE NORTH SIDE OF THE STREET IS A LARGE WOODEN
;              BUILDING THAT IS MARKED, "HOTEL." ON THE SOUTH SIDE OF THE
;              STREET IS A LARGE BRICK BUILDING THAT IS MARKED, "BANK" IN
;              LARGE LETTERS ON A WOODEN SIGN OUT FRONT. IN THE WINDOW
;              THERE IS A SMALL PAINTED SIGN THAT READS, "TOTAL
;              ASSETS....33,000.00."
;
;
52FD:    04 23                           ;   ---- Section SECTION_04_COMMANDS length=0x0023
52FF:       0B 21 0A                     ;     COM_0B_switch length=0x0021, function=COM_0A_is_input_phrase(phrase_num)
5302:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5303:          02                        ;       ELSE goto=0x5306
5304:             00 9C                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_TOWN)
5306:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5307:          06                        ;       ELSE goto=0x530E
5308:             0D 04                  ;         COM_0D_while_pass length=0x0004
530A:                30 96               ;           COM_30_set_current_room(room=RM_3_EAST_ALLEY_INTERSECTION)
530C:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
530E:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
530F:          08                        ;       ELSE goto=0x5318
5310:             0E 06                  ;         COM_0E_while_fail length=0x0006
5312:                14                  ;           COM_14_execute_and_reverse_status next command
5313:                1C 0E               ;           COM_1C_set_var_object(obj=OBJ_0E_DOOR_MAIN_STREET_EAST_HOTEL)
5315:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5316:                00 AA               ;           COM_00_move_and_look(room=RM_4_HOTEL_LOBBY)
5318:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5319:          08                        ;       ELSE goto=0x5322
531A:             0E 06                  ;         COM_0E_while_fail length=0x0006
531C:                14                  ;           COM_14_execute_and_reverse_status next command
531D:                1C 10               ;           COM_1C_set_var_object(obj=OBJ_10_DOOR_MAIN_STREET_EAST_BANK)
531F:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5320:                00 9A               ;           COM_00_move_and_look(room=RM_4_BANK)

; --------------------------------------------------------------------------------------------------------------------
;
5322: 9A 28 00                           ; ----- Room 0x9A RM_4_BANK, Length: 0x0028, Data: 0x00
;
5325:    03 16                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0016
5327:       04 14                        ;     COM_04_print_command length=0x0014
5329:          D0 4C 5B 89 C7 DE 94 14 4B 5E 9B 9A DB 59 5F BE ; 
5339:          AB 14 6F 99               ; 
;
;              BANK. YOU ARE INSIDE THE BANK.
;
;
533D:    04 0D                           ;   ---- Section SECTION_04_COMMANDS length=0x000D
533F:       0B 0B 0A                     ;     COM_0B_switch length=0x000B, function=COM_0A_is_input_phrase(phrase_num)
5342:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5343:          08                        ;       ELSE goto=0x534C
5344:             0E 06                  ;         COM_0E_while_fail length=0x0006
5346:                14                  ;           COM_14_execute_and_reverse_status next command
5347:                1C 11               ;           COM_1C_set_var_object(obj=OBJ_11_DOOR_BANK)
5349:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
534A:                00 99               ;           COM_00_move_and_look(room=RM_4_MAIN_STREET_EAST)

; --------------------------------------------------------------------------------------------------------------------
;
534C: 9B 80 A6 00                        ; ----- Room 0x9B RM_4_SOUTH_OF_BANK, Length: 0x00A6, Data: 0x00
;
5350:    03 80 8D                        ;   ---- Section SECTION_03_DESCRIPTION length=0x008D
5353:       04 80 8A                     ;     COM_04_print_command length=0x008A
5356:          47 B9 53 BE C3 9E D0 4C 5B 89 C7 DE 94 14 55 5E ; 
5366:          36 A1 11 71 83 64 3B 16 B7 B1 14 EE F3 5F 73 4F ; 
5376:          8B 54 EB 4F C3 8B CF 98 89 17 51 18 23 C6 B5 D0 ; 
5386:          73 C1 C7 DE D3 14 95 96 1B 60 5F BE AB 14 8B 54 ; 
5396:          C3 9E 5F BE 84 15 57 9E E5 AF 48 F4 3E C6 F4 72 ; 
53A6:          F7 17 F3 B9 C7 DE D3 14 95 96 1B 60 5F BE AB 14 ; 
53B6:          8B 54 C3 9E 83 48 09 47 5B 4D EB 4F C3 8B CF 98 ; 
53C6:          82 17 46 5E 57 62 B3 B3 0E 67 0B 8E 5F BE 61 17 ; 
53D6:          82 C6 38 62 A9 15 1C B2 27 A0 ; 
;
;              SOUTH OF BANK. YOU ARE SOUTH OF A LARGE, RED BRICK
;              BUILDING. TO YOUR WEST, YOU CAN SEE THE BACK OF THE
;              GROCER'S. FURTHER WEST YOU CAN SEE THE BACK OF AN ADOBE
;              BUILDING. THE DESERT FILLS THE SOUTHERN HORIZON.
;
;
53E0:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
53E2:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
53E5:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
53E6:          02                        ;       ELSE goto=0x53E9
53E7:             00 B2                  ;         COM_00_move_and_look(room=RM_4_DESERT_SOUTH3)
53E9:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
53EA:          02                        ;       ELSE goto=0x53ED
53EB:             00 9E                  ;         COM_00_move_and_look(room=RM_4_SOUTHEAST_OF_BANK)
53ED:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
53EE:          06                        ;       ELSE goto=0x53F5
53EF:             0D 04                  ;         COM_0D_while_pass length=0x0004
53F1:                30 98               ;           COM_30_set_current_room(room=RM_3_SOUTH_OF_EAST_ALLEY)
53F3:                2F 03               ;           COM_2F_load_section_from_disk(section=3)

; --------------------------------------------------------------------------------------------------------------------
;
53F5: 9C 81 92 00                        ; ----- Room 0x9C RM_4_EAST_OF_TOWN, Length: 0x0192, Data: 0x00
;
53F9:    03 81 79                        ;   ---- Section SECTION_03_DESCRIPTION length=0x0179
53FC:       04 81 76                     ;     COM_04_print_command length=0x0176
53FF:          95 5F 11 BC 96 64 80 A1 5B F4 1B A1 2F 49 66 17 ; 
540F:          8E 48 91 7A C0 16 82 17 4A 5E 7A 79 1B D0 96 14 ; 
541F:          82 17 47 5E 66 49 30 15 11 58 96 64 80 A1 43 F4 ; 
542F:          5F 17 46 48 5B 17 03 6E F4 72 54 5E 86 5F 33 BB ; 
543F:          2F 1D B3 B1 84 BF 45 DB 93 7B 43 16 D6 92 5C BB ; 
544F:          51 18 45 C2 83 48 A7 B7 5B 17 04 D5 CE C4 90 5A ; 
545F:          CB 6E 83 7A 5F BE 89 17 27 D2 C0 16 82 17 50 5E ; 
546F:          BE A0 15 71 FF 78 B8 16 82 17 55 5E EF BF 73 62 ; 
547F:          5F BE 5B B1 4B 7B 44 45 CE C4 90 5A CF 6A 35 49 ; 
548F:          16 60 72 13 FF A0 9C 8F 8F 16 33 D9 6B BF 73 7B ; 
549F:          C7 DE D3 14 8F 96 17 48 C7 16 16 BC DB 72 49 B8 ; 
54AF:          F3 9B F9 1A E5 4B 9B 15 51 B1 2F 49 23 EE 83 7A ; 
54BF:          79 68 B3 9A C3 9E 59 45 36 A0 83 61 0C BA E6 C3 ; 
54CF:          2F C6 55 F4 8E BE 08 8A 3E C6 F4 72 09 15 03 D2 ; 
54DF:          5F BE 66 17 67 B1 73 C1 03 A0 5F BE 53 17 1B 92 ; 
54EF:          46 B8 B3 63 4B 7B 4E 45 31 49 59 5E 36 A0 83 61 ; 
54FF:          EB 4F C3 8B CF 98 C0 16 82 17 55 5E 36 A1 15 71 ; 
550F:          FF 78 B8 16 82 17 55 5E EF BF 73 62 5F BE 5B B1 ; 
551F:          4B 7B 54 45 F3 5F 73 4F 8B 54 D0 4C 5B 89 7A 98 ; 
552F:          16 BC CB 9C 06 BC 80 A1 82 17 55 5E EF BF 73 62 ; 
553F:          4B 7B 1B D1 03 BC E3 A4 8B B3 6B BF 5B 4D 55 45 ; 
554F:          8E 91 09 8A F5 B2 43 62 66 17 AF A0 48 F4 8B 7A ; 
555F:          13 8D 16 EE F4 72 4B 5E C3 B5 83 96 74 5B 44 5E ; 
556F:          CE C4 90 5A 5B 70         ; 
;
;              EAST OF TOWN. YOU ARE STANDING ON THE HIGHWAY AT THE EAST
;              END OF TOWN. A SMALL SIGN HERE READS, "PURGATORY CITY
;              LIMITS." YOU CAN SEE SIX BUILDINGS IN THE TOWN. ON THE
;              NORTH SIDE OF THE STREET THERE IS A BUILDING MARKED,
;              "HOTEL." NEXT TO IT YOU CAN MAKE OUT THE SIGN, "BOB'S
;              HARDWARE," IN FRONT OF A WOODEN STRUCTURE. STILL FURTHER
;              DOWN THE STREET, ON THE SAME SIDE, IS A LARGE WOODEN
;              BUILDING. ON THE SOUTH SIDE OF THE STREET THERE IS A RED
;              BRICK BANK. NEXT TO IT DOWN THE STREET IS WHAT APEARS TO BE
;              A SMALL GROCERY STORE. FINALLY, THERE IS AN ADOBE BUILDING.
;
;
5575:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5577:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
557A:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
557B:          02                        ;       ELSE goto=0x557E
557C:             00 AC                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_HOTEL)
557E:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
557F:          02                        ;       ELSE goto=0x5582
5580:             00 9D                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_BANK)
5582:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5583:          02                        ;       ELSE goto=0x5586
5584:             00 B4                  ;         COM_00_move_and_look(room=RM_4_HIGHWAY_EAST)
5586:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5587:          02                        ;       ELSE goto=0x558A
5588:             00 99                  ;         COM_00_move_and_look(room=RM_4_MAIN_STREET_EAST)

; --------------------------------------------------------------------------------------------------------------------
;
558A: 9D 80 88 00                        ; ----- Room 0x9D RM_4_EAST_OF_BANK, Length: 0x0088, Data: 0x00
;
558E:    03 74                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0074
5590:       04 72                        ;     COM_04_print_command length=0x0072
5592:          95 5F 11 BC 84 64 95 48 5B F4 1B A1 2F 49 23 15 ; 
55A2:          F3 B9 C3 9E 54 45 F3 5F 73 4F 8B 54 EB 4F C3 8B ; 
55B2:          AB 98 73 49 5F BE 23 15 F3 B9 8E 61 B8 16 89 17 ; 
55C2:          27 D2 89 17 82 17 50 5E BE A0 1B 71 1B A1 10 53 ; 
55D2:          57 17 56 5E DB 72 89 73 B3 75 DB E0 6B BF 5F BE ; 
55E2:          61 17 82 C6 90 14 07 58 66 49 10 EE 02 A1 91 7A ; 
55F2:          D5 15 D3 17 44 B8 DB 8B 03 A0 5F BE FF 14 B4 B7 ; 
5602:          9B C1                     ; 
;
;              EAST OF BANK. YOU ARE EAST OF A RED BRICK BUILDING AT THE
;              EAST END OF TOWN. TO THE NORTH YOU CAN SEE THE HIGHWAY. TO
;              THE SOUTH AND EAST, NOTHING IS VISIBLE ON THE DESERT.
;
;
5604:    04 0F                           ;   ---- Section SECTION_04_COMMANDS length=0x000F
5606:       0B 0D 0A                     ;     COM_0B_switch length=0x000D, function=COM_0A_is_input_phrase(phrase_num)
5609:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
560A:          02                        ;       ELSE goto=0x560D
560B:             00 9C                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_TOWN)
560D:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
560E:          02                        ;       ELSE goto=0x5611
560F:             00 9E                  ;         COM_00_move_and_look(room=RM_4_SOUTHEAST_OF_BANK)
5611:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5612:          02                        ;       ELSE goto=0x5615
5613:             00 B5                  ;         COM_00_move_and_look(room=RM_4_SOUTH_OF_HIGHWAY)

; --------------------------------------------------------------------------------------------------------------------
;
5615: 9E 80 98 00                        ; ----- Room 0x9E RM_4_SOUTHEAST_OF_BANK, Length: 0x0098, Data: 0x00
;
5619:    03 79                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0079
561B:       04 77                        ;     COM_04_print_command length=0x0077
561D:          47 B9 5F BE 66 49 B8 16 AB 14 6F 99 51 18 43 C2 ; 
562D:          5B B1 09 9A 66 17 8E 48 91 7A D0 15 82 17 46 5E ; 
563D:          57 62 B3 B3 47 B9 53 BE C3 9E 5F BE A3 15 31 6D ; 
564D:          5E 4A 90 14 08 58 23 49 95 5F 11 BC 96 64 80 A1 ; 
565D:          56 F4 D6 9C DB 72 B5 D0 73 C1 C7 DE D3 14 95 96 ; 
566D:          1B 60 5F BE AB 14 A5 54 B8 16 82 17 44 5E CE C4 ; 
567D:          90 5A CB 6E 5B BE 0E BC 8F 7A 61 17 82 C6 63 16 ; 
568D:          83 7A 0C BA 36 60 2E      ; 
;
;              SOUTHEAST OF BANK. YOU ARE NOW STANDING IN THE DESERT SOUTH
;              OF THE HIGHWAY, AND FAR EAST OF TOWN. TO THE WEST, YOU CAN
;              SEE THE BACKS OF THE BUILDINGS THAT LINE SOUTH MAIN STREET.
;
;
5694:    04 1A                           ;   ---- Section SECTION_04_COMMANDS length=0x001A
5696:       0B 18 0A                     ;     COM_0B_switch length=0x0018, function=COM_0A_is_input_phrase(phrase_num)
5699:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
569A:          02                        ;       ELSE goto=0x569D
569B:             00 9D                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_BANK)
569D:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
569E:          02                        ;       ELSE goto=0x56A1
569F:             00 B2                  ;         COM_00_move_and_look(room=RM_4_DESERT_SOUTH3)
56A1:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
56A2:          09                        ;       ELSE goto=0x56AC
56A3:             0D 07                  ;         COM_0D_while_pass length=0x0007
56A5:                30 E2               ;           COM_30_set_current_room(room=RM_5_DESERT23)
56A7:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
56AA:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
56AC:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
56AD:          02                        ;       ELSE goto=0x56B0
56AE:             00 9B                  ;         COM_00_move_and_look(room=RM_4_SOUTH_OF_BANK)

; --------------------------------------------------------------------------------------------------------------------
;
56B0: A9 80 B9 00                        ; ----- Room 0xA9 RM_4_NORTH_OF_HOTEL, Length: 0x00B9, Data: 0x00
;
56B4:    03 80 9C                        ;   ---- Section SECTION_03_DESCRIPTION length=0x009C
56B7:       04 80 99                     ;     COM_04_print_command length=0x0099
56BA:          04 9A 53 BE C3 9E 86 74 57 61 51 18 43 C2 5B B1 ; 
56CA:          09 9A D0 15 82 17 46 5E 57 62 B3 B3 6A 4D 8E 7A ; 
56DA:          7B 14 C1 C0 66 17 C3 A0 BF 14 3E 7A 91 7A 96 14 ; 
56EA:          82 17 50 5E BE A0 E3 72 F3 B9 8E 61 B8 16 89 17 ; 
56FA:          27 D2 56 13 D6 9C DB 72 B5 D0 1B BC 1B A1 10 53 ; 
570A:          57 17 56 5E DB 72 C5 4C CB 87 C3 9E C1 C0 01 18 ; 
571A:          7F 9E 84 96 CE C4 90 5A EF 6E 89 17 82 17 50 5E ; 
572A:          BE A0 03 71 33 98 95 5F 73 C1 5F BE CF 15 FB A5 ; 
573A:          04 53 DB 8B F5 59 3E 62 3A 15 F0 BD 0B 5C 89 BF ; 
574A:          2E 49 D0 15 10 67 93 7B 2E ; 
;
;              NORTH OF HOTEL. YOU ARE NOW IN THE DESERT BEHIND A TWO
;              STORY BUILDING AT THE NORTHEAST END OF TOWN.  TO THE WEST
;              YOU CAN SEE THE BACKS OF TWO WOODEN BUILDINGS. TO THE NORTH
;              AND EAST, THE IMPLACABLE DESERT EXTENDS TOWARD INFINITY.
;
;
5753:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5755:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
5758:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5759:          06                        ;       ELSE goto=0x5760
575A:             0D 04                  ;         COM_0D_while_pass length=0x0004
575C:                30 B8               ;           COM_30_set_current_room(room=RM_3_DESERT_NORTH2)
575E:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
5760:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5761:          02                        ;       ELSE goto=0x5764
5762:             00 AB                  ;         COM_00_move_and_look(room=RM_4_NORTHEAST_OF_HOTEL)
5764:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5765:          06                        ;       ELSE goto=0x576C
5766:             0D 04                  ;         COM_0D_while_pass length=0x0004
5768:                30 A7               ;           COM_30_set_current_room(room=RM_3_NORTH_OF_EAST_ALLEY)
576A:                2F 03               ;           COM_2F_load_section_from_disk(section=3)

; --------------------------------------------------------------------------------------------------------------------
;
576C: AA 80 A8 00                        ; ----- Room 0xAA RM_4_HOTEL_LOBBY, Length: 0x00A8, Data: 0x00
;
5770:    03 80 8D                        ;   ---- Section SECTION_03_DESCRIPTION length=0x008D
5773:       04 80 8A                     ;     COM_04_print_command length=0x008A
5776:          86 74 33 61 74 8D 9F 50 51 18 50 C2 6B A1 FB B9 ; 
5786:          33 98 9D 7A FF 78 82 17 52 5E 31 C6 89 49 7B B4 ; 
5796:          86 74 57 61 89 17 82 17 47 5E 66 49 82 17 2F 62 ; 
57A6:          D5 15 7B 14 FB B9 2D 7B 57 49 3F 16 03 47 AB 98 ; 
57B6:          D3 C5 6B BF 5F BE 57 17 40 55 08 58 81 8D 1B B5 ; 
57C6:          5F BE 5B B1 4B 7B 83 48 23 63 16 BC D6 9C DB 72 ; 
57D6:          47 B9 77 BE D0 15 7B 14 F9 A6 D0 92 9E 61 E6 16 ; 
57E6:          D7 46 C0 16 82 17 59 5E 46 48 82 17 2F 62 D5 15 ; 
57F6:          7B 14 E3 B8 F3 8C 49 B8 1B 9C ; 
;
;              HOTEL LOBBY. YOU NOW STAND INSIDE THE PURGATORY HOTEL. TO
;              THE EAST THERE IS A STAIRCASE LEADING UP TO THE SECOND
;              FLOOR. THERE IS AN EXIT TO THE SOUTH. IN A PROMINENT PLACE
;              ON THE WALL THERE IS A SMALL SIGN.
;
;
5800:    04 15                           ;   ---- Section SECTION_04_COMMANDS length=0x0015
5802:       0B 13 0A                     ;     COM_0B_switch length=0x0013, function=COM_0A_is_input_phrase(phrase_num)
5805:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5806:          08                        ;       ELSE goto=0x580F
5807:             0E 06                  ;         COM_0E_while_fail length=0x0006
5809:                14                  ;           COM_14_execute_and_reverse_status next command
580A:                1C 0F               ;           COM_1C_set_var_object(obj=OBJ_0F_DOOR_HOTEL_LOBBY)
580C:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
580D:                00 99               ;           COM_00_move_and_look(room=RM_4_MAIN_STREET_EAST)
580F:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5810:          02                        ;       ELSE goto=0x5813
5811:             00 DD                  ;         COM_00_move_and_look(room=RM_4_HALLWAY)
5813:          54                        ;       COM_0A_is_input_phrase("CLIMB * UP *")
5814:          02                        ;       ELSE goto=0x5817
5815:             00 DD                  ;         COM_00_move_and_look(room=RM_4_HALLWAY)

; --------------------------------------------------------------------------------------------------------------------
;
5817: AB 80 D4 00                        ; ----- Room 0xAB RM_4_NORTHEAST_OF_HOTEL, Length: 0x00D4, Data: 0x00
;
581B:    03 80 B0                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00B0
581E:       04 80 AD                     ;     COM_04_print_command length=0x00AD
5821:          04 9A 5F BE 66 49 B8 16 A9 15 EE BD 5B F4 1B A1 ; 
5831:          2F 49 99 16 CB CE 96 96 DB 72 F5 59 3E 62 99 16 ; 
5841:          C2 B3 95 5F 11 BC 96 64 80 A1 56 F4 D6 9C DB 72 ; 
5851:          B5 D0 1B BC 1B A1 10 53 57 17 56 5E DB 72 C5 4C ; 
5861:          D1 83 83 64 91 17 D5 9C 84 BF 44 DB CE C4 90 5A ; 
5871:          5B 70 F4 68 5F BE 99 AF 66 62 51 18 45 C2 83 48 ; 
5881:          A7 B7 82 17 44 5E DD 46 B8 16 FA 17 73 49 EA 48 ; 
5891:          94 5F D6 B5 C4 9C 43 5E 5F 17 46 48 66 17 AF A0 ; 
58A1:          4B F4 96 96 DB 72 95 5A 50 BD 9B 53 6B BF 5F BE ; 
58B1:          F7 17 F3 B9 5F BE 5B B1 4B 7B 36 DD 90 14 02 A1 ; 
58C1:          23 62 41 D2 F0 59 BF 14 3E 7A 91 7A 2E ; 
;
;              NORTHEAST OF HOTEL. YOU ARE NOW IN THE DESERT NORTHEAST OF
;              TOWN. TO THE WEST YOU CAN SEE THE BACK OF A TWO STORY
;              BUILDING. FURTHER WEST YOU CAN SEE THE BACK OF WHAT APPEARS
;              TO BE A SMALL STORE. IN THE DISTANCE TO THE WEST THERE IS
;              YET ANOTHER WOODEN BUILDING.
;
;
58CE:    04 1E                           ;   ---- Section SECTION_04_COMMANDS length=0x001E
58D0:       0B 1C 0A                     ;     COM_0B_switch length=0x001C, function=COM_0A_is_input_phrase(phrase_num)
58D3:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
58D4:          06                        ;       ELSE goto=0x58DB
58D5:             0D 04                  ;         COM_0D_while_pass length=0x0004
58D7:                30 B8               ;           COM_30_set_current_room(room=RM_3_DESERT_NORTH2)
58D9:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
58DB:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
58DC:          02                        ;       ELSE goto=0x58DF
58DD:             00 AC                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_HOTEL)
58DF:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
58E0:          09                        ;       ELSE goto=0x58EA
58E1:             0D 07                  ;         COM_0D_while_pass length=0x0007
58E3:                30 F1               ;           COM_30_set_current_room(room=RM_5_DESERT_SMALL_TRAIL1)
58E5:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
58E8:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
58EA:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
58EB:          02                        ;       ELSE goto=0x58EE
58EC:             00 A9                  ;         COM_00_move_and_look(room=RM_4_NORTH_OF_HOTEL)

; --------------------------------------------------------------------------------------------------------------------
;
58EE: AC 80 87 00                        ; ----- Room 0xAC RM_4_EAST_OF_HOTEL, Length: 0x0087, Data: 0x00
;
58F2:    03 73                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0073
58F4:       04 71                        ;     COM_04_print_command length=0x0071
58F6:          95 5F 11 BC 8A 64 FF A0 9B 8F C7 DE 94 14 43 5E ; 
5906:          16 BC DB 72 95 5F 15 BC FF 78 B8 16 82 17 4A 5E ; 
5916:          FF A0 9B 8F 6B BF 5F BE 99 16 C2 B3 90 14 07 58 ; 
5926:          66 49 82 17 4B 5E 7A 98 AB A0 7F 4E FF 14 B4 B7 ; 
5936:          15 BC EF BF 9A BD 4B 62 8E 61 F5 8B D3 B8 56 F4 ; 
5946:          D6 9C DB 72 47 B9 53 BE C7 DE D3 14 95 96 1B 60 ; 
5956:          5F BE A3 15 31 6D 3B 4A E3 8B 10 CB D6 6A 80 A1 ; 
5966:          2E                        ; 
;
;              EAST OF HOTEL. YOU ARE AT THE EAST SIDE OF THE HOTEL. TO
;              THE NORTH AND EAST THE INEXORABLE DESERT STRETCHES
;              ENDLESSLY. TO THE SOUTH YOU CAN SEE THE HIGHWAY LEAVING
;              TOWN.
;
;
5967:    04 0F                           ;   ---- Section SECTION_04_COMMANDS length=0x000F
5969:       0B 0D 0A                     ;     COM_0B_switch length=0x000D, function=COM_0A_is_input_phrase(phrase_num)
596C:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
596D:          02                        ;       ELSE goto=0x5970
596E:             00 AB                  ;         COM_00_move_and_look(room=RM_4_NORTHEAST_OF_HOTEL)
5970:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5971:          02                        ;       ELSE goto=0x5974
5972:             00 9C                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_TOWN)
5974:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5975:          02                        ;       ELSE goto=0x5978
5976:             00 B9                  ;         COM_00_move_and_look(room=RM_4_NORTH_OF_HIGHWAY4)

; --------------------------------------------------------------------------------------------------------------------
;
5978: B2 4D 00                           ; ----- Room 0xB2 RM_4_DESERT_SOUTH3, Length: 0x004D, Data: 0x00
;
597B:    03 26                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0026
597D:       04 24                        ;     COM_04_print_command length=0x0024
597F:          F5 59 3E 62 61 17 82 C6 5B F4 1B A1 2F 49 D0 15 ; 
598F:          82 17 46 5E 57 62 B3 B3 47 B9 53 BE C3 9E 5F BE ; 
599F:          89 17 27 D2               ; 
;
;              DESERT SOUTH. YOU ARE IN THE DESERT SOUTH OF THE TOWN.
;
;
59A3:    04 22                           ;   ---- Section SECTION_04_COMMANDS length=0x0022
59A5:       0B 20 0A                     ;     COM_0B_switch length=0x0020, function=COM_0A_is_input_phrase(phrase_num)
59A8:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
59A9:          02                        ;       ELSE goto=0x59AC
59AA:             00 9B                  ;         COM_00_move_and_look(room=RM_4_SOUTH_OF_BANK)
59AC:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
59AD:          06                        ;       ELSE goto=0x59B4
59AE:             0D 04                  ;         COM_0D_while_pass length=0x0004
59B0:                30 B3               ;           COM_30_set_current_room(room=RM_3_DESERT1)
59B2:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
59B4:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
59B5:          09                        ;       ELSE goto=0x59BF
59B6:             0D 07                  ;         COM_0D_while_pass length=0x0007
59B8:                30 E2               ;           COM_30_set_current_room(room=RM_5_DESERT23)
59BA:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
59BD:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
59BF:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
59C0:          06                        ;       ELSE goto=0x59C7
59C1:             0D 04                  ;         COM_0D_while_pass length=0x0004
59C3:                30 B1               ;           COM_30_set_current_room(room=RM_3_DESERT_SOUTH2)
59C5:                2F 03               ;           COM_2F_load_section_from_disk(section=3)

; --------------------------------------------------------------------------------------------------------------------
;
59C7: B4 80 BB 00                        ; ----- Room 0xB4 RM_4_HIGHWAY_EAST, Length: 0x00BB, Data: 0x00
;
59CB:    03 80 9B                        ;   ---- Section SECTION_03_DESCRIPTION length=0x009B
59CE:       04 80 98                     ;     COM_04_print_command length=0x0098
59D1:          89 73 B3 75 47 DB 66 49 5B F4 1B A1 2F 49 C0 16 ; 
59E1:          82 17 4A 5E 7A 79 1B D0 56 F4 D6 9C DB 72 B5 D0 ; 
59F1:          0B BC 96 96 DB 72 95 5A 50 BD 9B 53 C7 DE 57 17 ; 
5A01:          59 5E 56 72 92 14 E3 A4 8B B3 6B BF 5B 4D 55 45 ; 
5A11:          8E 91 16 8A 80 A1 56 F4 D6 9C DB 72 04 9A 53 BE ; 
5A21:          8E 48 61 17 82 C6 82 17 4F 5E 19 A0 80 BF 35 A1 ; 
5A31:          FF 14 B4 B7 15 BC 3C C6 30 A1 0B 5C C7 DE 56 F4 ; 
5A41:          DB 72 89 73 B3 75 4E DB 3D A0 CE B5 17 7A 7B 14 ; 
5A51:          7B 4E 8B 54 04 B2 00 4F 66 17 76 B1 23 54 AB 98 ; 
5A61:          6B BF 5F BE 23 15 17 BA   ; 
;
;              HIGHWAY EAST. YOU ARE ON THE HIGHWAY. TO THE WEST IN THE
;              DISTANCE YOU SEE WHAT APPEARS TO BE A SMALL TOWN. TO THE
;              NORTH AND SOUTH THE MONOTONOUS DESERT SURROUNDS YOU. THE
;              HIGHWAY LOOKS LIKE A BLACK RIBBON STRETCHING TO THE EAST.
;
;
5A69:    04 1A                           ;   ---- Section SECTION_04_COMMANDS length=0x001A
5A6B:       0B 18 0A                     ;     COM_0B_switch length=0x0018, function=COM_0A_is_input_phrase(phrase_num)
5A6E:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5A6F:          09                        ;       ELSE goto=0x5A79
5A70:             0D 07                  ;         COM_0D_while_pass length=0x0007
5A72:                30 F0               ;           COM_30_set_current_room(room=RM_5_EMPTY_HIGHWAY_DESERT)
5A74:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5A77:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5A79:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5A7A:          02                        ;       ELSE goto=0x5A7D
5A7B:             00 B9                  ;         COM_00_move_and_look(room=RM_4_NORTH_OF_HIGHWAY4)
5A7D:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5A7E:          02                        ;       ELSE goto=0x5A81
5A7F:             00 B5                  ;         COM_00_move_and_look(room=RM_4_SOUTH_OF_HIGHWAY)
5A81:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5A82:          02                        ;       ELSE goto=0x5A85
5A83:             00 9C                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_TOWN)

; --------------------------------------------------------------------------------------------------------------------
;
5A85: B5 6F 00                           ; ----- Room 0xB5 RM_4_SOUTH_OF_HIGHWAY, Length: 0x006F, Data: 0x00
;
5A88:    03 49                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0049
5A8A:       04 47                        ;     COM_04_print_command length=0x0047
5A8C:          47 B9 53 BE C3 9E 89 73 B3 75 DB E0 C7 DE 94 14 ; 
5A9C:          55 5E 36 A1 11 71 96 64 DB 72 89 73 B3 75 DB E0 ; 
5AAC:          83 7A 5F BE 03 15 FB B9 17 98 89 17 82 17 59 5E ; 
5ABC:          66 62 51 18 45 C2 83 48 A7 B7 57 17 74 CA 33 48 ; 
5ACC:          EB 4F C3 8B C5 98 2E      ; 
;
;              SOUTH OF HIGHWAY. YOU ARE SOUTH OF THE HIGHWAY. IN THE
;              DISTANCE TO THE WEST YOU CAN SEE SEVERAL BUILDINGS.
;
;
5AD3:    04 21                           ;   ---- Section SECTION_04_COMMANDS length=0x0021
5AD5:       0B 1F 0A                     ;     COM_0B_switch length=0x001F, function=COM_0A_is_input_phrase(phrase_num)
5AD8:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5AD9:          02                        ;       ELSE goto=0x5ADC
5ADA:             00 B4                  ;         COM_00_move_and_look(room=RM_4_HIGHWAY_EAST)
5ADC:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5ADD:          09                        ;       ELSE goto=0x5AE7
5ADE:             0D 07                  ;         COM_0D_while_pass length=0x0007
5AE0:                30 E2               ;           COM_30_set_current_room(room=RM_5_DESERT23)
5AE2:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5AE5:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5AE7:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5AE8:          09                        ;       ELSE goto=0x5AF2
5AE9:             0D 07                  ;         COM_0D_while_pass length=0x0007
5AEB:                30 F0               ;           COM_30_set_current_room(room=RM_5_EMPTY_HIGHWAY_DESERT)
5AED:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5AF0:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5AF2:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5AF3:          02                        ;       ELSE goto=0x5AF6
5AF4:             00 9D                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_BANK)

; --------------------------------------------------------------------------------------------------------------------
;
5AF6: B9 75 00                           ; ----- Room 0xB9 RM_4_NORTH_OF_HIGHWAY4, Length: 0x0075, Data: 0x00
;
5AF9:    03 4F                           ;   ---- Section SECTION_03_DESCRIPTION length=0x004F
5AFB:       04 4D                        ;     COM_04_print_command length=0x004D
5AFD:          04 9A 53 BE C3 9E 89 73 B3 75 DB E0 C7 DE 94 14 ; 
5B0D:          4B 5E 96 96 DB 72 F5 59 3E 62 99 16 C2 B3 B8 16 ; 
5B1D:          82 17 4A 5E 7A 79 1B D0 4B F4 96 96 DB 72 95 5A ; 
5B2D:          50 BD 9B 53 6B BF 5F BE F7 17 F3 B9 C7 DE D3 14 ; 
5B3D:          95 96 1B 60 55 45 8E 91 16 8A 80 A1 2E ; 
;
;              NORTH OF HIGHWAY. YOU ARE IN THE DESERT NORTH OF THE
;              HIGHWAY. IN THE DISTANCE TO THE WEST YOU CAN SEE A SMALL
;              TOWN.
;
;
5B4A:    04 21                           ;   ---- Section SECTION_04_COMMANDS length=0x0021
5B4C:       0B 1F 0A                     ;     COM_0B_switch length=0x001F, function=COM_0A_is_input_phrase(phrase_num)
5B4F:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5B50:          09                        ;       ELSE goto=0x5B5A
5B51:             0D 07                  ;         COM_0D_while_pass length=0x0007
5B53:                30 F1               ;           COM_30_set_current_room(room=RM_5_DESERT_SMALL_TRAIL1)
5B55:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5B58:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5B5A:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5B5B:          02                        ;       ELSE goto=0x5B5E
5B5C:             00 B4                  ;         COM_00_move_and_look(room=RM_4_HIGHWAY_EAST)
5B5E:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5B5F:          09                        ;       ELSE goto=0x5B69
5B60:             0D 07                  ;         COM_0D_while_pass length=0x0007
5B62:                30 F0               ;           COM_30_set_current_room(room=RM_5_EMPTY_HIGHWAY_DESERT)
5B64:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5B67:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5B69:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5B6A:          02                        ;       ELSE goto=0x5B6D
5B6B:             00 AC                  ;         COM_00_move_and_look(room=RM_4_EAST_OF_HOTEL)

; --------------------------------------------------------------------------------------------------------------------
;
5B6D: DD 44 00                           ; ----- Room 0xDD RM_4_HALLWAY, Length: 0x0044, Data: 0x00
;
5B70:    03 20                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0020
5B72:       04 1E                        ;     COM_04_print_command length=0x001E
5B74:          4E 72 B3 8E DB E0 C7 DE 94 14 4B 5E 83 96 5A 17 ; 
5B84:          BE A0 10 EE 3C 49 6B A1 4E 72 B3 8E DB E0 ; 
;
;              HALLWAY. YOU ARE IN A SHORT, NARROW HALLWAY. 
;
;
5B92:    04 1F                           ;   ---- Section SECTION_04_COMMANDS length=0x001F
5B94:       0B 1D 0A                     ;     COM_0B_switch length=0x001D, function=COM_0A_is_input_phrase(phrase_num)
5B97:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5B98:          08                        ;       ELSE goto=0x5BA1
5B99:             0E 06                  ;         COM_0E_while_fail length=0x0006
5B9B:                14                  ;           COM_14_execute_and_reverse_status next command
5B9C:                1C 16               ;           COM_1C_set_var_object(obj=OBJ_16_RED_DOOR_HALLWAY)
5B9E:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5B9F:                00 DE               ;           COM_00_move_and_look(room=RM_4_NORTH_ROOM)
5BA1:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5BA2:          08                        ;       ELSE goto=0x5BAB
5BA3:             0E 06                  ;         COM_0E_while_fail length=0x0006
5BA5:                14                  ;           COM_14_execute_and_reverse_status next command
5BA6:                1C 18               ;           COM_1C_set_var_object(obj=OBJ_18_BLUE_DOOR_HALLWAY)
5BA8:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5BA9:                00 DF               ;           COM_00_move_and_look(room=RM_4_SOUTH_ROOM)
5BAB:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5BAC:          02                        ;       ELSE goto=0x5BAF
5BAD:             00 AA                  ;         COM_00_move_and_look(room=RM_4_HOTEL_LOBBY)
5BAF:          55                        ;       COM_0A_is_input_phrase("CLIMB * DOWN *")
5BB0:          02                        ;       ELSE goto=0x5BB3
5BB1:             00 AA                  ;         COM_00_move_and_look(room=RM_4_HOTEL_LOBBY)

; --------------------------------------------------------------------------------------------------------------------
;
5BB3: DE 4E 00                           ; ----- Room 0xDE RM_4_NORTH_ROOM, Length: 0x004E, Data: 0x00
;
5BB6:    03 3C                           ;   ---- Section SECTION_03_DESCRIPTION length=0x003C
5BB8:       04 3A                        ;     COM_04_print_command length=0x003A
5BBA:          04 9A 53 BE 01 B3 DB 95 C7 DE 94 14 4B 5E 83 96 ; 
5BCA:          5F 17 46 48 39 17 FF 9F 82 17 2F 62 D5 15 7B 14 ; 
5BDA:          66 4D 03 EE DA 14 D4 47 03 EE 33 98 55 45 8E 91 ; 
5BEA:          06 8A 75 B1 B4 B7 9F 15 7F B1 ; 
;
;              NORTH ROOM. YOU ARE IN A SMALL ROOM. THERE IS A BED, A
;              CHAIR, AND A SMALL DRESSER HERE.
;
;
5BF4:    04 0D                           ;   ---- Section SECTION_04_COMMANDS length=0x000D
5BF6:       0B 0B 0A                     ;     COM_0B_switch length=0x000B, function=COM_0A_is_input_phrase(phrase_num)
5BF9:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5BFA:          08                        ;       ELSE goto=0x5C03
5BFB:             0E 06                  ;         COM_0E_while_fail length=0x0006
5BFD:                14                  ;           COM_14_execute_and_reverse_status next command
5BFE:                1C 17               ;           COM_1C_set_var_object(obj=OBJ_17_DOOR_NORTH_ROOM)
5C00:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5C01:                00 DD               ;           COM_00_move_and_look(room=RM_4_HALLWAY)

; --------------------------------------------------------------------------------------------------------------------
;
5C03: DF 4E 00                           ; ----- Room 0xDF RM_4_SOUTH_ROOM, Length: 0x004E, Data: 0x00
;
5C06:    03 3C                           ;   ---- Section SECTION_03_DESCRIPTION length=0x003C
5C08:       04 3A                        ;     COM_04_print_command length=0x003A
5C0A:          47 B9 53 BE 01 B3 DB 95 C7 DE 94 14 4B 5E 83 96 ; 
5C1A:          5F 17 46 48 39 17 FF 9F 82 17 2F 62 D5 15 7B 14 ; 
5C2A:          66 4D 03 EE DA 14 D4 47 03 EE 33 98 55 45 8E 91 ; 
5C3A:          06 8A 75 B1 B4 B7 9F 15 7F B1 ; 
;
;              SOUTH ROOM. YOU ARE IN A SMALL ROOM. THERE IS A BED, A
;              CHAIR, AND A SMALL DRESSER HERE.
;
;
5C44:    04 0D                           ;   ---- Section SECTION_04_COMMANDS length=0x000D
5C46:       0B 0B 0A                     ;     COM_0B_switch length=0x000B, function=COM_0A_is_input_phrase(phrase_num)
5C49:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5C4A:          08                        ;       ELSE goto=0x5C53
5C4B:             0E 06                  ;         COM_0E_while_fail length=0x0006
5C4D:                14                  ;           COM_14_execute_and_reverse_status next command
5C4E:                1C 19               ;           COM_1C_set_var_object(obj=OBJ_19_DOOR_SOUTH_ROOM)
5C50:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5C51:                00 DD               ;           COM_00_move_and_look(room=RM_4_HALLWAY)
```

# Unitialized data

```code
5C53: 4C 41 52 47 45 0E 05 53 4D 41 4C 4C 0F 06 4C 49 ; LARGE..SMALL..LI
5C63: 54 54 4C 45 0F 03 54 4F 50 28 06 4D 49 44 44 4C ; TTLE..TOP(.MIDDL
5C73: 45 3C 06 42 4F 54 54 4F 4D 3E 04 46 4C 41 54 22 ; E<.BOTTOM>.FLAT"
5C83: 05 53 50 41 52 45 23 04 42 4C 55 45 0D 06 4D 41 ; .SPARE#.BLUE..MA
5C93: 53 53 49 56 3F 04 42 41 4E 4B 40 06 53 41 4C 4F ; SSIV?.BANK@.SALO
5CA3: 4F 4E 41 06 53 48 45 52 49 46 42 06 4F 46 46 49 ; ONA.SHERIFB.OFFI
5CB3: 43 45 42 06 53 4C 49 4D 27 53 43 05 53 4C 49 4D ; CEB.SLIM'SC.SLIM
5CC3: 53 43 05 42 4F 42 27 53 44 04 42 4F 42 53 44 06 ; SC.BOB'SD.BOBSD.
5CD3: 44 4F 55 42 4C 45 45 05 48 4F 54 45 4C 47 06 53 ; DOUBLEE.HOTELG.S
5CE3: 57 49 4E 47 49 46 04 54 53 4F 4D 6B 04 43 4F 4F ; WINGIF.TSOMk.COO
5CF3: 4C 72 05 43 4C 45 41 52 74 05 42 52 4F 57 
```

