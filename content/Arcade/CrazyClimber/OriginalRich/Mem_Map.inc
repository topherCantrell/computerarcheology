;-----------------------------------------------------------------------------
; ($8000 - $83FF  1024 bytes)  General purpose RAM
;-----------------------------------------------------------------------------
RAM_START		.equ		$8000              ; Start of RAM (1024 bytes)
RAM_SIZE        .equ		$0400              ; Size of RAM
RAM_END_SP      .equ		RAM_START+RAM_SIZE ; Where to set the stack pointer @ end of RAM

; Sound data for channel A
SNDA_DATA_START	.equ		$8000	; Start of sound channel A data
SNDA_DATA_PTR	.equ		$8000	; Points to sound data (2 bytes)
SNDA_ADDRESS_FLG .equ		$8002	; 0 - normal sound data addressing, != 0 - Alternate addressing
SNDA_INIT_CNT	.equ		$8003	; Initial counter 1 value
SNDA_CNTR1		.equ		$8004	; Sound data counter 1
SNDA_CNTR2		.equ		$8005	; Sound data counter 2
SNDA_FA_PTR 	.equ		$8006	; Saved data pointer for $FA data code (2 bytes)
SNDA_FA_CNT		.equ		$8008	; Saved data count for $FA data code
SNDA_FC_PTR 	.equ		$8009	; Saved data pointer for $FC data code (2 bytes)
SNDA_FC_CNT		.equ		$800B	; Saved data count for $FC data code

; Sound data for channel B
SNDB_DATA_START	.equ		$800C	; Start of sound channel B data
SNDB_DATA_PTR	.equ		$800C	; Points to sound data (2 bytes)
SNDB_ADDRESS_FLG .equ		$800E	; 0 - normal sound data addressing, != 0 - Alternate addressing
SNDB_INIT_CNT	.equ		$800F	; Initial counter 1 value
SNDB_CNTR1		.equ		$8010	; Sound data counter 1
SNDB_CNTR2		.equ		$8011	; Sound data counter 2
SNDB_FA_PTR 	.equ		$8012	; Saved data pointer for $FA data code (2 bytes)
SNDB_FA_CNT		.equ		$8014	; Saved data count for $FA data code
SNDB_FC_PTR 	.equ		$8015	; Saved data pointer for $FC data code (2 bytes)
SNDB_FC_CNT		.equ		$8017	; Saved data count for $FC data code

; Sound data for channel C
SNDC_DATA_START	.equ		$8018	; Start of sound channel C data
SNDC_DATA_PTR	.equ		$8018	; Points to sound data (2 bytes)
SNDC_ADDRESS_FLG .equ		$801A	; 0 - normal sound data addressing, != 0 - Alternate addressing
SNDC_INIT_CNT	.equ		$801B	; Initial counter 1 counter
SNDC_CNTR1		.equ		$801C	; Sound data counter 1
SNDC_CNTR2		.equ		$801D	; Sound data counter 2
SNDC_FA_PTR 	.equ		$801E	; Saved data pointer for $FA data code (2 bytes)
SNDC_FA_CNT		.equ		$8020	; Saved data count for $FA data code
SNDC_FC_PTR 	.equ		$8021	; Saved data pointer for $FC data code (2 bytes)
SNDC_FC_CNT		.equ		$8023	; Saved data count for $FC data code

; Sound data for samples
SNDS_DATA_START	.equ		$8024	; Start of sound data for samples
SNDS_DATA_PTR	.equ		$8024	; Points to sound data (2 bytes)
SNDS_ADDRESS_FLG .equ		$8026	; 0 - normal sound data addressing, != 0 - Alternate addressing
SNDS_INIT_CNT	.equ		$8027	; Initial counter 1 value
SNDS_CNTR1		.equ		$8028	; Sound data counter 1
SNDS_CNTR2		.equ		$8029	; Sound data counter 2
SNDS_FA_PTR 	.equ		$802A	; Saved data pointer for $FA data code (2 bytes)
SNDS_FA_CNT		.equ		$802C	; Saved data count for $FA data code
SNDS_FC_PTR 	.equ		$802D	; Saved data pointer for $FC data code (2 bytes)
SNDS_FC_CNT		.equ		$802F	; Saved data count for $FC data code
SNDS_VOLUME		.equ		$8030	; Sample volume

 
ISR_INDEX 		.equ		$8040	; Index value for the interrupt service routine.  This value
									; is used to index into various ISR data tables

ISR_JUMP_TABLE_PTR .equ		$8042	; Points to the ISR jump table
KEEP_SAME_ISR_FLAG .equ		$8044	; 0 - Goes to next ISR table value to process, 1 - Locks the current ISR table value being processed
ISR_COUNTER		.equ		$8045	; Increments each time the ISR is called (2 bytes: $8045 - $8046)


;-----------------------------------------------------------------------------
; Interrupt service routine tables
;
; Each table has 10 locations available.  Each location represents a different
; "process" or time-sliced set of routines that are run.
;-----------------------------------------------------------------------------

;-----------------------------------------------------------------------------
; The SP_SAVE_TABLE stores the stack pointers for the time slices
; Each stack pointer location takes 2 bytes of data, for a total of 20 bytes.
; Memory range: $8049-$805C
SP_SAVE_TABLE	.equ		$8049	; Stack pointer save table 

;-----------------------------------------------------------------------------
; The ISR_FLAG_TABLE stores various flags associated with the time slice
;
; Bit	Comment
; ---	----------------------------------------------------------------------
; 4     0 - Timer is zero (ready to execute), 1 - Timer is still counting down
;
; Each location takes 1 byte.
; Memory range: $805D-$8066
ISR_FLAG_TABLE	.equ		$805D	; ISR flag table

;-----------------------------------------------------------------------------
; The ISR_TIMER_TABLE contains count-down timers that determine which
; routine needs to be run next?
; Each location takes 1 byte.
; Memory range: $8067-$8070
ISR_TIMER_TABLE	.equ		$8067	; Timer for each ISR jump routine (10 locations) ($8067 - $8070)



COIN_PRESENT	.equ		$8071	; Coin present flag (slot 1 or 2) (1 - Coin present, 0 - not present)
NUM_CREDITS		.equ		$8072	; Number of credits (1 byte)
PLAYER_DIED_FLAG .equ		$8073	; 1 if the player has died, 0 otherwise
GAME_IN_PROGRESS .equ		$8075	; Flag for game in progress (0 - No game in progress, 1 - game in progress
BONUS_LIFE		.equ		$8076	; 0 - Xtra @ 30,000, 1 - Xtra @ 50,000
COIN_SLOT		.equ		$8077	; Coin slot (0 - slot 1, 1 - slot 2)
COIN_PER_PLAY 	.equ		$8078	; Coins per play (1 - 4)
COINS_INSERTED	.equ		$8079	; # coins inserted for a play (kept track of if < # coins per play)
									; (Ex. 3 coins per play, then this would keep track of # coins entered)
PLAY_PER_COIN 	.equ		$807A	; Plays per coin (1 - 4) (4 is free play)
MACH_VER		.equ		$807C	; 0 - Table, 1 - Upright
BONUS_LIFE_SCORE .equ		$807D	; Bonus life score (3 - 30,000, 5 - 50,000)
MAX_LIVES		.equ		$807E	; Starting number of lives
NUM_PLAYERS		.equ		$8080	; Flag for number of players (0 - 1 player, 1 - 2 players)
CURRENT_PLAYER	.equ		$8081	; Current player (0 - Player 1, != 0 -Player 2)
OTHER_PLAYER_LIVES .equ		$8082	; # lives for other player
HI_SCORE_VAL1   .equ		$8083	; High score 1 (3 bytes)
HI_SCORE_VAL2   .equ		$8086	; High score 2 (3 bytes)
HI_SCORE_VAL3   .equ		$8089	; High score 3 (3 bytes)
HI_SCORE_VAL4   .equ		$808C	; High score 4 (3 bytes)
HI_SCORE_VAL5   .equ		$808F	; High score 5 (3 bytes)
;----------------------------------
; High score table data for names
; High score 1
; $8092 - Color
; $8093 - Row
; $8094 - Column
; $8095 - $809E - Name
; $809F -  Terminator ($FF)
; 
; High score 2
; $80A0 - Color
; $80A1 - Row
; $80A2 - Column
; $80A3 - $80AC - Name
; $80AD - Terminator ($FF)
;
; High score 3
; $80AE - Color
; $80AF - Row
; $80B0 - Column
; $80B1 - $80BA - Name
; $80BB - Terminator ($FF)
;
; High score 4
; $80BC - Color
; $80BD - Row
; $80BE - Column
; $80BF - $80C8 - Name
; $80C9 - Terminator ($FF)
;
; High score 5
; $80CA - Color
; $80CB - Row
; $80CC - Column
; $80CD - $80D6 - Name
; $80D7 - Terminator ($FF)
;
HS_NAME_DATA1	.equ		$8092	; Data area of name text
HS_NAME1		.equ		$8095	; Name text (10 bytes) + $FF terminator
HS_NAME_DATA2	.equ		$80A0	; Data area of name text
HS_NAME2		.equ		$80A3	; Name text (10 bytes) + $FF terminator
HS_NAME_DATA3	.equ		$80AE	; Data area of name text
HS_NAME3		.equ		$80B1	; Name text (10 bytes) + $FF terminator
HS_NAME_DATA4	.equ		$80BC	; Data area of name text
HS_NAME4		.equ		$80BF	; Name text (10 bytes) + $FF terminator
HS_NAME_DATA5	.equ		$80CA	; Data area of name text
HS_NAME5		.equ		$80CD	; Name text (10 bytes) + $FF terminator


;---------------------------------------------
; $80D8 - $80E9 are the current values
CURRENT_DATA	.equ		$80D8
CUR_NUM_LIVES	.equ		CURRENT_DATA ; Number of lives during play
CUR_SCORE		.equ		$80D9	; Current score (3 bytes -- $80D9 $80DA $80DB)
FLOOR_GROUP_IDX	.equ		$80DC	; Group of floors in the building (Range: 0 - 31)
FLOOR_IDX		.equ		$80DD	; The current floor within the current floor group
XTRA_LIFE_FLAG	.equ		$80DE	; 1 if we have received our extra life, 0 otherwise
BUILDING_NUMBER	.equ		$80DF	; Current building number (base 0). This ranges from 0 - 3.
STEP_POINT1		.equ		$80E0	; 2 bytes for BCD step point
STEP_POINT2		.equ		$80E1

DEC_BONUS_RATE1	.equ		$80E2	; 2 bytes for BCD bonus rate decrement
DEC_BONUS_RATE2	.equ		$80E3

BONUS_RATE1		.equ		$80E4	; 3 bytes for BCD bonus rate
BONUS_RATE2		.equ		$80E5
BONUS_RATE3		.equ		$80E6

CLIMBER_X_POS	.equ		$80E7	; Climber X position
CUR_FLOOR_NUM	.equ		$80E8	; Current floor number
CUR_FLOOR_GROUP	.equ		$80E9	; Current floor group
;---------------------------------------------

;---------------------------------------------
; $80EA - $80FB are the saved player 1 values
P1_DATA			.equ		$80EA
P1_NUM_LIVES	.equ		P1_DATA	; Player 1 number of lives
P1_SCORE        .equ		$80EB	; Player 1 score (3 bytes)
P1_FLOOR_NUM	.equ		$80FA	; Player 1 floor number
P1_FLOOR_GROUP	.equ		$80FB	; Player 1 floor group
;---------------------------------------------

;---------------------------------------------
; $80FC - $810D are the saved player 2 values
P2_DATA			.equ		$80FC
P2_NUM_LIVES	.equ		P2_DATA	; Player 2 number of lives
P2_SCORE        .equ		$80FD	; Player 2 score (3 bytes)
P2_FLOOR_NUM	.equ		$810C	; Player 2 floor number
P2_FLOOR_GROUP	.equ		$810D	; Player 2 floor group
;---------------------------------------------

HS_NAME_REG_DATA .equ		$810E	; High score name registration data start
									; Offset	Comment
									; 0			$810E - Color
									; 1			$810F - Row
									; 2			$8110 - Column
USER_HS_NAME		.equ	$8111	; User's entered high score name (3 bytes US, 10 bytes Japan)
									; $8111 - $811A
HS_TERMINATION		.equ	$811B	; Reserved for terminating the high score name
HS_CURSOR_POS		.equ	$811C   ; The high score cursor position
HS_NUM_CHARS		.equ	$811D	; Number of characters in the high score name
HS_CHOSEN_CHAR		.equ	$811E	; Chosen high score name character during registration
HS_TABLE_IDX		.equ	$811F	; High score table index value (0 - 4 for the 5 high scores)

ISR_JUMP3_CNTR1		.equ	$8120	; ISR_JUMP3 decrement counters
ISR_JUMP3_CNTR2		.equ	$8121	; These two are count-down timers, starting with counter 1 then continuing with counter 2

RANDOM_NUMBER		.equ	$8122	; Pseudo-random number
FLOOR_GROUP			.equ	$8130	; Floor group
FLOOR_NUM			.equ	$8131	; Floor number (within a group) This value is a mod 8 value (0, 8, 16, 24, ...)

;---------------------------------------------------------------------------------------------------
CLIMBER_SPRITE_CTRL	.equ	$8132	; Holds data for the climber sprites (Sprites controls 5 - 8)
									; There are 4 sprites that make up the climber:
									;
									; Range: $8132 - $8141
									;
CLIMBER_LLEG_CTRL	.equ	$8132	; Sprite control 5 - Left leg
									; $8132	Sprite code, inversion
									; $8133	Color / character set
									; $8134	Y position
									; $8135	X position
									;
CLIMBER_RLEG_CTRL	.equ	$8136	; Sprite control 6 - Right leg
									; $8136	Sprite code, inversion
									; $8137	Color / character set
									; $8138	Y position
									; $8139	X position
									;
CLIMBER_LARM_CTRL	.equ	$813A	; Sprite control 7 - Left arm
									; $813A	Sprite code, inversion
									; $813B	Color / character set
									; $813C	Y position
									; $813D	X position
									;
CLIMBER_RARM_CTRL	.equ	$813E	; Sprite control 8 - Right arm
									; $813E	Sprite code, inversion
									; $813F	Color / character set
									; $8140	Y position
									; $8141	X position
;---------------------------------------------------------------------------------------------------

; Flags for user input
RINPUT_X_FLAG	 	.equ	$8142	; Right stick X input (1 = left, -1 = right, 0 = no input)
RINPUT_Y_FLAG		.equ	$8143	; Right stick Y input (1 = up, -1 = down, 0 = no input)
LINPUT_X_FLAG		.equ	$8144	; Left stick X input (1 = left, -1 = right, 0 = no input)
LINPUT_Y_FLAG		.equ	$8145	; Left stick Y input (1 = up, -1 = down, 0 = no input)

LHAND_MOVEMENT_FLAG	.equ	$8146	; 0 - No movement allowed, 1 - movement allowed
RHAND_MOVEMENT_FLAG	.equ	$8147	; 0 - No movement allowed, 1 - movement allowed

R_CLIMBER_ANIM_IDX1	.equ	$8148	; Right-side climber animation sequence index 1 (0 - arm fully down, 1, 2, 3, 4 - arm fully up)
R_CLIMBER_ANIM_IDX2	.equ	$8149	; Right-side climber animation sequence index 2 (0 - arm out, 1 - arm in)
L_CLIMBER_ANIM_IDX1	.equ	$814A	; Left-side climber animation sequence index 1 (0 - arm fully down, 1, 2, 3, 4 - arm fully up)
L_CLIMBER_ANIM_IDX2	.equ	$814B	; Left-side climber animation sequence index 2 (0 - arm in, 1 - arm out)


BLDG_GROUP_IDX		.equ	$814F	; Building group index value (index into the building floor group pointer list)
BLDG_CHAR_TBL_IDX	.equ	$8151	; Index into building floor character table

CUR_PLAYER_INPUT	.equ	$8154	; Current player input (player 1 or player 2 or scripted input for attract mode)
SCRIPTED_INPUT_IDX	.equ	$8155	; Scripted input index for attract mode
ISR_MODE_IDX		.equ	$815B	; ISR mode (start a building (01), ???)

UNKNOWN_815C		.equ	$815C	; Four 8-byte items, unknown usage right now
									; Item[0] $815C - $8163
									; Item[1] $8164 - $816B
									; Item[2] $816C - $8173
									; Item[3] $8174 - $817B
									; Byte 0 - ???
									; Byte 1-4 - Copies over to SPRITE_CTRL
									; Bytes 5-7 - ???

PLAYFIELD			.equ	$8181	; 8 values wide by 16 values deep = 128 bytes ($8181 - $8200)
									; This represents the playfield (where the player can go, etc)
									; 00 - Open window
									; 01 - 04  Window closing
									; 05 - 0B  Window closed
									; 0C - 0F  Window opening
									; 80       Unknown
									; FF       Cannot move there (no window or guy in window)

UNK_TABLE_8201		.equ	$8201	; Unknown table (indexed by threes)

UNKNOWN_8283		.equ	$8283	; Size: 32 bytes ($8283 - $82A2)


COPTER_STATE		.equ	$82A5	; State of helicopter (0 - not active, 1 active, 2 animate and move helicopter down, 3 animate and move helicopter up)
									; When the helicopter is being moved (state >= 2), bit 0 is used to tell if the helicopter is moving up or down.
									; If bit 0 is 1, the helicopter is moving up. If bit 0 is 0, the helicopter is moving down
COPTER_BLADE1_INDEX	.equ	$82A6	; Index for helicopter top blade graphics (used for movement)
COPTER_BLADE2_INDEX	.equ	$82A7	; Index for helicopter tail blade graphics (used for movement)
COPTER_BLADE1_TIMING .equ	$82A8	; Counter used for helicopter top blade movement timing
COPTER_BLADE2_TIMING .equ	$82A9	; Counter used for helicopter tail blade movement timing
BIGSPRITE_DIRECTION	.equ	$82AE	; Bit 0 = 1 if moving left, 0 if moving right
GP_82AF				.equ	$82AF	; General purpose counter / flag
GP_TIMING			.equ	$82B0	; Used for animating the bird, electric sign, falling sign (and others?)
GP_82B1				.equ	$82B1	; General purpose index / flag / counter
REG_TIME_SEC_VAL	.equ	$82B2	; Name registration time left (seconds)
REG_TIME_TENTHS_VAL	.equ	$82B3	; Name registration time left (tenths)
CURRENT_FIELD_FLAG	.equ	$82B4	; 0 - Inverted, 1 - Normal
HELO_BALLOON_TIMER	.equ	$82B5	; 82B5 and 82B6 - 2 bytes that hold a countdown timer for how long the helicopter / baloon  stays

ISR_JUMP3_CNTR3		.equ	$82BA	; ISR_JUMP3 count up counter. Starts with the building number and increases. Is this used for window speed?


; Window update FIFO
; ($82BB - $82DA)
; This FIFO contains row, column combinations that are used for
; updating the window locations.
;
; This FIFO is organized as a 16 deep x 2 byte memory space.
; Data is read out of the top (2 bytes read at $82BB), then all data values are
; shifted up two memory locations.  New data is written into the bottom (2 bytes
; written at $82D9).
; $82BB - Top of FIFO (row/column data read from here)
; $82D9 - Bottom of FIFO (row/column data written into here)
;
WINDOW_ROW_COL_FIFO	.equ	$82BB	; Top of FIFO


UNK_82DB			.equ	$82DB	; 1 byte
ISR_JUMP3_ACTION	.equ	$82DC	; ISR_JUMP3 building action pointer


;-----------------------------------------------------------------------------
; ($8800 - $88FF  256 bytes)  Big sprite RAM
;
; This is arranged as a 16 byte x 16 byte block, used for the entire
; big sprite.
;-----------------------------------------------------------------------------
BIG_SPRITE_RAM		.equ	$8800		; Start of big sprite RAM (256 bytes)
BIG_SPRITE_RAM_SIZE .equ	$100		; Size of big sprite RAM




;-----------------------------------------------------------------------------
; ($9000 - $93FF  1024 bytes)  Screen RAM
;-----------------------------------------------------------------------------
SCREEN_RAM		.equ		$9000			; Screen RAM
SCREEN_RAM_SIZE	.equ		$0400			; Size of screen RAM

;-----------------------------------------------------------------------------
; ($9400 - $97FF  1024 bytes)  Mirrored Screen RAM (i.e. 9400 is the same as 9000)
;-----------------------------------------------------------------------------
SCREEN_RAM_MIRROR      .equ	$9400			; Mirrored Screen RAM
SCREEN_RAM_MIRROR_SIZE .equ	$0400			; Size of mirrored screen RAM

;-----------------------------------------------------------------------------
; ($9800 - $981F  32 bytes)  Column smooth scrolling 
;
; Each value corresponds to a column
;-----------------------------------------------------------------------------
COLUMN_SCROLL	.equ		$9800			; Column smooth scrolling


;-----------------------------------------------------------------------------
; ($9880 - $989F  32 bytes)  Sprite control
;
; 8 groups of 4 bytes
;
; 1st byte; code/attribute.
;		Bits 0-5: sprite code.
;		Bit    6: x invert.
;		Bit    7: y invert.
;
; 2nd byte ;color.
;		Bits 0-3: colour. (palette scheme 0-15)
;		Bit    4: 0=charset1, 1 =charset 2.
;
; 3rd byte ;y position
;
; 4th byte ;x position
;-----------------------------------------------------------------------------
SPRITE_CTRL		.equ		$9880			; Sprite control

;-----------------------------------------------------------------------------
; ($98DC - $98DF  4 bytes)  Big Sprite control
;
; 1st byte; sprite number? Priority?
;
; 2nd byte ;color / attributes
;		Bits 0-2: colour.
;       Bit    3: ?
;		Bit    4: x invert
;		Bit    5: y invert
;
; 3rd byte ;y position
;
; 4th byte ;x position
;-----------------------------------------------------------------------------
BIG_SPRITE_CTRL	.equ		$98DC			; Big Sprite control start


;-----------------------------------------------------------------------------
; ($9C00 - $9FFF  1024 bytes)  Color RAM
;
; Each byte is used to color / select the character located at the
; corresponding screen ram location.  Each byte works as follows:
;
; Bits 7-5: Not used
; Bit 4: 0 = character set 1, 1 = character set 2
; Bits 3-0: color (palette scheme 0-15)
;-----------------------------------------------------------------------------
COLOR_RAM		.equ		$9C00			; Color RAM
COLOR_RAM_SIZE	.equ		$0400			; Size of color RAM



;-----------------------------------------------------------------------------
; Write memory space
;-----------------------------------------------------------------------------
NMI_MASK_WR:	.equ				$A000		; Write 0 - mask, Write 1 - unmask NMI interrupts
HINV_WR:		.equ				$A001		; 0 - Normal, 1 - Invert
VINV_WR:		.equ				$A002		; 0 - Normal, 1 - Invert
SMPL_TRIG_WR:	.equ				$A004		; 0 - Sample trigger
SOUND_CS_WR:	.equ				$A007		; 0 - Enable sound chip, 1 - Disable sound chip
SMPL_RATE_WR:	.equ				$A800		; Write for sample rate of sound chip
SMPL_VOL_WR:	.equ				$B000		; Write for sample volume

;-----------------------------------------------------------------------------
; Read memory space
;-----------------------------------------------------------------------------
PL1_CONT_RD:	.equ				$A000		; Read for player 1 controls
								;	Bit
								;   0: Left up
								;	1: Left down
								;	2: Left left
								;	3: Left right
								;	4: Right up
								;	5: Right down
								;	6: Right left
								;	7: Right right

PL2_CONT_RD:	.equ				$A800		; Read for player 2 controls
								;	Bit
								;   0: Left up
								;	1: Left down
								;	2: Left left
								;	3: Left right
								;	4: Right up
								;	5: Right down
								;	6: Right left
								;	7: Right right

DIP_SW_RD:		.equ				$B000		; Read for DIP switches
								;	Bit 1,0: Number of climbers.
								;		00=3, 01=4, 10=5, 11=6.
								;	Bit   2: Extra climber bonus.
								;		0=30000, 1=50000.
								;	Bit   3: 1=Test Pattern
								;	Bit 5,4: Coins per credit.
								;		00=1, 01=2, 10=3 11=4.
								;	Bit 7,6: Plays per credit.
								;		00=1, 01=2, 10=3, 11=Freeplay.

MACH_SW_RD:		.equ				$B800		; Read for machine switches (also pets the watchdog)
								;  	Bit 0: Coin 1.
								;	Bit 1: Coin 2.
								;	Bit 2: 1 Player start.
								;	Bit 3: 2 Player start.
								;	Bit 4: Upright/table select.
								;		0=table, 1=upright.


;-----------------------------------------------------------------------------
; I/O Memory Space
;-----------------------------------------------------------------------------
; Output
IO_SOUND_CTRL	.equ			$08			; AY-3-8910 Sound Control
IO_SND_W		.equ			$09			; AY-3-8910 Sound Data Write

; Input
IO_SND_R		.equ			$0C			; AY-3-8910 Sound Data Read
