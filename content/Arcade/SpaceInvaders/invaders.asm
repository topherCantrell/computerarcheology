; This ASMX assembly file was created by:
; David Levy
; https://github.com/valleyco/invaders
	
	CPU	8080
	ORG	0
	; Execution begins here on power-up and reset.
Reset:
	NOP							; This provides a slot ...
	NOP							; ... to put in a JP for ...
	NOP							; ... development
	JMP	init					; {code.init} Continue startup at 18D4
D_0006:
	DB	0x00, 0x00				; Padding before fixed ISR address
	;Interrupt brings us here when the beam is *near* the middle of the screen. The real middle
	;would be 224/2 = 112. The code pretends this interrupt happens at line 128.
ScanLine96:
	PUSH	PSW					; Save ...
	PUSH	B					; ...
	PUSH	D					; ...
	PUSH	H					; ... everything
	JMP	L_008C					; {} Continue ISR at 8C
D_000F:
	DB	0x00					; Padding before fixed ISR address
	; Interrupt brings us here when the beam is at the end of the screen (line 224) when the VBLANK begins.
ScanLine224:
	PUSH	PSW					; Save ...
	PUSH	B					; ...
	PUSH	D					; ...
	PUSH	H					; ... everything
	MVI	A,0x80					; Flag that tells objects ...
	STA	0x2072					; {ram.vblankStatus} ... on the lower half of the screen to draw/move
	LXI	H,0x20C0				; {+ram.isrDelay} Decrement ...
	DCR	M						; ... the general countdown (used for pauses)
	CALL	CheckHandleTilt		; {code.CheckHandleTilt} Check and handle TILT
L_0020:
	IN	0x01					; {hard.INP1} Read coin switch
	RRC							; Has a coin been deposited (bit 0)?
	JC	L_0067					; {} Yes ... note that switch is closed and continue at 3F with A=1
	LDA	0x20EA					; {ram.coinSwitch} Switch is now open. Was it ...
	ANA	A						; ... closed last time?
	JZ	L_0042					; {} No ... skip registering the credit
	;
	; Handle bumping credit count
	LDA	0x20EB					; {ram.numCoins} Number of credits in BCD
L_0030:
	CPI	0x99					; 99 credits already?
	JZ	L_003E					; {} Yes ... ignore this (better than rolling over to 00)
	ADI	0x01					; Bump number of credits
	DAA							; Make it binary coded decimal
L_0038:
	STA	0x20EB					; {ram.numCoins} New number of credits
	CALL	DrawNumCredits		; {code.DrawNumCredits} Draw credits on screen
L_003E:
	XRA	A						; Credit switch ...
L_003F:
	STA	0x20EA					; {ram.coinSwitch} ... has opened
	;
L_0042:
	LDA	0x20E9					; {ram.suspendPlay} Are we moving ...
	ANA	A						; ... game objects?
	JZ	L_0082					; {} No ... restore registers and out
	LDA	0x20EF					; {ram.gameMode} Are we in ...
	ANA	A						; ... game mode?
	JNZ	L_006F					; {} Yes ... go process game-play things and out
	LDA	0x20EB					; {ram.numCoins} Number of credits
	ANA	A						; Are there any credits (player standing there)?
	JNZ	L_005D					; {} Yes ... skip any ISR animations for the splash screens
	CALL	ISRSplTasks			; {code.ISRSplTasks} Process ISR tasks for splash screens
	JMP	L_0082					; {} Restore registers and out
	;
	; At this point no game is going and there are credits
L_005D:
	LDA	0x2093					; {ram.waitStartLoop} Are we in the ...
	ANA	A						; ... "press start" loop?
	JNZ	L_0082					; {} Yes ... restore registers and out
	JMP	WaitForStart			; {code.WaitForStart} Start the "press start" loop
	;
	; Mark credit as needing registering
L_0067:
	MVI	A,0x01					; Remember switch ...
	STA	0x20EA					; {ram.coinSwitch} ... state for debounce
	JMP	L_003F					; {} Continue
	;
	; Main game-play timing loop
L_006F:
	CALL	TimeFleetSound		; {code.TimeFleetSound} Time down fleet sound and sets flag if needs new delay value
L_0072:
	LDA	0x2032					; {ram.obj2TimerExtra} Use rolling shot's timer to sync ...
	STA	0x2080					; {ram.shotSync} ... other two shots
	CALL	DrawAlien			; {code.DrawAlien} Draw the current alien (or exploding alien)
	CALL	RunGameObjs			; {code.RunGameObjs} Process game objects (including player object)
	CALL	TimeToSaucer		; {code.TimeToSaucer} Count down time to saucer
	NOP							; ** Why are we waiting?
	;
L_0082:
	POP	H						; Restore ...
	POP	D						; ...
	POP	B						; ...
	POP	PSW						; ... everything
	EI							; Enable interrupts
	RET							; Return from interrupt
D_0088:
	DB	0x00, 0x00, 0x00, 0x00	; ** Why waste the space?
	; Continues here at scanline 96
	;
L_008C:
	XRA	A						; Flag that tells ...
	STA	0x2072					; {ram.vblankStatus} ... objects on the upper half of screen to draw/move
	LDA	0x20E9					; {ram.suspendPlay} Are we moving ...
	ANA	A						; ... game objects?
	JZ	L_0082					; {} No ... restore and return
	LDA	0x20EF					; {ram.gameMode} Are we in ...
	ANA	A						; ... game mode?
	JNZ	L_00A5					; {} Yes .... process game objects and out
	LDA	0x20C1					; {ram.isrSplashTask} Splash-animation tasks
	RRC							; If we are in demo-mode then we'll process the tasks anyway
	JNC	L_0082					; {} Not in demo mode ... done
	;
L_00A5:
	LXI	H,0x2020				; Game object table (skip player-object at 2010)
	CALL	L_024B				; {} Process all game objects (except player object)
	CALL	CursorNextAlien		; {code.CursorNextAlien} Advance cursor to next alien (move the alien if it is last one)
	JMP	L_0082					; {} Restore and return
	; The Aliens
	; Initialize the player's rack of aliens. Copy the reference-location and deltas from the
	; player's data bank.
	;
InitRack:
	CALL	GetAlRefPtr			; {code.GetAlRefPtr} 2xFC Get current player's ref-alien position pointer
	PUSH	H					; Hold pointer
	MOV	A,M						; Get player's ...
	INX	H						; ... ref-alien ...
	MOV	H,M						; ...
	MOV	L,A						; ... coordinates
	SHLD	0x2009				; {ram.refAlienYr} Set game's reference alien's X,Y
	SHLD	0x200B				; {ram.alienPosLSB} Set game's alien cursor bit position
	POP	H						; Restore pointer
	DCX	H						; 21FB or 22FB ref alien's delta (left or right)
	MOV	A,M						; Get ref alien's delta X
	CPI	0x03					; If there is one alien it will move right at 3
	JNZ	L_00C8					; {} Not 3 ... keep it
	DCR	A						; If it is 3, back it down to 2 until it switches again
L_00C8:
	STA	0x2008					; {ram.refAlienDXr} Store alien deltaY
	CPI	0xFE					; Moving left?
	MVI	A,0x00					; Value of 0 for rack-moving-right (not XOR so flags are unaffected)
	JNZ	L_00D3					; {} Not FE ... keep the value 0 for right
	INR	A						; It IS FE ... use 1 for left
L_00D3:
	STA	0x200D					; {ram.rackDirection} Store rack direction
	RET							; Done
L_00D7:
	MVI	A,0x02					; Set ...
	STA	0x21FB					; {ram.p1RefAlienDX} ... player 1 and 2 ...
	STA	0x22FB					; {ram.p2RefAlienDX} ... alien delta to 2 (right 2 pixels)
	JMP	L_08E4					; {}
D_00E2:
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	;
	; This is heavily patched from a previous version of the code. There was a test here to jump to a
	; self-test routine on startup (based on a dip switch). Even the original code padded with zeros
	; to make the next function begin at 0100. Room for expansion?
	; 2006 holds the index into the alien flag data grid. 2067 holds the MSB of the pointer (21xx or 22xx).
	; If there is an alien exploding time it down. Otherwise draw the alien if it alive (or skip if
	; it isn't). If an alien is drawn (or blank) then the 2000 alien-drawing flag is cleared.
	;
DrawAlien:
	LXI	H,0x2002				; Is there an ...
	MOV	A,M						; ... alien ...
	ANA	A						; ... exploding?
	JNZ	AExplodeTime			; {code.AExplodeTime} Yes ... go time it down and out
	;
	PUSH	H					; 2002 on the stack
	LDA	0x2006					; {ram.alienCurIndex} Get alien index ...
	MOV	L,A						; ... for the 21xx or 22xx pointer
	LDA	0x2067					; {ram.playerDataMSB} Get MSB ...
	MOV	H,A						; ... of data area (21xx or 22xx)
	MOV	A,M						; Get alien status flag
	ANA	A						; Is the alien alive?
	POP	H						; HL=2002
	JZ	L_0136					; {} No alien ... skip drawing alien sprite (but flag done)
	INX	H						; HL=2003 Bump descriptor
	INX	H						; HL=2004 Point to alien's row
	MOV	A,M						; Get alien type
	INX	H						; HL=2005 Bump descriptor
	MOV	B,M						; Get animation number
	ANI	0xFE					; Translate row to type offset as follows: ...
	RLC							; ... 0,1 -> 32 (type 1) ...
	RLC							; ... 2,3 -> 16 (type 2) ...
	RLC							; ...   4 -> 32 (type 3) on top row
	MOV	E,A						; Sprite offset LSB
	MVI	D,0x00					; MSB is 0
	LXI	H,AlienSprA				; Position 0 alien sprites
	DAD	D						; Offset to sprite type
	XCHG						; Sprite offset to DE
	MOV	A,B						; Animation frame number
	ANA	A						; Is it position 0?
	CNZ	L_013B					; {} No ... add 30 and use position 1 alien sprites
	LHLD	0x200B				; {ram.alienPosLSB} Pixel position
	MVI	B,0x10					; 16 rows in alien sprites
	CALL	DrawSprite			; {code.DrawSprite} Draw shifted sprite
	;
L_0136:
	XRA	A						; Let the ISR routine ...
	STA	0x2000					; {ram.waitOnDraw} ... advance the cursor to the next alien
	RET							; Out
	;
L_013B:
	LXI	H,L_0030				; Offset sprite pointer ...
	DAD	D						; ... to animation frame 1 sprites
	XCHG						; Back to DE
	RET							; Out
	; This is called from the mid-screen ISR to set the cursor for the next alien to draw.
	; When the cursor moves over all aliens then it is reset to the beginning and the reference
	; alien is moved to its next position.
	;
	; The flag at 2000 keeps this in sync with the alien-draw routine called from the end-screen ISR.
	; When the cursor is moved here then the flag at 2000 is set to 1. This routine will not change
	; the cursor until the alien-draw routine at 100 clears the flag. Thus no alien is skipped.
	;
CursorNextAlien:
	LDA	0x2068					; {ram.playerOK} Is the player ...
	ANA	A						; ... blowing up?
	RZ							; Yes ... ignore the aliens
	LDA	0x2000					; {ram.waitOnDraw} Still waiting on ...
	ANA	A						; ... this alien to be drawn?
	RNZ							; Yes ... leave cursor in place
	LDA	0x2067					; {ram.playerDataMSB} Load alien-data ...
	MOV	H,A						; ... MSB (either 21xx or 22xx)
	LDA	0x2006					; {ram.alienCurIndex} Load the xx part of the alien flag pointer
	MVI	D,0x02					; When all are gone this triggers 1A1 to return from this stack frame
L_0154:
	INR	A						; Have we drawn all aliens ...
	CPI	0x37					; ... at last position?
	CZ	MoveRefAlien			; {code.MoveRefAlien} Yes ... move the bottom/right alien and reset index to 0
	MOV	L,A						; HL now points to alien flag
	MOV	B,M						; Is alien ...
	DCR	B						; ... alive?
	JNZ	L_0154					; {} No ... skip to next alien
	STA	0x2006					; {ram.alienCurIndex} New alien index
	CALL	GetAlienCoords		; {code.GetAlienCoords} Calculate bit position and type for index
	MOV	H,C						; The calculation returns the MSB in C
	SHLD	0x200B				; {ram.alienPosLSB} Store new bit position
	MOV	A,L						; Has this alien ...
	CPI	0x28					; ... reached the end of screen?
	JC	L_1971					; {} Yes ... kill the player
	MOV	A,D						; This alien's ...
	STA	0x2004					; {ram.alienRow} ... row index
	MVI	A,0x01					; Set the wait-flag for the ...
	STA	0x2000					; {ram.waitOnDraw} ... draw-alien routine to clear
	RET							; Done
	; Convert alien index in L to screen bit position in C,L.
	; Return alien row index (converts to type) in D.
	;
GetAlienCoords:
	MVI	D,0x00					; Row 0
	MOV	A,L						; Hold onto alien index
	LXI	H,0x2009				; Get alien X ...
	MOV	B,M						; ... to B
	INX	H						; Get alien y ...
	MOV	C,M						; ... to C
L_0183:
	CPI	0x0B					; Can we take a full row off of index?
	JM	L_0194					; {} No ... we have the row
	SBI	0x0B					; Subtract off 11 (one whole row)
	MOV	E,A						; Hold the new index
	MOV	A,B						; Add ...
	ADI	0x10					; ... 16 to bit ...
	MOV	B,A						; ... position Y (1 row in rack)
	MOV	A,E						; Restore tallied index
	INR	D						; Next row
	JMP	L_0183					; {} Keep skipping whole rows
	;
L_0194:
	MOV	L,B						; We have the LSB (the row)
L_0195:
	ANA	A						; Are we in the right column?
	RZ							; Yes ... X and Y are right
	MOV	E,A						; Hold index
	MOV	A,C						; Add ...
	ADI	0x10					; ... 16 to bit ...
	MOV	C,A						; ... position X (1 column in rack)
	MOV	A,E						; Restore index
	DCR	A						; We adjusted for 1 column
	JMP	L_0195					; {} Keep moving over column
	; The "reference alien" is the bottom left. All other aliens are drawn relative to this
	; reference. This routine moves the reference alien (the delta is set elsewhere) and toggles
	; the animation frame number between 0 and 1.
	;
MoveRefAlien:
	DCR	D						; This decrements with each call to move
	JZ	ReturnTwo				; {code.ReturnTwo} Return out of TWO call frames (only used if no aliens left)
	LXI	H,0x2006				; Set current alien ...
	MVI	M,0x00					; ... index to 0
	INX	H						; Point to DeltaX
	MOV	C,M						; Load DX into C
	MVI	M,0x00					; Set DX to 0
	CALL	AddDelta			; {code.AddDelta} Move alien
	LXI	H,0x2005				; Alien animation frame number
	MOV	A,M						; Toggle ...
	INR	A						; ... animation ...
	ANI	0x01					; ... number between ...
	MOV	M,A						; ... 0 and 1
	XRA	A						; Alien index in A is now 0
	LXI	H,0x2067				; Restore H ...
	MOV	H,M						; ... to player data MSB (21 or 22)
	RET							; Done
D_01BF:
	DB	0x00					; ** Why?
	; Initialize the 55 aliens from last to 1st. 1 means alive.
	;
InitAliens:
	LXI	H,0x2100				; Start of alien structures (this is the last alien)
L_01C3:
	MVI	B,0x37					; Count to 55 (that's five rows of 11 aliens)
L_01C5:
	MVI	M,0x01					; Bring alien to live
	INX	H						; Next alien
	DCR	B						; All done?
	JNZ	L_01C5					; {} No ... keep looping
	RET							; Done
	; If there are no aliens left on the screen then MoveDrawAlien comes here which returns from the
	; caller's stack frame.
	;
ReturnTwo:
	POP	H						; Drop return to caller
	RET							; Return to caller's caller
	; Misc
	; Draw a 1px line across the player's stash at the bottom of the screen.
	;
DrawBottomLine:
	MVI	A,0x01					; Bit 1 set ... going to draw a 1-pixel stripe down left side
	MVI	B,0xE0					; All the way down the screen
	LXI	H,0x2402				; Screen coordinates (3rd byte from upper left)
	JMP	L_14CC					; {} Draw line down left side
	; HL points to descriptor: DX DY XX YY except DX is already loaded in C
	; ** Why the "already loaded" part? Why not just load it here?
	;
AddDelta:
	INX	H						; We loaded delta-x already ... skip over it
	MOV	B,M						; Get delta-y
	INX	H						; Skip over it
	MOV	A,C						; Add delta-x ...
	ADD	M						; ... to x
	MOV	M,A						; Store new x
	INX	H						; Skip to y
	MOV	A,B						; Add delta-y ...
	ADD	M						; ... to y
	MOV	M,A						; Store new y
	RET							; Done
	; Block copy ROM mirror 1B00-1BBF to initialize RAM at 2000-20BF.
	;
CopyRAMMirror:
	MVI	B,0xC0					; Number of bytes
L_01E6:
	LXI	D,0x1B00				; RAM mirror in ROM
	LXI	H,0x2000				; Start of RAM
	JMP	BlockCopy				; {code.BlockCopy} Copy [DE]->[HL] and return
	; Copy/Restore Shields
	; Draw the shields for player 1 (draws it in the buffer in the player's data area).
	;
DrawShieldPl1:
	LXI	H,0x2142				; Player 1 shield buffer (remember between games in multi-player)
	JMP	L_01F8					; {} Common draw point
	;
	; Draw the shields for player 1 (draws it in the buffer in the player's data area).
	;
DrawShieldPl2:
	LXI	H,0x2242				; Player 2 shield buffer (remember between games in multi-player)
	;
L_01F8:
	MVI	C,0x04					; Going to draw 4 shields
	LXI	D,ShieldImage			; Shield pixel pattern
L_01FD:
	PUSH	D					; Hold the start for the next shield
	MVI	B,0x2C					; 44 bytes to copy
	CALL	BlockCopy			; {code.BlockCopy} Block copy DE to HL (B bytes)
	POP	D						; Restore start of shield pattern
	DCR	C						; Drawn all shields?
	JNZ	L_01FD					; {} No ... go draw them all
	RET							; Done
	; Copy shields on the screen to player 1's data area.
	;
RememberShields1:
	MVI	A,0x01					; Not zero means remember
	JMP	L_021B					; {} Shuffle-shields player 1
	; Copy shields on the screen to player 2's data area.
	;
RememberShields2:
	MVI	A,0x01					; Not zero means remember
	JMP	L_0214					; {} Shuffle-shields player 2
	; Copy shields from player 2's data area to screen.
	;
RestoreShields2:
	XRA	A						; Zero means restore
L_0214:
	LXI	D,0x2242				; Player 2 shield buffer (remember between games in multi-player)
	JMP	CopyShields				; {code.CopyShields} Shuffle-shields player 2
	; Copy shields from player 1's data area to screen.
	;
RestoreShields1:
	XRA	A						; Zero means restore
L_021B:
	LXI	D,0x2142				; Player 1 shield buffer (remember between games in multi-player)
	; A is 1 for screen-to-buffer, 0 for to buffer-to-screen
	; HL is screen coordinates of first shield. There are 23 rows between shields.
	; DE is sprite buffer in memory.
	;
CopyShields:
	STA	0x2081					; {ram.tmp2081} Remember copy/restore flag
	LXI	B,0x1602				; 22 rows, 2 bytes/row (for 1 shield pattern)
	LXI	H,0x2806				; Screen coordinates
	MVI	A,0x04					; Four shields to move
L_0229:
	PUSH	PSW					; Hold shield count
	PUSH	B					; Hold sprite-size
	LDA	0x2081					; {ram.tmp2081} Get back copy/restore flag
	ANA	A						; Not zero ...
	JNZ	L_0242					; {} ... means remember shidles
	CALL	RestoreShields		; {code.RestoreShields} Restore player's shields
L_0235:
	POP	B						; Get back sprite-size
	POP	PSW						; Get back shield count
	DCR	A						; Have we moved all shields?
	RZ							; Yes ... out
	PUSH	D					; Hold sprite buffer
	LXI	D,0x02E0				; Add 2E0 (23 rows) to get to ...
	DAD	D						; ... next shield on screen
	POP	D						; restore sprite buffer
	JMP	L_0229					; {} Go back and do all
	;
L_0242:
	CALL	RememberShields		; {code.RememberShields} Remember player's shields
	JMP	L_0235					; {} Continue with next shield
	; Game Objects
	; Process game objects. Each game object has a 16 byte structure. The handler routine for the object
	; is at xx03 and xx04 of the structure. The pointer to xx04 is pushed onto the stack before calling
	; the handler.
	;
	; All game objects (except task 0 ... the player) are called at the mid-screen and end-screen renderings.
	; Each object decides when to run based on its Y (not rotated) coordinate. If an object is on the lower
	; half of the screen then it does its work when the beam is at the top of the screen. If an object is
	; on the top of the screen then it does its work when the beam is at the bottom. This keeps the
	; object from updating while it is being drawn which would result in an ugly flicker.
	;
	;
	; The player is only processed at the mid-screen interrupt. I am not sure why.
	;
	; The first three bytes of the structure are used for status and timers.
	;
	; If the first byte is FF then the end of the game-task list has been reached.
	; If the first byte is FE then the object is skipped.
	;
	; If the first-two bytes are non-zero then they are treated like a two-byte counter
	; and decremented as such. The 2nd byte is the LSB (moves the fastest).
	;
	; If the first-two bytes are zero then the third byte is treated as an additional counter. It
	; is decremented as such.
	;
	; When all three bytes reach zero the task is executed.
	;
	; The third-byte-counter was used as a speed-governor for the player's object, but evidently even the slowest
	; setting was too slow. It got changed to 0 (fastest possible).
	;
RunGameObjs:
	LXI	H,0x2010				; First game object (active player)
L_024B:
	MOV	A,M						; Have we reached the ...
	CPI	0xFF					; ... end of the object list?
	RZ							; Yes ... done
	CPI	0xFE					; Is object active?
	JZ	L_0281					; {} No ... skip it
	INX	H						; xx01
	MOV	B,M						; First byte to B
	MOV	C,A						; Hold 1st byte
	ORA	B						; OR 1st and 2nd byte
	MOV	A,C						; Restore 1st byte
	JNZ	L_0277					; {} If word at xx00,xx02 is non zero then decrement it
	;
	INX	H						; xx02
	MOV	A,M						; Get byte counter
	ANA	A						; Is it 0?
	JNZ	L_0288					; {} No ... decrement byte counter at xx02
	INX	H						; xx03
	MOV	E,M						; Get handler address LSB
	INX	H						; xx04
	MOV	D,M						; Get handler address MSB
	PUSH	H					; Remember pointer to MSB
	XCHG						; Handler address to HL
	PUSH	H					; Now to stack (making room for indirect call)
	LXI	H,D_026F				; Return address to 026F
	XTHL						; Return address (026F) now on stack. Handler in HL.
	PUSH	D					; Push pointer to data struct (xx04) for handler to use
	PCHL						; Run object's code (will return to next line)
D_026F:
	DB	0xE1, 0x11, 0x0C, 0x00, 0x19, 0xC3, 0x4B, 0x02	; Restore pointer to xx04
	;
	; Word at xx00 and xx01 is non-zero. Decrement it and move to next task.
L_0277:
	DCR	B						; Decrement ...
	INR	B						; ... two ...
	JNZ	L_027D					; {} ... byte ...
	DCR	A						; ... value ...
L_027D:
	DCR	B						; ... at ...
	MOV	M,B						; ... xx00 ...
	DCX	H						; ... and ...
	MOV	M,A						; ... xx01
	;
L_0281:
	LXI	D,ScanLine224			; Next ...
	DAD	D						; ... object descriptor
	JMP	L_024B					; {} Keep processing game objects
	;
	; Word at xx00 and xx01 is zero and byte at xx02 is non-zero. Decrement xx02 and
	; move to next task.
L_0288:
	DCR	M						; Decrement the xx02 counter
	DCX	H						; Back up to ...
	DCX	H						; ... start of game task
	JMP	L_0281					; {} Next game task
	; Game object 0: Move/draw the player
	;
	; This task is only called at the mid-screen ISR. It ALWAYS does its work here, even though
	; the player can be on the top or bottom of the screen (not rotated).
	;
GameObj0:
	DB	0xE1, 0x23, 0x7E, 0xFE, 0xFF, 0xCA, 0x3B, 0x03, 0x23, 0x35, 0xC0, 0x47, 0xAF, 0x32, 0x68, 0x20	; Get player object structure 2014
	DB	0x32, 0x69, 0x20, 0x3E, 0x30, 0x32, 0x6A, 0x20, 0x78, 0x36, 0x05, 0x23, 0x35, 0xC2, 0x9B, 0x03
	DB	0x2A, 0x1A, 0x20, 0x06, 0x10, 0xCD, 0x24, 0x14, 0x21, 0x10, 0x20, 0x11, 0x10, 0x1B, 0x06, 0x10
	DB	0xCD, 0x32, 0x1A, 0x06, 0x00, 0xCD, 0xDC, 0x19, 0x3A, 0x6D, 0x20, 0xA7, 0xC0, 0x3A, 0xEF, 0x20
	DB	0xA7, 0xC8, 0x31, 0x00, 0x24, 0xFB, 0xCD, 0xD7, 0x19, 0xCD, 0x2E, 0x09, 0xA7, 0xCA, 0x6D, 0x16
	DB	0xCD, 0xE7, 0x18, 0x7E, 0xA7, 0xCA, 0x2C, 0x03, 0x3A, 0xCE, 0x20, 0xA7, 0xCA, 0x2C, 0x03
L_02ED:
	LDA	0x2067					; {ram.playerDataMSB} Player data MSB
	PUSH	PSW					; Hold the MSB
	RRC							; Player 1 is active player?
	JC	L_0332					; {} Yes ... go store player 1 shields and come back to 02F8
	CALL	RememberShields2	; {code.RememberShields2} No ... go store player 2 shields
L_02F8:
	CALL	L_0878				; {} Get ref-alien info and pointer to storage
	MOV	M,E						; Hold the ...
	INX	H						; ... ref-alien ...
	MOV	M,D						; ... screen coordinates
	DCX	H						; Back up ...
	DCX	H						; .. to delta storage
	MOV	M,B						; Store ref-alien's delta (direction)
	NOP							; ** Why?
	CALL	CopyRAMMirror		; {code.CopyRAMMirror} Copy RAM mirror (getting ready to switch players)
	POP	PSW						; Restore active player MSB
	RRC							; Player 1?
	MVI	A,0x21					; Player 1 data pointer
	MVI	B,0x00					; Cocktail bit=0 (player 1)
	JNC	L_0312					; {} It was player one ... keep data for player 2
	MVI	B,0x20					; Cocktail bit=1 (player 2)
	MVI	A,0x22					; Player 2 data pointer
L_0312:
	STA	0x2067					; {ram.playerDataMSB} Change players
	CALL	TwoSecDelay			; {code.TwoSecDelay} Two second delay
	XRA	A						; Clear the player-object ...
	STA	0x2011					; {ram.obj0TimerLSB} ... timer (player can move instantly after switching players)
	MOV	A,B						; Cocktail bit to A
	OUT	0x05					; {hard.SOUND2} Set the cocktail mode
	INR	A						; Fleet sound 1 (first tone)
	STA	0x2098					; {ram.soundPort5} Set the port 5 hold
	CALL	ClearPlayField		; {code.ClearPlayField} Clear center window
	CALL	RemoveShip			; {code.RemoveShip} Remove a ship and update indicators
	JMP	L_07F9					; {} Tell the players that the switch has been made
	;
D_032C:
	DB	0xCD, 0x7F, 0x1A, 0xC3, 0x17, 0x08	; {code.RemoveShip} Remove a ship and update indicators
	;
L_0332:
	CALL	RememberShields1	; {code.RememberShields1} Remember the shields for player 1
	JMP	L_02F8					; {} Back to switching-players above
D_0338:
	DB	0x00, 0x00, 0x00, 0x21, 0x68, 0x20, 0x36, 0x01, 0x23, 0x7E, 0xA7, 0xC3, 0xB0, 0x03, 0x00, 0x2B	; ** Why
	DB	0x36, 0x01, 0x3A, 0x1B, 0x20, 0x47, 0x3A, 0xEF, 0x20, 0xA7, 0xC2, 0x63, 0x03, 0x3A, 0x1D, 0x20
	DB	0x0F, 0xDA, 0x81, 0x03, 0x0F, 0xDA, 0x8E, 0x03, 0xC3, 0x6F, 0x03, 0xCD, 0xC0, 0x17, 0x07, 0x07
	DB	0xDA, 0x81, 0x03, 0x07, 0xDA, 0x8E, 0x03, 0x21, 0x18, 0x20, 0xCD, 0x3B, 0x1A, 0xCD, 0x47, 0x1A
	DB	0xCD, 0x39, 0x14, 0x3E, 0x00, 0x32, 0x12, 0x20, 0xC9
	; Handle player moving right
MovePlayerRight:
	DB	0x78, 0xFE, 0xD9, 0xCA, 0x6F, 0x03, 0x3C, 0x32, 0x1B, 0x20, 0xC3, 0x6F, 0x03	; Player coordinate
	; Handle player moving left
MovePlayerLeft:
	DB	0x78, 0xFE, 0x30, 0xCA, 0x6F, 0x03, 0x3D, 0x32, 0x1B, 0x20, 0xC3, 0x6F, 0x03	; Player coordinate
	; Toggle the player's blowing-up sprite between two pictures and draw it
DrawPlayerDie:
	DB	0x3C, 0xE6, 0x01, 0x32, 0x15, 0x20, 0x07, 0x07, 0x07, 0x07, 0x21, 0x70, 0x1C, 0x85, 0x6F, 0x22	; Toggle blowing-up ...
	DB	0x18, 0x20, 0xC3, 0x6F, 0x03, 0xC2, 0x4A, 0x03, 0x23, 0x35, 0xC2, 0x4A, 0x03, 0xC3, 0x46, 0x03
	; Game object 1: Move/draw the player shot
	;
	; This task executes at either mid-screen ISR (if it is on the top half of the non-rotated screen) or
	; at the end-screen ISR (if it is on the bottom half of the screen).
	;
GameObj1:
	DB	0x11, 0x2A, 0x20, 0xCD, 0x06, 0x1A, 0xE1, 0xD0, 0x23, 0x7E, 0xA7, 0xC8, 0xFE, 0x01, 0xCA, 0xFA	; Object's Yn coordiante
	DB	0x03, 0xFE, 0x02, 0xCA, 0x0A, 0x04, 0x23, 0xFE, 0x03, 0xC2, 0x2A, 0x04, 0x35, 0xCA, 0x36, 0x04
	DB	0x7E, 0xFE, 0x0F, 0xC0, 0xE5, 0xCD, 0x30, 0x04, 0xCD, 0x52, 0x14, 0xE1, 0x23, 0x34, 0x23, 0x23
	DB	0x35, 0x35, 0x23, 0x35, 0x35, 0x35, 0x23, 0x36, 0x08, 0xCD, 0x30, 0x04, 0xC3, 0x00, 0x14
	;
InitPlyShot:
	DB	0x3C, 0x77, 0x3A, 0x1B, 0x20, 0xC6, 0x08, 0x32, 0x2A, 0x20, 0xCD, 0x30, 0x04, 0xC3, 0x00, 0x14	; Type is now ...
	;
MovePlyShot:
	DB	0xCD, 0x30, 0x04, 0xD5, 0xE5, 0xC5, 0xCD, 0x52, 0x14, 0xC1, 0xE1, 0xD1, 0x3A, 0x2C, 0x20, 0x85	; {code.ReadPlyShot} Read the shot structure
	DB	0x6F, 0x32, 0x29, 0x20, 0xCD, 0x91, 0x14, 0x3A, 0x61, 0x20, 0xA7, 0xC8, 0x32, 0x02, 0x20, 0xC9
	DB	0xFE, 0x05, 0xC8, 0xC3, 0x36, 0x04
ReadPlyShot:
	DB	0x21, 0x27, 0x20, 0xC3, 0x3B, 0x1A	; Read 5 byte sprite structure for ...
EndOfBlowup:
	DB	0xCD, 0x30, 0x04, 0xCD, 0x52, 0x14, 0x21, 0x25, 0x20, 0x11, 0x25, 0x1B, 0x06, 0x07, 0xCD, 0x32	; {code.ReadPlyShot} Read the shot structure
	DB	0x1A, 0x2A, 0x8D, 0x20, 0x2C, 0x7D, 0xFE, 0x63, 0xDA, 0x53, 0x04, 0x2E, 0x54, 0x22, 0x8D, 0x20
	DB	0x2A, 0x8F, 0x20, 0x2C, 0x22, 0x8F, 0x20, 0x3A, 0x84, 0x20, 0xA7, 0xC0, 0x7E, 0xE6, 0x01, 0x01
	DB	0x29, 0x02, 0xC2, 0x6E, 0x04, 0x01, 0xE0, 0xFE, 0x21, 0x8A, 0x20, 0x71, 0x23, 0x23, 0x70, 0xC9
	; Game object 2: Alien rolling-shot (targets player specifically)
	;
	; The 2-byte value at 2038 is where the firing-column-table-pointer would be (see other
	; shots ... next game objects). This shot doesn't use that table. It targets the player
	; specifically. Instead the value is used as a flag to have the shot skip its first
	; attempt at firing every time it is reinitialized (when it blows up).
	;
	; The task-timer at 2032 is copied to 2080 in the game loop. The flag is used as a
	; synchronization flag to keep all the shots processed on separate interrupt ticks. This
	; has the main effect of slowing the shots down.
	;
	; When the timer is 2 the squiggly-shot/saucer (object 4 ) runs.
	; When the timer is 1 the plunger-shot (object 3) runs.
	; When the timer is 0 this object, the rolling-shot, runs.
	;
GameObj2:
	DB	0xE1, 0x3A, 0x32, 0x1B, 0x32, 0x32, 0x20, 0x2A, 0x38, 0x20, 0x7D, 0xB4, 0xC2, 0x8A, 0x04, 0x2B	; Game object data
	DB	0x22, 0x38, 0x20, 0xC9, 0x11, 0x35, 0x20, 0x3E, 0xF9, 0xCD, 0x50, 0x05, 0x3A, 0x46, 0x20, 0x32
	DB	0x70, 0x20, 0x3A, 0x56, 0x20, 0x32, 0x71, 0x20, 0xCD, 0x63, 0x05, 0x3A, 0x78, 0x20, 0xA7, 0x21
	DB	0x35, 0x20, 0xC2, 0x5B, 0x05
	; The rolling-shot has blown up. Reset the data structure.
ResetShot:
	DB	0x11, 0x30, 0x1B, 0x21, 0x30, 0x20, 0x06, 0x10, 0xC3, 0x32, 0x1A	; Reload ...
	; Game object 3: Alien plunger-shot
	; This is skipped if there is only one alien left on the screen.
	;
GameObj3:
	DB	0xE1, 0x3A, 0x6E, 0x20, 0xA7, 0xC0, 0x3A, 0x80, 0x20, 0xFE, 0x01, 0xC0, 0x11, 0x45, 0x20, 0x3E	; Game object data
	DB	0xED, 0xCD, 0x50, 0x05, 0x3A, 0x36, 0x20, 0x32, 0x70, 0x20, 0x3A, 0x56, 0x20, 0x32, 0x71, 0x20
	DB	0xCD, 0x63, 0x05, 0x3A, 0x76, 0x20, 0xFE, 0x10, 0xDA, 0xE7, 0x04, 0x3A, 0x48, 0x1B, 0x32, 0x76
	DB	0x20, 0x3A, 0x78, 0x20, 0xA7, 0x21, 0x45, 0x20, 0xC2, 0x5B, 0x05, 0x11, 0x40, 0x1B, 0x21, 0x40
	DB	0x20, 0x06, 0x10, 0xCD, 0x32, 0x1A, 0x3A, 0x82, 0x20, 0x3D, 0xC2, 0x08, 0x05, 0x3E, 0x01, 0x32
	DB	0x6E, 0x20, 0x2A, 0x76, 0x20, 0xC3, 0x7E, 0x06, 0xE1, 0x11, 0x55, 0x20, 0x3E, 0xDB, 0xCD, 0x50
	DB	0x05, 0x3A, 0x46, 0x20, 0x32, 0x70, 0x20, 0x3A, 0x36, 0x20, 0x32, 0x71, 0x20, 0xCD, 0x63, 0x05
	DB	0x3A, 0x76, 0x20, 0xFE, 0x15, 0xDA, 0x34, 0x05, 0x3A, 0x58, 0x1B, 0x32, 0x76, 0x20, 0x3A, 0x78
	DB	0x20, 0xA7, 0x21, 0x55, 0x20, 0xC2, 0x5B, 0x05, 0x11, 0x50, 0x1B, 0x21, 0x50, 0x20, 0x06, 0x10
	DB	0xCD, 0x32, 0x1A, 0x2A, 0x76, 0x20, 0x22, 0x58, 0x20, 0xC9
ToShotStruct:
	DB	0x32, 0x7F, 0x20, 0x21, 0x73, 0x20, 0x06, 0x0B, 0xC3, 0x32, 0x1A	; {ram.shotPicEnd} LSB of last byte of last picture in sprite
FromShotStruct:
	DB	0x11, 0x73, 0x20, 0x06, 0x0B, 0xC3, 0x32, 0x1A	; Source is the shot-structure
	; Each of the 3 shots copy their data to the 2073 structure (0B bytes) and call this.
	; Then they copy back if the shot is still active. Otherwise they copy from the mirror.
	;
	; The alien "fire rate" is based on the number of steps the other two shots on the screen
	; have made. The smallest number-of-steps is compared to the reload-rate. If it is too
	; soon then no shot is made. The reload-rate is based on the player's score. The MSB
	; is looked up in a table to get the reload-rate. The smaller the rate the faster the
	; aliens fire. Setting rate this way keeps shots from walking on each other.
	;
HandleAlienShot:
	DB	0x21, 0x73, 0x20, 0x7E, 0xE6, 0x80, 0xC2, 0xC1, 0x05, 0x3A, 0xC1, 0x20, 0xFE, 0x04, 0x3A, 0x69	; Start of active shot structure
	DB	0x20, 0xCA, 0xB7, 0x05, 0xA7, 0xC8, 0x23, 0x36, 0x00, 0x3A, 0x70, 0x20, 0xA7, 0xCA, 0x89, 0x05
	DB	0x47, 0x3A, 0xCF, 0x20, 0xB8, 0xD0, 0x3A, 0x71, 0x20, 0xA7, 0xCA, 0x96, 0x05, 0x47, 0x3A, 0xCF
	DB	0x20, 0xB8, 0xD0, 0x23, 0x7E, 0xA7, 0xCA, 0x1B, 0x06, 0x2A, 0x76, 0x20, 0x4E, 0x23, 0x00, 0x22
	DB	0x76, 0x20, 0xCD, 0x2F, 0x06, 0xD0, 0xCD, 0x7A, 0x01, 0x79, 0xC6, 0x07, 0x67, 0x7D, 0xD6, 0x0A
	DB	0x6F, 0x22, 0x7B, 0x20, 0x21, 0x73, 0x20, 0x7E, 0xF6, 0x80, 0x77, 0x23, 0x34, 0xC9, 0x11, 0x7C
	DB	0x20, 0xCD, 0x06, 0x1A, 0xD0, 0x23, 0x7E, 0xE6, 0x01, 0xC2, 0x44, 0x06, 0x23, 0x34, 0xCD, 0x75
	DB	0x06, 0x3A, 0x79, 0x20, 0xC6, 0x03, 0x21, 0x7F, 0x20, 0xBE, 0xDA, 0xE2, 0x05, 0xD6, 0x0C, 0x32
	DB	0x79, 0x20, 0x3A, 0x7B, 0x20, 0x47, 0x3A, 0x7E, 0x20, 0x80, 0x32, 0x7B, 0x20, 0xCD, 0x6C, 0x06
	DB	0x3A, 0x7B, 0x20, 0xFE, 0x15, 0xDA, 0x12, 0x06, 0x3A, 0x61, 0x20, 0xA7, 0xC8, 0x3A, 0x7B, 0x20
	DB	0xFE, 0x1E, 0xDA, 0x12, 0x06, 0xFE, 0x27, 0x00, 0xD2, 0x12, 0x06, 0x97, 0x32, 0x15, 0x20, 0x3A
	DB	0x73, 0x20, 0xF6, 0x01, 0x32, 0x73, 0x20, 0xC9, 0x3A, 0x1B, 0x20, 0xC6, 0x08, 0x67, 0xCD, 0x6F
	DB	0x15, 0x79, 0xFE, 0x0C, 0xDA, 0xA5, 0x05, 0x0E, 0x0B, 0xC3, 0xA5, 0x05
	; C contains the target column. Look for a live alien in the column starting with
	; the lowest position. Return C=1 if found ... HL points to found slot.
FindInColumn:
	DB	0x0D, 0x3A, 0x67, 0x20, 0x67, 0x69, 0x16, 0x05, 0x7E, 0xA7, 0x37, 0xC0, 0x7D, 0xC6, 0x0B, 0x6F	; Column that is firing
	DB	0x15, 0xC2, 0x37, 0x06, 0xC9
	; Alien shot is blowing up
ShotBlowingUp:
	DB	0x21, 0x78, 0x20, 0x35, 0x7E, 0xFE, 0x03, 0xC2, 0x67, 0x06, 0xCD, 0x75, 0x06, 0x21, 0xDC, 0x1C	; Blow up timer
	DB	0x22, 0x79, 0x20, 0x21, 0x7C, 0x20, 0x35, 0x35, 0x2B, 0x35, 0x35, 0x3E, 0x06, 0x32, 0x7D, 0x20
	DB	0xC3, 0x6C, 0x06, 0xA7, 0xC0, 0xC3, 0x75, 0x06, 0x21, 0x79, 0x20, 0xCD, 0x3B, 0x1A, 0xC3, 0x91
	DB	0x14, 0x21, 0x79, 0x20, 0xCD, 0x3B, 0x1A, 0xC3, 0x52, 0x14, 0x22, 0x48, 0x20, 0xC9
	; Game object 4: Flying Saucer OR squiggly shot
	;
	; This task is shared by the squiggly-shot and the flying saucer. The saucer waits until the
	; squiggly-shot is over before it begins.
	;
GameObj4:
	DB	0xE1, 0x3A, 0x80, 0x20, 0xFE, 0x02, 0xC0, 0x21, 0x83, 0x20, 0x7E, 0xA7, 0xCA, 0x0F, 0x05, 0x3A	; Pull data pointer from the stack (not going to use it)
	DB	0x56, 0x20, 0xA7, 0xC2, 0x0F, 0x05, 0x23, 0x7E, 0xA7, 0xC2, 0xAB, 0x06, 0x3A, 0x82, 0x20, 0xFE
	DB	0x08, 0xDA, 0x0F, 0x05, 0x36, 0x01, 0xCD, 0x3C, 0x07, 0x11, 0x8A, 0x20, 0xCD, 0x06, 0x1A, 0xD0
	DB	0x21, 0x85, 0x20, 0x7E, 0xA7, 0xC2, 0xD6, 0x06, 0x21, 0x8A, 0x20, 0x7E, 0x23, 0x23, 0x86, 0x32
	DB	0x8A, 0x20, 0xCD, 0x3C, 0x07, 0x21, 0x8A, 0x20, 0x7E, 0xFE, 0x28, 0xDA, 0xF9, 0x06, 0xFE, 0xE1
	DB	0xD2, 0xF9, 0x06, 0xC9, 0x06, 0xFE, 0xCD, 0xDC, 0x19, 0x23, 0x35, 0x7E, 0xFE, 0x1F, 0xCA, 0x4B
	DB	0x07, 0xFE, 0x18, 0xCA, 0x0C, 0x07, 0xA7, 0xC0, 0x06, 0xEF, 0x21, 0x98, 0x20, 0x7E, 0xA0, 0x77
	DB	0xE6, 0x20, 0xD3, 0x05, 0x00, 0x00, 0x00, 0xCD, 0x42, 0x07, 0xCD, 0xCB, 0x14, 0x21, 0x83, 0x20
	DB	0x06, 0x0A, 0xCD, 0x5F, 0x07
L_0707:
	MVI	B,0xFE					; Turn off UFO ...
	JMP	SoundBits3Off			; {code.SoundBits3Off} ... sound and out
D_070C:
	DB	0x3E, 0x01, 0x32, 0xF1, 0x20, 0x2A, 0x8D, 0x20, 0x46, 0x0E, 0x04, 0x21, 0x50, 0x1D, 0x11, 0x4C	; Flag the score ...
	DB	0x1D, 0x1A, 0xB8, 0xCA, 0x28, 0x07, 0x23, 0x13, 0x0D, 0xC2, 0x1D, 0x07, 0x7E, 0x32, 0x87, 0x20
	DB	0x26, 0x00, 0x68, 0x29, 0x29, 0x29, 0x29, 0x22, 0xF2, 0x20, 0xCD, 0x42, 0x07, 0xC3, 0xF1, 0x08
	DB	0xCD, 0x42, 0x07, 0xC3, 0x39, 0x14, 0x21, 0x87, 0x20, 0xCD, 0x3B, 0x1A, 0xC3, 0x47, 0x1A, 0x06
	DB	0x10, 0x21, 0x98, 0x20, 0x7E, 0xB0, 0x77, 0xCD, 0x70, 0x17, 0x21, 0x7C, 0x1D, 0x22, 0x87, 0x20
	DB	0xC3, 0x3C, 0x07, 0x11, 0x83, 0x1B, 0xC3, 0x32, 0x1A
	; Wait for player 1 start button press
WaitForStart:
	MVI	A,0x01					; Tell ISR that we ...
	STA	0x2093					; {ram.waitStartLoop} ... have started to wait
	LXI	SP,0x2400				; Reset stack
	EI							; Enable interrupts
	CALL	L_1979				; {} Suspend game tasks
	CALL	ClearPlayField		; {code.ClearPlayField} Clear center window
	LXI	H,0x3013				; Screen coordinates
	LXI	D,MessagePush			; "PRESS"
	MVI	C,0x04					; Message length
	CALL	PrintMessage		; {code.PrintMessage} Print it
L_077F:
	LDA	0x20EB					; {ram.numCoins} Number of credits
	DCR	A						; Set flags
	LXI	H,0x2810				; Screen coordinates
	MVI	C,0x14					; Message length
	JNZ	L_0857					; {} Take 1 or 2 player start
	LXI	D,Message1Only			; "ONLY 1PLAYER BUTTON "
	CALL	PrintMessage		; {code.PrintMessage} Print message
	IN	0x01					; {hard.INP1} Read player controls
	ANI	0x04					; 1Player start button?
	JZ	L_077F					; {} No ... wait for button or credit
	; Start New Game
	; 1 Player start
NewGame:
	MVI	B,0x99					; Essentially a -1 for DAA
	XRA	A						; Clear two player flag
	;
	; 2 player start sequence enters here with a=1 and B=98 (-2)
L_079B:
	STA	0x20CE					; {ram.twoPlayers} Set flag for 1 or 2 players
	LDA	0x20EB					; {ram.numCoins} Number of credits
	ADD	B						; Take away credits
	DAA							; Convert back to DAA
	STA	0x20EB					; {ram.numCoins} New credit count
	CALL	DrawNumCredits		; {code.DrawNumCredits} Display number of credits
	LXI	H,Reset					; Score of 0000
	SHLD	0x20F8				; {ram.P1ScorL} Clear player-1 score
	SHLD	0x20FC				; {ram.P2ScorL} Clear player-2 score
	CALL	L_1925				; {} Print player-1 score
	CALL	L_192B				; {} Print player-2 score
	CALL	DsableGameTasks		; {code.DsableGameTasks} Disable game tasks
	LXI	H,0x0101				; Two bytes 1, 1
	MOV	A,H						; 1 to A
	STA	0x20EF					; {ram.gameMode} 20EF=1 ... game mode
	SHLD	0x20E7				; {ram.player1Alive} 20E7 and 20E8 both one ... players 1 and 2 are alive
	SHLD	0x20E5				; {ram.player1Ex} Extra-ship is available for player-1 and player-2
	CALL	DrawStatus			; {code.DrawStatus} Print scores and credits
	CALL	DrawShieldPl1		; {code.DrawShieldPl1} Draw shields for player-1
	CALL	DrawShieldPl2		; {code.DrawShieldPl2} Draw shields for player-2
	CALL	GetShipsPerCred		; {code.GetShipsPerCred} Get number of ships from DIP settings
	STA	0x21FF					; {ram.p1ShipsRem} Player-1 ships
	STA	0x22FF					; {ram.p2ShipsRem} Player-2 ships
	CALL	L_00D7				; {} Set player-1 and player-2 alien racks going right
	XRA	A						; Make a 0
	STA	0x21FE					; {ram.p1RackCnt} Player 1 is on first rack of aliens
	STA	0x22FE					; {ram.p2RackCnt} Player 2 is on first rack of aliens
	CALL	InitAliens			; {code.InitAliens} Initialize 55 aliens for player 1
	CALL	InitAliensP2		; {code.InitAliensP2} Initialize 55 aliens for player 2
	LXI	H,0x3878				; Screen coordinates for lower-left alien
	SHLD	0x21FC				; {ram.p1RefAlienY} Initialize reference alien for player 1
	SHLD	0x22FC				; {ram.p2RefAlienYr} Initialize reference alien for player 2
	CALL	CopyRAMMirror		; {code.CopyRAMMirror} Copy ROM mirror to RAM (2000 - 20C0)
	CALL	RemoveShip			; {code.RemoveShip} Initialize ship hold indicator
	;
L_07F9:
	CALL	PromptPlayer		; {code.PromptPlayer} Prompt with "PLAY PLAYER "
	CALL	ClearPlayField		; {code.ClearPlayField} Clear the playfield
	NOP							; % Why?
	XRA	A						; Make a 0
	STA	0x20C1					; {ram.isrSplashTask} Disable isr splash-task animation
L_0804:
	CALL	DrawBottomLine		; {code.DrawBottomLine} Draw line across screen under player
	LDA	0x2067					; {ram.playerDataMSB} Current player
	RRC							; Right bit tells all
	JC	L_0872					; {} Go do player 1
	;
	CALL	RestoreShields2		; {code.RestoreShields2} Restore shields for player 2
	CALL	DrawBottomLine		; {code.DrawBottomLine} Draw line across screen under player
L_0814:
	CALL	InitRack			; {code.InitRack} Initialize alien rack for current player
	CALL	EnableGameTasks		; {code.EnableGameTasks} Enable game tasks in ISR
	MVI	B,0x20					; Enable ...
	CALL	SoundBits3On		; {code.SoundBits3On} ... sound amplifier
	;
	; GAME LOOP
	;
L_081F:
	CALL	PlrFireOrDemo		; {code.PlrFireOrDemo} Initiate player shot if button pressed
	CALL	PlyrShotAndBump		; {code.PlyrShotAndBump} Collision detect player's shot and rack-bump
	CALL	CountAliens			; {code.CountAliens} Count aliens (count to 2082)
	CALL	AdjustScore			; {code.AdjustScore} Adjust score (and print) if there is an adjustment
	LDA	0x2082					; {ram.numAliens} Number of live aliens
	ANA	A						; All aliens gone?
	JZ	L_09EF					; {} Yes ... end of turn
	CALL	AShotReloadRate		; {code.AShotReloadRate} Update alien-shot-rate based on player's score
	CALL	L_0935				; {} Check (and handle) extra ship award
	CALL	SpeedShots			; {code.SpeedShots} Adjust alien shot speed
	CALL	ShotSound			; {code.ShotSound} Shot sound on or off with 2025
	CALL	L_0A59				; {} Check if player is hit
	JZ	L_0849					; {} No hit ... jump handler
	MVI	B,0x04					; Player hit sound
	CALL	SoundBits3On		; {code.SoundBits3On} Make explosion sound
L_0849:
	CALL	FleetDelayExShip	; {code.FleetDelayExShip} Extra-ship sound timer, set fleet-delay, play fleet movement sound
	OUT	0x06					; {hard.WATCHDOG} Feed the watchdog
	CALL	CtrlSaucerSound		; {code.CtrlSaucerSound} Control saucer sound
	JMP	L_081F					; {} Continue game loop
D_0854:
	DB	0x00, 0x00, 0x00		; ** Why?
	; Test for 1 or 2 player start button press
L_0857:
	LXI	D,MessageB1or2			; "1 OR 2PLAYERS BUTTON"
	CALL	PrintMessage		; {code.PrintMessage} Print message
	MVI	B,0x98					; -2 (take away 2 credits)
	IN	0x01					; {hard.INP1} Read player controls
	RRC							; Test ...
	RRC							; ... bit 2
	JC	L_086D					; {} 2 player button pressed ... do it
	RRC							; Test bit 3
	JC	NewGame					; {code.NewGame} One player start ... do it
	JMP	L_077F					; {} Keep waiting on credit or button
	; 2 PLAYER START
L_086D:
	MVI	A,0x01					; Flag 2 player game
	JMP	L_079B					; {} Continue normal startup
L_0872:
	CALL	RestoreShields1		; {code.RestoreShields1} Restore shields for player 1
	JMP	L_0814					; {} Continue in game loop
L_0878:
	LDA	0x2008					; {ram.refAlienDXr} Alien deltaY
	MOV	B,A						; Hold it
	LHLD	0x2009				; {ram.refAlienYr} Alien coordinates
	XCHG						; Coordinates to DE
	JMP	GetAlRefPtr				; {code.GetAlRefPtr} HL is 21FC or 22FC and out
D_0883:
	DB	0x00, 0x00, 0x00		; ** Why?
	; Get pointer to player's alien ref coordiantes
GetAlRefPtr:
	LDA	0x2067					; {ram.playerDataMSB} Player data MSB (21 or 22)
	MOV	H,A						; To H
	MVI	L,0xFC					; 21FC or 22FC ... alien coordinates
	RET							; Done
	; Print "PLAY PLAYER <n>" and blink score for 2 seconds.
	;
PromptPlayer:
	LXI	H,0x2B11				; Screen coordinates
	LXI	D,MesssageP1			; Message "PLAY PLAYER<1>"
	MVI	C,0x0E					; 14 bytes in message
	CALL	PrintMessage		; {code.PrintMessage} Print the message
	LDA	0x2067					; {ram.playerDataMSB} Get the player number
	RRC							; C will be set for player 1
	MVI	A,0x1C					; The "2" character
	LXI	H,0x3711				; Replace the "<1>" with "<2">
	CNC	DrawChar				; {code.DrawChar} If player 2 ... change the message
	MVI	A,0xB0					; Delay of 176 (roughly 2 seconds)
	STA	0x20C0					; {ram.isrDelay} Set the ISR delay value
	;
L_08A9:
	LDA	0x20C0					; {ram.isrDelay} Get the ISR delay value
	ANA	A						; Has the 2 second delay expired?
	RZ							; Yes ... done
	ANI	0x04					; Every 4 ISRs ...
	JNZ	L_08BC					; {} ... flash the player's score
	CALL	L_09CA				; {} Get the score descriptor for the active player
	CALL	DrawScore			; {code.DrawScore} Draw the score
	JMP	L_08A9					; {} Back to the top of the wait loop
	;
L_08BC:
	MVI	B,0x20					; 32 rows (4 characters * 8 bytes each)
	LXI	H,0x271C				; Player-1 score on the screen
	LDA	0x2067					; {ram.playerDataMSB} Get the player number
	RRC							; C will be set for player 1
	JC	L_08CB					; {} We have the right score coordinates
	LXI	H,0x391C				; Use coordinates for player-2's score
L_08CB:
	CALL	ClearSmallSprite	; {code.ClearSmallSprite} Clear a one byte sprite at HL
	JMP	L_08A9					; {} Back to the top of the wait loop
	; Get number of ships from DIP settings
GetShipsPerCred:
	IN	0x02					; {hard.INP2} DIP settings
	ANI	0x03					; Get number of ships
	ADI	0x03					; From 3-6
	RET							; Out
	; With less than 9 aliens on the screen the alien shots get a tad bit faster. Probably
	; because the advancing rack can catch them.
	;
SpeedShots:
	LDA	0x2082					; {ram.numAliens} Number of aliens on screen
	CPI	0x09					; More than 8?
	RNC							; Yes ... leave shot speed alone
	MVI	A,0xFB					; Normally FF (-4) ... now FB (-5)
	STA	0x207E					; {ram.alienShotDelta} Speed up alien shots
	RET							; Done
L_08E4:
	LDA	0x20CE					; {ram.twoPlayers} Number of players
	ANA	A						; Skip if ...
	RNZ							; ... two player
	LXI	H,0x391C				; Player 2's score
	MVI	B,0x20					; 32 rows is 4 digits * 8 rows each
	JMP	ClearSmallSprite		; {code.ClearSmallSprite} Clear a one byte sprite (32 rows long) at HL
D_08F1:
	DB	0x0E, 0x03				; Length of saucer-score message ... fall into print
	; Print a message on the screen
	; HL = coordinates
	; DE = message buffer
	; C = length
PrintMessage:
	LDAX	D					; Get character
	PUSH	D					; Preserve
	CALL	DrawChar			; {code.DrawChar} Print character
	POP	D						; Restore
	INX	D						; Next character
	DCR	C						; All done?
	JNZ	PrintMessage			; {code.PrintMessage} Print all of message
	RET							; Out
	;=============================================================
	; Get pointer to 8 byte sprite number in A and
	; draw sprite on screen at HL
DrawChar:
	LXI	D,Characters			; Character set
	PUSH	H					; Preserve
	MVI	H,0x00					; MSB=0
	MOV	L,A						; Character number to L
	DAD	H						; HL = HL *2
	DAD	H						; *4
	DAD	H						; *8 (8 bytes each)
	DAD	D						; Get pointer to sprite
	XCHG						; Now into DE
	POP	H						; Restore HL
	MVI	B,0x08					; 8 bytes each
	OUT	0x06					; {hard.WATCHDOG} Feed watchdog
	JMP	DrawSimpSprite			; {code.DrawSimpSprite} To screen
TimeToSaucer:
	LDA	0x2009					; {ram.refAlienYr} Reference alien's X coordinate
	CPI	0x78					; Don't process saucer timer ... ($78 is 1st rack Yr)
	RNC							; ... unless aliens are closer to bottom
	LHLD	0x2091				; {ram.tillSaucerLSB} Time to saucer
	MOV	A,L						; Is it time ...
	ORA	H						; ... for a saucer
	JNZ	L_0929					; {} No ... skip flagging
	LXI	H,0x0600				; Reset timer to 600 game loops
	MVI	A,0x01					; Flag a ...
	STA	0x2083					; {ram.saucerStart} ... saucer sequence
L_0929:
	DCX	H						; Decrement the ...
	SHLD	0x2091				; {ram.tillSaucerLSB} ... time-to-saucer
	RET							; Done
	;=============================================================
	; Get number of ships for acive player
L_092E:
	CALL	GetPlayerDataPtr	; {code.GetPlayerDataPtr} HL points to player data
	MVI	L,0xFF					; Last byte = numbe of ships
	MOV	A,M						; Get number of ships
	RET							; Done
	;=============================================================
	; Award extra ship if score has reached ceiling
L_0935:
	CALL	CurPlyAlive			; {code.CurPlyAlive} Get descriptor of sorts
	DCX	H						; Back up ...
	DCX	H						; ... two bytes
	MOV	A,M						; Has extra ship ...
	ANA	A						; already been awarded?
	RZ							; Yes ... ignore
	MVI	B,0x15					; Default 1500
	IN	0x02					; {hard.INP2} Read DIP settings
	ANI	0x08					; Extra ship at 1000 or 1500
	JZ	L_0948					; {} 0=1500
	MVI	B,0x10					; Awarded at 1000
L_0948:
	CALL	L_09CA				; {} Get score descriptor for active player
	INX	H						; MSB of score ...
	MOV	A,M						; ... to accumulator
	CMP	B						; Time for an extra ship?
	RC							; No ... out
	CALL	L_092E				; {} Get pointer to number of ships
	INR	M						; Bump number of ships
	MOV	A,M						; Get the new total
	PUSH	PSW					; Hang onto it for a bit
	LXI	H,0x2501				; Screen coords for ship hold
L_0958:
	INR	H						; Bump to ...
	INR	H						; ... next
	DCR	A						; ... spot
	JNZ	L_0958					; {} Find spot for new ship
	MVI	B,0x10					; 16 byte sprite
	LXI	D,PlayerSprite			; Player sprite
	CALL	DrawSimpSprite		; {code.DrawSimpSprite} Draw the sprite
	POP	PSW						; Restore the count
	INR	A						; +1
	CALL	L_1A8B				; {} Print the number of ships
	CALL	CurPlyAlive			; {code.CurPlyAlive} Get descriptor for active player of some sort
	DCX	H						; Back up ...
	DCX	H						; ... two bytes
	MVI	M,0x00					; Flag extra ship has been awarded
	MVI	A,0xFF					; Set timer ...
	STA	0x2099					; {ram.extraHold} ... for extra-ship sound
	MVI	B,0x10					; Make sound ...
	JMP	SoundBits3On			; {code.SoundBits3On} ... for extra man
AlienScoreValue:
	LXI	H,AlienScores			; Table for scores for hitting alien
	CPI	0x02					; 0 or 1 (lower two rows) ...
	RC							; ... return HL points to value 10
	INX	H						; next value
	CPI	0x04					; 2 or 3 (middle two rows) ...
	RC							; ... return HL points to value 20
	INX	H						; Top row ...
	RET							; ... return HL points to value 30
	; Adjust the score for the active player. 20F1 is 1 if there is a new value to add.
	; The adjustment is in 20F2,20F3. Then print the score.
AdjustScore:
	CALL	L_09CA				; {} Get score structure for active player
	LDA	0x20F1					; {ram.adjustScore} Does the score ...
	ANA	A						; ... need increasing?
	RZ							; No ... done
	XRA	A						; Mark score ...
	STA	0x20F1					; {ram.adjustScore} ... as adjusted
	PUSH	H					; Hold the pointer to the structure
	LHLD	0x20F2				; {ram.scoreDeltaLSB} Get requested adjustment
	XCHG						; Adjustment to DE
	POP	H						; Get back pointer to structure
	MOV	A,M						; Add adjustment ...
	ADD	E						; ... first byte
	DAA							; Adjust it for BCD
	MOV	M,A						; Store new LSB
	MOV	E,A						; Add adjustment ...
	INX	H						; ... to ...
	MOV	A,M						; ... second ...
	ADC	D						; ... byte
	DAA							; Adjust for BCD (cary gets dropped)
	MOV	M,A						; Store second byte
	MOV	D,A						; Second byte to D (first byte still in E)
	INX	H						; Load ...
	MOV	A,M						; ... the ...
	INX	H						; ... screen ...
	MOV	H,M						; ... coordinates ...
	MOV	L,A						; ... to HL
	JMP	Print4Digits			; {code.Print4Digits} ** Usually a good idea, but wasted here
	; Print 4 digits in DE
Print4Digits:
	MOV	A,D						; Get first 2 digits of BCD or hex
	CALL	DrawHexByte			; {code.DrawHexByte} Print them
	MOV	A,E						; Get second 2 digits of BCD or hex (fall into print)
	; Display 2 digits in A to screen at HL
DrawHexByte:
	PUSH	D					; Preserve
	PUSH	PSW					; Save for later
	RRC							; Get ...
	RRC							; ...
	RRC							; ...
	RRC							; ... left digit
	ANI	0x0F					; Mask out lower digit's bits
	CALL	L_09C5				; {} To screen at HL
	POP	PSW						; Restore digit
	ANI	0x0F					; Mask out upper digit
	CALL	L_09C5				; {} To screen
	POP	D						; Restore
	RET							; Done
	;
L_09C5:
	ADI	0x1A					; Bump to number characters
	JMP	DrawChar				; {code.DrawChar} Continue ...
	; Get score descriptor for active player
L_09CA:
	LDA	0x2067					; {ram.playerDataMSB} Get active player
	RRC							; Test for player
	LXI	H,0x20F8				; Player 1 score descriptor
	RC							; Keep it if player 1 is active
	LXI	H,0x20FC				; Else get player 2 descriptor
	RET							; Out
	; Clear center window of screen
ClearPlayField:
	LXI	H,0x2402				; Thrid from left, top of screen
L_09D9:
	MVI	M,0x00					; Clear screen byte
	INX	H						; Next in row
	MOV	A,L						; Get X ...
	ANI	0x1F					; ... coordinate
	CPI	0x1C					; Edge minus a buffer?
	JC	L_09E8					; {} No ... keep going
	LXI	D,D_0006				; Else ... bump to
	DAD	D						; ... next edge + buffer
L_09E8:
	MOV	A,H						; Get Y coordinate
	CPI	0x40					; Reached bottom?
	JC	L_09D9					; {} No ... keep going
	RET							; Done
L_09EF:
	CALL	L_0A3C				; {}
	XRA	A						; Suspend ...
	STA	0x20E9					; {ram.suspendPlay} ... ISR game tasks
	CALL	ClearPlayField		; {code.ClearPlayField} Clear playfield
	LDA	0x2067					; {ram.playerDataMSB} Hold current player number ...
	PUSH	PSW					; ... on stack
	CALL	CopyRAMMirror		; {code.CopyRAMMirror} Block copy RAM mirror from ROM
	POP	PSW						; Restore ...
	STA	0x2067					; {ram.playerDataMSB} ... current player number
	LDA	0x2067					; {ram.playerDataMSB} ** Why load this again? Nobody ever jumps to 0A04?
	MOV	H,A						; To H
	PUSH	H					; Hold player-data pointer
	MVI	L,0xFE					; 2xFE ... rack count
	MOV	A,M						; Get the number of racks the player has beaten
	ANI	0x07					; 0-7
	INR	A						; Now 1-8
	MOV	M,A						; Update count since player just beat a rack
	LXI	H,0x1DA2				; Starting coordinate of alien table
L_0A13:
	INX	H						; Find the ...
	DCR	A						; ... right entry ...
	JNZ	L_0A13					; {} ... in the table
	MOV	A,M						; Get the starting Y coordiante
	POP	H						; Restore player's pointer
	MVI	L,0xFC					; 2xFC ...
	MOV	M,A						; Set rack's starting Y coordinate
	INX	H						; Point to X
	MVI	M,0x38					; Set rack's starting X coordinate to 38
	MOV	A,H						; Player ...
	RRC							; ... number to carry
	JC	L_0A33					; {} 2nd player stuff
	MVI	A,0x21					; Start fleet with ...
	STA	0x2098					; {ram.soundPort5} ... first sound
	CALL	DrawShieldPl2		; {code.DrawShieldPl2} Draw shields for player 2
	CALL	InitAliensP2		; {code.InitAliensP2} Initalize aliens for player 2
	JMP	L_0804					; {} Continue at top of game loop
	;
L_0A33:
	CALL	DrawShieldPl1		; {code.DrawShieldPl1} Draw shields for player 1
	CALL	InitAliens			; {code.InitAliens} Initialize aliens for player 1
	JMP	L_0804					; {} Continue at top of game loop
	;
L_0A3C:
	CALL	L_0A59				; {} Check player collision
	JNZ	L_0A52					; {} Player is not alive ... skip delay
	MVI	A,0x30					; Half second delay
	STA	0x20C0					; {ram.isrDelay} Set ISR timer
L_0A47:
	LDA	0x20C0					; {ram.isrDelay} Has timer expired?
	ANA	A						; Check exipre
	RZ							; Out if done
	CALL	L_0A59				; {} Check player collision
	JZ	L_0A47					; {} No collision ... wait on timer
L_0A52:
	CALL	L_0A59				; {} Wait for ...
	JNZ	L_0A52					; {} ... collision to end
	RET							; Done
	; Check to see if player is hit
L_0A59:
	LDA	0x2015					; {ram.playerAlive} Active player hit flag
	CPI	0xFF					; All FFs means player is OK
	RET							; Out
	; Start the hit-alien sound and flag the adjustment for the score.
	; B contains the row, which determines the score value.
ScoreForAlien:
	LDA	0x20EF					; {ram.gameMode} Are we in ...
	ANA	A						; ... game mode?
	JZ	L_0A7C					; {} No ... skip scoring in demo
	MOV	C,B						; Hold row number
	MVI	B,0x08					; Alien hit sound
	CALL	SoundBits3On		; {code.SoundBits3On} Enable sound
	MOV	B,C						; Restore row number
	MOV	A,B						; Into A
	CALL	AlienScoreValue		; {code.AlienScoreValue} Look up the score for the alien
	MOV	A,M						; Get the score value
	LXI	H,0x20F3				; Pointer to score delta
	MVI	M,0x00					; Upper byte of score delta is "00"
	DCX	H						; Point to score delta LSB
	MOV	M,A						; Set score for hitting alien
	DCX	H						; Point to adjust-score-flag
	MVI	M,0x01					; The score will get changed elsewhere
L_0A7C:
	LXI	H,0x2062				; Return exploding-alien descriptor
	RET							; Out
	; Start the ISR moving the sprite. Return when done.
Animate:
	MVI	A,0x02					; Start simple linear ...
	STA	0x20C1					; {ram.isrSplashTask} ... sprite animation (splash)
L_0A85:
	OUT	0x06					; {hard.WATCHDOG} Feed watchdog
	LDA	0x20CB					; {ram.splashReached} Has the ...
	ANA	A						; ... sprite reached target?
	JZ	L_0A85					; {} No ... wait
	XRA	A						; Stop ...
	STA	0x20C1					; {ram.isrSplashTask} ... ISR animation
	RET							; Done
	; Print message from DE to screen at HL (length in C) with a
	; delay between letters.
PrintMessageDel:
	PUSH	D					; Preserve
	LDAX	D					; Get character
	CALL	DrawChar			; {code.DrawChar} Draw character on screen
	POP	D						; Preserve
	MVI	A,0x07					; Delay between letters
	STA	0x20C0					; {ram.isrDelay} Set counter
L_0A9E:
	LDA	0x20C0					; {ram.isrDelay} Get counter
	DCR	A						; Is it 1?
	JNZ	L_0A9E					; {} No ... wait on it
	INX	D						; Next in message
	DCR	C						; All done?
	JNZ	PrintMessageDel			; {code.PrintMessageDel} No ... do all
	RET							; Out
SplashSquiggly:
	LXI	H,0x2050				; Pointer to game-object 4 timer
	JMP	L_024B					; {} Process squiggly-shot in demo mode
	; Delay 64 interrupts
OneSecDelay:
	MVI	A,0x40					; Delay of 64 (tad over 1 sec)
	JMP	WaitOnDelay				; {code.WaitOnDelay} Do delay
	; Delay 128 interrupts
TwoSecDelay:
	MVI	A,0x80					; Delay of 80 (tad over 2 sec)
	JMP	WaitOnDelay				; {code.WaitOnDelay} Do delay
SplashDemo:
	POP	H						; Drop the call to ABF and ...
	JMP	L_0072					; {} ... do a demo game loop without sound
	; Different types of splash tasks managed by ISR in splash screens. The ISR
	; calls this if in splash-mode. These may have been bit flags to allow all 3
	; at the same time. Maybe it is just easier to do a switch with a rotate-to-carry.
	;
ISRSplTasks:
	LDA	0x20C1					; {ram.isrSplashTask} Get the ISR task number
	RRC							; In demo play mode?
	JC	SplashDemo				; {code.SplashDemo} 1: Yes ... go do game play (without sound)
	RRC							; Moving little alien from point A to B?
	JC	SplashSprite			; {code.SplashSprite} 2: Yes ... go move little alien from point A to B
	RRC							; Shooting extra "C" with squiggly shot?
	JC	SplashSquiggly			; {code.SplashSquiggly} 4: Yes ... go shoot extra "C" in splash
	RET							; No task to do
	; Message to center of screen.
	; Only used in one place for "SPACE  INVADERS"
L_0ACF:
	LXI	H,0x2B14				; Near center of screen
	MVI	C,0x0F					; 15 bytes in message
	JMP	PrintMessageDel			; {code.PrintMessageDel} Print and out
	; Wait on ISR counter to reach 0
WaitOnDelay:
	STA	0x20C0					; {ram.isrDelay} Delay counter
L_0ADA:
	LDA	0x20C0					; {ram.isrDelay} Get current delay
	ANA	A						; Zero yet?
	JNZ	L_0ADA					; {} No ... wait on it
	RET							; Out
	; Init the splash-animation block
IniSplashAni:
	LXI	H,0x20C2				; The splash-animation descriptor
	MVI	B,0x0C					; C bytes
	JMP	BlockCopy				; {code.BlockCopy} Block copy DE to descriptor
	;=============================================================
	; After initialization ... splash screens
L_0AEA:
	XRA	A						; Make a 0
	OUT	0x03					; {hard.SOUND1} Turn off sound
	OUT	0x05					; {hard.SOUND2} Turn off sound
	CALL	L_1982				; {} Turn off ISR splash-task
	EI							; Enable interrupts (using them for delays)
	CALL	OneSecDelay			; {code.OneSecDelay} One second delay
	LDA	0x20EC					; {ram.splashAnimate} Splash screen type
	ANA	A						; Set flags based on type
	LXI	H,0x3017				; Screen coordinates (middle near top)
	MVI	C,0x04					; 4 characters in "PLAY"
	JNZ	L_0BE8					; {} Not 0 ... do "normal" PLAY
	LXI	D,MessagePlayUY			; The "PLAy" with an upside down 'Y'
	CALL	PrintMessageDel		; {code.PrintMessageDel} Print the "PLAy"
	LXI	D,MessageInvaders		; "SPACE  INVADERS" message
L_0B0B:
	CALL	L_0ACF				; {} Print to middle-ish of screen
	CALL	OneSecDelay			; {code.OneSecDelay} One second delay
	CALL	DrawAdvTable		; {code.DrawAdvTable} Draw "SCORE ADVANCE TABLE" with print delay
	CALL	TwoSecDelay			; {code.TwoSecDelay} Two second delay
	LDA	0x20EC					; {ram.splashAnimate} Do splash ...
	ANA	A						; ... animations?
	JNZ	L_0B4A					; {} Not 0 ... no animations
	;
	; Animate small alien replacing upside-down Y with correct Y
	LXI	D,0x1A95				; Animate sprite from Y=FE to Y=9E step -1
	CALL	IniSplashAni		; {code.IniSplashAni} Copy to splash-animate structure
	CALL	Animate				; {code.Animate} Wait for ISR to move sprite (small alien)
	LXI	D,0x1BB0				; Animate sprite from Y=98 to Y=FF step 1
	CALL	IniSplashAni		; {code.IniSplashAni} Copy to splash-animate structure
	CALL	Animate				; {code.Animate} Wait for ISR to move sprite (alien pulling upside down Y)
	CALL	OneSecDelay			; {code.OneSecDelay} One second delay
	LXI	D,0x1FC9				; Animate sprite from Y=FF to Y=97 step 1
	CALL	IniSplashAni		; {code.IniSplashAni} Copy to splash-animate structure
	CALL	Animate				; {code.Animate} Wait for ISR to move sprite (alien pushing Y)
	CALL	OneSecDelay			; {code.OneSecDelay} One second delay
	LXI	H,0x33B7				; Where the splash alien ends up
	MVI	B,0x0A					; 10 rows
	CALL	ClearSmallSprite	; {code.ClearSmallSprite} Clear a one byte sprite at HL
	CALL	TwoSecDelay			; {code.TwoSecDelay} Two second delay
	;
	; Play demo
L_0B4A:
	CALL	ClearPlayField		; {code.ClearPlayField} Clear playfield
	LDA	0x21FF					; {ram.p1ShipsRem} Number of ships for player-1
	ANA	A						; If non zero ...
	JNZ	L_0B5D					; {} ... keep it (counts down between demos)
	CALL	GetShipsPerCred		; {code.GetShipsPerCred} Get number of ships from DIP settings
	STA	0x21FF					; {ram.p1ShipsRem} Reset number of ships for player-1
	CALL	RemoveShip			; {code.RemoveShip} Remove a ship from stash and update indicators
	;
L_0B5D:
	CALL	CopyRAMMirror		; {code.CopyRAMMirror} Block copy ROM mirror to initialize RAM
	CALL	InitAliens			; {code.InitAliens} Initialize all player 1 aliens
	CALL	DrawShieldPl1		; {code.DrawShieldPl1} Draw shields for player 1 (to buffer)
	CALL	RestoreShields1		; {code.RestoreShields1} Restore shields for player 1 (to screen)
	MVI	A,0x01					; ISR splash-task ...
	STA	0x20C1					; {ram.isrSplashTask} ... playing demo
	CALL	DrawBottomLine		; {code.DrawBottomLine} Draw playfield line
	;
L_0B71:
	CALL	PlrFireOrDemo		; {code.PlrFireOrDemo} In demo ... process demo movement and always fire
	CALL	L_0BF1				; {} Check player shot and aliens bumping edges of screen and hidden message
	OUT	0x06					; {hard.WATCHDOG} Feed watchdog
	CALL	L_0A59				; {} Has demo player been hit?
	JZ	L_0B71					; {} No ... continue game
	XRA	A						; Remove player shot ...
	STA	0x2025					; {ram.plyrShotStatus} ... from activity
L_0B83:
	CALL	L_0A59				; {} Wait for demo player ...
	JNZ	L_0B83					; {} ... to stop exploding
	;
	; Credit information
L_0B89:
	XRA	A						; Turn off ...
	STA	0x20C1					; {ram.isrSplashTask} ... splash animation
	CALL	OneSecDelay			; {code.OneSecDelay} One second delay
	CALL	L_1988				; {} ** Something else at one time? Jump straight to clear-play-field
	MVI	C,0x0C					; Message size
	LXI	H,0x2C11				; Screen coordinates
	LXI	D,MessageCoin			; "INSERT  COIN"
	CALL	PrintMessage		; {code.PrintMessage} Print message
	LDA	0x20EC					; {ram.splashAnimate} Do splash ...
	CPI	0x00					; ... animations?
	JNZ	L_0BAE					; {} Not 0 ... not on this screen
	LXI	H,0x3311				; Screen coordinates
	MVI	A,0x02					; Character "C"
	CALL	DrawChar			; {code.DrawChar} Put an extra "C" for "CCOIN" on the screen
L_0BAE:
	LXI	B,CreditTable			; "<1 OR 2 PLAYERS>  "
	CALL	ReadPriStruct		; {code.ReadPriStruct} Load the screen,pointer
	CALL	L_184C				; {} Print the message
	IN	0x02					; {hard.INP2} Display coin info (bit 7) ...
	RLC							; ... on demo screen?
	JC	L_0BC3					; {} 1 means no ... skip it
	LXI	B,0x1FA0				; "*1 PLAYER  1 COIN "
	CALL	L_183A				; {} Load the descriptor
L_0BC3:
	CALL	TwoSecDelay			; {code.TwoSecDelay} Print TWO descriptors worth
	LDA	0x20EC					; {ram.splashAnimate} Doing splash ...
	CPI	0x00					; ... animation?
	JNZ	L_0BDA					; {} Not 0 ... not on this screen
	LXI	D,0x1FD5				; Animation for small alien to line up with extra "C"
	CALL	IniSplashAni		; {code.IniSplashAni} Copy the animation block
	CALL	Animate				; {code.Animate} Wait for the animation to complete
	CALL	L_189E				; {} Animate alien shot to extra "C"
L_0BDA:
	LXI	H,0x20EC				; Toggle ...
	MOV	A,M						; ... the ...
	INR	A						; ... splash screen ...
	ANI	0x01					; ... animation for ...
	MOV	M,A						; ... next time
	CALL	ClearPlayField		; {code.ClearPlayField} Clear play field
	JMP	L_18DF					; {} Keep splashing
L_0BE8:
	LXI	D,MessagePlayY			; "PLAY" with normal 'Y'
	CALL	PrintMessageDel		; {code.PrintMessageDel} Print it
	JMP	L_0B0B					; {} Continue with splash (HL will be pointing to next message)
L_0BF1:
	CALL	PlyrShotAndBump		; {code.PlyrShotAndBump} Check if player is shot and aliens bumping the edge of screen
	JMP	CheckHiddenMes			; {code.CheckHiddenMes} Check for hidden-message display sequence
	; "TAITO COP"
MessageCorp:
	DB	0x13, 0x00, 0x08, 0x13, 0x0E, 0x26, 0x02, 0x0E, 0x0F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
	;1000: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1040: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;10A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;10C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;10E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1100: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1120: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1140: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1160: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;11A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;11C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;11E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1200: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1220: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1240: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1260: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1280: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;12A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;12C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;12E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1300: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1320: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1340: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1360: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;1380: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;13A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;13C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	;13E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	; The only differences between this and EraseSimpleSprite is two CPL instructions in the latter and
	; the use of AND instead of OR. NOP takes the same amount of time/space as CPL. So the two NOPs
	; here make these two parallel routines the same size and speed.
	;
DrawShiftedSprite:
	DB	0x00, 0xCD, 0x74, 0x14, 0x00, 0xC5, 0xE5, 0x1A, 0xD3, 0x04, 0xDB, 0x03, 0xB6, 0x77, 0x23, 0x13	; Time/size pad to match CPL in EraseShiftedSprite
	DB	0xAF, 0xD3, 0x04, 0xDB, 0x03, 0xB6, 0x77, 0xE1, 0x01, 0x20, 0x00, 0x09, 0xC1, 0x05, 0xC2, 0x05
	DB	0x14, 0xC9, 0x00, 0x00
	; Clear a sprite from the screen (standard pixel number descriptor).
	; ** We clear 2 bytes even though the draw-simple only draws one.
EraseSimpleSprite:
	CALL	CnvtPixNumber		; {code.CnvtPixNumber} Convert pixel number in HL
L_1427:
	PUSH	B					; Hold
	PUSH	H					; Hold
	XRA	A						; 0
	MOV	M,A						; Clear screen byte
	INX	H						; Next byte
	MOV	M,A						; Clear byte
	INX	H						; ** Is this to mimic timing? We increment then pop
	POP	H						; Restore screen coordinate
	LXI	B,L_0020				; Add 1 row ...
	DAD	B						; ... to screen coordinate
	POP	B						; Restore counter
	DCR	B						; All rows done?
	JNZ	L_1427					; {} Do all rows
	RET							; out
	; Display character to screen
	; HL = screen coordinates
	; DE = character data
	; B = number of rows
DrawSimpSprite:
	PUSH	B					; Preserve counter
	LDAX	D					; From character set ...
	MOV	M,A						; ... to screen
	INX	D						; Next in character set
	LXI	B,L_0020				; Next row ...
	DAD	B						; ... on screen
	POP	B						; Restore counter
	DCR	B						; Decrement counter
	JNZ	DrawSimpSprite			; {code.DrawSimpSprite} Do all
	RET							; Out
D_1447:
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00	; ** Why?
	; Erases a shifted sprite from screen (like for player's explosion)
EraseShifted:
	DB	0xCD, 0x74, 0x14, 0xC5, 0xE5, 0x1A, 0xD3, 0x04, 0xDB, 0x03, 0x2F, 0xA6, 0x77, 0x23, 0x13, 0xAF	; {code.CnvtPixNumber} Convert pixel number in HL to coorinates with shift
	DB	0xD3, 0x04, 0xDB, 0x03, 0x2F, 0xA6, 0x77, 0xE1, 0x01, 0x20, 0x00, 0x09, 0xC1, 0x05, 0xC2, 0x55
	DB	0x14, 0xC9
	; Convert pixel number in HL to screen coordinate and shift amount.
	; HL gets screen coordinate.
	; Hardware shift-register gets amount.
CnvtPixNumber:
	MOV	A,L						; Get X coordinate
	ANI	0x07					; Shift by pixel position
	OUT	0x02					; {hard.SHFTAMNT} Write shift amount to hardware
	JMP	ConvToScr				; {code.ConvToScr} HL = HL/8 + 2000 (screen coordinate)
	; In a multi-player game the player's shields are block-copied to and from RAM between turns.
	; HL = screen pointer
	; DE = memory buffer
	; B = number of rows
	; C = number of columns
RememberShields:
	PUSH	B					; Hold counter
	PUSH	H					; Hold start
L_147E:
	MOV	A,M						; From sprite ... (should be DE)
	STAX	D					; ... to screen ... (should be HL)
	INX	D						; Next in sprite
	INX	H						; Next on screen
	DCR	C						; All columns done?
	JNZ	L_147E					; {} No ... do multi columns
	POP	H						; Restore screen start
	LXI	B,L_0020				; Add 32 ...
	DAD	B						; ... to get to next row
	POP	B						; Pop the counters
	DCR	B						; All rows done?
	JNZ	RememberShields			; {code.RememberShields} No ... do multi rows
	RET							; Done
DrawSprCollision:
	DB	0xCD, 0x74, 0x14, 0xAF, 0x32, 0x61, 0x20, 0xC5, 0xE5, 0x1A, 0xD3, 0x04, 0xDB, 0x03, 0xF5, 0xA6	; {code.CnvtPixNumber} Convert pixel number to coord and shift
	DB	0xCA, 0xA9, 0x14, 0x3E, 0x01, 0x32, 0x61, 0x20, 0xF1, 0xB6, 0x77, 0x23, 0x13, 0xAF, 0xD3, 0x04
	DB	0xDB, 0x03, 0xF5, 0xA6, 0xCA, 0xBD, 0x14, 0x3E, 0x01, 0x32, 0x61, 0x20, 0xF1, 0xB6, 0x77, 0xE1
	DB	0x01, 0x20, 0x00, 0x09, 0xC1, 0x05, 0xC2, 0x98, 0x14, 0xC9
	; Clear a one byte sprite at HL. B=number of rows.
ClearSmallSprite:
	XRA	A						; 0
L_14CC:
	PUSH	B					; Preserve BC
	MOV	M,A						; Clear screen byte
	LXI	B,L_0020				; Bump HL ...
	DAD	B						; ... one screen row
	POP	B						; Restore
	DCR	B						; All done?
	JNZ	L_14CC					; {} No ... clear all
	RET
	; The player's shot hit something (or is being removed from play)
	;
PlayerShotHit:
	LDA	0x2025					; {ram.plyrShotStatus} Player shot flag
	CPI	0x05					; Alien explosion in progress?
	RZ							; Yes ... ignore this function
	CPI	0x02					; Normal movement?
	RNZ							; No ... out
	;
	LDA	0x2029					; {ram.obj1CoorYr} Get Yr coordinate of player shot
	CPI	0xD8					; Compare to 216 (40 from Top-rotated)
	MOV	B,A						; Hold value for later
	JNC	L_1530					; {} Yr is within 40 from top initiate miss-explosion (shot flag 3)
	LDA	0x2002					; {ram.alienIsExploding} Is an alien ...
	ANA	A						; ... blowing up?
	RZ							; No ... out
	;
	MOV	A,B						; Get original Yr coordinate back to A
	CPI	0xCE					; Compare to 206 (50 from rotated top)
	JNC	L_1579					; {} Yr is within 50 from top? Yes ... saucer must be hit
	ADI	0x06					; Offset to coordinate for wider "explosion" picture
	MOV	B,A						; Hold that
	LDA	0x2009					; {ram.refAlienYr} Ref alien Y coordianate
	; If the lower 4 rows are all empty then the reference alien's Y coordinate will wrap around from 0 to F8.
	; At this point the top row of aliens is in the shields and we will assume that everything is within
	; the rack.
	CPI	0x90					; This is true if ...
	JNC	CodeBug1				; {code.CodeBug1} ... aliens are down in the shields
	CMP	B						; Compare to shot's coordinate
	JNC	L_1530					; {} Outside the rack-square ... do miss explosion
	;
	; We get here if the player's shot hit something within the rack area (a shot or an alien).
	; Find the alien that is (or would be) where the shot hit. If there is no alien alive at the row/column
	; thn the player hit an alien missile. If there is an alien then explode the alien.
	;
	; There is a code bug here, but it is extremely subtle. The algorithm for finding the row/column in the
	; rack works by adding 16 to the reference coordinates (X for column, Y for row) until it passes or equals
	; the target coordinates. This works great as long as the target point is within the alien's rack area.
	; If the reference point is far to the right, the column number will be greater than 11, which messes
	; up the column/row-to-pointer math.
	;
	; The entire rack of aliens is based on the lower left alien. Imagine all aliens are dead except the
	; upper left. It wiggles down the screen and enters the players shields on the lower left where it begins
	; to eat them. Imagine the player is under his own shields on the right side of the screen and fires a
	; shot into his own shield.
	;
	; The alien is in the rack on row 4 (rows are numbered from bottom up starting with 0). The shot hits
	; the shields below the alien's Y coordinate and gets correctly assigned to row 3. The alien is in the rack
	; at column 0 (columns are numbered from left to right starting with 0). The shot hits the shields far to
	; the right of the alien's X coordinate. The algorithm says it is in column 11. But 0-10 are the only
	; correct values.
	;
	; The column/row-to-pointer math works by multiplying the row by 11 and adding the column. For the alien
	; that is 11*4 + 0 = 44. For the shot that is 11*3 +11 = 44. The game thinks the shot hit the alien.
	;
CodeBug1:
	MOV	L,B						; L now holds the shot coordinate (adjusted)
	CALL	FindRow				; {code.FindRow} Look up row number to B
	LDA	0x202A					; {ram.obj1CoorXr} Player's shot's Xr coordinate ...
	MOV	H,A						; ... to H
	CALL	FindColumn			; {code.FindColumn} Get alien's coordinate
	SHLD	0x2064				; {ram.expAlienYr} Put it in the exploding-alien descriptor
	MVI	A,0x05					; Flag alien explosion ...
	STA	0x2025					; {ram.plyrShotStatus} ... in progress
	CALL	GetAlienStatPtr		; {code.GetAlienStatPtr} Get descriptor for alien
	MOV	A,M						; Is alien ...
	ANA	A						; ... alive
	JZ	L_1530					; {} No ... must have been an alien shot
	;
	MVI	M,0x00					; Make alien invader dead
	CALL	ScoreForAlien		; {code.ScoreForAlien} Makes alien explosion sound and adjust score
	CALL	ReadDesc			; {code.ReadDesc} Load 5 byte sprite descriptor
	CALL	DrawSprite			; {code.DrawSprite} Draw explosion sprite on screen
	MVI	A,0x10					; Initiate alien-explosion
	STA	0x2003					; {ram.expAlienTimer} ... timer to 16
	RET							; Out
	;
	; Player shot leaving playfield, hitting shield, or hitting an alien shot
L_1530:
	MVI	A,0x03					; Mark ...
	STA	0x2025					; {ram.plyrShotStatus} ... player shot hit something other than alien
	JMP	L_154A					; {} Finish up
	;
	; Time down the alien explosion. Remove when done.
AExplodeTime:
	LXI	H,0x2003				; Decrement alien explosion ...
	DCR	M						; ... timer
	RNZ							; Not done  ... out
	LHLD	0x2064				; {ram.expAlienYr} Pixel pointer for exploding alien
	MVI	B,0x10					; 16 row pixel
	CALL	EraseSimpleSprite	; {code.EraseSimpleSprite} Clear the explosion sprite from the screen
L_1545:
	MVI	A,0x04					; 4 means that ...
	STA	0x2025					; {ram.plyrShotStatus} ... alien has exploded (remove from active duty)
	;
L_154A:
	XRA	A						; Turn off ...
	STA	0x2002					; {ram.alienIsExploding} ... alien-is-blowing-up flag
	MVI	B,0xF7					; Turn off ...
	JMP	SoundBits3Off			; {code.SoundBits3Off} ... alien exploding sound
D_1553:
	DB	0x00
	; Count number of 16s needed to bring reference (in A) up to target (in H).
	; If the reference starts out beyond the target then we add 16s as long as
	; the reference has a signed bit. But these aren't signed quantities. This
	; doesn't make any sense. This counting algorithm produces questionable
	; results if the reference is beyond the target.
	;
Cnt16s:
	MVI	C,0x00					; Count of 16s
	CMP	H						; Compare reference coordinate to target
	CNC	WrapRef					; {code.WrapRef} If reference is greater or equal then do something questionable ... see below
L_155A:
	CMP	H						; Compare reference coordinate to target
	RNC							; If reference is greater or equal then done
	ADI	0x10					; Add 16 to reference
	INR	C						; Bump 16s count
	JMP	L_155A					; {} Keep testing
	; L contains a Yr coordinate. Find the row number within the rack that corresponds
	; to the Yr coordinate. Return the row coordinate in L and the row number in C.
	;
FindRow:
	LDA	0x2009					; {ram.refAlienYr} Reference alien Yr coordinate
	MOV	H,L						; Target Yr coordinate to H
	CALL	Cnt16s				; {code.Cnt16s} Count 16s needed to bring ref alien to target
	MOV	B,C						; Count to B
	DCR	B						; Base 0
	SBI	0x10					; The counting also adds 16 no matter what
	MOV	L,A						; To coordinate
	RET							; Done
	; H contains a Xr coordinate. Find the column number within the rack that corresponds
	; to the Xr coordinate. Return the column coordinate in H and the column number in C.
	;
FindColumn:
	LDA	0x200A					; {ram.refAlienXr} Reference alien Yn coordinate
	CALL	Cnt16s				; {code.Cnt16s} Count 16s to bring Y to target Y
	SBI	0x10					; Subtract off extra 16
	MOV	H,A						; To H
	RET							; Done
L_1579:
	MVI	A,0x01					; Mark flying ...
	STA	0x2085					; {ram.saucerHit} ... saucer has been hit
	JMP	L_1545					; {} Remove player shot
	; B is row number. C is column number (starts at 1).
	; Return pointer to alien-status flag for current player.
GetAlienStatPtr:
	MOV	A,B						; Hold original
	RLC							; *2
	RLC							; *4
	RLC							; *8
	ADD	B						; *9
	ADD	B						; *10
	ADD	B						; *11
	ADD	C						; Add row offset to column offset
	DCR	A						; -1
	MOV	L,A						; Set LSB of HL
	LDA	0x2067					; {ram.playerDataMSB} Set ...
	MOV	H,A						; ... MSB of HL with active player indicator
	RET
	; This is called if the reference point is greater than the target point. I believe the goal is to
	; wrap the reference back around until it is lower than the target point. But the algorithm simply adds
	; until the sign bit of the the reference is 0. If the target is 2 and the reference is 238 then this
	; algorithm moves the reference 238+16=244 then 244+16=4. Then the algorithm stops. But the reference is
	; STILL greater than the target.
	;
	; Also imagine that the target is 20 and the reference is 40. The algorithm adds 40+16=56, which is not
	; negative, so it stops there.
	;
	; I think the intended code is "JP NC" instead of "JP M", but even that doesn't make sense.
	;
WrapRef:
	INR	C						; Increase 16s count
	ADI	0x10					; Add 16 to ref
	JM	WrapRef					; {code.WrapRef} Keep going till result is positive
	RET							; Out
	; When rack bumps the edge of the screen then the direction flips and the rack
	; drops 8 pixels. The deltaX and deltaY values are changed here. Interestingly
	; if there is only one alien left then the right value is 3 instead of the
	; usual 2. The left direction is always -2.
RackBump:
	LDA	0x200D					; {ram.rackDirection} Get rack direction
	ANA	A						; Moving right?
	JNZ	L_15B7					; {} No ... handle moving left
	;
	LXI	H,0x3EA4				; Line down the right edge of playfield
	CALL	L_15C5				; {} Check line down the edge
	RNC							; Nothing is there ... return
	MVI	B,0xFE					; Delta X of -2
	MVI	A,0x01					; Rack now moving right
	;
L_15A9:
	STA	0x200D					; {ram.rackDirection} Set new rack direction
	MOV	A,B						; B has delta X
	STA	0x2008					; {ram.refAlienDXr} Set new delta X
	LDA	0x200E					; {ram.rackDownDelta} Set delta Y ...
	STA	0x2007					; {ram.refAlienDYr} ... to drop rack by 8
	RET							; Done
	;
L_15B7:
	LXI	H,0x2524				; Line down the left edge of playfield
	CALL	L_15C5				; {} Check line down the edge
	RNC							; Nothing is there ... return
	CALL	L_18F1				; {} Get moving-right delta X value of 2 (3 if just one alien left)
	XRA	A						; Rack now moving left
	JMP	L_15A9					; {} Set rack direction
	;
L_15C5:
	MVI	B,0x17					; Checking 23 bytes in a line up the screen from near the bottom
L_15C7:
	MOV	A,M						; Get screen memory
	ANA	A						; Is screen memory empty?
	JNZ	L_166B					; {} No ... set carry flag and out
	INX	H						; Next byte on screen
	DCR	B						; All column done?
	JNZ	L_15C7					; {} No ... keep looking
	RET							; Return with carry flag clear
D_15D2:
	DB	0x00					; ** Why? Something optimized?
	; Draw sprite at [DE] to screen at pixel position in HL
	; The hardware shift register is used in converting pixel positions
	; to screen coordinates.
DrawSprite:
	CALL	CnvtPixNumber		; {code.CnvtPixNumber} Convert pixel number to screen/shift
	PUSH	H					; Preserve screen coordinate
L_15D7:
	PUSH	B					; Hold for a second
	PUSH	H					; Hold for a second
	LDAX	D					; From sprite data
	OUT	0x04					; {hard.SHFT_DATA} Write data to shift register
	IN	0x03					; {hard.SHFT_IN} Read back shifted amount
	MOV	M,A						; Shifted sprite to screen
	INX	H						; Adjacent cell
	INX	D						; Next in sprite data
	XRA	A						; 0
	OUT	0x04					; {hard.SHFT_DATA} Write 0 to shift register
	IN	0x03					; {hard.SHFT_IN} Read back remainder of previous
	MOV	M,A						; Write remainder to adjacent
	POP	H						; Old screen coordinate
	LXI	B,L_0020				; Offset screen ...
	DAD	B						; ... to next row
	POP	B						; Restore count
	DCR	B						; All done?
	JNZ	L_15D7					; {} No ... do all
	POP	H						; Restore HL
	RET							; Done
	; Count number of aliens remaining in active game and return count 2082 holds the current count.
	; If only 1, 206B gets a flag of 1 ** but ever nobody checks this
CountAliens:
	CALL	GetPlayerDataPtr	; {code.GetPlayerDataPtr} Get active player descriptor
	LXI	B,0x3700				; B=55 aliens to check?
L_15F9:
	MOV	A,M						; Get byte
	ANA	A						; Is it a zero?
	JZ	L_15FF					; {} Yes ... don't count it
	INR	C						; Count the live aliens
L_15FF:
	INX	H						; Next alien
	DCR	B						; Count ...
	JNZ	L_15F9					; {} ... all alien indicators
	MOV	A,C						; Get the count
	STA	0x2082					; {ram.numAliens} Hold it
	CPI	0x01					; Just one?
	RNZ							; No keep going
	LXI	H,0x206B				; Set flag if ...
	MVI	M,0x01					; ... only one alien left
	RET							; Out
	; Set HL with 2100 if player 1 is active or 2200 if player 2 is active
	;
GetPlayerDataPtr:
	MVI	L,0x00					; Byte boundary
	LDA	0x2067					; {ram.playerDataMSB} Active player number
	MOV	H,A						; Set HL to data
	RET							; Done
	; Initiate player fire if button is pressed.
	; Demo commands are parsed here if in demo mode
PlrFireOrDemo:
	LDA	0x2015					; {ram.playerAlive} Is there an active player?
	CPI	0xFF					; FF = alive
	RNZ							; Player has been shot - no firing
	LXI	H,0x2010				; Get player ...
	MOV	A,M						; ... task ...
	INX	H						; ... timer ...
	MOV	B,M						; ... value
	ORA	B						; Is the timer 0 (object active)?
	RNZ							; No ... no firing till player object starts
	LDA	0x2025					; {ram.plyrShotStatus} Does the player have ...
	ANA	A						; ... a shot on the screen?
	RNZ							; Yes ... ignore
	LDA	0x20EF					; {ram.gameMode} Are we in ...
	ANA	A						; ... game mode?
	JZ	L_1652					; {} No ... in demo mode ... constant firing in demo
	LDA	0x202D					; {ram.fireBounce} Is fire button ...
	ANA	A						; ... being held down?
	JNZ	L_1648					; {} Yes ... wait for bounce
	CALL	ReadInputs			; {code.ReadInputs} Read active player controls
	ANI	0x10					; Fire-button pressed?
	RZ							; No ... out
	MVI	A,0x01					; Flag
	STA	0x2025					; {ram.plyrShotStatus} Flag shot active
	STA	0x202D					; {ram.fireBounce} Flag that fire button is down
	RET							; Out
L_1648:
	CALL	ReadInputs			; {code.ReadInputs} Read active player controls
	ANI	0x10					; Fire-button pressed?
	RNZ							; Yes ... ignore
	STA	0x202D					; {ram.fireBounce} Else ... clear flag
	RET							; Out
	; Handle demo (constant fire, parse demo commands)
L_1652:
	LXI	H,0x2025				; Demo fires ...
	MVI	M,0x01					; ... constantly
	LHLD	0x20ED				; {ram.demoCmdPtrLSB} Demo command bufer
	INX	H						; Next position
	MOV	A,L						; Command buffer ...
	CPI	0x7E					; ... wraps around
	JC	L_1663					; {} ... Buffer from 1F74 to 1F7E
	MVI	L,0x74					; ... overflow
L_1663:
	SHLD	0x20ED				; {ram.demoCmdPtrLSB} Next demo command
	MOV	A,M						; Get next command
	STA	0x201D					; {ram.nextDemoCmd} Set command for movement
	RET							; Done
L_166B:
	STC							; Set carry flag
	RET							; Done
D_166D:
	DB	0xAF, 0xCD, 0x8B, 0x1A	; 0
L_1671:
	CALL	CurPlyAlive			; {code.CurPlyAlive} Get active-flag ptr for current player
	MVI	M,0x00					; Flag player is dead
	CALL	L_09CA				; {} Get score descriptor for current player
	INX	H						; Point to high two digits
	LXI	D,0x20F5				; Current high score upper two digits
	LDAX	D					; Is player score greater ...
	CMP	M						; ... than high score?
	DCX	D						; Point to LSB
	DCX	H						; Point to LSB
	LDAX	D					; Go ahead and fetch high score lower two digits
	JZ	L_168B					; {} Upper two are the same ... have to check lower two
	JNC	L_1698					; {} Player score is lower than high ... nothing to do
	JMP	L_168F					; {} Player socre is higher ... go copy the new high score
	;
L_168B:
	CMP	M						; Is lower digit higher? (upper was the same)
	JNC	L_1698					; {} No ... high score is still greater than player's score
L_168F:
	MOV	A,M						; Copy the new ...
	STAX	D					; ... high score lower two digits
	INX	D						; Point to MSB
	INX	H						; Point to MSB
	MOV	A,M						; Copy the new ...
	STAX	D					; ... high score upper two digits
	CALL	PrintHiScore		; {code.PrintHiScore} Draw the new high score
L_1698:
	LDA	0x20CE					; {ram.twoPlayers} Number of players
	ANA	A						; Is this a single player game?
	JZ	L_16C9					; {} Yes ... short message
	LXI	H,0x2803				; Screen coordinates
	LXI	D,MessageGOver			; "GAME OVER PLAYER< >"
	MVI	C,0x14					; 20 characters
	CALL	PrintMessageDel		; {code.PrintMessageDel} Print message
	DCR	H						; Back up ...
	DCR	H						; ... to player indicator
	MVI	B,0x1B					; "1"
	LDA	0x2067					; {ram.playerDataMSB} Player number
	RRC							; Is this player 1?
	JC	L_16B7					; {} Yes ... keep the digit
	MVI	B,0x1C					; Else ... set digit 2
L_16B7:
	MOV	A,B						; To A
	CALL	DrawChar			; {code.DrawChar} Print player number
	CALL	OneSecDelay			; {code.OneSecDelay} Short delay
	CALL	L_18E7				; {} Get current player "alive" flag
	MOV	A,M						; Is player ...
	ANA	A						; ... alive?
	JZ	L_16C9					; {} No ... skip to "GAME OVER" sequence
	JMP	L_02ED					; {} Switch players and game loop
	;
L_16C9:
	LXI	H,0x2D18				; Screen coordinates
	LXI	D,MessageGOver			; "GAME OVER PLAYER< >"
	MVI	C,0x0A					; Just the "GAME OVER" part
	CALL	PrintMessageDel		; {code.PrintMessageDel} Print message
	CALL	TwoSecDelay			; {code.TwoSecDelay} Long delay
	CALL	ClearPlayField		; {code.ClearPlayField} Clear center window
	XRA	A						; Now in ...
	STA	0x20EF					; {ram.gameMode} ... demo mode
	OUT	0x05					; {hard.SOUND2} All sound off
	CALL	EnableGameTasks		; {code.EnableGameTasks} Enable ISR game tasks
	JMP	L_0B89					; {} Print credit information and do splash
L_16E6:
	LXI	SP,0x2400				; Reset stack
	EI							; Enable interrupts
	XRA	A						; Flag ...
	STA	0x2015					; {ram.playerAlive} ... player is shot
L_16EE:
	CALL	PlayerShotHit		; {code.PlayerShotHit} Player's shot collision detection
	MVI	B,0x04					; Player has been hit ...
	CALL	SoundBits3On		; {code.SoundBits3On} ... sound
	CALL	L_0A59				; {} Has flag been set?
	JNZ	L_16EE					; {} No ... wait for the flag
	CALL	DsableGameTasks		; {code.DsableGameTasks} Disable ISR game tasks
	LXI	H,0x2701				; Player's stash of ships
	CALL	L_19FA				; {} Erase the stash of shps
	XRA	A						; Print ...
	CALL	L_1A8B				; {} ... a zero (number of ships)
	MVI	B,0xFB					; Turn off ...
	JMP	L_196B					; {} ... player shot sound
	; Use the player's MSB to determine how fast the aliens reload their
	; shots for another fire.
AShotReloadRate:
	CALL	L_09CA				; {} Get score descriptor for active player
	INX	H						; MSB value
	MOV	A,M						; Get the MSB value
	LXI	D,AReloadScoreTab		; Score MSB table
	LXI	H,ShotReloadRate		; Corresponding fire reload rate table
	MVI	C,0x04					; Only 4 entries (a 5th value of 7 is used after that)
	MOV	B,A						; Hold the score value
L_171C:
	LDAX	D					; Get lookup from table
	CMP	B						; Compare them
	JNC	L_1727					; {} Equal or below ... use this table entry
	INX	H						; Next ...
	INX	D						; ... entry in table
	DCR	C						; Do all ...
	JNZ	L_171C					; {} ... 4 entries in the tables
L_1727:
	MOV	A,M						; Load the shot reload value
	STA	0x20CF					; {ram.aShotReloadRate} Save the value for use in shot routine
	RET							; Done
	; Shot sound on or off depending on 2025
ShotSound:
	LDA	0x2025					; {ram.plyrShotStatus} Player shot flag
	CPI	0x00					; Active shot?
	JNZ	L_1739					; {} Yes ... go
	MVI	B,0xFD					; Sound mask
	JMP	SoundBits3Off			; {code.SoundBits3Off} Mask off sound
	;
L_1739:
	MVI	B,0x02					; Sound bit
	JMP	SoundBits3On			; {code.SoundBits3On} OR on sound
D_173E:
	DB	0x00, 0x00				; ** Why?
	; This called from the ISR times down the fleet and sets the flag at 2095 if
	; the fleet needs a change in sound handling (new delay, new sound)
TimeFleetSound:
	LXI	H,0x209B				; Pointer to hold time for fleet
	DCR	M						; Decrement hold time
	CZ	L_176D					; {} If 0 turn fleet movement sound off
	LDA	0x2068					; {ram.playerOK} Is player OK?
	ANA	A						; 1  means OK
	JZ	L_176D					; {} Player not OK ... fleet movement sound off and out
	LXI	H,0x2096				; Current time on fleet sound
	DCR	M						; Count down
	RNZ							; Not time to change sound ... out
	LXI	H,0x2098				; Current sound port 3 value
	MOV	A,M						; Get value
	OUT	0x05					; {hard.SOUND2} Set sounds
	LDA	0x2082					; {ram.numAliens} Number of aliens on active screen
	ANA	A						; Is it zero?
	JZ	L_176D					; {} Yes ... turn off fleet movement sound and out
	DCX	H						; (2097) Point to fleet timer reload
	MOV	A,M						; Get fleet delay value
	DCX	H						; (2096) Point to fleet timer
	MOV	M,A						; Reload the timer
	DCX	H						; Point to change-sound
	MVI	M,0x01					; (2095) time to change sound
	MVI	A,0x04					; Set hold ...
	STA	0x209B					; {ram.fleetSndHold} ... time for fleet sound
	RET							; Done
L_176D:
	LDA	0x2098					; {ram.soundPort5} Current sound port 3 value
	ANI	0x30					; Mask off fleet movement sounds
	OUT	0x05					; {hard.SOUND2} Set sounds
	RET							; Out
	; This game-loop routine handles two sound functions. The routine does:
	; 1) Time out the extra-ship awarded sound and turn it off when done
	; 2) Load the fleet sound delay based on number of remaining aliens
	; 3) Make the changing fleet sound
	;
	; The 2095 flag is set by the ISR and cleared here. The ISR does the timing and sets 2095 when it
	; is time to make a new fleet sound.
	;
FleetDelayExShip:
	LDA	0x2095					; {ram.changeFleetSnd} Time for new ...
	ANA	A						; ... fleet movement sound?
	JZ	L_17AA					; {} No ... skip to extra-man timing
	LXI	H,0x1A11				; Number of aliens list coupled ...
	LXI	D,0x1A21				; ... with delay list
	LDA	0x2082					; {ram.numAliens} Get the number of aliens on the screen
L_1785:
	CMP	M						; Compare it to the first list value
	JNC	L_178E					; {} Number of live aliens is higher than value ... use the delay
	INX	H						; Move to ...
	INX	D						; ... next list value
	JMP	L_1785					; {} Find the right delay
L_178E:
	LDAX	D					; Get the delay from the second list
	STA	0x2097					; {ram.fleetSndReload} Store the new alien sound delay
	LXI	H,0x2098				; Get current state ...
	MOV	A,M						; ... of sound port
	ANI	0x30					; Mask off all fleet movement sounds
	MOV	B,A						; Hold the value
	MOV	A,M						; Get current state
	ANI	0x0F					; This time ONLY the fleet movement sounds
	RLC							; Shift next to next sound
	CPI	0x10					; Overflow?
	JNZ	L_17A4					; {} No ... keep it
	MVI	A,0x01					; Reset back to first sound
L_17A4:
	ORA	B						; Add fleet sounds to current sound value
	MOV	M,A						; Store new sound value
	XRA	A						; Restart ...
	STA	0x2095					; {ram.changeFleetSnd} ... waiting on fleet time
	;
L_17AA:
	LXI	H,0x2099				; Sound timer for award extra ship
	DCR	M						; Time expired?
	RNZ							; No ... leave sound playing
	MVI	B,0xEF					; Turn off bit set with #$10 (award extra ship)
	JMP	SoundBits3Off			; {code.SoundBits3Off} Stop sound and out
SndOffExtPly:
	DB	0x06, 0xEF, 0x21, 0x98, 0x20, 0x7E, 0xA0, 0x77, 0xD3, 0x05, 0xC9, 0x00	; Mask off sound bit 4 (Extended play)
	; Read control inputs for active player
ReadInputs:
	LDA	0x2067					; {ram.playerDataMSB} Get active player
	RRC							; Test player
	JNC	L_17CA					; {} Player 2 ... read port 2
	IN	0x01					; {hard.INP1} Player 1 ... read port 1
	RET							; Out
L_17CA:
	IN	0x02					; {hard.INP2} Get controls for player 2
	RET							; Out
	; Check and handle TILT
CheckHandleTilt:
	IN	0x02					; {hard.INP2} Read input port
	ANI	0x04					; Tilt?
	RZ							; No tilt ... return
	LDA	0x209A					; {ram.tilt} Already in TILT handle?
	ANA	A						; 1 = yes
	RNZ							; Yes ... ignore it now
	LXI	SP,0x2400				; Reset stack
	MVI	B,0x04					; Do this 4 times
L_17DC:
	CALL	ClearPlayField		; {code.ClearPlayField} Clear center window
	DCR	B						; All done?
	JNZ	L_17DC					; {} No ... do again
	MVI	A,0x01					; Flag ...
	STA	0x209A					; {ram.tilt} ... handling TILT
	CALL	DsableGameTasks		; {code.DsableGameTasks} Disable game tasks
	EI							; Re-enable interrupts
	LXI	D,MessageTilt			; Message "TILT"
	LXI	H,0x3016				; Center of screen
	MVI	C,0x04					; Four letters
	CALL	PrintMessageDel		; {code.PrintMessageDel} Print "TILT"
	CALL	OneSecDelay			; {code.OneSecDelay} Short delay
	XRA	A						; Zero
	STA	0x209A					; {ram.tilt} TILT handle over
	STA	0x2093					; {ram.waitStartLoop} Back into splash screens
	JMP	L_16C9					; {} Handle game over for player
CtrlSaucerSound:
	LXI	H,0x2084				; Saucer on screen flag
	MOV	A,M						; Is the saucer ...
	ANA	A						; ... on the screen?
	JZ	L_0707					; {} No ... UFO sound off
	INX	H						; Saucer hit flag
	MOV	A,M						; (2085) Get saucer hit flag
	ANA	A						; Is saucer in "hit" sequence?
	RNZ							; Yes ... out
	MVI	B,0x01					; Retrigger saucer ...
	JMP	SoundBits3On			; {code.SoundBits3On} ... sound (retrigger makes it warble?)
	; Draw "SCORE ADVANCE TABLE"
DrawAdvTable:
	LXI	H,0x2810				; 0x410 is 1040 rotCol=32, rotRow=16
	LXI	D,MessageAdv			; "*SCORE ADVANCE TABLE*"
	MVI	C,0x15					; 21 bytes in message
	CALL	PrintMessage		; {code.PrintMessage} Print message
	MVI	A,0x0A					; 10 bytes in every "=xx POINTS" string
	STA	0x206C					; {ram.temp206C} Hold the count
	LXI	B,0x1DBE				; Coordinate/sprite for drawing table
L_1828:
	CALL	ReadPriStruct		; {code.ReadPriStruct} Get HL=coordinate, DE=image
	JC	L_1837					; {} Move on if done
	CALL	L_1844				; {} Draw 16-byte sprite
	JMP	L_1828					; {} Do all in table
	;
D_1834:
	DB	0xCD, 0xB1, 0x0A		; {code.OneSecDelay} One second delay
L_1837:
	LXI	B,AlienScoreTable		; Coordinate/message for drawing table
L_183A:
	CALL	ReadPriStruct		; {code.ReadPriStruct} Get HL=coordinate, DE=message
	RC							; Out if done
	CALL	L_184C				; {} Print message
	JMP	L_183A					; {} Do all in table
	;
L_1844:
	PUSH	B					; Hold BC
	MVI	B,0x10					; 16 bytes
	CALL	DrawSimpSprite		; {code.DrawSimpSprite} Draw simple
	POP	B						; Restore BC
	RET							; Out
	;
L_184C:
	PUSH	B					; Hold BC
	LDA	0x206C					; {ram.temp206C} Count of 10 ...
	MOV	C,A						; ... to C
	CALL	PrintMessageDel		; {code.PrintMessageDel} Print the message with delay between letters
	POP	B						; Restore BC
	RET							; Out
	; Read a 4-byte print-structure pointed to by BC
	; HL=Screen coordiante, DE=pointer to message
	; If the first byte is FF then return with Carry Set, Carry Cleared otherwise.
ReadPriStruct:
	LDAX	B					; Get the screen LSB
	CPI	0xFF					; Valid?
	STC							; If not Carry will be Set
	RZ							; Return if 255
	MOV	L,A						; Screen LSB to L
	INX	B						; Next
	LDAX	B					; Read screen MSB
	MOV	H,A						; Screen MSB to H
	INX	B						; Next
	LDAX	B					; Read message LSB
	MOV	E,A						; Message LSB to E
	INX	B						; Next
	LDAX	B					; Read message MSB
	MOV	D,A						; Message MSB to D
	INX	B						; Next (for next print)
	ANA	A						; Clear Carry
	RET							; Done
	; Moves a sprite up or down in splash mode. Interrupt moves the sprite. When it reaches
	; Y value in 20CA the flag at 20CB is raised. The image flips between two pictures every
	; 4 movements.
SplashSprite:
	LXI	H,0x20C2				; Descriptor
	INR	M						; Change image
	INX	H						; Point to delta-x
	MOV	C,M						; Get delta-x
	CALL	AddDelta			; {code.AddDelta} Add delta-X and delta-Y to X and Y
	MOV	B,A						; Current y coordinate
	LDA	0x20CA					; {ram.splashTargetY} Has sprite reached ...
	CMP	B						; ... target coordinate?
	JZ	L_1898					; {} Yes ... flag and out
	LDA	0x20C2					; {ram.splashAnForm} Image number
	ANI	0x04					; Watching bit 3 for flip delay
	LHLD	0x20CC				; {ram.splashImRestLSB} Image
	JNZ	L_1888					; {} Did bit 3 go to 0? No ... keep current image
	LXI	D,L_0030				; 16*3 ...
	DAD	D						; ...  use other image form
L_1888:
	SHLD	0x20C7				; {ram.splashImageLSB} Image to descriptor structure
	LXI	H,0x20C5				; X,Y,Image descriptor
	CALL	ReadDesc			; {code.ReadDesc} Read sprite descriptor
	XCHG						; Image to DE, position to HL
	JMP	DrawSprite				; {code.DrawSprite} Draw the sprite
D_1895:
	DB	0x00, 0x00, 0x00
L_1898:
	MVI	A,0x01					; Flag that sprite ...
	STA	0x20CB					; {ram.splashReached} ... reached location
	RET							; Out
	;Animate alien shot to extra "C" in splash
L_189E:
	LXI	H,0x2050				; Task descriptor for game object 4 (squiggly shot)
	LXI	D,0x1BC0				; Task info for animate-shot-to-extra-C
	MVI	B,0x10					; Block copy ...
	CALL	BlockCopy			; {code.BlockCopy} ... 16 bytes
	MVI	A,0x02					; Set shot sync ...
	STA	0x2080					; {ram.shotSync} ... to run the squiggly shot
	MVI	A,0xFF					; Shot direction (-1)
	STA	0x207E					; {ram.alienShotDelta} Alien shot delta
	MVI	A,0x04					; Animate ...
	STA	0x20C1					; {ram.isrSplashTask} ... shot
L_18B8:
	LDA	0x2055					; {ram.squShotStatus} Has shot ...
	ANI	0x01					; ... collided?
	JZ	L_18B8					; {} No ... keep waiting
L_18C0:
	LDA	0x2055					; {ram.squShotStatus} Wait ...
	ANI	0x01					; ... for explosion ...
	JNZ	L_18C0					; {} ... to finish
	LXI	H,0x3311				; Here is where the extra C is
	MVI	A,0x26					; Space character
	NOP							; ** Why?
	CALL	DrawChar			; {code.DrawChar} Draw character
	JMP	TwoSecDelay				; {code.TwoSecDelay} Two second delay and out
	; Initializiation comes here
	;
init:
	LXI	SP,0x2400				; Set stack pointer just below screen
	MVI	B,0x00					; Count 256 bytes
	CALL	L_01E6				; {} Copy ROM to RAM
	CALL	DrawStatus			; {code.DrawStatus} Print scores and credits
	;
L_18DF:
	MVI	A,0x08					; Set alien ...
	STA	0x20CF					; {ram.aShotReloadRate} ... shot reload rate
	JMP	L_0AEA					; {} Top of splash screen loop
	; Get player-alive flag for OTHER player
L_18E7:
	LDA	0x2067					; {ram.playerDataMSB} Player data MSB
	LXI	H,0x20E7				; Alive flags (player 1 and 2)
	RRC							; Bit 1=1 for player 1
	RNC							; Player 2 ... we have it ... out
	INX	H						; Player 1's flag
	RET							; Done
	; If there is one alien left then the right motion is 3 instead of 2. That's
	; why the timing is hard to hit after the change.
L_18F1:
	MVI	B,0x02					; Rack moving right delta X
	LDA	0x2082					; {ram.numAliens} Number of aliens on screen
	DCR	A						; Just one left?
	RNZ							; No ... use right delta X of 2
	INR	B						; Just one alien ... move right at 3 instead of 2
	RET							; Done
	; Add in bit for sound
SoundBits3On:
	LDA	0x2094					; {ram.soundPort3} Current value of sound port
	ORA	B						; Add in new sounds
	STA	0x2094					; {ram.soundPort3} New value of sound port
	OUT	0x03					; {hard.SOUND1} Write new value to sound hardware
	RET
InitAliensP2:
	LXI	H,0x2200				; Player 2 data area
	JMP	L_01C3					; {} Initialize player 2 aliens
PlyrShotAndBump:
	CALL	PlayerShotHit		; {code.PlayerShotHit} Player's shot collision detection
	JMP	RackBump				; {code.RackBump} Change alien deltaX and deltaY when rack bumps edges
	; Get the current player's alive status
CurPlyAlive:
	LXI	H,0x20E7				; Alive flags
	LDA	0x2067					; {ram.playerDataMSB} Player 1 or 2
	RRC							; Will be 1 if player 1
	RC							; Return if player 1
	INX	H						; Bump to player 2
	RET							; Return
	; Print score header " SCORE<1> HI-SCORE SCORE<2> "
DrawScoreHead:
	MVI	C,0x1C					; 28 bytes in message
	LXI	H,0x241E				; Screen coordinates
	LXI	D,MessageScore			; Score header message
	JMP	PrintMessage			; {code.PrintMessage} Print score header
L_1925:
	LXI	H,0x20F8				; Player 1 score descriptor
	JMP	DrawScore				; {code.DrawScore} Print score
L_192B:
	LXI	H,0x20FC				; Player 2 score descriptor
	JMP	DrawScore				; {code.DrawScore} Print score
	; Print score.
	; HL = descriptor
DrawScore:
	MOV	E,M						; Get score LSB
	INX	H						; Next
	MOV	D,M						; Get score MSB
	INX	H						; Next
	MOV	A,M						; Get coordinate LSB
	INX	H						; Next
	MOV	H,M						; Get coordiante MSB
	MOV	L,A						; Set LSB
	JMP	Print4Digits			; {code.Print4Digits} Print 4 digits in DE
	; Print message "CREDIT "
L_193C:
	MVI	C,0x07					; 7 bytes in message
	LXI	H,0x3501				; Screen coordinates
	LXI	D,MessageCredit			; Message = "CREDIT "
	JMP	PrintMessage			; {code.PrintMessage} Print message
	; Display number of credits on screen
DrawNumCredits:
	LDA	0x20EB					; {ram.numCoins} Number of credits
	LXI	H,0x3C01				; Screen coordinates
	JMP	DrawHexByte				; {code.DrawHexByte} Character to screen
PrintHiScore:
	LXI	H,0x20F4				; Hi Score descriptor
	JMP	DrawScore				; {code.DrawScore} Print Hi-Score
	; Print scores (with header) and credits (with label)
DrawStatus:
	CALL	ClearScreen			; {code.ClearScreen} Clear the screen
	CALL	DrawScoreHead		; {code.DrawScoreHead} Print score header
	CALL	L_1925				; {} Print player 1 score
	CALL	L_192B				; {} Print player 2 score
	CALL	PrintHiScore		; {code.PrintHiScore} Print hi score
	CALL	L_193C				; {} Print credit lable
	JMP	DrawNumCredits			; {code.DrawNumCredits} Number of credits
L_196B:
	CALL	SoundBits3Off		; {code.SoundBits3Off} From 170B with B=FB. Turn off player shot sound
	JMP	L_1671					; {} Update high-score if player's score is greater
L_1971:
	MVI	A,0x01					; Set flag that ...
	STA	0x206D					; {ram.invaded} ... aliens reached bottom of screen
	JMP	L_16E6					; {} End of round
L_1979:
	CALL	DsableGameTasks		; {code.DsableGameTasks} Disable ISR game tasks
	CALL	DrawNumCredits		; {code.DrawNumCredits} Display number of credits on screen
	JMP	L_193C					; {} Print message "CREDIT"
L_1982:
	STA	0x20C1					; {ram.isrSplashTask} Set ISR splash task
	RET							; Done
	; The original code (from TAITO) printed this message on the screen. When Midway branched the code
	; they changed the logic so it isn't printed.
D_1986:
	DB	0x8B, 0x19				; Points to print TAITO CORPORATION message ... not sure why
L_1988:
	JMP	ClearPlayField			; {code.ClearPlayField} Clear playfield and out
	; Print "*TAITO CORPORATION*"
D_198B:
	DB	0x21, 0x03, 0x28, 0x11, 0xBE, 0x19, 0x0E, 0x13, 0xC3, 0xF3, 0x08, 0x00, 0x00, 0x00, 0x00	; Screen coordinates
	; There is a hidden message "TAITO COP" (with no "R") in the game. It can only be
	; displayed in the demonstration game during the splash screens. You must enter
	; 2 seqences of buttons. Timing is not critical. As long as you eventually get all
	; the buttons up/down in the correct pattern then the game will register the
	; sequence.
	;
	; 1st: 2start(down) 1start(up)   1fire(down) 1left(down) 1right(down)
	; 2nd: 2start(up)   1start(down) 1fire(down) 1left(down) 1right(up)
	;
	; Unfortunately MAME does not deliver the simultaneous button presses correctly. You can see the message in
	; MAME by changing 19A6 to 02 and 19B1 to 02. Then the 2start(down) is the only sequence.
	;
CheckHiddenMes:
	LDA	0x201E					; {ram.hidMessSeq} Has the 1st "hidden-message" sequence ...
	ANA	A						; ... been registered?
	JNZ	L_19AC					; {} Yes ... go look for the 2nd sequence
	IN	0x01					; {hard.INP1} Get player inputs
	ANI	0x76					; 0111_0110 Keep 2Pstart, 1Pstart, 1Pshot, 1Pleft, 1Pright
	SUI	0x72					; 0111_0010 1st sequence: 2Pstart, 1Pshot, 1Pleft, 1Pright
	RNZ							; Not first sequence ... out
	INR	A						; Flag that 1st sequence ...
	STA	0x201E					; {ram.hidMessSeq} ... has been entered
L_19AC:
	IN	0x01					; {hard.INP1} Check inputs for 2nd sequence
	ANI	0x76					; 0111_0110 Keep 2Pstart, 1Pstart, 1Pshot, 1Pleft, 1Pright
	CPI	0x34					; 0011_0100 2nd sequence: 1Pstart, 1Pshot, 1Pleft
	RNZ							; If not second sequence ignore
	LXI	H,0x2E1B				; Screen coordinates
	LXI	D,MessageCorp			; Message = "TAITO COP" (no R)
	MVI	C,0x09					; Message length
	JMP	PrintMessage			; {code.PrintMessage} Print message and out
	; "*TAITO CORPORATION*"
MessageTaito:
	DB	0x28, 0x13, 0x00, 0x08, 0x13, 0x0E, 0x26, 0x02, 0x0E, 0x11, 0x0F, 0x0E, 0x11, 0x00, 0x13, 0x08
	DB	0x0E, 0x0D, 0x28
	; Enable ISR game tasks
EnableGameTasks:
	MVI	A,0x01					; Set ISR ...
L_19D3:
	STA	0x20E9					; {ram.suspendPlay} ... game tasks enabled
	RET							; Done
	; Disable ISR game tasks
	; Clear 20E9 flag
DsableGameTasks:
	XRA	A						; Clear ISR game tasks flag
	JMP	L_19D3					; {} Save a byte (the RET)
D_19DB:
	DB	0x00					; ** Here is the byte saved. I wonder if this was an optimizer pass.
	; Turn off bit in sound port
SoundBits3Off:
	LDA	0x2094					; {ram.soundPort3} Current sound effects value
	ANA	B						; Mask bits off
	STA	0x2094					; {ram.soundPort3} Store new hold value
	OUT	0x03					; {hard.SOUND1} Change sounds
	RET							; Done
	; Show ships remaining in hold for the player
DrawNumShips:
	LXI	H,0x2701				; Screen coordinates
	JZ	L_19FA					; {} None in reserve ... skip display
	; Draw line of ships
L_19EC:
	LXI	D,PlayerSprite			; Player sprite
	MVI	B,0x10					; 16 rows
	MOV	C,A						; Hold count
	CALL	DrawSimpSprite		; {code.DrawSimpSprite} Display 1byte sprite to screen
	MOV	A,C						; Restore remaining
	DCR	A						; All done?
	JNZ	L_19EC					; {} No ... keep going
	; Clear remainder of line
L_19FA:
	MVI	B,0x10					; 16 rows
	CALL	ClearSmallSprite	; {code.ClearSmallSprite} Clear 1byte sprite at HL
	MOV	A,H						; Get Y coordinate
	CPI	0x35					; At edge?
	JNZ	L_19FA					; {} No ... do all
	RET							; Out
	;
	; The ISRs set the upper bit of 2072 based on where the beam is. This is compared to the
	; upper bit of an object's Y coordinate to decide whic ISR should handle it. When the
	; beam passes the halfway point (or near it ... at scanline 96), the upper bit is cleared.
	; When the beam reaches the end of the screen the upper bit is set.
	;
	; The task then runs in the ISR if the Y coordiante bit matches the 2072 flag. Objects that
	; are at the top of the screen (upper bit of Y clear) run in the mid-screen ISR when
	; the beam has moved to the bottom of the screen. Objects that are at the bottom of the screen
	; (upper bit of Y set) run in the end-screen ISR when the beam is moving back to the top.
	;
	; The pointer to the object's Y coordinate is passed in DE. CF is set if the upper bits are
	; the same (the calling ISR should execute the task).
	;
CompYToBeam:
	DB	0x21, 0x72, 0x20, 0x46, 0x1A, 0xE6, 0x80, 0xA8, 0xC0, 0x37, 0xC9, 0x32, 0x2B, 0x24, 0x1C, 0x16	; Get the ...
	DB	0x11, 0x0D, 0x0A, 0x08, 0x07, 0x06, 0x05, 0x04, 0x03, 0x02, 0x01, 0x34, 0x2E, 0x27, 0x22, 0x1C
	DB	0x18, 0x15, 0x13, 0x10, 0x0E, 0x0D, 0x0C, 0x0B, 0x09, 0x07, 0x05, 0xFF
	; Copy from [DE] to [HL] (b bytes)
BlockCopy:
	LDAX	D					; Copy from [DE] to ...
	MOV	M,A						; ... [HL]
	INX	H						; Next destination
	INX	D						; Next source
	DCR	B						; Count in B
	JNZ	BlockCopy				; {code.BlockCopy} Do all
	RET							; Done
	; Load 5 bytes sprite descriptor from [HL]
ReadDesc:
	MOV	E,M						; Descriptor ...
	INX	H						; ... sprite ...
	MOV	D,M						; ...
	INX	H						; ... picture
	MOV	A,M						; Descriptor ...
	INX	H						; ... screen ...
	MOV	C,M						; ...
	INX	H						; ... location
	MOV	B,M						; Number of bytes in sprite
	MOV	H,C						; From A,C to ...
	MOV	L,A						; ... H,L
	RET							; Done
	; The screen is organized as one-bit-per-pixel.
	; In: HL contains pixel number (bbbbbbbbbbbbbppp)
	; Convert from pixel number to screen coordinates (without shift)
	; Shift HL right 3 bits (clearing the top 2 bits)
	; and set the third bit from the left.
ConvToScr:
	PUSH	B					; Hold B (will mangle)
	MVI	B,0x03					; 3 shifts (divide by 8)
L_1A4A:
	MOV	A,H						; H to A
	RAR							; Shift right (into carry, from doesn't matter)
	MOV	H,A						; Back to H
	MOV	A,L						; L to A
	RAR							; Shift right (from/to carry)
	MOV	L,A						; Back to L
	DCR	B						; Do all ...
	JNZ	L_1A4A					; {} ... 3 shifts
	MOV	A,H						; H to A
	ANI	0x3F					; Mask off all but screen (less than or equal 3F)
	ORI	0x20					; Offset into RAM
	MOV	H,A						; Back to H
	POP	B						; Restore B
	RET							; Done
	; Clear the screen
	; Thanks to Mark Tankard for pointing out what this really does
ClearScreen:
	LXI	H,0x2400				; Screen coordinate
L_1A5F:
	MVI	M,0x00					; Clear it
	INX	H						; Next byte
	MOV	A,H						; Have we done ...
	CPI	0x40					; ... all the screen?
	JNZ	L_1A5F					; {} No ... keep going
	RET							; Out
	; Logically OR the player's shields back onto the playfield
	; DE = sprite
	; HL = screen
	; C = bytes per row
	; B = number of rows
RestoreShields:
	PUSH	B					; Preserve BC
	PUSH	H					; Hold for a bit
L_1A6B:
	LDAX	D					; From sprite
	ORA	M						; OR with screen
	MOV	M,A						; Back to screen
	INX	D						; Next sprite
	INX	H						; Next on screen
	DCR	C						; Row done?
	JNZ	L_1A6B					; {} No ... do entire row
	POP	H						; Original start
	LXI	B,L_0020				; Bump HL by ...
	DAD	B						; ... one screen row
	POP	B						; Restore
	DCR	B						; Row counter
	JNZ	RestoreShields			; {code.RestoreShields} Do all rows
	RET
	; Remove a ship from the players stash and update the
	; hold indicators on the screen.
RemoveShip:
	CALL	L_092E				; {} Get last byte from player data
	ANA	A						; Is it 0?
	RZ							; Skip
	PUSH	PSW					; Preserve number remaining
	DCR	A						; Remove a ship from the stash
	MOV	M,A						; New number of ships
	CALL	DrawNumShips		; {code.DrawNumShips} Draw the line of ships
	POP	PSW						; Restore number
L_1A8B:
	LXI	H,0x2501				; Screen coordinates
	ANI	0x0F					; Make sure it is a digit
	JMP	L_09C5					; {} Print number remaining
	; Data From Here Down
D_1A93:
	DB	0x00, 0x00, 0x00, 0x00, 0xFF, 0xB8, 0xFE, 0x20, 0x1C, 0x10, 0x9E, 0x00, 0x20, 0x1C
	; The tables at 1CB8 and 1AA1 control how fast shots are created. The speed is based
	; on the upper byte of the player's score. For a score of less than or equal 0200 then
	; the fire speed is 30. For a score less than or equal 1000 the shot speed is 10. Less
	; than or equal 2000 the speed is 0B. Less than or equal 3000 is 08. And anything
	; above 3000 is 07.
	;
	; 1CB8: 02 10 20 30
	;
ShotReloadRate:
	DB	0x30, 0x10, 0x0B, 0x08, 0x07
	; GAME OVER PLAYER< >"
MessageGOver:
	DB	0x06, 0x00, 0x0C, 0x04, 0x26, 0x0E, 0x15, 0x04, 0x11, 0x26, 0x26, 0x0F, 0x0B, 0x00, 0x18, 0x04
	DB	0x11, 0x24, 0x26, 0x25
	; "1 OR 2PLAYERS BUTTON"
MessageB1or2:
	DB	0x1B, 0x26, 0x0E, 0x11, 0x26, 0x1C, 0x0F, 0x0B, 0x00, 0x18, 0x04, 0x11, 0x12, 0x26, 0x01, 0x14
	DB	0x13, 0x13, 0x0E, 0x0D, 0x26
	; "ONLY 1PLAYER BUTTON "
	; Note the space on the end ... both alternatives are same length
Message1Only:
	DB	0x0E, 0x0D, 0x0B, 0x18, 0x26, 0x1B, 0x0F, 0x0B, 0x00, 0x18, 0x04, 0x11, 0x26, 0x26, 0x01, 0x14
	DB	0x13, 0x13, 0x0E, 0x0D, 0x26
	; " SCORE<1> HI-SCORE SCORE<2>"
MessageScore:
	DB	0x26, 0x12, 0x02, 0x0E, 0x11, 0x04, 0x24, 0x1B, 0x25, 0x26, 0x07, 0x08, 0x3F, 0x12, 0x02, 0x0E
	DB	0x11, 0x04, 0x26, 0x12, 0x02, 0x0E, 0x11, 0x04, 0x24, 0x1C, 0x25, 0x26, 0x01, 0x00, 0x00, 0x10
	DB	0x00, 0x00, 0x00, 0x00, 0x02, 0x78, 0x38, 0x78, 0x38, 0x00, 0xF8, 0x00, 0x00, 0x80, 0x00, 0x8E
	DB	0x02, 0xFF, 0x05, 0x0C, 0x60, 0x1C, 0x20, 0x30, 0x10, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0xBB
	DB	0x03, 0x00, 0x10, 0x90, 0x1C, 0x28, 0x30, 0x01, 0x04, 0x00, 0xFF, 0xFF, 0x00, 0x00, 0x02, 0x76
	DB	0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0xEE, 0x1C, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0xB6
	DB	0x04, 0x00, 0x00, 0x01, 0x00, 0x1D, 0x04, 0xE2, 0x1C, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x82
	DB	0x06, 0x00, 0x00, 0x01, 0x06, 0x1D, 0x04, 0xD0, 0x1C, 0x00, 0x00, 0x03, 0xFF, 0x00, 0xC0, 0x1C
	DB	0x00, 0x00, 0x10, 0x21, 0x01, 0x00, 0x30, 0x00, 0x12, 0x00, 0x00, 0x00
	; These don't need to be copied over to RAM (see 1BA0 below).
	; "PLAY PLAYER<1>"
MesssageP1:
	DB	0x0F, 0x0B, 0x00, 0x18, 0x26, 0x0F, 0x0B, 0x00, 0x18, 0x04, 0x11, 0x24, 0x1B, 0x25, 0xFC, 0x00
	DB	0x01, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x20, 0x64, 0x1D, 0xD0, 0x29, 0x18, 0x02, 0x54, 0x1D, 0x00
	DB	0x08, 0x00, 0x06, 0x00, 0x00, 0x01, 0x40, 0x00, 0x01, 0x00, 0x00, 0x10, 0x9E, 0x00, 0x20, 0x1C
	; These don't need to be copied over to RAM I believe this to be a mistake. The constant at 01E4 is C0,
	; which is the size of this mirror with the added sprite. It should be A0. I believe there was a macro
	; to size this area and later the splash screens where put in. Some of the data spilled over into this
	; and the macro automatically included it. No harm.
	; Alien Pulling Upside Down 'Y' visual
	; <canvas width="130" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x16Data"
	;          data-address="1BA0"
	;          data-gridX="16"
	;          data-gridY="8"
	;          data-command="0">
	; </canvas>
	; Alien sprite type C pulling upside down Y
	; ........
	; **......
	; ..*.....
	; ...****.
	; ..*.*...
	; **..*...
	; ...*....
	; .*.**...
	; *.****..
	; ...*.**.
	; ..******
	; ..******
	; ...*.**.
	; *.****..
	; .*.**...
	; ........
AlienSprCYA:
	DB	0x00, 0x03, 0x04, 0x78, 0x14, 0x13, 0x08, 0x1A, 0x3D, 0x68, 0xFC, 0xFC, 0x68, 0x3D, 0x1A, 0x00
	DB	0x00, 0x00, 0x01, 0xB8, 0x98, 0xA0, 0x1B, 0x10, 0xFF, 0x00, 0xA0, 0x1B, 0x00, 0x00, 0x00, 0x00
	DB	0x00, 0x10, 0x00, 0x0E, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xD0, 0x1C, 0xC8, 0x9B, 0x03
	; <canvas width="130" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x16Data"
	;          data-address="1BD0"
	;          data-gridX="16"
	;          data-gridY="8"
	;          data-command="0">
	; </canvas>
	; Alien sprite C pulling upside down Y. Note the difference between this and the first picutre
	; above. The Y is closer to the ship. This gives the effect of the Y kind of "sticking" in the
	; animation.
	; ........
	; ........
	; **......
	; ..*.....
	; ...****.
	; ..*.*...
	; **.*....
	; *..**...
	; .*.***..
	; *.**.**.
	; .*.*****
	; .*.*****
	; *.**.**.
	; .*.***..
	; *..**...
	; ........
	;
AlienSprCYB:
	DB	0x00, 0x00, 0x03, 0x04, 0x78, 0x14, 0x0B, 0x19, 0x3A, 0x6D, 0xFA, 0xFA, 0x6D, 0x3A, 0x19, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x01, 0x74, 0x1F, 0x00
	DB	0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1C, 0x2F, 0x00, 0x00, 0x1C, 0x27, 0x00, 0x00, 0x1C, 0x39
	; Alien Images visual
	; <canvas width="400" height="140"
	;      data-getTileDataFunction="SpaceInvaders.get8x16Data"
	;          data-address="1C00"
	;          data-gridX="16"
	;          data-gridY="8"
	;          data-command="0,+x,1,+x,2,*,+y,3,+x,4,+x,5">
	;  </canvas>
	; Alien sprite type A,B, and C at positions 0
	;  ........ ........ ........
	;  ........ ........ ........
	;  *..***.. ........ ........
	;  *..****. ...****. ........
	;  .*.****. *.***... *..**...
	;  .***.**. .*****.* .*.***..
	;  ..**.*** ..**.**. *.**.**.
	;  .*.***** ..****.. .*.*****
	;  .*.***** ..****.. .*.*****
	;  ..**.*** ..****.. *.**.**.
	;  .***.**. ..**.**. .*.***..
	;  .*.****. .*****.* *..**...
	;  *..****. *.***... ........
	;  *..***.. ...****. ........
	;  ........ ........ ........
	;  ........ ........ ........
AlienSprA:
	DB	0x00, 0x00, 0x39, 0x79, 0x7A, 0x6E, 0xEC, 0xFA, 0xFA, 0xEC, 0x6E, 0x7A, 0x79, 0x39, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x78, 0x1D, 0xBE, 0x6C, 0x3C, 0x3C, 0x3C, 0x6C, 0xBE, 0x1D, 0x78, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x19, 0x3A, 0x6D, 0xFA, 0xFA, 0x6D, 0x3A, 0x19, 0x00, 0x00, 0x00, 0x00
	; Alien sprite type A,B, and C at positions 1
	;  ........ ........ ........
	;  ........ ........ ........
	;  ...***.. ........ ........
	;  .*.****. .***.... ........
	;  *******. ...**... .*.**...
	;  *.**.**. .*****.* *.****..
	;  ..**.*** *.**.**. ...*.**.
	;  .*.***** *.****.. ..******
	;  .*.***** ..****.. ..******
	;  ..**.*** *.****.. ...*.**.
	;  *.**.**. *.**.**. *.****..
	;  *******. .*****.* .*.**...
	;  .*.****. ...**... ........
	;  ...***.. .***.... ........
	;  ........ ........ ........
	;  ........ ........ ........
AlienSprB:
	DB	0x00, 0x00, 0x38, 0x7A, 0x7F, 0x6D, 0xEC, 0xFA, 0xFA, 0xEC, 0x6D, 0x7F, 0x7A, 0x38, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x0E, 0x18, 0xBE, 0x6D, 0x3D, 0x3C, 0x3D, 0x6D, 0xBE, 0x18, 0x0E, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x1A, 0x3D, 0x68, 0xFC, 0xFC, 0x68, 0x3D, 0x1A, 0x00, 0x00, 0x00, 0x00
	; Player Sprite visual
	;  <canvas width="400" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x16Data"
	;          data-address="1C60"
	;          data-gridX="16"
	;          data-gridY="8"
	;          data-command="0,+x,1,+x,2">
	;  </canvas>
	;  ........
	;  ........
	;  ****....
	;  *****...
	;  *****...
	;  *****...
	;  *****...
	;  *******.
	;  ********
	;  *******.
	;  *****...
	;  *****...
	;  *****...
	;  *****...
	;  ****....
	;  ........
PlayerSprite:
	DB	0x00, 0x00, 0x0F, 0x1F, 0x1F, 0x1F, 0x1F, 0x7F, 0xFF, 0x7F, 0x1F, 0x1F, 0x1F, 0x1F, 0x0F, 0x00
	;  ........
	;  ..*.....
	;  *.......
	;  **..*...
	;  **......
	;  ***.....
	;  **..**.*
	;  ****....
	;  ****.*..
	;  **......
	;  ****.*..
	;  *..*..*.
	;  ..*.....
	;  **......
	;  ........
	;  *.......
	;
PlrBlowupSprites:
	DB	0x00, 0x04, 0x01, 0x13, 0x03, 0x07, 0xB3, 0x0F, 0x2F, 0x03, 0x2F, 0x49, 0x04, 0x03, 0x00, 0x01
	DB	0x40, 0x08, 0x05, 0xA3, 0x0A, 0x03, 0x5B, 0x0F, 0x27, 0x27, 0x0B, 0x4B, 0x40, 0x84, 0x11, 0x48
	; Player Shot Sprite visual
	;  <canvas width="10" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get1x8Data"
	;          data-address="1C90"
	;          data-gridX="1"
	;          data-gridY="8"
	;          data-command="0">
	;  </canvas>
PlayerShotSpr:
	DB	0x0F					; ++++....
	; Player Shot Exploding visual
	;  <canvas width="65" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x8Data"
	;          data-address="1C91"
	;          data-gridX="8"
	;          data-gridY="8"
	;          data-command="0">
	;  </canvas>
	; *..**..*
	; ..****..
	; .******.
	; *.****..
	; ..****.*
	; .*****..
	; ..*****.
	; *..**..*
ShotExploding:
	DB	0x99, 0x3C, 0x7E, 0x3D, 0xBC, 0x3E, 0x7C, 0x99
	; Ran out of space at 1DFE
Message10Pts:
	DB	0x27, 0x1B, 0x1A, 0x26, 0x0F, 0x0E, 0x08, 0x0D, 0x13, 0x12	; "=10 POINTS"
	; "*SCORE ADVANCE TABLE*"
MessageAdv:
	DB	0x28, 0x12, 0x02, 0x0E, 0x11, 0x04, 0x26, 0x00, 0x03, 0x15, 0x00, 0x0D, 0x02, 0x04, 0x26, 0x13
	DB	0x00, 0x01, 0x0B, 0x04, 0x28
	; The tables at 1CB8 and 1AA1 control how fast shots are created. The speed is based
	; on the upper byte of the player's score. For a score of less than or equal 0200 then
	; the fire speed is 30. For a score less than or equal 1000 the shot speed is 10. Less
	; than or equal 2000 the speed is 0B. Less than or equal 3000 is 08. And anything
	; above 3000 is 07.
	;
	; 1AA1: 30 10 0B 08
	; 1AA5: 07           ; Fastest shot firing speed
	;
AReloadScoreTab:
	DB	0x02, 0x10, 0x20, 0x30
MessageTilt:
	DB	0x13, 0x08, 0x0B, 0x13	; "TILT"
	; Alien Exploding Sprite visual
	;  <canvas width="130" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x16Data"
	;          data-address="1CC0"
	;          data-gridX="16"
	;          data-gridY="8"
	;          data-command="0">
	;  </canvas>
	; Alien exploding sprite
	;  ........
	;  ...*....
	;  *..*..*.
	;  .*...*..
	;  ..*.*...
	;  *......*
	;  .*....*.
	;  ........
	;  .*....*.
	;  *......*
	;  ..*.*...
	;  .*...*..
	;  *..*..*.
	;  ...*....
	;  ........
	;  ........
AlienExplode:
	DB	0x00, 0x08, 0x49, 0x22, 0x14, 0x81, 0x42, 0x00, 0x42, 0x81, 0x14, 0x22, 0x49, 0x08, 0x00, 0x00
	; Squigly Shot Sprite visual
	;  <canvas width="120" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x3Data"
	;          data-address="1CD0"
	;          data-gridX="3"
	;          data-gridY="8"
	;          data-command="0,+x,1,+x,2,+x,3">
	;  </canvas>
	; Squigly shot picture in 4 animation frames
SquiglyShot:
	DB	0x44, 0xAA, 0x10, 0x88, 0x54, 0x22, 0x10, 0xAA, 0x44, 0x22, 0x54, 0x88	; ..*...*.
	; Alien Shot Exploding visual
	;  <canvas width="65" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get6x8Data"
	;          data-address="1CDC"
	;          data-gridX="6"
	;          data-gridY="8"
	;          data-command="0">
	;  </canvas>
	; Alien shot exploding
	; .*.*..*.
	; *.*.*...
	; .*****.*
	; ******..
	; .****.*.
	; *.*..*..
AShotExplo:
	DB	0x4A, 0x15, 0xBE, 0x3F, 0x5E, 0x25
	; Plunger Shot Sprite visual
	;  <canvas width="120" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x3Data"
	;          data-address="1CE2"
	;          data-gridX="3"
	;          data-gridY="8"
	;          data-command="0,+x,1,+x,2,+x,3">
	;  </canvas>
	; Alien shot ... the plunger looking one
PlungerShot:
	DB	0x04, 0xFC, 0x04, 0x10, 0xFC, 0x10, 0x20, 0xFC, 0x20, 0x80, 0xFC, 0x80	; ..*.....
	; Rolling Shot Sprite visual
	;  <canvas width="120" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x3Data"
	;          data-address="1CEE"
	;          data-gridX="3"
	;          data-gridY="8"
	;          data-command="0,+x,1,+x,2,+x,3">
	;  </canvas>
	; Alien shot ... the rolling one
RollShot:
	DB	0x00, 0xFE, 0x00, 0x24, 0xFE, 0x12, 0x00, 0xFE, 0x00, 0x48, 0xFE, 0x90	; ........
MessagePlayUY:
	DB	0x0F, 0x0B, 0x00, 0x29, 0x00, 0x00	; "PLAy" with an upside down 'Y' for splash screen
	; This table decides which column a shot will fall from. The column number is read from the
	; table (1-11) and the pointer increases for the shot type. For instance, the "squiggly" shot
	; will fall from columns in this order: 0B, 01, 06, 03. If you play the game you'll see that
	; order.
	;
	; The "plunger" shot uses index 00-0F (inclusive)
	; The "squiggly" shot uses index 06-14 (inclusive)
	; The "rolling" shot targets the player
ColFireTable:
	DB	0x01, 0x07, 0x01, 0x01, 0x01, 0x04, 0x0B, 0x01, 0x06, 0x03, 0x01, 0x01, 0x0B, 0x09, 0x02, 0x08
	DB	0x02, 0x0B, 0x04, 0x07, 0x0A, 0x05, 0x02, 0x05, 0x04, 0x06, 0x07, 0x08, 0x0A, 0x06, 0x0A, 0x03
	; Shield Image visual
	;  <canvas width="180" height="130"
	;      data-getTileDataFunction="SpaceInvaders.get16x22Data"
	;          data-address="1D20"
	;          data-gridX="22"
	;          data-gridY="16"
	;          data-command="0">
	;  </canvas>
	; Shield image pattern. 2 x 22 = 44 bytes.
	;
	;************....
	;*************...
	;**************..
	;***************.
	;****************
	;..**************
	;...*************
	;....************
	;....************
	;....************
	;....************
	;....************
	;....************
	;....************
	;...*************
	;..**************
	;****************
	;****************
	;***************.
	;**************..
	;*************...
	;************....
	;
ShieldImage:
	DB	0xFF, 0x0F, 0xFF, 0x1F, 0xFF, 0x3F, 0xFF, 0x7F, 0xFF, 0xFF, 0xFC, 0xFF, 0xF8, 0xFF, 0xF0, 0xFF
	DB	0xF0, 0xFF, 0xF0, 0xFF, 0xF0, 0xFF, 0xF0, 0xFF, 0xF0, 0xFF, 0xF0, 0xFF, 0xF8, 0xFF, 0xFC, 0xFF
	DB	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0xFF, 0x3F, 0xFF, 0x1F, 0xFF, 0x0F, 0x05, 0x10, 0x15, 0x30
	DB	0x94, 0x97, 0x9A, 0x9D
	; 208D points here to the score given when the saucer is shot. It advances
	; every time the player-shot is removed. The code wraps after 15, but there
	; are 16 values in this table. This is a bug in the code at 044E (thanks to
	; Colin Dooley for finding this).
	;
	; Thus the one and only 300 comes up every 15 shots (after an initial 8).
SaucerScrTab:
	DB	0x10, 0x05, 0x05, 0x10, 0x15, 0x10, 0x10, 0x05, 0x30, 0x10, 0x10, 0x10, 0x05, 0x15, 0x10, 0x05
	; Flying Saucer Sprite visual
	;  <canvas width="410" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x24Data"
	;          data-address="1D64"
	;          data-gridX="24"
	;          data-gridY="8"
	;          data-command="0,+x,1">
	;  </canvas>
	; ........
	; ........
	; ........
	; ........
	; ..*.....
	; ..**....
	; .****...
	; ***.**..
	; .*****..
	; ..*****.
	; ..*.***.
	; .******.
	; .******.
	; ..*.***.
	; ..*****.
	; .*****..
	; ***.**..
	; .****...
	; ..**....
	; ..*.....
	; ........
	; ........
	; ........
	; ........
SpriteSaucer:
	DB	0x00, 0x00, 0x00, 0x00, 0x04, 0x0C, 0x1E, 0x37, 0x3E, 0x7C, 0x74, 0x7E, 0x7E, 0x74, 0x7C, 0x3E
	DB	0x37, 0x1E, 0x0C, 0x04, 0x00, 0x00, 0x00, 0x00
	;........
	;.*...*..
	;........
	;*.*..*.*
	;......*.
	;...*....
	;...**..*
	;*.****..
	;.**.**.*
	;..****..
	;.**.**..
	;*.***...
	;....*...
	;...*..*.
	;.*...**.
	;.**.**.*
	;*.***...
	;...**..*
	;...*....
	;.*....*.
	;....*..*
	;...*....
	;........
	;........
SpriteSaucerExp:
	DB	0x00, 0x22, 0x00, 0xA5, 0x40, 0x08, 0x98, 0x3D, 0xB6, 0x3C, 0x36, 0x1D, 0x10, 0x48, 0x62, 0xB6
	DB	0x1D, 0x98, 0x08, 0x42, 0x90, 0x08, 0x00, 0x00
SaucSoreStr:
	DB	0x26, 0x1F, 0x1A, 0x1B, 0x1A, 0x1A, 0x1B, 0x1F, 0x1A, 0x1D, 0x1A, 0x1A	; _50
	; Score table for hitting alien type
AlienScores:
	DB	0x10, 0x20, 0x30		; Bottom 2 rows
	; Starting Y coordinates for aliens at beginning of rounds. The first round is initialized to $78 at 07EA.
	; After that this table is used for 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, and 9th. The 10th starts over at
	; 1DA3 (60).
AlienStartTable:
	DB	0x60, 0x50, 0x48, 0x48, 0x48, 0x40, 0x40, 0x40
MessagePlayY:
	DB	0x0F, 0x0B, 0x00, 0x18	; "PLAY" with normal Y
	; "SPACE  INVADERS"
MessageInvaders:
	DB	0x12, 0x0F, 0x00, 0x02, 0x04, 0x26, 0x26, 0x08, 0x0D, 0x15, 0x00, 0x03, 0x04, 0x11, 0x12, 0x0E
	DB	0x2C, 0x68, 0x1D, 0x0C, 0x2C, 0x20, 0x1C, 0x0A, 0x2C, 0x40, 0x1C, 0x08, 0x2C, 0x00, 0x1C, 0xFF
	;
AlienScoreTable:
	DB	0x0E, 0x2E, 0xE0, 0x1D, 0x0C, 0x2E, 0xEA, 0x1D, 0x0A, 0x2E, 0xF4, 0x1D, 0x08, 0x2E, 0x99, 0x1C	; "=? MYSTERY"
	DB	0xFF
MessageMyst:
	DB	0x27, 0x38, 0x26, 0x0C, 0x18, 0x12, 0x13, 0x04, 0x11, 0x18	; "=? MYSTERY"
Message30Pts:
	DB	0x27, 0x1D, 0x1A, 0x26, 0x0F, 0x0E, 0x08, 0x0D, 0x13, 0x12	; "=30 POINTS"
Message20Pts:
	DB	0x27, 0x1C, 0x1A, 0x26, 0x0F, 0x0E, 0x08, 0x0D, 0x13, 0x12, 0x00, 0x00	; "=20 POINTS"
	; Text Character Sprites visual
	;  <canvas width="520" height="520"
	;      data-getTileDataFunction="SpaceInvaders.get8x8CharData"
	;          data-labelColor="#FFFFFF"
	;          data-address="1E00"
	;          data-gridX="8"
	;          data-gridY="8"
	;          data-command=":8x8:0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,
	;                         10,11,12,13,14,15,16,17,18,19,1A,1B,1C,1D,1E,1F,
	;                         20,21,22,23,24,25,26,27,28,29,#UNUSED,2A,2B,2C,2D,2E,2F,
	;                         30,31,32,33,34,35,36,37,#CS0,38,#UNUSED,39,3A,3B,3C,3D,3E,#CS0,3F">
	;  </canvas>
	; 8 byte sprites
	; The screen is turned so rotate these pictures counter-clockwise.
	; Some of the font characters at the end were never needed. The ROM overwrites these characters with
	; data near the end. For instance, 1F90 would be a character but has the "INSERT COIN" message. The "?"
	; character is at 1FC0 and is used in messages as is 1FF8 "-". The "light colored" tiles in the grid below
	; show the character slots that have been repurposed.
Characters:
	DB	0x00, 0x1F, 0x24, 0x44, 0x24, 0x1F, 0x00, 0x00, 0x00, 0x7F, 0x49, 0x49, 0x49, 0x36, 0x00, 0x00	; ........ ........ ........ ........ ........ ........ ........ ........
	DB	0x00, 0x3E, 0x41, 0x41, 0x41, 0x22, 0x00, 0x00, 0x00, 0x7F, 0x41, 0x41, 0x41, 0x3E, 0x00, 0x00
	DB	0x00, 0x7F, 0x49, 0x49, 0x49, 0x41, 0x00, 0x00, 0x00, 0x7F, 0x48, 0x48, 0x48, 0x40, 0x00, 0x00
	DB	0x00, 0x3E, 0x41, 0x41, 0x45, 0x47, 0x00, 0x00, 0x00, 0x7F, 0x08, 0x08, 0x08, 0x7F, 0x00, 0x00
	DB	0x00, 0x00, 0x41, 0x7F, 0x41, 0x00, 0x00, 0x00, 0x00, 0x02, 0x01, 0x01, 0x01, 0x7E, 0x00, 0x00
	DB	0x00, 0x7F, 0x08, 0x14, 0x22, 0x41, 0x00, 0x00, 0x00, 0x7F, 0x01, 0x01, 0x01, 0x01, 0x00, 0x00
	DB	0x00, 0x7F, 0x20, 0x18, 0x20, 0x7F, 0x00, 0x00, 0x00, 0x7F, 0x10, 0x08, 0x04, 0x7F, 0x00, 0x00
	DB	0x00, 0x3E, 0x41, 0x41, 0x41, 0x3E, 0x00, 0x00, 0x00, 0x7F, 0x48, 0x48, 0x48, 0x30, 0x00, 0x00
	DB	0x00, 0x3E, 0x41, 0x45, 0x42, 0x3D, 0x00, 0x00, 0x00, 0x7F, 0x48, 0x4C, 0x4A, 0x31, 0x00, 0x00
	DB	0x00, 0x32, 0x49, 0x49, 0x49, 0x26, 0x00, 0x00, 0x00, 0x40, 0x40, 0x7F, 0x40, 0x40, 0x00, 0x00
	DB	0x00, 0x7E, 0x01, 0x01, 0x01, 0x7E, 0x00, 0x00, 0x00, 0x7C, 0x02, 0x01, 0x02, 0x7C, 0x00, 0x00
	DB	0x00, 0x7F, 0x02, 0x0C, 0x02, 0x7F, 0x00, 0x00, 0x00, 0x63, 0x14, 0x08, 0x14, 0x63, 0x00, 0x00
	DB	0x00, 0x60, 0x10, 0x0F, 0x10, 0x60, 0x00, 0x00, 0x00, 0x43, 0x45, 0x49, 0x51, 0x61, 0x00, 0x00
	DB	0x00, 0x3E, 0x45, 0x49, 0x51, 0x3E, 0x00, 0x00, 0x00, 0x00, 0x21, 0x7F, 0x01, 0x00, 0x00, 0x00
	DB	0x00, 0x23, 0x45, 0x49, 0x49, 0x31, 0x00, 0x00, 0x00, 0x42, 0x41, 0x49, 0x59, 0x66, 0x00, 0x00
	DB	0x00, 0x0C, 0x14, 0x24, 0x7F, 0x04, 0x00, 0x00, 0x00, 0x72, 0x51, 0x51, 0x51, 0x4E, 0x00, 0x00
	DB	0x00, 0x1E, 0x29, 0x49, 0x49, 0x46, 0x00, 0x00, 0x00, 0x40, 0x47, 0x48, 0x50, 0x60, 0x00, 0x00
	DB	0x00, 0x36, 0x49, 0x49, 0x49, 0x36, 0x00, 0x00, 0x00, 0x31, 0x49, 0x49, 0x4A, 0x3C, 0x00, 0x00
	DB	0x00, 0x08, 0x14, 0x22, 0x41, 0x00, 0x00, 0x00, 0x00, 0x00, 0x41, 0x22, 0x14, 0x08, 0x00, 0x00
	DB	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x14, 0x14, 0x14, 0x14, 0x00, 0x00
	DB	0x00, 0x22, 0x14, 0x7F, 0x14, 0x22, 0x00, 0x00, 0x00, 0x03, 0x04, 0x78, 0x04, 0x03, 0x00, 0x00
	;                                ; ..*.*... ..*.....
	;                                ; *******. ...****.
	;                                ; ..*.*... ..*.....
	;                                ; .*...*.. **......
	;                                ; ........ ........
	;                                ; ........ ........
MessageP1or2:
	DB	0x24, 0x1B, 0x26, 0x0E, 0x11, 0x26, 0x1C, 0x26, 0x0F, 0x0B, 0x00, 0x18, 0x04, 0x11, 0x12, 0x25	; "<1 OR 2 PLAYERS>  "
	DB	0x26, 0x26
Message1Coin:
	DB	0x28, 0x1B, 0x26, 0x0F, 0x0B, 0x00, 0x18, 0x04, 0x11, 0x26, 0x26, 0x1B, 0x26, 0x02, 0x0E, 0x08	; "*1 PLAYER  1 COIN "
	DB	0x0D, 0x26
	; (1=Right, 2=Left)
DemoCommands:
	DB	0x01, 0x01, 0x00, 0x00, 0x01, 0x00, 0x02, 0x01, 0x00, 0x02, 0x01, 0x00
	; Alien Sprite Carrying 'Y' visual
	;  <canvas width="140" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x16Data"
	;          data-labelColor=""
	;          data-address="1F80"
	;          data-gridX="16"
	;          data-gridY="8"
	;          data-command="0">
	;  </canvas>
	;  <canvas width="140" height="65"
	;      data-getTileDataFunction="SpaceInvaders.get8x16Data"
	;          data-address="1FB0"
	;          data-gridX="16"
	;          data-gridY="8"
	;          data-command="0">
	;  </canvas>
	; Small alien pushing Y back onto screen
	; .....**.
	; ....*...
	; ****....
	; ....*...
	; .....**.
	; ....**..
	; ...**...
	; .*.**...
	; *.****..
	; ...*.**.
	; ..******
	; ..******
	; ...*.**.
	; *.****..
	; .*.**...
	; ........
AlienSprCA:
	DB	0x60, 0x10, 0x0F, 0x10, 0x60, 0x30, 0x18, 0x1A, 0x3D, 0x68, 0xFC, 0xFC, 0x68, 0x3D, 0x1A, 0x00
MessageCoin:
	DB	0x08, 0x0D, 0x12, 0x04, 0x11, 0x13, 0x26, 0x26, 0x02, 0x0E, 0x08, 0x0D	; "INSERT  COIN"
CreditTable:
	DB	0x0D, 0x2A, 0x50, 0x1F, 0x0A, 0x2A, 0x62, 0x1F, 0x07, 0x2A, 0xE1, 0x1F, 0xFF	; "<1 OR 2 PLAYERS>  " to screen at 2A0D
MessageCredit:
	DB	0x02, 0x11, 0x04, 0x03, 0x08, 0x13, 0x26	; "CREDIT " (with space on the end)
	; ........
	; .....**.
	; ....*...
	; ****....
	; ....*...
	; .....**.
	; ...***..
	; *..**...
	; .*.***..
	; *.**.**.
	; .*.*****
	; .*.*****
	; *.**.**.
	; .*.***..
	; *..**...
	; ........
AlienSprCB:
	DB	0x00, 0x60, 0x10, 0x0F, 0x10, 0x60, 0x38, 0x19, 0x3A, 0x6D, 0xFA, 0xFA, 0x6D, 0x3A, 0x19, 0x00
	DB	0x00, 0x20, 0x40, 0x4D, 0x50, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xB8, 0xFF, 0x80, 0x1F
	DB	0x10, 0x97, 0x00, 0x80, 0x1F, 0x00, 0x00, 0x01, 0xD0, 0x22, 0x20, 0x1C, 0x10, 0x94, 0x00, 0x20
	DB	0x1C
Message2Coins:
	DB	0x28, 0x1C, 0x26, 0x0F, 0x0B, 0x00, 0x18, 0x04, 0x11, 0x12, 0x26, 0x1C, 0x26, 0x02, 0x0E, 0x08	; "*2 PLAYERS 2 COINS"
	DB	0x0D, 0x12
MessagePush:
	DB	0x0F, 0x14, 0x12, 0x07, 0x26, 0x00, 0x08, 0x08, 0x08, 0x08, 0x08, 0x00, 0x00	; "PUSH " (with space on the end)
	END

; --- Auto-generated symbols ---
; Type,Address,Value
; SYM,0x0000,Reset  ; auto-data
; SYM,0x0006,D_0006  ; auto-data
; SYM,0x0008,ScanLine96  ; auto-data
; SYM,0x000F,D_000F  ; auto-data
; SYM,0x0010,ScanLine224  ; auto-data
; SYM,0x0018,L_0018  ; auto-code
; SYM,0x0020,L_0020  ; auto-code
; SYM,0x0028,L_0028  ; auto-code
; SYM,0x0030,L_0030  ; auto-code
; SYM,0x0038,L_0038  ; auto-code
; SYM,0x003E,L_003E  ; auto-code
; SYM,0x003F,L_003F  ; auto-code
; SYM,0x0042,L_0042  ; auto-code
; SYM,0x005D,L_005D  ; auto-code
; SYM,0x0067,L_0067  ; auto-code
; SYM,0x006F,L_006F  ; auto-code
; SYM,0x0072,L_0072  ; auto-code
; SYM,0x0082,L_0082  ; auto-code
; SYM,0x0088,D_0088  ; auto-data
; SYM,0x008C,L_008C  ; auto-code
; SYM,0x00A5,L_00A5  ; auto-code
; SYM,0x00B1,InitRack  ; auto-data
; SYM,0x00C8,L_00C8  ; auto-code
; SYM,0x00D3,L_00D3  ; auto-code
; SYM,0x00D7,L_00D7  ; auto-code
; SYM,0x00E2,D_00E2  ; auto-data
; SYM,0x0100,DrawAlien  ; auto-data
; SYM,0x0136,L_0136  ; auto-code
; SYM,0x013B,L_013B  ; auto-code
; SYM,0x0141,CursorNextAlien  ; auto-data
; SYM,0x0154,L_0154  ; auto-code
; SYM,0x017A,GetAlienCoords  ; auto-data
; SYM,0x0183,L_0183  ; auto-code
; SYM,0x0194,L_0194  ; auto-code
; SYM,0x0195,L_0195  ; auto-code
; SYM,0x01A1,MoveRefAlien  ; auto-data
; SYM,0x01BF,D_01BF  ; auto-data
; SYM,0x01C0,InitAliens  ; auto-data
; SYM,0x01C3,L_01C3  ; auto-code
; SYM,0x01C5,L_01C5  ; auto-code
; SYM,0x01CD,ReturnTwo  ; auto-data
; SYM,0x01CF,DrawBottomLine  ; auto-data
; SYM,0x01D9,AddDelta  ; auto-data
; SYM,0x01E4,CopyRAMMirror  ; auto-data
; SYM,0x01E6,L_01E6  ; auto-code
; SYM,0x01EF,DrawShieldPl1  ; auto-data
; SYM,0x01F5,DrawShieldPl2  ; auto-data
; SYM,0x01F8,L_01F8  ; auto-code
; SYM,0x01FD,L_01FD  ; auto-code
; SYM,0x0209,RememberShields1  ; auto-data
; SYM,0x020E,RememberShields2  ; auto-data
; SYM,0x0213,RestoreShields2  ; auto-data
; SYM,0x0214,L_0214  ; auto-code
; SYM,0x021A,RestoreShields1  ; auto-data
; SYM,0x021B,L_021B  ; auto-code
; SYM,0x021E,CopyShields  ; auto-data
; SYM,0x0229,L_0229  ; auto-code
; SYM,0x0235,L_0235  ; auto-code
; SYM,0x0242,L_0242  ; auto-code
; SYM,0x0248,RunGameObjs  ; auto-data
; SYM,0x024B,L_024B  ; auto-code
; SYM,0x026F,D_026F  ; auto-data
; SYM,0x0277,L_0277  ; auto-code
; SYM,0x027D,L_027D  ; auto-code
; SYM,0x0281,L_0281  ; auto-code
; SYM,0x0288,L_0288  ; auto-code
; SYM,0x028E,GameObj0  ; auto-data
; SYM,0x02ED,L_02ED  ; auto-code
; SYM,0x02F8,L_02F8  ; auto-code
; SYM,0x0312,L_0312  ; auto-code
; SYM,0x032C,D_032C  ; auto-data
; SYM,0x0332,L_0332  ; auto-code
; SYM,0x0338,D_0338  ; auto-data
; SYM,0x0381,MovePlayerRight  ; auto-data
; SYM,0x038E,MovePlayerLeft  ; auto-data
; SYM,0x039B,DrawPlayerDie  ; auto-data
; SYM,0x03BB,GameObj1  ; auto-data
; SYM,0x03FA,InitPlyShot  ; auto-data
; SYM,0x040A,MovePlyShot  ; auto-data
; SYM,0x0430,ReadPlyShot  ; auto-data
; SYM,0x0436,EndOfBlowup  ; auto-data
; SYM,0x0476,GameObj2  ; auto-data
; SYM,0x04AB,ResetShot  ; auto-data
; SYM,0x04B6,GameObj3  ; auto-data
; SYM,0x0550,ToShotStruct  ; auto-data
; SYM,0x055B,FromShotStruct  ; auto-data
; SYM,0x0563,HandleAlienShot  ; auto-data
; SYM,0x062F,FindInColumn  ; auto-data
; SYM,0x0644,ShotBlowingUp  ; auto-data
; SYM,0x0682,GameObj4  ; auto-data
; SYM,0x0707,L_0707  ; auto-code
; SYM,0x070C,D_070C  ; auto-data
; SYM,0x0765,WaitForStart  ; auto-data
; SYM,0x077F,L_077F  ; auto-code
; SYM,0x0798,NewGame  ; auto-data
; SYM,0x079B,L_079B  ; auto-code
; SYM,0x07F9,L_07F9  ; auto-code
; SYM,0x0804,L_0804  ; auto-code
; SYM,0x0814,L_0814  ; auto-code
; SYM,0x081F,L_081F  ; auto-code
; SYM,0x0849,L_0849  ; auto-code
; SYM,0x0854,D_0854  ; auto-data
; SYM,0x0857,L_0857  ; auto-code
; SYM,0x086D,L_086D  ; auto-code
; SYM,0x0872,L_0872  ; auto-code
; SYM,0x0878,L_0878  ; auto-code
; SYM,0x0883,D_0883  ; auto-data
; SYM,0x0886,GetAlRefPtr  ; auto-data
; SYM,0x088D,PromptPlayer  ; auto-data
; SYM,0x08A9,L_08A9  ; auto-code
; SYM,0x08BC,L_08BC  ; auto-code
; SYM,0x08CB,L_08CB  ; auto-code
; SYM,0x08D1,GetShipsPerCred  ; auto-data
; SYM,0x08D8,SpeedShots  ; auto-data
; SYM,0x08E4,L_08E4  ; auto-code
; SYM,0x08F1,D_08F1  ; auto-data
; SYM,0x08F3,PrintMessage  ; auto-data
; SYM,0x08FF,DrawChar  ; auto-data
; SYM,0x0913,TimeToSaucer  ; auto-data
; SYM,0x0929,L_0929  ; auto-code
; SYM,0x092E,L_092E  ; auto-code
; SYM,0x0935,L_0935  ; auto-code
; SYM,0x0948,L_0948  ; auto-code
; SYM,0x0958,L_0958  ; auto-code
; SYM,0x097C,AlienScoreValue  ; auto-data
; SYM,0x0988,AdjustScore  ; auto-data
; SYM,0x09AD,Print4Digits  ; auto-data
; SYM,0x09B2,DrawHexByte  ; auto-data
; SYM,0x09C5,L_09C5  ; auto-code
; SYM,0x09CA,L_09CA  ; auto-code
; SYM,0x09D6,ClearPlayField  ; auto-data
; SYM,0x09D9,L_09D9  ; auto-code
; SYM,0x09E8,L_09E8  ; auto-code
; SYM,0x09EF,L_09EF  ; auto-code
; SYM,0x0A13,L_0A13  ; auto-code
; SYM,0x0A33,L_0A33  ; auto-code
; SYM,0x0A3C,L_0A3C  ; auto-code
; SYM,0x0A47,L_0A47  ; auto-code
; SYM,0x0A52,L_0A52  ; auto-code
; SYM,0x0A59,L_0A59  ; auto-code
; SYM,0x0A5F,ScoreForAlien  ; auto-data
; SYM,0x0A7C,L_0A7C  ; auto-code
; SYM,0x0A80,Animate  ; auto-data
; SYM,0x0A85,L_0A85  ; auto-code
; SYM,0x0A93,PrintMessageDel  ; auto-data
; SYM,0x0A9E,L_0A9E  ; auto-code
; SYM,0x0AAB,SplashSquiggly  ; auto-data
; SYM,0x0AB1,OneSecDelay  ; auto-data
; SYM,0x0AB6,TwoSecDelay  ; auto-data
; SYM,0x0ABB,SplashDemo  ; auto-data
; SYM,0x0ABF,ISRSplTasks  ; auto-data
; SYM,0x0ACF,L_0ACF  ; auto-code
; SYM,0x0AD7,WaitOnDelay  ; auto-data
; SYM,0x0ADA,L_0ADA  ; auto-code
; SYM,0x0AE2,IniSplashAni  ; auto-data
; SYM,0x0AEA,L_0AEA  ; auto-code
; SYM,0x0B0B,L_0B0B  ; auto-code
; SYM,0x0B4A,L_0B4A  ; auto-code
; SYM,0x0B5D,L_0B5D  ; auto-code
; SYM,0x0B71,L_0B71  ; auto-code
; SYM,0x0B83,L_0B83  ; auto-code
; SYM,0x0B89,L_0B89  ; auto-code
; SYM,0x0BAE,L_0BAE  ; auto-code
; SYM,0x0BC3,L_0BC3  ; auto-code
; SYM,0x0BDA,L_0BDA  ; auto-code
; SYM,0x0BE8,L_0BE8  ; auto-code
; SYM,0x0BF1,L_0BF1  ; auto-code
; SYM,0x0BF7,MessageCorp  ; auto-data
; SYM,0x1400,DrawShiftedSprite  ; auto-data
; SYM,0x1424,EraseSimpleSprite  ; auto-data
; SYM,0x1427,L_1427  ; auto-code
; SYM,0x1439,DrawSimpSprite  ; auto-data
; SYM,0x1447,D_1447  ; auto-data
; SYM,0x1452,EraseShifted  ; auto-data
; SYM,0x1474,CnvtPixNumber  ; auto-data
; SYM,0x147C,RememberShields  ; auto-data
; SYM,0x147E,L_147E  ; auto-code
; SYM,0x1491,DrawSprCollision  ; auto-data
; SYM,0x14CB,ClearSmallSprite  ; auto-data
; SYM,0x14CC,L_14CC  ; auto-code
; SYM,0x14D8,PlayerShotHit  ; auto-data
; SYM,0x1504,CodeBug1  ; auto-data
; SYM,0x1530,L_1530  ; auto-code
; SYM,0x1538,AExplodeTime  ; auto-data
; SYM,0x1545,L_1545  ; auto-code
; SYM,0x154A,L_154A  ; auto-code
; SYM,0x1553,D_1553  ; auto-data
; SYM,0x1554,Cnt16s  ; auto-data
; SYM,0x155A,L_155A  ; auto-code
; SYM,0x1562,FindRow  ; auto-data
; SYM,0x156F,FindColumn  ; auto-data
; SYM,0x1579,L_1579  ; auto-code
; SYM,0x1581,GetAlienStatPtr  ; auto-data
; SYM,0x1590,WrapRef  ; auto-data
; SYM,0x1597,RackBump  ; auto-data
; SYM,0x15A9,L_15A9  ; auto-code
; SYM,0x15B7,L_15B7  ; auto-code
; SYM,0x15C5,L_15C5  ; auto-code
; SYM,0x15C7,L_15C7  ; auto-code
; SYM,0x15D2,D_15D2  ; auto-data
; SYM,0x15D3,DrawSprite  ; auto-data
; SYM,0x15D7,L_15D7  ; auto-code
; SYM,0x15F3,CountAliens  ; auto-data
; SYM,0x15F9,L_15F9  ; auto-code
; SYM,0x15FF,L_15FF  ; auto-code
; SYM,0x1611,GetPlayerDataPtr  ; auto-data
; SYM,0x1618,PlrFireOrDemo  ; auto-data
; SYM,0x1648,L_1648  ; auto-code
; SYM,0x1652,L_1652  ; auto-code
; SYM,0x1663,L_1663  ; auto-code
; SYM,0x166B,L_166B  ; auto-code
; SYM,0x166D,D_166D  ; auto-data
; SYM,0x1671,L_1671  ; auto-code
; SYM,0x168B,L_168B  ; auto-code
; SYM,0x168F,L_168F  ; auto-code
; SYM,0x1698,L_1698  ; auto-code
; SYM,0x16B7,L_16B7  ; auto-code
; SYM,0x16C9,L_16C9  ; auto-code
; SYM,0x16E6,L_16E6  ; auto-code
; SYM,0x16EE,L_16EE  ; auto-code
; SYM,0x170E,AShotReloadRate  ; auto-data
; SYM,0x171C,L_171C  ; auto-code
; SYM,0x1727,L_1727  ; auto-code
; SYM,0x172C,ShotSound  ; auto-data
; SYM,0x1739,L_1739  ; auto-code
; SYM,0x173E,D_173E  ; auto-data
; SYM,0x1740,TimeFleetSound  ; auto-data
; SYM,0x176D,L_176D  ; auto-code
; SYM,0x1775,FleetDelayExShip  ; auto-data
; SYM,0x1785,L_1785  ; auto-code
; SYM,0x178E,L_178E  ; auto-code
; SYM,0x17A4,L_17A4  ; auto-code
; SYM,0x17AA,L_17AA  ; auto-code
; SYM,0x17B4,SndOffExtPly  ; auto-data
; SYM,0x17C0,ReadInputs  ; auto-data
; SYM,0x17CA,L_17CA  ; auto-code
; SYM,0x17CD,CheckHandleTilt  ; auto-data
; SYM,0x17DC,L_17DC  ; auto-code
; SYM,0x1804,CtrlSaucerSound  ; auto-data
; SYM,0x1815,DrawAdvTable  ; auto-data
; SYM,0x1828,L_1828  ; auto-code
; SYM,0x1834,D_1834  ; auto-data
; SYM,0x1837,L_1837  ; auto-code
; SYM,0x183A,L_183A  ; auto-code
; SYM,0x1844,L_1844  ; auto-code
; SYM,0x184C,L_184C  ; auto-code
; SYM,0x1856,ReadPriStruct  ; auto-data
; SYM,0x1868,SplashSprite  ; auto-data
; SYM,0x1888,L_1888  ; auto-code
; SYM,0x1895,D_1895  ; auto-data
; SYM,0x1898,L_1898  ; auto-code
; SYM,0x189E,L_189E  ; auto-code
; SYM,0x18B8,L_18B8  ; auto-code
; SYM,0x18C0,L_18C0  ; auto-code
; SYM,0x18D4,init  ; auto-data
; SYM,0x18DF,L_18DF  ; auto-code
; SYM,0x18E7,L_18E7  ; auto-code
; SYM,0x18F1,L_18F1  ; auto-code
; SYM,0x18FA,SoundBits3On  ; auto-data
; SYM,0x1904,InitAliensP2  ; auto-data
; SYM,0x190A,PlyrShotAndBump  ; auto-data
; SYM,0x1910,CurPlyAlive  ; auto-data
; SYM,0x191A,DrawScoreHead  ; auto-data
; SYM,0x1925,L_1925  ; auto-code
; SYM,0x192B,L_192B  ; auto-code
; SYM,0x1931,DrawScore  ; auto-data
; SYM,0x193C,L_193C  ; auto-code
; SYM,0x1947,DrawNumCredits  ; auto-data
; SYM,0x1950,PrintHiScore  ; auto-data
; SYM,0x1956,DrawStatus  ; auto-data
; SYM,0x196B,L_196B  ; auto-code
; SYM,0x1971,L_1971  ; auto-code
; SYM,0x1979,L_1979  ; auto-code
; SYM,0x1982,L_1982  ; auto-code
; SYM,0x1986,D_1986  ; auto-data
; SYM,0x1988,L_1988  ; auto-code
; SYM,0x198B,D_198B  ; auto-data
; SYM,0x199A,CheckHiddenMes  ; auto-data
; SYM,0x19AC,L_19AC  ; auto-code
; SYM,0x19BE,MessageTaito  ; auto-data
; SYM,0x19D1,EnableGameTasks  ; auto-data
; SYM,0x19D3,L_19D3  ; auto-code
; SYM,0x19D7,DsableGameTasks  ; auto-data
; SYM,0x19DB,D_19DB  ; auto-data
; SYM,0x19DC,SoundBits3Off  ; auto-data
; SYM,0x19E6,DrawNumShips  ; auto-data
; SYM,0x19EC,L_19EC  ; auto-code
; SYM,0x19FA,L_19FA  ; auto-code
; SYM,0x1A06,CompYToBeam  ; auto-data
; SYM,0x1A32,BlockCopy  ; auto-data
; SYM,0x1A3B,ReadDesc  ; auto-data
; SYM,0x1A47,ConvToScr  ; auto-data
; SYM,0x1A4A,L_1A4A  ; auto-code
; SYM,0x1A5C,ClearScreen  ; auto-data
; SYM,0x1A5F,L_1A5F  ; auto-code
; SYM,0x1A69,RestoreShields  ; auto-data
; SYM,0x1A6B,L_1A6B  ; auto-code
; SYM,0x1A7F,RemoveShip  ; auto-data
; SYM,0x1A8B,L_1A8B  ; auto-code
; SYM,0x1A93,D_1A93  ; auto-data
; SYM,0x1AA1,ShotReloadRate  ; auto-data
; SYM,0x1AA6,MessageGOver  ; auto-data
; SYM,0x1ABA,MessageB1or2  ; auto-data
; SYM,0x1ACF,Message1Only  ; auto-data
; SYM,0x1AE4,MessageScore  ; auto-data
; SYM,0x1B70,MesssageP1  ; auto-data
; SYM,0x1BA0,AlienSprCYA  ; auto-data
; SYM,0x1BD0,AlienSprCYB  ; auto-data
; SYM,0x1C00,AlienSprA  ; auto-data
; SYM,0x1C30,AlienSprB  ; auto-data
; SYM,0x1C60,PlayerSprite  ; auto-data
; SYM,0x1C70,PlrBlowupSprites  ; auto-data
; SYM,0x1C90,PlayerShotSpr  ; auto-data
; SYM,0x1C91,ShotExploding  ; auto-data
; SYM,0x1C99,Message10Pts  ; auto-data
; SYM,0x1CA3,MessageAdv  ; auto-data
; SYM,0x1CB8,AReloadScoreTab  ; auto-data
; SYM,0x1CBC,MessageTilt  ; auto-data
; SYM,0x1CC0,AlienExplode  ; auto-data
; SYM,0x1CD0,SquiglyShot  ; auto-data
; SYM,0x1CDC,AShotExplo  ; auto-data
; SYM,0x1CE2,PlungerShot  ; auto-data
; SYM,0x1CEE,RollShot  ; auto-data
; SYM,0x1CFA,MessagePlayUY  ; auto-data
; SYM,0x1D00,ColFireTable  ; auto-data
; SYM,0x1D20,ShieldImage  ; auto-data
; SYM,0x1D54,SaucerScrTab  ; auto-data
; SYM,0x1D64,SpriteSaucer  ; auto-data
; SYM,0x1D7C,SpriteSaucerExp  ; auto-data
; SYM,0x1D94,SaucSoreStr  ; auto-data
; SYM,0x1DA0,AlienScores  ; auto-data
; SYM,0x1DA3,AlienStartTable  ; auto-data
; SYM,0x1DAB,MessagePlayY  ; auto-data
; SYM,0x1DAF,MessageInvaders  ; auto-data
; SYM,0x1DCF,AlienScoreTable  ; auto-data
; SYM,0x1DE0,MessageMyst  ; auto-data
; SYM,0x1DEA,Message30Pts  ; auto-data
; SYM,0x1DF4,Message20Pts  ; auto-data
; SYM,0x1E00,Characters  ; auto-data
; SYM,0x1F50,MessageP1or2  ; auto-data
; SYM,0x1F62,Message1Coin  ; auto-data
; SYM,0x1F74,DemoCommands  ; auto-data
; SYM,0x1F80,AlienSprCA  ; auto-data
; SYM,0x1F90,MessageCoin  ; auto-data
; SYM,0x1F9C,CreditTable  ; auto-data
; SYM,0x1FA9,MessageCredit  ; auto-data
; SYM,0x1FB0,AlienSprCB  ; auto-data
; SYM,0x1FE1,Message2Coins  ; auto-data
; SYM,0x1FF3,MessagePush  ; auto-data
