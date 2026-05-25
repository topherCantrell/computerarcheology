.cpu Z80

; This script is used when the room doesn't have a script for the input command.

GeneralCommandHandler:

.byte 0x01, 0x04          ; N
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x02, 0x04          ; E
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x03, 0x04          ; S
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x04, 0x04          ; W
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x05, 0x04          ; NE
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x06, 0x04          ; SE
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x07, 0x04          ; SW
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x08, 0x04          ; NW
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x09, 0x04          ; U
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x0A, 0x04          ; D
.byte 0x04                ;    Print(PS_7A:"THERE_IS_NO_WAY_FOR_YOU_TO_GO_THAT_DIRECTION.[CR]")
.word PS_7A
.byte 0x0B, 0x04          ; IN
.byte 0x04                ;    Print(PS_7B:"I_DON'T_KNOW_IN_FROM_OUT_HERE.__USE_COMPASS_POINTS.[CR]")
.word PS_7B
.byte 0x0C, 0x04          ; OUT
.byte 0x04                ;    Print(PS_7B:"I_DON'T_KNOW_IN_FROM_OUT_HERE.__USE_COMPASS_POINTS.[CR]")
.word PS_7B
.byte 0x0E, 0x04          ; LEFT
.byte 0x04                ;    Print(PS_7C:"I_AM_UNSURE_HOW_YOU_ARE_FACING.__USE_COMPASS_POINTS.[CR]")
.word PS_7C
.byte 0x0F, 0x04          ; RIGHT
.byte 0x04                ;    Print(PS_7C:"I_AM_UNSURE_HOW_YOU_ARE_FACING.__USE_COMPASS_POINTS.[CR]")
.word PS_7C
.byte 0x12, 0x04          ; PANEL
.byte 0x04                ;    Print(PS_7D:"NOTHING_HAPPENS.[CR]")
.word PS_7D
.byte 0x14, 0x02          ; BACK
.byte 0x0E                ;    MoveToLastRoom
.byte 0x16, 0x04          ; SWIM
.byte 0x04                ;    Print(PS_7E:"I_DON'T_KNOW_HOW.[CR]")
.word PS_7E
.byte 0x17, 0x18          ; ON
.byte 0x07, 0x0C          ;    StopIfPassElseContinue
.byte 0x02, 0x0E          ;        AssertObjectIsInPack(obj_LAMP_off)
.byte 0x15, 0x0E, 0x00    ;        MoveObjectToRoom(obj_LAMP_off, room_0)
.byte 0x15, 0x0F, 0xFF    ;        MoveObjectToRoom(obj_LAMP_on, room_255)
.byte 0x04                ;        Print(PS_80:"YOUR_LAMP_IS_NOW_ON.[CR]")
.word PS_80
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x02, 0x0F          ;        AssertObjectIsInPack(obj_LAMP_on)
.byte 0x04                ;        Print(PS_80:"YOUR_LAMP_IS_NOW_ON.[CR]")
.word PS_80
.byte 0x04                ;    Print(PS_81:"YOU_HAVE_NO_SOURCE_OF_LIGHT.[CR]")
.word PS_81
.byte 0x18, 0x18          ; OFF
.byte 0x07, 0x0C          ;    StopIfPassElseContinue
.byte 0x02, 0x0F          ;        AssertObjectIsInPack(obj_LAMP_on)
.byte 0x15, 0x0F, 0x00    ;        MoveObjectToRoom(obj_LAMP_on, room_0)
.byte 0x15, 0x0E, 0xFF    ;        MoveObjectToRoom(obj_LAMP_off, room_255)
.byte 0x04                ;        Print(PS_82:"YOUR_LAMP_IS_NOW_OFF.[CR]")
.word PS_82
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x02, 0x0E          ;        AssertObjectIsInPack(obj_LAMP_off)
.byte 0x04                ;        Print(PS_82:"YOUR_LAMP_IS_NOW_OFF.[CR]")
.word PS_82
.byte 0x04                ;    Print(PS_81:"YOU_HAVE_NO_SOURCE_OF_LIGHT.[CR]")
.word PS_81
.byte 0x19, 0x02          ; QUIT
.byte 0x09                ;    PrintScoreAndStop
.byte 0x1A, 0x02          ; SCORE
.byte 0x08                ;    PrintScore
.byte 0x1B, 0x02          ; INVENT
.byte 0x0F                ;    PrintInventory
.byte 0x1C, 0x02          ; LOOK
.byte 0x10                ;    PrintRoomDescription
.byte 0x1D, 0x04          ; HELP
.byte 0x04                ;    Print(PS_83:"I'M_AS_CONFUSED_AS_YOU_ARE.[CR]")
.word PS_83
.byte 0x1E, 0x04          ; FIND
.byte 0x04                ;    Print(PS_84:"I_CAN_ONLY_TELL_YOU_WHAT_YOU_SEE_AS_YOU_MOVE_ABOUT_AND__________
.word PS_84
;                                 MANIPULATE_THINGS.__I_CAN_NOT_TELL_YOU_WHERE_REMOTE_THINGS_ARE.[CR]")
.byte 0x28, 0x47          ; TAKE
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x07          ;        AssertObjectMatchesUserInput(obj_PLANT_A)
.byte 0x04                ;        Print(PS_A8:"THE_PLANT_HAS_EXCEPTIONALLY_DEEP_ROOTS_AND_CANNOT_BE_PULLED_____
.word PS_A8
;                                     FREE.[CR]")
.byte 0x07, 0x17          ;    StopIfPassElseContinue
.byte 0x11, 0x13          ;        AssertObjectMatchesUserInput(obj_BIRD)
.byte 0x07, 0x06          ;        StopIfPassElseContinue
.byte 0x02, 0x11          ;            AssertObjectIsInPack(obj_SCEPTER)
.byte 0x04                ;            Print(PS_AA:"AS_YOU_APPROACH_THE_STATUE,_IT_COMES_TO_LIFE_AND_FLIES_ACROSS___
.word PS_AA
;                                         THE_CHAMBER_WHERE_IT_LANDS_AND_RETURNS_TO_STONE.[CR]")
.byte 0x07, 0x09          ;        StopIfPassElseContinue
.byte 0x02, 0x10          ;            AssertObjectIsInPack(obj_BOX)
.byte 0x15, 0x13, 0x00    ;            MoveObjectToRoom(obj_BIRD, room_0)
.byte 0x19, 0x14, 0x10    ;            MoveObjectIntoContainer(obj_BIRD_boxed, obj_BOX)
.byte 0x04                ;        Print(PS_AB:"YOU_CAN_LIFT_THE_STATUE,_BUT_YOU_CANNOT_CARRY_IT.[CR]")
.word PS_AB
.byte 0x07, 0x0A          ;    StopIfPassElseContinue
.byte 0x11, 0x20          ;        AssertObjectMatchesUserInput(obj_VASE_pillow)
.byte 0x12, 0x21          ;        GetObjectFromRoom(obj_VASE_solo)
.byte 0x15, 0x20, 0x00    ;        MoveObjectToRoom(obj_VASE_pillow, room_0)
.byte 0x18, 0x12          ;        MoveObjectToCurrentRoom(obj_PILLOW)
.byte 0x07, 0x0D          ;    StopIfPassElseContinue
.byte 0x11, 0x1E          ;        AssertObjectMatchesUserInput(obj_STREAM_56)
.byte 0x07, 0x06          ;        StopIfPassElseContinue
.byte 0x02, 0x1C          ;            AssertObjectIsInPack(obj_WATER)
.byte 0x04                ;            Print(PS_AC:"YOUR_BOTTLE_IS_ALREADY_FULL.[CR]")
.word PS_AC
.byte 0x19, 0x1C, 0x1B    ;        MoveObjectIntoContainer(obj_WATER, obj_BOTTLE)
.byte 0x07, 0x0C          ;    StopIfPassElseContinue
.byte 0x11, 0x12          ;        AssertObjectMatchesUserInput(obj_PILLOW)
.byte 0x1A, 0x20          ;        AssertObjectIsInCurrentRoom(obj_VASE_pillow)
.byte 0x15, 0x20, 0x00    ;        MoveObjectToRoom(obj_VASE_pillow, room_0)
.byte 0x18, 0x21          ;        MoveObjectToCurrentRoom(obj_VASE_solo)
.byte 0x12, 0x12          ;        GetObjectFromRoom(obj_PILLOW)
.byte 0x16                ;    GetUserInputObject
.byte 0x21, 0x17          ; DROP
.byte 0x07, 0x14          ;    StopIfPassElseContinue
.byte 0x11, 0x21          ;        AssertObjectMatchesUserInput(obj_VASE_solo)
.byte 0x15, 0x21, 0x00    ;        MoveObjectToRoom(obj_VASE_solo, room_0)
.byte 0x07, 0x08          ;        StopIfPassElseContinue
.byte 0x1A, 0x12          ;            AssertObjectIsInCurrentRoom(obj_PILLOW)
.byte 0x18, 0x20          ;            MoveObjectToCurrentRoom(obj_VASE_pillow)
.byte 0x04                ;            Print(PS_B0:"THE_VASE_IS_NOW_RESTING,_DELICATELY,_ON_A_VELVET_PILLOW.[CR]")
.word PS_B0
.byte 0x18, 0x15          ;        MoveObjectToCurrentRoom(obj_POTTERY)
.byte 0x04                ;        Print(PS_B1:"THE_VASE_DROPS_WITH_A_DELICATE_CRASH.[CR]")
.word PS_B1
.byte 0x17                ;    DropUserInputObject
.byte 0x26, 0x0E          ; THROW
.byte 0x07, 0x0B          ;    StopIfPassElseContinue
.byte 0x11, 0x21          ;        AssertObjectMatchesUserInput(obj_VASE_solo)
.byte 0x15, 0x21, 0x00    ;        MoveObjectToRoom(obj_VASE_solo, room_0)
.byte 0x18, 0x15          ;        MoveObjectToCurrentRoom(obj_POTTERY)
.byte 0x04                ;        Print(PS_B3:"YOU_HAVE_TAKEN_THE_VASE_AND_HURLED_IT_DELICATELY_TO_THE_GROUND.[CR]")
.word PS_B3
.byte 0x17                ;    DropUserInputObject
.byte 0x29, 0x36          ; OPEN
.byte 0x07, 0x1C          ;    StopIfPassElseContinue
.byte 0x11, 0x17          ;        AssertObjectMatchesUserInput(obj_SARCOPH_full)
.byte 0x07, 0x06          ;        StopIfPassElseContinue
.byte 0x02, 0x17          ;            AssertObjectIsInPack(obj_SARCOPH_full)
.byte 0x04                ;            Print(PS_94:"I'D_ADVISE_YOU_TO_PUT_DOWN_THE_SARCOPHAGUS_BEFORE_OPENING_IT!![CR]")
.word PS_94
.byte 0x07, 0x0E          ;        StopIfPassElseContinue
.byte 0x02, 0x22          ;            AssertObjectIsInPack(obj_KEY)
.byte 0x04                ;            Print(PS_93:"A_GLISTENING_PEARL_FALLS_OUT_OF_THE_SARCOPHAGUS_AND_ROLLS_AWAY._
.word PS_93
;                                         THE_SARCOPHAGUS_SNAPS_SHUT_AGAIN.[CR]")
.byte 0x15, 0x16, 0x40    ;            MoveObjectToRoom(obj_PEARL, room_64)
.byte 0x15, 0x17, 0x00    ;            MoveObjectToRoom(obj_SARCOPH_full, room_0)
.byte 0x18, 0x18          ;            MoveObjectToCurrentRoom(obj_SARCOPH_empty)
.byte 0x04                ;        Print(PS_96:"YOU_DON'T_HAVE_ANYTHING_STRONG_ENOUGH_TO_OPEN_THE_SARCOPHAGUS.[CR]")
.word PS_96
.byte 0x07, 0x14          ;    StopIfPassElseContinue
.byte 0x11, 0x18          ;        AssertObjectMatchesUserInput(obj_SARCOPH_empty)
.byte 0x07, 0x06          ;        StopIfPassElseContinue
.byte 0x02, 0x18          ;            AssertObjectIsInPack(obj_SARCOPH_empty)
.byte 0x04                ;            Print(PS_94:"I'D_ADVISE_YOU_TO_PUT_DOWN_THE_SARCOPHAGUS_BEFORE_OPENING_IT!![CR]")
.word PS_94
.byte 0x07, 0x06          ;        StopIfPassElseContinue
.byte 0x02, 0x22          ;            AssertObjectIsInPack(obj_KEY)
.byte 0x04                ;            Print(PS_95:"THE_SARCOPHAGUS_CREAKS_OPEN,_REVEALING_NOTHING_INSIDE.__IT______
.word PS_95
;                                         PROMPTLY_SNAPS_SHUT_AGAIN.[CR]")
.byte 0x04                ;        Print(PS_96:"YOU_DON'T_HAVE_ANYTHING_STRONG_ENOUGH_TO_OPEN_THE_SARCOPHAGUS.[CR]")
.word PS_96
.byte 0x04                ;    Print(PS_97:"I_DON'T_KNOW_HOW_TO_LOCK_OR_UNLOCK_SUCH_A_THING.[CR]")
.word PS_97
.byte 0x23, 0x04          ; WAVE
.byte 0x04                ;    Print(PS_7D:"NOTHING_HAPPENS.[CR]")
.word PS_7D
.byte 0x24, 0x0E          ; POUR
.byte 0x07, 0x09          ;    StopIfPassElseContinue
.byte 0x11, 0x1C          ;        AssertObjectMatchesUserInput(obj_WATER)
.byte 0x15, 0x1C, 0x00    ;        MoveObjectToRoom(obj_WATER, room_0)
.byte 0x04                ;        Print(PS_8C:"YOUR_BOTTLE_IS_EMPTY_AND_THE_GROUND_IS_WET.[CR]")
.word PS_8C
.byte 0x04                ;    Print(PS_8D:"YOU_CAN'T_POUR_THAT.[CR]")
.word PS_8D
.byte 0x25, 0x12          ; RUB
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x0E          ;        AssertObjectMatchesUserInput(obj_LAMP_off)
.byte 0x04                ;        Print(PS_8E:"RUBBING_THE_ELECTRIC_LAMP_IS_NOT_PARTICULARLY_REWARDING.________
.word PS_8E
;                                     ANYWAY,_NOTHING_EXCITING_HAPPENS.[CR]")
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x0F          ;        AssertObjectMatchesUserInput(obj_LAMP_on)
.byte 0x04                ;        Print(PS_8E:"RUBBING_THE_ELECTRIC_LAMP_IS_NOT_PARTICULARLY_REWARDING.________
.word PS_8E
;                                     ANYWAY,_NOTHING_EXCITING_HAPPENS.[CR]")
.byte 0x04                ;    Print(PS_8F:"PECULIAR.__NOTHING_UNEXPECTED_HAPPENS.[CR]")
.word PS_8F
.byte 0x27, 0x12          ; FILL
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x1B          ;        AssertObjectMatchesUserInput(obj_BOTTLE)
.byte 0x04                ;        Print(PS_90:"THERE_IS_NOTHING_HERE_WITH_WHICH_TO_FILL_THE_BOTTLE.[CR]")
.word PS_90
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x21          ;        AssertObjectMatchesUserInput(obj_VASE_solo)
.byte 0x04                ;        Print(PS_8B:"DON'T_BE_RIDICULOUS![CR]")
.word PS_8B
.byte 0x04                ;    Print(PS_92:"YOU_CAN'T_FILL_THAT.[CR]")
.word PS_92
.byte 0x2C, 0x2D          ; ATTACK
.byte 0x07, 0x09          ;    StopIfPassElseContinue
.byte 0x11, 0x13          ;        AssertObjectMatchesUserInput(obj_BIRD)
.byte 0x15, 0x13, 0x00    ;        MoveObjectToRoom(obj_BIRD, room_0)
.byte 0x04                ;        Print(PS_98:"THE_BIRD_STATUE_IS_NOW_DEAD.__ITS_BODY_DISAPPEARS.[CR]")
.word PS_98
.byte 0x07, 0x09          ;    StopIfPassElseContinue
.byte 0x11, 0x14          ;        AssertObjectMatchesUserInput(obj_BIRD_boxed)
.byte 0x15, 0x14, 0x00    ;        MoveObjectToRoom(obj_BIRD_boxed, room_0)
.byte 0x04                ;        Print(PS_98:"THE_BIRD_STATUE_IS_NOW_DEAD.__ITS_BODY_DISAPPEARS.[CR]")
.word PS_98
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x17          ;        AssertObjectMatchesUserInput(obj_SARCOPH_full)
.byte 0x04                ;        Print(PS_99:"THE_STONE_IS_VERY_STRONG_AND_IS_IMPERVIOUS_TO_ATTACK.[CR]")
.word PS_99
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x18          ;        AssertObjectMatchesUserInput(obj_SARCOPH_empty)
.byte 0x04                ;        Print(PS_99:"THE_STONE_IS_VERY_STRONG_AND_IS_IMPERVIOUS_TO_ATTACK.[CR]")
.word PS_99
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x0B          ;        AssertObjectMatchesUserInput(obj_SERPENT)
.byte 0x04                ;        Print(PS_9A:"ATTACKING_THE_SERPENT_BOTH_DOESN'T_WORK_AND_IS_VERY_DANGEROUS.[CR]")
.word PS_9A
.byte 0x04                ;    Print(PS_9B:"YOU_CAN'T_BE_SERIOUS![CR]")
.word PS_9B
.byte 0x30, 0x04          ; BREAK
.byte 0x04                ;    Print(PS_9C:"IT_IS_BEYOND_YOUR_POWER_TO_DO_THAT.[CR]")
.word PS_9C
.byte 0x2E, 0x23          ; EAT
.byte 0x07, 0x09          ;    StopIfPassElseContinue
.byte 0x11, 0x1A          ;        AssertObjectMatchesUserInput(obj_FOOD)
.byte 0x15, 0x1A, 0x00    ;        MoveObjectToRoom(obj_FOOD, room_0)
.byte 0x04                ;        Print(PS_9D:"THANK_YOU,_IT_WAS_DELICIOUS![CR]")
.word PS_9D
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x0A          ;        AssertObjectMatchesUserInput(obj_UNUSED_10)
.byte 0x04                ;        Print(PS_9E:"I_THINK_I_JUST_LOST_MY_APPETITE.[CR]")
.word PS_9E
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x13          ;        AssertObjectMatchesUserInput(obj_BIRD)
.byte 0x04                ;        Print(PS_9E:"I_THINK_I_JUST_LOST_MY_APPETITE.[CR]")
.word PS_9E
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x14          ;        AssertObjectMatchesUserInput(obj_BIRD_boxed)
.byte 0x04                ;        Print(PS_9E:"I_THINK_I_JUST_LOST_MY_APPETITE.[CR]")
.word PS_9E
.byte 0x04                ;    Print(PS_8B:"DON'T_BE_RIDICULOUS![CR]")
.word PS_8B
.byte 0x2F, 0x15          ; DRINK
.byte 0x07, 0x09          ;    StopIfPassElseContinue
.byte 0x11, 0x1C          ;        AssertObjectMatchesUserInput(obj_WATER)
.byte 0x15, 0x1C, 0x00    ;        MoveObjectToRoom(obj_WATER, room_0)
.byte 0x04                ;        Print(PS_91:"THE_BOTTLE_IS_NOW_EMPTY.[CR]")
.word PS_91
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x1E          ;        AssertObjectMatchesUserInput(obj_STREAM_56)
.byte 0x04                ;        Print(PS_9F:"YOU_HAVE_TAKEN_A_DRINK_FROM_THE_STREAM.__THE_WATER_TASTES_______
.word PS_9F
;                                     STRONGLY_OF_MINERALS,_BUT_IS_NOT_UNPLEASANT.__IT_IS_EXTREMELY___
;                                     COLD.[CR]")
.byte 0x04                ;    Print(PS_9B:"YOU_CAN'T_BE_SERIOUS![CR]")
.word PS_9B
.byte 0x2D, 0x38          ; FEED
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x13          ;        AssertObjectMatchesUserInput(obj_BIRD)
.byte 0x04                ;        Print(PS_A0:"IT'S_NOT_HUNGRY.__BESIDES,_YOU_HAVE_NO_BIRD_SEED.[CR]")
.word PS_A0
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x14          ;        AssertObjectMatchesUserInput(obj_BIRD_boxed)
.byte 0x04                ;        Print(PS_A0:"IT'S_NOT_HUNGRY.__BESIDES,_YOU_HAVE_NO_BIRD_SEED.[CR]")
.word PS_A0
.byte 0x07, 0x10          ;    StopIfPassElseContinue
.byte 0x11, 0x0B          ;        AssertObjectMatchesUserInput(obj_SERPENT)
.byte 0x07, 0x09          ;        StopIfPassElseContinue
.byte 0x02, 0x14          ;            AssertObjectIsInPack(obj_BIRD_boxed)
.byte 0x15, 0x14, 0x00    ;            MoveObjectToRoom(obj_BIRD_boxed, room_0)
.byte 0x04                ;            Print(PS_A2:"THE_SERPENT_HAS_NOW_DEVOURED_YOUR_BIRD_STATUE.[CR]")
.word PS_A2
.byte 0x04                ;        Print(PS_A3:"THERE_IS_NOTHING_HERE_IT_WANTS_TO_EAT_-_EXCEPT_PERHAPS_YOU.[CR]")
.word PS_A3
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x17          ;        AssertObjectMatchesUserInput(obj_SARCOPH_full)
.byte 0x04                ;        Print(PS_A5:"I'M_GAME.__WOULD_YOU_CARE_TO_EXPLAIN_HOW?[CR]")
.word PS_A5
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x18          ;        AssertObjectMatchesUserInput(obj_SARCOPH_empty)
.byte 0x04                ;        Print(PS_A5:"I'M_GAME.__WOULD_YOU_CARE_TO_EXPLAIN_HOW?[CR]")
.word PS_A5
.byte 0x07, 0x06          ;    StopIfPassElseContinue
.byte 0x11, 0x0D          ;        AssertObjectMatchesUserInput(obj_UNUSED_13)
.byte 0x04                ;        Print(PS_A3:"THERE_IS_NOTHING_HERE_IT_WANTS_TO_EAT_-_EXCEPT_PERHAPS_YOU.[CR]")
.word PS_A3
.byte 0x04                ;    Print(PS_8B:"DON'T_BE_RIDICULOUS![CR]")
.word PS_8B
.byte 0x39, 0x02          ; PLUGH
.byte 0x1D                ;    RandomizeDirections
.byte 0x3A, 0x02          ; LOAD
.byte 0x1B                ;    LoadGame
.byte 0x3B, 0x02          ; SAVE
.byte 0x1C                ;    SaveGame
.byte 0x00