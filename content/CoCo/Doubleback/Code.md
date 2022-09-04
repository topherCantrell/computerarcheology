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
C037: CC 1C 46        LDD     #$1C46              
C03A: 33 8D 0D 33     LEAU    $CD71,PC            ; {code.StrCopyright1}
C03E: 17 09 02        LBSR    $C943               ; {code.PrintChars}
C041: CC 14 4E        LDD     #$144E              
C044: 33 8D 0D 3A     LEAU    $CD82,PC            ; {code.StrCopyright2}
C048: 17 08 F8        LBSR    $C943               ; {code.PrintChars}
C04B: CC 14 56        LDD     #$1456              
C04E: 33 8D 0D D1     LEAU    $CE23,PC            ; {code.StrCopyright3}
C052: 17 08 EE        LBSR    $C943               ; {code.PrintChars}
C055: 8E 00 E4        LDX     #$00E4              
C058: 86 1F           LDA     #$1F                
C05A: A7 84           STA     ,X                  
C05C: 86 18           LDA     #$18                
C05E: A7 02           STA     2,X                 
C060: 33 8D 0E 5F     LEAU    $CEC3,PC            ; {}
C064: 34 04           PSHS    B                   
C066: C6 05           LDB     #$05                
C068: E7 E4           STB     ,S                  
C06A: EC C1           LDD     ,U++                
C06C: 27 42           BEQ     $C0B0               ; {}
C06E: 34 06           PSHS    B,A                 
C070: C4 07           ANDB    #$07                
C072: 58              ASLB                        
C073: 31 8D 0E B6     LEAY    $CF2D,PC            ; {}
C077: EC A5           LDD     B,Y                 
C079: AB 84           ADDA    ,X                  
C07B: EB 02           ADDB    2,X                 
C07D: A7 84           STA     ,X                  
C07F: E7 02           STB     2,X                 
C081: 40              NEGA                        
C082: 8B 80           ADDA    #$80                
C084: A7 01           STA     1,X                 
C086: 50              NEGB                        
C087: CB 3C           ADDB    #$3C                
C089: E7 03           STB     3,X                 
C08B: 34 50           PSHS    U,X                 
C08D: 17 08 CF        LBSR    $C95F               ; {}
C090: 30 01           LEAX    1,X                 
C092: 17 08 CA        LBSR    $C95F               ; {}
C095: E6 84           LDB     ,X                  
C097: C4 01           ANDB    #$01                
C099: 26 03           BNE     $C09E               ; {}
C09B: 17 0A 51        LBSR    $CAEF               ; {code.WaitVBlank}
C09E: 35 50           PULS    X,U                 
C0A0: 35 06           PULS    A,B                 
C0A2: 6A E4           DEC     ,S                  
C0A4: 27 C0           BEQ     $C066               ; {}
C0A6: 44              LSRA                        
C0A7: 56              RORB                        
C0A8: 44              LSRA                        
C0A9: 56              RORB                        
C0AA: 44              LSRA                        
C0AB: 56              RORB                        
C0AC: 34 06           PSHS    B,A                 
C0AE: 20 C0           BRA     $C070               ; {}

C0B0: 35 04           PULS    B                   

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
C110: DC BB           LDD     $BB                 ; {ram.HighScore}
C112: CE 04 EE        LDU     #$04EE              
C115: 17 05 13        LBSR    $C62B               ; {code.DrawNumber}
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
C134: 0F BE           CLR     $BE                 ; {ram.BE}
C136: 0F D1           CLR     $D1                 ; {ram.D1}
C138: 0F CE           CLR     $CE                 ; {ram.CE}
C13A: 0F D0           CLR     $D0                 ; {ram.D0}
C13C: 0F C7           CLR     $C7                 ; {ram.C7}
C13E: 0F D6           CLR     $D6                 ; {ram.D6}
C140: 0F CF           CLR     $CF                 ; {ram.CF}
C142: C6 28           LDB     #$28                
C144: D7 D5           STB     $D5                 ; {ram.D5}
C146: CC 2C 28        LDD     #$2C28              
C149: 33 8D 0A FF     LEAU    $CC4C,PC            ; {code.StrPlayer}
C14D: 17 07 F3        LBSR    $C943               ; {code.PrintChars}
C150: CC 44 28        LDD     #$4428              
C153: 33 8D 0B 26     LEAU    $CC7D,PC            ; {code.StrOne}
C157: 0D B6           TST     $B6                 ; {ram.Player} Player 0 or 1?
C159: 27 06           BEQ     $C161               ; {} Player 0 ???
C15B: 86 46           LDA     #$46                
C15D: 33 8D 0B 3D     LEAU    $CC9E,PC            ; {code.StrTwo}
C161: 17 07 DF        LBSR    $C943               ; {code.PrintChars}
C164: D6 B5           LDB     $B5                 ; {ram.NumLives}
C166: 33 8D 0E 1B     LEAU    $CF85,PC            ; {}
C16A: 5A              DECB                        
C16B: 27 0B           BEQ     $C178               ; {}
C16D: 33 8D 0D F0     LEAU    $CF61,PC            ; {}
C171: 5A              DECB                        
C172: 27 04           BEQ     $C178               ; {}
C174: 33 8D 0D C5     LEAU    $CF3D,PC            ; {}
C178: 17 09 03        LBSR    $CA7E               ; {}
C17B: 17 08 E5        LBSR    $CA63               ; {code.DrawPlayfiled}
C17E: C6 02           LDB     #$02                
C180: 34 04           PSHS    B                   
C182: 8E 00 E4        LDX     #$00E4              
C185: C1 56           CMPB    #$56                
C187: 2E 12           BGT     $C19B               ; {}
C189: E7 02           STB     2,X                 
C18B: C6 02           LDB     #$02                
C18D: E7 84           STB     ,X                  
C18F: 17 07 CD        LBSR    $C95F               ; {}
C192: C6 7E           LDB     #$7E                
C194: E7 84           STB     ,X                  
C196: 17 07 C6        LBSR    $C95F               ; {}
C199: E6 02           LDB     2,X                 
C19B: E7 84           STB     ,X                  
C19D: C6 02           LDB     #$02                
C19F: E7 02           STB     2,X                 
C1A1: 17 07 BB        LBSR    $C95F               ; {}
C1A4: C6 56           LDB     #$56                
C1A6: E7 02           STB     2,X                 
C1A8: 17 07 B4        LBSR    $C95F               ; {}
C1AB: 6C E4           INC     ,S                  
C1AD: E6 E4           LDB     ,S                  
C1AF: C1 7E           CMPB    #$7E                
C1B1: 23 CF           BLS     $C182               ; {}
C1B3: 35 04           PULS    B                   
C1B5: 4F              CLRA                        
C1B6: C6 58           LDB     #$58                
C1B8: 33 8D 0A 90     LEAU    $CC4C,PC            ; {code.StrPlayer}
C1BC: 17 07 84        LBSR    $C943               ; {code.PrintChars}
C1BF: CC 18 58        LDD     #$1858              
C1C2: 33 8D 0A B7     LEAU    $CC7D,PC            ; {code.StrOne}
C1C6: 17 07 7A        LBSR    $C943               ; {code.PrintChars}
C1C9: 0D B4           TST     $B4                 ; {ram.NumPlayers}
C1CB: 27 0A           BEQ     $C1D7               ; {}
C1CD: CC 52 58        LDD     #$5258              
C1D0: 33 8D 0A CA     LEAU    $CC9E,PC            ; {code.StrTwo}
C1D4: 17 07 6C        LBSR    $C943               ; {code.PrintChars}
C1D7: 17 04 36        LBSR    $C610               ; {}

C1DA: 8E 00 E4        LDX     #$00E4              
C1DD: 6F 02           CLR     2,X                 
C1DF: C6 33           LDB     #$33                ; 1st slot X ...
C1E1: E7 84           STB     ,X                  ; ... coordinate
;
; First slot (active if 3 lives)
C1E3: 33 8D 0A 33     LEAU    $CC1A,PC            ; {} Life inidcator ACTIVE
C1E7: D6 B5           LDB     $B5                 ; {ram.NumLives} Number of lives
C1E9: C1 03           CMPB    #$03                ; All 3?
C1EB: 27 04           BEQ     $C1F1               ; {} Yes ... 1st bar is CURRENT
C1ED: 33 8D 0A 19     LEAU    $CC0A,PC            ; {code.LifeIndicator} Life indicator INACTIVE
C1F1: 17 05 69        LBSR    $C75D               ; {code.Draw16x8} Draw the indicator
C1F4: C6 3D           LDB     #$3D                ; 2nd slot X ...
C1F6: E7 84           STB     ,X                  ; ... cooridinate
;
; Second slot (active if 2 lives)
C1F8: 33 8D 0A 1E     LEAU    $CC1A,PC            ; {} Life inidcator ACTIVE
C1FC: D6 B5           LDB     $B5                 ; {ram.NumLives} Number of lives
C1FE: C1 02           CMPB    #$02                ; 2 remaining?
C200: 27 04           BEQ     $C206               ; {} Yes ... 2nd bar is CURRENT
C202: 33 8D 0A 04     LEAU    $CC0A,PC            ; {code.LifeIndicator} Life indicator INACTIVE
C206: 17 05 54        LBSR    $C75D               ; {code.Draw16x8} Draw the indicator
C209: C6 47           LDB     #$47                ; 3rd slot X ...
C20B: E7 84           STB     ,X                  ; ... coordinate
;
; Third slot (active if 1 life)
C20D: 33 8D 0A 09     LEAU    $CC1A,PC            ; {} Life inidcator ACTIVE
C211: D6 B5           LDB     $B5                 ; {ram.NumLives} Number of lives
C213: C1 01           CMPB    #$01                ; 1 remaining?
C215: 27 04           BEQ     $C21B               ; {} Yes ... 3rd bar is CURRENT
C217: 33 8D 09 EF     LEAU    $CC0A,PC            ; {code.LifeIndicator} Life indicator INACTIVE
C21B: 17 05 3F        LBSR    $C75D               ; {code.Draw16x8} Draw the indicator
; 
C21E: 8E 00 D8        LDX     #$00D8              
C221: 86 40           LDA     #$40                
C223: A7 84           STA     ,X                  
C225: A7 02           STA     2,X                 
C227: 8E 02 00        LDX     #$0200              
C22A: 5F              CLRB                        
C22B: A7 80           STA     ,X+                 
C22D: 5A              DECB                        
C22E: 26 FB           BNE     $C22B               ; {}
C230: 8E 01 60        LDX     #$0160              
C233: C6 A0           LDB     #$A0                
C235: 6F 80           CLR     ,X+                 
C237: 5A              DECB                        
C238: 26 FB           BNE     $C235               ; {}
C23A: 0F BD           CLR     $BD                 ; {ram.BD}
C23C: 17 00 16        LBSR    $C255               ; {}
C23F: 0D BD           TST     $BD                 ; {ram.BD}
C241: 27 F9           BEQ     $C23C               ; {}
C243: C6 F0           LDB     #$F0                ; Dull screen ...
C245: F7 FF 22        STB     $FF22               ; {hard.PIA1_DB} ... color mode
C248: 33 8D 0D 59     LEAU    $CFA5,PC            ; {}
C24C: 17 08 2F        LBSR    $CA7E               ; {}
C24F: C6 F8           LDB     #$F8                ; Bright screen ...
C251: F7 FF 22        STB     $FF22               ; {hard.PIA1_DB} ... color mode
C254: 39              RTS                         ; Done

C255: 17 08 68        LBSR    $CAC0               ; {code.CheckForBreak} Check for BREAK (reset if so)
C258: 8E 02 00        LDX     #$0200              
C25B: D6 BE           LDB     $BE                 ; {ram.BE} ?? Player number? Unlikely
C25D: 3A              ABX                         
C25E: EC 84           LDD     ,X                  
C260: 8E 00 DE        LDX     #$00DE              
C263: A7 84           STA     ,X                  
C265: E7 02           STB     2,X                 
C267: 17 07 48        LBSR    $C9B2               ; {code.GetScreenAndShift}
C26A: 17 07 29        LBSR    $C996               ; {}
C26D: 0C D4           INC     $D4                 ; {ram.D4} ?? odd/even page numbers for double buffering?

C26F: 8E 01 60        LDX     #$0160              ; List of objects

ObjectLoop:
C272: 6D 06           TST     6,X                 ; Object type 0?
C274: 10 27 01 17     LBEQ    $C38F               ; {} Yes ... done with list
C278: 30 08           LEAX    8,X                 
C27A: 1F 10           TFR     X,D                 
C27C: 54              LSRB                        
C27D: 54              LSRB                        ; Maybe a delay?
C27E: 54              LSRB                        
C27F: DB D4           ADDB    $D4                 ; {ram.D4}
C281: C4 07           ANDB    #$07                
C283: 26 ED           BNE     $C272               ; {code.ObjectLoop} Skip this object
C285: 30 18           LEAX    -8,X                ; Back up to start of this object
C287: E6 06           LDB     6,X                 ; Object type
C289: 5A              DECB                        ; 1=APPLE?
C28A: 26 0A           BNE     $C296               ; {} No ... check other types
C28C: 33 8D 08 6A     LEAU    $CAFA,PC            ; {code.ImageApple} Apple graphic
C290: 17 04 CA        LBSR    $C75D               ; {code.Draw16x8} Draw apple
C293: 16 00 F0        LBRA    $C386               ; {code.NextObject} Next object
;
C296: 5A              DECB                        ; 2=CHERRY
C297: 26 0A           BNE     $C2A3               ; {} No ... check other types
C299: 33 8D 08 6D     LEAU    $CB0A,PC            ; {code.ImageCherry} Cherry graphic
C29D: 17 04 BD        LBSR    $C75D               ; {code.Draw16x8} Draw cherry
C2A0: 16 00 E3        LBRA    $C386               ; {code.NextObject} Next object
;
C2A3: 5A              DECB                        ; 3=MAGNET
C2A4: 26 17           BNE     $C2BD               ; {} No ... check other types
C2A6: 33 8D 08 70     LEAU    $CB1A,PC            ; {code.ImageMagnet}
C2AA: 17 05 AE        LBSR    $C85B               ; {}
C2AD: CC 10 10        LDD     #$1010              
C2B0: 17 07 4C        LBSR    $C9FF               ; {}
C2B3: 33 8D 08 63     LEAU    $CB1A,PC            ; {code.ImageMagnet}
C2B7: 17 04 A3        LBSR    $C75D               ; {code.Draw16x8}
C2BA: 16 00 C9        LBRA    $C386               ; {code.NextObject} Next object
;
C2BD: 5A              DECB                        ; 4=SKATE
C2BE: 26 24           BNE     $C2E4               ; {} No ... check other types
C2C0: 8D 13           BSR     $C2D5               ; {}
C2C2: 17 05 96        LBSR    $C85B               ; {}
C2C5: 6C 07           INC     7,X                 
C2C7: 86 10           LDA     #$10                
C2C9: 5F              CLRB                        
C2CA: 17 07 32        LBSR    $C9FF               ; {}
C2CD: 8D 06           BSR     $C2D5               ; {}
C2CF: 17 04 8B        LBSR    $C75D               ; {code.Draw16x8}
C2D2: 16 00 B1        LBRA    $C386               ; {code.NextObject} Next object
;
C2D5: 33 8D 08 51     LEAU    $CB2A,PC            ; {code.ImageSkate} Skate graphic 1
C2D9: E6 07           LDB     7,X                 
C2DB: C4 01           ANDB    #$01                
C2DD: 26 04           BNE     $C2E3               ; {}
C2DF: 33 8D 08 57     LEAU    $CB3A,PC            ; {} Skate graphic 2
C2E3: 39              RTS                         ; Done
;
C2E4: 5A              DECB                        ; 5=YOYO
C2E5: 26 3C           BNE     $C323               ; {} No ... check other types
C2E7: 33 8D 08 9F     LEAU    $CB8A,PC            ; {}
C2EB: 17 05 6D        LBSR    $C85B               ; {}
C2EE: 4F              CLRA                        
C2EF: A7 04           STA     4,X                 
C2F1: C6 20           LDB     #$20                
C2F3: 6D 07           TST     7,X                 
C2F5: 27 01           BEQ     $C2F8               ; {}
C2F7: 50              NEGB                        
C2F8: E7 05           STB     5,X                 
C2FA: 17 06 CB        LBSR    $C9C8               ; {}
C2FD: E6 02           LDB     2,X                 
C2FF: C1 0C           CMPB    #$0C                
C301: 24 04           BHS     $C307               ; {}
C303: 6F 07           CLR     7,X                 
C305: C6 0C           LDB     #$0C                
C307: C1 42           CMPB    #$42                
C309: 25 04           BLO     $C30F               ; {}
C30B: 6C 07           INC     7,X                 
C30D: C6 42           LDB     #$42                
C30F: E7 02           STB     2,X                 
C311: 33 8D 08 35     LEAU    $CB4A,PC            ; {code.ImageYoYo} YoYo images
C315: C4 03           ANDB    #$03                ; 4 of them
C317: 58              ASLB                        ; 16 ...
C318: 58              ASLB                        ; ... bytes ...
C319: 58              ASLB                        ; ... each ...
C31A: 58              ASLB                        ; ... image
C31B: 33 C5           LEAU    B,U                 ; Point to current image
C31D: 17 04 3D        LBSR    $C75D               ; {code.Draw16x8}
C320: 16 00 63        LBRA    $C386               ; {code.NextObject} Next object
;
C323: 5A              DECB                        ; 6=PEAR
C324: 26 09           BNE     $C32F               ; {} No ... check other types
C326: 33 8D 08 90     LEAU    $CBBA,PC            ; {code.ImagePear}
C32A: 17 04 30        LBSR    $C75D               ; {code.Draw16x8}
C32D: 20 57           BRA     $C386               ; {code.NextObject} Next object
;
C32F: 5A              DECB                        ; 7=SPIDER
C330: 26 21           BNE     $C353               ; {} No ... check other types
C332: 8D 10           BSR     $C344               ; {}
C334: 17 05 24        LBSR    $C85B               ; {}
C337: CC 30 30        LDD     #$3030              
C33A: 17 06 C2        LBSR    $C9FF               ; {}
C33D: 8D 05           BSR     $C344               ; {}
C33F: 17 04 1B        LBSR    $C75D               ; {code.Draw16x8}
C342: 20 42           BRA     $C386               ; {code.NextObject} Next object
;
C344: 33 8D 08 82     LEAU    $CBCA,PC            ; {code.ImageSpider}
C348: E6 02           LDB     2,X                 
C34A: C4 01           ANDB    #$01                
C34C: 26 04           BNE     $C352               ; {}
C34E: 33 8D 08 88     LEAU    $CBDA,PC            ; {}
C352: 39              RTS                         
;
C353: 5A              DECB                        ; 8=SKULL
C354: 26 09           BNE     $C35F               ; {} No ... check other types
C356: 33 8D 08 50     LEAU    $CBAA,PC            ; {code.ImageSkull}
C35A: 17 04 00        LBSR    $C75D               ; {code.Draw16x8}
C35D: 20 27           BRA     $C386               ; {code.NextObject} Next object

C35F: 5A              DECB                        ; 9=X
C360: 26 24           BNE     $C386               ; {code.NextObject} No. Anything but 0-9 ... skip.
C362: 8D 13           BSR     $C377               ; {} Get the current image
C364: 17 04 F4        LBSR    $C85B               ; {}
C367: 6C 07           INC     7,X                 
C369: CC 7F 7F        LDD     #$7F7F              
C36C: 17 06 90        LBSR    $C9FF               ; {}
C36F: 8D 06           BSR     $C377               ; {}
C371: 17 03 E9        LBSR    $C75D               ; {code.Draw16x8}
C374: 16 00 0F        LBRA    $C386               ; {code.NextObject} Next object
;
C377: 33 8D 08 6F     LEAU    $CBEA,PC            ; {code.ImageX} X picture small
C37B: E6 07           LDB     7,X                 
C37D: C4 01           ANDB    #$01                
C37F: 26 04           BNE     $C385               ; {}
C381: 33 8D 08 75     LEAU    $CBFA,PC            ; {} X picture large
C385: 39              RTS                         

NextObject:
C386: 6F 04           CLR     4,X                 
C388: 6F 05           CLR     5,X                 
C38A: 30 08           LEAX    8,X                 
C38C: 16 FE E3        LBRA    $C272               ; {code.ObjectLoop}

C38F: 9F D2           STX     $D2                 ; {ram.D2}
C391: AD 9F A0 0A     JSR     [$A00A]             ; {hard.JOYIN} JOYIN reads all 4 joysticks (15A,15B,15C,15D)
C395: 8E 00 D8        LDX     #$00D8              
C398: 10 8E 01 5A     LDY     #$015A              
C39C: D6 B6           LDB     $B6                 ; {ram.Player} Player number
C39E: 58              ASLB                        ; 2 axis per joystick
C39F: 31 A5           LEAY    B,Y                 ; Point to 15A, 15B (player 0) or 15C, 15D (player 1)
C3A1: E6 A4           LDB     ,Y                  
C3A3: A6 A4           LDA     ,Y                  ; Add in ...
C3A5: 9B D7           ADDA    $D7                 ; {ram.Random} ... some ...
C3A7: 97 D7           STA     $D7                 ; {ram.Random} ... randomness
C3A9: C0 20           SUBB    #$20                
C3AB: E7 04           STB     4,X                 
C3AD: E6 21           LDB     1,Y                 ; Next axis
C3AF: C0 20           SUBB    #$20                
C3B1: E7 05           STB     5,X                 
C3B3: 17 06 12        LBSR    $C9C8               ; {}
C3B6: 17 03 66        LBSR    $C71F               ; {}
C3B9: 8E 00 D8        LDX     #$00D8              
C3BC: 17 05 A0        LBSR    $C95F               ; {}
C3BF: D7 BF           STB     $BF                 ; {ram.BF}
C3C1: 17 03 4F        LBSR    $C713               ; {}
C3C4: 0F C3           CLR     $C3                 ; {ram.C3}
C3C6: D6 BE           LDB     $BE                 ; {ram.BE}
C3C8: D7 C0           STB     $C0                 ; {ram.C0}
C3CA: D6 C0           LDB     $C0                 ; {ram.C0}
C3CC: C0 02           SUBB    #$02                
C3CE: D7 C0           STB     $C0                 ; {ram.C0}
C3D0: D1 BE           CMPB    $BE                 ; {ram.BE}
C3D2: 10 27 01 24     LBEQ    $C4FA               ; {}
C3D6: 8E 02 00        LDX     #$0200              
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
C3F7: 0F BF           CLR     $BF                 ; {ram.BF}
C3F9: 0D C3           TST     $C3                 ; {ram.C3}
C3FB: 27 CD           BEQ     $C3CA               ; {}
C3FD: 0F BF           CLR     $BF                 ; {ram.BF}
C3FF: D6 C0           LDB     $C0                 ; {ram.C0}
C401: D7 C1           STB     $C1                 ; {ram.C1}
C403: D6 BE           LDB     $BE                 ; {ram.BE}
C405: D7 C0           STB     $C0                 ; {ram.C0}
C407: D6 C0           LDB     $C0                 ; {ram.C0}
C409: C0 02           SUBB    #$02                
C40B: D7 C0           STB     $C0                 ; {ram.C0}
C40D: 8E 02 00        LDX     #$0200              
C410: 3A              ABX                         
C411: EC 84           LDD     ,X                  
C413: C0 03           SUBB    #$03                
C415: D7 C2           STB     $C2                 ; {ram.C2}
C417: 80 03           SUBA    #$03                
C419: 8E 01 60        LDX     #$0160              
C41C: 6D 06           TST     6,X                 
C41E: 27 15           BEQ     $C435               ; {}
C420: D6 C2           LDB     $C2                 ; {ram.C2}
C422: E0 02           SUBB    2,X                 
C424: 54              LSRB                        
C425: 26 0A           BNE     $C431               ; {}
C427: A1 84           CMPA    ,X                  
C429: 22 04           BHI     $C42F               ; {}
C42B: 6C 04           INC     4,X                 
C42D: 20 02           BRA     $C431               ; {}
C42F: 6C 05           INC     5,X                 
C431: 30 08           LEAX    8,X                 
C433: 20 E7           BRA     $C41C               ; {}
C435: D6 C0           LDB     $C0                 ; {ram.C0}
C437: D1 C1           CMPB    $C1                 ; {ram.C1}
C439: 26 CC           BNE     $C407               ; {}
C43B: 8E 01 60        LDX     #$0160              
C43E: 0F C4           CLR     $C4                 ; {ram.C4}
C440: 0F C8           CLR     $C8                 ; {ram.C8}
C442: 0F C9           CLR     $C9                 ; {ram.C9}
C444: E6 06           LDB     6,X                 
C446: 27 5D           BEQ     $C4A5               ; {}
C448: 6D 04           TST     4,X                 
C44A: 27 55           BEQ     $C4A1               ; {}
C44C: 6D 05           TST     5,X                 
C44E: 27 51           BEQ     $C4A1               ; {}
C450: C1 08           CMPB    #$08                
C452: 27 4D           BEQ     $C4A1               ; {}
C454: 0C C4           INC     $C4                 ; {ram.C4}
C456: 0C D0           INC     $D0                 ; {ram.D0}
C458: 0A CE           DEC     $CE                 ; {ram.CE}
C45A: 33 8D 0B 4B     LEAU    $CFA9,PC            ; {} Copyright info
C45E: E6 C5           LDB     B,U                 
C460: 1D              SEX                         
C461: D3 C8           ADDD    $C8                 ; {ram.C8}
C463: DD C8           STD     $C8                 ; {ram.C8}
C465: CE 00 EA        LDU     #$00EA              
C468: E6 84           LDB     ,X                  
C46A: E7 C4           STB     ,U                  
C46C: E6 02           LDB     2,X                 
C46E: E7 42           STB     2,U                 
C470: 33 8D 07 B7     LEAU    $CC2B,PC            ; {code.StrWhiteBlock}
C474: 17 03 E4        LBSR    $C85B               ; {}
C477: E6 06           LDB     6,X                 
C479: C1 05           CMPB    #$05                
C47B: 26 11           BNE     $C48E               ; {}
C47D: 33 8D 07 19     LEAU    $CB9A,PC            ; {}
C481: 17 03 D7        LBSR    $C85B               ; {}
C484: E6 02           LDB     2,X                 
C486: C0 04           SUBB    #$04                
C488: E7 02           STB     2,X                 
C48A: C1 03           CMPB    #$03                
C48C: 2E F3           BGT     $C481               ; {}
C48E: 1F 13           TFR     X,U                 
C490: C6 08           LDB     #$08                
C492: DF D2           STU     $D2                 ; {ram.D2}
C494: A6 48           LDA     8,U                 
C496: A7 C0           STA     ,U+                 
C498: 5A              DECB                        
C499: 26 F9           BNE     $C494               ; {}
C49B: 6D 46           TST     6,U                 
C49D: 26 F1           BNE     $C490               ; {}
C49F: 20 A3           BRA     $C444               ; {}
C4A1: 30 08           LEAX    8,X                 
C4A3: 20 9F           BRA     $C444               ; {}
C4A5: 0D C4           TST     $C4                 ; {ram.C4}
C4A7: 27 51           BEQ     $C4FA               ; {}
C4A9: 17 02 73        LBSR    $C71F               ; {}
C4AC: 4F              CLRA                        
C4AD: 5F              CLRB                        
C4AE: D3 C8           ADDD    $C8                 ; {ram.C8}
C4B0: 0A C4           DEC     $C4                 ; {ram.C4}
C4B2: 26 FA           BNE     $C4AE               ; {}
C4B4: DD CA           STD     $CA                 ; {ram.CA}
C4B6: 0D B6           TST     $B6                 ; {ram.Player} Player 0 or 1
C4B8: 26 06           BNE     $C4C0               ; {} ... player 1 ???
C4BA: D3 B7           ADDD    $B7                 ; {ram.P1Score} Player 0 score???
C4BC: DD B7           STD     $B7                 ; {ram.P1Score}
C4BE: 20 04           BRA     $C4C4               ; {}
C4C0: D3 B9           ADDD    $B9                 ; {ram.P2Score} Player 1 score???
C4C2: DD B9           STD     $B9                 ; {ram.P2Score}
C4C4: C6 3C           LDB     #$3C                
C4C6: D7 C6           STB     $C6                 ; {ram.C6}
C4C8: 8E 00 EA        LDX     #$00EA              
C4CB: E6 84           LDB     ,X                  
C4CD: C1 60           CMPB    #$60                
C4CF: 2F 02           BLE     $C4D3               ; {}
C4D1: C6 60           LDB     #$60                
C4D3: E7 84           STB     ,X                  
C4D5: 17 04 DA        LBSR    $C9B2               ; {code.GetScreenAndShift}
C4D8: DF CC           STU     $CC                 ; {ram.CC}
C4DA: 0C C7           INC     $C7                 ; {ram.C7}
C4DC: 17 01 31        LBSR    $C610               ; {}
C4DF: 7F FF 20        CLR     $FF20               ; {hard.PIA1_DA}
C4E2: BD A9 76        JSR     $A976               
C4E5: C6 80           LDB     #$80                
C4E7: 1F 98           TFR     B,A                 
C4E9: 4A              DECA                        
C4EA: 26 FD           BNE     $C4E9               ; {}
C4EC: F7 FF 20        STB     $FF20               ; {hard.PIA1_DA}
C4EF: 1F 98           TFR     B,A                 
C4F1: 4A              DECA                        
C4F2: 26 FD           BNE     $C4F1               ; {}
C4F4: 7F FF 20        CLR     $FF20               ; {hard.PIA1_DA}
C4F7: 5A              DECB                        
C4F8: 26 ED           BNE     $C4E7               ; {}
C4FA: 8E 02 00        LDX     #$0200              
C4FD: D6 BE           LDB     $BE                 ; {ram.BE}
C4FF: 3A              ABX                         
C500: CE 00 D8        LDU     #$00D8              
C503: A6 C4           LDA     ,U                  
C505: E6 42           LDB     2,U                 
C507: ED 84           STD     ,X                  
C509: D6 BF           LDB     $BF                 ; {ram.BF}
C50B: DB BD           ADDB    $BD                 ; {ram.BD}
C50D: D7 BD           STB     $BD                 ; {ram.BD}
C50F: 0C BE           INC     $BE                 ; {ram.BE}
C511: 0C BE           INC     $BE                 ; {ram.BE}
C513: 0C D1           INC     $D1                 ; {ram.D1}
C515: 10 26 00 B3     LBNE    $C5CC               ; {}
C519: D6 CE           LDB     $CE                 ; {ram.CE}
C51B: C1 13           CMPB    #$13                
C51D: 10 2C 00 AB     LBGE    $C5CC               ; {}
C521: 0C CE           INC     $CE                 ; {ram.CE}
C523: 33 8D 0A 7A     LEAU    $CFA1,PC            ; {}
C527: 17 05 54        LBSR    $CA7E               ; {}
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
C541: 84 07           ANDA    #$07                
C543: 4C              INCA                        
C544: 81 08           CMPA    #$08                
C546: 26 09           BNE     $C551               ; {}
C548: 0C CF           INC     $CF                 ; {ram.CF}
C54A: D6 CF           LDB     $CF                 ; {ram.CF}
C54C: C1 0A           CMPB    #$0A                
C54E: 23 01           BLS     $C551               ; {}
C550: 4C              INCA                        
C551: 9E D2           LDX     $D2                 ; {ram.D2}
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
C5CC: 17 05 20        LBSR    $CAEF               ; {code.WaitVBlank}
C5CF: 0D C7           TST     $C7                 ; {ram.C7}
C5D1: 27 09           BEQ     $C5DC               ; {}
C5D3: 0A C6           DEC     $C6                 ; {ram.C6}
C5D5: 26 05           BNE     $C5DC               ; {}
C5D7: 17 01 45        LBSR    $C71F               ; {}
C5DA: 0F C7           CLR     $C7                 ; {ram.C7}
C5DC: 0A D5           DEC     $D5                 ; {ram.D5}
C5DE: 26 2F           BNE     $C60F               ; {}
C5E0: C6 28           LDB     #$28                
C5E2: D7 D5           STB     $D5                 ; {ram.D5}
C5E4: C6 58           LDB     #$58                
C5E6: 0D B6           TST     $B6                 ; {ram.Player}
C5E8: 26 12           BNE     $C5FC               ; {}
C5EA: 86 18           LDA     #$18                
C5EC: 03 D6           COM     $D6                 ; {ram.D6}
C5EE: 26 06           BNE     $C5F6               ; {}
C5F0: 33 8D 06 89     LEAU    $CC7D,PC            ; {code.StrOne}
C5F4: 20 16           BRA     $C60C               ; {}
C5F6: 33 8D 06 31     LEAU    $CC2B,PC            ; {code.StrWhiteBlock}
C5FA: 20 10           BRA     $C60C               ; {}
C5FC: 86 52           LDA     #$52                
C5FE: 03 D6           COM     $D6                 ; {ram.D6}
C600: 26 06           BNE     $C608               ; {}
C602: 33 8D 06 98     LEAU    $CC9E,PC            ; {code.StrTwo}
C606: 20 04           BRA     $C60C               ; {}
C608: 33 8D 06 1F     LEAU    $CC2B,PC            ; {code.StrWhiteBlock}
C60C: 17 03 34        LBSR    $C943               ; {code.PrintChars}
C60F: 39              RTS                         
C610: C6 FF           LDB     #$FF                
C612: D7 C5           STB     $C5                 ; {ram.C5}
C614: DC B7           LDD     $B7                 ; {ram.P1Score}
C616: CE 0F 2B        LDU     #$0F2B              
C619: 17 00 0F        LBSR    $C62B               ; {code.DrawNumber}
C61C: 0D B4           TST     $B4                 ; {ram.NumPlayers}
C61E: 27 08           BEQ     $C628               ; {}
C620: DC B9           LDD     $B9                 ; {ram.P2Score}
C622: CE 0F 3A        LDU     #$0F3A              
C625: 17 00 03        LBSR    $C62B               ; {code.DrawNumber}
C628: 0F C5           CLR     $C5                 ; {ram.C5}
C62A: 39              RTS                         

DrawNumber:
; Numbers are kept in words ... max value 65_536. Max 5 digits.
C62B: 10 83 27 10     CMPD    #$2710              ; Decimal 10_000
C62F: 24 14           BHS     $C645               ; {}
C631: 10 83 03 E8     CMPD    #$03E8              ; Decimal 1_000
C635: 24 13           BHS     $C64A               ; {}
C637: 10 83 00 64     CMPD    #$0064              ; Decimal 100
C63B: 24 12           BHS     $C64F               ; {}
C63D: 10 83 00 0A     CMPD    #$000A              ; Decimal 10
C641: 24 11           BHS     $C654               ; {}
C643: 20 14           BRA     $C659               ; {}
;
C645: 8E 27 10        LDX     #$2710              
C648: 8D 19           BSR     $C663               ; {}
C64A: 8E 03 E8        LDX     #$03E8              
C64D: 8D 14           BSR     $C663               ; {}
C64F: 8E 00 64        LDX     #$0064              
C652: 8D 0F           BSR     $C663               ; {}
C654: 8E 00 0A        LDX     #$000A              
C657: 8D 0A           BSR     $C663               ; {}
;
C659: 8E 00 01        LDX     #$0001              
C65C: 8D 05           BSR     $C663               ; {}
C65E: 4F              CLRA                        
C65F: 5F              CLRB                        
C660: 8D 01           BSR     $C663               ; {}
C662: 39              RTS                         
;
C663: 34 10           PSHS    X                   
C665: 30 8D 00 78     LEAX    $C6E1,PC            ; {code.Digit0} Graphics for "0"
C669: A3 E4           SUBD    ,S                  
C66B: 25 46           BLO     $C6B3               ; {}
C66D: 30 8D 00 75     LEAX    $C6E6,PC            ; {code.Digit1} Graphics for "1"
C671: A3 E4           SUBD    ,S                  
C673: 25 3E           BLO     $C6B3               ; {}
C675: 30 8D 00 72     LEAX    $C6EB,PC            ; {code.Digit2}
C679: A3 E4           SUBD    ,S                  
C67B: 25 36           BLO     $C6B3               ; {}
C67D: 30 8D 00 6F     LEAX    $C6F0,PC            ; {code.Digit3}
C681: A3 E4           SUBD    ,S                  
C683: 25 2E           BLO     $C6B3               ; {}
C685: 30 8D 00 6C     LEAX    $C6F5,PC            ; {code.Digit4}
C689: A3 E4           SUBD    ,S                  
C68B: 25 26           BLO     $C6B3               ; {}
C68D: 30 8D 00 69     LEAX    $C6FA,PC            ; {code.Digit5}
C691: A3 E4           SUBD    ,S                  
C693: 25 1E           BLO     $C6B3               ; {}
C695: 30 8D 00 66     LEAX    $C6FF,PC            ; {code.Digit6}
C699: A3 E4           SUBD    ,S                  
C69B: 25 16           BLO     $C6B3               ; {}
C69D: 30 8D 00 63     LEAX    $C704,PC            ; {code.Digit7}
C6A1: A3 E4           SUBD    ,S                  
C6A3: 25 0E           BLO     $C6B3               ; {}
C6A5: 30 8D 00 60     LEAX    $C709,PC            ; {code.Digit8}
C6A9: A3 E4           SUBD    ,S                  
C6AB: 25 06           BLO     $C6B3               ; {}
C6AD: 30 8D 00 5D     LEAX    $C70E,PC            ; {code.Digit9}
C6B1: A3 E4           SUBD    ,S                  
C6B3: E3 E4           ADDD    ,S                  
C6B5: 34 06           PSHS    B,A                 
C6B7: E6 84           LDB     ,X                  
C6B9: 54              LSRB                        
C6BA: D8 C5           EORB    $C5                 ; {ram.C5}
C6BC: E7 C0           STB     ,U+                 
C6BE: E6 01           LDB     1,X                 
C6C0: 54              LSRB                        
C6C1: D8 C5           EORB    $C5                 ; {ram.C5}
C6C3: E7 C8 1F        STB     $1F,U               
C6C6: E6 02           LDB     2,X                 
C6C8: 54              LSRB                        
C6C9: D8 C5           EORB    $C5                 ; {ram.C5}
C6CB: E7 C8 3F        STB     $3F,U               
C6CE: E6 03           LDB     3,X                 
C6D0: 54              LSRB                        
C6D1: D8 C5           EORB    $C5                 ; {ram.C5}
C6D3: E7 C8 5F        STB     $5F,U               
C6D6: E6 04           LDB     4,X                 
C6D8: 54              LSRB                        
C6D9: D8 C5           EORB    $C5                 ; {ram.C5}
C6DB: E7 C8 7F        STB     $7F,U               
C6DE: 35 16           PULS    A,B,X               
C6E0: 39              RTS                         

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
C6EB: 20 88 08 20 A8 

Digit3:
C6F0: A8 08 28 08 A8 

Digit4:
C6F5: 80 88 88 A8 08            

Digit5:
C6FA: A8 80 20 08 A0 

Digit6:
C6FF: A8 80 A8 88 A8 

Digit7:
C704: A8 08 08 20 20 

Digit8:
C709: A8 88 A8 88 A8 

Digit9:
C70E: 20 88 28 08 A0 

; Draws CA ??? Might be score of the object
C713: 0D C7           TST     $C7                 ; {ram.C7}
C715: 27 07           BEQ     $C71E               ; {}
C717: DE CC           LDU     $CC                 ; {ram.CC} Screen coordinate
C719: DC CA           LDD     $CA                 ; {ram.CA} Value
C71B: 17 FF 0D        LBSR    $C62B               ; {code.DrawNumber} Draw number
C71E: 39              RTS                         

; Erase CA ??? Might be the score of the object
C71F: 0D C7           TST     $C7                 ; {ram.C7}
C721: 27 2A           BEQ     $C74D               ; {}
C723: DE CC           LDU     $CC                 ; {ram.CC} Screen coordinate
C725: DC CA           LDD     $CA                 ; {ram.CA} Value
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

Draw16x8:
C75D: C6 08           LDB     #$08                ; 8 Rows
C75F: 34 54           PSHS    U,X,B               
C761: 17 02 4E        LBSR    $C9B2               ; {code.GetScreenAndShift}
C764: 10 8E 03 80     LDY     #$0380              ; Mask table
C768: AE 63           LDX     3,S                 ; Incoming U (data pointer) to X
C76A: 5D              TSTB                        ; 0 means ...
C76B: 10 27 00 CA     LBEQ    $C839               ; {} ... draw with no shift
C76F: 5A              DECB                        ; 1 means ...
C770: 10 27 00 88     LBEQ    $C7FC               ; {} ... one shift right
C774: 5A              DECB                        ; 2 means ...
C775: 10 27 00 3E     LBEQ    $C7B7               ; {} ... four shift right ???
;
C779: E6 80           LDB     ,X+                 ; Two shift left
C77B: 4F              CLRA                        
C77C: 58              ASLB                        
C77D: 49              ROLA                        
C77E: 58              ASLB                        
C77F: 49              ROLA                        
C780: 34 06           PSHS    B,A                 
C782: E6 80           LDB     ,X+                 
C784: 4F              CLRA                        
C785: 58              ASLB                        
C786: 49              ROLA                        
C787: 58              ASLB                        
C788: 49              ROLA                        
C789: AB 61           ADDA    1,S                 
C78B: A7 61           STA     1,S                 
C78D: 34 04           PSHS    B                   
C78F: A6 A5           LDA     B,Y                 
C791: A4 42           ANDA    2,U                 
C793: AB E4           ADDA    ,S                  
C795: A7 42           STA     2,U                 
C797: E6 62           LDB     2,S                 
C799: A6 A5           LDA     B,Y                 
C79B: A4 41           ANDA    1,U                 
C79D: AB 62           ADDA    2,S                 
C79F: A7 41           STA     1,U                 
C7A1: E6 61           LDB     1,S                 
C7A3: A6 A5           LDA     B,Y                 
C7A5: A4 C4           ANDA    ,U                  
C7A7: AB 61           ADDA    1,S                 
C7A9: A7 C4           STA     ,U                  
C7AB: 32 63           LEAS    3,S                 
C7AD: 33 C8 20        LEAU    $20,U               
C7B0: 6A E4           DEC     ,S                  
C7B2: 26 C5           BNE     $C779               ; {}
C7B4: 16 00 A1        LBRA    $C858               ; {}
;
C7B7: E6 80           LDB     ,X+                 
C7B9: 4F              CLRA                        
C7BA: 54              LSRB                        
C7BB: 46              RORA                        
C7BC: 54              LSRB                        
C7BD: 46              RORA                        
C7BE: 54              LSRB                        
C7BF: 46              RORA                        
C7C0: 54              LSRB                        
C7C1: 46              RORA                        
C7C2: 34 06           PSHS    B,A                 
C7C4: E6 80           LDB     ,X+                 
C7C6: 4F              CLRA                        
C7C7: 54              LSRB                        
C7C8: 46              RORA                        
C7C9: 54              LSRB                        
C7CA: 46              RORA                        
C7CB: 54              LSRB                        
C7CC: 46              RORA                        
C7CD: 54              LSRB                        
C7CE: 46              RORA                        
C7CF: EB E4           ADDB    ,S                  
C7D1: E7 E4           STB     ,S                  
C7D3: 34 02           PSHS    A                   
C7D5: A6 A6           LDA     A,Y                 
C7D7: A4 42           ANDA    2,U                 
C7D9: AB E4           ADDA    ,S                  
C7DB: A7 42           STA     2,U                 
C7DD: E6 61           LDB     1,S                 
C7DF: A6 A5           LDA     B,Y                 
C7E1: A4 41           ANDA    1,U                 
C7E3: AB 61           ADDA    1,S                 
C7E5: A7 41           STA     1,U                 
C7E7: E6 62           LDB     2,S                 
C7E9: A6 A5           LDA     B,Y                 
C7EB: A4 C4           ANDA    ,U                  
C7ED: AB 62           ADDA    2,S                 
C7EF: A7 C4           STA     ,U                  
C7F1: 32 63           LEAS    3,S                 
C7F3: 33 C8 20        LEAU    $20,U               
C7F6: 6A E4           DEC     ,S                  
C7F8: 26 BD           BNE     $C7B7               ; {}
C7FA: 20 5C           BRA     $C858               ; {}
;
; One shift right
C7FC: E6 80           LDB     ,X+                 
C7FE: 4F              CLRA                        
C7FF: 54              LSRB                        
C800: 46              RORA                        
C801: 54              LSRB                        
C802: 46              RORA                        
C803: 34 06           PSHS    B,A                 
C805: E6 80           LDB     ,X+                 
C807: 4F              CLRA                        
C808: 54              LSRB                        
C809: 46              RORA                        
C80A: 54              LSRB                        
C80B: 46              RORA                        
C80C: EB E4           ADDB    ,S                  
C80E: E7 E4           STB     ,S                  
C810: 34 02           PSHS    A                   
C812: A6 A6           LDA     A,Y                 
C814: A4 42           ANDA    2,U                 
C816: AB E4           ADDA    ,S                  
C818: A7 42           STA     2,U                 
C81A: E6 61           LDB     1,S                 
C81C: A6 A5           LDA     B,Y                 
C81E: A4 41           ANDA    1,U                 
C820: AB 61           ADDA    1,S                 
C822: A7 41           STA     1,U                 
C824: E6 62           LDB     2,S                 
C826: A6 A5           LDA     B,Y                 
C828: A4 C4           ANDA    ,U                  
C82A: AB 62           ADDA    2,S                 
C82C: A7 C4           STA     ,U                  
C82E: 32 63           LEAS    3,S                 
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

C85B: C6 08           LDB     #$08                
C85D: 34 54           PSHS    U,X,B               
C85F: 17 01 50        LBSR    $C9B2               ; {code.GetScreenAndShift}
C862: 10 8E 03 80     LDY     #$0380              
C866: AE 63           LDX     3,S                 
C868: 5D              TSTB                        
C869: 10 27 00 B8     LBEQ    $C925               ; {}
C86D: 5A              DECB                        
C86E: 10 27 00 7C     LBEQ    $C8EE               ; {}
C872: 5A              DECB                        
C873: 10 27 00 38     LBEQ    $C8AF               ; {}
C877: E6 80           LDB     ,X+                 
C879: 4F              CLRA                        
C87A: 58              ASLB                        
C87B: 49              ROLA                        
C87C: 58              ASLB                        
C87D: 49              ROLA                        
C87E: 34 06           PSHS    B,A                 
C880: E6 80           LDB     ,X+                 
C882: 4F              CLRA                        
C883: 58              ASLB                        
C884: 49              ROLA                        
C885: 58              ASLB                        
C886: 49              ROLA                        
C887: AB 61           ADDA    1,S                 
C889: A7 61           STA     1,S                 
C88B: 34 04           PSHS    B                   
C88D: A6 A5           LDA     B,Y                 
C88F: A4 42           ANDA    2,U                 
C891: A7 42           STA     2,U                 
C893: E6 62           LDB     2,S                 
C895: A6 A5           LDA     B,Y                 
C897: A4 41           ANDA    1,U                 
C899: A7 41           STA     1,U                 
C89B: E6 61           LDB     1,S                 
C89D: A6 A5           LDA     B,Y                 
C89F: A4 C4           ANDA    ,U                  
C8A1: A7 C4           STA     ,U                  
C8A3: 32 63           LEAS    3,S                 
C8A5: 33 C8 20        LEAU    $20,U               
C8A8: 6A E4           DEC     ,S                  
C8AA: 26 CB           BNE     $C877               ; {}
C8AC: 16 00 91        LBRA    $C940               ; {}
C8AF: E6 80           LDB     ,X+                 
C8B1: 4F              CLRA                        
C8B2: 54              LSRB                        
C8B3: 46              RORA                        
C8B4: 54              LSRB                        
C8B5: 46              RORA                        
C8B6: 54              LSRB                        
C8B7: 46              RORA                        
C8B8: 54              LSRB                        
C8B9: 46              RORA                        
C8BA: 34 06           PSHS    B,A                 
C8BC: E6 80           LDB     ,X+                 
C8BE: 4F              CLRA                        
C8BF: 54              LSRB                        
C8C0: 46              RORA                        
C8C1: 54              LSRB                        
C8C2: 46              RORA                        
C8C3: 54              LSRB                        
C8C4: 46              RORA                        
C8C5: 54              LSRB                        
C8C6: 46              RORA                        
C8C7: EB E4           ADDB    ,S                  
C8C9: E7 E4           STB     ,S                  
C8CB: 34 02           PSHS    A                   
C8CD: A6 A6           LDA     A,Y                 
C8CF: A4 42           ANDA    2,U                 
C8D1: A7 42           STA     2,U                 
C8D3: E6 61           LDB     1,S                 
C8D5: A6 A5           LDA     B,Y                 
C8D7: A4 41           ANDA    1,U                 
C8D9: A7 41           STA     1,U                 
C8DB: E6 62           LDB     2,S                 
C8DD: A6 A5           LDA     B,Y                 
C8DF: A4 C4           ANDA    ,U                  
C8E1: A7 C4           STA     ,U                  
C8E3: 32 63           LEAS    3,S                 
C8E5: 33 C8 20        LEAU    $20,U               
C8E8: 6A E4           DEC     ,S                  
C8EA: 26 C3           BNE     $C8AF               ; {}
C8EC: 20 52           BRA     $C940               ; {}
C8EE: E6 80           LDB     ,X+                 
C8F0: 4F              CLRA                        
C8F1: 54              LSRB                        
C8F2: 46              RORA                        
C8F3: 54              LSRB                        
C8F4: 46              RORA                        
C8F5: 34 06           PSHS    B,A                 
C8F7: E6 80           LDB     ,X+                 
C8F9: 4F              CLRA                        
C8FA: 54              LSRB                        
C8FB: 46              RORA                        
C8FC: 54              LSRB                        
C8FD: 46              RORA                        
C8FE: EB E4           ADDB    ,S                  
C900: E7 E4           STB     ,S                  
C902: 34 02           PSHS    A                   
C904: A6 A6           LDA     A,Y                 
C906: A4 42           ANDA    2,U                 
C908: A7 42           STA     2,U                 
C90A: E6 61           LDB     1,S                 
C90C: A6 A5           LDA     B,Y                 
C90E: A4 41           ANDA    1,U                 
C910: A7 41           STA     1,U                 
C912: E6 62           LDB     2,S                 
C914: A6 A5           LDA     B,Y                 
C916: A4 C4           ANDA    ,U                  
C918: A7 C4           STA     ,U                  
C91A: 32 63           LEAS    3,S                 
C91C: 33 C8 20        LEAU    $20,U               
C91F: 6A E4           DEC     ,S                  
C921: 26 CB           BNE     $C8EE               ; {}
C923: 20 1B           BRA     $C940               ; {}
C925: EC 81           LDD     ,X++                
C927: 34 06           PSHS    B,A                 
C929: A6 A6           LDA     A,Y                 
C92B: A4 C4           ANDA    ,U                  
C92D: A7 C4           STA     ,U                  
C92F: E6 61           LDB     1,S                 
C931: A6 A5           LDA     B,Y                 
C933: A4 41           ANDA    1,U                 
C935: A7 41           STA     1,U                 
C937: 32 62           LEAS    2,S                 
C939: 33 C8 20        LEAU    $20,U               
C93C: 6A E4           DEC     ,S                  
C93E: 26 E5           BNE     $C925               ; {}
C940: 35 54           PULS    B,X,U               
C942: 39              RTS                         

PrintChars:
C943: 8E 00 E4        LDX     #$00E4              
C946: A7 84           STA     ,X                  
C948: E7 02           STB     2,X                 
C94A: E6 5F           LDB     -1,U                ; Characters ...
C94C: E7 04           STB     4,X                 ; ... to print
C94E: 17 FE 0C        LBSR    $C75D               ; {code.Draw16x8}
C951: 33 C8 10        LEAU    $10,U               ; Next image
C954: A6 84           LDA     ,X                  ; X coordinate
C956: 8B 08           ADDA    #$08                ; Next character ...
C958: A7 84           STA     ,X                  ; ... over
C95A: 6A 04           DEC     4,X                 ; All done?
C95C: 26 F0           BNE     $C94E               ; {} No ... do all
C95E: 39              RTS                         ; Done

C95F: 17 00 50        LBSR    $C9B2               ; {code.GetScreenAndShift}
C962: A6 C4           LDA     ,U                  
C964: 5D              TSTB                        
C965: 26 0A           BNE     $C971               ; {}
C967: 84 3F           ANDA    #$3F                
C969: 1F 89           TFR     A,B                 
C96B: E0 C4           SUBB    ,U                  
C96D: 8A 80           ORA     #$80                
C96F: 20 22           BRA     $C993               ; {}
C971: 5A              DECB                        
C972: 26 0A           BNE     $C97E               ; {}
C974: 84 CF           ANDA    #$CF                
C976: 1F 89           TFR     A,B                 
C978: E0 C4           SUBB    ,U                  
C97A: 8A 20           ORA     #$20                
C97C: 20 15           BRA     $C993               ; {}
C97E: 5A              DECB                        
C97F: 26 0A           BNE     $C98B               ; {}
C981: 84 F3           ANDA    #$F3                
C983: 1F 89           TFR     A,B                 
C985: E0 C4           SUBB    ,U                  
C987: 8A 08           ORA     #$08                
C989: 20 08           BRA     $C993               ; {}
C98B: 84 FC           ANDA    #$FC                
C98D: 1F 89           TFR     A,B                 
C98F: E0 C4           SUBB    ,U                  
C991: 8A 02           ORA     #$02                
C993: A7 C4           STA     ,U                  
C995: 39              RTS                         
C996: A6 C4           LDA     ,U                  
C998: 5D              TSTB                        
C999: 26 04           BNE     $C99F               ; {}
C99B: 84 3F           ANDA    #$3F                
C99D: 20 10           BRA     $C9AF               ; {}
C99F: 5A              DECB                        
C9A0: 26 04           BNE     $C9A6               ; {}
C9A2: 84 CF           ANDA    #$CF                
C9A4: 20 09           BRA     $C9AF               ; {}
C9A6: 5A              DECB                        
C9A7: 26 04           BNE     $C9AD               ; {}
C9A9: 84 F3           ANDA    #$F3                
C9AB: 20 02           BRA     $C9AF               ; {}
C9AD: 84 FC           ANDA    #$FC                
C9AF: A7 C4           STA     ,U                  
C9B1: 39              RTS                         
   
GetScreenAndShift:
; Input: X pointer to object structure
; Mangle: A, Y
; Return: U screen pointer
; Return: B shift amount
C9B2: E6 84           LDB     ,X                  ; ?? Something to do with screen coords X coordinate?
C9B4: A6 02           LDA     2,X                 ; ?? Y coordinate?
C9B6: 58              ASLB                        ; ?? X times 2
C9B7: 47              ASRA                        ; Divide by ...
C9B8: 56              RORB                        ; ?? 8
C9B9: 47              ASRA                        
C9BA: 56              RORB                        
C9BB: 47              ASRA                        
C9BC: 56              RORB                        
C9BD: 10 8E 04 00     LDY     #$0400              ; Start of screen memory
C9C1: 33 AB           LEAU    D,Y                 ; Point to screen memory
C9C3: E6 84           LDB     ,X                  ; X coordinate
C9C5: C4 03           ANDB    #$03                ; 4 pixels per byte ... 4 possible shifts
C9C7: 39              RTS                         

C9C8: E6 04           LDB     4,X                 
C9CA: 1D              SEX                         
C9CB: 58              ASLB                        
C9CC: 49              ROLA                        
C9CD: 58              ASLB                        
C9CE: 49              ROLA                        
C9CF: 58              ASLB                        
C9D0: 49              ROLA                        
C9D1: E3 84           ADDD    ,X                  
C9D3: 80 03           SUBA    #$03                
C9D5: 81 7B           CMPA    #$7B                
C9D7: 25 07           BLO     $C9E0               ; {}
C9D9: 86 7A           LDA     #$7A                
C9DB: 6D 04           TST     4,X                 
C9DD: 2A 01           BPL     $C9E0               ; {}
C9DF: 4F              CLRA                        
C9E0: 8B 03           ADDA    #$03                
C9E2: ED 84           STD     ,X                  
C9E4: E6 05           LDB     5,X                 
C9E6: 1D              SEX                         
C9E7: 58              ASLB                        
C9E8: 58              ASLB                        
C9E9: 58              ASLB                        
C9EA: 49              ROLA                        
C9EB: E3 02           ADDD    2,X                 
C9ED: 80 03           SUBA    #$03                
C9EF: 81 53           CMPA    #$53                
C9F1: 25 07           BLO     $C9FA               ; {}
C9F3: 86 52           LDA     #$52                
C9F5: 6D 05           TST     5,X                 
C9F7: 2A 01           BPL     $C9FA               ; {}
C9F9: 4F              CLRA                        
C9FA: 8B 03           ADDA    #$03                
C9FC: ED 02           STD     2,X                 
C9FE: 39              RTS                         
C9FF: A7 04           STA     4,X                 
CA01: E7 05           STB     5,X                 
CA03: CE 00 D8        LDU     #$00D8              
CA06: A6 84           LDA     ,X                  
CA08: 8B 04           ADDA    #$04                
CA0A: A7 84           STA     ,X                  
CA0C: A0 C4           SUBA    ,U                  
CA0E: 2B 07           BMI     $CA17               ; {}
CA10: 60 04           NEG     4,X                 
CA12: 4D              TSTA                        
CA13: 26 02           BNE     $CA17               ; {}
CA15: 6F 04           CLR     4,X                 
CA17: E6 04           LDB     4,X                 
CA19: A6 02           LDA     2,X                 
CA1B: 8B 04           ADDA    #$04                
CA1D: A7 02           STA     2,X                 
CA1F: A0 42           SUBA    2,U                 
CA21: 2B 07           BMI     $CA2A               ; {}
CA23: 60 05           NEG     5,X                 
CA25: 4D              TSTA                        
CA26: 26 02           BNE     $CA2A               ; {}
CA28: 6F 05           CLR     5,X                 
CA2A: 17 FF 9B        LBSR    $C9C8               ; {}
CA2D: A6 84           LDA     ,X                  
CA2F: 80 04           SUBA    #$04                
CA31: 81 03           CMPA    #$03                
CA33: 2C 02           BGE     $CA37               ; {}
CA35: 86 03           LDA     #$03                
CA37: 81 76           CMPA    #$76                
CA39: 2F 02           BLE     $CA3D               ; {}
CA3B: 86 76           LDA     #$76                
CA3D: A7 84           STA     ,X                  
CA3F: A6 02           LDA     2,X                 
CA41: 80 04           SUBA    #$04                
CA43: 81 03           CMPA    #$03                
CA45: 2C 02           BGE     $CA49               ; {}
CA47: 86 03           LDA     #$03                
CA49: 81 4E           CMPA    #$4E                
CA4B: 2F 02           BLE     $CA4F               ; {}
CA4D: 86 4E           LDA     #$4E                
CA4F: A7 02           STA     2,X                 
CA51: 39              RTS                         

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

CA7E: 7F FF 20        CLR     $FF20               ; {hard.PIA1_DA}
CA81: BD A9 76        JSR     $A976               
CA84: 17 00 39        LBSR    $CAC0               ; {code.CheckForBreak}
CA87: EC C1           LDD     ,U++                
CA89: 27 34           BEQ     $CABF               ; {}
CA8B: 34 06           PSHS    B,A                 
CA8D: 1F 98           TFR     B,A                 
CA8F: 4A              DECA                        
CA90: 1E 11           EXG     X,X                 
CA92: 1E 11           EXG     X,X                 
CA94: 1E 11           EXG     X,X                 
CA96: 1E 11           EXG     X,X                 
CA98: 26 F5           BNE     $CA8F               ; {}
CA9A: 86 3C           LDA     #$3C                
CA9C: B7 FF 20        STA     $FF20               ; {hard.PIA1_DA}
CA9F: 1F 98           TFR     B,A                 
CAA1: A0 61           SUBA    1,S                 
CAA3: 43              COMA                        
CAA4: 4A              DECA                        
CAA5: 1E 11           EXG     X,X                 
CAA7: 1E 11           EXG     X,X                 
CAA9: 1E 11           EXG     X,X                 
CAAB: 1E 11           EXG     X,X                 
CAAD: 26 F5           BNE     $CAA4               ; {}
CAAF: 7F FF 20        CLR     $FF20               ; {hard.PIA1_DA}
CAB2: 5A              DECB                        
CAB3: 26 02           BNE     $CAB7               ; {}
CAB5: E6 61           LDB     1,S                 
CAB7: 6A E4           DEC     ,S                  
CAB9: 26 D2           BNE     $CA8D               ; {}
CABB: 35 06           PULS    A,B                 
CABD: 20 BF           BRA     $CA7E               ; {}
CABF: 39              RTS                         

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

; ???
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
StrWhiteBlock:
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

CD0F: 06 
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

CEC3: 6D B6           TST     [A,Y]               
CEC5: 27 6D           BEQ     $CF34               ; {}
CEC7: 12              NOP                         
CEC8: 52 ; ????
CEC9: 12              NOP                         
CECA: 49              ROLA                        
CECB: 5A              DECB                        
CECC: 49              ROLA                        
CECD: 5B ; ????
CECE: 6D 29           TST     9,Y                 
CED0: 25 12           BLO     $CEE4               ; {}
CED2: 4A              DECA                        
CED3: 5D              TSTB                        
CED4: 92 24           SBCA    $24                 
CED6: E5 30           BITB    -16,Y               
CED8: 09 52           ROL     $52                 
CEDA: 53              COMB                        
CEDB: 24 E5           BHS     $CEC2               ; {}
CEDD: 52 ; ????
CEDE: 49              ROLA                        
CEDF: 24 ED           BHS     $CECE               ; {}
CEE1: 12              NOP                         
CEE2: 52 ; ????
CEE3: 10 ; ????
CEE4: 49              ROLA                        
CEE5: 5C              INCB                        
CEE6: 00 4B           NEG     $4B                 
CEE8: 2D 39           BLT     $CF23               ; {}
CEEA: 25 70           BLO     $CF5C               ; {}
CEEC: 52 ; ????
CEED: 24 93           BHS     $CE82               ; {}
CEEF: 02 ; ????
CEF0: 49              ROLA                        
CEF1: 60 01           NEG     1,X                 
CEF3: 59              ROLB                        
CEF4: 6D 49           TST     9,U                 
CEF6: 2C 24           BGE     $CF1C               ; {}
CEF8: 93 02           SUBD    $02                 
CEFA: 4A              DECA                        
CEFB: 49              ROLA                        
CEFC: 76 24 93        ROR     $2493               
CEFF: 12              NOP                         
CF00: 92 02           SBCA    $02                 
CF02: 49              ROLA                        
CF03: 60 01           NEG     1,X                 
CF05: 59              ROLB                        
CF06: 6D 49           TST     9,U                 
CF08: 2C 02           BGE     $CF0C               ; {}
CF0A: 93 14           SUBD    $14                 
CF0C: 9F 64           STX     $64                 
CF0E: 8A 39           ORA     #$39                
CF10: 6E 40           JMP     0,U                 
CF12: 4A              DECA                        
CF13: 14 ; ????
CF14: 9D 24           JSR     $24                 
CF16: 49              ROLA                        
CF17: 6D ; ????
CF18: DA 39           ORB     $39                 
CF1A: 2E 24           BGT     $CF40               ; {}
CF1C: 92 12           SBCA    $12                 
CF1E: 49              ROLA                        
CF1F: 00 41           NEG     $41                 
CF21: 5B ; ????
CF22: 70 4B 2C        NEG     $4B2C               
CF25: 24 4C           BHS     $CF73               ; {}
CF27: 37 AB           PULU    CC,A,DP,Y,PC        
CF29: 12              NOP                         
CF2A: 52 ; ????
CF2B: 00 00           NEG     $00                 
CF2D: 00 FF           NEG     $FF                 
CF2F: 01 ; ????
CF30: FF 01 00        STU     $0100               
CF33: 01 ; ????
CF34: 01 ; ????
CF35: 00 01           NEG     $01                 
CF37: FF 01 FF        STU     $01FF               
CF3A: 00 FF           NEG     $FF                 
CF3C: FF 28 80        STU     $2880               
CF3F: 40              NEGA                        
CF40: 40              NEGA                        
CF41: 28 80           BVC     $CEC3               ; {}
CF43: 40              NEGA                        
CF44: 40              NEGA                        
CF45: 28 80           BVC     $CEC7               ; {}
CF47: 40              NEGA                        
CF48: 40              NEGA                        
CF49: 28 80           BVC     $CECB               ; {}
CF4B: 40              NEGA                        
CF4C: 40              NEGA                        
CF4D: 19              DAA                         
CF4E: 5F              CLRB                        
CF4F: 19              DAA                         
CF50: 64 19           LSR     -7,X                
CF52: 5F              CLRB                        
CF53: 1A 55           ORCC    #$55                
CF55: 1C 4B           ANDCC   #$4B                
CF57: 1C 55           ANDCC   #$55                
CF59: 1C 4B           ANDCC   #$4B                
CF5B: 1C 43           ANDCC   #$43                
CF5D: 40              NEGA                        
CF5E: 40              NEGA                        
CF5F: 00 00           NEG     $00                 
CF61: 28 80           BVC     $CEE3               ; {}
CF63: 40              NEGA                        
CF64: 40              NEGA                        
CF65: 40              NEGA                        
CF66: 43              COMA                        
CF67: 40              NEGA                        
CF68: 40              NEGA                        
CF69: 37 5F           PULU    CC,A,B,DP,X,S       
CF6B: 37 4B           PULU    CC,A,DP,S           
CF6D: 37 55           PULU    CC,B,X,S            
CF6F: 37 4B           PULU    CC,A,DP,S           
CF71: 19              DAA                         
CF72: 5F              CLRB                        
CF73: 19              DAA                         
CF74: 64 19           LSR     -7,X                
CF76: 5F              CLRB                        
CF77: 1A 55           ORCC    #$55                
CF79: 1C 4B           ANDCC   #$4B                
CF7B: 1C 55           ANDCC   #$55                
CF7D: 1C 4B           ANDCC   #$4B                
CF7F: 1C 43           ANDCC   #$43                
CF81: 40              NEGA                        
CF82: 40              NEGA                        
CF83: 00 00           NEG     $00                 
CF85: 28 80           BVC     $CF07               ; {}
CF87: 40              NEGA                        
CF88: 40              NEGA                        
CF89: 40              NEGA                        
CF8A: 43              COMA                        
CF8B: 3C 4B           CWAI    $4B                 
CF8D: 39              RTS                         
CF8E: 55 ; ????
CF8F: 37 5F           PULU    CC,A,B,DP,X,S       
CF91: 37 64           PULU    B,Y,S               
CF93: 37 5F           PULU    CC,A,B,DP,X,S       
CF95: 39              RTS                         
CF96: 55 ; ????
CF97: 3C 4B           CWAI    $4B                 
CF99: 40              NEGA                        
CF9A: 43              COMA                        
CF9B: 39              RTS                         
CF9C: 55 ; ????
CF9D: 40              NEGA                        
CF9E: 40              NEGA                        
CF9F: 00 00           NEG     $00                 
CFA1: 14 ; ????
CFA2: 1E 00           EXG     D,D                 
CFA4: 00 FF           NEG     $FF                 
CFA6: FF 00 00        STU     $0000               

CFA9: 00 07 0A 0F 14 19 1E 32 00 64                  

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
        Canvas.redrawGraphics()       
    }    
</script>
```

