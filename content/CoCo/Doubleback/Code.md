![](doubleback.jpg)

# Doubleback

>>> cpu 6809

>>> binary C000:roms/doubleback.bin

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](..\Hardware.md)

```code
C000: 0F BB           CLR     $BB                 ; {ram.HighScore} First RESET comes here. Clear ...
C002: 0F BC           CLR     $BC                 ; {ram.HighScore+1} ... high-score
;
Reset:
C004: 12              NOP                         ; Required by BASIC ROM RESET handler
C005: 1A 50           ORCC    #$50                ; Disable IRQ
C007: 10 CE 01 50     LDS     #$0150              ; Stack
C00B: 30 8C F6        LEAX    $C004,PC            ; {code.Reset} RESET button ...
C00E: 9F 72           STX     $72                 ; ... now comes to C004
;
; There are 4 pixels per memory byte: aa_bb_cc_dd
; The value 00 is considered transparent. When an image is blitted to the screen,
; any pixels with value 00 are left unchanged at the destination.
; In order to set the non-zero bits, a mask is needed to zero-out the pixels at
; the destination. The pixel mask value is 11 for pixel value 00 and 00 for any
; other pixel value.
;
; For instance: 00_01_10_00 has two visible pixels in the middle and two transparents on the ends
; The mask:     11_00_00_11 this would AND out any 1s at the destination allowing the new value
;                           to be ORed into the destination
;
; Building the mask on the fly is tedious (costly in time). Instead, the code builds a 256-value
; lookup table to get the mask from the pixel pattern. TABLE[$18] = $C3 for the example above.
;
; Build the bit mask table from 0380 to 0390
C010: 8E 03 80        LDX     #$0380              ; Start of mask table
C013: 5F              CLRB                        ; Start with ...
C014: 34 04           PSHS    B                   ; ... entry 0
C016: A6 E4           LDA     ,S                  ; Table entry index
C018: E6 E4           LDB     ,S                  ; Table entry value
C01A: C4 AA           ANDB    #$AA                ; Keep the upper bit of each pixel
C01C: 54              LSRB                        ; Copy to lower bit of each pixel
C01D: E7 86           STB     A,X                 ; Accumulate that
C01F: E6 E4           LDB     ,S                  ; Table entry value
C021: C4 55           ANDB    #$55                ; Keep the lower bit of each pixel
C023: 58              ASLB                        ; Copy to upper bit of each pixel
C024: EA 86           ORB     A,X                 ; Accumulate that
C026: EA E4           ORB     ,S                  ; OR in the original bits
C028: 53              COMB                        ; 1's to 0 for an AND mask
C029: E7 86           STB     A,X                 ; Store the entry
C02B: 6C E4           INC     ,S                  ; Do all ...
C02D: 26 E7           BNE     $C016               ; {} ... 256 entries
C02F: 35 04           PULS    B                   ; remove stack temporary
;          
NewGame:
C031: 17 0A 1E        LBSR    $CA52               ; {code.ClearScreen} Clear the screen
C034: 17 0A 98        LBSR    $CACF               ; {code.SetVideoMode} Set the graphics mode
C037: CC 1C 46        LDD     #$1C46              ; Screen coordinates
C03A: 33 8D 0D 33     LEAU    $CD71,PC            ; {code.StrCopyright1} Print ...
C03E: 17 09 02        LBSR    $C943               ; {code.PrintChars} ... copyright line 1
C041: CC 14 4E        LDD     #$144E              ; Screen coordinates
C044: 33 8D 0D 3A     LEAU    $CD82,PC            ; {code.StrCopyright2} Print ...
C048: 17 08 F8        LBSR    $C943               ; {code.PrintChars} ... copyright line 2
C04B: CC 14 56        LDD     #$1456              ; Screen coordinates
C04E: 33 8D 0D D1     LEAU    $CE23,PC            ; {code.StrCopyright3} Print ...
C052: 17 08 EE        LBSR    $C943               ; {code.PrintChars} ... copyright line 3
;
; Cursive "doubleback"
C055: 8E 00 E4        LDX     #$00E4              ; Utility object structure
C058: 86 1F           LDA     #$1F                ; Set ...
C05A: A7 84           STA     ,X                  ; ... X coordinate
C05C: 86 18           LDA     #$18                ; Set ...
C05E: A7 02           STA     2,X                 ; ... Y coordinate
C060: 33 8D 0E 5F     LEAU    $CEC3,PC            ; {} Cursive "doubleback" data
C064: 34 04           PSHS    B                   ; Space on stack for counter
C066: C6 05           LDB     #$05                ; Each word has 3*5 = 15 data points
C068: E7 E4           STB     ,S                  ; Store the count
C06A: EC C1           LDD     ,U++                ; Get the next 5 data points
C06C: 27 42           BEQ     $C0B0               ; {} No more ... we are done
C06E: 34 06           PSHS    B,A                 ; Hold the data points
C070: C4 07           ANDB    #$07                ; Lower 3 bits
C072: 58              ASLB                        ; 2 bytes per
C073: 31 8D 0E B6     LEAY    $CF2D,PC            ; {code.DirTable} Offset table
C077: EC A5           LDD     B,Y                 ; Get X and Y offsets
C079: AB 84           ADDA    ,X                  ; Add X offset
C07B: EB 02           ADDB    2,X                 ; Add Y offset
C07D: A7 84           STA     ,X                  ; Nex X position
C07F: E7 02           STB     2,X                 ; New Y position
C081: 40              NEGA                        ; Mirror ...
C082: 8B 80           ADDA    #$80                ; ... X ...
C084: A7 01           STA     1,X                 ; ... coordinate
C086: 50              NEGB                        ; Mirror ...
C087: CB 3C           ADDB    #$3C                ; ... Y ...
C089: E7 03           STB     3,X                 ; ... coordinate
C08B: 34 50           PSHS    U,X                 ; Hold data pointer and screen pointer
C08D: 17 08 CF        LBSR    $C95F               ; {code.SetPixel} Draw top pixel
C090: 30 01           LEAX    1,X                 ; Skip over to 2nd screen pointer
C092: 17 08 CA        LBSR    $C95F               ; {code.SetPixel} Draw bottom (reflected) pixel
C095: E6 84           LDB     ,X                  ; Is the X ...
C097: C4 01           ANDB    #$01                ; ... coordinate odd?
C099: 26 03           BNE     $C09E               ; {} No ... skip the pause
C09B: 17 0A 51        LBSR    $CAEF               ; {code.WaitVBlank} Yes ... slight pause
C09E: 35 50           PULS    X,U                 ; Restore the data pointer and the screen pointer
C0A0: 35 06           PULS    A,B                 ; Pop the data points
C0A2: 6A E4           DEC     ,S                  ; All 5 datapoints done?
C0A4: 27 C0           BEQ     $C066               ; {} Yes ... reload next five
C0A6: 44              LSRA                        ; No ...
C0A7: 56              RORB                        ; ... shift ...
C0A8: 44              LSRA                        ; ... over ...
C0A9: 56              RORB                        ; ... next ...
C0AA: 44              LSRA                        ; ... data ...
C0AB: 56              RORB                        ; ... point
C0AC: 34 06           PSHS    B,A                 ; Hold current data
C0AE: 20 C0           BRA     $C070               ; {} Do next point
;
C0B0: 35 04           PULS    B                   ; Remove the stack counter

C0B2: CC 28 3A        LDD     #$283A              ; Print coordinates
C0B5: 33 8D 0C 57     LEAU    $CD10,PC            ; {code.Str1or2Players} Print ...
C0B9: 17 08 87        LBSR    $C943               ; {code.PrintChars} ... "1 or 2 Players"
;
C0BC: AD 9F A0 0A     JSR     [$A00A]             ; {hard.JOYIN} Read the joysticks
C0C0: 0F B4           CLR     $B4                 ; {ram.NumPlayers} Number of players = 1
C0C2: CE 0C 2A        LDU     #$0C2A              ; Screen coordinate for the underline for 1 or 2
C0C5: 6F C4           CLR     ,U                  ; Erase the 1 underline
C0C7: 6F 43           CLR     3,U                 ; Erase the 2 underline
C0C9: B6 01 5A        LDA     $015A               ; Player one X axis
C0CC: 81 1F           CMPA    #$1F                ; Left or right of middle?
C0CE: 2F 04           BLE     $C0D4               ; {} Left ...
C0D0: 0C B4           INC     $B4                 ; {ram.NumPlayers} Number of players = 1
C0D2: 33 43           LEAU    3,U                 ; U points to 2 underline
C0D4: 6A C4           DEC     ,U                  ; Underline the 1 or 2 with a white 4 pixels
C0D6: 17 0A 16        LBSR    $CAEF               ; {code.WaitVBlank} Wait for VBLANKing
C0D9: F6 FF 00        LDB     $FF00               ; {hard.PIA0_DA} Button ...
C0DC: C4 01           ANDB    #$01                ; ... pressed?
C0DE: 26 DC           BNE     $C0BC               ; {} No ... keep waiting
;
C0E0: 0F B7           CLR     $B7                 ; {ram.P1Score} Clear player ...
C0E2: 0F B8           CLR     $B8                 ; {ram.P1Score+1} ... one score
C0E4: 0F B9           CLR     $B9                 ; {ram.P2Score} Clear player ...
C0E6: 0F BA           CLR     $BA                 ; {ram.P2Score+1} ... two score
C0E8: C6 03           LDB     #$03                ; Start with ...
C0EA: D7 B5           STB     $B5                 ; {ram.NumLives} ... three lives
;
C0EC: 0F B6           CLR     $B6                 ; {ram.Player} Player 0
C0EE: 17 00 3E        LBSR    $C12F               ; {code.PlayRound} Play one round for player 0
C0F1: 0D B4           TST     $B4                 ; {ram.NumPlayers} Two player game?
C0F3: 27 05           BEQ     $C0FA               ; {} No ... skip second player
C0F5: 0C B6           INC     $B6                 ; {ram.Player} Player 1
C0F7: 17 00 35        LBSR    $C12F               ; {code.PlayRound} Play one round for player 1
C0FA: 0A B5           DEC     $B5                 ; {ram.NumLives} Subtract one from lives
C0FC: 26 EE           BNE     $C0EC               ; {} Go back for all lives
;
C0FE: DC B7           LDD     $B7                 ; {ram.P1Score} Player 1 score
C100: 10 93 BB        CMPD    $BB                 ; {ram.HighScore} Beat the high score?
C103: 23 02           BLS     $C107               ; {} No ... move on
C105: DD BB           STD     $BB                 ; {ram.HighScore} Change the high score
;
C107: DC B9           LDD     $B9                 ; {ram.P2Score} Player 2 score
C109: 10 93 BB        CMPD    $BB                 ; {ram.HighScore} Beat the high score?
C10C: 23 02           BLS     $C110               ; {} No ... move on
C10E: DD BB           STD     $BB                 ; {ram.HighScore} Change the high score
;
C110: DC BB           LDD     $BB                 ; {ram.HighScore} Print ...
C112: CE 04 EE        LDU     #$04EE              ; ... high score at top ...
C115: 17 05 13        LBSR    $C62B               ; {code.DrawNumber} ... of screen
C118: CC 2C 28        LDD     #$2C28              ; Print coordinates
C11B: 33 8D 0B A0     LEAU    $CCBF,PC            ; {code.StrGameOver} Print ...
C11F: 17 08 21        LBSR    $C943               ; {code.PrintChars} ... "Game Over"
C122: 17 09 9B        LBSR    $CAC0               ; {code.CheckForBreak} Check for break
C125: F6 FF 00        LDB     $FF00               ; {hard.PIA0_DA} Wait for ...
C128: C4 01           ANDB    #$01                ; ... button ...
C12A: 26 F6           BNE     $C122               ; {} ... press ...
C12C: 16 FF 02        LBRA    $C031               ; {code.NewGame} Start a new game

PlayRound:
C12F: C6 FF           LDB     #$FF                ; Fill screen ...
C131: 17 09 1F        LBSR    $CA53               ; {code.FillScreen} ... with white {}
C134: 0F BE           CLR     $BE                 ; {ram.EndOfPlayer} Offset in player's line buffer (0x200)
C136: 0F D1           CLR     $D1                 ; {ram.D1}
C138: 0F CE           CLR     $CE                 ; {ram.CE}
C13A: 0F D0           CLR     $D0                 ; {ram.D0}
C13C: 0F C7           CLR     $C7                 ; {ram.HasLoopScore} Not showing a loop score
C13E: 0F D6           CLR     $D6                 ; {ram.FlashType} Flash player "word" is off
C140: 0F CF           CLR     $CF                 ; {ram.SkullCount}
C142: C6 28           LDB     #$28                ; Reload counter for ...
C144: D7 D5           STB     $D5                 ; {ram.FlashCount} ... flashing player "word"
;
C146: CC 2C 28        LDD     #$2C28              ; Screen coordinates
C149: 33 8D 0A FF     LEAU    $CC4C,PC            ; {code.StrPlayer} Graphics for "Player"
C14D: 17 07 F3        LBSR    $C943               ; {code.PrintChars} Print "player"
C150: CC 44 28        LDD     #$4428              ; Screen coordinates
C153: 33 8D 0B 26     LEAU    $CC7D,PC            ; {code.StrOne} Graphics for "one"
C157: 0D B6           TST     $B6                 ; {ram.Player} Player 0 or 1?
C159: 27 06           BEQ     $C161               ; {} Player 0 ... keep the "one"
C15B: 86 46           LDA     #$46                ; Move "two" over a hair
C15D: 33 8D 0B 3D     LEAU    $CC9E,PC            ; {code.StrTwo} Graphics for "two"
C161: 17 07 DF        LBSR    $C943               ; {code.PrintChars} Print the player (one or two)
;
C164: D6 B5           LDB     $B5                 ; {ram.NumLives} What life-number are we on?
C166: 33 8D 0E 1B     LEAU    $CF85,PC            ; {code.MusicThirdLife} Song for "3rd life"
C16A: 5A              DECB                        ; Is this the last life?
C16B: 27 0B           BEQ     $C178               ; {} Yes ... play this song
C16D: 33 8D 0D F0     LEAU    $CF61,PC            ; {code.MusicSecondLife} Song for "2nd life"
C171: 5A              DECB                        ; Is this the second life?
C172: 27 04           BEQ     $C178               ; {} Yes ... play this song
C174: 33 8D 0D C5     LEAU    $CF3D,PC            ; {code.MusicFirstLife} Song for 1st life
C178: 17 09 03        LBSR    $CA7E               ; {code.PlaySong} Play the song
;
C17B: 17 08 E5        LBSR    $CA63               ; {code.DrawPlayfiled}
C17E: C6 02           LDB     #$02                ; X/Y coordinate ...
C180: 34 04           PSHS    B                   ; ... temporary
C182: 8E 00 E4        LDX     #$00E4              ; Utility object to draw border
C185: C1 56           CMPB    #$56                ; Left/Right side is shorter
C187: 2E 12           BGT     $C19B               ; {} Beyond the bounds of up/down ... skip up/down lines
C189: E7 02           STB     2,X                 ; Set the Y coordinate
C18B: C6 02           LDB     #$02                ; X coordinate ...
C18D: E7 84           STB     ,X                  ; ... is 2
C18F: 17 07 CD        LBSR    $C95F               ; {code.SetPixel} Draw the line down left side
C192: C6 7E           LDB     #$7E                ; X cooridante ...
C194: E7 84           STB     ,X                  ; ... is right side
C196: 17 07 C6        LBSR    $C95F               ; {code.SetPixel} Draw the line down right side
C199: E6 02           LDB     2,X                 ; Counter now ...
C19B: E7 84           STB     ,X                  ; ... in the X coordinate
C19D: C6 02           LDB     #$02                ; Top Y ...
C19F: E7 02           STB     2,X                 ; coordinate
C1A1: 17 07 BB        LBSR    $C95F               ; {code.SetPixel} Draw the line across the top
C1A4: C6 56           LDB     #$56                ; Bottom ...
C1A6: E7 02           STB     2,X                 ; ... Y coordinate
C1A8: 17 07 B4        LBSR    $C95F               ; {code.SetPixel} Draw the line across the bottom
C1AB: 6C E4           INC     ,S                  ; Increment the counter
C1AD: E6 E4           LDB     ,S                  ; New counter value
C1AF: C1 7E           CMPB    #$7E                ; All edge pixels drawn?
C1B1: 23 CF           BLS     $C182               ; {} No ... go do them all
C1B3: 35 04           PULS    B                   ; Pop the counter
;
C1B5: 4F              CLRA                        ; X coordinate
C1B6: C6 58           LDB     #$58                ; Y coordinate
C1B8: 33 8D 0A 90     LEAU    $CC4C,PC            ; {code.StrPlayer} Print "player" at bottom ...
C1BC: 17 07 84        LBSR    $C943               ; {code.PrintChars} ... of screen
C1BF: CC 18 58        LDD     #$1858              ; Coordinates for "one"
C1C2: 33 8D 0A B7     LEAU    $CC7D,PC            ; {code.StrOne} Graphics for "one"
C1C6: 17 07 7A        LBSR    $C943               ; {code.PrintChars} Print "one" after "player"
C1C9: 0D B4           TST     $B4                 ; {ram.NumPlayers} One are two players?
C1CB: 27 0A           BEQ     $C1D7               ; {} Just one ... skip the "two"
C1CD: CC 52 58        LDD     #$5258              ; Coordinates for "two"
C1D0: 33 8D 0A CA     LEAU    $CC9E,PC            ; {code.StrTwo} Print "two" farther ...
C1D4: 17 07 6C        LBSR    $C943               ; {code.PrintChars} ... farther right
C1D7: 17 04 36        LBSR    $C610               ; {code.PrintScores} Print the player scores (both if two player)
;
C1DA: 8E 00 E4        LDX     #$00E4              ; Utility object
C1DD: 6F 02           CLR     2,X                 ; Y = 0
C1DF: C6 33           LDB     #$33                ; 1st slot X ...
C1E1: E7 84           STB     ,X                  ; ... coordinate
;
; First slot (active if 3 lives)
C1E3: 33 8D 0A 33     LEAU    $CC1A,PC            ; {} Life inidcator ACTIVE
C1E7: D6 B5           LDB     $B5                 ; {ram.NumLives} Number of lives
C1E9: C1 03           CMPB    #$03                ; All 3?
C1EB: 27 04           BEQ     $C1F1               ; {} Yes ... 1st bar is CURRENT
C1ED: 33 8D 0A 19     LEAU    $CC0A,PC            ; {code.LifeIndicator} Life indicator INACTIVE
C1F1: 17 05 69        LBSR    $C75D               ; {code.Draw8x8} Draw the indicator
C1F4: C6 3D           LDB     #$3D                ; 2nd slot X ...
C1F6: E7 84           STB     ,X                  ; ... cooridinate
;
; Second slot (active if 2 lives)
C1F8: 33 8D 0A 1E     LEAU    $CC1A,PC            ; {} Life inidcator ACTIVE
C1FC: D6 B5           LDB     $B5                 ; {ram.NumLives} Number of lives
C1FE: C1 02           CMPB    #$02                ; 2 remaining?
C200: 27 04           BEQ     $C206               ; {} Yes ... 2nd bar is CURRENT
C202: 33 8D 0A 04     LEAU    $CC0A,PC            ; {code.LifeIndicator} Life indicator INACTIVE
C206: 17 05 54        LBSR    $C75D               ; {code.Draw8x8} Draw the indicator
C209: C6 47           LDB     #$47                ; 3rd slot X ...
C20B: E7 84           STB     ,X                  ; ... coordinate
;
; Third slot (active if 1 life)
C20D: 33 8D 0A 09     LEAU    $CC1A,PC            ; {} Life inidcator ACTIVE
C211: D6 B5           LDB     $B5                 ; {ram.NumLives} Number of lives
C213: C1 01           CMPB    #$01                ; 1 remaining?
C215: 27 04           BEQ     $C21B               ; {} Yes ... 3rd bar is CURRENT
C217: 33 8D 09 EF     LEAU    $CC0A,PC            ; {code.LifeIndicator} Life indicator INACTIVE
C21B: 17 05 3F        LBSR    $C75D               ; {code.Draw8x8} Draw the indicator
; 
C21E: 8E 00 D8        LDX     #$00D8              ; Player-point object
C221: 86 40           LDA     #$40                ; Set X ...
C223: A7 84           STA     ,X                  ; ... to 64 ...
C225: A7 02           STA     2,X                 ; ... and Y to 64
C227: 8E 02 00        LDX     #$0200              ; Clear ...
C22A: 5F              CLRB                        ; ... the ...
C22B: A7 80           STA     ,X+                 ; ... player ...
C22D: 5A              DECB                        ; ... line
C22E: 26 FB           BNE     $C22B               ; {} ... points
C230: 8E 01 60        LDX     #$0160              ; Start of game objects
C233: C6 A0           LDB     #$A0                ; 160 / 8 = 20 possible objects
C235: 6F 80           CLR     ,X+                 ; Clear ...
C237: 5A              DECB                        ; ... all ...
C238: 26 FB           BNE     $C235               ; {} ... game objects
C23A: 0F BD           CLR     $BD                 ; {ram.Collision} Clear the collision flag
C23C: 17 00 16        LBSR    $C255               ; {code.OneCycle} Move the player and the objects
C23F: 0D BD           TST     $BD                 ; {ram.Collision} Was there a collision?
C241: 27 F9           BEQ     $C23C               ; {} No ... keep playing
;
; End of life (and return)
C243: C6 F0           LDB     #$F0                ; Dull screen ...
C245: F7 FF 22        STB     $FF22               ; {hard.PIA1_DB} ... color mode
C248: 33 8D 0D 59     LEAU    $CFA5,PC            ; {code.MusicEndOfLife} Play the ...
C24C: 17 08 2F        LBSR    $CA7E               ; {code.PlaySong} ... end of life song
C24F: C6 F8           LDB     #$F8                ; Bright screen ...
C251: F7 FF 22        STB     $FF22               ; {hard.PIA1_DB} ... color mode
C254: 39              RTS                         ; Done

OneCycle:
C255: 17 08 68        LBSR    $CAC0               ; {code.CheckForBreak} Check for BREAK (reset if so)
C258: 8E 02 00        LDX     #$0200              ; Player's drawn coordinates
C25B: D6 BE           LDB     $BE                 ; {ram.EndOfPlayer} End of the list
C25D: 3A              ABX                         ; Offset to last point
C25E: EC 84           LDD     ,X                  ; X,Y of last point
C260: 8E 00 DE        LDX     #$00DE              ; Descriptor for erasing points
C263: A7 84           STA     ,X                  ; Set X ...
C265: E7 02           STB     2,X                 ; ... and Y coordinate
C267: 17 07 48        LBSR    $C9B2               ; {code.GetScreenAndShift} Pointer and pixel number
C26A: 17 07 29        LBSR    $C996               ; {code.ErasePixel} Erase the tail of the player
C26D: 0C D4           INC     $D4                 ; {ram.CycleCount} Cycle count used to pace the objects

C26F: 8E 01 60        LDX     #$0160              ; List of objects

; Object structure
;
; 00 X coordinate
; 01 X residue
; 02 Y coordinate
; 03 Y residue
; 04 delta X (if used)
; 05 delta Y (if used)
; 06 Object type (0 means end of list)
; 07 image number if used (for flipping images)

ObjectLoop:
C272: 6D 06           TST     6,X                 ; Object type 0 (end of list)?
C274: 10 27 01 17     LBEQ    $C38F               ; {} Yes ... done with list
C278: 30 08           LEAX    8,X                 ; Next slot
C27A: 1F 10           TFR     X,D                 ; 8 bytes per slot ...
C27C: 54              LSRB                        ; ... get the ...
C27D: 54              LSRB                        ; ... slot number ...
C27E: 54              LSRB                        ; ... to B
C27F: DB D4           ADDB    $D4                 ; {ram.CycleCount} Add in cycle count
C281: C4 07           ANDB    #$07                ; Time for this slot to update?
C283: 26 ED           BNE     $C272               ; {code.ObjectLoop} No ... skip this object
C285: 30 18           LEAX    -8,X                ; Back up to start of this object
;
C287: E6 06           LDB     6,X                 ; Object type
C289: 5A              DECB                        ; 1=APPLE?
C28A: 26 0A           BNE     $C296               ; {} No ... check other types
C28C: 33 8D 08 6A     LEAU    $CAFA,PC            ; {code.ImageApple} Apple graphic
C290: 17 04 CA        LBSR    $C75D               ; {code.Draw8x8} Draw apple
C293: 16 00 F0        LBRA    $C386               ; {code.NextObject} Next object
;
C296: 5A              DECB                        ; 2=CHERRY
C297: 26 0A           BNE     $C2A3               ; {} No ... check other types
C299: 33 8D 08 6D     LEAU    $CB0A,PC            ; {code.ImageCherry} Cherry graphic
C29D: 17 04 BD        LBSR    $C75D               ; {code.Draw8x8} Draw cherry
C2A0: 16 00 E3        LBRA    $C386               ; {code.NextObject} Next object
;
C2A3: 5A              DECB                        ; 3=MAGNET
C2A4: 26 17           BNE     $C2BD               ; {} No ... check other types
C2A6: 33 8D 08 70     LEAU    $CB1A,PC            ; {code.ImageMagnet} Erase current ...
C2AA: 17 05 AE        LBSR    $C85B               ; {code.Erase8x8} ... magnet
C2AD: CC 10 10        LDD     #$1010              ; DeltaX,DeltaY = 16,16
C2B0: 17 07 4C        LBSR    $C9FF               ; {code.FollowPlayer}
C2B3: 33 8D 08 63     LEAU    $CB1A,PC            ; {code.ImageMagnet} Draw the ...
C2B7: 17 04 A3        LBSR    $C75D               ; {code.Draw8x8} ... magnet
C2BA: 16 00 C9        LBRA    $C386               ; {code.NextObject} Next object
;
C2BD: 5A              DECB                        ; 4=SKATE
C2BE: 26 24           BNE     $C2E4               ; {} No ... check other types
C2C0: 8D 13           BSR     $C2D5               ; {} Get skate image
C2C2: 17 05 96        LBSR    $C85B               ; {code.Erase8x8} Erase the current skate
C2C5: 6C 07           INC     7,X                 ; Next skate image
C2C7: 86 10           LDA     #$10                ; DeltaX,DeltaY = ...
C2C9: 5F              CLRB                        ; ... 16,0
C2CA: 17 07 32        LBSR    $C9FF               ; {code.FollowPlayer}
C2CD: 8D 06           BSR     $C2D5               ; {} Get the skate image
C2CF: 17 04 8B        LBSR    $C75D               ; {code.Draw8x8} Draw the skate
C2D2: 16 00 B1        LBRA    $C386               ; {code.NextObject} Next object
;
C2D5: 33 8D 08 51     LEAU    $CB2A,PC            ; {code.ImageSkate} Skate graphic 1
C2D9: E6 07           LDB     7,X                 ; Image number
C2DB: C4 01           ANDB    #$01                ; Either 0 or 1
C2DD: 26 04           BNE     $C2E3               ; {} Not 1 ... use this graphic
C2DF: 33 8D 08 57     LEAU    $CB3A,PC            ; {} Use skate graphic 2
C2E3: 39              RTS                         ; Done
;
C2E4: 5A              DECB                        ; 5=YOYO
C2E5: 26 3C           BNE     $C323               ; {} No ... check other types
C2E7: 33 8D 08 9F     LEAU    $CB8A,PC            ; {} Erase the current yoyo but ...
C2EB: 17 05 6D        LBSR    $C85B               ; {code.Erase8x8} ... leave the string piece of the image
C2EE: 4F              CLRA                        ; Set deltaX ...
C2EF: A7 04           STA     4,X                 ; ... to zero
C2F1: C6 20           LDB     #$20                ; Downward deltaY
C2F3: 6D 07           TST     7,X                 ; Moving down?
C2F5: 27 01           BEQ     $C2F8               ; {} Yes ... keep this
C2F7: 50              NEGB                        ; No ... moving UP. Negate it
C2F8: E7 05           STB     5,X                 ; Store deltaY
C2FA: 17 06 CB        LBSR    $C9C8               ; {code.MoveObject}
C2FD: E6 02           LDB     2,X                 ; Y coordinate
C2FF: C1 0C           CMPB    #$0C                ; At the top-most allowed?
C301: 24 04           BHS     $C307               ; {} No ... keep moving in current direction
C303: 6F 07           CLR     7,X                 ; Yes ... now moving down
C305: C6 0C           LDB     #$0C                ; Set to the top-most allowed
C307: C1 42           CMPB    #$42                ; At the bottom-most allowed?
C309: 25 04           BLO     $C30F               ; {} No ... keep moving in current direction
C30B: 6C 07           INC     7,X                 ; Yes ... now moving up
C30D: C6 42           LDB     #$42                ; Set to the bottom-most allowed
C30F: E7 02           STB     2,X                 ; New Y coordinate
C311: 33 8D 08 35     LEAU    $CB4A,PC            ; {code.ImageYoYo} YoYo images
C315: C4 03           ANDB    #$03                ; 4 of them based on Y coordinate
C317: 58              ASLB                        ; 16 ...
C318: 58              ASLB                        ; ... bytes ...
C319: 58              ASLB                        ; ... each ...
C31A: 58              ASLB                        ; ... image
C31B: 33 C5           LEAU    B,U                 ; Point to current image
C31D: 17 04 3D        LBSR    $C75D               ; {code.Draw8x8}
C320: 16 00 63        LBRA    $C386               ; {code.NextObject} Next object
;
C323: 5A              DECB                        ; 6=PEAR
C324: 26 09           BNE     $C32F               ; {} No ... check other types
C326: 33 8D 08 90     LEAU    $CBBA,PC            ; {code.ImagePear}
C32A: 17 04 30        LBSR    $C75D               ; {code.Draw8x8}
C32D: 20 57           BRA     $C386               ; {code.NextObject} Next object
;
C32F: 5A              DECB                        ; 7=SPIDER
C330: 26 21           BNE     $C353               ; {} No ... check other types
C332: 8D 10           BSR     $C344               ; {} Get spider image
C334: 17 05 24        LBSR    $C85B               ; {code.Erase8x8} Erase current spider image
C337: CC 30 30        LDD     #$3030              ; DeltaX,DeltaY = 48,48
C33A: 17 06 C2        LBSR    $C9FF               ; {code.FollowPlayer} Move towards player
C33D: 8D 05           BSR     $C344               ; {} Get spider image
C33F: 17 04 1B        LBSR    $C75D               ; {code.Draw8x8} Draw the spider
C342: 20 42           BRA     $C386               ; {code.NextObject} Next object
;
C344: 33 8D 08 82     LEAU    $CBCA,PC            ; {code.ImageSpider} First spider image
C348: E6 02           LDB     2,X                 ; Y coordinate
C34A: C4 01           ANDB    #$01                ; Is the Y coordinate odd?
C34C: 26 04           BNE     $C352               ; {} Yes ... use first image
C34E: 33 8D 08 88     LEAU    $CBDA,PC            ; {} No ... use 2nd image
C352: 39              RTS                         ; Done
;
C353: 5A              DECB                        ; 8=SKULL
C354: 26 09           BNE     $C35F               ; {} No ... check other types
C356: 33 8D 08 50     LEAU    $CBAA,PC            ; {code.ImageSkull}
C35A: 17 04 00        LBSR    $C75D               ; {code.Draw8x8}
C35D: 20 27           BRA     $C386               ; {code.NextObject} Next object

C35F: 5A              DECB                        ; 9=X
C360: 26 24           BNE     $C386               ; {code.NextObject} No. Anything but 0-9 ... skip.
C362: 8D 13           BSR     $C377               ; {} Get the current image
C364: 17 04 F4        LBSR    $C85B               ; {code.Erase8x8} Erase the current image
C367: 6C 07           INC     7,X                 ; Next image index
C369: CC 7F 7F        LDD     #$7F7F              ; DeltaX,DeltaY = 127,127 ! Very fast!
C36C: 17 06 90        LBSR    $C9FF               ; {code.FollowPlayer} Move towards player
C36F: 8D 06           BSR     $C377               ; {} Get the image
C371: 17 03 E9        LBSR    $C75D               ; {code.Draw8x8} Draw the image
C374: 16 00 0F        LBRA    $C386               ; {code.NextObject} Next object
;
C377: 33 8D 08 6F     LEAU    $CBEA,PC            ; {code.ImageX} X picture small
C37B: E6 07           LDB     7,X                 ; The image number
C37D: C4 01           ANDB    #$01                ; Is image number odd?
C37F: 26 04           BNE     $C385               ; {} Yes ... keep small picture
C381: 33 8D 08 75     LEAU    $CBFA,PC            ; {} No ... use large picture
C385: 39              RTS                         ; Done

NextObject:
C386: 6F 04           CLR     4,X                 ; Clear any ...
C388: 6F 05           CLR     5,X                 ; ... deltas
C38A: 30 08           LEAX    8,X                 ; Next object
C38C: 16 FE E3        LBRA    $C272               ; {code.ObjectLoop} continue with next

C38F: 9F D2           STX     $D2                 ; {ram.NextFreeObj}
C391: AD 9F A0 0A     JSR     [$A00A]             ; {hard.JOYIN} JOYIN reads all 4 joysticks (15A,15B,15C,15D)
C395: 8E 00 D8        LDX     #$00D8              ; Object for drawing player point
C398: 10 8E 01 5A     LDY     #$015A              ; Memory for analog inputs
C39C: D6 B6           LDB     $B6                 ; {ram.Player} Player number
C39E: 58              ASLB                        ; 2 axis per joystick
C39F: 31 A5           LEAY    B,Y                 ; Point to 15A, 15B (player 0) or 15C, 15D (player 1)
C3A1: E6 A4           LDB     ,Y                  ; Get the X stick value
C3A3: A6 A4           LDA     ,Y                  ; Add in ...
C3A5: 9B D7           ADDA    $D7                 ; {ram.Random} ... some ...
C3A7: 97 D7           STA     $D7                 ; {ram.Random} ... randomness to RNG
C3A9: C0 20           SUBB    #$20                ; Less sensitive
C3AB: E7 04           STB     4,X                 ; Hold as delta X
;
C3AD: E6 21           LDB     1,Y                 ; Next axis
C3AF: C0 20           SUBB    #$20                ; Less sensitive
C3B1: E7 05           STB     5,X                 ; Hold as delta Y
C3B3: 17 06 12        LBSR    $C9C8               ; {code.MoveObject} Move ...
C3B6: 17 03 66        LBSR    $C71F               ; {code.EraseLoopScore} ... player's dot
;
C3B9: 8E 00 D8        LDX     #$00D8              ; Player point structure
C3BC: 17 05 A0        LBSR    $C95F               ; {code.SetPixel} Draw the new player dot
C3BF: D7 BF           STB     $BF                 ; {ram.OrigPixel} Hold the original pixel (for collision detection)
C3C1: 17 03 4F        LBSR    $C713               ; {code.DrawLoopScore} Erase any last-drawn score
C3C4: 0F C3           CLR     $C3                 ; {ram.C3}
C3C6: D6 BE           LDB     $BE                 ; {ram.EndOfPlayer}
C3C8: D7 C0           STB     $C0                 ; {ram.C0}
C3CA: D6 C0           LDB     $C0                 ; {ram.C0}
C3CC: C0 02           SUBB    #$02                
C3CE: D7 C0           STB     $C0                 ; {ram.C0}
C3D0: D1 BE           CMPB    $BE                 ; {ram.EndOfPlayer}
C3D2: 10 27 01 24     LBEQ    $C4FA               ; {}
;
C3D6: 8E 02 00        LDX     #$0200              ; Player's points
C3D9: 3A              ABX                         
C3DA: EC 84           LDD     ,X                  
C3DC: 8E 00 D8        LDX     #$00D8              
C3DF: A0 84           SUBA    ,X                  
C3E1: 4C              INCA                        
C3E2: 81 02           CMPA    #$02                
C3E4: 22 07           BHI     $C3ED               ; {}
C3E6: E0 02           SUBB    2,X                 
C3E8: 5C              INCB                        
C3E9: C1 02           CMPB    #$02                
C3EB: 23 04           BLS     $C3F1               ; {}
C3ED: 0C C3           INC     $C3                 ; {ram.C3}
C3EF: 20 D9           BRA     $C3CA               ; {}
C3F1: 10 83 01 01     CMPD    #$0101              
C3F5: 26 02           BNE     $C3F9               ; {}
C3F7: 0F BF           CLR     $BF                 ; {ram.OrigPixel}
C3F9: 0D C3           TST     $C3                 ; {ram.C3}
C3FB: 27 CD           BEQ     $C3CA               ; {}
C3FD: 0F BF           CLR     $BF                 ; {ram.OrigPixel}
C3FF: D6 C0           LDB     $C0                 ; {ram.C0}
C401: D7 C1           STB     $C1                 ; {ram.C1}
C403: D6 BE           LDB     $BE                 ; {ram.EndOfPlayer}
C405: D7 C0           STB     $C0                 ; {ram.C0}
C407: D6 C0           LDB     $C0                 ; {ram.C0}
C409: C0 02           SUBB    #$02                
C40B: D7 C0           STB     $C0                 ; {ram.C0}
C40D: 8E 02 00        LDX     #$0200              ; Player line points
C410: 3A              ABX                         
C411: EC 84           LDD     ,X                  
C413: C0 03           SUBB    #$03                
C415: D7 C2           STB     $C2                 ; {ram.C2}
C417: 80 03           SUBA    #$03                
;
C419: 8E 01 60        LDX     #$0160              ; Start of objects
C41C: 6D 06           TST     6,X                 ; Reached the end of the list?
C41E: 27 15           BEQ     $C435               ; {} yes ... done
C420: D6 C2           LDB     $C2                 ; {ram.C2}
C422: E0 02           SUBB    2,X                 ; Y coordinate
C424: 54              LSRB                        
C425: 26 0A           BNE     $C431               ; {}
C427: A1 84           CMPA    ,X                  
C429: 22 04           BHI     $C42F               ; {}
C42B: 6C 04           INC     4,X                 
C42D: 20 02           BRA     $C431               ; {}
C42F: 6C 05           INC     5,X                 
C431: 30 08           LEAX    8,X                 ; Check all ...
C433: 20 E7           BRA     $C41C               ; {} ... objects
;
C435: D6 C0           LDB     $C0                 ; {ram.C0}
C437: D1 C1           CMPB    $C1                 ; {ram.C1}
C439: 26 CC           BNE     $C407               ; {}
C43B: 8E 01 60        LDX     #$0160              
C43E: 0F C4           CLR     $C4                 ; {ram.NumLooped} Number of objects looped
C440: 0F C8           CLR     $C8                 ; {ram.LoopScoreTmp} Sum of ...
C442: 0F C9           CLR     $C9                 ; {ram.LoopScoreTmp+1} ... looped objects score
;
C444: E6 06           LDB     6,X                 ; End of the object list?
C446: 27 5D           BEQ     $C4A5               ; {} Yes ... done
C448: 6D 04           TST     4,X                 
C44A: 27 55           BEQ     $C4A1               ; {}
C44C: 6D 05           TST     5,X                 
C44E: 27 51           BEQ     $C4A1               ; {}
C450: C1 08           CMPB    #$08                ; This object a skull?
C452: 27 4D           BEQ     $C4A1               ; {} Yes ... it doesn't count ... next object
C454: 0C C4           INC     $C4                 ; {ram.NumLooped} ?? number of objects looped?
C456: 0C D0           INC     $D0                 ; {ram.D0}
C458: 0A CE           DEC     $CE                 ; {ram.CE}
C45A: 33 8D 0B 4B     LEAU    $CFA9,PC            ; {code.ScoreTable} The table of object scores
C45E: E6 C5           LDB     B,U                 ; Get the score for this object
C460: 1D              SEX                         ; No score is greater than 127 ... this is a quick way to clear A
C461: D3 C8           ADDD    $C8                 ; {ram.LoopScoreTmp} Add the score ...
C463: DD C8           STD     $C8                 ; {ram.LoopScoreTmp} ... to the accumulated loop score
C465: CE 00 EA        LDU     #$00EA              ; Descriptor for erasing
C468: E6 84           LDB     ,X                  ; Copy ...
C46A: E7 C4           STB     ,U                  ; ... X coordinate
C46C: E6 02           LDB     2,X                 ; Copy ...
C46E: E7 42           STB     2,U                 ; ... Y coordinate
C470: 33 8D 07 B7     LEAU    $CC2B,PC            ; {code.GenericEraser} Erase the ...
C474: 17 03 E4        LBSR    $C85B               ; {code.Erase8x8} ... object
C477: E6 06           LDB     6,X                 ; Is this ...
C479: C1 05           CMPB    #$05                ; ... a yoyo?
C47B: 26 11           BNE     $C48E               ; {} No ... skip the string
C47D: 33 8D 07 19     LEAU    $CB9A,PC            ; {code.StringEraser} Line erase graphic
C481: 17 03 D7        LBSR    $C85B               ; {code.Erase8x8} Erase the string
C484: E6 02           LDB     2,X                 ; Move ...
C486: C0 04           SUBB    #$04                ; ... up by ...
C488: E7 02           STB     2,X                 ; ... 4 pixels
C48A: C1 03           CMPB    #$03                ; At the top of the screen?
C48C: 2E F3           BGT     $C481               ; {} No ... keep erasing possible string
C48E: 1F 13           TFR     X,U                 ; For memory copy
C490: C6 08           LDB     #$08                ; 8 bytes per object
C492: DF D2           STU     $D2                 ; {ram.NextFreeObj} ?? end of object list?
C494: A6 48           LDA     8,U                 ; Close ...
C496: A7 C0           STA     ,U+                 ; ... up ...
C498: 5A              DECB                        ; ... list ...
C499: 26 F9           BNE     $C494               ; {} ... over ...
C49B: 6D 46           TST     6,U                 ; ... removed ...
C49D: 26 F1           BNE     $C490               ; {} ... object
C49F: 20 A3           BRA     $C444               ; {} Next object
;
C4A1: 30 08           LEAX    8,X                 ; Next object
C4A3: 20 9F           BRA     $C444               ; {} Continue checking

C4A5: 0D C4           TST     $C4                 ; {ram.NumLooped} Were any objects looped?
C4A7: 27 51           BEQ     $C4FA               ; {} No ... skip score update
C4A9: 17 02 73        LBSR    $C71F               ; {code.EraseLoopScore} Erase any loop score being shown
C4AC: 4F              CLRA                        ; Score for all ...
C4AD: 5F              CLRB                        ; Looped ...
C4AE: D3 C8           ADDD    $C8                 ; {ram.LoopScoreTmp} Sum of looped objects score
C4B0: 0A C4           DEC     $C4                 ; {ram.NumLooped} Multiply score of summed by ...
C4B2: 26 FA           BNE     $C4AE               ; {} ... number of objects looped
C4B4: DD CA           STD     $CA                 ; {ram.LoopScoreShown} The value of the loop score to show
C4B6: 0D B6           TST     $B6                 ; {ram.Player} Player 0 or 1
C4B8: 26 06           BNE     $C4C0               ; {} ... player 1
C4BA: D3 B7           ADDD    $B7                 ; {ram.P1Score} Player 1 score
C4BC: DD B7           STD     $B7                 ; {ram.P1Score} Update player 1 score
C4BE: 20 04           BRA     $C4C4               ; {} Continue
C4C0: D3 B9           ADDD    $B9                 ; {ram.P2Score} Player 2 score
C4C2: DD B9           STD     $B9                 ; {ram.P2Score} Update player 2 score
C4C4: C6 3C           LDB     #$3C                ; Counter for showing ...
C4C6: D7 C6           STB     $C6                 ; {ram.C6} ... loop score
C4C8: 8E 00 EA        LDX     #$00EA              ; Current game object
C4CB: E6 84           LDB     ,X                  ; X coordinate
C4CD: C1 60           CMPB    #$60                ; Too far to the right to print score?
C4CF: 2F 02           BLE     $C4D3               ; {} No ... keep it
C4D1: C6 60           LDB     #$60                ; Keep loop score on the screen
C4D3: E7 84           STB     ,X                  ; Constrained X coordinate
C4D5: 17 04 DA        LBSR    $C9B2               ; {code.GetScreenAndShift} Store the screen ...
C4D8: DF CC           STU     $CC                 ; {ram.LoopScoreLoc} ... location of the loop score
C4DA: 0C C7           INC     $C7                 ; {ram.HasLoopScore} We now have a loop score to show
C4DC: 17 01 31        LBSR    $C610               ; {code.PrintScores} Print the scores (both if 2 player)
;
; Make popping sound after scoring object
C4DF: 7F FF 20        CLR     $FF20               ; {hard.PIA1_DA} DAC to zero
C4E2: BD A9 76        JSR     $A976               ; Enable the sound
C4E5: C6 80           LDB     #$80                ; Outer loop
C4E7: 1F 98           TFR     B,A                 ; Outter to inner
C4E9: 4A              DECA                        ; Slight ...
C4EA: 26 FD           BNE     $C4E9               ; {} ... delay
C4EC: F7 FF 20        STB     $FF20               ; {hard.PIA1_DA} Store samples
C4EF: 1F 98           TFR     B,A                 ; Another ...
C4F1: 4A              DECA                        ; ... slight ...
C4F2: 26 FD           BNE     $C4F1               ; {} ... delay
C4F4: 7F FF 20        CLR     $FF20               ; {hard.PIA1_DA} DAC to 0
C4F7: 5A              DECB                        ; All loops made?
C4F8: 26 ED           BNE     $C4E7               ; {} No ... continue popping sound
;
C4FA: 8E 02 00        LDX     #$0200              
C4FD: D6 BE           LDB     $BE                 ; {ram.EndOfPlayer}
C4FF: 3A              ABX                         
C500: CE 00 D8        LDU     #$00D8              
C503: A6 C4           LDA     ,U                  
C505: E6 42           LDB     2,U                 
C507: ED 84           STD     ,X                  
C509: D6 BF           LDB     $BF                 ; {ram.OrigPixel} The pixel the player over-drew
C50B: DB BD           ADDB    $BD                 ; {ram.Collision} Mark ...
C50D: D7 BD           STB     $BD                 ; {ram.Collision} ... collision
C50F: 0C BE           INC     $BE                 ; {ram.EndOfPlayer} Next point ...
C511: 0C BE           INC     $BE                 ; {ram.EndOfPlayer} ... slot in player line
C513: 0C D1           INC     $D1                 ; {ram.D1}
C515: 10 26 00 B3     LBNE    $C5CC               ; {}
C519: D6 CE           LDB     $CE                 ; {ram.CE}
C51B: C1 13           CMPB    #$13                
C51D: 10 2C 00 AB     LBGE    $C5CC               ; {}
C521: 0C CE           INC     $CE                 ; {ram.CE}
C523: 33 8D 0A 7A     LEAU    $CFA1,PC            ; {}
C527: 17 05 54        LBSR    $CA7E               ; {code.PlaySong} ?? Is this the touch an object sound?
C52A: 96 D0           LDA     $D0                 ; {ram.D0}
C52C: 48              ASLA                        
C52D: 48              ASLA                        
C52E: 8E 00 B7        LDX     #$00B7              
C531: D6 B6           LDB     $B6                 ; {ram.Player}
C533: 58              ASLB                        
C534: AB 85           ADDA    B,X                 
C536: 94 D7           ANDA    $D7                 ; {ram.Random}
C538: 97 D1           STA     $D1                 ; {ram.D1}
C53A: A6 85           LDA     B,X                 
C53C: 8B 04           ADDA    #$04                
C53E: D6 D7           LDB     $D7                 ; {ram.Random}
C540: 3D              MUL                         
C541: 84 07           ANDA    #$07                ; Random object type ...
C543: 4C              INCA                        ; ... from 1 to 8
C544: 81 08           CMPA    #$08                ; Is this a skull?
C546: 26 09           BNE     $C551               ; {} No ... keep whatever it is
C548: 0C CF           INC     $CF                 ; {ram.SkullCount} Bump the skull count
C54A: D6 CF           LDB     $CF                 ; {ram.SkullCount} Do we have ...
C54C: C1 0A           CMPB    #$0A                ; ... 10 skulls on the screen?
C54E: 23 01           BLS     $C551               ; {} No ... this is a new skull
C550: 4C              INCA                        ; Yes ... promote this to a moving "X"
C551: 9E D2           LDX     $D2                 ; {ram.NextFreeObj}
C553: A7 06           STA     6,X                 
C555: 6F 07           CLR     7,X                 
C557: 96 D7           LDA     $D7                 ; {ram.Random}
C559: 1F 89           TFR     A,B                 
C55B: 54              LSRB                        
C55C: 46              RORA                        
C55D: 54              LSRB                        
C55E: 46              RORA                        
C55F: 97 D7           STA     $D7                 ; {ram.Random}
C561: 54              LSRB                        
C562: 46              RORA                        
C563: 54              LSRB                        
C564: 46              RORA                        
C565: C6 44           LDB     #$44                
C567: 3D              MUL                         
C568: 8B 08           ADDA    #$08                
C56A: A7 02           STA     2,X                 
C56C: 96 D7           LDA     $D7                 ; {ram.Random}
C56E: C6 60           LDB     #$60                
C570: 3D              MUL                         
C571: 84 FC           ANDA    #$FC                
C573: 8B 0C           ADDA    #$0C                
C575: 8B 04           ADDA    #$04                
C577: 81 6C           CMPA    #$6C                
C579: 24 FA           BHS     $C575               ; {}
C57B: 81 10           CMPA    #$10                
C57D: 23 F6           BLS     $C575               ; {}
C57F: A7 84           STA     ,X                  
C581: E6 02           LDB     2,X                 
C583: CE 00 D8        LDU     #$00D8              
C586: E0 42           SUBB    2,U                 
C588: CB 14           ADDB    #$14                
C58A: C1 28           CMPB    #$28                
C58C: 24 0C           BHS     $C59A               ; {}
C58E: A0 C4           SUBA    ,U                  
C590: 8B 14           ADDA    #$14                
C592: 81 28           CMPA    #$28                
C594: 24 04           BHS     $C59A               ; {}
C596: A6 84           LDA     ,X                  
C598: 20 DB           BRA     $C575               ; {}
C59A: 1F 13           TFR     X,U                 
C59C: 11 83 01 60     CMPU    #$0160              
C5A0: 27 2A           BEQ     $C5CC               ; {}
C5A2: 33 58           LEAU    -8,U                
C5A4: E6 46           LDB     6,U                 
C5A6: E1 06           CMPB    6,X                 
C5A8: 26 F2           BNE     $C59C               ; {}
C5AA: E6 84           LDB     ,X                  
C5AC: E0 C4           SUBB    ,U                  
C5AE: CB 08           ADDB    #$08                
C5B0: C1 10           CMPB    #$10                
C5B2: 22 E8           BHI     $C59C               ; {}
C5B4: E6 02           LDB     2,X                 
C5B6: E0 42           SUBB    2,U                 
C5B8: CB 08           ADDB    #$08                
C5BA: C1 10           CMPB    #$10                
C5BC: 22 DE           BHI     $C59C               ; {}
C5BE: E6 02           LDB     2,X                 
C5C0: CB 15           ADDB    #$15                
C5C2: C1 4C           CMPB    #$4C                
C5C4: 2D 02           BLT     $C5C8               ; {}
C5C6: C0 44           SUBB    #$44                
C5C8: E7 02           STB     2,X                 
C5CA: 20 CA           BRA     $C596               ; {}
C5CC: 17 05 20        LBSR    $CAEF               ; {code.WaitVBlank} Sync the gameloop to VBLANK
;
C5CF: 0D C7           TST     $C7                 ; {ram.HasLoopScore} Is there a loop score showing?
C5D1: 27 09           BEQ     $C5DC               ; {} No ... skip timing it out
C5D3: 0A C6           DEC     $C6                 ; {ram.C6} Time to erase it?
C5D5: 26 05           BNE     $C5DC               ; {} No ... leave it alone
C5D7: 17 01 45        LBSR    $C71F               ; {code.EraseLoopScore} Erase the loop score
C5DA: 0F C7           CLR     $C7                 ; {ram.HasLoopScore} No longer showing the loop score
C5DC: 0A D5           DEC     $D5                 ; {ram.FlashCount} Time to flash the player word?
;
C5DE: 26 2F           BNE     $C60F               ; {} No ... skip it
C5E0: C6 28           LDB     #$28                ; Reload the ...
C5E2: D7 D5           STB     $D5                 ; {ram.FlashCount} ... player word flash counter
C5E4: C6 58           LDB     #$58                ; Y coordinate of player word
C5E6: 0D B6           TST     $B6                 ; {ram.Player} Player one?
C5E8: 26 12           BNE     $C5FC               ; {} No ... go to player one
C5EA: 86 18           LDA     #$18                ; X coordinate of player "one"
C5EC: 03 D6           COM     $D6                 ; {ram.FlashType} Value was zero?
C5EE: 26 06           BNE     $C5F6               ; {} Yes ... erase the word
C5F0: 33 8D 06 89     LEAU    $CC7D,PC            ; {code.StrOne} No ... print the word
C5F4: 20 16           BRA     $C60C               ; {} Go print and out
C5F6: 33 8D 06 31     LEAU    $CC2B,PC            ; {code.GenericEraser} Erase the word
C5FA: 20 10           BRA     $C60C               ; {} Go erase and out
;
C5FC: 86 52           LDA     #$52                ; X coordinate for "two"
C5FE: 03 D6           COM     $D6                 ; {ram.FlashType} Value was zero?
C600: 26 06           BNE     $C608               ; {} Yes ... erase the word
C602: 33 8D 06 98     LEAU    $CC9E,PC            ; {code.StrTwo} No ... print the word
C606: 20 04           BRA     $C60C               ; {} Go print and out
C608: 33 8D 06 1F     LEAU    $CC2B,PC            ; {code.GenericEraser} Erase graphics
C60C: 17 03 34        LBSR    $C943               ; {code.PrintChars} Draw whatever graphics
C60F: 39              RTS                         ; Done

PrintScores:
C610: C6 FF           LDB     #$FF                ; White background chars ...
C612: D7 C5           STB     $C5                 ; {ram.DigitColor} ... for score digits
C614: DC B7           LDD     $B7                 ; {ram.P1Score} Player one score
C616: CE 0F 2B        LDU     #$0F2B              ; Location of player one score on screen
C619: 17 00 0F        LBSR    $C62B               ; {code.DrawNumber} Print player one score
C61C: 0D B4           TST     $B4                 ; {ram.NumPlayers} Is there a second player?
C61E: 27 08           BEQ     $C628               ; {} No ... skip player two score
C620: DC B9           LDD     $B9                 ; {ram.P2Score} Player two score
C622: CE 0F 3A        LDU     #$0F3A              ; Location of player two score on screen
C625: 17 00 03        LBSR    $C62B               ; {code.DrawNumber} Print the player two score
C628: 0F C5           CLR     $C5                 ; {ram.DigitColor} Default back to black background chars
C62A: 39              RTS                         ; Done

DrawNumber:
; Numbers are kept in words ... max value 65_536. Max 5 digits.
; An extra "0" is always added to the end of the number (multiply by 10)
C62B: 10 83 27 10     CMPD    #$2710              ; Decimal 10_000
C62F: 24 14           BHS     $C645               ; {} Handle digits
C631: 10 83 03 E8     CMPD    #$03E8              ; Decimal 1_000
C635: 24 13           BHS     $C64A               ; {} Handle 4 digits
C637: 10 83 00 64     CMPD    #$0064              ; Decimal 100
C63B: 24 12           BHS     $C64F               ; {} Handle 3 digits
C63D: 10 83 00 0A     CMPD    #$000A              ; Decimal 10
C641: 24 11           BHS     $C654               ; {} Handle 2 digit
C643: 20 14           BRA     $C659               ; {} Just one digit
;
C645: 8E 27 10        LDX     #$2710              ; Base amount 10000
C648: 8D 19           BSR     $C663               ; {} Draw digit picture
C64A: 8E 03 E8        LDX     #$03E8              ; Base amount 1000
C64D: 8D 14           BSR     $C663               ; {} Draw digit picture
C64F: 8E 00 64        LDX     #$0064              ; Base amount 100
C652: 8D 0F           BSR     $C663               ; {} Draw digit picture
C654: 8E 00 0A        LDX     #$000A              ; Base amount 10
C657: 8D 0A           BSR     $C663               ; {} Draw digit picture
C659: 8E 00 01        LDX     #$0001              ; Base amount 1
C65C: 8D 05           BSR     $C663               ; {} Draw digit picture
C65E: 4F              CLRA                        ; Add a ...
C65F: 5F              CLRB                        ; ... zero to everything
C660: 8D 01           BSR     $C663               ; {} Print 0
C662: 39              RTS                         ; Done
;
C663: 34 10           PSHS    X                   ; Hold the value
C665: 30 8D 00 78     LEAX    $C6E1,PC            ; {code.Digit0} Graphics for "0"
C669: A3 E4           SUBD    ,S                  ; Subtract off base amount
C66B: 25 46           BLO     $C6B3               ; {} This is the digit
C66D: 30 8D 00 75     LEAX    $C6E6,PC            ; {code.Digit1} Graphics for "1"
C671: A3 E4           SUBD    ,S                  ; Subtract off base amount
C673: 25 3E           BLO     $C6B3               ; {} This is the digit
C675: 30 8D 00 72     LEAX    $C6EB,PC            ; {code.Digit2} Graphics for "2"
C679: A3 E4           SUBD    ,S                  ; Subtract off base amount
C67B: 25 36           BLO     $C6B3               ; {} This is the digit
C67D: 30 8D 00 6F     LEAX    $C6F0,PC            ; {code.Digit3} Graphics for "3"
C681: A3 E4           SUBD    ,S                  ; Subtract off base amount
C683: 25 2E           BLO     $C6B3               ; {} This is the digit
C685: 30 8D 00 6C     LEAX    $C6F5,PC            ; {code.Digit4} Graphics for "4"
C689: A3 E4           SUBD    ,S                  ; Subtract off base amount
C68B: 25 26           BLO     $C6B3               ; {} This is the digit
C68D: 30 8D 00 69     LEAX    $C6FA,PC            ; {code.Digit5} Graphics for "5"
C691: A3 E4           SUBD    ,S                  ; Subtract off base amount
C693: 25 1E           BLO     $C6B3               ; {} This is the digit
C695: 30 8D 00 66     LEAX    $C6FF,PC            ; {code.Digit6} Graphics for "6"
C699: A3 E4           SUBD    ,S                  ; Subtract off base amount
C69B: 25 16           BLO     $C6B3               ; {} This is the digit
C69D: 30 8D 00 63     LEAX    $C704,PC            ; {code.Digit7} Graphics for "7"
C6A1: A3 E4           SUBD    ,S                  ; Subtract off base amount
C6A3: 25 0E           BLO     $C6B3               ; {} This is the digit
C6A5: 30 8D 00 60     LEAX    $C709,PC            ; {code.Digit8} Graphics for "8"
C6A9: A3 E4           SUBD    ,S                  ; Subtract off base amount
C6AB: 25 06           BLO     $C6B3               ; {} This is the digit
C6AD: 30 8D 00 5D     LEAX    $C70E,PC            ; {code.Digit9} Graphics for "9"
C6B1: A3 E4           SUBD    ,S                  ; Subtract off base amount
C6B3: E3 E4           ADDD    ,S                  ; Add one base amount back (we overshot above)
C6B5: 34 06           PSHS    B,A                 ; Hold the value
C6B7: E6 84           LDB     ,X                  ; Get first row data
C6B9: 54              LSRB                        ; Everything draw in color "01" (not sure why it wasn't defined that way to begin with)
C6BA: D8 C5           EORB    $C5                 ; {ram.DigitColor} Flip the color if needed
C6BC: E7 C0           STB     ,U+                 ; Store to screen
C6BE: E6 01           LDB     1,X                 ; Repeat ...
C6C0: 54              LSRB                        ; ... with ...
C6C1: D8 C5           EORB    $C5                 ; {ram.DigitColor} ... next ...
C6C3: E7 C8 1F        STB     $1F,U               ; ... row
C6C6: E6 02           LDB     2,X                 ; Repeat ...
C6C8: 54              LSRB                        ; ... with ...
C6C9: D8 C5           EORB    $C5                 ; {ram.DigitColor} ... next ...
C6CB: E7 C8 3F        STB     $3F,U               ; ... row
C6CE: E6 03           LDB     3,X                 ; Repeat ...
C6D0: 54              LSRB                        ; ... with ...
C6D1: D8 C5           EORB    $C5                 ; {ram.DigitColor} ... next ...
C6D3: E7 C8 5F        STB     $5F,U               ; ... row
C6D6: E6 04           LDB     4,X                 ; Repeat ...
C6D8: 54              LSRB                        ; ... with ...
C6D9: D8 C5           EORB    $C5                 ; {ram.DigitColor} ... next ...
C6DB: E7 C8 7F        STB     $7F,U               ; ... row
C6DE: 35 16           PULS    A,B,X               ; Restore
C6E0: 39              RTS                         ; Done
```

```html
<canvas width="754" height="96"
  data-canvasFunction="TileEngine.handleTileCanvas"
  data-getTileDataFunction="Doubleback.get8x5Tile"
  data-gridX="4"
  data-gridY="5"
  data-colors='["#000000","#FF0000","#0000FF","#FFFFFF"]'  
  data-address="C6E1"
  data-labelColor=""
  data-pixWidth="15"
  data-pixHeight="15"
  data-gap="1"
  data-background="#808080"
  data-margin="10"
  data-command="0,+x,1,+x,2,+x,3,+x,4,+x,5,+x,6,+x,7,+x,8,+x,9">
</canvas>
```

```code
Digit0:
; ..#.....
; #...#...
; #...#...
; #...#...
; ..#.....
C6E1: 20 88 88 88 20 

Digit1:
; ..#.....
; #.#.....
; ..#.....
; ..#.....
; #.#.#...
C6E6: 20 A0 20 20 A8

Digit2:
; ..#.....
; #...#...
; ....#...
; ..#.....
; #.#.#...
C6EB: 20 88 08 20 A8 

Digit3:
; #.#.#...
; ....#...
; ..#.#...
; ....#...
; #.#.#...
C6F0: A8 08 28 08 A8 

Digit4:
; #.......
; #...#...
; #...#...
; #.#.#...
; ....#...
C6F5: 80 88 88 A8 08            

Digit5:
; #.#.#...
; #.......
; ..#.....
; ....#...
; #.#.....
C6FA: A8 80 20 08 A0 

Digit6:
; #.#.#...
; #.......
; #.#.#...
; #...#...
; #.#.#...
C6FF: A8 80 A8 88 A8 

Digit7:
; #.#.#...
; ....#...
; ....#...
; ..#.....
; ..#.....
C704: A8 08 08 20 20 

Digit8:
; #.#.#...
; #...#...
; #.#.#...
; #...#...
; #.#.#...
C709: A8 88 A8 88 A8 

Digit9:
; ..#.....
; #...#...
; ..#.#...
; ....#...
; #.#.....
C70E: 20 88 28 08 A0 

DrawLoopScore:
; If there is a loop score, draw it
C713: 0D C7           TST     $C7                 ; {ram.HasLoopScore} Is there a value?
C715: 27 07           BEQ     $C71E               ; {} No ... skip drawing it
C717: DE CC           LDU     $CC                 ; {ram.LoopScoreLoc} Screen coordinate
C719: DC CA           LDD     $CA                 ; {ram.LoopScoreShown} Value
C71B: 17 FF 0D        LBSR    $C62B               ; {code.DrawNumber} Draw number
C71E: 39              RTS                         ; Done

EraseLoopScore:
C71F: 0D C7           TST     $C7                 ; {ram.HasLoopScore} Is there a value?
C721: 27 2A           BEQ     $C74D               ; {} No ... skip erasing it
C723: DE CC           LDU     $CC                 ; {ram.LoopScoreLoc} Screen coordinate
C725: DC CA           LDD     $CA                 ; {ram.LoopScoreShown} Value
C727: 10 83 27 10     CMPD    #$2710              ; Decimal 10_000
C72B: 24 14           BHS     $C741               ; {} Erase 6 digits
C72D: 10 83 03 E8     CMPD    #$03E8              ; Decimal 1_000
C731: 24 10           BHS     $C743               ; {} Erase 5 digits
C733: 10 83 00 64     CMPD    #$0064              ; Decimal 100
C737: 24 0C           BHS     $C745               ; {} Erase 4 digits
C739: 10 83 00 0A     CMPD    #$000A              ; Decimal 10
C73D: 24 08           BHS     $C747               ; {} Erase 3 digits
C73F: 20 08           BRA     $C749               ; {} Erase 2 digits
;
; Erase number of digits
C741: 8D 0B           BSR     $C74E               ; {code.EraseDigit} Erase 1 digit and advance
C743: 8D 09           BSR     $C74E               ; {code.EraseDigit} Erase 1 digit and advance
C745: 8D 07           BSR     $C74E               ; {code.EraseDigit} Erase 1 digit and advance
C747: 8D 05           BSR     $C74E               ; {code.EraseDigit} Erase 1 digit and advance
C749: 8D 03           BSR     $C74E               ; {code.EraseDigit} Erase 1 digit and advance
C74B: 8D 01           BSR     $C74E               ; {code.EraseDigit} Erase 1 digit and advance
C74D: 39              RTS                         ; Done

EraseDigit:
; Erase the digit and advance U to next digit start
C74E: 6F C0           CLR     ,U+                 ; Erase 1st line and advance U
C750: 6F C8 1F        CLR     $1F,U               ; Erase 2nd line
C753: 6F C8 3F        CLR     $3F,U               ; Erase 3rd line
C756: 6F C8 5F        CLR     $5F,U               ; Erase 4th line
C759: 6F C8 7F        CLR     $7F,U               ; Erase 5th line
C75C: 39              RTS                         ; Done

Draw8x8:
; X = object pointer (has X,Y coordinate)
; U = pointer to data (8x8 pixels = 16 bytes)
C75D: C6 08           LDB     #$08                ; 8 Rows
C75F: 34 54           PSHS    U,X,B               ; Hold these
C761: 17 02 4E        LBSR    $C9B2               ; {code.GetScreenAndShift} Get pointer to screen memory
C764: 10 8E 03 80     LDY     #$0380              ; Mask table
C768: AE 63           LDX     3,S                 ; Incoming U (data pointer) to X
C76A: 5D              TSTB                        ; 0 means ...
C76B: 10 27 00 CA     LBEQ    $C839               ; {} ... draw with no shift
C76F: 5A              DECB                        ; 1 means ...
C770: 10 27 00 88     LBEQ    $C7FC               ; {} ... one pixel shift right
C774: 5A              DECB                        ; 2 means ...
C775: 10 27 00 3E     LBEQ    $C7B7               ; {} ... two pixel shift right
;
; One pixel shift left (three pixel shift right)
C779: E6 80           LDB     ,X+                 ; First byte of pixel data
C77B: 4F              CLRA                        ; Make it a word with leading 0s
C77C: 58              ASLB                        ; Shift ...
C77D: 49              ROLA                        ; ... left ...
C77E: 58              ASLB                        ; ... one ...
C77F: 49              ROLA                        ; ... pixel
C780: 34 06           PSHS    B,A                 ; Hold this
C782: E6 80           LDB     ,X+                 ; Second byte of pixel data
C784: 4F              CLRA                        ; Make it a word with leading 0s
C785: 58              ASLB                        ; Shift ...
C786: 49              ROLA                        ; ... left ...
C787: 58              ASLB                        ; ... one ...
C788: 49              ROLA                        ; ... pixel
C789: AB 61           ADDA    1,S                 ; Combine pixels ...
C78B: A7 61           STA     1,S                 ; ... in middle byte
C78D: 34 04           PSHS    B                   ; Third byte
C78F: A6 A5           LDA     B,Y                 ; Mask ...
C791: A4 42           ANDA    2,U                 ; ... screen ...
C793: AB E4           ADDA    ,S                  ; ... add pixels ...
C795: A7 42           STA     2,U                 ; ... to screen
C797: E6 62           LDB     2,S                 ; 2nd byte
C799: A6 A5           LDA     B,Y                 ; Mask ...
C79B: A4 41           ANDA    1,U                 ; ... screen ...
C79D: AB 62           ADDA    2,S                 ; ... add pixels ...
C79F: A7 41           STA     1,U                 ; ... to screen
C7A1: E6 61           LDB     1,S                 ; First byte
C7A3: A6 A5           LDA     B,Y                 ; Mask ...
C7A5: A4 C4           ANDA    ,U                  ; ... screen ...
C7A7: AB 61           ADDA    1,S                 ; ... add pixels ...
C7A9: A7 C4           STA     ,U                  ; ... to screen
C7AB: 32 63           LEAS    3,S                 ; Pull the 3-byte temporary
C7AD: 33 C8 20        LEAU    $20,U               ; Next row
C7B0: 6A E4           DEC     ,S                  ; All rows done?
C7B2: 26 C5           BNE     $C779               ; {} No ... keep going
C7B4: 16 00 A1        LBRA    $C858               ; {} Yes ... done
;
; Two pixel shift right
C7B7: E6 80           LDB     ,X+                 ; First byte of pixel data
C7B9: 4F              CLRA                        ; Make it a word with leading 0s
C7BA: 54              LSRB                        ; Shift ...
C7BB: 46              RORA                        ; ... right ...
C7BC: 54              LSRB                        ; ... two ...
C7BD: 46              RORA                        ; ...
C7BE: 54              LSRB                        ; ...
C7BF: 46              RORA                        ; ...
C7C0: 54              LSRB                        ; ...
C7C1: 46              RORA                        ; ... pixels
C7C2: 34 06           PSHS    B,A                 ; Hold this
C7C4: E6 80           LDB     ,X+                 ; Second byte of pixel data
C7C6: 4F              CLRA                        ; Make it a word with leading 0s
C7C7: 54              LSRB                        ; Shift ...
C7C8: 46              RORA                        ; ... right ...
C7C9: 54              LSRB                        ; ... two ...
C7CA: 46              RORA                        ; ...
C7CB: 54              LSRB                        ; ...
C7CC: 46              RORA                        ; ...
C7CD: 54              LSRB                        ; ...
C7CE: 46              RORA                        ; ... pixels
C7CF: EB E4           ADDB    ,S                  ; Combine pixels ...
C7D1: E7 E4           STB     ,S                  ; ... in middle byte
C7D3: 34 02           PSHS    A                   ; Third byte
C7D5: A6 A6           LDA     A,Y                 ; Mask ...
C7D7: A4 42           ANDA    2,U                 ; ... screen ...
C7D9: AB E4           ADDA    ,S                  ; ... add pixels ...
C7DB: A7 42           STA     2,U                 ; ... to screen
C7DD: E6 61           LDB     1,S                 ; 2nd byte
C7DF: A6 A5           LDA     B,Y                 ; Mask ...
C7E1: A4 41           ANDA    1,U                 ; ... screen ...
C7E3: AB 61           ADDA    1,S                 ; ... add pixels ...
C7E5: A7 41           STA     1,U                 ; ... to screen
C7E7: E6 62           LDB     2,S                 ; 3rd byte
C7E9: A6 A5           LDA     B,Y                 ; Mask ...
C7EB: A4 C4           ANDA    ,U                  ; ... screen ...
C7ED: AB 62           ADDA    2,S                 ; ... add pixels ...
C7EF: A7 C4           STA     ,U                  ; ... to screen
C7F1: 32 63           LEAS    3,S                 ; Pull the 3-byte temporary
C7F3: 33 C8 20        LEAU    $20,U               ; Next row
C7F6: 6A E4           DEC     ,S                  ; All rows done?
C7F8: 26 BD           BNE     $C7B7               ; {} No ... keep going
C7FA: 20 5C           BRA     $C858               ; {} Yes ... done
;
; One pixel shift right
C7FC: E6 80           LDB     ,X+                 ; First byte of pixel data
C7FE: 4F              CLRA                        ; Make it a word with leading 0s
C7FF: 54              LSRB                        ; Shift ...
C800: 46              RORA                        ; ... right ...
C801: 54              LSRB                        ; ... one ...
C802: 46              RORA                        ; ... pixel
C803: 34 06           PSHS    B,A                 ; Hold this
C805: E6 80           LDB     ,X+                 ; Second byte of pixel data
C807: 4F              CLRA                        ; Make it a word with leading 0s
C808: 54              LSRB                        ; Shift ...
C809: 46              RORA                        ; ... right ...
C80A: 54              LSRB                        ; ... one ...
C80B: 46              RORA                        ; ... pixel
C80C: EB E4           ADDB    ,S                  ; Combine pixels ...
C80E: E7 E4           STB     ,S                  ; ... in middle byte
C810: 34 02           PSHS    A                   ; Third byte
C812: A6 A6           LDA     A,Y                 ; Mask ...
C814: A4 42           ANDA    2,U                 ; ... screen ...
C816: AB E4           ADDA    ,S                  ; ... add pixels ...
C818: A7 42           STA     2,U                 ; ... to screen
C81A: E6 61           LDB     1,S                 ; 2nd byte
C81C: A6 A5           LDA     B,Y                 ; Mask ...
C81E: A4 41           ANDA    1,U                 ; ... screen ...
C820: AB 61           ADDA    1,S                 ; ... add pixels ...
C822: A7 41           STA     1,U                 ; ... to screen
C824: E6 62           LDB     2,S                 ; 3rd byte
C826: A6 A5           LDA     B,Y                 ; Mask ...
C828: A4 C4           ANDA    ,U                  ; ... screen ...
C82A: AB 62           ADDA    2,S                 ; ... add pixels ...
C82C: A7 C4           STA     ,U                  ; ... to screen
C82E: 32 63           LEAS    3,S                 ; Pull the 3-byte temporary
C830: 33 C8 20        LEAU    $20,U               ; Next row
C833: 6A E4           DEC     ,S                  ; All rows done?
C835: 26 C5           BNE     $C7FC               ; {} No ... keep going
C837: 20 1F           BRA     $C858               ; {} All done
;               
; Draw with no shift
C839: EC 81           LDD     ,X++                ; Pixel data
C83B: 34 06           PSHS    B,A                 ; Hold it
C83D: A6 A6           LDA     A,Y                 ; Look up mask for value
C83F: A4 C4           ANDA    ,U                  ; Get pixels from screen
C841: AB E4           ADDA    ,S                  ; Add in the image pixels
C843: A7 C4           STA     ,U                  ; To the screen
C845: E6 61           LDB     1,S                 ; 2nd byte
C847: A6 A5           LDA     B,Y                 ; Look up mask for value
C849: A4 41           ANDA    1,U                 ; Get pixels from screen
C84B: AB 61           ADDA    1,S                 ; Add in the image pixels
C84D: A7 41           STA     1,U                 ; To the screen
C84F: 32 62           LEAS    2,S                 ; Pop the temporaries
C851: 33 C8 20        LEAU    $20,U               ; Next row
C854: 6A E4           DEC     ,S                  ; All rows done?
C856: 26 E1           BNE     $C839               ; {} No ... keep going
C858: 35 54           PULS    B,X,U               ; Restore
C85A: 39              RTS                         ; Done

Erase8x8:
; X = object pointer (has X,Y coordinate)
; U = pointer to data (8x8 pixels = 16 bytes)
C85B: C6 08           LDB     #$08                ; 8 rows
C85D: 34 54           PSHS    U,X,B               ; Hold these
C85F: 17 01 50        LBSR    $C9B2               ; {code.GetScreenAndShift} Get pointer to screen memory
C862: 10 8E 03 80     LDY     #$0380              ; Mask table
C866: AE 63           LDX     3,S                 ; Incoming U (data pointer) to X
C868: 5D              TSTB                        ; 0 means ...
C869: 10 27 00 B8     LBEQ    $C925               ; {} ... erase with no shift
C86D: 5A              DECB                        ; 1 means ...
C86E: 10 27 00 7C     LBEQ    $C8EE               ; {} ... one pixel shift right
C872: 5A              DECB                        ; 2 means ...
C873: 10 27 00 38     LBEQ    $C8AF               ; {} ... two pixel shift right
;
; One pixel shift left (three pixel shift right)
C877: E6 80           LDB     ,X+                 ; First byte of pixel data
C879: 4F              CLRA                        ; Make it a word with leading 0s
C87A: 58              ASLB                        ; Shift ...
C87B: 49              ROLA                        ; ... left ...
C87C: 58              ASLB                        ; ... one ...
C87D: 49              ROLA                        ; ... pixel
C87E: 34 06           PSHS    B,A                 ; Hold this
C880: E6 80           LDB     ,X+                 ; Second byte of pixel data
C882: 4F              CLRA                        ; Make it a word with leading 0s
C883: 58              ASLB                        ; Shift ...
C884: 49              ROLA                        ; ... left ...
C885: 58              ASLB                        ; ... one ...
C886: 49              ROLA                        ; ... pixel
C887: AB 61           ADDA    1,S                 ; Combine pixels ...
C889: A7 61           STA     1,S                 ; ... in middle byte
C88B: 34 04           PSHS    B                   ; Third byte
C88D: A6 A5           LDA     B,Y                 ; Mask ...
C88F: A4 42           ANDA    2,U                 ; ... screen ...
C891: A7 42           STA     2,U                 ; ... to screen
C893: E6 62           LDB     2,S                 ; 2nd byte
C895: A6 A5           LDA     B,Y                 ; Mask ...
C897: A4 41           ANDA    1,U                 ; ... screen ...
C899: A7 41           STA     1,U                 ; ... to screen
C89B: E6 61           LDB     1,S                 ; 3rd byte
C89D: A6 A5           LDA     B,Y                 ; Mask ...
C89F: A4 C4           ANDA    ,U                  ; ... screen ...
C8A1: A7 C4           STA     ,U                  ; ... to screen
C8A3: 32 63           LEAS    3,S                 ; Pull the 3-byte temporary
C8A5: 33 C8 20        LEAU    $20,U               ; Next row
C8A8: 6A E4           DEC     ,S                  ; All rows done?
C8AA: 26 CB           BNE     $C877               ; {} No ... keep going
C8AC: 16 00 91        LBRA    $C940               ; {} yest ... done
;
; Two pixel shift right
C8AF: E6 80           LDB     ,X+                 ; First byte of pixel data
C8B1: 4F              CLRA                        ; Make it a word with leading 0s
C8B2: 54              LSRB                        ; Shift ...
C8B3: 46              RORA                        ; ... right ...
C8B4: 54              LSRB                        ; ... two ...
C8B5: 46              RORA                        ; ...
C8B6: 54              LSRB                        ; ...
C8B7: 46              RORA                        ; ...
C8B8: 54              LSRB                        ; ...
C8B9: 46              RORA                        ; ... pixels
C8BA: 34 06           PSHS    B,A                 ; Hold this
C8BC: E6 80           LDB     ,X+                 ; Second byte of pixel data
C8BE: 4F              CLRA                        ; Shift ...
C8BF: 54              LSRB                        ; ... right ...
C8C0: 46              RORA                        ; ... two
C8C1: 54              LSRB                        ; ...
C8C2: 46              RORA                        ; ...
C8C3: 54              LSRB                        ; ...
C8C4: 46              RORA                        ; ...
C8C5: 54              LSRB                        ; ...
C8C6: 46              RORA                        ; ... pixels
C8C7: EB E4           ADDB    ,S                  ; Combine pixels ...
C8C9: E7 E4           STB     ,S                  ; ... in middle byte
C8CB: 34 02           PSHS    A                   ; Third byte
C8CD: A6 A6           LDA     A,Y                 ; Mask ...
C8CF: A4 42           ANDA    2,U                 ; ... screen ...
C8D1: A7 42           STA     2,U                 ; ... to screen
C8D3: E6 61           LDB     1,S                 ; Second byte
C8D5: A6 A5           LDA     B,Y                 ; Mask ...
C8D7: A4 41           ANDA    1,U                 ; ... screen ...
C8D9: A7 41           STA     1,U                 ; ... to screen
C8DB: E6 62           LDB     2,S                 ; Third byte
C8DD: A6 A5           LDA     B,Y                 ; Mask ...
C8DF: A4 C4           ANDA    ,U                  ; ... screen ...
C8E1: A7 C4           STA     ,U                  ; ... to screen
C8E3: 32 63           LEAS    3,S                 ; Pull the 3-byte temporary
C8E5: 33 C8 20        LEAU    $20,U               ; Next row
C8E8: 6A E4           DEC     ,S                  ; All rows done?
C8EA: 26 C3           BNE     $C8AF               ; {} No ... keep going
C8EC: 20 52           BRA     $C940               ; {} Yes ... done
;
; One pixel shift right
C8EE: E6 80           LDB     ,X+                 ; First byte of pixel data
C8F0: 4F              CLRA                        ; Make it a word with leading 0s
C8F1: 54              LSRB                        ; Shift ...
C8F2: 46              RORA                        ; ... right ...
C8F3: 54              LSRB                        ; ... one ...
C8F4: 46              RORA                        ; ... pixel
C8F5: 34 06           PSHS    B,A                 ; Hold this
C8F7: E6 80           LDB     ,X+                 ; Second byte of pixel data
C8F9: 4F              CLRA                        ; Make it a word with leading 0s
C8FA: 54              LSRB                        ; Shift ...
C8FB: 46              RORA                        ; ... right ...
C8FC: 54              LSRB                        ; ... one ...
C8FD: 46              RORA                        ; ... pixel
C8FE: EB E4           ADDB    ,S                  ; Combine pixels ...
C900: E7 E4           STB     ,S                  ; ... in middle byte
C902: 34 02           PSHS    A                   ; Third byte
C904: A6 A6           LDA     A,Y                 ; Mask ...
C906: A4 42           ANDA    2,U                 ; ... screen ...
C908: A7 42           STA     2,U                 ; ... to screen
C90A: E6 61           LDB     1,S                 ; 2nd byte
C90C: A6 A5           LDA     B,Y                 ; Mask ...
C90E: A4 41           ANDA    1,U                 ; ... screen ...
C910: A7 41           STA     1,U                 ; ... to screen
C912: E6 62           LDB     2,S                 ; Third byte
C914: A6 A5           LDA     B,Y                 ; Mask ...
C916: A4 C4           ANDA    ,U                  ; ... screen ...
C918: A7 C4           STA     ,U                  ; ... to screen
C91A: 32 63           LEAS    3,S                 ; Pull the 3 byte temporary
C91C: 33 C8 20        LEAU    $20,U               ; Next row
C91F: 6A E4           DEC     ,S                  ; All rows done?
C921: 26 CB           BNE     $C8EE               ; {} No ... keep going
C923: 20 1B           BRA     $C940               ; {} All done
;
; Erase with no shift
C925: EC 81           LDD     ,X++                ; Pixel data
C927: 34 06           PSHS    B,A                 ; Hold it
C929: A6 A6           LDA     A,Y                 ; Look up mask for value
C92B: A4 C4           ANDA    ,U                  ; Mask screen
C92D: A7 C4           STA     ,U                  ; Back to screen
C92F: E6 61           LDB     1,S                 ; 2nd byte
C931: A6 A5           LDA     B,Y                 ; Look up mask for value
C933: A4 41           ANDA    1,U                 ; Mas screen
C935: A7 41           STA     1,U                 ; Back to screen
C937: 32 62           LEAS    2,S                 ; Pop the temporaries
C939: 33 C8 20        LEAU    $20,U               ; Next row
C93C: 6A E4           DEC     ,S                  ; All rows done?
C93E: 26 E5           BNE     $C925               ; {} No ... keep going
C940: 35 54           PULS    B,X,U               ; Restore
C942: 39              RTS                         ; Done

PrintChars:
; A = X coordinate
; B = Y coordinate
; U = text string
C943: 8E 00 E4        LDX     #$00E4              ; Utility descriptor
C946: A7 84           STA     ,X                  ; Set the X coordinate
C948: E7 02           STB     2,X                 ; Set the Y coordinate
C94A: E6 5F           LDB     -1,U                ; Characters ...
C94C: E7 04           STB     4,X                 ; ... to print
C94E: 17 FE 0C        LBSR    $C75D               ; {code.Draw8x8}
C951: 33 C8 10        LEAU    $10,U               ; Next image
C954: A6 84           LDA     ,X                  ; X coordinate
C956: 8B 08           ADDA    #$08                ; Next character ...
C958: A7 84           STA     ,X                  ; ... over
C95A: 6A 04           DEC     4,X                 ; All done?
C95C: 26 F0           BNE     $C94E               ; {} No ... do all
C95E: 39              RTS                         ; Done

SetPixel:
C95F: 17 00 50        LBSR    $C9B2               ; {code.GetScreenAndShift}
C962: A6 C4           LDA     ,U                  ; Value from screen
C964: 5D              TSTB                        ; Shift 0 means ...
C965: 26 0A           BNE     $C971               ; {} ... upper pixel
C967: 84 3F           ANDA    #$3F                ; Mask off upper pixel ..111111
C969: 1F 89           TFR     A,B                 ; Return the bits ... ?? used by the caller at C3BF
C96B: E0 C4           SUBB    ,U                  ; ... we removed
C96D: 8A 80           ORA     #$80                ; OR in the upper pixel
C96F: 20 22           BRA     $C993               ; {} Set and done
;
C971: 5A              DECB                        ; Shift 1 means ...
C972: 26 0A           BNE     $C97E               ; {} ... 2nd pixel
C974: 84 CF           ANDA    #$CF                ; Mask off the 2nd pixel 11..1111
C976: 1F 89           TFR     A,B                 ; Return the bits ...
C978: E0 C4           SUBB    ,U                  ; ... we removed
C97A: 8A 20           ORA     #$20                ; OR in the 2nd pixel
C97C: 20 15           BRA     $C993               ; {} Set and done
;
C97E: 5A              DECB                        ; Shift 2 means ...
C97F: 26 0A           BNE     $C98B               ; {} ... 3rd pixel
C981: 84 F3           ANDA    #$F3                ; Mask off the 3rd pixel 1111..11
C983: 1F 89           TFR     A,B                 ; Return the bits ...
C985: E0 C4           SUBB    ,U                  ; ... we removed
C987: 8A 08           ORA     #$08                ; OR in the 3rd pixel
C989: 20 08           BRA     $C993               ; {} Set and done
;
C98B: 84 FC           ANDA    #$FC                ; Mask off the last pixel 111111..
C98D: 1F 89           TFR     A,B                 ; Return the bits ...
C98F: E0 C4           SUBB    ,U                  ; ... we removed
C991: 8A 02           ORA     #$02                ; OR in the last pixel
;
C993: A7 C4           STA     ,U                  ; Store pixel to screen
C995: 39              RTS                         ; Done

ErasePixel:
; U = pointer to screen memory
C996: A6 C4           LDA     ,U                  ; Value from the screen
C998: 5D              TSTB                        ; Pixel shift value
C999: 26 04           BNE     $C99F               ; {} Not 0 (left most pixel) ... try others
C99B: 84 3F           ANDA    #$3F                ; Mask off the left most pixel ..111111
C99D: 20 10           BRA     $C9AF               ; {} Clear the pixel
C99F: 5A              DECB                        ; Is this the 2nd pixel?
C9A0: 26 04           BNE     $C9A6               ; {} No ... try the 3rd
C9A2: 84 CF           ANDA    #$CF                ; Mask off the 2nd pixel 11..1111
C9A4: 20 09           BRA     $C9AF               ; {} Clear the pixel
C9A6: 5A              DECB                        ; Is this the 3rd pixel?
C9A7: 26 04           BNE     $C9AD               ; {} No ... must be the 4th
C9A9: 84 F3           ANDA    #$F3                ; Mask off the 3rd pixel 1111..11
C9AB: 20 02           BRA     $C9AF               ; {} Clear the pixel
C9AD: 84 FC           ANDA    #$FC                ; Mask off the 4th pixel 111111..
C9AF: A7 C4           STA     ,U                  ; Clear the pixel on the screen
C9B1: 39              RTS                         ; Done
   
GetScreenAndShift:
; Ultimately, the equation for screen pointer is: Y*32 + X/4.
; This code cleverly does:
;     (Y*256 + X*2) / 8 = 
;     (Y*128 + X) / 4 = 
;     Y*32 + X/4
; Input: X pointer to object structure
; Mangle: A, Y
; Return: U screen pointer
; Return: B shift amount
C9B2: E6 84           LDB     ,X                  ; The object's X coordinate
C9B4: A6 02           LDA     2,X                 ; The object's Y coordinate
C9B6: 58              ASLB                        ; D = Y*256 + X*2
C9B7: 47              ASRA                        ; Divide ...
C9B8: 56              RORB                        ; ...
C9B9: 47              ASRA                        ; ...
C9BA: 56              RORB                        ; ...
C9BB: 47              ASRA                        ; ...
C9BC: 56              RORB                        ; ... eight
C9BD: 10 8E 04 00     LDY     #$0400              ; Start of screen memory
C9C1: 33 AB           LEAU    D,Y                 ; Point into screen memory
C9C3: E6 84           LDB     ,X                  ; X coordinate
C9C5: C4 03           ANDB    #$03                ; 4 pixels per byte ... 4 possible shifts
C9C7: 39              RTS                         ; Done

MoveObject:
; coordinates = coordinates + 8 * delta (with limits)
C9C8: E6 04           LDB     4,X                 ; Word ...
C9CA: 1D              SEX                         ; ... deltaX
C9CB: 58              ASLB                        ; Multiply ...
C9CC: 49              ROLA                        ; ...
C9CD: 58              ASLB                        ; ...
C9CE: 49              ROLA                        ; ... deltaX ...
C9CF: 58              ASLB                        ; ...
C9D0: 49              ROLA                        ; ... by 8
C9D1: E3 84           ADDD    ,X                  ; Add to the 2-byte X coordiante
C9D3: 80 03           SUBA    #$03                ; Temporarily translate for contraining
C9D5: 81 7B           CMPA    #$7B                ; X coordinate too high?
C9D7: 25 07           BLO     $C9E0               ; {} No ... keep it
C9D9: 86 7A           LDA     #$7A                ; Yes ... constrain it
C9DB: 6D 04           TST     4,X                 ; X coordinate too low?
C9DD: 2A 01           BPL     $C9E0               ; {} No ... keep it
C9DF: 4F              CLRA                        ; Yes ... constrain it
C9E0: 8B 03           ADDA    #$03                ; Translate back to the right
C9E2: ED 84           STD     ,X                  ; Store X coordinate (integer and fractional)
C9E4: E6 05           LDB     5,X                 ; Word ...
C9E6: 1D              SEX                         ; ... deltaY
C9E7: 58              ASLB                        ; Multiply ...
C9E8: 58              ASLB                        ; ...
C9E9: 58              ASLB                        ; ... ?? why no ROLA
C9EA: 49              ROLA                        ; ... by 8
C9EB: E3 02           ADDD    2,X                 ; Add to the 2-byte Y coordinate
C9ED: 80 03           SUBA    #$03                ; Temporarily translate for constraining
C9EF: 81 53           CMPA    #$53                ; Y coordinate too high?
C9F1: 25 07           BLO     $C9FA               ; {} No ... keep it
C9F3: 86 52           LDA     #$52                ; Yes ... constrain it
C9F5: 6D 05           TST     5,X                 ; Y coordinate too low?
C9F7: 2A 01           BPL     $C9FA               ; {} No ... keep it
C9F9: 4F              CLRA                        ; Yes ... constrain it
C9FA: 8B 03           ADDA    #$03                ; Translate back down
C9FC: ED 02           STD     2,X                 ; Store Y coordinate (integer and fractional)
C9FE: 39              RTS                         ; Done

FollowPlayer:
; X = object to move
C9FF: A7 04           STA     4,X                 ; Store the deltaX ...
CA01: E7 05           STB     5,X                 ; ... and deltaY
CA03: CE 00 D8        LDU     #$00D8              ; Player object to U
CA06: A6 84           LDA     ,X                  ; Objects are 8 pixels wide. Get ...
CA08: 8B 04           ADDA    #$04                ; ... the center X of the object
CA0A: A7 84           STA     ,X                  ; Update coordinate
CA0C: A0 C4           SUBA    ,U                  ; Compare object X to player X
CA0E: 2B 07           BMI     $CA17               ; {} Object X is less ... keep deltaX
CA10: 60 04           NEG     4,X                 ; Reverse direction on deltaX
CA12: 4D              TSTA                        ; Are the coordinates the same?
CA13: 26 02           BNE     $CA17               ; {} No ... keep this
CA15: 6F 04           CLR     4,X                 ; Yes ... no movement on X axis
;
CA17: E6 04           LDB     4,X                 ; DeltaX to B
CA19: A6 02           LDA     2,X                 ; Objects are 8 pixels tall. Get ...
CA1B: 8B 04           ADDA    #$04                ; ... the center Y of the object
CA1D: A7 02           STA     2,X                 ; Update coordinate
CA1F: A0 42           SUBA    2,U                 ; Compare object Y to player Y
CA21: 2B 07           BMI     $CA2A               ; {} Object Y is less ... keep deltaY
CA23: 60 05           NEG     5,X                 ; Reverse direction on deltaY
CA25: 4D              TSTA                        ; Are the coordinates the same?
CA26: 26 02           BNE     $CA2A               ; {} No ... keep this
CA28: 6F 05           CLR     5,X                 ; Yes ... no movement on Y axis
;
CA2A: 17 FF 9B        LBSR    $C9C8               ; {code.MoveObject} Move the object towards the player
CA2D: A6 84           LDA     ,X                  ; X coordinate
CA2F: 80 04           SUBA    #$04                ; Translate back to upper left corner
CA31: 81 03           CMPA    #$03                ; Is coordinate too small?
CA33: 2C 02           BGE     $CA37               ; {} No ... keep it.
CA35: 86 03           LDA     #$03                ; Yes ... constrain to X>=3
CA37: 81 76           CMPA    #$76                ; Is coordinate too big?
CA39: 2F 02           BLE     $CA3D               ; {} No ... keep it
CA3B: 86 76           LDA     #$76                ; Yes ... constrain to X<=118
CA3D: A7 84           STA     ,X                  ; Update the object's X coordiante
CA3F: A6 02           LDA     2,X                 ; Get the Y coordinate
CA41: 80 04           SUBA    #$04                ; Translate back to the upper left corner
CA43: 81 03           CMPA    #$03                ; Is coordinate too small?
CA45: 2C 02           BGE     $CA49               ; {} No ... keep it.
CA47: 86 03           LDA     #$03                ; Yes ... constrain to Y>=3
CA49: 81 4E           CMPA    #$4E                ; Is coordinate too big?
CA4B: 2F 02           BLE     $CA4F               ; {} No ... keep it
CA4D: 86 4E           LDA     #$4E                ; Yes ... constrain to Y<=78
CA4F: A7 02           STA     2,X                 ; Update the object's Y coordinate
CA51: 39              RTS                         ; Done

ClearScreen:
CA52: 5F              CLRB                        ; Clear value is black
FillScreen:
CA53: CE 04 00        LDU     #$0400              ; Start of screen
CA56: 33 C9 0C 00     LEAU    $0C00,U             ; Now to the end of screen
CA5A: E7 C2           STB     ,-U                 ; Store value ...
CA5C: 11 83 04 00     CMPU    #$0400              ; ... to the ...
CA60: 22 F8           BHI     $CA5A               ; {} ... screen
CA62: 39              RTS                         ; Done

DrawPlayfiled:
CA63: CE 04 00        LDU     #$0400              ; Start of screen
CA66: 33 C8 60        LEAU    $60,U               ; 3rd row down
CA69: 86 53           LDA     #$53                ; 83 rows in the playfield
CA6B: C6 F0           LDB     #$F0                ; 2 pixels on the left ...
CA6D: E7 C0           STB     ,U+                 ; ... are white
CA6F: C6 1E           LDB     #$1E                ; Clear ...
CA71: 6F C0           CLR     ,U+                 ; ... 30 columns ...
CA73: 5A              DECB                        ; ... on each ...
CA74: 26 FB           BNE     $CA71               ; {} ... row
CA76: C6 0F           LDB     #$0F                ; 2 pixels on the right ...
CA78: E7 C0           STB     ,U+                 ; ... are white
CA7A: 4A              DECA                        ; Do ...
CA7B: 26 EE           BNE     $CA6B               ; {} ... all rows
CA7D: 39              RTS                         ; Done

PlaySong:
CA7E: 7F FF 20        CLR     $FF20               ; {hard.PIA1_DA} D/A to 0
CA81: BD A9 76        JSR     $A976               ; Enable analog mux
CA84: 17 00 39        LBSR    $CAC0               ; {code.CheckForBreak}
CA87: EC C1           LDD     ,U++                ; Get next data
CA89: 27 34           BEQ     $CABF               ; {} No more ... done
CA8B: 34 06           PSHS    B,A                 ; 
CA8D: 1F 98           TFR     B,A                 
CA8F: 4A              DECA                        ; Delay amount
CA90: 1E 11           EXG     X,X                 ; Small ...
CA92: 1E 11           EXG     X,X                 ; ...
CA94: 1E 11           EXG     X,X                 ; ...
CA96: 1E 11           EXG     X,X                 ; ... delay
CA98: 26 F5           BNE     $CA8F               ; {} Finish the delay
CA9A: 86 3C           LDA     #$3C                ; 6 bit D/A to ...
CA9C: B7 FF 20        STA     $FF20               ; {hard.PIA1_DA} ... 111100
CA9F: 1F 98           TFR     B,A                 
CAA1: A0 61           SUBA    1,S                 
CAA3: 43              COMA                        
CAA4: 4A              DECA                        ; Delay amount
CAA5: 1E 11           EXG     X,X                 ; Small ...
CAA7: 1E 11           EXG     X,X                 ; ...
CAA9: 1E 11           EXG     X,X                 ; ...
CAAB: 1E 11           EXG     X,X                 ; ... delay
CAAD: 26 F5           BNE     $CAA4               ; {} Finish the delay
CAAF: 7F FF 20        CLR     $FF20               ; {hard.PIA1_DA} D/A to 0
CAB2: 5A              DECB                        
CAB3: 26 02           BNE     $CAB7               ; {}
CAB5: E6 61           LDB     1,S                 
CAB7: 6A E4           DEC     ,S                  
CAB9: 26 D2           BNE     $CA8D               ; {}
CABB: 35 06           PULS    A,B                 
CABD: 20 BF           BRA     $CA7E               ; {code.PlaySong} Play until end
CABF: 39              RTS                         ; Done

CheckForBreak:
CAC0: C6 FB           LDB     #$FB                ; All high but ...
CAC2: F7 FF 02        STB     $FF02               ; {hard.PIA0_DB} ... BREAK column
CAC5: F6 FF 00        LDB     $FF00               ; {hard.PIA0_DA} Read keyboard rows
CAC8: C4 40           ANDB    #$40                ; Is BREAK row low?
CACA: 10 27 F5 36     LBEQ    $C004               ; {code.Reset} Yes ...break is pressed ... restart
CACE: 39              RTS                         ; Break not pressed ... continue

SetVideoMode:
; Set mode 128x96 Color Graphics
; Set display offset to $400
; V2 V1 V0 7 6 5 4 3 2 1 0
;  1  0  0 1 1 1 1 1 x x x
CACF: 8D 1E           BSR     $CAEF               ; {code.WaitVBlank} Wait for VBLANK
CAD1: 8E FF C6        LDX     #$FFC6              ; Set ...
CAD4: E7 84           STB     ,X                  ; ... display ... 000010
CAD6: E7 03           STB     3,X                 ; ... offset to ...
CAD8: E7 04           STB     4,X                 ; ... 00010 ...
CADA: E7 06           STB     6,X                 ; ... 0.5K * 2 = 1K ...
CADC: E7 08           STB     8,X                 ; ... ...
CADE: E7 0A           STB     10,X                ; ... address=$400
CAE0: F7 FF C0        STB     $FFC0               ; {hard.dispMode} V0=0
CAE3: F7 FF C2        STB     $FFC2               ; {hard.dispMode+2} V1=0
CAE6: F7 FF C5        STB     $FFC5               ; {hard.dispMode+5} V2=1 (Mode 100 = G3C)
CAE9: C6 F8           LDB     #$F8                ; Bright screen ...
CAEB: F7 FF 22        STB     $FF22               ; {hard.PIA1_DB} ... color mode
CAEE: 39              RTS                         ; Cone

WaitVBlank:
CAEF: 7D FF 02        TST     $FF02               ; {hard.PIA0_DB} ??? why read the keyboard register? It doesn't clear anything
CAF2: 0C D7           INC     $D7                 ; {ram.Random} ?? randomness?
CAF4: 7D FF 03        TST     $FF03               ; {hard.PIA0_CB} Wait for ...
CAF7: 2A F9           BPL     $CAF2               ; {} ... vertical blank
CAF9: 39              RTS                         ; Cone

; Data from here down

ImageApple:
```

```html
<canvas width="138" height="138"
  data-canvasFunction="TileEngine.handleTileCanvas"
  data-getTileDataFunction="Doubleback.get8x8Tile"
  data-gridY="8"
  data-gridX="8"
  data-colors='["#000000","#FF0000","#0000FF","#FFFFFF"]'
  data-address="CAFA"
  data-labelColor=""
  data-pixWidth="15"
  data-pixHeight="15"
  data-gap="1"
  data-background="#808080"
  data-margin="10"
  data-command="0">
</canvas>
```

```code
; Object type 1
CAFA: 00 80 ; ....2...
CAFC: 16 50 ; .11211..
CAFE: 55 54 ; 1111111.
CB00: 55 D4 ; 1111311.
CB02: 55 D4 ; 1111311.
CB04: 15 50 ; .11111..
CB06: 05 40 ; ..111...
CB08: 00 00 ; ........

ImageCherry:
```

```html
<canvas width="138" height="138"
  data-address="CB0A"
  data-command="0">
</canvas>
```

```code
; Object type 2
CB0A: 00 20 ; .....2..
CB0C: 00 80 ; ....2...
CB0E: 02 20 ; ...2.2..
CB10: 08 14 ; ..2..11.
CB12: 14 5D ; .11.1131
CB14: 5D 55 ; 11311111
CB16: 55 14 ; 1111.11.
CB18: 14 00 ; .11.....

ImageMagnet:
```

```html
<canvas width="138" height="138"
  data-address="CB1A"
  data-command="0">
</canvas>
```

```code
; Object type 3
CB1A: 0A A0 ; ..2222..
CB1C: 2A A8 ; .222222.
CB1E: A8 2A ; 222..222
CB20: A0 0A ; 22....22
CB22: A0 0A ; 22....22
CB24: A0 0A ; 22....22
CB26: 28 28 ; .22..22.
CB28: 28 28 ; .22..22.

ImageSkate: 
```

```html
<canvas width="275" height="140"
  data-address="CB2A"
  data-command="0,+x,1">
</canvas>
```

```code
; Object type 4
; 2 images
CB2A: FC 00 ; 333.....
CB2C: F7 00 ; 3313....
CB2E: FF 74 ; 3333131.
CB30: FF FF ; 33333333
CB32: 55 55 ; 11111111
CB34: 10 04 ; .1....1.
CB36: 54 15 ; 111..111
CB38: 10 04 ; .1....1.
;
CB3A: FC 00 ; 333.....
CB3C: F7 00 ; 3313....
CB3E: FF 74 ; 3333131.
CB40: FF FF ; 33333333
CB42: 55 55 ; 11111111
CB44: 44 11 ; 1.1..1.1
CB46: 10 04 ; .1....1.
CB48: 44 11 ; 1.1..1.1

ImageYoYo:
```

```html
<canvas width="680" height="140"
  data-address="CB4A"
  data-command="0,+x,1,+x,2,+x,3,+x,4">
</canvas>
```

```code
; Object type 5
; 5 images
CB4A: 00 10 ; .....1..
CB4C: 0A 90 ; ..2221..
CB4E: 2A A0 ; .22222..
CB50: AA A8 ; 2222222.
CB52: FF FC ; 3333333.
CB54: AA A8 ; 2222222.
CB56: 2A A0 ; .22222..
CB58: 0A 80 ; ..222...
;
CB5A: 00 10 ; .....1..
CB5C: 0A 90 ; ..2221..
CB5E: 2A B0 ; .22223..
CB60: AA E8 ; 2222322.
CB62: AB A8 ; 2223222.
CB64: AE A8 ; 2232222.
CB66: 3A A0 ; .32222..
CB68: 0A 80 ; ..222...
;
CB6A: 00 10 ; .....1..
CB6C: 0B 90 ; ..2321..
CB6E: 2B A0 ; .22322..
CB70: AB A8 ; 2223222.
CB72: AB A8 ; 2223222.
CB74: AB A8 ; 2223222.
CB76: 2B A0 ; .22322..
CB78: 0B 80 ; ..232...
;
CB7A: 00 10 ; .....1..
CB7C: 0A 90 ; ..2221..
CB7E: 3A A0 ; .32222..
CB80: AE A8 ; 2232222.
CB82: AB A8 ; 2223222.
CB84: AA E8 ; 2222322.
CB86: 2A B0 ; .22223..
CB88: 0A 80 ; ..222...
;
CB8A: 00 00 ; ........
CB8C: 0A 80 ; ..222...
CB8E: 2A A0 ; .22222..
CB90: AA A8 ; 2222222.
CB92: AA A8 ; 2222222.
CB94: AA A8 ; 2222222.
CB96: 2A A0 ; .22222..
CB98: 0A 80 ; ..222...

StringEraser:
CB9A: 00 30 ; .....3..
CB9C: 00 30 ; .....3..
CB9E: 00 30 ; .....3..
CBA0: 00 30 ; .....3..
CBA2: 00 30 ; .....3..
CBA4: 00 30 ; .....3..
CBA6: 00 30 ; .....3..
CBA8: 00 30 ; .....3..

ImageSkull:
```

```html
<canvas width="138" height="138"
  data-address="CBAA"
  data-command="0">
</canvas>
```

```code
; Object type 8
CBAA: 0F C0 ; ..333...
CBAC: 3F F0 ; .33333..
CBAE: 37 70 ; .31313..
CBB0: 3F F0 ; .33333..
CBB2: 0F C0 ; ..333...
CBB4: CF CC ; 3.333.3.
CBB6: 30 30 ; .3...3..
CBB8: C0 0C ; 3.....3.

ImagePear:
```

```html
<canvas width="138" height="138"
  data-address="CBBA"
  data-command="0">
</canvas>
```

```code
; Object type 6
CBBA: 00 10 ; .....1..
CBBC: 00 40 ; ....1...
CBBE: 00 C0 ; ....3...
CBC0: 03 C0 ; ...33...
CBC2: 0F F0 ; ..3333..
CBC4: 3F F0 ; .33333..
CBC6: 3F F0 ; .33333..
CBC8: 0F C0 ; ..333...

ImageSpider:
```

```html
<canvas width="275" height="140"
  data-address="CBCA"
  data-command="0,+x,1">
</canvas>
```

```code
; Object type 7
; 2 images
CBCA: 04 10 ; ..1..1..
CBCC: 44 11 ; 1.1..1.1
CBCE: 12 84 ; .1.22.1.
CBD0: 06 90 ; ..1221..
CBD2: 06 90 ; ..1221..
CBD4: 12 84 ; .1.22.1.
CBD6: 42 81 ; 1..22..1
CBD8: 40 01 ; 1......1
;
CBDA: 04 10 ; ..1..1..
CBDC: 04 10 ; ..1..1..
CBDE: 02 80 ; ...22...
CBE0: 56 95 ; 11122111
CBE2: 02 80 ; ...22...
CBE4: 16 94 ; .112211.
CBE6: 42 81 ; 1..22..1
CBE8: 00 00 ; ........

ImageX:
```

```html
<canvas width="275" height="140"
  data-address="CBEA"
  data-command="0,+x,1">
</canvas>
```

```code
; Object type 9
; 2 images
CBEA: 00 00 ; ........
CBEC: 00 00 ; ........
CBEE: 08 20 ; ..2..2..
CBF0: 02 80 ; ...22...
CBF2: 02 80 ; ...22...
CBF4: 08 20 ; ..2..2..
CBF6: 00 00 ; ........
CBF8: 00 00 ; ........
;
CBFA: 80 02 ; 2......2
CBFC: 20 08 ; .2....2.
CBFE: 08 20 ; ..2..2..
CC00: 02 80 ; ...22...
CC02: 02 80 ; ...22...
CC04: 08 20 ; ..2..2..
CC06: 20 08 ; .2....2.
CC08: 80 02 ; 2......2

LifeIndicator:
```

```html
<canvas width="275" height="140"
  data-address="CC0A"
  data-command="0,+x,1">
</canvas>
```

```code
; Inactive
CC0A: AA 80 ; 22222...
CC0C: 00 00 ; ........
CC0E: 00 00 ; ........
CC10: 00 00 ; ........
CC12: 00 00 ; ........
CC14: 00 00 ; ........
CC16: 00 00 ; ........
CC18: 00 00 ; ........
; Active
CC1A: 55 40 ; 11111...
CC1C: 00 00 ; ........
CC1E: 00 00 ; ........
CC20: 00 00 ; ........
CC22: 00 00 ; ........
CC24: 00 00 ; ........
CC26: 00 00 ; ........
CC28: 00 00 ; ........

CC2A: 02 ; 2 tiles
GenericEraser:
; 3333333333333333
; 3333333333333333
; 3333333333333333
; 3333333333333333
; 3333333333333333
; 3333333333333333
; 3333333333333333
; 3333333333333333
;
CC2B: FF FF ; 33333333
CC2D: FF FF ; 33333333
CC2F: FF FF ; 33333333
CC31: FF FF ; 33333333
CC33: FF FF ; 33333333
CC35: FF FF ; 33333333
CC37: FF FF ; 33333333
CC39: FF FF ; 33333333
;
CC3B: FF FF ; 33333333
CC3D: FF FF ; 33333333
CC3F: FF FF ; 33333333
CC41: FF FF ; 33333333
CC43: FF FF ; 33333333
CC45: FF FF ; 33333333
CC47: FF FF ; 33333333
CC49: FF FF ; 33333333
```

```html
<canvas width="380" height="140"
  data-address="CC4C"
  data-command="0,1,2">
</canvas>
```

```code
CC4B: 03 ; 3 tiles
StrPlayer:
; .....1..................
; .....1..................
; 111..1..11.......11..111
; 1..1.1...1.1..1.1111.1..
; 1..1.1.111.1..1.1....1..
; 111..1.111..111..11..1..
; 1.............1.........
; 1..........111..........
;
CC4C: 00 10 ; .....1..
CC4E: 00 10 ; .....1..
CC50: 54 10 ; 111..1..
CC52: 41 10 ; 1..1.1..
CC54: 41 11 ; 1..1.1.1
CC56: 54 11 ; 111..1.1
CC58: 40 00 ; 1.......
CC5A: 40 00 ; 1.......
;
CC5C: 00 00 ; ........
CC5E: 00 00 ; ........
CC60: 50 00 ; 11......
CC62: 11 04 ; .1.1..1.
CC64: 51 04 ; 11.1..1.
CC66: 50 54 ; 11..111.
CC68: 00 04 ; ......1.
CC6A: 01 50 ; ...111..
;
CC6C: 00 00 ; ........
CC6E: 00 00 ; ........
CC70: 14 15 ; .11..111
CC72: 55 10 ; 1111.1..
CC74: 40 10 ; 1....1..
CC76: 14 10 ; .11..1..
CC78: 00 00 ; ........
CC7A: 00 00 ; ........
```

```html
<canvas width="260" height="140"
  data-address="CC7D"
  data-command="0,1">
</canvas>
```

```code
CC7C: 02 ; 2 tiles
StrOne:
; ................
; ................
; ...11..111...11.
; ..1..1.1..1.1111
; ..1..1.1..1.1...
; ...11..1..1..11.
; ................
; ................
;
CC7D: 00 00 ; ........
CC7F: 00 00 ; ........
CC81: 01 41 ; ...11..1
CC83: 04 11 ; ..1..1.1
CC85: 04 11 ; ..1..1.1
CC87: 01 41 ; ...11..1
CC89: 00 00 ; ........
CC8B: 00 00 ; ........
;
CC8D: 00 00 ; ........
CC8F: 00 00 ; ........
CC91: 50 14 ; 11...11.
CC93: 04 55 ; ..1.1111
CC95: 04 40 ; ..1.1...
CC97: 04 14 ; ..1..11.
CC99: 00 00 ; ........
CC9B: 00 00 ; ........
```

```html
<canvas width="260" height="140"
  data-address="CC9E"
  data-command="0,1">
</canvas>
```

```code
CC9D: 02 ; 2 tiles
StrTwo:
; ................
; .1..............
; 111..1..1..11...
; .1...1..1.1..1..
; .1.1.1111.1..1..
; ..1..1111..11...
; ................
; ................
;
CC9E: 00 00 ; ........
CCA0: 10 00 ; .1......
CCA2: 54 10 ; 111..1..
CCA4: 10 10 ; .1...1..
CCA6: 11 15 ; .1.1.111
CCA8: 04 15 ; ..1..111
CCAA: 00 00 ; ........
CCAC: 00 00 ; ........
;
CCAE: 00 00 ; ........
CCB0: 00 00 ; ........
CCB2: 41 40 ; 1..11...
CCB4: 44 10 ; 1.1..1..
CCB6: 44 10 ; 1.1..1..
CCB8: 41 40 ; 1..11...
CCBA: 00 00 ; ........
CCBC: 00 00 ; ........
```

```html
<canvas width="620" height="140"
  data-address="CCBF"
  data-command="0,1,2,3,4">
</canvas>
```

```code
CCBE: 05 ; 5 tiles
StrGameOver:
; ..33333333333333333333333333333333333...
; .3333333333333333333333333333333333333..
; 332233322322223322333332233232332233222.
; 323323332322223222233323323232322223233.
; 323323222323323233333323323323323333233.
; 332223222323323322333332233323332233233.
; .3332333333333333333333333333333333333..
; .222333333333333333333333333333333333...
;
CCBF: 0F FF ; ..333333
CCC1: 3F FF ; .3333333
CCC3: FA FE ; 33223332
CCC5: EF BF ; 32332333
CCC7: EF BA ; 32332322
CCC9: FA BA ; 33222322
CCCB: 3F BF ; .3332333
CCCD: 2A FF ; .2223333
;
CCCF: FF FF ; 33333333
CCD1: FF FF ; 33333333
CCD3: BA AF ; 23222233
CCD5: BA AE ; 23222232
CCD7: BB EE ; 23233232
CCD9: BB EF ; 23233233
CCDB: FF FF ; 33333333
CCDD: FF FF ; 33333333
;
CCDF: FF FF ; 33333333
CCE1: FF FF ; 33333333
CCE3: AF FE ; 22333332
CCE5: AB FB ; 22233323
CCE7: FF FB ; 33333323
CCE9: AF FE ; 22333332
CCEB: FF FF ; 33333333
CCED: FF FF ; 33333333
;
CCEF: FF FF ; 33333333
CCF1: FF FF ; 33333333
CCF3: BE EF ; 23323233
CCF5: EE EE ; 32323232
CCF7: EF BE ; 32332332
CCF9: BF BF ; 23332333
CCFB: FF FF ; 33333333
CCFD: FF FF ; 33333333
;
CCFF: FF C0 ; 33333...
CD01: FF F0 ; 333333..
CD03: AF A8 ; 2233222.
CD05: AB BC ; 2223233.
CD07: FF BC ; 3333233.
CD09: AF BC ; 2233233.
CD0B: FF F0 ; 333333..
CD0D: FF C0 ; 33333...
```

```html
<canvas width="740" height="140"
  data-address="CD10"
  data-command="0,1,2,3,4,5">
</canvas>
```

```code
CD0F: 06 ; Six tiles
Str1or2Players:
;. 3...........33.........1.......................
; 33..111.11..3..3...111..1.......................
; .3..1.1.1.....3....1..1.1..11.1..1..11..111..11.
; .3..1.1.1....3.....1..1.1...1.1..1.1111.1...1...
; .3..111.1...3......1..1.1.111.1..1.1....1....11.
; 333.........3333...111..1.111..111..11..1...11..
; ...................1.............1..............
; ...................1...........111..............   
;
CD10: 30 00 ; .3......
CD12: F0 54 ; 33..111.
CD14: 30 44 ; .3..1.1.
CD16: 30 44 ; .3..1.1.
CD18: 30 54 ; .3..111.
CD1A: FC 00 ; 333.....
CD1C: 00 00 ; ........
CD1E: 00 00 ; ........
;
CD20: 00 3C ; .....33.
CD22: 50 C3 ; 11..3..3
CD24: 40 0C ; 1.....3.
CD26: 40 30 ; 1....3..
CD28: 40 C0 ; 1...3...
CD2A: 00 FF ; ....3333
CD2C: 00 00 ; ........
CD2E: 00 00 ; ........
;
CD30: 00 00 ; ........
CD32: 01 50 ; ...111..
CD34: 01 04 ; ...1..1.
CD36: 01 04 ; ...1..1.
CD38: 01 04 ; ...1..1.
CD3A: 01 50 ; ...111..
CD3C: 01 00 ; ...1....
CD3E: 01 00 ; ...1....
;
CD40: 40 00 ; 1.......
CD42: 40 00 ; 1.......
CD44: 41 44 ; 1..11.1.
CD46: 40 44 ; 1...1.1.
CD48: 45 44 ; 1.111.1.
CD4A: 45 41 ; 1.111..1
CD4C: 00 00 ; ........
CD4E: 00 01 ; .......1
;
CD50: 00 00 ; ........
CD52: 00 00 ; ........
CD54: 10 50 ; .1..11..
CD56: 11 54 ; .1.1111.
CD58: 11 00 ; .1.1....
CD5A: 50 50 ; 11..11..
CD5C: 10 00 ; .1......
CD5E: 50 00 ; 11......
;
CD60: 00 00 ; ........
CD62: 00 00 ; ........
CD64: 54 14 ; 111..11.
CD66: 40 40 ; 1...1...
CD68: 40 14 ; 1....11.
CD6A: 40 50 ; 1...11..
CD6C: 00 00 ; ........
CD6E: 00 00 ; ........
```

```html
<canvas width="1217" height="380"
  data-address="CD71"
  data-command=":10x3:,0,,,,,,,,,@CD82,0,1,2,3,4,5,6,7,8,9,@CE23,0,1,2,3,4,5,6,7,8,9">
</canvas>
```

```code

; Copyright message in 3 lines of tiles
;         ........
;         ........
;         ........
;         ........
;         ........
;         ........
;         .2222...
;         2....2..
; .......2..22..2..2..22...22...22................................................
; .......2.2....2.22.2..2.2..2.2..2......22...2..2...222...2...222..2..22.........
; .......2.2....2..2..222..22....2.......2.2.2.2.2...2.....2...2...2.2.2.2........
; .......2..22..2..2....2.2..2..2........2.2.222.2...22....2...22..222.22.........
; ........2....2..222.22...22..2222......22..2.2.222.222...222.222.2.2.2.2........
; .........2222...................................................................
; ........................................22222.22..2..2.222..2.2.................
; 2...2..22.222.2..2..22.222.22...222..2....2..2..2.22.2.2..2.2.2...22..2..22..22.
; 2...2.2...2...22.2.2...2...2.2...2..2.2...2..2..2.22.2.2..2.222..2...2.2.2.2.2.2
; 2...2.2...22..2.22..22.22..2.2...2..2.2...2..2222.2.22.2..2..2...2...2.2.22..22.
; 222.2..22.222.2..2.22..222.22....2...2....2..2..2.2.22.222...2....22..2..2.2.2..
; ................................................................................
; .......2..2...2.....22..2..22.2.2.222..22...22..222..22.222.22..2.2.222.22......
; ......2.2.2...2.....2.2.2.2...2.2..2..2.....2.2.2...2...2...2.2.2.2.2...2.2.....
; ......222.2...2.....22..2.2.2.222..2...22...22..22...22.22..22..2.2.22..2.2.....
; ......2.2.222.222...2.2.2..22.2.2..2..22....2.2.222.22..222.2.2..2..222.22......

CD70: 01 ; 1 tile
StrCopyright1: 
CD71: 00 00 ; ........
CD73: 00 00 ; ........
CD75: 00 00 ; ........
CD77: 00 00 ; ........
CD79: 00 00 ; ........
CD7B: 00 00 ; ........
CD7D: 2A 80 ; .2222...
CD7F: 80 20 ; 2....2..

CD81: 0A ; 10 tiles
StrCopyright2: 
; .......2..22..2..2..22...22...22................................................
; .......2.2....2.22.2..2.2..2.2..2......22...2..2...222...2...222..2..22.........
; .......2.2....2..2..222..22....2.......2.2.2.2.2...2.....2...2...2.2.2.2........
; .......2..22..2..2....2.2..2..2........2.2.222.2...22....2...22..222.22.........
; ........2....2..222.22...22..2222......22..2.2.222.222...222.222.2.2.2.2........
; .........2222...................................................................
; ........................................22222.22..2..2.222..2.2.................
; 2...2..22.222.2..2..22.222.22...222..2....2..2..2.22.2.2..2.2.2...22..2..22..22.
;
CD82: 00 02 ; .......2
CD84: 00 02 ; .......2
CD86: 00 02 ; .......2
CD88: 00 02 ; .......2
CD8A: 00 00 ; ........
CD8C: 00 00 ; ........
CD8E: 00 00 ; ........
CD90: 80 82 ; 2...2..2
;
CD92: 0A 08 ; ..22..2.
CD94: 20 08 ; .2....2.
CD96: 20 08 ; .2....2.
CD98: 0A 08 ; ..22..2.
CD9A: 80 20 ; 2....2..
CD9C: 2A 80 ; .2222...
CD9E: 00 00 ; ........
CDA0: 8A 88 ; 2.222.2.
;
CDA2: 20 A0 ; .2..22..
CDA4: A2 08 ; 22.2..2.
CDA6: 20 A8 ; .2..222.
CDA8: 20 08 ; .2....2.
CDAA: A8 A0 ; 222.22..
CDAC: 00 00 ; ........
CDAE: 00 00 ; ........
CDB0: 20 A2 ; .2..22.2
;
CDB2: 28 0A ; .22...22
CDB4: 82 20 ; 2..2.2..
CDB6: 28 02 ; .22....2
CDB8: 82 08 ; 2..2..2.
CDBA: 28 2A ; .22..222
CDBC: 00 00 ; ........
CDBE: 00 00 ; ........
CDC0: A2 80 ; 22.22...
;
CDC2: 00 00 ; ........
CDC4: 80 02 ; 2......2
CDC6: 00 02 ; .......2
CDC8: 00 02 ; .......2
CDCA: 80 02 ; 2......2
CDCC: 00 00 ; ........
CDCE: 00 00 ; ........
CDD0: A8 20 ; 222..2..
;
CDD2: 00 00 ; ........
CDD4: 80 82 ; 2...2..2
CDD6: 22 22 ; .2.2.2.2
CDD8: 22 A2 ; .2.222.2
CDDA: 82 22 ; 2..2.2.2
CDDC: 00 00 ; ........
CDDE: AA 8A ; 22222.22
CDE0: 08 20 ; ..2..2..
;
CDE2: 00 00 ; ........
CDE4: 02 A0 ; ...222..
CDE6: 02 00 ; ...2....
CDE8: 02 80 ; ...22...
CDEA: A2 A0 ; 22.222..
CDEC: 00 00 ; ........
CDEE: 08 22 ; ..2..2.2
CDF0: 8A 22 ; 2.22.2.2
;
CDF2: 00 00 ; ........
CDF4: 20 2A ; .2...222
CDF6: 20 20 ; .2...2..
CDF8: 20 28 ; .2...22.
CDFA: 2A 2A ; .222.222
CDFC: 00 00 ; ........
CDFE: A0 88 ; 22..2.2.
CE00: 08 88 ; ..2.2.2.
;
CE02: 00 00 ; ........
CE04: 08 28 ; ..2..22.
CE06: 22 22 ; .2.2.2.2
CE08: 2A 28 ; .222.22.
CE0A: 22 22 ; .2.2.2.2
CE0C: 00 00 ; ........
CE0E: 00 00 ; ........
CE10: 0A 08 ; ..22..2.
;
CE12: 00 00 ; ........
CE14: 00 00 ; ........
CE16: 00 00 ; ........
CE18: 00 00 ; ........
CE1A: 00 00 ; ........
CE1C: 00 00 ; ........
CE1E: 00 00 ; ........
CE20: 28 28 ; .22..22.

CE22: 0A
StrCopyright3:
; 2...2.2...2...22.2.2...2...2.2...2..2.2...2..2..2.22.2.2..2.222..2...2.2.2.2.2.2
; 2...2.2...22..2.22..22.22..2.2...2..2.2...2..2222.2.22.2..2..2...2...2.2.22..22.
; 222.2..22.222.2..2.22..222.22....2...2....2..2..2.2.22.222...2....22..2..2.2.2..
; ................................................................................
; .......2..2...2.....22..2..22.2.2.222..22...22..222..22.222.22..2.2.222.22......
; ......2.2.2...2.....2.2.2.2...2.2..2..2.....2.2.2...2...2...2.2.2.2.2...2.2.....
; ......222.2...2.....22..2.2.2.222..2...22...22..22...22.22..22..2.2.22..2.2.....
; ......2.2.222.222...2.2.2..22.2.2..2..22....2.2.222.22..222.2.2..2..222.22......
;
CE23: 80 88 ; 2...2.2.
CE25: 80 88 ; 2...2.2.
CE27: A8 82 ; 222.2..2
CE29: 00 00 ; ........
CE2B: 00 02 ; .......2
CE2D: 00 08 ; ......2.
CE2F: 00 0A ; ......22
CE31: 00 08 ; ......2.
;
CE33: 08 0A ; ..2...22
CE35: 0A 08 ; ..22..2.
CE37: 8A 88 ; 2.222.2.
CE39: 00 00 ; ........
CE3B: 08 08 ; ..2...2.
CE3D: 88 08 ; 2.2...2.
CE3F: 88 08 ; 2.2...2.
CE41: 8A 8A ; 2.222.22
;
CE43: 22 02 ; .2.2...2
CE45: A0 A2 ; 22..22.2
CE47: 22 82 ; .2.22..2
CE49: 00 00 ; ........
CE4B: 00 A0 ; ....22..
CE4D: 00 88 ; ....2.2.
CE4F: 00 A0 ; ....22..
CE51: 80 88 ; 2...2.2.
;
CE53: 02 20 ; ...2.2..
CE55: 82 20 ; 2..2.2..
CE57: A2 80 ; 22.22...
CE59: 00 00 ; ........
CE5B: 82 88 ; 2..22.2.
CE5D: 88 08 ; 2.2...2.
CE5F: 88 8A ; 2.2.2.22
CE61: 82 88 ; 2..22.2.
;
CE63: 20 88 ; .2..2.2.
CE65: 20 88 ; .2..2.2.
CE67: 20 20 ; .2...2..
CE69: 00 00 ; ........
CE6B: 8A 82 ; 2.222..2
CE6D: 82 08 ; 2..2..2.
CE6F: 82 02 ; 2..2...2
CE71: 82 0A ; 2..2..22
;
CE73: 08 20 ; ..2..2..
CE75: 08 2A ; ..2..222
CE77: 08 20 ; ..2..2..
CE79: 00 00 ; ........
CE7B: 80 A0 ; 2...22..
CE7D: 00 88 ; ....2.2.
CE7F: 80 A0 ; 2...22..
CE81: 00 88 ; ....2.2.
;
CE83: 8A 22 ; 2.22.2.2
CE85: 88 A2 ; 2.2.22.2
CE87: 88 A2 ; 2.2.22.2
CE89: 00 00 ; ........
CE8B: A8 28 ; 222..22.
CE8D: 80 80 ; 2...2...
CE8F: A0 28 ; 22...22.
CE91: A8 A0 ; 222.22..
;
CE93: 08 A8 ; ..2.222.
CE95: 08 20 ; ..2..2..
CE97: A0 20 ; 22...2..
CE99: 00 00 ; ........
CE9B: A8 A0 ; 222.22..
CE9D: 80 88 ; 2...2.2.
CE9F: A0 A0 ; 22..22..
CEA1: A8 88 ; 222.2.2.
;
CEA3: 20 22 ; .2...2.2
CEA5: 20 22 ; .2...2.2
CEA7: 0A 08 ; ..22..2.
CEA9: 00 00 ; ........
CEAB: 88 A8 ; 2.2.222.
CEAD: 88 80 ; 2.2.2...
CEAF: 88 A0 ; 2.2.22..
CEB1: 20 A8 ; .2..222.
;
CEB3: 22 22 ; .2.2.2.2
CEB5: 28 28 ; .22..22.
CEB7: 22 20 ; .2.2.2..
CEB9: 00 00 ; ........
CEBB: A0 00 ; 22......
CEBD: 88 00 ; 2.2.....
CEBF: 88 00 ; 2.2.....
CEC1: A0 00 ; 22......
```

```html
<canvas id="cursiveArea" width="640" height="304" style="border: 1px solid black">
</canvas><br>
<button class="btn btn-primary" style="margin-top:8px" onclick="Doubleback.slowCursive()">Slow</button>
<button class="btn btn-primary" style="margin-top:8px" onclick="Doubleback.stepCursive()">Step</button>
```

```code
; Cursive "doubleback" data. Each 2 bytes holds 5 directional data points.
; The upper bit is unused.
CEC3: 6D B6   ; 0 110 110 110 110 110    W  W  W  W  W
CEC5: 27 6D   ; 0 010 011 101 101 101   SW SW SW SE  E
CEC7: 12 52   ; 0 001 001 001 010 010    E  E NE NE NE
CEC9: 12 49   ; 0 001 001 001 001 001   NE NE NE NE NE
CECB: 5A 49   ; 0 101 101 001 001 001   NE NE NE SW SW
CECD: 5B 6D   ; 0 101 101 101 101 101   SW SW SW SW SW
CECF: 29 25   ; 0 010 100 100 100 101   SW  S  S  S  E
CED1: 12 4A   ; 0 001 001 001 001 010    E NE NE NE NE
CED3: 5D 92   ; 0 101 110 110 010 010    E  E  W  W SW
CED5: 24 E5   ; 0 010 010 011 100 101   SW  S SE  E  E
CED7: 30 09   ; 0 011 000 000 001 001   NE NE  N  N SE
CED9: 52 53   ; 0 101 001 001 010 011   SE  E NE NE SW
CEDB: 24 E5   ; 0 010 010 011 100 101   SW  S SE  E  E
CEDD: 52 49   ; 0 101 001 001 001 001   NE NE NE NE SW
CEDF: 24 ED   ; 0 010 010 011 101 101   SW SW SE  E  E
CEE1: 12 52   ; 0 001 001 001 010 010    E  E NE NE NE
CEE3: 10 49   ; 0 001 000 001 001 001   NE NE NE  N NE
CEE5: 5C 00   ; 0 101 110 000 000 000    N  N  N  W SW
CEE7: 4B 2D   ; 0 100 101 100 101 101   SW SW  S SW  S
CEE9: 39 25   ; 0 011 100 100 100 101   SW  S  S  S SE
CEEB: 70 52   ; 0 111 000 001 010 010    E  E NE  N NW
CEED: 24 93   ; 0 010 010 010 010 011   SE  E  E  E  E
CEEF: 02 49   ; 0 000 001 001 001 001   NE NE NE NE  N
CEF1: 60 01   ; 0 110 000 000 000 001   NE  N  N  N  W
CEF3: 59 6D   ; 0 101 100 101 101 101   SW SW SW  S SW
CEF5: 49 2C   ; 0 100 100 100 101 100    S SW  S  S  S
CEF7: 24 93   ; 0 010 010 010 010 011   SE  E  E  E  E
CEF9: 02 4A   ; 0 000 001 001 001 010    E NE NE NE  N
CEFB: 49 76   ; 0 100 100 101 110 110    W  W SW  S  S
CEFD: 24 93   ; 0 010 010 010 010 011   SE  E  E  E  E
CEFF: 12 92   ; 0 001 001 010 010 010    E  E  E NE NE
CF01: 02 49   ; 0 000 001 001 001 001   NE NE NE NE  N
CF03: 60 01   ; 0 110 000 000 000 001   NE  N  N  N  W
CF05: 59 6D   ; 0 101 100 101 101 101   SW SW SW  S SW
CF07: 49 2C   ; 0 100 100 100 101 100    S SW  S  S  S
CF09: 02 93   ; 0 000 001 010 010 011   SE  E  E NE  N
CF0B: 14 9F   ; 0 001 010 010 011 111   NW SE  E  E NE
CF0D: 64 8A   ; 0 110 010 010 001 010    E NE  E  E  W
CF0F: 39 6E   ; 0 011 100 101 101 110    W SW SW  S SE
CF11: 40 4A   ; 0 100 000 001 001 010    E NE NE  N  S
CF13: 14 9D   ; 0 001 010 010 011 101   SW SE  E  E NE
CF15: 24 49   ; 0 010 010 001 001 001   NE NE NE  E  E
CF17: 6D DA   ; 0 110 110 111 011 010    E SE NW  W  W
CF19: 39 2E   ; 0 011 100 100 101 110    W SW  S  S SE
CF1B: 24 92   ; 0 010 010 010 010 010    E  E  E  E  E
CF1D: 12 49   ; 0 001 001 001 001 001   NE NE NE NE NE
CF1F: 00 41   ; 0 000 000 001 000 001   NE  N NE  N  N
CF21: 5B 70   ; 0 101 101 101 110 000    N  W SW SW SW
CF23: 4B 2C   ; 0 100 101 100 101 100    S SW  S SW  S
CF25: 24 4C   ; 0 010 010 001 001 100    S NE NE  E  E
CF27: 37 AB   ; 0 011 011 110 101 011   SE SW  W SE SE
CF29: 12 52   ; 0 001 001 001 010 010    E  E NE NE NE
CF2B: 00 00   ; END       

DirTable:
; These are X/Y offsets for each 8 directions
CF2D: 00 FF  ; 0 N
CF2F: 01 FF  ; 1 NE
CF31: 01 00  ; 2 E
CF33: 01 01  ; 3 SE
CF35: 00 01  ; 4 S
CF37: FF 01  ; 5 SW
CF39: FF 00  ; 6 W
CF3B: FF FF  ; 7 NW

MusicFirstLife:
CF3D: 28 80                
CF3F: 40 40                              
CF41: 28 80          
CF43: 40 40                                  
CF45: 28 80          
CF47: 40 40                               
CF49: 28 80          
CF4B: 40 40                                   
CF4D: 19 5F                                 
CF4F: 19 64 
CF51: 19 5F                                  
CF53: 1A 55                        
CF55: 1C 4B                        
CF57: 1C 55                         
CF59: 1C 4B                        
CF5B: 1C 43                       
CF5D: 40 40                                 
CF5F: 00 00          

MusicSecondLife:
CF61: 28 80 
CF63: 40 40   
CF65: 40 43
CF67: 40 40
CF69: 37 5F
CF6B: 37 4B
CF6D: 37 55
CF6F: 37 4B
CF71: 19 5F
CF73: 19 64
CF75: 19 5F
CF77: 1A 55
CF79: 1C 4B
CF7B: 1C 55
CF7D: 1C 4B
CF7F: 1C 43
CF81: 40 40
CF83: 00 00

MusicThirdLife:
CF85: 28 80
CF87: 40 40
CF89: 40 43
CF8B: 3C 4B
CF8D: 39 55
CF8F: 37 5F
CF91: 37 64
CF93: 37 5F
CF95: 39 55
CF97: 3C 4B
CF99: 40 43
CF9B: 39 55
CF9D: 40 40
CF9F: 00 00

CFA1: 14 1E
CFA3: 00 00 

MusicEndOfLife:
; Just one long note
CFA5: FF FF 
CFA7: 00 00              

ScoreTable:
; A zero is added to the end of all scores
CFA9: 00     ; End marker
CFAA: 07     ; Type 1: Apple     70
CFAB: 0A     ; Type 2: Cherry   100
CFAC: 0F     ; Type 3: Magnet   150
CFAD: 14     ; Type 4: Skate    200
CFAE: 19     ; Type 5: YoYo     250
CFAF: 1E     ; Type 6: Pear     300
CFB0: 32     ; Type 7: Spider   500
CFB1: 00     ; Type 8: Skull   (no score)
CFB2: 64     ; Type 9: X       1000       

; "COPYRIGHT 1982 DALE A. LEAR ALL RIGHTS RESERVED LICENSED TO TANDY COPRPORATION"
CFB3: 43 4F 50 59 52 49 47 48 54 20 31 39 38 32 20 44 41 4C 45 20 41 2E 20 4C 45 41 52 20 41 4C 4C 20 
CFD3: 52 49 47 48 54 53 20 52 45 53 45 52 56 45 44 20 4C 49 43 45 4E 53 45 44 20 54 4F 20 54 41 4E 44 
CFF3: 59 20 43 4F 52 50 4F 52 41 54 49 4F 4E
```

```html
<script src="/js/Binary.js"></script>
<script src="doubleback.js"></script>
<script src="/js/TileEngine.js"></script>
<script src="/js/Canvas.js"></script>
<script>
    window.onload = function() {   
        Doubleback.data = Binary.readBinary('Code.md.bin')     
        Doubleback.origin = 0xC000
        Doubleback.loadCursiveData()
        Doubleback.origin = 0xC000
        Canvas.redrawGraphics()       
    }    
</script>
```

