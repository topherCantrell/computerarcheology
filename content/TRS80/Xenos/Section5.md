![Xenos](Xenos.png)

# Xenos SECTION5.DAT

>>> cpu Z80

>>> binary 5200:roms/section5.bin

```code
5200: 00 8A 63                           ; List_ID=0x00, length=0x0A63

; --------------------------------------------------------------------------------------------------------------------
;
5203: 98 1D 00                           ; ----- Room 0x98 RM_5_DESERT2, Length: 0x001D, Data: 0x00
;
5206:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5208:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5209:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
520B:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
520E:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
520F:          06                        ;       ELSE goto=0x5216
5210:             0D 04                  ;         COM_0D_while_pass length=0x0004
5212:                30 97               ;           COM_30_set_current_room(room=RM_6_DESERT_CANYON4)
5214:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
5216:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5217:          02                        ;       ELSE goto=0x521A
5218:             00 BB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT8)
521A:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
521B:          02                        ;       ELSE goto=0x521E
521C:             00 99                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CANYON1)
521E:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
521F:          02                        ;       ELSE goto=0x5222
5220:             00 BA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT7)

; --------------------------------------------------------------------------------------------------------------------
;
5222: 99 1A 00                           ; ----- Room 0x99 RM_5_DESERT_CANYON1, Length: 0x001A, Data: 0x00
;
5225:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
5227:       0D 02                        ;     COM_0D_while_pass length=0x0002
5229:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
522A:          96                        ;       FN_96_PRINT_VAST_CANYON
;
522B:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011
522D:       0B 0F 0A                     ;     COM_0B_switch length=0x000F, function=COM_0A_is_input_phrase(phrase_num)
5230:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5231:          01                        ;       ELSE goto=0x5233
5232:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
5233:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5234:          02                        ;       ELSE goto=0x5237
5235:             00 9A                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CANYON2)
5237:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5238:          01                        ;       ELSE goto=0x523A
5239:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
523A:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
523B:          02                        ;       ELSE goto=0x523E
523C:             00 98                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT2)

; --------------------------------------------------------------------------------------------------------------------
;
523E: 9A 1A 00                           ; ----- Room 0x9A RM_5_DESERT_CANYON2, Length: 0x001A, Data: 0x00
;
5241:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
5243:       0D 02                        ;     COM_0D_while_pass length=0x0002
5245:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5246:          96                        ;       FN_96_PRINT_VAST_CANYON
;
5247:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011
5249:       0B 0F 0A                     ;     COM_0B_switch length=0x000F, function=COM_0A_is_input_phrase(phrase_num)
524C:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
524D:          02                        ;       ELSE goto=0x5250
524E:             00 99                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CANYON1)
5250:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5251:          01                        ;       ELSE goto=0x5253
5252:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
5253:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5254:          01                        ;       ELSE goto=0x5256
5255:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
5256:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5257:          02                        ;       ELSE goto=0x525A
5258:             00 BB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT8)

; --------------------------------------------------------------------------------------------------------------------
;
525A: 9B 62 00                           ; ----- Room 0x9B RM_5_NARROW_PATH, Length: 0x0062, Data: 0x00
;
525D:    03 45                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0045
525F:       04 43                        ;     COM_04_print_message length=0x0043
5261:          C7 DE 94 14 51 5E 83 96 8B 16 79 B3 D2 CE 82 49 ; 
5271:          82 17 73 49 E3 8B 0B 5C 89 5B 96 96 DB 72 C5 65 ; 
5281:          51 5E 96 64 DB 72 C3 54 83 66 6B BF 5F BE 99 16 ; 
5291:          C2 B3 4B F4 0B BC D8 B5 43 62 8C 17 85 5F F4 72 ; 
52A1:          35 A1 21                  ; 
;
;              YOU ARE ON A NARROW PATH THAT LEADS DOWN THE FACE OF THE
;              CLIFF TO THE NORTH. IT IS VERY TREACHEROUS!
;
;
52A4:    04 18                           ;   ---- Section SECTION_04_COMMANDS length=0x0018
52A6:       0B 16 0A                     ;     COM_0B_switch length=0x0016, function=COM_0A_is_input_phrase(phrase_num)
52A9:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
52AA:          01                        ;       ELSE goto=0x52AC
52AB:             99                     ;         FN_99_DIE_CANYON_PLUNGE
52AC:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
52AD:          01                        ;       ELSE goto=0x52AF
52AE:             99                     ;         FN_99_DIE_CANYON_PLUNGE
52AF:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
52B0:          09                        ;       ELSE goto=0x52BA
52B1:             0E 07                  ;         COM_0E_while_fail length=0x0007
52B3:                0D 04               ;           COM_0D_while_pass length=0x0004
52B5:                   05 F0            ;             COM_05_is_less_equal_last_random(value=240)
52B7:                   00 9C            ;             COM_00_move_ACTIVE_and_look(room=RM_5_CANYON_FLOOR)
52B9:                99                  ;           FN_99_DIE_CANYON_PLUNGE
52BA:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
52BB:          02                        ;       ELSE goto=0x52BE
52BC:             00 BC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT9)

; --------------------------------------------------------------------------------------------------------------------
;
52BE: 9C 68 00                           ; ----- Room 0x9C RM_5_CANYON_FLOOR, Length: 0x0068, Data: 0x00
;
52C1:    03 52                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0052
52C3:       04 50                        ;     COM_04_print_message length=0x0050
52C5:          C7 DE 94 14 50 5E 6B A1 03 A0 5F BE D3 14 91 9B ; 
52D5:          88 96 81 8D 1B B5 6B BF 5F BE F7 17 F3 B9 C7 DE ; 
52E5:          D3 14 95 96 1B 60 4E 45 31 49 45 5E D6 B0 23 62 ; 
52F5:          56 D1 03 71 EB 14 90 8C F3 5B 0E 53 67 16 4E BD ; 
5305:          CB 78 34 9E E6 5F 2F 17 03 BA AB 98 83 7A 97 7B ; 
;
;              YOU ARE NOW ON THE CANYON FLOOR. TO THE WEST YOU CAN SEE A
;              LARGE CRATER WITH A CYLINDRICAL METALIC OBJECT RESTING IN
;              IT.
;
;
5315:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011
5317:       0B 0F 0A                     ;     COM_0B_switch length=0x000F, function=COM_0A_is_input_phrase(phrase_num)
531A:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
531B:          01                        ;       ELSE goto=0x531D
531C:             9A                     ;         FN_9A_PRINT_CANYON_PREVENTS
531D:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
531E:          02                        ;       ELSE goto=0x5321
531F:             00 9D                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_UFO_CRATER)
5321:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5322:          01                        ;       ELSE goto=0x5324
5323:             9A                     ;         FN_9A_PRINT_CANYON_PREVENTS
5324:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5325:          02                        ;       ELSE goto=0x5328
5326:             00 9B                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_NARROW_PATH)

; --------------------------------------------------------------------------------------------------------------------
;
5328: 9D 80 B3 00                        ; ----- Room 0x9D RM_5_UFO_CRATER, Length: 0x00B3, Data: 0x00
;
532C:    03 37                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0037
532E:       04 35                        ;     COM_04_print_message length=0x0035
5330:          C7 DE 94 14 50 5E 6B A1 83 7A 5F BE E4 14 7F 49 ; 
5340:          99 AF F4 72 43 5E A8 17 CA 9C 4B 49 50 8B E6 59 ; 
5350:          D6 06 DB 72 AB 55 F4 BD C2 16 9D 61 89 17 82 17 ; 
5360:          47 5E 66 49 2E            ; 
;
;              YOU ARE NOW IN THE CRATER WHERE A UFO HAS LANDED! THE
;              CRATER OPENS TO THE EAST.
;
;
5365:    04 77                           ;   ---- Section SECTION_04_COMMANDS length=0x0077
5367:       0B 75 0A                     ;     COM_0B_switch length=0x0075, function=COM_0A_is_input_phrase(phrase_num)
536A:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
536B:          2D                        ;       ELSE goto=0x5399
536C:             0E 2B                  ;         COM_0E_while_fail length=0x002B
536E:                0D 20               ;           COM_0D_while_pass length=0x0020
5370:                   01 4E            ;             COM_01_is_in_pack_or_room(obj=OBJ_4E_BOULDER)
5372:                   04 1C            ;             COM_04_print_message length=0x001C
5374:                      5F BE B9 14 3E C5 23 62 89 4E A5 54 DB 16 D3 B9 ; 
5384:                      9B 6C 9E 7A D6 9C DB 72 23 B8 9B A8 ; 
;
;                          THE BOULDER BLOCKS PASSAGE INTO THE SHIP. 
;
5390:                0D 07               ;           COM_0D_while_pass length=0x0007
5392:                   30 80            ;             COM_30_set_current_room(room=RM_7_EXIT1)
5394:                   17 9D 00         ;             COM_17_move_object_to_destination(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
5397:                   2F 07            ;             COM_2F_load_section_from_disk(section=7)
5399:          36                        ;       COM_0A_is_input_phrase("ENTER * * *")
539A:          39                        ;       ELSE goto=0x53D4
539B:             0E 37                  ;         COM_0E_while_fail length=0x0037
539D:                0D 26               ;           COM_0D_while_pass length=0x0026
539F:                   0E 04            ;             COM_0E_while_fail length=0x0004
53A1:                      09 00         ;               COM_09_compare_to_second_noun(obj=nothing)
53A3:                      09 99         ;               COM_09_compare_to_second_noun(obj=OBJ_99_SHIP)
53A5:                   01 4E            ;             COM_01_is_in_pack_or_room(obj=OBJ_4E_BOULDER)
53A7:                   04 1C            ;             COM_04_print_message length=0x001C
53A9:                      5F BE B9 14 3E C5 23 62 89 4E A5 54 DB 16 D3 B9 ; 
53B9:                      9B 6C 9E 7A D6 9C DB 72 23 B8 9B A8 ; 
;
;                          THE BOULDER BLOCKS PASSAGE INTO THE SHIP. 
;
53C5:                0D 0D               ;           COM_0D_while_pass length=0x000D
53C7:                   0E 04            ;             COM_0E_while_fail length=0x0004
53C9:                      09 00         ;               COM_09_compare_to_second_noun(obj=nothing)
53CB:                      09 99         ;               COM_09_compare_to_second_noun(obj=OBJ_99_SHIP)
53CD:                   30 80            ;             COM_30_set_current_room(room=RM_7_EXIT1)
53CF:                   17 9D 00         ;             COM_17_move_object_to_destination(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
53D2:                   2F 07            ;             COM_2F_load_section_from_disk(section=7)
53D4:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
53D5:          01                        ;       ELSE goto=0x53D7
53D6:             9A                     ;         FN_9A_PRINT_CANYON_PREVENTS
53D7:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
53D8:          01                        ;       ELSE goto=0x53DA
53D9:             9A                     ;         FN_9A_PRINT_CANYON_PREVENTS
53DA:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
53DB:          02                        ;       ELSE goto=0x53DE
53DC:             00 9C                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_CANYON_FLOOR)

; --------------------------------------------------------------------------------------------------------------------
;
53DE: 9E 59 00                           ; ----- Room 0x9E RM_5_STRANGE_FOOTPRINTS1, Length: 0x0059, Data: 0x00
;
53E1:    03 42                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0042
53E3:       0D 40                        ;     COM_0D_while_pass length=0x0040
53E5:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
53E6:          96                        ;       FN_96_PRINT_VAST_CANYON
53E7:          04 3C                     ;       COM_04_print_message length=0x003C
53E9:             0C BA 91 48 48 5E 46 A0 F3 A6 CD 9A 3F 16 F3 46 ; 
53F9:             47 B9 53 BE 79 68 4A 90 2F 62 56 F4 FB 72 57 17 ; 
5409:             5B 61 6B BF B3 A0 50 6D 7F 49 96 14 82 17 47 5E ; 
5419:             37 5A B8 16 82 17 45 5E A3 48 27 A0 ; 
;
;                 STRANGE FOOTPRINTS LEAD SOUTH FROM HERE. THEY SEEM TO
;                 ORIGINATE AT THE EDGE OF THE CANYON.
;
;
5425:    04 12                           ;   ---- Section SECTION_04_COMMANDS length=0x0012
5427:       0B 10 0A                     ;     COM_0B_switch length=0x0010, function=COM_0A_is_input_phrase(phrase_num)
542A:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
542B:          02                        ;       ELSE goto=0x542E
542C:             00 BC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT9)
542E:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
542F:          02                        ;       ELSE goto=0x5432
5430:             00 9F                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CANYON3)
5432:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5433:          01                        ;       ELSE goto=0x5435
5434:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
5435:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5436:          02                        ;       ELSE goto=0x5439
5437:             00 BD                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_FOOTPRINTS_LEAD)

; --------------------------------------------------------------------------------------------------------------------
;
5439: 9F 1A 00                           ; ----- Room 0x9F RM_5_DESERT_CANYON3, Length: 0x001A, Data: 0x00
;
543C:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
543E:       0D 02                        ;     COM_0D_while_pass length=0x0002
5440:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5441:          96                        ;       FN_96_PRINT_VAST_CANYON
;
5442:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011
5444:       0B 0F 0A                     ;     COM_0B_switch length=0x000F, function=COM_0A_is_input_phrase(phrase_num)
5447:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5448:          02                        ;       ELSE goto=0x544B
5449:             00 9E                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_STRANGE_FOOTPRINTS1)
544B:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
544C:          01                        ;       ELSE goto=0x544E
544D:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
544E:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
544F:          01                        ;       ELSE goto=0x5451
5450:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
5451:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5452:          02                        ;       ELSE goto=0x5455
5453:             00 BE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)

; --------------------------------------------------------------------------------------------------------------------
;
5455: A0 44 00                           ; ----- Room 0xA0 RM_5_ERRATIC_FOOTPRINTS, Length: 0x0044, Data: 0x00
;
5458:    03 2E                           ;   ---- Section SECTION_03_DESCRIPTION length=0x002E
545A:       0D 2C                        ;     COM_0D_while_pass length=0x002C
545C:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
545D:          96                        ;       FN_96_PRINT_VAST_CANYON
545E:          04 28                     ;       COM_04_print_message length=0x0028
5460:             3F B9 FA 62 73 49 3C 62 83 49 C8 51 46 A0 F3 A6 ; 
5470:             CD 9A 3F 16 F3 46 79 68 56 90 DB 72 95 5F 16 BC ; 
5480:             D6 9C DB 72 47 B9 77 BE ; 
;
;                 SOMEWHAT ERRATIC FOOTPRINTS LEAD FROM THE EAST TO THE SOUTH.
;
;
5488:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011
548A:       0B 0F 0A                     ;     COM_0B_switch length=0x000F, function=COM_0A_is_input_phrase(phrase_num)
548D:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
548E:          02                        ;       ELSE goto=0x5491
548F:             00 BE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)
5491:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5492:          01                        ;       ELSE goto=0x5494
5493:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
5494:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5495:          01                        ;       ELSE goto=0x5497
5496:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
5497:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5498:          02                        ;       ELSE goto=0x549B
5499:             00 BF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_WEARY_FOOTPRINTS)

; --------------------------------------------------------------------------------------------------------------------
;
549B: A1 3F 00                           ; ----- Room 0xA1 RM_5_WEAVING_FOOTPRINTS, Length: 0x003F, Data: 0x00
;
549E:    03 28                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0028
54A0:       0D 26                        ;     COM_0D_while_pass length=0x0026
54A2:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
54A3:          96                        ;       FN_96_PRINT_VAST_CANYON
54A4:          04 22                     ;       COM_04_print_message length=0x0022
54A6:             A3 D0 10 CB C8 6A 46 A0 F3 A6 CD 9A 3F 16 F3 46 ; 
54B6:             79 68 56 90 DB 72 95 5F 16 BC D6 9C DB 72 47 B9 ; 
54C6:             77 BE                  ; 
;
;                 WEAVING FOOTPRINTS LEAD FROM THE EAST TO THE SOUTH.
;
;
54C8:    04 12                           ;   ---- Section SECTION_04_COMMANDS length=0x0012
54CA:       0B 10 0A                     ;     COM_0B_switch length=0x0010, function=COM_0A_is_input_phrase(phrase_num)
54CD:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
54CE:          02                        ;       ELSE goto=0x54D1
54CF:             00 BF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_WEARY_FOOTPRINTS)
54D1:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
54D2:          02                        ;       ELSE goto=0x54D5
54D3:             00 A3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT3)
54D5:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
54D6:          01                        ;       ELSE goto=0x54D8
54D7:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
54D8:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
54D9:          02                        ;       ELSE goto=0x54DC
54DA:             00 A2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_STRANGE_FOOTPRINTS2)

; --------------------------------------------------------------------------------------------------------------------
;
54DC: A2 40 00                           ; ----- Room 0xA2 RM_5_STRANGE_FOOTPRINTS2, Length: 0x0040, Data: 0x00
;
54DF:    03 28                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0028
54E1:       0D 26                        ;     COM_0D_while_pass length=0x0026
54E3:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
54E4:          04 23                     ;       COM_04_print_message length=0x0023
54E6:             0C BA 91 48 48 5E 46 A0 F3 A6 CD 9A F7 17 CF 49 ; 
54F6:             5C 15 DB 9F 5F BE 99 16 C2 B3 89 17 82 17 47 5E ; 
5506:             66 49 2E               ; 
;
;                 STRANGE FOOTPRINTS WEAVE FROM THE NORTH TO THE EAST.
;
;
5509:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
550B:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
550E:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
550F:          02                        ;       ELSE goto=0x5512
5510:             00 C0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_STAGGERING_FOOTPRINTS)
5512:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5513:          02                        ;       ELSE goto=0x5516
5514:             00 A4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT4)
5516:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5517:          02                        ;       ELSE goto=0x551A
5518:             00 A1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_WEAVING_FOOTPRINTS)
551A:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
551B:          02                        ;       ELSE goto=0x551E
551C:             00 A3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT3)

; --------------------------------------------------------------------------------------------------------------------
;
551E: A3 19 00                           ; ----- Room 0xA3 RM_5_DESERT3, Length: 0x0019, Data: 0x00
;
5521:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5523:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5524:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5526:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5529:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
552A:          02                        ;       ELSE goto=0x552D
552B:             00 C1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CRAWL_MARKS)
552D:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
552E:          02                        ;       ELSE goto=0x5531
552F:             00 C3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT11)
5531:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5532:          02                        ;       ELSE goto=0x5535
5533:             00 A2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_STRANGE_FOOTPRINTS2)
5535:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5536:          02                        ;       ELSE goto=0x5539
5537:             00 A4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT4)

; --------------------------------------------------------------------------------------------------------------------
;
5539: A4 19 00                           ; ----- Room 0xA4 RM_5_DESERT4, Length: 0x0019, Data: 0x00
;
553C:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
553E:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
553F:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5541:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5544:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5545:          02                        ;       ELSE goto=0x5548
5546:             00 C2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT10)
5548:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5549:          02                        ;       ELSE goto=0x554C
554A:             00 C4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT12)
554C:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
554D:          02                        ;       ELSE goto=0x5550
554E:             00 A3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT3)
5550:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5551:          02                        ;       ELSE goto=0x5554
5552:             00 A5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT5)

; --------------------------------------------------------------------------------------------------------------------
;
5554: A5 19 00                           ; ----- Room 0xA5 RM_5_DESERT5, Length: 0x0019, Data: 0x00
;
5557:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5559:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
555A:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
555C:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
555F:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5560:          02                        ;       ELSE goto=0x5563
5561:             00 C3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT11)
5563:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5564:          02                        ;       ELSE goto=0x5567
5565:             00 C2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT10)
5567:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5568:          02                        ;       ELSE goto=0x556B
5569:             00 A4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT4)
556B:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
556C:          02                        ;       ELSE goto=0x556F
556D:             00 A6                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT6)

; --------------------------------------------------------------------------------------------------------------------
;
556F: A6 1D 00                           ; ----- Room 0xA6 RM_5_DESERT6, Length: 0x001D, Data: 0x00
;
5572:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5574:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5575:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5577:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
557A:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
557B:          02                        ;       ELSE goto=0x557E
557C:             00 C4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT12)
557E:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
557F:          02                        ;       ELSE goto=0x5582
5580:             00 C3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT11)
5582:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5583:          02                        ;       ELSE goto=0x5586
5584:             00 A5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT5)
5586:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5587:          06                        ;       ELSE goto=0x558E
5588:             0D 04                  ;         COM_0D_while_pass length=0x0004
558A:                30 A7               ;           COM_30_set_current_room(room=RM_6_DESERT_EMPTY_HIGHWAY4)
558C:                2F 06               ;           COM_2F_load_section_from_disk(section=6)

; --------------------------------------------------------------------------------------------------------------------
;
558E: BA 1D 00                           ; ----- Room 0xBA RM_5_DESERT7, Length: 0x001D, Data: 0x00
;
5591:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5593:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5594:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5596:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
5599:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
559A:          06                        ;       ELSE goto=0x55A1
559B:             0D 04                  ;         COM_0D_while_pass length=0x0004
559D:                30 B9               ;           COM_30_set_current_room(room=RM_6_DESERT_LAKE4)
559F:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
55A1:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
55A2:          02                        ;       ELSE goto=0x55A5
55A3:             00 D5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT14)
55A5:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
55A6:          02                        ;       ELSE goto=0x55A9
55A7:             00 98                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT2)
55A9:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
55AA:          02                        ;       ELSE goto=0x55AD
55AB:             00 D3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT13)

; --------------------------------------------------------------------------------------------------------------------
;
55AD: BB 19 00                           ; ----- Room 0xBB RM_5_DESERT8, Length: 0x0019, Data: 0x00
;
55B0:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
55B2:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
55B3:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
55B5:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
55B8:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
55B9:          02                        ;       ELSE goto=0x55BC
55BA:             00 98                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT2)
55BC:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
55BD:          02                        ;       ELSE goto=0x55C0
55BE:             00 BC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT9)
55C0:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
55C1:          02                        ;       ELSE goto=0x55C4
55C2:             00 9A                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CANYON2)
55C4:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
55C5:          02                        ;       ELSE goto=0x55C8
55C6:             00 D5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT14)

; --------------------------------------------------------------------------------------------------------------------
;
55C8: BC 19 00                           ; ----- Room 0xBC RM_5_DESERT9, Length: 0x0019, Data: 0x00
;
55CB:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
55CD:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
55CE:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
55D0:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
55D3:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
55D4:          02                        ;       ELSE goto=0x55D7
55D5:             00 BB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT8)
55D7:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
55D8:          02                        ;       ELSE goto=0x55DB
55D9:             00 9E                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_STRANGE_FOOTPRINTS1)
55DB:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
55DC:          02                        ;       ELSE goto=0x55DF
55DD:             00 9B                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_NARROW_PATH)
55DF:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
55E0:          02                        ;       ELSE goto=0x55E3
55E1:             00 D6                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT15)

; --------------------------------------------------------------------------------------------------------------------
;
55E3: BD 35 00                           ; ----- Room 0xBD RM_5_DESERT_FOOTPRINTS_LEAD, Length: 0x0035, Data: 0x00
;
55E6:    03 1D                           ;   ---- Section SECTION_03_DESCRIPTION length=0x001D
55E8:       0D 1B                        ;     COM_0D_while_pass length=0x001B
55EA:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
55EB:          04 18                     ;       COM_04_print_message length=0x0018
55ED:             01 68 AC BF 9E 7A CE B5 86 5F 5C 15 DB 9F 04 9A ; 
55FD:             53 BE 6B BF B5 D0 9B C1 ; 
;
;                 FOOTPRINTS LEAD FROM NORTH TO WEST. 
;
;
5605:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5607:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
560A:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
560B:          02                        ;       ELSE goto=0x560E
560C:             00 D6                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT15)
560E:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
560F:          02                        ;       ELSE goto=0x5612
5610:             00 BE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)
5612:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5613:          02                        ;       ELSE goto=0x5616
5614:             00 9E                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_STRANGE_FOOTPRINTS1)
5616:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5617:          02                        ;       ELSE goto=0x561A
5618:             00 D8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL3)

; --------------------------------------------------------------------------------------------------------------------
;
561A: BE 3F 00                           ; ----- Room 0xBE RM_5_DESERT_STRANGE_FOOTPRINTS3, Length: 0x003F, Data: 0x00
;
561D:    03 27                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0027
561F:       0D 25                        ;     COM_0D_while_pass length=0x0025
5621:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5622:          04 22                     ;       COM_04_print_message length=0x0022
5624:             0C BA 91 48 48 5E 46 A0 F3 A6 CD 9A 3F 16 F3 46 ; 
5634:             79 68 56 90 DB 72 95 5F 16 BC D6 9C DB 72 B5 D0 ; 
5644:             9B C1                  ; 
;
;                 STRANGE FOOTPRINTS LEAD FROM THE EAST TO THE WEST. 
;
;
5646:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5648:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
564B:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
564C:          02                        ;       ELSE goto=0x564F
564D:             00 BD                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_FOOTPRINTS_LEAD)
564F:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5650:          02                        ;       ELSE goto=0x5653
5651:             00 A0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_ERRATIC_FOOTPRINTS)
5653:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5654:          02                        ;       ELSE goto=0x5657
5655:             00 9F                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CANYON3)
5657:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5658:          02                        ;       ELSE goto=0x565B
5659:             00 D9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT16)

; --------------------------------------------------------------------------------------------------------------------
;
565B: BF 3D 00                           ; ----- Room 0xBF RM_5_DESERT_WEARY_FOOTPRINTS, Length: 0x003D, Data: 0x00
;
565E:    03 25                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0025
5660:       0D 23                        ;     COM_0D_while_pass length=0x0023
5662:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5663:          04 20                     ;       COM_04_print_message length=0x0020
5665:             A3 D0 7B B4 01 68 AC BF 9E 7A C9 B5 C8 9C FF B2 ; 
5675:             82 17 50 5E BE A0 16 71 D6 9C DB 72 B5 D0 9B C1 ; 
;
;                 WEARY FOOTPRINTS GO FROM THE NORTH TO THE WEST. 
;
;
5685:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5687:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
568A:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
568B:          02                        ;       ELSE goto=0x568E
568C:             00 D9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT16)
568E:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
568F:          02                        ;       ELSE goto=0x5692
5690:             00 A1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_WEAVING_FOOTPRINTS)
5692:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5693:          02                        ;       ELSE goto=0x5696
5694:             00 A0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_ERRATIC_FOOTPRINTS)
5696:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5697:          02                        ;       ELSE goto=0x569A
5698:             00 C0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_STAGGERING_FOOTPRINTS)

; --------------------------------------------------------------------------------------------------------------------
;
569A: C0 41 00                           ; ----- Room 0xC0 RM_5_DESERT_STAGGERING_FOOTPRINTS, Length: 0x0041, Data: 0x00
;
569D:    03 29                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0029
569F:       0D 27                        ;     COM_0D_while_pass length=0x0027
56A1:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
56A2:          04 24                     ;       COM_04_print_message length=0x0024
56A4:             FB B9 F7 6C 10 B2 C8 6A 46 A0 F3 A6 CD 9A 3F 16 ; 
56B4:             F3 46 79 68 56 90 DB 72 B5 D0 16 BC D6 9C DB 72 ; 
56C4:             47 B9 77 BE            ; 
;
;                 STAGGERING FOOTPRINTS LEAD FROM THE WEST TO THE SOUTH.
;
;
56C8:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
56CA:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
56CD:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
56CE:          02                        ;       ELSE goto=0x56D1
56CF:             00 DA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT17)
56D1:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
56D2:          02                        ;       ELSE goto=0x56D5
56D3:             00 A2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_STRANGE_FOOTPRINTS2)
56D5:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
56D6:          02                        ;       ELSE goto=0x56D9
56D7:             00 BF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_WEARY_FOOTPRINTS)
56D9:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
56DA:          02                        ;       ELSE goto=0x56DD
56DB:             00 C1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CRAWL_MARKS)

; --------------------------------------------------------------------------------------------------------------------
;
56DD: C1 47 00                           ; ----- Room 0xC1 RM_5_DESERT_CRAWL_MARKS, Length: 0x0047, Data: 0x00
;
56E0:    03 2F                           ;   ---- Section SECTION_03_DESCRIPTION length=0x002F
56E2:       0D 2D                        ;     COM_0D_while_pass length=0x002D
56E4:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
56E5:          04 2A                     ;       COM_04_print_message length=0x002A
56E7:             AB 55 B3 D1 94 91 CB 87 E3 8B 08 58 FF B2 82 17 ; 
56F7:             50 5E BE A0 16 71 D6 9C DB 72 95 5F 9B C1 5F BE ; 
5707:             4E DB 3D A0 2F 17 B0 53 9B C1 ; 
;
;                 CRAWL MARKS LEAD FROM THE NORTH TO THE EAST. THEY LOOK
;                 RECENT.
;
;
5711:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5713:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5716:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5717:          02                        ;       ELSE goto=0x571A
5718:             00 DB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT18)
571A:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
571B:          02                        ;       ELSE goto=0x571E
571C:             00 A3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT3)
571E:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
571F:          02                        ;       ELSE goto=0x5722
5720:             00 C0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_STAGGERING_FOOTPRINTS)
5722:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5723:          02                        ;       ELSE goto=0x5726
5724:             00 C2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT10)

; --------------------------------------------------------------------------------------------------------------------
;
5726: C2 19 00                           ; ----- Room 0xC2 RM_5_DESERT10, Length: 0x0019, Data: 0x00
;
5729:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
572B:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
572C:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
572E:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5731:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5732:          02                        ;       ELSE goto=0x5735
5733:             00 DC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT19)
5735:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5736:          02                        ;       ELSE goto=0x5739
5737:             00 A4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT4)
5739:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
573A:          02                        ;       ELSE goto=0x573D
573B:             00 C1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CRAWL_MARKS)
573D:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
573E:          02                        ;       ELSE goto=0x5741
573F:             00 C3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT11)

; --------------------------------------------------------------------------------------------------------------------
;
5741: C3 19 00                           ; ----- Room 0xC3 RM_5_DESERT11, Length: 0x0019, Data: 0x00
;
5744:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5746:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5747:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5749:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
574C:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
574D:          02                        ;       ELSE goto=0x5750
574E:             00 DD                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_HIGHWAY_CURVES)
5750:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5751:          02                        ;       ELSE goto=0x5754
5752:             00 A5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT5)
5754:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5755:          02                        ;       ELSE goto=0x5758
5756:             00 C2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT10)
5758:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5759:          02                        ;       ELSE goto=0x575C
575A:             00 C4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT12)

; --------------------------------------------------------------------------------------------------------------------
;
575C: C4 1D 00                           ; ----- Room 0xC4 RM_5_DESERT12, Length: 0x001D, Data: 0x00
;
575F:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5761:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5762:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5764:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
5767:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5768:          02                        ;       ELSE goto=0x576B
5769:             00 DE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_HIGHWAY_LEADS)
576B:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
576C:          02                        ;       ELSE goto=0x576F
576D:             00 A6                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT6)
576F:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5770:          02                        ;       ELSE goto=0x5773
5771:             00 C3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT11)
5773:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5774:          06                        ;       ELSE goto=0x577B
5775:             0D 04                  ;         COM_0D_while_pass length=0x0004
5777:                30 C5               ;           COM_30_set_current_room(room=RM_6_DESERT_EMPTY_HIGHWAY6)
5779:                2F 06               ;           COM_2F_load_section_from_disk(section=6)

; --------------------------------------------------------------------------------------------------------------------
;
577B: D3 1D 00                           ; ----- Room 0xD3 RM_5_DESERT13, Length: 0x001D, Data: 0x00
;
577E:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5780:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5781:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5783:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
5786:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5787:          06                        ;       ELSE goto=0x578E
5788:             0D 04                  ;         COM_0D_while_pass length=0x0004
578A:                30 D2               ;           COM_30_set_current_room(room=RM_6_DESERT72)
578C:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
578E:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
578F:          02                        ;       ELSE goto=0x5792
5790:             00 D4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL1)
5792:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5793:          02                        ;       ELSE goto=0x5796
5794:             00 BA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT7)
5796:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5797:          02                        ;       ELSE goto=0x579A
5798:             00 E8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT24)

; --------------------------------------------------------------------------------------------------------------------
;
579A: D4 1C 00                           ; ----- Room 0xD4 RM_5_DESERT_TRAIL1, Length: 0x001C, Data: 0x00
;
579D:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
579F:       0D 02                        ;     COM_0D_while_pass length=0x0002
57A1:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
57A2:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;
57A3:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
57A5:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
57A8:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
57A9:          02                        ;       ELSE goto=0x57AC
57AA:             00 D7                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL2)
57AC:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
57AD:          02                        ;       ELSE goto=0x57B0
57AE:             00 E9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL4)
57B0:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
57B1:          02                        ;       ELSE goto=0x57B4
57B2:             00 EA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT25)
57B4:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
57B5:          02                        ;       ELSE goto=0x57B8
57B6:             00 BA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT7)

; --------------------------------------------------------------------------------------------------------------------
;
57B8: D5 19 00                           ; ----- Room 0xD5 RM_5_DESERT14, Length: 0x0019, Data: 0x00
;
57BB:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
57BD:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
57BE:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
57C0:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
57C3:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
57C4:          02                        ;       ELSE goto=0x57C7
57C5:             00 BA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT7)
57C7:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
57C8:          02                        ;       ELSE goto=0x57CB
57C9:             00 D6                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT15)
57CB:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
57CC:          02                        ;       ELSE goto=0x57CF
57CD:             00 BB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT8)
57CF:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
57D0:          02                        ;       ELSE goto=0x57D3
57D1:             00 D4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL1)

; --------------------------------------------------------------------------------------------------------------------
;
57D3: D6 19 00                           ; ----- Room 0xD6 RM_5_DESERT15, Length: 0x0019, Data: 0x00
;
57D6:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
57D8:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
57D9:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
57DB:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
57DE:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
57DF:          02                        ;       ELSE goto=0x57E2
57E0:             00 D5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT14)
57E2:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
57E3:          02                        ;       ELSE goto=0x57E6
57E4:             00 BD                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_FOOTPRINTS_LEAD)
57E6:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
57E7:          02                        ;       ELSE goto=0x57EA
57E8:             00 BC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT9)
57EA:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
57EB:          02                        ;       ELSE goto=0x57EE
57EC:             00 D7                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL2)

; --------------------------------------------------------------------------------------------------------------------
;
57EE: D7 1C 00                           ; ----- Room 0xD7 RM_5_DESERT_TRAIL2, Length: 0x001C, Data: 0x00
;
57F1:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
57F3:       0D 02                        ;     COM_0D_while_pass length=0x0002
57F5:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
57F6:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;
57F7:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
57F9:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
57FC:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
57FD:          02                        ;       ELSE goto=0x5800
57FE:             00 D8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL3)
5800:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5801:          02                        ;       ELSE goto=0x5804
5802:             00 D4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL1)
5804:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5805:          02                        ;       ELSE goto=0x5808
5806:             00 EA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT25)
5808:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5809:          02                        ;       ELSE goto=0x580C
580A:             00 D6                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT15)

; --------------------------------------------------------------------------------------------------------------------
;
580C: D8 1C 00                           ; ----- Room 0xD8 RM_5_DESERT_TRAIL3, Length: 0x001C, Data: 0x00
;
580F:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
5811:       0D 02                        ;     COM_0D_while_pass length=0x0002
5813:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5814:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;
5815:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5817:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
581A:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
581B:          02                        ;       ELSE goto=0x581E
581C:             00 EB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL5)
581E:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
581F:          02                        ;       ELSE goto=0x5822
5820:             00 D7                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL2)
5822:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5823:          02                        ;       ELSE goto=0x5826
5824:             00 EA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT25)
5826:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5827:          02                        ;       ELSE goto=0x582A
5828:             00 BE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)

; --------------------------------------------------------------------------------------------------------------------
;
582A: D9 19 00                           ; ----- Room 0xD9 RM_5_DESERT16, Length: 0x0019, Data: 0x00
;
582D:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
582F:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5830:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5832:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5835:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5836:          02                        ;       ELSE goto=0x5839
5837:             00 D8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL3)
5839:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
583A:          02                        ;       ELSE goto=0x583D
583B:             00 BF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_WEARY_FOOTPRINTS)
583D:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
583E:          02                        ;       ELSE goto=0x5841
583F:             00 BE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_STRANGE_FOOTPRINTS3)
5841:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5842:          02                        ;       ELSE goto=0x5845
5843:             00 DA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT17)

; --------------------------------------------------------------------------------------------------------------------
;
5845: DA 19 00                           ; ----- Room 0xDA RM_5_DESERT17, Length: 0x0019, Data: 0x00
;
5848:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
584A:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
584B:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
584D:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5850:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5851:          02                        ;       ELSE goto=0x5854
5852:             00 EB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL5)
5854:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5855:          02                        ;       ELSE goto=0x5858
5856:             00 C0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_STAGGERING_FOOTPRINTS)
5858:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5859:          02                        ;       ELSE goto=0x585C
585A:             00 D9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT16)
585C:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
585D:          02                        ;       ELSE goto=0x5860
585E:             00 DB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT18)

; --------------------------------------------------------------------------------------------------------------------
;
5860: DB 19 00                           ; ----- Room 0xDB RM_5_DESERT18, Length: 0x0019, Data: 0x00
;
5863:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5865:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5866:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5868:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
586B:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
586C:          02                        ;       ELSE goto=0x586F
586D:             00 EC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL6)
586F:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5870:          02                        ;       ELSE goto=0x5873
5871:             00 C1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_CRAWL_MARKS)
5873:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5874:          02                        ;       ELSE goto=0x5877
5875:             00 DA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT17)
5877:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5878:          02                        ;       ELSE goto=0x587B
5879:             00 DC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT19)

; --------------------------------------------------------------------------------------------------------------------
;
587B: DC 19 00                           ; ----- Room 0xDC RM_5_DESERT19, Length: 0x0019, Data: 0x00
;
587E:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5880:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5881:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5883:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5886:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5887:          02                        ;       ELSE goto=0x588A
5888:             00 ED                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT26)
588A:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
588B:          02                        ;       ELSE goto=0x588E
588C:             00 C2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT10)
588E:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
588F:          02                        ;       ELSE goto=0x5892
5890:             00 DB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT18)
5892:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5893:          02                        ;       ELSE goto=0x5896
5894:             00 DD                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_HIGHWAY_CURVES)

; --------------------------------------------------------------------------------------------------------------------
;
5896: DD 40 00                           ; ----- Room 0xDD RM_5_DESERT_HIGHWAY_CURVES, Length: 0x0040, Data: 0x00
;
5899:    03 28                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0028
589B:       0D 26                        ;     COM_0D_while_pass length=0x0026
589D:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
589E:          04 23                     ;       COM_04_print_message length=0x0023
58A0:             5F BE A3 15 31 6D 3B 4A 34 56 75 CA 9F 15 7E B1 ; 
58B0:             3F 16 03 47 AB 98 67 5C 23 15 F3 B9 8E 48 61 17 ; 
58C0:             82 C6 2E               ; 
;
;                 THE HIGHWAY CURVES HERE, LEADING DUE EAST AND SOUTH.
;
;
58C3:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
58C5:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
58C8:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
58C9:          02                        ;       ELSE goto=0x58CC
58CA:             00 EE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY1)
58CC:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
58CD:          02                        ;       ELSE goto=0x58D0
58CE:             00 C3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT11)
58D0:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
58D1:          02                        ;       ELSE goto=0x58D4
58D2:             00 DC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT19)
58D4:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
58D5:          02                        ;       ELSE goto=0x58D8
58D6:             00 DE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_HIGHWAY_LEADS)

; --------------------------------------------------------------------------------------------------------------------
;
58D8: DE 38 00                           ; ----- Room 0xDE RM_5_DESERT_HIGHWAY_LEADS, Length: 0x0038, Data: 0x00
;
58DB:    03 1C                           ;   ---- Section SECTION_03_DESCRIPTION length=0x001C
58DD:       0D 1A                        ;     COM_0D_while_pass length=0x001A
58DF:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
58E0:          04 17                     ;       COM_04_print_message length=0x0017
58E2:             5F BE A3 15 31 6D 3B 4A E3 8B 0B 5C 04 9A 53 BE ; 
58F2:             8E 48 61 17 82 C6 2E   ; 
;
;                 THE HIGHWAY LEADS NORTH AND SOUTH.
;
;
58F9:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
58FB:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
58FE:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
58FF:          02                        ;       ELSE goto=0x5902
5900:             00 DF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT20)
5902:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5903:          02                        ;       ELSE goto=0x5906
5904:             00 C4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT12)
5906:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5907:          02                        ;       ELSE goto=0x590A
5908:             00 DD                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_HIGHWAY_CURVES)
590A:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
590B:          06                        ;       ELSE goto=0x5912
590C:             0D 04                  ;         COM_0D_while_pass length=0x0004
590E:                30 C6               ;           COM_30_set_current_room(room=RM_6_DESERT_HIGHWAY_TURNS)
5910:                2F 06               ;           COM_2F_load_section_from_disk(section=6)

; --------------------------------------------------------------------------------------------------------------------
;
5912: DF 1D 00                           ; ----- Room 0xDF RM_5_DESERT20, Length: 0x001D, Data: 0x00
;
5915:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5917:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5918:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
591A:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
591D:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
591E:          02                        ;       ELSE goto=0x5921
591F:             00 E0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT21)
5921:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5922:          02                        ;       ELSE goto=0x5925
5923:             00 DE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_HIGHWAY_LEADS)
5925:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5926:          02                        ;       ELSE goto=0x5929
5927:             00 EE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY1)
5929:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
592A:          06                        ;       ELSE goto=0x5931
592B:             0D 04                  ;         COM_0D_while_pass length=0x0004
592D:                30 C7               ;           COM_30_set_current_room(room=RM_6_DESERT62)
592F:                2F 06               ;           COM_2F_load_section_from_disk(section=6)

; --------------------------------------------------------------------------------------------------------------------
;
5931: E0 1D 00                           ; ----- Room 0xE0 RM_5_DESERT21, Length: 0x001D, Data: 0x00
;
5934:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5936:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5937:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5939:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
593C:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
593D:          02                        ;       ELSE goto=0x5940
593E:             00 E1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT22)
5940:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5941:          02                        ;       ELSE goto=0x5944
5942:             00 DF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT20)
5944:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5945:          02                        ;       ELSE goto=0x5948
5946:             00 EF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY2)
5948:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5949:          06                        ;       ELSE goto=0x5950
594A:             0D 04                  ;         COM_0D_while_pass length=0x0004
594C:                30 C8               ;           COM_30_set_current_room(room=RM_6_DESERT63)
594E:                2F 06               ;           COM_2F_load_section_from_disk(section=6)

; --------------------------------------------------------------------------------------------------------------------
;
5950: E1 25 00                           ; ----- Room 0xE1 RM_5_DESERT22, Length: 0x0025, Data: 0x00
;
5953:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5955:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5956:    04 1F                           ;   ---- Section SECTION_04_COMMANDS length=0x001F
5958:       0B 1D 0A                     ;     COM_0B_switch length=0x001D, function=COM_0A_is_input_phrase(phrase_num)
595B:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
595C:          02                        ;       ELSE goto=0x595F
595D:             00 E2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT23)
595F:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5960:          02                        ;       ELSE goto=0x5963
5961:             00 E0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT21)
5963:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5964:          0A                        ;       ELSE goto=0x596F
5965:             0D 08                  ;         COM_0D_while_pass length=0x0008
5967:                C8                  ;           FN_C8_BACK_TO_TOWN
5968:                30 B3               ;           COM_30_set_current_room(room=RM_3_DESERT1)
596A:                17 9D 00            ;           COM_17_move_object_to_destination(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
596D:                2F 03               ;           COM_2F_load_section_from_disk(section=3)
596F:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5970:          06                        ;       ELSE goto=0x5977
5971:             0D 04                  ;         COM_0D_while_pass length=0x0004
5973:                30 C9               ;           COM_30_set_current_room(room=RM_6_DESERT64)
5975:                2F 06               ;           COM_2F_load_section_from_disk(section=6)

; --------------------------------------------------------------------------------------------------------------------
;
5977: E2 21 00                           ; ----- Room 0xE2 RM_5_DESERT23, Length: 0x0021, Data: 0x00
;
597A:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
597C:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
597D:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B
597F:       0B 19 0A                     ;     COM_0B_switch length=0x0019, function=COM_0A_is_input_phrase(phrase_num)
5982:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5983:          06                        ;       ELSE goto=0x598A
5984:             0D 04                  ;         COM_0D_while_pass length=0x0004
5986:                30 E3               ;           COM_30_set_current_room(room=RM_6_DESERT73)
5988:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
598A:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
598B:          02                        ;       ELSE goto=0x598E
598C:             00 E1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT22)
598E:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
598F:          02                        ;       ELSE goto=0x5992
5990:             00 F0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_EMPTY_HIGHWAY_DESERT)
5992:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5993:          06                        ;       ELSE goto=0x599A
5994:             0D 04                  ;         COM_0D_while_pass length=0x0004
5996:                30 CA               ;           COM_30_set_current_room(room=RM_6_DESERT65)
5998:                2F 06               ;           COM_2F_load_section_from_disk(section=6)

; --------------------------------------------------------------------------------------------------------------------
;
599A: E8 1D 00                           ; ----- Room 0xE8 RM_5_DESERT24, Length: 0x001D, Data: 0x00
;
599D:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
599F:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
59A0:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
59A2:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
59A5:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
59A6:          06                        ;       ELSE goto=0x59AD
59A7:             0D 04                  ;         COM_0D_while_pass length=0x0004
59A9:                30 E7               ;           COM_30_set_current_room(room=RM_6_DESERT76)
59AB:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
59AD:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
59AE:          02                        ;       ELSE goto=0x59B1
59AF:             00 E9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL4)
59B1:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
59B2:          02                        ;       ELSE goto=0x59B5
59B3:             00 D3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT13)
59B5:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
59B6:          02                        ;       ELSE goto=0x59B9
59B7:             00 F2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TWISTY_TRAIL)

; --------------------------------------------------------------------------------------------------------------------
;
59B9: E9 1C 00                           ; ----- Room 0xE9 RM_5_DESERT_TRAIL4, Length: 0x001C, Data: 0x00
;
59BC:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
59BE:       0D 02                        ;     COM_0D_while_pass length=0x0002
59C0:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
59C1:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;
59C2:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
59C4:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
59C7:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
59C8:          02                        ;       ELSE goto=0x59CB
59C9:             00 D4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL1)
59CB:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
59CC:          02                        ;       ELSE goto=0x59CF
59CD:             00 F3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL_FORKS)
59CF:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
59D0:          02                        ;       ELSE goto=0x59D3
59D1:             00 EA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT25)
59D3:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
59D4:          02                        ;       ELSE goto=0x59D7
59D5:             00 E8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT24)

; --------------------------------------------------------------------------------------------------------------------
;
59D7: EA 19 00                           ; ----- Room 0xEA RM_5_DESERT25, Length: 0x0019, Data: 0x00
;
59DA:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
59DC:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
59DD:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
59DF:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
59E2:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
59E3:          02                        ;       ELSE goto=0x59E6
59E4:             00 E9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL4)
59E6:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
59E7:          02                        ;       ELSE goto=0x59EA
59E8:             00 EB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL5)
59EA:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
59EB:          02                        ;       ELSE goto=0x59EE
59EC:             00 D7                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL2)
59EE:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
59EF:          02                        ;       ELSE goto=0x59F2
59F0:             00 F4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL7)

; --------------------------------------------------------------------------------------------------------------------
;
59F2: EB 1C 00                           ; ----- Room 0xEB RM_5_DESERT_TRAIL5, Length: 0x001C, Data: 0x00
;
59F5:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
59F7:       0D 02                        ;     COM_0D_while_pass length=0x0002
59F9:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
59FA:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;
59FB:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
59FD:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5A00:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5A01:          02                        ;       ELSE goto=0x5A04
5A02:             00 EC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL6)
5A04:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5A05:          02                        ;       ELSE goto=0x5A08
5A06:             00 D8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL3)
5A08:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5A09:          02                        ;       ELSE goto=0x5A0C
5A0A:             00 EA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT25)
5A0C:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5A0D:          02                        ;       ELSE goto=0x5A10
5A0E:             00 DA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT17)

; --------------------------------------------------------------------------------------------------------------------
;
5A10: EC 1C 00                           ; ----- Room 0xEC RM_5_DESERT_TRAIL6, Length: 0x001C, Data: 0x00
;
5A13:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
5A15:       0D 02                        ;     COM_0D_while_pass length=0x0002
5A17:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5A18:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;
5A19:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5A1B:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5A1E:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5A1F:          02                        ;       ELSE goto=0x5A22
5A20:             00 F4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL7)
5A22:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5A23:          02                        ;       ELSE goto=0x5A26
5A24:             00 EB                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL5)
5A26:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5A27:          02                        ;       ELSE goto=0x5A2A
5A28:             00 EA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT25)
5A2A:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5A2B:          02                        ;       ELSE goto=0x5A2E
5A2C:             00 DC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT19)

; --------------------------------------------------------------------------------------------------------------------
;
5A2E: ED 19 00                           ; ----- Room 0xED RM_5_DESERT26, Length: 0x0019, Data: 0x00
;
5A31:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5A33:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5A34:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5A36:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5A39:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5A3A:          02                        ;       ELSE goto=0x5A3D
5A3B:             00 F5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT27)
5A3D:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5A3E:          02                        ;       ELSE goto=0x5A41
5A3F:             00 DC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT19)
5A41:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5A42:          02                        ;       ELSE goto=0x5A45
5A43:             00 EC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL6)
5A45:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5A46:          02                        ;       ELSE goto=0x5A49
5A47:             00 EE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY1)

; --------------------------------------------------------------------------------------------------------------------
;
5A49: EE 1C 00                           ; ----- Room 0xEE RM_5_DESERT_EMPTY_HIGHWAY1, Length: 0x001C, Data: 0x00
;
5A4C:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
5A4E:       0D 02                        ;     COM_0D_while_pass length=0x0002
5A50:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5A51:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;
5A52:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5A54:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5A57:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5A58:          02                        ;       ELSE goto=0x5A5B
5A59:             00 EF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY2)
5A5B:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5A5C:          02                        ;       ELSE goto=0x5A5F
5A5D:             00 DD                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_HIGHWAY_CURVES)
5A5F:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5A60:          02                        ;       ELSE goto=0x5A63
5A61:             00 ED                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT26)
5A63:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5A64:          02                        ;       ELSE goto=0x5A67
5A65:             00 DF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT20)

; --------------------------------------------------------------------------------------------------------------------
;
5A67: EF 24 00                           ; ----- Room 0xEF RM_5_DESERT_EMPTY_HIGHWAY2, Length: 0x0024, Data: 0x00
;
5A6A:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
5A6C:       0D 02                        ;     COM_0D_while_pass length=0x0002
5A6E:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5A6F:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;
5A70:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B
5A72:       0B 19 0A                     ;     COM_0B_switch length=0x0019, function=COM_0A_is_input_phrase(phrase_num)
5A75:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5A76:          0A                        ;       ELSE goto=0x5A81
5A77:             0D 08                  ;         COM_0D_while_pass length=0x0008
5A79:                C8                  ;           FN_C8_BACK_TO_TOWN
5A7A:                30 80               ;           COM_30_set_current_room(room=RM_1_HIGHWAY_WEST)
5A7C:                17 9D 00            ;           COM_17_move_object_to_destination(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
5A7F:                2F 01               ;           COM_2F_load_section_from_disk(section=1)
5A81:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5A82:          02                        ;       ELSE goto=0x5A85
5A83:             00 EE                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY1)
5A85:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5A86:          02                        ;       ELSE goto=0x5A89
5A87:             00 F5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT27)
5A89:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5A8A:          02                        ;       ELSE goto=0x5A8D
5A8B:             00 E0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT21)

; --------------------------------------------------------------------------------------------------------------------
;
5A8D: F0 28 00                           ; ----- Room 0xF0 RM_5_EMPTY_HIGHWAY_DESERT, Length: 0x0028, Data: 0x00
;
5A90:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
5A92:       0D 02                        ;     COM_0D_while_pass length=0x0002
5A94:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
5A95:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
;
5A96:    04 1F                           ;   ---- Section SECTION_04_COMMANDS length=0x001F
5A98:       0B 1D 0A                     ;     COM_0B_switch length=0x001D, function=COM_0A_is_input_phrase(phrase_num)
5A9B:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5A9C:          06                        ;       ELSE goto=0x5AA3
5A9D:             0D 04                  ;         COM_0D_while_pass length=0x0004
5A9F:                30 E4               ;           COM_30_set_current_room(room=RM_6_DESERT_EMPTY_HIGHWAY8)
5AA1:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
5AA3:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5AA4:          0A                        ;       ELSE goto=0x5AAF
5AA5:             0D 08                  ;         COM_0D_while_pass length=0x0008
5AA7:                C8                  ;           FN_C8_BACK_TO_TOWN
5AA8:                30 B4               ;           COM_30_set_current_room(room=RM_4_HIGHWAY_EAST)
5AAA:                17 9D 00            ;           COM_17_move_object_to_destination(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
5AAD:                2F 04               ;           COM_2F_load_section_from_disk(section=4)
5AAF:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5AB0:          02                        ;       ELSE goto=0x5AB3
5AB1:             00 F1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_SMALL_TRAIL1)
5AB3:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5AB4:          02                        ;       ELSE goto=0x5AB7
5AB5:             00 E2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT23)

; --------------------------------------------------------------------------------------------------------------------
;
5AB7: F1 3F 00                           ; ----- Room 0xF1 RM_5_DESERT_SMALL_TRAIL1, Length: 0x003F, Data: 0x00
;
5ABA:    03 23                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0023
5ABC:       0D 21                        ;     COM_0D_while_pass length=0x0021
5ABE:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5ABF:          04 1E                     ;       COM_04_print_message length=0x001E
5AC1:             55 45 8E 91 16 8A CB B0 0E 8A 86 5F D9 B5 66 62 ; 
5AD1:             90 14 10 58 BE A0 08 71 FF B2 9F 15 7F B1 ; 
;
;                 A SMALL TRAIL LEADS WEST AND NORTH FROM HERE.
;
;
5ADF:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5AE1:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
5AE4:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5AE5:          06                        ;       ELSE goto=0x5AEC
5AE6:             0D 04                  ;         COM_0D_while_pass length=0x0004
5AE8:                30 E5               ;           COM_30_set_current_room(room=RM_6_DESERT74)
5AEA:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
5AEC:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5AED:          02                        ;       ELSE goto=0x5AF0
5AEE:             00 F6                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_SMALL_TRAIL2)
5AF0:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5AF1:          02                        ;       ELSE goto=0x5AF4
5AF2:             00 F2                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TWISTY_TRAIL)
5AF4:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5AF5:          02                        ;       ELSE goto=0x5AF8
5AF6:             00 F0                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_EMPTY_HIGHWAY_DESERT)

; --------------------------------------------------------------------------------------------------------------------
;
5AF8: F2 41 00                           ; ----- Room 0xF2 RM_5_DESERT_TWISTY_TRAIL, Length: 0x0041, Data: 0x00
;
5AFB:    03 25                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0025
5AFD:       0D 23                        ;     COM_0D_while_pass length=0x0023
5AFF:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5B00:          04 20                     ;       COM_04_print_message length=0x0020
5B02:             55 45 8E 91 16 8A 55 D1 FB C0 EB BF 33 7A E3 8B ; 
5B12:             0B 5C B5 D0 03 BC 33 98 47 B9 53 BE F4 72 DB 63 ; 
;
;                 A SMALL TWISTY TRAIL LEADS WEST AND SOUTH HERE. 
;
;
5B22:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017
5B24:       0B 15 0A                     ;     COM_0B_switch length=0x0015, function=COM_0A_is_input_phrase(phrase_num)
5B27:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5B28:          06                        ;       ELSE goto=0x5B2F
5B29:             0D 04                  ;         COM_0D_while_pass length=0x0004
5B2B:                30 E6               ;           COM_30_set_current_room(room=RM_6_DESERT75)
5B2D:                2F 06               ;           COM_2F_load_section_from_disk(section=6)
5B2F:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5B30:          02                        ;       ELSE goto=0x5B33
5B31:             00 F3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL_FORKS)
5B33:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5B34:          02                        ;       ELSE goto=0x5B37
5B35:             00 E8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT24)
5B37:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5B38:          02                        ;       ELSE goto=0x5B3B
5B39:             00 F1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_SMALL_TRAIL1)

; --------------------------------------------------------------------------------------------------------------------
;
5B3B: F3 35 00                           ; ----- Room 0xF3 RM_5_DESERT_TRAIL_FORKS, Length: 0x0035, Data: 0x00
;
5B3E:    03 1D                           ;   ---- Section SECTION_03_DESCRIPTION length=0x001D
5B40:       0D 1B                        ;     COM_0D_while_pass length=0x001B
5B42:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5B43:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
5B44:          04 17                     ;       COM_04_print_message length=0x0017
5B46:             5F BE 8C 17 CE 47 8E 14 2B B9 04 68 CB 87 6B BF ; 
5B56:             5F BE 61 17 82 C6 2E   ; 
;
;                 THE TRAIL ALSO FORKS TO THE SOUTH.
;
;
5B5D:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5B5F:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5B62:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5B63:          02                        ;       ELSE goto=0x5B66
5B64:             00 E9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL4)
5B66:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5B67:          02                        ;       ELSE goto=0x5B6A
5B68:             00 F4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL7)
5B6A:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5B6B:          02                        ;       ELSE goto=0x5B6E
5B6C:             00 EA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT25)
5B6E:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5B6F:          02                        ;       ELSE goto=0x5B72
5B70:             00 F1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_SMALL_TRAIL1)

; --------------------------------------------------------------------------------------------------------------------
;
5B72: F4 1C 00                           ; ----- Room 0xF4 RM_5_DESERT_TRAIL7, Length: 0x001C, Data: 0x00
;
5B75:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004
5B77:       0D 02                        ;     COM_0D_while_pass length=0x0002
5B79:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5B7A:          95                        ;       FN_95_PRINT_TRAIL_MEANDERS
;
5B7B:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5B7D:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5B80:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5B81:          02                        ;       ELSE goto=0x5B84
5B82:             00 F3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL_FORKS)
5B84:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5B85:          02                        ;       ELSE goto=0x5B88
5B86:             00 EC                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL6)
5B88:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5B89:          02                        ;       ELSE goto=0x5B8C
5B8A:             00 EA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT25)
5B8C:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5B8D:          02                        ;       ELSE goto=0x5B90
5B8E:             00 F5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT27)

; --------------------------------------------------------------------------------------------------------------------
;
5B90: F5 19 00                           ; ----- Room 0xF5 RM_5_DESERT27, Length: 0x0019, Data: 0x00
;
5B93:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5B95:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5B96:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5B98:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5B9B:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5B9C:          02                        ;       ELSE goto=0x5B9F
5B9D:             00 F6                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_SMALL_TRAIL2)
5B9F:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5BA0:          02                        ;       ELSE goto=0x5BA3
5BA1:             00 ED                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT26)
5BA3:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5BA4:          02                        ;       ELSE goto=0x5BA7
5BA5:             00 F4                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL7)
5BA7:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5BA8:          02                        ;       ELSE goto=0x5BAB
5BA9:             00 EF                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_EMPTY_HIGHWAY2)

; --------------------------------------------------------------------------------------------------------------------
;
5BAB: F6 45 00                           ; ----- Room 0xF6 RM_5_DESERT_SMALL_TRAIL2, Length: 0x0045, Data: 0x00
;
5BAE:    03 25                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0025
5BB0:       0D 23                        ;     COM_0D_while_pass length=0x0023
5BB2:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5BB3:          04 20                     ;       COM_04_print_message length=0x0020
5BB5:             55 45 8E 91 16 8A CB B0 0E 8A 86 5F C8 B5 FF B2 ; 
5BC5:             82 17 55 5E 36 A1 16 71 D6 9C DB 72 95 5F 9B C1 ; 
;
;                 A SMALL TRAIL LEADS FROM THE SOUTH TO THE EAST. 
;
;
5BD5:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B
5BD7:       0B 19 0A                     ;     COM_0B_switch length=0x0019, function=COM_0A_is_input_phrase(phrase_num)
5BDA:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5BDB:          02                        ;       ELSE goto=0x5BDE
5BDC:             00 F1                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_SMALL_TRAIL1)
5BDE:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5BDF:          02                        ;       ELSE goto=0x5BE2
5BE0:             00 F5                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT27)
5BE2:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5BE3:          02                        ;       ELSE goto=0x5BE6
5BE4:             00 F3                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT_TRAIL_FORKS)
5BE6:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5BE7:          0A                        ;       ELSE goto=0x5BF2
5BE8:             0D 08                  ;         COM_0D_while_pass length=0x0008
5BEA:                C8                  ;           FN_C8_BACK_TO_TOWN
5BEB:                30 B7               ;           COM_30_set_current_room(room=RM_2_DESERT_PATH)
5BED:                17 9D 00            ;           COM_17_move_object_to_destination(obj=OBJ_9D_THIRST_TRACKER, destination=nowhere)
5BF0:                2F 02               ;           COM_2F_load_section_from_disk(section=2)

; --------------------------------------------------------------------------------------------------------------------
;
5BF2: F7 19 00                           ; ----- Room 0xF7 RM_5_DESERT28, Length: 0x0019, Data: 0x00
;
5BF5:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5BF7:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5BF8:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5BFA:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5BFD:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5BFE:          02                        ;       ELSE goto=0x5C01
5BFF:             00 FA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT31)
5C01:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5C02:          02                        ;       ELSE goto=0x5C05
5C03:             00 F7                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT28)
5C05:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5C06:          02                        ;       ELSE goto=0x5C09
5C07:             00 F7                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT28)
5C09:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5C0A:          02                        ;       ELSE goto=0x5C0D
5C0B:             00 F8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT29)

; --------------------------------------------------------------------------------------------------------------------
;
5C0D: F8 19 00                           ; ----- Room 0xF8 RM_5_DESERT29, Length: 0x0019, Data: 0x00
;
5C10:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5C12:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5C13:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5C15:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5C18:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5C19:          02                        ;       ELSE goto=0x5C1C
5C1A:             00 F8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT29)
5C1C:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5C1D:          02                        ;       ELSE goto=0x5C20
5C1E:             00 F9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT30)
5C20:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5C21:          02                        ;       ELSE goto=0x5C24
5C22:             00 F8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT29)
5C24:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5C25:          02                        ;       ELSE goto=0x5C28
5C26:             00 F8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT29)

; --------------------------------------------------------------------------------------------------------------------
;
5C28: F9 21 00                           ; ----- Room 0xF9 RM_5_DESERT30, Length: 0x0021, Data: 0x00
;
5C2B:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5C2D:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5C2E:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B
5C30:       0B 19 0A                     ;     COM_0B_switch length=0x0019, function=COM_0A_is_input_phrase(phrase_num)
5C33:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5C34:          0A                        ;       ELSE goto=0x5C3F
5C35:             0E 08                  ;         COM_0E_while_fail length=0x0008
5C37:                0D 04               ;           COM_0D_while_pass length=0x0004
5C39:                   05 3E            ;             COM_05_is_less_equal_last_random(value=62)
5C3B:                   00 86            ;             COM_00_move_ACTIVE_and_look(room=RM_5_86_??)
5C3D:                00 F9               ;           COM_00_move_ACTIVE_and_look(room=RM_5_DESERT30)
5C3F:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5C40:          02                        ;       ELSE goto=0x5C43
5C41:             00 F8                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT29)
5C43:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5C44:          02                        ;       ELSE goto=0x5C47
5C45:             00 FA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT31)
5C47:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5C48:          02                        ;       ELSE goto=0x5C4B
5C49:             00 F9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT30)

; --------------------------------------------------------------------------------------------------------------------
;
5C4B: FA 19 00                           ; ----- Room 0xFA RM_5_DESERT31, Length: 0x0019, Data: 0x00
;
5C4E:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001
5C50:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5C51:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013
5C53:       0B 11 0A                     ;     COM_0B_switch length=0x0011, function=COM_0A_is_input_phrase(phrase_num)
5C56:          03                        ;       COM_0A_is_input_phrase("EAST * * *")
5C57:          02                        ;       ELSE goto=0x5C5A
5C58:             00 FA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT31)
5C5A:          04                        ;       COM_0A_is_input_phrase("WEST * * *")
5C5B:          02                        ;       ELSE goto=0x5C5E
5C5C:             00 F7                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT28)
5C5E:          01                        ;       COM_0A_is_input_phrase("NORTH * * *")
5C5F:          02                        ;       ELSE goto=0x5C62
5C60:             00 FA                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT31)
5C62:          02                        ;       COM_0A_is_input_phrase("SOUTH * * *")
5C63:          02                        ;       ELSE goto=0x5C66
5C64:             00 F9                  ;         COM_00_move_ACTIVE_and_look(room=RM_5_DESERT30)
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

