._CPU = 6502

; Hardware definitions
.include stella.asm

; RAM Usage
.TMP0      = 128
.TMP1      = 129
.TMP2      = 130
.PLAYR0Y   = 131
.PLAYR1Y   = 132
.MUS_TMP0  = 133
.MUS_TMP1  = 134
.SCANCNT   = 135
.MODE      = 136
.WALL_INC  = 137
.WALLCNT   = 138
.WALLDELY  = 139
.WALLDELYR = 140
.ENTROPYA  = 141
.ENTROPYB  = 142
.ENTROPYC  = 143
.DEBOUNCE  = 144
.WALLDRELA = 145
.WALLDRELB = 146
.WALLDRELC = 147
.WALLSTART = 148
.WALLHEI   = 149
.GAPBITS   = 150
.SCORE_PF1 = 151
.SCORE_PF2 = 157
.MUSADEL   = 163
.MUSAIND   = 164
.MUSAVOL   = 165
.MUSBDEL   = 166
.MUSBIND   = 167
.MUSBVOL   = 168

0xF000:
main:
    SEI                       ; Turn off interrupts
    CLD                       ; Clear the "decimal" flag
    LDX      #0xFF            ; Set stack ...
    TXS                       ; ... to the end of RAM
    JSR      INIT             ; Initialize game environment
    JSR      INIT_SELMODE     ; Start out in SELECT-MODE

VIDEO_KERNEL:

    LDA      #2               ; D1 bit ON
    STA      WSYNC            ; Wait for the end of the current line
    STA      VBLANK           ; Turn the electron beam off
    STA      WSYNC            ; Wait for all ...
    STA      WSYNC            ; ... the electrons ...
    STA      WSYNC            ; ... to drain out.
    STA      VSYNC            ; Trigger the vertical sync signal
    STA      WSYNC            ; Hold the vsync signal for ...
    STA      WSYNC            ; ... three ...
    STA      WSYNC            ; ... scanlines
    STA      HMOVE            ; Tell hardware to move all game objects
    LDA      #0               ; D1 bit OFF
    STA      VSYNC            ; Release the vertical sync signal
    LDA      #43              ; Set timer to 43*64 = 2752 machine ...
    STA      TIM64T           ; ... cycles 2752/(228/3) = 36 scanlines

    ;  ***** LENGTHY GAME LOGIC PROCESSING BEGINS HERE *****

    ;  Do one of 3 routines while the beam travels back to the top
    ;  0 = Game Over processing
    ;  1 = Playing-Game processing
    ;  2 = Selecting-Game processing

    INC      ENTROPYA         ; Counting video frames as part of the random number
    LDA      MODE             ; What are we doing between frames?

    CMP      #0               ; Mode is ...
    BEQ      DoGameOverMode   ; ... "game over"
    CMP      #1               ; Mode is ...
    BEQ      DoPlayMode       ; ... "game play"
    JSR      SELMODE          ; Mode is "select game"
    JMP      DrawFrame        ; Continue to the visible screen area

DoPlayMode:
    JSR      PLAYMODE         ; Playing-game processing
    JMP      DrawFrame        ; Continue to the visible screen area

DoGameOverMode:
    JSR      GOMODE           ; Game-over processing

    ;  ***** LENGTHY GAME LOGIC PROCESSING ENDS HERE *****

DrawFrame:
    LDA      INTIM            ; Wait for ...
    CMP      #0               ; ... the visible area ...
    BNE      DrawFrame        ; ... of the screen

    STA      WSYNC            ; 37th scanline
    LDA      #0               ; Turn the ...
    STA      VBLANK           ; ... electron beam back on

    LDA      #0               ; Zero out ...
    STA      SCANCNT          ; ... scanline count ...
    STA      TMP0             ; ... and all ...
    STA      TMP1             ; ... returns ...
    STA      TMP2             ; ... expected ...
    TAX                       ; ... to come from ...
    TAY                       ; ... BUILDROW

    STA      CXCLR            ; Clear collision detection

DrawVisibleRows:

    LDA      TMP0             ; Get A ready (PF0 value)
    STA      WSYNC            ; Wait for very start of row
    STX      GRP0             ; Player 0 -- in X
    STY      GRP1             ; Player 1 -- in Y
    STA      PF0              ; PF0      -- in TMP0 (already in A)
    LDA      TMP1             ; PF1      -- in TMP1
    STA      PF1              ; ...
    LDA      TMP2             ; PP2      -- in TMP2
    STA      PF2              ; ...

    JSR      BUILDROW         ; This MUST take through to the next line

    INC      SCANCNT          ; Next scan line
    LDA      SCANCNT          ; Do 109*2 = 218 lines
    CMP      #109             ; All done?
    BNE      DrawVisibleRows  ; No ... get all the visible rows

    ;  END VISIBLE PART OF FRAME

    LDA      #0               ; Turn off electron beam
    STA      WSYNC            ; Next scanline
    STA      PF0              ; Play field 0 off
    STA      GRP0             ; Player 0 off
    STA      GRP1             ; Player 1 off
    STA      PF1              ; Play field 1 off
    STA      PF2              ; Play field 2 off
    STA      WSYNC            ; Next scanline

    JMP      VIDEO_KERNEL

BUILDROW:

    LDA      SCANCNT          ; Where are we on the screen?

    CMP      #6               ; If we are in the ...
    BCC      ShowScore        ; ... score area

    AND      #7               ; Lower 3 bits as an index again
    TAY                       ; Using Y to lookup graphics
    LDA      GR_PLAYER,Y      ; Get the graphics (if enabled on this row)
    TAX                       ; Hold it (for return as player 0)
    TAY                       ; Hold it (for return as player 1)
    LDA      SCANCNT          ; Scanline count again
    LSR      A                ; This time ...
    LSR      A                ; ... we divide ...
    LSR      A                ; ... by eight (8 rows in picture)

    CMP      PLAYR0Y          ; Scanline group of the P0 object?
    BEQ      ShowP0           ; Yes ... keep the picture
    LDX      #0               ; Not time for Player 0 ... no graphics
ShowP0:

    CMP      PLAYR1Y          ; Scanline group of the P1 object?
    BEQ      ShowP1           ; Yes ... keep the picture
    LDY      #0               ; Not time for Player 0 ... no graphics
ShowP1:

    LDA      WALLSTART        ; Calculate ...
    CLC                       ; ... the bottom ...
    ADC      WALLHEI          ; ... of ...
    STA      TMP0             ; ... the wall

    LDA      SCANCNT          ; Scanline count

    CMP      WALLSTART        ; Past upper part of wall?
    BCC      NoWall           ; No ... skip it
    CMP      TMP0             ; Past lower part of wall
    BCS      NoWall           ; Yes ... skip it

    ;  The wall is on this row
    LDA      WALLDRELA        ; Draw wall ...
    STA      TMP0             ; ... by transfering ...
    LDA      WALLDRELB        ; ... playfield ...
    STA      TMP1             ; ... patterns ...
    LDA      WALLDRELC        ; ... to ...
    STA      TMP2             ; ... return area
    RTS                       ; Done

NoWall:
    ;  The wall is NOT on this row
    LDA      #0               ; No walls on this row
    STA      TMP0             ; ... clear ...
    STA      TMP1             ; ... out ...
    STA      TMP2             ; ... the playfield
    RTS                       ; Done

ShowScore:
    AND      #7               ; OLine=182  Only need the lower 3 bits
    TAY                       ; OLine=183  Soon to be an index into a list

    ;  At this point, the beam is past the loading of the
    ;  playfield for the left half. We want to make sure
    ;  that the right half of the playfield is off, so do that
    ;  now.

    LDX      #0               ; Blank bit pattern
    STX      TMP0             ; This will always be blank
    STX      PF1              ; Turn off playfield ...
    STX      PF2              ; ... for right half of the screen

    TAX                       ; Another index
    LDA      SCORE_PF1,Y      ; Lookup the PF1 graphics for this row
    STA      TMP1             ; Return it to the caller
    TAY                       ; We'll need this value again in a second
    LDA      SCORE_PF2,X      ; Lookup the PF2 graphics for this row
    STA      TMP2             ; Return it to the caller

    STA      WSYNC            ; Now on the next row

    STY      PF1              ; Repeat the left-side playfield ...
    STA      PF2              ; ... onto the new row

    LDA      SCORE_PF2,X      ; Kill some time waiting for the ...
    LDA      SCORE_PF2,X      ; ... beam to pass the left half ...
    LDA      SCORE_PF2,X      ; ... of the playfield again
    LDA      SCORE_PF2,X      ; ...
    LDA      SCORE_PF2,X      ; ...
    LDA      SCORE_PF2,X      ; ...

    LDX      #0               ; Return 0 (off) for player 0 ...
    LDY      #0               ; ... and player 1

    ;  The beam is past the left half of the field again.
    ;  Turn off the playfield.

    STX      PF1              ; 0 to PF1 ...
    STX      PF2              ; ... and PF2
    RTS                       ;  Done

INIT:
    ;  This function is called ONCE at power-up/reset to initialize various
    ;  game settings and variables.
                                           
    LDA      #64              ; Wall is ...
    STA      COLUPF           ; ... redish
    LDA      #126             ; P0 is ...
    STA      COLUP0           ; ... white
    LDA      #0               ; P1 ...
    STA      COLUP1           ; ... black
                                           
    LDA      #5               ; Right half of playfield is reflection of left ...
    STA      CTRLPF           ; ... and playfield is on top of players

    ; TODO other hardware inits here
                                           
    LDX      #4               ; Player 0 position count
    LDY      #3               ; Player 1 position count
    STA      WSYNC            ; Get a fresh scanline
                                           
TimeP0Pos:
    DEX                       ; Kill time while the beam moves ...
    CPX      #0               ; ... to desired ...
    BNE      TimeP0Pos        ; ... position
    STA      RESP0            ; Mark player 0's X position
                                           
TimeP1Pos:
    DEY                       ; Kill time while the beam moves ...
    CPY      #0               ; ... to desired ...
    BNE      TimeP1Pos        ; ... position
    STA      RESP1            ; Mark player 1's X position

    JSR      EXPERTISE        ; Initialize the players' Y positions base on expert-settings
                                           
    LDA      #10              ; Wall is ...
    STA      WALLHEI          ; ... 10 double-scanlines high
                                           
    LDA      #0               ; Set score to ...
    STA      WALLCNT          ; ... 0
    JSR      MAKE_SCORE       ; Blank the score digits
    LDA      #0               ; Blank bits ...
    STA      SCORE_PF2+5      ; ... on the end of each ...
    STA      SCORE_PF1+5      ; ... digit pattern
                                           
    JSR      ADJUST_DIF       ; Initialize the wall parameters
    JSR      NEW_GAPS         ; Build the wall's initial gap
                                           
    LDA      #112             ; Set wall position off bottom ...
    STA      WALLSTART        ; ... to force a restart on first move
                                           
    LDA      #0               ; Zero out ...
    STA      HMP0             ; ... player 0 motion ...
    STA      HMP1             ; ... and player 1 motion
                                           
    RTS                       ; Done

INIT_PLAYMODE:

    ;  This function initializes the game play mode

    LDA      #192             ; Background is ...
    STA      COLUBK           ; ... greenish
    LDA      #1               ; Game mode is ...
    STA      MODE             ; ... SELECT
    LDA      #255             ; Restart wall score to ...
    STA      WALLCNT          ; ... 0 on first move
    LDA      #112             ; Force wall to start ...
    STA      WALLSTART        ; ... over on first move
    JSR      INIT_MUSIC       ; Initialize the music
    RTS                       ; Done

PLAYMODE:

    ;  This function is called once per frame to process the main game play.


    JSR      SEL_RESET_CHK    ; Check to see if Reset/Select has changed

    CMP      #0               ; Is select pressed?
    BEQ      NoSelect         ; No ... skip
    STX      DEBOUNCE         ; Restore the old value ...
    JSR      INIT_SELMODE     ; ... and let select-mode process the toggle
    RTS                       ; Done

NoSelect:
    JSR      PROCESS_MUSIC    ; Process any playing music
    JSR      MOVE_WALLS       ; Move the walls

    CMP      #1               ; Wall on first row?
    BNE      NoFirst          ; No ... move on
    INC      WALLCNT          ; Bump the score
    JSR      ADJUST_DIF       ; Change the wall parameters based on score
    LDA      WALLCNT          ; Change the ...
    JSR      MAKE_SCORE       ; ... score pattern
    JSR      NEW_GAPS         ; Calculate the new gap position

NoFirst:
     LDA      CXP0FB          ; Player 0 collision with playfield
     STA      TMP0            ; Hold it
     LDA      CXP1FB          ; Player 1 collision with playfield
     ORA      TMP0            ; Did either ...
     AND      #128            ; ... player hit ...
     CMP      #0              ; ... wall?
     BEQ      NoHit           ; No ... move on
     JSR      INIT_GOMODE     ; Go to Game-Over mode
     RTS                      ; Done

NoHit:
     LDA      SWCHA           ; Joystick
     AND      #128            ; Player 0 ...
     CMP      #0              ; ... moving left?
     BEQ      MoveP0Left      ; Yes ... move left
     LDA      SWCHA           ; Joystick
     AND      #64             ; Player 0 ...
     CMP      #0              ; ... moving right?
     BEQ      MoveP0Right     ; Yes ... move right
     LDA      #0              ; Not moving value
     JMP      SetMoveP0       ; Don't move the player
MoveP0Right:
     LDA      #16             ; +1
     JMP      SetMoveP0       ; Set HMP0
MoveP0Left:
     LDA      #240            ; -1
SetMoveP0:
     STA      HMP0            ; New movement value P0

     LDA      SWCHA           ; Joystick
     AND      #8              ; Player 1 ...
     CMP      #0              ; ... moving left?
     BEQ      MoveP1Left      ; Yes ... move left
     LDA      SWCHA           ; Joystick
     AND      #4              ; Player 0 ...
     CMP      #0              ; ... moving right?
     BEQ      MoveP1Right     ; Yes ... move right
     LDA      #0              ; Not moving value
     JMP      SetMoveP1       ; Don't move the player
MoveP1Right:
     LDA      #16             ; +1
     JMP      SetMoveP1       ; Set HMP0
MoveP1Left:
     LDA      #240            ; -1
SetMoveP1:
     STA      HMP1            ; New movement value P1

     RTS                      ; Done

INIT_SELMODE:

     ;  This function initializes the games SELECT-MODE

     LDA      #0              ; Turn off ...
     STA      AUDV0           ; ... all ...
     STA      AUDV1           ; ... sound
     LDA      #200            ; Background ...
     STA      COLUBK          ; ... greenish bright
     LDA      #2              ; Now in ...
     STA      MODE            ; SELECT game mode
     RTS                      ; Done


SELMODE:

     ;  This function is called once per frame to process the SELECT-MODE.
     ;  The wall moves here, but doesn't change or collide with players.
     ;  This function selects between 1 and 2 player game.

     JSR      MOVE_WALLS       ; Move the walls
     JSR      SEL_RESET_CHK    ; Check the reset/select switches
     CMP      #1               ; RESET button?
     BEQ      SelStartGame     ; Yes ... start game
     CMP      #3               ; RESET and SELECT?
     BEQ      SelStartGame     ; Yes ... start game
     CMP      #2               ; Select only?
     BNE      SelExp           ; No ... stay in this mode
     LDA      PLAYR1Y          ; Select toggled. Get player 1 Y coordinate
     CMP      #255             ; 2nd player on the screen?
     BEQ      SelP1On          ; No ... toggle it on
     LDA      #255             ; Yes ...
     STA      PLAYR1Y          ; ... toggle it off
     JMP      SelExp           ; Move to expertise
SelP1On:
     LDA      #12              ; Y coordinate
     STA      PLAYR1Y          ; On screen now
     JMP      SelExp           ; Move to expertise

SelStartGame:
     JSR      INIT_PLAYMODE    ; Reset toggled ... start game
SelExp:
     JSR      EXPERTISE        ; Adjust both players for pro settings
     RTS                       ; Done

INIT_GOMODE:

     ;  This function initializes the GAME-OVER game mode.

     STA      HMCLR            ; Stop both players from moving
     LDA      CXP0FB           ; P0 collision ...
     AND      #128             ; ... with wall
     CMP      #0               ; Did P0 hit the wall?
     BNE      GoCheckP1        ; Yes ... leave it at bottom
     LDA      #2               ; No ... move player 0 ...
     STA      PLAYR0Y          ; ... up the screen to show win

GoCheckP1:
     LDA      CXP1FB           ; P1 collision ...
     AND      #128             ; ... with wall
     CMP      #0               ; Did P1 hit the wall?
     BNE      GoP1Hit          ; Yes ... leave it at the bottom
     LDA      PLAYR1Y          ; Is P1 even ...
     CMP      #255             ; ... on the screen (2 player game?)
     BEQ      GoP1Hit          ; No ... skip it
     LDA      #2               ; Player 1 is onscreen and didn't collide ...
     STA      PLAYR1Y          ; ... move up the screen to show win

GoP1Hit:
     LDA      #0               ; Going to ...
     STA      MODE             ; ... game-over mode
     STA      AUDV0            ; Turn off any ...
     STA      AUDV1            ; ... sound
     JSR      INIT_GO_FX       ; Initialize sound effects
     RTS                       ; Done

GOMODE:

     ; This function is called every frame to process the game
     ; over sequence. When the sound effect has finished, the
     ; game switches to select mode.

     JSR      PROCESS_GO_FX    ; Process the sound effects
     CMP      #0               ; Effects still running?
     BEQ      GoKeepGoing      ; Yes ... let them run
     JSR      INIT_SELMODE     ; When effect is over, go to select mode
GoKeepGoing:
     RTS                       ; Done

MOVE_WALLS:

     ;  This function moves the wall down the screen and back to position 0
     ;  when it reaches (or passes) 112.

     DEC      WALLDELY         ; Wall motion timer
     LDA      WALLDELY         ; Time to ...
     CMP      #0               ; ... move the wall?
     BNE      WallDone         ; No ... leave it alone
     LDA      WALLDELYR        ; Reset the ...
     STA      WALLDELY         ; ... delay count
     LDA      WALLSTART        ; Current wall position
     CLC                       ; Increment ...
     ADC      WALL_INC         ; ... wall position
     CMP      #112             ; At the bottom?
     BCC      WallOK           ; No ... leave it alone
     LDA      #0               ; Else restart ...
     STA      WALLSTART        ; ... wall at top of screen
     LDA      #1               ; Return flag that wall DID restart
     RTS                       ; Done
WallOK:
     STA      WALLSTART        ; Store new wall position
WallDone:
     LDA      #0               ; Return flag that wall did NOT restart
     RTS                       ; Done


NEW_GAPS:

     ;  This function builds the PF0, PF1, and PF2 graphics for a wall
     ;  with the gap pattern (GAPBITS) placed at random in the 20 bit
     ;  area.

     LDA      #255             ; Start with ...
     STA      WALLDRELA        ; ... solid wall in PF0 ...
     STA      WALLDRELB        ; ... and PF1
     LDA      GAPBITS          ; Store the gap pattern ...
     STA      WALLDRELC        ; ... in PF2

     LDA      ENTROPYA         ; Get ...
     ADC      ENTROPYB         ; ... a randomish ...
     ADC      ENTROPYC         ; ... number ...
     STA      ENTROPYC         ; Update the random seed
     AND      #15              ; 0 to 15
     CMP      #12              ; Too far to the right?
     BEQ      GapOK            ; No ... 12 is OK
     BCC      GapOK            ; No ... less than 12 is OK
     SBC      #9               ; Back up 9

GapOK:
     CMP      #0               ; Gap already at far left?
     BEQ      GapDone          ; Yes ... done
     SEC                       ; Roll gap ...
     ROR      WALLDRELC        ; ... left ...
     ROL      WALLDRELB        ; ... desired ...
     ROR      WALLDRELA        ; ... times ...
     SEC                       ; All rolls ...
     SBC      #1               ; ... done?
     JMP      GapOK            ; No ... do them all
GapDone:
     RTS                       ; New wall pattern is ready

MAKE_SCORE:

     ;  This function builds the PF1 and PF2 graphics rows for
     ;  the byte value passed in A. The current implementation is
     ;  two-digits only ... PF2 is blank.

     LDX      #0               ; 100's digit
     LDY      #0               ; 10's digit

Count100s:
     CMP      #100             ; Need another 100s digit?
     BCC      Count10s         ; No ... move on to 10s
     INX                       ; Count ...
     SEC                       ; ... value
     SBC      #100             ; Take off this 100
     JMP      Count100s        ; Keep counting
Count10s:
     CMP      #10              ; Need another 10s digit?
     BCC      CountDone        ; No ... got all the tens
     INY                       ; Count ...
     SEC                       ; ... value
     SBC      #10              ; Take off this 10
     JMP      Count10s         ; Keep counting

CountDone:
     ASL      A                ; One's digit ...
     ASL      A                ; ... *8 ....
     ASL      A                ; ... to find picture
     TAX                       ; One's digit picture to X
     TYA                       ; Now the 10's digit
     ASL      A                ; Multiply ...
     ASL      A                ; ... by 8 ...
     ASL      A                ; ... to find picture
     TAY                       ; 10's picture in Y

     LDA      DIGITS,Y         ; Get the 10's digit
     AND      #0xF0            ; Upper nibble
     STA      SCORE_PF1        ; Store left side
     LDA      DIGITS,X         ; Get the 1's digit
     AND      #0x0F            ; Lower nibble
     ORA      SCORE_PF1        ; Put left and right half together
     STA      SCORE_PF1        ; And store image

     ; We have plenty of code space. Time and registers are at a premium.
     ; So copy/past the code for each row

     LDA      DIGITS+1,Y       ; Repeat for 2nd line of picture ...
     AND      #0xF0            ; ...
     STA      SCORE_PF1+1      ; ...
     LDA      DIGITS+1,X       ; ...
     AND      #15              ; ...
     ORA      SCORE_PF1+1      ; ...
     STA      SCORE_PF1+1      ; ...

     LDA      DIGITS+2,Y       ; Repeat for 3nd line of picture
     AND      #0xF0            ; ...
     STA      SCORE_PF1+2      ; ...
     LDA      DIGITS+2,X       ; ...
     AND      #0x0F            ; ...
     ORA      SCORE_PF1+2      ; ...
     STA      SCORE_PF1+2      ; ...

     LDA      DIGITS+3,Y       ; Repeat for 4th line of picture
     AND      #0xF0            ; ...
     STA      SCORE_PF1+3      ; ...
     LDA      DIGITS+3,X       ; ...
     AND      #0x0F            ; ...
     ORA      SCORE_PF1+3      ; ...
     STA      SCORE_PF1+3      ; ...

     LDA      DIGITS+4,Y       ; Repeat for 5th line of picture
     AND      #0xF0            ; ...
     STA      SCORE_PF1+4      ; ...
     LDA      DIGITS+4,X       ; ...
     AND      #0x0F            ; ...
     ORA      SCORE_PF1+4      ; ...
     STA      SCORE_PF1+4      ; ...

     LDA      #0               ; For now ...
     STA      SCORE_PF2        ; ... there ...
     STA      SCORE_PF2+1      ; ... is ...
     STA      SCORE_PF2+2      ; ... no ...
     STA      SCORE_PF2+3      ; ... 100s ...
     STA      SCORE_PF2+4      ; ... digit drawn

     RTS                       ; Done

EXPERTISE:
                                           
     ;  This function changes the Y position of the players based on the
     ;  position of their respective pro/novice switches. The player 1
     ;  position is NOT changed if the mode is a single-player game.
                                           
     LDA      SWCHB            ; Check P0 ...
     AND      #0x40            ; ... pro/novice settings
     CMP      #0               ; Amateur?
     BEQ      ExpP0Ama         ; Yes ... near the bottom of screen
     LDA      #8               ; Pro ... near the top
     JMP      ExpP1            ; Store and check P0
ExpP0Ama:
     LDA      #12              ; near the bottom

ExpP1:
     STA      PLAYR0Y          ; Player 0 Y coordinate
                                           
     LDX      PLAYR1Y          ; Is P1 on ...
     CPX      #255             ; ... the screen?
     BEQ      ExpNoP1          ; No ... skip all this
     LDA      SWCHB            ; Check P1 ...
     AND      #0x80            ; ... pro/novice settings
     CMP      #0               ; Amateur?
     BEQ      ExpP1Ama         ; Yes ... near the bottom of the screen
     LDX      #8               ; Pro ... near the top
     JMP      ExpDone          ; Store and out
ExpP1Ama:
     LDX      #12              ; Novice ... near the bottom
ExpDone:
     STX      PLAYR1Y          ; Player 1 Y coordinate
ExpNoP1:
     RTS                       ; Done

ADJUST_DIF:
                                           
     ;  This function adjusts the wall game difficulty values based on the
     ;  current score. The music can also change with the difficulty. A single
     ;  table describes the new values and when they take effect.

     LDX      #0               ; Starting at index 0
                                           
AdjNextRow:
     LDA      SKILL_VALUES,X   ; Get the score match
     CMP      #255             ; At the end of the table?
     BNE      AdjCheckTable    ; No ... check this row
     RTS                       ; End of the table ... leave it alone
AdjCheckTable:
     CMP      WALLCNT          ; Is this our row?
     BNE      AdjBump          ; No ... bump to next
     INX                       ; Copy ...
     LDA      SKILL_VALUES,X   ; ... new ...
     STA      WALL_INC         ; ... wall increment
     INX                       ; Copy ...
     LDA      SKILL_VALUES,X   ; ... new ...
     STA      WALLDELY         ; ... wall ...
     STA      WALLDELYR        ; ... delay
     INX                       ; Copy ...
     LDA      SKILL_VALUES,X   ; ... new ...
     STA      GAPBITS          ; ... gap pattern
     INX                       ; Copy ...
     LDA      SKILL_VALUES,X   ; ... new ...
     STA      MUSAIND          ; ... MusicA index
     INX                       ; Copy ...
     LDA      SKILL_VALUES,X   ; ... new ...
     STA      MUSBIND          ; ... MusicB index
     LDA      #1               ; Force ...
     STA      MUSADEL          ; ... music to ...
     STA      MUSBDEL          ; ... start new
     RTS                       ; Done
AdjBump:
     INX                       ; Move ...
     INX                       ; ... X ...
     INX                       ; ... to ...
     INX                       ; ... next ...
     INX                       ; ... row of ...
     INX                       ; ... table
     JMP      AdjNextRow       ; Try next row
                                           
                                           
SEL_RESET_CHK:
                                           
     ;  This function checks for changes to the reset/select
     ;  switches and debounces the transitions.
     ;  xxxxxxSR (Select, Reset)
                                           
     LDX      DEBOUNCE         ; Get the last value
     LDA      SWCHB            ; New value
     AND      #3               ; Only need bottom 2 bits
     CMP      DEBOUNCE         ; Same as before?
     BEQ      SelDebounce      ; Yes ... return nothing changed
     STA      DEBOUNCE         ; Hold new last value
     EOR      #255             ; Active low to active high
     AND      #3               ; Only need select/reset
     RTS                       ; Return changes
SelDebounce:
     LDA      #0               ; Return 0 ...
     RTS                       ; ... nothing changed

                                           
INIT_MUSIC:

     ;  This function initializes the hardware and temporaries
     ;  for 2-channel music

     LDA      #6               ; Audio control ...
     STA      AUDC0            ; ... to pure ...
     STA      AUDC1            ; ... tones
     LDA      #0               ; Turn off ...
     STA      AUDV0            ; ... all ...
     STA      AUDV1            ; ... sound
     STA      MUSAIND          ; Music pointers ...
     STA      MUSBIND          ; ... to top of data
     LDA      #1               ; Force ...
     STA      MUSADEL          ; ... music ...
     STA      MUSBDEL          ; ... reload
     LDA      #15              ; Set volume levels ...
     STA      MUSAVOL          ; ... to ...
     STA      MUSBVOL          ; ... maximum
     RTS                       ; Done

PROCESS_MUSIC:
                                           
     ;  This function is called once per frame to process the
     ;  2 channel music. Two tables contain the commands/notes
     ;  for individual channels. This function changes the
     ;  notes at the right time.

     DEC      MUSADEL          ; Current note on Channel A ended?
     BNE      MusDoB           ; No ... let it play
                                           
MusChanA:
     LDX      MUSAIND          ; Voice-A index
     LDA      MUSICA,X         ; Get the next music command
     CMP      #0               ; Jump?
     BEQ      MusCmdJumpA      ; Yes ... handle it
     CMP      #1               ; Control?
     BEQ      MusCmdCtrlA      ; Yes ... handle it
     CMP      #2               ; Volume?
     BNE      MusCmdToneA      ; No ... must be a note
     INX                       ; Point to volume value
     INC      MUSAIND          ; Bump the music pointer
     LDA      MUSICA,X         ; Get the volume value
     INC      MUSAIND          ; Bump the music pointer
     STA      MUSAVOL          ; Store the new volume value
     JMP      MusChanA         ; Keep processing through a tone

MusCmdCtrlA:
     INX                       ; Point to the control value
     INC      MUSAIND          ; Bump the music pointer
     LDA      MUSICA,X         ; Get the control value
     INC      MUSAIND          ; Bump the music pointer
     STA      AUDC0            ; Store the new control value
     JMP      MusChanA         ; Keep processing through a tone

MusCmdJumpA:
     INX                       ; Point to jump value
     TXA                       ; X to ...
     TAY                       ; ... Y (pointer to jump value)
     INX                       ; Point one past jump value
     TXA                       ; Into A so we can subtract
     SEC                       ; New ...
     SBC      MUSICA,Y         ; ... index
     STA      MUSAIND          ; Store it
     JMP      MusChanA         ; Keep processing through a tone

MusCmdToneA:
     LDY      MUSAVOL          ; Get the volume
     AND      #0x1F            ; Lower 5 bits are frequency
     CMP      #0x1F            ; Is this a silence?
     BNE      MusNoteA         ; No ... play it
     LDY      #0               ; Frequency of 31 flags silence
MusNoteA:
     STA      AUDF0            ; Store the frequency
     STY      AUDV0            ; Store the volume
     LDA      MUSICA,X         ; Get the note value again
     INC      MUSAIND          ; Bump to the next command
     ROR      A                ; The upper ...
     ROR      A                ; ... three ...
     ROR      A                ; ... bits ...
     ROR      A                ; ... hold ...
     ROR      A                ; ... the ...
     AND      #7               ; ... delay
     CLC                       ; No accidental carry
     ROL      A                ; Every delay tick ...
     ROL      A                ; ... is *4 frames
     STA      MUSADEL          ; Store the note delay

MusDoB:
                                           
     DEC      MUSBDEL
     BNE      MusDoDone
                                           
MusChanB:
     LDX      MUSBIND
     LDA      MUSICB,X
     CMP      #0
     BEQ      MusCmdJumpB
     CMP      #1
     BEQ      MusCmdCtrlB
     CMP      #2
     BNE      MusCmdToneB
     INX
     INC      MUSBIND
     LDA      MUSICB,X
     INC      MUSBIND
     STA      MUSBVOL
     JMP      MusChanB

MusCmdCtrlB:
     INX
     INC      MUSBIND
     LDA      MUSICB,X
     INC      MUSBIND
     STA      AUDC1
     JMP      MusChanB

MusCmdJumpB:
     INX
     TXA
     TAY
     INX
     TXA
     SEC
     SBC      MUSICB,Y
     STA      MUSBIND
     JMP      MusChanB

MusCmdToneB:
     LDY      MUSBVOL
     AND      #0x1F
     CMP      #0x1F
     BNE      MusNoteB
     LDY      #0
MusNoteB:
     STA      AUDF1
     STY      AUDV1
     LDA      MUSICB,X
     INC      MUSBIND
     ROR      A
     ROR      A
     ROR      A
     ROR      A
     ROR      A
     AND      #7
     CLC
     ROL      A
     ROL      A
     STA      MUSBDEL

MusDoDone:
     RTS                       ; Done


INIT_GO_FX:
                                           
     ;  This function initializes the hardware and temporaries
     ;  to play the soundeffect of a player hitting the wall
                                           
     LDA      #5               ; Set counter for frame delay ...
     STA      MUS_TMP1         ; ... between frequency change
     LDA      #3               ; Tone type ...
     STA      AUDC0            ; ... poly tone
     LDA      #15              ; Volume A ...
     STA      AUDV0            ; ... to max
     LDA      #0               ; Volume B ...
     STA      AUDV1            ; ... silence
     LDA      #240             ; Initial ...
     STA      MUS_TMP0         ; ... sound ...
     STA      AUDF0            ; ... frequency
     RTS                       ; Done

PROCESS_GO_FX:
                                           
     ;  This function is called once per scanline to play the
     ;  soundeffects of a player hitting the wall.

     DEC      MUS_TMP1         ; Time to change the frequency?
     BNE      FxRun            ; No ... let it run
     LDA      #5               ; Reload ...
     STA      MUS_TMP1         ; ... the frame count
     INC      MUS_TMP0         ; Increment ...
     LDA      MUS_TMP0         ; ... the frequency divisor
     STA      AUDF0            ; Change the frequency
     CMP      #0
     BNE      FxRun
     LDA      #1               ; All done ... return 1
     RTS                       ; Done
FxRun:
     LDA      #0               ; Keep playing
     RTS                       ; Done

	 ;  Music commands for Channel A and Channel B

	 ;  A word on music and wall timing ...

	 ;  Wall moves between scanlines 0 and 111 (112 total)

	 ;  Wall-increment   frames-to-top
	 ;       3             336
	 ;       2             224
	 ;       1             112
	 ;      0.5             56  ; Ah ... but we are getting one less

	 ;  Each tick is multiplied by 4 to yield 4 frames per tick
	 ;  32 ticks/song = 32*4 = 128 frames / song

	 ;  We want songs to start with wall at top ...

	 ;  Find the least-common-multiple
	 ;  336 and 128 : 2688 8 walls, 21 musics
	 ;  224 and 128 :  896 4 walls,  7 musics
	 ;  112 and 128 :  896 8 walls,  7 musics
	 ;   56 and 128 :  896 16 walls, 7 musics

	 ;  Wall moving every other gives us 112*2=224 scanlines
	 ;  Song and wall are at start every 4
	 ;  1 scanline, every 8
	 ;  Wall delay=3 gives us 128*3=336 scanlines 2

.MUSCMD_JUMP      =     0      ; Music command value for JUMP
.MUSCMD_CONTROL   =     1      ; Music command value for CONTROL
.MUSCMD_VOLUME    =     2      ; Music command value for VOLUME
.MUS_REST         =     31     ; Frequency value for silence
.MUS_DEL_1        =     32*1   ; Note duration 1
.MUS_DEL_2        =     32*2   ; Note duration 2
.MUS_DEL_3        =     32*3   ; Note duration 3
.MUS_DEL_4        =     32*4   ; Note duration 4
                                           
MUSICA:
                                           
MA_SONG_1:
                                           
     .byte  MUSCMD_CONTROL, 12
     .byte  MUSCMD_VOLUME,  15 ; Volume (full)
                                           
MA1_01:
     .byte  MUS_DEL_3  +  15
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_3  +  15
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  7
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  7
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_2  +  MUS_REST
     .byte  MUS_DEL_1  +  8
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_4  +  MUS_REST
     .byte  MUS_DEL_2  +  17
     .byte  MUS_DEL_2  +  MUS_REST
     .byte  MUS_DEL_2  +  17
     .byte  MUS_DEL_2  +  MUS_REST
     .byte  MUS_DEL_3  +  16
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUSCMD_JUMP, (MA1_END - MA1_01) ; Repeat back to top
MA1_END:
                                           
MA_SONG_2:
     .byte  MUSCMD_CONTROL, 12
     .byte  MUSCMD_VOLUME,  15
                                           
MA2_01:
     .byte  MUS_DEL_1  +  15
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  15
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_2  +  MUS_REST
     .byte  MUS_DEL_4  +  7
     .byte  MUS_DEL_4  +  MUS_REST
     .byte  MUS_DEL_2  +  15
     .byte  MUS_DEL_4  +  MUS_REST
     .byte  MUS_DEL_2  +  12
     .byte  MUS_DEL_2  +  MUS_REST
     .byte  MUS_DEL_2  +  15
     .byte  MUS_DEL_2  +  MUS_REST
     .byte  MUS_DEL_2  +  17
     .byte  MUS_DEL_2  +  MUS_REST
     .byte  MUSCMD_JUMP, (MA2_END - MA2_01) ; Repeat back to top
MA2_END:
                                           
MUSICB:
                                           
MB_SONG_1:
                                           
     .byte  MUSCMD_CONTROL, 8
     .byte  MUSCMD_VOLUME,  8 ; Volume (half)
                                           
MB1_01:
     .byte  MUS_DEL_1  +  10
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  20
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  30
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  15
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  10
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  20
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  30
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  15
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUSCMD_JUMP, (MB1_END - MB1_01) ; Repeat back to top
MB1_END:
                                           
MB_SONG_2:
                                           
     .byte  MUSCMD_CONTROL, 8
     .byte  MUSCMD_VOLUME,  8
                                           
MB2_01:
     .byte  MUS_DEL_1  +  1
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  1
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  1
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  1
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  30
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  30
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  30
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUS_DEL_1  +  30
     .byte  MUS_DEL_1  +  MUS_REST
     .byte  MUSCMD_JUMP, (MB2_END - MB2_01) ; Repeat back to top
MB2_END:

SKILL_VALUES:
                                           
     ;  This table describes how to change the various
     ;  difficulty parameters as the game progresses.
     ;  For instance, the second entry in the table
     ;  says that when the score is 4, change the values of
     ;  wall-increment to 1, frame-delay to 2, gap-pattern to 0,
     ;  MusicA to 24, and MusicB to 22.

     ;  A 255 on the end of the table indicates the end

     ;       Wall  Inc  Delay   Gap       MA                 MB
     .byte  0,     1,   3,     0  ,MA_SONG_1-MUSICA , MB_SONG_1-MUSICB
     .byte  4,     1,   2,     0  ,MA_SONG_2-MUSICA , MB_SONG_2-MUSICB
     .byte  8,     1,   1,     0  ,MA_SONG_1-MUSICA , MB_SONG_1-MUSICB
     .byte  16,    1,   1,     1  ,MA_SONG_2-MUSICA , MB_SONG_2-MUSICB
     .byte  24,    1,   1,     3  ,MA_SONG_1-MUSICA , MB_SONG_1-MUSICB
     .byte  32,    1,   1,     7  ,MA_SONG_2-MUSICA , MB_SONG_2-MUSICB
     .byte  40,    1,   1,    15  ,MA_SONG_1-MUSICA , MB_SONG_1-MUSICB
     .byte  48,    2,   1,     0  ,MA_SONG_2-MUSICA , MB_SONG_2-MUSICB
     .byte  64,    2,   1,     1  ,MA_SONG_1-MUSICA , MB_SONG_1-MUSICB
     .byte  80,    2,   1,     3  ,MA_SONG_2-MUSICA , MB_SONG_2-MUSICB
     .byte  96 ,   2,   1,     7  ,MA_SONG_1-MUSICA , MB_SONG_1-MUSICB
     .byte  255
                                           
GR_PLAYER:
     ;  Image for players (8x8)
     ;
     .byte  0b__...1....
     .byte  0b__...1....
     .byte  0b__..1.1...
     .byte  0b__..1.1...
     .byte  0b__.1.1.1..
     .byte  0b__.1.1.1..
     .byte  0b__1.1.1.1.
     .byte  0b__.11111..
                                           
DIGITS:
     ;  Images for numbers
     ;  We only need 5 rows, but the extra space on the end makes each digit 8 rows,
     ;  which makes it the multiplication easier.

     .byte 0b__....111.  ; 0 (leading 0 is blank)
     .byte 0b__....1.1.
     .byte 0b__....1.1.
     .byte 0b__....1.1.
     .byte 0b__....111.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

     .byte 0b__..1...1.  ; 1
     .byte 0b__..1...1.
     .byte 0b__..1...1.
     .byte 0b__..1...1.
     .byte 0b__..1...1.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

     .byte 0b__111.111.  ; 2
     .byte 0b__..1...1.
     .byte 0b__111.111.
     .byte 0b__1...1...
     .byte 0b__111.111.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

     .byte 0b__111.111.  ; 3
     .byte 0b__..1...1.
     .byte 0b__.11..11.
     .byte 0b__..1...1.
     .byte 0b__111.111.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

     .byte 0b__1.1.1.1.  ; 4
     .byte 0b__1.1.1.1.
     .byte 0b__111.111.
     .byte 0b__..1...1.
     .byte 0b__..1...1.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

     .byte 0b__111.111. ; 5
     .byte 0b__1...1...
     .byte 0b__111.111.
     .byte 0b__..1...1.
     .byte 0b__111.111.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

     .byte 0b__111.111. ; 6
     .byte 0b__1...1...
     .byte 0b__111.111.
     .byte 0b__1.1.1.1.
     .byte 0b__111.111.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

     .byte 0b__111.111. ; 7
     .byte 0b__..1...1.
     .byte 0b__..1...1.
     .byte 0b__..1...1.
     .byte 0b__..1...1.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

     .byte 0b__111.111. ; 8
     .byte 0b__1.1.1.1.
     .byte 0b__111.111.
     .byte 0b__1.1.1.1.
     .byte 0b__111.111.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

     .byte 0b__111.111. ; 9
     .byte 0b__1.1.1.1.
     .byte 0b__111.111.
     .byte 0b__..1...1.
     .byte 0b__111.111.
     .byte 0b__........
     .byte 0b__........
     .byte 0b__........

0xF7FA:
	 ; 6502 vectors
     .word main
     .word main  ; Reset vector (top of program)
     .word main

