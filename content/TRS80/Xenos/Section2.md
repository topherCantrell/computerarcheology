![Xenos](Xenos.png)

# Xenos SECTION2.DAT

>>> cpu Z80

>>> binary 5200:roms/section2.bin

```code
5200: 00 8A 1D                           ; List_ID=0x00, length=0x0A1D

; --------------------------------------------------------------------------------------------------------------------
;
5203: 8A 81 48 00                        ; ----- Room 0x8A RM_2_WEST_OF_TOWN, Length: 0x0148, Data: 0x00
;
5207:    03 81 2B                        ;   ---- Section SECTION_03_DESCRIPTION length=0x012B
520A:       04 81 28                     ;     COM_04_print_command length=0x0128
520D:          B5 D0 11 BC 96 64 80 A1 5B F4 1B A1 2F 49 C0 16 ; 
521D:          82 17 54 5E 06 9E 96 14 82 17 45 5E 93 7B 43 16 ; 
522D:          D6 92 D9 B5 66 62 B8 16 89 17 27 D2 89 17 82 17 ; 
523D:          59 5E 66 62 51 18 45 C2 83 48 A7 B7 7B 14 15 6C ; 
524D:          66 17 83 49 03 A0 F5 81 15 BC 36 A1 11 71 96 64 ; 
525D:          DB 72 89 73 B3 75 DB E0 6B BF 5F BE 23 15 F3 B9 ; 
526D:          C7 DE D3 14 94 96 86 5F 82 17 55 5E 80 79 D1 B5 ; 
527D:          95 96 E7 9F B8 16 82 17 44 5E CE C4 90 5A CB 6E ; 
528D:          83 7A 89 BF 1B 9C 5F BE BF 14 3E 7A 91 7A C0 16 ; 
529D:          82 17 55 5E 36 A1 15 71 FF 78 B8 16 82 17 55 5E ; 
52AD:          EF BF 73 62 4B 7B 83 48 09 47 5B 4D 0C BA E6 C3 ; 
52BD:          2F C6 FB 17 53 BE D4 4C CB B5 96 96 DB 72 50 D1 ; 
52CD:          89 5B 33 BB 5F BE 5B 17 03 6E 36 A1 5C 15 1E A0 ; 
52DD:          2F 17 0D 47 FC ED 1F B8 08 B2 1C 6A 82 17 44 5E ; 
52ED:          CE C4 90 5A D1 6A 96 96 DB 72 04 9A 53 BE 46 B8 ; 
52FD:          51 5E 96 64 DB 72 0C BA 36 60 9B 15 C3 B5 5F 17 ; 
530D:          46 48 8F 16 03 A0 49 B8 91 96 8D C6 FF 78 82 17 ; 
531D:          73 49 63 B1 2E 5C 72 13 40 49 3D 63 C4 B5 23 49 ; 
532D:          8E 48 84 15 46 7A 63 F4   ; 
;
;              WEST OF TOWN. YOU ARE ON THE ROAD AT THE CITY LIMITS WEST
;              OF TOWN. TO THE WEST YOU CAN SEE A GAS STATION JUST SOUTH
;              OF THE HIGHWAY. TO THE EAST YOU CAN READ THE SIGNS ON SOME
;              OF THE BUILDINGS IN TOWN. THE BUILDING ON THE SOUTH SIDE OF
;              THE STREET IS AN ADOBE STRUCTURE WITH BARS IN THE WINDOWS,
;              THE SIGN OUT FRONT READS, "SHERIFF." THE BUILDING ON THE
;              NORTH SIDE OF THE STREET HAS A SMALL NEON SIGN OUTSIDE THAT
;              READS, "HARVEY'S BAR AND GRILL."
;
;
5335:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5337:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
533A:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
533B:          06                        ;       ELSE goto=0x5342
533C:             0D 04                  ;         COM_0D_while_pass length=0x0004
533E:                30 89               ;           COM_30_set_current_room(room=RM_1_CITY_LIMIT)
5340:                2F 01               ;           COM_2F_load_section_from_disk(section=1)
5342:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5343:          02                        ;       ELSE goto=0x5346
5344:             00 8D                  ;         COM_00_move_and_look(room=RM_2_MAIN_STREET_WEST)
5346:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5347:          02                        ;       ELSE goto=0x534A
5348:             00 A0                  ;         COM_00_move_and_look(room=RM_2_WEST_SIDE_OF_SALOON)
534A:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
534B:          02                        ;       ELSE goto=0x534E
534C:             00 8B                  ;         COM_00_move_and_look(room=RM_2_WEST_OF_SHERIFF)

; --------------------------------------------------------------------------------------------------------------------
;
534E: 8B 80 C2 00                        ; ----- Room 0x8B RM_2_WEST_OF_SHERIFF, Length: 0x00C2, Data: 0x00
;
5352:    03 80 A5                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00A5
5355:       04 80 A2                     ;     COM_04_print_command length=0x00A2
5358:          B5 D0 11 BC 95 64 F4 72 50 79 5B F4 1B A1 2F 49 ; 
5368:          66 17 8E 48 91 7A 96 14 82 17 59 5E 66 62 5B 17 ; 
5378:          DB 59 C3 9E 5F BE 5A 17 33 62 85 66 D1 B5 93 66 ; 
5388:          BF 53 89 17 82 17 50 5E BE A0 1B 71 1B A1 10 53 ; 
5398:          57 17 56 5E DB 72 46 B8 51 5E 96 64 DB 72 D4 4C ; 
53A8:          56 F4 D6 9C DB 72 B5 D0 1B BC 1B A1 10 53 57 17 ; 
53B8:          43 5E 73 15 D5 B5 56 BD C0 7A D0 15 82 17 46 5E ; 
53C8:          66 7B 8D 48 B3 63 8E 48 61 17 1B 92 34 9E E6 5F ; 
53D8:          C4 B5 A3 60 33 98 97 7B 82 17 46 5E 57 62 B3 B3 ; 
53E8:          0E 67 0B 8E 5F BE 61 17 82 C6 38 62 A9 15 1C B2 ; 
53F8:          27 A0                     ; 
;
;              WEST OF SHERIFF. YOU ARE STANDING AT THE WEST SIDE OF THE
;              SHERIFF'S OFFICE. TO THE NORTH YOU CAN SEE THE SIDE OF THE
;              BAR. TO THE WEST YOU CAN SEE A GAS STATION IN THE DISTANCE,
;              AND SOME OBJECTS BEHIND IT. THE DESERT FILLS THE SOUTHERN
;              HORIZON.
;
;
53FA:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
53FC:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
53FF:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5400:          02                        ;       ELSE goto=0x5403
5401:             00 8A                  ;         COM_00_move_and_look(room=RM_2_WEST_OF_TOWN)
5403:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5404:          06                        ;       ELSE goto=0x540B
5405:             0D 04                  ;         COM_0D_while_pass length=0x0004
5407:                30 88               ;           COM_30_set_current_room(room=RM_1_EAST_OF_STATION)
5409:                2F 01               ;           COM_2F_load_section_from_disk(section=1)
540B:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
540C:          06                        ;       ELSE goto=0x5413
540D:             0D 04                  ;         COM_0D_while_pass length=0x0004
540F:                30 8C               ;           COM_30_set_current_room(room=RM_1_SOUTHWEST_OF_SHERIFF)
5411:                2F 01               ;           COM_2F_load_section_from_disk(section=1)

; --------------------------------------------------------------------------------------------------------------------
;
5413: 8D 81 62 00                        ; ----- Room 0x8D RM_2_MAIN_STREET_WEST, Length: 0x0162, Data: 0x00
;
5417:    03 81 39                        ;   ---- Section SECTION_03_DESCRIPTION length=0x0139
541A:       04 81 36                     ;     COM_04_print_command length=0x0136
541D:          8B 91 95 96 EF BF 73 62 B5 D0 9B C1 C7 DE 94 14 ; 
542D:          55 5E 50 BD 90 5A D1 6A 8F 96 D0 47 66 17 67 B1 ; 
543D:          03 BC 16 BC DB 72 B5 D0 15 BC FF 78 B8 16 89 17 ; 
544D:          27 D2 89 17 82 17 50 5E BE A0 1B 71 1B A1 10 53 ; 
545D:          57 17 56 5E DB 72 0E B7 40 A0 56 F4 D6 9C DB 72 ; 
546D:          47 B9 53 BE 5F BE 5B B1 4B 7B 5F BE 5A 17 33 62 ; 
547D:          85 66 D1 B5 93 66 BF 53 4B 15 96 AF D6 9C DB 72 ; 
548D:          B5 D0 1B BC 1B A1 A7 B7 7B 14 EB 4F C3 8B CF 98 ; 
549D:          89 17 82 17 47 5E 66 49 51 18 45 C2 83 48 A7 B7 ; 
54AD:          5B 17 1D 6E C0 16 57 17 74 CA 33 48 EB 4F C3 8B ; 
54BD:          C5 98 56 F4 DB 72 EB 4F C3 8B AB 98 75 4D FF 78 ; 
54CD:          82 17 44 5E 23 49 63 B1 2E 5C 6C 13 25 9E CA B5 ; 
54DD:          2E 49 14 D0 B4 63 82 17 44 5E CE C4 90 5A C8 6A ; 
54ED:          3E C6 F4 72 09 15 03 D2 5F BE 39 17 F3 46 63 B1 ; 
54FD:          2E 5C 72 13 FF A0 9C 8F 82 17 55 5E FF BF 0F 56 ; 
550D:          5B B1 7A 98 16 BC D6 9C DB 72 1F B8 08 B2 E5 64 ; 
551D:          B8 16 05 67 54 5E 86 5F 33 BB 9E 1D 5D 7A C9 B5 ; 
552D:          F5 B2 33 62 6E 62 96 19 DB 72 0C BA E6 C3 2F C6 ; 
553D:          AF 14 C0 DE 16 58 56 72 5B 17 E6 93 55 DB 55 4A ; 
554D:          FC ED D0 4C 5C 89         ; 
;
;              MAIN STREET WEST. YOU ARE STANDING ON MAIN STREET AT THE
;              WEST SIDE OF TOWN. TO THE NORTH YOU CAN SEE THE SALOON. TO
;              THE SOUTH THERE IS THE SHERIFF'S OFFICE. FAR TO THE WEST
;              YOU SEE A BUILDING. TO THE EAST YOU CAN SEE SIGNS ON
;              SEVERAL BUILDINGS. THE BUILDING BESIDE THE BAR READS,
;              "BOB'S HARDWARE," THE BUILDING FURTHER DOWN THE ROAD READS,
;              "HOTEL." THE STRUCTURE NEXT TO THE SHERIFF'S OFFICE READS,
;              "SLIM'S GROCERIES," THE STRUCTURE BEYOND THAT SIMPLY SAYS,
;              "BANK."
;
;
5553:    04 23                           ;   ---- Section SECTION_04_COMMANDS length=0x0023
5555:       0B 21 0A                     ;     COM_0B_switch length=0x0021, function=COM_0A_is_input_phrase(phrase_num)
5558:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5559:          08                        ;       ELSE goto=0x5562
555A:             0E 06                  ;         COM_0E_while_fail length=0x0006
555C:                14                  ;           COM_14_execute_and_reverse_status next command
555D:                1C 06               ;           COM_1C_set_var_object(obj=OBJ_06_DOOR_MAIN_STREET_WEST)
555F:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5560:                00 A2               ;           COM_00_move_and_look(room=RM_2_SALOON)
5562:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5563:          06                        ;       ELSE goto=0x556A
5564:             0D 04                  ;         COM_0D_while_pass length=0x0004
5566:                30 90               ;           COM_30_set_current_room(room=RM_3_WEST_ALLEY_INTERSECTION)
5568:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
556A:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
556B:          02                        ;       ELSE goto=0x556E
556C:             00 8A                  ;         COM_00_move_and_look(room=RM_2_WEST_OF_TOWN)
556E:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
556F:          08                        ;       ELSE goto=0x5578
5570:             0E 06                  ;         COM_0E_while_fail length=0x0006
5572:                14                  ;           COM_14_execute_and_reverse_status next command
5573:                1C 08               ;           COM_1C_set_var_object(obj=OBJ_08_DOOR_MAIN_STREET_WEST)
5575:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5576:                00 8E               ;           COM_00_move_and_look(room=RM_2_SHERIFFS_OFFICE)

; --------------------------------------------------------------------------------------------------------------------
;
5578: 8E 80 8D 00                        ; ----- Room 0x8E RM_2_SHERIFFS_OFFICE, Length: 0x008D, Data: 0x00
;
557C:    03 7B                           ;   ---- Section SECTION_03_DESCRIPTION length=0x007B
557E:       04 79                        ;     COM_04_print_command length=0x0079
5580:          1F B8 08 B2 E5 64 B8 16 05 67 DB 63 C7 DE 94 14 ; 
5590:          50 5E 6B A1 9D 7A FF 78 82 17 55 5E F4 72 50 79 ; 
55A0:          CB 23 D0 9E D7 78 43 F4 63 16 DB B9 5B CA 36 92 ; 
55B0:          33 48 F5 59 D5 83 8D 7B 89 14 D0 47 F3 B9 5F BE ; 
55C0:          23 15 F3 B9 0E D0 9B 8F 73 7B 55 72 82 17 67 B1 ; 
55D0:          0C 15 F7 49 8B B3 79 68 56 90 53 A0 6B BF 06 4F ; 
55E0:          7F BF 43 F4 08 4F 56 5E DB 72 F5 59 CB 83 C3 B5 ; 
55F0:          87 15 85 96 B3 46 76 98 2E ; 
;
;              SHERIFF'S OFFICE. YOU ARE NOW INSIDE THE SHERIFF'S OFFICE.
;              A MASSIVE METAL DESK SITS AGAINST THE EAST WALL. IT HAS
;              THREE DRAWERS FROM TOP TO BOTTOM. ABOVE THE DESK IS A GUN
;              CABINET.
;
;
55F9:    04 0D                           ;   ---- Section SECTION_04_COMMANDS length=0x000D
55FB:       0B 0B 0A                     ;     COM_0B_switch length=0x000B, function=COM_0A_is_input_phrase(phrase_num)
55FE:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
55FF:          08                        ;       ELSE goto=0x5608
5600:             0E 06                  ;         COM_0E_while_fail length=0x0006
5602:                14                  ;           COM_14_execute_and_reverse_status next command
5603:                1C 09               ;           COM_1C_set_var_object(obj=OBJ_09_DOOR_SHERIFFS_OFFICE)
5605:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5606:                00 8D               ;           COM_00_move_and_look(room=RM_2_MAIN_STREET_WEST)

; --------------------------------------------------------------------------------------------------------------------
;
5608: 8F 66 00                           ; ----- Room 0x8F RM_2_SOUTH_OF_SHERIFF, Length: 0x0066, Data: 0x00
;
560B:    03 4A                           ;   ---- Section SECTION_03_DESCRIPTION length=0x004A
560D:       04 48                        ;     COM_04_print_command length=0x0048
560F:          47 B9 53 BE C3 9E 1F B8 08 B2 1B 6A C7 DE 94 14 ; 
561F:          50 5E 6B A1 FB B9 43 98 AB 98 47 B9 53 BE C3 9E ; 
562F:          5F BE 5A 17 33 62 85 66 D1 B5 93 66 BF 53 82 17 ; 
563F:          2F 62 D5 15 7B 14 D4 4C 66 B1 FB 17 49 98 D1 CE ; 
564F:          96 96 DB 72 0E D0 9B 8F   ; 
;
;              SOUTH OF SHERIFF. YOU ARE NOW STANDING SOUTH OF THE
;              SHERIFF'S OFFICE. THERE IS A BARRED WINDOW ON THE WALL.
;
;
5657:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5659:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
565C:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
565D:          06                        ;       ELSE goto=0x5664
565E:             0D 04                  ;         COM_0D_while_pass length=0x0004
5660:                30 8C               ;           COM_30_set_current_room(room=RM_1_SOUTHWEST_OF_SHERIFF)
5662:                2F 01               ;           COM_2F_load_section_from_disk(section=1)
5664:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5665:          06                        ;       ELSE goto=0x566C
5666:             0D 04                  ;         COM_0D_while_pass length=0x0004
5668:                30 B1               ;           COM_30_set_current_room(room=RM_3_DESERT_SOUTH2)
566A:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
566C:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
566D:          02                        ;       ELSE goto=0x5670
566E:             00 92                  ;         COM_00_move_and_look(room=RM_2_SOUTH_OF_WEST_ALLEY)

; --------------------------------------------------------------------------------------------------------------------
;
5670: 92 80 8C 00                        ; ----- Room 0x92 RM_2_SOUTH_OF_WEST_ALLEY, Length: 0x008C, Data: 0x00
;
5674:    03 68                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0068
5676:       04 66                        ;     COM_04_print_command length=0x0066
5678:          47 B9 53 BE C3 9E B5 D0 03 BC FF 8C DB E0 C7 DE ; 
5688:          94 14 50 5E 6B A1 FB B9 43 98 AB 98 47 B9 53 BE ; 
5698:          C3 9E 5F BE 8E 14 FB 8B AF 14 B7 C0 83 61 5F BE ; 
56A8:          5A 17 33 62 85 66 D1 B5 93 66 9B 53 8E 48 82 17 ; 
56B8:          49 5E F5 B2 43 62 56 F4 D6 9C DB 72 95 5F 73 C1 ; 
56C8:          47 B9 76 BE 90 14 19 58 66 62 D5 15 2F 15 53 A7 ; 
56D8:          FF 14 B4 B7 9B C1         ; 
;
;              SOUTH OF WEST ALLEY. YOU ARE NOW STANDING SOUTH OF THE
;              ALLEY BETWEEN THE SHERIFF'S OFFICE AND THE GROCERY. TO THE
;              EAST, SOUTH, AND WEST IS EMPTY DESERT.
;
;
56DE:    04 1F                           ;   ---- Section SECTION_04_COMMANDS length=0x001F
56E0:       0B 1D 0A                     ;     COM_0B_switch length=0x001D, function=COM_0A_is_input_phrase(phrase_num)
56E3:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
56E4:          06                        ;       ELSE goto=0x56EB
56E5:             0D 04                  ;         COM_0D_while_pass length=0x0004
56E7:                30 95               ;           COM_30_set_current_room(room=RM_3_SOUTH_OF_SLIMS)
56E9:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
56EB:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
56EC:          06                        ;       ELSE goto=0x56F3
56ED:             0D 04                  ;         COM_0D_while_pass length=0x0004
56EF:                30 91               ;           COM_30_set_current_room(room=RM_3_WEST_ALLEY_SOUTH)
56F1:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
56F3:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
56F4:          06                        ;       ELSE goto=0x56FB
56F5:             0D 04                  ;         COM_0D_while_pass length=0x0004
56F7:                30 B1               ;           COM_30_set_current_room(room=RM_3_DESERT_SOUTH2)
56F9:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
56FB:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
56FC:          02                        ;       ELSE goto=0x56FF
56FD:             00 8F                  ;         COM_00_move_and_look(room=RM_2_SOUTH_OF_SHERIFF)

; --------------------------------------------------------------------------------------------------------------------
;
56FF: 9F 80 D3 00                        ; ----- Room 0x9F RM_2_NORTHWEST_OF_SALOON, Length: 0x00D3, Data: 0x00
;
5703:    03 80 B3                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00B3
5706:       04 80 B0                     ;     COM_04_print_command length=0x00B0
5709:          04 9A 71 BE 66 62 B8 16 53 17 81 8D 1B 9C C7 DE ; 
5719:          94 14 55 5E 50 BD 90 5A CB 6A 96 96 DB 72 F5 59 ; 
5729:          3E 62 99 16 C2 B3 B5 D0 11 BC 96 64 80 A1 56 F4 ; 
5739:          D6 9C DB 72 95 5F 1B BC 1B A1 10 53 57 17 56 5E ; 
5749:          DB 72 C5 4C D1 83 83 64 3B 16 B7 B1 01 18 7F 9E ; 
5759:          84 96 CE C4 90 5A 33 70 F4 68 5F BE 87 AF 66 49 ; 
5769:          51 18 45 C2 83 48 A7 B7 82 17 44 5E DD 46 B8 16 ; 
5779:          FA 17 73 49 A7 B7 4B 94 6B BF 5B 4D 55 45 8E 91 ; 
5789:          15 8A 84 BF DB 63 83 7A 5F BE 03 15 FB B9 17 98 ; 
5799:          03 EE 21 8E 89 17 82 17 47 5E 66 49 D5 15 90 14 ; 
57A9:          02 A1 23 62 41 D2 F0 59 66 17 E5 B3 74 C0 DB 63 ; 
;
;              NORTHWEST OF SALOON. YOU ARE STANDING IN THE DESERT
;              NORTHWEST OF TOWN. TO THE EAST YOU CAN SEE THE BACK OF A
;              LARGE WOODEN BUILDING, FURTHER EAST YOU CAN SEE THE BACK OF
;              WHAT SEEMS TO BE A SMALL STORE. IN THE DISTANCE, ALSO TO
;              THE EAST IS ANOTHER WOODEN STRUCTURE.
;
;
57B9:    04 1A                           ;   ---- Section SECTION_04_COMMANDS length=0x001A
57BB:       0B 18 0A                     ;     COM_0B_switch length=0x0018, function=COM_0A_is_input_phrase(phrase_num)
57BE:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
57BF:          02                        ;       ELSE goto=0x57C2
57C0:             00 B6                  ;         COM_00_move_and_look(room=RM_2_DESERT_NORTH1)
57C2:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
57C3:          02                        ;       ELSE goto=0x57C6
57C4:             00 A0                  ;         COM_00_move_and_look(room=RM_2_WEST_SIDE_OF_SALOON)
57C6:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
57C7:          02                        ;       ELSE goto=0x57CA
57C8:             00 A1                  ;         COM_00_move_and_look(room=RM_2_NORTH_OF_SALOON)
57CA:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
57CB:          09                        ;       ELSE goto=0x57D5
57CC:             0D 07                  ;         COM_0D_while_pass length=0x0007
57CE:                30 F5               ;           COM_30_set_current_room(room=RM_5_DESERT27)
57D0:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
57D3:                2F 05               ;           COM_2F_load_section_from_disk(section=5)

; --------------------------------------------------------------------------------------------------------------------
;
57D5: A0 80 F5 00                        ; ----- Room 0xA0 RM_2_WEST_SIDE_OF_SALOON, Length: 0x00F5, Data: 0x00
;
57D9:    03 80 C0                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00C0
57DC:       04 80 BD                     ;     COM_04_print_command length=0x00BD
57DF:          B5 D0 15 BC FF 78 B8 16 53 17 81 8D 1B 9C C7 DE ; 
57EF:          94 14 50 5E 6B A1 04 9A 53 BE C3 9E 5F BE A3 15 ; 
57FF:          31 6D 3B 4A 73 49 5F BE F7 17 F3 B9 8E 61 B8 16 ; 
580F:          89 17 27 D2 89 17 82 17 47 5E 66 49 51 18 45 C2 ; 
581F:          83 48 A7 B7 82 17 55 5E FF 78 B8 16 7B 14 54 8B ; 
582F:          9B 6C 41 D2 F0 59 BF 14 3E 7A 91 7A 56 F4 D6 9C ; 
583F:          DB 72 47 B9 76 BE C0 16 82 17 48 5E 23 49 46 B8 ; 
584F:          51 5E 96 64 DB 72 0C BA 36 60 1B EE 1B A1 10 53 ; 
585F:          57 17 56 5E DB 72 46 B8 51 5E 83 64 83 96 74 5B ; 
586F:          44 5E CE C4 90 5A 5B 70 6B BF 5F BE 99 16 C2 B3 ; 
587F:          90 14 16 58 DB 72 B5 D0 16 BC DB 72 F5 59 3E 62 ; 
588F:          53 15 0D 8D 82 17 4A 5E B3 A0 00 E5 2E ; 
;
;              WEST SIDE OF SALOON. YOU ARE NOW NORTH OF THE HIGHWAY AT
;              THE WEST END OF TOWN. TO THE EAST YOU CAN SEE THE SIDE OF A
;              LARGE WOODEN BUILDING. TO THE SOUTH, ON THE FAR SIDE OF THE
;              STREET, YOU CAN SEE THE SIDE OF AN ADOBE BUILDING. TO THE
;              NORTH AND THE WEST THE DESERT FILLS THE HORIZON.
;
;
589C:    04 2F                           ;   ---- Section SECTION_04_COMMANDS length=0x002F
589E:       0B 2D 0A                     ;     COM_0B_switch length=0x002D, function=COM_0A_is_input_phrase(phrase_num)
58A1:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
58A2:          02                        ;       ELSE goto=0x58A5
58A3:             00 9F                  ;         COM_00_move_and_look(room=RM_2_NORTHWEST_OF_SALOON)
58A5:          55                        ;       COM_0A_is_input_phrase("CLIMB * DOWN *")
58A6:          08                        ;       ELSE goto=0x58AF
58A7:             0E 06                  ;         COM_0E_while_fail length=0x0006
58A9:                14                  ;           COM_14_execute_and_reverse_status next command
58AA:                1C 14               ;           COM_1C_set_var_object(obj=OBJ_14_DOOR_COVERED_SHELTER)
58AC:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
58AD:                00 DB               ;           COM_00_move_and_look(room=RM_2_STORM_SHELTER)
58AF:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
58B0:          10                        ;       ELSE goto=0x58C1
58B1:             0D 0E                  ;         COM_0D_while_pass length=0x000E
58B3:                0E 04               ;           COM_0E_while_fail length=0x0004
58B5:                   09 00            ;             COM_09_compare_to_second_noun(obj=nothing)
58B7:                   09 5F            ;             COM_09_compare_to_second_noun(obj=OBJ_5F_SHELTER)
58B9:                0E 06               ;           COM_0E_while_fail length=0x0006
58BB:                   14               ;             COM_14_execute_and_reverse_status next command
58BC:                   1C 14            ;             COM_1C_set_var_object(obj=OBJ_14_DOOR_COVERED_SHELTER)
58BE:                   8D               ;             FN_8D_ASSERT_OBJECT_IS_CLOSED
58BF:                   00 DB            ;             COM_00_move_and_look(room=RM_2_STORM_SHELTER)
58C1:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
58C2:          02                        ;       ELSE goto=0x58C5
58C3:             00 8A                  ;         COM_00_move_and_look(room=RM_2_WEST_OF_TOWN)
58C5:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
58C6:          06                        ;       ELSE goto=0x58CD
58C7:             0D 04                  ;         COM_0D_while_pass length=0x0004
58C9:                30 AF               ;           COM_30_set_current_room(room=RM_1_NORTH_OF_HIGHWAY3)
58CB:                2F 01               ;           COM_2F_load_section_from_disk(section=1)

; --------------------------------------------------------------------------------------------------------------------
;
58CD: A1 80 82 00                        ; ----- Room 0xA1 RM_2_NORTH_OF_SALOON, Length: 0x0082, Data: 0x00
;
58D1:    03 6E                           ;   ---- Section SECTION_03_DESCRIPTION length=0x006E
58D3:       04 6C                        ;     COM_04_print_command length=0x006C
58D5:          04 9A 53 BE C3 9E 0E B7 40 A0 5B F4 1B A1 2F 49 ; 
58E5:          99 16 C2 B3 B8 16 82 17 4E 5E 31 49 59 5E 36 A0 ; 
58F5:          83 61 EB 4F C3 8B AB 98 73 49 5F BE F7 17 F3 B9 ; 
5905:          8E 61 B8 16 89 17 27 D2 89 17 82 17 47 5E 66 49 ; 
5915:          1B EE 1B A1 10 53 57 17 56 5E 2B D2 02 A1 23 62 ; 
5925:          EB 4F C3 8B C5 98 44 F4 91 62 30 60 82 17 5B 61 ; 
5935:          F0 B3 5F 17 46 48 8E 14 FB 8B 5B BB ; 
;
;              NORTH OF SALOON. YOU ARE NORTH OF THE LARGE WOODEN BUILDING
;              AT THE WEST END OF TOWN. TO THE EAST, YOU CAN SEE TWO OTHER
;              BUILDINGS. BETWEEN THEM RUN SMALL ALLEYS.
;
;
5941:    04 0F                           ;   ---- Section SECTION_04_COMMANDS length=0x000F
5943:       0B 0D 0A                     ;     COM_0B_switch length=0x000D, function=COM_0A_is_input_phrase(phrase_num)
5946:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5947:          02                        ;       ELSE goto=0x594A
5948:             00 B6                  ;         COM_00_move_and_look(room=RM_2_DESERT_NORTH1)
594A:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
594B:          02                        ;       ELSE goto=0x594E
594C:             00 A3                  ;         COM_00_move_and_look(room=RM_2_NORTH_OF_WEST_ALLEY)
594E:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
594F:          02                        ;       ELSE goto=0x5952
5950:             00 9F                  ;         COM_00_move_and_look(room=RM_2_NORTHWEST_OF_SALOON)

; --------------------------------------------------------------------------------------------------------------------
;
5952: A2 6E 00                           ; ----- Room 0xA2 RM_2_SALOON, Length: 0x006E, Data: 0x00
;
5955:    03 5C                           ;   ---- Section SECTION_03_DESCRIPTION length=0x005C
5957:       04 5A                        ;     COM_04_print_command length=0x005A
5959:          0E B7 40 A0 5B F4 1B A1 2F 49 D0 15 46 B8 56 5E ; 
5969:          DB 72 EB 4F C3 8B CF 98 82 17 2F 62 D5 15 7B 14 ; 
5979:          54 8B 9B 6C D4 4C 8E 14 11 A0 82 17 47 5E 66 49 ; 
5989:          F3 17 17 8D 57 17 74 CA 33 48 1B 54 3D 7B 90 14 ; 
5999:          16 58 B6 46 4B 62 2F 49 55 17 8E 49 2F 62 03 58 ; 
59A9:          07 B3 33 98 5F BE 39 17 FF 9F ; 
;
;              SALOON. YOU ARE INSIDE THE BUILDING. THERE IS A LARGE BAR
;              ALONG THE EAST WALL. SEVERAL CHAIRS AND TABLES ARE
;              SCATTERED AROUND THE ROOM.
;
;
59B3:    04 0D                           ;   ---- Section SECTION_04_COMMANDS length=0x000D
59B5:       0B 0B 0A                     ;     COM_0B_switch length=0x000B, function=COM_0A_is_input_phrase(phrase_num)
59B8:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
59B9:          08                        ;       ELSE goto=0x59C2
59BA:             0E 06                  ;         COM_0E_while_fail length=0x0006
59BC:                14                  ;           COM_14_execute_and_reverse_status next command
59BD:                1C 07               ;           COM_1C_set_var_object(obj=OBJ_07_DOOR_SALOON)
59BF:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
59C0:                00 8D               ;           COM_00_move_and_look(room=RM_2_MAIN_STREET_WEST)

; --------------------------------------------------------------------------------------------------------------------
;
59C2: A3 80 C8 00                        ; ----- Room 0xA3 RM_2_NORTH_OF_WEST_ALLEY, Length: 0x00C8, Data: 0x00
;
59C6:    03 80 AB                        ;   ---- Section SECTION_03_DESCRIPTION length=0x00AB
59C9:       04 80 A8                     ;     COM_04_print_command length=0x00A8
59CC:          04 9A 53 BE C3 9E B5 D0 03 BC FF 8C DB E0 C7 DE ; 
59DC:          94 14 4B 5E 96 96 DB 72 F5 59 3E 62 96 14 82 17 ; 
59EC:          47 5E CC 9A 8D 48 51 5E 96 64 DB 72 46 48 3B 63 ; 
59FC:          73 49 5F BE F7 17 F3 B9 8E 61 B8 16 89 17 27 D2 ; 
5A0C:          89 17 82 17 59 5E 66 62 D5 15 7B 14 54 8B 9B 6C ; 
5A1C:          41 D2 F0 59 BF 14 3E 7A 91 7A 48 F4 23 49 6B BF ; 
5A2C:          5F BE 23 15 F3 B9 C7 DE D3 14 95 96 1B 60 36 DD ; 
5A3C:          90 14 02 A1 23 62 41 D2 F0 59 BF 14 3E 7A 91 7A ; 
5A4C:          56 F4 D6 9C DB 72 04 9A 53 BE 5F BE FF 14 B4 B7 ; 
5A5C:          07 BC 3F D9 4D 98 95 14 4B 15 83 AF D6 B5 DB 72 ; 
5A6C:          47 63 D3 14 95 96 3F 60   ; 
;
;              NORTH OF WEST ALLEY. YOU ARE IN THE DESERT AT THE ENTRANCE
;              OF THE ALLEY AT THE WEST END OF TOWN. TO THE WEST IS A
;              LARGE WOODEN BUILDING. FAR TO THE EAST YOU CAN SEE YET
;              ANOTHER WOODEN BUILDING. TO THE NORTH THE DESERT EXTENDS AS
;              FAR AS THE EYE CAN SEE.
;
;
5A74:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5A76:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
5A79:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5A7A:          02                        ;       ELSE goto=0x5A7D
5A7B:             00 B6                  ;         COM_00_move_and_look(room=RM_2_DESERT_NORTH1)
5A7D:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5A7E:          02                        ;       ELSE goto=0x5A81
5A7F:             00 A4                  ;         COM_00_move_and_look(room=RM_2_WEST_ALLEY_NORTH)
5A81:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5A82:          06                        ;       ELSE goto=0x5A89
5A83:             0D 04                  ;         COM_0D_while_pass length=0x0004
5A85:                30 A5               ;           COM_30_set_current_room(room=RM_3_NORTH_OF_BOBS)
5A87:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
5A89:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5A8A:          02                        ;       ELSE goto=0x5A8D
5A8B:             00 A1                  ;         COM_00_move_and_look(room=RM_2_NORTH_OF_SALOON)

; --------------------------------------------------------------------------------------------------------------------
;
5A8D: A4 44 00                           ; ----- Room 0xA4 RM_2_WEST_ALLEY_NORTH, Length: 0x0044, Data: 0x00
;
5A90:    03 30                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0030
5A92:       04 2E                        ;     COM_04_print_command length=0x002E
5A94:          B5 D0 03 BC FF 8C 50 DB BE A0 9B 76 C7 DE 94 14 ; 
5AA4:          44 5E 91 62 30 60 82 17 55 5E 49 48 03 A0 8E 48 ; 
5AB4:          82 17 4A 5E 2E 49 14 D0 55 5E 84 BF DB 63 ; 
;
;              WEST ALLEY NORTH. YOU ARE BETWEEN THE SALOON AND THE
;              HARDWARE STORE.
;
;
5AC2:    04 0F                           ;   ---- Section SECTION_04_COMMANDS length=0x000F
5AC4:       0B 0D 0A                     ;     COM_0B_switch length=0x000D, function=COM_0A_is_input_phrase(phrase_num)
5AC7:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5AC8:          02                        ;       ELSE goto=0x5ACB
5AC9:             00 A3                  ;         COM_00_move_and_look(room=RM_2_NORTH_OF_WEST_ALLEY)
5ACB:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5ACC:          06                        ;       ELSE goto=0x5AD3
5ACD:             0D 04                  ;         COM_0D_while_pass length=0x0004
5ACF:                30 90               ;           COM_30_set_current_room(room=RM_3_WEST_ALLEY_INTERSECTION)
5AD1:                2F 03               ;           COM_2F_load_section_from_disk(section=3)

; --------------------------------------------------------------------------------------------------------------------
;
5AD3: B6 51 00                           ; ----- Room 0xB6 RM_2_DESERT_NORTH1, Length: 0x0051, Data: 0x00
;
5AD6:    03 2E                           ;   ---- Section SECTION_03_DESCRIPTION length=0x002E
5AD8:       04 2C                        ;     COM_04_print_command length=0x002C
5ADA:          F5 59 3E 62 99 16 C2 B3 5B F4 1B A1 2F 49 66 17 ; 
5AEA:          8E 48 91 7A D0 15 82 17 46 5E 57 62 B3 B3 D4 65 ; 
5AFA:          99 16 C2 B3 B8 16 7B 14 89 BF 1B 9C ; 
;
;              DESERT NORTH. YOU ARE STANDING IN THE DESERT FAR NORTH OF A
;              TOWN.
;
;
5B06:    04 1E                           ;   ---- Section SECTION_04_COMMANDS length=0x001E
5B08:       0B 1C 0A                     ;     COM_0B_switch length=0x001C, function=COM_0A_is_input_phrase(phrase_num)
5B0B:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5B0C:          02                        ;       ELSE goto=0x5B0F
5B0D:             00 B7                  ;         COM_00_move_and_look(room=RM_2_DESERT_PATH)
5B0F:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5B10:          02                        ;       ELSE goto=0x5B13
5B11:             00 A3                  ;         COM_00_move_and_look(room=RM_2_NORTH_OF_WEST_ALLEY)
5B13:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5B14:          09                        ;       ELSE goto=0x5B1E
5B15:             0D 07                  ;         COM_0D_while_pass length=0x0007
5B17:                30 F5               ;           COM_30_set_current_room(room=RM_5_DESERT27)
5B19:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5B1C:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5B1E:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5B1F:          06                        ;       ELSE goto=0x5B26
5B20:             0D 04                  ;         COM_0D_while_pass length=0x0004
5B22:                30 B8               ;           COM_30_set_current_room(room=RM_3_DESERT_NORTH2)
5B24:                2F 03               ;           COM_2F_load_section_from_disk(section=3)

; --------------------------------------------------------------------------------------------------------------------
;
5B26: B7 80 80 00                        ; ----- Room 0xB7 RM_2_DESERT_PATH, Length: 0x0080, Data: 0x00
;
5B2A:    03 4F                           ;   ---- Section SECTION_03_DESCRIPTION length=0x004F
5B2C:       04 4D                        ;     COM_04_print_command length=0x004D
5B2E:          F5 59 3E 62 DB 16 77 BE 51 18 43 C2 5B B1 FB B9 ; 
5B3E:          43 98 AB 98 03 A0 52 45 82 49 82 17 73 49 E3 8B ; 
5B4E:          0B 5C 47 B9 53 BE 89 BF 2E 49 D6 B5 DB 72 95 5A ; 
5B5E:          50 BD 16 BC 80 A1 90 14 10 58 BE A0 06 71 32 60 ; 
5B6E:          23 62 9E 7A D6 9C DB 72 F5 59 3E 62 2E ; 
;
;              DESERT PATH. YOU ARE STANDING ON A PATH THAT LEADS SOUTH
;              TOWARDS THE DISTANT TOWN AND NORTH DEEPER INTO THE DESERT.
;
;
5B7B:    04 2C                           ;   ---- Section SECTION_04_COMMANDS length=0x002C
5B7D:       0B 2A 0A                     ;     COM_0B_switch length=0x002A, function=COM_0A_is_input_phrase(phrase_num)
5B80:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5B81:          09                        ;       ELSE goto=0x5B8B
5B82:             0D 07                  ;         COM_0D_while_pass length=0x0007
5B84:                30 F6               ;           COM_30_set_current_room(room=RM_5_DESERT_SMALL_TRAIL2)
5B86:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5B89:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5B8B:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5B8C:          09                        ;       ELSE goto=0x5B96
5B8D:             0D 07                  ;         COM_0D_while_pass length=0x0007
5B8F:                30 F1               ;           COM_30_set_current_room(room=RM_5_DESERT_SMALL_TRAIL1)
5B91:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5B94:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5B96:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5B97:          09                        ;       ELSE goto=0x5BA1
5B98:             0D 07                  ;         COM_0D_while_pass length=0x0007
5B9A:                30 F5               ;           COM_30_set_current_room(room=RM_5_DESERT27)
5B9C:                17 9D 01            ;           COM_17_move_to(obj=OBJ_9D_THIRST_TRACKER, destination=OBJ_01_PLAYER)
5B9F:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
5BA1:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5BA2:          06                        ;       ELSE goto=0x5BA9
5BA3:             0D 04                  ;         COM_0D_while_pass length=0x0004
5BA5:                30 B8               ;           COM_30_set_current_room(room=RM_3_DESERT_NORTH2)
5BA7:                2F 03               ;           COM_2F_load_section_from_disk(section=3)

; --------------------------------------------------------------------------------------------------------------------
;
5BA9: DB 75 00                           ; ----- Room 0xDB RM_2_STORM_SHELTER, Length: 0x0075, Data: 0x00
;
5BAC:    03 51                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0051
5BAE:       04 4F                        ;     COM_04_print_command length=0x004F
5BB0:          09 BA 9B B2 1F B8 3F 8E 1B B5 C7 DE 9B 15 5B CA ; 
5BC0:          9E 61 2F 62 03 58 66 17 B7 A0 5A 17 4E 61 47 62 ; 
5BD0:          D6 15 D5 15 3A 15 EF BF 2E 92 46 DB 35 49 03 EE ; 
5BE0:          33 98 C7 DE 94 14 56 5E 91 48 E6 8B D0 15 7B 14 ; 
5BF0:          54 95 86 78 B8 16 62 17 FF 78 99 AF BD 5F 2E ; 
;
;              STORM SHELTER. YOU HAVE ENTERED A STORM SHELTER. IT IS
;              EXTREMELY DARK, AND YOU ARE TANGLED IN A MYRIAD OF SPIDER
;              WEBS.
;
;
5BFF:    04 1F                           ;   ---- Section SECTION_04_COMMANDS length=0x001F
5C01:       0B 1D 0A                     ;     COM_0B_switch length=0x001D, function=COM_0A_is_input_phrase(phrase_num)
5C04:          37                        ;       COM_0A_is_input_phrase("CLIMB * OUT *")
5C05:          10                        ;       ELSE goto=0x5C16
5C06:             0D 0E                  ;         COM_0D_while_pass length=0x000E
5C08:                0E 04               ;           COM_0E_while_fail length=0x0004
5C0A:                   09 00            ;             COM_09_compare_to_second_noun(obj=nothing)
5C0C:                   09 60            ;             COM_09_compare_to_second_noun(obj=OBJ_60_SHELTER)
5C0E:                0E 06               ;           COM_0E_while_fail length=0x0006
5C10:                   14               ;             COM_14_execute_and_reverse_status next command
5C11:                   1C 15            ;             COM_1C_set_var_object(obj=OBJ_15_DOOR_SHELTER)
5C13:                   8D               ;             FN_8D_ASSERT_OBJECT_IS_CLOSED
5C14:                   00 A0            ;             COM_00_move_and_look(room=RM_2_WEST_SIDE_OF_SALOON)
5C16:          54                        ;       COM_0A_is_input_phrase("CLIMB * UP *")
5C17:          08                        ;       ELSE goto=0x5C20
5C18:             0E 06                  ;         COM_0E_while_fail length=0x0006
5C1A:                14                  ;           COM_14_execute_and_reverse_status next command
5C1B:                1C 15               ;           COM_1C_set_var_object(obj=OBJ_15_DOOR_SHELTER)
5C1D:                8D                  ;           FN_8D_ASSERT_OBJECT_IS_CLOSED
5C1E:                00 A0               ;           COM_00_move_and_look(room=RM_2_WEST_SIDE_OF_SALOON)
```

# Unitialized data

```code
5C20: 44 13 06 4D 41 53 54 45 52 14 05 42 52 41 53 53 ; D..MASTER..BRASS
5C30: 15 06 53 45 43 52 45 54 3D 06 53 4B 45 4C 45 54 ; ..SECRET=.SKELET
5C40: 17 05 53 54 45 45 4C 18 03 43 41 42 4B 03 42 49 ; ..STEEL..CABK.BI
5C50: 47 0E 05 4C 41 52 47 45 0E 05 53 4D 41 4C 4C 0F ; G..LARGE..SMALL.
5C60: 06 4C 49 54 54 4C 45 0F 03 54 4F 50 28 06 4D 49 ; .LITTLE..TOP(.MI
5C70: 44 44 4C 45 3C 06 42 4F 54 54 4F 4D 3E 04 46 4C ; DDLE<.BOTTOM>.FL
5C80: 41 54 22 05 53 50 41 52 45 23 04 42 4C 55 45 0D ; AT".SPARE#.BLUE.
5C90: 06 4D 41 53 53 49 56 3F 04 42 41 4E 4B 40 06 53 ; .MASSIV?.BANK@.S
5CA0: 41 4C 4F 4F 4E 41 06 53 48 45 52 49 46 42 06 4F ; ALOONA.SHERIFB.O
5CB0: 46 46 49 43 45 42 06 53 4C 49 4D 27 53 43 05 53 ; FFICEB.SLIM'SC.S
5CC0: 4C 49 4D 53 43 05 42 4F 42 27 53 44 04 42 4F 42 ; LIMSC.BOB'SD.BOB
5CD0: 53 44 06 44 4F 55 42 4C 45 45 05 48 4F 54 45 4C ; SD.DOUBLEE.HOTEL
5CE0: 47 06 53 57 49 4E 47 49 46 04 54 53 4F 4D 6B 04 ; G.SWINGIF.TSOMk.
5CF0: 43 4F 4F 4C 72 05 43 4C 45 41 52 74 05 42 52 4F ; COOLr.CLEARt.BRO
5D00: 57
```

