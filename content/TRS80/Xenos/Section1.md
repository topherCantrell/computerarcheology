![Xenos](Xenos.png)

# Xenos SECTION1.DAT

>>> cpu Z80

>>> binary 5200:roms/section1.bin

```code
5200: 00 89 24                           ; List_ID=0x00, length=0x0924

5203: 80 80 DC 00                        ; ----- Room RM_1_HIGHWAY_WEST, Length: 0x00DC, Data: 0x00
;
5207:    03 80 AE                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00AE
520A:       04 80 AB                     ;     COM_04_print_command length=0x00AB
520D:          89 73 B3 75 59 DB 66 62 5B F4 1B A1 2F 49 66 17 ; 
521D:          8E 48 91 7A C0 16 82 17 4A 5E 7A 79 1B D0 0B EE ; 
522D:          96 96 DB 72 95 5A 50 BD 9B 53 6B BF 5F BE 23 15 ; 
523D:          F3 B9 C7 DE D3 14 95 96 1B 60 55 45 8E 91 16 8A ; 
524D:          80 A1 56 F4 F4 72 43 5E 9F A6 3D 49 89 17 AF 14 ; 
525D:          7B 14 15 6C 66 17 83 49 03 A0 03 A0 5F BE 61 17 ; 
526D:          82 C6 5B 17 DB 59 C3 9E 5F BE 39 17 F3 46 B9 46 ; 
527D:          73 C6 4E 72 99 64 3B 4A 76 4D A7 D0 9B 96 1B A1 ; 
528D:          8E 48 82 17 56 5E 80 A1 56 F4 D6 9C DB 72 B5 D0 ; 
529D:          73 C1 5F BE A3 15 31 6D 3B 4A 0C BA 7D 62 F5 72 ; 
52AD:          89 17 82 17 4A 5E B3 A0 00 E5 2E ; 
;
;              HIGHWAY WEST. YOU ARE STANDING ON THE HIGHWAY, IN THE
;              DISTANCE TO THE EAST YOU CAN SEE A SMALL TOWN. THERE
;              APPEARS TO BE A GAS STATION ON THE SOUTH SIDE OF THE ROAD
;              ABOUT HALF WAY BETWEEN YOU AND THE TOWN. TO THE WEST, THE
;              HIGHWAY STRETCHES TO THE HORIZON.
;
;
52B8:    04 28                           ;   ---- Section SECTION_04_COMMANDS length=0x0028
52BA:       0B 26 0A                     ;     COM_0B_switch length=0x0026, function=COM_0A_is_input_phrase(phrase_num)
52BD:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
52BE:          09                        ;       ELSE goto=0x52C8
52BF:             0D 07                  ;         COM_0D_while_pass length=0x0007
52C1:                30 EF               ;           COM_30_set_current_room(room=RM_5_DESERT_EMPTY_HIGHWAY2)
52C3:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
52C6:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
52C8:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
52C9:          09                        ;       ELSE goto=0x52D3
52CA:             0D 07                  ;         COM_0D_while_pass length=0x0007
52CC:                30 EF               ;           COM_30_set_current_room(room=RM_5_DESERT_EMPTY_HIGHWAY2)
52CE:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
52D1:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
52D3:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
52D4:          09                        ;       ELSE goto=0x52DE
52D5:             0D 07                  ;         COM_0D_while_pass length=0x0007
52D7:                30 EF               ;           COM_30_set_current_room(room=RM_5_DESERT_EMPTY_HIGHWAY2)
52D9:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
52DC:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
52DE:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
52DF:          02                        ;       ELSE goto=0x52E2
52E0:             00 81                  ;         COM_00_move_and_look(room=RM_1_WEST_OF_STATION1)

52E2: 81 76 00                           ; ----- Room RM_1_WEST_OF_STATION1, Length: 0x0076, Data: 0x00
;
52E5:    03 5E                           ;   ---- Section SECTION_03_DESCRIPTION length=0x005E
52E7:       04 5C                        ;     COM_04_print_command length=0x005C
52E9:          B5 D0 11 BC 95 64 56 BD C0 7A 5B F4 1B A1 2F 49 ; 
52F9:          C0 16 82 17 54 5E 06 9E F7 17 F3 B9 C3 9E 5F BE ; 
5309:          73 15 D5 B5 56 BD C0 7A 48 F4 FF B2 9F 15 5B B1 ; 
5319:          C7 DE D3 14 95 96 1B 60 4F 45 65 62 77 47 DB 16 ; 
5329:          9E 7A F3 5F 03 A0 5F BE F7 17 F3 B9 0E D0 11 8A ; 
5339:          96 64 DB 72 15 6C 66 17 83 49 27 A0 ; 
;
;              WEST OF STATION. YOU ARE ON THE ROAD WEST OF THE GAS
;              STATION. FROM HERE YOU CAN SEE A MESSAGE PAINTED ON THE
;              WEST WALL OF THE GAS STATION.
;
;
5345:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5347:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
534A:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
534B:          02                        ;       ELSE goto=0x534E
534C:             00 AD                  ;         COM_00_move_and_look(room=RM_1_NORTH_OF_HIGHWAY1)
534E:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
534F:          02                        ;       ELSE goto=0x5352
5350:             00 82                  ;         COM_00_move_and_look(room=RM_1_FRONT_OF_STATION)
5352:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5353:          02                        ;       ELSE goto=0x5356
5354:             00 80                  ;         COM_00_move_and_look(room=RM_1_HIGHWAY_WEST)
5356:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5357:          02                        ;       ELSE goto=0x535A
5358:             00 84                  ;         COM_00_move_and_look(room=RM_1_WEST_OF_STATION2)

535A: 82 80 C0 00                        ; ----- Room RM_1_FRONT_OF_STATION, Length: 0x00C0, Data: 0x00
;
535E:    03 80 A1                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00A1
5361:       04 80 9E                     ;     COM_04_print_command length=0x009E
5364:          79 68 B3 9A C3 9E FB B9 91 BE 1B 9C C7 DE 94 14 ; 
5374:          55 5E 50 BD 90 5A CB 6A 88 96 00 B3 11 BC 96 64 ; 
5384:          DB 72 55 8B 05 BC 50 72 9B 53 15 6C 66 17 83 49 ; 
5394:          27 A0 89 17 82 17 47 5E 66 49 51 18 45 C2 83 48 ; 
53A4:          8D 91 51 5E 73 C6 8E 7A D3 7B 63 5C 04 8A CE C4 ; 
53B4:          90 5A CB 6E 83 7A 89 BF 1B 9C 6B BF 5F BE F7 17 ; 
53C4:          F3 B9 5F BE 39 17 F3 46 95 5A EA 48 94 5F CB B5 ; 
53D4:          C9 9A 7B 14 A7 B7 D0 92 D3 6D 30 15 FF 5A CB B9 ; 
53E4:          F5 59 3E 62 43 F4 09 15 A3 A0 E3 8B 0B 5C 47 B9 ; 
53F4:          53 BE 9E 7A D6 9C DB 72 FB B9 91 BE 1B 9C ; 
;
;              FRONT OF STATION. YOU ARE STANDING IN FRONT OF THE LAST
;              CHANCE GAS STATION. TO THE EAST YOU CAN MAKE OUT INDIVIDUAL
;              BUILDINGS IN TOWN. TO THE WEST THE ROAD DISAPPEARS INTO A
;              SEEMINGLY ENDLESS DESERT. A DOOR LEADS SOUTH INTO THE
;              STATION.
;
;
5402:    04 19                           ;   ---- Section SECTION_04_COMMANDS length=0x0019
5404:       0B 17 0A                     ;     COM_0B_switch length=0x0017, function=COM_0A_is_input_phrase(phrase_num)
5407:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5408:          02                        ;       ELSE goto=0x540B
5409:             00 81                  ;         COM_00_move_and_look(room=RM_1_WEST_OF_STATION1)
540B:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
540C:          08                        ;       ELSE goto=0x5415
540D:             0E 06                  ;         COM_0E_while_fail length=0x0006
540F:                14                  ;           COM_14_execute_and_reverse_status next command
5410:                1C 03               ;           COM_1C_set_var_object(obj=OBJ_03_DOOR_FRONT_OF_STATION)
5412:                8D                  ;           FN_8D_PRINT_OBJECT_IS_CLOSED
5413:                00 83               ;           COM_00_move_and_look(room=RM_1_GAS_STATION)
5415:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5416:          02                        ;       ELSE goto=0x5419
5417:             00 AE                  ;         COM_00_move_and_look(room=RM_1_NORTH_OF_HIGHWAY2)
5419:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
541A:          02                        ;       ELSE goto=0x541D
541B:             00 89                  ;         COM_00_move_and_look(room=RM_1_CITY_LIMIT)

541D: 83 77 00                           ; ----- Room RM_1_GAS_STATION, Length: 0x0077, Data: 0x00
;
5420:    03 65                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0065
5422:       04 63                        ;     COM_04_print_command length=0x0063
5424:          15 6C 66 17 83 49 27 A0 51 18 43 C2 5B B1 09 9A ; 
5434:          66 17 8E 48 91 7A D0 15 82 17 49 5E 4B 49 FB B9 ; 
5444:          91 BE 91 96 93 66 BF 53 82 17 51 5E 93 66 9B 53 ; 
5454:          4B 7B 46 45 3E 7B 4E DB 8E 7B DB 8B 01 B3 59 90 ; 
5464:          82 7B C0 16 FB 8E 0F A0 30 15 EB BF 17 98 43 F4 ; 
5474:          7B 17 7F 4E 4B 15 B5 53 82 17 55 5E 36 A1 19 71 ; 
5484:          46 48 2E                  ; 
;
;              GAS STATION. YOU ARE NOW STANDING IN THE GAS STATION
;              OFFICE. THE OFFICE IS A DIRTY LITTLE ROOM WITH ONLY ONE
;              ENTRANCE. A TABLE FACES THE SOUTH WALL.
;
;
5487:    04 0D                           ;   ---- Section SECTION_04_COMMANDS length=0x000D
5489:       0B 0B 0A                     ;     COM_0B_switch length=0x000B, function=COM_0A_is_input_phrase(phrase_num)
548C:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
548D:          08                        ;       ELSE goto=0x5496
548E:             0E 06                  ;         COM_0E_while_fail length=0x0006
5490:                14                  ;           COM_14_execute_and_reverse_status next command
5491:                1C 02               ;           COM_1C_set_var_object(obj=OBJ_02_DOOR_GAS_STATION)
5493:                8D                  ;           FN_8D_PRINT_OBJECT_IS_CLOSED
5494:                00 82               ;           COM_00_move_and_look(room=RM_1_FRONT_OF_STATION)

5496: 84 80 B7 00                        ; ----- Room RM_1_WEST_OF_STATION2, Length: 0x00B7, Data: 0x00
;
549A:    03 80 9B                        ;   ---- Section SECTION_03_DESCRIPTION length=0x009B
549D:       04 80 98                     ;     COM_04_print_command length=0x0098
54A0:          B5 D0 11 BC 95 64 56 BD C0 7A 5B F4 1B A1 2F 49 ; 
54B0:          96 14 82 17 59 5E 66 62 5B 17 DB 59 C3 9E 5F BE ; 
54C0:          73 15 D5 B5 56 BD C0 7A 56 F4 D6 9C DB 72 04 9A ; 
54D0:          76 BE 61 17 82 C6 03 EE 33 98 B5 D0 1B BC 1B A1 ; 
54E0:          A7 B7 30 15 FF 5A CB B9 15 D0 EE BD 8E 48 4B F4 ; 
54F0:          8E 96 31 49 4E 5E 8E 62 3D 62 B8 16 DA 14 EA 7A ; 
5500:          F3 5F 66 B1 DB 16 9E 7A 82 17 49 5E 4B 49 FB B9 ; 
5510:          91 BE 92 96 07 B3 13 5B FF 14 BB 54 75 B1 FC ED ; 
5520:          55 8B 05 BC 50 72 BE 53 8F 16 33 D9 15 6C 5B 17 ; 
5530:          53 D9 6B 16 F5 8B 63 F4   ; 
;
;              WEST OF STATION. YOU ARE AT THE WEST SIDE OF THE GAS
;              STATION. TO THE NORTH, SOUTH, AND WEST YOU SEE ENDLESS
;              WASTELAND. IN LARGE LETTERS OF CHIPPED RED PAINT THE GAS
;              STATION PROUDLY DECLARES, "LAST CHANCE, NEXT GAS SIXTY
;              MILES."
;
;
5538:    04 16                           ;   ---- Section SECTION_04_COMMANDS length=0x0016
553A:       0B 14 0A                     ;     COM_0B_switch length=0x0014, function=COM_0A_is_input_phrase(phrase_num)
553D:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
553E:          02                        ;       ELSE goto=0x5541
553F:             00 81                  ;         COM_00_move_and_look(room=RM_1_WEST_OF_STATION1)
5541:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5542:          09                        ;       ELSE goto=0x554C
5543:             0D 07                  ;         COM_0D_while_pass length=0x0007
5545:                30 EF               ;           COM_30_set_current_room(room=RM_5_DESERT_EMPTY_HIGHWAY2)
5547:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
554A:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
554C:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
554D:          02                        ;       ELSE goto=0x5550
554E:             00 85                  ;         COM_00_move_and_look(room=RM_1_SOUTHWEST_OF_STATION)

5550: 85 80 85 00                        ; ----- Room RM_1_SOUTHWEST_OF_STATION, Length: 0x0085, Data: 0x00
;
5554:    03 66                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0066
5556:       04 64                        ;     COM_04_print_command length=0x0064
5558:          47 B9 71 BE 66 62 B8 16 66 17 83 49 27 A0 51 18 ; 
5568:          43 C2 5B B1 09 9A 66 17 8E 48 91 7A 61 17 82 C6 ; 
5578:          B8 16 82 17 4E 5E 66 49 DA 14 8D 48 49 5E 4B 49 ; 
5588:          FB B9 91 BE 1B 9C 6B BF 5F BE 23 15 F3 B9 6A 4D ; 
5598:          8E 7A 82 17 55 5E 56 BD C0 7A 82 17 2F 62 92 14 ; 
55A8:          E3 A4 8B B3 6B BF 5B 4D 55 45 8E 91 0C 8A 95 C5 ; 
55B8:          43 18 57 B1               ; 
;
;              SOUTHWEST OF STATION. YOU ARE NOW STANDING SOUTH OF THE
;              LAST CHANCE GAS STATION. TO THE EAST BEHIND THE STATION
;              THERE APPEARS TO BE A SMALL JUNK YARD.
;
;
55BC:    04 1A                           ;   ---- Section SECTION_04_COMMANDS length=0x001A
55BE:       0B 18 0A                     ;     COM_0B_switch length=0x0018, function=COM_0A_is_input_phrase(phrase_num)
55C1:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
55C2:          02                        ;       ELSE goto=0x55C5
55C3:             00 84                  ;         COM_00_move_and_look(room=RM_1_WEST_OF_STATION2)
55C5:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
55C6:          09                        ;       ELSE goto=0x55D0
55C7:             0D 07                  ;         COM_0D_while_pass length=0x0007
55C9:                30 E0               ;           COM_30_set_current_room(room=RM_5_DESERT21)
55CB:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
55CE:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
55D0:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
55D1:          02                        ;       ELSE goto=0x55D4
55D2:             00 86                  ;         COM_00_move_and_look(room=RM_1_JUNKYARD)
55D4:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
55D5:          02                        ;       ELSE goto=0x55D8
55D6:             00 B0                  ;         COM_00_move_and_look(room=RM_1_DESERT_SOUTH1)

55D8: 86 41 00                           ; ----- Room RM_1_JUNKYARD, Length: 0x0041, Data: 0x00
;
55DB:    03 2D                           ;   ---- Section SECTION_03_DESCRIPTION length=0x002D
55DD:       04 2B                        ;     COM_04_print_command length=0x002B
55DF:          F0 81 C3 88 57 B1 51 18 50 C2 6B A1 FB B9 33 98 ; 
55EF:          83 7A 4C 45 95 C5 43 18 33 B1 47 B9 53 BE C3 9E ; 
55FF:          5F BE 73 15 D5 B5 56 BD C0 7A 2E ; 
;
;              JUNKYARD. YOU NOW STAND IN A JUNK YARD SOUTH OF THE GAS
;              STATION.
;
;
560A:    04 0F                           ;   ---- Section SECTION_04_COMMANDS length=0x000F
560C:       0B 0D 0A                     ;     COM_0B_switch length=0x000D, function=COM_0A_is_input_phrase(phrase_num)
560F:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5610:          02                        ;       ELSE goto=0x5613
5611:             00 87                  ;         COM_00_move_and_look(room=RM_1_SOUTHEAST_OF_STATION)
5613:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5614:          02                        ;       ELSE goto=0x5617
5615:             00 85                  ;         COM_00_move_and_look(room=RM_1_SOUTHWEST_OF_STATION)
5617:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5618:          02                        ;       ELSE goto=0x561B
5619:             00 B0                  ;         COM_00_move_and_look(room=RM_1_DESERT_SOUTH1)

561B: 87 7A 00                           ; ----- Room RM_1_SOUTHEAST_OF_STATION, Length: 0x007A, Data: 0x00
;
561E:    03 62                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0062
5620:       04 60                        ;     COM_04_print_command length=0x0060
5622:          47 B9 5F BE 66 49 B8 16 66 17 83 49 27 A0 51 18 ; 
5632:          43 C2 5B B1 09 9A 66 17 8E 48 91 7A 61 17 82 C6 ; 
5642:          95 5F 11 BC 96 64 DB 72 55 8B 05 BC 50 72 9B 53 ; 
5652:          15 6C 66 17 83 49 27 A0 89 17 82 17 59 5E 66 62 ; 
5662:          AF 14 90 73 16 58 DB 72 FB B9 91 BE 96 96 F4 72 ; 
5672:          4B 5E C3 B5 5F 17 46 48 FF 15 4B 99 94 DC 9B 5D ; 
;
;              SOUTHEAST OF STATION. YOU ARE NOW STANDING SOUTHEAST OF THE
;              LAST CHANCE GAS STATION. TO THE WEST BEHIND THE STATION
;              THERE IS A SMALL JUNK YARD.
;
;
5682:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5684:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5687:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5688:          02                        ;       ELSE goto=0x568B
5689:             00 8C                  ;         COM_00_move_and_look(room=RM_1_SOUTHWEST_OF_SHERIFF)
568B:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
568C:          02                        ;       ELSE goto=0x568F
568D:             00 86                  ;         COM_00_move_and_look(room=RM_1_JUNKYARD)
568F:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5690:          02                        ;       ELSE goto=0x5693
5691:             00 88                  ;         COM_00_move_and_look(room=RM_1_EAST_OF_STATION)
5693:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5694:          02                        ;       ELSE goto=0x5697
5695:             00 B0                  ;         COM_00_move_and_look(room=RM_1_DESERT_SOUTH1)

5697: 88 80 84 00                        ; ----- Room RM_1_EAST_OF_STATION, Length: 0x0084, Data: 0x00
;
569B:    03 62                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0062
569D:       04 60                        ;     COM_04_print_command length=0x0060
569F:          95 5F 11 BC 95 64 56 BD C0 7A 5B F4 1B A1 2F 49 ; 
56AF:          96 14 82 17 47 5E 66 49 5B 17 DB 59 C3 9E 5F BE ; 
56BF:          73 15 D5 B5 56 BD C0 7A 56 F4 F4 72 4B 5E C3 B5 ; 
56CF:          09 15 A3 A0 F4 72 59 5E 85 73 03 71 11 BC 5B 98 ; 
56DF:          8F BE 4A 5E F3 46 3F B9 82 62 91 7A 04 18 8E 7B ; 
56EF:          83 61 03 A0 73 7B 56 D1 14 71 F3 5F 4B A4 D7 9A ; 
;
;              EAST OF STATION. YOU ARE AT THE EAST SIDE OF THE GAS
;              STATION. THERE IS A DOOR HERE WHICH AT ONE TIME HAD
;              SOMETHING WRITTEN ON IT WITH RED PAINT.
;
;
56FF:    04 1D                           ;   ---- Section SECTION_04_COMMANDS length=0x001D
5701:       0B 1B 0A                     ;     COM_0B_switch length=0x001B, function=COM_0A_is_input_phrase(phrase_num)
5704:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5705:          02                        ;       ELSE goto=0x5708
5706:             00 89                  ;         COM_00_move_and_look(room=RM_1_CITY_LIMIT)
5708:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5709:          06                        ;       ELSE goto=0x5710
570A:             0D 04                  ;         COM_0D_while_pass length=0x0004
570C:                30 8B               ;           COM_30_set_current_room(room=RM_2_WEST_OF_SHERIFF)
570E:                2F 02               ;           COM_2F_load_section_from_disk(section=2)
5710:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5711:          08                        ;       ELSE goto=0x571A
5712:             0E 06                  ;         COM_0E_while_fail length=0x0006
5714:                14                  ;           COM_14_execute_and_reverse_status next command
5715:                1C 04               ;           COM_1C_set_var_object(obj=OBJ_04_DOOR_EAST_OF_STATION)
5717:                8D                  ;           FN_8D_PRINT_OBJECT_IS_CLOSED
5718:                00 DA               ;           COM_00_move_and_look(room=RM_1_RESTROOM)
571A:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
571B:          02                        ;       ELSE goto=0x571E
571C:             00 87                  ;         COM_00_move_and_look(room=RM_1_SOUTHEAST_OF_STATION)

571E: 89 6D 00                           ; ----- Room RM_1_CITY_LIMIT, Length: 0x006D, Data: 0x00
;
5721:    03 51                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0051
5723:       04 4F                        ;     COM_04_print_command length=0x004F
5725:          56 54 4E DB 6B 7A 9B C1 C7 DE 94 14 51 5E 96 96 ; 
5735:          DB 72 F3 B2 07 58 66 49 B8 16 82 17 49 5E 4B 49 ; 
5745:          FB B9 91 BE 1B 9C C7 DE D3 14 95 96 1B 60 55 45 ; 
5755:          8E 91 15 8A 80 79 89 17 82 17 47 5E 66 49 0B EE ; 
5765:          14 BC 86 5F 33 BB 1B 1B FB C0 8F 8C 97 7B 22 ; 
;
;              CITY LIMIT. YOU ARE ON THE ROAD EAST OF THE GAS STATION.
;              YOU CAN SEE A SMALL SIGN TO THE EAST, IT READS, "CITY
;              LIMIT."
;
;
5774:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5776:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
5779:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
577A:          02                        ;       ELSE goto=0x577D
577B:             00 82                  ;         COM_00_move_and_look(room=RM_1_FRONT_OF_STATION)
577D:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
577E:          06                        ;       ELSE goto=0x5785
577F:             0D 04                  ;         COM_0D_while_pass length=0x0004
5781:                30 8A               ;           COM_30_set_current_room(room=RM_2_WEST_OF_TOWN)
5783:                2F 02               ;           COM_2F_load_section_from_disk(section=2)
5785:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5786:          02                        ;       ELSE goto=0x5789
5787:             00 88                  ;         COM_00_move_and_look(room=RM_1_EAST_OF_STATION)
5789:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
578A:          02                        ;       ELSE goto=0x578D
578B:             00 AF                  ;         COM_00_move_and_look(room=RM_1_NORTH_OF_HIGHWAY3)

578D: 8C 80 C7 00                        ; ----- Room RM_1_SOUTHWEST_OF_SHERIFF, Length: 0x00C7, Data: 0x00
;
5791:    03 80 A6                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00A6
5794:       04 80 A3                     ;     COM_04_print_command length=0x00A3
5797:          47 B9 71 BE 66 62 B8 16 5A 17 33 62 A7 66 51 18 ; 
57A7:          43 C2 5B B1 FB B9 43 98 AB 98 73 49 5F BE 61 17 ; 
57B7:          82 C6 B5 D0 05 BC B8 A0 23 62 C3 9E 5F BE 5A 17 ; 
57C7:          33 62 85 66 D1 B5 93 66 BF 53 89 17 82 17 47 5E ; 
57D7:          66 49 51 18 45 C2 83 48 A7 B7 82 17 44 5E DD 46 ; 
57E7:          D1 B5 96 64 DB 72 EB 4F C3 8B C5 98 82 17 73 49 ; 
57F7:          90 8C 56 5E DB 72 47 B9 53 BE 46 B8 51 5E 96 64 ; 
5807:          DB 72 89 73 B3 75 DB E0 6B BF 5F BE F7 17 F3 B9 ; 
5817:          C7 DE D3 14 95 96 1B 60 44 45 CE C4 90 5A D5 6A ; 
5827:          50 BD 90 5A C3 6A 80 8D 4B 5E 96 96 DB 72 F5 59 ; 
5837:          3E 62 2E                  ; 
;
;              SOUTHWEST OF SHERIFF. YOU ARE STANDING AT THE SOUTHWEST
;              CORNER OF THE SHERIFF'S OFFICE. TO THE EAST YOU CAN SEE THE
;              BACKS OF THE BUILDINGS THAT LINE THE SOUTH SIDE OF THE
;              HIGHWAY. TO THE WEST YOU CAN SEE A BUILDING STANDING ALONE
;              IN THE DESERT.
;
;
583A:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B
583C:       0B 19 0A                     ;     COM_0B_switch length=0x0019, function=COM_0A_is_input_phrase(phrase_num)
583F:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5840:          06                        ;       ELSE goto=0x5847
5841:             0D 04                  ;         COM_0D_while_pass length=0x0004
5843:                30 8F               ;           COM_30_set_current_room(room=RM_2_SOUTH_OF_SHERIFF)
5845:                2F 02               ;           COM_2F_load_section_from_disk(section=2)
5847:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5848:          02                        ;       ELSE goto=0x584B
5849:             00 87                  ;         COM_00_move_and_look(room=RM_1_SOUTHEAST_OF_STATION)
584B:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
584C:          02                        ;       ELSE goto=0x584F
584D:             00 B0                  ;         COM_00_move_and_look(room=RM_1_DESERT_SOUTH1)
584F:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5850:          06                        ;       ELSE goto=0x5857
5851:             0D 04                  ;         COM_0D_while_pass length=0x0004
5853:                30 8B               ;           COM_30_set_current_room(room=RM_2_WEST_OF_SHERIFF)
5855:                2F 02               ;           COM_2F_load_section_from_disk(section=2)

5857: AD 80 9A 00                        ; ----- Room RM_1_NORTH_OF_HIGHWAY1, Length: 0x009A, Data: 0x00
;
585B:    03 74                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0074
585D:       04 72                        ;     COM_04_print_command length=0x0072
585F:          04 9A 53 BE C3 9E 89 73 B3 75 DB E0 C7 DE 94 14 ; 
586F:          4B 5E 96 96 DB 72 F5 59 3E 62 99 16 C2 B3 B8 16 ; 
587F:          82 17 4A 5E 7A 79 1B D0 56 F4 D6 9C DB 72 47 B9 ; 
588F:          5F BE 66 49 51 18 45 C2 83 48 A7 B7 FA 17 73 49 ; 
589F:          EA 48 94 5F D6 B5 C4 9C 43 5E 73 15 D5 B5 56 BD ; 
58AF:          C0 7A 48 F4 23 49 6B BF 5F BE 23 15 F3 B9 C7 DE ; 
58BF:          D3 14 95 96 1B 60 B8 B7 2B 62 04 8A CE C4 90 5A ; 
58CF:          EF 6E                     ; 
;
;              NORTH OF HIGHWAY. YOU ARE IN THE DESERT NORTH OF THE
;              HIGHWAY. TO THE SOUTHEAST YOU CAN SEE WHAT APPEARS TO BE A
;              GAS STATION. FAR TO THE EAST YOU CAN SEE SEVERAL BUILDINGS.
;
;
58D1:    04 21                           ;   ---- Section SECTION_04_COMMANDS length=0x0021
58D3:       0B 1F 0A                     ;     COM_0B_switch length=0x001F, function=COM_0A_is_input_phrase(phrase_num)
58D6:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
58D7:          02                        ;       ELSE goto=0x58DA
58D8:             00 81                  ;         COM_00_move_and_look(room=RM_1_WEST_OF_STATION1)
58DA:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
58DB:          09                        ;       ELSE goto=0x58E5
58DC:             0D 07                  ;         COM_0D_while_pass length=0x0007
58DE:                30 F5               ;           COM_30_set_current_room(room=RM_5_DESERT27)
58E0:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
58E3:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
58E5:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
58E6:          09                        ;       ELSE goto=0x58F0
58E7:             0D 07                  ;         COM_0D_while_pass length=0x0007
58E9:                30 EF               ;           COM_30_set_current_room(room=RM_5_DESERT_EMPTY_HIGHWAY2)
58EB:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
58EE:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
58F0:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
58F1:          02                        ;       ELSE goto=0x58F4
58F2:             00 AE                  ;         COM_00_move_and_look(room=RM_1_NORTH_OF_HIGHWAY2)

58F4: AE 80 89 00                        ; ----- Room RM_1_NORTH_OF_HIGHWAY2, Length: 0x0089, Data: 0x00
;
58F8:    03 6A                           ;   ---- Section SECTION_03_DESCRIPTION length=0x006A
58FA:       04 68                        ;     COM_04_print_command length=0x0068
58FC:          04 9A 53 BE C3 9E 89 73 B3 75 DB E0 C7 DE 94 14 ; 
590C:          4B 5E 96 96 DB 72 F5 59 3E 62 99 16 C2 B3 B8 16 ; 
591C:          82 17 4A 5E 7A 79 1B D0 56 F4 D6 9C DB 72 47 B9 ; 
592C:          53 BE C7 DE D3 14 95 96 1B 60 5F BE 76 13 66 49 ; 
593C:          DA 14 8D 48 49 5E 4B 49 FB B9 91 BE 1C 9C 89 17 ; 
594C:          82 17 47 5E 66 49 51 18 45 C2 83 48 A7 B7 7B 14 ; 
595C:          E3 B8 F3 8C 89 BF 1B 9C   ; 
;
;              NORTH OF HIGHWAY. YOU ARE IN THE DESERT NORTH OF THE
;              HIGHWAY. TO THE SOUTH YOU CAN SEE THE "LAST CHANCE GAS
;              STATION." TO THE EAST YOU CAN SEE A SMALL TOWN.
;
;
5964:    04 1A                           ;   ---- Section SECTION_04_COMMANDS length=0x001A
5966:       0B 18 0A                     ;     COM_0B_switch length=0x0018, function=COM_0A_is_input_phrase(phrase_num)
5969:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
596A:          09                        ;       ELSE goto=0x5974
596B:             0D 07                  ;         COM_0D_while_pass length=0x0007
596D:                30 F5               ;           COM_30_set_current_room(room=RM_5_DESERT27)
596F:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5972:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5974:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5975:          02                        ;       ELSE goto=0x5978
5976:             00 82                  ;         COM_00_move_and_look(room=RM_1_FRONT_OF_STATION)
5978:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5979:          02                        ;       ELSE goto=0x597C
597A:             00 AF                  ;         COM_00_move_and_look(room=RM_1_NORTH_OF_HIGHWAY3)
597C:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
597D:          02                        ;       ELSE goto=0x5980
597E:             00 AD                  ;         COM_00_move_and_look(room=RM_1_NORTH_OF_HIGHWAY1)

5980: AF 80 B7 00                        ; ----- Room RM_1_NORTH_OF_HIGHWAY3, Length: 0x00B7, Data: 0x00
;
5984:    03 80 93                        ;   ---- Section SECTION_03_DESCRIPTION length=0x0093
5987:       04 80 90                     ;     COM_04_print_command length=0x0090
598A:          04 9A 53 BE C3 9E 89 73 B3 75 DB E0 C7 DE 94 14 ; 
599A:          4B 5E 96 96 DB 72 F5 59 3E 62 99 16 C2 B3 B8 16 ; 
59AA:          82 17 4A 5E 7A 79 1B D0 56 F4 D6 9C DB 72 47 B9 ; 
59BA:          71 BE 66 62 51 18 45 C2 83 48 A7 B7 7B 14 15 6C ; 
59CA:          66 17 83 49 27 A0 89 17 82 17 47 5E 66 49 51 18 ; 
59DA:          45 C2 83 48 A7 B7 7B 14 54 8B 9B 6C 41 D2 F0 59 ; 
59EA:          BF 14 3E 7A 91 7A 56 F4 D6 9C DB 72 47 B9 5F BE ; 
59FA:          66 49 C2 16 85 A6 7F 7B D6 15 51 18 45 C2 83 48 ; 
5A0A:          A7 B7 90 14 86 14 2F 9E 66 17 E5 B3 74 C0 DB 63 ; 
;
;              NORTH OF HIGHWAY. YOU ARE IN THE DESERT NORTH OF THE
;              HIGHWAY. TO THE SOUTHWEST YOU CAN SEE A GAS STATION. TO THE
;              EAST YOU CAN SEE A LARGE WOODEN BUILDING. TO THE SOUTHEAST
;              OPPOSITE IT YOU CAN SEE AN ADOBE STRUCTURE.
;
;
5A1A:    04 1E                           ;   ---- Section SECTION_04_COMMANDS length=0x001E
5A1C:       0B 1C 0A                     ;     COM_0B_switch length=0x001C, function=COM_0A_is_input_phrase(phrase_num)
5A1F:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5A20:          09                        ;       ELSE goto=0x5A2A
5A21:             0D 07                  ;         COM_0D_while_pass length=0x0007
5A23:                30 F5               ;           COM_30_set_current_room(room=RM_5_DESERT27)
5A25:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5A28:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5A2A:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5A2B:          02                        ;       ELSE goto=0x5A2E
5A2C:             00 89                  ;         COM_00_move_and_look(room=RM_1_CITY_LIMIT)
5A2E:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5A2F:          06                        ;       ELSE goto=0x5A36
5A30:             0D 04                  ;         COM_0D_while_pass length=0x0004
5A32:                30 A0               ;           COM_30_set_current_room(room=RM_2_WEST_SIDE_OF_SALOON)
5A34:                2F 02               ;           COM_2F_load_section_from_disk(section=2)
5A36:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5A37:          02                        ;       ELSE goto=0x5A3A
5A38:             00 AE                  ;         COM_00_move_and_look(room=RM_1_NORTH_OF_HIGHWAY2)

5A3A: B0 79 00                           ; ----- Room RM_1_DESERT_SOUTH1, Length: 0x0079, Data: 0x00
;
5A3D:    03 52                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0052
5A3F:       04 50                        ;     COM_04_print_command length=0x0050
5A41:          F5 59 3E 62 61 17 82 C6 5B F4 1B A1 2F 49 D0 15 ; 
5A51:          82 17 46 5E 57 62 B3 B3 47 B9 53 BE C3 9E 5F BE ; 
5A61:          73 15 D5 B5 56 BD C0 7A 4B F4 96 96 DB 72 95 5A ; 
5A71:          50 BD 9B 53 6B BF 5F BE 99 16 C2 B3 95 5F 1B BC ; 
5A81:          1B A1 10 53 57 17 43 5E 5F 17 46 48 89 17 27 D2 ; 
;
;              DESERT SOUTH. YOU ARE IN THE DESERT SOUTH OF THE GAS
;              STATION. IN THE DISTANCE TO THE NORTHEAST YOU CAN SEE A
;              SMALL TOWN.
;
;
5A91:    04 22                           ;   ---- Section SECTION_04_COMMANDS length=0x0022
5A93:       0B 20 0A                     ;     COM_0B_switch length=0x0020, function=COM_0A_is_input_phrase(phrase_num)
5A96:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5A97:          02                        ;       ELSE goto=0x5A9A
5A98:             00 87                  ;         COM_00_move_and_look(room=RM_1_SOUTHEAST_OF_STATION)
5A9A:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5A9B:          06                        ;       ELSE goto=0x5AA2
5A9C:             0D 04                  ;         COM_0D_while_pass length=0x0004
5A9E:                30 B3               ;           COM_30_set_current_room(room=RM_3_DESERT)
5AA0:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
5AA2:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5AA3:          09                        ;       ELSE goto=0x5AAD
5AA4:             0D 07                  ;         COM_0D_while_pass length=0x0007
5AA6:                30 E0               ;           COM_30_set_current_room(room=RM_5_DESERT21)
5AA8:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5AAB:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5AAD:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5AAE:          06                        ;       ELSE goto=0x5AB5
5AAF:             0D 04                  ;         COM_0D_while_pass length=0x0004
5AB1:                30 B1               ;           COM_30_set_current_room(room=RM_3_DESERT_SOUTH2)
5AB3:                2F 03               ;           COM_2F_load_section_from_disk(section=3)

5AB5: DA 70 00                           ; ----- Room RM_1_RESTROOM, Length: 0x0070, Data: 0x00
;
5AB8:    03 5E                           ;   ---- Section SECTION_03_DESCRIPTION length=0x005E
5ABA:       04 5C                        ;     COM_04_print_command length=0x005C
5ABC:          75 B1 F9 BF FF 9F 51 18 43 C2 5B B1 09 9A 66 17 ; 
5ACC:          8E 48 91 7A D0 15 7B 14 E3 B8 F3 8C 75 B1 F9 BF ; 
5ADC:          FF 9F 82 17 2F 62 D5 15 7B 14 49 B8 91 96 91 96 ; 
5AEC:          5B 98 0E D0 16 8A 56 72 2F 17 0D 47 FC ED 1F D1 ; 
5AFC:          9B 96 1B A1 2F 49 82 17 07 B3 36 6D E6 16 95 5F ; 
5B0C:          54 5E 8F 62 C3 B2 5F BE 17 16 DC E0 ; 
;
;              RESTROOM. YOU ARE NOW STANDING IN A SMALL RESTROOM. THERE
;              IS A SIGN ON ONE WALL THAT READS, "WHEN YOU ARE THROUGH,
;              PLEASE RETURN THE KEY."
;
;
5B18:    04 0D                           ;   ---- Section SECTION_04_COMMANDS length=0x000D
5B1A:       0B 0B 0A                     ;     COM_0B_switch length=0x000B, function=COM_0A_is_input_phrase(phrase_num)
5B1D:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5B1E:          08                        ;       ELSE goto=0x5B27
5B1F:             0E 06                  ;         COM_0E_while_fail length=0x0006
5B21:                14                  ;           COM_14_execute_and_reverse_status next command
5B22:                1C 05               ;           COM_1C_set_var_object(obj=OBJ_05_DOOR_RESTROOM)
5B24:                8D                  ;           FN_8D_PRINT_OBJECT_IS_CLOSED
5B25:                00 88               ;           COM_00_move_and_look(room=RM_1_EAST_OF_STATION)
```

# Unitialized data

```code
5B27: 56 06 57 49 4E 44 4F 57 59 06 53 48 45 4C 54 45  ; V.WINDOWY.SHELTE
5B37: 5A 05 41 4C 49 45 4E 5B 06 43 52 45 41 54 55 5B  ; Z.ALIEN[.CREATU[
5B47: 04 41 4E 54 53 5B 03 41 4E 54 5B 04 43 55 42 45  ; .ANTS[.ANT[.CUBE
5B57: 5C 06 50 49 43 54 55 52 5D 06 43 59 4C 49 4E 44  ; \.PICTUR].CYLIND
5B67: 5E 05 47 4C 4F 42 45 5E 06 47 4C 4F 42 45 53 5E  ; ^.GLOBE^.GLOBES^
5B77: 06 4C 49 47 48 54 53 5F 06 43 4F 4E 53 4F 4C 62  ; .LIGHTS_.CONSOLb
5B87: 05 50 41 4E 45 4C 62 06 53 43 52 45 45 4E 63 05  ; .PANELb.SCREENc.
5B97: 45 41 52 54 48 64 04 4D 4F 4F 4E 65 04 53 48 49  ; EARTHd.MOONe.SHI
5BA7: 50 66 06 48 41 4E 44 47 52 67 06 48 41 4E 44 4C  ; Pf.HANDGRg.HANDL
5BB7: 45 67 04 56 49 41 4C 68 06 50 45 44 45 53 54 69  ; Eg.VIALh.PEDESTi
5BC7: 03 52 4F 44 6E 06 4D 41 43 48 49 4E 6F 06 50 52  ; .RODn.MACHINo.PR
5BD7: 4F 53 50 45 70 06 47 4F 4F 4C 55 42 71 00 04 47  ; OSPEp.GOOLUBq..G
5BE7: 52 45 59 6C 04 47 52 41 59 6C 04 49 4E 43 48 6D  ; REYl.GRAYl.INCHm
5BF7: 06 4D 41 52 4F 4F 4E 61 05 57 48 49 54 45 60 05  ; .MAROONa.WHITE..
5C07: 47 52 45 45 4E 6A 06 59 45 4C 4C 4F 57 48 06 4F  ; GREENj.YELLOWH.O
5C17: 52 41 4E 47 45 49 03 52 45 44 13 06 4D 41 53 54  ; RANGEI.RED..MAST
5C27: 45 52 14 05 42 52 41 53 53 15 06 53 45 43 52 45  ; ER..BRASS..SECRE
5C37: 54 3D 06 53 4B 45 4C 45 54 17 05 53 54 45 45 4C  ; T=.SKELET..STEEL
5C47: 18 03 43 41 42 4B 03 42 49 47 0E 05 4C 41 52 47  ; ..CABK.BIG..LARG
5C57: 45 0E 05 53 4D 41 4C 4C 0F 06 4C 49 54 54 4C 45  ; E..SMALL..LITTLE
5C67: 0F 03 54 4F 50 28 06 4D 49 44 44 4C 45 3C 06 42  ; ..TOP(.MIDDLE<.B
5C77: 4F 54 54 4F 4D 3E 04 46 4C 41 54 22 05 53 50 41  ; OTTOM>.FLAT".SPA
5C87: 52 45 23 04 42 4C 55 45 0D 06 4D 41 53 53 49 56  ; RE#.BLUE..MASSIV
5C97: 3F 04 42 41 4E 4B 40 06 53 41 4C 4F 4F 4E 41 06  ; ?.BANK@.SALOONA.
5CA7: 53 48 45 52 49 46 42 06 4F 46 46 49 43 45 42 06  ; SHERIFB.OFFICEB.
5CB7: 53 4C 49 4D 27 53 43 05 53 4C 49 4D 53 43 05 42  ; SLIM'SC.SLIMSC.B
5CC7: 4F 42 27 53 44 04 42 4F 42 53 44 06 44 4F 55 42  ; OB'SD.BOBSD.DOUB
5CD7: 4C 45 45 05 48 4F 54 45 4C 47 06 53 57 49 4E 47  ; LEE.HOTELG.SWING
5CE7: 49 46 04 54 53 4F 4D 6B 04 43 4F 4F 4C 72 05 43  ; IF.TSOMk.COOLr.C
5CF7: 4C 45 41 52 74 05 42 52 4F 57 
```

