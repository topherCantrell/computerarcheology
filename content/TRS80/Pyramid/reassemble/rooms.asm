; Room Table

; Each entry is 4 bytes. The first word is the packed room description.
; The second word is the room's command script.

RoomTable:
;
; 81 rooms numbered starting at 1
;      Description   Script
;4888: DB 5B CC 49 ; room_1
;488C: 10 5C E1 49 ; room_2
;4890: 57 5C F2 49 ; room_3
;4894: 57 5C 03 4A ; room_4
;4898: 57 5C 14 4A ; room_5
;489C: 57 5C 25 4A ; room_6
;48A0: 68 5C 36 4A ; room_7
;48A4: E2 5C 47 4A ; room_8
;48A8: 28 5D 58 4A ; room_9
;48AC: 7D 5D 69 4A ; room_10
;48B0: A0 5D 7E 4A ; room_11
;48B4: 1E 5E 87 4A ; room_12
;48B8: 8E 5E 9D 4A ; room_13
;48BC: 69 5F C8 4A ; room_14
;48C0: AB 5F D1 4A ; room_15
;48C4: 08 60 0D 4B ; room_16
;48C8: 3C 60 48 4B ; room_17
;48CC: 55 60 51 4B ; room_18
;48D0: 85 60 90 4B ; room_19
;48D4: F1 60 A9 4B ; room_20
;48D8: 5F 61 BE 4B ; room_21
;48DC: AC 61 C7 4B ; room_22
;48E0: D8 61 D8 4B ; room_23
;48E4: E0 61 E1 4B ; room_24
;48E8: 18 62 F2 4B ; room_25
;48EC: 58 62 07 4C ; room_26
;48F0: B0 62 14 4C ; room_27
;48F4: C8 62 21 4C ; room_28
;48F8: C8 62 36 4C ; room_29
;48FC: C8 62 47 4C ; room_30
;4900: C8 62 60 4C ; room_31
;4904: C8 62 69 4C ; room_32
;4908: C8 62 76 4C ; room_33
;490C: C8 62 87 4C ; room_34
;4910: C8 62 98 4C ; room_35
;4914: C8 62 B1 4C ; room_36
;4918: C8 62 C2 4C ; room_37
;491C: C8 62 CB 4C ; room_38
;4920: C8 62 DC 4C ; room_39
;4924: C8 62 E9 4C ; room_40
;4928: C8 62 F6 4C ; room_41
;492C: D8 61 03 4D ; room_42
;4930: D8 61 08 4D ; room_43
;4934: D8 61 0D 4D ; room_44
;4938: D8 61 12 4D ; room_45
;493C: D8 61 17 4D ; room_46
;4940: D8 61 1C 4D ; room_47
;4944: D8 61 21 4D ; room_48
;4948: D8 61 26 4D ; room_49
;494C: D8 61 2B 4D ; room_50
;4950: D8 61 30 4D ; room_51
;4954: EA 62 41 4D ; room_52
;4958: D8 61 56 4D ; room_53
;495C: 49 63 5B 4D ; room_54
;4960: A6 63 68 4D ; room_55
;4964: DA 63 75 4D ; room_56
;4968: 1F 64 93 4D ; room_57
;496C: 7A 64 9C 4D ; room_58
;4970: 0A 65 B1 4D ; room_59
;4974: A1 65 BE 4D ; room_60
;4978: D5 65 06 4E ; room_61
;497C: 82 66 21 4E ; room_62
;4980: E0 66 2A 4E ; room_63
;4984: 07 67 33 4E ; room_64
;4988: 29 67 3C 4E ; room_65
;498C: 89 67 65 4E ; room_66
;4990: 00 00 00 00 ; room_67
;4994: D2 6B 3B 4F ; room_68
;4998: 00 00 00 00 ; room_69
;499C: B1 6B 32 4F ; room_70
;49A0: 5C 6B 25 4F ; room_71
;49A4: 25 68 6E 4E ; room_72
;49A8: 82 68 77 4E ; room_73
;49AC: 00 00 00 00 ; room_74
;49B0: 00 00 00 00 ; room_75
;49B4: F6 68 86 4E ; room_76
;49B8: F3 6A 0E 4F ; room_77
;49BC: 3F 69 9B 4E ; room_78
;49C0: 21 6A A8 4E ; room_79
;49C4: 4B 6A B1 4E ; room_80
;49C8: 9D 6A BE 4E ; room_81

; Room Scripts

RoomScripts:

room_1:
; PS_00
; YOU_ARE_STANDING_BEFORE_THE_ENTRANCE_OF_A_PYRAMID.__AROUND_YOU__
; IS_A_DESERT.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x02          ;     MoveToRoom(room_2)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x03          ;     MoveToRoom(room_3)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x04          ;     MoveToRoom(room_4)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x05          ;     MoveToRoom(room_5)
.byte 0x0B, 0x03          ; IN
.byte 0x01, 0x02          ;     MoveToRoom(room_2)
.byte 0x00

room_2:
; PS_01
; YOU_ARE_IN_THE_ENTRANCE_TO_THE_PYRAMID.__A_HOLE_IN_THE_FLOOR____
; LEADS_TO_A_PASSAGE_BENEATH_THE_SURFACE.[CR]
;
.byte 0x03, 0x03          ; S
.byte 0x01, 0x01          ;    MoveToRoom(room_1)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x07          ;    MoveToRoom(room_7)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x01          ;    MoveToRoom(room_1)
.byte 0x12, 0x03          ; PANEL
.byte 0x01, 0x1A          ;    MoveToRoom(room_26)
.byte 0x00

room_3:
; PS_02
; YOU_ARE_IN_THE_DESERT.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x06          ;    MoveToRoom(room_6)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x03          ;    MoveToRoom(room_3)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x04          ;    MoveToRoom(room_4)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x01          ;    MoveToRoom(room_1)
.byte 0x00

room_4:
; PS_02
; YOU_ARE_IN_THE_DESERT.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x01          ;    MoveToRoom(room_1)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x03          ;    MoveToRoom(room_3)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x04          ;    MoveToRoom(room_4)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x05          ;    MoveToRoom(room_5)
.byte 0x00

room_5:
; PS_02
; YOU_ARE_IN_THE_DESERT.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x06          ;    MoveToRoom(room_6)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x01          ;    MoveToRoom(room_1)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x04          ;    MoveToRoom(room_4)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x05          ;    MoveToRoom(room_5)
.byte 0x00

room_6:
; PS_02
; YOU_ARE_IN_THE_DESERT.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x06          ;    MoveToRoom(room_6)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x03          ;    MoveToRoom(room_3)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x01          ;    MoveToRoom(room_1)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x05          ;    MoveToRoom(room_5)
.byte 0x00

room_7:
; PS_03
; YOU_ARE_IN_A_SMALL_CHAMBER_BENEATH_A_HOLE_FROM_THE_SURFACE.__A__
; LOW_CRAWL_LEADS_INWARD_TO_THE_WEST.__HIEROGLYPHICS_ON_THE_WALL__
; TRANSLATE,_"CURSE_ALL_WHO_ENTER_THIS_SACRED_CRYPT."[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x02          ;    MoveToRoom(room_2)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x02          ;    MoveToRoom(room_2)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x08          ;    MoveToRoom(room_8)
.byte 0x0B, 0x03          ; IN
.byte 0x01, 0x08          ;    MoveToRoom(room_8)
.byte 0x00

room_8:
; PS_04
; YOU_ARE_CRAWLING_OVER_PEBBLES_IN_A_LOW_PASSAGE.__THERE_IS_A_DIM_
; LIGHT_AT_THE_EAST_END_OF_THE_PASSAGE.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x07          ;    MoveToRoom(room_7)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x07          ;    MoveToRoom(room_7)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x09          ;    MoveToRoom(room_9)
.byte 0x0B, 0x03          ; IN
.byte 0x01, 0x09          ;    MoveToRoom(room_9)
.byte 0x00

room_9:
; PS_05
; YOU_ARE_IN_A_ROOM_FILLED_WITH_BROKEN_POTTERY_SHARDS_OF_ANCIENT__
; EGYPTIAN_CRAFTS.__AN_AWKWARD_CORRIDOR_LEADS_UPWARD_AND_WEST.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x08          ;    MoveToRoom(room_8)
.byte 0x0B, 0x03          ; IN
.byte 0x01, 0x0A          ;    MoveToRoom(room_10)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x0A          ;    MoveToRoom(room_10)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x0A          ;    MoveToRoom(room_10)
.byte 0x00

room_10:
; PS_06
; YOU_ARE_IN_AN_AWKWARD_SLOPING_EAST/WEST_CORRIDOR.[CR]
;
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x09          ;    MoveToRoom(room_9)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x09          ;    MoveToRoom(room_9)
.byte 0x0B, 0x03          ; IN
.byte 0x01, 0x0B          ;    MoveToRoom(room_11)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x0B          ;    MoveToRoom(room_11)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x0B          ;    MoveToRoom(room_11)
.byte 0x00

room_11:
; PS_07
; YOU_ARE_IN_A_SPLENDID_CHAMBER_THIRTY_FEET_HIGH.__THE_WALLS_ARE__
; FROZEN_RIVERS_OF_ORANGE_STONE.__AN_AWKWARD_CORRIDOR_AND_A_GOOD__
; PASSAGE_EXIT_FROM_THE_EAST_AND_WEST_SIDES_OF_THE_CHAMBER.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x0A          ;    MoveToRoom(room_10)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x0C          ;    MoveToRoom(room_12)
.byte 0x00

room_12:
; PS_08
; AT_YOUR_FEET_IS_A_SMALL_PIT_BREATHING_TRACES_OF_WHITE_MIST.__AN_
; EAST_PASSAGE_ENDS_HERE_EXCEPT_FOR_A_SMALL_CRACK_LEADING_ON._____
; ROUGH_STONE_STEPS_LEAD_DOWN_THE_PIT.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x0B          ;    MoveToRoom(room_11)
.byte 0x0A, 0x0B          ; D
.byte 0x07, 0x07          ;    StopIfPassElseContinue
.byte 0x02, 0x25          ;        AssertObjectIsInPack(obj_GOLD)
.byte 0x04                ;        Print(PS_6B:"YOU_ARE_AT_THE_BOTTOM_OF_THE_PIT_WITH_A_BROKEN_NECK.[CR]")
.word PS_6B
.byte 0x05                ;        PrintScoreAndStop
.byte 0x01, 0x0D          ;    MoveToRoom(room_13)
.byte 0x04, 0x04          ; W
.byte 0x04                ;    Print(PS_6C:"THE_CRACK_IS_FAR_TOO_SMALL_FOR_YOU_TO_FOLLOW.[CR]")
.word PS_6C
.byte 0x00

room_13:
; PS_09
; YOU_ARE_AT_ONE_END_OF_A_VAST_HALL_STRETCHING_FORWARD_OUT_OF_____
; SIGHT_TO_THE_WEST.__THERE_ARE_OPENINGS_TO_EITHER_SIDE.__NEARBY,_
; A_WIDE_STONE_STAIRCASE_LEADS_DOWNWARD.__THE_HALL_IS_VERY_MUSTY__
; AND_A_COLD_WIND_BLOWS_UP_THE_STAIRCASE.__THERE_IS_A_PASSAGE_AT__
; THE_TOP_OF_A_DOME_BEHIND_YOU.__ROUGH_STONE_STEPS_LEAD_UP_THE____
; DOME.[CR]
;
.byte 0x03, 0x03          ; S
.byte 0x01, 0x0E          ;    MoveToRoom(room_14)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x0F          ;    MoveToRoom(room_15)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x10          ;    MoveToRoom(room_16)
.byte 0x01, 0x03          ; N
.byte 0x01, 0x10          ;    MoveToRoom(room_16)
.byte 0x09, 0x0A          ; U
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x02, 0x25          ;        AssertObjectIsInPack(obj_GOLD)
.byte 0x04                ;        Print(PS_6D:"THE_DOME_IS_UNCLIMBABLE.[CR]")
.word PS_6D
.byte 0x01, 0x0C          ;    MoveToRoom(room_12)
.byte 0x02, 0x0A          ; E
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x02, 0x25          ;        AssertObjectIsInPack(obj_GOLD)
.byte 0x04                ;        Print(PS_6D:"THE_DOME_IS_UNCLIMBABLE.[CR]")
.word PS_6D
.byte 0x01, 0x0C          ;    MoveToRoom(room_12)
.byte 0x20, 0x03          ; ??20??
.byte 0x01, 0x1A          ;    MoveToRoom(room_26)
.byte 0x00

room_14:
; PS_0A
; THIS_IS_A_LOW_ROOM_WITH_A_HIEROGLYPH_ON_THE_WALL.__IT_TRANSLATES
; "YOU_WON'T_GET_IT_UP_THE_STEPS".[CR]
;
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x0D          ;    MoveToRoom(room_13)
.byte 0x01, 0x03          ; N
.byte 0x01, 0x0D          ;    MoveToRoom(room_13)
.byte 0x00

room_15:
; PS_0B
; YOU_ARE_ON_THE_EAST_BANK_OF_A_BOTTOMLESS_PIT_STRETCHING_ACROSS__
; THE_HALL.__THE_MIST_IS_QUITE_THICK_HERE,_AND_THE_PIT_IS_TOO_WIDE
; TO_JUMP.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x0D          ;    MoveToRoom(room_13)
.byte 0x10, 0x0C          ; JUMP
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x03, 0x01          ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_15)
.byte 0x04                ;        Print(PS_6E:"I_RESPECTFULLY_SUGGEST_YOU_GO_ACROSS_THE_BRIDGE_INSTEAD_OF______
.word PS_6E
;                                     JUMPING.[CR]")
.byte 0x04                ;    Print(PS_6F:"YOU_DIDN'T_MAKE_IT.[CR]")
.word PS_6F
.byte 0x05                ;    PrintScoreAndStop
.byte 0x04, 0x0A          ; W
.byte 0x07, 0x05          ;    StopIfPassElseContinue
.byte 0x03, 0x01          ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_15)
.byte 0x01, 0x12          ;        MoveToRoom(room_18)
.byte 0x04                ;    Print(PS_70:"THERE_IS_NO_WAY_ACROSS_THE_BOTTOMLESS_PIT.[CR]")
.word PS_70
.byte 0x0D, 0x05          ; CROSS
.byte 0x03, 0x01          ;    AssertObjectIsInCurrentRoomOrPack(obj_bridge_15)
.byte 0x01, 0x12          ;    MoveToRoom(room_18)
.byte 0x23, 0x18          ; WAVE
.byte 0x11, 0x11          ;    AssertObjectMatchesUserInput(obj_SCEPTER)
.byte 0x07, 0x0C          ;    StopIfPassElseContinue
.byte 0x03, 0x01          ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_15)
.byte 0x15, 0x01, 0x00    ;        MoveObjectToRoom(obj_bridge_15, room_0)
.byte 0x15, 0x02, 0x00    ;        MoveObjectToRoom(obj_bridge_18, room_0)
.byte 0x04                ;        Print(PS_AE:"THE_STONE_BRIDGE_HAS_RETRACTED![CR]")
.word PS_AE
.byte 0x18, 0x01          ;    MoveObjectToCurrentRoom(obj_bridge_15)
.byte 0x15, 0x02, 0x12    ;    MoveObjectToRoom(obj_bridge_18, room_18)
.byte 0x04                ;    Print(PS_AF:"A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]")
.word PS_AF
.byte 0x00

room_16:
; PS_0C
; YOU_ARE_IN_THE_PHARAOH'S_CHAMBER,_WITH_PASSAGES_OFF_IN_ALL______
; DIRECTIONS.[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x0D          ;    MoveToRoom(room_13)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x0D          ;    MoveToRoom(room_13)
.byte 0x03, 0x0A          ; S
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x03, 0x0B          ;        AssertObjectIsInCurrentRoomOrPack(obj_SERPENT)
.byte 0x04                ;        Print(PS_71:"YOU_CAN'T_GET_BY_THE_SERPENT.[CR]")
.word PS_71
.byte 0x01, 0x11          ;    MoveToRoom(room_17)
.byte 0x01, 0x0A          ; N
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x03, 0x0B          ;        AssertObjectIsInCurrentRoomOrPack(obj_SERPENT)
.byte 0x04                ;        Print(PS_71:"YOU_CAN'T_GET_BY_THE_SERPENT.[CR]")
.word PS_71
.byte 0x01, 0x19          ;    MoveToRoom(room_25)
.byte 0x04, 0x0A          ; W
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x03, 0x0B          ;        AssertObjectIsInCurrentRoomOrPack(obj_SERPENT)
.byte 0x04                ;        Print(PS_71:"YOU_CAN'T_GET_BY_THE_SERPENT.[CR]")
.word PS_71
.byte 0x01, 0x18          ;    MoveToRoom(room_24)
.byte 0x26, 0x10          ; THROW
.byte 0x11, 0x14          ;    AssertObjectMatchesUserInput(obj_BIRD_boxed)
.byte 0x03, 0x0B          ;    AssertObjectIsInCurrentRoomOrPack(obj_SERPENT)
.byte 0x15, 0x0B, 0x00    ;    MoveObjectToRoom(obj_SERPENT, room_0)
.byte 0x18, 0x13          ;    MoveObjectToCurrentRoom(obj_BIRD)
.byte 0x15, 0x14, 0x00    ;    MoveObjectToRoom(obj_BIRD_boxed, room_0)
.byte 0x04                ;    Print(PS_B4:"THE_BIRD_STATUE_COMES_TO_LIFE_AND_ATTACKS_THE_SERPENT_AND_IN_AN_
.word PS_B4
;                                 ASTOUNDING_FLURRY,_DRIVES_THE_SERPENT_AWAY.__THE_BIRD_TURNS_BACK
;                                 INTO_A_STATUE.[CR]")
.byte 0x00

room_17:
; PS_0D
; YOU_ARE_IN_THE_SOUTH_SIDE_CHAMBER.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x10          ;    MoveToRoom(room_16)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x10          ;    MoveToRoom(room_16)
.byte 0x00

room_18:
; PS_0E
; YOU_ARE_ON_THE_WEST_SIDE_OF_THE_BOTTOMLESS_PIT_IN_THE_HALL_OF___
; GODS.[CR]
;
.byte 0x10, 0x0C          ; JUMP
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x03, 0x02          ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_18)
.byte 0x04                ;        Print(PS_6E:"I_RESPECTFULLY_SUGGEST_YOU_GO_ACROSS_THE_BRIDGE_INSTEAD_OF______
.word PS_6E
;                                     JUMPING.[CR]")
.byte 0x04                ;    Print(PS_6F:"YOU_DIDN'T_MAKE_IT.[CR]")
.word PS_6F
.byte 0x05                ;    PrintScoreAndStop
.byte 0x02, 0x0A          ; E
.byte 0x07, 0x05          ;    StopIfPassElseContinue
.byte 0x03, 0x02          ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_18)
.byte 0x01, 0x0F          ;        MoveToRoom(room_15)
.byte 0x04                ;    Print(PS_70:"THERE_IS_NO_WAY_ACROSS_THE_BOTTOMLESS_PIT.[CR]")
.word PS_70
.byte 0x01, 0x06          ; N
.byte 0x04                ;    Print(PS_72:"YOU_HAVE_CRAWLED_THROUGH_A_VERY_LOW_WIDE_PASSAGE_PARALLEL_TO_AND
.word PS_72
;                                 NORTH_OF_THE_HALL_OF_GODS.[CR]")
.byte 0x01, 0x13          ;    MoveToRoom(room_19)
.byte 0x0D, 0x05          ; CROSS
.byte 0x03, 0x02          ;    AssertObjectIsInCurrentRoomOrPack(obj_bridge_18)
.byte 0x01, 0x0F          ;    MoveToRoom(room_15)
.byte 0x23, 0x18          ; WAVE
.byte 0x11, 0x11          ;    AssertObjectMatchesUserInput(obj_SCEPTER)
.byte 0x07, 0x0C          ;    StopIfPassElseContinue
.byte 0x03, 0x02          ;        AssertObjectIsInCurrentRoomOrPack(obj_bridge_18)
.byte 0x15, 0x02, 0x00    ;        MoveObjectToRoom(obj_bridge_18, room_0)
.byte 0x15, 0x01, 0x00    ;        MoveObjectToRoom(obj_bridge_15, room_0)
.byte 0x04                ;        Print(PS_AE:"THE_STONE_BRIDGE_HAS_RETRACTED![CR]")
.word PS_AE
.byte 0x18, 0x02          ;    MoveObjectToCurrentRoom(obj_bridge_18)
.byte 0x15, 0x01, 0x0F    ;    MoveObjectToRoom(obj_bridge_15, room_15)
.byte 0x04                ;    Print(PS_AF:"A_STONE_BRIDGE_NOW_SPANS_THE_BOTTOMLESS_PIT.[CR]")
.word PS_AF
.byte 0x00

room_19:
; PS_0F
; YOU_ARE_AT_THE_WEST_END_OF_THE_HALL_OF_GODS.___A_LOW_WIDE_PASS__
; CONTINUES_WEST_AND_ANOTHER_GOES_NORTH.__TO_THE_SOUTH_IS_A_LITTLE
; PASSAGE_SIX_FEET_OFF_THE_FLOOR.[CR]
;
.byte 0x03, 0x03          ; S
.byte 0x01, 0x1C          ;    MoveToRoom(room_28)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x1C          ;    MoveToRoom(room_28)
.byte 0x11, 0x03          ; CLIMB
.byte 0x01, 0x1C          ;    MoveToRoom(room_28)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x12          ;    MoveToRoom(room_18)
.byte 0x01, 0x03          ; N
.byte 0x01, 0x12          ;    MoveToRoom(room_18)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x14          ;    MoveToRoom(room_20)
.byte 0x00

room_20:
; PS_10
; YOU_ARE_AT_EAST_END_OF_A_VERY_LONG_HALL_APPARENTLY_WITHOUT_SIDE_
; CHAMBERS.__TO_THE_EAST_A_LOW_WIDE_CRAWL_SLANTS_UP.__TO_THE_NORTH
; A_ROUND_TWO_FOOT_HOLE_SLANTS_DOWN.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x13          ;    MoveToRoom(room_19)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x13          ;    MoveToRoom(room_19)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x15          ;    MoveToRoom(room_21)
.byte 0x01, 0x03          ; N
.byte 0x01, 0x16          ;    MoveToRoom(room_22)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x16          ;    MoveToRoom(room_22)
.byte 0x00

room_21:
; PS_11
; YOU_ARE_AT_THE_WEST_END_OF_A_VERY_LONG_FEATURELESS_HALL.__THE___
; HALL_JOINS_; UP_WITH_A_NARROW_NORTH/SOUTH_PASSAGE.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x14          ;    MoveToRoom(room_20)
.byte 0x01, 0x03          ; N
.byte 0x01, 0x16          ;    MoveToRoom(room_22)
.byte 0x00

room_22:
; PS_12
; YOU_ARE_AT_A_CROSSOVER_OF_A_HIGH_N/S_PASSAGE_AND_A_LOW_E/W_ONE.[CR]
;
.byte 0x04, 0x03          ; W
.byte 0x01, 0x14          ;    MoveToRoom(room_20)
.byte 0x01, 0x03          ; N
.byte 0x01, 0x17          ;    MoveToRoom(room_23)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x18          ;    MoveToRoom(room_24)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x15          ;    MoveToRoom(room_21)
.byte 0x00

room_23:
; PS_13
; DEAD_END.[CR]
;
.byte 0x03, 0x03          ; S
.byte 0x01, 0x16          ;    MoveToRoom(room_22)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x16          ;    MoveToRoom(room_22)
.byte 0x00

room_24:
; PS_14
; YOU_ARE_IN_THE_WEST_THRONE_CHAMBER.__A_PASSAGE_CONTINUES_WEST___
; AND_UP_FROM_HERE.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x10          ;    MoveToRoom(room_16)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x10          ;    MoveToRoom(room_16)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x16          ;    MoveToRoom(room_22)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x16          ;    MoveToRoom(room_22)
.byte 0x00

room_25:
; PS_15
; YOU_ARE_IN_A_LOW_N/S_PASSAGE_AT_A_HOLE_IN_THE_FLOOR.__THE_HOLE__
; GOES_DOWN_TO_AN_E/W_PASSAGE.[CR]
;
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x10          ;    MoveToRoom(room_16)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x10          ;    MoveToRoom(room_16)
.byte 0x01, 0x03          ; N
.byte 0x01, 0x1A          ;    MoveToRoom(room_26)
.byte 0x20, 0x03          ; ??20??
.byte 0x01, 0x1A          ;    MoveToRoom(room_26)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x36          ;    MoveToRoom(room_54)
.byte 0x00

room_26:
; PS_16
; YOU_ARE_IN_A_LARGE_ROOM,_WITH_A_PASSAGE_TO_THE_SOUTH,_AND_A_WALL
; OF_BROKEN_ROCK_TO_THE_EAST.__THERE_IS_A_PANEL_ON_THE_NORTH_WALL.[CR]
;
.byte 0x12, 0x03          ; PANEL
.byte 0x01, 0x02          ;    MoveToRoom(room_2)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x19          ;    MoveToRoom(room_25)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x1B          ;    MoveToRoom(room_27)
.byte 0x00

room_27:
; PS_17
; YOU_ARE_IN_THE_CHAMBER_OF_ANUBIS.[CR]
;
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x1A          ;    MoveToRoom(room_26)
.byte 0x20, 0x03          ; ??20??
.byte 0x01, 0x1A          ;    MoveToRoom(room_26)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x0D          ;    MoveToRoom(room_13)
.byte 0x00

room_28:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x1C          ;    MoveToRoom(room_28)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x20          ;    MoveToRoom(room_32)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x1E          ;    MoveToRoom(room_30)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x1D          ;    MoveToRoom(room_29)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x13          ;    MoveToRoom(room_19)
.byte 0x00

room_29:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x1C          ;    MoveToRoom(room_28)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x33          ;    MoveToRoom(room_51)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x1D          ;    MoveToRoom(room_29)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x1D          ;    MoveToRoom(room_29)
.byte 0x00

room_30:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x20          ;    MoveToRoom(room_32)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x2A          ;    MoveToRoom(room_42)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x2B          ;    MoveToRoom(room_43)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x1C          ;    MoveToRoom(room_28)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x1F          ;    MoveToRoom(room_31)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x1F          ;    MoveToRoom(room_31)
.byte 0x00

room_31:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x1E          ;    MoveToRoom(room_30)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x1E          ;    MoveToRoom(room_30)
.byte 0x00

room_32:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x1E          ;    MoveToRoom(room_30)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x21          ;    MoveToRoom(room_33)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x1C          ;    MoveToRoom(room_28)
.byte 0x00

room_33:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x2C          ;    MoveToRoom(room_44)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x20          ;    MoveToRoom(room_32)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x22          ;    MoveToRoom(room_34)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x2D          ;    MoveToRoom(room_45)
.byte 0x00

room_34:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x21          ;    MoveToRoom(room_33)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x23          ;    MoveToRoom(room_35)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x25          ;    MoveToRoom(room_37)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x26          ;    MoveToRoom(room_38)
.byte 0x00

room_35:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x24          ;    MoveToRoom(room_36)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x26          ;    MoveToRoom(room_38)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x23          ;    MoveToRoom(room_35)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x22          ;    MoveToRoom(room_34)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x27          ;    MoveToRoom(room_39)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x2F          ;    MoveToRoom(room_47)
.byte 0x00

room_36:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x24          ;    MoveToRoom(room_36)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x34          ;    MoveToRoom(room_52)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x23          ;    MoveToRoom(room_35)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x30          ;    MoveToRoom(room_48)
.byte 0x00

room_37:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x22          ;    MoveToRoom(room_34)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x26          ;    MoveToRoom(room_38)
.byte 0x00

room_38:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x23          ;    MoveToRoom(room_35)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x27          ;    MoveToRoom(room_39)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x25          ;    MoveToRoom(room_37)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x22          ;    MoveToRoom(room_34)
.byte 0x00

room_39:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x23          ;    MoveToRoom(room_35)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x2E          ;    MoveToRoom(room_46)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x26          ;    MoveToRoom(room_38)
.byte 0x00

room_40:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x34          ;    MoveToRoom(room_52)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x29          ;    MoveToRoom(room_41)
.byte 0x08, 0x03          ; NW
.byte 0x01, 0x35          ;    MoveToRoom(room_53)
.byte 0x00

room_41:
; PS_18
; YOU_ARE_IN_A_MAZE_OF_TWISTY_PASSAGES,_ALL_ALIKE.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x28          ;    MoveToRoom(room_40)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x34          ;    MoveToRoom(room_52)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x32          ;    MoveToRoom(room_50)
.byte 0x00

room_42:
; PS_13
; DEAD_END.[CR]
;
.byte 0x04, 0x03          ; W
.byte 0x01, 0x1E          ;    MoveToRoom(room_30)
.byte 0x00

room_43:
; PS_13
; DEAD_END.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x1E          ;    MoveToRoom(room_30)
.byte 0x00

room_44:
; PS_13
; DEAD_END.[CR]
;
.byte 0x03, 0x03          ; S
.byte 0x01, 0x21          ;    MoveToRoom(room_33)
.byte 0x00

room_45:
; PS_13
; DEAD_END.[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x21          ;    MoveToRoom(room_33)
.byte 0x00

room_46:
; PS_13
; DEAD_END.[CR]
;
.byte 0x04, 0x03          ; W
.byte 0x01, 0x27          ;    MoveToRoom(room_39)
.byte 0x00

room_47:
; PS_13
; DEAD_END.[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x23          ;    MoveToRoom(room_35)
.byte 0x00

room_48:
; PS_13
; DEAD_END.[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x24          ;    MoveToRoom(room_36)
.byte 0x00

room_49:
; PS_13
; DEAD_END.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x34          ;    MoveToRoom(room_52)
.byte 0x00

room_50:
; PS_13
; DEAD_END.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x29          ;    MoveToRoom(room_41)
.byte 0x00

room_51:
; PS_13
; DEAD_END.[CR]
;
.byte 0x04, 0x03          ; W
.byte 0x01, 0x1D          ;    MoveToRoom(room_29)
.byte 0x21, 0x0B          ; DROP
.byte 0x11, 0x29          ;    AssertObjectMatchesUserInput(obj_COINS)
.byte 0x15, 0x29, 0x00    ;    MoveObjectToRoom(obj_COINS, room_0)
.byte 0x18, 0x23          ;    MoveObjectToCurrentRoom(obj_BATTERIES_fresh)
.byte 0x04                ;    Print(PS_B2:"THERE_ARE_NOW_SOME_FRESH_BATTERIES_HERE.[CR]")
.word PS_B2
.byte 0x00

room_52:
; PS_19
; YOU_ARE_ON_THE_BRINK_OF_A_LARGE_PIT.__YOU_COULD_CLIMB_DOWN,_BUT_
; YOU_WOULD_NOT_BE_ABLE_TO_CLIMB_BACK_UP.__THE_MAZE_CONTINUES_ON__
; THIS_LEVEL.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x29          ;    MoveToRoom(room_41)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x28          ;    MoveToRoom(room_40)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x31          ;    MoveToRoom(room_49)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x24          ;    MoveToRoom(room_36)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x0B          ;    MoveToRoom(room_11)
.byte 0x00

room_53:
; PS_13
; DEAD_END.[CR]
;
.byte 0x06, 0x03          ; SE
.byte 0x01, 0x28          ;    MoveToRoom(room_40)
.byte 0x00

room_54:
; PS_1A
; YOU_ARE_IN_A_DIRTY_BROKEN_PASSAGE.__TO_THE_EAST_IS_A_CRAWL.__TO_
; THE_WEST_IS_A_LARGE_PASSAGE.__ABOVE_YOU_IS_A_HOLE_TO_ANOTHER____
; PASSAGE.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x37          ;    MoveToRoom(room_55)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x39          ;    MoveToRoom(room_57)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x19          ;    MoveToRoom(room_25)
.byte 0x00

room_55:
; PS_1B
; YOU_ARE_ON_THE_BRINK_OF_A_SMALL_CLEAN_CLIMBABLE_PIT.__A_CRAWL___
; LEADS_WEST.[CR]
;
.byte 0x04, 0x03          ; W
.byte 0x01, 0x36          ;    MoveToRoom(room_54)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x38          ;    MoveToRoom(room_56)
.byte 0x11, 0x03          ; CLIMB
.byte 0x01, 0x38          ;    MoveToRoom(room_56)
.byte 0x00

room_56:
; PS_1C
; YOU_ARE_IN_THE_BOTTOM_OF_A_SMALL_PIT_WITH_A_LITTLE_STREAM,_WHICH
; ENTERS_AND_EXITS_THROUGH_TINY_SLITS.[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x37          ;    MoveToRoom(room_55)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x37          ;    MoveToRoom(room_55)
.byte 0x11, 0x03          ; CLIMB
.byte 0x01, 0x37          ;    MoveToRoom(room_55)
.byte 0x0A, 0x04          ; D
.byte 0x04                ;    Print(PS_73:"YOU_DON'T_FIT_THROUGH_TWO-INCH_SLIT![CR]")
.word PS_73
.byte 0x27, 0x0B          ; FILL
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x02, 0x1C          ;        AssertObjectIsInPack(obj_WATER)
.byte 0x04                ;        Print(PS_AC:"YOUR_BOTTLE_IS_ALREADY_FULL.[CR]")
.word PS_AC
.byte 0x19, 0x1C, 0x1B    ;    MoveObjectIntoContainer(obj_WATER, obj_BOTTLE)
.byte 0x00

room_57:
; PS_1D
; YOU_ARE_IN_A_THE_ROOM_OF_BES,_WHOSE_PICTURE_IS_ON_THE_WALL._____
; THERE_IS_A_BIG_HOLE_IN_THE_FLOOR.__THERE_IS_A_PASSAGE_LEADING___
; EAST.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x36          ;    MoveToRoom(room_54)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x3A          ;    MoveToRoom(room_58)
.byte 0x00

room_58:
; PS_1E
; YOU_ARE_AT_A_COMPLEX_JUNCTION.__A_LOW_HANDS_AND_KNEES_PASSAGE___
; FROM_THE_NORTH_JOINS_A_HIGHER_CRAWL_FROM_THE_EAST_TO_MAKE_A_____
; WALKING_PASSAGE_GOING_WEST.__THERE_IS_ALSO_A_LARGE_ROOM_ABOVE.__
; THE_AIR_IS_DAMP_HERE.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x3D          ;    MoveToRoom(room_61)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x41          ;    MoveToRoom(room_65)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x39          ;    MoveToRoom(room_57)
.byte 0x11, 0x03          ; CLIMB
.byte 0x01, 0x39          ;    MoveToRoom(room_57)
.byte 0x00

room_59:
; PS_1F
; YOU_ARE_IN_THE_UNDERWORLD_ANTEROOM_OF_SEKER.__PASSAGES_GO_EAST,_
; WEST,_AND_UP.__HUMAN_BONES_ARE_STREWN_ABOUT_ON_THE_FLOOR._______
; HIEROGLYPHICS_ON_THE_WALL_ROUGHLY_TRANSLATE_TO_"THOSE_WHO_______
; PROCEED_EAST_MAY_NEVER_RETURN."[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x3C          ;    MoveToRoom(room_60)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x41          ;    MoveToRoom(room_65)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x3A          ;    MoveToRoom(room_58)
.byte 0x00

room_60:
; PS_20
; YOU_ARE_AT_THE_LAND_OF_DEAD.__PASSAGES_LEAD_OFF_IN_>ALL<________
; DIRECTIONS.[CR]
;
.byte 0x01, 0x07          ; N
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xF0          ;        AssertRandomIsLessOrEqual(240)
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x02, 0x07          ; E
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xF0          ;        AssertRandomIsLessOrEqual(240)
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x03, 0x07          ; S
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xF0          ;        AssertRandomIsLessOrEqual(240)
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x05, 0x07          ; NE
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xF0          ;        AssertRandomIsLessOrEqual(240)
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x06, 0x07          ; SE
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xF0          ;        AssertRandomIsLessOrEqual(240)
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x07, 0x07          ; SW
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xF0          ;        AssertRandomIsLessOrEqual(240)
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x08, 0x07          ; NW
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xF0          ;        AssertRandomIsLessOrEqual(240)
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x09, 0x07          ; U
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xF0          ;        AssertRandomIsLessOrEqual(240)
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x04, 0x06          ; W
.byte 0x04                ;    Print(PS_75:"YOU_HAVE_CRAWLED_AROUND_IN_SOME_LITTLE_HOLES_AND_FOUND_YOUR_WAY_
.word PS_75
;                                 BLOCKED_BY_A_FALLEN_SLAB.__YOU_ARE_NOW_BACK_IN_THE_MAIN_PASSAGE.[CR]")
.byte 0x01, 0x3C          ;    MoveToRoom(room_60)
.byte 0x00

room_61:
; PS_21
; YOU'RE_IN_A_LARGE_ROOM_WITH_ANCIENT_DRAWINGS_ON_ALL_WALLS.______
; THE_PICTURES_DEPICT_ATUM,_A_PHARAOH_WEARING_THE_DOUBLE_CROWN.___
; A_SHALLOW_PASSAGE_PROCEEDS_DOWNWARD,_AND_A_SOMEWHAT_STEEPER_ONE_
; LEADS_UP.__A_LOW_HANDS_AND_KNEES_PASSAGE_ENTERS_FROM_THE_SOUTH. [CR]
;
.byte 0x03, 0x11          ; S
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x02, 0x17          ;        AssertObjectIsInPack(obj_SARCOPH_full)
.byte 0x04                ;        Print(PS_76:"YOU_CAN'T_FIT_THIS_BIG_SARCOPHAGUS_THROUGH_THAT_LITTLE_PASSAGE![CR]")
.word PS_76
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x02, 0x18          ;        AssertObjectIsInPack(obj_SARCOPH_empty)
.byte 0x04                ;        Print(PS_76:"YOU_CAN'T_FIT_THIS_BIG_SARCOPHAGUS_THROUGH_THAT_LITTLE_PASSAGE![CR]")
.word PS_76
.byte 0x01, 0x3A          ;    MoveToRoom(room_58)
.byte 0x09, 0x03          ; U
.byte 0x01, 0x3E          ;    MoveToRoom(room_62)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x3F          ;    MoveToRoom(room_63)
.byte 0x00

room_62:
; PS_22
; YOU_ARE_IN_A_CHAMBER_WHOSE_WALL_CONTAINS_A_PICTURE_OF_A_MAN_____
; WEARING_THE_LUNAR_DISK_ON_HIS_HEAD.__HE_IS_THE_GOD_KHONS,_THE___
; MOON_GOD.[CR]
;
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x3D          ;    MoveToRoom(room_61)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x3D          ;    MoveToRoom(room_61)
.byte 0x00

room_63:
; PS_23
; YOU_ARE_IN_A_LONG_SLOPING_CORRIDOR_WITH_RAGGED_WALLS._ [CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x3D          ;    MoveToRoom(room_61)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x40          ;    MoveToRoom(room_64)
.byte 0x00

room_64:
; PS_24
; YOU_ARE_IN_A_CUL-DE-SAC_ABOUT_EIGHT_FEET_ACROSS.[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x3F          ;    MoveToRoom(room_63)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x3F          ;    MoveToRoom(room_63)
.byte 0x00

room_65:
; PS_25
; YOU_ARE_IN_THE_CHAMBER_OF_HORUS,_A_LONG_EAST/WEST_PASSAGE_WITH__
; HOLES_EVERYWHERE.__TO_EXPLORE_AT_RANDOM,_SELECT_NORTH,_SOUTH,___
; UP,_OR_DOWN.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x3A          ;    MoveToRoom(room_58)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x4E          ;    MoveToRoom(room_78)
.byte 0x09, 0x07          ; U
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xCC          ;        AssertRandomIsLessOrEqual(204)
.byte 0x01, 0x48          ;    MoveToRoom(room_72)
.byte 0x01, 0x07          ; N
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xCC          ;        AssertRandomIsLessOrEqual(204)
.byte 0x01, 0x49          ;    MoveToRoom(room_73)
.byte 0x03, 0x07          ; S
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xCC          ;        AssertRandomIsLessOrEqual(204)
.byte 0x01, 0x42          ;    MoveToRoom(room_66)
.byte 0x0A, 0x07          ; D
.byte 0x07, 0x03          ;    StopIfPassElseContinue
.byte 0x0A, 0xCC          ;        AssertRandomIsLessOrEqual(204)
.byte 0x01, 0x3B          ;    MoveToRoom(room_59)
.byte 0x00

room_66:
; PS_26
; YOU_ARE_IN_A_LARGE_LOW_CIRCULAR_CHAMBER_WHOSE_FLOOR_IS_AN_______
; IMMENSE_SLAB_FALLEN_FROM_THE_CEILING.__EAST_AND_WEST_THERE_ONCE_
; WHERE_LARGE_PASSAGES,_BUT_THEY_ARE_NOW_FILLED_WITH_SAND.________
; LOW_SMALL_PASSAGES_GO_NORTH_AND_SOUTH.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x41          ;    MoveToRoom(room_65)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x50          ;    MoveToRoom(room_80)
.byte 0x00

room_72:
; PS_27
; YOU_ARE_IN_THE_PRIEST'S_BEDROOM.__THE_WALLS_ARE_COVERED_WITH____
; CURTAINS,_THE_FLOOR_WITH_A_THICK_PILE_CARPET.__MOSS_COVERS_THE__
; CEILING.[CR]
;
.byte 0x04, 0x03          ; W
.byte 0x01, 0x41          ;    MoveToRoom(room_65)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x41          ;    MoveToRoom(room_65)
.byte 0x00

room_73:
; PS_28
; THIS_IS_THE_CHAMBER_OF_THE_HIGH_PRIEST.___ANCIENT_DRAWINGS_COVER
; THE_WALLS.__AN_EXTREMELY_TIGHT_TUNNEL_LEADS_WEST.__IT_LOOKS_LIKE
; A_TIGHT_SQUEEZE.__ANOTHER_PASSAGE_LEADS_SE.[CR]
;
.byte 0x04, 0x09          ; W
.byte 0x07, 0x04          ;    StopIfPassElseContinue
.byte 0x0D                ;        AssertPackIsEmptyExceptForEmerald
.byte 0x01, 0x4C          ;        MoveToRoom(room_76)
.byte 0x04                ;    Print(PS_77:"SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.
.word PS_77
;                                 YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]")
.byte 0x06, 0x03          ; SE
.byte 0x01, 0x41          ;    MoveToRoom(room_65)
.byte 0x00

room_76:
; PS_29
; YOU_ARE_IN_THE_HIGH_PRIEST'S_TREASURE_ROOM_LIT_BY_AN_EERIE_GREEN
; LIGHT.__A_NARROW_TUNNEL_EXITS_TO_THE_EAST.[CR]
;
.byte 0x02, 0x09          ; E
.byte 0x07, 0x04          ;    StopIfPassElseContinue
.byte 0x0D                ;        AssertPackIsEmptyExceptForEmerald
.byte 0x01, 0x49          ;        MoveToRoom(room_73)
.byte 0x04                ;    Print(PS_77:"SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.
.word PS_77
;                                 YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]")
.byte 0x0C, 0x09          ; OUT
.byte 0x07, 0x04          ;    StopIfPassElseContinue
.byte 0x0D                ;        AssertPackIsEmptyExceptForEmerald
.byte 0x01, 0x49          ;        MoveToRoom(room_73)
.byte 0x04                ;    Print(PS_77:"SOMETHING_YOU'RE_CARRYING_WON'T_FIT_THROUGH_THE_TUNNEL_WITH_YOU.
.word PS_77
;                                 YOU'D_BEST_TAKE_INVENTORY_AND_DROP_SOMETHING.[CR]")
.byte 0x00

room_78:
; PS_2A
; YOU_ARE_AT_THE_EAST_END_OF_THE_TWOPIT_ROOM.__THE_FLOOR_HERE_IS__
; LITTERED_WITH_THIN_ROCK_SLABS,_WHICH_MAKE_IT_EASY_TO_DESCEND_THE
; PITS.__THERE_IS_A_PATH_HERE_BYPASSING_THE_PITS_TO_CONNECT_______
; PASSAGES_EAST_AND_WEST.__THERE_ARE_HOLES_ALL_OVER,_BUT_THE_ONLY_
; BIG_ONE_IS_ON_THE_WALL_DIRECTLY_OVER_THE_WEST_PIT_WHERE_YOU_____
; CAN'T_GET_TO_IT.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x41          ;    MoveToRoom(room_65)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x50          ;    MoveToRoom(room_80)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x4F          ;    MoveToRoom(room_79)
.byte 0x00

room_79:
; PS_2B
; YOU_ARE_AT_THE_BOTTOM_OF_THE_EASTERN_PIT_IN_THE_TWOPIT_ROOM.[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x4E          ;    MoveToRoom(room_78)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x4E          ;    MoveToRoom(room_78)
.byte 0x00

room_80:
; PS_2C
; YOU_ARE_AT_THE_WEST_END_OF_THE_TWOPIT_ROOM.__THERE_IS_A_LARGE___
; HOLE_IN_THE_WALL_ABOVE_THE_PIT_AT_THIS_END_OF_THE_ROOM.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x4E          ;    MoveToRoom(room_78)
.byte 0x04, 0x03          ; W
.byte 0x01, 0x42          ;    MoveToRoom(room_66)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x51          ;    MoveToRoom(room_81)
.byte 0x00

room_81:
; PS_2D
; YOU_ARE_AT_THE_BOTTOM_OF_THE_WEST_PIT_IN_THE_TWOPIT_ROOM.__THERE
; IS_A_LARGE_HOLE_IN_THE_WALL_ABOUT_TWENTY_FIVE_FEET_ABOVE_YOU.[CR]
;
.byte 0x09, 0x03          ; U
.byte 0x01, 0x50          ;    MoveToRoom(room_80)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x50          ;    MoveToRoom(room_80)
.byte 0x11, 0x16          ; CLIMB
.byte 0x07, 0x08          ;    StopIfPassElseContinue
.byte 0x03, 0x09          ;        AssertObjectIsInCurrentRoomOrPack(obj_PLANT_C)
.byte 0x04                ;        Print(PS_78:"YOU_CLAMBER_UP_THE_PLANT_AND_SCURRY_THROUGH_THE_HOLE_AT_THE_TOP.[CR]")
.word PS_78
.byte 0x01, 0x4D          ;        MoveToRoom(room_77)
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x03, 0x08          ;        AssertObjectIsInCurrentRoomOrPack(obj_PLANT_B)
.byte 0x04                ;        Print(PS_79:"YOU'VE_CLIMBED_UP_THE_PLANT_AND_OUT_OF_THE_PIT.[CR]")
.word PS_79
.byte 0x01, 0x50          ;    MoveToRoom(room_80)
.byte 0x04                ;    Print(PS_B8:"THERE_IS_NOTHING_HERE_TO_CLIMB.__USE_UP_OR_OUT_TO_LEAVE_THE_PIT.[CR]")
.word PS_B8
.byte 0x24, 0x2F          ; POUR
.byte 0x11, 0x1C          ;    AssertObjectMatchesUserInput(obj_WATER)
.byte 0x15, 0x1C, 0x00    ;    MoveObjectToRoom(obj_WATER, room_0)
.byte 0x07, 0x0E          ;    StopIfPassElseContinue
.byte 0x03, 0x07          ;        AssertObjectIsInCurrentRoomOrPack(obj_PLANT_A)
.byte 0x15, 0x07, 0x00    ;        MoveObjectToRoom(obj_PLANT_A, room_0)
.byte 0x18, 0x08          ;        MoveObjectToCurrentRoom(obj_PLANT_B)
.byte 0x04                ;        Print(PS_B5:"THE_PLANT_SPURTS_INTO_FURIOUS_GROWTH_FOR_A_FEW_SECONDS.[CR]")
.word PS_B5
.byte 0x04                ;        Print(PS_4C:"THERE_IS_A_TWELVE_FOOT_BEAN_STALK_STRETCHING_UP_OUT_OF_THE_PIT,_
.word PS_4C
;                                     BELLOWING_"WATER..._WATER..."[CR]")
.byte 0x07, 0x0E          ;    StopIfPassElseContinue
.byte 0x03, 0x08          ;        AssertObjectIsInCurrentRoomOrPack(obj_PLANT_B)
.byte 0x15, 0x08, 0x00    ;        MoveObjectToRoom(obj_PLANT_B, room_0)
.byte 0x18, 0x09          ;        MoveObjectToCurrentRoom(obj_PLANT_C)
.byte 0x04                ;        Print(PS_B6:"THE_PLANT_GROWS_EXPLOSIVELY,_ALMOST_FILLING_THE_BOTTOM_OF_THE___
.word PS_B6
;                                     PIT.[CR]")
.byte 0x04                ;        Print(PS_4D:"THERE_IS_A_GIGANTIC_BEAN_STALK_STRETCHING_ALL_THE_WAY_UP_TO_THE_
.word PS_4D
;                                     HOLE.[CR]")
.byte 0x15, 0x09, 0x00    ;    MoveObjectToRoom(obj_PLANT_C, room_0)
.byte 0x18, 0x07          ;    MoveObjectToCurrentRoom(obj_PLANT_A)
.byte 0x04                ;    Print(PS_B7:"YOU'VE_OVER-WATERED_THE_PLANT!__IT'S_SHRIVELING_UP![CR]")
.word PS_B7
.byte 0x04                ;    Print(PS_4B:"THERE_IS_A_TINY_PLANT_IN_THE_PIT,_MURMURING_"WATER,_WATER,_..."[CR]")
.word PS_4B
.byte 0x00

room_77:
; PS_2E
; YOU_ARE_IN_A_LONG,_NARROW_CORRIDOR_STRETCHING_OUT_OF_SIGHT_TO___
; THE_WEST.__AT_THE_EASTERN_END_IS_A_HOLE_THROUGH_WHICH_YOU_CAN___
; SEE_A_PROFUSION_OF_LEAVES.[CR]
;
.byte 0x02, 0x03          ; E
.byte 0x01, 0x51          ;    MoveToRoom(room_81)
.byte 0x0A, 0x03          ; D
.byte 0x01, 0x51          ;    MoveToRoom(room_81)
.byte 0x11, 0x03          ; CLIMB
.byte 0x01, 0x51          ;    MoveToRoom(room_81)
.byte 0x10, 0x05          ; JUMP
.byte 0x04                ;    Print(PS_6B:"YOU_ARE_AT_THE_BOTTOM_OF_THE_PIT_WITH_A_BROKEN_NECK.[CR]")
.word PS_6B
.byte 0x05                ;    PrintScoreAndStop
.byte 0x04, 0x03          ; W
.byte 0x01, 0x47          ;    MoveToRoom(room_71)
.byte 0x00

room_71:
; PS_2F
; YOU_ARE_IN_THE_CHAMBER_OF_OSIRIS._THE_CEILING_IS_TOO_HIGH_UP_FOR
; YOUR_LAMP_TO_SHOW_IT.__PASSAGES_LEAD_EAST,_NORTH,_AND_SOUTH.[CR]
;
.byte 0x01, 0x03          ; N
.byte 0x01, 0x44          ;    MoveToRoom(room_68)
.byte 0x02, 0x03          ; E
.byte 0x01, 0x46          ;    MoveToRoom(room_70)
.byte 0x03, 0x03          ; S
.byte 0x01, 0x4D          ;    MoveToRoom(room_77)
.byte 0x00

room_70:
; PS_30
; THE_PASSAGE_HERE_IS_BLOCKED_BY_A_FALLEN_BLOCK.[CR]
;
.byte 0x03, 0x03          ; S
.byte 0x01, 0x47          ;    MoveToRoom(room_71)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x47          ;    MoveToRoom(room_71)
.byte 0x00

room_68:
; PS_31
; YOU_ARE_IN_THE_CHAMBER_OF_NEKHEBET,_A_WOMAN_WITH_THE_HEAD_OF_A__
; VULTURE,_WEARING_THE_CROWN_OF_EGYPT.__A_PASSAGE_EXITS_TO_THE____
; SOUTH.[CR]
;
.byte 0x03, 0x03          ; S
.byte 0x01, 0x47          ;    MoveToRoom(room_71)
.byte 0x0C, 0x03          ; OUT
.byte 0x01, 0x47          ;    MoveToRoom(room_71)
.byte 0x00

.byte 0xFF
