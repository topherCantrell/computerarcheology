![Xenos](Xenos.png)

# Xenos SECTION5.DAT

>>> cpu Z80

>>> binary 5200:roms/section5.bin

```code
5200: 00 8A 63                           ; List_ID=0x00, length=0x0A63 (to 0x5C66)

; --------------------------------------------------------------------------------------------------------------------
;
5203: 98 1D 00                           ; ----- Room 0x98 RM_5_DESERT2, Length: 0x001D, Data: 0x00
;
5206:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5209)
5208:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5209:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5222)
520B:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x5223), function=COM_0A_is_input_phrase(phrase_num)
520E:          03 06                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0006
5210:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5216)
5212:                30 97               ;           COM_30_set_current_room(room=RM_6_DESERT_CANYON4)
5214:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5210
;                                        ;       end case
5216:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5218:             00 BB                  ;         COM_00_move_and_look(room=RM_5_DESERT8)
;                                        ;       end case
521A:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
521C:             00 99                  ;         COM_00_move_and_look(room=RM_5_DESERT_CANYON1)
;                                        ;       end case
521E:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5220:             00 BA                  ;         COM_00_move_and_look(room=RM_5_DESERT7)
;                                        ;       end case
;                                        ;     end decode_switch at 0x520B

; --------------------------------------------------------------------------------------------------------------------
;
5222: 99 1A 00                           ; ----- Room 0x99 RM_5_DESERT_CANYON1, Length: 0x001A, Data: 0x00
;
5225:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x522B)
5227:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x522B)
5229:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
522A:          96                        ;       FN_96_PRINT_VAST_CANYON
;                                        ;     end group_AND at 0x5227
;
522B:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011 (to 0x523E)
522D:       0B 0F 0A                     ;     COM_0B_switch length=0x000F (to 0x523F), function=COM_0A_is_input_phrase(phrase_num)
5230:          03 01                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0001
5232:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5233:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5235:             00 9A                  ;         COM_00_move_and_look(room=RM_5_DESERT_CANYON2)
;                                        ;       end case
5237:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
5239:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
523A:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
523C:             00 98                  ;         COM_00_move_and_look(room=RM_5_DESERT2)
;                                        ;       end case
;                                        ;     end decode_switch at 0x522D

; --------------------------------------------------------------------------------------------------------------------
;
523E: 9A 1A 00                           ; ----- Room 0x9A RM_5_DESERT_CANYON2, Length: 0x001A, Data: 0x00
;
5241:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5247)
5243:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5247)
5245:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5246:          96                        ;       FN_96_PRINT_VAST_CANYON
;                                        ;     end group_AND at 0x5243
;
5247:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011 (to 0x525A)
5249:       0B 0F 0A                     ;     COM_0B_switch length=0x000F (to 0x525B), function=COM_0A_is_input_phrase(phrase_num)
524C:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
524E:             00 99                  ;         COM_00_move_and_look(room=RM_5_DESERT_CANYON1)
;                                        ;       end case
5250:          04 01                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0001
5252:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5253:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
5255:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5256:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5258:             00 BB                  ;         COM_00_move_and_look(room=RM_5_DESERT8)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5249

; --------------------------------------------------------------------------------------------------------------------
;
525A: 9B 62 00                           ; ----- Room 0x9B RM_5_NARROW_PATH, Length: 0x0062, Data: 0x00
;
525D:    03 45                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0045 (to 0x52A4)
525F:       04 43                        ;     COM_04_print_message length=0x0043 (to 0x52A4)
5261:          C7 DE 94 14 51 5E 83 96 8B 16 79 B3 D2 CE 82 49
5271:          82 17 73 49 E3 8B 0B 5C 89 5B 96 96 DB 72 C5 65
5281:          51 5E 96 64 DB 72 C3 54 83 66 6B BF 5F BE 99 16
5291:          C2 B3 4B F4 0B BC D8 B5 43 62 8C 17 85 5F F4 72
52A1:          35 A1 21                 
;
;              YOU ARE ON A NARROW PATH THAT LEADS DOWN THE FACE OF THE
;              CLIFF TO THE NORTH. IT IS VERY TREACHEROUS!
;
;
52A4:    04 18                           ;   ---- Section SECTION_04_COMMANDS length=0x0018 (to 0x52BE)
52A6:       0B 16 0A                     ;     COM_0B_switch length=0x0016 (to 0x52BF), function=COM_0A_is_input_phrase(phrase_num)
52A9:          03 01                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0001
52AB:             99                     ;         FN_99_DIE_CANYON_PLUNGE
;                                        ;       end case
52AC:          04 01                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0001
52AE:             99                     ;         FN_99_DIE_CANYON_PLUNGE
;                                        ;       end case
52AF:          01 09                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0009
52B1:             0E 07                  ;         COM_0E_group_OR length=0x0007 (to 0x52BA)
52B3:                0D 04               ;           COM_0D_group_AND length=0x0004 (to 0x52B9)
52B5:                   05 F0            ;             COM_05_is_leq_last_random(value=240)
52B7:                   00 9C            ;             COM_00_move_and_look(room=RM_5_CANYON_FLOOR)
;                                        ;           end group_AND at 0x52B3
52B9:                99                  ;           FN_99_DIE_CANYON_PLUNGE
;                                        ;         end group_OR at 0x52B1
;                                        ;       end case
52BA:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
52BC:             00 BC                  ;         COM_00_move_and_look(room=RM_5_DESERT9)
;                                        ;       end case
;                                        ;     end decode_switch at 0x52A6

; --------------------------------------------------------------------------------------------------------------------
;
52BE: 9C 68 00                           ; ----- Room 0x9C RM_5_CANYON_FLOOR, Length: 0x0068, Data: 0x00
;
52C1:    03 52                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0052 (to 0x5315)
52C3:       04 50                        ;     COM_04_print_message length=0x0050 (to 0x5315)
52C5:          C7 DE 94 14 50 5E 6B A1 03 A0 5F BE D3 14 91 9B
52D5:          88 96 81 8D 1B B5 6B BF 5F BE F7 17 F3 B9 C7 DE
52E5:          D3 14 95 96 1B 60 4E 45 31 49 45 5E D6 B0 23 62
52F5:          56 D1 03 71 EB 14 90 8C F3 5B 0E 53 67 16 4E BD
5305:          CB 78 34 9E E6 5F 2F 17 03 BA AB 98 83 7A 97 7B
;
;              YOU ARE NOW ON THE CANYON FLOOR. TO THE WEST YOU CAN SEE A
;              LARGE CRATER WITH A CYLINDRICAL METALIC OBJECT RESTING IN
;              IT.
;
;
5315:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011 (to 0x5328)
5317:       0B 0F 0A                     ;     COM_0B_switch length=0x000F (to 0x5329), function=COM_0A_is_input_phrase(phrase_num)
531A:          03 01                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0001
531C:             9A                     ;         FN_9A_PRINT_CANYON_PREVENTS
;                                        ;       end case
531D:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
531F:             00 9D                  ;         COM_00_move_and_look(room=RM_5_UFO_CRATER)
;                                        ;       end case
5321:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
5323:             9A                     ;         FN_9A_PRINT_CANYON_PREVENTS
;                                        ;       end case
5324:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5326:             00 9B                  ;         COM_00_move_and_look(room=RM_5_NARROW_PATH)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5317

; --------------------------------------------------------------------------------------------------------------------
;
5328: 9D 80 B3 00                        ; ----- Room 0x9D RM_5_UFO_CRATER, Length: 0x00B3, Data: 0x00
;
532C:    03 37                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0037 (to 0x5365)
532E:       04 35                        ;     COM_04_print_message length=0x0035 (to 0x5365)
5330:          C7 DE 94 14 50 5E 6B A1 83 7A 5F BE E4 14 7F 49
5340:          99 AF F4 72 43 5E A8 17 CA 9C 4B 49 50 8B E6 59
5350:          D6 06 DB 72 AB 55 F4 BD C2 16 9D 61 89 17 82 17
5360:          47 5E 66 49 2E           
;
;              YOU ARE NOW IN THE CRATER WHERE A UFO HAS LANDED! THE
;              CRATER OPENS TO THE EAST.
;
;
5365:    04 77                           ;   ---- Section SECTION_04_COMMANDS length=0x0077 (to 0x53DE)
5367:       0B 75 0A                     ;     COM_0B_switch length=0x0075 (to 0x53DF), function=COM_0A_is_input_phrase(phrase_num)
536A:          04 2D                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x002D
536C:             0E 2B                  ;         COM_0E_group_OR length=0x002B (to 0x5399)
536E:                0D 20               ;           COM_0D_group_AND length=0x0020 (to 0x5390)
5370:                   01 4E            ;             COM_01_is_in_pack_or_room(obj=OBJ_4E_BOULDER)
5372:                   04 1C            ;             COM_04_print_message length=0x001C (to 0x5390)
5374:                      5F BE B9 14 3E C5 23 62 89 4E A5 54 DB 16 D3 B9
5384:                      9B 6C 9E 7A D6 9C DB 72 23 B8 9B A8
;
;                          THE BOULDER BLOCKS PASSAGE INTO THE SHIP. 
;
;                                        ;           end group_AND at 0x536E
5390:                0D 07               ;           COM_0D_group_AND length=0x0007 (to 0x5399)
5392:                   30 80            ;             COM_30_set_current_room(room=RM_7_EXIT1)
5394:                   17 9D 00         ;             COM_17_move_object_to(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
5397:                   2F 07            ;             COM_2F_load_section_from_disk(section=7)
;                                        ;           end group_AND at 0x5390
;                                        ;         end group_OR at 0x536C
;                                        ;       end case
5399:          36 39                     ;       case COM_0A_is_input_phrase("ENTER * * *"), length=0x0039
539B:             0E 37                  ;         COM_0E_group_OR length=0x0037 (to 0x53D4)
539D:                0D 26               ;           COM_0D_group_AND length=0x0026 (to 0x53C5)
539F:                   0E 04            ;             COM_0E_group_OR length=0x0004 (to 0x53A5)
53A1:                      09 00         ;               COM_09_is_noun2(obj=nothing)
53A3:                      09 99         ;               COM_09_is_noun2(obj=OBJ_99_SHIP)
;                                        ;             end group_OR at 0x539F
53A5:                   01 4E            ;             COM_01_is_in_pack_or_room(obj=OBJ_4E_BOULDER)
53A7:                   04 1C            ;             COM_04_print_message length=0x001C (to 0x53C5)
53A9:                      5F BE B9 14 3E C5 23 62 89 4E A5 54 DB 16 D3 B9
53B9:                      9B 6C 9E 7A D6 9C DB 72 23 B8 9B A8
;
;                          THE BOULDER BLOCKS PASSAGE INTO THE SHIP. 
;
;                                        ;           end group_AND at 0x539D
53C5:                0D 0D               ;           COM_0D_group_AND length=0x000D (to 0x53D4)
53C7:                   0E 04            ;             COM_0E_group_OR length=0x0004 (to 0x53CD)
53C9:                      09 00         ;               COM_09_is_noun2(obj=nothing)
53CB:                      09 99         ;               COM_09_is_noun2(obj=OBJ_99_SHIP)
;                                        ;             end group_OR at 0x53C7
53CD:                   30 80            ;             COM_30_set_current_room(room=RM_7_EXIT1)
53CF:                   17 9D 00         ;             COM_17_move_object_to(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
53D2:                   2F 07            ;             COM_2F_load_section_from_disk(section=7)
;                                        ;           end group_AND at 0x53C5
;                                        ;         end group_OR at 0x539B
;                                        ;       end case
53D4:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
53D6:             9A                     ;         FN_9A_PRINT_CANYON_PREVENTS
;                                        ;       end case
53D7:          02 01                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0001
53D9:             9A                     ;         FN_9A_PRINT_CANYON_PREVENTS
;                                        ;       end case
53DA:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
53DC:             00 9C                  ;         COM_00_move_and_look(room=RM_5_CANYON_FLOOR)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5367

; --------------------------------------------------------------------------------------------------------------------
;
53DE: 9E 59 00                           ; ----- Room 0x9E RM_5_DESERT_STRANGE_FOOTPRINTS1, Length: 0x0059, Data: 0x00
;
53E1:    03 42                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0042 (to 0x5425)
53E3:       0D 40                        ;     COM_0D_group_AND length=0x0040 (to 0x5425)
53E5:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
53E6:          96                        ;       FN_96_PRINT_VAST_CANYON
53E7:          04 3C                     ;       COM_04_print_message length=0x003C (to 0x5425)
53E9:             0C BA 91 48 48 5E 46 A0 F3 A6 CD 9A 3F 16 F3 46
53F9:             47 B9 53 BE 79 68 4A 90 2F 62 56 F4 FB 72 57 17
5409:             5B 61 6B BF B3 A0 50 6D 7F 49 96 14 82 17 47 5E
5419:             37 5A B8 16 82 17 45 5E A3 48 27 A0
;
;                 STRANGE FOOTPRINTS LEAD SOUTH FROM HERE. THEY SEEM TO
;                 ORIGINATE AT THE EDGE OF THE CANYON.
;
;                                        ;     end group_AND at 0x53E3
;
5425:    04 12                           ;   ---- Section SECTION_04_COMMANDS length=0x0012 (to 0x5439)
5427:       0B 10 0A                     ;     COM_0B_switch length=0x0010 (to 0x543A), function=COM_0A_is_input_phrase(phrase_num)
542A:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
542C:             00 BC                  ;         COM_00_move_and_look(room=RM_5_DESERT9)
;                                        ;       end case
542E:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5430:             00 9F                  ;         COM_00_move_and_look(room=RM_5_DESERT_CANYON3)
;                                        ;       end case
5432:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
5434:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5435:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5437:             00 BD                  ;         COM_00_move_and_look(room=RM_5_DESERT_FOOTPRINTS_LEAD)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5427

; --------------------------------------------------------------------------------------------------------------------
;
5439: 9F 1A 00                           ; ----- Room 0x9F RM_5_DESERT_CANYON3, Length: 0x001A, Data: 0x00
;
543C:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5442)
543E:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5442)
5440:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5441:          96                        ;       FN_96_PRINT_VAST_CANYON
;                                        ;     end group_AND at 0x543E
;
5442:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011 (to 0x5455)
5444:       0B 0F 0A                     ;     COM_0B_switch length=0x000F (to 0x5456), function=COM_0A_is_input_phrase(phrase_num)
5447:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5449:             00 9E                  ;         COM_00_move_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS1)
;                                        ;       end case
544B:          04 01                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0001
544D:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
544E:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
5450:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5451:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5453:             00 BE                  ;         COM_00_move_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5444

; --------------------------------------------------------------------------------------------------------------------
;
5455: A0 44 00                           ; ----- Room 0xA0 RM_5_DESERT_ERRATIC_FOOTPRINTS, Length: 0x0044, Data: 0x00
;
5458:    03 2E                           ;   ---- Section SECTION_03_DESCRIPTION length=0x002E (to 0x5488)
545A:       0D 2C                        ;     COM_0D_group_AND length=0x002C (to 0x5488)
545C:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
545D:          96                        ;       FN_96_PRINT_VAST_CANYON
545E:          04 28                     ;       COM_04_print_message length=0x0028 (to 0x5488)
5460:             3F B9 FA 62 73 49 3C 62 83 49 C8 51 46 A0 F3 A6
5470:             CD 9A 3F 16 F3 46 79 68 56 90 DB 72 95 5F 16 BC
5480:             D6 9C DB 72 47 B9 77 BE
;
;                 SOMEWHAT ERRATIC FOOTPRINTS LEAD FROM THE EAST TO THE SOUTH.
;
;                                        ;     end group_AND at 0x545A
;
5488:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011 (to 0x549B)
548A:       0B 0F 0A                     ;     COM_0B_switch length=0x000F (to 0x549C), function=COM_0A_is_input_phrase(phrase_num)
548D:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
548F:             00 BE                  ;         COM_00_move_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)
;                                        ;       end case
5491:          04 01                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0001
5493:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5494:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
5496:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5497:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5499:             00 BF                  ;         COM_00_move_and_look(room=RM_5_DESERT_WEARY_FOOTPRINTS)
;                                        ;       end case
;                                        ;     end decode_switch at 0x548A

; --------------------------------------------------------------------------------------------------------------------
;
549B: A1 3F 00                           ; ----- Room 0xA1 RM_5_DESERT_WEAVING_FOOTPRINTS, Length: 0x003F, Data: 0x00
;
549E:    03 28                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0028 (to 0x54C8)
54A0:       0D 26                        ;     COM_0D_group_AND length=0x0026 (to 0x54C8)
54A2:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
54A3:          96                        ;       FN_96_PRINT_VAST_CANYON
54A4:          04 22                     ;       COM_04_print_message length=0x0022 (to 0x54C8)
54A6:             A3 D0 10 CB C8 6A 46 A0 F3 A6 CD 9A 3F 16 F3 46
54B6:             79 68 56 90 DB 72 95 5F 16 BC D6 9C DB 72 47 B9
54C6:             77 BE                 
;
;                 WEAVING FOOTPRINTS LEAD FROM THE EAST TO THE SOUTH.
;
;                                        ;     end group_AND at 0x54A0
;
54C8:    04 12                           ;   ---- Section SECTION_04_COMMANDS length=0x0012 (to 0x54DC)
54CA:       0B 10 0A                     ;     COM_0B_switch length=0x0010 (to 0x54DD), function=COM_0A_is_input_phrase(phrase_num)
54CD:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
54CF:             00 BF                  ;         COM_00_move_and_look(room=RM_5_DESERT_WEARY_FOOTPRINTS)
;                                        ;       end case
54D1:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
54D3:             00 A3                  ;         COM_00_move_and_look(room=RM_5_DESERT3)
;                                        ;       end case
54D5:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
54D7:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
54D8:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
54DA:             00 A2                  ;         COM_00_move_and_look(room=RM_5_STRANGE_FOOTPRINTS2)
;                                        ;       end case
;                                        ;     end decode_switch at 0x54CA

; --------------------------------------------------------------------------------------------------------------------
;
54DC: A2 40 00                           ; ----- Room 0xA2 RM_5_STRANGE_FOOTPRINTS2, Length: 0x0040, Data: 0x00
;
54DF:    03 28                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0028 (to 0x5509)
54E1:       0D 26                        ;     COM_0D_group_AND length=0x0026 (to 0x5509)
54E3:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
54E4:          04 23                     ;       COM_04_print_message length=0x0023 (to 0x5509)
54E6:             0C BA 91 48 48 5E 46 A0 F3 A6 CD 9A F7 17 CF 49
54F6:             5C 15 DB 9F 5F BE 99 16 C2 B3 89 17 82 17 47 5E
5506:             66 49 2E              
;
;                 STRANGE FOOTPRINTS WEAVE FROM THE NORTH TO THE EAST.
;
;                                        ;     end group_AND at 0x54E1
;
5509:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x551E)
550B:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x551F), function=COM_0A_is_input_phrase(phrase_num)
550E:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5510:             00 C0                  ;         COM_00_move_and_look(room=RM_5_DESERT_STAGGERING_FOOTPRINTS)
;                                        ;       end case
5512:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5514:             00 A4                  ;         COM_00_move_and_look(room=RM_5_DESERT4)
;                                        ;       end case
5516:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5518:             00 A1                  ;         COM_00_move_and_look(room=RM_5_DESERT_WEAVING_FOOTPRINTS)
;                                        ;       end case
551A:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
551C:             00 A3                  ;         COM_00_move_and_look(room=RM_5_DESERT3)
;                                        ;       end case
;                                        ;     end decode_switch at 0x550B

; --------------------------------------------------------------------------------------------------------------------
;
551E: A3 19 00                           ; ----- Room 0xA3 RM_5_DESERT3, Length: 0x0019, Data: 0x00
;
5521:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5524)
5523:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5524:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5539)
5526:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x553A), function=COM_0A_is_input_phrase(phrase_num)
5529:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
552B:             00 C1                  ;         COM_00_move_and_look(room=RM_5_DESERT_CRAWL_MARKS)
;                                        ;       end case
552D:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
552F:             00 C3                  ;         COM_00_move_and_look(room=RM_5_DESERT11)
;                                        ;       end case
5531:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5533:             00 A2                  ;         COM_00_move_and_look(room=RM_5_STRANGE_FOOTPRINTS2)
;                                        ;       end case
5535:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5537:             00 A4                  ;         COM_00_move_and_look(room=RM_5_DESERT4)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5526

; --------------------------------------------------------------------------------------------------------------------
;
5539: A4 19 00                           ; ----- Room 0xA4 RM_5_DESERT4, Length: 0x0019, Data: 0x00
;
553C:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x553F)
553E:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
553F:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5554)
5541:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5555), function=COM_0A_is_input_phrase(phrase_num)
5544:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5546:             00 C2                  ;         COM_00_move_and_look(room=RM_5_DESERT10)
;                                        ;       end case
5548:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
554A:             00 C4                  ;         COM_00_move_and_look(room=RM_5_DESERT12)
;                                        ;       end case
554C:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
554E:             00 A3                  ;         COM_00_move_and_look(room=RM_5_DESERT3)
;                                        ;       end case
5550:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5552:             00 A5                  ;         COM_00_move_and_look(room=RM_5_DESERT5)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5541

; --------------------------------------------------------------------------------------------------------------------
;
5554: A5 19 00                           ; ----- Room 0xA5 RM_5_DESERT5, Length: 0x0019, Data: 0x00
;
5557:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x555A)
5559:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
555A:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x556F)
555C:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5570), function=COM_0A_is_input_phrase(phrase_num)
555F:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5561:             00 C3                  ;         COM_00_move_and_look(room=RM_5_DESERT11)
;                                        ;       end case
5563:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5565:             00 C2                  ;         COM_00_move_and_look(room=RM_5_DESERT10)
;                                        ;       end case
5567:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5569:             00 A4                  ;         COM_00_move_and_look(room=RM_5_DESERT4)
;                                        ;       end case
556B:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
556D:             00 A6                  ;         COM_00_move_and_look(room=RM_5_DESERT6)
;                                        ;       end case
;                                        ;     end decode_switch at 0x555C

; --------------------------------------------------------------------------------------------------------------------
;
556F: A6 1D 00                           ; ----- Room 0xA6 RM_5_DESERT6, Length: 0x001D, Data: 0x00
;
5572:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5575)
5574:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5575:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x558E)
5577:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x558F), function=COM_0A_is_input_phrase(phrase_num)
557A:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
557C:             00 C4                  ;         COM_00_move_and_look(room=RM_5_DESERT12)
;                                        ;       end case
557E:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5580:             00 C3                  ;         COM_00_move_and_look(room=RM_5_DESERT11)
;                                        ;       end case
5582:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5584:             00 A5                  ;         COM_00_move_and_look(room=RM_5_DESERT5)
;                                        ;       end case
5586:          02 06                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0006
5588:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x558E)
558A:                30 A7               ;           COM_30_set_current_room(room=RM_6_DESERT_EMPTY_HIGHWAY4)
558C:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5588
;                                        ;       end case
;                                        ;     end decode_switch at 0x5577

; --------------------------------------------------------------------------------------------------------------------
;
558E: BA 1D 00                           ; ----- Room 0xBA RM_5_DESERT7, Length: 0x001D, Data: 0x00
;
5591:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5594)
5593:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5594:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x55AD)
5596:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x55AE), function=COM_0A_is_input_phrase(phrase_num)
5599:          03 06                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0006
559B:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x55A1)
559D:                30 B9               ;           COM_30_set_current_room(room=RM_6_DESERT_LAKE4)
559F:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x559B
;                                        ;       end case
55A1:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
55A3:             00 D5                  ;         COM_00_move_and_look(room=RM_5_DESERT14)
;                                        ;       end case
55A5:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
55A7:             00 98                  ;         COM_00_move_and_look(room=RM_5_DESERT2)
;                                        ;       end case
55A9:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
55AB:             00 D3                  ;         COM_00_move_and_look(room=RM_5_DESERT13)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5596

; --------------------------------------------------------------------------------------------------------------------
;
55AD: BB 19 00                           ; ----- Room 0xBB RM_5_DESERT8, Length: 0x0019, Data: 0x00
;
55B0:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x55B3)
55B2:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
55B3:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x55C8)
55B5:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x55C9), function=COM_0A_is_input_phrase(phrase_num)
55B8:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
55BA:             00 98                  ;         COM_00_move_and_look(room=RM_5_DESERT2)
;                                        ;       end case
55BC:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
55BE:             00 BC                  ;         COM_00_move_and_look(room=RM_5_DESERT9)
;                                        ;       end case
55C0:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
55C2:             00 9A                  ;         COM_00_move_and_look(room=RM_5_DESERT_CANYON2)
;                                        ;       end case
55C4:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
55C6:             00 D5                  ;         COM_00_move_and_look(room=RM_5_DESERT14)
;                                        ;       end case
;                                        ;     end decode_switch at 0x55B5

; --------------------------------------------------------------------------------------------------------------------
;
55C8: BC 19 00                           ; ----- Room 0xBC RM_5_DESERT9, Length: 0x0019, Data: 0x00
;
55CB:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x55CE)
55CD:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
55CE:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x55E3)
55D0:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x55E4), function=COM_0A_is_input_phrase(phrase_num)
55D3:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
55D5:             00 BB                  ;         COM_00_move_and_look(room=RM_5_DESERT8)
;                                        ;       end case
55D7:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
55D9:             00 9E                  ;         COM_00_move_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS1)
;                                        ;       end case
55DB:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
55DD:             00 9B                  ;         COM_00_move_and_look(room=RM_5_NARROW_PATH)
;                                        ;       end case
55DF:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
55E1:             00 D6                  ;         COM_00_move_and_look(room=RM_5_DESERT15)
;                                        ;       end case
;                                        ;     end decode_switch at 0x55D0

; --------------------------------------------------------------------------------------------------------------------
;
55E3: BD 35 00                           ; ----- Room 0xBD RM_5_DESERT_FOOTPRINTS_LEAD, Length: 0x0035, Data: 0x00
;
55E6:    03 1D                           ;   ---- Section SECTION_03_DESCRIPTION length=0x001D (to 0x5605)
55E8:       0D 1B                        ;     COM_0D_group_AND length=0x001B (to 0x5605)
55EA:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
55EB:          04 18                     ;       COM_04_print_message length=0x0018 (to 0x5605)
55ED:             01 68 AC BF 9E 7A CE B5 86 5F 5C 15 DB 9F 04 9A
55FD:             53 BE 6B BF B5 D0 9B C1
;
;                 FOOTPRINTS LEAD FROM NORTH TO WEST. 
;
;                                        ;     end group_AND at 0x55E8
;
5605:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x561A)
5607:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x561B), function=COM_0A_is_input_phrase(phrase_num)
560A:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
560C:             00 D6                  ;         COM_00_move_and_look(room=RM_5_DESERT15)
;                                        ;       end case
560E:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5610:             00 BE                  ;         COM_00_move_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)
;                                        ;       end case
5612:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5614:             00 9E                  ;         COM_00_move_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS1)
;                                        ;       end case
5616:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5618:             00 D8                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL3)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5607

; --------------------------------------------------------------------------------------------------------------------
;
561A: BE 3F 00                           ; ----- Room 0xBE RM_5_DESERT_STRANGE_FOOTPRINTS3, Length: 0x003F, Data: 0x00
;
561D:    03 27                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0027 (to 0x5646)
561F:       0D 25                        ;     COM_0D_group_AND length=0x0025 (to 0x5646)
5621:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5622:          04 22                     ;       COM_04_print_message length=0x0022 (to 0x5646)
5624:             0C BA 91 48 48 5E 46 A0 F3 A6 CD 9A 3F 16 F3 46
5634:             79 68 56 90 DB 72 95 5F 16 BC D6 9C DB 72 B5 D0
5644:             9B C1                 
;
;                 STRANGE FOOTPRINTS LEAD FROM THE EAST TO THE WEST. 
;
;                                        ;     end group_AND at 0x561F
;
5646:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x565B)
5648:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x565C), function=COM_0A_is_input_phrase(phrase_num)
564B:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
564D:             00 BD                  ;         COM_00_move_and_look(room=RM_5_DESERT_FOOTPRINTS_LEAD)
;                                        ;       end case
564F:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5651:             00 A0                  ;         COM_00_move_and_look(room=RM_5_DESERT_ERRATIC_FOOTPRINTS)
;                                        ;       end case
5653:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5655:             00 9F                  ;         COM_00_move_and_look(room=RM_5_DESERT_CANYON3)
;                                        ;       end case
5657:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5659:             00 D9                  ;         COM_00_move_and_look(room=RM_5_DESERT16)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5648

; --------------------------------------------------------------------------------------------------------------------
;
565B: BF 3D 00                           ; ----- Room 0xBF RM_5_DESERT_WEARY_FOOTPRINTS, Length: 0x003D, Data: 0x00
;
565E:    03 25                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0025 (to 0x5685)
5660:       0D 23                        ;     COM_0D_group_AND length=0x0023 (to 0x5685)
5662:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5663:          04 20                     ;       COM_04_print_message length=0x0020 (to 0x5685)
5665:             A3 D0 7B B4 01 68 AC BF 9E 7A C9 B5 C8 9C FF B2
5675:             82 17 50 5E BE A0 16 71 D6 9C DB 72 B5 D0 9B C1
;
;                 WEARY FOOTPRINTS GO FROM THE NORTH TO THE WEST. 
;
;                                        ;     end group_AND at 0x5660
;
5685:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x569A)
5687:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x569B), function=COM_0A_is_input_phrase(phrase_num)
568A:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
568C:             00 D9                  ;         COM_00_move_and_look(room=RM_5_DESERT16)
;                                        ;       end case
568E:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5690:             00 A1                  ;         COM_00_move_and_look(room=RM_5_DESERT_WEAVING_FOOTPRINTS)
;                                        ;       end case
5692:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5694:             00 A0                  ;         COM_00_move_and_look(room=RM_5_DESERT_ERRATIC_FOOTPRINTS)
;                                        ;       end case
5696:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5698:             00 C0                  ;         COM_00_move_and_look(room=RM_5_DESERT_STAGGERING_FOOTPRINTS)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5687

; --------------------------------------------------------------------------------------------------------------------
;
569A: C0 41 00                           ; ----- Room 0xC0 RM_5_DESERT_STAGGERING_FOOTPRINTS, Length: 0x0041, Data: 0x00
;
569D:    03 29                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0029 (to 0x56C8)
569F:       0D 27                        ;     COM_0D_group_AND length=0x0027 (to 0x56C8)
56A1:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
56A2:          04 24                     ;       COM_04_print_message length=0x0024 (to 0x56C8)
56A4:             FB B9 F7 6C 10 B2 C8 6A 46 A0 F3 A6 CD 9A 3F 16
56B4:             F3 46 79 68 56 90 DB 72 B5 D0 16 BC D6 9C DB 72
56C4:             47 B9 77 BE           
;
;                 STAGGERING FOOTPRINTS LEAD FROM THE WEST TO THE SOUTH.
;
;                                        ;     end group_AND at 0x569F
;
56C8:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x56DD)
56CA:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x56DE), function=COM_0A_is_input_phrase(phrase_num)
56CD:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
56CF:             00 DA                  ;         COM_00_move_and_look(room=RM_5_DESERT17)
;                                        ;       end case
56D1:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
56D3:             00 A2                  ;         COM_00_move_and_look(room=RM_5_STRANGE_FOOTPRINTS2)
;                                        ;       end case
56D5:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
56D7:             00 BF                  ;         COM_00_move_and_look(room=RM_5_DESERT_WEARY_FOOTPRINTS)
;                                        ;       end case
56D9:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
56DB:             00 C1                  ;         COM_00_move_and_look(room=RM_5_DESERT_CRAWL_MARKS)
;                                        ;       end case
;                                        ;     end decode_switch at 0x56CA

; --------------------------------------------------------------------------------------------------------------------
;
56DD: C1 47 00                           ; ----- Room 0xC1 RM_5_DESERT_CRAWL_MARKS, Length: 0x0047, Data: 0x00
;
56E0:    03 2F                           ;   ---- Section SECTION_03_DESCRIPTION length=0x002F (to 0x5711)
56E2:       0D 2D                        ;     COM_0D_group_AND length=0x002D (to 0x5711)
56E4:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
56E5:          04 2A                     ;       COM_04_print_message length=0x002A (to 0x5711)
56E7:             AB 55 B3 D1 94 91 CB 87 E3 8B 08 58 FF B2 82 17
56F7:             50 5E BE A0 16 71 D6 9C DB 72 95 5F 9B C1 5F BE
5707:             4E DB 3D A0 2F 17 B0 53 9B C1
;
;                 CRAWL MARKS LEAD FROM THE NORTH TO THE EAST. THEY LOOK
;                 RECENT.
;
;                                        ;     end group_AND at 0x56E2
;
5711:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5726)
5713:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5727), function=COM_0A_is_input_phrase(phrase_num)
5716:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5718:             00 DB                  ;         COM_00_move_and_look(room=RM_5_DESERT18)
;                                        ;       end case
571A:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
571C:             00 A3                  ;         COM_00_move_and_look(room=RM_5_DESERT3)
;                                        ;       end case
571E:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5720:             00 C0                  ;         COM_00_move_and_look(room=RM_5_DESERT_STAGGERING_FOOTPRINTS)
;                                        ;       end case
5722:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5724:             00 C2                  ;         COM_00_move_and_look(room=RM_5_DESERT10)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5713

; --------------------------------------------------------------------------------------------------------------------
;
5726: C2 19 00                           ; ----- Room 0xC2 RM_5_DESERT10, Length: 0x0019, Data: 0x00
;
5729:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x572C)
572B:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
572C:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5741)
572E:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5742), function=COM_0A_is_input_phrase(phrase_num)
5731:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5733:             00 DC                  ;         COM_00_move_and_look(room=RM_5_DESERT19)
;                                        ;       end case
5735:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5737:             00 A4                  ;         COM_00_move_and_look(room=RM_5_DESERT4)
;                                        ;       end case
5739:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
573B:             00 C1                  ;         COM_00_move_and_look(room=RM_5_DESERT_CRAWL_MARKS)
;                                        ;       end case
573D:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
573F:             00 C3                  ;         COM_00_move_and_look(room=RM_5_DESERT11)
;                                        ;       end case
;                                        ;     end decode_switch at 0x572E

; --------------------------------------------------------------------------------------------------------------------
;
5741: C3 19 00                           ; ----- Room 0xC3 RM_5_DESERT11, Length: 0x0019, Data: 0x00
;
5744:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5747)
5746:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5747:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x575C)
5749:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x575D), function=COM_0A_is_input_phrase(phrase_num)
574C:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
574E:             00 DD                  ;         COM_00_move_and_look(room=RM_5_DESERT_HIGHWAY_CURVES)
;                                        ;       end case
5750:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5752:             00 A5                  ;         COM_00_move_and_look(room=RM_5_DESERT5)
;                                        ;       end case
5754:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5756:             00 C2                  ;         COM_00_move_and_look(room=RM_5_DESERT10)
;                                        ;       end case
5758:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
575A:             00 C4                  ;         COM_00_move_and_look(room=RM_5_DESERT12)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5749

; --------------------------------------------------------------------------------------------------------------------
;
575C: C4 1D 00                           ; ----- Room 0xC4 RM_5_DESERT12, Length: 0x001D, Data: 0x00
;
575F:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5762)
5761:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5762:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x577B)
5764:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x577C), function=COM_0A_is_input_phrase(phrase_num)
5767:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5769:             00 DE                  ;         COM_00_move_and_look(room=RM_5_DESERT_HIGHWAY_LEADS)
;                                        ;       end case
576B:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
576D:             00 A6                  ;         COM_00_move_and_look(room=RM_5_DESERT6)
;                                        ;       end case
576F:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5771:             00 C3                  ;         COM_00_move_and_look(room=RM_5_DESERT11)
;                                        ;       end case
5773:          02 06                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0006
5775:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x577B)
5777:                30 C5               ;           COM_30_set_current_room(room=RM_6_DESERT_EMPTY_HIGHWAY6)
5779:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5775
;                                        ;       end case
;                                        ;     end decode_switch at 0x5764

; --------------------------------------------------------------------------------------------------------------------
;
577B: D3 1D 00                           ; ----- Room 0xD3 RM_5_DESERT13, Length: 0x001D, Data: 0x00
;
577E:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5781)
5780:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5781:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x579A)
5783:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x579B), function=COM_0A_is_input_phrase(phrase_num)
5786:          03 06                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0006
5788:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x578E)
578A:                30 D2               ;           COM_30_set_current_room(room=RM_6_DESERT72)
578C:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5788
;                                        ;       end case
578E:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5790:             00 D4                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL1)
;                                        ;       end case
5792:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5794:             00 BA                  ;         COM_00_move_and_look(room=RM_5_DESERT7)
;                                        ;       end case
5796:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5798:             00 E8                  ;         COM_00_move_and_look(room=RM_5_DESERT24)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5783

; --------------------------------------------------------------------------------------------------------------------
;
579A: D4 1C 00                           ; ----- Room 0xD4 RM_5_DESERT_TRAIL1, Length: 0x001C, Data: 0x00
;
579D:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x57A3)
579F:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x57A3)
57A1:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
57A2:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;                                        ;     end group_AND at 0x579F
;
57A3:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x57B8)
57A5:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x57B9), function=COM_0A_is_input_phrase(phrase_num)
57A8:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
57AA:             00 D7                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL2)
;                                        ;       end case
57AC:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
57AE:             00 E9                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL4)
;                                        ;       end case
57B0:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
57B2:             00 EA                  ;         COM_00_move_and_look(room=RM_5_DESERT25)
;                                        ;       end case
57B4:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
57B6:             00 BA                  ;         COM_00_move_and_look(room=RM_5_DESERT7)
;                                        ;       end case
;                                        ;     end decode_switch at 0x57A5

; --------------------------------------------------------------------------------------------------------------------
;
57B8: D5 19 00                           ; ----- Room 0xD5 RM_5_DESERT14, Length: 0x0019, Data: 0x00
;
57BB:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x57BE)
57BD:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
57BE:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x57D3)
57C0:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x57D4), function=COM_0A_is_input_phrase(phrase_num)
57C3:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
57C5:             00 BA                  ;         COM_00_move_and_look(room=RM_5_DESERT7)
;                                        ;       end case
57C7:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
57C9:             00 D6                  ;         COM_00_move_and_look(room=RM_5_DESERT15)
;                                        ;       end case
57CB:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
57CD:             00 BB                  ;         COM_00_move_and_look(room=RM_5_DESERT8)
;                                        ;       end case
57CF:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
57D1:             00 D4                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL1)
;                                        ;       end case
;                                        ;     end decode_switch at 0x57C0

; --------------------------------------------------------------------------------------------------------------------
;
57D3: D6 19 00                           ; ----- Room 0xD6 RM_5_DESERT15, Length: 0x0019, Data: 0x00
;
57D6:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x57D9)
57D8:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
57D9:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x57EE)
57DB:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x57EF), function=COM_0A_is_input_phrase(phrase_num)
57DE:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
57E0:             00 D5                  ;         COM_00_move_and_look(room=RM_5_DESERT14)
;                                        ;       end case
57E2:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
57E4:             00 BD                  ;         COM_00_move_and_look(room=RM_5_DESERT_FOOTPRINTS_LEAD)
;                                        ;       end case
57E6:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
57E8:             00 BC                  ;         COM_00_move_and_look(room=RM_5_DESERT9)
;                                        ;       end case
57EA:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
57EC:             00 D7                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL2)
;                                        ;       end case
;                                        ;     end decode_switch at 0x57DB

; --------------------------------------------------------------------------------------------------------------------
;
57EE: D7 1C 00                           ; ----- Room 0xD7 RM_5_DESERT_TRAIL2, Length: 0x001C, Data: 0x00
;
57F1:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x57F7)
57F3:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x57F7)
57F5:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
57F6:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;                                        ;     end group_AND at 0x57F3
;
57F7:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x580C)
57F9:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x580D), function=COM_0A_is_input_phrase(phrase_num)
57FC:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
57FE:             00 D8                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL3)
;                                        ;       end case
5800:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5802:             00 D4                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL1)
;                                        ;       end case
5804:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5806:             00 EA                  ;         COM_00_move_and_look(room=RM_5_DESERT25)
;                                        ;       end case
5808:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
580A:             00 D6                  ;         COM_00_move_and_look(room=RM_5_DESERT15)
;                                        ;       end case
;                                        ;     end decode_switch at 0x57F9

; --------------------------------------------------------------------------------------------------------------------
;
580C: D8 1C 00                           ; ----- Room 0xD8 RM_5_DESERT_TRAIL3, Length: 0x001C, Data: 0x00
;
580F:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5815)
5811:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5815)
5813:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5814:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;                                        ;     end group_AND at 0x5811
;
5815:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x582A)
5817:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x582B), function=COM_0A_is_input_phrase(phrase_num)
581A:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
581C:             00 EB                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL5)
;                                        ;       end case
581E:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5820:             00 D7                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL2)
;                                        ;       end case
5822:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5824:             00 EA                  ;         COM_00_move_and_look(room=RM_5_DESERT25)
;                                        ;       end case
5826:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5828:             00 BE                  ;         COM_00_move_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5817

; --------------------------------------------------------------------------------------------------------------------
;
582A: D9 19 00                           ; ----- Room 0xD9 RM_5_DESERT16, Length: 0x0019, Data: 0x00
;
582D:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5830)
582F:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5830:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5845)
5832:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5846), function=COM_0A_is_input_phrase(phrase_num)
5835:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5837:             00 D8                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL3)
;                                        ;       end case
5839:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
583B:             00 BF                  ;         COM_00_move_and_look(room=RM_5_DESERT_WEARY_FOOTPRINTS)
;                                        ;       end case
583D:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
583F:             00 BE                  ;         COM_00_move_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)
;                                        ;       end case
5841:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5843:             00 DA                  ;         COM_00_move_and_look(room=RM_5_DESERT17)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5832

; --------------------------------------------------------------------------------------------------------------------
;
5845: DA 19 00                           ; ----- Room 0xDA RM_5_DESERT17, Length: 0x0019, Data: 0x00
;
5848:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x584B)
584A:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
584B:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5860)
584D:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5861), function=COM_0A_is_input_phrase(phrase_num)
5850:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5852:             00 EB                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL5)
;                                        ;       end case
5854:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5856:             00 C0                  ;         COM_00_move_and_look(room=RM_5_DESERT_STAGGERING_FOOTPRINTS)
;                                        ;       end case
5858:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
585A:             00 D9                  ;         COM_00_move_and_look(room=RM_5_DESERT16)
;                                        ;       end case
585C:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
585E:             00 DB                  ;         COM_00_move_and_look(room=RM_5_DESERT18)
;                                        ;       end case
;                                        ;     end decode_switch at 0x584D

; --------------------------------------------------------------------------------------------------------------------
;
5860: DB 19 00                           ; ----- Room 0xDB RM_5_DESERT18, Length: 0x0019, Data: 0x00
;
5863:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5866)
5865:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5866:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x587B)
5868:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x587C), function=COM_0A_is_input_phrase(phrase_num)
586B:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
586D:             00 EC                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL6)
;                                        ;       end case
586F:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5871:             00 C1                  ;         COM_00_move_and_look(room=RM_5_DESERT_CRAWL_MARKS)
;                                        ;       end case
5873:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5875:             00 DA                  ;         COM_00_move_and_look(room=RM_5_DESERT17)
;                                        ;       end case
5877:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5879:             00 DC                  ;         COM_00_move_and_look(room=RM_5_DESERT19)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5868

; --------------------------------------------------------------------------------------------------------------------
;
587B: DC 19 00                           ; ----- Room 0xDC RM_5_DESERT19, Length: 0x0019, Data: 0x00
;
587E:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5881)
5880:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5881:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5896)
5883:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5897), function=COM_0A_is_input_phrase(phrase_num)
5886:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5888:             00 ED                  ;         COM_00_move_and_look(room=RM_5_DESERT26)
;                                        ;       end case
588A:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
588C:             00 C2                  ;         COM_00_move_and_look(room=RM_5_DESERT10)
;                                        ;       end case
588E:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5890:             00 DB                  ;         COM_00_move_and_look(room=RM_5_DESERT18)
;                                        ;       end case
5892:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5894:             00 DD                  ;         COM_00_move_and_look(room=RM_5_DESERT_HIGHWAY_CURVES)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5883

; --------------------------------------------------------------------------------------------------------------------
;
5896: DD 40 00                           ; ----- Room 0xDD RM_5_DESERT_HIGHWAY_CURVES, Length: 0x0040, Data: 0x00
;
5899:    03 28                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0028 (to 0x58C3)
589B:       0D 26                        ;     COM_0D_group_AND length=0x0026 (to 0x58C3)
589D:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
589E:          04 23                     ;       COM_04_print_message length=0x0023 (to 0x58C3)
58A0:             5F BE A3 15 31 6D 3B 4A 34 56 75 CA 9F 15 7E B1
58B0:             3F 16 03 47 AB 98 67 5C 23 15 F3 B9 8E 48 61 17
58C0:             82 C6 2E              
;
;                 THE HIGHWAY CURVES HERE, LEADING DUE EAST AND SOUTH.
;
;                                        ;     end group_AND at 0x589B
;
58C3:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x58D8)
58C5:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x58D9), function=COM_0A_is_input_phrase(phrase_num)
58C8:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
58CA:             00 EE                  ;         COM_00_move_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY1)
;                                        ;       end case
58CC:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
58CE:             00 C3                  ;         COM_00_move_and_look(room=RM_5_DESERT11)
;                                        ;       end case
58D0:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
58D2:             00 DC                  ;         COM_00_move_and_look(room=RM_5_DESERT19)
;                                        ;       end case
58D4:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
58D6:             00 DE                  ;         COM_00_move_and_look(room=RM_5_DESERT_HIGHWAY_LEADS)
;                                        ;       end case
;                                        ;     end decode_switch at 0x58C5

; --------------------------------------------------------------------------------------------------------------------
;
58D8: DE 38 00                           ; ----- Room 0xDE RM_5_DESERT_HIGHWAY_LEADS, Length: 0x0038, Data: 0x00
;
58DB:    03 1C                           ;   ---- Section SECTION_03_DESCRIPTION length=0x001C (to 0x58F9)
58DD:       0D 1A                        ;     COM_0D_group_AND length=0x001A (to 0x58F9)
58DF:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
58E0:          04 17                     ;       COM_04_print_message length=0x0017 (to 0x58F9)
58E2:             5F BE A3 15 31 6D 3B 4A E3 8B 0B 5C 04 9A 53 BE
58F2:             8E 48 61 17 82 C6 2E  
;
;                 THE HIGHWAY LEADS NORTH AND SOUTH.
;
;                                        ;     end group_AND at 0x58DD
;
58F9:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5912)
58FB:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x5913), function=COM_0A_is_input_phrase(phrase_num)
58FE:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5900:             00 DF                  ;         COM_00_move_and_look(room=RM_5_DESERT20)
;                                        ;       end case
5902:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5904:             00 C4                  ;         COM_00_move_and_look(room=RM_5_DESERT12)
;                                        ;       end case
5906:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5908:             00 DD                  ;         COM_00_move_and_look(room=RM_5_DESERT_HIGHWAY_CURVES)
;                                        ;       end case
590A:          02 06                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0006
590C:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5912)
590E:                30 C6               ;           COM_30_set_current_room(room=RM_6_DESERT_HIGHWAY_TURNS)
5910:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x590C
;                                        ;       end case
;                                        ;     end decode_switch at 0x58FB

; --------------------------------------------------------------------------------------------------------------------
;
5912: DF 1D 00                           ; ----- Room 0xDF RM_5_DESERT20, Length: 0x001D, Data: 0x00
;
5915:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5918)
5917:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5918:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5931)
591A:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x5932), function=COM_0A_is_input_phrase(phrase_num)
591D:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
591F:             00 E0                  ;         COM_00_move_and_look(room=RM_5_DESERT21)
;                                        ;       end case
5921:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5923:             00 DE                  ;         COM_00_move_and_look(room=RM_5_DESERT_HIGHWAY_LEADS)
;                                        ;       end case
5925:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5927:             00 EE                  ;         COM_00_move_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY1)
;                                        ;       end case
5929:          02 06                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0006
592B:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5931)
592D:                30 C7               ;           COM_30_set_current_room(room=RM_6_DESERT62)
592F:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x592B
;                                        ;       end case
;                                        ;     end decode_switch at 0x591A

; --------------------------------------------------------------------------------------------------------------------
;
5931: E0 1D 00                           ; ----- Room 0xE0 RM_5_DESERT21, Length: 0x001D, Data: 0x00
;
5934:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5937)
5936:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5937:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5950)
5939:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x5951), function=COM_0A_is_input_phrase(phrase_num)
593C:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
593E:             00 E1                  ;         COM_00_move_and_look(room=RM_5_DESERT22)
;                                        ;       end case
5940:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5942:             00 DF                  ;         COM_00_move_and_look(room=RM_5_DESERT20)
;                                        ;       end case
5944:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5946:             00 EF                  ;         COM_00_move_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY2)
;                                        ;       end case
5948:          02 06                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0006
594A:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5950)
594C:                30 C8               ;           COM_30_set_current_room(room=RM_6_DESERT63)
594E:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x594A
;                                        ;       end case
;                                        ;     end decode_switch at 0x5939

; --------------------------------------------------------------------------------------------------------------------
;
5950: E1 25 00                           ; ----- Room 0xE1 RM_5_DESERT22, Length: 0x0025, Data: 0x00
;
5953:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5956)
5955:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5956:    04 1F                           ;   ---- Section SECTION_04_COMMANDS length=0x001F (to 0x5977)
5958:       0B 1D 0A                     ;     COM_0B_switch length=0x001D (to 0x5978), function=COM_0A_is_input_phrase(phrase_num)
595B:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
595D:             00 E2                  ;         COM_00_move_and_look(room=RM_5_DESERT23)
;                                        ;       end case
595F:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5961:             00 E0                  ;         COM_00_move_and_look(room=RM_5_DESERT21)
;                                        ;       end case
5963:          01 0A                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x000A
5965:             0D 08                  ;         COM_0D_group_AND length=0x0008 (to 0x596F)
5967:                C8                  ;           FN_C8_BACK_TO_TOWN
5968:                30 B3               ;           COM_30_set_current_room(room=RM_3_DESERT1)
596A:                17 9D 00            ;           COM_17_move_object_to(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
596D:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
;                                        ;         end group_AND at 0x5965
;                                        ;       end case
596F:          02 06                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0006
5971:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5977)
5973:                30 C9               ;           COM_30_set_current_room(room=RM_6_DESERT64)
5975:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5971
;                                        ;       end case
;                                        ;     end decode_switch at 0x5958

; --------------------------------------------------------------------------------------------------------------------
;
5977: E2 21 00                           ; ----- Room 0xE2 RM_5_DESERT23, Length: 0x0021, Data: 0x00
;
597A:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x597D)
597C:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
597D:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B (to 0x599A)
597F:       0B 19 0A                     ;     COM_0B_switch length=0x0019 (to 0x599B), function=COM_0A_is_input_phrase(phrase_num)
5982:          03 06                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0006
5984:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x598A)
5986:                30 E3               ;           COM_30_set_current_room(room=RM_6_DESERT73)
5988:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5984
;                                        ;       end case
598A:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
598C:             00 E1                  ;         COM_00_move_and_look(room=RM_5_DESERT22)
;                                        ;       end case
598E:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5990:             00 F0                  ;         COM_00_move_and_look(room=RM_5_EMPTY_HIGHWAY_DESERT)
;                                        ;       end case
5992:          02 06                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0006
5994:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x599A)
5996:                30 CA               ;           COM_30_set_current_room(room=RM_6_DESERT65)
5998:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5994
;                                        ;       end case
;                                        ;     end decode_switch at 0x597F

; --------------------------------------------------------------------------------------------------------------------
;
599A: E8 1D 00                           ; ----- Room 0xE8 RM_5_DESERT24, Length: 0x001D, Data: 0x00
;
599D:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x59A0)
599F:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
59A0:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x59B9)
59A2:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x59BA), function=COM_0A_is_input_phrase(phrase_num)
59A5:          03 06                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0006
59A7:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x59AD)
59A9:                30 E7               ;           COM_30_set_current_room(room=RM_6_DESERT76)
59AB:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x59A7
;                                        ;       end case
59AD:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
59AF:             00 E9                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL4)
;                                        ;       end case
59B1:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
59B3:             00 D3                  ;         COM_00_move_and_look(room=RM_5_DESERT13)
;                                        ;       end case
59B5:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
59B7:             00 F2                  ;         COM_00_move_and_look(room=RM_5_DESERT_TWISTY_TRAIL)
;                                        ;       end case
;                                        ;     end decode_switch at 0x59A2

; --------------------------------------------------------------------------------------------------------------------
;
59B9: E9 1C 00                           ; ----- Room 0xE9 RM_5_DESERT_TRAIL4, Length: 0x001C, Data: 0x00
;
59BC:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x59C2)
59BE:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x59C2)
59C0:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
59C1:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;                                        ;     end group_AND at 0x59BE
;
59C2:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x59D7)
59C4:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x59D8), function=COM_0A_is_input_phrase(phrase_num)
59C7:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
59C9:             00 D4                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL1)
;                                        ;       end case
59CB:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
59CD:             00 F3                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL_FORKS)
;                                        ;       end case
59CF:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
59D1:             00 EA                  ;         COM_00_move_and_look(room=RM_5_DESERT25)
;                                        ;       end case
59D3:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
59D5:             00 E8                  ;         COM_00_move_and_look(room=RM_5_DESERT24)
;                                        ;       end case
;                                        ;     end decode_switch at 0x59C4

; --------------------------------------------------------------------------------------------------------------------
;
59D7: EA 19 00                           ; ----- Room 0xEA RM_5_DESERT25, Length: 0x0019, Data: 0x00
;
59DA:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x59DD)
59DC:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
59DD:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x59F2)
59DF:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x59F3), function=COM_0A_is_input_phrase(phrase_num)
59E2:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
59E4:             00 E9                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL4)
;                                        ;       end case
59E6:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
59E8:             00 EB                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL5)
;                                        ;       end case
59EA:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
59EC:             00 D7                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL2)
;                                        ;       end case
59EE:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
59F0:             00 F4                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL7)
;                                        ;       end case
;                                        ;     end decode_switch at 0x59DF

; --------------------------------------------------------------------------------------------------------------------
;
59F2: EB 1C 00                           ; ----- Room 0xEB RM_5_DESERT_TRAIL5, Length: 0x001C, Data: 0x00
;
59F5:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x59FB)
59F7:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x59FB)
59F9:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
59FA:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;                                        ;     end group_AND at 0x59F7
;
59FB:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5A10)
59FD:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5A11), function=COM_0A_is_input_phrase(phrase_num)
5A00:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5A02:             00 EC                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL6)
;                                        ;       end case
5A04:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5A06:             00 D8                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL3)
;                                        ;       end case
5A08:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5A0A:             00 EA                  ;         COM_00_move_and_look(room=RM_5_DESERT25)
;                                        ;       end case
5A0C:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5A0E:             00 DA                  ;         COM_00_move_and_look(room=RM_5_DESERT17)
;                                        ;       end case
;                                        ;     end decode_switch at 0x59FD

; --------------------------------------------------------------------------------------------------------------------
;
5A10: EC 1C 00                           ; ----- Room 0xEC RM_5_DESERT_TRAIL6, Length: 0x001C, Data: 0x00
;
5A13:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5A19)
5A15:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5A19)
5A17:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5A18:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;                                        ;     end group_AND at 0x5A15
;
5A19:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5A2E)
5A1B:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5A2F), function=COM_0A_is_input_phrase(phrase_num)
5A1E:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5A20:             00 F4                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL7)
;                                        ;       end case
5A22:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5A24:             00 EB                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL5)
;                                        ;       end case
5A26:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5A28:             00 EA                  ;         COM_00_move_and_look(room=RM_5_DESERT25)
;                                        ;       end case
5A2A:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5A2C:             00 DC                  ;         COM_00_move_and_look(room=RM_5_DESERT19)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5A1B

; --------------------------------------------------------------------------------------------------------------------
;
5A2E: ED 19 00                           ; ----- Room 0xED RM_5_DESERT26, Length: 0x0019, Data: 0x00
;
5A31:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5A34)
5A33:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5A34:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5A49)
5A36:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5A4A), function=COM_0A_is_input_phrase(phrase_num)
5A39:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5A3B:             00 F5                  ;         COM_00_move_and_look(room=RM_5_DESERT27)
;                                        ;       end case
5A3D:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5A3F:             00 DC                  ;         COM_00_move_and_look(room=RM_5_DESERT19)
;                                        ;       end case
5A41:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5A43:             00 EC                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL6)
;                                        ;       end case
5A45:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5A47:             00 EE                  ;         COM_00_move_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY1)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5A36

; --------------------------------------------------------------------------------------------------------------------
;
5A49: EE 1C 00                           ; ----- Room 0xEE RM_5_DESERT_EMPTY_HIGHWAY1, Length: 0x001C, Data: 0x00
;
5A4C:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5A52)
5A4E:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5A52)
5A50:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5A51:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;                                        ;     end group_AND at 0x5A4E
;
5A52:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5A67)
5A54:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5A68), function=COM_0A_is_input_phrase(phrase_num)
5A57:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5A59:             00 EF                  ;         COM_00_move_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY2)
;                                        ;       end case
5A5B:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5A5D:             00 DD                  ;         COM_00_move_and_look(room=RM_5_DESERT_HIGHWAY_CURVES)
;                                        ;       end case
5A5F:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5A61:             00 ED                  ;         COM_00_move_and_look(room=RM_5_DESERT26)
;                                        ;       end case
5A63:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5A65:             00 DF                  ;         COM_00_move_and_look(room=RM_5_DESERT20)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5A54

; --------------------------------------------------------------------------------------------------------------------
;
5A67: EF 24 00                           ; ----- Room 0xEF RM_5_DESERT_EMPTY_HIGHWAY2, Length: 0x0024, Data: 0x00
;
5A6A:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5A70)
5A6C:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5A70)
5A6E:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5A6F:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;                                        ;     end group_AND at 0x5A6C
;
5A70:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B (to 0x5A8D)
5A72:       0B 19 0A                     ;     COM_0B_switch length=0x0019 (to 0x5A8E), function=COM_0A_is_input_phrase(phrase_num)
5A75:          03 0A                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x000A
5A77:             0D 08                  ;         COM_0D_group_AND length=0x0008 (to 0x5A81)
5A79:                C8                  ;           FN_C8_BACK_TO_TOWN
5A7A:                30 80               ;           COM_30_set_current_room(room=RM_1_HIGHWAY_WEST)
5A7C:                17 9D 00            ;           COM_17_move_object_to(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
5A7F:                2F 01               ;           COM_2F_load_section_from_disk(section=1)
;                                        ;         end group_AND at 0x5A77
;                                        ;       end case
5A81:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5A83:             00 EE                  ;         COM_00_move_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY1)
;                                        ;       end case
5A85:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5A87:             00 F5                  ;         COM_00_move_and_look(room=RM_5_DESERT27)
;                                        ;       end case
5A89:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5A8B:             00 E0                  ;         COM_00_move_and_look(room=RM_5_DESERT21)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5A72

; --------------------------------------------------------------------------------------------------------------------
;
5A8D: F0 28 00                           ; ----- Room 0xF0 RM_5_EMPTY_HIGHWAY_DESERT, Length: 0x0028, Data: 0x00
;
5A90:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5A96)
5A92:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5A96)
5A94:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
5A95:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
;                                        ;     end group_AND at 0x5A92
;
5A96:    04 1F                           ;   ---- Section SECTION_04_COMMANDS length=0x001F (to 0x5AB7)
5A98:       0B 1D 0A                     ;     COM_0B_switch length=0x001D (to 0x5AB8), function=COM_0A_is_input_phrase(phrase_num)
5A9B:          03 06                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0006
5A9D:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5AA3)
5A9F:                30 E4               ;           COM_30_set_current_room(room=RM_6_DESERT_EMPTY_HIGHWAY8)
5AA1:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5A9D
;                                        ;       end case
5AA3:          04 0A                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x000A
5AA5:             0D 08                  ;         COM_0D_group_AND length=0x0008 (to 0x5AAF)
5AA7:                C8                  ;           FN_C8_BACK_TO_TOWN
5AA8:                30 B4               ;           COM_30_set_current_room(room=RM_4_HIGHWAY_EAST)
5AAA:                17 9D 00            ;           COM_17_move_object_to(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
5AAD:                2F 04               ;           COM_2F_load_section_from_disk(section=4)
;                                        ;         end group_AND at 0x5AA5
;                                        ;       end case
5AAF:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5AB1:             00 F1                  ;         COM_00_move_and_look(room=RM_5_DESERT_SMALL_TRAIL1)
;                                        ;       end case
5AB3:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5AB5:             00 E2                  ;         COM_00_move_and_look(room=RM_5_DESERT23)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5A98

; --------------------------------------------------------------------------------------------------------------------
;
5AB7: F1 3F 00                           ; ----- Room 0xF1 RM_5_DESERT_SMALL_TRAIL1, Length: 0x003F, Data: 0x00
;
5ABA:    03 23                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0023 (to 0x5ADF)
5ABC:       0D 21                        ;     COM_0D_group_AND length=0x0021 (to 0x5ADF)
5ABE:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5ABF:          04 1E                     ;       COM_04_print_message length=0x001E (to 0x5ADF)
5AC1:             55 45 8E 91 16 8A CB B0 0E 8A 86 5F D9 B5 66 62
5AD1:             90 14 10 58 BE A0 08 71 FF B2 9F 15 7F B1
;
;                 A SMALL TRAIL LEADS WEST AND NORTH FROM HERE.
;
;                                        ;     end group_AND at 0x5ABC
;
5ADF:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5AF8)
5AE1:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x5AF9), function=COM_0A_is_input_phrase(phrase_num)
5AE4:          03 06                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0006
5AE6:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5AEC)
5AE8:                30 E5               ;           COM_30_set_current_room(room=RM_6_DESERT74)
5AEA:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5AE6
;                                        ;       end case
5AEC:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5AEE:             00 F6                  ;         COM_00_move_and_look(room=RM_5_DESERT_SMALL_TRAIL2)
;                                        ;       end case
5AF0:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5AF2:             00 F2                  ;         COM_00_move_and_look(room=RM_5_DESERT_TWISTY_TRAIL)
;                                        ;       end case
5AF4:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5AF6:             00 F0                  ;         COM_00_move_and_look(room=RM_5_EMPTY_HIGHWAY_DESERT)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5AE1

; --------------------------------------------------------------------------------------------------------------------
;
5AF8: F2 41 00                           ; ----- Room 0xF2 RM_5_DESERT_TWISTY_TRAIL, Length: 0x0041, Data: 0x00
;
5AFB:    03 25                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0025 (to 0x5B22)
5AFD:       0D 23                        ;     COM_0D_group_AND length=0x0023 (to 0x5B22)
5AFF:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5B00:          04 20                     ;       COM_04_print_message length=0x0020 (to 0x5B22)
5B02:             55 45 8E 91 16 8A 55 D1 FB C0 EB BF 33 7A E3 8B
5B12:             0B 5C B5 D0 03 BC 33 98 47 B9 53 BE F4 72 DB 63
;
;                 A SMALL TWISTY TRAIL LEADS WEST AND SOUTH HERE. 
;
;                                        ;     end group_AND at 0x5AFD
;
5B22:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5B3B)
5B24:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x5B3C), function=COM_0A_is_input_phrase(phrase_num)
5B27:          03 06                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0006
5B29:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5B2F)
5B2B:                30 E6               ;           COM_30_set_current_room(room=RM_6_DESERT75)
5B2D:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
;                                        ;         end group_AND at 0x5B29
;                                        ;       end case
5B2F:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5B31:             00 F3                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL_FORKS)
;                                        ;       end case
5B33:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5B35:             00 E8                  ;         COM_00_move_and_look(room=RM_5_DESERT24)
;                                        ;       end case
5B37:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5B39:             00 F1                  ;         COM_00_move_and_look(room=RM_5_DESERT_SMALL_TRAIL1)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5B24

; --------------------------------------------------------------------------------------------------------------------
;
5B3B: F3 35 00                           ; ----- Room 0xF3 RM_5_DESERT_TRAIL_FORKS, Length: 0x0035, Data: 0x00
;
5B3E:    03 1D                           ;   ---- Section SECTION_03_DESCRIPTION length=0x001D (to 0x5B5D)
5B40:       0D 1B                        ;     COM_0D_group_AND length=0x001B (to 0x5B5D)
5B42:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5B43:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
5B44:          04 17                     ;       COM_04_print_message length=0x0017 (to 0x5B5D)
5B46:             5F BE 8C 17 CE 47 8E 14 2B B9 04 68 CB 87 6B BF
5B56:             5F BE 61 17 82 C6 2E  
;
;                 THE TRAIL ALSO FORKS TO THE SOUTH.
;
;                                        ;     end group_AND at 0x5B40
;
5B5D:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5B72)
5B5F:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5B73), function=COM_0A_is_input_phrase(phrase_num)
5B62:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5B64:             00 E9                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL4)
;                                        ;       end case
5B66:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5B68:             00 F4                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL7)
;                                        ;       end case
5B6A:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5B6C:             00 EA                  ;         COM_00_move_and_look(room=RM_5_DESERT25)
;                                        ;       end case
5B6E:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5B70:             00 F1                  ;         COM_00_move_and_look(room=RM_5_DESERT_SMALL_TRAIL1)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5B5F

; --------------------------------------------------------------------------------------------------------------------
;
5B72: F4 1C 00                           ; ----- Room 0xF4 RM_5_DESERT_TRAIL7, Length: 0x001C, Data: 0x00
;
5B75:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5B7B)
5B77:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5B7B)
5B79:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5B7A:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;                                        ;     end group_AND at 0x5B77
;
5B7B:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5B90)
5B7D:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5B91), function=COM_0A_is_input_phrase(phrase_num)
5B80:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5B82:             00 F3                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL_FORKS)
;                                        ;       end case
5B84:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5B86:             00 EC                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL6)
;                                        ;       end case
5B88:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5B8A:             00 EA                  ;         COM_00_move_and_look(room=RM_5_DESERT25)
;                                        ;       end case
5B8C:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5B8E:             00 F5                  ;         COM_00_move_and_look(room=RM_5_DESERT27)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5B7D

; --------------------------------------------------------------------------------------------------------------------
;
5B90: F5 19 00                           ; ----- Room 0xF5 RM_5_DESERT27, Length: 0x0019, Data: 0x00
;
5B93:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5B96)
5B95:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5B96:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5BAB)
5B98:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5BAC), function=COM_0A_is_input_phrase(phrase_num)
5B9B:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5B9D:             00 F6                  ;         COM_00_move_and_look(room=RM_5_DESERT_SMALL_TRAIL2)
;                                        ;       end case
5B9F:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5BA1:             00 ED                  ;         COM_00_move_and_look(room=RM_5_DESERT26)
;                                        ;       end case
5BA3:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5BA5:             00 F4                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL7)
;                                        ;       end case
5BA7:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5BA9:             00 EF                  ;         COM_00_move_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY2)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5B98

; --------------------------------------------------------------------------------------------------------------------
;
5BAB: F6 45 00                           ; ----- Room 0xF6 RM_5_DESERT_SMALL_TRAIL2, Length: 0x0045, Data: 0x00
;
5BAE:    03 25                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0025 (to 0x5BD5)
5BB0:       0D 23                        ;     COM_0D_group_AND length=0x0023 (to 0x5BD5)
5BB2:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5BB3:          04 20                     ;       COM_04_print_message length=0x0020 (to 0x5BD5)
5BB5:             55 45 8E 91 16 8A CB B0 0E 8A 86 5F C8 B5 FF B2
5BC5:             82 17 55 5E 36 A1 16 71 D6 9C DB 72 95 5F 9B C1
;
;                 A SMALL TRAIL LEADS FROM THE SOUTH TO THE EAST. 
;
;                                        ;     end group_AND at 0x5BB0
;
5BD5:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B (to 0x5BF2)
5BD7:       0B 19 0A                     ;     COM_0B_switch length=0x0019 (to 0x5BF3), function=COM_0A_is_input_phrase(phrase_num)
5BDA:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5BDC:             00 F1                  ;         COM_00_move_and_look(room=RM_5_DESERT_SMALL_TRAIL1)
;                                        ;       end case
5BDE:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5BE0:             00 F5                  ;         COM_00_move_and_look(room=RM_5_DESERT27)
;                                        ;       end case
5BE2:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5BE4:             00 F3                  ;         COM_00_move_and_look(room=RM_5_DESERT_TRAIL_FORKS)
;                                        ;       end case
5BE6:          02 0A                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x000A
5BE8:             0D 08                  ;         COM_0D_group_AND length=0x0008 (to 0x5BF2)
5BEA:                C8                  ;           FN_C8_BACK_TO_TOWN
5BEB:                30 B7               ;           COM_30_set_current_room(room=RM_2_DESERT_PATH)
5BED:                17 9D 00            ;           COM_17_move_object_to(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
5BF0:                2F 02               ;           COM_2F_load_section_from_disk(section=2)
;                                        ;         end group_AND at 0x5BE8
;                                        ;       end case
;                                        ;     end decode_switch at 0x5BD7

; --------------------------------------------------------------------------------------------------------------------
;
5BF2: F7 19 00                           ; ----- Room 0xF7 RM_5_DESERT28, Length: 0x0019, Data: 0x00
;
5BF5:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5BF8)
5BF7:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5BF8:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5C0D)
5BFA:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5C0E), function=COM_0A_is_input_phrase(phrase_num)
5BFD:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5BFF:             00 FA                  ;         COM_00_move_and_look(room=RM_5_DESERT31)
;                                        ;       end case
5C01:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5C03:             00 F7                  ;         COM_00_move_and_look(room=RM_5_DESERT28)
;                                        ;       end case
5C05:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5C07:             00 F7                  ;         COM_00_move_and_look(room=RM_5_DESERT28)
;                                        ;       end case
5C09:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5C0B:             00 F8                  ;         COM_00_move_and_look(room=RM_5_DESERT29)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5BFA

; --------------------------------------------------------------------------------------------------------------------
;
5C0D: F8 19 00                           ; ----- Room 0xF8 RM_5_DESERT29, Length: 0x0019, Data: 0x00
;
5C10:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5C13)
5C12:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5C13:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5C28)
5C15:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5C29), function=COM_0A_is_input_phrase(phrase_num)
5C18:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5C1A:             00 F8                  ;         COM_00_move_and_look(room=RM_5_DESERT29)
;                                        ;       end case
5C1C:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5C1E:             00 F9                  ;         COM_00_move_and_look(room=RM_5_DESERT30)
;                                        ;       end case
5C20:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5C22:             00 F8                  ;         COM_00_move_and_look(room=RM_5_DESERT29)
;                                        ;       end case
5C24:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5C26:             00 F8                  ;         COM_00_move_and_look(room=RM_5_DESERT29)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5C15

; --------------------------------------------------------------------------------------------------------------------
;
5C28: F9 21 00                           ; ----- Room 0xF9 RM_5_DESERT30, Length: 0x0021, Data: 0x00
;
5C2B:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5C2E)
5C2D:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5C2E:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B (to 0x5C4B)
5C30:       0B 19 0A                     ;     COM_0B_switch length=0x0019 (to 0x5C4C), function=COM_0A_is_input_phrase(phrase_num)
5C33:          03 0A                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x000A
5C35:             0E 08                  ;         COM_0E_group_OR length=0x0008 (to 0x5C3F)
5C37:                0D 04               ;           COM_0D_group_AND length=0x0004 (to 0x5C3D)
5C39:                   05 3E            ;             COM_05_is_leq_last_random(value=62)
5C3B:                   00 86            ;             COM_00_move_and_look(room=RM_5_86_??)
;                                        ;           end group_AND at 0x5C37
5C3D:                00 F9               ;           COM_00_move_and_look(room=RM_5_DESERT30)
;                                        ;         end group_OR at 0x5C35
;                                        ;       end case
5C3F:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5C41:             00 F8                  ;         COM_00_move_and_look(room=RM_5_DESERT29)
;                                        ;       end case
5C43:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5C45:             00 FA                  ;         COM_00_move_and_look(room=RM_5_DESERT31)
;                                        ;       end case
5C47:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5C49:             00 F9                  ;         COM_00_move_and_look(room=RM_5_DESERT30)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5C30

; --------------------------------------------------------------------------------------------------------------------
;
5C4B: FA 19 00                           ; ----- Room 0xFA RM_5_DESERT31, Length: 0x0019, Data: 0x00
;
5C4E:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5C51)
5C50:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5C51:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5C66)
5C53:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5C67), function=COM_0A_is_input_phrase(phrase_num)
5C56:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5C58:             00 FA                  ;         COM_00_move_and_look(room=RM_5_DESERT31)
;                                        ;       end case
5C5A:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5C5C:             00 F7                  ;         COM_00_move_and_look(room=RM_5_DESERT28)
;                                        ;       end case
5C5E:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5C60:             00 FA                  ;         COM_00_move_and_look(room=RM_5_DESERT31)
;                                        ;       end case
5C62:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5C64:             00 F9                  ;         COM_00_move_and_look(room=RM_5_DESERT30)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5C53
```

# Unitialized data

```code
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

