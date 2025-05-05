![Phoenix](Phoenix.jpg)

# Phoenix

>>> cpu Z80

>>> binary 0000:roms/ic45 +  roms/ic46 + roms/ic47 + roms/ic48 + roms/h5-ic49.5a + roms/h6-ic50.6a + roms/h7-ic51.7a + roms/h8-ic52.8a

>>> memoryTable hard

[Hardware Info](Hardware.md)

>>> memoryTable ram

[RAM Usage](RAMUse.md)

```code
L0000:
0000: 00              NOP                         ; Start/restart and interrupts end up at 0008
0001: 00              NOP                         ; 
0002: 00              NOP                         ; 
0003: 00              NOP                         ; 
0004: 00              NOP                         ; 
0005: 00              NOP                         ; 
0006: 00              NOP                         ; 
0007: 00              NOP                         ; 
; 
0008: 31 FF 4B        LD      SP,$4BFF            ; Top-ish of RAM
000B: 26 50           LD      H,$50               ; 50xx video register
000D: 36 00           LD      (HL),$00            ; Select the first bank of RAM
000F: CD 50 00        CALL    $0050               ; {code.InitSoundScreen} Turn sound off and clear both screen areas
0012: 21 00 18        LD      HL,$1800            ; {+code.T1800} Screen draw info
0015: 0E 03           LD      C,$03               ; 3 columns (rotated to 3 rows)
0017: CD D0 01        CALL    $01D0               ; {code.PrintTextLines} Draw the first 3 rows of the background (scores and coins)

;*****************************************************************************
;* Main loop begin
;*****************************************************************************
MainLoop:
001A: CD 80 00        CALL    $0080               ; {code.WaitVBlankCoin} Wait for VBlank and count any coins
001D: 3A A2 43        LD      A,($43A2)           ; {ram.GameOrAttract}
0020: A7              AND     A                   ; updates the zero flag
0021: CA 2D 00        JP      Z,$002D             ; {code.L002D} if 'Attract mode'
; Game mode
0024: CD 00 04        CALL    $0400               ; {code.GameStateMachine} controls the flow of the game.
0027: CD 00 27        CALL    $2700               ; {code.UpdateScoresAndSound} updates scores and lives on screen, and sound HW
002A: C3 1A 00        JP      $001A               ; {code.MainLoop} Back to top of main loop
; Attract mode (no sound, no scoreing, no manual steering)
L002D:
002D: 3E 0F           LD      A,$0F               ; 0000_1111 mute the sound chip TMS36XX
002F: 26 60           LD      H,$60               ; 60xx sound A
0031: 77              LD      (HL),A              ; 
0032: 26 68           LD      H,$68               ; 68xx sound B
0034: 77              LD      (HL),A              ; 
0035: CD 77 03        CALL    $0377               ; {code.UpdateSoundControlRAM}
0038: 00              NOP                         ; 
0039: CD E0 17        CALL    $17E0               ; {code.CoinChecking}
003C: A7              AND     A                   ; updates the zero flag
003D: CA 46 00        JP      Z,$0046             ; {code.L0046} No credits ... continue splash
0040: CD 88 02        CALL    $0288               ; {code.PromptForStartGame}
0043: C3 1A 00        JP      $001A               ; {code.MainLoop} Back to top of main loop
; 
L0046:
0046: CD E3 00        CALL    $00E3               ; {code.SplashAndDemo}
0049: C3 1A 00        JP      $001A               ; {code.MainLoop} Back to top of main loop
; Main loop end.
; not used
004C: FF FF FF FF

;*****************************************************************************
;* Initialize the sound (off) and screen (clear)
;*****************************************************************************
InitSoundScreen:
0050: 26 68           LD      H,$68               ; 68xx sound B
0052: 36 00           LD      (HL),$00            ; Sound off
0054: 26 60           LD      H,$60               ; 60xx sound A
0056: 36 00           LD      (HL),$00            ; Sound off
0058: 26 58           LD      H,$58               ; 58xx scroll register
005A: 36 00           LD      (HL),$00            ; First memory bank
005C: CD 6B 00        CALL    $006B               ; {code.ClearRAMBank} Clear the bank (includes screen)
005F: 26 50           LD      H,$50               ; 50xx video register
0061: 36 01           LD      (HL),$01            ; Second memory bank
0063: CD 6B 00        CALL    $006B               ; {code.ClearRAMBank} Clear the bank (includes screen)
0066: 26 50           LD      H,$50               ; 50xx video register
0068: 36 00           LD      (HL),$00            ; Back to first memory bank
006A: C9              RET                         ; Done

;*****************************************************************************
;* Clear a RAM Bank (bank 0 or 1)
;* Set the lower bit of the video register to pick the bank before calling.
;* 4000 - 4BF8
;* We call this function, which means we don't want to clear the return on the stack.
;* That's why we start clearing at 4BF8 instead of 4BFF.
;* Since screen memory is part of this bank, we are clearing the screen too.
;*****************************************************************************
ClearRAMBank:
006B: 21 F8 4B        LD      HL,$4BF8            ; Highest point ... skip the top of the stack
006E: 3E 3F           LD      A,$3F               ; Stop when H reaches 3F
L0070:
0070: 36 00           LD      (HL),$00            ; Clear the memory
0072: 2B              DEC     HL                  ; Point to next
0073: BC              CP      H                   ; All done?
0074: C2 70 00        JP      NZ,$0070            ; {code.L0070} No ... go back for all
0077: C9              RET                         ; Done

;*****************************************************************************
;* Slow printing the static texts and filling the scroll register
;* with background tiles.
;* Only used at attract mode during the intro splash.
;*****************************************************************************
SlowPrintScrollRegisterUpdate:
0078: CD 96 01        CALL    $0196               ; {code.SlowPrintScoreAverageTable}
007B: C3 F0 06        JP      $06F0               ; {code.L06F0} update scroll register and fill background
;
007E: FF FF

;*****************************************************************************
;* Wait for the vertical blanking and then handle coin counting
;*****************************************************************************
WaitVBlankCoin:
0080: 26 78           LD      H,$78               ; 78xx DSW0 Check ...
0082: 7E              LD      A,(HL)              ; ... screen blanking flag
0083: E6 80           AND     $80                 ; Wait for it ...
0085: CA 80 00        JP      Z,$0080             ; {code.WaitVBlankCoin} ... to set
; 
L0088:
0088: 7E              LD      A,(HL)              ; Check screen blanking flag
0089: E6 80           AND     $80                 ; Wait for it ...
008B: C2 88 00        JP      NZ,$0088            ; {code.L0088} ... to clear (0=in blanking)
008E: 26 70           LD      H,$70               ; 70xx IN0 Current value ...
0090: 7E              LD      A,(HL)              ; ... of IN0 inputs
0091: 21 A0 43        LD      HL,$43A0            ; {+ram.IN0Current} Value from ...
0094: 46              LD      B,(HL)              ; ... last read
0095: 77              LD      (HL),A              ; Store new value
0096: 2C              INC     L                   ; To 43A1 IN0Previous
0097: 70              LD      (HL),B              ; Store old value
0098: 2E 9B           LD      L,$9B               ; Bump the Counter9A+1
009A: CD 00 02        CALL    $0200               ; {code.AddOneToMem}
009D: 2E 8F           LD      L,$8F               ; Get CoinCount
009F: 7E              LD      A,(HL)              ; 
;
; !! There are two digits for "coins" on the screen, but only the one's digit is
; !! changed. Once you get to 9, the code stops counting. It takes the coin
; !! from you, but it doesn't give you credit.
;
00A0: FE 09           CP      $09                 ; Already 9?
00A2: C8              RET     Z                   ; Yes ... nothing more to check
00A3: D2 00 00        JP      NC,$0000            ; {code.L0000} More than 9? OOPS -- soft reset
00A6: 06 01           LD      B,$01               ; Coin bit of the input register
00A8: CD BB 00        CALL    $00BB               ; {code.CheckInputBits} Has the coin input gone from 1 to 0?
00AB: C8              RET     Z                   ; No ... no coins inserted ... done
00AC: 2E 8F           LD      L,$8F               ; Add one ...
00AE: 34              INC     (HL)                ; ... to coin count
00AF: 7E              LD      A,(HL)              ; Current value ...
00B0: C6 20           ADD     $20                 ; ... to number tile
00B2: 32 42 41        LD      ($4142),A           ; {-} Change number of coins on screen
00B5: C9              RET                         ; Done
;
; Ghost code bytes from an older version.
; The code was probably shortened at this point during development and the following bytes were not specifically deleted.
00B6: 00              NOP                         ; 
00B7: C9              RET                         ; 

00B8: FF FF FF

;*****************************************************************************
;* Check to see if a particular bit(s) in the input register has changed
;* from 1 to 0 since last we checked. Return NZ if transitioned from 1 to 0.
;*****************************************************************************
CheckInputBits:
00BB: 21 A0 43        LD      HL,$43A0            ; {+ram.IN0Current} Get current ...
00BE: 7E              LD      A,(HL)              ; ... input value
00BF: 2F              CPL                         ; Flip the current bits
00C0: A0              AND     B                   ; Mask off all but the ones we are checking
00C1: 2C              INC     L                   ; Point to last input value
00C2: A6              AND     (HL)                ; Zero unles new bit is 0 and old is 1
00C3: C9              RET                         ; Return state

;*****************************************************************************
;* Prints the number pointed to by HL (points to the end of the number) to the screen pointed
;* to by DE (points to the end of the screen area). B is the number of digits to print.
;*****************************************************************************
PrintNumber:
00C4: 7E              LD      A,(HL)              ; Get the two digits
00C5: E6 0F           AND     $0F                 ; Keep the LSB
00C7: F6 20           OR      $20                 ; Offset to number tile
00C9: 12              LD      (DE),A              ; Store the number tile to screen memory
00CA: CD 10 02        CALL    $0210               ; {code.LeftOneColumn} next screen position
00CD: 05              DEC     B                   ; All done?
00CE: C8              RET     Z                   ; Yes ... out
00CF: 7E              LD      A,(HL)              ; Keep the ...
00D0: 0F              RRCA                        ; ...
00D1: 0F              RRCA                        ; ...
00D2: 0F              RRCA                        ; ...
00D3: 0F              RRCA                        ; ...
00D4: E6 0F           AND     $0F                 ; ... LSB
00D6: F6 20           OR      $20                 ; Offset to number tile
00D8: 12              LD      (DE),A              ; Store the number tile to screen memory
00D9: CD 10 02        CALL    $0210               ; {code.LeftOneColumn} next screen position
00DC: 2B              DEC     HL                  ; Next data position
00DD: 05              DEC     B                   ; All digits done?
00DE: C2 C4 00        JP      NZ,$00C4            ; {code.PrintNumber} No ... keep going
00E1: C9              RET                         ; Yes ... out
;
00E2: FF

;*****************************************************************************
;* Handles the intro splash and the game demo.
;*****************************************************************************
SplashAndDemo:
00E3: 21 99 43        LD      HL,$4399            ; {+ram.Counter98+1} starts with 0
00E6: CD 00 02        CALL    $0200               ; {code.AddOneToMem} increases it by one
00E9: 01 01 00        LD      BC,$0001            ; 
00EC: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
00EF: CA E1 01        JP      Z,$01E1             ; {code.PrintCopyright} do if Counter98 is >= 00 01
00F2: 01 02 00        LD      BC,$0002            ; 
00F5: 11 1F 01        LD      DE,$011F            ; used as delay counter
00F8: CD 60 02        CALL    $0260               ; {code.SubtractIfEnough}
00FB: D2 96 01        JP      NC,$0196            ; {code.SlowPrintScoreAverageTable} do if Counter98 is >= 00 02
00FE: 01 20 01        LD      BC,$0120            ; for a longer break
0101: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
0104: CA CA 0B        JP      Z,$0BCA             ; {code.DrawScoreAverageTableTiles} do if Counter98 is >= 01 20
0107: 0E B0           LD      C,$B0               ; for a short break
0109: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
010C: CA E1 01        JP      Z,$01E1             ; {code.PrintCopyright} do if Counter98 is >= 01 B0
010F: 0E B8           LD      C,$B8               ; 
0111: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
0114: CA 80 05        JP      Z,$0580             ; {code.InitGlobalLevelData} do if Counter98 is >= 01 B8
0117: 0E C0           LD      C,$C0               ; for a short break
0119: 11 DF 02        LD      DE,$02DF            ; 
011C: CD 60 02        CALL    $0260               ; {code.SubtractIfEnough}
011F: D2 78 00        JP      NC,$0078            ; {code.SlowPrintScrollRegisterUpdate} do if Counter98 is >= 01 C0
0122: 01 00 03        LD      BC,$0300            ; 
0125: 11 AF 03        LD      DE,$03AF            ; 
0128: CD 60 02        CALL    $0260               ; {code.SubtractIfEnough}
012B: D2 DC 21        JP      NC,$21DC            ; {code.DrawIntroBirdAnimationFrame} do if Counter98 is >= 03 00
012E: 01 E6 03        LD      BC,$03E6            ; 
0131: 11 FF FF        LD      DE,$FFFF            ; 
0134: CD 60 02        CALL    $0260               ; {code.SubtractIfEnough}
0137: D2 B0 03        JP      NC,$03B0            ; {code.GameDemo} do if Counter98 is >= 03 E6
013A: C9              RET                         ; 

013B: FF FF FF FF FF

;*****************************************************************************
;* Clears foreground and background but leaves the 3 score rows.
;*****************************************************************************
ClearForeAndBackground:
0140: CD A0 03        CALL    $03A0               ; {code.ClearBackground} Clear the background
0143: CD 80 00        CALL    $0080               ; {code.WaitVBlankCoin} Wait for VBlank
0146: CD 80 03        CALL    $0380               ; {code.ClearForeground} Clear the foreground (leave the 3 score rows)
0149: 21 A3 43        LD      HL,$43A3            ; {+ram.GameAndDemoOrSplash}
014C: 36 02           LD      (HL),$02            ; set to: 'Intro splash'
014E: 2C              INC     L                   ; GameState
014F: 36 00           LD      (HL),$00            ; to 0
0151: 00              NOP                         ; Old command removed or space for a future replace patch
0152: 00              NOP                         ; ..
0153: 00              NOP                         ; ..
0154: 2E B8           LD      L,$B8               ; LevelAndRound, CounterB9, AliensLeft, BirdsLeft, $43BC, $43BD, BonusLivesAt, $43BF to 0
0156: 06 08           LD      B,$08               ; number of bytes to clear
0158: CD D8 05        CALL    $05D8               ; {code.ClearBbytesAtHL}
015B: 2E BA           LD      L,$BA               ; Set AliensLeft
015D: 36 10           LD      (HL),$10            ; to 16 aliens left in wave
015F: 2E BE           LD      L,$BE               ; BonusLivesAt
0161: 3A 00 78        LD      A,($7800)           ; {hard.DSW0} 78xx DSW0, get DIP switch settings
0164: E6 0C           AND     $0C                 ; mask out 0000_1100 the Bonus lives
0166: 07              RLCA                        ; rotate left ..
0167: 07              RLCA                        ; .. to 0011_0000
0168: C6 30           ADD     $30                 ; $30, $40, $50, or $60
016A: 77              LD      (HL),A              ; save to BonusLivesAt
016B: 26 58           LD      H,$58               ; 58xx scroll register
016D: 36 00           LD      (HL),$00            ; init screen scrolling
016F: CD 80 00        CALL    $0080               ; {code.WaitVBlankCoin}
0172: C9              RET                         ; 

;*****************************************************************************
;* Used for the game demo during attract mode.
;* Returning the bits for feeding the IN0Current for the simulated player inputs.
;* Resulting values are depending on Counter98 .
;* Counter value goes from $03E6 to $1510 during the demo.
;* 1010_1110...move left
;* 1100_1110...move right
;* 1111_1110...push fire
;* 0111_1110...push shield
;*****************************************************************************
GetPlayerInputsForDemo:
0173: 7E              LD      A,(HL)              ; get Counter98+1 (LSB from 16 bit counter)
0174: E6 7F           AND     $7F                 ; mask out 0111_1111, (counter goes from 00 to $7F)
0176: 06 CE           LD      B,$CE               ; return : 1100_1110...move right
0178: FE 1F           CP      $1F                 ; 1st trigger point of demo
017A: D8              RET     C                   ; return if greater
017B: 06 FE           LD      B,$FE               ; 1111_1110...push fire
017D: C8              RET     Z                   ; return if equal
017E: 06 AE           LD      B,$AE               ; 1010_1110...move left
0180: FE 5F           CP      $5F                 ; 2nd trigger point of demo
0182: D8              RET     C                   ; return if greater
0183: 06 FE           LD      B,$FE               ; 1111_1110...push fire
0185: C8              RET     Z                   ; return if equal
0186: 06 CE           LD      B,$CE               ; 1100_1110...move right
0188: FE 7F           CP      $7F                 ; 3rd trigger point of demo
018A: D8              RET     C                   ; return if greater
018B: 06 FE           LD      B,$FE               ; 1111_1110...push fire
018D: 2D              DEC     L                   ; 
018E: 7E              LD      A,(HL)              ; get Counter98 (MSB from 16 bit counter)
018F: FE 09           CP      $09                 ; 4rd trigger point of demo
0191: C0              RET     NZ                  ; return if not equal
0192: 06 7E           LD      B,$7E               ; 0111_1110...push shield
0194: C9              RET                         ; 

0195: FF

;*****************************************************************************
;* Slow printing the static texts for the score average table 
;* and the big letters of phoenix title.
;*****************************************************************************
SlowPrintScoreAverageTable:
0196: 7E              LD      A,(HL)              ; get actual index for slow print ($4399)
0197: E6 1F           AND     $1F                 ; mask out 0001_1111
0199: FE 06           CP      $06                 ; reached state 6 ?
019B: D8              RET     C                   ; no..return
019C: 5F              LD      E,A                 ; save the state
019D: 7E              LD      A,(HL)              ; get actual index for slow print ($4399)
019E: E6 E0           AND     $E0                 ; mask out 1110_0000
01A0: 4F              LD      C,A                 ; save bits 5,6,7
01A1: 2D              DEC     L                   ; 
01A2: 46              LD      B,(HL)              ; get zero reference from $4398
01A3: 2E A8           LD      L,$A8               ; ..and..
01A5: 70              LD      (HL),B              ; save it to $43A8
01A6: 2C              INC     L                   ; 
01A7: 71              LD      (HL),C              ; save bits 5,6,7 to $43A9
01A8: 01 60 18        LD      BC,$1860            ; {+code.T1860} data block starting with 'INSERT  COIN' text
01AB: CD 06 02        CALL    $0206               ; {code.AddBCtoMem} stores MSB LSB
01AE: 7E              LD      A,(HL)              ; 
01AF: 2D              DEC     L                   ; 
01B0: 66              LD      H,(HL)              ; 
01B1: 6F              LD      L,A                 ; 
01B2: 7B              LD      A,E                 ; 
01B3: 56              LD      D,(HL)              ; get the data
01B4: 2C              INC     L                   ; 
01B5: 5E              LD      E,(HL)              ; 
01B6: 2D              DEC     L                   ; 
01B7: 4F              LD      C,A                 ; 
01B8: 85              ADD     A,L                 ; 
01B9: 6F              LD      L,A                 ; 
01BA: 79              LD      A,C                 ; 
01BB: D6 06           SUB     $06                 ; 
01BD: 4F              LD      C,A                 ; 
01BE: CA C8 01        JP      Z,$01C8             ; {code.L01C8}
L01C1:
01C1: CD 17 02        CALL    $0217               ; {code.RightOneColumn} move to next screen position
01C4: 0D              DEC     C                   ; 
01C5: C2 C1 01        JP      NZ,$01C1            ; {code.L01C1}
L01C8:
01C8: 7E              LD      A,(HL)              ; 
01C9: 12              LD      (DE),A              ; print one character on the screen
01CA: C3 E0 14        JP      $14E0               ; {code.L14E0} check for coin event
; Ghost code bytes from an older version.
; The code was probably shortened at this point during development and the following bytes were not specifically deleted.
01CD: C2 C0 01        JP      NZ,$01C0            ; {}

;*****************************************************************************
;* Print the top 3 lines (scores, lives, coins)
;*****************************************************************************
PrintTextLines:
01D0: 56              LD      D,(HL)              ; Get ...
01D1: 2C              INC     L                   ; ... the ...
01D2: 5E              LD      E,(HL)              ; ... screen coord
01D3: 7D              LD      A,L                 ; Add 5 ...
01D4: C6 05           ADD     $05                 ; ... go get ...
01D6: 6F              LD      L,A                 ; ... data
01D7: 06 1A           LD      B,$1A               ; 26 columns
01D9: CD ED 01        CALL    $01ED               ; {code.DrawRow} Draw next row
01DC: 0D              DEC     C                   ; All lines done?
01DD: C2 D0 01        JP      NZ,$01D0            ; {code.PrintTextLines} No ... draw all rows
01E0: C9              RET                         ; Done

;*****************************************************************************
;* Print the copyright lines (bottom 3 lines)
;*****************************************************************************
PrintCopyright:
01E1: CD 40 01        CALL    $0140               ; {code.ClearForeAndBackground}
L01E4:
01E4: 21 60 19        LD      HL,$1960            ; {+code.T1960} "PHOENIX ... U.S.A"
01E7: 0E 03           LD      C,$03               ; 3 lines at the bottom
01E9: C3 D0 01        JP      $01D0               ; {code.PrintTextLines} Print the copyright
;
01EC: FF

;*****************************************************************************
;* Remember the screen is rotated.
;* This draws a column in screen memory (row on the screen)
;*****************************************************************************
DrawRow:
01ED: 7E              LD      A,(HL)              ; Copy the data ...
01EE: 12              LD      (DE),A              ; .. to the screen
01EF: 23              INC     HL                  ; Next in data
01F0: CD 17 02        CALL    $0217               ; {code.RightOneColumn} Move DE to next row
01F3: 05              DEC     B                   ; All drawn?
01F4: C2 ED 01        JP      NZ,$01ED            ; {code.DrawRow} Draw them all
01F7: C9              RET                         ; Done

01F8: FF FF FF FF FF FF FF FF

;*****************************************************************************
;* Two-byte +1 to (HL-1) : (HL).
;*****************************************************************************
AddOneToMem:
0200: 34              INC     (HL)                ; Add one to LSB
0201: C0              RET     NZ                  ; We didn't overflow ... done
0202: 2D              DEC     L                   ; Back up to MSB
0203: 34              INC     (HL)                ; Carry into the MSB
0204: 2C              INC     L                   ; Restore point to LSB
0205: C9              RET                         ; Done

;*****************************************************************************
;* Two-byte addition. BC is added to (HL-1) : (HL).
;*****************************************************************************
AddBCtoMem:
0206: 7E              LD      A,(HL)              ; Get the lower byte
0207: 81              ADD     A,C                 ; Add C to the lower
0208: 77              LD      (HL),A              ; Store the new lower
0209: 2D              DEC     L                   ; Back up to upper byte
020A: 7E              LD      A,(HL)              ; Add B and carry ...
020B: 88              ADC     A,B                 ; ... to upper byte
020C: 77              LD      (HL),A              ; Store the new upper byte
020D: 2C              INC     L                   ; Restore pointer to LSB
020E: C9              RET                         ; Done

020F: FF

;*****************************************************************************
;* Add 32 (left one column on the rotated screen) to DE (two bytes)
;*****************************************************************************
LeftOneColumn:
0210: 7B              LD      A,E                 ; Add ...
0211: C6 20           ADD     $20                 ; ... 32 to ...
0213: 5F              LD      E,A                 ; ... E
0214: D0              RET     NC                  ; No carry ... we are done
0215: 14              INC     D                   ; Carry into D
0216: C9              RET                         ; Done

;*****************************************************************************
;* Subtract 32 (right one column on the rotated screen) from DE (two bytes)
;*****************************************************************************
RightOneColumn:
0217: 7B              LD      A,E                 ; Subtract ...
0218: D6 20           SUB     $20                 ; ... 32 from ...
021A: 5F              LD      E,A                 ; ... E
021B: D0              RET     NC                  ; No borrow ... we are done
021C: 15              DEC     D                   ; Borrow from D
021D: C9              RET                         ; Done

021E: FF FF

;*****************************************************************************
;* 3-byte (6 digit) BCD addition. Add BC*10 to (HL-2):(HL-1):(HL).
;* The games keeps the lowest digit of the scores to 0.
;*****************************************************************************
AddToScore:
0220: AF              XOR     A                   ; !! Pointless. We are about to change A and the flags
0221: 7E              LD      A,(HL)              ; Lowest 2 digits
0222: 81              ADD     A,C                 ; Add C to score
0223: 27              DAA                         ; Adjust for binary coded decimal
0224: 77              LD      (HL),A              ; Update lowest 2 digits
0225: 2D              DEC     L                   ; Point to middle 2 digits
0226: 7E              LD      A,(HL)              ; Add B to ...
0227: 88              ADC     A,B                 ; ... score
0228: 27              DAA                         ; Adjust for BCD
0229: 77              LD      (HL),A              ; Store the middle 2 digits
022A: 2D              DEC     L                   ; Point to the upper 2 digits
022B: 7E              LD      A,(HL)              ; Add in ...
022C: CE 00           ADC     $00                 ; ... any carry
022E: 27              DAA                         ; Adjust for binary coded decimal
022F: 77              LD      (HL),A              ; Store the upper 2 digits
0230: 2C              INC     L                   ; Restore ...
0231: 2C              INC     L                   ; ... pointer
0232: C9              RET                         ; Done

0233: FF FF FF

; 3-byte (6 digit) BCD subtraction. This is never called.
;
; !! We have score ADDER above. I like the symmetry of a score SUBTRACTER, but
; !! this is never called. Scores never decrease.
;
0236: 37              SCF                         ; Take ...
0237: 3E 99           LD      A,$99               ; ... the BCD ...
0239: CE 00           ADC     $00                 ; ... add-complement ...
023B: 91              SUB     C                   ; ... of C
023C: 86              ADD     A,(HL)              ; Lower two digits
023D: 27              DAA                         ; Adjust for BCD
023E: 77              LD      (HL),A              ; Update lower two digits
023F: 2D              DEC     L                   ; Point to middle digits
0240: 3E 99           LD      A,$99               ; Take the BCD ...
0242: CE 00           ADC     $00                 ; ... add-complement ...
0244: 90              SUB     B                   ; ... of C
0245: 86              ADD     A,(HL)              ; Middle two digits
0246: 27              DAA                         ; Adjust for BCD
0247: 77              LD      (HL),A              ; Update middle two digits
0248: 2D              DEC     L                   ; Point to upper digits
0249: 3E 99           LD      A,$99               ; Take the BCD add-complement ...
024B: CE 00           ADC     $00                 ; ... of any carry
024D: 86              ADD     A,(HL)              ; Upper two digits
024E: 27              DAA                         ; Adjust for BCD
024F: 77              LD      (HL),A              ; Update upper two digits
0250: 2C              INC     L                   ; Restore ...
0251: 2C              INC     L                   ; ... pointer
0252: C9              RET                         ; Done

0253: FF FF FF FF FF

;*****************************************************************************
;* Two byte compare of BC to memory at (HL-1):(HL)
;*****************************************************************************
CompareBCtoMem:
0258: 7E              LD      A,(HL)              ; Value from memory
0259: B9              CP      C                   ; Are the lower values the same?
025A: C0              RET     NZ                  ; No ... return not-zero
025B: 2D              DEC     L                   ; Point to MSB
025C: 7E              LD      A,(HL)              ; Get the MSB value
025D: 2C              INC     L                   ; Restore the pointer
025E: B8              CP      B                   ; Compare the MSBs
025F: C9              RET                         ; Return the flags

;*****************************************************************************
;* Subtract DE from memory if memory is greater/equal to BC.
;*****************************************************************************
SubtractIfEnough:
0260: CD 70 02        CALL    $0270               ; {code.SubtractFromMemory} Try subtraction. Is memory larger (or equal) to BC?
0263: D8              RET     C                   ; No ... ignore request
0264: CD 77 02        CALL    $0277               ; {code.SubtractToMemory} Yes ... subtract DE from memory
0267: C9              RET                         ; Done

0268: FF FF FF FF FF FF FF FF

;*****************************************************************************
;* Two byte subtraction of memory from BC. BC = BC -  (HL-1):(HL)
;*****************************************************************************
SubtractFromMemory:
0270: 7E              LD      A,(HL)              ; Get the low byte
0271: 91              SUB     C                   ; Subtract from C
0272: 2D              DEC     L                   ; Point to upper byte
0273: 7E              LD      A,(HL)              ; Get the upper byte
0274: 98              SBC     B                   ; Subtract from B (with borrow)
0275: 2C              INC     L                   ; Restore pointer
0276: C9              RET                         ; Done

;*****************************************************************************
;* Two byte subtraction of DE from memory. (HL-1):(HL) = (HL-1):(HL) - DE
;*****************************************************************************
SubtractToMemory:
0277: 7B              LD      A,E                 ; Lower byte
0278: 96              SUB     (HL)                ; Subtract it from memory
0279: 2D              DEC     L                   ; Point to upper byte
027A: 7A              LD      A,D                 ; Value to A
027B: 9E              SBC     (HL)                ; Subtract upper byte from memory (with borrow)
027C: 2C              INC     L                   ; Restore pointer
027D: C9              RET                         ; Done

027E: FF FF

;*****************************************************************************
;* Two byte compare of HL to BC
;*****************************************************************************
CompareHLtoBC:
0280: 7D              LD      A,L                 ; Compare lower ...
0281: B9              CP      C                   ; ... bytes
0282: C0              RET     NZ                  ; Not the same ... return NZ
0283: 7C              LD      A,H                 ; Compare upper ...
0284: B8              CP      B                   ; ... bytes
0285: C9              RET                         ; Return the check

0286: FF FF

;*****************************************************************************
;* Start game screen 
;*****************************************************************************
PromptForStartGame:
0288: CD 40 01        CALL    $0140               ; {code.ClearForeAndBackground}
028B: 21 C0 19        LD      HL,$19C0            ; {+code.T19C0}
028E: 0E 02           LD      C,$02               ; print two lines: 'PUSH ONLY...1PLAYER BUTTON'
0290: CD D0 01        CALL    $01D0               ; {code.PrintTextLines}
0293: 0E 02           LD      C,$02               ; 
0295: CD E0 17        CALL    $17E0               ; {code.CoinChecking}
0298: FE 02           CP      $02                 ; 2 player mode possible if credit > 1
029A: DA A7 02        JP      C,$02A7             ; {code.L02A7}
029D: 21 A0 1B        LD      HL,$1BA0            ; {+code.T1BA0}
02A0: 0E 01           LD      C,$01               ; print one line: '1 OR 2PLAYERS BUTTON'
02A2: CD D0 01        CALL    $01D0               ; {code.PrintTextLines}
02A5: 0E 06           LD      C,$06               ; 
L02A7:
02A7: 3A 00 70        LD      A,($7000)           ; {hard.IN0} 70xx IN0  Get the bits...
02AA: 2F              CPL                         ; ...for the two...
02AB: A1              AND     C                   ; ...start buttons and...
02AC: C8              RET     Z                   ; ...ret if no start button was pressed.
02AD: CD CB 02        CALL    $02CB               ; {code.DecrementCoins} (GameOrAttract will be affected here as well)
02B0: CD F0 02        CALL    $02F0               ; {code.UpdateHiScore}
02B3: CD 2E 03        CALL    $032E               ; {code.ClearAndPrintScores}
02B6: CD 50 03        CALL    $0350               ; {code.GetPlayerLivesFromDip}
02B9: CD 40 01        CALL    $0140               ; {code.ClearForeAndBackground}
02BC: 26 50           LD      H,$50               ; 50xx video register
02BE: 36 01           LD      (HL),$01            ; 
02C0: CD 40 01        CALL    $0140               ; {code.ClearForeAndBackground}
02C3: 26 50           LD      H,$50               ; 50xx video register
02C5: 36 00           LD      (HL),$00            ; 
02C7: C9              RET                         ; 

02C8: FF FF FF

;*****************************************************************************
;* Coin handling
;*****************************************************************************
DecrementCoins:
02CB: 0E 01           LD      C,$01               ; Value for 'one player game mode'
02CD: FE 02           CP      $02                 ; A register holds the value of start buttons
02CF: CA D4 02        JP      Z,$02D4             ; {code.L02D4} jump if 'start 1' was pressed.
02D2: 0E 02           LD      C,$02               ; Value for 'two players game mode'
L02D4:
02D4: 21 A2 43        LD      HL,$43A2            ; {+ram.GameOrAttract}
02D7: 71              LD      (HL),C              ; set it to 1 or 2 and leave the attract mode.
02D8: 3A 00 78        LD      A,($7800)           ; {hard.DSW0} 78xx DSW0
02DB: E6 10           AND     $10                 ; mask for coinage 0001_0000
02DD: CA E3 02        JP      Z,$02E3             ; {code.L02E3}
02E0: 79              LD      A,C                 ; 
02E1: 07              RLCA                        ; Multiply by 2
02E2: 4F              LD      C,A                 ; 
L02E3:
02E3: 2E 8F           LD      L,$8F               ; LSB of CoinCount
02E5: 7E              LD      A,(HL)              ; get CoinCount value
02E6: 91              SUB     C                   ; decrement coins
02E7: 77              LD      (HL),A              ; save it
02E8: C6 20           ADD     $20                 ; map value to character code
02EA: 32 42 41        LD      ($4142),A           ; {ram.ForegroundScreen+142} updates the number of coins on the screen
02ED: C9              RET                         ; 

02EE: FF FF

;*****************************************************************************
;* Copy the score to hi score if greater
;*****************************************************************************
UpdateHiScore:
02F0: 11 83 43        LD      DE,$4383            ; {+ram.Score1low} score of player 1
02F3: 21 8B 43        LD      HL,$438B            ; {+ram.HiScorelow} current hi score
02F6: CD 14 03        CALL    $0314               ; {code.L0314}
02F9: D4 20 03        CALL    NC,$0320            ; {code.L0320}
02FC: 1E 87           LD      E,$87               ; LSB of Score2low
02FE: 2E 8B           LD      L,$8B               ; LSB of HiScorelow
0300: CD 14 03        CALL    $0314               ; {code.L0314}
0303: D4 20 03        CALL    NC,$0320            ; {code.L0320}
0306: 2E 8B           LD      L,$8B               ; LSB of HiScorelow
0308: 11 41 41        LD      DE,$4141            ; High-score Screen coordinates (LSB)
030B: 06 06           LD      B,$06               ; 6 digits
030D: CD C4 00        CALL    $00C4               ; {code.PrintNumber} Print the 6-digit number
0310: C9              RET                         ; Done
;
0311: FF FF FF
;
L0314:
0314: 1A              LD      A,(DE)              ; 
0315: 96              SUB     (HL)                ; 
0316: 1D              DEC     E                   ; 
0317: 2D              DEC     L                   ; 
0318: 1A              LD      A,(DE)              ; 
0319: 9E              SBC     (HL)                ; 
031A: 1D              DEC     E                   ; 
031B: 2D              DEC     L                   ; 
031C: 1A              LD      A,(DE)              ; 
031D: 9E              SBC     (HL)                ; 
031E: C9              RET                         ; 
;
031F: FF
;
L0320:
0320: 1A              LD      A,(DE)              ; 
0321: 77              LD      (HL),A              ; 
0322: 13              INC     DE                  ; 
0323: 23              INC     HL                  ; 
0324: 1A              LD      A,(DE)              ; 
0325: 77              LD      (HL),A              ; 
0326: 13              INC     DE                  ; 
0327: 23              INC     HL                  ; 
0328: 1A              LD      A,(DE)              ; 
0329: 77              LD      (HL),A              ; 
032A: C9              RET                         ; 

032B: FF FF FF

;*****************************************************************************
;* Update of the score values on screen.
;*****************************************************************************
ClearAndPrintScores:
032E: 21 80 43        LD      HL,$4380            ; {+ram.M4380} Clear scores..
L0331:
0331: 36 00           LD      (HL),$00            ; ..from $4380..
0333: 23              INC     HL                  ; 
0334: 7D              LD      A,L                 ; 
0335: FE 88           CP      $88                 ; ..to $4387
0337: C2 31 03        JP      NZ,$0331            ; {code.L0331}
033A: 2E 83           LD      L,$83               ; print player 1 score
033C: 11 61 42        LD      DE,$4261            ; Score1 screen coordinates (LSB)
033F: 06 06           LD      B,$06               ; 6 digits
0341: CD C4 00        CALL    $00C4               ; {code.PrintNumber}
0344: 2E 87           LD      L,$87               ; print player 2 score
0346: 11 21 40        LD      DE,$4021            ; Score2 screen coordinates (LSB)
0349: 06 06           LD      B,$06               ; 6 digits
034B: CD C4 00        CALL    $00C4               ; {code.PrintNumber}
034E: C9              RET                         ; Done

034F: FF

;*****************************************************************************
;* Gets the DIP switch settings for player lives.
;*****************************************************************************
GetPlayerLivesFromDip:
0350: 3A 00 78        LD      A,($7800)           ; {hard.DSW0} 78xx DSW0, get DIP switch settings
0353: E6 03           AND     $03                 ; mask out 0000_0011 number of lives
0355: C6 03           ADD     $03                 ; to get : 03, 04, 05 or 06
0357: 47              LD      B,A                 ; 
0358: 21 90 43        LD      HL,$4390            ; {+ram.Player1Lives}
035B: 70              LD      (HL),B              ; save it
035C: 2E A2           LD      L,$A2               ; LSB of GameOrAttract
035E: 7E              LD      A,(HL)              ; load GameOrAttract and ..
035F: FE 01           CP      $01                 ; check if one or two players mode
0361: CA 67 03        JP      Z,$0367             ; {code.UpdateLivesScreen}
0364: 2E 91           LD      L,$91               ; LSB of Player2Lives
0366: 70              LD      (HL),B              ; save it to Player2Lives

;*****************************************************************************
;* Updates the number of lives on the screen
;*****************************************************************************
UpdateLivesScreen:
0367: 2E 90           LD      L,$90               ; LSB of Player1Lives
0369: 7E              LD      A,(HL)              ; load Player1Lives
036A: F6 20           OR      $20                 ; map value to character code
036C: 32 A2 42        LD      ($42A2),A           ; {ram.ForegroundScreen+2A2} number of lives, for player 1 at screen ram
036F: 2C              INC     L                   ; 
0370: 7E              LD      A,(HL)              ; load Player2Lives
0371: F6 20           OR      $20                 ; map value to character code
0373: 32 62 40        LD      ($4062),A           ; {ram.ForegroundScreen+62} number of lives, for player 2 at screen ram
0376: C9              RET                         ; 

;*****************************************************************************
;* Update the sound control RAM registers
;*****************************************************************************
UpdateSoundControlRAM:
0377: 21 8C 43        LD      HL,$438C            ; {+ram.SoundControlA}
037A: 77              LD      (HL),A              ; 
037B: 2C              INC     L                   ; and update ..
037C: 77              LD      (HL),A              ; .. SoundControlB
037D: C9              RET                         ; 

037E: FF FF

;*****************************************************************************
;* Clears the foreground except for the top 3 rows (the scores)
;*****************************************************************************
ClearForeground:
0380: 21 3F 43        LD      HL,$433F            ; {+ram.ForegroundScreen+33F} End of foreground screen
0383: 11 1F 00        LD      DE,$001F            ; 00 for clear and 1F for finding end of a column
0386: 01 3F 03        LD      BC,$033F            ; 03 for leaving top 3 rows and 3F for find the beginning of screen memory
L0389:
0389: 72              LD      (HL),D              ; Clear the screen
038A: 2B              DEC     HL                  ; Next location
038B: 72              LD      (HL),D              ; Clear the screen
038C: 2B              DEC     HL                  ; Next location
038D: 7D              LD      A,L                 ; Keep lower 5 ...
038E: A3              AND     E                   ; ... bits (32 bytes in a column)
038F: B8              CP      B                   ; At the top of the column?
0390: C2 89 03        JP      NZ,$0389            ; {code.L0389} No ... keep clearing the column
0393: 72              LD      (HL),D              ; Clear the 4th column from the top
0394: 2B              DEC     HL                  ; To ...
0395: 2B              DEC     HL                  ; ... top ...
0396: 2B              DEC     HL                  ; ... of the ...
0397: 2B              DEC     HL                  ; ... row
0398: 7C              LD      A,H                 ; Have we reached ...
0399: B9              CP      C                   ; ... 3FFF ?
039A: C2 89 03        JP      NZ,$0389            ; {code.L0389} No ... clear all columns
039D: C9              RET                         ; Done
; 
039E: FF FF

;*****************************************************************************
;* Clears the background screen.
;*****************************************************************************
ClearBackground:
03A0: 21 3F 4B        LD      HL,$4B3F            ; {+ram.BackgroundScreen+33F} End of background screen memory
03A3: 11 47 00        LD      DE,$0047            ; 00 for clear and 47 to find the beginning of screen memory
L03A6:
03A6: 72              LD      (HL),D              ; Clear the screen
03A7: 2B              DEC     HL                  ; Next location
03A8: 72              LD      (HL),D              ; Clear the screen
03A9: 2B              DEC     HL                  ; Next location
03AA: 7C              LD      A,H                 ; Have we reached ...
03AB: BB              CP      E                   ; HL = 47FF ?
03AC: C2 A6 03        JP      NZ,$03A6            ; {code.L03A6} No ... keep clearing
03AF: C9              RET                         ; Done

;*****************************************************************************
;* The game demo is using the real game code with simulated player inputs.
;* The timeline of the game demo, as part of the attract mode,
;* is covered by the 16 bit counter: Counter98.
;* 1st demo from value: $03E6 to $07A0.
;* 2nd demo from value: $0800 to $0B60.
;* 3rd demo from value: $0C00 to $1510.
;*****************************************************************************
GameDemo:
03B0: 01 A0 07        LD      BC,$07A0            ; 
03B3: CD 70 02        CALL    $0270               ; {code.SubtractFromMemory}
03B6: DA CE 03        JP      C,$03CE             ; {code.L03CE}
03B9: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
03BC: CA EB 03        JP      Z,$03EB             ; {code.L03EB}
03BF: 01 60 0B        LD      BC,$0B60            ; 
03C2: CD 70 02        CALL    $0270               ; {code.SubtractFromMemory}
03C5: DA CE 03        JP      C,$03CE             ; {code.L03CE}
03C8: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
03CB: CA E2 03        JP      Z,$03E2             ; {code.L03E2}
;
L03CE:
03CE: CD 73 01        CALL    $0173               ; {code.GetPlayerInputsForDemo}
03D1: 21 A0 43        LD      HL,$43A0            ; {+ram.IN0Current}
03D4: 7E              LD      A,(HL)              ; 
03D5: E6 01           AND     $01                 ; mask out real button presses, but leave the coin event.
03D7: B0              OR      B                   ; feed the IN0Current with movement data
03D8: 77              LD      (HL),A              ; for the game demo.
03D9: C3 00 04        JP      $0400               ; {code.GameStateMachine}
; Ghost code bytes from an older version.
; The code was probably shortened at this point during development and the following bytes were not specifically deleted.
03DC: C3 00 04        JP      $0400               ; {code.GameStateMachine}
;
03DF: FF FF FF

;*****************************************************************************
;* Changing the game demo level at attract mode.
;*****************************************************************************
L03E2:
03E2: 01 08 01        LD      BC,$0108            ; Next interval game state is 1, set LevelAndRound to 1st round, level 8 (mothership wave)
03E5: 11 00 10        LD      DE,$1000            ; set AliensLeft to 1 and BirdsLeft to 0 ?
03E8: C3 F1 03        JP      $03F1               ; {code.L03F1}

;*****************************************************************************
;* Changing the game demo level at attract mode.
;*****************************************************************************
L03EB:
03EB: 01 04 01        LD      BC,$0104            ; 
03EE: 11 08 00        LD      DE,$0008            ; 
L03F1:
03F1: 21 A4 43        LD      HL,$43A4            ; {+ram.GameState} Next interval game state ...
03F4: 70              LD      (HL),B              ; ... is 1 (flashing of score)
03F5: 2E B8           LD      L,$B8               ; 
03F7: 71              LD      (HL),C              ; set LevelAndRound to 1st round, level 4 (blue birds wave)
03F8: 2E BA           LD      L,$BA               ; 
03FA: 72              LD      (HL),D              ; set AliensLeft to 0
03FB: 2C              INC     L                   ; 
03FC: 73              LD      (HL),E              ; set BirdsLeft to 8
03FD: C9              RET                         ; 
;
03FE: FF FF

;*****************************************************************************
;* Game state machine.
;* Jump to function by number in GameState.
;*****************************************************************************
GameStateMachine:
0400: 21 0E 04        LD      HL,$040E            ; {+code.T040E} Jump table
0403: 3A A4 43        LD      A,($43A4)           ; {ram.GameState}
0406: 07              RLCA                        ; *2
0407: 85              ADD     A,L                 ; Offset ...
0408: 6F              LD      L,A                 ; ... into the table
0409: 7E              LD      A,(HL)              ; MSB of destination
040A: 2C              INC     L                   ; Get the
040B: 6E              LD      L,(HL)              ; ... LSB of destination
040C: 67              LD      H,A                 ; Now point to function
040D: E9              JP      (HL)                ; Jump to function

; Notice these addresses are MSB:LSB (backwards from the processor's endianness)
T040E:
040E: 04 30       ; game state 0: called once at 'new game start'
0410: 04 AC       ; game state 1: called for each frame during 'flashing of score1 or 2'
0412: 05 15       ; game state 2: called once for initialization of game and level data
0414: 08 00       ; game state 3: called for each frame of normal game play
0416: 0A EA       ; game state 4: called for each frame of 'player ship partikel explosion'
0418: 0B 60       ; game state 5: called for each frame during 'GAME OVER' text
041A: 24 00       ; game state 6: called for each frame during 'mother ship partikel explosion'
041C: 24 4C       ; game state 7: called for each frame during 'mother ship score display'

;*****************************************************************************
;* Set lower bits of video register,
;* for the color palette, memory bank, and the screen flipping at cocktail mode.
;*****************************************************************************
SetBitsVideoRegister:
041E: 3A A3 43        LD      A,($43A3)           ; {ram.GameAndDemoOrSplash}
0421: E6 01           AND     $01                 ; mask out 0000_0001 for 'memory bank'
0423: 47              LD      B,A                 ; 
0424: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
0427: E6 02           AND     $02                 ; masc out 0000_0010 for 'color palette'
0429: B0              OR      B                   ; set the bits at...
042A: 32 00 50        LD      ($5000),A           ; {hard.videoRegister} 50xx video register
042D: C9              RET                         ; 
; Ghost code bytes from an older version.
; The code was probably shortened at this point during development and the following bytes were not specifically deleted.
042E: 18 05           JR      $435                ; {}

;*****************************************************************************
;* Game state 0.
;* New game start.
;*****************************************************************************
L0430:
0430: 21 A4 43        LD      HL,$43A4            ; {+ram.GameState} Next interval game state ...
0433: 36 01           LD      (HL),$01            ; ... is 1 (flashing of score)
0435: 2C              INC     L                   ; 
0436: 36 80           LD      (HL),$80            ; Set value for CounterA5 (score flash time)
0438: 2E A3           LD      L,$A3               ; save the value of..
043A: 7E              LD      A,(HL)              ; .. GameAndDemoOrSplash
043B: 36 00           LD      (HL),$00            ; set it to game demo / game play
043D: FE 02           CP      $02                 ; 
043F: C8              RET     Z                   ; return if it was 'Intro splash' before.
0440: 77              LD      (HL),A              ; set GameAndDemoOrSplash to 'Game and demo for player 1'
0441: 2D              DEC     L                   ; 
0442: 7E              LD      A,(HL)              ; get GameOrAttract
0443: FE 01           CP      $01                 ; 
0445: C8              RET     Z                   ; return if 'One player game mode'
0446: 2C              INC     L                   ; 
0447: 7E              LD      A,(HL)              ; get GameAndDemoOrSplash
0448: A7              AND     A                   ; updates the zero flag
0449: CA A0 04        JP      Z,$04A0             ; {code.L04A0} if 'Game and demo'
044C: 2E 90           LD      L,$90               ; 
044E: 7E              LD      A,(HL)              ; get Player1Lives
044F: A7              AND     A                   ; updates the zero flag
0450: C8              RET     Z                   ; return if no lives left.
0451: 2E A3           LD      L,$A3               ; 
0453: 36 00           LD      (HL),$00            ; set GameAndDemoOrSplash to 'Game and demo for player 1'
0455: 01 00 01        LD      BC,$0100            ; from bank 1 to bank 0
0458: CD 60 04        CALL    $0460               ; {code.CopyMemoryBank} to toggle the player
045B: C9              RET                         ; 

045C: FF FF FF FF

;*****************************************************************************
;* Copy memory bank to bank
;* B=from bank number, C=to bank number
;* Starts at 4320
;*****************************************************************************
CopyMemoryBank:
0460: 21 00 50        LD      HL,$5000            ; 50xx video register
0463: 11 20 43        LD      DE,$4320            ; {+ram.ForegroundScreen+320} 1st row 1st line
;
L0466:
0466: 70              LD      (HL),B              ; 
0467: 1A              LD      A,(DE)              ; 
0468: 71              LD      (HL),C              ; 
0469: 12              LD      (DE),A              ; 
046A: 1C              INC     E                   ; 
046B: 7B              LD      A,E                 ; 
046C: E6 03           AND     $03                 ; 0000_0011
046E: C2 66 04        JP      NZ,$0466            ; {code.L0466}
0471: 7B              LD      A,E                 ; 
0472: E6 F0           AND     $F0                 ; 1111_0000
0474: D6 20           SUB     $20                 ; 
0476: 5F              LD      E,A                 ; 
0477: D2 66 04        JP      NC,$0466            ; {code.L0466}
047A: 15              DEC     D                   ; 
047B: 7A              LD      A,D                 ; 
047C: FE 3F           CP      $3F                 ; 
047E: C2 66 04        JP      NZ,$0466            ; {code.L0466}
0481: 11 80 43        LD      DE,$4380            ; {+ram.M4380}
;
L0484:
0484: 70              LD      (HL),B              ; 
0485: 1A              LD      A,(DE)              ; 
0486: 71              LD      (HL),C              ; 
0487: 12              LD      (DE),A              ; 
0488: 1C              INC     E                   ; 
0489: 7B              LD      A,E                 ; 
048A: FE B8           CP      $B8                 ; 
048C: C2 84 04        JP      NZ,$0484            ; {code.L0484}
048F: 11 C0 4B        LD      DE,$4BC0            ; {!+ram.B4BC0}
;
L0492:
0492: 70              LD      (HL),B              ; 
0493: 1A              LD      A,(DE)              ; 
0494: 71              LD      (HL),C              ; 
0495: 12              LD      (DE),A              ; 
0496: 1C              INC     E                   ; 
0497: 7B              LD      A,E                 ; 
0498: FE 00           CP      $00                 ; 
049A: C2 92 04        JP      NZ,$0492            ; {code.L0492}
049D: C9              RET                         ; 

049E: FF FF

;*****************************************************************************
;* Changing the player at attract mode.
;*****************************************************************************
L04A0:
04A0: 2E A3           LD      L,$A3               ; set GameAndDemoOrSplash
04A2: 36 01           LD      (HL),$01            ; to 'Game for player 2'
04A4: 01 01 00        LD      BC,$0001            ; from bank 0 to bank 1
04A7: CD 60 04        CALL    $0460               ; {code.CopyMemoryBank} to toggle the player
04AA: C9              RET                         ; 
; 
04AB: FF

;*****************************************************************************
;* Game state 1.
;* Flashing of score1 or 2.
;*****************************************************************************
L04AC:
04AC: 21 A5 43        LD      HL,$43A5            ; {+ram.CounterA5}
04AF: 35              DEC     (HL)                ; decrement counter
04B0: 7E              LD      A,(HL)              ; save value
04B1: 2D              DEC     L                   ; HL=A3A4 next game state ..
04B2: 36 02           LD      (HL),$02            ; .. is 2
04B4: A7              AND     A                   ; ret if ..
04B5: C8              RET     Z                   ; counter 0
04B6: 36 01           LD      (HL),$01            ; set game state to 1
04B8: FE 7F           CP      $7F                 ; 0111_1111
04BA: CA F0 07        JP      Z,$07F0             ; {code.L07F0}
04BD: 2E 9A           LD      L,$9A               ; 
04BF: 36 00           LD      (HL),$00            ; reset Counter9A MSB
04C1: 2C              INC     L                   ; and ..
04C2: 36 00           LD      (HL),$00            ; LSB
04C4: E6 08           AND     $08                 ; 0000_1000
04C6: C2 E6 04        JP      NZ,$04E6            ; {code.L04E6}
04C9: CD E8 06        CALL    $06E8               ; {code.L06E8}
04CC: 00              NOP                         ; 
04CD: 21 A3 43        LD      HL,$43A3            ; {+ram.GameAndDemoOrSplash}
04D0: 7E              LD      A,(HL)              ; 
04D1: A7              AND     A                   ; updates the zero flag
04D2: 2E 83           LD      L,$83               ; LSB of Score1low adress
04D4: 11 61 42        LD      DE,$4261            ; screen ram addr. of lowest score digit player 1
04D7: CA DF 04        JP      Z,$04DF             ; {code.L04DF}
04DA: 2E 87           LD      L,$87               ; LSB of Score2low adress
04DC: 11 21 40        LD      DE,$4021            ; screen ram addr. of lowest score digit player 2
L04DF:
04DF: 06 06           LD      B,$06               ; number of digits to print
04E1: CD C4 00        CALL    $00C4               ; {code.PrintNumber}
04E4: C9              RET                         ; 

04E5: FF
;
L04E6:
04E6: 21 A3 43        LD      HL,$43A3            ; {+ram.GameAndDemoOrSplash}
04E9: 7E              LD      A,(HL)              ; 
04EA: A7              AND     A                   ; updates the zero flag
04EB: 11 61 42        LD      DE,$4261            ; screen ram addr. of lowest score digit player 1
04EE: CA F4 04        JP      Z,$04F4             ; {code.L04F4}
04F1: 11 21 40        LD      DE,$4021            ; screen ram addr. of lowest score digit player 2
L04F4:
04F4: 06 06           LD      B,$06               ; number of digits to delete
04F6: CD FB 04        CALL    $04FB               ; {code.L04FB}
04F9: C9              RET                         ; 

04FA: FF
;
L04FB:
04FB: 3E 00           LD      A,$00               ; delete ..
04FD: 12              LD      (DE),A              ; ..one digit
04FE: CD 10 02        CALL    $0210               ; {code.LeftOneColumn}
0501: 05              DEC     B                   ; decrement number of digits
0502: C2 FB 04        JP      NZ,$04FB            ; {code.L04FB} ..until
0505: C9              RET                         ; ..done

;*****************************************************************************
;* Clear $4392 to $4397 and
;* init start value list pointer for alien movement MSB $4394
;*****************************************************************************
L0506:
0506: 21 92 43        LD      HL,$4392            ; {+ram.M4392}
0509: 06 06           LD      B,$06               ; number of bytes to clear
050B: CD D8 05        CALL    $05D8               ; {code.ClearBbytesAtHL}
050E: 3A 50 4B        LD      A,($4B50)           ; {+ram.M4B50} get alien movement pattern table MSB
0511: 32 94 43        LD      ($4394),A           ; {+ram.M4394} save start value list pointer for alien movement MSB
0514: C9              RET                         ; 

;*****************************************************************************
;* Game state 2.
;* Initialization of game and level data.
;*****************************************************************************
L0515:
0515: CD 1E 04        CALL    $041E               ; {code.SetBitsVideoRegister} set color palette according to LevelAndRound
0518: 21 A4 43        LD      HL,$43A4            ; {+ram.GameState} Next interval game state ...
051B: 36 03           LD      (HL),$03            ; ... is 3 (normal game play)
051D: CD 80 05        CALL    $0580               ; {code.InitGlobalLevelData}
0520: CD 47 05        CALL    $0547               ; {code.InitPlayerDataStructure}
0523: CD A0 09        CALL    $09A0               ; {code.L09A0} get screen ram adress for player ship position
L0526:
0526: CD 32 05        CALL    $0532               ; {code.L0532} init alien data for a new level and round
0529: CD 6C 0A        CALL    $0A6C               ; {code.L0A6C} get screen ram adress for all aliens
052C: CD 06 05        CALL    $0506               ; {code.L0506} clear $4392 to $4397, init $4394
052F: C3 B0 32        JP      $32B0               ; {code.L32B0}

;*****************************************************************************
;* Init alien data for a new level and round
;*****************************************************************************
L0532:
0532: 21 50 4B        LD      HL,$4B50            ; {+ram.M4B50}
0535: 06 A0           LD      B,$A0               ; clear $4B50 to $4BEF
0537: CD D8 05        CALL    $05D8               ; {code.ClearBbytesAtHL}
053A: CD EC 05        CALL    $05EC               ; {code.InitAlienControlStates}
053D: CD 50 06        CALL    $0650               ; {code.L0650} copy init values for 16 aliens to $4B50-$4B6F
0540: CD 10 06        CALL    $0610               ; {code.InitAlienPositions} load alien screen coordinates (X,Y grid), for a new level and round
0543: C9              RET                         ; 

0544: FF FF FF

;*****************************************************************************
;* Copy 32 byte from $0560 to $43C0 Player and bullets data structure (grid)
;* and clear 32 bytes of player and bullets data structure (screen ram).
;*****************************************************************************
InitPlayerDataStructure:
0547: 21 60 05        LD      HL,$0560            ; {+code.T0560}
054A: 11 C0 43        LD      DE,$43C0            ; {+ram.PlayerState} base of data structure (grid)
054D: 06 20           LD      B,$20               ; 
054F: CD E0 05        CALL    $05E0               ; {code.CopyBbytesHLtoDE}
0552: 21 E0 43        LD      HL,$43E0            ; {+ram.OldPlayerShipMSB}
0555: 06 20           LD      B,$20               ; 
0557: CD D8 05        CALL    $05D8               ; {code.ClearBbytesAtHL}
055A: C9              RET                         ; 

055B: FF FF FF FF FF

; Data copied to $43C0-$43DF
; Default values for player and bullets data structure (grid).
T0560:
0560: 0C 10 64 D8       ; PlayerState, PlayerShape, PlayerShipX, PlayerShipY
0564: 00 50 00 D0       ; PlayerBulletState, PlayerBulletShape, PlayerBulletX, PlayerBulletY
0568: 00 50 00 D0       ; AbovePlayerBulletState, AbovePlayerBulletShape, AbovePlayerBulletX, AbovePlayerBulletY
056C: 00 58 00 20       ; EnemyBullet0State, EnemyBullet0Shape, EnemyBullet0X, EnemyBullet0Y
0570: 00 58 00 20       ; EnemyBullet1State, EnemyBullet1Shape, EnemyBullet1X, EnemyBullet1Y
0574: 00 58 00 20       ; EnemyBullet2State, EnemyBullet2Shape, EnemyBullet2X, EnemyBullet2Y
0578: 00 58 00 20       ; EnemyBullet3State, EnemyBullet3Shape, EnemyBullet3X, EnemyBullet3Y
057C: 00 58 00 20       ; EnemyBullet4State, EnemyBullet4Shape, EnemyBullet4X, EnemyBullet4Y

;*****************************************************************************
;* Init of global level data, dependent on level and round.
;*****************************************************************************
InitGlobalLevelData:
0580: 21 98 05        LD      HL,$0598            ; {+code.T0598}
0583: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
0586: E6 0F           AND     $0F                 ; 0000_1111
0588: 85              ADD     A,L                 ; 
0589: 6F              LD      L,A                 ; 
058A: 6E              LD      L,(HL)              ; 
058B: 26 05           LD      H,$05               ; 
058D: 11 AB 43        LD      DE,$43AB            ; {+ram.M43AB}
0590: 06 0C           LD      B,$0C               ; number of bytes to copy
0592: CD E0 05        CALL    $05E0               ; {code.CopyBbytesHLtoDE}
0595: C9              RET                         ; 

0596: FF FF

; Table for the global level data, over game levels.
; Bit0 - bit3 of $43B8 is the table index.
; Data will be fetched two times. Once before and once after the 'spiral fill' animation.
T0598:
0598: A8 A8     ;init values for 1st alien wave (pointer to $05A8, $05A8)
059A: C0 C0     ;init values for 2st alien wave (pointer to $05C0, $05C0)
059C: A8 A8     ;init values for blue birds wave (pointer to $05A8, $05A8)
059E: A8 A8     ;init values for pink birds wave (pointer to $05A8, $05A8)
05A0: B4 CC     ;init values for mothership wave (pointer to $05B4, $05CC)
05A2: B4 B4     ;init values for mothership wave (pointer to $05B4, $05B4)
05A4: A8 A8     ;not used? pointer to $05A8, $05A8
05A6: A8 A8     ;not used? pointer to $05A8, $05A8
;
; e.g.:counter values, timer values, T1C00, T1D00, T1F00, ..
; Data copied to $43AB-$43B6
T05A8:
05A8: 80 7F 00 00 40 3F 00 1C 00 FF FF FF
;
T05B4:
05B4: 60 5F 01 02 30 2F 00 1C 00 C0 FF FF
;
T05C0:
05C0: 80 7F 03 04 40 3F 00 1F 00 A0 FF FF
;
T05CC:
05CC: 60 60 05 06 50 30 00 1D 00 48 FF FF

;*****************************************************************************
;* Clears B memories starting at HL.
;*****************************************************************************
ClearBbytesAtHL:
05D8: AF              XOR     A                   ; A=0
L05D9:
05D9: 77              LD      (HL),A              ; store
05DA: 23              INC     HL                  ; next
05DB: 05              DEC     B                   ; decrease counter.
05DC: C2 D9 05        JP      NZ,$05D9            ; {code.L05D9}
05DF: C9              RET                         ; 

;*****************************************************************************
;* Copy number of bytes (B register) from DE to HL.
;*****************************************************************************
CopyBbytesHLtoDE:
05E0: 7E              LD      A,(HL)              ; Copy to HL ...
05E1: 12              LD      (DE),A              ; ... from DE
05E2: 23              INC     HL                  ; Next destination
05E3: 13              INC     DE                  ; Next source
05E4: 05              DEC     B                   ; All done?
05E5: C2 E0 05        JP      NZ,$05E0            ; {code.CopyBbytesHLtoDE} no ... keep going
05E8: C9              RET                         ; Out

05E9: FF FF FF

;*****************************************************************************
;* Init all alien control states for a given level and round.
;*****************************************************************************
InitAlienControlStates:
05EC: 21 00 15        LD      HL,$1500            ; {+code.T1500}
05EF: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
05F2: E6 0F           AND     $0F                 ; 0000_1111
05F4: 07              RLCA                        ; Multiply by 2
05F5: 85              ADD     A,L                 ; 
05F6: 6F              LD      L,A                 ; 
05F7: 56              LD      D,(HL)              ; 
05F8: 23              INC     HL                  ; 
05F9: 5E              LD      E,(HL)              ; 
;
L05FA:
05FA: 21 70 4B        LD      HL,$4B70            ; {+ram.M4B70}
05FD: 3A BA 43        LD      A,($43BA)           ; {ram.AliensLeft}
0600: 47              LD      B,A                 ; 
0601: A7              AND     A                   ; updates the zero flag
0602: C8              RET     Z                   ; if no AliensLeft
;
L0603:
0603: 72              LD      (HL),D              ; set control state A
0604: 2C              INC     L                   ; 
0605: 73              LD      (HL),E              ; set control state B
0606: 2C              INC     L                   ; 
0607: 2C              INC     L                   ; 
0608: 2C              INC     L                   ; 
0609: 05              DEC     B                   ; number of aliens left
060A: C2 03 06        JP      NZ,$0603            ; {code.L0603}
060D: C9              RET                         ; 

060E: FF FF

;*****************************************************************************
;* Load alien screen coordinates for a given level and round to $4B70 - $4BAF.
;*****************************************************************************
InitAlienPositions:
0610: 21 3A 06        LD      HL,$063A            ; {+code.T063A}
0613: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
0616: 0F              RRCA                        ; 
0617: E6 0F           AND     $0F                 ; mask out 0000_1111
0619: 85              ADD     A,L                 ; 
061A: 6F              LD      L,A                 ; 
061B: 00              NOP                         ; Old command removed or space for a future replace patch
061C: 00              NOP                         ; ..
061D: 00              NOP                         ; ..
061E: 6E              LD      L,(HL)              ; 
061F: 26 15           LD      H,$15               ; MSB for T1540-T15E0
0621: 11 72 4B        LD      DE,$4B72            ; {+ram.M4B72}
0624: 3A BA 43        LD      A,($43BA)           ; {ram.AliensLeft}
0627: 47              LD      B,A                 ; 
0628: A7              AND     A                   ; updates the zero flag
0629: C8              RET     Z                   ; if no AliensLeft
;
L062A:
062A: 7E              LD      A,(HL)              ; get value from table
062B: 12              LD      (DE),A              ; save to alien screen coordinate
062C: 23              INC     HL                  ; 
062D: 13              INC     DE                  ; 
062E: 7E              LD      A,(HL)              ; 
062F: 12              LD      (DE),A              ; 
0630: 23              INC     HL                  ; 
0631: 13              INC     DE                  ; 
0632: 13              INC     DE                  ; 
0633: 13              INC     DE                  ; 
0634: 05              DEC     B                   ; 
0635: C2 2A 06        JP      NZ,$062A            ; {code.L062A} loop for all AliensLeft
0638: C9              RET                         ; 

0639: FF
; Init data for 1st game round.
; LSB's for T1560, T1540, T15E0.
T063A:
063A: 60 40 E0 E0 E0 E0 FF FF 
; Init data for 2nd game round.
; LSB's for T15C0, T15A0, T1580.
0642: C0 A0 80 80 80 80 FF FF 
;
064A: FF FF FF FF FF FF 

;*****************************************************************************
;* Copy init values for 16 aliens to $4B50-$4B6F (Pointer to alien movement pattern)
;*****************************************************************************
L0650:
0650: 21 20 15        LD      HL,$1520            ; {+code.T1520}
0653: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
0656: E6 0F           AND     $0F                 ; mask out 0000_1111
0658: 07              RLCA                        ; Multiply by 2
0659: 85              ADD     A,L                 ; 
065A: 6F              LD      L,A                 ; 
065B: 56              LD      D,(HL)              ; 
065C: 23              INC     HL                  ; 
065D: 5E              LD      E,(HL)              ; 
065E: 21 50 4B        LD      HL,$4B50            ; {+ram.M4B50}
0661: 3A BA 43        LD      A,($43BA)           ; {ram.AliensLeft}
0664: 47              LD      B,A                 ; 
0665: A7              AND     A                   ; updates the zero flag
0666: C8              RET     Z                   ; if no AliensLeft
L0667:
0667: 72              LD      (HL),D              ; 
0668: 2C              INC     L                   ; 
0669: 73              LD      (HL),E              ; 
066A: 2C              INC     L                   ; 
066B: 05              DEC     B                   ; 
066C: C2 67 06        JP      NZ,$0667            ; {code.L0667} loop for all AliensLeft
066F: C9              RET                         ; 

;not used
0670: 21 B1 43        LD      HL,$43B1            ; {+ram.M43B1}
0673: 46              LD      B,(HL)              
0674: 2E B9           LD      L,$B9               
0676: 4E              LD      C,(HL)              ; get CounterB9 (free running 8 bit backwards) counter value
0677: 79              LD      A,C                 
0678: 90              SUB     B                   
0679: 77              LD      (HL),A              

;*****************************************************************************
;* Scroll down the background screen one pixel.
;*****************************************************************************
StarsScrollDown:
067A: 21 B9 43        LD      HL,$43B9            ; {+ram.CounterB9}
067D: 7E              LD      A,(HL)              ; 
067E: 35              DEC     (HL)                ; decrement the backwards counter
067F: 32 00 58        LD      ($5800),A           ; {hard.scrollRegister} 58xx scroll register
0682: E6 07           AND     $07                 ; mask out 0000_0111
0684: C0              RET     NZ                  ; continue after 8 pixels...
; Fill the background with stars or mothership.
0685: 01 47 20        LD      BC,$2047            ; 
0688: 11 21 4B        LD      DE,$4B21            ; get character from the background screen (1st row, 2nd line)
068B: 7E              LD      A,(HL)              ; get $43B9 free running 8 bit backwards counter value
068C: 0F              RRCA                        ; 
068D: 0F              RRCA                        ; 
068E: 0F              RRCA                        ; 
068F: E6 1F           AND     $1F                 ; mask out 0001_1111
0691: 83              ADD     A,E                 ; 
0692: 5F              LD      E,A                 ; 
0693: 2E B2           LD      L,$B2               ; 
0695: 7E              LD      A,(HL)              ; get $43B2 (MSB of T1C00 or T1D00 or T1F00)
0696: 2C              INC     L                   ; 
0697: 6E              LD      L,(HL)              ; get $43B3 (LSB of T1C00 or T1D00 or T1F00)
0698: 67              LD      H,A                 ; 
L0699:
0699: 7E              LD      A,(HL)              ; 
069A: 12              LD      (DE),A              ; to background screen
069B: 2C              INC     L                   ; 
069C: 7B              LD      A,E                 ; 
069D: 90              SUB     B                   ; 
069E: 5F              LD      E,A                 ; 
069F: D2 99 06        JP      NC,$0699            ; {code.L0699}
06A2: 15              DEC     D                   ; 
06A3: 7A              LD      A,D                 ; 
06A4: B9              CP      C                   ; 
06A5: C2 99 06        JP      NZ,$0699            ; {code.L0699}
06A8: 7D              LD      A,L                 ; 
06A9: 32 B3 43        LD      ($43B3),A           ; {ram.M43B3}
06AC: C9              RET                         ; 

06AD: FF FF FF

;*****************************************************************************
;* Fill the background with (2x2) planets.
;*****************************************************************************
AddPlanetsToBackground:
06B0: 21 AB 43        LD      HL,$43AB            ; {+ram.M43AB} counter value for (2x2) planets
06B3: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9}
06B6: 4F              LD      C,A                 ; 
06B7: BE              CP      (HL)                ; 
06B8: C0              RET     NZ                  ; 
;
06B9: 7E              LD      A,(HL)              ; 
06BA: 2C              INC     L                   ; 
06BB: 86              ADD     A,(HL)              ; 
06BC: 2D              DEC     L                   ; 
06BD: 77              LD      (HL),A              ; 
06BE: 2C              INC     L                   ; 
06BF: 2C              INC     L                   ; 
06C0: 34              INC     (HL)                ; 
06C1: 46              LD      B,(HL)              ; 
06C2: 2C              INC     L                   ; 
06C3: 34              INC     (HL)                ; 
06C4: 7E              LD      A,(HL)              ; 
06C5: 21 20 1E        LD      HL,$1E20            ; {+code.T1E20} MSB's of screen ram for planets
06C8: E6 1F           AND     $1F                 ; 0001_1111
06CA: 85              ADD     A,L                 ; 
06CB: 6F              LD      L,A                 ; 
06CC: 56              LD      D,(HL)              ; 
06CD: C6 20           ADD     $20                 ; 
06CF: 6F              LD      L,A                 ; 
06D0: 5E              LD      E,(HL)              ; 
06D1: 79              LD      A,C                 ; 
06D2: 0F              RRCA                        ; 
06D3: 0F              RRCA                        ; 
06D4: 0F              RRCA                        ; 
06D5: E6 1E           AND     $1E                 ; 0001_1111
06D7: 83              ADD     A,E                 ; 
06D8: C6 02           ADD     $02                 ; 
06DA: 5F              LD      E,A                 ; 
06DB: 21 60 1E        LD      HL,$1E60            ; {+code.T1E60} LSB's of screen ram for planets
06DE: 78              LD      A,B                 ; 
06DF: E6 1F           AND     $1F                 ; 0001_1111
06E1: 85              ADD     A,L                 ; 
06E2: 6F              LD      L,A                 ; 
06E3: 6E              LD      L,(HL)              ; 
06E4: CD DC 07        CALL    $07DC               ; {code.L07DC} draw the characters at background
06E7: C9              RET                         ; 

;*****************************************************************************
;* Print score column
;*****************************************************************************
L06E8:
06E8: 21 00 18        LD      HL,$1800            ; {+code.T1800} base addr. table for 'screen ram adresses and static texts'
06EB: 0E 01           LD      C,$01               ; 1 column (rotated to 1 row)
06ED: C3 D0 01        JP      $01D0               ; {code.PrintTextLines}

;*****************************************************************************
;* Update scroll register and fill background
;*****************************************************************************
L06F0:
06F0: CD 7A 06        CALL    $067A               ; {code.StarsScrollDown}
06F3: CD 40 20        CALL    $2040               ; {code.AddGalaxiesToBackground}
06F6: C3 B0 06        JP      $06B0               ; {code.AddPlanetsToBackground}
;
06F9: FF FF FF FF FF FF FF

;*****************************************************************************
;* Controller for player data structure.
;* Handles: PlayerState, OldPlayerShipMSB, PlayerBulletState, PlayerBulletMSB, AbovePlayerBulletState, $43E8
;*****************************************************************************
PlayerDataController:
0700: 01 C0 43        LD      BC,$43C0            ; {+ram.PlayerState} Player data structure (grid)
0703: 11 E0 43        LD      DE,$43E0            ; {+ram.OldPlayerShipMSB} Player data structure (screen ram)
L0706:
0706: CD 18 07        CALL    $0718               ; {code.UpdateScreenObjects}
0709: 79              LD      A,C                 ; 
070A: C6 04           ADD     $04                 ; 
070C: 4F              LD      C,A                 ; 
070D: C6 20           ADD     $20                 ; 
070F: 5F              LD      E,A                 ; 
0710: 50              LD      D,B                 ; 
0711: FE EC           CP      $EC                 ; 
0713: C2 06 07        JP      NZ,$0706            ; {code.L0706} loop until $43EC
0716: C9              RET                         ; 

; not used
0717: C9              RET                         

;*****************************************************************************
;* Draw or delete screen objects dep. on control state of player, alien and bullet.
;*****************************************************************************
UpdateScreenObjects:
0718: CD 20 07        CALL    $0720               ; {code.Bit4Controller} for deleting screen objects
071B: C3 40 07        JP      $0740               ; {code.Bit3Controller} for drawing screen objects

; not used
071E: E6 EF           AND     $EF                 

;*****************************************************************************
;* Handles the bit4 actions for deleting screen objects.
;*****************************************************************************
Bit4Controller:
0720: 0A              LD      A,(BC)              ; get value from data structure (grid)
0721: 67              LD      H,A                 ; save the bits
0722: E6 10           AND     $10                 ; mask out 0001_0000 (bit4 of control state A)
0724: C8              RET     Z                   ; ret if bit not set.
0725: 7C              LD      A,H                 ; restore the bits
0726: E6 EF           AND     $EF                 ; mask out 1110_1111
0728: 02              LD      (BC),A              ; save to control state A
0729: 07              RLCA                        ; Multiply by 8 ..
072A: 07              RLCA                        ; ..
072B: 07              RLCA                        ; ..
072C: E6 07           AND     $07                 ; mask out 0000_0111
072E: C6 38           ADD     $38                 ; add to base for jump table
0730: 6F              LD      L,A                 ; 
0731: 26 07           LD      H,$07               ; MSB for jump table
0733: 6E              LD      L,(HL)              ; 
0734: E9              JP      (HL)                ; jump to control function

; LSB jump table:
;.....not used
;........not used
;...........not used
;..............0763..................control state A: 0001_xxxx...Delete 1x1 screen objects.
;.................0779...............control state A: 0011_xxxx...Delete 2x1 screen objects.
;....................not used
;.......................079E.........control state A: 0111_xxxx...Delete 1x2 screen objects.
;..........................07BE......control state A: 1001_xxxx...Delete 2x2 screen objects.
T0735:
0735: 6C FF 8A 63 79 FF 9E BE
;
073D: FF FF FF

;*****************************************************************************
;* Handles the bit3 actions for drawing screen objects.
;*****************************************************************************
Bit3Controller:
0740: 0A              LD      A,(BC)              ; get value from data structure (grid)
0741: 67              LD      H,A                 ; save it
0742: E6 08           AND     $08                 ; mask out 0000_1000 (bit3 of control state A)
0744: C8              RET     Z                   ; ret if bit not set.
0745: 7C              LD      A,H                 ; restore the bits
0746: E6 07           AND     $07                 ; mask out 0000_0111
0748: 67              LD      H,A                 ; save it
0749: 0F              RRCA                        ; Divide by 8 ..
074A: 0F              RRCA                        ; ..
074B: 0F              RRCA                        ; ..
074C: B4              OR      H                   ; add original bits
074D: F6 18           OR      $18                 ; set 0001_1000 flag
074F: 02              LD      (BC),A              ; set the bits at control state A
0750: 03              INC     BC                  ; go to control state B
0751: 7C              LD      A,H                 ; 
0752: C6 5B           ADD     $5B                 ; add to base for jump table
0754: 6F              LD      L,A                 ; 
0755: 26 07           LD      H,$07               ; MSB for jump table
0757: 6E              LD      L,(HL)              ; 
0758: E9              JP      (HL)                ; jump to control function

; LSB jump table:
;.....not used
;........not used
;...........076D.....................control state A: xxxx_1000...Draw 1x1 screen objects.
;..............0788..................control state A: xxxx_1001...Draw 2x1 screen objects.
;.................not used
;....................07AA............control state A: xxxx_1011...Draw 1x2 screen objects.
;.......................07D2.........control state A: xxxx_1100...Draw 2x2 screen objects.
;..........................not used
T0759:
0759: 5E 0A 6D 88 FF AA D2 FF
;
0761: FF FF

;*****************************************************************************
;* Bit4 control function 63:
;* If control state A: 0001_xxxx
;* Delete 1x1 screen objects (bullet, alien).
;*****************************************************************************
L0763:
0763: EB              EX      DE,HL               ; 
0764: 56              LD      D,(HL)              ; get screen ram adress MSB
0765: 23              INC     HL                  ; 
0766: 5E              LD      E,(HL)              ; get screen ram adress LSB
0767: 2B              DEC     HL                  ; restore pointer
0768: AF              XOR     A                   ; A=0
0769: 12              LD      (DE),A              ; delete at screen
076A: EB              EX      DE,HL               ; 
076B: C9              RET                         ; 
; not used
076C: EB              EX      DE,HL               

;*****************************************************************************
;* Bit3 control function 6D:
;* If control state A: xxxx_1000
;* Set alien control state B value to screen ram.
;* Draw 1x1 screen objects (used at 'fade in' animation).
;*****************************************************************************
L076D:
076D: EB              EX      DE,HL               ; 
076E: 23              INC     HL                  ; 
076F: 23              INC     HL                  ; 
0770: 56              LD      D,(HL)              ; get MSB screen ram adress of alien
0771: 23              INC     HL                  ; 
0772: 5E              LD      E,(HL)              ; get LSB screen ram adress of alien
0773: 0A              LD      A,(BC)              ; get alien control state B
0774: 12              LD      (DE),A              ; set at screen ram
0775: 0B              DEC     BC                  ; move to alien control state A
0776: C9              RET                         ; 
; not used
0777: 12              LD      (DE),A              
0778: 23              INC     HL                  

;*****************************************************************************
;* Bit4 control function 79:
;* If control state A: 0011_xxxx
;* Delete 2x1 screen objects (alien).
;*****************************************************************************
L0779:
0779: EB              EX      DE,HL               ; 
077A: 56              LD      D,(HL)              ; 
077B: 23              INC     HL                  ; 
077C: 5E              LD      E,(HL)              ; 
077D: 2B              DEC     HL                  ; restore pointer
077E: AF              XOR     A                   ; A=0
077F: 12              LD      (DE),A              ; delete at screen, left part
0780: CD 17 02        CALL    $0217               ; {code.RightOneColumn}
0783: AF              XOR     A                   ; A=0
0784: 12              LD      (DE),A              ; delete at screen, right part
0785: EB              EX      DE,HL               ; 
0786: C9              RET                         ; 
; not used
0787: 23              INC     HL                  

;*****************************************************************************
;* Bit3 control function 88:
;* If control state A: xxxx_1001
;* Map alien control state B to shape and draw it.
;* Draw 2x1 screen objects (alien).
;*****************************************************************************
L0788:
0788: EB              EX      DE,HL               ; 
0789: 23              INC     HL                  ; 
078A: 23              INC     HL                  ; 
078B: 56              LD      D,(HL)              ; 
078C: 23              INC     HL                  ; 
078D: 5E              LD      E,(HL)              ; 
078E: 0A              LD      A,(BC)              ; get alien control state B
078F: 6F              LD      L,A                 ; as offset for...
0790: 26 14           LD      H,$14               ; get T14xx alien character block shapes table
0792: 7E              LD      A,(HL)              ; 
0793: 12              LD      (DE),A              ; draw alien character left part
0794: 23              INC     HL                  ; next character
0795: CD 17 02        CALL    $0217               ; {code.RightOneColumn}
0798: 7E              LD      A,(HL)              ; 
0799: 12              LD      (DE),A              ; draw alien character right part
079A: 0B              DEC     BC                  ; 
079B: C9              RET                         ; 
;
079C: FF
; not used
079D: EB              EX      DE,HL               

;*****************************************************************************
;* Bit4 control function 9E:
;* If control state A: 0111_xxxx
;* Delete 1x2 screen objects (alien).
;*****************************************************************************
L079E:
079E: EB              EX      DE,HL               ; 
079F: 56              LD      D,(HL)              ; get MSB of screen ram
07A0: 23              INC     HL                  ; 
07A1: 5E              LD      E,(HL)              ; get LSB of screen ram
07A2: 2B              DEC     HL                  ; restore pointer
07A3: AF              XOR     A                   ; A=0
07A4: 12              LD      (DE),A              ; delete at screen, upper part
07A5: 13              INC     DE                  ; 
07A6: 12              LD      (DE),A              ; delete at screen, lower part
07A7: EB              EX      DE,HL               ; 
07A8: C9              RET                         ; 
;
07A9: FF

;*****************************************************************************
;* Bit3 control function AA:
;* If control state A: xxxx_1011
;* Draw 1x2 screen objects (alien).
;*****************************************************************************
L07AA:
07AA: EB              EX      DE,HL               ; 
07AB: 23              INC     HL                  ; 
07AC: 23              INC     HL                  ; 
07AD: 56              LD      D,(HL)              ; 
07AE: 23              INC     HL                  ; 
07AF: 5E              LD      E,(HL)              ; 
07B0: 0A              LD      A,(BC)              ; 
07B1: 6F              LD      L,A                 ; 
07B2: 26 14           LD      H,$14               ; get T1420 alien character block shapes table
07B4: 7E              LD      A,(HL)              ; 
07B5: 12              LD      (DE),A              ; draw upper part on screen
07B6: 23              INC     HL                  ; 
07B7: 13              INC     DE                  ; 
07B8: 7E              LD      A,(HL)              ; 
07B9: 12              LD      (DE),A              ; draw lower part on screen
07BA: 0B              DEC     BC                  ; 
07BB: C9              RET                         ; 
; not used
07BC: 23              INC     HL                  
07BD: 13              INC     DE                  

;*****************************************************************************
;* Bit4 control function BE:
;* If control state A: 1001_xxxx
;* Delete 2x2 screen objects (player ship, alien).
;*****************************************************************************
L07BE:
07BE: EB              EX      DE,HL               ; 
07BF: 56              LD      D,(HL)              ; 
07C0: 23              INC     HL                  ; 
07C1: 5E              LD      E,(HL)              ; 
07C2: 2B              DEC     HL                  ; 
07C3: AF              XOR     A                   ; A=0
07C4: 12              LD      (DE),A              ; delete upper left part
07C5: 13              INC     DE                  ; 
07C6: 12              LD      (DE),A              ; delete upper right part
07C7: CD 17 02        CALL    $0217               ; {code.RightOneColumn}
07CA: AF              XOR     A                   ; A=0
07CB: 12              LD      (DE),A              ; delete lower left part
07CC: 1B              DEC     DE                  ; 
07CD: 12              LD      (DE),A              ; delete lower right part
07CE: EB              EX      DE,HL               ; 
07CF: C9              RET                         ; 
; not used
07D0: CD 4C

;*****************************************************************************
;* Bit3 control function D2:
;* If control state A: xxxx_1100
;* Draw 2x2 screen objects (player ship, alien, planets).
;*****************************************************************************
L07D2:
07D2: EB              EX      DE,HL               ; 
07D3: 23              INC     HL                  ; 
07D4: 23              INC     HL                  ; 
07D5: 56              LD      D,(HL)              ; get MSB from player data structure (screen ram)
07D6: 23              INC     HL                  ; 
07D7: 5E              LD      E,(HL)              ; get LSB from player data structure (screen ram)
07D8: 0A              LD      A,(BC)              ; get value from player data structure (grid)
07D9: 6F              LD      L,A                 ; 
07DA: 26 14           LD      H,$14               ; get T14xx player ship character block shapes table
L07DC:
07DC: 7E              LD      A,(HL)              ; Entry point for general draw
07DD: 12              LD      (DE),A              ; draw upper left part
07DE: 23              INC     HL                  ; 
07DF: 13              INC     DE                  ; 
07E0: 7E              LD      A,(HL)              ; 
07E1: 12              LD      (DE),A              ; draw upper right part
07E2: 23              INC     HL                  ; 
07E3: 1B              DEC     DE                  ; 
07E4: CD 17 02        CALL    $0217               ; {code.RightOneColumn}
07E7: 7E              LD      A,(HL)              ; 
07E8: 12              LD      (DE),A              ; draw lower left part
07E9: 23              INC     HL                  ; 
07EA: 13              INC     DE                  ; 
07EB: 7E              LD      A,(HL)              ; 
07EC: 12              LD      (DE),A              ; draw lower right part
07ED: 0B              DEC     BC                  ; 
07EE: C9              RET                         ; 
;
07EF: FF

;*****************************************************************************
;* Reset scroll register for background at score flash
;*****************************************************************************
L07F0:
07F0: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9}
07F3: 32 00 58        LD      ($5800),A           ; {hard.scrollRegister} 58xx scroll register
07F6: CD 80 03        CALL    $0380               ; {code.ClearForeground}
07F9: C3 1E 04        JP      $041E               ; {code.SetBitsVideoRegister}
;
07FC: FF FF FF FF

;*****************************************************************************
;* Game state 3.
;* Normal game play.
;*****************************************************************************
L0800:
0800: 21 14 08        LD      HL,$0814            ; {+code.T0814}
0803: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound} bit0 - 3: game level, bit4 - 7: game round
0806: 07              RLCA                        ; Multiply by 2 to get a 2 byte offset
0807: E6 1E           AND     $1E                 ; mask out 0001_1110 game level
0809: 85              ADD     A,L                 ; add offset ...
080A: 6F              LD      L,A                 ; ... to base of table
080B: 7E              LD      A,(HL)              ; MSB of destination
080C: 2C              INC     L                   ; Get the
080D: 6E              LD      L,(HL)              ; ... LSB of destination
080E: 67              LD      H,A                 ; Now point to function
080F: E9              JP      (HL)                ; jump to corresponding function according to LevelAndRound.
;
0810: FF FF FF FF
;
T0814:
0814: 08 34       ;Game level 0: called for each frame during stars scrolling down and 'aliens fade in'
0816: 20 00       ;Game level 1: called for each frame during 'player alife' with aliens, after 'fade in'
0818: 08 34       ;Game level 2: called for each frame during stars scrolling down and 'aliens fade in'
081A: 20 00       ;Game level 3: called for each frame during 'player alife' with aliens, after 'fade in'
081C: 22 30       ;Game level 4: called for each frame during 'spiral fill'
081E: 34 00       ;Game level 5: called for each frame during birds level including 'fade in'
0820: 22 30       ;Game level 6: called for each frame during 'spiral fill'
0822: 34 00       ;Game level 7: called for each frame during birds level including 'fade in'
0824: 22 30       ;Game level 8: called for each frame during 'spiral fill'
0826: 22 B4       ;Game level 9: called for each frame during mothership 'fade in'
0828: 22 CA       ;Game level A: called for each frame during mothership and aliens 'fade in'
082A: 20 00       ;Game level B: called for each frame during 'player alife' with aliens and mothership, after 'fade in'
082C: 22 4C       ;not used in this context
082E: 22 4C       ;not used in this context
0830: 22 4C       ;not used in this context
0832: 22 4C       ;not used in this context

;*****************************************************************************
;* Game level 0 and 2:
;* Stars scrolling down and 'aliens fade in'
;*****************************************************************************
L0834:
0834: CD F0 06        CALL    $06F0               ; {code.L06F0} update scroll register and fill background
0837: 21 B4 43        LD      HL,$43B4            ; {+ram.CounterB4}
083A: 35              DEC     (HL)                ; decrement the counter
083B: 7E              LD      A,(HL)              ; 
083C: FE 15           CP      $15                 ; 
083E: D0              RET     NC                  ; 
083F: CD 5A 08        CALL    $085A               ; {code.GetAnimationChrs} for 'aliens fade in'
0842: CD FA 05        CALL    $05FA               ; {code.L05FA} init all alien control states
0845: CD 50 0A        CALL    $0A50               ; {code.AlienDataController}
L0848:
0848: 21 B4 43        LD      HL,$43B4            ; {+ram.CounterB4}
084B: 7E              LD      A,(HL)              ; 
084C: A7              AND     A                   ; updates the zero flag
084D: C0              RET     NZ                  ; if CounterB4 is 0.
084E: 2E B8           LD      L,$B8               ; LevelAndRound
0850: 34              INC     (HL)                ; increment game level
0851: 2E A4           LD      L,$A4               ; Next interval game state ...
0853: 36 02           LD      (HL),$02            ; .. is 2
0855: C9              RET                         ; 
;
0856: FF FF FF FF

;*****************************************************************************
;* The 'aliens fade in' animation sequence is:
;* 6C, 6D, 6E, 6F, 68, from foreground tiles.
;*****************************************************************************
GetAnimationChrs:
085A: 11 6C 08        LD      DE,$086C            ; 
085D: FE 11           CP      $11                 ; 
085F: D0              RET     NC                  ; 
0860: 1E 6D           LD      E,$6D               ; 
0862: FE 0D           CP      $0D                 ; 
0864: D0              RET     NC                  ; 
0865: 1E 6E           LD      E,$6E               ; 
0867: FE 09           CP      $09                 ; 
0869: D0              RET     NC                  ; 
086A: 1E 6F           LD      E,$6F               ; 
086C: FE 05           CP      $05                 ; 
086E: D0              RET     NC                  ; 
086F: 1E 68           LD      E,$68               ; 
0871: C9              RET                         ; 
;
0872: FF FF FF FF

;*****************************************************************************
; Updates the player ship, player bullet and the shield.
;*****************************************************************************
PlayerUpdate:
0876: CD 00 07        CALL    $0700               ; {code.PlayerDataController}
0879: CD 86 08        CALL    $0886               ; {code.L0886} copy current player data to old player data
087C: CD A0 08        CALL    $08A0               ; {code.L08A0} update player position, bullet and shield
087F: CD A0 09        CALL    $09A0               ; {code.L09A0} get screen ram adress for player ship position
0882: CD 7A 09        CALL    $097A               ; {code.L097A} map player ship position to $439E $439F
0885: C9              RET                         ; 

;*****************************************************************************
; Copy current player data to old player data.
;*****************************************************************************
L0886:
0886: 21 EB 43        LD      HL,$43EB            ; {+ram.M43EB}
0889: 06 03           LD      B,$03               ; 
L088B:
088B: 56              LD      D,(HL)              ; 
088C: 2B              DEC     HL                  ; 
088D: 5E              LD      E,(HL)              ; 
088E: 2B              DEC     HL                  ; 
088F: 72              LD      (HL),D              ; 
0890: 2B              DEC     HL                  ; 
0891: 73              LD      (HL),E              ; 
0892: 2B              DEC     HL                  ; 
0893: 05              DEC     B                   ; 
0894: C2 8B 08        JP      NZ,$088B            ; {code.L088B}
0897: C9              RET                         ; 
;
0898: FF FF FF FF FF FF FF FF

;*****************************************************************************
;* Update player position, bullet and shield
;*****************************************************************************
L08A0:
08A0: CD C4 08        CALL    $08C4               ; {code.MovePlayer}
08A3: 21 C4 43        LD      HL,$43C4            ; {+ram.PlayerBulletState}
08A6: CD 30 09        CALL    $0930               ; {code.L0930} get the assigned player bullet tile if fire button was pressed
08A9: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
08AC: E6 0F           AND     $0F                 ; 0000_1111
08AE: FE 03           CP      $03                 ; 
08B0: C0              RET     NZ                  ; return if not game level 3 (2nd alien wave)
08B1: 21 C8 43        LD      HL,$43C8            ; {+ram.AbovePlayerBulletState}
08B4: CD 30 09        CALL    $0930               ; {code.L0930} get the assigned player bullet tile if fire button was pressed
08B7: C9              RET                         ; 
;
08B8: FF FF FF FF FF FF FF FF
08C0: FF FF FF FF

;*****************************************************************************
;* Player ship, shield and bullets handler.
;*****************************************************************************
MovePlayer:
08C4: 21 C0 43        LD      HL,$43C0            ; {+ram.PlayerState}
08C7: 7E              LD      A,(HL)              ; 
08C8: E6 08           AND     $08                 ; mask out 0000_1000
08CA: CA A0 0A        JP      Z,$0AA0             ; {code.DrawShields} Draw shields
08CD: 2E A6           LD      L,$A6               ; 
08CF: 7E              LD      A,(HL)              ; get ShieldCount
08D0: A7              AND     A                   ; updates the zero flag
08D1: C2 EA 08        JP      NZ,$08EA            ; {code.L08EA} if ShieldCount not 0.
08D4: 06 80           LD      B,$80               ; 1000_0000 (bit7='shield')
08D6: CD BB 00        CALL    $00BB               ; {code.CheckInputBits}
08D9: CA EB 08        JP      Z,$08EB             ; {code.L08EB}
08DC: 2E 62           LD      L,$62               ; 
08DE: 36 40           LD      (HL),$40            ; set bit6 at $4362
08E0: 2E C0           LD      L,$C0               ; 
08E2: 7E              LD      A,(HL)              ; get $43C0 PlayerState
08E3: E6 F7           AND     $F7                 ; mask out 1111_0111
08E5: 77              LD      (HL),A              ; 
08E6: 2E A6           LD      L,$A6               ; ShieldCount
08E8: 36 FF           LD      (HL),$FF            ; 
L08EA:
08EA: 35              DEC     (HL)                ; decrement ShieldCount
L08EB:
08EB: 2E C2           LD      L,$C2               ; LSB of $43C2 PlayerShipX
08ED: CD 00 09        CALL    $0900               ; {code.L0900} Update the player ship x coordinate.
08F0: 01 00 16        LD      BC,$1600            ; {+code.T1600}
08F3: C3 26 09        JP      $0926               ; {code.L0926} get player ship animation frame values, mapped with T1600/T1620
;
08F6: FF FF FF FF FF FF FF FF FF FF

;*****************************************************************************
;* Update the player ship x coordinate.
;*****************************************************************************
L0900:
0900: 3A A0 43        LD      A,($43A0)           ; {ram.IN0Current}
0903: 2F              CPL                         ; flip the current bits
0904: E6 60           AND     $60                 ; mask out 0110_0000
0906: C8              RET     Z                   ; if no button pressed
0907: E6 40           AND     $40                 ; mask out 0100_0000
0909: CA 17 09        JP      Z,$0917             ; {code.L0917}
090C: 7E              LD      A,(HL)              ; get $43C2 PlayerShipX
090D: FE 0D           CP      $0D                 ; 
090F: D8              RET     C                   ; if left boundary reached
0910: 35              DEC     (HL)                ; 'left' button: dec $43C2 PlayerShipX
0911: 3E FF           LD      A,$FF               ; 
0913: 32 60 43        LD      ($4360),A           ; {ram.PlayerMoved} set 'player moved' flag
0916: C9              RET                         ; 
L0917:
0917: 7E              LD      A,(HL)              ; get $43C2 PlayerShipX
0918: FE C0           CP      $C0                 ; 
091A: D0              RET     NC                  ; if right boundary reached
091B: 34              INC     (HL)                ; 'right' button: inc $43C2 PlayerShipX
091C: 3E FF           LD      A,$FF               ; 
091E: 32 60 43        LD      ($4360),A           ; {ram.PlayerMoved} set 'player moved' flag
0921: C9              RET                         ; 
;
0922: FF FF FF FF

;*****************************************************************************
;* Get player ship animation frame values, mapped with T1600/T1620.
;*****************************************************************************
L0926:
0926: 7E              LD      A,(HL)              ; 
0927: E6 07           AND     $07                 ; mask out 0000_0111
0929: 81              ADD     A,C                 ; 
092A: 4F              LD      C,A                 ; 
092B: 0A              LD      A,(BC)              ; get data from table
092C: 2D              DEC     L                   ; 
092D: 77              LD      (HL),A              ; 
092E: C9              RET                         ; 
;
092F: FF

;*****************************************************************************
;* Get the assigned player bullet tile if fire button was pressed.
;*****************************************************************************
L0930:
0930: 7E              LD      A,(HL)              ; 
0931: E6 08           AND     $08                 ; mask out 0000_1000
0933: C2 64 09        JP      NZ,$0964            ; {code.L0964} update PlayerBulletY (grid) and PlayerBulletState
0936: EB              EX      DE,HL               ; 
0937: 06 10           LD      B,$10               ; 0001_0000 (bit4='fire')
0939: CD BB 00        CALL    $00BB               ; {code.CheckInputBits}
093C: C8              RET     Z                   ; return if button not pressed
093D: 7E              LD      A,(HL)              ; 
093E: E6 EF           AND     $EF                 ; mask out 1110_1111
0940: 77              LD      (HL),A              ; 
0941: 1A              LD      A,(DE)              ; 
0942: F6 08           OR      $08                 ; set bit3 at..
0944: 12              LD      (DE),A              ; $43C4 PlayerBulletState
0945: 13              INC     DE                  ; 
0946: 13              INC     DE                  ; 
0947: 3A C2 43        LD      A,($43C2)           ; {ram.PlayerShipX}
094A: C6 04           ADD     $04                 ; mask out 0000_0100
094C: 12              LD      (DE),A              ; 
094D: 13              INC     DE                  ; 
094E: 3A C3 43        LD      A,($43C3)           ; {ram.PlayerShipY} $D8
0951: D6 08           SUB     $08                 ; 
0953: 12              LD      (DE),A              ; 
0954: 1B              DEC     DE                  ; 
0955: EB              EX      DE,HL               ; 
0956: 01 20 16        LD      BC,$1620            ; {+code.T1620} get character for player bullets
0959: CD 26 09        CALL    $0926               ; {code.L0926} get player ship animation frame values, mapped with T1600/T1620
095C: 3E 30           LD      A,$30               ; 0011_0000
095E: 32 61 43        LD      ($4361),A           ; {ram.BulletTriggered} set 'bullet triggered' flag
0961: C9              RET                         ; 
;
0962: FF FF

;*****************************************************************************
;* Update PlayerBulletY (grid) and PlayerBulletState.
;*****************************************************************************
L0964:
0964: 2C              INC     L                   ; 
0965: 2C              INC     L                   ; 
0966: 2C              INC     L                   ; 
0967: 7E              LD      A,(HL)              ; get $43C7 PlayerBulletY (grid)
0968: D6 08           SUB     $08                 ; move bullet ($08 represents the bullet speed)
096A: 77              LD      (HL),A              ; 
096B: FE 1F           CP      $1F                 ; top of the screen reached?
096D: D0              RET     NC                  ; if not reached
L096E:
096E: 2D              DEC     L                   ; 
096F: 2D              DEC     L                   ; 
0970: 2D              DEC     L                   ; 
0971: 7E              LD      A,(HL)              ; get $43C4 PlayerBulletState
0972: E6 F7           AND     $F7                 ; 1111_0111
0974: 77              LD      (HL),A              ; del bit3 at PlayerBulletState
0975: C9              RET                         ; 
;
0976: FF FF
; not used
0978: 7E E6

;*****************************************************************************
;* Player ship X position mapping.
;*****************************************************************************
L097A:
097A: 3A C2 43        LD      A,($43C2)           ; {ram.PlayerShipX}
097D: 47              LD      B,A                 ; save it
097E: E6 07           AND     $07                 ; mask out 0000_0111
0980: 07              RLCA                        ; 
0981: 21 38 0B        LD      HL,$0B38            ; {+code.T0B38} mapping table
0984: 85              ADD     A,L                 ; 
0985: 6F              LD      L,A                 ; 
0986: 78              LD      A,B                 ; restore it
0987: 96              SUB     (HL)                ; 
0988: 32 9E 43        LD      ($439E),A           ; {ram.M439E} Mapped player ship position, left part
098B: 23              INC     HL                  ; 
098C: 78              LD      A,B                 ; 
098D: 86              ADD     A,(HL)              ; 
098E: 32 9F 43        LD      ($439F),A           ; {ram.M439F} Mapped player ship position, right part
0991: C9              RET                         ; 
; not used
0992: 32 9F 43        LD      ($439F),A           ; {ram.M439F}
0995: C9              RET                         ; 
;
0996: FF FF FF FF FF FF FF FF FF FF

;*****************************************************************************
;* Get screen ram adress for player and bullet positions.
;* from: 43C2:43C3, 43C6:43C7, 43CA:43CB
;* ......PlayerShipX
;* ...........PlayerShipY
;* .................PlayerBulletX
;* ......................PlayerBulletY
;* ............................AbovePlayerBulletX
;* .................................AbovePlayerBulletY
;* to:   43E2:43E3, 43E6:43E7, 43EA:43EB
;*****************************************************************************
L09A0:
09A0: 01 C2 43        LD      BC,$43C2            ; {+ram.PlayerShipX}
09A3: 11 E2 43        LD      DE,$43E2            ; {+ram.PlayerShipMSB}
L09A6:
09A6: CD BA 09        CALL    $09BA               ; {code.GetScreenRamAddress}
09A9: 03              INC     BC                  ; 
09AA: 03              INC     BC                  ; 
09AB: 03              INC     BC                  ; 
09AC: 13              INC     DE                  ; 
09AD: 13              INC     DE                  ; 
09AE: 13              INC     DE                  ; 
09AF: 79              LD      A,C                 ; 
09B0: FE CE           CP      $CE                 ; end of data structure
09B2: C2 A6 09        JP      NZ,$09A6            ; {code.L09A6}
09B5: C9              RET                         ; 
;
09B6: FF  FF FF  FF

;*****************************************************************************
;* Mapping of 'grid values' to screen ram address.
;*****************************************************************************
GetScreenRamAddress:
09BA: 21 00 0A        LD      HL,$0A00            ; {+code.T0A00} Screen ram addresses for the top row (left to right)
09BD: 0A              LD      A,(BC)              ; get the coordinate
09BE: E6 F8           AND     $F8                 ; 1111_1000
09C0: 0F              RRCA                        ; 0111_1100
09C1: 0F              RRCA                        ; 0011_1110
09C2: 85              ADD     A,L                 ; 
09C3: 6F              LD      L,A                 ; 
09C4: 7E              LD      A,(HL)              ; get MSB of screen ram address for row
09C5: 12              LD      (DE),A              ; save it
09C6: 03              INC     BC                  ; 
09C7: 13              INC     DE                  ; 
09C8: 23              INC     HL                  ; move to LSB for T0A00
09C9: 0A              LD      A,(BC)              ; get the coordinate
09CA: E6 F8           AND     $F8                 ; 1111_1000
09CC: 0F              RRCA                        ; 0111_1100
09CD: 0F              RRCA                        ; 0011_1110
09CE: 0F              RRCA                        ; 0001_1111
09CF: 86              ADD     A,(HL)              ; add to LSB of screen ram address for row
09D0: 12              LD      (DE),A              ; save it
09D1: C9              RET                         ; 
;
09D2: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
09E2: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
09F2: FF FF FF FF FF FF FF FF FF FF FF FF FF FF

; Screen ram addresses for the top row (left to right)
; Notice these addresses are MSB:LSB (backwards from the processors endianness)
T0A00:
0A00: 43 20 ; ForegroundScreen+$320 (Upper left corner of rotated screen)
0A02: 43 00 ; ForegroundScreen+$300
0A04: 42 e0 ; ForegroundScreen+$2E0
0A06: 42 c0 ; ForegroundScreen+$2C0
0A08: 42 a0 ; ForegroundScreen+$2A0
0A0A: 42 80 ; ForegroundScreen+$280
0A0C: 42 60 ; ForegroundScreen+$260
0A0E: 42 40 ; ForegroundScreen+$240
0A10: 42 20 ; ForegroundScreen+$220
0A12: 42 00 ; ForegroundScreen+$200
0A14: 41 e0 ; ForegroundScreen+$1E0
0A16: 41 c0 ; ForegroundScreen+$1C0
0A18: 41 a0 ; ForegroundScreen+$1A0
0A1A: 41 80 ; ForegroundScreen+$180
0A1C: 41 60 ; ForegroundScreen+$160
0A1E: 41 40 ; ForegroundScreen+$140
0A20: 41 20 ; ForegroundScreen+$120
0A22: 41 00 ; ForegroundScreen+$100
0A24: 40 e0 ; ForegroundScreen+$E0
0A26: 40 c0 ; ForegroundScreen+$C0
0A28: 40 a0 ; ForegroundScreen+$A0
0A2A: 40 80 ; ForegroundScreen+$80
0A2C: 40 60 ; ForegroundScreen+$60
0A2E: 40 40 ; ForegroundScreen+$40
0A30: 40 20 ; ForegroundScreen+$20
0A32: 40 00 ; ForegroundScreen (Upper right corner of rotated screen)

; Mapping the 'out of screen' objects
0A34: 00 00
0A36: 00 00
0A38: 00 00
0A3A: 00 00
0A3C: 00 00
0A3E: 00 00
;
T0A40:
0A40: AA BA AB BB     ;alien shape #37 (set A)
0A44: 80 90 81 91     ;alien shape #34 (set A)
T0A48:
0A48: 74 7C 75 7D     ;alien pilot shape (set B)
;
0A4C: FF FF FF FF

;*****************************************************************************
;* Handle alien control states for all aliens.
;* This routine has a bug!
;* Loop goes 20 times for 16 aliens. But bit 3 or 4 is not set at 
;* UpdateScreenObjects. So luckily no effect.
;* Possible fix would be: 'CP $F0' at $0A63.
;*****************************************************************************
AlienDataController:
0A50: 01 70 4B        LD      BC,$4B70            ; {+ram.M4B70} alien data structure (grid)
0A53: 11 B0 4B        LD      DE,$4BB0            ; {+ram.M4BB0} alien data structure (screen ram)
L0A56:
0A56: C5              PUSH    BC                  ; 
0A57: CD 18 07        CALL    $0718               ; {code.UpdateScreenObjects}
0A5A: C1              POP     BC                  ; 
0A5B: 79              LD      A,C                 ; 
0A5C: C6 04           ADD     $04                 ; 
0A5E: 4F              LD      C,A                 ; 
0A5F: C6 40           ADD     $40                 ; 
0A61: 5F              LD      E,A                 ; 
0A62: 50              LD      D,B                 ; 
0A63: A7              AND     A                   ; updates the zero flag
0A64: C2 56 0A        JP      NZ,$0A56            ; {code.L0A56}
0A67: C9              RET                         ; 
;
0A68: FF FF FF FF

;*****************************************************************************
;* Get screen ram adress for all aliens.
;*****************************************************************************
L0A6C:
0A6C: 01 70 4B        LD      BC,$4B70            ; {+ram.M4B70} data structure for alien control and screen coordinate
0A6F: 11 B3 4B        LD      DE,$4BB3            ; {+ram.M4BB3} data structure for alien screen ram address
L0A72:
0A72: C5              PUSH    BC                  ; 
0A73: D5              PUSH    DE                  ; 
0A74: 0A              LD      A,(BC)              ; 
0A75: E6 18           AND     $18                 ; mask out 0001_1000
0A77: CA 8A 0A        JP      Z,$0A8A             ; {code.L0A8A} if 0 then skip the mapping
0A7A: EB              EX      DE,HL               ; 
0A7B: 56              LD      D,(HL)              ; 
0A7C: 2B              DEC     HL                  ; 
0A7D: 5E              LD      E,(HL)              ; 
0A7E: 2B              DEC     HL                  ; 
0A7F: 72              LD      (HL),D              ; 
0A80: 2B              DEC     HL                  ; 
0A81: 73              LD      (HL),E              ; 
0A82: EB              EX      DE,HL               ; 
0A83: 13              INC     DE                  ; 
0A84: 13              INC     DE                  ; 
0A85: 03              INC     BC                  ; 
0A86: 03              INC     BC                  ; 
0A87: CD BA 09        CALL    $09BA               ; {code.GetScreenRamAddress}
L0A8A:
0A8A: D1              POP     DE                  ; 
0A8B: C1              POP     BC                  ; 
0A8C: 79              LD      A,C                 ; 
0A8D: C6 04           ADD     $04                 ; 
0A8F: 4F              LD      C,A                 ; 
0A90: 7B              LD      A,E                 ; 
0A91: C6 04           ADD     $04                 ; 
0A93: 5F              LD      E,A                 ; 
0A94: FE 03           CP      $03                 ; 
0A96: C2 72 0A        JP      NZ,$0A72            ; {code.L0A72} loop for all aliens
0A99: C9              RET                         ; 
;
0A9A: FF FF FF FF FF FF

;*****************************************************************************
;* Handler for the player shield.
;*****************************************************************************
DrawShields:
0AA0: 2E E2           LD      L,$E2               ; HL=43E2 Player's screen memory location
0AA2: 56              LD      D,(HL)              ; Get the PlayerScreenRamMSB
0AA3: 23              INC     HL                  ; Get the ... PlayerScreenRamLSB
0AA4: 5E              LD      E,(HL)              ; ... LSB (ignore any fine bit shifting of the player)
0AA5: CD 10 02        CALL    $0210               ; {code.LeftOneColumn} Shield pictures begin one column to the left of the ship
0AA8: 1B              DEC     DE                  ; Shield pictures begin one row above the ship
0AA9: 01 04 04        LD      BC,$0404            ; Shiled images are 4x4
0AAC: 2E A6           LD      L,$A6               ; Decrement the ...
0AAE: 35              DEC     (HL)                ; ... shield counter
0AAF: 7E              LD      A,(HL)              ; Current shield counter value
0AB0: 21 F0 17        LD      HL,$17F0            ; {+code.FourByFourEmpty} Blank 4x4
0AB3: FE C0           CP      $C0                 ; Shield time done?
0AB5: CA 48 0B        JP      Z,$0B48             ; {code.ShieldsExpired} Yes ... turn shields off
0AB8: 21 70 17        LD      HL,$1770            ; {+code.T1770} Four shield-active pictures
0ABB: E6 0C           AND     $0C                 ; Drop lower 2 bits (0000_1100). Images change every 4 ticks.
0ABD: 07              RLCA                        ; Multiply by 4 ...
0ABE: 07              RLCA                        ; ... to get a 16-byte offest (4x4 pictures)
0ABF: 85              ADD     A,L                 ; Point to the ...
0AC0: 6F              LD      L,A                 ; ... correct image
0AC1: C3 D6 0A        JP      $0AD6               ; {code.DrawImageCbyB} Draw the new shield image
;
0AC4: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0AD4: FF FF

;*****************************************************************************
; B is number of rows
; C is number of columns
; HL is the data
; DE is the pointer to the screen
;*****************************************************************************
DrawImageCbyB:
0AD6: D5              PUSH    DE                  ; Hold screen pointer
0AD7: C5              PUSH    BC                  ; Hold width/Height
L0AD8:
0AD8: 7E              LD      A,(HL)              ; Character to ...
0AD9: 12              LD      (DE),A              ; ... the screen
0ADA: 23              INC     HL                  ; Next in data
0ADB: 13              INC     DE                  ; Next column on screen
0ADC: 05              DEC     B                   ; All rows done in this column?
0ADD: C2 D8 0A        JP      NZ,$0AD8            ; {code.L0AD8} No ... finish the rows
0AE0: C1              POP     BC                  ; Restore the counters
0AE1: D1              POP     DE                  ; Restore the screen pointer
0AE2: CD 17 02        CALL    $0217               ; {code.RightOneColumn} Move over one column
0AE5: 0D              DEC     C                   ; All columns done?
0AE6: C2 D6 0A        JP      NZ,$0AD6            ; {code.DrawImageCbyB} No ... do all columns
0AE9: C9              RET                         ; Done

;*****************************************************************************
;* Game state 4.
;* Player ship partikel explosion.
;*****************************************************************************
L0AEA:
0AEA: 21 B9 43        LD      HL,$43B9            ; {+ram.CounterB9}
0AED: 7E              LD      A,(HL)              
0AEE: E6 F8           AND     $F8                 ; 1111_1000
0AF0: 77              LD      (HL),A              
0AF1: 32 00 58        LD      ($5800),A           ; {hard.scrollRegister} 58xx scroll register
0AF4: 2E E2           LD      L,$E2               ; PlayerShipMSB
0AF6: 56              LD      D,(HL)              
0AF7: 2C              INC     L                   ; PlayerShipLSB
0AF8: 5E              LD      E,(HL)              
0AF9: CD 10 02        CALL    $0210               ; {code.LeftOneColumn}
0AFC: 1B              DEC     DE                  
0AFD: 00              NOP                         
0AFE: 2E A5           LD      L,$A5               ; CounterA5
0B00: 35              DEC     (HL)                
0B01: 7E              LD      A,(HL)              
0B02: CA 15 0B        JP      Z,$0B15             ; {code.L0B15}
0B05: FE 20           CP      $20                 
0B07: DA A0 0B        JP      C,$0BA0             ; {code.L0BA0}
0B0A: CA 80 03        JP      Z,$0380             ; {code.ClearForeground}
0B0D: C3 BA 0B        JP      $0BBA               ; {code.L0BBA}

; not used 
0B10: 70 20 C3 E8 20                              ;
;
L0B15:
0B15: 2D              DEC     L                   ; 
0B16: 36 05           LD      (HL),$05            
0B18: 2D              DEC     L                   
0B19: 7E              LD      A,(HL)              
0B1A: C6 90           ADD     $90                 
0B1C: 6F              LD      L,A                 
0B1D: 7E              LD      A,(HL)              
0B1E: A7              AND     A                   ; updates the zero flag
0B1F: C8              RET     Z                   
0B20: 35              DEC     (HL)                
0B21: E5              PUSH    HL                  
0B22: CD 67 03        CALL    $0367               ; {code.UpdateLivesScreen}
0B25: E1              POP     HL                  
0B26: 7E              LD      A,(HL)              
0B27: A7              AND     A                   ; updates the zero flag
0B28: C8              RET     Z                   
0B29: 2E A4           LD      L,$A4               ; GameState
0B2B: 36 00           LD      (HL),$00            ; set to: 'new game start'
0B2D: C9              RET                         
; 
0B2E: FF FF FF
; not used 
0B31: F0 E0 B0 C0 D0 C0 B0                        ;

; Player ship X position mapping table
T0B38:
0B38: 00 08 
0B3A: 01 09 
0B3C: 02 0A 
0B3E: 03 0B 
0B40: 03 0B 
0B42: 02 0A 
0B44: 01 09 
0B46: 00 08 

;*****************************************************************************
;* The player shield is expired.
;* Shield and player gets removed from screen.
;* PlayerShipX position is reset.
;*****************************************************************************
ShieldsExpired:
0B48: CD D6 0A        CALL    $0AD6               ; {code.DrawImageCbyB}
0B4B: 21 C0 43        LD      HL,$43C0            ; {+ram.PlayerState}
0B4E: 36 0C           LD      (HL),$0C            ; 0000_1100
0B50: 2C              INC     L                   ; PlayerShape
0B51: 36 0C           LD      (HL),$0C            ; 0000_1100
0B53: 2C              INC     L                   ; PlayerShipX
0B54: 7E              LD      A,(HL)              ; get
0B55: E6 F8           AND     $F8                 ; 1111_1000
0B57: F6 03           OR      $03                 ; 0000_0011
0B59: 77              LD      (HL),A              ; reset PlayerShipX
0B5A: C9              RET                         ; 

0B5B: FF FF FF FF FF

;*****************************************************************************
;* Game state 5.
;* 'GAME OVER'.
;*****************************************************************************
L0B60:
0B60: 21 A5 43        LD      HL,$43A5            ; {+ram.CounterA5}
0B63: 34              INC     (HL)                
0B64: 7E              LD      A,(HL)              
0B65: FE 40           CP      $40                 
0B67: CA A0 03        JP      Z,$03A0             ; {code.ClearBackground}
0B6A: 21 00 1A        LD      HL,$1A00            ; {+code.T1A00} "        GAME  OVER        "
0B6D: 0E 01           LD      C,$01               
0B6F: FE 80           CP      $80                 
0B71: C2 95 0B        JP      NZ,$0B95            ; {code.L0B95}
0B74: 21 A4 43        LD      HL,$43A4            ; {+ram.GameState} Next interval game state ...
0B77: 36 00           LD      (HL),$00            ; ... is 0 (new game start)
0B79: 2E 90           LD      L,$90               ; Player1Lives
0B7B: 7E              LD      A,(HL)              
0B7C: 2C              INC     L                   ; Player2Lives
0B7D: B6              OR      (HL)                
0B7E: C0              RET     NZ                  
0B7F: AF              XOR     A                   ; A=0
0B80: 2E 98           LD      L,$98               ; Counter98
0B82: 77              LD      (HL),A              
0B83: 2C              INC     L                   ; Counter98+1
0B84: 77              LD      (HL),A              
0B85: 2E A2           LD      L,$A2               ; GameOrAttract
0B87: 77              LD      (HL),A              
0B88: 2C              INC     L                   ; GameAndDemoOrSplash
0B89: 7E              LD      A,(HL)              
0B8A: A7              AND     A                   ; updates the zero flag
0B8B: C8              RET     Z                   
0B8C: 36 00           LD      (HL),$00            
0B8E: 01 00 01        LD      BC,$0100            ; from bank 1 to bank 0
0B91: CD 60 04        CALL    $0460               ; {code.CopyMemoryBank}
0B94: C9              RET                         
; 
L0B95:
0B95: CD D0 01        CALL    $01D0               ; {code.PrintTextLines} "        GAME  OVER        "
0B98: CD E4 01        CALL    $01E4               ; {code.L01E4} print the copyright lines
0B9B: C3 F0 1D        JP      $1DF0               ; {code.L1DF0} protection against piracy
; 
0B9E: FF FF
; 
L0BA0:
0BA0: 21 B8 43        LD      HL,$43B8            ; {+ram.LevelAndRound}
0BA3: 7E              LD      A,(HL)              ; 
0BA4: E6 0F           AND     $0F                 ; mask out 0000_1111
0BA6: FE 04           CP      $04                 ; 
0BA8: D8              RET     C                   ; return if < game level 4 (alien waves)
0BA9: FE 09           CP      $09                 ; 
0BAB: D0              RET     NC                  ; return if > game level 9 (mothership)
0BAC: 2C              INC     L                   ; CounterB9
0BAD: AF              XOR     A                   ; A=0
0BAE: 77              LD      (HL),A              ; CounterB9 to 0
0BAF: 32 00 58        LD      ($5800),A           ; {hard.scrollRegister} reset the 58xx scroll register
0BB2: C3 A0 03        JP      $03A0               ; {code.ClearBackground}
; 
0BB5: FF FF FF FF FF
; 
L0BBA:
0BBA: 47              LD      B,A                 ; 
0BBB: 0F              RRCA                        ; 
0BBC: D2 C0 0F        JP      NC,$0FC0            ; {code.L0FC0} Handle animations for killed aliens
0BBF: 0F              RRCA                        ; 
0BC0: 78              LD      A,B                 ; 
0BC1: DA 70 20        JP      C,$2070             ; {code.L2070}
0BC4: C3 E8 20        JP      $20E8               ; {code.L20E8}
; 
0BC7: FF FF FF

;*****************************************************************************
;* Draws the character tiles for the score average table.
;*****************************************************************************
DrawScoreAverageTableTiles:
0BCA: 21 D0 42        LD      HL,$42D0            ; upper left corner screen ram position
0BCD: 01 DF FF        LD      BC,$FFDF            ; Screen offset constant -33 right one column (-1), up one row (-32)
0BD0: 36 64           LD      (HL),$64            ; left part of alien shape #3
0BD2: 09              ADD     HL,BC               ; 
0BD3: 23              INC     HL                  ; 
0BD4: 36 65           LD      (HL),$65            ; right part of alien shape #3
0BD6: 21 F2 42        LD      HL,$42F2            ; screen ram position for
0BD9: 11 40 0A        LD      DE,$0A40            ; {+code.T0A40} alien shape #37 and alien shape #34
0BDC: CD 38 35        CALL    $3538               ; {code.Draw4x2}
0BDF: 21 15 4B        LD      HL,$4B15            ; screen ram position for
0BE2: 11 00 3C        LD      DE,$3C00            ; {+code.T3C00} bird shape #24 (Object 3C00)
0BE5: CD 28 35        CALL    $3528               ; {code.Draw6x2}
0BE8: 21 D8 4A        LD      HL,$4AD8            ; screen ram position for
0BEB: 11 48 0A        LD      DE,$0A48            ; {+code.T0A48} alien pilot shape
0BEE: CD 48 35        CALL    $3548               ; {code.Draw2x2}
0BF1: C9              RET                         ; 

0BF2: FF FF FF FF FF FF FF FF FF FF FF FF FF FF

L0C00:
0C00: E5              PUSH    HL                  
0C01: 7D              LD      A,L                 
0C02: D6 72           SUB     $72                 
0C04: 0F              RRCA                        
0C05: C6 50           ADD     $50                 
0C07: 6F              LD      L,A                 
0C08: 7E              LD      A,(HL)              ; get MSB pointer of alien movement pattern
0C09: 2C              INC     L                   
0C0A: 6E              LD      L,(HL)              ; get LSB pointer of alien movement pattern
0C0B: 67              LD      H,A                 
0C0C: 11 04 0C        LD      DE,$0C04            
0C0F: 7E              LD      A,(HL)              ; get movement pattern value
0C10: E1              POP     HL                  
0C11: FE 07           CP      $07                 
0C13: DA A4 0E        JP      C,$0EA4             ; {code.L0EA4} if < $07
0C16: FE 09           CP      $09                 
0C18: D2 A4 0E        JP      NC,$0EA4            ; {code.L0EA4} if >= $09
0C1B: 11 20 10        LD      DE,$1020            ; set E reg. for bonus explosion score 200
0C1E: 3E FF           LD      A,$FF               ; set bonus explosion flag
0C20: 32 69 43        LD      ($4369),A           ; {ram.M4369}
0C23: C3 A4 0E        JP      $0EA4               ; {code.L0EA4}
; 
0C26: FF FF FF FF FF FF FF FF FF FF  FF FF FF FF FF FF
0C36: FF FF FF FF FF FF FF FF FF FF

;*****************************************************************************
; Updates the enemy bullets.
;*****************************************************************************
EnemyBulletUpdate:
0C40: 21 FF 43        LD      HL,$43FF            ; {+ram.EnemyBullet4LSB}
0C43: 06 05           LD      B,$05               ; 5 bullet slots
0C45: CD 8B 08        CALL    $088B               ; {code.L088B} Copy current enemy bullet data to old enemy bullet data.
0C48: CD 56 0C        CALL    $0C56               ; {code.L0C56} Enemy bullets movement and animation
0C4B: CD 6B 0C        CALL    $0C6B               ; {code.L0C6B} Get the screen ram address for all enemy bullets
0C4E: CD D8 0C        CALL    $0CD8               ; {code.EnemyBulletDataController} Draw or delete the screen objects
0C51: C9              RET                         ; 

0C52: FF FF FF FF

;*****************************************************************************
;* Enemy bullets movement and animation.
;* Handles all 5 bullet slots.
;*****************************************************************************
L0C56:
0C56: 21 CC 43        LD      HL,$43CC            ; {+ram.EnemyBullet0State}
L0C59:
0C59: E5              PUSH    HL                  
0C5A: CD 84 0C        CALL    $0C84               ; {code.L0C84} movement and animation of enemy bullet
0C5D: E1              POP     HL                  
0C5E: 7D              LD      A,L                 
0C5F: C6 04           ADD     $04                 
0C61: 6F              LD      L,A                 
0C62: FE E0           CP      $E0                 
0C64: C2 59 0C        JP      NZ,$0C59            ; {code.L0C59} loop for 5 enemy bullet slots
0C67: C9              RET                         

0C68: FF FF FF

;*****************************************************************************
;* Get the screen ram address for all enemy bullets.
;*****************************************************************************
L0C6B:
0C6B: 01 CE 43        LD      BC,$43CE            ; {+ram.EnemyBullet0X}
0C6E: 11 EE 43        LD      DE,$43EE            ; {+ram.EnemyBullet0MSB}
L0C71:
0C71: CD BA 09        CALL    $09BA               ; {code.GetScreenRamAddress}
0C74: 03              INC     BC                  
0C75: 03              INC     BC                  
0C76: 03              INC     BC                  
0C77: 13              INC     DE                  
0C78: 13              INC     DE                  
0C79: 13              INC     DE                  
0C7A: 79              LD      A,C                 
0C7B: FE E2           CP      $E2                 
0C7D: C2 71 0C        JP      NZ,$0C71            ; {code.L0C71} loop for 5 enemy bullet slots
0C80: C9              RET                         

0C81: FF FF FF

;*****************************************************************************
;* Movement and animation of enemy bullet.
;* They have half the speed of player bullets and a simple animation.
;*****************************************************************************
L0C84:
0C84: 7E              LD      A,(HL)              ; get enemy bullet control state
0C85: E6 08           AND     $08                 ; 0000_1000
0C87: C8              RET     Z                   ; if bit 3 not set
0C88: 00              NOP                         ; 
0C89: 00              NOP                         ; 
0C8A: 2C              INC     L                   ; 
0C8B: 7E              LD      A,(HL)              ; get enemy bullet character code
0C8C: EE 04           XOR     $04                 ; toggle 0000_0100 for animation: $58/$5C, $59/$5D, ...
0C8E: 77              LD      (HL),A              ; set new character code
0C8F: 2C              INC     L                   ; 
0C90: 2C              INC     L                   ; 
0C91: 7E              LD      A,(HL)              ; get enemy bullet coordinate Y
0C92: C6 04           ADD     $04                 ; move bullet down
0C94: 77              LD      (HL),A              ; 
0C95: FE F9           CP      $F9                 ; bottom of screen
0C97: D2 6E 09        JP      NC,$096E            ; {code.L096E} if bottom of screen reached
0C9A: 2D              DEC     L                   ; enemy bullet coordinate X
0C9B: CD B4 0C        CALL    $0CB4               ; {code.L0CB4}
0C9E: 54              LD      D,H                 ;
0C9F: 7D              LD      A,L                 ;
0CA0: C6 20           ADD     $20                 ; move to EnemyBullet(x)MSB
0CA2: 5F              LD      E,A                 ;
0CA3: EB              EX      DE,HL               ; 
0CA4: 46              LD      B,(HL)              ; get EnemyBullet(x)MSB
0CA5: 23              INC     HL                  ; 
0CA6: 4E              LD      C,(HL)              ; get EnemyBullet(x)LSB
0CA7: 0A              LD      A,(BC)              ; 
0CA8: EB              EX      DE,HL               ; 
0CA9: 2C              INC     L                   ; 
0CAA: FE E8           CP      $E8                 ; 
0CAC: D2 6E 09        JP      NC,$096E            ; {code.L096E} if >= $E8 (fgtiles upper part of player shield)
0CAF: C9              RET                         ; 
;
0CB0: FF FF FF FF
;
L0CB4:
0CB4: FE DC           CP      $DC                 ; lower part of screen
0CB6: D8              RET     C                   ; if not reached
0CB7: FE E9           CP      $E9                 
0CB9: D0              RET     NC                  
0CBA: 3A 9F 43        LD      A,($439F)           ; {ram.M439F} Mapped player ship position, right part: ($17 to $C8)
0CBD: BE              CP      (HL)                
0CBE: D8              RET     C                   
0CBF: 3A 9E 43        LD      A,($439E)           ; {ram.M439E} Mapped player ship position, left part: ($09 to $C0)
0CC2: BE              CP      (HL)                
0CC3: D0              RET     NC                  

;*****************************************************************************
;* The player ship was hit.
;* MAME cheat code "Invincibility": Set $0CC4 to $C9 (RET).
;*****************************************************************************
L0CC4:
0CC4: 3E 04           LD      A,$04               ; Next interval game state is 4 (player ship partikel explosion)
0CC6: 32 A4 43        LD      ($43A4),A           ; {ram.GameState}
0CC9: 3E 60           LD      A,$60               ; set a new counter value for ...
0CCB: 32 A5 43        LD      ($43A5),A           ; {ram.CounterA5}
0CCE: 3E 10           LD      A,$10               ; set flag and counter for ..
0CD0: 32 63 43        LD      ($4363),A           ; {ram.ParticleExplosion}
0CD3: C9              RET                         ; 
; 
0CD4: FF FF FF FF

;*****************************************************************************
;* Handle enemy bullet control states for 5 bullet slots,
;* and draw or delete the screen object.
;*****************************************************************************
EnemyBulletDataController:
0CD8: 01 CC 43        LD      BC,$43CC            ; {+ram.EnemyBullet0State} data structure (grid)
0CDB: 11 EC 43        LD      DE,$43EC            ; {+ram.OldEnemyBullet0MSB} screen ram
L0CDE:
0CDE: C5              PUSH    BC                  
0CDF: CD 18 07        CALL    $0718               ; {code.UpdateScreenObjects}
0CE2: C1              POP     BC                  
0CE3: 79              LD      A,C                 
0CE4: C6 04           ADD     $04                 
0CE6: 4F              LD      C,A                 
0CE7: C6 20           ADD     $20                 
0CE9: 5F              LD      E,A                 
0CEA: 50              LD      D,B                 
0CEB: A7              AND     A                   ; updates the zero flag
0CEC: C2 DE 0C        JP      NZ,$0CDE            ; {code.L0CDE} loop for all bullet slots
0CEF: C9              RET                         
; 
0CF0: FF FF FF FF
;
; Alien collision on left or right side of player ship.
L0CF4:
0CF4: D1              POP     DE                  
0CF5: C1              POP     BC                  
0CF6: C9              RET                         

0CF7: FF FF FF FF FF FF FF FF
0CFF: FF FF FF FF FF FF FF FF FF

; not used 
0D08: 21 93 43        LD      HL,$4393            ; {+ram.Counter93}
0D0B: 34              INC     (HL)                
0D0C: 7E              LD      A,(HL)              
0D0D: E6 07           AND     $07                 
0D0F: C0              RET     NZ                  
0D10: 2C              INC     L                   
0D11: 2C              INC     L                   
0D12: 7E              LD      A,(HL)              
0D13: 3C              INC     A                   
0D14: E6 0F           AND     $0F                 
0D16: 77              LD      (HL),A              
0D17: C9              RET                         

0D18: FF FF FF FF

;*****************************************************************************
;* Alien movement update.
;*****************************************************************************
AlienMovementUpdate:
0D1C: 01 70 4B        LD      BC,$4B70            ; {+ram.M4B70} Alien control state A
0D1F: 21 50 4B        LD      HL,$4B50            ; {+ram.M4B50} Alien movement pattern table
L0D22:
0D22: CD 30 0D        CALL    $0D30               ; {code.L0D30}
0D25: 0C              INC     C                   ; 
0D26: 0C              INC     C                   ; 
0D27: 2C              INC     L                   ; 
0D28: 3E B0           LD      A,$B0               ; 
0D2A: B9              CP      C                   ; 
0D2B: C2 22 0D        JP      NZ,$0D22            ; {code.L0D22} loop for 16 aliens
0D2E: C9              RET                         ; 

0D2F: FF
;
L0D30:
0D30: 56              LD      D,(HL)              ; get MSB of pointer for alien movement pattern
0D31: 23              INC     HL                  ; 
0D32: 0A              LD      A,(BC)              ; get alien control state A
0D33: 03              INC     BC                  ; 
0D34: 03              INC     BC                  ; 
0D35: E6 08           AND     $08                 ; 0000_1000
0D37: C8              RET     Z                   ; if bit3 of alien control state A, not set
0D38: 5E              LD      E,(HL)              ; get LSB of pointer for alien movement pattern
0D39: EB              EX      DE,HL               ; 
0D3A: 7E              LD      A,(HL)              ; get pointer to movement list (T1000)
0D3B: 07              RLCA                        ; multiply by 2 to get a 2 byte offset at T1700
0D3C: C6 00           ADD     $00                 ; reset all flags
0D3E: 6F              LD      L,A                 ; get LSB for movement direction table (T1700)
0D3F: 26 17           LD      H,$17               ; get MSB for movement direction table (T1700)
0D41: AF              XOR     A                   ; A=0
0D42: BE              CP      (HL)                ; check for end marker
0D43: CA 4F 0D        JP      Z,$0D4F             ; {code.L0D4F} if end reached
0D46: 23              INC     HL                  ; value for Y movement
0D47: BE              CP      (HL)                ; check for Y movement
0D48: CA 5E 0D        JP      Z,$0D5E             ; {code.L0D5E} if no Y movement
0D4B: 2B              DEC     HL                  ; value for X movement
0D4C: 0A              LD      A,(BC)              ; get alien screen coordinate X
0D4D: 86              ADD     A,(HL)              ; add both
0D4E: 02              LD      (BC),A              ; save
L0D4F:
0D4F: 03              INC     BC                  ; alien screen coordinate Y
0D50: 23              INC     HL                  ; Y from alien movement direction table (T1700)
0D51: 0A              LD      A,(BC)              ; get alien screen coordinate Y
0D52: 86              ADD     A,(HL)              ; add both
0D53: 02              LD      (BC),A              ; save
0D54: 0B              DEC     BC                  ; alien screen coordinate X
0D55: E6 07           AND     $07                 ; 0000_0111
0D57: EB              EX      DE,HL               ; 
0D58: C0              RET     NZ                  ; if grid border not reached
0D59: 34              INC     (HL)                ; next movement list pointer (T1000)
0D5A: C9              RET                         ; 

0D5B: FF FF FF

L0D5E:
0D5E: 2B              DEC     HL                  ; value for X movement
0D5F: 0A              LD      A,(BC)              ; get Alien screen coordinate X
0D60: 86              ADD     A,(HL)              ; add both
0D61: 02              LD      (BC),A              ; save 
0D62: E6 07           AND     $07                 ; 0000_0111
0D64: EB              EX      DE,HL               ; 
0D65: C0              RET     NZ                  ; if grid border not reached
0D66: 34              INC     (HL)                ; next movement list pointer (T1000)
0D67: C9              RET                         ; 
; 
0D68: FF FF FF FF FF FF FF FF

;*****************************************************************************
;* Alien animation update.
;*****************************************************************************
AlienAnimationUpdate:
0D70: 01 70 4B        LD      BC,$4B70            ; {+ram.M4B70} Alien control state A
0D73: 21 50 4B        LD      HL,$4B50            ; {+ram.M4B50} Alien movement pattern table
L0D76:
0D76: CD 86 0D        CALL    $0D86               ; {code.L0D86}
0D79: 79              LD      A,C                 ; 
0D7A: C6 04           ADD     $04                 ; 
0D7C: 4F              LD      C,A                 ; 
0D7D: 3E B0           LD      A,$B0               ; 
0D7F: B9              CP      C                   ; 
0D80: C2 76 0D        JP      NZ,$0D76            ; {code.L0D76} loop for 16 aliens
0D83: C9              RET                         ; 

0D84: FF FF
;
L0D86:
0D86: 56              LD      D,(HL)              ; get MSB of pointer for alien movement pattern
0D87: 23              INC     HL                  ; 
0D88: 5E              LD      E,(HL)              ; get LSB of pointer for alien movement pattern
0D89: 23              INC     HL                  ; 
0D8A: 0A              LD      A,(BC)              ; get alien control state A
0D8B: E6 08           AND     $08                 ; 0000_1000
0D8D: C8              RET     Z                   ; if bit3 of alien control state A, not set
0D8E: EB              EX      DE,HL               ; 
0D8F: 7E              LD      A,(HL)              ; get pointer to movement list (T1000)
0D90: A7              AND     A                   ; updates the zero flag
0D91: CC DE 0D        CALL    Z,$0DDE             ; {code.L0DDE} if end of movement list reached
0D94: 6F              LD      L,A                 ; get pointer to movement list
0D95: 07              RLCA                        ; multiply by ..
0D96: 85              ADD     A,L                 ; .. 3, to get a 3 byte offset at T16A0
0D97: C6 A0           ADD     $A0                 ; LSB of T16A0
0D99: 6F              LD      L,A                 ; 
0D9A: 26 16           LD      H,$16               ; MSB of T16A0
0D9C: 0A              LD      A,(BC)              ; get alien control state A
0D9D: E6 F8           AND     $F8                 ; 1111_1000
0D9F: B6              OR      (HL)                ; 1st byte of alien animation table
0DA0: 02              LD      (BC),A              ; set alien control state A
0DA1: 03              INC     BC                  ; 
0DA2: 03              INC     BC                  ; 
0DA3: 03              INC     BC                  ; alien screen coordinate Y
0DA4: 23              INC     HL                  ; 
0DA5: 7E              LD      A,(HL)              ; get 2nd byte of alien animation table
0DA6: 23              INC     HL                  ; 3rd byte of alien animation table
0DA7: 0F              RRCA                        ; divide by 2
0DA8: DA BB 0D        JP      C,$0DBB             ; {code.L0DBB} if 2nd byte is: $01
0DAB: 0F              RRCA                        ; divide by 2
0DAC: DA CC 0D        JP      C,$0DCC             ; {code.L0DCC} if 2nd byte is: $02
; 2nd byte of alien animation table is: $04
0DAF: 0A              LD      A,(BC)              ; get alien screen coordinate Y
0DB0: 0F              RRCA                        ; divide by 2
0DB1: E6 03           AND     $03                 ; 0000_0011
0DB3: 86              ADD     A,(HL)              ; add with 3rd byte of alien animation table
0DB4: 0B              DEC     BC                  ; alien screen coordinate X
0DB5: C3 D2 0D        JP      $0DD2               ; {code.L0DD2}
; 
0DB8: FF FF FF
; 2nd byte of alien animation table is: $01
L0DBB:
0DBB: 0A              LD      A,(BC)              ; get alien screen coordinate Y
0DBC: 0F              RRCA                        ; divide by 2
0DBD: E6 03           AND     $03                 ; 0000_0011
0DBF: 86              ADD     A,(HL)              ; add with 3rd byte of alien animation table
0DC0: 67              LD      H,A                 ; save
0DC1: 0B              DEC     BC                  ; 
0DC2: 0A              LD      A,(BC)              ; get alien screen coordinate X
0DC3: E6 04           AND     $04                 ; 0000_0100
0DC5: 84              ADD     A,H                 ; add with 3rd byte of alien animation table
0DC6: C3 D2 0D        JP      $0DD2               ; {code.L0DD2}
; 
0DC9: FF FF FF
; 2nd byte of alien animation table is: $02
L0DCC:
0DCC: 0B              DEC     BC                  ; 
0DCD: 0A              LD      A,(BC)              ; get alien screen coordinate X
0DCE: 0F              RRCA                        ; divide by 2
0DCF: E6 03           AND     $03                 ; 0000_0011
0DD1: 86              ADD     A,(HL)              ; add with 3rd byte of alien animation table
L0DD2:
0DD2: 6F              LD      L,A                 ; LSB for T1600
0DD3: 26 16           LD      H,$16               ; MSB for T1600
0DD5: 7E              LD      A,(HL)              ; get data from T1600
0DD6: 0B              DEC     BC                  ; 
0DD7: 02              LD      (BC),A              ; set alien control state B (LSB for T14xx)
0DD8: 0B              DEC     BC                  ; alien control state A
0DD9: EB              EX      DE,HL               ;
0DDA: C9              RET                         ;
; 
0DDB: FF FF FF
; End of movement list reached
L0DDE:
0DDE: 1B              DEC     DE                  ; 
0DDF: 1B              DEC     DE                  ; 
0DE0: 3A 94 43        LD      A,($4394)           ; {ram.M4394} get start value list pointer for alien movement MSB
0DE3: 12              LD      (DE),A              ; save alien movement pattern table MSB
0DE4: 67              LD      H,A                 ; 
0DE5: 13              INC     DE                  ; 
0DE6: 3A 95 43        LD      A,($4395)           ; {ram.M4395} get start value list pointer for alien movement LSB
0DE9: 12              LD      (DE),A              ; save alien movement pattern table LSB
0DEA: 6F              LD      L,A                 ; 
0DEB: 13              INC     DE                  ; 
0DEC: 7E              LD      A,(HL)              ; get value from pointer table to alien movement list
0DED: C9              RET                         ; 
; 
0DEE: FF FF

;*****************************************************************************
;* Enemy bullet to player ship, collission detection.
;*****************************************************************************
L0DF0:
0DF0: 01 C4 43        LD      BC,$43C4            ; {+ram.PlayerBulletState}
0DF3: 21 E6 43        LD      HL,$43E6            ; {+ram.AbovePlayerBulletMSB} MSB screen ram: One character above player bullet
0DF6: CD 10 0E        CALL    $0E10               ; {code.L0E10}
0DF9: 01 C8 43        LD      BC,$43C8            ; {+ram.AbovePlayerBulletState}
0DFC: 21 EA 43        LD      HL,$43EA            ; {+ram.M43EA} MSB screen ram: Left screen edge, one character above player ship
0DFF: C3 10 0E        JP      $0E10               ; {code.L0E10}

; not used
0E02: 01 CC 43        LD      BC,$43CC            ; {+ram.EnemyBullet0State}
0E05: 21 EE 43        LD      HL,$43EE            ; {+ram.EnemyBullet0MSB}
0E08: CD 10 0E        CALL    $0E10               ; {code.L0E10}
0E0B: C9              RET                         ; 
; 
0E0C: FF FF FF FF
; 
L0E10:
0E10: 0A              LD      A,(BC)              ; ?
0E11: E6 08           AND     $08                 ; mask out 0000_1000
0E13: C8              RET     Z                   ; if bit3 not set
0E14: 56              LD      D,(HL)              ; get MSB screen ram adress
0E15: 2C              INC     L                   ; 
0E16: 5E              LD      E,(HL)              ; get LSB screen ram adress
0E17: 1A              LD      A,(DE)              ; get character
0E18: FE C0           CP      $C0                 ; bullets and alien ($50 - $BF)
0E1A: D0              RET     NC                  ; 
0E1B: FE 60           CP      $60                 ; alien ($60 - $BF)
0E1D: D8              RET     C                   ; if no character
0E1E: FE 68           CP      $68                 ; alien
0E20: D2 39 0E        JP      NC,$0E39            ; {code.L0E39} if >= $68 (fgtiles aliens out of formation)
0E23: E6 07           AND     $07                 ; mask out 0000_0111
0E25: 07              RLCA                        ; Multiply by 4 ..
0E26: 07              RLCA                        ; ..
0E27: C6 40           ADD     $40                 ; 
0E29: 6F              LD      L,A                 ; 
0E2A: 26 17           LD      H,$17               ; T1740
0E2C: 03              INC     BC                  ; 
0E2D: 03              INC     BC                  ; 
0E2E: 0A              LD      A,(BC)              ; 
0E2F: E6 07           AND     $07                 ; 0000_0111
0E31: BE              CP      (HL)                ; 
0E32: D0              RET     NC                  ; 
0E33: 23              INC     HL                  ; 
0E34: BE              CP      (HL)                ; 
0E35: D8              RET     C                   ; 
0E36: C3 70 0E        JP      $0E70               ; {code.L0E70}

; 
L0E39:
0E39: 03              INC     BC                  
0E3A: 03              INC     BC                  
0E3B: 0A              LD      A,(BC)              
0E3C: 57              LD      D,A                 
0E3D: 03              INC     BC                  
0E3E: 0A              LD      A,(BC)              
0E3F: E6 F8           AND     $F8                 ; 1111_1000
0E41: 5F              LD      E,A                 
0E42: 21 70 4B        LD      HL,$4B70            ; {+ram.M4B70}
L0E45:
0E45: 7E              LD      A,(HL)              
0E46: 23              INC     HL                  
0E47: 23              INC     HL                  
0E48: E6 08           AND     $08                 ; 0000_1000
0E4A: C4 58 0E        CALL    NZ,$0E58            ; {code.L0E58}
0E4D: 23              INC     HL                  
0E4E: 23              INC     HL                  
0E4F: 3E B0           LD      A,$B0               
0E51: BD              CP      L                   
0E52: C2 45 0E        JP      NZ,$0E45            ; {code.L0E45}
0E55: C9              RET                         
; 
0E56: FF FF
; 
L0E58:
0E58: 7A              LD      A,D                 
0E59: BE              CP      (HL)                
0E5A: D8              RET     C                   
0E5B: 7E              LD      A,(HL)              
0E5C: C6 08           ADD     $08                 
0E5E: BA              CP      D                   
0E5F: D8              RET     C                   
0E60: 23              INC     HL                  
0E61: 7E              LD      A,(HL)              
0E62: 2B              DEC     HL                  
0E63: C6 04           ADD     $04                 
0E65: BB              CP      E                   
0E66: D8              RET     C                   
0E67: D6 0C           SUB     $0C                 
0E69: BB              CP      E                   
0E6A: D0              RET     NC                  
0E6B: C3 00 0C        JP      $0C00               ; {code.L0C00}
; 
0E6E: FF FF
; 
L0E70:
0E70: 23              INC     HL                  
0E71: 0A              LD      A,(BC)              
0E72: E6 F8           AND     $F8                 ; 1111_1000
0E74: 86              ADD     A,(HL)              
0E75: 57              LD      D,A                 
0E76: 03              INC     BC                  
0E77: 0A              LD      A,(BC)              
0E78: E6 F8           AND     $F8                 ; 1111_1000
0E7A: 5F              LD      E,A                 
0E7B: 21 70 4B        LD      HL,$4B70            ; {+ram.M4B70}
L0E7E:
0E7E: 7E              LD      A,(HL)              
0E7F: 23              INC     HL                  
0E80: 23              INC     HL                  
0E81: E6 08           AND     $08                 ; 0000_1000
0E83: C4 90 0E        CALL    NZ,$0E90            ; {code.L0E90}
0E86: 23              INC     HL                  
0E87: 23              INC     HL                  
0E88: 3E B0           LD      A,$B0               
0E8A: BD              CP      L                   
0E8B: C2 7E 0E        JP      NZ,$0E7E            ; {code.L0E7E}
0E8E: C9              RET                         
; 
0E8F: FF
; 
L0E90:
0E90: 7E              LD      A,(HL)              
0E91: C6 02           ADD     $02                 
0E93: BA              CP      D                   
0E94: D8              RET     C                   
0E95: D6 05           SUB     $05                 
0E97: BA              CP      D                   
0E98: D0              RET     NC                  
0E99: 23              INC     HL                  
0E9A: 7E              LD      A,(HL)              
0E9B: 2B              DEC     HL                  
0E9C: E6 F8           AND     $F8                 ; 1111_1000
0E9E: BB              CP      E                   
0E9F: C0              RET     NZ                  
0EA0: 11 02 0C        LD      DE,$0C02            ; E reg. set to: 'bonus explosion score 020'.
0EA3: 00              NOP                         
; 
L0EA4:
0EA4: 2B              DEC     HL                  
0EA5: 2B              DEC     HL                  ; move to alien X control state A
0EA6: 0B              DEC     BC                  
0EA7: 0B              DEC     BC                  
0EA8: 0B              DEC     BC                  ; move to PlayerBulletState
0EA9: 0A              LD      A,(BC)              
0EAA: E6 F7           AND     $F7                 ; 1111_0111
0EAC: 02              LD      (BC),A              
L0EAD:
0EAD: 7E              LD      A,(HL)              
0EAE: E6 F7           AND     $F7                 ; 1111_0111
0EB0: 77              LD      (HL),A              
0EB1: 7D              LD      A,L                 
0EB2: C6 42           ADD     $42                 ; move to MSB screen ram adress alien X
0EB4: 6F              LD      L,A                 
0EB5: 46              LD      B,(HL)              ; get MSB screen ram adress alien X
0EB6: 23              INC     HL                  
0EB7: 4E              LD      C,(HL)              ; get LSB screen ram adress alien X
0EB8: 21 78 43        LD      HL,$4378            ; {+ram.M4378} Animation counter for the bonus explosion
0EBB: 7A              LD      A,D                 
0EBC: FE 10           CP      $10                 
0EBE: CA C3 0E        JP      Z,$0EC3             ; {code.L0EC3}
0EC1: 2E 70           LD      L,$70               
L0EC3:
0EC3: 7E              LD      A,(HL)              
0EC4: A7              AND     A                   ; updates the zero flag
0EC5: CA D5 0E        JP      Z,$0ED5             ; {code.L0ED5}
0EC8: 2C              INC     L                   
0EC9: 2C              INC     L                   
0ECA: 2C              INC     L                   
0ECB: 2C              INC     L                   
0ECC: 7E              LD      A,(HL)              
0ECD: A7              AND     A                   ; updates the zero flag
0ECE: CA D5 0E        JP      Z,$0ED5             ; {code.L0ED5}
0ED1: 2C              INC     L                   
0ED2: 2C              INC     L                   
0ED3: 2C              INC     L                   
0ED4: 2C              INC     L                   
L0ED5:
0ED5: 72              LD      (HL),D              
0ED6: 2C              INC     L                   
0ED7: 73              LD      (HL),E              ; set $4379 (bonus explosion score)
0ED8: 2C              INC     L                   
0ED9: 70              LD      (HL),B              
0EDA: 2C              INC     L                   
0EDB: 71              LD      (HL),C              
0EDC: 2E 64           LD      L,$64               
0EDE: 36 FF           LD      (HL),$FF            
0EE0: 2E BA           LD      L,$BA               ; AliensLeft
0EE2: 35              DEC     (HL)                ; decrement it
0EE3: E1              POP     HL                  
0EE4: E1              POP     HL                  
0EE5: E9              JP      (HL)                ; to: $0DF9, $0027, $2199, $2006
; 
0EE6: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
0EF6: FF FF FF FF FF FF FF FF FF  FF

;*****************************************************************************
;* 'Alien with player' collision check.
;* MAME cheat code "Invisibility for aliens": Set $0F00 to $C9 (RET)
;*****************************************************************************
L0F00:
0F00: 21 A6 43        LD      HL,$43A6            ; {+ram.ShieldCount}
0F03: 7E              LD      A,(HL)              ; 
0F04: FE C0           CP      $C0                 ; 
0F06: D2 74 0F        JP      NC,$0F74            ; {code.L0F74} if >= $C0 (fgtiles all explosion parts)
0F09: 2E E2           LD      L,$E2               ; 
0F0B: 56              LD      D,(HL)              ; get $43E2 PlayerShipMSB
0F0C: 2C              INC     L                   ; 
0F0D: 5E              LD      E,(HL)              ; get $43E3 PlayerShipLSB
0F0E: 01 02 02        LD      BC,$0202            
0F11: CD 56 0F        CALL    $0F56               ; {code.L0F56} 'alien with player' collision check
0F14: C8              RET     Z                   ; if no collision
0F15: 00              NOP                         
0F16: 00              NOP                         
0F17: 21 9E 43        LD      HL,$439E            ; {+ram.M439E} Mapped player ship position, left part: ($09 to $C0)
0F1A: 7E              LD      A,(HL)              
0F1B: D6 06           SUB     $06                 
0F1D: 47              LD      B,A                 
0F1E: 2C              INC     L                   
0F1F: 4E              LD      C,(HL)              
0F20: 21 70 4B        LD      HL,$4B70            ; {+ram.M4B70}
L0F23:
0F23: 7E              LD      A,(HL)              
0F24: 2C              INC     L                   
0F25: 2C              INC     L                   
0F26: E6 08           AND     $08                 ; 0000_1000
0F28: C4 38 0F        CALL    NZ,$0F38            ; {code.L0F38}
0F2B: 2C              INC     L                   
0F2C: 2C              INC     L                   
0F2D: 3E B0           LD      A,$B0               
0F2F: BD              CP      L                   
0F30: C2 23 0F        JP      NZ,$0F23            ; {code.L0F23}
0F33: C9              RET                         
; 
0F34: FF FF FF FF
; 
L0F38:
0F38: 2C              INC     L                   
0F39: 7E              LD      A,(HL)              
0F3A: 2D              DEC     L                   
0F3B: FE D2           CP      $D2                 
0F3D: D8              RET     C                   
0F3E: FE E7           CP      $E7                 
0F40: D0              RET     NC                  
0F41: 7E              LD      A,(HL)              
0F42: B9              CP      C                   
0F43: D0              RET     NC                  
0F44: B8              CP      B                   
0F45: D8              RET     C                   
0F46: CD C4 0C        CALL    $0CC4               ; {code.L0CC4}
0F49: 11 04 0D        LD      DE,$0D04            
0F4C: 2B              DEC     HL                  
0F4D: 2B              DEC     HL                  
0F4E: C3 AD 0E        JP      $0EAD               ; {code.L0EAD}
; Ghost code bytes from an older version.
; The code was probably shortened at this point during development and the following bytes were not specifically deleted.
0F51: AD 0E FF FF FF

; 'alien with player' collision check.
; All parts of the player ship object are checked for a collision with aliens.
L0F56:
0F56: C5              PUSH    BC                  ; 
0F57: D5              PUSH    DE                  ; 
L0F58:
0F58: 1A              LD      A,(DE)              ; get upper left character of player ship
0F59: FE 60           CP      $60                 ; alien characters ($60 to $BF)
0F5B: DA 63 0F        JP      C,$0F63             ; {code.L0F63} if no collision on left side
0F5E: FE C0           CP      $C0                 ; 
0F60: DA F4 0C        JP      C,$0CF4             ; {code.L0CF4} if collision on left or right side
L0F63:
0F63: 13              INC     DE                  ; get upper right character of player ship
0F64: 05              DEC     B                   ; 
0F65: C2 58 0F        JP      NZ,$0F58            ; {code.L0F58}
0F68: D1              POP     DE                  ; 
0F69: C1              POP     BC                  ; 
0F6A: CD 17 02        CALL    $0217               ; {code.RightOneColumn} for lower part of player ship
0F6D: 0D              DEC     C                   ; 
0F6E: C2 56 0F        JP      NZ,$0F56            ; {code.L0F56}
0F71: C9              RET                         ; 
; 
0F72: FF FF
;
L0F74:
0F74: 2E E2           LD      L,$E2               ; PlayerShipMSB
0F76: 56              LD      D,(HL)              
0F77: 2C              INC     L                   ; PlayerShipLSB
0F78: 5E              LD      E,(HL)              
0F79: CD 17 02        CALL    $0217               ; {code.RightOneColumn}
0F7C: 1B              DEC     DE                  
0F7D: 01 04 04        LD      BC,$0404            
0F80: CD 56 0F        CALL    $0F56               ; {code.L0F56}
0F83: C8              RET     Z                   
0F84: 00              NOP                         
0F85: 00              NOP                         
0F86: 3A C2 43        LD      A,($43C2)           ; {ram.PlayerShipX}
0F89: D6 0E           SUB     $0E                 
0F8B: 47              LD      B,A                 
0F8C: C6 2D           ADD     $2D                 
0F8E: 4F              LD      C,A                 
0F8F: 21 70 4B        LD      HL,$4B70            ; {+ram.M4B70}
L0F92:
0F92: 7E              LD      A,(HL)              
0F93: 2C              INC     L                   
0F94: 2C              INC     L                   
0F95: E6 08           AND     $08                 ; 0000_1000
0F97: C4 A6 0F        CALL    NZ,$0FA6            ; {code.L0FA6}
0F9A: 2C              INC     L                   
0F9B: 2C              INC     L                   
0F9C: 3E B0           LD      A,$B0               
0F9E: BD              CP      L                   
0F9F: C2 92 0F        JP      NZ,$0F92            ; {code.L0F92}
0FA2: C9              RET                         
; 
0FA3: FF FF FF
; 
L0FA6:
0FA6: 2C              INC     L                   
0FA7: 7E              LD      A,(HL)              
0FA8: 2D              DEC     L                   
0FA9: FE CA           CP      $CA                 
0FAB: D8              RET     C                   
0FAC: FE EF           CP      $EF                 
0FAE: D0              RET     NC                  
0FAF: 7E              LD      A,(HL)              
0FB0: B9              CP      C                   
0FB1: D0              RET     NC                  
0FB2: B8              CP      B                   
0FB3: D8              RET     C                   
0FB4: 11 02 0D        LD      DE,$0D02            
0FB7: 2B              DEC     HL                  
0FB8: 2B              DEC     HL                  
0FB9: C3 AD 0E        JP      $0EAD               ; {code.L0EAD}
; Ghost code bytes from an older version.
; The code was probably shortened at this point during development and the following bytes were not specifically deleted.
0FBC: AD 0E FF FF

;*****************************************************************************
;* Handle animations for killed aliens
;*****************************************************************************
L0FC0:
0FC0: 21 70 43        LD      HL,$4370            ; {+ram.M4370}
0FC3: CD D8 0F        CALL    $0FD8               ; {code.L0FD8}
0FC6: 21 74 43        LD      HL,$4374            ; {+ram.M4374}
0FC9: CD D8 0F        CALL    $0FD8               ; {code.L0FD8}
0FCC: 21 78 43        LD      HL,$4378            ; {+ram.M4378}
0FCF: CD 58 37        CALL    $3758               ; {code.L3758}
0FD2: 21 7C 43        LD      HL,$437C            ; {+ram.M437C}
0FD5: C3 58 37        JP      $3758               ; {code.L3758}
; 
L0FD8:
0FD8: 7E              LD      A,(HL)              
0FD9: A7              AND     A                   ; updates the zero flag
0FDA: C8              RET     Z                   
0FDB: 46              LD      B,(HL)              
0FDC: 35              DEC     (HL)                
0FDD: 2C              INC     L                   
0FDE: 2C              INC     L                   
0FDF: 56              LD      D,(HL)              
0FE0: 2C              INC     L                   
0FE1: 5E              LD      E,(HL)              
0FE2: 00              NOP                         
0FE3: CD 10 02        CALL    $0210               ; {code.LeftOneColumn}
0FE6: 78              LD      A,B                 
0FE7: E6 0E           AND     $0E                 ; 0000_1110
0FE9: 0F              RRCA                        
0FEA: C6 B0           ADD     $B0                 
0FEC: 6F              LD      L,A                 
0FED: 26 17           LD      H,$17               
0FEF: 6E              LD      L,(HL)              
0FF0: EB              EX      DE,HL               
0FF1: 01 DF FF        LD      BC,$FFDF            ; Screen offset constant -33 right one column (-1), up one row (-32)
0FF4: C3 40 35        JP      $3540               ; {code.Draw3x2}

; not used 
0FF7: 68              LD      L,B                 
0FF8: 3E 05           LD      A,$05               
0FFA: 32 96 43        LD      ($4396),A           ; {ram.M4396}
0FFD: C3 A4 0E        JP      $0EA4               ; {code.L0EA4}

; Pointer table to alien movement list (T1700):
; Value * 2 ==> LSB of T1700
; This is the default movement pattern for the alien formation:
; Right, right, right, right, left, left, left, left, 
; left, left, left, left, right, right, right, right, 
; end mark. Used at phase 0, 1, 2 and 3.
T1000:
1000: 01 01 01 01 02 02 02 02 02 02 02 02 01 01 01 01
1010: 00

; not used
1011: FF FF FF FF FF FF FF FF
1019: FF FF FF FF FF FF FF

; Closed loop pattern table part 1:
; Used for single or multiple aliens, depending on the game round.
; Pattern 1
T1020:
1020: 10 11 12 13 10 1D 0D 0E 0B 0C 0D 0E 0B 0C 06 06
1030: 1E 03 1F 05 1C 04 1D 06 1E 03 03 03 03 03 1F 1C
1040: 1D 1E 03 03 03 03 03 1F 05 1C 04 1D 06 1E 03 1F
1050: 05 05 05 05 05 05 05 05 05 05 1C 04 04 11 12 13
1060: 00
; not used
1061: FF FF FF
; Pattern 2
T1064:
1064: 0B 1E 19 06 06 06 06 06 06 1E 1F 1C 1D 06 06 06
1074: 06 06 1E 03 1F 05 1C 04 1D 06 06 1A 04 1B 05 18
1084: 19 06 1A 04 1B 05 05 1C 04 1D 06 1E 03 1F 05 05
1094: 05 05 05 1C 1D 1E 1F 05 05 05 05 05 05 05 18 1F
10A4: 00
10A5: FF FF FF
; Pattern 3 (phase 3)
T10A8:
10A8: 10 04 04 1D 0D 0E 0B 0C 0D 0E 01 01 01 01 01 01
10B8: 01 01 05 05 05 05 05 1C 04 04 1D 06 06 1E 03 03
10C8: 1F 05 05 05 1C 11 12 13
10D0: 00
10D1: FF FF FF
; Pattern 4
T10D4:
10D4: 0B 0C 0D 0E 0B 0C 0D 0E 0B 0C 1A 1B 05 18 19 06
10E4: 0D 0E 01 01 01 01 01 01 01 01 05 05 1C 1B 05 05
10F4: 1C 04 1B 05 05 1C 04 1B
10FC: 00
10FD: FF FF FF
; Pattern 5
T1100:
1100: 0B 0C 0D 0E 0B 0C 09 09 09 09 0A 0A 09 09 0A 09
1110: 16 17 14 07 07 07 1C 04 1D 06 1E 03 1F 05 1C 08
1120: 08 08 08 08 08 08 08 05 05 05 05
112B: 00
112C: FF FF FF FF
; Pattern 6
T1130:
1130: 0B 0C 0D 0E 0B 0C 0A 0A 0A 0A 09 09 0A 0A 09 0A
1140: 12 13 10 08 08 08 18 07 07 07 07 05 1C 04 1D 06
1150: 1E 03 1F 07 07 07 07 05 05 05 05
115B: 00
115C: FF FF FF FF
; Pattern 7
T1160:
1160: 1C 04 04 04 1D 06 0D 0E 0B 0C 06 06 1E 15 16 17
1170: 14 19 06 1A 04 1D 06 1E 03 19 06 1A 04 1D 1E 03
1180: 1F 1C 04 1B 05 18 03 1F 05 1C 04 1B 05 18 03 15
1190: 16 17 14 1F 05 05 05 05 05 05 05 1C 04 1D 1A 1B
11A0: 00
11A1: FF FF FF
; Pattern 8
T11A4:
11A4: 0B 0C 0D 0E 0B 0C 0D 0E 0B 0C 0D 0E 02 02 02 02
11B4: 02 02 02 02 05 05 18 03 19 1A 04 1B 05 18 03 1F
11C4: 05 18 03 1F 05 05 18 1F
11CC: 00
11CD: FF FF FF
; Pattern 9
T11D0:
11D0: 0B 0C 0D 0E 0B 0C 06 06 09 09 09 0A 09 09 0A 09
11E0: 09 09 06 1A 04 11 12 13 10 08 08 08 07 07 07 08
11F0: 08 08 05 05 05 05 05 05 05 05 05 05 05
11FD: 00
11FE: FF FF
; Pattern 10
T1200:
1200: 1C 11 12 13 10 04 1D 0D 0E 0B 0C 0D 0E 0B 0C 1E
1210: 1F 05 18 19 0D 0E 0B 0C 1E 1F 05 05 05 05 05 18
1220: 19 0D 0E 0B 0C 06 1E 1F 05 05 05 05 18 19 06 1E
1230: 1F 05 05 05 05 05 05 05 05 1C 04 04 1D 1A 04 1B
1240: 00
1241: FF FF FF
; Pattern 11
T1244:
1244: 18 03 03 19 06 06 06 06 06 06 06 06 06 06 06 06
1254: 1A 04 1B 05 1C 04 1D 06 1E 03 03 19 06 1A 04 04
1264: 04 1B 05 18 03 03 1F 05 1C 04 1D 06 1A 04 1B 05
1274: 05 05 05 05 05 05 05 05 05 05 05 18 03 19 1E 1F
1284: 00
1285: FF FF FF
; Pattern 12
T1288:
1288: 0B 0C 1A 1D 1E 03 19 06 1A 04 04 1D 06 1E 03 03
1298: 03 19 06 06 1A 04 04 04 04 1D 06 06 1E 03 03 03
12A8: 03 03 03 1F 05 05 1C 04 04 04 04 1B 05 05 18 03
12B8: 03 03 1F 05 1C 04 04 1B 05 18 03 1F 1C 1B 05 05
12C8: 00
12C9: FF
; Pattern 13
T12CA:
12CA: 18 03 19 06 06 06 06 06 06 1A 1D 1E 19 1A 1D 06
12DA: 1E 19 06 1E 15 16 17 14 07 07 07 08 08 08 08 05
12EA: 05 18 03 03 19 06 06 1A 04 04 1B 08 08 08 08 05
12FA: 05 05 05 18 1F
12FF: 00
; Pattern 14
T1300:
1300: 0B 0C 0A 0A 09 09 09 0A 0A 09 09 09 0A 09 09 16
1310: 17 14 07 07 07 08 08 08 08 07 07 08 08 08 08 07
1320: 08 11 12 13
1324: 00
1325: FF FF FF
; Pattern 15
T1328:
1328: 0B 0C 09 09 0A 09 09 0A 0A 0A 0A 09 0A 0A 0A 12
1338: 13 10 04 04 04 1B 18 03 03 07 07 08 08 07 07 08
1348: 08 07 07 07 07 07
134E: 00
134F: FF FF FF FF FF
; Pattern 16
T1354:
1354: 1C 11 12 13 10 1D 0D 0E 0B 0C 09 0A 09 09 0A 09
1364: 09 09 06 1A 04 1B 05 18 03 19 09 09 0D 0E 0B 0C
1374: 0D 0E 02 02 02 02 02 02 02 02 02 02 02 02 08 07
1384: 07 08 07 07 08 08 07 07 07 07 07 05 05 05 05 05
1394: 05 1C 11 12 13
1399: 00
139A: FF FF
; Pattern 17
T139C:
139C: 0B 0C 0D 0E 0B 0C 0D 0E 0B 0C 1A 1D 06 1E 19 06
13AC: 06 1A 04 1B 1C 04 1D 1A 04 1B 1C 04 1D 1A 04 1B
13BC: 05 18 07 07 07 08 08 07 07 07 07 08 08 07 07 07
13CC: 07
13CD: 00
13CE: FF FF
; Pattern 18
T13D0:
13D0: 14 03 19 0D 0E 0B 0C 0A 0A 0A 09 0A 0A 0A 09 0A
13E0: 0A 0A 06 1E 15 16 17 14 03 1F 05 05 08 07 07 07
13F0: 08 07 07 07 08 08 05 05 05 05 05
13FB: 00
13FC: FF FF FF FF

; Player ship character block shapes table
; used for fine bit shifting of the player
T1400:
1400: 30 40 31 41     ;frame#1
1404: 32 42 33 43     ;frame#2
1408: 34 44 35 45     ;frame#3
140C: 36 46 37 47     ;frame#4
1410: 38 48 39 49     ;frame#5
1414: 3A 4A 3B 4B     ;frame#6
1418: 3C 4C 3D 4D     ;frame#7
141C: 3E 4E 3F 4F     ;frame#8

; Alien character block shapes table ($00=SPACE)
T1420:
1420: 60 61           ;alien shape #1
1422: 62 63           ;#2
1424: 64 65           ;#3
1426: 66 67           ;#4
1428: 69 00           ;#6
142A: 69 00           ;#6
142C: 7A 7B           ;#28
142E: 7A 7B           ;#28
1430: 6B 00           ;#8
1432: 6B 00           ;#8
1434: 8C 8D           ;#29
1436: 8C 8D           ;#29
1438: 68 00           ;#5
143A: 68 00           ;#5
143C: 8A 9A           ;#30
143E: 8A 9A           ;#30
1440: 6A 00           ;#7
1442: 6A 00           ;#7
1444: 8B 9B           ;#31
1446: 8B 9B           ;#31
1448: 68 00           ;#5
144A: 6B 00           ;#8
144C: 6A 00           ;#7
144E: 69 00           ;#6
1450: 76 77           ;#18
1452: 74 75           ;#19
1454: 72 73           ;#16
1456: 70 71           ;#17
1458: 68 00           ;#5
145A: 86 96           ;#22
145C: 69 00           ;#6
145E: 87 97           ;#21
1460: 6A 00           ;#7
1462: 88 98           ;#20
1464: 6B 00           ;#8
1466: 89 99           ;#23
1468: 68 00           ;#5
146A: 00 00
146C: A2 B2 A3 B3     ;#26
1470: 69 00           ;#6
1472: 00 00
1474: A4 B4 A5 B5     ;#25
1478: 6A 00           ;#7
147A: 00 00
147C: A6 B6 A7 B7     ;#24
1480: 6B 00           ;#8
1482: 00 00
1484: A8 B8 A9 B9     ;#27
1488: FF FF FF FF
148C: 8A 9A           ;#30
148E: 00 00
1490: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
14A0: 8B 9B           ;#31
14A2: 00 00
14A4: FF FF FF FF
14A8: 8E 9E 8F 9F     ;#14
14AC: A0 B0 A1 B1     ;#15
14B0: 00 00 00 00
14B4: FF FF FF FF FF FF FF FF FF FF FF FF
14C0: 9C 00           ;#32
14C2: 00 00
14C4: 84 94 85 95     ;#36
14C8: 82 92 83 93     ;#35
14CC: 80 90 81 91     ;#34
14D0: 9D 00 00 00     ;#33
14D4: AE BE AF BF     ;#39
14D8: AC BC AD 00     ;#38
14DC: AA BA AB BB     ;#37

;
L14E0:
14E0: 47              LD      B,A                 ; save A
14E1: 3A 00 78        LD      A,($7800)           ; {hard.DSW0} 78xx DSW0
14E4: E6 10           AND     $10                 ; 0001_0000 Coinage
14E6: C8              RET     Z                   ; return if no coins entered
14E7: EB              EX      DE,HL               ; 
14E8: 7A              LD      A,D                 ; 
14E9: FE 18           CP      $18                 ; 
14EB: C0              RET     NZ                  ; 
14EC: 7B              LD      A,E                 ; 
14ED: FE 95           CP      $95                 ; 
14EF: 36 22           LD      (HL),$22            ; 
14F1: C8              RET     Z                   ; 
14F2: FE 9A           CP      $9A                 ; 
14F4: 36 13           LD      (HL),$13            ; 
14F6: C8              RET     Z                   ; 
14F7: FE B5           CP      $B5                 ; 
14F9: 36 24           LD      (HL),$24            ; 
14FB: C8              RET     Z                   ; 
14FC: 70              LD      (HL),B              ; 
14FD: C9              RET                         ; 
;
14FE: FF FF

; Copied inside $4B70-$4BAF.
; Init values for the alien control states A and B.
T1500:
1500: 08 6C 09 60 
1504: 08 6C 09 60 
1508: 08 6C 09 60 
150C: 08 6C 09 60 
1510: 08 6C 09 60 
1514: 08 6C 09 60 
1518: 08 6C 09 60 
151C: 09 60 09 60 

; Init values for 16 aliens.
; Pointer to alien movement pattern table.
T1520:
1520: 10 00 
1522: 10 00 
1524: 10 00 
1526: 10 00 
1528: 10 00 
152A: 10 00 
152C: 10 00 
152E: 10 00 
1530: 10 00 
1532: 10 00 
1534: 10 00 
1536: 10 00 
1538: 10 00 
153A: 10 00 
153C: 10 00 
153E: 10 00 

; Level 2 initial screen coordinates for the aliens.
; First byte is X, 2nd byte is Y. There are 16 aliens
; on the level (numbered here 0 - F). The starts are shown
; on the screen below.
;
;      0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 A A B B C C
;      0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8
;      | | | | | | | | | | | | | | | | | | | | | | | | | |
; 00 - . S C O R E 1 . . H I - S C O R E . . S C O R E 2 . 
; 08 - . 0 0 0 0 0 0 . . . 0 0 0 0 0 0 . . . 0 0 0 0 0 0 .
; 10 - . . . * 1 . . . . . C O I N 0 0 . . . . . * 0 . . .
; 18 - . . . . . . . . . . . . . . . . . . . . . . . . . .
; 20 - . . . . . . . . . . 0 . . . 1 . . . . . . . . . . .
; 28 - . . . . . . . . . . . . 2 . . . . . . . . . . . . .
; 30 - . . . . . . 8 . . . . . . . . . . . 9 . . . . . . .
; 38 - . . . . A . . . 6 . . . 3 . . . 7 . . . B . . . . .
; 40 - . . . . . . . . . . 4 . . . 5 . . . . . . . . . . .
; 48 - . . . C . . . . . . . . E . . . . . . . . D . . . .
; 50 - . . . . . . . . . . . . . . . . . . . . . . . . . .
; 58 - . . . . . . . . . . . . F . . . . . . . . . . . . .
;
T1540:
1540: 50 20     ; 0 : x,y = 50,20 (decimal 80,32)
1542: 70 20     ; 1  
1544: 60 28     ; 2 
1546: 60 38     ; 3  
1548: 50 40     ; 4  
154A: 70 40     ; 5 
154C: 40 38     ; 6 
154E: 80 38     ; 7 
1550: 30 30     ; 8 
1552: 90 30     ; 9 
1554: 20 38     ; A 
1556: A0 38     ; B 
1558: 18 48     ; C
155A: A8 48     ; D
155C: 60 48     ; E
155E: 60 58     ; F

; Level 1 initial screen coordinates for the aliens.
; Same structure as 1540 above.
;
;      0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 A A B B C C
;      0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8
;      | | | | | | | | | | | | | | | | | | | | | | | | | |
; 00 - . S C O R E 1 . . H I - S C O R E . . S C O R E 2 . 
; 08 - . 0 0 0 0 0 0 . . . 0 0 0 0 0 0 . . . 0 0 0 0 0 0 .
; 10 - . . . * 1 . . . . . C O I N 0 0 . . . . . * 0 . . .
; 18 - . . . . . . . . . . . . . . . . . . . . . . . . . .
; 20 - . . . . . . . E . . . . . . . . . F . . . . . . . .
; 28 - . . . . . C . . . . . . . . . . . . . D . . . . . .
; 30 - . . . A . . . . . . . . . . . . . . . . . B . . . .
; 38 - . . . . . . . . . . . . . . . . . . . . . . . . . .
; 40 - . . . 8 . . . . . . . . . . . . . . . . . 9 . . . .
; 48 - . . . . . 6 . . . . . . 0 . . . . . . 7 . . . . . .
; 50 - . . . . . . . 4 . . . . . . . . . 5 . . . . . . . .
; 58 - . . . . . . . . . 2 . . 1 . . 3 . . . . . . . . . .
;
T1560:
1560: 60 48     ; 0
1562: 60 58     ; 1
1564: 48 58     ; 2
1566: 78 58     ; 3
1568: 38 50     ; 4
156A: 88 50     ; 5
156C: 28 48     ; 6
156E: 98 48     ; 7
1570: 18 40     ; 8
1572: A8 40     ; 9
1574: 18 30     ; A
1576: A8 30     ; B
1578: 28 28     ; C
157A: 98 28     ; D
157C: 38 20     ; E
157E: 88 20     ; F

;level 10 initial screen coordinates for the aliens.
;      0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 A A B B C C
;      0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8
;      | | | | | | | | | | | | | | | | | | | | | | | | | |
; 20 - . . . . . . . . . . 1 . 0 . 2 . . . . . . . . . . .
; 28 - . . . . . . . . 3 . . . . . . . 4 . . . . . . . . .
; 30 - . . . . . . 5 . . . . . . . . . . . 6 . . . . . . .
; 38 - . . . . 7 . . . . . . . . . . . . . . . 8 . . . . .
; 40 - . . . . . . . . . . . . . . . . . . . . . . . . . .
; 48 - . . . . . . . . . . . . . . . . . . . . . . . . . .
; 50 - . . . . . . . . . . . . . . . . . . . . . . . . . .
; 58 - . . . . . . E . C . A . 9 . B . D . F . . . . . . .
;
T1580:
1580: 60 20     ; 0
1582: 50 20     ; 1
1584: 70 20     ; 2
1586: 40 28     ; 3
1588: 80 28     ; 4
158A: 30 30     ; 5
158C: 90 30     ; 6
158E: 20 38     ; 7
1590: A0 38     ; 8
1592: 60 58     ; 9
1594: 50 58     ; A
1596: 70 58     ; B
1598: 40 58     ; C
159A: 80 58     ; D
159C: 30 58     ; E
159E: 90 58     ; F

;level 7 initial screen coordinates for the aliens.
;      0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 A A B B C C
;      0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8
;      | | | | | | | | | | | | | | | | | | | | | | | | | |
; 20 - . . . . . . . . . . . . 0 . . . . . . . . . . . . .
; 28 - . . . . . . . . . . 1 . . . 2 . . . . . . . . . . .
; 30 - . . . . . . . . 3 . . . . . . . 4 . . . . . . . . .
; 38 - . . . . . . 5 . . . . . . . . . . . 6 . . . . . . .
; 40 - . . . . 7 . . . . . . . . . . . . . . . 8 . . . . .
; 48 - . . . . . . E . . . . . . . . . . . F . . . . . . .
; 50 - . . . . . . . . C . . . . . . . D . . . . . . . . .
; 58 - . . . . . . . . . . A . 9 . B . . . . . . . . . . .
;
T15A0:
15A0: 60 20     ; 0
15A2: 50 28     ; 1
15A4: 70 28     ; 2
15A6: 40 30     ; 3
15A8: 80 30     ; 4
15AA: 30 38     ; 5
15AC: 90 38     ; 6
15AE: 20 40     ; 7
15B0: A0 40     ; 8
15B2: 60 58     ; 9
15B4: 50 58     ; A
15B6: 70 58     ; B
15B8: 40 50     ; C
15BA: 80 50     ; D
15BC: 30 48     ; E
15BE: 90 48     ; F

;level 6 initial screen coordinates for the aliens.
;      0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 A A B B C C
;      0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8
;      | | | | | | | | | | | | | | | | | | | | | | | | | |
; 20 - . . E . . . . . . . . . . . . . . . . . . . F . . .
; 28 - . . . . C . . . . . . . . . . . . . . . D . . . . .
; 30 - . . . . . . A . . . . . . . . . . . B . . . . . . .
; 38 - . . . . . . . . 8 . . . . . . . 9 . . . . . . . . .
; 40 - . . . . . . . . . . 6 . . . 7 . . . . . . . . . . .
; 48 - . . . . . . . . 4 . . . 3 . . . 5 . . . . . . . . .
; 50 - . . . . . . . . . . 1 . . . 2 . . . . . . . . . . .
; 58 - . . . . . . . . . . . . 0 . . . . . . . . . . . . .
;
T15C0:
15C0: 60 58     ; 0
15C2: 50 50     ; 1
15C4: 70 50     ; 2
15C6: 60 48     ; 3
15C8: 40 48     ; 4
15CA: 80 48     ; 5
15CC: 50 40     ; 6
15CE: 70 40     ; 7
15D0: 40 38     ; 8
15D2: 80 38     ; 9
15D4: 30 30     ; A
15D6: 90 30     ; B
15D8: 20 28     ; C
15DA: A0 28     ; D
15DC: 10 20     ; E
15DE: B0 20     ; F

;level 5 initial screen coordinates for the aliens.
;      0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 A A B B C C
;      0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8 0 8
;      | | | | | | | | | | | | | | | | | | | | | | | | | |
; 20 - . . . . . . . . . . . . 0 . . . . . . . . . . . . .
; 28 - . . . . . . . . . . 1 . . . 2 . . . . . . . . . . .
; 30 - . . . . . . . . 3 . . . . . . . 4 . . . . . . . . .
; 38 - . . . . . . 5 . . . . . . . . . . . 6 . . . . . . .
; 40 - . . . . 7 . . . . . . . . . . . . . . . 8 . . . . .
; 48 - . . . . . . . . . . . . . . . . . . . . . . . . . .
; 50 - . . . . . . . . . . . . . . . . . . . . . . . . . .
; 58 - . . . . . . . . . . . . . . . . . . . . . . . . . .
T15E0:
15E0: 60 20     ; 0
15E2: 50 28     ; 1
15E4: 70 28     ; 2
15E6: 40 30     ; 3
15E8: 80 30     ; 4
15EA: 30 38     ; 5
15EC: 90 38     ; 6
15EE: 20 40     ; 7
15F0: A0 40     ; 8
15F2: 60 20     ; 9 (two aliens at same position)
15F4: 50 28     ; A (two aliens at same position)
15F6: 70 28     ; B (two aliens at same position)
15F8: 40 30     ; C (two aliens at same position)
15FA: 80 30     ; D (two aliens at same position)
15FC: 30 38     ; E (two aliens at same position)
15FE: 90 38     ; F (two aliens at same position)

; Pointer table for character block shapes table (T14xx):
T1600:
1600: 10 14 18 1C             ; to player ship frame #5, #6, #7, #8
1604: 00 04 08 0C             ; to player ship frame #1, #2, #3, #4
1608: 20 22 24 26             ; to alien shape #1, #2, #3, #4
160C: 28 2A 2C 2E             ; to alien shape #6, #6, #28, #28
1610: 30 32 34 36             ; to alien shape #8, #8, #29, #29
1614: 38 3A 3C 3E             ; to alien shape #5, #5, #30, #30
1618: 40 42 44 46             ; to alien shape #7, #7, #31, #31
161C: 5C 5C 5E 5E             ; to alien shape #6, #6, #21, #21

; 8 player bullets for the fine bit shifting.
; Foreground tiles (no pointer).
T1620:
1620: 50 51 52 53 54 55 56 57
;
1628: FF FF FF FF FF FF FF FF

; Pointer table for character block shapes table (T14xx):
1630: 48 48 50 50             ; to alien shape #5, #5, #18, #18
1634: 4A 4A 52 52             ; to alien shape #8, #8, #19, #19
1638: 4C 4C 54 54             ; to alien shape #7, #7, #16, #16
163C: 4E 4E 56 56             ; to alien shape #6, #6, #17, #17
1640: 48 48 56 56             ; to alien shape #5, #5, #17, #17
1644: 4E 4E 54 54             ; to alien shape #6, #6, #16, #16
1648: 4C 4C 52 52             ; to alien shape #7, #7, #19, #19
164C: 4A 4A 50 50             ; to alien shape #8, #8, #18, #18

1650: 68 68 6C 6C             ; to alien shape #5, #5, #26, #26
1654: 70 70 74 74             ; to alien shape #6, #6, #25, #25
1658: 78 78 7C 7C             ; to alien shape #7, #7, #24, #24
165C: 80 80 84 84             ; to alien shape #8, #8, #27, #27
1660: 68 68 84 84             ; to alien shape #5, #5, #27, #27
1664: 80 80 7C 7C             ; to alien shape #8, #8, #24, #24
1668: 78 78 74 74             ; to alien shape #7, #7, #25, #25
166C: 70 70 6C 6C             ; to alien shape #6, #6, #26, #26

1670: 58 58 5A 5A             ; to alien shape #5, #5, #22, #22
1674: 5C 5C 5E 5E             ; to alien shape #6, #6, #21, #21
1678: 60 60 62 62             ; to alien shape #7, #7, #20, #20
167C: 64 64 66 66             ; to alien shape #8, #8, #23, #23

1680: 78 FF A0 FF FF A8 FF AC ; to alien shape #7, #31, #14, #15
1688: C0 FF C8 FF FF C4 FF CC ; to alien shape #32, #35, #36, #34
1690: D0 FF D8 FF FF D4 FF DC ; to alien shape #33, #38, #39, #37
;
1698: FF FF FF FF FF FF FF FF

; Alien animation table.
; 1st byte: bit0-3 of alien control state A:
;           xxxx_x000...draw 1x1 screen objects
;           xxxx_x001...draw 2x1 screen objects
;           xxxx_x011...draw 1x2 screen objects
;           xxxx_x100...draw 2x2 screen objects
; 2nd byte: type of offset calculation:
;           xxxx_xxx1...use X and Y coordinate
;           xxxx_xx10...use X coordinate
;           xxxx_x100...use Y coordinate
; 3rd byte: LSB base address for table T1600
T16A0:
16A0: FF FF FF                ; Dummy
16A3: 01 02 08                ; 2x1 screen object, X , T1608
16A6: 01 02 08                ; 2x1 screen object, X , T1608
16A9: 01 02 0C                ; 2x1 screen object, X , T160C
16AC: 01 02 10                ; 2x1 screen object, X , T1610

16AF: 03 04 14                ; 1x2 screen object,  Y, T1614
16B2: 03 04 18                ; 1x2 screen object,  Y, T1618

16B5: 04 01 88                ; 2x2 screen object, XY, T1688
16B8: 04 01 90                ; 2x2 screen object, XY, T1690
16BB: 04 01 80                ; 2x2 screen object, XY, T1680
16BE: 04 01 80                ; 2x2 screen object, XY, T1680

16C1: 03 04 70                ; 1x2 screen object,  Y, T1670
16C4: 03 04 74                ; 1x2 screen object,  Y, T1674
16C7: 03 04 78                ; 1x2 screen object,  Y, T1678
16CA: 03 04 7C                ; 1x2 screen object,  Y, T167C

16CD: FF FF FF                ; Dummy

16D0: 01 02 30                ; 2x1 screen object, X , T1630
16D3: 01 02 34                ; 2x1 screen object, X , T1634
16D6: 01 02 38                ; 2x1 screen object, X , T1638
16D9: 01 02 3C                ; 2x1 screen object, X , T163C
16DC: 01 02 40                ; 2x1 screen object, X , T1640
16DF: 01 02 44                ; 2x1 screen object, X , T1644
16E2: 01 02 48                ; 2x1 screen object, X , T1648
16E5: 01 02 4C                ; 2x1 screen object, X , T164C

16E8: 04 04 50                ; 2x2 screen object,  Y, T1650
16EB: 04 04 54                ; 2x2 screen object,  Y, T1654
16EE: 04 04 58                ; 2x2 screen object,  Y, T1658
16F1: 04 04 5C                ; 2x2 screen object,  Y, T165C
16F4: 04 04 60                ; 2x2 screen object,  Y, T1660
16F7: 04 04 64                ; 2x2 screen object,  Y, T1664
16FA: 04 04 68                ; 2x2 screen object,  Y, T1668
16FD: 04 04 6C                ; 2x2 screen object,  Y, T166C

; Alien movement direction table.
; Positive or negative offset for X and Y.
T1700:
1700: FF FF                   ; Dummy
1702: 01 00                   ; X+1 (right), Y+0
1704: FF 00                   ; X-1 (left), Y+0
1706: 04 00                   ; X+4, Y+0
1708: FC 00                   ; X-4, Y+0
170A: 00 FC                   ; X+0, Y-4 (up)
170C: 00 04                   ; X+0, Y+4 (down)
170E: 04 FE                   ; X+4, Y-2
1710: FC FE                   ; X-4, Y-2
1712: 04 02                   ; X+4, Y+2
1714: FC 02                   ; X-4, Y+2
1716: 00 04                   ; X+0, Y+4
1718: 00 04                   ; X+0, Y+4
171A: 00 04                   ; X+0, Y+4
171C: 00 04                   ; X+0, Y+4
171E: FF FF                   ; X-1, Y-1
1720: FC 00                   ; X-4, Y+0
1722: FC 00                   ; X-4, Y+0
1724: FC 00                   ; X-4, Y+0
1726: FC 00                   ; X-4, Y+0
1728: 04 00                   ; X+4, Y+0
172A: 04 00                   ; X+4, Y+0
172C: 04 00                   ; X+4, Y+0
172E: 04 00                   ; X+4, Y+0
1730: 04 FC                   ; X+4, Y-4
1732: 04 04                   ; X+4, Y+4
1734: FC 04                   ; X-4, Y+4
1736: FC FC                   ; X-4, Y-4
1738: FC FC                   ; X-4, Y-4
173A: FC 04                   ; X-4, Y+4
173C: 04 04                   ; X+4, Y+4
173E: 04 FC                   ; X+4, Y-4

;?
T1740:
1740: 08 00 00 FF 01 00 F8 FF 08 01 02 FF 04 00 FA FF ;
1750: 08 01 04 FF 08 00 FC FF 08 05 06 FF 08 00 FE FF ;

; Parity table and initial number of aliens/birds for levels:
; odd, odd, even (P), even (P), odd, odd, odd, odd
; used with $43B8 LevelAndRound.
T1760:
1760: 10 10 88 88 10 10 10 10 ; 
;
1768: FF FF FF FF FF FF FF FF ;
;
T1770:
1770: EC FC FD F4 ED 30 40 F5 EE 31 41 F6 EF FF FE F7 ; [Object 1770](fgtiles.html#object-1770) Regular ship, large shields
1780: E8 F8 F9 F0 E9 30 40 F1 EA 31 41 F2 EB FB FA F3 ; [Object 1780](fgtiles.html#object-1780) Regular ship, small shields
1790: E8 F8 F9 F0 E9 E4 E6 F1 EA E5 E7 F2 EB FB FA F3 ; [Object 1790](fgtiles.html#object-1790) Green ship, large shields
17A0: 00 00 00 00 00 E4 E6 00 00 E5 E7 00 00 00 00 00 ; [Object 17A0](fgtiles.html#object-17a0) Green ship, no shields

;
17B0: F0 CA C4 BE B8 BE B8 BE ; LSB's of the Alien explosion frame sequence (#5,#4,#3,#2,#1,#2,#1,#2) why wrong order?
;
17B8: C8 D8 C9 D9 CA DA ; [Object 17B8](fgtiles.html#object-17b8) 3x2 Alien explosion frame #1
17BE: CB DB CC DC CD DD ; [Object 17BE](fgtiles.html#object-17be) 3x2 Alien explosion frame #2
17C4: C0 C1 C1 C2 00 C0 ; [Object 17C4](fgtiles.html#object-17c4) 3x2 Alien explosion frame #3
17CA: 00 00 00 C3 00 00 ; [Object 17CA](fgtiles.html#object-17ca) 3x2 Alien explosion frame #4
;
T17D0:
17D0: C4 D4 C5 D5 C3 C3 ; [Object 17D0](fgtiles.html#object-17d0) 3x2 Bonus explosion left part
T17D6:
17D6: C3 C3 C6 D6 C7 D7 ; [Object 17D6](fgtiles.html#object-17d6) 3x2 Bonus explosion right part
;
17DC: FF FF FF FF ;
;
;
CoinChecking:
17E0: 3A 00 78        LD      A,($7800)           ; {hard.DSW0} 78xx DSW0
17E3: E6 10           AND     $10                 ; 0001_0000 Coinage
17E5: 3A 8F 43        LD      A,($438F)           ; {ram.CoinCount}
17E8: C8              RET     Z                   
17E9: 0F              RRCA                        
17EA: E6 0F           AND     $0F                 ; 0000_1111
17EC: C9              RET                         
;
17ED: FF FF FF

; Used for blank out characters
; and Alien explosion frame #5
FourByFourEmpty:
17F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

; Screen ram adresses and static texts using setA
T1800:
1800: 43 20
1802: FF FF FF FF
; " SCORE1  HI-SCORE  SCORE2 "
1806: 00 13 03 0F 12 05 21 00 00 08 09 2B 13 03 0F 12 05 00 00 13 03 0F 12 05 22 00

1820: 43 21
1822: FF FF FF FF
; " 000000   000000   000000 "
1826: 00 20 20 20 20 20 20 00 00 00 20 20 20 20 20 20 00 00 00 20 20 20 20 20 20 00

1840: 43 22
1842: FF FF FF FF
; "   %0     COIN00     %0   "
1846: 00 00 00 7F 20 00 00 00 00 00 03 0F 09 0E 20 20 00 00 00 00 00 7F 20 00 00 00

T1860:
1860: 43 25
1862: FF FF FF FF
; "       INSERT  COIN       "
1866: 00 00 00 00 00 00 00 09 0E 13 05 12 14 00 00 03 0F 09 0E 00 00 00 00 00 00 00

1880: 43 27
1882: FF FF FF FF
; "   * 1PLAYER   1COIN  *   "
1886: 00 00 00 1F 00 21 10 0C 01 19 05 12 00 00 00 21 03 0F 09 0E 00 00 1F 00 00 00

18A0: 43 29
18A2: FF FF FF FF
; "   * 2PLAYERS  2COINS *   "
18A6: 00 00 00 1F 00 22 10 0C 01 19 05 12 13 00 00 22 03 0F 09 0E 13 00 1F 00 00 00

18C0: 43 2E
18C2: FF FF FF FF
; "   SCORE AVERAGE TABLE    "
18C6: 00 00 00 13 03 0F 12 05 00 01 16 05 12 01 07 05 00 14 01 02 0C 05 00 00 00 00

18E0: 43 30
18E2: FF FF FF FF
; "        20 40 80          "
18E6: 00 00 00 00 00 00 00 00 22 20 00 24 20 00 28 20 00 00 00 00 00 00 00 00 00 00

1900: 43 33
1902: FF FF FF FF
; "        200               "
1906: 00 00 00 00 00 00 00 00 22 20 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

1920: 43 36
1922: FF FF FF FF
; "        50 100 ?[100-800] "
1926: 00 00 00 00 00 00 00 00 25 20 00 21 20 20 00 2F 1B 21 20 20 2B 28 20 20 1C 00

1940: 43 39
1942: FF FF FF FF
; "        1000-9000         "
1946: 00 00 00 00 00 00 00 00 21 20 20 20 2B 29 20 20 20 00 00 00 00 00 00 00 00 00

T1960:
1960: 43 3C
1962: 00 00 32 21
; "PHOENIX% COPYRIGHT 1980   "
1966: 10 08 0F 05 0E 09 18 7E 00 03 0F 10 19 12 09 07 08 14 00 21 29 28 20 00 00 00

1980: 43 3D
1982: 02 05 21 28
; " AMSTAR ELECTRONICS CORP. "
1986: 00 01 0D 13 14 01
L198C:
198C: 12 00 05 0C 05 03 14 12 0F 0E 09 03 13 00 03 0F 12 10 2A 00

19A0: 43 3E
19A2: FF FF FF FF
; "  PHOENIX AZ. U.S.A.      "
19A6: 00 00 10 08 0F 05 0E 09 18 00 01 1A 2A 00 15 2A 13 2A 01 2A 00 00 00 00 00 00

T19C0:
19C0: 43 28
19C2: FF FF FF FF
; "           PUSH           "
19C6: 00 00 00 00 00 00 00 00 00 00 00 10 15 13 08 00 00 00 00 00 00 00 00 00 00 00

19E0: 43 2C
19E2: FF FF FF FF
; "    ONLY 1PLAYER BUTTON   "
19E6: 00 00 00 00 0F 0E 0C 19 00 21 10 0C 01 19 05 12 00 02 15 14 14 0F 0E 00 00 00

T1A00:
1A00: 43 28
1A02: FF FF FF FF
; "        GAME  OVER        "
1A06: 00 00 00 00 00 00 00 00 07 01 0D 05 00 00 0F 16 05 12 00 00 00 00 00 00 00 00

1A20: 43 28
1A22: 00 FF FF FF
; "%%%%%%%%                %%"
1A26: 64 65 64 65 64 65 60 61 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 78 79

1A40: 43 29
1A42: FF FF FF FF
; "%%    %%                %%"
1A46: 64 65 00 00 00 00 64 65 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 7C 7D

1A60: 43 2A
1A62: FF FF FF FF
; "%%%%%%%%                  "
1A66: 64 65 64 65 64 65 60 61 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

1A80: 43 2B
1A82: FF FF FF FF
; "%%                        "
1A86: 64 65 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

1AA0: 43 2C
1AA2: FF FF FF FF
; "%% % % %%% %%% %% % % %  %"
1AA6: 64 65 00 68 00 68 00 68 68 68 00 68 64 65 00 62 63 00 68 00 68 00 68 00 00 68

1AC0: 43 2D
1AC2: FF FF FF FF
; "%% % % % % %   %% % % %%%%"
1AC6: 64 65 00 68 00 68 00 68 00 68 00 68 00 00 00 68 9D 00 68 00 68 00 76 77 70 71

1AE0: 43 2E
1AE2: FF FF FF FF
; "%% %%% % % %%% %%%% %  %% "
1AE6: 64 65 00 68 68 68 00 68 00 68 00 68 62 63 00 68 76 77 68 00 68 00 00 64 65 00

1B00: 43 2F
1B02: 00 00 00 00
; "%% % % % % %   % %% % %%%%"
1B06: 64 65 00 68 00 68 00 68 00 68 00 68 00 00 00 68 00 9D 68 00 68 00 74 75 72 73

1B20: 43 30
1B22: FF FF FF FF
; "%% % % %%% %%% % %% % %  %"
1B26: 64 65 00 68 00 68 00 68 68 68 00 68 64 65 00 68 00 66 67 00 68 00 68 00 00 68

;alien character block shapes table using setA (for fade in)
T1B40:
1B40: 6C              ;#9
1B41: 6D              ;#10
1B42: 6E              ;#11
1B43: 6F              ;#12
;
1B44: FF FF FF FF

;character block shapes table using setB
;parts of the mothership's purple conveyor belt
T1B48:
1B48: 6C 6D 6E 6F 64 65 66 67 63 FF
1B52: 63 61 67 FF
1B56: 67 65 6B FF
1B5A: 6B 69 6F FF
1B5E: 6F 6D

;characters used for explosions using setB
T1B60:
1B60: 80 83 83 85 81 8C 8C 86 81 8C 8C 86 82 84 84 87
1B70: 00 89 89 00 88 8D 8D 8B 88 8D 8D 8B 00 8A 8A 00
1B80: 00 00 00 00 00 80 85 00 00 82 87 00 00 00 00 00

;adress table for instumentation of explosion
T1B90:
1B90: 1B 80
1B92: 1B 70
1B94: 1B 60
1B96: 1B 70
1B98: 17 F0                         ;for deletion
1B9A: 17 F0                         ;
1B9C: 17 F0                         ;
1B9E: 17 F0                         ;

;characters using setA: '1 OR 2 PLAYERS BUTTON'
T1BA0:
1BA0: 43 2C                         ; screen ram position
1BA2: 00 00 00 00 00 00 00 21 00 0F 12 00 22 10
1BB0: 0C 01 19 05 12 13 00 02 15 14 14 0F 0E 00 00 00

;characters using setB for animation of the mothership's
;.....antenna animation and the
;...........alien pilot animation
T1BC0:
1BC0: 41 54 76 7E   ; frame 0
1BC4: 42 55 77 7F   ; 
1BC8: 41 56 74 7C   ; frame 1
1BCC: 42 57 75 7D   ; 
1BD0: 44 51 72 7A   ; frame 2
1BD4: 45 52 73 7B   ; 
1BD8: 46 51 70 78   ; frame 3
1BDC: 47 52 71 79   ; 
1BE0: 41 51 70 78   ; frame 4
1BE4: 42 52 71 79   ; 
1BE8: 41 51 72 7A   ; frame 5
1BEC: 42 52 73 7B   ; 
1BF0: 41 51 74 7C   ; frame 6
1BF4: 42 52 75 7D   ; 
1BF8: 41 51 76 7E   ; frame 7
1BFC: 42 52 77 7F   ; 

;part of the starfield (without planets) using setB
; This is a 20x9 tile image used to erase the mothership
T1C00:
1C00: 00 01 00 06 00 02 03 04 00 01 00 08 00 02 03 04 00 00 07 00 
1C14: 01 02 00 09 00 03 04 00 00 03 04 00 00 01 00 02 00 03 0A 00 
1C28: 04 00 00 01 02 00 06 00 03 04 00 00 01 00 02 00 03 00 04 00 
1C3C: 03 05 00 00 00 00 07 00 01 00 02 00 00 05 00 00 03 00 04 01 
1C50: 02 00 03 00 08 04 00 01 02 06 00 03 00 04 00 02 01 02 03 00 
1C64: 05 00 00 04 00 01 02 00 00 03 04 0B 00 01 00 02 00 03 00 00 
1C78: 04 00 00 09 00 00 02 00 07 00 00 01 00 00 02 00 00 03 00 08 
1C8C: 04 00 01 00 00 06 00 01 00 02 00 01 03 04 01 03 01 02 03 04 
1CA0: 00 05 00 01 02 00 09 00 03 04 00 01 00 01 02 03 04 00 02 00 

1CB4: 00 01 02 00 03 04 00 06 00 00 01 00 
1CC0: 00 01 02 00 05 00 00 03 00 04 00 07 00 01 00 02 
1CD0: 00 00 03 00 04 00 04 00 0A 00 01 00 02 00 03 00 
1CE0: 01 00 07 00 02 00 03 04 00 05 00 01 00 02 00 00 
1CF0: 08 03 04 00 01 00 02 00 03 00 04 00 00 06 00 03 

; Mother ship object 26x9 tiles (upside down)
; [Object 1D00](bgtiles.html#object-1d00)
; Maybe these are upside down because the mother ship scrolls down from the top
; of the screen. The rows appear in the order given here.
T1D00:
1D00: 0C 0D 0C 0F 07 07 01 00 00 4C 4D 4E 4F 4F 4E 4D 4C 00 00 1F 0E 06 0D 01 0E 05 
1D1A: 08 0C 0E 0C 0A 00 00 4D 4F 5E 5E 5E 5E 5E 5E 5E 5E 4F 4D 00 00 06 0B 0D 08 0E 
1D34: 03 02 00 01 00 4C 4F 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 4F 4C 00 09 07 0A 03 
1D4E: 04 00 0A 00 4D 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 5E 4D 00 00 0E 0F 
1D68: 08 08 00 5C 60 6A 60 6A 60 6A 60 6A 60 6A 60 6A 60 6A 60 6A 60 6A 5D 00 01 02 
1D82: 02 06 01 00 00 00 58 59 5A 5B 5B 5B 7E 7F 5B 5B 5B 4A 49 48 00 00 00 03 0E 0B 
1D9C: 0D 05 04 05 0A 08 00 00 58 59 5A 4B 76 77 4B 4A 49 48 00 00 01 03 0F 02 03 00 
1DB6: 00 03 03 07 02 0A 03 07 00 00 58 50 51 52 53 48 00 00 0B 01 02 03 0F 0E 0C 02 
1DD0: 05 0C 06 00 04 06 07 0E 0F 09 00 40 41 42 43 00 07 03 0A 08 0D 00 09 0B 0C 0A 

1DEA: FF FF FF FF FF FF

;
; This is a simple protection against piracy.
L1DF0:
1DF0: 3A 1D 43        LD      A,($431D)           ; {ram.ForegroundScreen+31D} 'A' from 'AMSTAR ..' copyright text
1DF3: D6 01           SUB     $01                 ; 
1DF5: C8              RET     Z                   ; 
; crash the program and reset.
1DF6: 32 8F 43        LD      ($438F),A           ; {ram.CoinCount}
1DF9: 00              NOP                         ; 
1DFA: 00              NOP                         ; 
1DFB: 00              NOP                         ; 
1DFC: 00              NOP                         ; 
1DFD: 00              NOP                         ; 
1DFE: 00              NOP                         ; 
1DFF: 00              NOP                         ; 
;
;data for the 8 (2x2) planets / galaxies from setB
T1E00:
1E00: 20 30 21 31
1E04: 22 32 23 33
1E08: 24 34 25 35
1E0C: 26 36 27 37
1E10: 28 38 29 39
1E14: 2A 3A 2B 3B
1E18: 2C 3C 2D 3D
1E1C: 2E 3E 2F 3F
;MSB's of screen ram for planets / galaxies
T1E20:
1E20: 49 48 4A 4B
1E24: 4A 49 4A 49
1E28: 48 4A 48 49
1E2C: 4B 48 4A 48
1E30: 4A 49 4B 49
1E34: 4B 4A 49 48
1E38: 49 49 4A 4A
1E3C: 48 49 4A 48
;
T1E40:
1E40: A0 60 40 00
1E44: E0 C0 C0 60
1E48: 80 20 60 40
1E4C: 20 40 00 80
1E50: 40 00 20 E0
1E54: 00 60 00 A0
1E58: E0 20 80 00
1E5C: C0 80 A0 E0
;LSB's of screen ram for planets / galaxies
T1E60:
1E60: 00 04 08 0C
1E64: 10 14 18 1C
1E68: 00 08 10 18
1E6C: 04 0C 14 1C
1E70: 00 0C 18 04
1E74: 04 1C 08 14
1E78: 00 10 04 14
1E7C: 08 18 0C 1C
;data for the 16 (1x1) small galaxies from setB
T1E80:
1E80: 10 11 12 13
1E84: 14 15 16 17
1E88: 18 19 1A 1B
1E8C: 1C 1D 1E 1F
1E90: 10 12 14 16
1E94: 18 1A 1C 1E
1E98: 11 13 15 17
1E9C: 19 1B 1D 1F
;
T1EA0:
1EA0: 4A 4B 49 4A
1EA4: 48 4A 48 49
1EA8: 49 4A 49 4B
1EAC: 48 4B 4A 4A
1EB0: 48 49 48 4A
1EB4: 48 48 49 4A
1EB8: 49 49 4A 48
1EBC: 4A 49 4B 48
;
T1EC0:
1EC0: 00 20 60 40
1EC4: E0 80 20 60
1EC8: 40 A0 00 00
1ECC: 40 20 C0 20
1ED0: A0 80 E0 40
1ED4: 60 C0 20 A0
1ED8: E0 40 60 C0
1EDC: 20 40 20 80

;*****************************************************************************
;* Used for the animation speed at bird intro.
;*****************************************************************************
L1EE0:
1EE0: 11 3D 43        LD      DE,$433D            ; {+ram.ForegroundScreen+33D} holding 0
1EE3: 01 1A 00        LD      BC,$001A            ; 
L1EE6:
1EE6: 1A              LD      A,(DE)              ; 
1EE7: 80              ADD     A,B                 ; 
1EE8: 47              LD      B,A                 ; 
1EE9: CD 17 02        CALL    $0217               ; {code.RightOneColumn}
1EEC: 0D              DEC     C                   ; 
1EED: C2 E6 1E        JP      NZ,$1EE6            ; {code.L1EE6}
1EF0: 1A              LD      A,(DE)              ; 
1EF1: 80              ADD     A,B                 ; 
1EF2: C6 27           ADD     $27                 ; 
1EF4: 21 89 43        LD      HL,$4389            ; {+ram.HiScorehigh}
1EF7: 86              ADD     A,(HL)              ; 
1EF8: 77              LD      (HL),A              ; 
1EF9: 00              NOP                         ; 
1EFA: C9              RET                         ; 
;
1EFB: FF FF FF FF FF
;
; Part of the starfield background without planets
T1F00:
1F00: 00 00 00 01 00 00 00 02 00 00 00 00 03 00 00 00 
1F10: 00 04 00 00 00 00 01 00 00 00 05 00 02 00 03 00 
1F20: 00 00 04 00 07 00 00 00 06 00 01 00 02 0C 00 03 
1F30: 04 00 00 01 00 08 00 00 02 00 0C 03 04 0E 00 00 
1F40: 00 01 02 00 0D 03 04 0F 01 0C 07 0A 02 0D 03 08 
1F50: 06 0C 04 09 05 0F 01 02 0D 03 0C 04 0D 05 0F 0C 
1F60: 01 02 0E 0C 03 0F 0D 05 0E 0D 0C 0F 0D 04 0C 01 
1F70: 0E 05 0F 0D 07 0C 06 0E 0D 0F 09 0C 0F 0D 0E 0D 
1F80: 02 0D 0C 0F 05 0E 0D 0C 0F 06 0E 0F 0C 0D 0F 0C 
1F90: 06 0D 04 0B 0C 0F 05 0D 05 03 0E 07 0C 0D 04 05 
1FA0: 01 02 0E 03 0C 04 0F 05 08 0C 07 01 0D 04 0E 02 
1FB0: 0C 01 0F 03 05 0D 00 0E 00 09 0C 06 0D 00 01 02 
1FC0: 01 02 03 00 00 0D 00 0A 00 00 00 0E 00 05 00 08 
1FD0: 00 0C 00 00 03 00 00 07 00 00 00 04 00 00 06 00 
1FE0: 00 00 00 01 00 00 00 00 02 00 00 00 00 03 00 00 
1FF0: 00 04 00 05 00 00 00 00 00 01 00 00 00 00 02 00 

;*****************************************************************************
;* Game level 1, 3 and B:
;* 'player alife' with aliens, after 'fade in'
;*****************************************************************************
L2000:
2000: CD 76 08        CALL    $0876               ; {code.PlayerUpdate} Updates the player ship, player bullet and the shield.
2003: CD F0 0D        CALL    $0DF0               ; {code.L0DF0} alien bullet to player, collission detection ?
2006: CD A0 24        CALL    $24A0               ; {code.L24A0}
2009: 21 5F 43        LD      HL,$435F            ; {+ram.M435F} 8 bit counter for alien movement
200C: 7E              LD      A,(HL)              ; get value
200D: E6 03           AND     $03                 ; mask out 0000_0011 for count 0 to 3
200F: 47              LD      B,A                 ; save the masked counter
2010: 34              INC     (HL)                ; increment alien movement counter
2011: 3A BA 43        LD      A,($43BA)           ; {ram.AliensLeft}
2014: A7              AND     A                   ; updates the zero flag
2015: CA BA 21        JP      Z,$21BA             ; {code.L21BA} if no AliensLeft
2018: FE 05           CP      $05                 ; 
201A: D2 30 21        JP      NC,$2130            ; {code.L2130} if >= 5 left
201D: 2D              DEC     L                   ; $435E
201E: 78              LD      A,B                 ; get masked counter
201F: A7              AND     A                   ; updates the zero flag
2020: C2 25 20        JP      NZ,$2025            ; {code.L2025} if masked counter <> 0
2023: 36 FF           LD      (HL),$FF            ; set all bits at $435E
L2025:
2025: 7E              LD      A,(HL)              ; get $435E
2026: A7              AND     A                   ; updates the zero flag
2027: CA 30 21        JP      Z,$2130             ; {code.L2130} if $435E = 0
202A: C3 46 21        JP      $2146               ; {code.L2146}
; 
202D: FF FF FF
;
L2030:
2030: E6 03           AND     $03                 ; 0000_0011
2032: FE 01           CP      $01                 
2034: 11 50 1B        LD      DE,$1B50            
2037: C3 AC 23        JP      $23AC               ; {code.L23AC}
; 
203A: FF FF FF FF FF FF

;*****************************************************************************
;* Add 1x1 small galaxies to background.
;*****************************************************************************
AddGalaxiesToBackground:
2040: 21 AF 43        LD      HL,$43AF            ; {+ram.M43AF}
2043: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9}
2046: 4F              LD      C,A                 ; 
2047: BE              CP      (HL)                ; 
2048: C0              RET     NZ                  ; 
2049: 7E              LD      A,(HL)              ; 
204A: 2C              INC     L                   ; 
204B: 96              SUB     (HL)                ; 
204C: 2D              DEC     L                   ; 
204D: 77              LD      (HL),A              ; 
204E: 2C              INC     L                   ; 
204F: 2C              INC     L                   ; 
2050: 34              INC     (HL)                ; 
2051: 7E              LD      A,(HL)              ; 
2052: 21 80 1E        LD      HL,$1E80            ; {+code.T1E80} data for the 16 (1x1) small galaxies from setB
2055: E6 1F           AND     $1F                 ; 0001_1111
2057: 85              ADD     A,L                 ; 
2058: 6F              LD      L,A                 ; 
2059: 46              LD      B,(HL)              ; 
205A: C6 20           ADD     $20                 ; 
205C: 6F              LD      L,A                 ; 
205D: 56              LD      D,(HL)              ; 
205E: C6 20           ADD     $20                 ; 
2060: 6F              LD      L,A                 ; 
2061: 5E              LD      E,(HL)              ; 
2062: 79              LD      A,C                 ; 
2063: 0F              RRCA                        ; 
2064: 0F              RRCA                        ; 
2065: 0F              RRCA                        ; 
2066: E6 1F           AND     $1F                 ; 0001_1111
2068: 83              ADD     A,E                 ; 
2069: 3C              INC     A                   ; 
206A: 5F              LD      E,A                 ; 
206B: 78              LD      A,B                 ; 
206C: 12              LD      (DE),A              ; 
206D: C9              RET                         ; 

; not used 
206E: C9              RET                         
206F: FF
; 
L2070:
2070: 7B              LD      A,E                 
2071: D6 0A           SUB     $0A                 
2073: C6 C0           ADD     $C0                 
2075: 4F              LD      C,A                 
2076: 7A              LD      A,D                 
2077: CE 00           ADC     $00                 
2079: 47              LD      B,A                 
207A: 7E              LD      A,(HL)              
207B: 11 00 28        LD      DE,$2800            ; {+code.T2800} get the foreground tiles of the player ship particles explosion
207E: 21 00 29        LD      HL,$2900            ; {+code.T2900} and get the control data for it
2081: C3 85 20        JP      $2085               ; {code.L2085}
; 
2084: FF
; 
L2085:
2085: D6 20           SUB     $20                 
2087: 07              RLCA                        ; Multiply by 4 ..
2088: 07              RLCA                        ; ..
2089: 00              NOP                         
208A: E6 E0           AND     $E0                 ; 1110_0000
208C: 6F              LD      L,A                 
208D: 3E E0           LD      A,$E0               
208F: 95              SUB     L                   
2090: 6F              LD      L,A                 
L2091:
2091: 3E 3F           LD      A,$3F               
2093: 91              SUB     C                   
2094: 3E 43           LD      A,$43               
2096: 98              SBC     B                   
2097: D2 B0 20        JP      NC,$20B0            ; {code.L20B0}
209A: 23              INC     HL                  
209B: 23              INC     HL                  
209C: 7B              LD      A,E                 
209D: C6 10           ADD     $10                 
209F: 5F              LD      E,A                 
20A0: 79              LD      A,C                 
20A1: D6 20           SUB     $20                 
20A3: 4F              LD      C,A                 
20A4: 78              LD      A,B                 
20A5: DE 00           SBC     $00                 
20A7: 47              LD      B,A                 
20A8: C3 91 20        JP      $2091               ; {code.L2091}

20AB: FF FF FF FF FF

;*****************************************************************************
;* Player ship particles explosion.
;*****************************************************************************
L20B0:
20B0: C5              PUSH    BC                  
L20B1:
20B1: 7E              LD      A,(HL)              
20B2: E3              EX      (SP),HL             
20B3: 06 08           LD      B,$08               
L20B5:
20B5: 36 00           LD      (HL),$00            
20B7: 0F              RRCA                        
20B8: D2 BF 20        JP      NC,$20BF            ; {code.L20BF}
20BB: EB              EX      DE,HL               
20BC: 4E              LD      C,(HL)              
20BD: EB              EX      DE,HL               ; get data from $2800
20BE: 71              LD      (HL),C              
L20BF:
20BF: 23              INC     HL                  
20C0: 13              INC     DE                  
20C1: 05              DEC     B                   
20C2: C2 B5 20        JP      NZ,$20B5            ; {code.L20B5}
20C5: E3              EX      (SP),HL             
20C6: 23              INC     HL                  
20C7: 7D              LD      A,L                 
20C8: 0F              RRCA                        
20C9: DA B1 20        JP      C,$20B1             ; {code.L20B1}
20CC: 7D              LD      A,L                 
20CD: E6 1F           AND     $1F                 ; 0001_1111
20CF: CA E1 20        JP      Z,$20E1             ; {code.L20E1}
20D2: E3              EX      (SP),HL             
20D3: 7D              LD      A,L                 
20D4: D6 30           SUB     $30                 
20D6: 6F              LD      L,A                 
20D7: 7C              LD      A,H                 
20D8: DE 00           SBC     $00                 
20DA: 67              LD      H,A                 
20DB: E3              EX      (SP),HL             
20DC: FE 3F           CP      $3F                 
20DE: C2 B1 20        JP      NZ,$20B1            ; {code.L20B1}
L20E1:
20E1: C1              POP     BC                  
20E2: C9              RET                         
;
20E3: 20 FF FF FF FF
;
L20E8:
20E8: 47              LD      B,A                 
20E9: 7A              LD      A,D                 
20EA: C6 08           ADD     $08                 
20EC: 57              LD      D,A                 
20ED: CD 1C 21        CALL    $211C               ; {code.L211C}
20F0: 0F              RRCA                        
20F1: 0F              RRCA                        
20F2: 0F              RRCA                        
20F3: 83              ADD     A,E                 
20F4: E6 1F           AND     $1F                 ; 0001_1111
20F6: 4F              LD      C,A                 
20F7: 7B              LD      A,E                 
20F8: E6 E0           AND     $E0                 ; 1110_0000
20FA: B1              OR      C                   
20FB: 5F              LD      E,A                 
20FC: 78              LD      A,B                 
20FD: 0F              RRCA                        
20FE: 0F              RRCA                        
20FF: E6 0E           AND     $0E                 ; 0000_1110
2101: C6 90           ADD     $90                 
2103: 6F              LD      L,A                 
2104: 26 1B           LD      H,$1B               
2106: 7E              LD      A,(HL)              
2107: 2C              INC     L                   
2108: 6E              LD      L,(HL)              
2109: 67              LD      H,A                 
210A: 01 04 04        LD      BC,$0404            ; images are 4x4
210D: C3 D6 0A        JP      $0AD6               ; {code.DrawImageCbyB}

2110: FF FF FF FF FF FF FF FF FF FF FF FF
; 
L211C:
211C: 21 B9 43        LD      HL,$43B9            ; {+ram.CounterB9}
211F: 7E              LD      A,(HL)              
2120: FE 10           CP      $10                 
2122: D8              RET     C                   
2123: FE 30           CP      $30                 
2125: D0              RET     NC                  
2126: 3E 10           LD      A,$10               
2128: 77              LD      (HL),A              
2129: 32 00 58        LD      ($5800),A           ; {hard.scrollRegister} 58xx scroll register
212C: C9              RET                         
; 
212D: FF FF FF

; 
L2130:
2130: 78              LD      A,B                 ; get masked counter
2131: A7              AND     A                   ; updates the zero flag
2132: CA 50 21        JP      Z,$2150             ; {code.L2150} if = 0
2135: FE 01           CP      $01                 ; 
2137: CA 60 21        JP      Z,$2160             ; {code.L2160} if = 1
213A: FE 02           CP      $02                 ; 
213C: CA 70 21        JP      Z,$2170             ; {code.L2170} if = 2
213F: C3 80 21        JP      $2180               ; {code.L2180} counter = 3

; not used 
2142: 90              SUB     B                   
2143: A5              AND     L                   
2144: 50              LD      D,B                 
2145: 60              LD      H,B                 

; 
L2146:
2146: 78              LD      A,B                 
2147: 0F              RRCA                        
2148: D2 90 21        JP      NC,$2190            ; {code.L2190}
214B: C3 A5 21        JP      $21A5               ; {code.L21A5}

; not used 
214E: F0              RET     P                   
214F: F9              LD      SP,HL               

; masked counter = 0
L2150:
2150: CD 50 0A        CALL    $0A50               ; {code.AlienDataController} draw or delete alien
2153: CD 00 30        CALL    $3000               ; {code.AlienBehaviorUpdate}
2156: C3 00 0F        JP      $0F00               ; {code.L0F00} 'alien with player' collision check
; 
2159: FF FF FF FF FF FF FF

; masked counter = 1
L2160:
2160: CD C4 24        CALL    $24C4               ; {code.L24C4}
2163: CD 40 0C        CALL    $0C40               ; {code.EnemyBulletUpdate}
2166: CD 1C 0D        CALL    $0D1C               ; {code.AlienMovementUpdate}
2169: C3 C0 0F        JP      $0FC0               ; {code.L0FC0} Handle animations for killed aliens
; 
216C: FF FF FF  FF

; masked counter = 2
L2170:
2170: CD 70 0D        CALL    $0D70               ; {code.AlienAnimationUpdate}
2173: C3 60 25        JP      $2560               ; {code.L2560}
; 
2176: FF FF FF FF FF FF FF FF FF FF

; masked counter = 3
L2180:
2180: CD C4 24        CALL    $24C4               ; {code.L24C4}
2183: CD 40 0C        CALL    $0C40               ; {code.EnemyBulletUpdate}
2186: CD 6C 0A        CALL    $0A6C               ; {code.L0A6C} get screen ram adress for all aliens
2189: C3 C0 0F        JP      $0FC0               ; {code.L0FC0} Handle animations for killed aliens
; 
218C: FF FF FF FF
; 
L2190:
2190: CD 50 0A        CALL    $0A50               ; {code.AlienDataController} draw or delete alien
2193: CD 00 30        CALL    $3000               ; {code.AlienBehaviorUpdate}
2196: CD 00 0F        CALL    $0F00               ; {code.L0F00} 'alien with player' collision check
2199: CD 60 25        CALL    $2560               ; {code.L2560}
219C: C3 40 0C        JP      $0C40               ; {code.EnemyBulletUpdate}

219F: FF FF FF FF FF FF
; 
L21A5:
21A5: CD 1C 0D        CALL    $0D1C               ; {code.AlienMovementUpdate}
21A8: CD 70 0D        CALL    $0D70               ; {code.AlienAnimationUpdate}
21AB: CD 6C 0A        CALL    $0A6C               ; {code.L0A6C} get screen ram adress for all aliens
21AE: CD C0 0F        CALL    $0FC0               ; {code.L0FC0} Handle animations for killed aliens
21B1: C3 C4 24        JP      $24C4               ; {code.L24C4}

21B4: FF FF FF FF FF FF
; 
L21BA:
21BA: 78              LD      A,B                 ; 
21BB: 0F              RRCA                        ; 
21BC: D2 04 22        JP      NC,$2204            ; {code.L2204}
21BF: CD 40 0C        CALL    $0C40               ; {code.EnemyBulletUpdate}
21C2: CD C0 0F        CALL    $0FC0               ; {code.L0FC0} Handle animations for killed aliens
21C5: CD C4 24        CALL    $24C4               ; {code.L24C4}
21C8: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
21CB: E6 0F           AND     $0F                 ; mask out 0000_1111
21CD: FE 0B           CP      $0B                 ; 
21CF: DA 04 22        JP      C,$2204             ; {code.L2204} if < game level B
21D2: 3E 10           LD      A,$10               ; 16 aliens for a new wave
21D4: 32 BA 43        LD      ($43BA),A           ; {ram.AliensLeft}
21D7: C3 26 05        JP      $0526               ; {code.L0526} init alien data

21DA: FF FF

;*****************************************************************************
;* Handles the bird animation at intro.
;*****************************************************************************
DrawIntroBirdAnimationFrame:
21DC: 7E              LD      A,(HL)              ; {ram.M4399} Actual index for slow print at intro splash (starts with $300)
21DD: 00              NOP                         ; 
21DE: 47              LD      B,A                 ; save it
21DF: 21 73 4B        LD      HL,$4B73            ; {!+ram.B4B73} used as temp memory
21E2: E6 07           AND     $07                 ; mask out 0000_0111 in order to count from 0 to 7
21E4: 77              LD      (HL),A              ; save it
21E5: 2D              DEC     L                   ; 
21E6: 36 EF           LD      (HL),$EF            ; use $4B72 for LSB of screen ram
21E8: 2D              DEC     L                   ; 
21E9: 36 49           LD      (HL),$49            ; use $4B71 for MSB of screen ram
21EB: 2D              DEC     L                   ; $4B70 (bird0 index character block shape)
21EC: 78              LD      A,B                 ; restore $4399
21ED: E6 F8           AND     $F8                 ; mask out 1111_1000
21EF: 0F              RRCA                        ; Divide by 8 ..
21F0: 0F              RRCA                        ; ..
21F1: 0F              RRCA                        ; ..
21F2: C6 3A           ADD     $3A                 ; LSB of T233A
21F4: 5F              LD      E,A                 ; 
21F5: 16 23           LD      D,$23               ; MSB of T233A
21F7: 1A              LD      A,(DE)              ; get data starting at T233A for animation frame index
21F8: 77              LD      (HL),A              ; write to $4B70
21F9: CD C0 34        CALL    $34C0               ; {code.DrawBirdObject} draw the bird at intro
21FC: C3 E0 1E        JP      $1EE0               ; {code.L1EE0}
; 
21FF: FF FF FF FF FF
; 
L2204:
2204: 21 B6 43        LD      HL,$43B6            ; {+ram.M43B6}
2207: 35              DEC     (HL)                ; 
2208: 7E              LD      A,(HL)              ; 
2209: FE A0           CP      $A0                 ; 
220B: D0              RET     NC                  ; 
220C: 2E A4           LD      L,$A4               ; GameState
220E: 36 02           LD      (HL),$02            ; set GameState to: 'initialization of game and level data'
2210: 2E A6           LD      L,$A6               ; ShieldCount
2212: 36 00           LD      (HL),$00            ; clear ShieldCount
2214: 2E B8           LD      L,$B8               ; LevelAndRound
2216: 34              INC     (HL)                ; increment LevelAndRound
2217: 7E              LD      A,(HL)              ; 
2218: E6 0E           AND     $0E                 ; mask out 0000_1110
221A: 0F              RRCA                        ; divide by 2
221B: C6 60           ADD     $60                 ; add to base of table T1760
221D: 5F              LD      E,A                 ; 
221E: 16 17           LD      D,$17               ; 
2220: 2C              INC     L                   ; 
2221: 2C              INC     L                   ; AliensLeft
2222: 1A              LD      A,(DE)              ; get value from table T1760
2223: A7              AND     A                   ; updates the flags
2224: F2 2A 22        JP      P,$222A             ; {code.L222A} if not positive.
2227: 2C              INC     L                   ; use BirdsLeft
2228: E6 7F           AND     $7F                 ; mask out 0111_1111
; 
L222A:
222A: 77              LD      (HL),A              ; save to $43BA (AliensLeft) or $43BB (BirdsLeft)
222B: C3 80 03        JP      $0380               ; {code.ClearForeground}
; 
222E: FF FF

;*****************************************************************************
;* Game level 4, 6 and 8:
;* Do the 'spiral fill' animation.
;*****************************************************************************
L2230:
2230: 21 9C 43        LD      HL,$439C            ; {+ram.M439C}
2233: 7E              LD      A,(HL)              ; 
2234: 34              INC     (HL)                ; 
2235: 00              NOP                         ; 
2236: 0F              RRCA                        ; 
2237: E6 3F           AND     $3F                 ; mask out 0011_1111
2239: FE 0D           CP      $0D                 ; 
223B: CA 92 22        JP      Z,$2292             ; {+code.L2292}
223E: 06 1F           LD      B,$1F               ; The asterisk character
2240: DA 60 22        JP      C,$2260             ; {+code.L2260}
2243: 06 00           LD      B,$00               ; The space character
2245: D6 0E           SUB     $0E                 ; 
2247: FE 0D           CP      $0D                 ; 
2249: C2 60 22        JP      NZ,$2260            ; {+code.L2260}
224C: 21 B8 43        LD      HL,$43B8            ; {+ram.LevelAndRound}
224F: 34              INC     (HL)                ; increment game level $43B8
2250: 2E A4           LD      L,$A4               ; GameState
2252: 36 02           LD      (HL),$02            ; Next interval game state is 2: 'init game and level data'
2254: C9              RET                         ; 
; 
; not used
2255: 58              LD      E,B                 
2256: 2E A4           LD      L,$A4               
2258: 36 02           LD      (HL),$02            
225A: C9              RET                         
; 
225B: FF FF FF FF FF
; 
L2260:
2260: 4F              LD      C,A                 ; 
2261: 0F              RRCA                        ; 
2262: 0F              RRCA                        ; 
2263: 0F              RRCA                        ; 
2264: 57              LD      D,A                 ; 
2265: E6 1F           AND     $1F                 ; 0001_1111
2267: 5F              LD      E,A                 ; 
2268: 7A              LD      A,D                 ; 
2269: E6 E0           AND     $E0                 ; 1110_0000
226B: C6 B0           ADD     $B0                 ; 
226D: 6F              LD      L,A                 ; 
226E: 7B              LD      A,E                 ; 
226F: CE 41           ADC     $41                 ; 
2271: 67              LD      H,A                 ; 
2272: 7D              LD      A,L                 ; 
2273: 91              SUB     C                   ; 
2274: 6F              LD      L,A                 ; 
2275: 79              LD      A,C                 ; 
2276: 3C              INC     A                   ; 
2277: 4F              LD      C,A                 ; 
2278: 07              RLCA                        ; Multiply by 2
2279: 5F              LD      E,A                 ; 
; 
L227A:
227A: 51              LD      D,C                 ; D is the height counter for each pass
; 
L227B:
227B: 70              LD      (HL),B              ; draw the asterisk or space
227C: 23              INC     HL                  ; one row down
227D: 70              LD      (HL),B              ; another asterisk or space
227E: 23              INC     HL                  ; one row down
227F: 15              DEC     D                   ; all of this column done?
2280: C2 7B 22        JP      NZ,$227B            ; {+code.L227B} No ... do all rows
2283: 7D              LD      A,L                 ; LSB of screen pointer
2284: 91              SUB     C                   ; move up ...
2285: 91              SUB     C                   ; ... height * 2
2286: D6 20           SUB     $20                 ; Move right one column
2288: 6F              LD      L,A                 ; New LSB
2289: 7C              LD      A,H                 ; Borrow into ...
228A: DE 00           SBC     $00                 ; ... the ...
228C: 67              LD      H,A                 ; ... MSB
228D: 1D              DEC     E                   ; All columns done?
228E: C2 7A 22        JP      NZ,$227A            ; {+code.L227A} no ... do all columns
2291: C9              RET                         ; Done
; 
L2292:
2292: 21 B8 43        LD      HL,$43B8            ; {+ram.LevelAndRound}
2295: 7E              LD      A,(HL)              ; 
2296: E6 08           AND     $08                 ; mask out 0000_1000
2298: CA F0 22        JP      Z,$22F0             ; {+code.L22F0}
229B: 21 00 1C        LD      HL,$1C00            ; {+code.T1C00} Background stars to erase mother ship
229E: 11 3F 4B        LD      DE,$4B3F            ; End of background screen memory
22A1: 06 47           LD      B,$47               ; 
L22A3:
22A3: 7E              LD      A,(HL)              ; 
22A4: 12              LD      (DE),A              ; 
22A5: 2C              INC     L                   ; 
22A6: 1B              DEC     DE                  ; 
22A7: 7E              LD      A,(HL)              ; 
22A8: 12              LD      (DE),A              ; 
22A9: 2C              INC     L                   ; 
22AA: 1B              DEC     DE                  ; 
22AB: 78              LD      A,B                 ; 
22AC: BA              CP      D                   ; 
22AD: C2 A3 22        JP      NZ,$22A3            ; {+code.L22A3}
22B0: C3 E0 22        JP      $22E0               ; {code.L22E0}
; 
22B3: FF

;*****************************************************************************
;* Game level 9:
;* Mothership 'fade in' animation.
;*****************************************************************************
L22B4:
22B4: CD 7A 06        CALL    $067A               ; {code.StarsScrollDown}
22B7: 21 B4 43        LD      HL,$43B4            ; {+ram.CounterB4}
22BA: 35              DEC     (HL)                ; decrement CounterB4
22BB: 7E              LD      A,(HL)              ; get it
22BC: FE 28           CP      $28                 ; 
22BE: C2 48 08        JP      NZ,$0848            ; {code.L0848} if counter value not reached
22C1: 2E 67           LD      L,$67               ; 
22C3: 36 FF           LD      (HL),$FF            ; set flag for 'Mothership partially faded in'.
22C5: C9              RET                         ; 
; 
22C6: FF FF FF FF

;*****************************************************************************
;* Game level A:
;* Mothership and aliens 'fade in'
;*****************************************************************************
L22CA:
22CA: 21 B4 43        LD      HL,$43B4            ; {+ram.CounterB4}
22CD: 7E              LD      A,(HL)              ; 
22CE: FE C0           CP      $C0                 ; 
22D0: C2 34 08        JP      NZ,$0834            ; {code.L0834} Stars scrolling down and 'aliens fade in'
22D3: 36 30           LD      (HL),$30            ; 
22D5: 2E 67           LD      L,$67               ; 
22D7: 36 FF           LD      (HL),$FF            ; set flag for 'Mothership partially faded in'.
22D9: 2E BC           LD      L,$BC               ; 
22DB: 36 3F           LD      (HL),$3F            ; 
22DD: C9              RET                         ; 
; 
22DE: FF FF

; 
L22E0:
22E0: 3E 71           LD      A,$71               ; init the ...
; 
L22E2:
22E2: 32 B9 43        LD      ($43B9),A           ; {ram.CounterB9} free running 8 bit backwards counter
22E5: 32 00 58        LD      ($5800),A           ; {hard.scrollRegister} 58xx scroll register
22E8: C9              RET                         ; 
; 
22E9: FF FF FF FF FF FF FF

; 
L22F0:
22F0: CD A0 03        CALL    $03A0               ; {code.ClearBackground}
22F3: AF              XOR     A                   ; A=0
22F4: C3 E2 22        JP      $22E2               ; {code.L22E2}
; 
22F7: FF FF FF
; 
L22FA:
22FA: 21 AA 4A        LD      HL,$4AAA            ; {+ram.BackgroundScreen+2AA}
22FD: 06 12           LD      B,$12               
22FF: 3A 8A 48        LD      A,($488A)           ; {ram.BackgroundScreen+8A}
2302: 4F              LD      C,A                 
L2303:
2303: 79              LD      A,C                 
2304: E6 03           AND     $03                 ; 0000_0011
2306: 07              RLCA                        ; Multiply by 4 ..
2307: 07              RLCA                        ; ..
2308: 57              LD      D,A                 
2309: 4E              LD      C,(HL)              
230A: 79              LD      A,C                 
230B: E6 0C           AND     $0C                 ; 0000_1100
230D: 0F              RRCA                        
230E: 0F              RRCA                        
230F: B2              OR      D                   
2310: F6 60           OR      $60                 ; 0110_0000
2312: 77              LD      (HL),A              
2313: 7D              LD      A,L                 
2314: D6 20           SUB     $20                 
2316: 6F              LD      L,A                 
2317: D2 1B 23        JP      NC,$231B            ; {code.L231B}
231A: 25              DEC     H                   
L231B:
231B: 05              DEC     B                   
231C: C2 03 23        JP      NZ,$2303            ; {code.L2303}
231F: C9              RET                         
; 
2320: FF FF

;*****************************************************************************
;* Animation of the mothership's antenna and the alien pilot.
;*****************************************************************************
L2322:
2322: 21 A7 43        LD      HL,$43A7            ; {+ram.AnimationCounter}
2325: 34              INC     (HL)                ; increment the animation counter
2326: 7E              LD      A,(HL)              ; 
2327: E6 07           AND     $07                 ; mask out 0000_0111, in order to count from 0 to 7 for 8 frames
2329: 07              RLCA                        ; Multiply by 8 ..
232A: 07              RLCA                        ; ..to get..
232B: 07              RLCA                        ; ..the frame data adress (8 characters per frame)
232C: C6 C0           ADD     $C0                 ; LSB of T1BC0
232E: 6F              LD      L,A                 ; 
232F: 26 1B           LD      H,$1B               ; MSB of T1BC0
2331: 11 A6 49        LD      DE,$49A6            ; {+ram.BackgroundScreen+1A6} at the middle of the mothership
2334: 01 02 04        LD      BC,$0402            ; images are 2x4
2337: C3 D6 0A        JP      $0AD6               ; {code.DrawImageCbyB}
;
; Bird animation frame indexes at splash intro.
; Mapping to:?
T233A:
233A: 01 02 03 04 05 06 07 0A 07 0A 07 0A 07 0A 07 0A
234A: 09 08 04 03 02 01 FF
; 
L2351:
2351: 1A              LD      A,(DE)              
2352: E6 08           AND     $08                 ; 0000_1000
2354: C8              RET     Z                   
2355: 7E              LD      A,(HL)              
2356: 2C              INC     L                   
2357: 6E              LD      L,(HL)              
2358: C6 08           ADD     $08                 
235A: 67              LD      H,A                 
235B: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9}
235E: 0F              RRCA                        
235F: 0F              RRCA                        
2360: 0F              RRCA                        
2361: 85              ADD     A,L                 
2362: E6 1F           AND     $1F                 ; 0001_1111
2364: 47              LD      B,A                 
2365: 7D              LD      A,L                 
2366: E6 E0           AND     $E0                 ; 1110_0000
2368: B0              OR      B                   
2369: 6F              LD      L,A                 
236A: 7E              LD      A,(HL)              
236B: 47              LD      B,A                 
236C: E6 FC           AND     $FC                 ; 1111_1100
236E: FE 4C           CP      $4C                 
2370: CA 7B 23        JP      Z,$237B             ; {code.L237B}
2373: E6 F0           AND     $F0                 ; 1111_0000
2375: FE 60           CP      $60                 
2377: CA 98 23        JP      Z,$2398             ; {code.L2398}
237A: C9              RET                         
; 
L237B:
237B: 1A              LD      A,(DE)              
237C: E6 F7           AND     $F7                 ; 1111_0111
237E: 12              LD      (DE),A              
237F: 3E FF           LD      A,$FF               
2381: 32 66 43        LD      ($4366),A           ; {ram.M4366}
2384: 78              LD      A,B                 
2385: 3D              DEC     A                   
2386: 77              LD      (HL),A              
2387: FE 4B           CP      $4B                 
2389: C0              RET     NZ                  
238A: 36 00           LD      (HL),$00            
238C: 2D              DEC     L                   
238D: 7E              LD      A,(HL)              
238E: FE 5E           CP      $5E                 
2390: C0              RET     NZ                  
2391: 36 4F           LD      (HL),$4F            
2393: C9              RET                         

2394: FF FF FF FF
; 
L2398:
2398: 1A              LD      A,(DE)              
2399: E6 F7           AND     $F7                 ; 1111_0111
239B: 12              LD      (DE),A              
239C: 1C              INC     E                   
239D: 1C              INC     E                   
239E: 1A              LD      A,(DE)              
239F: E6 04           AND     $04                 ; 0000_0100
23A1: 78              LD      A,B                 
23A2: C2 30 20        JP      NZ,$2030            ; {code.L2030}
23A5: E6 0C           AND     $0C                 ; 0000_1100
23A7: FE 04           CP      $04                 
23A9: 11 40 1B        LD      DE,$1B40            
L23AC:
23AC: CA C0 23        JP      Z,$23C0             ; {code.L23C0}
23AF: 78              LD      A,B                 
23B0: E6 0F           AND     $0F                 ; 0000_1111
23B2: 83              ADD     A,E                 
23B3: 5F              LD      E,A                 
23B4: 1A              LD      A,(DE)              
23B5: 77              LD      (HL),A              
23B6: 3E FF           LD      A,$FF               
23B8: 32 66 43        LD      ($4366),A           ; {ram.M4366}
23BB: C9              RET                         

23BC: FF FF FF FF

L23C0:
23C0: 2D              DEC     L                   
23C1: 7E              LD      A,(HL)              
23C2: E6 F0           AND     $F0                 ; 1111_0000
23C4: FE 70           CP      $70                 
23C6: C0              RET     NZ                  
23C7: 21 A4 43        LD      HL,$43A4            ; {+ram.GameState} Next interval game state ...
23CA: 36 06           LD      (HL),$06            ; ... is 6 (mother ship partikel explosion)
23CC: 2C              INC     L                   ; CounterA5
23CD: 36 60           LD      (HL),$60            ; set counter value for
23CF: 2E 63           LD      L,$63               ; ParticleExplosion
23D1: 36 FF           LD      (HL),$FF            ; Set flag for: 'particle explosion start'
23D3: C9              RET                         ; 
; 
23D4: FF FF
; 
L23D6:
23D6: 21 B8 43        LD      HL,$43B8            ; {+ram.LevelAndRound}
23D9: 7E              LD      A,(HL)              ; 
23DA: E6 0F           AND     $0F                 ; mask out 0000_1111
23DC: FE 01           CP      $01                 ; 
23DE: CA 98 3A        JP      Z,$3A98             ; {code.L3A98} if game level is 1 (1st alien wave)
23E1: FE 03           CP      $03                 ; 
23E3: CA 98 3A        JP      Z,$3A98             ; {code.L3A98} if game level is 3 (2nd alien wave)
23E6: FE 05           CP      $05                 ; 
23E8: CA D0 3A        JP      Z,$3AD0             ; {code.L3AD0} if game level is 5 (1st bird wave)
23EB: FE 07           CP      $07                 ; 
23ED: CA D0 3A        JP      Z,$3AD0             ; {code.L3AD0} if game level is 7 (2nd bird wave)
23F0: FE 09           CP      $09                 ; 
23F2: D8              RET     C                   ; if game level is 9 (mothership 'fade in')
23F3: FE 0B           CP      $0B                 ; 
23F5: DA 02 3B        JP      C,$3B02             ; {code.L3B02} if game level is B (mothership)
23F8: CD 02 3B        CALL    $3B02               ; {code.L3B02}
23FB: C3 98 3A        JP      $3A98               ; {code.L3A98}
; 
23FE: FF FF

;*****************************************************************************
;* Game state 6.
;* Mother ship partikel explosion.
;*****************************************************************************
L2400:
2400: CD 2C 24        CALL    $242C               ; {code.L242C}
2403: CA 52 25        JP      Z,$2552             ; {code.L2552}
2406: FE 20           CP      $20                 
2408: DA 6A 24        JP      C,$246A             ; {code.EraseMothership}
240B: CA 20 25        JP      Z,$2520             ; {code.L2520} Calculation and display of the bonus score for mothership explosion
240E: 47              LD      B,A                 
240F: 0F              RRCA                        
2410: 00              NOP                         
2411: 78              LD      A,B                 
2412: D2 E8 20        JP      NC,$20E8            ; {code.L20E8}
2415: 7B              LD      A,E                 
2416: D6 05           SUB     $05                 
2418: C6 C0           ADD     $C0                 
241A: 4F              LD      C,A                 
241B: 7A              LD      A,D                 
241C: CE 00           ADC     $00                 
241E: 47              LD      B,A                 
241F: 7E              LD      A,(HL)              
2420: 11 00 2A        LD      DE,$2A00            ; {+code.T2A00} get the foreground tiles of the mothership particles explosion
2423: 21 00 2B        LD      HL,$2B00            ; {+code.T2B00} get the control data
2426: C3 85 20        JP      $2085               ; {code.L2085}

2429: FF FF FF
; 
L242C:
242C: 21 B9 43        LD      HL,$43B9            ; {+ram.CounterB9}
242F: 7E              LD      A,(HL)              
2430: E6 F8           AND     $F8                 ; 1111_1000
2432: 77              LD      (HL),A              
2433: 32 00 58        LD      ($5800),A           ; {hard.scrollRegister} 58xx scroll register
2436: 11 C6 41        LD      DE,$41C6            
2439: 0F              RRCA                        
243A: 0F              RRCA                        
243B: 0F              RRCA                        
243C: 47              LD      B,A                 
243D: 7B              LD      A,E                 
243E: 90              SUB     B                   
243F: E6 1F           AND     $1F                 ; 0001_1111
2441: 47              LD      B,A                 
2442: 7B              LD      A,E                 
2443: E6 E0           AND     $E0                 ; 1110_0000
2445: B0              OR      B                   
2446: 5F              LD      E,A                 
2447: 2E A5           LD      L,$A5               ; CounterA5
2449: 35              DEC     (HL)                ; decrement it
244A: 7E              LD      A,(HL)              
244B: C9              RET                         

;*****************************************************************************
;* Game state 7.
;* Mother ship score display.
;*****************************************************************************
L244C:
244C: 21 A5 43        LD      HL,$43A5            ; {+ram.CounterA5}
244F: 35              DEC     (HL)                ; 
2450: 7E              LD      A,(HL)              ; 
2451: 0F              RRCA                        ; 
2452: DA F0 06        JP      C,$06F0             ; {code.L06F0} update scroll register and fill background
2455: A7              AND     A                   ; updates the zero flag
2456: C0              RET     NZ                  ; 
2457: 2D              DEC     L                   ; 
2458: 36 02           LD      (HL),$02            ; 
245A: 2E B8           LD      L,$B8               ; LevelAndRound
245C: 7E              LD      A,(HL)              ; 
245D: E6 F0           AND     $F0                 ; 1111_0000
245F: C6 10           ADD     $10                 ; go to next round and ..
2461: 77              LD      (HL),A              ; .. store at LevelAndRound $43B8
2462: 2E BA           LD      L,$BA               ; AliensLeft
2464: 36 10           LD      (HL),$10            ; set AliensLeft to 16
2466: C3 80 03        JP      $0380               ; {code.ClearForeground}
; 
2469: FF

;
EraseMothership:
246A: 01 14 09        LD      BC,$0914            ; 20x9 image
246D: 11 C6 4A        LD      DE,$4AC6            ; Screen coordinate of mother ship
2470: 21 00 1C        LD      HL,$1C00            ; Background stars to erase the mother ship
2473: C3 D6 0A        JP      $0AD6               ; {code.DrawImageCbyB} Erase the mother ship
; 
L2476:
2476: 78              LD      A,B                 
2477: 81              ADD     A,C                 
2478: CD 95 24        CALL    $2495               ; {code.L2495}
247B: 2E D3           LD      L,$D3               ; $4BD3 (bird extended storage)
247D: 77              LD      (HL),A              
247E: 21 BB 43        LD      HL,$43BB            ; {+ram.BirdsLeft}
2481: 3E 08           LD      A,$08               ; number of birds
2483: 96              SUB     (HL)                ; 
2484: 07              RLCA                        ; Multiply by 2
2485: 2E 9A           LD      L,$9A               ; Counter9A
2487: 86              ADD     A,(HL)              
2488: 07              RLCA                        ; Multiply by 2
2489: 47              LD      B,A                 
248A: 2E 6F           LD      L,$6F               ; $436F
248C: 7E              LD      A,(HL)              
248D: E6 1E           AND     $1E                 ; 0001_1110
248F: 80              ADD     A,B                 
2490: 32 D1 4B        LD      ($4BD1),A           ; {!ram.B4BD1}
2493: C9              RET                         

; not used.
2494: 1F              RRA                         
; 
L2495:
2495: 80              ADD     A,B                 
2496: 0D              DEC     C                   
2497: C8              RET     Z                   
2498: 80              ADD     A,B                 
2499: 0D              DEC     C                   
249A: C8              RET     Z                   
249B: 80              ADD     A,B                 
249C: 0D              DEC     C                   
249D: C8              RET     Z                   
249E: 87              ADD     A,A                 
249F: C9              RET                         
; 
L24A0:
24A0: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
24A3: E6 0F           AND     $0F                 ; mask out 0000_1111
24A5: FE 08           CP      $08                 ; 
24A7: D8              RET     C                   ; return if game level < 8
24A8: 11 C4 43        LD      DE,$43C4            ; {+ram.PlayerBulletState}
24AB: 21 E6 43        LD      HL,$43E6            ; {+ram.AbovePlayerBulletMSB}
24AE: CD 51 23        CALL    $2351               ; {code.L2351}
24B1: 3A 9B 43        LD      A,($439B)           ; {ram.Counter9A+1}
24B4: E6 03           AND     $03                 ; mask out 0000_0011
24B6: FE 03           CP      $03                 ; 
24B8: C0              RET     NZ                  ; return if <> 3
24B9: C3 F2 24        JP      $24F2               ; {code.L24F2}

; not used 
24BC: CD 51 23        CALL    $2351               ; {code.L2351}
24BF: C9              RET                         

24C0: FF FF FF FF
; 
L24C4:
24C4: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
24C7: E6 0F           AND     $0F                 ; mask out 0000_1111
24C9: FE 08           CP      $08                 ; 
24CB: DA F0 06        JP      C,$06F0             ; {code.L06F0} update scroll register and fill background if game level < 8
24CE: CD E0 24        CALL    $24E0               ; {code.L24E0}
24D1: 21 AA 43        LD      HL,$43AA            ; {+ram.M43AA}
24D4: 34              INC     (HL)                ; 
24D5: 7E              LD      A,(HL)              ; 
24D6: E6 03           AND     $03                 ; mask out 0000_0011
24D8: CA FA 22        JP      Z,$22FA             ; {code.L22FA} if $43AA <> 3
24DB: C3 22 23        JP      $2322               ; {code.L2322} Animation of the mothership's antenna and the alien pilot

; not used
24DE: 24              INC     H                   
24DF: BF              CP      A                   

; 
L24E0:
24E0: 3A AA 43        LD      A,($43AA)           ; {ram.M43AA}
24E3: E6 0F           AND     $0F                 ; 0000_1111
24E5: C0              RET     NZ                  
24E6: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9}
24E9: FE A0           CP      $A0                 
24EB: D8              RET     C                   
24EC: C3 7A 06        JP      $067A               ; {code.StarsScrollDown}

; not used 
24EF: FA 22 C3        JP      M,$C322             
; 
L24F2:
24F2: CD AA 30        CALL    $30AA               ; {code.GetRandomNumber}
24F5: C6 60           ADD     $60                 
24F7: 00              NOP                         
24F8: 47              LD      B,A                 
24F9: 21 9B 43        LD      HL,$439B            ; {+ram.Counter9A+1}
24FC: E6 0E           AND     $0E                 ; 0000_1110
24FE: A6              AND     (HL)                
24FF: C0              RET     NZ                  
2500: 3A 9E 43        LD      A,($439E)           ; {ram.M439E}
2503: B8              CP      B                   
2504: D0              RET     NC                  
2505: 3A 9F 43        LD      A,($439F)           ; {ram.M439F}
2508: B8              CP      B                   
2509: D8              RET     C                   
250A: 78              LD      A,B                 
250B: D6 04           SUB     $04                 
250D: 47              LD      B,A                 
250E: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9}
2511: 2F              CPL                         
2512: 3C              INC     A                   
2513: E6 F8           AND     $F8                 ; 1111_1000
2515: C6 48           ADD     $48                 
2517: 4F              LD      C,A                 
2518: E5              PUSH    HL                  
2519: E5              PUSH    HL                  
251A: C3 B7 25        JP      $25B7               ; {code.L25B7}
; 
251D: FF FF FF

;*****************************************************************************
;* The 'alien pilot' at mothership was hit.
;* Calculation and display of the bonus score for mothership explosion.
;*****************************************************************************
L2520:
2520: D5              PUSH    DE                  ; 
2521: CD 80 03        CALL    $0380               ; {code.ClearForeground} remove all but the rest of the mothership
2524: D1              POP     DE                  ; 
2525: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9} get value from 8 bit backwards counter
2528: C6 60           ADD     $60                 ; use it for a ...
252A: 0F              RRCA                        ; ... score value
252B: 47              LD      B,A                 ; save it
252C: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
252F: E6 F0           AND     $F0                 ; mask out 1111_0000 (bit4 - 7: game round)
2531: 80              ADD     A,B                 ; add score value
2532: 06 90           LD      B,$90               ; 
2534: DA 3D 25        JP      C,$253D             ; {code.L253D}
2537: FE 90           CP      $90                 ; 
2539: D2 3D 25        JP      NC,$253D            ; {code.L253D} if >= $90
253C: 47              LD      B,A                 ; 
L253D:
253D: AF              XOR     A                   ; A=0
253E: 78              LD      A,B                 ; 
253F: 27              DAA                         ; adjust for BCD
2540: 21 9D 43        LD      HL,$439D            ; {+ram.M439D}
2543: 77              LD      (HL),A              ; set value for fist two digits of BCD score
2544: 2C              INC     L                   ; 
2545: 36 00           LD      (HL),$00            ; last two digits of BCD score set to '00'
2547: 7B              LD      A,E                 ; get LSB of screen ram...
2548: D6 5E           SUB     $5E                 ; ...
254A: 5F              LD      E,A                 ; ...
254B: 06 04           LD      B,$04               ; number of digits to print
254D: C3 C4 00        JP      $00C4               ; {code.PrintNumber} score for mothership explosion
; not used
2550: 32 80
; 
L2552:
2552: 2E A4           LD      L,$A4               ; GameState
2554: 36 07           LD      (HL),$07            ; set to 'mother ship score display'
2556: 2C              INC     L                   ; CounterA5
2557: 36 40           LD      (HL),$40            ; set it
2559: 2E 6B           LD      L,$6B               ; $436B
255B: 36 FF           LD      (HL),$FF            ; set flag for 'mother ship score display'
255D: C9              RET                         ; 

255E: FF FF

L2560:
2560: 21 93 43        LD      HL,$4393            ; {+ram.Counter93}
2563: 7E              LD      A,(HL)              
2564: E6 01           AND     $01                 ; 0000_0001
2566: 07              RLCA                        ; Multiply by 32 ..
2567: 07              RLCA                        ; ..
2568: 07              RLCA                        ; ..
2569: 07              RLCA                        ; ..
256A: 07              RLCA                        ; ..
256B: C6 70           ADD     $70                 
256D: 6F              LD      L,A                 
256E: 26 4B           LD      H,$4B               
2570: 1E 08           LD      E,$08               
2572: 3A 57 43        LD      A,($4357)           ; {ram.M4357}
2575: 07              RLCA                        ; Multiply by 8 ..
2576: 07              RLCA                        ; ..
2577: 07              RLCA                        ; ..
2578: 00              NOP                         
2579: C6 AD           ADD     $AD                 
257B: 57              LD      D,A                 
257C: 3A 9F 43        LD      A,($439F)           ; {ram.M439F}
257F: C6 03           ADD     $03                 
2581: 4F              LD      C,A                 
2582: 3A 9E 43        LD      A,($439E)           ; {ram.M439E}
2585: D6 0A           SUB     $0A                 
2587: 47              LD      B,A                 
L2588:
2588: E5              PUSH    HL                  
2589: CD 96 25        CALL    $2596               ; {code.L2596}
258C: E1              POP     HL                  
258D: 7D              LD      A,L                 
258E: C6 04           ADD     $04                 
2590: 6F              LD      L,A                 
2591: 1D              DEC     E                   
2592: C2 88 25        JP      NZ,$2588            ; {code.L2588}
2595: C9              RET                         
;
L2596:
2596: 7E              LD      A,(HL)              
2597: E6 08           AND     $08                 ; 0000_1000
2599: C8              RET     Z                   
259A: 2C              INC     L                   
259B: 7E              LD      A,(HL)              
259C: FE 08           CP      $08                 
259E: C8              RET     Z                   
259F: FE 88           CP      $88                 
25A1: D0              RET     NC                  
25A2: 2C              INC     L                   
25A3: 7E              LD      A,(HL)              
25A4: B8              CP      B                   
25A5: D8              RET     C                   
25A6: B9              CP      C                   
25A7: D0              RET     NC                  
25A8: 2C              INC     L                   
25A9: 7E              LD      A,(HL)              
25AA: BA              CP      D                   
25AB: D0              RET     NC                  
25AC: FE 80           CP      $80                 
25AE: D8              RET     C                   
25AF: 00              NOP                         
25B0: 00              NOP                         
25B1: 00              NOP                         
25B2: 00              NOP                         
25B3: 00              NOP                         
25B4: 4F              LD      C,A                 
25B5: 2D              DEC     L                   
25B6: 46              LD      B,(HL)              
L25B7:
25B7: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
25BA: 16 03           LD      D,$03               ; 
25BC: FE 10           CP      $10                 ; 0001_0000
25BE: DA CA 25        JP      C,$25CA             ; {code.L25CA} if game round < 1
25C1: 16 04           LD      D,$04               ; 
25C3: FE 20           CP      $20                 ; 0010_0000
25C5: DA CA 25        JP      C,$25CA             ; {code.L25CA} if game round < 2
25C8: 16 05           LD      D,$05               ; 
L25CA:
25CA: 21 CC 43        LD      HL,$43CC            ; {+ram.EnemyBullet0State}
L25CD:
25CD: 7E              LD      A,(HL)              ; 
25CE: E6 08           AND     $08                 ; mask out 0000_1000
25D0: CA E0 25        JP      Z,$25E0             ; {code.L25E0}
25D3: 7D              LD      A,L                 
25D4: C6 04           ADD     $04                 
25D6: 6F              LD      L,A                 
25D7: 15              DEC     D                   
25D8: C2 CD 25        JP      NZ,$25CD            ; {code.L25CD}
25DB: E1              POP     HL                  
25DC: E1              POP     HL                  
25DD: C9              RET                         

25DE: FF FF

L25E0:
25E0: 78              LD      A,B                 
25E1: C6 04           ADD     $04                 
25E3: 47              LD      B,A                 
25E4: 79              LD      A,C                 
25E5: C6 0C           ADD     $0C                 
25E7: 4F              LD      C,A                 
25E8: 36 08           LD      (HL),$08            
25EA: 2C              INC     L                   
25EB: 78              LD      A,B                 
25EC: 0F              RRCA                        
25ED: E6 03           AND     $03                 ; 0000_0011
25EF: 57              LD      D,A                 
25F0: 79              LD      A,C                 
25F1: E6 04           AND     $04                 ; 0000_0100
25F3: 82              ADD     A,D                 
25F4: C6 58           ADD     $58                 
25F6: 77              LD      (HL),A              
25F7: 2C              INC     L                   
25F8: 70              LD      (HL),B              
25F9: 2C              INC     L                   
25FA: 71              LD      (HL),C              
25FB: E1              POP     HL                  
25FC: E1              POP     HL                  
25FD: C9              RET                         

25FE: FF FF

;*****************************************************************************
;* Birds vertical movement update (with 58xx scroll register).
;*****************************************************************************
L2600:
2600: 00              NOP                         ; Old command removed or space for a future replace patch
2601: 00              NOP                         ; ..
2602: 00              NOP                         ; ..
2603: 00              NOP                         ; ..
2604: 00              NOP                         ; ..
2605: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9}
2608: 2F              CPL                         
2609: 0F              RRCA                        
260A: 0F              RRCA                        
260B: 0F              RRCA                        
260C: E6 1F           AND     $1F                 ; 0001_1111
260E: 21 D2 4B        LD      HL,$4BD2            ; {!+ram.B4BD2}
2611: 77              LD      (HL),A              
2612: 2C              INC     L                   
2613: 3A D1 4B        LD      A,($4BD1)           ; {!ram.B4BD1}
2616: BE              CP      (HL)                
2617: DA 50 26        JP      C,$2650             ; {code.L2650}
261A: 3A D5 4B        LD      A,($4BD5)           ; {!ram.B4BD5}
261D: 57              LD      D,A                 
261E: E6 03           AND     $03                 ; 0000_0011
2620: 5F              LD      E,A                 
2621: 3A 9B 43        LD      A,($439B)           ; {ram.Counter9A+1}
2624: 07              RLCA                        ; Multiply by 4 ..
2625: 07              RLCA                        ; ..
2626: E6 0C           AND     $0C                 ; 0000_1100
2628: 83              ADD     A,E                 
2629: C6 D0           ADD     $D0                 
262B: 6F              LD      L,A                 
262C: 26 3E           LD      H,$3E               
262E: 7A              LD      A,D                 
262F: 0F              RRCA                        
2630: 0F              RRCA                        
2631: E6 07           AND     $07                 ; 0000_0111
2633: 86              ADD     A,(HL)              
2634: 57              LD      D,A                 
2635: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9}
2638: 92              SUB     D                   
L2639:
2639: 32 B9 43        LD      ($43B9),A           ; {ram.CounterB9}
263C: 32 00 58        LD      ($5800),A           ; {hard.scrollRegister} 58xx scroll register
263F: 3A 9B 43        LD      A,($439B)           ; {ram.Counter9A+1}
2642: 0F              RRCA                        
2643: D2 D0 26        JP      NC,$26D0            ; {code.L26D0}
2646: CD 68 26        CALL    $2668               ; {code.L2668}
2649: C3 AA 26        JP      $26AA               ; {code.L26AA}

; not used 
264C: C2 3A 26 3A
;
L2650:
2650: 2C              INC     L                   ; 
2651: 3A 9B 43        LD      A,($439B)           ; {ram.Counter9A+1}
2654: 07              RLCA                        ; Multiply by 4 ..
2655: 07              RLCA                        ; ..
2656: E6 0C           AND     $0C                 ; 0000_1100
2658: 86              ADD     A,(HL)              
2659: C6 D0           ADD     $D0                 
265B: 6F              LD      L,A                 
265C: 26 3E           LD      H,$3E               
265E: 3A B9 43        LD      A,($43B9)           ; {ram.CounterB9}
2661: 86              ADD     A,(HL)              
2662: C3 39 26        JP      $2639               ; {code.L2639}
2665: D2 AE 26        JP      NC,$26AE            ; {code.L26AE}

;
L2668:
2668: 3A 6E 43        LD      A,($436E)           ; {ram.M436E}
266B: 00              NOP                         
266C: 47              LD      B,A                 
266D: 3A 9A 43        LD      A,($439A)           ; {ram.Counter9A}
2670: FE 18           CP      $18                 
2672: DA 76 26        JP      C,$2676             ; {code.L2676}
2675: 04              INC     B                   
L2676:
2676: FE 10           CP      $10                 
2678: DA 7C 26        JP      C,$267C             ; {code.L267C}
267B: 04              INC     B                   
L267C:
267C: 3A BA 43        LD      A,($43BA)           ; {ram.AliensLeft}
267F: FE 03           CP      $03                 
2681: D2 85 26        JP      NC,$2685            ; {code.L2685} if >= $03
2684: 04              INC     B                   
L2685:
2685: 3A D6 4B        LD      A,($4BD6)           ; {!ram.B4BD6}
2688: C6 E0           ADD     $E0                 
268A: 6F              LD      L,A                 
268B: 26 3E           LD      H,$3E               
268D: 78              LD      A,B                 
268E: BE              CP      (HL)                
268F: DA 93 26        JP      C,$2693             ; {code.L2693}
2692: 7E              LD      A,(HL)              
L2693:
2693: 57              LD      D,A                 
2694: 3A BB 43        LD      A,($43BB)           ; {ram.BirdsLeft}
2697: FE 04           CP      $04                 
2699: D2 9D 26        JP      NC,$269D            ; {code.L269D} if >= $04
269C: 14              INC     D                   
L269D:
269D: FE 02           CP      $02                 
269F: D2 A3 26        JP      NC,$26A3            ; {code.L26A3} if >= $02
26A2: 14              INC     D                   
L26A3:
26A3: 7A              LD      A,D                 
26A4: 32 D5 4B        LD      ($4BD5),A           ; {!ram.B4BD5}
26A7: C9              RET                         
; not used
26A8: 00              NOP                         
26A9: 58              LD      E,B                 
L26AA:
26AA: 21 D3 4B        LD      HL,$4BD3            ; {!+ram.B4BD3}
26AD: 7E              LD      A,(HL)              
L26AE:
26AE: 35              DEC     (HL)                
26AF: A7              AND     A                   ; updates the zero flag
26B0: C0              RET     NZ                  
26B1: 34              INC     (HL)                
26B2: 2E D6           LD      L,$D6               ; $4BD6
26B4: 7E              LD      A,(HL)              
26B5: FE 16           CP      $16                 
26B7: D0              RET     NC                  
26B8: FE 08           CP      $08                 
26BA: D8              RET     C                   
26BB: 2C              INC     L                   
26BC: 96              SUB     (HL)                
26BD: 07              RLCA                        ; Multiply by 2
26BE: 47              LD      B,A                 
26BF: 3A 6F 43        LD      A,($436F)           ; {ram.M436F}
26C2: E6 03           AND     $03                 ; 0000_0011
26C4: 2E D4           LD      L,$D4               ; $4BD4
26C6: 77              LD      (HL),A              
26C7: 2F              CPL                         
26C8: E6 03           AND     $03                 ; 0000_0011
26CA: 3C              INC     A                   
26CB: 4F              LD      C,A                 
26CC: C3 76 24        JP      $2476               ; {code.L2476}
; not used 
26CF: C9              RET                         
;
L26D0:
26D0: 21 A8 4B        LD      HL,$4BA8            ; {+ram.M4BA8}
26D3: 01 00 08        LD      BC,$0800            
26D6: 11 00 80        LD      DE,$8000            
L26D9:
26D9: 7E              LD      A,(HL)              
26DA: A7              AND     A                   ; updates the zero flag
26DB: CA E5 26        JP      Z,$26E5             ; {code.L26E5}
26DE: 7A              LD      A,D                 
26DF: 07              RLCA                        ; Multiply by 2
26E0: D2 E4 26        JP      NC,$26E4            ; {code.L26E4}
26E3: 51              LD      D,C                 
L26E4:
26E4: 59              LD      E,C                 
L26E5:
26E5: 0C              INC     C                   
26E6: 7D              LD      A,L                 
26E7: 90              SUB     B                   
26E8: 6F              LD      L,A                 
26E9: FE 68           CP      $68                 
26EB: C2 D9 26        JP      NZ,$26D9            ; {code.L26D9}
26EE: 3A D2 4B        LD      A,($4BD2)           ; {!ram.B4BD2}
26F1: 82              ADD     A,D                 
26F2: 83              ADD     A,E                 
26F3: E6 1F           AND     $1F                 ; 0001_1111
26F5: 32 D6 4B        LD      ($4BD6),A           ; {!ram.B4BD6}
26F8: 7B              LD      A,E                 
26F9: 92              SUB     D                   
26FA: 32 D7 4B        LD      ($4BD7),A           ; {!ram.B4BD7}
26FD: C9              RET                         

26FE: FF FF

;*****************************************************************************
;* Handles the scoring, and the update of sound control HW.
;*****************************************************************************
UpdateScoresAndSound:
2700: 21 A2 43        LD      HL,$43A2            ; {+ram.GameOrAttract}
2703: 7E              LD      A,(HL)              ; get it
2704: A7              AND     A                   ; updates the zero flag
2705: C8              RET     Z                   ; if GameOrAttract is 'Attract mode'.
2706: 2C              INC     L                   ; 
2707: 7E              LD      A,(HL)              ; get GameAndDemoOrSplash
2708: E6 01           AND     $01                 ; mask out 0000_0001 'Game for player 2'
270A: 07              RLCA                        ; Multiply by 4 ..
270B: 07              RLCA                        ; ..
270C: C6 83           ADD     $83                 ; 
270E: 6F              LD      L,A                 ; 
270F: 3E FF           LD      A,$FF               ; 
2711: 32 97 43        LD      ($4397),A           ; {ram.M4397}
2714: 11 70 43        LD      DE,$4370            ; {+ram.M4370}
L2717:
2717: CD 48 27        CALL    $2748               ; {code.L2748} add score values for all enemies hit.
271A: 1C              INC     E                   ; 
271B: 1C              INC     E                   ; 
271C: 1C              INC     E                   ; 
271D: 7B              LD      A,E                 ; 
271E: FE 80           CP      $80                 ; from $4370 to $4380
2720: C2 17 27        JP      NZ,$2717            ; {code.L2717}
2723: 1E 9D           LD      E,$9D               ; 
2725: 3A A4 43        LD      A,($43A4)           ; {ram.GameState}
2728: FE 06           CP      $06                 ; 
272A: C2 39 27        JP      NZ,$2739            ; {code.L2739}
272D: 1A              LD      A,(DE)              ; 
272E: 47              LD      B,A                 ; 
272F: 0E 00           LD      C,$00               ; 
2731: CD 20 02        CALL    $0220               ; {code.AddToScore}
2734: AF              XOR     A                   ; A=0
2735: 12              LD      (DE),A              ; 
2736: 32 97 43        LD      ($4397),A           ; {ram.M4397}
L2739:
2739: 3A 97 43        LD      A,($4397)           ; {ram.M4397}
273C: A7              AND     A                   ; updates the zero flag
273D: CC 68 27        CALL    Z,$2768             ; {code.L2768} if $4397 is 0.
2740: CD A8 27        CALL    $27A8               ; {code.UpdateSoundControlHW}
2743: C3 10 3A        JP      $3A10               ; {code.L3A10}

2746: FF FF
; Add score values for enemies hit.
L2748:
2748: 1A              LD      A,(DE)              ; get $4370
2749: 1C              INC     E                   ; 
274A: FE 01           CP      $01                 ; 
274C: C0              RET     NZ                  ; if not 1
274D: 1A              LD      A,(DE)              ; 
274E: A7              AND     A                   ; updates the zero flag
274F: C8              RET     Z                   ; 
2750: 0F              RRCA                        ; enemy has been hit
2751: 0F              RRCA                        ; 
2752: 0F              RRCA                        ; 
2753: 0F              RRCA                        ; 
2754: 47              LD      B,A                 ; 
2755: E6 F0           AND     $F0                 ; 1111_0000
2757: 4F              LD      C,A                 ; 
2758: 78              LD      A,B                 ; 
2759: E6 0F           AND     $0F                 ; 0000_1111
275B: 47              LD      B,A                 ; 
275C: CD 20 02        CALL    $0220               ; {code.AddToScore}
275F: AF              XOR     A                   ; Clear A Reg.
2760: 12              LD      (DE),A              ; clear the temp. score storage and ...
2761: 32 97 43        LD      ($4397),A           ; {ram.M4397} ... the first two digits of BCD score value
2764: C9              RET                         ; 
; 
2765: FF FF FF
; 
L2768:
2768: E5              PUSH    HL                  
2769: 11 61 42        LD      DE,$4261            ; end of the screen area of player 1 score
276C: 06 06           LD      B,$06               ; number of digits to print
276E: 3A A3 43        LD      A,($43A3)           ; {ram.GameAndDemoOrSplash}
2771: A7              AND     A                   ; updates the zero flag
2772: CA 78 27        JP      Z,$2778             ; {} if GameAndDemoOrSplash is 'Game and demo for player 1'
2775: 11 21 40        LD      DE,$4021            ; end of the screen area of player 2 score
2778: CD C4 00        CALL    $00C4               ; {code.PrintNumber} update the score on screen
277B: E1              POP     HL                  
277C: 11 BD 43        LD      DE,$43BD            ; {+ram.M43BD}
277F: EB              EX      DE,HL               
2780: 7E              LD      A,(HL)              
2781: 2C              INC     L                   
2782: B6              OR      (HL)                
2783: C8              RET     Z                   
2784: 2C              INC     L                   
2785: EB              EX      DE,HL               
2786: CD 14 03        CALL    $0314               ; {code.L0314}
2789: D0              RET     NC                  
278A: 3A A3 43        LD      A,($43A3)           ; {ram.GameAndDemoOrSplash}
278D: C6 90           ADD     $90                 
278F: 6F              LD      L,A                 
2790: 34              INC     (HL)                
2791: CD 67 03        CALL    $0367               ; {code.UpdateLivesScreen}
2794: 3E FF           LD      A,$FF               
2796: 32 6A 43        LD      ($436A),A           ; {ram.M436A}
2799: 2E BE           LD      L,$BE               ; BonusLivesAt
279B: 7E              LD      A,(HL)              
279C: 36 00           LD      (HL),$00            
279E: 0F              RRCA                        
279F: 0F              RRCA                        
27A0: 0F              RRCA                        
27A1: 0F              RRCA                        
27A2: 2D              DEC     L                   ; $43BD
27A3: 77              LD      (HL),A              
27A4: C9              RET                         

27A5: FF FF FF

;*****************************************************************************
;* Update the sound control hardware registers
;*****************************************************************************
UpdateSoundControlHW:
27A8: 21 8C 43        LD      HL,$438C            ; {+ram.SoundControlA} ..
27AB: 7E              LD      A,(HL)              ; .. to
27AC: 32 00 60        LD      ($6000),A           ; {hard.soundControlA} 60xx sound A
27AF: 2C              INC     L                   ; SoundControlB ..
27B0: 7E              LD      A,(HL)              ; .. to
27B1: 32 00 68        LD      ($6800),A           ; {hard.soundControlB} 68xx sound B
27B4: F6 0F           OR      $0F                 ; 0000_1111
27B6: 77              LD      (HL),A              ; 
27B7: 2D              DEC     L                   ; 
27B8: 36 0F           LD      (HL),$0F            ; 
27BA: C9              RET                         ; 

27BB: FF FF
; 
L27BD:
27BD: 21 63 43        LD      HL,$4363            ; {+ram.ParticleExplosion}
27C0: 7E              LD      A,(HL)              ; 
27C1: A7              AND     A                   ; updates the zero flag
27C2: C2 E2 27        JP      NZ,$27E2            ; {code.L27E2} if player ship was hit.
27C5: 2E 61           LD      L,$61               ; BulletTriggered
27C7: 7E              LD      A,(HL)              
27C8: A7              AND     A                   ; updates the zero flag
27C9: C8              RET     Z                   
27CA: FE 19           CP      $19                 
27CC: D2 D8 27        JP      NC,$27D8            ; {code.L27D8} if >= $19
27CF: 35              DEC     (HL)                
27D0: 2E 8C           LD      L,$8C               ; SoundControlA
27D2: 7E              LD      A,(HL)              
27D3: F6 40           OR      $40                 ; 0100_0000
27D5: 77              LD      (HL),A              
27D6: C9              RET                         
; not used
27D7: 77              LD      (HL),A              
L27D8:
27D8: 36 18           LD      (HL),$18            
27DA: 2E 8C           LD      L,$8C               ; SoundControlA
27DC: 7E              LD      A,(HL)              
27DD: E6 BF           AND     $BF                 ; 1011_1111
27DF: 77              LD      (HL),A              
27E0: C9              RET                         
; not used 
27E1: 36

L27E2:
27E2: FE 40           CP      $40                 
27E4: DA E9 27        JP      C,$27E9             ; {code.L27E9}
27E7: 36 40           LD      (HL),$40            
L27E9:
27E9: 35              DEC     (HL)                
27EA: 2E 8C           LD      L,$8C               ; SoundControlA
27EC: 36 8F           LD      (HL),$8F            ; 1000_1111
27EE: C9              RET                         

27EF: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

;foreground tiles of the player ship particles explosion
T2800:
2800: 00 32 00 00 00 00 00 00 00 00 00 00 00 00 42 42
2810: 00 00 00 00 00 00 00 00 00 00 E1 00 00 E2 00 00
2820: 32 00 00 00 00 00 00 00 00 E0 00 00 40 00 00 C3
2830: 00 00 00 00 00 00 DF 00 00 E2 00 00 E0 00 E1 00
2840: 00 30 00 00 00 00 DE 00 00 00 C2 00 40 00 E0 00
2850: 00 00 00 30 00 30 00 5A 00 00 E1 00 40 00 E2 00
2860: 00 00 00 00 00 00 00 30 C1 3E 00 E0 00 40 C2 00
2870: 00 00 00 00 00 00 00 00 00 5A C1 3E C8 D8 00 00
2880: E0 E1 C2 E2 E0 00 E1 00 C2 00 E2 CE CA DA 00 00
2890: 00 00 00 00 00 00 00 00 CF CF C3 3F C2 41 E0 00
28A0: 00 00 00 00 00 00 00 DE 00 3F 00 C2 41 00 E1 00
28B0: 00 00 00 00 00 3D DF 3D 00 00 E1 00 41 00 00 C2
28C0: 00 00 00 3D 00 00 00 00 00 E0 00 00 41 00 00 E2
28D0: 00 00 3D 00 00 00 00 00 E2 00 00 00 00 4F 00 E0
28E0: 00 3B 00 00 00 00 00 00 00 C2 00 00 00 4F 00 00
28F0: 00 00 3B 00 00 00 00 00 00 00 00 00 00 00 4D 4D

;control data of the player ship particles explosion
T2900:
2900: 00 00 00 00 00 00 00 00 00 00 00 00 00 20 00 38
2910: 00 34 00 28 00 00 00 00 00 00 00 00 00 00 00 00
2920: 00 00 00 00 00 00 00 00 00 00 00 10 00 02 00 00
2930: 00 01 00 00 12 00 00 00 00 00 00 00 00 00 00 00
2940: 00 00 00 00 00 00 00 00 00 10 00 00 80 48 00 04
2950: 40 08 00 50 00 00 80 10 00 00 00 00 00 00 00 00
2960: 00 00 00 00 00 00 00 10 00 00 20 44 00 00 00 02
2970: 10 00 00 04 00 48 20 00 00 10 00 00 00 00 00 00
2980: 00 00 00 00 00 10 00 00 00 44 08 00 00 01 00 00
2990: 08 00 00 02 00 00 00 84 08 00 00 20 00 00 00 00
29A0: 00 00 00 20 00 00 00 42 02 00 80 00 00 00 00 00
29B0: 04 00 00 01 00 00 00 00 00 82 04 00 00 20 00 00
29C0: 00 40 00 00 01 82 00 00 40 00 00 00 00 00 00 00
29D0: 02 00 00 00 80 00 00 00 00 00 00 81 02 00 00 40
29E0: 02 80 00 04 00 00 40 00 00 00 00 00 00 00 00 00
29F0: 01 00 00 00 00 00 40 00 00 00 00 00 00 02 04 08

;foreground tiles of the mothership particles explosion
T2A00:
2A00: 00 00 00 00 00 00 00 D2 00 00 00 00 00 00 00 00
2A10: 00 00 00 00 00 DE 00 5E E0 00 00 E1 00 00 00 00
2A20: 00 00 C1 00 00 CF 53 E2 00 D2 E0 00 00 D0 00 00
2A30: 00 00 00 DE 00 CE 53 E1 D1 E3 00 E1 D3 00 00 00
2A40: 00 00 CF C0 DE DF 53 D3 E2 00 E2 D2 00 5E E2 00
2A50: 00 00 00 CE C1 C2 DE D2 E1 E3 D1 00 D2 00 00 00
2A60: 00 00 00 00 DF DE C2 CF E0 D0 E2 E1 C2 C3 00 00
2A70: DF DE CF CE DF DE CF C8 D8 5E CE 00 CF DE DF CE
2A80: E0 E3 E2 E1 00 E0 D1 CA DA D1 D2 D3 D0 D1 D2 D3
2A90: 00 00 00 00 E3 D2 CE D2 E2 E0 D3 D1 D3 00 00 00
2AA0: 00 00 00 E2 D3 CF DF E1 D0 E3 E1 D2 00 00 00 00
2AB0: 00 00 E1 D0 DE 00 DE E2 00 D3 53 E2 5E C1 C0 00
2AC0: 00 00 00 DF 00 00 CF 5E D1 D2 00 53 E3 00 00 00
2AD0: 00 00 CE 00 CF 00 CE D2 D2 00 53 00 5E E0 00 00
2AE0: 00 00 00 00 00 DE 00 E1 D3 00 E2 00 00 00 00 00
2AF0: 00 00 00 00 00 00 00 5E D0 00 00 00 00 00 00 00

;control data of the mothership particles explosion
T2B00:
2B00: 00 00 00 00 00 00 00 00 00 00 80 01 40 02 80 05
2B10: A0 01 40 02 00 01 00 00 00 00 00 00 00 00 00 00
2B20: 00 00 00 00 00 00 80 00 00 01 20 04 00 01 40 12
2B30: 48 02 80 01 20 04 00 00 00 01 00 00 00 00 00 00
2B40: 00 00 00 00 80 00 00 02 10 08 00 01 80 04 A0 21
2B50: 84 05 20 02 80 01 10 08 00 00 00 01 00 00 00 00
2B60: 00 00 80 00 00 04 08 10 00 01 40 00 40 0A 10 40
2B70: 02 08 40 00 10 04 80 02 08 10 00 00 00 01 00 00
2B80: 80 00 00 08 04 20 00 02 20 00 20 14 00 01 08 80
2B90: 01 10 80 02 20 00 08 04 80 02 04 20 00 00 00 01
2BA0: 01 01 01 01 01 04 20 00 10 28 80 02 04 00 00 04
2BB0: 20 20 00 04 40 01 10 00 04 08 80 04 00 00 00 00
2BC0: 00 00 00 08 20 00 88 10 00 44 00 00 00 10 02 00
2BD0: 08 40 00 00 00 08 40 00 08 01 00 10 80 04 00 00
2BE0: 00 00 20 00 84 20 00 08 00 00 00 00 00 20 01 00
2BF0: 04 80 00 00 00 00 00 10 40 00 04 01 00 00 80 00

; Closed loop pattern table part 2:
; Used for single or multiple aliens, depending on the game round.
; Pattern 18
T2C00:
2C00: 0B 0C 0D 0E 0B 0C 0A 0A 0A 0A 0A 0A 0A 06 06 1E
2C10: 03 03 1F 05 05 1C 04 04 04 1D 06 06 1A 04 04 04
2C20: 1B 05 05 05 05 18 1F 07 07 07 07 07 07 07 07 07
2C30: 00 FF FF FF
; Pattern 19
T2C34:
2C34: 05 05 1C 04 1D 0A 0A 0A 0A 0A 0A 06
2C40: 06 1E 03 03 1F 05 1C 04 04 1D 0A 06 06 1E 03 03
2C50: 1F 05 1C 04 04 1D 0A 06 06 1E 03 03 1F 05 1C 04
2C60: 04 1D 0A 06 1E 03 1F 05 1C 04 1D 06 1E 03 03 03
2C70: 03 15 16 17 01 01 05 05 01 01 05 05 01 01 05 05
2C80: 01 01 05 05 02 02 18 07 07 07 00 FF FF FF FF FF
; Pattern 20 (phase 3)
T2C90:
2C90: 1C 04 04 04 04 04 04 04 04 04 04 04 04 04 04 1D
2CA0: 06 06 06 06 06 06 06 1E 03 03 03 03 03 03 1F 05
2CB0: 05 05 05 1C 04 04 1D 06 09 09 09 1E 03 07 07 08
2CC0: 08 07 07 08 07 00 FF FF
; Pattern 21 (phase 3)
T2CC8:
2CC8: 05 05 05 05 1C 04 04 04
2CD0: 04 04 04 04 04 04 04 04 04 04 04 1D 09 09 09 09
2CE0: 0A 0A 0A 09 0A 0A 06 1E 03 03 03 1F 05 05 18 03
2CF0: 19 06 06 1E 03 03 1F 05 05 05 05 05 05 05 00 FF
; Pattern 22
T2D00:
2D00: 0B 0C 0D 0E 0B 0C 06 1E 03 03 03 03 03 03 03 03
2D10: 03 03 03 03 03 03 1F 05 05 1C 04 04 04 04 04 04
2D20: 04 04 04 04 1D 06 06 1E 03 03 03 03 03 03 1F 05
2D30: 05 05 05 05 1C 04 04 04 04 04 04 04 04 04 04 1B
2D40: 00 FF FF FF
; Pattern 23 (phase 3)
T2D44:
2D44: 05 05 05 18 03 03 03 03 03 03 03 03
2D50: 03 19 06 06 1A 04 04 1B 05 05 18 03 03 03 03 03
2D60: 03 03 19 06 06 06 06 06 06 06 06 06 06 1A 04 04
2D70: 1B 05 05 1C 04 04 1D 06 06 1A 04 04 1B 05 05 05
2D80: 05 05 05 05 00 FF FF FF
; Pattern 24 (phase 3)
T2D88:
2D88: 1C 04 04 1D 06 06 09 0A
2D90: 0A 09 09 09 16 17 14 03 03 03 1F 05 05 1C 04 04
2DA0: 1D 06 06 1E 03 03 03 03 07 07 08 08 07 07 05 05
2DB0: 1C 04 04 04 04 04 04 04 1D 1A 04 1B 00 FF FF FF
; Pattern 25 (phase 3)
T2DC0:
2DC0: 14 03 03 19 06 0A 0A 09 09 09 0A 12 13 10 11 12
2DD0: 13 10 11 12 13 10 04 04 04 04 1B 05 18 03 19 06
2DE0: 1A 04 1B 05 18 07 07 07 08 08 07 07 07 03 03 19
2DF0: 0D 0E 00 FF FF FF FF FF FF FF FF FF FF FF FF FF
; Pattern 26
; Used for all aliens.
; This is the 'Angry movement pattern A'.
; At the end of that sequence, the alien formation is further down 
; and the 'phase' is increased by 1.
T2E00:
2E00: 0B 0C 0D 0E 02 02 02 02 0B 0C 0D 0E 01 01 14 15
2E10: 16 17 01 01 05 05 05 05 02 02 02 02 00 FF FF FF
; Pattern 27 (phase 3)
T2E20:
2E20: 0B 0C 0D 0E 0B 0C 0D 0E 02 02 02 02 02 02 02 02
2E30: 05 05 01 05 05 01 05 05 01 05 05 01 00 FF FF FF
; Pattern 28
; Used for all aliens.
; This is the 'Angry movement pattern B'.
; At the end of that sequence, the alien formation is further down 
; and the 'phase' is increased by 1.
T2E40:
2E40: 0B 0C 0D 0E 01 01 01 18 03 19 06 06 1A 04 1B 05
2E50: 18 03 19 06 06 1A 04 04 04 04 04 04 04 04 04 1B
2E60: 05 05 05 01 01 01 01 01 00 FF FF FF
; Pattern 29 (phase 3)
T2E6C:
2E6C: 0B 0C 0D 0E
2E70: 01 01 0B 0C 0D 0E 01 01 05 05 05 05 01 01 0B 0C
2E80: 0D 0E 01 01 07 08 08 07 08 08 08 07 00 FF FF FF
; Pattern 30
T2E90:
2E90: 14 15 16 17 14 15 16 17 14 03 03 03 03 03 03 03
2EA0: 03 03 03 03 03 19 09 0A 0A 09 09 0A 0A 12 13 08
2EB0: 08 07 07 08 08 08 08 04 04 04 11 12 13 10 11 12
2EC0: 13 00 FF FF
; Pattern 31
T2EC4:
2EC4: 10 11 12 13 10 11 12 13 10 04 04 04
2ED0: 04 04 04 04 04 04 0A 0A 0A 09 0A 09 0A 09 16 17
2EE0: 14 03 03 03 07 07 07 07 03 19 06 1A 04 1B 05 18
2EF0: 07 07 07 07 00 FF FF FF FF FF FF FF FF FF FF FF
; Pattern 32
T2F00:
2F00: 05 1C 04 1D 06 06 06 06 06 09 09 09 0A 0A 0A 09
2F10: 09 16 17 14 1F 05 18 03 19 06 1E 03 1F 05 18 03
2F20: 19 06 1E 03 1F 05 05 1C 08 08 08 08 08 08 08 08
2F30: 00 FF FF FF
; Pattern 33
T2F34:
2F34: 05 18 03 19 06 06 06 06 0A 0A 09 09
2F40: 0A 0A 09 0A 0A 12 13 10 1B 05 1C 04 1D 1E 1F 1C
2F50: 04 1D 06 1A 04 04 1B 05 18 07 07 07 07 08 07 07
2F60: 07 07 00 FF
; Pattern 34
T2F64:
2F64: 0B 0C 0D 0E 0B 0C 1E 03 19 06 1E 03
2F70: 19 06 1E 03 19 06 1E 1F 1C 1D 1E 03 03 03 1F 05
2F80: 18 03 19 06 1E 03 1F 05 08 08 08 08 08 08 08 07
2F90: 07 08 08 08 08 08 00 FF FF FF FF FF FF FF FF FF
; Pattern 35
T2FA0:
2FA0: 05 05 18 03 03 03 03 03 03 03 03 19 06 06 06 06
2FB0: 06 06 06 1A 04 1B 05 18 03 03 03 03 19 06 06 06
2FC0: 1A 04 1B 05 18 03 03 03 03 19 06 06 06 1A 04 1B
2FD0: 05 18 03 03 03 03 19 06 06 06 1A 04 1B 05 18 03
2FE0: 03 19 06 06 1A 11 12 13 02 02 02 05 05 02 02 02
2FF0: 05 05 02 02 02 05 1C 08 08 07 07 08 08 08 00 FF

;*****************************************************************************
;* AlienBehaviorUpdate
;*****************************************************************************
AlienBehaviorUpdate:
3000: 21 93 43        LD      HL,$4393            ; {+ram.Counter93}
3003: 7E              LD      A,(HL)              ; load and save ram value
3004: 34              INC     (HL)                ; increment Counter93
3005: E6 07           AND     $07                 ; masc out 0000_0111 the saved value in order to count from 0 to 7
3007: 21 18 30        LD      HL,$3018            ; {+code.T3018} base of jump table
300A: 07              RLCA                        ; Multiply by 2 to get a 2 byte offset
300B: 85              ADD     A,L                 ; 
300C: 6F              LD      L,A                 ; 
300D: 7E              LD      A,(HL)              ; get MSB from jump table
300E: 23              INC     HL                  ; 
300F: 6E              LD      L,(HL)              ; get LSB from jump table
3010: 67              LD      H,A                 ; 
3011: E9              JP      (HL)                ; jump to the corresponding function
; from jump table T3018 if Counter93 is 7
L3012:
3012: C9              RET                         ; 
; 
3013: FF FF FF FF FF
; 
T3018:
3018: 32 64 ; if Counter93 is 0
301A: 30 28 ; if Counter93 is 1
301C: 30 BA ; if Counter93 is 2
301E: 31 24 ; if Counter93 is 3
3020: 31 5A ; if Counter93 is 4
3022: 31 B4 ; if Counter93 is 5
3024: 32 2C ; if Counter93 is 6
3026: 30 12 ; if Counter93 is 7

; from jump table T3018 if Counter93 is 1
L3028:
3028: 21 57 43        LD      HL,$4357            ; {+ram.M4357}
302B: 7E              LD      A,(HL)              ; 
302C: FE 03           CP      $03                 ; 
302E: D0              RET     NC                  ; if >= 3
302F: 2E 50           LD      L,$50               ; 
3031: 7E              LD      A,(HL)              ; get $4350 Alien behavior state
3032: FE 04           CP      $04                 ; 
3034: D0              RET     NC                  ; if >= 4
3035: 2E 58           LD      L,$58               ; 
3037: 7E              LD      A,(HL)              ; get $4358
3038: A7              AND     A                   ; updates the zero flag
3039: CA 5C 30        JP      Z,$305C             ; {code.L305C}
303C: 35              DEC     (HL)                ; $4358
303D: C0              RET     NZ                  ; 
303E: 2D              DEC     L                   ; 
303F: 34              INC     (HL)                ; $4357
3040: 2E 50           LD      L,$50               ; 
3042: 36 04           LD      (HL),$04            ; set $4350 next alien behavior state to 4
3044: 2E 53           LD      L,$53               ; 
3046: 36 10           LD      (HL),$10            ; set $4353 Number of aliens doing the closed loop pattern
3048: 2C              INC     L                   ; 
3049: 36 50           LD      (HL),$50            ; set $4354
304B: 2E 51           LD      L,$51               ; 
304D: 36 2E           LD      (HL),$2E            ; set $4351 for T2Exx
304F: 2C              INC     L                   ; 
3050: 36 00           LD      (HL),$00            ; set $4352 for T2E00
3052: 3A C2 43        LD      A,($43C2)           ; {ram.PlayerShipX}
3055: 0F              RRCA                        ; 
3056: D8              RET     C                   ; if result is odd number
3057: 36 40           LD      (HL),$40            ; set $4352 for T2E40
3059: C9              RET                         ; 
; 
305A: FF FF
; 
L305C:
305C: CD 74 30        CALL    $3074               ; {code.L3074}
305F: 21 57 43        LD      HL,$4357            ; {+ram.M4357}
3062: 7E              LD      A,(HL)              ; get $4357
3063: 07              RLCA                        ; Multiply by 4 ..
3064: 07              RLCA                        ; ..
3065: 00              NOP                         ; 
3066: 00              NOP                         ; 
3067: 81              ADD     A,C                 ; 
3068: C6 07           ADD     $07                 ; 
306A: 2E 58           LD      L,$58               ; 
306C: 77              LD      (HL),A              ; store to $4358
306D: C9              RET                         ; 
; 
306E: FF FF FF FF FF FF
; 
L3074:
3074: 21 B8 43        LD      HL,$43B8            ; {+ram.LevelAndRound}
3077: 7E              LD      A,(HL)              
3078: 0F              RRCA                        
3079: 00              NOP                         
307A: E6 07           AND     $07                 ; 0000_0111
307C: 47              LD      B,A                 
307D: 3E 07           LD      A,$07               
307F: 90              SUB     B                   
3080: 4F              LD      C,A                 
3081: 7E              LD      A,(HL)              ; get LevelAndRound
3082: FE 80           CP      $80                 
3084: DA 89 30        JP      C,$3089             ; {code.L3089}
3087: 3E 70           LD      A,$70               
L3089:
3089: 0F              RRCA                        
308A: 0F              RRCA                        
308B: 0F              RRCA                        
308C: 0F              RRCA                        
308D: E6 07           AND     $07                 ; 0000_0111
308F: 47              LD      B,A                 
3090: 3E 07           LD      A,$07               
3092: 90              SUB     B                   
3093: 81              ADD     A,C                 
3094: 4F              LD      C,A                 
3095: 3A BA 43        LD      A,($43BA)           ; {ram.AliensLeft}
3098: D6 05           SUB     $05                 
309A: D2 9F 30        JP      NC,$309F            ; {code.L309F}
309D: 3E 10           LD      A,$10               
L309F:
309F: 81              ADD     A,C                 
30A0: 4F              LD      C,A                 
30A1: CD AA 30        CALL    $30AA               ; {code.GetRandomNumber}
30A4: E6 07           AND     $07                 ; 0000_0111  for 0 to 7
30A6: 81              ADD     A,C                 
30A7: 4F              LD      C,A                 
30A8: C9              RET                         
; 
30A9: FF

;*****************************************************************************
;* Free running counter ($439B) and the X position of the player ship ($43C2)
;* is the base for a pseudo random number.
;* Returns A-register: $00 to $0F.
;*****************************************************************************
GetRandomNumber:
30AA: 21 9B 43        LD      HL,$439B            ; {+ram.Counter9A+1}
30AD: 7E              LD      A,(HL)              ; 
30AE: 07              RLCA                        ; Multiply by 8 ..
30AF: 07              RLCA                        ; ..
30B0: 07              RLCA                        ; ..
30B1: E6 07           AND     $07                 ; mask out 0000_0111 in order to count from 0 to 7
30B3: 2E C2           LD      L,$C2               ; get $43C2 PlayerShipX
30B5: 86              ADD     A,(HL)              ; add to counter value
30B6: E6 0F           AND     $0F                 ; mask out 0000_1111
30B8: C9              RET                         ; 

; not used 
30B9: C0              RET     NZ                  

; from jump table T3018 if Counter93 is 2
L30BA:
30BA: 21 58 43        LD      HL,$4358            ; {+ram.M4358}
30BD: CD DA 30        CALL    $30DA               ; {code.L30DA} for $4359
30C0: CD DA 30        CALL    $30DA               ; {code.L30DA} for $435A
30C3: CD DA 30        CALL    $30DA               ; {code.L30DA} for $435B
30C6: 2E 50           LD      L,$50               ; 
30C8: 7E              LD      A,(HL)              ; get $4350 Alien behavior state
30C9: A7              AND     A                   ; updates the zero flag
30CA: C0              RET     NZ                  ; if <> 0
30CB: 2E 55           LD      L,$55               ; 
30CD: 7E              LD      A,(HL)              ; get $4355
30CE: A7              AND     A                   ; updates the zero flag
30CF: CA E4 30        JP      Z,$30E4             ; {code.L30E4} if 0
30D2: 35              DEC     (HL)                
30D3: C0              RET     NZ                  
30D4: 2E 50           LD      L,$50               ; $4350 next alien behavior state to 1
30D6: 36 01           LD      (HL),$01            ; 
30D8: C9              RET                         ; 

; not used 
30D9: FE                                          

; 
L30DA:
30DA: 2C              INC     L                   
30DB: 7E              LD      A,(HL)              
30DC: A7              AND     A                   ; updates the zero flag
30DD: C8              RET     Z                   ; if 4359, 435A, 435B = 0
30DE: 35              DEC     (HL)                
30DF: C9              RET                         

; not used 
30E0: 7E              LD      A,(HL)              
30E1: FE 01           CP      $01                 
30E3: D0              RET     NC                  

L30E4:
30E4: CD 74 30        CALL    $3074               ; {code.L3074}
30E7: 21 9A 43        LD      HL,$439A            ; {+ram.Counter9A}
30EA: 7E              LD      A,(HL)              
30EB: FE 10           CP      $10                 
30ED: DA F2 30        JP      C,$30F2             ; {code.L30F2}
30F0: 3E 0F           LD      A,$0F               
L30F2:
30F2: 47              LD      B,A                 
30F3: 3E 0F           LD      A,$0F               
30F5: 90              SUB     B                   
30F6: 81              ADD     A,C                 
30F7: 4F              LD      C,A                 
30F8: 06 01           LD      B,$01               
30FA: 2E 58           LD      L,$58               ; $4358
30FC: CD 12 31        CALL    $3112               ; {code.L3112} for $4359
30FF: CD 12 31        CALL    $3112               ; {code.L3112} for $435A
3102: CD 12 31        CALL    $3112               ; {code.L3112} for $435B
3105: 79              LD      A,C                 
3106: 0F              RRCA                        
3107: 0F              RRCA                        
3108: E6 3F           AND     $3F                 ; 0011_1111
310A: C6 01           ADD     $01                 
310C: 2E 55           LD      L,$55               
310E: 77              LD      (HL),A              ; set $4355
310F: C9              RET                         

; not used
3110: 21 50                                       

;
L3112:
3112: 2C              INC     L                   
3113: 7E              LD      A,(HL)              
3114: A7              AND     A                   ; updates the zero flag
3115: C0              RET     NZ                  ; if <> 0
3116: 79              LD      A,C                 
3117: 0F              RRCA                        
3118: E6 7F           AND     $7F                 ; 0111_1111
311A: 4F              LD      C,A                 
311B: 78              LD      A,B                 
311C: A7              AND     A                   ; updates the zero flag
311D: C8              RET     Z                   
311E: 05              DEC     B                   
311F: 36 0C           LD      (HL),$0C            
3121: C9              RET                         

; not used 
3122: 86              ADD     A,(HL)              
3123: 47              LD      B,A                 

; from jump table T3018 if Counter93 is 3
L3124:
3124: 21 50 43        LD      HL,$4350            ; {+ram.M4350} 
3127: 7E              LD      A,(HL)              ; get alien behavior state
3128: FE 01           CP      $01                 ; 
312A: C0              RET     NZ                  ; if $4350 <> 1
312B: 36 02           LD      (HL),$02            ; set $4350 next alien behavior state to 2
312D: 2E B8           LD      L,$B8               ; 
312F: 7E              LD      A,(HL)              ; get LevelAndRound
3130: 0F              RRCA                        ; 
3131: 0F              RRCA                        ; 
3132: E6 0F           AND     $0F                 ; 0000_1111 (bit 0,1 game round / bit 2,3 game level)
3134: C6 05           ADD     $05                 ; 
3136: FE 11           CP      $11                 ; 
3138: DA 3D 31        JP      C,$313D             ; {code.L313D} if game round < 4
313B: 3E 05           LD      A,$05               ; 
L313D:
313D: 2E 57           LD      L,$57               ; $4357
313F: 96              SUB     (HL)                ; 
3140: 47              LD      B,A                 ; 
3141: CD AA 30        CALL    $30AA               ; {code.GetRandomNumber}
3144: 3C              INC     A                   ; 
3145: B8              CP      B                   ; 
3146: DA 4B 31        JP      C,$314B             ; {code.L314B}
3149: 3E 01           LD      A,$01               ; only one alien
L314B:
314B: 2E 53           LD      L,$53               ; $4353
314D: 77              LD      (HL),A              ; set $4353 Number of aliens doing the closed loop pattern
314E: C9              RET                         ; 

; not used 
314F: 0A 0C 0B 0C 0B 0E 0F 0E 0F FF FF

; from jump table T3018 if Counter93 is 4
L315A:
315A: 21 50 43        LD      HL,$4350            ; {+ram.M4350}
315D: 7E              LD      A,(HL)              ; get alien behavior state
315E: FE 02           CP      $02                 
3160: C0              RET     NZ                  ; if <> 2
3161: CD AA 30        CALL    $30AA               ; {code.GetRandomNumber}
3164: 00              NOP                         
3165: 47              LD      B,A                 
3166: 07              RLCA                        ; Multiply by 2
3167: C6 50           ADD     $50                 
3169: 6F              LD      L,A                 
316A: 26 4B           LD      H,$4B               ; $4B50
316C: 78              LD      A,B                 
316D: 07              RLCA                        ; Multiply by 4 ..
316E: 07              RLCA                        ; 
316F: C6 70           ADD     $70                 
3171: 5F              LD      E,A                 
3172: 16 4B           LD      D,$4B               ; $4B70
3174: 0E 10           LD      C,$10               ; for all 16 aliens
3176: 79              LD      A,C                 
3177: 90              SUB     B                   
3178: 47              LD      B,A                 
L3179:
3179: CD 92 31        CALL    $3192               ; {code.L3192}
317C: 13              INC     DE                  
317D: 13              INC     DE                  
317E: 13              INC     DE                  
317F: 13              INC     DE                  
3180: 23              INC     HL                  
3181: 23              INC     HL                  
3182: 05              DEC     B                   
3183: C2 8A 31        JP      NZ,$318A            ; {code.L318A}
3186: 1E 70           LD      E,$70               
3188: 2E 50           LD      L,$50               ; $4350
L318A:
318A: 0D              DEC     C                   
318B: C2 79 31        JP      NZ,$3179            ; {code.L3179} loop for all 16 aliens
318E: C9              RET                         
; 
318F: FF FF FF
; 
L3192:
3192: 1A              LD      A,(DE)              
3193: E6 08           AND     $08                 ; 0000_1000
3195: C8              RET     Z                   
3196: 3A 94 43        LD      A,($4394)           ; {ram.M4394} get start value list pointer for alien movement MSB
3199: BE              CP      (HL)                
319A: C0              RET     NZ                  
319B: 3A 56 43        LD      A,($4356)           ; {ram.M4356}
319E: 2C              INC     L                   
319F: 46              LD      B,(HL)              
31A0: 2D              DEC     L                   
31A1: B8              CP      B                   
31A2: C0              RET     NZ                  
31A3: 7D              LD      A,L                 
31A4: 32 54 43        LD      ($4354),A           ; {ram.M4354}
31A7: 3E 03           LD      A,$03               
31A9: 32 50 43        LD      ($4350),A           ; {ram.M4350} set next alien behavior state to 3
31AC: E1              POP     HL                  
31AD: C9              RET                         
; 
31AE: FF FF FF FF FF FF

; from jump table T3018 if Counter93 is 5
L31B4:
31B4: 3A 50 43        LD      A,($4350)           ; {ram.M4350} get alien behavior state
31B7: FE 03           CP      $03                 ; 
31B9: C0              RET     NZ                  ; if <> 3
31BA: 3A 54 43        LD      A,($4354)           ; {ram.M4354}
31BD: D6 50           SUB     $50                 ; 
31BF: 07              RLCA                        ; Multiply by 2 to get 2 byte offset
31C0: C6 72           ADD     $72                 ; base for alien data structure (grid)
31C2: 6F              LD      L,A                 ; 
31C3: 26 4B           LD      H,$4B               ; 
31C5: 46              LD      B,(HL)              ; get alien screen coordinate X
31C6: 2C              INC     L                   ; 
31C7: 56              LD      D,(HL)              ; get alien screen coordinate Y
31C8: 3A C2 43        LD      A,($43C2)           ; {ram.PlayerShipX}
31CB: 0E 04           LD      C,$04               ; 
31CD: B8              CP      B                   ; 
31CE: D2 D6 31        JP      NC,$31D6            ; {code.L31D6} if PlayerShipX > alien screen coordinate X
31D1: 4F              LD      C,A                 ; 
31D2: 78              LD      A,B                 ; 
31D3: 41              LD      B,C                 ; 
31D4: 0E 00           LD      C,$00               ; 
L31D6:
31D6: 90              SUB     B                   ; 
31D7: 07              RLCA                        ; Multiply by 8 ..
31D8: 07              RLCA                        ; ..
31D9: 07              RLCA                        ; ..
31DA: E6 07           AND     $07                 ; 0000_0111
31DC: C6 00           ADD     $00                 ; LSB for table T3300
31DE: 6F              LD      L,A                 ; 
31DF: 26 33           LD      H,$33               ; get MSB for table T3300
31E1: 7E              LD      A,(HL)              ; get data from T3300
31E2: 81              ADD     A,C                 ; 
31E3: 07              RLCA                        ; Multiply by 4 ..
31E4: 07              RLCA                        ; ..
31E5: 4F              LD      C,A                 ; 
31E6: 00              NOP                         ; 
31E7: 00              NOP                         ; 
31E8: 00              NOP                         ; 
31E9: 3A 57 43        LD      A,($4357)           ; {ram.M4357}
31EC: 47              LD      B,A                 ; 
31ED: CD 10 32        CALL    $3210               ; {code.L3210}
31F0: 79              LD      A,C                 ; 
31F1: 80              ADD     A,B                 ; 
31F2: C6 10           ADD     $10                 ; LSB for table T3310
31F4: 6F              LD      L,A                 ; 
31F5: 26 33           LD      H,$33               ; get MSB for table T3310
31F7: 4E              LD      C,(HL)              ; get data from T3310
31F8: CD AA 30        CALL    $30AA               ; {code.GetRandomNumber}
31FB: E6 06           AND     $06                 ; 0000_0110 (0, 2, 4 or 6)
31FD: 81              ADD     A,C                 ; 
31FE: 6F              LD      L,A                 ; 
31FF: 26 33           LD      H,$33               ; get MSB for table T3330 (base adresses of closed loop pattern tables for aliens)
3201: 7E              LD      A,(HL)              ; 
3202: 2C              INC     L                   ; 
3203: 46              LD      B,(HL)              ; 
3204: 21 50 43        LD      HL,$4350            ; {+ram.M4350}
3207: 36 05           LD      (HL),$05            ; set $4350 next alien behavior state to 5
3209: 2C              INC     L                   ; 
320A: 77              LD      (HL),A              ; set MSB of next closed loop pattern at $4351
320B: 2C              INC     L                   ; 
320C: 70              LD      (HL),B              ; set LSB of next closed loop pattern at $4352
320D: C9              RET                         ;

; not used 
320E: 81              ADD     A,C                 
320F: 6F              LD      L,A                 

; 
L3210:
3210: 3A 53 43        LD      A,($4353)           ; {ram.M4353} Number of aliens doing the closed loop pattern
3213: FE 01           CP      $01                 ; 
3215: C0              RET     NZ                  ; if $4353 <> 1
3216: 7A              LD      A,D                 ; alien screen coordinate Y
3217: 06 00           LD      B,$00               ; return B = 0
3219: FE 58           CP      $58                 ; 
321B: D8              RET     C                   ; if alien screen coordinate Y < $58
321C: 06 01           LD      B,$01               ; return B = 1
321E: FE 78           CP      $78                 ; 
3220: D8              RET     C                   ; if alien screen coordinate Y < $78
3221: 06 02           LD      B,$02               ; return B = 2
3223: FE 98           CP      $98                 ; 
3225: D8              RET     C                   ; if alien screen coordinate Y < $98
3226: 06 03           LD      B,$03               ; return B = 3
3228: C9              RET                         ; 

; not used 
3229: C0 21 50                                    

; from jump table T3018 if Counter93 is 6
L322C:
322C: 3A 50 43        LD      A,($4350)           ; {ram.M4350} get alien behavior state
322F: FE 04           CP      $04                 
3231: C0              RET     NZ                  ; if <> 4
3232: 21 50 4B        LD      HL,$4B50            ; {+ram.M4B50} Pointer to alien movement pattern
3235: 11 70 4B        LD      DE,$4B70            ; {+ram.M4B70} Alien data structure (grid)
3238: 3A 56 43        LD      A,($4356)           ; {ram.M4356}
323B: 4F              LD      C,A                 
323C: 3A 94 43        LD      A,($4394)           ; {ram.M4394} get start value list pointer for alien movement MSB
323F: 47              LD      B,A                 
L3240:
3240: 1A              LD      A,(DE)              
3241: E6 08           AND     $08                 ; 0000_1000
3243: CA 4E 32        JP      Z,$324E             ; {code.L324E}
3246: 7E              LD      A,(HL)              
3247: B8              CP      B                   
3248: C0              RET     NZ                  
3249: 2C              INC     L                   
324A: 7E              LD      A,(HL)              
324B: 2D              DEC     L                   
324C: B9              CP      C                   
324D: C0              RET     NZ                  
L324E:
324E: 2C              INC     L                   
324F: 2C              INC     L                   
3250: 7B              LD      A,E                 
3251: C6 04           ADD     $04                 
3253: 5F              LD      E,A                 
3254: FE B0           CP      $B0                 
3256: C2 40 32        JP      NZ,$3240            ; {code.L3240}
3259: 3E 06           LD      A,$06               
325B: 32 50 43        LD      ($4350),A           ; {ram.M4350} set next alien behavior state to 6
325E: C9              RET                         

; not used 
325F: 3C E6 0F 77 2E                              

; from jump table T3018 if Counter93 is 0 
L3264:
3264: 21 95 43        LD      HL,$4395            ; {+ram.M4395}
3267: 7E              LD      A,(HL)              ; get start value list pointer for alien movement LSB
3268: 32 56 43        LD      ($4356),A           ; {ram.M4356}
326B: 3C              INC     A                   
326C: E6 0F           AND     $0F                 ; 0000_1111
326E: 77              LD      (HL),A              
326F: 2E 50           LD      L,$50               
3271: 7E              LD      A,(HL)              ; get $4350 Alien behavior state
3272: FE 05           CP      $05                 
3274: D8              RET     C                   ; if < 5
3275: 36 00           LD      (HL),$00            ; set $4350 next alien behavior state to 0
3277: 2E 53           LD      L,$53               
3279: 4E              LD      C,(HL)              ; get $4353 Number of aliens doing the closed loop pattern
327A: 2C              INC     L                   
327B: 6E              LD      L,(HL)              ; get $4354
327C: 26 4B           LD      H,$4B               
327E: 3A 56 43        LD      A,($4356)           ; {ram.M4356}
3281: 57              LD      D,A                 
3282: 3A 94 43        LD      A,($4394)           ; {ram.M4394} get start value list pointer for alien movement MSB
3285: 5F              LD      E,A                 
3286: 7D              LD      A,L                 
3287: D6 50           SUB     $50                 
3289: 0F              RRCA                        
328A: 47              LD      B,A                 
328B: 3E 10           LD      A,$10               
328D: 90              SUB     B                   
328E: 47              LD      B,A                 
L328F:
328F: 7E              LD      A,(HL)              
3290: 2C              INC     L                   
3291: BB              CP      E                   
3292: C2 A4 32        JP      NZ,$32A4            ; {code.L32A4}
3295: 7E              LD      A,(HL)              
3296: BA              CP      D                   
3297: C2 A4 32        JP      NZ,$32A4            ; {code.L32A4}
329A: 2D              DEC     L                   
329B: 3A 51 43        LD      A,($4351)           ; {ram.M4351} get MSB of next closed loop pattern
329E: 77              LD      (HL),A              
329F: 2C              INC     L                   
32A0: 3A 52 43        LD      A,($4352)           ; {ram.M4352} get LSB of next closed loop pattern
32A3: 77              LD      (HL),A              
L32A4:
32A4: 2C              INC     L                   
32A5: 05              DEC     B                   
32A6: C2 AB 32        JP      NZ,$32AB            ; {code.L32AB}
32A9: 2E 50           LD      L,$50               ; $4350
L32AB:
32AB: 0D              DEC     C                   
32AC: C2 8F 32        JP      NZ,$328F            ; {code.L328F} loop for Number of aliens doing the closed loop pattern
32AF: C9              RET                         

; 
L32B0:
32B0: 21 50 43        LD      HL,$4350            ; {+ram.M4350}
32B3: 06 30           LD      B,$30               ; 4350 to 437F
32B5: CD D8 05        CALL    $05D8               ; {code.ClearBbytesAtHL}
32B8: 2E 9A           LD      L,$9A               ; Counter9A
32BA: 06 04           LD      B,$04               ; 439A to 439D
32BC: CD D8 05        CALL    $05D8               ; {code.ClearBbytesAtHL}
32BF: 3A BB 43        LD      A,($43BB)           ; {ram.BirdsLeft}
32C2: A7              AND     A                   ; updates the zero flag
32C3: C8              RET     Z                   ; if no BirdsLeft
32C4: 07              RLCA                        ; Multiply by 8 ..
32C5: 07              RLCA                        ; ..
32C6: 07              RLCA                        ; ..
32C7: 4F              LD      C,A                 
32C8: 21 70 4B        LD      HL,$4B70            ; {+ram.M4B70}
32CB: 06 40           LD      B,$40               
32CD: CD D8 05        CALL    $05D8               ; {code.ClearBbytesAtHL}
32D0: 16 4B           LD      D,$4B               
32D2: 26 3F           LD      H,$3F               
32D4: 3E 40           LD      A,$40               
32D6: 91              SUB     C                   
32D7: C6 70           ADD     $70                 
32D9: 5F              LD      E,A                 
32DA: C6 10           ADD     $10                 
32DC: 6F              LD      L,A                 
32DD: 41              LD      B,C                 
32DE: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
32E1: 0F              RRCA                        
32E2: 0F              RRCA                        
32E3: D2 E0 05        JP      NC,$05E0            ; {code.CopyBbytesHLtoDE}
32E6: 7D              LD      A,L                 
32E7: C6 40           ADD     $40                 
32E9: 6F              LD      L,A                 
32EA: C3 E0 05        JP      $05E0               ; {code.CopyBbytesHLtoDE}

; not used
32ED: CD E0 05        CALL    $05E0               ; {code.CopyBbytesHLtoDE}
32F0: C3 A0 03        JP      $03A0               ; {code.ClearBackground}
; 
32F3: FF FF FF FF FF FF FF FF FF FF FF FF FF

; Mapping table for T3310.
T3300:
3300: 00 01 02 02 03 03 03 03
; not used
3308: FF FF FF FF FF FF FF FF

; Pointer table for T3330.
; T1160, T1020, T1020, T10A8
; T1160, T1020, T1020, T2C90...
; The random values (0, 2, 4 or 6) are added in order to
; address the rest of T3330.
T3310:
3310: 88 90 98 A0
3314: 68 70 78 80
3318: 48 50 58 60
331C: 48 30 38 40
3320: 88 90 98 A0
3324: A8 B0 B8 C0
3328: C8 D0 D8 E0
332C: C8 E8 F0 F8

; Base adresses of closed loop pattern tables for aliens.
; T1130, T2C00, T2FA0...
T3330:
3330: 11 30 2C 00 2F A0 2C 00 2E C4 2F A0 2F 34 2F A0
3340: 2C C8 2E C4 2E 20 2E C4 11 30 13 9C 13 D0 2C 00
3350: 11 30 13 28 2C 00 2F 34 11 A4 2C 90 2F 34 2F A0
3360: 2C 90 2C C8 2E 20 2E C4 11 60 13 54 13 9C 13 D0
3370: 10 20 10 64 11 A4 13 28 10 20 11 A4 12 00 2F 34
3380: 2C 90 2C C8 2D C0 2E 20 11 60 12 44 12 88 13 54
3390: 10 20 10 64 12 00 12 44 10 20 12 00 10 20 12 00
33A0: 10 A8 2D 88 10 A8 2D C0 11 D0 12 CA 13 00 13 54
33B0: 10 20 10 64 10 D4 13 00 10 20 10 D4 12 00 2F 00
33C0: 2D 00 2D 44 2D 88 2E 6C 11 00 11 D0 12 CA 2F 64
33D0: 11 00 13 00 2F 64 2F 00 10 D4 2D 00 2F 00 2C 34
33E0: 2D 00 2D 44 2E 6C 2E 90 11 00 2C 34 2F 64 2F 64
33F0: 2E 90 2F 00 2C 34 2C 34 2D 44 2E 6C 2E 90 2E 90

;*****************************************************************************
;* Game level 7
;* birds level including 'fade in'
;*****************************************************************************
L3400:
3400: CD 76 08        CALL    $0876               ; {code.PlayerUpdate} Updates the player ship, player bullet and the shield.
3403: CD 00 38        CALL    $3800               ; {code.L3800} Collision detection for birds
3406: CD 00 26        CALL    $2600               ; {code.L2600} birds vertical movement update (with 58xx scroll register)
3409: CD 00 38        CALL    $3800               ; {code.L3800} Collision detection for birds
340C: CD 80 39        CALL    $3980               ; {code.L3980}
340F: 3A BB 43        LD      A,($43BB)           ; {ram.BirdsLeft}
3412: A7              AND     A                   ; updates the zero flag
3413: CA 62 34        JP      Z,$3462             ; {+code.L3462} if no BirdsLeft.
3416: FE 04           CP      $04                 ; 
3418: D2 38 34        JP      NC,$3438            ; {+code.L3438} if >= $04
341B: CD 74 34        CALL    $3474               ; {code.DrawFirst4BirdObjects} including the horizontal movement update
341E: CD 86 34        CALL    $3486               ; {code.DrawSecond4BirdObjects} including the horizontal movement update
3421: CD 60 35        CALL    $3560               ; {code.L3560}
3424: CD 98 34        CALL    $3498               ; {code.L3498}
3427: CD AA 34        CALL    $34AA               ; {code.L34AA}
342A: 3A 9B 43        LD      A,($439B)           ; {ram.Counter9A+1}
342D: 0F              RRCA                        
342E: DA C0 0F        JP      C,$0FC0             ; {code.L0FC0} Handle animations for killed aliens
3431: CD 30 39        CALL    $3930               ; {code.L3930}
3434: C3 40 0C        JP      $0C40               ; {code.EnemyBulletUpdate}
; 
3437: FF
; 
L3438:
3438: 3A 9B 43        LD      A,($439B)           ; {ram.Counter9A+1}
343B: 0F              RRCA                        
343C: DA 52 34        JP      C,$3452             ; {+code.L3452}
343F: CD 74 34        CALL    $3474               ; {code.DrawFirst4BirdObjects}
3442: CD 60 35        CALL    $3560               ; {code.L3560}
3445: CD 98 34        CALL    $3498               ; {code.L3498}
3448: CD 30 39        CALL    $3930               ; {code.L3930}
344B: C3 40 0C        JP      $0C40               ; {code.EnemyBulletUpdate}
; 
344E: FF FF FF FF
; 
L3452:
3452: CD 86 34        CALL    $3486               ; {code.DrawSecond4BirdObjects}
3455: CD 60 35        CALL    $3560               ; {code.L3560}
3458: CD AA 34        CALL    $34AA               ; {code.L34AA}
345B: C3 C0 0F        JP      $0FC0               ; {code.L0FC0} Handle animations for killed aliens
; 
345E: FF FF FF FF
; 
L3462:
3462: 3A 9B 43        LD      A,($439B)           ; {ram.Counter9A+1}
3465: 0F              RRCA                        
3466: D8              RET     C                   
3467: CD 40 0C        CALL    $0C40               ; {code.EnemyBulletUpdate}
346A: CD C0 0F        CALL    $0FC0               ; {code.L0FC0} Handle animations for killed aliens
346D: C3 04 22        JP      $2204               ; {code.L2204}
; 
3470: FF FF FF FF

;*****************************************************************************
;* Draw bird objects 0 to 3.
;* Including the horizontal movement update.
;*****************************************************************************
DrawFirst4BirdObjects:
3474: 21 70 4B        LD      HL,$4B70            ; {!+ram.B4B70}
;
L3477:
3477: E5              PUSH    HL                  ; 
3478: CD C0 34        CALL    $34C0               ; {code.DrawBirdObject}
347B: E1              POP     HL                  ; 
347C: 7D              LD      A,L                 ; 
347D: C6 08           ADD     $08                 ; go to next bird object
347F: 6F              LD      L,A                 ; 
3480: FE 90           CP      $90                 ; for bird0 to bird3
3482: C2 77 34        JP      NZ,$3477            ; {+code.L3477}
3485: C9              RET                         ; 

;*****************************************************************************
;* Draw bird objects 4 to 7.
;* Including the horizontal movement update.
;*****************************************************************************
DrawSecond4BirdObjects:
3486: 21 90 4B        LD      HL,$4B90            ; {!+ram.B4B90}
;
L3489:
3489: E5              PUSH    HL                  ; 
348A: CD C0 34        CALL    $34C0               ; {code.DrawBirdObject}
348D: E1              POP     HL                  ; 
348E: 7D              LD      A,L                 ; 
348F: C6 08           ADD     $08                 ; go to next bird object
3491: 6F              LD      L,A                 ; 
3492: FE B0           CP      $B0                 ; for bird4 to bird7
3494: C2 89 34        JP      NZ,$3489            ; {+code.L3489}
3497: C9              RET                         ; 

; 
L3498:
3498: 21 70 4B        LD      HL,$4B70            ; {!+ram.B4B70}
; 
L349B:
349B: E5              PUSH    HL                  ; 
349C: CD B0 35        CALL    $35B0               ; {code.L35B0}
349F: E1              POP     HL                  ; 
34A0: 7D              LD      A,L                 ; 
34A1: C6 08           ADD     $08                 ; go to next bird object
34A3: 6F              LD      L,A                 ; 
34A4: FE 90           CP      $90                 ; for bird 0 to bird3
34A6: C2 9B 34        JP      NZ,$349B            ; {+code.L349B}
34A9: C9              RET                         ; 

; 
L34AA:
34AA: 21 90 4B        LD      HL,$4B90            ; {!+ram.B4B90}
; 
L34AD:
34AD: E5              PUSH    HL                  ; 
34AE: CD B0 35        CALL    $35B0               ; {code.L35B0}
34B1: E1              POP     HL                  ; 
34B2: 7D              LD      A,L                 ; 
34B3: C6 08           ADD     $08                 ; go to next bird object
34B5: 6F              LD      L,A                 ; 
34B6: FE B0           CP      $B0                 ; for bird4 to bird7
34B8: C2 AD 34        JP      NZ,$34AD            ; {+code.L34AD}
34BB: C9              RET                         ; 
;
34BC: FF FF FF FF

;*****************************************************************************
;* Draw a given bird object.
;* Input HL is the data structur of one bird object.
;* (For the 8 birds: $4B70, $4B78, $4B80, $4B88, $4B90, $4B98, $4BA0, $4BA8)
;*****************************************************************************
DrawBirdObject:
34C0: 7E              LD      A,(HL)              ; HL=$4B70 (or $4B78,...)
34C1: A7              AND     A                   ; updates the zero flag
34C2: C8              RET     Z                   ; if 0
34C3: 47              LD      B,A                 ; save it
34C4: C6 C0           ADD     $C0                 ; add to base for table T3EC0
34C6: 5F              LD      E,A                 ; save it
34C7: 16 3E           LD      D,$3E               ; MSB for T3EC0
34C9: 1A              LD      A,(DE)              ; get data starting from $3EC1
34CA: 4F              LD      C,A                 ; 
34CB: 2C              INC     L                   ; 
34CC: 56              LD      D,(HL)              ; get $4B71 MSB of screen ram
34CD: 2C              INC     L                   ; 
34CE: 5E              LD      E,(HL)              ; get $4B72 LSB of screen ram
34CF: 2C              INC     L                   ; 
34D0: 78              LD      A,B                 ; restore it
34D1: 07              RLCA                        ; Multiply by 8 ..
34D2: 07              RLCA                        ; ..
34D3: 07              RLCA                        ; ..
34D4: 86              ADD     A,(HL)              ; and add to $4B73 alien0 screen coordinate Y
34D5: E6 7E           AND     $7E                 ; mask out 0111_1110
34D7: 6F              LD      L,A                 ; 
34D8: 26 3E           LD      H,$3E               ; 
34DA: 7E              LD      A,(HL)              ; get MSB from address table for bird character block shapes (T3E08)
34DB: 2C              INC     L                   ; 
34DC: 6E              LD      L,(HL)              ; get LSB
34DD: 67              LD      H,A                 ; 
L34DE:
34DE: 7A              LD      A,D                 ; 
34DF: FE 4B           CP      $4B                 ; MSB of screen ram
34E1: C2 0C 35        JP      NZ,$350C            ; {+code.L350C} if value is not equal $4B
34E4: 7B              LD      A,E                 ; 
34E5: FE 50           CP      $50                 ; 
34E7: DA 0C 35        JP      C,$350C             ; {+code.L350C}
34EA: 06 08           LD      B,$08               ; 
34EC: 2C              INC     L                   ; 
34ED: 2C              INC     L                   ; 
34EE: D6 20           SUB     $20                 ; 
34F0: 5F              LD      E,A                 ; 
34F1: FE 50           CP      $50                 ; 
34F3: DA 09 35        JP      C,$3509             ; {+code.L3509}
34F6: 06 10           LD      B,$10               ; 
34F8: 2C              INC     L                   ; 
34F9: 2C              INC     L                   ; 
34FA: D6 20           SUB     $20                 ; 
34FC: 5F              LD      E,A                 ; 
34FD: FE 50           CP      $50                 ; 
34FF: DA 09 35        JP      C,$3509             ; {+code.L3509}
3502: 06 18           LD      B,$18               ; 
3504: 2C              INC     L                   ; 
3505: 2C              INC     L                   ; 
3506: D6 20           SUB     $20                 ; 
3508: 5F              LD      E,A                 ; 
;
L3509:
3509: 79              LD      A,C                 ; 
350A: 80              ADD     A,B                 ; 
350B: 4F              LD      C,A                 ; 
;
L350C:
350C: 06 35           LD      B,$35               ; MSB of return address for the draw shape entry.
350E: C5              PUSH    BC                  ; 
350F: 01 DF FF        LD      BC,$FFDF            ; Screen offset constant -33 right one column (-1), up one row (-32)
3512: EB              EX      DE,HL               ; 
3513: 36 00           LD      (HL),$00            ; delete character on screen
3515: 23              INC     HL                  ; 
3516: 36 00           LD      (HL),$00            ; delete character on screen
3518: 09              ADD     HL,BC               ; 
3519: C9              RET                         ; jumps to draw shape entry.
;
351A: FF FF FF FF FF FF

;*****************************************************************************
;* Draw a shape.
;* Entry dep. on size of shape: 2x2,3x2,4x2,5x2,6x2,7x2.
;*****************************************************************************
Draw7x2:
3520: 1A              LD      A,(DE)              ; 
3521: 77              LD      (HL),A              ; 
3522: 13              INC     DE                  ; 
3523: 23              INC     HL                  ; 
3524: 1A              LD      A,(DE)              ; 
3525: 77              LD      (HL),A              ; 
3526: 13              INC     DE                  ; 
3527: 09              ADD     HL,BC               ; 
Draw6x2:
3528: 1A              LD      A,(DE)              ; 
3529: 77              LD      (HL),A              ; 
352A: 13              INC     DE                  ; 
352B: 23              INC     HL                  ; 
352C: 1A              LD      A,(DE)              ; 
352D: 77              LD      (HL),A              ; 
352E: 13              INC     DE                  ; 
352F: 09              ADD     HL,BC               ; 
Draw5x2:
3530: 1A              LD      A,(DE)              ; 
3531: 77              LD      (HL),A              ; 
3532: 13              INC     DE                  ; 
3533: 23              INC     HL                  ; 
3534: 1A              LD      A,(DE)              ; 
3535: 77              LD      (HL),A              ; 
3536: 13              INC     DE                  ; 
3537: 09              ADD     HL,BC               ; 
Draw4x2:
3538: 1A              LD      A,(DE)              ; 
3539: 77              LD      (HL),A              ; 
353A: 13              INC     DE                  ; 
353B: 23              INC     HL                  ; 
353C: 1A              LD      A,(DE)              ; 
353D: 77              LD      (HL),A              ; 
353E: 13              INC     DE                  ; 
353F: 09              ADD     HL,BC               ; 
Draw3x2:
3540: 1A              LD      A,(DE)              ; 
3541: 77              LD      (HL),A              ; 
3542: 13              INC     DE                  ; 
3543: 23              INC     HL                  ; 
3544: 1A              LD      A,(DE)              ; 
3545: 77              LD      (HL),A              ; 
3546: 13              INC     DE                  ; 
3547: 09              ADD     HL,BC               ; 
Draw2x2:
3548: 1A              LD      A,(DE)              ; 
3549: 77              LD      (HL),A              ; 
354A: 13              INC     DE                  ; 
354B: 23              INC     HL                  ; 
354C: 1A              LD      A,(DE)              ; 
354D: 77              LD      (HL),A              ; 
354E: 13              INC     DE                  ; 
354F: 09              ADD     HL,BC               ; 
Draw1x2:
3550: 1A              LD      A,(DE)              ; 
3551: 77              LD      (HL),A              ; 
3552: 13              INC     DE                  ; 
3553: 23              INC     HL                  ; 
3554: 1A              LD      A,(DE)              ; 
3555: 77              LD      (HL),A              ; 
3556: 13              INC     DE                  ; 
3557: 09              ADD     HL,BC               ; 
;
L3558:
3558: 36 00           LD      (HL),$00            ; 
355A: 23              INC     HL                  ; 
355B: 36 00           LD      (HL),$00            ; 
355D: C9              RET                         ; 
;
355E: FF FF
; 
L3560:
3560: CD AA 30        CALL    $30AA               ; {code.GetRandomNumber}
3563: 47              LD      B,A                 ; 
3564: 07              RLCA                        ; Multiply by 4 ..
3565: 07              RLCA                        ; ..
3566: 4F              LD      C,A                 ; 
3567: 07              RLCA                        ; Multiply by 4 ..
3568: 07              RLCA                        ; ..
3569: B0              OR      B                   
356A: 32 6F 43        LD      ($436F),A           ; {ram.M436F}
356D: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
3570: FE 40           CP      $40                 ; 
3572: DA 77 35        JP      C,$3577             ; {code.L3577} if game round < 4
3575: 3E 30           LD      A,$30               
L3577:
3577: E6 30           AND     $30                 ; 0011_0000
3579: 0F              RRCA                        
357A: 47              LD      B,A                 
357B: 3A BB 43        LD      A,($43BB)           ; {ram.BirdsLeft}
357E: 3D              DEC     A                   
357F: FE 04           CP      $04                 
3581: DA 86 35        JP      C,$3586             ; {code.L3586}
3584: 3E 03           LD      A,$03               
L3586:
3586: 07              RLCA                        ; Multiply by 2
3587: B0              OR      B                   
3588: 47              LD      B,A                 
3589: 3A 9A 43        LD      A,($439A)           ; {ram.Counter9A}
358C: 07              RLCA                        ; Multiply by 4 ..
358D: 07              RLCA                        ; ..
358E: E6 20           AND     $20                 ; mask out 0010_0000
3590: B0              OR      B                   
3591: C6 80           ADD     $80                 
3593: 6F              LD      L,A                 
3594: 26 3E           LD      H,$3E               
3596: 7E              LD      A,(HL)              ; data from table T3E80
3597: 32 6E 43        LD      ($436E),A           ; {ram.M436E}
359A: 2C              INC     L                   
359B: 7E              LD      A,(HL)              ; data from table T3E80
359C: 81              ADD     A,C                 
359D: E6 F8           AND     $F8                 ; 1111_1000
359F: 32 6D 43        LD      ($436D),A           ; {ram.M436D}
35A2: C9              RET                         
; 
35A3: FF FF FF FF FF FF FF FF FF FF FF FF FF
; 
L35B0:
35B0: 7E              LD      A,(HL)              ; get index character block shape
35B1: A7              AND     A                   ; updates the zero flag
35B2: C8              RET     Z                   ; if index is 0
35B3: 47              LD      B,A                 ; save index to B
35B4: 2C              INC     L                   ; 
35B5: 2C              INC     L                   ; 
35B6: 2C              INC     L                   ; 
35B7: 2C              INC     L                   ; 
35B8: 7E              LD      A,(HL)              ; 
35B9: A7              AND     A                   ; updates the zero flag
35BA: CA BE 35        JP      Z,$35BE             ; {code.L35BE}
35BD: 35              DEC     (HL)                ; 
L35BE:
35BE: EB              EX      DE,HL               ; 
35BF: D5              PUSH    DE                  ; 
35C0: 78              LD      A,B                 ; load index
35C1: 07              RLCA                        ; Multiply by 8 ..
35C2: 07              RLCA                        ; ..
35C3: 07              RLCA                        ; ..
35C4: 6F              LD      L,A                 ; 
35C5: 26 3F           LD      H,$3F               ; MSB of table T3F00 for stack manipulation
35C7: 46              LD      B,(HL)              ; get 1st byte
35C8: 23              INC     HL                  ; 
35C9: 4E              LD      C,(HL)              ; get 2nd byte
35CA: C5              PUSH    BC                  ; to stack
35CB: 23              INC     HL                  ; 
35CC: 46              LD      B,(HL)              ; get 3rd byte
35CD: 23              INC     HL                  ; 
35CE: 4E              LD      C,(HL)              ; get 4rd byte
35CF: C5              PUSH    BC                  ; to stack
35D0: 23              INC     HL                  ; 
35D1: 46              LD      B,(HL)              ; get MSB of 1st address
35D2: 23              INC     HL                  ; 
35D3: 4E              LD      C,(HL)              ; get LSB of 1st address
35D4: C5              PUSH    BC                  ; to stack
35D5: 23              INC     HL                  ; 
35D6: 46              LD      B,(HL)              ; get MSB of 2nd address
35D7: 23              INC     HL                  ; 
35D8: 4E              LD      C,(HL)              ; get LSB of 2nd address
35D9: C5              PUSH    BC                  ; to stack
35DA: EB              EX      DE,HL               ; 
35DB: C9              RET                         ; calls the 2nd address

35DC: FF FF FF FF
; called by $35B0
L35E0:
35E0: 2C              INC     L                   
35E1: 2C              INC     L                   
35E2: 7E              LD      A,(HL)              
35E3: FE 10           CP      $10                 
35E5: D2 28 36        JP      NC,$3628            ; {code.L3628} if >= $10
35E8: 47              LD      B,A                 
35E9: 2D              DEC     L                   
35EA: 86              ADD     A,(HL)              
35EB: 77              LD      (HL),A              
35EC: 2D              DEC     L                   
35ED: 2D              DEC     L                   
35EE: 78              LD      A,B                 
35EF: 86              ADD     A,(HL)              
35F0: 77              LD      (HL),A              
35F1: FE 08           CP      $08                 
35F3: DA 6A 36        JP      C,$366A             ; {code.L366A}
35F6: E6 07           AND     $07                 ; 0000_0111
35F8: 77              LD      (HL),A              
35F9: 2D              DEC     L                   
35FA: 7E              LD      A,(HL)              
35FB: D6 20           SUB     $20                 
35FD: 77              LD      (HL),A              
35FE: D2 04 36        JP      NC,$3604            ; {code.L3604}
3601: 2D              DEC     L                   
3602: 35              DEC     (HL)                
3603: 2C              INC     L                   
L3604:
3604: 2C              INC     L                   
3605: 2C              INC     L                   
3606: 2C              INC     L                   
3607: 4E              LD      C,(HL)              
3608: 2C              INC     L                   
3609: 2C              INC     L                   
360A: 7E              LD      A,(HL)              
360B: 2D              DEC     L                   
360C: 36 10           LD      (HL),$10            
360E: 91              SUB     C                   
360F: CA 72 36        JP      Z,$3672             ; {code.L3672}
3612: 3D              DEC     A                   
3613: 0F              RRCA                        
3614: 0F              RRCA                        
3615: 0F              RRCA                        
3616: E6 1F           AND     $1F                 ; 0001_1111
3618: B8              CP      B                   
3619: 3C              INC     A                   
361A: 77              LD      (HL),A              
361B: D8              RET     C                   
361C: 3A 6E 43        LD      A,($436E)           ; {ram.M436E}
361F: 77              LD      (HL),A              
3620: B8              CP      B                   
3621: C8              RET     Z                   
3622: 04              INC     B                   
3623: 70              LD      (HL),B              
3624: C9              RET                         
; 
3625: FF FF FF

L3628:
3628: E6 0F           AND     $0F                 ; 0000_1111
362A: CA 44 37        JP      Z,$3744             ; {code.L3744}
362D: 47              LD      B,A                 
362E: 2D              DEC     L                   
362F: 7E              LD      A,(HL)              
3630: 90              SUB     B                   
3631: 77              LD      (HL),A              
3632: 2D              DEC     L                   
3633: 2D              DEC     L                   
3634: 7E              LD      A,(HL)              
3635: 90              SUB     B                   
3636: 77              LD      (HL),A              
3637: D2 95 36        JP      NC,$3695            ; {code.L3695}
363A: E6 07           AND     $07                 ; 0000_0111
363C: 77              LD      (HL),A              
363D: 2D              DEC     L                   
363E: 7E              LD      A,(HL)              
363F: C6 20           ADD     $20                 
3641: 77              LD      (HL),A              
3642: D2 48 36        JP      NC,$3648            ; {code.L3648}
3645: 2D              DEC     L                   
3646: 34              INC     (HL)                
3647: 2C              INC     L                   
L3648:
3648: 2C              INC     L                   
3649: 2C              INC     L                   
364A: 2C              INC     L                   
364B: 7E              LD      A,(HL)              
364C: 2C              INC     L                   
364D: 2C              INC     L                   
364E: 96              SUB     (HL)                
364F: 0F              RRCA                        
3650: 0F              RRCA                        
3651: 0F              RRCA                        
3652: E6 1F           AND     $1F                 ; 0001_1111
3654: B8              CP      B                   
3655: 3C              INC     A                   
3656: 2D              DEC     L                   
3657: DA 63 36        JP      C,$3663             ; {code.L3663}
365A: 3A 6E 43        LD      A,($436E)           ; {ram.M436E}
365D: B8              CP      B                   
365E: CA 63 36        JP      Z,$3663             ; {code.L3663}
3661: 78              LD      A,B                 
3662: 3C              INC     A                   
L3663:
3663: F6 10           OR      $10                 ; 0001_0000
3665: 77              LD      (HL),A              
3666: C9              RET                         
; not used
3667: 77              LD      (HL),A              
3668: C9              RET                         
3669: FF
; 
L366A:
366A: 78              LD      A,B                 
366B: A7              AND     A                   ; updates the zero flag
366C: C0              RET     NZ                  
366D: 2C              INC     L                   
366E: 2C              INC     L                   
366F: 2C              INC     L                   
3670: 34              INC     (HL)                
3671: C9              RET                         
; 
L3672:
3672: 2D              DEC     L                   
3673: 46              LD      B,(HL)              
3674: 2C              INC     L                   
3675: 2C              INC     L                   
3676: 3A C2 43        LD      A,($43C2)           ; {ram.PlayerShipX}
3679: E6 F8           AND     $F8                 ; 1111_1000
367B: B8              CP      B                   
367C: D2 80 36        JP      NC,$3680            ; {code.L3680}
367F: 47              LD      B,A                 
L3680:
3680: 3A 6D 43        LD      A,($436D)           ; {ram.M436D}
3683: 4F              LD      C,A                 
3684: C6 08           ADD     $08                 
3686: 32 6D 43        LD      ($436D),A           ; {ram.M436D}
3689: 78              LD      A,B                 
368A: 91              SUB     C                   
368B: 36 08           LD      (HL),$08            
368D: D8              RET     C                   
368E: FE 08           CP      $08                 
3690: D8              RET     C                   
3691: 77              LD      (HL),A              
3692: C9              RET                         
; not used
3693: D8 FE 
;
L3695:
3695: 2C              INC     L                   
3696: 2C              INC     L                   
3697: 46              LD      B,(HL)              
3698: 2C              INC     L                   
3699: 2C              INC     L                   
369A: 7E              LD      A,(HL)              
369B: B8              CP      B                   
369C: C0              RET     NZ                  
369D: 2D              DEC     L                   
369E: 36 00           LD      (HL),$00            
36A0: 2C              INC     L                   
36A1: 3A C2 43        LD      A,($43C2)           ; {ram.PlayerShipX}
36A4: E6 F8           AND     $F8                 ; 1111_1000
36A6: B8              CP      B                   
36A7: DA AB 36        JP      C,$36AB             ; {code.L36AB}
36AA: 47              LD      B,A                 
L36AB:
36AB: 3A 6D 43        LD      A,($436D)           ; {ram.M436D}
36AE: C6 08           ADD     $08                 
36B0: 32 6D 43        LD      ($436D),A           ; {ram.M436D}
36B3: 80              ADD     A,B                 
36B4: 36 C8           LD      (HL),$C8            
36B6: D8              RET     C                   
36B7: FE C8           CP      $C8                 
36B9: D0              RET     NC                  
36BA: 77              LD      (HL),A              
36BB: C9              RET                         
; not used
36BC: 77              LD      (HL),A              
36BD: C9              RET                         

36BE: FF FF
; called by $35B0
L36C0:
36C0: 7E              LD      A,(HL)              ; 
36C1: 0F              RRCA                        ; 
36C2: D8              RET     C                   ; 
36C3: 2D              DEC     L                   
36C4: 7E              LD      A,(HL)              
36C5: 3C              INC     A                   
36C6: E6 07           AND     $07                 ; 0000_0111
36C8: 77              LD      (HL),A              
36C9: C9              RET                         
; 
36CA: FF FF
; called by $35B0
L36CC:
36CC: D1              POP     DE                  
36CD: C1              POP     BC                  
36CE: E1              POP     HL                  
36CF: C9              RET                         
; 
36D0: FF FF
; called by $35B0
L36D2:
36D2: D1              POP     DE                  ; 
36D3: C1              POP     BC                  ; 
36D4: E1              POP     HL                  ; 
36D5: 7E              LD      A,(HL)              ; 
36D6: A7              AND     A                   ; updates the zero flag
36D7: C0              RET     NZ                  ; 
36D8: 70              LD      (HL),B              
36D9: 2D              DEC     L                   
36DA: 2D              DEC     L                   
36DB: 2D              DEC     L                   
36DC: 2D              DEC     L                   
36DD: 72              LD      (HL),D              
36DE: 3A 68 43        LD      A,($4368)           ; {ram.M4368}
36E1: F6 01           OR      $01                 ; 0000_0001
36E3: 32 68 43        LD      ($4368),A           ; {ram.M4368}
36E6: C9              RET                         

36E7: FF FF FF
; called by $35B0
L36EA:
36EA: D1              POP     DE                  
36EB: C1              POP     BC                  
36EC: E1              POP     HL                  
36ED: 7E              LD      A,(HL)              
36EE: A7              AND     A                   ; updates the zero flag
36EF: C0              RET     NZ                  
36F0: 2C              INC     L                   
36F1: 2C              INC     L                   
36F2: 7E              LD      A,(HL)              
36F3: E6 0F           AND     $0F                 ; 0000_1111
36F5: C0              RET     NZ                  
36F6: 2D              DEC     L                   
36F7: 2D              DEC     L                   
36F8: 70              LD      (HL),B              
36F9: 2D              DEC     L                   
36FA: 2D              DEC     L                   
36FB: 2D              DEC     L                   
36FC: 2D              DEC     L                   
36FD: 72              LD      (HL),D              
36FE: 3A 68 43        LD      A,($4368)           ; {ram.M4368}
3701: F6 02           OR      $02                 ; 0000_0010
3703: 32 68 43        LD      ($4368),A           ; {ram.M4368}
3706: C9              RET                         
; 
3707: FF FF FF
; called by $35B0
L370A:
370A: D1              POP     DE                  
370B: C1              POP     BC                  
370C: E1              POP     HL                  
370D: 7E              LD      A,(HL)              
370E: A7              AND     A                   ; updates the zero flag
370F: C0              RET     NZ                  
3710: 2C              INC     L                   
3711: 2C              INC     L                   
3712: 7E              LD      A,(HL)              
3713: E6 0F           AND     $0F                 ; 0000_1111
3715: C0              RET     NZ                  
3716: 2D              DEC     L                   
3717: 2D              DEC     L                   
3718: 70              LD      (HL),B              
3719: 2D              DEC     L                   
371A: 2D              DEC     L                   
371B: 2D              DEC     L                   
371C: 2D              DEC     L                   
371D: 72              LD      (HL),D              
371E: 3A 68 43        LD      A,($4368)           ; {ram.M4368}
3721: F6 04           OR      $04                 ; 0000_0100
3723: 32 68 43        LD      ($4368),A           ; {ram.M4368}
3726: 3A 6F 43        LD      A,($436F)           ; {ram.M436F}
3729: A3              AND     E                   
372A: E6 F0           AND     $F0                 ; 1111_0000
372C: C0              RET     NZ                  
372D: 7B              LD      A,E                 
372E: E6 0F           AND     $0F                 ; 0000_1111
3730: 77              LD      (HL),A              
3731: 2C              INC     L                   
3732: 2C              INC     L                   
3733: 2C              INC     L                   
3734: 2C              INC     L                   
3735: 71              LD      (HL),C              
3736: 3A 68 43        LD      A,($4368)           ; {ram.M4368}
3739: F6 08           OR      $08                 ; 0000_1000
373B: 32 68 43        LD      ($4368),A           ; {ram.M4368}
373E: C9              RET                         

373F: FF FF FF FF FF

L3744:
3744: 36 11           LD      (HL),$11            
3746: 2D              DEC     L                   
3747: 35              DEC     (HL)                
3748: 2D              DEC     L                   
3749: 2D              DEC     L                   
374A: 36 07           LD      (HL),$07            
374C: 2D              DEC     L                   
374D: 7E              LD      A,(HL)              
374E: C6 20           ADD     $20                 
3750: 77              LD      (HL),A              
3751: D0              RET     NC                  
3752: 2D              DEC     L                   
3753: 34              INC     (HL)                
3754: C9              RET                         

3755: FF FF FF
; 
L3758:
3758: 7E              LD      A,(HL)              
3759: A7              AND     A                   ; updates the zero flag
375A: C8              RET     Z                   ; if 0
375B: 35              DEC     (HL)                
375C: CA CC 37        JP      Z,$37CC             ; {code.L37CC}
375F: 7E              LD      A,(HL)              
3760: 0F              RRCA                        
3761: D2 B0 37        JP      NC,$37B0            ; {code.L37B0} Prints the score value in the middle of the bonus explosion
3764: 3E 0F           LD      A,$0F               
3766: 96              SUB     (HL)                
3767: E6 0E           AND     $0E                 ; mask out 0000_1110
3769: 07              RLCA                        ; Multiply by 16 ..
376A: 07              RLCA                        ; ..
376B: 07              RLCA                        ; ..
376C: 07              RLCA                        ; ..
376D: 2C              INC     L                   
376E: 2C              INC     L                   
376F: 56              LD      D,(HL)              
3770: 2C              INC     L                   
3771: 5E              LD      E,(HL)              
3772: F5              PUSH    AF                  
3773: D5              PUSH    DE                  
3774: 01 DF FF        LD      BC,$FFDF            ; Screen offset constant -33 right one column (-1), up one row (-32)
3777: CD 96 37        CALL    $3796               ; {code.L3796} left part of bonus explosion animation
377A: D1              POP     DE                  
377B: F1              POP     AF                  
377C: 2F              CPL                         
377D: 6F              LD      L,A                 
377E: 26 FF           LD      H,$FF               
3780: 23              INC     HL                  
3781: 19              ADD     HL,DE               
3782: EB              EX      DE,HL               
3783: 21 A0 BF        LD      HL,$BFA0            
3786: 19              ADD     HL,DE               
3787: D0              RET     NC                  
3788: EB              EX      DE,HL               
3789: 11 D6 17        LD      DE,$17D6            ; {+code.T17D6} (Bonus explosion right part)
378C: 36 00           LD      (HL),$00            
378E: 23              INC     HL                  
378F: 36 00           LD      (HL),$00            
3791: 09              ADD     HL,BC               
3792: C3 40 35        JP      $3540               ; {code.Draw3x2}
; 
3795: FF

;*****************************************************************************
;* Draws the left part of bonus explosion animation.
;*****************************************************************************
L3796:
3796: C6 60           ADD     $60                 
3798: 6F              LD      L,A                 
3799: 26 00           LD      H,$00               
379B: D2 9F 37        JP      NC,$379F            ; {code.L379F}
379E: 24              INC     H                   
L379F:
379F: 19              ADD     HL,DE               
37A0: EB              EX      DE,HL               
37A1: 21 C0 BC        LD      HL,$BCC0            
37A4: 19              ADD     HL,DE               
37A5: D8              RET     C                   
37A6: EB              EX      DE,HL               
37A7: 11 D0 17        LD      DE,$17D0            ; {+code.T17D0} (Bonus explosion left part)
37AA: C3 40 35        JP      $3540               ; {code.Draw3x2}
; 
37AD: FF FF FF
; Prints the score value in the middle of the bonus explosion animation.
; First two digits are from $4379. Last digit is ever 0.
L37B0:
37B0: 2C              INC     L                   ; 
37B1: 7E              LD      A,(HL)              ; 
37B2: 27              DAA                         ; 
37B3: 77              LD      (HL),A              ; 
37B4: 2C              INC     L                   ; 
37B5: 56              LD      D,(HL)              ; 
37B6: 2C              INC     L                   ; 
37B7: 5E              LD      E,(HL)              ; 
37B8: 2D              DEC     L                   ; 
37B9: 2D              DEC     L                   ; 
37BA: 00              NOP                         ; 
37BB: CD 17 02        CALL    $0217               ; {code.RightOneColumn}
37BE: 3E 20           LD      A,$20               ; character code for '0' (the right digit of bonus score)
37C0: 12              LD      (DE),A              ; write to screen ram (upper left corner of object 17D6)
37C1: CD 10 02        CALL    $0210               ; {code.LeftOneColumn}
37C4: 06 02           LD      B,$02               ; for the left two digits
37C6: C3 C4 00        JP      $00C4               ; {code.PrintNumber} score value for bonus explosion
; 
37C9: FF FF FF
; 
L37CC:
37CC: 2C              INC     L                   
37CD: 2C              INC     L                   
37CE: 2C              INC     L                   
37CF: 7E              LD      A,(HL)              
37D0: E6 1F           AND     $1F                 ; 0001_1111
37D2: C6 20           ADD     $20                 
37D4: 6F              LD      L,A                 
37D5: 26 43           LD      H,$43               
37D7: 01 DF FF        LD      BC,$FFDF            ; Screen offset constant -33 right one column (-1), up one row (-32)
37DA: 11 1A 00        LD      DE,$001A            
L37DD:
37DD: 72              LD      (HL),D              
37DE: 23              INC     HL                  
37DF: 72              LD      (HL),D              
37E0: 09              ADD     HL,BC               
37E1: 1D              DEC     E                   
37E2: C2 DD 37        JP      NZ,$37DD            ; {code.L37DD}
37E5: C9              RET                         
; 
37E6: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

;*****************************************************************************
;* Collision detection for birds.
;*****************************************************************************
L3800:
3800: 3A C4 43        LD      A,($43C4)           ; {ram.PlayerBulletState}
3803: E6 08           AND     $08                 ; 0000_1000
3805: C8              RET     Z                   
3806: 3A E6 43        LD      A,($43E6)           ; {ram.AbovePlayerBulletMSB}
3809: C6 08           ADD     $08                 
380B: 57              LD      D,A                 
380C: 3A D2 4B        LD      A,($4BD2)           ; {!ram.B4BD2}
380F: 5F              LD      E,A                 
3810: 3A E7 43        LD      A,($43E7)           ; {ram.AbovePlayerBulletLSB}
3813: E6 E0           AND     $E0                 ; 1110_0000
3815: 47              LD      B,A                 
3816: 3A E7 43        LD      A,($43E7)           ; {ram.AbovePlayerBulletLSB}
3819: 93              SUB     E                   
381A: 00              NOP                         
381B: E6 1F           AND     $1F                 ; 0001_1111
381D: B0              OR      B                   
381E: 5F              LD      E,A                 
381F: 1A              LD      A,(DE)              
3820: D6 90           SUB     $90                 
3822: D8              RET     C                   
3823: 47              LD      B,A                 
3824: 3A C6 43        LD      A,($43C6)           ; {ram.PlayerBulletX}
3827: E6 07           AND     $07                 ; 0000_0111
3829: C6 00           ADD     $00                 
382B: 6F              LD      L,A                 
382C: 26 3E           LD      H,$3E               
382E: 4E              LD      C,(HL)              
382F: 7B              LD      A,E                 
3830: E6 0E           AND     $0E                 ; 0000_1110
3832: 07              RLCA                        ; Multiply by 4 ..
3833: 07              RLCA                        ; ..
3834: 5F              LD      E,A                 
3835: 3E A8           LD      A,$A8               
3837: 93              SUB     E                   
3838: 5F              LD      E,A                 
3839: 16 4B           LD      D,$4B               
383B: 78              LD      A,B                 
383C: FE 50           CP      $50                 
383E: DC 44 38        CALL    C,$3844             ; {code.L3844}
3841: C3 1C 39        JP      $391C               ; {code.L391C}

; A bird has been hit
L3844:
3844: C6 60           ADD     $60                 ; LSB of table T3B60
3846: 6F              LD      L,A                 
3847: 26 3B           LD      H,$3B               ; MSB of table T3B60
3849: 7E              LD      A,(HL)              
384A: A1              AND     C                   
384B: C8              RET     Z                   
384C: CD A1 38        CALL    $38A1               ; {code.L38A1}
384F: EB              EX      DE,HL               
3850: 7E              LD      A,(HL)              
3851: 36 00           LD      (HL),$00            
3853: 2C              INC     L                   
3854: 2C              INC     L                   
3855: 2C              INC     L                   
3856: 2C              INC     L                   
3857: 56              LD      D,(HL)              
3858: E1              POP     HL                  
3859: 21 BB 43        LD      HL,$43BB            ; {+ram.BirdsLeft}
385C: 35              DEC     (HL)                ; decrement number of BirdsLeft
385D: FE 0B           CP      $0B                 
385F: DA 94 38        JP      C,$3894             ; {code.L3894}
3862: 5F              LD      E,A                 
3863: 3E FF           LD      A,$FF               ; set bonus explosion flag
3865: 32 69 43        LD      ($4369),A           ; {ram.M4369}
3868: 21 78 43        LD      HL,$4378            ; {+ram.M4378}
386B: 01 10 10        LD      BC,$1010            ; C reg. set to: 'bonus explosion score 100'.
386E: 7B              LD      A,E                 
386F: FE 0F           CP      $0F                 
3871: CA FB 38        JP      Z,$38FB             ; {code.L38FB}
3874: 7A              LD      A,D                 
3875: 0F              RRCA                        
3876: E6 7C           AND     $7C                 ; 0111_1100
3878: C6 30           ADD     $30                 
387A: 4F              LD      C,A                 
387B: 7B              LD      A,E                 
387C: FE 0E           CP      $0E                 
387E: CA FB 38        JP      Z,$38FB             ; {code.L38FB}
3881: 79              LD      A,C                 
3882: 0F              RRCA                        
3883: 4F              LD      C,A                 
3884: 7B              LD      A,E                 
3885: FE 0C           CP      $0C                 
3887: D2 FB 38        JP      NC,$38FB            ; {code.L38FB} if >= $0C
388A: 79              LD      A,C                 
388B: 0F              RRCA                        
388C: 4F              LD      C,A                 
388D: C3 FB 38        JP      $38FB               ; {code.L38FB}
; 
3890: FF FF FF FF
; 
L3894:
3894: 01 05 0D        LD      BC,$0D05            
3897: 3E FF           LD      A,$FF               
3899: 32 64 43        LD      ($4364),A           ; {ram.M4364}
389C: C3 F8 38        JP      $38F8               ; {code.L38F8}

389F: FF FF
; 
L38A1:
38A1: D5              PUSH    DE                  
38A2: 0E 20           LD      C,$20               
38A4: EB              EX      DE,HL               
38A5: 23              INC     HL                  
38A6: 56              LD      D,(HL)              
38A7: 23              INC     HL                  
38A8: 5E              LD      E,(HL)              
; This is a simple protection against piracy !
; Changing this single letter will result in a disturbing graphics garbage,
; when you hit a bird.
38A9: 3A 8C 19        LD      A,($198C)           ; {code.L198C} First letter 'R' from: " AMSTAR ELECTRONICS CORP. "
38AC: C6 DE           ADD     $DE                 ; 1101_1110
38AE: 6F              LD      L,A                 
38AF: 26 17           LD      H,$17               ; HL=$17F0 (FourByFourEmpty:)
38B1: CD DE 34        CALL    $34DE               ; {code.L34DE}
38B4: D1              POP     DE                  
38B5: C9              RET                         

; not used 
38B6: 35              DEC     (HL)                
38B7: D1              POP     DE                  
38B8: C9              RET                         
; 
38B9: FF FF FF
; 
L38BC:
38BC: C6 B0           ADD     $B0                 
38BE: 6F              LD      L,A                 
38BF: 26 3B           LD      H,$3B               
38C1: 7E              LD      A,(HL)              
38C2: A1              AND     C                   
38C3: C8              RET     Z                   
38C4: CD A1 38        CALL    $38A1               ; {code.L38A1}
38C7: 1A              LD      A,(DE)              
38C8: D6 0B           SUB     $0B                 
38CA: DA E9 38        JP      C,$38E9             ; {code.L38E9}
38CD: FE 03           CP      $03                 
38CF: D2 E9 38        JP      NC,$38E9            ; {code.L38E9} if >= $03
38D2: 47              LD      B,A                 
38D3: 62              LD      H,D                 
38D4: 7B              LD      A,E                 
38D5: C6 05           ADD     $05                 
38D7: 6F              LD      L,A                 
38D8: 3A C6 43        LD      A,($43C6)           ; {ram.PlayerBulletX}
38DB: BE              CP      (HL)                
38DC: 17              RLA                         
38DD: 07              RLCA                        ; Multiply by 4 ..
38DE: 07              RLCA                        ; ..
38DF: E6 04           AND     $04                 ; 0000_0100
38E1: B0              OR      B                   
38E2: C6 B8           ADD     $B8                 
38E4: 6F              LD      L,A                 
38E5: 26 3D           LD      H,$3D               
38E7: 7E              LD      A,(HL)              
38E8: 12              LD      (DE),A              
L38E9:
38E9: 3E FF           LD      A,$FF               
38EB: 32 66 43        LD      ($4366),A           ; {ram.M4366}
38EE: 01 02 07        LD      BC,$0702            
38F1: C3 F8 38        JP      $38F8               ; {code.L38F8}

38F4: FF FF FF FF
; 
L38F8:
38F8: 21 70 43        LD      HL,$4370            ; {+ram.M4370}
L38FB:
38FB: AF              XOR     A                   ; A=0
38FC: BE              CP      (HL)                
38FD: CA 06 39        JP      Z,$3906             ; {code.L3906}
3900: 2C              INC     L                   
3901: 2C              INC     L                   
3902: 2C              INC     L                   
3903: 2C              INC     L                   
3904: BE              CP      (HL)                
3905: C0              RET     NZ                  
L3906:
3906: 70              LD      (HL),B              
3907: 2C              INC     L                   
3908: 71              LD      (HL),C              
3909: 2C              INC     L                   
390A: 3A E6 43        LD      A,($43E6)           ; {ram.AbovePlayerBulletMSB}
390D: 77              LD      (HL),A              
390E: 2C              INC     L                   
390F: 3A E7 43        LD      A,($43E7)           ; {ram.AbovePlayerBulletLSB}
3912: 77              LD      (HL),A              
3913: 3A C4 43        LD      A,($43C4)           ; {ram.PlayerBulletState}
3916: E6 F7           AND     $F7                 ; 1111_0111
3918: 32 C4 43        LD      ($43C4),A           ; {ram.PlayerBulletState}
391B: C9              RET                         
; 
L391C:
391C: 78              LD      A,B                 
391D: FE 20           CP      $20                 
391F: D2 BC 38        JP      NC,$38BC            ; {code.L38BC} if >= $20
3922: C9              RET                         
; 
L3923:
3923: C8              RET     Z                   
3924: 35              DEC     (HL)                ; decrement $436B Counter for: 'mother ship score display'
3925: 2E 8D           LD      L,$8D               ; SoundControlB
3927: 7E              LD      A,(HL)              ; 
3928: E6 3F           AND     $3F                 ; 0011_1111
392A: F6 80           OR      $80                 ; 1000_0000
392C: 77              LD      (HL),A              ; 
392D: C9              RET                         ; 
; not used 
392E: C9              RET                         
; 
392F: FF
; 
L3930:
3930: 3A D2 4B        LD      A,($4BD2)           ; {!ram.B4BD2}
3933: E6 1E           AND     $1E                 ; 0001_1110
3935: C6 C0           ADD     $C0                 ; LSB of table T3DC0
3937: 6F              LD      L,A                 
3938: 26 3D           LD      H,$3D               ; MSB of table T3DC0
393A: 5E              LD      E,(HL)              
393B: 2C              INC     L                   
393C: 6E              LD      L,(HL)              
393D: 26 4B           LD      H,$4B               
393F: CD 00 3A        CALL    $3A00               ; {code.L3A00}
3942: 3A 9F 43        LD      A,($439F)           ; {ram.M439F}
3945: 82              ADD     A,D                 
3946: 4F              LD      C,A                 
3947: 3A 9E 43        LD      A,($439E)           ; {ram.M439E}
394A: 92              SUB     D                   
394B: 47              LD      B,A                 
L394C:
394C: E5              PUSH    HL                  
394D: CD 5C 39        CALL    $395C               ; {code.L395C}
3950: E1              POP     HL                  
3951: 7D              LD      A,L                 
3952: C6 08           ADD     $08                 
3954: 6F              LD      L,A                 
3955: 1D              DEC     E                   
3956: C2 4C 39        JP      NZ,$394C            ; {code.L394C}
3959: C9              RET                         

395A: FF FF
; 
L395C:
395C: 7E              LD      A,(HL)              
395D: FE 05           CP      $05                 
395F: D8              RET     C                   
3960: 7D              LD      A,L                 
3961: C6 05           ADD     $05                 
3963: 6F              LD      L,A                 
3964: 7E              LD      A,(HL)              
3965: B8              CP      B                   
3966: D8              RET     C                   
3967: B9              CP      C                   
3968: D0              RET     NC                  
3969: D6 04           SUB     $04                 
396B: 47              LD      B,A                 
396C: 2D              DEC     L                   
396D: 2D              DEC     L                   
396E: 2D              DEC     L                   
396F: 3A D2 4B        LD      A,($4BD2)           ; {!ram.B4BD2}
3972: 86              ADD     A,(HL)              
3973: E6 1F           AND     $1F                 ; 0001_1111
3975: 07              RLCA                        ; Multiply by 8 ..
3976: 07              RLCA                        ; ..
3977: 07              RLCA                        ; ..
3978: C6 08           ADD     $08                 
397A: 4F              LD      C,A                 
397B: C3 B7 25        JP      $25B7               ; {code.L25B7}

397E: FF FF
; 
L3980:
3980: 3A D2 4B        LD      A,($4BD2)           ; {!ram.B4BD2}
3983: D6 0C           SUB     $0C                 
3985: D8              RET     C                   
3986: FE 10           CP      $10                 
3988: D0              RET     NC                  
3989: 21 C4 43        LD      HL,$43C4            ; {+ram.PlayerBulletState}
398C: 11 C0 4B        LD      DE,$4BC0            ; {!+ram.B4BC0}
398F: 06 04           LD      B,$04               
3991: CD E0 05        CALL    $05E0               ; {code.CopyBbytesHLtoDE}
3994: 2E E6           LD      L,$E6               ; AbovePlayerBulletMSB
3996: 06 02           LD      B,$02               
3998: CD E0 05        CALL    $05E0               ; {code.CopyBbytesHLtoDE}
399B: 2E E2           LD      L,$E2               ; PlayerShipMSB
399D: 11 E6 43        LD      DE,$43E6            ; {+ram.AbovePlayerBulletMSB}
39A0: 06 02           LD      B,$02               
39A2: CD E0 05        CALL    $05E0               ; {code.CopyBbytesHLtoDE}
39A5: 2E C4           LD      L,$C4               ; PlayerBulletState
39A7: 36 08           LD      (HL),$08            
39A9: 11 9E 43        LD      DE,$439E            ; {+ram.M439E}
39AC: 3A 9B 43        LD      A,($439B)           ; {ram.Counter9A+1}
39AF: 0F              RRCA                        
39B0: DA BF 39        JP      C,$39BF             ; {code.L39BF}
39B3: 1C              INC     E                   
39B4: 2E E7           LD      L,$E7               ; AbovePlayerBulletLSB
39B6: 7E              LD      A,(HL)              
39B7: D6 20           SUB     $20                 
39B9: 77              LD      (HL),A              
39BA: 2D              DEC     L                   ; AbovePlayerBulletMSB
39BB: 7E              LD      A,(HL)              
39BC: DE 00           SBC     $00                 
39BE: 77              LD      (HL),A              
L39BF:
39BF: 1A              LD      A,(DE)              
39C0: 32 C6 43        LD      ($43C6),A           ; {ram.PlayerBulletX}
L39C3:
39C3: CD 00 38        CALL    $3800               ; {code.L3800} Collision detection for birds
39C6: 21 C4 43        LD      HL,$43C4            ; {+ram.PlayerBulletState}
39C9: 7E              LD      A,(HL)              
39CA: E6 08           AND     $08                 ; 0000_1000
39CC: CA F0 39        JP      Z,$39F0             ; {code.L39F0}
39CF: 21 E7 43        LD      HL,$43E7            ; {+ram.AbovePlayerBulletLSB}
39D2: 34              INC     (HL)                
39D3: 7E              LD      A,(HL)              
39D4: E6 1F           AND     $1F                 ; 0001_1111
39D6: FE 1D           CP      $1D                 
39D8: DA C3 39        JP      C,$39C3             ; {code.L39C3}
L39DB:
39DB: 21 C0 4B        LD      HL,$4BC0            ; {!+ram.B4BC0}
39DE: 11 C4 43        LD      DE,$43C4            ; {+ram.PlayerBulletState}
39E1: 06 04           LD      B,$04               
39E3: CD E0 05        CALL    $05E0               ; {code.CopyBbytesHLtoDE}
39E6: 1E E6           LD      E,$E6               
39E8: 06 02           LD      B,$02               
39EA: C3 E0 05        JP      $05E0               ; {code.CopyBbytesHLtoDE}

39ED: FF FF FF
; 
L39F0:
39F0: 2E A6           LD      L,$A6               ; ShieldCount
39F2: 7E              LD      A,(HL)              
39F3: FE C0           CP      $C0                 ; end of shield time
39F5: DA C4 0C        JP      C,$0CC4             ; {code.L0CC4}
39F8: D6 01           SUB     $01                 
39FA: 77              LD      (HL),A              
39FB: C3 DB 39        JP      $39DB               ; {code.L39DB}

39FE: FF FF
; 
L3A00:
3A00: 3A BB 43        LD      A,($43BB)           ; {ram.BirdsLeft}
3A03: D6 0C           SUB     $0C                 
3A05: 2F              CPL                         
3A06: 3C              INC     A                   
3A07: 57              LD      D,A                 
3A08: 3A 9B 43        LD      A,($439B)           ; {ram.Counter9A+1}
3A0B: 0F              RRCA                        
3A0C: 0F              RRCA                        
3A0D: D8              RET     C                   
3A0E: E1              POP     HL                  
3A0F: C9              RET                         
;
L3A10:
3A10: 21 B8 43        LD      HL,$43B8            ; {+ram.LevelAndRound}
3A13: 7E              LD      A,(HL)              ; get it
3A14: A7              AND     A                   ; updates the zero flag
3A15: C2 43 3B        JP      NZ,$3B43            ; {code.L3B43} if LevelAndRound is not 0.
3A18: 2E 8D           LD      L,$8D               ; set SoundControlB for...
3A1A: 36 CF           LD      (HL),$CF            ; ... 1100_1111 triggers Tune3 -- ESTUDIO (Phoenix theme song)
3A1C: C9              RET                         ; 
;
L3A1D:
3A1D: 21 69 43        LD      HL,$4369            ; {+ram.M4369}
3A20: 7E              LD      A,(HL)              ; 
3A21: A7              AND     A                   ; updates the zero flag
3A22: CA 40 3A        JP      Z,$3A40             ; {code.L3A40} if $4369 is 0.
3A25: FE 20           CP      $20                 
3A27: DA 2C 3A        JP      C,$3A2C             ; {code.L3A2C}
3A2A: 36 20           LD      (HL),$20            
L3A2C:
3A2C: 35              DEC     (HL)                
3A2D: 7E              LD      A,(HL)              
3A2E: 07              RLCA                        ; Multiply by 4 ..
3A2F: 07              RLCA                        ; ..
3A30: 00              NOP                         
3A31: 2F              CPL                         
3A32: E6 0E           AND     $0E                 ; 0000_1110
3A34: 2E 8D           LD      L,$8D               ; SoundControlB
3A36: 77              LD      (HL),A              
3A37: 2E 68           LD      L,$68               ; $4368
3A39: 36 00           LD      (HL),$00            
3A3B: 2E 66           LD      L,$66               ; $4366
3A3D: 36 00           LD      (HL),$00            
3A3F: C9              RET                         
; 
L3A40:
3A40: 2E 64           LD      L,$64               ; $4364
3A42: 7E              LD      A,(HL)              
3A43: A7              AND     A                   ; updates the zero flag
3A44: CA 62 3A        JP      Z,$3A62             ; {code.L3A62}
3A47: FE 10           CP      $10                 
3A49: DA 4E 3A        JP      C,$3A4E             ; {code.L3A4E}
3A4C: 36 10           LD      (HL),$10            
L3A4E:
3A4E: 35              DEC     (HL)                
3A4F: 7E              LD      A,(HL)              
3A50: 0F              RRCA                        
3A51: 00              NOP                         
3A52: 00              NOP                         
3A53: 2F              CPL                         
3A54: E6 07           AND     $07                 ; 0000_0111
3A56: F6 10           OR      $10                 ; 0001_0000
3A58: 2E 8C           LD      L,$8C               ; SoundControlA
3A5A: 77              LD      (HL),A              
3A5B: 2E 66           LD      L,$66               ; $4366
3A5D: 36 00           LD      (HL),$00            
3A5F: C9              RET                         

; not used 
3A60: 0F              RRCA                        
3A61: 00              NOP                         

;
L3A62:
3A62: 2E 66           LD      L,$66               ; $4366
3A64: 7E              LD      A,(HL)              
3A65: A7              AND     A                   ; updates the zero flag
3A66: C8              RET     Z                   
3A67: FE 10           CP      $10                 
3A69: DA 78 3A        JP      C,$3A78             ; {code.L3A78}
3A6C: 36 10           LD      (HL),$10            
3A6E: 3A B8 43        LD      A,($43B8)           ; {ram.LevelAndRound}
3A71: E6 08           AND     $08                 ; 0000_1000
3A73: CA 78 3A        JP      Z,$3A78             ; {code.L3A78}
3A76: 36 05           LD      (HL),$05            
L3A78:
3A78: 35              DEC     (HL)                
3A79: 2E 8C           LD      L,$8C               ; SoundControlA
3A7B: 7E              LD      A,(HL)              
3A7C: E6 08           AND     $08                 ; 0000_1000
3A7E: F6 04           OR      $04                 ; 0000_0100
3A80: 77              LD      (HL),A              
3A81: C9              RET                         
; 
L3A82:
3A82: 21 9A 43        LD      HL,$439A            ; {+ram.Counter9A}
3A85: 7E              LD      A,(HL)              
3A86: FE 03           CP      $03                 
3A88: D8              RET     C                   
3A89: 2E 8D           LD      L,$8D               ; SoundControlB
3A8B: 7E              LD      A,(HL)              
3A8C: E6 3F           AND     $3F                 ; 0011_1111
3A8E: 77              LD      (HL),A              
3A8F: C9              RET                         
; 
L3A90:
3A90: 21 6B 43        LD      HL,$436B            ; {+ram.M436B}
3A93: 7E              LD      A,(HL)              
3A94: A7              AND     A                   ; updates the zero flag
3A95: C3 23 39        JP      $3923               ; {code.L3923}
; 
L3A98:
3A98: 21 70 4B        LD      HL,$4B70            ; {+ram.M4B70}
3A9B: 01 00 08        LD      BC,$0800            
3A9E: 11 B0 03        LD      DE,$03B0            
L3AA1:
3AA1: 7E              LD      A,(HL)              
3AA2: 2C              INC     L                   
3AA3: A0              AND     B                   
3AA4: CA AE 3A        JP      Z,$3AAE             ; {code.L3AAE}
3AA7: 7E              LD      A,(HL)              
3AA8: FE 28           CP      $28                 
3AAA: DA AE 3A        JP      C,$3AAE             ; {code.L3AAE}
3AAD: 0C              INC     C                   
L3AAE:
3AAE: 7D              LD      A,L                 
3AAF: 82              ADD     A,D                 
3AB0: 6F              LD      L,A                 
3AB1: BB              CP      E                   
3AB2: C2 A1 3A        JP      NZ,$3AA1            ; {code.L3AA1}
3AB5: 79              LD      A,C                 
3AB6: A7              AND     A                   ; updates the zero flag
3AB7: C8              RET     Z                   
3AB8: FE 08           CP      $08                 
3ABA: DA BF 3A        JP      C,$3ABF             ; {code.L3ABF}
3ABD: 3E 08           LD      A,$08               
L3ABF:
3ABF: C6 25           ADD     $25                 
3AC1: 4F              LD      C,A                 
3AC2: 21 8C 43        LD      HL,$438C            ; {+ram.SoundControlA}
3AC5: 7E              LD      A,(HL)              
3AC6: E6 C0           AND     $C0                 ; mask out 1100_0000
3AC8: B1              OR      C                   
3AC9: 77              LD      (HL),A              ; trigger sound control A
3ACA: C9              RET                         
; 
3ACB: FF FF FF FF FF
; 
L3AD0:
3AD0: 21 8E 43        LD      HL,$438E            ; {+ram.M438E}
3AD3: 7E              LD      A,(HL)              
3AD4: E6 01           AND     $01                 ; 0000_0001
3AD6: 07              RLCA                        ; Multiply by 4 ..
3AD7: 07              RLCA                        ; ..
3AD8: F6 20           OR      $20                 ; 0010_0000
3ADA: 47              LD      B,A                 
3ADB: 2D              DEC     L                   
3ADC: 7E              LD      A,(HL)              
3ADD: E6 C0           AND     $C0                 ; 1100_0000
3ADF: B0              OR      B                   
3AE0: 77              LD      (HL),A              
3AE1: 2E 96           LD      L,$96               ; $4396
3AE3: 7E              LD      A,(HL)              
3AE4: 34              INC     (HL)                
3AE5: A7              AND     A                   ; updates the zero flag
3AE6: CA F8 3A        JP      Z,$3AF8             ; {code.L3AF8}
3AE9: 3A D6 4B        LD      A,($4BD6)           ; {!ram.B4BD6}
3AEC: C6 E0           ADD     $E0                 ; LSB of table T3DE0
3AEE: 5F              LD      E,A                 
3AEF: 16 3D           LD      D,$3D               ; MSB of table T3DE0
3AF1: 1A              LD      A,(DE)              
3AF2: BE              CP      (HL)                
3AF3: D0              RET     NC                  
3AF4: 36 00           LD      (HL),$00            
3AF6: C9              RET                         

; not used 
3AF7: 5F              LD      E,A                 

; 
L3AF8:
3AF8: 2E 8E           LD      L,$8E               ; $438E
3AFA: 34              INC     (HL)                
3AFB: 2D              DEC     L                   ; SoundControlB
3AFC: 7E              LD      A,(HL)              ; 
3AFD: F6 10           OR      $10                 ; 0001_0000
3AFF: 77              LD      (HL),A              ; 
3B00: C9              RET                         ; 

; not used 
3B01: 8E              ADC     A,(HL)              

; 
L3B02:
3B02: 21 9A 43        LD      HL,$439A            ; {+ram.Counter9A}
3B05: 7E              LD      A,(HL)              
3B06: FE 02           CP      $02                 
3B08: D0              RET     NC                  
3B09: 2C              INC     L                   
3B0A: 7E              LD      A,(HL)              
3B0B: 47              LD      B,A                 
3B0C: E6 60           AND     $60                 ; 0110_0000
3B0E: 2E 8D           LD      L,$8D               ; SoundControlB
3B10: 36 0A           LD      (HL),$0A            ; 0000_1010
3B12: C0              RET     NZ                  
3B13: 78              LD      A,B                 
3B14: E6 02           AND     $02                 ; 0000_0010
3B16: C6 1C           ADD     $1C                 
3B18: 77              LD      (HL),A              
3B19: C9              RET                         

; not used 
3B1A: 78              LD      A,B                 

; 
L3B1B:
3B1B: 21 62 43        LD      HL,$4362            ; {+ram.M4362}
3B1E: 7E              LD      A,(HL)              
3B1F: A7              AND     A                   ; updates the zero flag
3B20: C8              RET     Z                   ; if $4362 is 0.
3B21: FE 40           CP      $40                 
3B23: DA 28 3B        JP      C,$3B28             ; {code.L3B28}
3B26: 36 40           LD      (HL),$40            
L3B28:
3B28: 35              DEC     (HL)                
3B29: 7E              LD      A,(HL)              
3B2A: E6 06           AND     $06                 ; 0000_0110
3B2C: 07              RLCA                        ; Multiply by 2
3B2D: 00              NOP                         
3B2E: 2E 8D           LD      L,$8D               ; SoundControlB
3B30: 77              LD      (HL),A              
3B31: C9              RET                         

3B32: FF
; 
L3B33:
3B33: 21 6A 43        LD      HL,$436A            ; {+ram.M436A}
3B36: 7E              LD      A,(HL)              
3B37: A7              AND     A                   ; updates the zero flag
3B38: C8              RET     Z                   ; if $436A is 0.
3B39: 35              DEC     (HL)                
3B3A: E6 08           AND     $08                 ; 0000_1000
3B3C: F6 07           OR      $07                 ; 0000_0111
3B3E: 2E 8D           LD      L,$8D               ; SoundControlB
3B40: 77              LD      (HL),A              
3B41: C9              RET                         

; not used 
3B42: 8D              ADC     A,L                 
;
L3B43:
3B43: 21 A4 43        LD      HL,$43A4            ; {+ram.GameState}
3B46: 7E              LD      A,(HL)              ; 
3B47: FE 03           CP      $03                 ; 
3B49: CC D6 23        CALL    Z,$23D6             ; {code.L23D6} if GameState is 'normal game play'
3B4C: CD 33 3B        CALL    $3B33               ; {code.L3B33}
3B4F: CD 1B 3B        CALL    $3B1B               ; {code.L3B1B}
3B52: CD 1D 3A        CALL    $3A1D               ; {code.L3A1D}
3B55: CD BD 27        CALL    $27BD               ; {code.L27BD}
3B58: CD 82 3A        CALL    $3A82               ; {code.L3A82}
3B5B: C3 90 3A        JP      $3A90               ; {code.L3A90}
;
3B5E: FF FF
;
;?
T3B60:
3B60: 1F 7C F0 01 C0
3B65: 07 7F FC F0 07 C0 1F FF FC 03 F0
3B70: 0F C0 3F FC 1F F0 07 FE 3F F8 0F FF FF FC 1F FF
3B80: FC 1F FC 1F F0 7F F0 7F C0 FF 01 C0 FF 01 00 FF
3B90: 07 00 FF 07 FC 1F FC 1F F0 7F F0 7F C0 FF 01 C0
3BA0: FF 01 00 FF 07 FF 07 FC 1F F8 0F F0 C0 03 FF FF
3BB0: 03 E0 03 E0 0F 80 0F 00 3C 00 1E 3F 00 FC F0 00
3BC0: 7F FE 00 F0 03 E0 00 00 0F 80 00 00 3F 00 FE 30
3BD0: 00 06 FF 00 F8 00 00 03 E0 00 E0 08 20 04 C0 01
3BE0: E0 03 F8 0F 07 E0 3F 03 FF FF FF 3F FC FF F8 FF
3BF0: FF 07 E0 1F F0 FF FC FF 07 1E FC 1F 1F 7F FF FF

;bird character block shapes table (using character set B)
T3C00:
3C00: E8 00 E9 00 C4 C6 C5 C7 EA 00 EB 00 00 00       ;bird shape #24 [Object 3C00](bgtiles.html#object-3c00)
3C0E: EC 00 E9 00 C8 CA C9 CB EA 00 ED 00 00 00       ;#28 [Object 3C0E](bgtiles.html#object-3c0E)
3C1C: EE 00 EF 00 CC CF CD D0 CE D1 F0 00 F1 00       ;#29 [Object 3C1C](bgtiles.html#object-3c1c)
3C2A: F2 00 EF 00 D2 00 D3 D5 D4 D6 F0 00 F3 00       ;#30 [Object 3C2A](bgtiles.html#object-3c2a)
3C38: E8 00 E9 00 C4 C6 C5 C7 00 00                   ;#24 without right wing [Object 3C38](bgtiles.html#object-3c38)
3C42: EC 00 E9 00 C8 CA C9 CB 00 00                   ;#28 without right wing [Object 3C42](bgtiles.html#object-3c42)
3C4C: EE 00 EF 00 CC CF CD D0 DD D1                   ;#29 without right wing and regrowing ($DD) [Object 3C4C](bgtiles.html#object-3c4c)
3C56: F2 00 EF 00 D2 00 D3 D5 DD D6                   ;#30 without right wing and regrowing ($DD) [Object 3C56](bgtiles.html#object-3c56)
3C60: 00 00 00 00 C4 C6 C5 C7 EA 00 EB 00 00 00       ;#24 without left wing [Object 3C60](bgtiles.html#object-3c60)
3C6E: 00 00 00 00 DB CA C9 CB EA 00 ED 00 00 00       ;#28 without left wing and regrowing ($DB) [Object 3C6E](bgtiles.html#object-3c6e)
3C7C: 00 00 00 00 DC CF CD D0 CE D1 F0 00 F1 00       ;#29 without left wing and regrowing ($DC) [Object 3C7C](bgtiles.html#object-3c7c)
3C8A: 00 00 00 00 00 00 D3 D5 D4 D6 F0 00 F3 00       ;#30 without left wing [Object 3C8A](bgtiles.html#object-3c8a)
3C98: 00 00 00 00 C4 C6 C5 C7 00 00                   ;#24 without left and right wing [Object 3C98](bgtiles.html#object-3c98)
3CA2: 00 00 00 00 DB CA C9 CB 00 00                   ;#28 without left and right wing and regrowing ($DB) [Object 3CA2](bgtiles.html#object-3ca2)
3CAC: 00 00 00 00 DC CF CD D0 DD D1                   ;#29 without left and right wing and regrowing ($DC,$DD) [Object 3CAC](bgtiles.html#object-3cac)
3CB6: 00 00 00 00 00 00 D3 D5 DD D6                   ;#30 without left and right wing and regrowing ($DD) [Object 3CB6](bgtiles.html#object-3cb6)
3CC0: 00 00 DE E2 AB B2 AC B3 DF E3 00 00             ;#21 [Object 3CC0](bgtiles.html#object-3cc0)
3CCC: 00 00 00 E5 B4 B6 B5 B7 E4 E6 00 00             ;#25 [Object 3CCC](bgtiles.html#object-3ccc)
3CD8: 00 00 00 00 B8 BB B9 BC BA BD 00 00             ;#26 [Object 3CD8](bgtiles.html#object-3cd8)
3CE4: 00 00 00 00 BE C1 BF C2 C0 C3 00 E7             ;#27 [Object 3CE4](bgtiles.html#object-3ce4)
3CF0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF ;not used
3D00: 00 00 FA FC D7 D9 D8 DA FB FD 00 00             ;#22 [Object 3D00](bgtiles.html#object-3d00)
3D0C: F4 F6 F5 00 C4 C6 C5 C7 F7 00 F8 F9             ;#23 [Object 3D0C](bgtiles.html#object-3d0c)
3D18: 00 00 00 00 A7 A9 A8 AA 00 00                   ;#17 [Object 3D18](bgtiles.html#object-3d18)
3D22: 00 00 00 00 AB AD AC AE 00 00                   ;#18 [Object 3D22](bgtiles.html#object-3d22)
3D2C: 00 00 DE 00 AB B0 AC B1 DF 00                   ;#19 [Object 3D2C](bgtiles.html#object-3d2c)
3D36: 00 00 DE E0 AB B2 AC B3 DF E1                   ;#20 [Object 3D36](bgtiles.html#object-3d36)
3D40: 00 00 9D 00 9E 00 00 00                         ;#12 [Object 3D40](bgtiles.html#object-3d40)
3D48: 00 00 9F 00 A0 00 00 00                         ;#13 [Object 3D48](bgtiles.html#object-3d48)
3D50: 00 00 00 00 9C 00 00 00                         ;#11 [Object 3D50](bgtiles.html#object-3d50)
3D58: 00 00 00 00 A3 A5 A4 A6                         ;#16 [Object 3D58](bgtiles.html#object-3d58)
3D60: 00 00 9C 00 00 00                               ;#11 one pos moved to the left [Object 3D60](bgtiles.html#object-3d60)
3D66: 00 00 9D 00 9E 00                               ;#12 (but 3x2) [Object 3D66](bgtiles.html#object-3d66)
3D6C: 00 00 9F 00 A0 00                               ;#13 [Object 3D6C](bgtiles.html#object-3d6c)
3D72: 00 00 A1 00 A2 00                               ;#14 [Object 3D72](bgtiles.html#object-3d72)
3D78: 00 00 96 00 00 00                               ;#7 [Object 3D78](bgtiles.html#object-3d78)
3D7E: 00 00 97 00 93 00                               ;#8 [Object 3D7E](bgtiles.html#object-3d7e)
3D84: 00 00 98 00 99 00                               ;#9 [Object 3D84](bgtiles.html#object-3d84)
3D8A: 00 00 9A 00 9B 00                               ;#10 [Object 3D8A](bgtiles.html#object-3d8a)
3D90: 00 00 90 00 00 00                               ;#3 [Object 3D90](bgtiles.html#object-3d90)
3D96: 00 00 91 00 00 00                               ;#4 [Object 3D96](bgtiles.html#object-3d96)
3D9C: 00 00 92 00 93 00                               ;#5 [Object 3D9C](bgtiles.html#object-3d9c)
3DA2: 00 00 94 00 95 00                               ;#6 [Object 3DA2](bgtiles.html#object-3da2)
3DA8: 00 00 01 00                                     ;like small star [Object 3DA8](bgtiles.html#object-3da8)
3DAC: 00 00 08 00                                     ;like medium star [Object 3DAC](bgtiles.html#object-3cac)
3DB0: 00 00 0A 00                                     ;like big star [Object 3DB0](bgtiles.html#object-3db0)
3DB4: 00 00 0B 00 0C 0C 0E FF                         ;group of stars [Object 3DB4](bgtiles.html#object-3db4)
3DBC: 0D 0E 0D FF                                     ;group of stars [Object 3DBC](bgtiles.html#object-3dbc)

; ?
T3DC0:
3DC0: 06 70
3DC2: 07 70
3DC4: 08 70
3DC6: 08 70
3DC8: 08 70
3DCA: 07 78
3DCC: 06 80
3DCE: 05 88
3DD0: 04 90
3DD2: 03 98
3DD4: 02 A0
3DD6: 01 A8
3DD8: 02 70
3DDA: 03 70
3DDC: 04 70
3DDE: 05 70

; sinus motion like, y pos table used by big birds ?
T3DE0:
3DE0: 40 40 40 40 40 40 40 34 2C 26 20 1C 18 14 12 0F
3DF0: 0D 0B 09 08 07 06 05 04 03 02 02 02 02 02 02 02
3E00: 01 02 04 08 10 20 40 80

;address table for bird character block shapes (grouped by animation pattern)
T3E08:
3E08: 3D A8 ;like small star                  2x2
3E0A: 3D AC ;like medium star                 2x2
3E0C: 3D B0 ;like big star                    2x2

3E0E: 3D B4 ;group of stars

;growing up
3E10: 3D 90 ;#3                               3x2
3E12: 3D 96 ;#4                               3x2
3E14: 3D 9C ;#5                               3x2
3E16: 3D A2 ;#6                               3x2
3E18: 3D 78 ;#7                               3x2
3E1A: 3D 7E ;#8                               3x2
3E1C: 3D 84 ;#9                               3x2
3E1E: 3D 8A ;#10                              3x2
3E20: 3D 60 ;#11 one pos moved to the left    3x2
3E22: 3D 66 ;#12 (but 3x2)                    3x2
3E24: 3D 6C ;#13                              3x2
3E26: 3D 72 ;#14                              3x2

3E28: 3D 40 ;#12                              4x2
3E2A: 3D 48 ;#13                              4x2
3E2C: 3D 50 ;#11                              4x2
3E2E: 3D 58 ;#16                              4x2

3E30: 3D 18 ;#17                              5x2
3E32: 3D 22 ;#18                              5x2
3E34: 3D 2C ;#19                              5x2
3E36: 3D 36 ;#20                              5x2

3E38: 3C C0 ;#21                              6x2
3E3A: 3D 00 ;#22                              6x2
3E3C: 3D 0C ;#23                              6x2

3E3E: 3C 00 ;#24                              7x2

;get smaller and move to left
3E40: 3D 58 ;#16                              4x2
3E42: 3D 50 ;#11                              4x2
3E44: 3D 48 ;#13                              4x2
3E46: 3D 40 ;#12                              4x2

;get smaller
3E48: 3D 36 ;#20                              5x2
3E4A: 3D 2C ;#19                              5x2
3E4C: 3D 22 ;#18                              5x2
3E4E: 3D 18 ;#17                              5x2

;wings going down
3E50: 3C 00 ;#24                              7x2
3E52: 3D 0C ;#23                              6x2
3E54: 3D 00 ;#22                              6x2
3E56: 3C C0 ;#21                              6x2

;wings up and move to right
3E58: 3C 00 ;#24                              7x2
3E5A: 3C 0E ;#28                              7x2
3E5C: 3C 1C ;#29                              7x2
3E5E: 3C 2A ;#30                              7x2

;wings up and move to right
3E60: 3C 38 ;#24 without right wing           5x2
3E62: 3C 42 ;#28 without right wing           5x2
3E64: 3C 4C ;#29 without right wing reg.      5x2
3E66: 3C 56 ;#30 without right wing reg.      5x2

;wings up and move to right
3E68: 3C 60 ;#24 without left wing            7x2
3E6A: 3C 6E ;#28 without left wing reg.       7x2
3E6C: 3C 7C ;#29 without left wing reg.       7x2
3E6E: 3C 8A ;#30 without left wing            7x2

;wings up and move to right
3E70: 3C 98 ;#24 without left/right wing      5x2
3E72: 3C A2 ;#28 without left/right wing reg  5x2
3E74: 3C AC ;#29 without left/right wing reg  5x2
3E76: 3C B6 ;#30 without left/right wing reg  5x2

;wings down and move to right
3E78: 3C C0 ;#21                              6x2
3E7A: 3C CC ;#25                              6x2
3E7C: 3C D8 ;#26                              6x2
3E7E: 3C E4 ;#27                              6x2

;for birds
;copy to $436E,(+10) $436D
T3E80:
3E80: 05 40 
3E82: 05 20 
3E84: 04 30 
3E86: 04 10 
;not used?
3E88: 06 48 
3E8A: 06 28 
3E8C: 05 38 
3E8E: 05 18 
;not used?
3E90: 07 50 
3E92: 07 30 
3E94: 06 40 
3E96: 06 20 
;not used?
3E98: 08 58 
3E9A: 08 38 
3E9C: 07 48 
3E9E: 07 28 
;copy to $436E,(+10) $436D
3EA0: 06 10 
3EA2: 05 20 
3EA4: 05 30 
3EA6: 05 40 
;not used?
3EA8: 08 18 
3EAA: 07 28 
3EAC: 07 38 
3EAE: 06 48 
;not used?
3EB0: 08 20 
3EB2: 07 30 
3EB4: 07 40 
3EB6: 07 50 
;not used?
3EB8: 08 30 
3EBA: 08 40 
3EBC: 08 50 
3EBE: 08 60 

; LSB table for draw routine ($3520) entry.
; $3548, $3540, aso...
; for: 7x2, 7x3, 7x3, 7x3, 7x4, 7x5, 7x6, 7x4, 7x5, 7x6, 7x7, 7x5, 7x7, 7x5, 7x4.
T3EC0:
3EC0: FF
3EC1: 48 40 40 40 38 30 28 38 30 28 20 30 20 30 28

;big birds related. offsets for movement ?
T3ED0:
3ED0: 01 01 01 01
3ED4: 00 00 01 01
3ED8: 00 01 01 01
3EDC: 00 00 00 01

3EE0: 05 04 03 02 01 00
3EE6: 00 00 00 00 01 01
3EEC: 01 01 02 02
3EF0: 02 02 03 03
3EF4: 03 04 04 04
3EF8: 05 05 06 06
3EFC: 07 08 07 06

; Register contents and address for stack manipulation 
; used at level 3,4,8,9.
T3F00:
; for bird index to character block shape (0)
3F00: FF FF FF FF   ; not used
3F04: FF FF         ; not used
3F06: FF FF         ; not used
; for bird index to character block shape (1)
3F08: 20 FF 02 FF   ;BC and DE register contents
3F0C: 36 D2         ;address to call
3F0E: 36 C0         ;address to call
; for bird index to character block shape (2)
3F10: 20 FF 03 FF   ;
3F14: 36 D2         ;address
3F16: 35 E0         ;address
; for bird index to character block shape (3)
3F18: 30 FF 04 FF   ;
3F1C: 36 D2         ;address
3F1E: 35 E0         ;address
; for bird index to character block shape (4)
3F20: 10 FF 05 FF   ;
3F24: 36 EA         ;     address
3F26: 35 E0         ;address
; for bird index to character block shape (5)
3F28: 10 FF 06 FF   ;
3F2C: 36 EA         ;address
3F2E: 36 C0         ;address
; for bird index to character block shape (6)
3F30: 10 60 07 1F   ;
3F34: 37 0A         ;address
3F36: 36 C0         ;address
; for bird index to character block shape (7)
3F38: F0 10 0B 1A   ;
3F3C: 37 0A         ;address
3F3E: 36 C0         ;address
; for bird index to character block shape (8)
3F40: 40 FF 04 FF   ;
3F44: 36 EA         ;address
3F46: 36 C0         ;address
; for bird index to character block shape (9)
3F48: 10 FF 08 FF   ;
3F4C: 36 EA         ;address
3F4E: 36 C0         ;address
; for bird index to character block shape (A)
3F50: 40 10 0F 17   ;
3F54: 37 0A         ;address
3F56: 36 C0         ;address
; for bird index to character block shape (B)
3F58: 10 FF 0A FF   ;
3F5C: 36 EA         ;address
3F5E: 35 E0         ;address
; for bird index to character block shape (C)
3F60: FF FF FF FF   ;
3F64: 36 CC         ;address
3F66: 35 E0         ;address
; for bird index to character block shape (D)
3F68: FF FF FF FF   ;
3F6C: 36 CC         ;address
3F6E: 35 E0         ;address
; for bird index to character block shape (E)
3F70: 10 FF 06 FF   ;
3F74: 36 EA         ;address
3F76: 35 E0         ;address
; for bird index to character block shape (F)
3F78: 10 10 07 79   ;
3F7C: 37 0A         ;address
3F7E: 35 E0         ;address

;
;level 3 and 8 initial data for the 8 birds.
;data will be copied to $4B70-$4BAF
;.....:index to first character block shape
;........:MSB of initial screen address
;...........:LSB of the initial screen address
;..............:?
;.................:?
;....................:? grid coordinate x
;.......................:?
;..........................:? grid coordinate y
T3F80:
3F80: 01 48 EE 00 10 B0 10 20       ; 0
3F88: 01 49 2C 00 10 A0 00 B0       ; 1
3F90: 01 49 6A 00 10 90 00 B8       ; 2
3F98: 01 49 A8 00 10 80 00 C0       ; 3
3FA0: 01 49 E6 00 10 70 00 C8       ; 4
3FA8: 01 4A 24 00 10 60 00 C8       ; 5
3FB0: 01 4A 62 00 10 50 00 C8       ; 6
3FB8: 01 4A A0 00 10 40 00 C8       ; 7

;level 4 and 9 initial data for the 8 birds.
3FC0: 01 4A CE 00 10 38 00 B0       ; 0
3FC8: 01 48 CC 00 10 B8 10 20       ; 1
3FD0: 01 4A CA 00 10 38 00 B8       ; 2
3FD8: 01 48 C8 00 10 B8 10 18       ; 3
3FE0: 01 4A C6 00 10 38 00 C0       ; 4
3FE8: 01 48 C4 00 10 B8 10 10       ; 5
3FF0: 01 4A C2 00 10 38 00 C8       ; 6
3FF8: 01 48 C0 00 10 B8 10 08       ; 7
```

