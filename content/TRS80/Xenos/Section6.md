![Xenos](Xenos.png)

# Xenos SECTION6.DAT

>>> cpu Z80

>>> binary 5200:roms/section6.bin

```code
5200: 00 87 96                           ; List_ID=0x00, length=0x0796 (to 0x5999)

; --------------------------------------------------------------------------------------------------------------------
;
5203: 81 19 00                           ; ----- Room 0x81 RM_6_DESERT32, Length: 0x0019, Data: 0x00
;
5206:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5209)
5208:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5209:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x521E)
520B:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x521F), function=COM_0A_is_input_phrase(phrase_num)
520E:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5210:             00 82                  ;         COM_00_move_and_look(room=RM_6_DESERT33)
;                                        ;       end case
5212:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5214:             00 83                  ;         COM_00_move_and_look(room=RM_6_DESERT34)
;                                        ;       end case
5216:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5218:             00 A8                  ;         COM_00_move_and_look(room=RM_6_DESERT49)
;                                        ;       end case
521A:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
521C:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x520B

; --------------------------------------------------------------------------------------------------------------------
;
521E: 82 19 00                           ; ----- Room 0x82 RM_6_DESERT33, Length: 0x0019, Data: 0x00
;
5221:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5224)
5223:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5224:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5239)
5226:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x523A), function=COM_0A_is_input_phrase(phrase_num)
5229:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
522B:             00 83                  ;         COM_00_move_and_look(room=RM_6_DESERT34)
;                                        ;       end case
522D:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
522F:             00 81                  ;         COM_00_move_and_look(room=RM_6_DESERT32)
;                                        ;       end case
5231:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5233:             00 A9                  ;         COM_00_move_and_look(room=RM_6_DESERT50)
;                                        ;       end case
5235:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5237:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5226

; --------------------------------------------------------------------------------------------------------------------
;
5239: 83 19 00                           ; ----- Room 0x83 RM_6_DESERT34, Length: 0x0019, Data: 0x00
;
523C:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x523F)
523E:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
523F:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5254)
5241:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5255), function=COM_0A_is_input_phrase(phrase_num)
5244:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5246:             00 84                  ;         COM_00_move_and_look(room=RM_6_DESERT35)
;                                        ;       end case
5248:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
524A:             00 82                  ;         COM_00_move_and_look(room=RM_6_DESERT33)
;                                        ;       end case
524C:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
524E:             00 AA                  ;         COM_00_move_and_look(room=RM_6_DESERT51)
;                                        ;       end case
5250:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5252:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5241

; --------------------------------------------------------------------------------------------------------------------
;
5254: 84 19 00                           ; ----- Room 0x84 RM_6_DESERT35, Length: 0x0019, Data: 0x00
;
5257:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x525A)
5259:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
525A:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x526F)
525C:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5270), function=COM_0A_is_input_phrase(phrase_num)
525F:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5261:             00 85                  ;         COM_00_move_and_look(room=RM_6_DESERT36)
;                                        ;       end case
5263:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5265:             00 83                  ;         COM_00_move_and_look(room=RM_6_DESERT34)
;                                        ;       end case
5267:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5269:             00 AB                  ;         COM_00_move_and_look(room=RM_6_DESERT52)
;                                        ;       end case
526B:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
526D:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x525C

; --------------------------------------------------------------------------------------------------------------------
;
526F: 85 19 00                           ; ----- Room 0x85 RM_6_DESERT36, Length: 0x0019, Data: 0x00
;
5272:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5275)
5274:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5275:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x528A)
5277:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x528B), function=COM_0A_is_input_phrase(phrase_num)
527A:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
527C:             00 86                  ;         COM_00_move_and_look(room=RM_6_DESERT37)
;                                        ;       end case
527E:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5280:             00 84                  ;         COM_00_move_and_look(room=RM_6_DESERT35)
;                                        ;       end case
5282:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5284:             00 AC                  ;         COM_00_move_and_look(room=RM_6_DESERT53)
;                                        ;       end case
5286:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5288:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5277

; --------------------------------------------------------------------------------------------------------------------
;
528A: 86 19 00                           ; ----- Room 0x86 RM_6_DESERT37, Length: 0x0019, Data: 0x00
;
528D:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5290)
528F:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5290:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x52A5)
5292:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x52A6), function=COM_0A_is_input_phrase(phrase_num)
5295:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5297:             00 87                  ;         COM_00_move_and_look(room=RM_6_DESERT38)
;                                        ;       end case
5299:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
529B:             00 85                  ;         COM_00_move_and_look(room=RM_6_DESERT36)
;                                        ;       end case
529D:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
529F:             00 AD                  ;         COM_00_move_and_look(room=RM_6_DESERT54)
;                                        ;       end case
52A1:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
52A3:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5292

; --------------------------------------------------------------------------------------------------------------------
;
52A5: 87 19 00                           ; ----- Room 0x87 RM_6_DESERT38, Length: 0x0019, Data: 0x00
;
52A8:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x52AB)
52AA:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
52AB:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x52C0)
52AD:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x52C1), function=COM_0A_is_input_phrase(phrase_num)
52B0:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
52B2:             00 88                  ;         COM_00_move_and_look(room=RM_6_DESERT39)
;                                        ;       end case
52B4:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
52B6:             00 86                  ;         COM_00_move_and_look(room=RM_6_DESERT37)
;                                        ;       end case
52B8:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
52BA:             00 AE                  ;         COM_00_move_and_look(room=RM_6_DESERT55)
;                                        ;       end case
52BC:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
52BE:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x52AD

; --------------------------------------------------------------------------------------------------------------------
;
52C0: 88 19 00                           ; ----- Room 0x88 RM_6_DESERT39, Length: 0x0019, Data: 0x00
;
52C3:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x52C6)
52C5:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
52C6:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x52DB)
52C8:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x52DC), function=COM_0A_is_input_phrase(phrase_num)
52CB:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
52CD:             00 89                  ;         COM_00_move_and_look(room=RM_6_DESERT40)
;                                        ;       end case
52CF:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
52D1:             00 87                  ;         COM_00_move_and_look(room=RM_6_DESERT38)
;                                        ;       end case
52D3:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
52D5:             00 AF                  ;         COM_00_move_and_look(room=RM_6_DESERT56)
;                                        ;       end case
52D7:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
52D9:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x52C8

; --------------------------------------------------------------------------------------------------------------------
;
52DB: 89 19 00                           ; ----- Room 0x89 RM_6_DESERT40, Length: 0x0019, Data: 0x00
;
52DE:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x52E1)
52E0:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
52E1:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x52F6)
52E3:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x52F7), function=COM_0A_is_input_phrase(phrase_num)
52E6:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
52E8:             00 8A                  ;         COM_00_move_and_look(room=RM_6_DESERT41)
;                                        ;       end case
52EA:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
52EC:             00 88                  ;         COM_00_move_and_look(room=RM_6_DESERT39)
;                                        ;       end case
52EE:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
52F0:             00 B0                  ;         COM_00_move_and_look(room=RM_6_DESERT_SMALL_OASIS)
;                                        ;       end case
52F2:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
52F4:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x52E3

; --------------------------------------------------------------------------------------------------------------------
;
52F6: 8A 19 00                           ; ----- Room 0x8A RM_6_DESERT41, Length: 0x0019, Data: 0x00
;
52F9:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x52FC)
52FB:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
52FC:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5311)
52FE:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5312), function=COM_0A_is_input_phrase(phrase_num)
5301:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5303:             00 8B                  ;         COM_00_move_and_look(room=RM_6_DESERT42)
;                                        ;       end case
5305:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5307:             00 89                  ;         COM_00_move_and_look(room=RM_6_DESERT40)
;                                        ;       end case
5309:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
530B:             00 B1                  ;         COM_00_move_and_look(room=RM_6_DESERT57)
;                                        ;       end case
530D:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
530F:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x52FE

; --------------------------------------------------------------------------------------------------------------------
;
5311: 8B 19 00                           ; ----- Room 0x8B RM_6_DESERT42, Length: 0x0019, Data: 0x00
;
5314:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5317)
5316:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5317:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x532C)
5319:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x532D), function=COM_0A_is_input_phrase(phrase_num)
531C:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
531E:             00 89                  ;         COM_00_move_and_look(room=RM_6_DESERT40)
;                                        ;       end case
5320:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5322:             00 8A                  ;         COM_00_move_and_look(room=RM_6_DESERT41)
;                                        ;       end case
5324:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5326:             00 8C                  ;         COM_00_move_and_look(room=RM_6_DESERT43)
;                                        ;       end case
5328:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
532A:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5319

; --------------------------------------------------------------------------------------------------------------------
;
532C: 8C 19 00                           ; ----- Room 0x8C RM_6_DESERT43, Length: 0x0019, Data: 0x00
;
532F:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5332)
5331:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5332:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5347)
5334:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5348), function=COM_0A_is_input_phrase(phrase_num)
5337:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5339:             00 AF                  ;         COM_00_move_and_look(room=RM_6_DESERT56)
;                                        ;       end case
533B:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
533D:             00 B1                  ;         COM_00_move_and_look(room=RM_6_DESERT57)
;                                        ;       end case
533F:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5341:             00 8D                  ;         COM_00_move_and_look(room=RM_6_DESERT44)
;                                        ;       end case
5343:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5345:             00 8B                  ;         COM_00_move_and_look(room=RM_6_DESERT42)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5334

; --------------------------------------------------------------------------------------------------------------------
;
5347: 8D 19 00                           ; ----- Room 0x8D RM_6_DESERT44, Length: 0x0019, Data: 0x00
;
534A:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x534D)
534C:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
534D:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5362)
534F:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5363), function=COM_0A_is_input_phrase(phrase_num)
5352:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5354:             00 CC                  ;         COM_00_move_and_look(room=RM_6_DESERT67)
;                                        ;       end case
5356:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5358:             00 B2                  ;         COM_00_move_and_look(room=RM_6_DESERT58)
;                                        ;       end case
535A:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
535C:             00 8E                  ;         COM_00_move_and_look(room=RM_6_DESERT45)
;                                        ;       end case
535E:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5360:             00 8C                  ;         COM_00_move_and_look(room=RM_6_DESERT43)
;                                        ;       end case
;                                        ;     end decode_switch at 0x534F

; --------------------------------------------------------------------------------------------------------------------
;
5362: 8E 19 00                           ; ----- Room 0x8E RM_6_DESERT45, Length: 0x0019, Data: 0x00
;
5365:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5368)
5367:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5368:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x537D)
536A:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x537E), function=COM_0A_is_input_phrase(phrase_num)
536D:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
536F:             00 CD                  ;         COM_00_move_and_look(room=RM_6_DESERT68)
;                                        ;       end case
5371:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5373:             00 B3                  ;         COM_00_move_and_look(room=RM_6_DESERT59)
;                                        ;       end case
5375:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5377:             00 8F                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY3)
;                                        ;       end case
5379:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
537B:             00 8D                  ;         COM_00_move_and_look(room=RM_6_DESERT44)
;                                        ;       end case
;                                        ;     end decode_switch at 0x536A

; --------------------------------------------------------------------------------------------------------------------
;
537D: 8F 1C 00                           ; ----- Room 0x8F RM_6_DESERT_EMPTY_HIGHWAY3, Length: 0x001C, Data: 0x00
;
5380:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5386)
5382:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5386)
5384:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5385:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;                                        ;     end group_AND at 0x5382
;
5386:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x539B)
5388:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x539C), function=COM_0A_is_input_phrase(phrase_num)
538B:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
538D:             00 CE                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY7)
;                                        ;       end case
538F:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5391:             00 B4                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY5)
;                                        ;       end case
5393:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5395:             00 90                  ;         COM_00_move_and_look(room=RM_6_DESERT46)
;                                        ;       end case
5397:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5399:             00 8E                  ;         COM_00_move_and_look(room=RM_6_DESERT45)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5388

; --------------------------------------------------------------------------------------------------------------------
;
539B: 90 19 00                           ; ----- Room 0x90 RM_6_DESERT46, Length: 0x0019, Data: 0x00
;
539E:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x53A1)
53A0:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
53A1:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x53B6)
53A3:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x53B7), function=COM_0A_is_input_phrase(phrase_num)
53A6:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
53A8:             00 CF                  ;         COM_00_move_and_look(room=RM_6_DESERT69)
;                                        ;       end case
53AA:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
53AC:             00 B5                  ;         COM_00_move_and_look(room=RM_6_DESERT60)
;                                        ;       end case
53AE:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
53B0:             00 91                  ;         COM_00_move_and_look(room=RM_6_DESERT47)
;                                        ;       end case
53B2:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
53B4:             00 8F                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY3)
;                                        ;       end case
;                                        ;     end decode_switch at 0x53A3

; --------------------------------------------------------------------------------------------------------------------
;
53B6: 91 19 00                           ; ----- Room 0x91 RM_6_DESERT47, Length: 0x0019, Data: 0x00
;
53B9:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x53BC)
53BB:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
53BC:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x53D1)
53BE:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x53D2), function=COM_0A_is_input_phrase(phrase_num)
53C1:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
53C3:             00 D0                  ;         COM_00_move_and_look(room=RM_6_DESERT70)
;                                        ;       end case
53C5:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
53C7:             00 B6                  ;         COM_00_move_and_look(room=RM_6_DESERT61)
;                                        ;       end case
53C9:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
53CB:             00 92                  ;         COM_00_move_and_look(room=RM_6_DESERT48)
;                                        ;       end case
53CD:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
53CF:             00 90                  ;         COM_00_move_and_look(room=RM_6_DESERT46)
;                                        ;       end case
;                                        ;     end decode_switch at 0x53BE

; --------------------------------------------------------------------------------------------------------------------
;
53D1: 92 19 00                           ; ----- Room 0x92 RM_6_DESERT48, Length: 0x0019, Data: 0x00
;
53D4:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x53D7)
53D6:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
53D7:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x53EC)
53D9:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x53ED), function=COM_0A_is_input_phrase(phrase_num)
53DC:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
53DE:             00 D1                  ;         COM_00_move_and_look(room=RM_6_DESERT71)
;                                        ;       end case
53E0:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
53E2:             00 B7                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE2)
;                                        ;       end case
53E4:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
53E6:             00 93                  ;         COM_00_move_and_look(room=RM_6_DESERT_CANYON_LAKE1)
;                                        ;       end case
53E8:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
53EA:             00 91                  ;         COM_00_move_and_look(room=RM_6_DESERT47)
;                                        ;       end case
;                                        ;     end decode_switch at 0x53D9

; --------------------------------------------------------------------------------------------------------------------
;
53EC: 93 1C 00                           ; ----- Room 0x93 RM_6_DESERT_CANYON_LAKE1, Length: 0x001C, Data: 0x00
;
53EF:    03 05                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0005 (to 0x53F6)
53F1:       0D 03                        ;     COM_0D_group_AND length=0x0003 (to 0x53F6)
53F3:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
53F4:          96                        ;       FN_96_PRINT_VAST_CANYON
53F5:          98                        ;       FN_98_PRINT_LAKE
;                                        ;     end group_AND at 0x53F1
;
53F6:    04 12                           ;   ---- Section SECTION_04_COMMANDS length=0x0012 (to 0x540A)
53F8:       0B 10 0A                     ;     COM_0B_switch length=0x0010 (to 0x540B), function=COM_0A_is_input_phrase(phrase_num)
53FB:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
53FD:             00 B8                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE3)
;                                        ;       end case
53FF:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5401:             00 94                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE1)
;                                        ;       end case
5403:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
5405:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5406:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5408:             00 92                  ;         COM_00_move_and_look(room=RM_6_DESERT48)
;                                        ;       end case
;                                        ;     end decode_switch at 0x53F8

; --------------------------------------------------------------------------------------------------------------------
;
540A: 94 1C 00                           ; ----- Room 0x94 RM_6_DESERT_LAKE1, Length: 0x001C, Data: 0x00
;
540D:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5413)
540F:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5413)
5411:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5412:          98                        ;       FN_98_PRINT_LAKE
;                                        ;     end group_AND at 0x540F
;
5413:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5428)
5415:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5429), function=COM_0A_is_input_phrase(phrase_num)
5418:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
541A:             00 93                  ;         COM_00_move_and_look(room=RM_6_DESERT_CANYON_LAKE1)
;                                        ;       end case
541C:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
541E:             00 B8                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE3)
;                                        ;       end case
5420:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5422:             00 95                  ;         COM_00_move_and_look(room=RM_6_DESERT_CANYON_LAKE2)
;                                        ;       end case
5424:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5426:             00 B7                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE2)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5415

; --------------------------------------------------------------------------------------------------------------------
;
5428: 95 1B 00                           ; ----- Room 0x95 RM_6_DESERT_CANYON_LAKE2, Length: 0x001B, Data: 0x00
;
542B:    03 05                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0005 (to 0x5432)
542D:       0D 03                        ;     COM_0D_group_AND length=0x0003 (to 0x5432)
542F:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5430:          96                        ;       FN_96_PRINT_VAST_CANYON
5431:          98                        ;       FN_98_PRINT_LAKE
;                                        ;     end group_AND at 0x542D
;
5432:    04 11                           ;   ---- Section SECTION_04_COMMANDS length=0x0011 (to 0x5445)
5434:       0B 0F 0A                     ;     COM_0B_switch length=0x000F (to 0x5446), function=COM_0A_is_input_phrase(phrase_num)
5437:          03 01                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0001
5439:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
543A:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
543C:             00 96                  ;         COM_00_move_and_look(room=RM_6_DESERT_CANYON_LAKE3)
;                                        ;       end case
543E:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
5440:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5441:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5443:             00 94                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE1)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5434

; --------------------------------------------------------------------------------------------------------------------
;
5445: 96 1C 00                           ; ----- Room 0x96 RM_6_DESERT_CANYON_LAKE3, Length: 0x001C, Data: 0x00
;
5448:    03 05                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0005 (to 0x544F)
544A:       0D 03                        ;     COM_0D_group_AND length=0x0003 (to 0x544F)
544C:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
544D:          96                        ;       FN_96_PRINT_VAST_CANYON
544E:          98                        ;       FN_98_PRINT_LAKE
;                                        ;     end group_AND at 0x544A
;
544F:    04 12                           ;   ---- Section SECTION_04_COMMANDS length=0x0012 (to 0x5463)
5451:       0B 10 0A                     ;     COM_0B_switch length=0x0010 (to 0x5464), function=COM_0A_is_input_phrase(phrase_num)
5454:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5456:             00 95                  ;         COM_00_move_and_look(room=RM_6_DESERT_CANYON_LAKE2)
;                                        ;       end case
5458:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
545A:             00 B9                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE4)
;                                        ;       end case
545C:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
545E:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
545F:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5461:             00 B8                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE3)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5451

; --------------------------------------------------------------------------------------------------------------------
;
5463: 97 1E 00                           ; ----- Room 0x97 RM_6_DESERT_CANYON4, Length: 0x001E, Data: 0x00
;
5466:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x546C)
5468:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x546C)
546A:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
546B:          96                        ;       FN_96_PRINT_VAST_CANYON
;                                        ;     end group_AND at 0x5468
;
546C:    04 15                           ;   ---- Section SECTION_04_COMMANDS length=0x0015 (to 0x5483)
546E:       0B 13 0A                     ;     COM_0B_switch length=0x0013 (to 0x5484), function=COM_0A_is_input_phrase(phrase_num)
5471:          03 01                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0001
5473:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
5474:          04 06                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0006
5476:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x547C)
5478:                30 98               ;           COM_30_set_current_room(room=RM_5_DESERT2)
547A:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x5476
;                                        ;       end case
547C:          01 01                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0001
547E:             97                     ;         FN_97_PRINT_CERTAIN_DEATH
;                                        ;       end case
547F:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5481:             00 B9                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE4)
;                                        ;       end case
;                                        ;     end decode_switch at 0x546E

; --------------------------------------------------------------------------------------------------------------------
;
5483: A7 20 00                           ; ----- Room 0xA7 RM_6_DESERT_EMPTY_HIGHWAY4, Length: 0x0020, Data: 0x00
;
5486:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x548C)
5488:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x548C)
548A:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
548B:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;                                        ;     end group_AND at 0x5488
;
548C:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x54A5)
548E:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x54A6), function=COM_0A_is_input_phrase(phrase_num)
5491:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5493:             00 C5                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY6)
;                                        ;       end case
5495:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5497:             00 A7                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY4)
;                                        ;       end case
5499:          01 06                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0006
549B:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x54A1)
549D:                30 A6               ;           COM_30_set_current_room(room=RM_5_DESERT6)
549F:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x549B
;                                        ;       end case
54A1:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
54A3:             00 A8                  ;         COM_00_move_and_look(room=RM_6_DESERT49)
;                                        ;       end case
;                                        ;     end decode_switch at 0x548E

; --------------------------------------------------------------------------------------------------------------------
;
54A5: A8 19 00                           ; ----- Room 0xA8 RM_6_DESERT49, Length: 0x0019, Data: 0x00
;
54A8:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x54AB)
54AA:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
54AB:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x54C0)
54AD:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x54C1), function=COM_0A_is_input_phrase(phrase_num)
54B0:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
54B2:             00 A9                  ;         COM_00_move_and_look(room=RM_6_DESERT50)
;                                        ;       end case
54B4:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
54B6:             00 84                  ;         COM_00_move_and_look(room=RM_6_DESERT35)
;                                        ;       end case
54B8:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
54BA:             00 A7                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY4)
;                                        ;       end case
54BC:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
54BE:             00 81                  ;         COM_00_move_and_look(room=RM_6_DESERT32)
;                                        ;       end case
;                                        ;     end decode_switch at 0x54AD

; --------------------------------------------------------------------------------------------------------------------
;
54C0: A9 19 00                           ; ----- Room 0xA9 RM_6_DESERT50, Length: 0x0019, Data: 0x00
;
54C3:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x54C6)
54C5:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
54C6:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x54DB)
54C8:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x54DC), function=COM_0A_is_input_phrase(phrase_num)
54CB:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
54CD:             00 AA                  ;         COM_00_move_and_look(room=RM_6_DESERT51)
;                                        ;       end case
54CF:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
54D1:             00 A8                  ;         COM_00_move_and_look(room=RM_6_DESERT49)
;                                        ;       end case
54D3:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
54D5:             00 C5                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY6)
;                                        ;       end case
54D7:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
54D9:             00 82                  ;         COM_00_move_and_look(room=RM_6_DESERT33)
;                                        ;       end case
;                                        ;     end decode_switch at 0x54C8

; --------------------------------------------------------------------------------------------------------------------
;
54DB: AA 19 00                           ; ----- Room 0xAA RM_6_DESERT51, Length: 0x0019, Data: 0x00
;
54DE:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x54E1)
54E0:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
54E1:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x54F6)
54E3:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x54F7), function=COM_0A_is_input_phrase(phrase_num)
54E6:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
54E8:             00 AB                  ;         COM_00_move_and_look(room=RM_6_DESERT52)
;                                        ;       end case
54EA:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
54EC:             00 A9                  ;         COM_00_move_and_look(room=RM_6_DESERT50)
;                                        ;       end case
54EE:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
54F0:             00 C6                  ;         COM_00_move_and_look(room=RM_6_DESERT_HIGHWAY_TURNS)
;                                        ;       end case
54F2:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
54F4:             00 83                  ;         COM_00_move_and_look(room=RM_6_DESERT34)
;                                        ;       end case
;                                        ;     end decode_switch at 0x54E3

; --------------------------------------------------------------------------------------------------------------------
;
54F6: AB 19 00                           ; ----- Room 0xAB RM_6_DESERT52, Length: 0x0019, Data: 0x00
;
54F9:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x54FC)
54FB:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
54FC:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5511)
54FE:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5512), function=COM_0A_is_input_phrase(phrase_num)
5501:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5503:             00 AC                  ;         COM_00_move_and_look(room=RM_6_DESERT53)
;                                        ;       end case
5505:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5507:             00 AA                  ;         COM_00_move_and_look(room=RM_6_DESERT51)
;                                        ;       end case
5509:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
550B:             00 C7                  ;         COM_00_move_and_look(room=RM_6_DESERT62)
;                                        ;       end case
550D:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
550F:             00 84                  ;         COM_00_move_and_look(room=RM_6_DESERT35)
;                                        ;       end case
;                                        ;     end decode_switch at 0x54FE

; --------------------------------------------------------------------------------------------------------------------
;
5511: AC 19 00                           ; ----- Room 0xAC RM_6_DESERT53, Length: 0x0019, Data: 0x00
;
5514:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5517)
5516:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5517:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x552C)
5519:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x552D), function=COM_0A_is_input_phrase(phrase_num)
551C:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
551E:             00 AD                  ;         COM_00_move_and_look(room=RM_6_DESERT54)
;                                        ;       end case
5520:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5522:             00 AB                  ;         COM_00_move_and_look(room=RM_6_DESERT52)
;                                        ;       end case
5524:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5526:             00 C8                  ;         COM_00_move_and_look(room=RM_6_DESERT63)
;                                        ;       end case
5528:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
552A:             00 85                  ;         COM_00_move_and_look(room=RM_6_DESERT36)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5519

; --------------------------------------------------------------------------------------------------------------------
;
552C: AD 19 00                           ; ----- Room 0xAD RM_6_DESERT54, Length: 0x0019, Data: 0x00
;
552F:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5532)
5531:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5532:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5547)
5534:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5548), function=COM_0A_is_input_phrase(phrase_num)
5537:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5539:             00 AE                  ;         COM_00_move_and_look(room=RM_6_DESERT55)
;                                        ;       end case
553B:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
553D:             00 AC                  ;         COM_00_move_and_look(room=RM_6_DESERT53)
;                                        ;       end case
553F:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5541:             00 C9                  ;         COM_00_move_and_look(room=RM_6_DESERT64)
;                                        ;       end case
5543:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5545:             00 86                  ;         COM_00_move_and_look(room=RM_6_DESERT37)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5534

; --------------------------------------------------------------------------------------------------------------------
;
5547: AE 19 00                           ; ----- Room 0xAE RM_6_DESERT55, Length: 0x0019, Data: 0x00
;
554A:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x554D)
554C:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
554D:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5562)
554F:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5563), function=COM_0A_is_input_phrase(phrase_num)
5552:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5554:             00 AF                  ;         COM_00_move_and_look(room=RM_6_DESERT56)
;                                        ;       end case
5556:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5558:             00 AD                  ;         COM_00_move_and_look(room=RM_6_DESERT54)
;                                        ;       end case
555A:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
555C:             00 CA                  ;         COM_00_move_and_look(room=RM_6_DESERT65)
;                                        ;       end case
555E:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5560:             00 87                  ;         COM_00_move_and_look(room=RM_6_DESERT38)
;                                        ;       end case
;                                        ;     end decode_switch at 0x554F

; --------------------------------------------------------------------------------------------------------------------
;
5562: AF 19 00                           ; ----- Room 0xAF RM_6_DESERT56, Length: 0x0019, Data: 0x00
;
5565:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5568)
5567:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5568:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x557D)
556A:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x557E), function=COM_0A_is_input_phrase(phrase_num)
556D:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
556F:             00 B0                  ;         COM_00_move_and_look(room=RM_6_DESERT_SMALL_OASIS)
;                                        ;       end case
5571:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5573:             00 AE                  ;         COM_00_move_and_look(room=RM_6_DESERT55)
;                                        ;       end case
5575:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5577:             00 CB                  ;         COM_00_move_and_look(room=RM_6_DESERT66)
;                                        ;       end case
5579:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
557B:             00 88                  ;         COM_00_move_and_look(room=RM_6_DESERT39)
;                                        ;       end case
;                                        ;     end decode_switch at 0x556A

; --------------------------------------------------------------------------------------------------------------------
;
557D: B0 43 00                           ; ----- Room 0xB0 RM_6_DESERT_SMALL_OASIS, Length: 0x0043, Data: 0x00
;
5580:    03 2B                           ;   ---- Section SECTION_03_DESCRIPTION length=0x002B (to 0x55AD)
5582:       0D 29                        ;     COM_0D_group_AND length=0x0029 (to 0x55AD)
5584:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5585:          04 26                     ;       COM_04_print_message length=0x0026 (to 0x55AD)
5587:             5F BE 5B B1 4B 7B 55 45 8E 91 11 8A 5B 49 CA B5
5597:             2F 62 44 F4 96 C6 8E 14 6E 49 D6 15 9B 15 C6 B5
55A7:             07 B2 17 58 AB A2     
;
;                 THERE IS A SMALL OASIS HERE. BUT, ALAS, IT HAS DRIED UP! 
;
;                                        ;     end group_AND at 0x5582
;
55AD:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x55C2)
55AF:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x55C3), function=COM_0A_is_input_phrase(phrase_num)
55B2:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
55B4:             00 B1                  ;         COM_00_move_and_look(room=RM_6_DESERT57)
;                                        ;       end case
55B6:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
55B8:             00 AF                  ;         COM_00_move_and_look(room=RM_6_DESERT56)
;                                        ;       end case
55BA:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
55BC:             00 CC                  ;         COM_00_move_and_look(room=RM_6_DESERT67)
;                                        ;       end case
55BE:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
55C0:             00 89                  ;         COM_00_move_and_look(room=RM_6_DESERT40)
;                                        ;       end case
;                                        ;     end decode_switch at 0x55AF

; --------------------------------------------------------------------------------------------------------------------
;
55C2: B1 19 00                           ; ----- Room 0xB1 RM_6_DESERT57, Length: 0x0019, Data: 0x00
;
55C5:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x55C8)
55C7:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
55C8:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x55DD)
55CA:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x55DE), function=COM_0A_is_input_phrase(phrase_num)
55CD:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
55CF:             00 8C                  ;         COM_00_move_and_look(room=RM_6_DESERT43)
;                                        ;       end case
55D1:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
55D3:             00 B0                  ;         COM_00_move_and_look(room=RM_6_DESERT_SMALL_OASIS)
;                                        ;       end case
55D5:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
55D7:             00 B2                  ;         COM_00_move_and_look(room=RM_6_DESERT58)
;                                        ;       end case
55D9:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
55DB:             00 8A                  ;         COM_00_move_and_look(room=RM_6_DESERT41)
;                                        ;       end case
;                                        ;     end decode_switch at 0x55CA

; --------------------------------------------------------------------------------------------------------------------
;
55DD: B2 19 00                           ; ----- Room 0xB2 RM_6_DESERT58, Length: 0x0019, Data: 0x00
;
55E0:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x55E3)
55E2:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
55E3:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x55F8)
55E5:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x55F9), function=COM_0A_is_input_phrase(phrase_num)
55E8:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
55EA:             00 8D                  ;         COM_00_move_and_look(room=RM_6_DESERT44)
;                                        ;       end case
55EC:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
55EE:             00 CC                  ;         COM_00_move_and_look(room=RM_6_DESERT67)
;                                        ;       end case
55F0:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
55F2:             00 B3                  ;         COM_00_move_and_look(room=RM_6_DESERT59)
;                                        ;       end case
55F4:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
55F6:             00 B1                  ;         COM_00_move_and_look(room=RM_6_DESERT57)
;                                        ;       end case
;                                        ;     end decode_switch at 0x55E5

; --------------------------------------------------------------------------------------------------------------------
;
55F8: B3 19 00                           ; ----- Room 0xB3 RM_6_DESERT59, Length: 0x0019, Data: 0x00
;
55FB:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x55FE)
55FD:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
55FE:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5613)
5600:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5614), function=COM_0A_is_input_phrase(phrase_num)
5603:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5605:             00 8E                  ;         COM_00_move_and_look(room=RM_6_DESERT45)
;                                        ;       end case
5607:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5609:             00 CD                  ;         COM_00_move_and_look(room=RM_6_DESERT68)
;                                        ;       end case
560B:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
560D:             00 B4                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY5)
;                                        ;       end case
560F:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5611:             00 B2                  ;         COM_00_move_and_look(room=RM_6_DESERT58)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5600

; --------------------------------------------------------------------------------------------------------------------
;
5613: B4 1C 00                           ; ----- Room 0xB4 RM_6_DESERT_EMPTY_HIGHWAY5, Length: 0x001C, Data: 0x00
;
5616:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x561C)
5618:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x561C)
561A:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
561B:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;                                        ;     end group_AND at 0x5618
;
561C:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5631)
561E:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5632), function=COM_0A_is_input_phrase(phrase_num)
5621:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5623:             00 8F                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY3)
;                                        ;       end case
5625:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5627:             00 CE                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY7)
;                                        ;       end case
5629:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
562B:             00 B5                  ;         COM_00_move_and_look(room=RM_6_DESERT60)
;                                        ;       end case
562D:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
562F:             00 B3                  ;         COM_00_move_and_look(room=RM_6_DESERT59)
;                                        ;       end case
;                                        ;     end decode_switch at 0x561E

; --------------------------------------------------------------------------------------------------------------------
;
5631: B5 19 00                           ; ----- Room 0xB5 RM_6_DESERT60, Length: 0x0019, Data: 0x00
;
5634:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5637)
5636:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5637:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x564C)
5639:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x564D), function=COM_0A_is_input_phrase(phrase_num)
563C:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
563E:             00 90                  ;         COM_00_move_and_look(room=RM_6_DESERT46)
;                                        ;       end case
5640:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5642:             00 CF                  ;         COM_00_move_and_look(room=RM_6_DESERT69)
;                                        ;       end case
5644:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5646:             00 B6                  ;         COM_00_move_and_look(room=RM_6_DESERT61)
;                                        ;       end case
5648:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
564A:             00 B4                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY5)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5639

; --------------------------------------------------------------------------------------------------------------------
;
564C: B6 19 00                           ; ----- Room 0xB6 RM_6_DESERT61, Length: 0x0019, Data: 0x00
;
564F:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5652)
5651:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5652:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5667)
5654:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5668), function=COM_0A_is_input_phrase(phrase_num)
5657:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5659:             00 91                  ;         COM_00_move_and_look(room=RM_6_DESERT47)
;                                        ;       end case
565B:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
565D:             00 D0                  ;         COM_00_move_and_look(room=RM_6_DESERT70)
;                                        ;       end case
565F:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5661:             00 B7                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE2)
;                                        ;       end case
5663:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5665:             00 B5                  ;         COM_00_move_and_look(room=RM_6_DESERT60)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5654

; --------------------------------------------------------------------------------------------------------------------
;
5667: B7 1C 00                           ; ----- Room 0xB7 RM_6_DESERT_LAKE2, Length: 0x001C, Data: 0x00
;
566A:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5670)
566C:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5670)
566E:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
566F:          98                        ;       FN_98_PRINT_LAKE
;                                        ;     end group_AND at 0x566C
;
5670:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5685)
5672:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5686), function=COM_0A_is_input_phrase(phrase_num)
5675:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5677:             00 92                  ;         COM_00_move_and_look(room=RM_6_DESERT48)
;                                        ;       end case
5679:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
567B:             00 D1                  ;         COM_00_move_and_look(room=RM_6_DESERT71)
;                                        ;       end case
567D:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
567F:             00 94                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE1)
;                                        ;       end case
5681:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5683:             00 B6                  ;         COM_00_move_and_look(room=RM_6_DESERT61)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5672

; --------------------------------------------------------------------------------------------------------------------
;
5685: B8 1C 00                           ; ----- Room 0xB8 RM_6_DESERT_LAKE3, Length: 0x001C, Data: 0x00
;
5688:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x568E)
568A:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x568E)
568C:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
568D:          98                        ;       FN_98_PRINT_LAKE
;                                        ;     end group_AND at 0x568A
;
568E:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x56A3)
5690:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x56A4), function=COM_0A_is_input_phrase(phrase_num)
5693:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5695:             00 94                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE1)
;                                        ;       end case
5697:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5699:             00 D2                  ;         COM_00_move_and_look(room=RM_6_DESERT72)
;                                        ;       end case
569B:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
569D:             00 96                  ;         COM_00_move_and_look(room=RM_6_DESERT_CANYON_LAKE3)
;                                        ;       end case
569F:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
56A1:             00 D1                  ;         COM_00_move_and_look(room=RM_6_DESERT71)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5690

; --------------------------------------------------------------------------------------------------------------------
;
56A3: B9 20 00                           ; ----- Room 0xB9 RM_6_DESERT_LAKE4, Length: 0x0020, Data: 0x00
;
56A6:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x56AC)
56A8:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x56AC)
56AA:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
56AB:          98                        ;       FN_98_PRINT_LAKE
;                                        ;     end group_AND at 0x56A8
;
56AC:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x56C5)
56AE:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x56C6), function=COM_0A_is_input_phrase(phrase_num)
56B1:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
56B3:             00 96                  ;         COM_00_move_and_look(room=RM_6_DESERT_CANYON_LAKE3)
;                                        ;       end case
56B5:          04 06                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0006
56B7:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x56BD)
56B9:                30 BA               ;           COM_30_set_current_room(room=RM_5_DESERT7)
56BB:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x56B7
;                                        ;       end case
56BD:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
56BF:             00 97                  ;         COM_00_move_and_look(room=RM_6_DESERT_CANYON4)
;                                        ;       end case
56C1:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
56C3:             00 D2                  ;         COM_00_move_and_look(room=RM_6_DESERT72)
;                                        ;       end case
;                                        ;     end decode_switch at 0x56AE

; --------------------------------------------------------------------------------------------------------------------
;
56C5: C5 20 00                           ; ----- Room 0xC5 RM_6_DESERT_EMPTY_HIGHWAY6, Length: 0x0020, Data: 0x00
;
56C8:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x56CE)
56CA:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x56CE)
56CC:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
56CD:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;                                        ;     end group_AND at 0x56CA
;
56CE:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x56E7)
56D0:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x56E8), function=COM_0A_is_input_phrase(phrase_num)
56D3:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
56D5:             00 C6                  ;         COM_00_move_and_look(room=RM_6_DESERT_HIGHWAY_TURNS)
;                                        ;       end case
56D7:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
56D9:             00 A7                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY4)
;                                        ;       end case
56DB:          01 06                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0006
56DD:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x56E3)
56DF:                30 C4               ;           COM_30_set_current_room(room=RM_5_DESERT12)
56E1:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x56DD
;                                        ;       end case
56E3:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
56E5:             00 A9                  ;         COM_00_move_and_look(room=RM_6_DESERT50)
;                                        ;       end case
;                                        ;     end decode_switch at 0x56D0

; --------------------------------------------------------------------------------------------------------------------
;
56E7: C6 43 00                           ; ----- Room 0xC6 RM_6_DESERT_HIGHWAY_TURNS, Length: 0x0043, Data: 0x00
;
56EA:    03 27                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0027 (to 0x5713)
56EC:       0D 25                        ;     COM_0D_group_AND length=0x0025 (to 0x5713)
56EE:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
56EF:          04 22                     ;       COM_04_print_message length=0x0022 (to 0x5713)
56F1:             5F BE A3 15 31 6D 3B 4A 74 C0 8B 9A 3B 6E AB 98
5701:             79 68 56 90 DB 72 04 9A 53 BE 6B BF 5F BE F7 17
5711:             17 BA                 
;
;                 THE HIGHWAY TURNS GOING FROM THE NORTH TO THE WEST.
;
;                                        ;     end group_AND at 0x56EC
;
5713:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x572C)
5715:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x572D), function=COM_0A_is_input_phrase(phrase_num)
5718:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
571A:             00 C7                  ;         COM_00_move_and_look(room=RM_6_DESERT62)
;                                        ;       end case
571C:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
571E:             00 C5                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY6)
;                                        ;       end case
5720:          01 06                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0006
5722:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5728)
5724:                30 DE               ;           COM_30_set_current_room(room=RM_5_DESERT_HIGHWAY_LEADS)
5726:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x5722
;                                        ;       end case
5728:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
572A:             00 AA                  ;         COM_00_move_and_look(room=RM_6_DESERT51)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5715

; --------------------------------------------------------------------------------------------------------------------
;
572C: C7 1D 00                           ; ----- Room 0xC7 RM_6_DESERT62, Length: 0x001D, Data: 0x00
;
572F:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5732)
5731:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5732:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x574B)
5734:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x574C), function=COM_0A_is_input_phrase(phrase_num)
5737:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5739:             00 C8                  ;         COM_00_move_and_look(room=RM_6_DESERT63)
;                                        ;       end case
573B:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
573D:             00 C6                  ;         COM_00_move_and_look(room=RM_6_DESERT_HIGHWAY_TURNS)
;                                        ;       end case
573F:          01 06                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0006
5741:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5747)
5743:                30 DF               ;           COM_30_set_current_room(room=RM_5_DESERT20)
5745:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x5741
;                                        ;       end case
5747:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5749:             00 AB                  ;         COM_00_move_and_look(room=RM_6_DESERT52)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5734

; --------------------------------------------------------------------------------------------------------------------
;
574B: C8 1D 00                           ; ----- Room 0xC8 RM_6_DESERT63, Length: 0x001D, Data: 0x00
;
574E:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5751)
5750:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5751:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x576A)
5753:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x576B), function=COM_0A_is_input_phrase(phrase_num)
5756:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5758:             00 C9                  ;         COM_00_move_and_look(room=RM_6_DESERT64)
;                                        ;       end case
575A:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
575C:             00 C7                  ;         COM_00_move_and_look(room=RM_6_DESERT62)
;                                        ;       end case
575E:          01 06                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0006
5760:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5766)
5762:                30 E0               ;           COM_30_set_current_room(room=RM_5_DESERT21)
5764:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x5760
;                                        ;       end case
5766:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5768:             00 AC                  ;         COM_00_move_and_look(room=RM_6_DESERT53)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5753

; --------------------------------------------------------------------------------------------------------------------
;
576A: C9 1D 00                           ; ----- Room 0xC9 RM_6_DESERT64, Length: 0x001D, Data: 0x00
;
576D:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5770)
576F:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5770:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5789)
5772:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x578A), function=COM_0A_is_input_phrase(phrase_num)
5775:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5777:             00 CA                  ;         COM_00_move_and_look(room=RM_6_DESERT65)
;                                        ;       end case
5779:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
577B:             00 C8                  ;         COM_00_move_and_look(room=RM_6_DESERT63)
;                                        ;       end case
577D:          01 06                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0006
577F:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x5785)
5781:                30 E1               ;           COM_30_set_current_room(room=RM_5_DESERT22)
5783:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x577F
;                                        ;       end case
5785:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5787:             00 AD                  ;         COM_00_move_and_look(room=RM_6_DESERT54)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5772

; --------------------------------------------------------------------------------------------------------------------
;
5789: CA 1D 00                           ; ----- Room 0xCA RM_6_DESERT65, Length: 0x001D, Data: 0x00
;
578C:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x578F)
578E:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
578F:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x57A8)
5791:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x57A9), function=COM_0A_is_input_phrase(phrase_num)
5794:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5796:             00 CB                  ;         COM_00_move_and_look(room=RM_6_DESERT66)
;                                        ;       end case
5798:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
579A:             00 C9                  ;         COM_00_move_and_look(room=RM_6_DESERT64)
;                                        ;       end case
579C:          01 06                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0006
579E:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x57A4)
57A0:                30 E2               ;           COM_30_set_current_room(room=RM_5_DESERT23)
57A2:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x579E
;                                        ;       end case
57A4:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
57A6:             00 AE                  ;         COM_00_move_and_look(room=RM_6_DESERT55)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5791

; --------------------------------------------------------------------------------------------------------------------
;
57A8: CB 19 00                           ; ----- Room 0xCB RM_6_DESERT66, Length: 0x0019, Data: 0x00
;
57AB:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x57AE)
57AD:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
57AE:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x57C3)
57B0:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x57C4), function=COM_0A_is_input_phrase(phrase_num)
57B3:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
57B5:             00 CC                  ;         COM_00_move_and_look(room=RM_6_DESERT67)
;                                        ;       end case
57B7:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
57B9:             00 CA                  ;         COM_00_move_and_look(room=RM_6_DESERT65)
;                                        ;       end case
57BB:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
57BD:             00 E3                  ;         COM_00_move_and_look(room=RM_6_DESERT73)
;                                        ;       end case
57BF:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
57C1:             00 AF                  ;         COM_00_move_and_look(room=RM_6_DESERT56)
;                                        ;       end case
;                                        ;     end decode_switch at 0x57B0

; --------------------------------------------------------------------------------------------------------------------
;
57C3: CC 19 00                           ; ----- Room 0xCC RM_6_DESERT67, Length: 0x0019, Data: 0x00
;
57C6:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x57C9)
57C8:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
57C9:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x57DE)
57CB:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x57DF), function=COM_0A_is_input_phrase(phrase_num)
57CE:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
57D0:             00 B2                  ;         COM_00_move_and_look(room=RM_6_DESERT58)
;                                        ;       end case
57D2:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
57D4:             00 CB                  ;         COM_00_move_and_look(room=RM_6_DESERT66)
;                                        ;       end case
57D6:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
57D8:             00 CD                  ;         COM_00_move_and_look(room=RM_6_DESERT68)
;                                        ;       end case
57DA:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
57DC:             00 B0                  ;         COM_00_move_and_look(room=RM_6_DESERT_SMALL_OASIS)
;                                        ;       end case
;                                        ;     end decode_switch at 0x57CB

; --------------------------------------------------------------------------------------------------------------------
;
57DE: CD 19 00                           ; ----- Room 0xCD RM_6_DESERT68, Length: 0x0019, Data: 0x00
;
57E1:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x57E4)
57E3:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
57E4:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x57F9)
57E6:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x57FA), function=COM_0A_is_input_phrase(phrase_num)
57E9:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
57EB:             00 B3                  ;         COM_00_move_and_look(room=RM_6_DESERT59)
;                                        ;       end case
57ED:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
57EF:             00 E3                  ;         COM_00_move_and_look(room=RM_6_DESERT73)
;                                        ;       end case
57F1:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
57F3:             00 CE                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY7)
;                                        ;       end case
57F5:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
57F7:             00 CC                  ;         COM_00_move_and_look(room=RM_6_DESERT67)
;                                        ;       end case
;                                        ;     end decode_switch at 0x57E6

; --------------------------------------------------------------------------------------------------------------------
;
57F9: CE 1C 00                           ; ----- Room 0xCE RM_6_DESERT_EMPTY_HIGHWAY7, Length: 0x001C, Data: 0x00
;
57FC:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x5802)
57FE:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x5802)
5800:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
5801:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;                                        ;     end group_AND at 0x57FE
;
5802:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5817)
5804:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5818), function=COM_0A_is_input_phrase(phrase_num)
5807:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5809:             00 B4                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY5)
;                                        ;       end case
580B:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
580D:             00 E4                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY8)
;                                        ;       end case
580F:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5811:             00 CF                  ;         COM_00_move_and_look(room=RM_6_DESERT69)
;                                        ;       end case
5813:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5815:             00 CD                  ;         COM_00_move_and_look(room=RM_6_DESERT68)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5804

; --------------------------------------------------------------------------------------------------------------------
;
5817: CF 19 00                           ; ----- Room 0xCF RM_6_DESERT69, Length: 0x0019, Data: 0x00
;
581A:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x581D)
581C:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
581D:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5832)
581F:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5833), function=COM_0A_is_input_phrase(phrase_num)
5822:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5824:             00 B5                  ;         COM_00_move_and_look(room=RM_6_DESERT60)
;                                        ;       end case
5826:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5828:             00 E5                  ;         COM_00_move_and_look(room=RM_6_DESERT74)
;                                        ;       end case
582A:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
582C:             00 D0                  ;         COM_00_move_and_look(room=RM_6_DESERT70)
;                                        ;       end case
582E:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5830:             00 CE                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY7)
;                                        ;       end case
;                                        ;     end decode_switch at 0x581F

; --------------------------------------------------------------------------------------------------------------------
;
5832: D0 19 00                           ; ----- Room 0xD0 RM_6_DESERT70, Length: 0x0019, Data: 0x00
;
5835:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5838)
5837:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5838:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x584D)
583A:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x584E), function=COM_0A_is_input_phrase(phrase_num)
583D:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
583F:             00 B6                  ;         COM_00_move_and_look(room=RM_6_DESERT61)
;                                        ;       end case
5841:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5843:             00 E6                  ;         COM_00_move_and_look(room=RM_6_DESERT75)
;                                        ;       end case
5845:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5847:             00 D1                  ;         COM_00_move_and_look(room=RM_6_DESERT71)
;                                        ;       end case
5849:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
584B:             00 CF                  ;         COM_00_move_and_look(room=RM_6_DESERT69)
;                                        ;       end case
;                                        ;     end decode_switch at 0x583A

; --------------------------------------------------------------------------------------------------------------------
;
584D: D1 19 00                           ; ----- Room 0xD1 RM_6_DESERT71, Length: 0x0019, Data: 0x00
;
5850:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5853)
5852:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5853:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5868)
5855:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5869), function=COM_0A_is_input_phrase(phrase_num)
5858:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
585A:             00 B7                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE2)
;                                        ;       end case
585C:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
585E:             00 E7                  ;         COM_00_move_and_look(room=RM_6_DESERT76)
;                                        ;       end case
5860:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5862:             00 B8                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE3)
;                                        ;       end case
5864:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5866:             00 D0                  ;         COM_00_move_and_look(room=RM_6_DESERT70)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5855

; --------------------------------------------------------------------------------------------------------------------
;
5868: D2 1D 00                           ; ----- Room 0xD2 RM_6_DESERT72, Length: 0x001D, Data: 0x00
;
586B:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x586E)
586D:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
586E:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5887)
5870:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x5888), function=COM_0A_is_input_phrase(phrase_num)
5873:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5875:             00 B8                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE3)
;                                        ;       end case
5877:          04 06                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0006
5879:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x587F)
587B:                30 D3               ;           COM_30_set_current_room(room=RM_5_DESERT13)
587D:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x5879
;                                        ;       end case
587F:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5881:             00 B9                  ;         COM_00_move_and_look(room=RM_6_DESERT_LAKE4)
;                                        ;       end case
5883:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5885:             00 E7                  ;         COM_00_move_and_look(room=RM_6_DESERT76)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5870

; --------------------------------------------------------------------------------------------------------------------
;
5887: E3 1D 00                           ; ----- Room 0xE3 RM_6_DESERT73, Length: 0x001D, Data: 0x00
;
588A:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x588D)
588C:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
588D:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x58A6)
588F:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x58A7), function=COM_0A_is_input_phrase(phrase_num)
5892:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5894:             00 CD                  ;         COM_00_move_and_look(room=RM_6_DESERT68)
;                                        ;       end case
5896:          04 06                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0006
5898:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x589E)
589A:                30 E2               ;           COM_30_set_current_room(room=RM_5_DESERT23)
589C:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x5898
;                                        ;       end case
589E:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
58A0:             00 E4                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY8)
;                                        ;       end case
58A2:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
58A4:             00 CB                  ;         COM_00_move_and_look(room=RM_6_DESERT66)
;                                        ;       end case
;                                        ;     end decode_switch at 0x588F

; --------------------------------------------------------------------------------------------------------------------
;
58A6: E4 20 00                           ; ----- Room 0xE4 RM_6_DESERT_EMPTY_HIGHWAY8, Length: 0x0020, Data: 0x00
;
58A9:    03 04                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0004 (to 0x58AF)
58AB:       0D 02                        ;     COM_0D_group_AND length=0x0002 (to 0x58AF)
58AD:          AB                        ;       FN_AB_PRINT_STILL_IN_DESERT
58AE:          9B                        ;       FN_9B_PRINT_EMPTY_HIGHWAY
;                                        ;     end group_AND at 0x58AB
;
58AF:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x58C8)
58B1:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x58C9), function=COM_0A_is_input_phrase(phrase_num)
58B4:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
58B6:             00 CE                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY7)
;                                        ;       end case
58B8:          04 06                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0006
58BA:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x58C0)
58BC:                30 F0               ;           COM_30_set_current_room(room=RM_5_EMPTY_HIGHWAY_DESERT)
58BE:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x58BA
;                                        ;       end case
58C0:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
58C2:             00 E5                  ;         COM_00_move_and_look(room=RM_6_DESERT74)
;                                        ;       end case
58C4:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
58C6:             00 E3                  ;         COM_00_move_and_look(room=RM_6_DESERT73)
;                                        ;       end case
;                                        ;     end decode_switch at 0x58B1

; --------------------------------------------------------------------------------------------------------------------
;
58C8: E5 1D 00                           ; ----- Room 0xE5 RM_6_DESERT74, Length: 0x001D, Data: 0x00
;
58CB:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x58CE)
58CD:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
58CE:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x58E7)
58D0:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x58E8), function=COM_0A_is_input_phrase(phrase_num)
58D3:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
58D5:             00 CF                  ;         COM_00_move_and_look(room=RM_6_DESERT69)
;                                        ;       end case
58D7:          04 06                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0006
58D9:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x58DF)
58DB:                30 F1               ;           COM_30_set_current_room(room=RM_5_DESERT_SMALL_TRAIL1)
58DD:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x58D9
;                                        ;       end case
58DF:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
58E1:             00 E6                  ;         COM_00_move_and_look(room=RM_6_DESERT75)
;                                        ;       end case
58E3:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
58E5:             00 E4                  ;         COM_00_move_and_look(room=RM_6_DESERT_EMPTY_HIGHWAY8)
;                                        ;       end case
;                                        ;     end decode_switch at 0x58D0

; --------------------------------------------------------------------------------------------------------------------
;
58E7: E6 1D 00                           ; ----- Room 0xE6 RM_6_DESERT75, Length: 0x001D, Data: 0x00
;
58EA:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x58ED)
58EC:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
58ED:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5906)
58EF:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x5907), function=COM_0A_is_input_phrase(phrase_num)
58F2:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
58F4:             00 D0                  ;         COM_00_move_and_look(room=RM_6_DESERT70)
;                                        ;       end case
58F6:          04 06                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0006
58F8:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x58FE)
58FA:                30 F2               ;           COM_30_set_current_room(room=RM_5_DESERT_TWISTY_TRAIL)
58FC:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x58F8
;                                        ;       end case
58FE:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5900:             00 E7                  ;         COM_00_move_and_look(room=RM_6_DESERT76)
;                                        ;       end case
5902:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5904:             00 E5                  ;         COM_00_move_and_look(room=RM_6_DESERT74)
;                                        ;       end case
;                                        ;     end decode_switch at 0x58EF

; --------------------------------------------------------------------------------------------------------------------
;
5906: E7 1D 00                           ; ----- Room 0xE7 RM_6_DESERT76, Length: 0x001D, Data: 0x00
;
5909:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x590C)
590B:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
590C:    04 17                           ;   ---- Section SECTION_04_COMMANDS length=0x0017 (to 0x5925)
590E:       0B 15 0A                     ;     COM_0B_switch length=0x0015 (to 0x5926), function=COM_0A_is_input_phrase(phrase_num)
5911:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5913:             00 D1                  ;         COM_00_move_and_look(room=RM_6_DESERT71)
;                                        ;       end case
5915:          04 06                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0006
5917:             0D 04                  ;         COM_0D_group_AND length=0x0004 (to 0x591D)
5919:                30 E8               ;           COM_30_set_current_room(room=RM_5_DESERT24)
591B:                2F 05               ;           COM_2F_load_section_from_disk(section=5)
;                                        ;         end group_AND at 0x5917
;                                        ;       end case
591D:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
591F:             00 D2                  ;         COM_00_move_and_look(room=RM_6_DESERT72)
;                                        ;       end case
5921:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5923:             00 E6                  ;         COM_00_move_and_look(room=RM_6_DESERT75)
;                                        ;       end case
;                                        ;     end decode_switch at 0x590E

; --------------------------------------------------------------------------------------------------------------------
;
5925: F7 19 00                           ; ----- Room 0xF7 RM_6_DESERT77, Length: 0x0019, Data: 0x00
;
5928:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x592B)
592A:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
592B:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5940)
592D:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x5941), function=COM_0A_is_input_phrase(phrase_num)
5930:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
5932:             00 FA                  ;         COM_00_move_and_look(room=RM_6_DESERT80)
;                                        ;       end case
5934:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5936:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
5938:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
593A:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
593C:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
593E:             00 F8                  ;         COM_00_move_and_look(room=RM_6_DESERT78)
;                                        ;       end case
;                                        ;     end decode_switch at 0x592D

; --------------------------------------------------------------------------------------------------------------------
;
5940: F8 19 00                           ; ----- Room 0xF8 RM_6_DESERT78, Length: 0x0019, Data: 0x00
;
5943:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5946)
5945:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5946:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x595B)
5948:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x595C), function=COM_0A_is_input_phrase(phrase_num)
594B:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
594D:             00 F8                  ;         COM_00_move_and_look(room=RM_6_DESERT78)
;                                        ;       end case
594F:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5951:             00 F9                  ;         COM_00_move_and_look(room=RM_6_DESERT79)
;                                        ;       end case
5953:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5955:             00 F8                  ;         COM_00_move_and_look(room=RM_6_DESERT78)
;                                        ;       end case
5957:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5959:             00 F8                  ;         COM_00_move_and_look(room=RM_6_DESERT78)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5948

; --------------------------------------------------------------------------------------------------------------------
;
595B: F9 21 00                           ; ----- Room 0xF9 RM_6_DESERT79, Length: 0x0021, Data: 0x00
;
595E:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5961)
5960:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5961:    04 1B                           ;   ---- Section SECTION_04_COMMANDS length=0x001B (to 0x597E)
5963:       0B 19 0A                     ;     COM_0B_switch length=0x0019 (to 0x597F), function=COM_0A_is_input_phrase(phrase_num)
5966:          03 0A                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x000A
5968:             0E 08                  ;         COM_0E_group_OR length=0x0008 (to 0x5972)
596A:                0D 04               ;           COM_0D_group_AND length=0x0004 (to 0x5970)
596C:                   05 3E            ;             COM_05_is_leq_last_random(value=62)
596E:                   00 86            ;             COM_00_move_and_look(room=RM_6_DESERT37)
;                                        ;           end group_AND at 0x596A
5970:                00 F9               ;           COM_00_move_and_look(room=RM_6_DESERT79)
;                                        ;         end group_OR at 0x5968
;                                        ;       end case
5972:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
5974:             00 F8                  ;         COM_00_move_and_look(room=RM_6_DESERT78)
;                                        ;       end case
5976:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5978:             00 FA                  ;         COM_00_move_and_look(room=RM_6_DESERT80)
;                                        ;       end case
597A:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
597C:             00 F9                  ;         COM_00_move_and_look(room=RM_6_DESERT79)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5963

; --------------------------------------------------------------------------------------------------------------------
;
597E: FA 19 00                           ; ----- Room 0xFA RM_6_DESERT80, Length: 0x0019, Data: 0x00
;
5981:    03 01                           ;   ---- Section SECTION_03_DESCRIPTION length=0x0001 (to 0x5984)
5983:       AB                           ;     FN_AB_PRINT_STILL_IN_DESERT
;
5984:    04 13                           ;   ---- Section SECTION_04_COMMANDS length=0x0013 (to 0x5999)
5986:       0B 11 0A                     ;     COM_0B_switch length=0x0011 (to 0x599A), function=COM_0A_is_input_phrase(phrase_num)
5989:          03 02                     ;       case COM_0A_is_input_phrase("EAST * * *"), length=0x0002
598B:             00 FA                  ;         COM_00_move_and_look(room=RM_6_DESERT80)
;                                        ;       end case
598D:          04 02                     ;       case COM_0A_is_input_phrase("WEST * * *"), length=0x0002
598F:             00 F7                  ;         COM_00_move_and_look(room=RM_6_DESERT77)
;                                        ;       end case
5991:          01 02                     ;       case COM_0A_is_input_phrase("NORTH * * *"), length=0x0002
5993:             00 FA                  ;         COM_00_move_and_look(room=RM_6_DESERT80)
;                                        ;       end case
5995:          02 02                     ;       case COM_0A_is_input_phrase("SOUTH * * *"), length=0x0002
5997:             00 F9                  ;         COM_00_move_and_look(room=RM_6_DESERT79)
;                                        ;       end case
;                                        ;     end decode_switch at 0x5986
```

# Unitialized data

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

