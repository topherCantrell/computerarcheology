![Time Pilot](timeplt.jpg)

# Time Pilot

>>> cpu Z80

>>> binary 0000:roms/tm1 + roms/tm2 + roms/tm3

>>> memoryTable hard

[Hardware Info](Hardware.md)

>>> memoryTable ram

[RAM Usage](RAMUse.md)

```code
; Time Pilot (Konami, 1982). A free-roaming aerial shooter: your fighter holds
; the centre of the screen and turns to face the way you steer, while the
; whole world scrolls and banks around it, and you gun down swarms of enemy
; craft and the boss mother-ship that anchors each wave. Clearing a wave
; carries you forward through five eras of flight, each faster and more
; crowded than the last; parachutists drifting down are worth extra points if
; you collect them. Run out of fighters to end the game.
;
; Architecture: on reset ($0000) the CPU jumps to
; seatTheStackAndSettleTheControlLatch ($07B1). What follows is the code
; reached from the reset and interrupt entry points, shown as instructions;
; spans never reached appear as data (the "---- data ----" blocks).


; a bare transfer to 0x07B1 and no return; no cell is read or written and
; no register moves
trampolineToSeatTheStackAndSettleTheControlLatch:
0000: C3 B1 07        JP      $07B1               ; {code.seatTheStackAndSettleTheControlLatch}

; ---- $0003-$0007: data ----
0003: FF FF FF 33 4B

; step a table pointer on by an index and return the byte it lands on,
; leaving the pointer at that entry
fetchTableByte:
0008: 85              ADD     A,L                 ; step the byte-table pointer on by the index
0009: 6F              LD      L,A                 
000A: 30 01           JR      NC,$000D            ; {code.loc_000d} no carry out of the low byte -- the pointer's high half stands
000C: 24              INC     H                   ; carry into the table pointer's high byte

loc_000d:
000D: 7E              LD      A,(HL)              ; read the byte the pointer now lands on
000E: C9              RET                         

; ---- $000F-$000F: data ----
000F: 4F

; fetch the two-byte entry an index selects from a word table and hand
; back both the word and the address past it
fetchTableWord:
0010: 87              ADD     A,A                 ; double the entry number to reach its two-byte entry
0011: DF              RST     $18                 ; add that offset onto the word-table pointer
0012: 5E              LD      E,(HL)              ; read the entry's low byte
0013: 23              INC     HL                  
0014: 56              LD      D,(HL)              ; and its high byte
0015: 23              INC     HL                  ; leave the pointer just past the entry
0016: C9              RET                         

; ---- $0017-$0017: data ----
0017: 4E

; move a 16-bit address forward by an unsigned byte offset, echoing the
; low half of the result back
offsetAddress:
0018: 85              ADD     A,L                 ; add the unsigned byte offset onto the address
0019: 6F              LD      L,A                 
001A: D0              RET     NC                  ; no carry -- the address's high half stands
001B: 24              INC     H                   ; carry into the address's high byte
001C: C9              RET                         

; ---- $001D-$001F: data ----
001D: FF FF 41

; step the character-cell cursor on to the next cell of the line being
; drawn
advanceCharCursor:
0020: 7B              LD      A,E                 
0021: D6 20           SUB     $20                 ; drop the cursor thirty-two addresses on to the next cell of the line
0023: 5F              LD      E,A                 
0024: D0              RET     NC                  ; no borrow -- the cursor's high byte stands
0025: 15              DEC     D                   ; borrow into the cursor's high byte
0026: C9              RET                         

; ---- $0027-$0027: data ----
0027: 4D

; step the character-cell cursor one cell back along the line being drawn,
; the inverse of the advance vector
retreatCharCursor:
0028: 7B              LD      A,E                 
0029: C6 20           ADD     A,$20               ; push the cursor thirty-two addresses back, one cell along the line
002B: 5F              LD      E,A                 
002C: D0              RET     NC                  ; no carry -- the cursor's high byte stands
002D: 14              INC     D                   ; carry into the cursor's high byte
002E: C9              RET                         

; ---- $002F-$002F: data ----
002F: 49

loc_0030:
0030: E1              POP     HL                  ; take the inline word table the caller left behind -- its return address points straight at it
0031: D7              RST     $10                 ; index that table by the selector in A and read the entry it picks
0032: EB              EX      DE,HL               ; bring the selected arm's address into the jump register
0033: E9              JP      (HL)                ; jump to the selected arm -- control never returns to the table

; ---- $0034-$0037: data ----
0034: FF FF FF FF

; queue a command byte and its argument in the command ring, dropping the
; pair when the cursor's cell is still occupied
postCommand:
0038: E5              PUSH    HL                  
0039: 26 AC           LD      H,$AC               ; point the high byte at the command ring's page
003B: 3A B2 A9        LD      A,($A9B2)           ; {hard.workRam+1B2} fetch the ring's write cursor
003E: 6F              LD      L,A                 ; complete the pointer to the target cell
003F: CB 7E           BIT     7,(HL)              ; is that cell free? -- a free cell carries its high bit set
0041: 28 0A           JR      Z,$004D             ; {code.loc_004d} still occupied -- drop this command and return
0043: 72              LD      (HL),D              ; write the command byte
0044: 2C              INC     L                   
0045: 73              LD      (HL),E              ; write its argument
0046: 2C              INC     L                   
0047: 7D              LD      A,L                 
0048: E6 3F           AND     $3F                 ; wrap the cursor inside the sixty-four-cell ring
004A: 32 B2 A9        LD      ($A9B2),A           ; {hard.workRam+1B2} store the advanced write cursor

loc_004d:
004D: E1              POP     HL                  
004E: C9              RET                         

; ---- $004F-$0065: data ----
004F: 0F A7 11 ED 77 68 D7 34 F1 D7 A5 3B 7C FD 3B 7D
005F: F1 DC A5 8C 57 34 B9

; the per-frame (vblank) interrupt vector: hardware dispatches it once per
; interrupt and it transfers straight to the frame-service handler at
; 0x00d8, writing nothing of its own
enterVblankInterrupt:
0066: C3 D8 00        JP      $00D8               ; {code.saveAccumulatorForFrameInterrupt} hand the per-frame interrupt straight on to the frame-service handler

; cold-start clear reached once at boot via 0x07B1: kicks the watchdog
; four times, zeroes the 0xB410 sprite-bank run and the whole 2 KB work
; RAM, sums the fixed 256-byte program run at 0x00D8 and runs the frame
; service out of band on a non-genuine total, then hands off to the
; screen-RAM clear and image verify
clearWorkRamAndSpriteBanksThenColdInit:
0069: 32 00 C2        LD      ($C200),A           ; kick the watchdog
006C: 21 11 B4        LD      HL,$B411            ; point at the sprite-bank run
006F: 06 30           LD      B,$30               ; forty-eight bytes of it to clear

loc_0071:
0071: 36 00           LD      (HL),$00            ; clear this sprite-bank byte
0073: 23              INC     HL                  
0074: 10 FB           DJNZ    $0071               ; {code.loc_0071} on across the whole run
0076: 32 00 C2        LD      ($C200),A           ; kick the watchdog
0079: 21 10 B4        LD      HL,$B410            ; point at the second sprite bank
007C: 06 30           LD      B,$30               ; another forty-eight bytes to clear

loc_007e:
007E: 36 00           LD      (HL),$00            ; clear this sprite-bank byte
0080: 23              INC     HL                  
0081: 10 FB           DJNZ    $007E               ; {code.loc_007e} on across the run
0083: 32 00 C2        LD      ($C200),A           ; kick the watchdog
0086: 21 00 A8        LD      HL,$A800            ; point at the base of work RAM
0089: 11 01 A8        LD      DE,$A801            ; one cell on -- the block-fill destination
008C: 01 FF 07        LD      BC,$07FF            ; two kilobytes, less the seed cell, to clear
008F: 36 00           LD      (HL),$00            ; seed the first cell with zero
0091: ED B0           LDIR                        ; copy the zero forward through the whole of work RAM
0093: 32 00 C2        LD      ($C200),A           ; kick the watchdog
0096: 06 00           LD      B,$00               ; two hundred fifty-six bytes to fold
0098: 21 D8 00        LD      HL,$00D8            ; point at the fixed program run to fold -- the frame service's own bytes
009B: AF              XOR     A                   ; clear the running total

loc_009c:
009C: 86              ADD     A,(HL)              ; fold this byte into the total
009D: 23              INC     HL                  
009E: 10 FC           DJNZ    $009C               ; {code.loc_009c} on across all two hundred fifty-six bytes
00A0: D6 87           SUB     $87                 ; weigh the total against a genuine image's value
00A2: C4 D8 00        CALL    NZ,$00D8            ; {code.saveAccumulatorForFrameInterrupt} on a tampered image, run the frame service out of band
00A5: C3 66 58        JP      $5866               ; {code.clearScreenRamAndVerifyImageThenColdInit} hand off to the screen-RAM clear and image verify

; bring the machine up and never come back: set the interrupt-enable bit
; of the output latch from the low bit of the byte the caller carries, pet
; the watchdog, and fall into the foreground loop -- neither store reaches
; work RAM, and there is no return path
enableInterruptAndEnterForegroundLoop:
00A8: 32 00 C3        LD      ($C300),A           ; raise the interrupt-enable line from the low bit the caller carries
00AB: 32 00 C2        LD      ($C200),A           ; kick the watchdog
00AE: C3 93 0B        JP      $0B93               ; {code.runCommandRingDrainLoop} fall into the foreground command loop, never to return

; tile the character plane with a lattice of boxes -- fourteen bands of
; sixteen, each box two cells wide and two lines deep, every one of them
; laid down by stampGridBox -- walking a cursor that starts a full line
; above the first band it writes and skips a line before each band, so the
; lattice keeps clear of the top of the plane and its bands come out
; contiguous; every position is counted out here and nothing is read to
; decide where a box goes
tileCharPlaneWithBoxLattice:
00B1: 21 20 A4        LD      HL,$A420            ; point the cursor one line above the lattice's first band
00B4: 0E 0E           LD      C,$0E               ; fourteen bands to lay down

loc_00b6:
00B6: 11 20 00        LD      DE,$0020            
00B9: 19              ADD     HL,DE               ; skip a line before this band -- keeps the lattice off the top and spaces the bands
00BA: 06 10           LD      B,$10               ; sixteen boxes across the band

loc_00bc:
00BC: CD C7 00        CALL    $00C7               ; {code.stampGridBox} stamp one box at the cursor
00BF: 23              INC     HL                  ; step the cursor two cells on to the next box
00C0: 23              INC     HL                  
00C1: 10 F9           DJNZ    $00BC               ; {code.loc_00bc} on across all sixteen boxes of the band
00C3: 0D              DEC     C                   ; one band done
00C4: 20 F0           JR      NZ,$00B6            ; {code.loc_00b6} go lay the next band
00C6: C9              RET                         

; lay the four corner tiles of one hollow sixteen-by-sixteen box into the
; character plane at the cursor -- two cells across and two rows down --
; and give the cursor back unmoved
stampGridBox:
00C7: E5              PUSH    HL                  ; remember the cursor so it comes back unmoved
00C8: 36 56           LD      (HL),$56            ; stamp the box's top-left corner tile
00CA: 23              INC     HL                  
00CB: 36 83           LD      (HL),$83            ; stamp the top-right corner, one cell along
00CD: 11 1F 00        LD      DE,$001F            ; step down to the row below
00D0: 19              ADD     HL,DE               
00D1: 36 C7           LD      (HL),$C7            ; stamp the bottom-left corner
00D3: 23              INC     HL                  
00D4: 36 EF           LD      (HL),$EF            ; stamp the bottom-right corner
00D6: E1              POP     HL                  ; put the cursor back where it was found
00D7: C9              RET                         

; one byte, `push af`, falling into the register-save prologue at 0x00D9
; that owns the rest of the frame service and the frame's work; the two
; bytes it stacks land in work RAM, so they are part of what the machine
; leaves behind
saveAccumulatorForFrameInterrupt:
00D8: F5              PUSH    AF                  ; save the interrupted program's registers -- both banks and the index pair

loc_00d9:
00D9: C5              PUSH    BC                  
00DA: D5              PUSH    DE                  
00DB: E5              PUSH    HL                  
00DC: 08              EX      AF,AF'              
00DD: D9              EXX                         
00DE: F5              PUSH    AF                  
00DF: C5              PUSH    BC                  
00E0: D5              PUSH    DE                  
00E1: E5              PUSH    HL                  
00E2: DD E5           PUSH    IX                  
00E4: FD E5           PUSH    IY                  
00E6: CD 65 03        CALL    $0365               ; {code.publishSpriteShadow} copy the sprite shadow out to the hardware first, so the picture lands during blanking
00E9: CD 86 52        CALL    $5286               ; {code.drainBothDeferredCellLists} flush both deferred character-cell lists into the planes
00EC: AF              XOR     A                   
00ED: 32 00 C3        LD      ($C300),A           ; disarm this interrupt's own enable line
00F0: 32 00 C2        LD      ($C200),A           ; kick the watchdog
00F3: 3C              INC     A                   
00F4: 32 87 A9        LD      ($A987),A           ; {hard.workRam+187} provisionally mark the screen to flip this frame
00F7: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the cabinet flip setting
00FA: A7              AND     A                   
00FB: 28 09           JR      Z,$0106             ; {code.loc_0106} setting clear: leave the flip mark as it stands
00FD: 3A C2 A9        LD      A,($A9C2)           ; {hard.workRam+1C2} read which player is up
0100: A7              AND     A                   
0101: 20 03           JR      NZ,$0106            ; {code.loc_0106} the second player is up: leave the flip mark as it stands
0103: 32 87 A9        LD      ($A987),A           ; {hard.workRam+187} first player on a flip-enabled cabinet: clear the flip mark

loc_0106:
0106: 3A 87 A9        LD      A,($A987)           ; {hard.workRam+187} take the frame's flip decision
0109: 32 02 C3        LD      ($C302),A           ; drive the screen-flip latch line
010C: 3A 00 C2        LD      A,($C200)           ; read the dip-switch bank
010F: 2F              CPL                         ; invert it -- the ports read active-low
0110: 32 AD A9        LD      ($A9AD),A           ; {hard.workRam+1AD} store the mirror the game reads instead of the live port
0113: 3A 00 C3        LD      A,($C300)           ; read the player-one controls
0116: 2F              CPL                         
0117: 32 AE A9        LD      ($A9AE),A           ; {hard.workRam+1AE} store the player-one-control mirror
011A: 3A 20 C3        LD      A,($C320)           ; read the next input port
011D: 2F              CPL                         
011E: 32 AF A9        LD      ($A9AF),A           ; {hard.workRam+1AF} store its mirror
0121: 3A 40 C3        LD      A,($C340)           ; read the next input port
0124: 2F              CPL                         
0125: 32 B0 A9        LD      ($A9B0),A           ; {hard.workRam+1B0} store its mirror
0128: 3A 60 C3        LD      A,($C360)           ; read the last input port
012B: 2F              CPL                         
012C: 32 B1 A9        LD      ($A9B1),A           ; {hard.workRam+1B1} store its mirror
012F: 21 80 A9        LD      HL,$A980            
0132: 34              INC     (HL)                ; bump the plain binary frame counter
0133: 21 CE A9        LD      HL,$A9CE            
0136: 7E              LD      A,(HL)              
0137: 3C              INC     A                   ; step the decimal frame counter
0138: 27              DAA                         ; keep it counting in decimal
0139: 77              LD      (HL),A              
013A: 21 17 A8        LD      HL,$A817            ; point at the first frame-countdown timer
013D: 7E              LD      A,(HL)              
013E: A7              AND     A                   
013F: 28 01           JR      Z,$0142             ; {code.loc_0142} already run out: leave it at zero
0141: 35              DEC     (HL)                ; otherwise tick it down one frame

loc_0142:
0142: 21 12 A8        LD      HL,$A812            ; point at the second countdown timer
0145: 7E              LD      A,(HL)              
0146: A7              AND     A                   
0147: 28 01           JR      Z,$014A             ; {code.loc_014a} already at zero: leave it
0149: 35              DEC     (HL)                ; tick it down one frame

loc_014a:
014A: 21 F4 A8        LD      HL,$A8F4            ; point at the third countdown timer
014D: 7E              LD      A,(HL)              
014E: A7              AND     A                   
014F: 28 01           JR      Z,$0152             ; {code.loc_0152} already at zero: leave it
0151: 35              DEC     (HL)                ; tick it down one frame

loc_0152:
0152: CD BE 48        CALL    $48BE               ; {code.serviceCoinInputs} run the coin service
0155: 21 74 01        LD      HL,$0174            
0158: E5              PUSH    HL                  ; push the epilogue's address as the dispatched arm's return
0159: 3A AB A9        LD      A,($A9AB)           ; {hard.workRam+1AB} read the game-mode selector
015C: E6 03           AND     $03                 ; keep its low two bits -- one of four modes
015E: F7              RST     $30                 ; dispatch through the inline table that follows, entering the selected mode handler

; ---- $015F-$0166: jump table ----
015F: C2 15 51 16 FE 17 1F 0F

loc_0167:
0167: 6F              LD      L,A                 
0168: A6              AND     (HL)                
0169: 14              INC     D                   
016A: 88              ADC     A,B                 
016B: 57              LD      D,A                 
016C: A5              AND     L                   
016D: BF              CP      A                   
016E: 34              INC     (HL)                
016F: D7              RST     $10                 
0170: F1              POP     AF                  
0171: 96              SUB     (HL)                
0172: F1              POP     AF                  
0173: B9              CP      C                   

loc_0174:
0174: CD D4 55        CALL    $55D4               ; {code.sendOldestQueuedSoundCommand} hand one queued byte off to the sound processor
0177: FD E1           POP     IY                  
0179: DD E1           POP     IX                  
017B: E1              POP     HL                  
017C: D1              POP     DE                  
017D: C1              POP     BC                  
017E: F1              POP     AF                  
017F: D9              EXX                         
0180: 08              EX      AF,AF'              
0181: E1              POP     HL                  
0182: D1              POP     DE                  
0183: C1              POP     BC                  
0184: 3A 00 16        LD      A,($1600)           ; {hard.rom+1600} read the interrupt-enable pattern from the program image
0187: 32 00 C3        LD      ($C300),A           ; re-arm this interrupt for the next frame
018A: F1              POP     AF                  
018B: C9              RET                         

; fetch the word an index selects from a word table, with the index
; doubling carrying into the high byte so the table may run past the reach
; of its narrow sibling
fetchWideTableWord:
018C: 87              ADD     A,A                 ; double the index to reach its two-byte entry
018D: 30 01           JR      NC,$0190            ; {code.loc_0190}
018F: 24              INC     H                   ; the doubling overflowed -- carry into the table's high byte so it may run past 256 entries

loc_0190:
0190: 85              ADD     A,L                 ; add the doubled index onto the table pointer
0191: 6F              LD      L,A                 
0192: 30 01           JR      NC,$0195            ; {code.loc_0195}
0194: 24              INC     H                   ; carry into the pointer's high byte

loc_0195:
0195: 5E              LD      E,(HL)              ; read the entry's low byte
0196: 23              INC     HL                  
0197: 56              LD      D,(HL)              ; and its high byte
0198: 23              INC     HL                  ; leave the pointer just past the entry
0199: C9              RET                         

; seat the character-plane wipe on the plane's very first cell and put a
; whole plane's worth of lines against the counter beside it, so the next
; pass starts at the top with everything still to do; then fold a fixed
; 240-byte run of the program image into one eight-bit total and, on
; anything but the total a genuine image gives, transfer into bytes that
; carry no routine. The wipe is armed EITHER WAY -- the fold gates nothing
; above it, and the run it folds lies elsewhere in the image and has
; nothing to do with the wipe -- so a reader who takes this for a guarded
; arm will be wrong on every dispatch
armWholePlaneWipeThenDerailOnATamperedImage:
019A: 21 00 A4        LD      HL,$A400            ; the character plane's first cell
019D: 22 89 A9        LD      ($A989),HL          ; {hard.workRam+189} seat the wipe cursor there
01A0: 3E 20           LD      A,$20               ; thirty-two lines -- the whole plane
01A2: 32 88 A9        LD      ($A988),A           ; {hard.workRam+188} set that as the lines-left count
01A5: 06 F0           LD      B,$F0               ; two hundred forty bytes of the image to fold
01A7: 21 A5 4B        LD      HL,$4BA5            ; point at the checked run of the program image
01AA: AF              XOR     A                   ; clear the running total

loc_01ab:
01AB: 86              ADD     A,(HL)              ; fold this byte into the total
01AC: 23              INC     HL                  
01AD: 10 FC           DJNZ    $01AB               ; {code.loc_01ab} on across all two hundred forty bytes
01AF: D6 11           SUB     $11                 ; weigh the total against a genuine image's value
01B1: C4 67 01        CALL    NZ,$0167            ; {code.loc_0167} on a tampered image, transfer into bytes that carry no routine
01B4: C9              RET                         

; arm the character-plane wipe to start at the plane's fifth cell and to
; run for a count taken from a fixed cell of the program image rather than
; carried as an immediate; neither armed cell is read here, and nothing a
; caller held survives into either
armLineWipeFromFifthLine:
01B5: 21 04 A4        LD      HL,$A404            ; the plane's fifth cell, where this wipe starts
01B8: 22 89 A9        LD      ($A989),HL          ; {hard.workRam+189} seat the wipe cursor there
01BB: 3A CD 0C        LD      A,($0CCD)           ; {hard.rom+CCD} take the line count from a fixed cell of the program image
01BE: 32 88 A9        LD      ($A988),A           ; {hard.workRam+188} set it as the lines-left count
01C1: C9              RET                         

; blank one line of the character plane in both planes, step the wipe's
; cursor on to the next line, and count the lines still owed down by one;
; the zero test is left in the flags for the caller
blankNextLine:
01C2: 2A 89 A9        LD      HL,($A989)          ; {hard.workRam+189} fetch the wipe cursor -- where this line starts
01C5: 06 20           LD      B,$20               ; thirty-two cells across the line
01C7: 11 20 00        LD      DE,$0020            ; the step from one cell to the next

loc_01ca:
01CA: 36 F1           LD      (HL),$F1            ; lay a blank glyph in this cell
01CC: CB 94           RES     2,H                 ; cross to the colour plane for the same cell
01CE: 36 10           LD      (HL),$10            ; set its colour
01D0: CB D4           SET     2,H                 ; cross back to the glyph plane
01D2: 19              ADD     HL,DE               ; step to the next cell of the line
01D3: 10 F5           DJNZ    $01CA               ; {code.loc_01ca} on across all thirty-two cells
01D5: 2A 89 A9        LD      HL,($A989)          ; {hard.workRam+189} reload the wipe cursor
01D8: 23              INC     HL                  ; step it on to the start of the next line
01D9: 22 89 A9        LD      ($A989),HL          ; {hard.workRam+189} store the advanced cursor
01DC: 21 88 A9        LD      HL,$A988            
01DF: 35              DEC     (HL)                ; count the lines still owed down by one
01E0: C9              RET                         

; put the cell-stamping pen back at the start of its route -- leg index to
; zero and both coordinates to the route's first point, each written a
; word at a time so the whole-cell part and the fraction below it land
; together, and each lifted out of a fixed pair of program bytes rather
; than carried as a literal -- then fold a fixed 256-byte run of the image
; into one eight-bit total and, on anything but the total a genuine image
; gives, transfer into the cold start, which clears the work RAM the stack
; sits on and never comes back here. The arming is unconditional: the fold
; gates nothing above it
armThePenRouteThenColdStartOnATamperedImage:
01E1: AF              XOR     A                   
01E2: 32 E2 A9        LD      ($A9E2),A           ; {hard.workRam+1E2} send the pen back to leg zero of its route
01E5: 2A 45 0D        LD      HL,($0D45)          ; {hard.rom+D45} the route's first row coordinate, from the program image
01E8: 22 E3 A9        LD      ($A9E3),HL          ; {hard.workRam+1E3} seat the pen's row -- whole cell and fraction together
01EB: 2A 0C 28        LD      HL,($280C)          ; {hard.rom+280C} the route's first column coordinate
01EE: 22 E5 A9        LD      ($A9E5),HL          ; {hard.workRam+1E5} seat the pen's column the same way
01F1: 06 00           LD      B,$00               ; two hundred fifty-six bytes to fold
01F3: 21 33 0E        LD      HL,$0E33            ; point at the checked run of the program image
01F6: AF              XOR     A                   ; clear the running total

loc_01f7:
01F7: 86              ADD     A,(HL)              ; fold this byte into the total
01F8: 23              INC     HL                  
01F9: 10 FC           DJNZ    $01F7               ; {code.loc_01f7} on across all two hundred fifty-six bytes
01FB: D6 FD           SUB     $FD                 ; weigh the total against a genuine image's value
01FD: C4 69 00        CALL    NZ,$0069            ; {code.clearWorkRamAndSpriteBanksThenColdInit} on a tampered image, drop into the cold start, which never returns here
0200: C9              RET                         

; draw one interpolated run of pen-glyph cells from the current row/column
; toward a target pair (signed per-step increment (target-current)>>4),
; stamping each cell until the stamped video cell hits the run's end cell,
; then advance the run index, load the next run's endpoint from the word
; table at 0x0290, reseat the pen, and leave Z set when the new row
; integer is 0 (callers ret nz on it)
drawInterpolatedPenRun:
0201: CD 6F 02        CALL    $026F               ; {code.plotPenCell} stamp the pen glyph at the run's start cell
0204: 2A F5 32        LD      HL,($32F5)          ; {hard.rom+32F5} the run's target row, from the program image
0207: ED 4B E3 A9     LD      BC,($A9E3)          ; {hard.workRam+1E3} the pen's current row
020B: A7              AND     A                   
020C: ED 42           SBC     HL,BC               ; target row minus current row
020E: 29              ADD     HL,HL               
020F: 29              ADD     HL,HL               
0210: 29              ADD     HL,HL               
0211: 29              ADD     HL,HL               ; the difference times sixteen
0212: 3E 00           LD      A,$00               
0214: DE 00           SBC     A,$00               ; carry the difference's sign into the top byte
0216: 6C              LD      L,H                 
0217: 67              LD      H,A                 ; keep the top byte, sign-extended -- the per-step row increment
0218: 22 E7 A9        LD      ($A9E7),HL          ; {hard.workRam+1E7} store the row step
021B: 2A 45 0B        LD      HL,($0B45)          ; {hard.rom+B45} the run's target column
021E: ED 4B E5 A9     LD      BC,($A9E5)          ; {hard.workRam+1E5} the pen's current column
0222: A7              AND     A                   
0223: ED 42           SBC     HL,BC               ; target column minus current column
0225: 29              ADD     HL,HL               
0226: 29              ADD     HL,HL               
0227: 29              ADD     HL,HL               
0228: 29              ADD     HL,HL               ; the difference times sixteen
0229: 3E 00           LD      A,$00               
022B: DE 00           SBC     A,$00               ; carry the difference's sign into the top byte
022D: 6C              LD      L,H                 
022E: 67              LD      H,A                 ; keep the top byte, sign-extended -- the per-step column increment
022F: 22 E9 A9        LD      ($A9E9),HL          ; {hard.workRam+1E9} store the column step

loc_0232:
0232: 2A E3 A9        LD      HL,($A9E3)          ; {hard.workRam+1E3} take the pen's current row
0235: ED 4B E7 A9     LD      BC,($A9E7)          ; {hard.workRam+1E7} the row step
0239: 09              ADD     HL,BC               ; advance the row by one step
023A: 22 E3 A9        LD      ($A9E3),HL          ; {hard.workRam+1E3} store it back
023D: 2A E5 A9        LD      HL,($A9E5)          ; {hard.workRam+1E5} take the pen's current column
0240: ED 4B E9 A9     LD      BC,($A9E9)          ; {hard.workRam+1E9} the column step
0244: 09              ADD     HL,BC               ; advance the column by one step
0245: 22 E5 A9        LD      ($A9E5),HL          ; {hard.workRam+1E5} store it back
0248: CD 6F 02        CALL    $026F               ; {code.plotPenCell} stamp the pen glyph at the new cell
024B: ED 5B B2 14     LD      DE,($14B2)          ; {hard.rom+14B2} the run's end cell, from the program image
024F: A7              AND     A                   
0250: ED 52           SBC     HL,DE               ; has the stamped cell reached the run's end?
0252: C2 32 02        JP      NZ,$0232            ; {code.loc_0232} not yet -- step and stamp again
0255: 21 E2 A9        LD      HL,$A9E2            
0258: 34              INC     (HL)                ; advance to the next run of the route
0259: 7E              LD      A,(HL)              ; take the new run index
025A: 21 90 02        LD      HL,$0290            ; point at the route's endpoint word table
025D: D7              RST     $10                 ; read the new run's endpoint
025E: 21 E3 A9        LD      HL,$A9E3            
0261: 36 00           LD      (HL),$00            ; clear the row's fraction
0263: 23              INC     HL                  
0264: 73              LD      (HL),E              ; seat the row's whole cell from the endpoint
0265: 21 E5 A9        LD      HL,$A9E5            
0268: 36 00           LD      (HL),$00            ; clear the column's fraction
026A: 23              INC     HL                  
026B: 72              LD      (HL),D              ; seat the column's whole cell from the endpoint
026C: 7B              LD      A,E                 
026D: A7              AND     A                   ; test the new run's row cell -- callers keep drawing runs until it reaches zero
026E: C9              RET                         

; stamp the current pen glyph and pen colour into the one character cell a
; row cell and a column cell name, and hand back the video-plane address
; of that cell
plotPenCell:
026F: 3A E4 A9        LD      A,($A9E4)           ; {hard.workRam+1E4} read the pen's row cell
0272: 87              ADD     A,A                 ; scale the row up toward its offset down the plane -- a byte-wide doubling, so a row past the thirty-second folds back to the top
0273: 87              ADD     A,A                 
0274: 87              ADD     A,A                 
0275: 6F              LD      L,A                 
0276: 26 00           LD      H,$00               
0278: 29              ADD     HL,HL               ; finish scaling the row to thirty-two cells, one whole plane row
0279: 29              ADD     HL,HL               
027A: 3A E6 A9        LD      A,($A9E6)           ; {hard.workRam+1E6} read the pen's column cell
027D: 85              ADD     A,L                 
027E: 6F              LD      L,A                 ; fold the column into the low half of the address, so a column past the row's end wraps within the row
027F: 3E A4           LD      A,$A4               
0281: 84              ADD     A,H                 
0282: 67              LD      H,A                 ; land the address in the character plane
0283: 3A 0B AD        LD      A,($AD0B)           ; {hard.workRam+50B} read the pen glyph
0286: 77              LD      (HL),A              ; stamp the glyph into the cell
0287: CB 94           RES     2,H                 ; cross to the colour plane for the same cell
0289: 3A 0C AD        LD      A,($AD0C)           ; {hard.workRam+50C} read the pen colour
028C: 77              LD      (HL),A              ; paint the cell that colour
028D: CB D4           SET     2,H                 ; cross back to the glyph cell -- the address handed back to the caller
028F: C9              RET                         

; ---- $0290-$0364: data ----
0290: 10 04 11 04 12 04 13 04 14 04 15 04 16 04 17 04
02A0: 18 04 19 04 1A 04 1B 04 1C 04 1D 04 1D 05 1D 06
02B0: 1D 07 1D 08 1D 09 1D 0A 1D 0B 1D 0C 1D 0D 1D 0E
02C0: 1D 0F 1D 10 1D 11 1D 12 1D 13 1D 14 1D 15 1D 16
02D0: 1D 17 1D 18 1D 19 1D 1A 1D 1B 1D 1C 1D 1D 1D 1E
02E0: 1C 1E 1B 1E 1A 1E 19 1E 18 1E 17 1E 16 1E 15 1E
02F0: 14 1E 13 1E 12 1E 11 1E 10 1E 0F 1E 0E 1E 0D 1E
0300: 0C 1E 0B 1E 0A 1E 09 1E 08 1E 07 1E 06 1E 05 1E
0310: 04 1E 03 1E 02 1E 02 1D 02 1C 02 1B 02 1A 02 19
0320: 02 18 02 17 02 16 02 15 02 14 02 13 02 12 02 11
0330: 02 10 02 0F 02 0E 02 0D 02 0C 02 0B 02 0A 02 09
0340: 02 08 02 07 02 06 02 05 02 04 03 04 04 04 05 04
0350: 06 04 07 04 08 04 09 04 0A 04 0B 04 0C 04 0D 04
0360: 0E 04 0F 04 00

; gather the sprite shadow into the two hardware banks, three runs per
; bank in an order that is not their order in memory, transforming each
; byte by which half of its sprite it is and which way round the cabinet
; has the picture; then, inside one window of the sequence, ask for the
; eight scenery slots to be shown a second time half a screen away
publishSpriteShadow:
0365: 21 30 AA        LD      HL,$AA30            ; point at the sprite shadow, the working copy of the sprites
0368: 11 10 B0        LD      DE,$B010            ; point at the first hardware sprite bank
036B: 3A 87 A9        LD      A,($A987)           ; {hard.workRam+187} read the cabinet-orientation flag
036E: A7              AND     A                   
036F: CA 56 05        JP      Z,$0556             ; {code.loc_0556} picture turned round: take the flipped copy path
0372: ED A0           LDI                         ; copy the six scenery-slot-zero sprite bytes straight into the bank
0374: ED A0           LDI                         
0376: ED A0           LDI                         
0378: ED A0           LDI                         
037A: ED A0           LDI                         
037C: ED A0           LDI                         
037E: 21 10 AA        LD      HL,$AA10            ; point at the player's thirty-two sprite bytes
0381: ED A0           LDI                         ; copy them straight in
0383: ED A0           LDI                         
0385: ED A0           LDI                         
0387: ED A0           LDI                         
0389: ED A0           LDI                         
038B: ED A0           LDI                         
038D: ED A0           LDI                         
038F: ED A0           LDI                         
0391: ED A0           LDI                         
0393: ED A0           LDI                         
0395: ED A0           LDI                         
0397: ED A0           LDI                         
0399: ED A0           LDI                         
039B: ED A0           LDI                         
039D: ED A0           LDI                         
039F: ED A0           LDI                         
03A1: ED A0           LDI                         
03A3: ED A0           LDI                         
03A5: ED A0           LDI                         
03A7: ED A0           LDI                         
03A9: ED A0           LDI                         
03AB: ED A0           LDI                         
03AD: ED A0           LDI                         
03AF: ED A0           LDI                         
03B1: ED A0           LDI                         
03B3: ED A0           LDI                         
03B5: ED A0           LDI                         
03B7: ED A0           LDI                         
03B9: ED A0           LDI                         
03BB: ED A0           LDI                         
03BD: ED A0           LDI                         
03BF: ED A0           LDI                         
03C1: 21 36 AA        LD      HL,$AA36            ; point at scenery slot three's ten sprite bytes
03C4: ED A0           LDI                         ; copy them straight in
03C6: ED A0           LDI                         
03C8: ED A0           LDI                         
03CA: ED A0           LDI                         
03CC: ED A0           LDI                         
03CE: ED A0           LDI                         
03D0: ED A0           LDI                         
03D2: ED A0           LDI                         
03D4: ED A0           LDI                         
03D6: ED A0           LDI                         
03D8: 21 60 AA        LD      HL,$AA60            ; point at the sprite-attribute shadow
03DB: 11 10 B4        LD      DE,$B410            ; point at the second hardware sprite bank
03DE: ED A0           LDI                         ; pass this sprite's first attribute byte through unchanged
03E0: 7E              LD      A,(HL)              ; read its second attribute byte
03E1: C6 0E           ADD     A,$0E               ; bias it by fourteen
03E3: 2F              CPL                         ; complement it -- the upright transform for the second attribute half
03E4: 12              LD      (DE),A              ; store it -- the run carries on this way, one attribute pair at a time
03E5: 2C              INC     L                   
03E6: 1C              INC     E                   
03E7: ED A0           LDI                         
03E9: 7E              LD      A,(HL)              
03EA: C6 0E           ADD     A,$0E               
03EC: 2F              CPL                         
03ED: 12              LD      (DE),A              
03EE: 2C              INC     L                   
03EF: 1C              INC     E                   
03F0: ED A0           LDI                         
03F2: 7E              LD      A,(HL)              
03F3: C6 0E           ADD     A,$0E               
03F5: 2F              CPL                         
03F6: 12              LD      (DE),A              
03F7: 2C              INC     L                   
03F8: 1C              INC     E                   
03F9: 21 40 AA        LD      HL,$AA40            ; move the source on to the player's attribute block
03FC: ED A0           LDI                         
03FE: 7E              LD      A,(HL)              
03FF: C6 0E           ADD     A,$0E               
0401: 2F              CPL                         
0402: 12              LD      (DE),A              
0403: 2C              INC     L                   
0404: 1C              INC     E                   
0405: ED A0           LDI                         
0407: 7E              LD      A,(HL)              
0408: C6 0E           ADD     A,$0E               
040A: 2F              CPL                         
040B: 12              LD      (DE),A              
040C: 2C              INC     L                   
040D: 1C              INC     E                   
040E: ED A0           LDI                         
0410: 7E              LD      A,(HL)              
0411: C6 0E           ADD     A,$0E               
0413: 2F              CPL                         
0414: 12              LD      (DE),A              
0415: 2C              INC     L                   
0416: 1C              INC     E                   
0417: ED A0           LDI                         
0419: 7E              LD      A,(HL)              
041A: C6 0E           ADD     A,$0E               
041C: 2F              CPL                         
041D: 12              LD      (DE),A              
041E: 2C              INC     L                   
041F: 1C              INC     E                   
0420: ED A0           LDI                         
0422: 7E              LD      A,(HL)              
0423: C6 0E           ADD     A,$0E               
0425: 2F              CPL                         
0426: 12              LD      (DE),A              
0427: 2C              INC     L                   
0428: 1C              INC     E                   
0429: ED A0           LDI                         
042B: 7E              LD      A,(HL)              
042C: C6 0E           ADD     A,$0E               
042E: 2F              CPL                         
042F: 12              LD      (DE),A              
0430: 2C              INC     L                   
0431: 1C              INC     E                   
0432: ED A0           LDI                         
0434: 7E              LD      A,(HL)              
0435: C6 0E           ADD     A,$0E               
0437: 2F              CPL                         
0438: 12              LD      (DE),A              
0439: 2C              INC     L                   
043A: 1C              INC     E                   
043B: ED A0           LDI                         
043D: 7E              LD      A,(HL)              
043E: C6 0E           ADD     A,$0E               
0440: 2F              CPL                         
0441: 12              LD      (DE),A              
0442: 2C              INC     L                   
0443: 1C              INC     E                   
0444: ED A0           LDI                         
0446: 7E              LD      A,(HL)              
0447: C6 0E           ADD     A,$0E               
0449: 2F              CPL                         
044A: 12              LD      (DE),A              
044B: 2C              INC     L                   
044C: 1C              INC     E                   
044D: ED A0           LDI                         
044F: 7E              LD      A,(HL)              
0450: C6 0E           ADD     A,$0E               
0452: 2F              CPL                         
0453: 12              LD      (DE),A              
0454: 2C              INC     L                   
0455: 1C              INC     E                   
0456: ED A0           LDI                         
0458: 7E              LD      A,(HL)              
0459: C6 0E           ADD     A,$0E               
045B: 2F              CPL                         
045C: 12              LD      (DE),A              
045D: 2C              INC     L                   
045E: 1C              INC     E                   
045F: ED A0           LDI                         
0461: 7E              LD      A,(HL)              
0462: C6 0E           ADD     A,$0E               
0464: 2F              CPL                         
0465: 12              LD      (DE),A              
0466: 2C              INC     L                   
0467: 1C              INC     E                   
0468: ED A0           LDI                         
046A: 7E              LD      A,(HL)              
046B: C6 0E           ADD     A,$0E               
046D: 2F              CPL                         
046E: 12              LD      (DE),A              
046F: 2C              INC     L                   
0470: 1C              INC     E                   
0471: ED A0           LDI                         
0473: 7E              LD      A,(HL)              
0474: C6 0E           ADD     A,$0E               
0476: 2F              CPL                         
0477: 12              LD      (DE),A              
0478: 2C              INC     L                   
0479: 1C              INC     E                   
047A: ED A0           LDI                         
047C: 7E              LD      A,(HL)              
047D: C6 0E           ADD     A,$0E               
047F: 2F              CPL                         
0480: 12              LD      (DE),A              
0481: 2C              INC     L                   
0482: 1C              INC     E                   
0483: ED A0           LDI                         
0485: 7E              LD      A,(HL)              
0486: C6 0E           ADD     A,$0E               
0488: 2F              CPL                         
0489: 12              LD      (DE),A              
048A: 2C              INC     L                   
048B: 1C              INC     E                   
048C: 21 66 AA        LD      HL,$AA66            ; move the source on to scenery slot three's attributes
048F: ED A0           LDI                         
0491: 7E              LD      A,(HL)              
0492: C6 0E           ADD     A,$0E               
0494: 2F              CPL                         
0495: 12              LD      (DE),A              
0496: 2C              INC     L                   
0497: 1C              INC     E                   
0498: ED A0           LDI                         
049A: 7E              LD      A,(HL)              
049B: C6 0E           ADD     A,$0E               
049D: 2F              CPL                         
049E: 12              LD      (DE),A              
049F: 2C              INC     L                   
04A0: 1C              INC     E                   
04A1: ED A0           LDI                         
04A3: 7E              LD      A,(HL)              
04A4: C6 0E           ADD     A,$0E               
04A6: 2F              CPL                         
04A7: 12              LD      (DE),A              
04A8: 2C              INC     L                   
04A9: 1C              INC     E                   
04AA: ED A0           LDI                         
04AC: 7E              LD      A,(HL)              
04AD: C6 0E           ADD     A,$0E               
04AF: 2F              CPL                         
04B0: 12              LD      (DE),A              
04B1: 2C              INC     L                   
04B2: 1C              INC     E                   
04B3: ED A0           LDI                         
04B5: 7E              LD      A,(HL)              
04B6: C6 0E           ADD     A,$0E               
04B8: 2F              CPL                         
04B9: 12              LD      (DE),A              
04BA: 2C              INC     L                   
04BB: 1C              INC     E                   

loc_04bc:
04BC: 3A AB A9        LD      A,($A9AB)           ; {hard.workRam+1AB} read the sequence phase
04BF: FE 03           CP      $03                 ; is this the third sequence phase?
04C1: C0              RET     NZ                  ; other phase: leave the sprites untouched
04C2: 3A AC A9        LD      A,($A9AC)           ; {hard.workRam+1AC} read the sequence sub-step
04C5: 21 32 08        LD      HL,$0832            ; point at the sub-step floor value
04C8: BE              CP      (HL)                ; below the floor sub-step?
04C9: D8              RET     C                   ; yes: nothing to raise
04CA: FE 08           CP      $08                 ; at or past sub-step eight?
04CC: D0              RET     NC                  ; yes: nothing to raise
04CD: 3A 11 B4        LD      A,($B411)           ; read this sprite's second bank byte
04D0: C6 80           ADD     A,$80               ; add its own top bit back to probe it
04D2: 38 0A           JR      C,$04DE             ; {code.loc_04de} already raised: skip to the next sprite
04D4: 32 11 B4        LD      ($B411),A           ; raise the second byte's top bit
04D7: 21 10 B0        LD      HL,$B010            ; point at the matching first-bank byte
04DA: 7E              LD      A,(HL)              
04DB: C6 80           ADD     A,$80               ; raise its top bit too
04DD: 77              LD      (HL),A              

loc_04de:
04DE: 3A 13 B4        LD      A,($B413)           ; same top-bit raise for the next of the eight sprites
04E1: C6 80           ADD     A,$80               
04E3: 38 0A           JR      C,$04EF             ; {code.loc_04ef}
04E5: 32 13 B4        LD      ($B413),A           
04E8: 21 12 B0        LD      HL,$B012            
04EB: 7E              LD      A,(HL)              
04EC: C6 80           ADD     A,$80               
04EE: 77              LD      (HL),A              

loc_04ef:
04EF: 3A 15 B4        LD      A,($B415)           ; same raise for the next sprite
04F2: C6 80           ADD     A,$80               
04F4: 38 0A           JR      C,$0500             ; {code.loc_0500}
04F6: 32 15 B4        LD      ($B415),A           
04F9: 21 14 B0        LD      HL,$B014            
04FC: 7E              LD      A,(HL)              
04FD: C6 80           ADD     A,$80               
04FF: 77              LD      (HL),A              

loc_0500:
0500: 3A 37 B4        LD      A,($B437)           ; same raise for the next sprite
0503: C6 80           ADD     A,$80               
0505: 38 0A           JR      C,$0511             ; {code.loc_0511}
0507: 32 37 B4        LD      ($B437),A           
050A: 21 36 B0        LD      HL,$B036            
050D: 7E              LD      A,(HL)              
050E: C6 80           ADD     A,$80               
0510: 77              LD      (HL),A              

loc_0511:
0511: 3A 39 B4        LD      A,($B439)           ; same raise for the next sprite
0514: C6 80           ADD     A,$80               
0516: 38 0A           JR      C,$0522             ; {code.loc_0522}
0518: 32 39 B4        LD      ($B439),A           
051B: 21 38 B0        LD      HL,$B038            
051E: 7E              LD      A,(HL)              
051F: C6 80           ADD     A,$80               
0521: 77              LD      (HL),A              

loc_0522:
0522: 3A 3B B4        LD      A,($B43B)           ; same raise for the next sprite
0525: C6 80           ADD     A,$80               
0527: 38 0A           JR      C,$0533             ; {code.loc_0533}
0529: 32 3B B4        LD      ($B43B),A           
052C: 21 3A B0        LD      HL,$B03A            
052F: 7E              LD      A,(HL)              
0530: C6 80           ADD     A,$80               
0532: 77              LD      (HL),A              

loc_0533:
0533: 3A 3D B4        LD      A,($B43D)           ; same raise for the next sprite
0536: C6 80           ADD     A,$80               
0538: 38 0A           JR      C,$0544             ; {code.loc_0544}
053A: 32 3D B4        LD      ($B43D),A           
053D: 21 3C B0        LD      HL,$B03C            
0540: 7E              LD      A,(HL)              
0541: C6 80           ADD     A,$80               
0543: 77              LD      (HL),A              

loc_0544:
0544: 3A 3F B4        LD      A,($B43F)           ; same raise for the last of the eight sprites
0547: C6 80           ADD     A,$80               
0549: 38 0A           JR      C,$0555             ; {code.loc_0555}
054B: 32 3F B4        LD      ($B43F),A           
054E: 21 3E B0        LD      HL,$B03E            
0551: 7E              LD      A,(HL)              
0552: C6 80           ADD     A,$80               
0554: 77              LD      (HL),A              

loc_0555:
0555: C9              RET                         ; done: return

loc_0556:
0556: 7E              LD      A,(HL)              ; read this sprite's first byte
0557: C6 0F           ADD     A,$0F               ; bias it by fifteen
0559: 2F              CPL                         ; complement it -- the flipped transform for the first half
055A: 12              LD      (DE),A              ; store it
055B: 2C              INC     L                   
055C: 1C              INC     E                   
055D: ED A0           LDI                         ; pass the second byte through unchanged
055F: 7E              LD      A,(HL)              
0560: C6 0F           ADD     A,$0F               
0562: 2F              CPL                         
0563: 12              LD      (DE),A              
0564: 2C              INC     L                   
0565: 1C              INC     E                   
0566: ED A0           LDI                         
0568: 7E              LD      A,(HL)              
0569: C6 0F           ADD     A,$0F               
056B: 2F              CPL                         
056C: 12              LD      (DE),A              
056D: 2C              INC     L                   
056E: 1C              INC     E                   
056F: ED A0           LDI                         
0571: 21 10 AA        LD      HL,$AA10            ; move the source on to the player's thirty-two sprite bytes
0574: 7E              LD      A,(HL)              
0575: C6 0F           ADD     A,$0F               
0577: 2F              CPL                         
0578: 12              LD      (DE),A              
0579: 2C              INC     L                   
057A: 1C              INC     E                   
057B: ED A0           LDI                         
057D: 7E              LD      A,(HL)              
057E: C6 0F           ADD     A,$0F               
0580: 2F              CPL                         
0581: 12              LD      (DE),A              
0582: 2C              INC     L                   
0583: 1C              INC     E                   
0584: ED A0           LDI                         
0586: 7E              LD      A,(HL)              
0587: C6 0F           ADD     A,$0F               
0589: 2F              CPL                         
058A: 12              LD      (DE),A              
058B: 2C              INC     L                   
058C: 1C              INC     E                   
058D: ED A0           LDI                         
058F: 7E              LD      A,(HL)              
0590: C6 0F           ADD     A,$0F               
0592: 2F              CPL                         
0593: 12              LD      (DE),A              
0594: 2C              INC     L                   
0595: 1C              INC     E                   
0596: ED A0           LDI                         
0598: 7E              LD      A,(HL)              
0599: C6 0F           ADD     A,$0F               
059B: 2F              CPL                         
059C: 12              LD      (DE),A              
059D: 2C              INC     L                   
059E: 1C              INC     E                   
059F: ED A0           LDI                         
05A1: 7E              LD      A,(HL)              
05A2: C6 0F           ADD     A,$0F               
05A4: 2F              CPL                         
05A5: 12              LD      (DE),A              
05A6: 2C              INC     L                   
05A7: 1C              INC     E                   
05A8: ED A0           LDI                         
05AA: 7E              LD      A,(HL)              
05AB: C6 0F           ADD     A,$0F               
05AD: 2F              CPL                         
05AE: 12              LD      (DE),A              
05AF: 2C              INC     L                   
05B0: 1C              INC     E                   
05B1: ED A0           LDI                         
05B3: 7E              LD      A,(HL)              
05B4: C6 0F           ADD     A,$0F               
05B6: 2F              CPL                         
05B7: 12              LD      (DE),A              
05B8: 2C              INC     L                   
05B9: 1C              INC     E                   
05BA: ED A0           LDI                         
05BC: 7E              LD      A,(HL)              
05BD: C6 0F           ADD     A,$0F               
05BF: 2F              CPL                         
05C0: 12              LD      (DE),A              
05C1: 2C              INC     L                   
05C2: 1C              INC     E                   
05C3: ED A0           LDI                         
05C5: 7E              LD      A,(HL)              
05C6: C6 0F           ADD     A,$0F               
05C8: 2F              CPL                         
05C9: 12              LD      (DE),A              
05CA: 2C              INC     L                   
05CB: 1C              INC     E                   
05CC: ED A0           LDI                         
05CE: 7E              LD      A,(HL)              
05CF: C6 0F           ADD     A,$0F               
05D1: 2F              CPL                         
05D2: 12              LD      (DE),A              
05D3: 2C              INC     L                   
05D4: 1C              INC     E                   
05D5: ED A0           LDI                         
05D7: 7E              LD      A,(HL)              
05D8: C6 0F           ADD     A,$0F               
05DA: 2F              CPL                         
05DB: 12              LD      (DE),A              
05DC: 2C              INC     L                   
05DD: 1C              INC     E                   
05DE: ED A0           LDI                         
05E0: 7E              LD      A,(HL)              
05E1: C6 0F           ADD     A,$0F               
05E3: 2F              CPL                         
05E4: 12              LD      (DE),A              
05E5: 2C              INC     L                   
05E6: 1C              INC     E                   
05E7: ED A0           LDI                         
05E9: 7E              LD      A,(HL)              
05EA: C6 0F           ADD     A,$0F               
05EC: 2F              CPL                         
05ED: 12              LD      (DE),A              
05EE: 2C              INC     L                   
05EF: 1C              INC     E                   
05F0: ED A0           LDI                         
05F2: 7E              LD      A,(HL)              
05F3: C6 0F           ADD     A,$0F               
05F5: 2F              CPL                         
05F6: 12              LD      (DE),A              
05F7: 2C              INC     L                   
05F8: 1C              INC     E                   
05F9: ED A0           LDI                         
05FB: 7E              LD      A,(HL)              
05FC: C6 0F           ADD     A,$0F               
05FE: 2F              CPL                         
05FF: 12              LD      (DE),A              
0600: 2C              INC     L                   
0601: 1C              INC     E                   
0602: ED A0           LDI                         
0604: 21 36 AA        LD      HL,$AA36            ; move the source on to scenery slot three's ten bytes
0607: 7E              LD      A,(HL)              
0608: C6 0F           ADD     A,$0F               
060A: 2F              CPL                         
060B: 12              LD      (DE),A              
060C: 2C              INC     L                   
060D: 1C              INC     E                   
060E: ED A0           LDI                         
0610: 7E              LD      A,(HL)              
0611: C6 0F           ADD     A,$0F               
0613: 2F              CPL                         
0614: 12              LD      (DE),A              
0615: 2C              INC     L                   
0616: 1C              INC     E                   
0617: ED A0           LDI                         
0619: 7E              LD      A,(HL)              
061A: C6 0F           ADD     A,$0F               
061C: 2F              CPL                         
061D: 12              LD      (DE),A              
061E: 2C              INC     L                   
061F: 1C              INC     E                   
0620: ED A0           LDI                         
0622: 7E              LD      A,(HL)              
0623: C6 0F           ADD     A,$0F               
0625: 2F              CPL                         
0626: 12              LD      (DE),A              
0627: 2C              INC     L                   
0628: 1C              INC     E                   
0629: ED A0           LDI                         
062B: 7E              LD      A,(HL)              
062C: C6 0F           ADD     A,$0F               
062E: 2F              CPL                         
062F: 12              LD      (DE),A              
0630: 2C              INC     L                   
0631: 1C              INC     E                   
0632: ED A0           LDI                         
0634: 21 60 AA        LD      HL,$AA60            ; point at the sprite-attribute shadow
0637: 11 10 B4        LD      DE,$B410            ; point at the second hardware sprite bank
063A: 7E              LD      A,(HL)              ; read this attribute's first byte
063B: EE C0           XOR     $C0                 ; toggle its top two bits -- the flipped transform for the first attribute half
063D: 12              LD      (DE),A              ; store it
063E: 2C              INC     L                   
063F: 1C              INC     E                   
0640: 7E              LD      A,(HL)              ; read its second byte
0641: 3C              INC     A                   ; step it on by one -- the flipped transform for the second attribute half
0642: 12              LD      (DE),A              ; store it -- the run carries on this way, one attribute pair at a time
0643: 2C              INC     L                   
0644: 1C              INC     E                   
0645: 7E              LD      A,(HL)              
0646: EE C0           XOR     $C0                 
0648: 12              LD      (DE),A              
0649: 2C              INC     L                   
064A: 1C              INC     E                   
064B: 7E              LD      A,(HL)              
064C: 3C              INC     A                   
064D: 12              LD      (DE),A              
064E: 2C              INC     L                   
064F: 1C              INC     E                   
0650: 7E              LD      A,(HL)              
0651: EE C0           XOR     $C0                 
0653: 12              LD      (DE),A              
0654: 2C              INC     L                   
0655: 1C              INC     E                   
0656: 7E              LD      A,(HL)              
0657: 3C              INC     A                   
0658: 12              LD      (DE),A              
0659: 2C              INC     L                   
065A: 1C              INC     E                   
065B: 21 40 AA        LD      HL,$AA40            ; move the source on to the player's attribute block
065E: 7E              LD      A,(HL)              
065F: EE C0           XOR     $C0                 
0661: 12              LD      (DE),A              
0662: 2C              INC     L                   
0663: 1C              INC     E                   
0664: 7E              LD      A,(HL)              
0665: 3C              INC     A                   
0666: 12              LD      (DE),A              
0667: 2C              INC     L                   
0668: 1C              INC     E                   
0669: 7E              LD      A,(HL)              
066A: EE C0           XOR     $C0                 
066C: 12              LD      (DE),A              
066D: 2C              INC     L                   
066E: 1C              INC     E                   
066F: 7E              LD      A,(HL)              
0670: 3C              INC     A                   
0671: 12              LD      (DE),A              
0672: 2C              INC     L                   
0673: 1C              INC     E                   
0674: 7E              LD      A,(HL)              
0675: EE C0           XOR     $C0                 
0677: 12              LD      (DE),A              
0678: 2C              INC     L                   
0679: 1C              INC     E                   
067A: 7E              LD      A,(HL)              
067B: 3C              INC     A                   
067C: 12              LD      (DE),A              
067D: 2C              INC     L                   
067E: 1C              INC     E                   
067F: 7E              LD      A,(HL)              
0680: EE C0           XOR     $C0                 
0682: 12              LD      (DE),A              
0683: 2C              INC     L                   
0684: 1C              INC     E                   
0685: 7E              LD      A,(HL)              
0686: 3C              INC     A                   
0687: 12              LD      (DE),A              
0688: 2C              INC     L                   
0689: 1C              INC     E                   
068A: 7E              LD      A,(HL)              
068B: EE C0           XOR     $C0                 
068D: 12              LD      (DE),A              
068E: 2C              INC     L                   
068F: 1C              INC     E                   
0690: 7E              LD      A,(HL)              
0691: 3C              INC     A                   
0692: 12              LD      (DE),A              
0693: 2C              INC     L                   
0694: 1C              INC     E                   
0695: 7E              LD      A,(HL)              
0696: EE C0           XOR     $C0                 
0698: 12              LD      (DE),A              
0699: 2C              INC     L                   
069A: 1C              INC     E                   
069B: 7E              LD      A,(HL)              
069C: 3C              INC     A                   
069D: 12              LD      (DE),A              
069E: 2C              INC     L                   
069F: 1C              INC     E                   
06A0: 7E              LD      A,(HL)              
06A1: EE C0           XOR     $C0                 
06A3: 12              LD      (DE),A              
06A4: 2C              INC     L                   
06A5: 1C              INC     E                   
06A6: 7E              LD      A,(HL)              
06A7: 3C              INC     A                   
06A8: 12              LD      (DE),A              
06A9: 2C              INC     L                   
06AA: 1C              INC     E                   
06AB: 7E              LD      A,(HL)              
06AC: EE C0           XOR     $C0                 
06AE: 12              LD      (DE),A              
06AF: 2C              INC     L                   
06B0: 1C              INC     E                   
06B1: 7E              LD      A,(HL)              
06B2: 3C              INC     A                   
06B3: 12              LD      (DE),A              
06B4: 2C              INC     L                   
06B5: 1C              INC     E                   
06B6: 7E              LD      A,(HL)              
06B7: EE C0           XOR     $C0                 
06B9: 12              LD      (DE),A              
06BA: 2C              INC     L                   
06BB: 1C              INC     E                   
06BC: 7E              LD      A,(HL)              
06BD: 3C              INC     A                   
06BE: 12              LD      (DE),A              
06BF: 2C              INC     L                   
06C0: 1C              INC     E                   
06C1: 7E              LD      A,(HL)              
06C2: EE C0           XOR     $C0                 
06C4: 12              LD      (DE),A              
06C5: 2C              INC     L                   
06C6: 1C              INC     E                   
06C7: 7E              LD      A,(HL)              
06C8: 3C              INC     A                   
06C9: 12              LD      (DE),A              
06CA: 2C              INC     L                   
06CB: 1C              INC     E                   
06CC: 7E              LD      A,(HL)              
06CD: EE C0           XOR     $C0                 
06CF: 12              LD      (DE),A              
06D0: 2C              INC     L                   
06D1: 1C              INC     E                   
06D2: 7E              LD      A,(HL)              
06D3: 3C              INC     A                   
06D4: 12              LD      (DE),A              
06D5: 2C              INC     L                   
06D6: 1C              INC     E                   
06D7: 7E              LD      A,(HL)              
06D8: EE C0           XOR     $C0                 
06DA: 12              LD      (DE),A              
06DB: 2C              INC     L                   
06DC: 1C              INC     E                   
06DD: 7E              LD      A,(HL)              
06DE: 3C              INC     A                   
06DF: 12              LD      (DE),A              
06E0: 2C              INC     L                   
06E1: 1C              INC     E                   
06E2: 7E              LD      A,(HL)              
06E3: EE C0           XOR     $C0                 
06E5: 12              LD      (DE),A              
06E6: 2C              INC     L                   
06E7: 1C              INC     E                   
06E8: 7E              LD      A,(HL)              
06E9: 3C              INC     A                   
06EA: 12              LD      (DE),A              
06EB: 2C              INC     L                   
06EC: 1C              INC     E                   
06ED: 7E              LD      A,(HL)              
06EE: EE C0           XOR     $C0                 
06F0: 12              LD      (DE),A              
06F1: 2C              INC     L                   
06F2: 1C              INC     E                   
06F3: 7E              LD      A,(HL)              
06F4: 3C              INC     A                   
06F5: 12              LD      (DE),A              
06F6: 2C              INC     L                   
06F7: 1C              INC     E                   
06F8: 7E              LD      A,(HL)              
06F9: EE C0           XOR     $C0                 
06FB: 12              LD      (DE),A              
06FC: 2C              INC     L                   
06FD: 1C              INC     E                   
06FE: 7E              LD      A,(HL)              
06FF: 3C              INC     A                   
0700: 12              LD      (DE),A              
0701: 2C              INC     L                   
0702: 1C              INC     E                   
0703: 7E              LD      A,(HL)              
0704: EE C0           XOR     $C0                 
0706: 12              LD      (DE),A              
0707: 2C              INC     L                   
0708: 1C              INC     E                   
0709: 7E              LD      A,(HL)              
070A: 3C              INC     A                   
070B: 12              LD      (DE),A              
070C: 2C              INC     L                   
070D: 1C              INC     E                   
070E: 21 66 AA        LD      HL,$AA66            ; move the source on to scenery slot three's attributes
0711: 7E              LD      A,(HL)              
0712: EE C0           XOR     $C0                 
0714: 12              LD      (DE),A              
0715: 2C              INC     L                   
0716: 1C              INC     E                   
0717: 7E              LD      A,(HL)              
0718: 3C              INC     A                   
0719: 12              LD      (DE),A              
071A: 2C              INC     L                   
071B: 1C              INC     E                   
071C: 7E              LD      A,(HL)              
071D: EE C0           XOR     $C0                 
071F: 12              LD      (DE),A              
0720: 2C              INC     L                   
0721: 1C              INC     E                   
0722: 7E              LD      A,(HL)              
0723: 3C              INC     A                   
0724: 12              LD      (DE),A              
0725: 2C              INC     L                   
0726: 1C              INC     E                   
0727: 7E              LD      A,(HL)              
0728: EE C0           XOR     $C0                 
072A: 12              LD      (DE),A              
072B: 2C              INC     L                   
072C: 1C              INC     E                   
072D: 7E              LD      A,(HL)              
072E: 3C              INC     A                   
072F: 12              LD      (DE),A              
0730: 2C              INC     L                   
0731: 1C              INC     E                   
0732: 7E              LD      A,(HL)              
0733: EE C0           XOR     $C0                 
0735: 12              LD      (DE),A              
0736: 2C              INC     L                   
0737: 1C              INC     E                   
0738: 7E              LD      A,(HL)              
0739: 3C              INC     A                   
073A: 12              LD      (DE),A              
073B: 2C              INC     L                   
073C: 1C              INC     E                   
073D: 7E              LD      A,(HL)              
073E: EE C0           XOR     $C0                 
0740: 12              LD      (DE),A              
0741: 2C              INC     L                   
0742: 1C              INC     E                   
0743: 7E              LD      A,(HL)              
0744: 3C              INC     A                   
0745: 12              LD      (DE),A              
0746: 2C              INC     L                   
0747: 1C              INC     E                   
0748: C3 BC 04        JP      $04BC               ; {code.loc_04bc} go raise the eight sprites, then return

; attract-sequence arm (phase 1, sub-step 0, reached by rst-30 computed
; dispatch from dispatchSequencePhase1SubStepArm): fold the fixed 256-byte
; run at 0x4AA0 into an eight-bit total and derail into the checksum-
; failure landing 0x08FA on any total but 0xB8; otherwise set the pen
; colour 0xAD0C to 5 and the stamp glyph 0xAD0B to the blanking glyph 0xF1
; (so the pen erases), re-arm the pen route via 0x01E1, then step the
; sequence sub-step 0x0F1A -- twice when the pen colour already held 5
erasePenRouteThenAdvanceStep:
074B: 06 00           LD      B,$00               ; two hundred fifty-six program bytes to fold -- a zero count means the full round
074D: 21 A0 4A        LD      HL,$4AA0            ; point at the program run to be checksummed
0750: AF              XOR     A                   ; clear the running total

loc_0751:
0751: 86              ADD     A,(HL)              ; add the next program byte into the total
0752: 23              INC     HL                  
0753: 10 FC           DJNZ    $0751               ; {code.loc_0751}
0755: D6 B8           SUB     $B8                 ; subtract the genuine total
0757: C2 FA 08        JP      NZ,$08FA            ; {code.loc_08fa} any other total means a tampered image: derail to the failure landing
075A: 3A 0C AD        LD      A,($AD0C)           ; {hard.workRam+50C} read the current pen colour
075D: FE 05           CP      $05                 ; was the pen colour already the set value?
075F: F5              PUSH    AF                  
0760: 3E 05           LD      A,$05               
0762: 32 0C AD        LD      ($AD0C),A           ; {hard.workRam+50C} set the pen colour to five
0765: 3E F1           LD      A,$F1               
0767: 32 0B AD        LD      ($AD0B),A           ; {hard.workRam+50B} set the stamp glyph to the blanking glyph, so the pen erases
076A: CD E1 01        CALL    $01E1               ; {code.armThePenRouteThenColdStartOnATamperedImage} arm the pen to the start of its route
076D: F1              POP     AF                  
076E: CC 1A 0F        CALL    Z,$0F1A             ; {code.advanceSequenceSubStep} step the sequence sub-step an extra time when the pen colour already held five
0771: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-step

loc_0774:
0774: 06 00           LD      B,$00               ; two hundred fifty-six program bytes to fold -- a zero count means the full round
0776: 21 99 4C        LD      HL,$4C99            ; point at the program run to verify
0779: 97              SUB     A                   ; clear the running total

loc_077a:
077A: AE              XOR     (HL)                ; fold the next byte into the total by exclusive-or
077B: 23              INC     HL                  
077C: 10 FC           DJNZ    $077A               ; {code.loc_077a}
077E: C6 95           ADD     A,$95               ; add the genuine total's complement -- zero only when the fold matches
0780: C4 11 0F        CALL    NZ,$0F11            ; {code.advanceSequencePhase} step the sequence phase when the fold does not match -- the image-tamper response
0783: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} read the first setup flag
0786: A7              AND     A                   
0787: 28 17           JR      Z,$07A0             ; {code.loc_07a0} nothing set: skip to the shared tail
0789: ED 5B 5B 12     LD      DE,($125B)          ; {hard.rom+125B} read a fixed command pair from the program image
078D: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the second setup flag
0790: A7              AND     A                   
0791: 28 01           JR      Z,$0794             ; {code.loc_0794} clear: leave the argument as is
0793: 1C              INC     E                   ; set: bump the command argument

loc_0794:
0794: FF              RST     $38                 ; post the command pair to the ring
0795: 3A 0E AD        LD      A,($AD0E)           ; {hard.workRam+50E} read the third setup flag
0798: A7              AND     A                   
0799: 28 05           JR      Z,$07A0             ; {code.loc_07a0} clear: skip to the shared tail
079B: 16 07           LD      D,$07               ; set the command to number seven
079D: FF              RST     $38                 ; post that command to the ring
079E: 18 04           JR      $07A4               ; {code.loc_07a4} join the shared tail

loc_07a0:
07A0: 11 02 02        LD      DE,$0202            ; command two, argument two
07A3: FF              RST     $38                 ; post it to the ring

loc_07a4:
07A4: CD 09 08        CALL    $0809               ; {code.drawKillMeter} repaint the kill meter
07A7: CD F0 19        CALL    $19F0               ; {code.resetPlayfieldAndArmNewRound} reset the playfield and arm a new round
07AA: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-step

; park the eight-bit total the image fold arrives with into B, where the
; helper the verdict arm calls hands it back to A after its own address
; arithmetic has clobbered A; then hand on by jump, so the verdict's own
; exits carry this entry too. Nothing is read or written and no flag moves
parkTheImageTotalForTheTamperVerdict:
07AD: 47              LD      B,A                 ; set the folded program total aside for the tamper verdict
07AE: C3 03 53        JP      $5303               ; {code.advanceSequenceUnlessImageTampered} hand on to the verdict

; power-on: probe the expansion socket and give the machine away to it if
; a board answers there, otherwise seat the stack at the top of work RAM,
; kick the watchdog, drive the four control lines the latch's first eight
; addresses carry low, raise the video-enable line from a byte of the
; program image, and hand on to the cold start. No work memory is touched
; -- the whole effect is the seated stack and the latched lines. Latch
; bits 5, 6 and 7 are NEVER WRITTEN here: the walk stops at 0xC307 and the
; only other store is to 0xC308, so 'settle the control latch' is five of
; its eight lines and not all eight
seatTheStackAndSettleTheControlLatch:
07B1: 3A 00 60        LD      A,($6000)           ; read the expansion socket
07B4: FE 55           CP      $55                 ; is an expansion board fitted?
07B6: CA 00 60        JP      Z,$6000             ; fitted: hand control to the expansion -- never taken on a stock board, an empty socket floats high, not the magic value
07B9: 31 00 B0        LD      SP,$B000            ; seat the stack just below sprite RAM, so it grows down through work RAM
07BC: 32 00 C2        LD      ($C200),A           ; kick the watchdog
07BF: 21 00 C3        LD      HL,$C300            ; point at the control latch
07C2: 06 08           LD      B,$08               ; eight latch addresses to clear

loc_07c4:
07C4: 36 00           LD      (HL),$00            ; clear this latch line
07C6: 23              INC     HL                  
07C7: 10 FB           DJNZ    $07C4               ; {code.loc_07c4}
07C9: 3A 4B 2D        LD      A,($2D4B)           ; {hard.rom+2D4B} read a byte of the program image
07CC: 32 08 C3        LD      ($C308),A           ; drive the video-enable line from it
07CF: C3 69 00        JP      $0069               ; {code.clearWorkRamAndSpriteBanksThenColdInit} hand on to the cold start

; blank a fixed run of fourteen character cells, walking back one native
; row at a time from a fixed cell, and give every one of them the same
; colour
blankFourteenCharCells:
07D2: 21 9F A7        LD      HL,$A79F            ; point at the first cell of the run
07D5: 11 E0 FF        LD      DE,$FFE0            ; step of minus thirty-two -- walk one plane row back each cell
07D8: 06 0E           LD      B,$0E               ; fourteen cells to blank

loc_07da:
07DA: 36 F1           LD      (HL),$F1            ; blank this cell's glyph
07DC: CB 94           RES     2,H                 ; cross to the colour plane
07DE: 36 16           LD      (HL),$16            ; give it the fixed colour
07E0: CB D4           SET     2,H                 ; cross back to the glyph plane
07E2: 19              ADD     HL,DE               ; step back one plane row
07E3: 10 F5           DJNZ    $07DA               ; {code.loc_07da}
07E5: C9              RET                         

; copyright / insert-coin attract sequence arm (table-dispatched): re-
; stamp the copyright strip, re-request the flashing copyright line,
; sample one character cell (0xA61C) into a two-byte record (0xABFE), then
; read the IN0 mirror -- hand off to the one-player game start when
; 1-player start (bit 3) is held, return when the credit count at 0xA986
; is one, otherwise queue ring command 1/argument 25 and step the sequence
; sub-step
stepCopyrightScreenAwaitingStart:
07E6: CD 06 0B        CALL    $0B06               ; {code.stampCopyrightStrip} re-stamp the copyright caption strip
07E9: CD 39 0B        CALL    $0B39               ; {code.flashCopyrightLine} re-request the flashing copyright line
07EC: 21 1C A6        LD      HL,$A61C            ; point at the title cell to sample
07EF: 11 FE AB        LD      DE,$ABFE            ; and where to stash its glyph and colour
07F2: CD FC 1A        CALL    $1AFC               ; {code.sampleCellGlyphAndColour} sample the cell
07F5: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the player-one controls
07F8: CB 5F           BIT     3,A                 ; is the one-player start held?
07FA: C2 15 32        JP      NZ,$3215            ; {code.startOnePlayerGame} held: begin a one-player game
07FD: 3A 86 A9        LD      A,($A986)           ; {hard.workRam+186} read the credit count
0800: 3D              DEC     A                   
0801: C8              RET     Z                   ; just one credit: hold on this screen rather than advancing
0802: 11 19 01        LD      DE,$0119            ; command one, caption argument twenty-five
0805: FF              RST     $38                 ; post it to the command ring
0806: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the attract sequence

; repaint the meter that shows how many kills are still owed: a bar of
; era-selected glyphs one cell long per four kills, an end glyph carrying
; the remainder, and one blanking cell past it
drawKillMeter:
0809: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era
080C: 87              ADD     A,A                 ; scale the era by ten to reach its row in the glyph table
080D: 47              LD      B,A                 
080E: 87              ADD     A,A                 
080F: 87              ADD     A,A                 
0810: 80              ADD     A,B                 
0811: 21 7C 08        LD      HL,$087C            ; point at the table of per-era glyph rows
0814: DF              RST     $18                 ; index into it by the era offset
0815: 46              LD      B,(HL)              ; take the first bar glyph
0816: 23              INC     HL                  
0817: 4E              LD      C,(HL)              ; and the second bar glyph
0818: 23              INC     HL                  ; step past to the eight end glyphs
0819: 3A 02 AD        LD      A,($AD02)           ; {hard.workRam+502} read how many kills are still owed
081C: 5F              LD      E,A                 
081D: E6 07           AND     $07                 ; its low three bits choose which end glyph
081F: CF              RST     $08                 ; read that end glyph from the row
0820: 08              EX      AF,AF'              ; set the end glyph aside
0821: 7B              LD      A,E                 ; bring the count back
0822: 21 9F A7        LD      HL,$A79F            ; point at the fixed end of the meter line
0825: 11 E0 FF        LD      DE,$FFE0            ; step of minus thirty-two -- one cell back per bar cell laid
0828: 0F              RRCA                        ; divide the count by four -- one bar cell per four kills
0829: 0F              RRCA                        
082A: E6 1F           AND     $1F                 ; cap the bar at thirty-one cells
082C: 28 0A           JR      Z,$0838             ; {code.loc_0838} no full cells: skip straight to the end glyph

loc_082e:
082E: 70              LD      (HL),B              ; lay a first-glyph bar cell
082F: 19              ADD     HL,DE               
0830: 3D              DEC     A                   
0831: 28 05           JR      Z,$0838             ; {code.loc_0838} count exhausted: lay the end glyph
0833: 71              LD      (HL),C              ; lay a second-glyph bar cell
0834: 19              ADD     HL,DE               
0835: 3D              DEC     A                   
0836: 20 F6           JR      NZ,$082E            ; {code.loc_082e} more cells to lay: go back for another pair

loc_0838:
0838: 08              EX      AF,AF'              ; bring the end glyph back
0839: 77              LD      (HL),A              ; lay the end glyph
083A: 19              ADD     HL,DE               
083B: 36 F1           LD      (HL),$F1            ; blank the cell past the end glyph
083D: C9              RET                         

; title/attract copyright-screen layout arm (table-dispatched, no static
; call site): request the flashing copyright line, stamp the copyright
; caption strip, post caption commands (command 1, arguments
; 0,1,3..7,20,21) to the command ring, then XOR-fold the 24-byte program
; block at 0x176A and step the sequence sub-step when the fold matches
; 0xC9, else transfer to the checksum-failure landing
buildCopyrightScreenThenVerifyImage:
083E: CD 39 0B        CALL    $0B39               ; {code.flashCopyrightLine} request the flashing copyright line
0841: CD 06 0B        CALL    $0B06               ; {code.stampCopyrightStrip} stamp the copyright caption strip
0844: 11 00 01        LD      DE,$0100            ; command one, first caption argument
0847: 06 02           LD      B,$02               ; two captions to post in this run

loc_0849:
0849: FF              RST     $38                 ; post this caption command
084A: 1C              INC     E                   ; step to the next caption argument
084B: 10 FC           DJNZ    $0849               ; {code.loc_0849}
084D: 1C              INC     E                   ; skip an argument
084E: 06 05           LD      B,$05               ; five more captions to post

loc_0850:
0850: FF              RST     $38                 ; post this caption command
0851: 1C              INC     E                   
0852: 10 FC           DJNZ    $0850               ; {code.loc_0850}
0854: 1E 14           LD      E,$14               ; the twentieth caption argument
0856: FF              RST     $38                 ; post it
0857: 1C              INC     E                   ; step to the twenty-first caption argument
0858: FF              RST     $38                 ; post it
0859: 21 6A 17        LD      HL,$176A            ; point at the program block to verify
085C: 06 18           LD      B,$18               ; twenty-four bytes to fold
085E: AF              XOR     A                   ; clear the running total

loc_085f:
085F: AE              XOR     (HL)                ; fold the next byte in by exclusive-or
0860: 2C              INC     L                   
0861: 10 FC           DJNZ    $085F               ; {code.loc_085f}
0863: D6 C9           SUB     $C9                 ; subtract the genuine total
0865: C2 FA 08        JP      NZ,$08FA            ; {code.loc_08fa} any other total means a tampered image: derail to the failure landing
0868: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-step

; ---- $086B-$08AD: data ----
086B: BC A6 10 30 F1 7C 68 3B A5 38 FD F1 96 5D 17 9B
087B: B9 4C 4F F1 41 72 A6 F1 8D E2 FB 37 A7 F1 AB 31
088B: 07 F1 5A 75 85 D9 1B F1 C1 E1 FA F1 B3 A0 47 7B
089B: 78 F1 04 05 C2 F1 DE F9 BB 93 AC F1 36 06 4B F1
08AB: EE D3 D4

; hand back where a fixed block of the program image starts and how many
; bytes of it to take; nothing is read and nothing is written
selectFoldBlock:
08AE: 21 5E 33        LD      HL,$335E            ; point at the program block to fold
08B1: 06 1E           LD      B,$1E               ; thirty bytes of it to take
08B3: C9              RET                         

loc_08b4:
08B4: CD 01 02        CALL    $0201               ; {code.drawInterpolatedPenRun} draw the interpolated pen run
08B7: C0              RET     NZ                  ; leave if the run has not finished
08B8: 06 00           LD      B,$00               ; two hundred fifty-six bytes to fold -- zero count means the full round
08BA: 21 80 48        LD      HL,$4880            ; point at the program run to verify
08BD: 97              SUB     A                   ; clear the running total

loc_08be:
08BE: AE              XOR     (HL)                ; fold the next byte in by exclusive-or
08BF: 23              INC     HL                  
08C0: 10 FC           DJNZ    $08BE               ; {code.loc_08be}
08C2: C6 D0           ADD     A,$D0               ; add the genuine total's complement
08C4: C2 D9 00        JP      NZ,$00D9            ; {code.loc_00d9} mismatch means a tampered image: derail
08C7: 11 13 01        LD      DE,$0113            ; command one, caption argument nineteen
08CA: FF              RST     $38                 ; post it to the ring
08CB: 1E 00           LD      E,$00               ; command one, caption argument zero
08CD: FF              RST     $38                 ; post it
08CE: 1E 14           LD      E,$14               ; caption argument twenty
08D0: FF              RST     $38                 ; post it
08D1: 1C              INC     E                   ; caption argument twenty-one
08D2: FF              RST     $38                 ; post it
08D3: 1E 0C           LD      E,$0C               ; caption argument twelve
08D5: FF              RST     $38                 ; post it
08D6: CD DC 4B        CALL    $4BDC               ; {code.paintFiveLabelledNumericReadouts} paint the five labelled numeric readouts
08D9: 21 95 A9        LD      HL,$A995            ; point at the five bytes to clear
08DC: AF              XOR     A                   ; the value to clear them with: zero
08DD: 06 05           LD      B,$05               ; five bytes to clear

loc_08df:
08DF: 77              LD      (HL),A              ; clear this byte
08E0: 23              INC     HL                  
08E1: 10 FC           DJNZ    $08DF               ; {code.loc_08df}
08E3: 36 03           LD      (HL),$03            ; set the sixth byte to three
08E5: ED 5B 93 A9     LD      DE,($A993)          ; {hard.workRam+193} read the destination pointer
08E9: 3A 99 A9        LD      A,($A999)           ; {hard.workRam+199} read the index
08EC: 21 C7 12        LD      HL,$12C7            ; point at the lookup table
08EF: CF              RST     $08                 ; read the entry the index selects
08F0: 12              LD      (DE),A              ; store it at the destination
08F1: CB 92           RES     2,D                 ; cross to the other plane for the same cell
08F3: 1A              LD      A,(DE)              ; read what stands there
08F4: 32 90 A9        LD      ($A990),A           ; {hard.workRam+190} keep it
08F7: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-step

loc_08fa:
08FA: 4B              LD      C,E                 
08FB: 01 4A 01        LD      BC,$014A            
08FE: 49              LD      C,C                 
08FF: 01 48 01        LD      BC,$0148            
0902: 47              LD      B,A                 
0903: 01 46 01        LD      BC,$0146            
0906: 45              LD      B,L                 
0907: 01 40 01        LD      BC,$0140            
090A: 3E 01           LD      A,$01               
090C: 3C              INC     A                   
090D: 01 3A 01        LD      BC,$013A            
0910: 38 01           JR      C,$0913             
0912: 32 01 2F        LD      ($2F01),A           ; {hard.rom+2F01}
0915: 01 2D 01        LD      BC,$012D            
0918: 27              DAA                         
0919: 01 24 01        LD      BC,$0124            
091C: 21 01 1E        LD      HL,$1E01            
091F: 01 18 01        LD      BC,$0118            
0922: 15              DEC     D                   

loc_0923:
0923: 01 12 01        LD      BC,$0112            
0926: 0C              INC     C                   
0927: 01 09 01        LD      BC,$0109            
092A: 06 01           LD      B,$01               
092C: 00              NOP                         
092D: 01 FD 00        LD      BC,$00FD            
0930: FA 00 F7        JP      M,$F700             
0933: 00              NOP                         
0934: F1              POP     AF                  
0935: 00              NOP                         
0936: EE 00           XOR     $00                 
0938: EB              EX      DE,HL               
0939: 00              NOP                         
093A: E5              PUSH    HL                  
093B: 00              NOP                         
093C: E2 00 DE        JP      PO,$DE00            
093F: 00              NOP                         
0940: D8              RET     C                   
0941: 00              NOP                         
0942: D5              PUSH    DE                  
0943: 00              NOP                         
0944: D1              POP     DE                  
0945: 00              NOP                         
0946: CA 00 C6        JP      Z,$C600             
0949: 00              NOP                         
094A: C3 00 BC        JP      $BC00               

; ---- $094D-$0B05: data ----
094D: 00 B6 00 AE 00 A9 00 9F 00 9C 00 93 00 8A 00 84
095D: 00 7B 00 71 00 6B 00 61 00 57 00 50 00 45 00 3B
096D: 00 34 00 29 00 1E 00 13 00 08 00 00 00 00 00 F8
097D: FF ED FF 00 00 D7 FF CC FF C5 FF BB FF B0 FF A9
098D: FF 9F FF 95 FF 8F FF 85 FF 7C FF 76 FF 6D FF 64
099D: FF 61 FF 64 FF 52 FF 4A FF 44 FF 3D FF 3A FF 36
09AD: FF 2F FF 2B FF 28 FF 22 FF 1E FF 1B FF 15 FF 12
09BD: FF 0F FF 0F FF 06 FF 03 FF 00 FF FA FE F7 FE F4
09CD: FE EE FE EB FE E8 FE E2 FE DF FE DC FE D9 FE D3
09DD: FE D1 FE CE FE C8 FE C6 FE C4 FE C2 FE C0 FE BB
09ED: FE BA FE B9 FE B8 FE B7 FE B6 FE B5 FE B5 FE B6
09FD: FE B7 FE B8 FE B9 FE BA FE BB FE C0 FE C2 FE C4
0A0D: FE C6 FE C8 FE CE FE D1 FE D3 FE D9 FE DC FE DF
0A1D: FE E2 FE E8 FE EB FE EE FE F4 FE F7 FE FA FE 00
0A2D: FF 03 FF 06 FF 09 FF 0F FF 12 FF 15 FF 1B FF 1E
0A3D: FF 22 FF 28 FF 2B FF 2F FF 36 FF 3A FF 3D FF 44
0A4D: FF 4A FF 52 FF 57 FF 61 FF 64 FF 6D FF 76 FF 7C
0A5D: FF 85 FF 8F FF 95 FF 9F FF A9 FF B0 FF BB FF C5
0A6D: FF CC FF D7 FF E2 FF ED FF F8 FF 00 00 00 00 08
0A7D: 00 13 00 1E 00 29 00 34 00 3B 00 45 00 50 00 57
0A8D: 00 61 00 6B 00 71 00 7B 00 84 00 8A 00 93 00 9C
0A9D: 00 9F 00 9F 00 AE 00 B6 00 BC 00 C3 00 C6 00 CA
0AAD: 00 D1 00 D5 00 D8 00 DE 00 E2 00 E5 00 EB 00 EE
0ABD: 00 F1 00 EE 00 FA 00 FD 00 00 01 06 01 09 01 0C
0ACD: 01 12 01 15 01 18 01 1E 01 21 01 24 01 27 01 2D
0ADD: 01 2F 01 27 01 38 01 3A 01 3C 01 3E 01 40 01 45
0AED: 01 46 01 47 01 48 01 49 01 4A 01 4B 01 77 A6 13
0AFD: ED DC A5 7D 34 F1 F1 F1 B9

; stamp the four fixed pieces of the copyright caption into the display-
; list shadow; it reads nothing, so re-stamping changes nothing
stampCopyrightStrip:
0B06: FD 21 10 AA     LD      IY,$AA10            ; point at the strip's four display-list entries
0B0A: 06 04           LD      B,$04               ; four pieces to lay
0B0C: 0E 04           LD      C,$04               ; first shape number, counting up one per piece
0B0E: 16 A0           LD      D,$A0               ; the leading edge on the stepping axis
0B10: 1E D8           LD      E,$D8               ; the shared position on the fixed axis

loc_0b12:
0B12: FD 72 31        LD      (IY+$31),D          ; set this piece's position on the stepping axis
0B15: FD 73 00        LD      (IY+$00),E          ; set its position on the fixed axis
0B18: FD 71 01        LD      (IY+$01),C          ; set its shape number
0B1B: FD 36 30 6C     LD      (IY+$30),$6C        ; set its colour and attributes
0B1F: FD 23           INC     IY                  
0B21: FD 23           INC     IY                  
0B23: 0C              INC     C                   ; next shape number
0B24: 7A              LD      A,D                 
0B25: D6 10           SUB     $10                 ; step the leading edge back by sixteen for the next piece
0B27: 57              LD      D,A                 
0B28: 10 E8           DJNZ    $0B12               ; {code.loc_0b12}
0B2A: C9              RET                         

; park the four sprites of the copyright caption above the first visible
; line by zeroing the vertical byte of each, leaving the rest of their
; slots standing
hideCaptionSprites:
0B2B: 21 41 AA        LD      HL,$AA41            ; point at the first caption sprite's position
0B2E: 11 02 00        LD      DE,$0002            ; step two slots at a time
0B31: 06 04           LD      B,$04               ; four caption sprites to hide
0B33: AF              XOR     A                   ; the value that hides them: zero

loc_0b34:
0B34: 77              LD      (HL),A              ; push this sprite above the top line by zeroing its vertical byte
0B35: 19              ADD     HL,DE               
0B36: 10 FC           DJNZ    $0B34               ; {code.loc_0b34}
0B38: C9              RET                         

; make the copyright line change colour every frame: ask for the same
; glyph run at the same place in one of two colours, choosing between them
; on the low bit of the frame counter, which it only reads. The request
; goes on the command ring and is dropped when the slot the write cursor
; names has not been consumed, so a frame can silently miss its turn
flashCopyrightLine:
0B39: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame counter
0B3C: CB 47           BIT     0,A                 ; test its low bit, which flips every frame
0B3E: 28 06           JR      Z,$0B46             ; {code.enqueueFixedCommandOnRing} even frame: queue the other version of the line
0B40: 11 00 01        LD      DE,$0100            ; command one, this frame's argument
0B43: C3 38 00        JP      $0038               ; {code.postCommand} post it to the command ring, so the line flashes frame to frame

; queue one fixed command, with its one fixed argument, in the command
; ring -- both bytes are chosen here and whatever the caller held is
; discarded; the pair is dropped when the slot the write cursor names has
; not been consumed, and this entry never learns that
enqueueFixedCommandOnRing:
0B46: 11 1F 01        LD      DE,$011F            ; command one, argument thirty-one -- the other version of the copyright line
0B49: C3 38 00        JP      $0038               ; {code.postCommand} post it to the command ring

; add a run of bytes together and answer whether the total is the byte the
; caller named; the length means a full 256 when it is zero, the total
; wraps at eight bits, nothing is written, and the answer is left for the
; caller rather than acted on here
sumByteRunAndCompareToExpected:
0B4C: AF              XOR     A                   ; clear the running total before folding the run

loc_0b4d:
0B4D: 86              ADD     A,(HL)              ; add the next byte into the total
0B4E: 23              INC     HL                  
0B4F: 10 FC           DJNZ    $0B4D               ; {code.loc_0b4d}
0B51: B9              CP      C                   ; does the total match the byte the caller named?
0B52: C8              RET     Z                   ; yes: answer that it matches
0B53: C9              RET                         ; no: answer that it does not

; ---- $0B54-$0B8F: data ----
0B54: AF AE 23 10 FC B9 C8 C3 00 00 AF 86 23 0D 28 02
0B64: 18 F9 CB 47 C8 C3 00 00 21 06 0B 06 24 0E 00 7E
0B74: 91 23 10 FB EB BE C9 0F A7 13 88 0D ED C4 F1 ED
0B84: DC A5 D7 DC F1 8C 0D DC DC 68 3B B9

; tail transfer into the foreground command-ring loop: a jp that hands
; control to the drain and never comes back; touches no memory or
; register, so its whole product is the drain's continuation handed
; straight back
enterCommandRingDrain:
0B90: C3 93 0B        JP      $0B93               ; {code.runCommandRingDrainLoop} back to the top of the command-ring drain

; the foreground loop: take commands off the ring one at a time and run
; each, for ever. A read cursor names a cell; while its high bit is set
; the cell holds nothing and the loop looks again, which is the only wait
; for the vblank among the foreground loops a coin-and-play tape reaches
; -- the ring is refilled from outside the loop. An occupied cell gives up
; a command byte and an argument byte, both cells are freed BEFORE the
; command runs so a command may reuse the pair it arrived in, and the low
; nibble of the command indexes a sixteen-way table. Where the handler
; lands is the exit test: it is handed one fixed place to come back to,
; and anything else means it has taken the machine somewhere this loop no
; longer owns
runCommandRingDrainLoop:
0B93: 26 AC           LD      H,$AC               ; the command ring lives on page $AC
0B95: 3A B3 A9        LD      A,($A9B3)           ; {hard.workRam+1B3} read the ring's read cursor
0B98: 6F              LD      L,A                 ; point at the cell it names
0B99: 7E              LD      A,(HL)              ; take that cell's command byte
0B9A: 07              RLCA                        ; rotate its top bit out
0B9B: DA 90 0B        JP      C,$0B90             ; {code.enterCommandRingDrain} top bit set means the cell is empty: wait a frame and look again
0B9E: 4E              LD      C,(HL)              ; keep the command
0B9F: 36 FF           LD      (HL),$FF            ; free the cell so it can be filled again
0BA1: 23              INC     HL                  ; step to the argument cell
0BA2: 46              LD      B,(HL)              ; take the argument
0BA3: 36 FF           LD      (HL),$FF            ; free that cell too
0BA5: 23              INC     HL                  
0BA6: 7D              LD      A,L                 
0BA7: E6 3F           AND     $3F                 ; keep the cursor inside the sixty-four-cell ring
0BA9: 32 B3 A9        LD      ($A9B3),A           ; {hard.workRam+1B3} save the advanced read cursor
0BAC: 79              LD      A,C                 
0BAD: E6 0F           AND     $0F                 ; the command's low nibble picks one of sixteen handlers
0BAF: 21 BC 0B        LD      HL,$0BBC            ; point at the handler table
0BB2: CD 8C 01        CALL    $018C               ; {code.fetchWideTableWord} read this handler's address from it
0BB5: 78              LD      A,B                 ; hand the argument to the handler
0BB6: 21 90 0B        LD      HL,$0B90            
0BB9: E5              PUSH    HL                  ; make the loop top the handler's return
0BBA: EB              EX      DE,HL               
0BBB: E9              JP      (HL)                ; run the handler

; ---- $0BBC-$0BF1: data ----
0BBC: DD 0B F2 0B 0F 0C 39 0C 90 0C 72 4D D7 0D AC 0E
0BCC: DC 0B DC 0B 21 34 23 0C DC 0B DC 0B DC 0B DC 0B
0BDC: C9 21 50 0C CD 8C 01 EB 5E 23 56 23 23 7E FE B9
0BEC: C8 12 23 E7 18 F7

; paint the caption an index selects: the index picks a record from one
; word table, and the record supplies the destination cell, the colour and
; the glyph run that drawTextRun then paints
drawTextRunByIndex:
0BF2: 21 50 0C        LD      HL,$0C50            ; point at the caption-record table
0BF5: CD 8C 01        CALL    $018C               ; {code.fetchWideTableWord} read the record pointer this caption index selects
0BF8: EB              EX      DE,HL               ; point at that record
0BF9: 5E              LD      E,(HL)              ; read the low byte of the cell the caption starts at
0BFA: 23              INC     HL                  ; step to the high byte
0BFB: 56              LD      D,(HL)              ; read the high byte -- the caption's first cell
0BFC: 23              INC     HL                  ; step on
0BFD: 4E              LD      C,(HL)              ; read the colour every cell of the caption takes
0BFE: 23              INC     HL                  ; step to the glyph run, then fall into the painter

; paint one caption into the character plane and give every cell of it one
; colour, taking glyphs in order from a run that ends at a fixed
; terminating code
drawTextRun:
0BFF: 7E              LD      A,(HL)              ; read the next glyph of the run
0C00: FE B9           CP      $B9                 ; is it the run-ending code?
0C02: C8              RET     Z                   ; end reached: stop, leaving the pointer on the terminator
0C03: 12              LD      (DE),A              ; write the glyph into the character cell
0C04: CB 92           RES     2,D                 ; drop to the colour plane beneath it
0C06: 79              LD      A,C                 ; fetch the caption's colour
0C07: 12              LD      (DE),A              ; give the cell its colour
0C08: CB D2           SET     2,D                 ; back up to the character plane
0C0A: 23              INC     HL                  ; step to the next glyph
0C0B: E7              RST     $20                 ; step the cursor one cell along the line
0C0C: C3 FF 0B        JP      $0BFF               ; {code.drawTextRun} round the loop for the next glyph

; ---- $0C0F-$0D6A: data ----
0C0F: 21 50 0C CD 8C 01 EB 5E 23 56 23 23 3A 0C AD E6
0C1F: 0F 4F 18 DC 21 50 0C CD 8C 01 EB 5E 23 56 23 23
0C2F: 3A 0C AD C6 0A E6 0F 4F 18 C6 21 50 0C CD 8C 01
0C3F: EB 5E 23 56 23 23 7E FE B9 C8 3E F1 12 23 E7 18
0C4F: F5 6B 08 73 16 7F 30 1D 58 FA 49 D6 15 4C 58 09
0C5F: 25 CA 15 67 01 42 4E 10 18 CE 48 A4 1B FA 0A 31
0C6F: 24 3B 12 9B 45 A4 2C 4F 00 9E 31 6E 29 7B 0B 5C
0C7F: 34 D2 3E 48 33 49 0F 14 4C 54 59 ED 55 D8 23 00
0C8F: 49 4F 06 00 3A 30 AD A7 CA E8 0C 79 A7 CA E9 0C
0C9F: 21 27 0D 09 09 09 11 33 AD 3A 32 AD A7 28 03 11
0CAF: 36 AD 1A 86 27 12 13 23 1A 8E 27 12 13 23 1A 8E
0CBF: 27 12 21 8D A9 01 03 00 1A BE 38 0F 20 07 1B 2B
0CCF: 0D 20 F5 18 06 EB ED B8 CD 6B 0D 3A 32 AD A7 20
0CDF: 05 CD 57 0D 18 03 CD 61 0D C9 3A 31 AD A7 20 1B
0CEF: 3A 31 0B CD F2 0B CD 57 0D 3A C6 15 CD 39 0C 11
0CFF: 01 A5 06 06 3E F1 12 E7 10 FA C9 3E 06 CD F2 0B
0D0F: CD 57 0D 3E 07 CD F2 0B CD 61 0D C9 3C A2 C7 AC
0D1F: 7C A2 43 AB FC A1 BE AC 00 00 00 00 01 00 00 02
0D2F: 00 00 03 00 00 04 00 00 05 00 00 06 00 00 07 00
0D3F: 00 08 00 00 09 00 00 10 00 00 15 00 00 20 00 00
0D4F: 30 00 00 40 00 00 50 00 11 81 A7 21 35 AD 0E 10
0D5F: 18 12 11 01 A5 21 38 AD 0E 10 18 08

; enter the shared packed-decimal digit routine at 0x0D73 with a third
; fixed triple -- first cell 0xA641, the field whose high end is 0xA98D,
; and a fixed colour; the routine walks the field downward, so the high
; end is where it starts
paintHighScoreReadout:
0D6B: 11 41 A6        LD      DE,$A641            ; the leftmost digit lands here
0D6E: 21 8D A9        LD      HL,$A98D            ; print from the high score's top byte -- the field is walked downward
0D71: 0E 10           LD      C,$10               ; colour for every digit, then fall into the printer

; paint a six-digit field: two packed bytes through the suppressing
; painter, sharing one suppression flag this entry clears, then a third
; through the plain painter so the last two digits always show, walking
; the source pointer backwards as it goes
paintSixDigitFieldSuppressingLeadingZeros:
0D73: 06 00           LD      B,$00               ; clear the leading-zero suppression flag for the whole field
0D75: CD A0 0D        CALL    $0DA0               ; {code.paintTwoSuppressedDigitsFromByte} print the top two digits, suppressing leading zeros
0D78: 2B              DEC     HL                  ; step back one source byte
0D79: CD A0 0D        CALL    $0DA0               ; {code.paintTwoSuppressedDigitsFromByte} print the next two, still suppressing
0D7C: 2B              DEC     HL                  
0D7D: CD 81 0D        CALL    $0D81               ; {code.paintTwoUnsuppressedDigitsFromByte} print the last two plainly, so they always show
0D80: C9              RET                         

; paint the two decimal digits packed into one byte, the high one first,
; stepping the cursor one cell on after each; the byte is read twice from
; the pointer the caller is walking, shifted down for the high digit and
; taken whole for the low, and the colour and cursor arrive as the caller
; left them
paintTwoUnsuppressedDigitsFromByte:
0D81: 7E              LD      A,(HL)              ; read the packed byte
0D82: 0F              RRCA                        ; rotate the high nibble down into the low four bits
0D83: 0F              RRCA                        
0D84: 0F              RRCA                        
0D85: 0F              RRCA                        
0D86: CD 90 0D        CALL    $0D90               ; {code.paintUnsuppressedDigit} print the high digit
0D89: E7              RST     $20                 ; step the cursor one cell on
0D8A: 7E              LD      A,(HL)              ; read the byte again for the low digit
0D8B: CD 90 0D        CALL    $0D90               ; {code.paintUnsuppressedDigit} print the low digit
0D8E: E7              RST     $20                 ; step the cursor on
0D8F: C9              RET                         

; paint one decimal digit and the caller's colour into the cell a cursor
; names, taking the glyph from the table at 0x0DCC by the value's low four
; bits -- a zero always paints the digit `0`, where the suppressing twin
; paints the blank instead while no significant digit has been seen yet --
; and leaving the cursor on the glyph side and the caller's run pointer
; where it was
paintUnsuppressedDigit:
0D90: E6 0F           AND     $0F                 ; keep the low four bits -- the digit value
0D92: E5              PUSH    HL                  ; save the caller's run pointer
0D93: 21 CC 0D        LD      HL,$0DCC            ; point at the digit-glyph table
0D96: CF              RST     $08                 ; look up this digit's glyph (zero prints a '0' here)
0D97: E1              POP     HL                  ; restore the run pointer
0D98: 12              LD      (DE),A              ; write the glyph into the cell
0D99: CB 92           RES     2,D                 ; drop to the colour plane
0D9B: 79              LD      A,C                 ; take the caller's colour
0D9C: 12              LD      (DE),A              ; colour the cell
0D9D: CB D2           SET     2,D                 ; back to the character plane
0D9F: C9              RET                         

; paint the two decimal digits packed into one byte with a leading zero
; suppressed, the high one first, stepping the cursor one cell on after
; each; the caller's suppression flag arrives, carries across both digits
; and goes back out, so a longer run of digits suppresses as one field
paintTwoSuppressedDigitsFromByte:
0DA0: 7E              LD      A,(HL)              ; read the packed byte
0DA1: 0F              RRCA                        ; rotate the high nibble down into the low four bits
0DA2: 0F              RRCA                        
0DA3: 0F              RRCA                        
0DA4: 0F              RRCA                        
0DA5: CD AF 0D        CALL    $0DAF               ; {code.paintSuppressedDigit} print the high digit, suppressing a leading zero
0DA8: E7              RST     $20                 ; step the cursor on
0DA9: 7E              LD      A,(HL)              ; read the byte again for the low digit
0DAA: CD AF 0D        CALL    $0DAF               ; {code.paintSuppressedDigit} print the low digit, still suppressing
0DAD: E7              RST     $20                 ; step the cursor on
0DAE: C9              RET                         

; paint one four-bit digit into the cell the cursor names with the
; caller's colour a plane below, using the blank glyph instead when the
; digit is zero and no significant digit has been seen yet, and stepping
; the caller's flag on at the first that is
paintSuppressedDigit:
0DAF: E6 0F           AND     $0F                 ; keep the low four bits -- the digit
0DB1: 28 03           JR      Z,$0DB6             ; {code.loc_0db6} a zero digit: decide blank versus '0'
0DB3: 04              INC     B                   ; non-zero: mark that a significant digit has been seen
0DB4: 18 08           JR      $0DBE               ; {code.loc_0dbe} and print it by its own value

loc_0db6:
0DB6: 3A 46 32        LD      A,($3246)           ; {hard.rom+3246} a zero: take the blank-glyph index from the program image
0DB9: 04              INC     B                   ; momentarily bump the seen-digit count
0DBA: 05              DEC     B                   ; drop it back, setting the flags: has a significant digit been seen yet?
0DBB: 28 01           JR      Z,$0DBE             ; {code.loc_0dbe} none yet: print the blank
0DBD: AF              XOR     A                   ; one already seen: print '0' instead

loc_0dbe:
0DBE: E5              PUSH    HL                  ; save the caller's run pointer
0DBF: 21 CC 0D        LD      HL,$0DCC            ; point at the digit-glyph table
0DC2: CF              RST     $08                 ; look up the glyph for this index
0DC3: E1              POP     HL                  ; restore the run pointer
0DC4: 12              LD      (DE),A              ; write the glyph into the cell
0DC5: CB 92           RES     2,D                 ; drop to the colour plane
0DC7: 79              LD      A,C                 ; take the caller's colour
0DC8: 12              LD      (DE),A              ; colour the cell
0DC9: CB D2           SET     2,D                 ; back to the character plane
0DCB: C9              RET                         

; ---- $0DCC-$0DD6: data ----
0DCC: 13 96 9B CD F3 7F 65 02 17 5D F1

; draw a clamped 0..99 value as a right-to-left row of denomination tiles
; (thirties, tens, fives, ones) from display cell 0xa463, pad the rest of
; the row to 0xa623 with the blank glyph, then verify a fixed three-word
; checksum (0x009d/0x00a0/0x00a3) and hard-reset via 0x0000 on mismatch
drawCountAsPictogramStrip:
0DD7: 11 63 A4        LD      DE,$A463            ; point at the start of the pictogram row
0DDA: FE 64           CP      $64                 ; is the count 100 or more?
0DDC: 38 02           JR      C,$0DE0             ; {code.loc_0de0} under 100: keep the value
0DDE: 3E 63           LD      A,$63               ; clamp to 99

loc_0de0:
0DE0: D9              EXX                         ; tally the denominations in the spare registers, leaving the row cursor alone
0DE1: 06 00           LD      B,$00               ; no thirties yet

loc_0de3:
0DE3: D6 1E           SUB     $1E                 ; subtract thirty
0DE5: 38 03           JR      C,$0DEA             ; {code.loc_0dea} gone negative: no more thirties
0DE7: 04              INC     B                   ; one more thirty
0DE8: 18 F9           JR      $0DE3               ; {code.loc_0de3} keep subtracting

loc_0dea:
0DEA: C6 1E           ADD     A,$1E               ; add the last thirty back
0DEC: 0E 00           LD      C,$00               ; no tens yet

loc_0dee:
0DEE: D6 0A           SUB     $0A                 ; subtract ten
0DF0: 38 03           JR      C,$0DF5             ; {code.loc_0df5} gone negative: no more tens
0DF2: 0C              INC     C                   ; one more ten
0DF3: 18 F9           JR      $0DEE               ; {code.loc_0dee} keep subtracting

loc_0df5:
0DF5: C6 0A           ADD     A,$0A               ; add the last ten back
0DF7: 16 00           LD      D,$00               ; no fives yet

loc_0df9:
0DF9: D6 05           SUB     $05                 ; subtract five
0DFB: 38 03           JR      C,$0E00             ; {code.loc_0e00} gone negative: no more fives
0DFD: 14              INC     D                   ; one more five
0DFE: 18 F9           JR      $0DF9               ; {code.loc_0df9} keep subtracting

loc_0e00:
0E00: C6 05           ADD     A,$05               ; add the last five back
0E02: 5F              LD      E,A                 ; what remains is the count of ones
0E03: D9              EXX                         ; return to the drawing registers
0E04: D9              EXX                         ; dip into the spare registers for the ones count
0E05: 7B              LD      A,E                 ; take the count of ones
0E06: D9              EXX                         ; back to the drawing registers
0E07: A7              AND     A                   ; any ones to draw?
0E08: 28 0C           JR      Z,$0E16             ; {code.loc_0e16} none: on to the fives
0E0A: 06 01           LD      B,$01               ; ones tile code
0E0C: 0E 13           LD      C,$13               ; ones colour

loc_0e0e:
0E0E: 08              EX      AF,AF'              ; park the remaining count out of the way
0E0F: CD 8D 0E        CALL    $0E8D               ; {code.drawSlotWithOneGlyph} draw one 'ones' block
0E12: 08              EX      AF,AF'              ; take the count back
0E13: 3D              DEC     A                   ; one fewer to draw
0E14: 20 F8           JR      NZ,$0E0E            ; {code.loc_0e0e} more ones? round again

loc_0e16:
0E16: D9              EXX                         ; dip into the spare registers
0E17: 7A              LD      A,D                 ; take the count of fives
0E18: D9              EXX                         ; back to the drawing registers
0E19: A7              AND     A                   ; any fives to draw?
0E1A: 28 0C           JR      Z,$0E28             ; {code.loc_0e28} none: on to the tens
0E1C: 06 32           LD      B,$32               ; fives tile code
0E1E: 0E 11           LD      C,$11               ; fives colour

loc_0e20:
0E20: 08              EX      AF,AF'              ; park the count
0E21: CD 9C 0E        CALL    $0E9C               ; {code.paintDoubleTile} draw one 'fives' block (a two-tile mark)
0E24: 08              EX      AF,AF'              ; take the count back
0E25: 3D              DEC     A                   ; one fewer
0E26: 20 F8           JR      NZ,$0E20            ; {code.loc_0e20} more fives? round again

loc_0e28:
0E28: D9              EXX                         ; dip into the spare registers
0E29: 79              LD      A,C                 ; take the count of tens
0E2A: D9              EXX                         ; back to the drawing registers
0E2B: A7              AND     A                   ; any tens to draw?
0E2C: 28 0C           JR      Z,$0E3A             ; {code.loc_0e3a} none: on to the thirties
0E2E: 06 CE           LD      B,$CE               ; tens tile code
0E30: 0E 16           LD      C,$16               ; tens colour

loc_0e32:
0E32: 08              EX      AF,AF'              ; park the count
0E33: CD 70 0E        CALL    $0E70               ; {code.paintQuadTile} draw one 'tens' block (a four-tile mark)
0E36: 08              EX      AF,AF'              ; take the count back
0E37: 3D              DEC     A                   ; one fewer
0E38: 20 F8           JR      NZ,$0E32            ; {code.loc_0e32} more tens? round again

loc_0e3a:
0E3A: D9              EXX                         ; dip into the spare registers
0E3B: 78              LD      A,B                 ; take the count of thirties
0E3C: D9              EXX                         ; back to the drawing registers
0E3D: A7              AND     A                   ; any thirties to draw?
0E3E: 28 0C           JR      Z,$0E4C             ; {code.loc_0e4c} none: on to padding the row
0E40: 06 23           LD      B,$23               ; thirties tile code
0E42: 0E 11           LD      C,$11               ; thirties colour

loc_0e44:
0E44: 08              EX      AF,AF'              ; park the count
0E45: CD 70 0E        CALL    $0E70               ; {code.paintQuadTile} draw one 'thirties' block (a four-tile mark)
0E48: 08              EX      AF,AF'              ; take the count back
0E49: 3D              DEC     A                   ; one fewer
0E4A: 20 F8           JR      NZ,$0E44            ; {code.loc_0e44} more thirties? round again

loc_0e4c:
0E4C: 01 10 F1        LD      BC,$F110            ; blank glyph in B, its colour in C

loc_0e4f:
0E4F: 21 DD 59        LD      HL,$59DD            ; load the end-of-row test value
0E52: 19              ADD     HL,DE               ; reached the end of the row?
0E53: 38 05           JR      C,$0E5A             ; {code.loc_0e5a} row full: run the integrity check
0E55: CD 8D 0E        CALL    $0E8D               ; {code.drawSlotWithOneGlyph} blank the next slot
0E58: 18 F5           JR      $0E4F               ; {code.loc_0e4f} keep padding

loc_0e5a:
0E5A: AF              XOR     A                   ; start the running total at zero
0E5B: 2A A0 00        LD      HL,($00A0)          ; {hard.rom+A0} take the first integrity word from the program image
0E5E: ED 5B A3 00     LD      DE,($00A3)          ; {hard.rom+A3} take the second integrity word

loc_0e62:
0E62: ED 4B 9D 00     LD      BC,($009D)          ; {hard.rom+9D} take the third integrity word

loc_0e66:
0E66: 19              ADD     HL,DE               ; fold the words together
0E67: 09              ADD     HL,BC               ; fold in the third
0E68: 85              ADD     A,L                 ; add in the low half
0E69: 84              ADD     A,H                 ; add in the high half
0E6A: D6 69           SUB     $69                 ; a genuine image nets to this constant
0E6C: C2 00 00        JP      NZ,$0000            ; {code.trampolineToSeatTheStackAndSettleTheControlLatch} tampered: restart the machine from the reset entry
0E6F: C9              RET                         

; lay one four-tile block into the character plane from a base code the
; caller fixes, give all four the caller's colour a plane below, and leave
; the cursor clear of the block for the next one
paintQuadTile:
0E70: 78              LD      A,B                 ; take the base tile code
0E71: 3C              INC     A                   ; the top-right quarter is base+1
0E72: 12              LD      (DE),A              ; lay it in the cursor cell
0E73: 3D              DEC     A                   ; back to the base code
0E74: 1B              DEC     DE                  ; step one cell back
0E75: 12              LD      (DE),A              ; lay the top-left quarter (the base code)
0E76: EF              RST     $28                 ; drop down one line
0E77: 78              LD      A,B                 ; the base code again
0E78: C6 02           ADD     A,$02               ; the bottom-left quarter is base+2
0E7A: 12              LD      (DE),A              ; lay it in
0E7B: 3C              INC     A                   ; the bottom-right quarter is base+3
0E7C: 13              INC     DE                  ; step one cell on
0E7D: 12              LD      (DE),A              ; lay it in
0E7E: 21 00 FC        LD      HL,$FC00            ; offset down to the colour plane
0E81: 19              ADD     HL,DE               ; point at the bottom-right quarter's colour cell
0E82: EF              RST     $28                 ; leave the cursor two lines on, clear of the block
0E83: 71              LD      (HL),C              ; colour the bottom-right quarter
0E84: 2B              DEC     HL                  ; step back one cell
0E85: 71              LD      (HL),C              ; colour the bottom-left quarter
0E86: EB              EX      DE,HL               
0E87: E7              RST     $20                 ; step up to the top row's colour cells
0E88: EB              EX      DE,HL               
0E89: 71              LD      (HL),C              ; colour the top-left quarter
0E8A: 23              INC     HL                  ; step on one cell
0E8B: 71              LD      (HL),C              ; colour the top-right quarter
0E8C: C9              RET                         

; paint a two-cell character slot with a single glyph, blanking the other
; cell of the slot, give both the caller's colour, and step the cursor on
; to the next slot
drawSlotWithOneGlyph:
0E8D: EB              EX      DE,HL               ; work with the cursor in HL
0E8E: 70              LD      (HL),B              ; write the glyph into the cell
0E8F: 2B              DEC     HL                  ; step one cell back
0E90: 36 F1           LD      (HL),$F1            ; blank that cell
0E92: CB 94           RES     2,H                 ; drop to the colour plane
0E94: 71              LD      (HL),C              ; colour the blanked cell
0E95: 23              INC     HL                  ; step one cell on
0E96: 71              LD      (HL),C              ; colour the glyph cell
0E97: CB D4           SET     2,H                 ; back to the character plane
0E99: EB              EX      DE,HL               ; cursor back into place
0E9A: EF              RST     $28                 ; step on to the next slot
0E9B: C9              RET                         

; lay one two-tile block into the character plane from a base code the
; caller fixes -- the base below the cursor and the base plus one at it --
; colour both cells a plane below, and step the cursor clear of the block
paintDoubleTile:
0E9C: EB              EX      DE,HL               ; work with the cursor in HL
0E9D: 04              INC     B                   ; the upper tile code is base+1
0E9E: 70              LD      (HL),B              ; lay it in the cursor cell
0E9F: 05              DEC     B                   ; back to the base code
0EA0: 2B              DEC     HL                  ; the cell below
0EA1: 70              LD      (HL),B              ; lay the lower tile (the base code)
0EA2: CB 94           RES     2,H                 ; drop to the colour plane
0EA4: 71              LD      (HL),C              ; colour the lower cell
0EA5: 23              INC     HL                  ; the cell above
0EA6: 71              LD      (HL),C              ; colour the upper cell
0EA7: CB D4           SET     2,H                 ; back to the character plane
0EA9: EB              EX      DE,HL               ; cursor back into place
0EAA: EF              RST     $28                 ; step on past the block
0EAB: C9              RET                         

; ---- $0EAC-$0F10: data ----
0EAC: 3A 01 AD FE 64 D0 3E 0E CD 0F 0C EF EF 21 01 AD
0EBC: 06 01 3A 0C AD 4F C5 0E 00 7E D6 0A 38 03 0C 18
0ECC: F9 C6 0A 08 79 C1 CD EB 0E E7 08 CD EB 0E E7 11
0EDC: 48 17 01 8C 10 1A 81 4F 13 10 FA C2 09 25 C9 E6
0EEC: 0F 28 10 06 00 E5 21 06 0F CF E1 12 CB 92 79 12
0EFC: CB D2 C9 78 A7 28 EE 05 EF C9 E3 49 A8 64 27 AE
0F0C: 42 B0 D5 86 F1

; advance the outer sequence phase and restart its inner step index at
; zero
advanceSequencePhase:
0F11: 21 AB A9        LD      HL,$A9AB            ; point at the sequence phase
0F14: 34              INC     (HL)                ; step to the next phase
0F15: AF              XOR     A                   
0F16: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} restart the inner sub-step at zero for the new phase
0F19: C9              RET                         

; step the jump-table sequence index on by one; reached as a tail jump so
; the caller's own return carries it
advanceSequenceSubStep:
0F1A: 21 AC A9        LD      HL,$A9AC            ; point at the sequence sub-step
0F1D: 34              INC     (HL)                ; step it on by one
0F1E: C9              RET                         

; the inner level of the two-level sequence machine for one outer mode:
; run the arm the LOW NIBBLE of the inner index selects out of a sixteen-
; word table laid inline just after this entry, then one fixed block; the
; arm returns through a slot this entry parks for it
dispatchSequenceSubStepArm:
0F1F: 21 54 0F        LD      HL,$0F54            ; the continuation to run once the arm returns
0F22: E5              PUSH    HL                  ; park it as the arm's return
0F23: 3A AC A9        LD      A,($A9AC)           ; {hard.workRam+1AC} take the sub-step
0F26: E6 0F           AND     $0F                 ; its low nibble picks the arm
0F28: F7              RST     $30                 ; jump into that arm through the inline table just past here

; ---- $0F29-$0F48: jump table ----
0F29: B1 27 5E 33 D7 5B 75 4C 74 07 AF 16 94 56 99 11
0F39: 0B 33 B4 08 C3 18 E2 12 FB 12 0F 4A 23 13 B5 15

; ---- $0F49-$0F53: data ----
0F49: 73 A6 14 7E 29 F8 96 5D 96 13 B9

; guarded tail of the phase-3 image-service step, reached as
; dispatchSequenceSubStepArm's pushed continuation: returns while the
; play-active flag (0xAD30) is set; on a nonzero credit count (0xA986) it
; zeroes the sequence sub-step (0xA9AC) and reloads the phase (0xA9AB)
; from the ROM constant at 0x1736; otherwise, only when the free-play flag
; (0xA9C0) is set and one of two input bits (0xA9AE & 0x18) is held, it
; zero-fills the work table 0x15b6 clears and tail-calls $1690
advanceAttractTowardGameStart:
0F54: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} read the play-active flag
0F57: A7              AND     A                   
0F58: C0              RET     NZ                  ; a game is running: nothing to do here
0F59: 3A 86 A9        LD      A,($A986)           ; {hard.workRam+186} read the credit count
0F5C: A7              AND     A                   
0F5D: 20 11           JR      NZ,$0F70            ; {code.loc_0f70} a credit is waiting: arm the start
0F5F: 3A C0 A9        LD      A,($A9C0)           ; {hard.workRam+1C0} read the free-play flag
0F62: A7              AND     A                   
0F63: C8              RET     Z                   ; not free play: nothing to start
0F64: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the control inputs
0F67: E6 18           AND     $18                 ; mask the two start buttons
0F69: C8              RET     Z                   ; neither held: wait
0F6A: CD B6 15        CALL    $15B6               ; {code.hideAllSprites} hide all the sprites
0F6D: C3 90 16        JP      $1690               ; {code.startGameOnFreePlay} start the free-play game

loc_0f70:
0F70: AF              XOR     A                   ; clear the sequence sub-step
0F71: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC}
0F74: 3A 36 17        LD      A,($1736)           ; {hard.rom+1736} take the "credit taken" phase from the program image
0F77: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} set the sequence phase to it
0F7A: C9              RET                         

; copy the four-byte record an index selects out of a fixed table and into
; the four cells that hold the difficulty settings in force; scaling the
; index by the record width is done as a BYTE, so an index of sixty-four
; or more selects a record a wider multiply would not
loadDifficultyRecord:
0F7B: 87              ADD     A,A                 ; double the index...
0F7C: 87              ADD     A,A                 ; ...and again: x4 for the four-byte record (kept to a byte, so index 64+ wraps onto a wrong record)
0F7D: 21 6A 18        LD      HL,$186A            ; point at the difficulty-record table
0F80: 11 D3 A9        LD      DE,$A9D3            ; point at the live difficulty settings
0F83: DF              RST     $18                 ; step to the selected record
0F84: ED A0           LDI                         ; copy the first setting byte
0F86: ED A0           LDI                         ; copy the second
0F88: ED A0           LDI                         ; copy the third
0F8A: ED A0           LDI                         ; copy the fourth
0F8C: C9              RET                         

loc_0f8d:
0F8D: F1              POP     AF                  
0F8E: 01 F1 02        LD      BC,$02F1            
0F91: F1              POP     AF                  
0F92: 03              INC     BC                  
0F93: F1              POP     AF                  
0F94: 04              INC     B                   
0F95: F1              POP     AF                  
0F96: 05              DEC     B                   

; scanline-gated sprite position fixup over 8 slots: for each slot whose Y
; byte (sprite bank 1) has bit 7 set and whose Y + scanline counter
; carries, clears bit 7 of that Y byte and toggles bit 7 of the paired X
; byte (sprite bank 0)
multiplexSpriteSlotsSkipping:
0F97: 3A 11 B4        LD      A,($B411)           ; read the first scenery slot's Y byte -- bit 7 marks a slot wanting a second image this frame
0F9A: CB 7F           BIT     7,A                 ; test that request bit
0F9C: 28 19           JR      Z,$0FB7             ; {code.loc_0fb7} clear -- move on to the next slot
0F9E: 4F              LD      C,A                 
0F9F: 3A 00 C0        LD      A,($C000)           ; read the live scanline counter
0FA2: 81              ADD     A,C                 ; add the slot's line -- carry once the beam has passed it
0FA3: 30 12           JR      NC,$0FB7            ; {code.loc_0fb7} beam not past yet -- leave this slot untouched this pass
0FA5: 23              INC     HL                  
0FA6: 23              INC     HL                  
0FA7: 2B              DEC     HL                  
0FA8: 2B              DEC     HL                  
0FA9: 79              LD      A,C                 
0FAA: E6 7F           AND     $7F                 ; clear bit 7 -- shifts the slot half a screen and clears its request
0FAC: 32 11 B4        LD      ($B411),A           ; store the moved Y byte
0FAF: 3A 10 B0        LD      A,($B010)           ; read the slot's paired X byte
0FB2: C6 80           ADD     A,$80               ; add half a screen across
0FB4: 32 10 B0        LD      ($B010),A           ; store it -- the same sprite draws again half a screen away, with no extra hardware slot

loc_0fb7:
0FB7: 3A 13 B4        LD      A,($B413)           ; read the next slot's Y byte
0FBA: CB 7F           BIT     7,A                 ; test its request bit
0FBC: 28 19           JR      Z,$0FD7             ; {code.loc_0fd7} clear -- next slot
0FBE: 4F              LD      C,A                 
0FBF: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
0FC2: 81              ADD     A,C                 ; carry once the beam is past this slot's line
0FC3: 30 12           JR      NC,$0FD7            ; {code.loc_0fd7} beam not past -- skip this slot this pass
0FC5: 23              INC     HL                  
0FC6: 23              INC     HL                  
0FC7: 2B              DEC     HL                  
0FC8: 2B              DEC     HL                  
0FC9: 79              LD      A,C                 
0FCA: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
0FCC: 32 13 B4        LD      ($B413),A           ; store the moved Y byte
0FCF: 3A 12 B0        LD      A,($B012)           ; read the paired X byte
0FD2: C6 80           ADD     A,$80               ; add half a screen across
0FD4: 32 12 B0        LD      ($B012),A           ; store it -- second image placed

loc_0fd7:
0FD7: 3A 15 B4        LD      A,($B415)           ; read the next slot's Y byte
0FDA: CB 7F           BIT     7,A                 ; test its request bit
0FDC: 28 19           JR      Z,$0FF7             ; {code.loc_0ff7} clear -- next slot
0FDE: 4F              LD      C,A                 
0FDF: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
0FE2: 81              ADD     A,C                 ; carry once the beam is past this slot's line
0FE3: 30 12           JR      NC,$0FF7            ; {code.loc_0ff7} beam not past -- skip this slot this pass
0FE5: 23              INC     HL                  
0FE6: 23              INC     HL                  
0FE7: 2B              DEC     HL                  
0FE8: 2B              DEC     HL                  
0FE9: 79              LD      A,C                 
0FEA: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
0FEC: 32 15 B4        LD      ($B415),A           ; store the moved Y byte
0FEF: 3A 14 B0        LD      A,($B014)           ; read the paired X byte
0FF2: C6 80           ADD     A,$80               ; add half a screen across
0FF4: 32 14 B0        LD      ($B014),A           ; store it -- second image placed

loc_0ff7:
0FF7: 3A 37 B4        LD      A,($B437)           ; read the next slot's Y byte
0FFA: CB 7F           BIT     7,A                 ; test its request bit
0FFC: 28 19           JR      Z,$1017             ; {code.loc_1017} clear -- next slot
0FFE: 4F              LD      C,A                 
0FFF: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1002: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1003: 30 12           JR      NC,$1017            ; {code.loc_1017} beam not past -- skip this slot this pass
1005: 23              INC     HL                  
1006: 23              INC     HL                  
1007: 2B              DEC     HL                  
1008: 2B              DEC     HL                  
1009: 79              LD      A,C                 
100A: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
100C: 32 37 B4        LD      ($B437),A           ; store the moved Y byte
100F: 3A 36 B0        LD      A,($B036)           ; read the paired X byte
1012: C6 80           ADD     A,$80               ; add half a screen across
1014: 32 36 B0        LD      ($B036),A           ; store it -- second image placed

loc_1017:
1017: 3A 39 B4        LD      A,($B439)           ; read the next slot's Y byte
101A: CB 7F           BIT     7,A                 ; test its request bit
101C: 28 19           JR      Z,$1037             ; {code.loc_1037} clear -- next slot
101E: 4F              LD      C,A                 
101F: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1022: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1023: 30 12           JR      NC,$1037            ; {code.loc_1037} beam not past -- skip this slot this pass
1025: 23              INC     HL                  
1026: 23              INC     HL                  
1027: 2B              DEC     HL                  
1028: 2B              DEC     HL                  
1029: 79              LD      A,C                 
102A: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
102C: 32 39 B4        LD      ($B439),A           ; store the moved Y byte
102F: 3A 38 B0        LD      A,($B038)           ; read the paired X byte
1032: C6 80           ADD     A,$80               ; add half a screen across
1034: 32 38 B0        LD      ($B038),A           ; store it -- second image placed

loc_1037:
1037: 3A 3B B4        LD      A,($B43B)           ; read the next slot's Y byte
103A: CB 7F           BIT     7,A                 ; test its request bit
103C: 28 19           JR      Z,$1057             ; {code.loc_1057} clear -- next slot
103E: 4F              LD      C,A                 
103F: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1042: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1043: 30 12           JR      NC,$1057            ; {code.loc_1057} beam not past -- skip this slot this pass
1045: 23              INC     HL                  
1046: 23              INC     HL                  
1047: 2B              DEC     HL                  
1048: 2B              DEC     HL                  
1049: 79              LD      A,C                 
104A: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
104C: 32 3B B4        LD      ($B43B),A           ; store the moved Y byte
104F: 3A 3A B0        LD      A,($B03A)           ; read the paired X byte
1052: C6 80           ADD     A,$80               ; add half a screen across
1054: 32 3A B0        LD      ($B03A),A           ; store it -- second image placed

loc_1057:
1057: 3A 3D B4        LD      A,($B43D)           ; read the next slot's Y byte
105A: CB 7F           BIT     7,A                 ; test its request bit
105C: 28 19           JR      Z,$1077             ; {code.loc_1077} clear -- next slot
105E: 4F              LD      C,A                 
105F: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1062: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1063: 30 12           JR      NC,$1077            ; {code.loc_1077} beam not past -- skip this slot this pass
1065: 23              INC     HL                  
1066: 23              INC     HL                  
1067: 2B              DEC     HL                  
1068: 2B              DEC     HL                  
1069: 79              LD      A,C                 
106A: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
106C: 32 3D B4        LD      ($B43D),A           ; store the moved Y byte
106F: 3A 3C B0        LD      A,($B03C)           ; read the paired X byte
1072: C6 80           ADD     A,$80               ; add half a screen across
1074: 32 3C B0        LD      ($B03C),A           ; store it -- second image placed

loc_1077:
1077: 3A 3F B4        LD      A,($B43F)           ; read the last slot's Y byte
107A: CB 7F           BIT     7,A                 ; test its request bit
107C: 28 19           JR      Z,$1097             ; {code.loc_1097} clear -- done
107E: 4F              LD      C,A                 
107F: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1082: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1083: 30 12           JR      NC,$1097            ; {code.loc_1097} beam not past -- skip this slot this pass
1085: 23              INC     HL                  
1086: 23              INC     HL                  
1087: 2B              DEC     HL                  
1088: 2B              DEC     HL                  
1089: 79              LD      A,C                 
108A: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
108C: 32 3F B4        LD      ($B43F),A           ; store the moved Y byte
108F: 3A 3E B0        LD      A,($B03E)           ; read the paired X byte
1092: C6 80           ADD     A,$80               ; add half a screen across
1094: 32 3E B0        LD      ($B03E),A           ; store it -- second image placed

loc_1097:
1097: C9              RET                         

; wait until the raster has passed each of eight scenery slots, then move
; that slot half a screen in both axes so the same sprite shows twice in
; one frame; a slot whose request bit is clear is left alone
multiplexSpriteSlots:
1098: 3A 11 B4        LD      A,($B411)           ; read the first scenery slot's Y byte -- this pass waits on the beam rather than skipping
109B: CB 7F           BIT     7,A                 ; test its request bit
109D: 28 19           JR      Z,$10B8             ; {code.loc_10b8} clear -- next slot
109F: 4F              LD      C,A                 
10A0: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
10A3: 81              ADD     A,C                 ; carry once the beam is past this slot's line
10A4: 30 F2           JR      NC,$1098            ; {code.multiplexSpriteSlots} beam not past -- hold here until it is
10A6: 23              INC     HL                  
10A7: 23              INC     HL                  
10A8: 2B              DEC     HL                  
10A9: 2B              DEC     HL                  
10AA: 79              LD      A,C                 
10AB: E6 7F           AND     $7F                 ; clear bit 7 -- shift the slot half a screen, clear its request
10AD: 32 11 B4        LD      ($B411),A           ; store the moved Y byte
10B0: 3A 10 B0        LD      A,($B010)           ; read the paired X byte
10B3: C6 80           ADD     A,$80               ; add half a screen across
10B5: 32 10 B0        LD      ($B010),A           ; store it -- second image placed

loc_10b8:
10B8: 3A 13 B4        LD      A,($B413)           ; read the next slot's Y byte
10BB: CB 7F           BIT     7,A                 ; test its request bit
10BD: 28 19           JR      Z,$10D8             ; {code.loc_10d8} clear -- next slot
10BF: 4F              LD      C,A                 
10C0: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
10C3: 81              ADD     A,C                 ; carry once the beam is past this slot's line
10C4: 30 F2           JR      NC,$10B8            ; {code.loc_10b8} beam not past -- hold here until it is
10C6: 23              INC     HL                  
10C7: 23              INC     HL                  
10C8: 2B              DEC     HL                  
10C9: 2B              DEC     HL                  
10CA: 79              LD      A,C                 
10CB: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
10CD: 32 13 B4        LD      ($B413),A           ; store the moved Y byte
10D0: 3A 12 B0        LD      A,($B012)           ; read the paired X byte
10D3: C6 80           ADD     A,$80               ; add half a screen across
10D5: 32 12 B0        LD      ($B012),A           ; store it -- second image placed

loc_10d8:
10D8: 3A 15 B4        LD      A,($B415)           ; read the next slot's Y byte
10DB: CB 7F           BIT     7,A                 ; test its request bit
10DD: 28 19           JR      Z,$10F8             ; {code.loc_10f8} clear -- next slot
10DF: 4F              LD      C,A                 
10E0: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
10E3: 81              ADD     A,C                 ; carry once the beam is past this slot's line
10E4: 30 F2           JR      NC,$10D8            ; {code.loc_10d8} beam not past -- hold here until it is
10E6: 23              INC     HL                  
10E7: 23              INC     HL                  
10E8: 2B              DEC     HL                  
10E9: 2B              DEC     HL                  
10EA: 79              LD      A,C                 
10EB: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
10ED: 32 15 B4        LD      ($B415),A           ; store the moved Y byte
10F0: 3A 14 B0        LD      A,($B014)           ; read the paired X byte
10F3: C6 80           ADD     A,$80               ; add half a screen across
10F5: 32 14 B0        LD      ($B014),A           ; store it -- second image placed

loc_10f8:
10F8: 3A 37 B4        LD      A,($B437)           ; read the next slot's Y byte
10FB: CB 7F           BIT     7,A                 ; test its request bit

; reused subroutine entry into the five-slot display-list split pass,
; joined inside the first slot: trades the first slot from the caller's
; held byte (or, below the raster line, restarts the whole pass and re-
; reads every slot from memory), then trades slots 2-5 wherever their top
; bit is set
spinRemainingSpriteMultiplexSlots:
10FD: 28 19           JR      Z,$1118             ; {code.loc_1118} clear -- skip ahead to the following slot
10FF: 4F              LD      C,A                 
1100: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1103: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1104: 30 F2           JR      NC,$10F8            ; {code.loc_10f8} still above the line -- restart the whole pass, re-reading every slot
1106: 23              INC     HL                  
1107: 23              INC     HL                  
1108: 2B              DEC     HL                  
1109: 2B              DEC     HL                  
110A: 79              LD      A,C                 
110B: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
110D: 32 37 B4        LD      ($B437),A           ; store the moved Y byte
1110: 3A 36 B0        LD      A,($B036)           ; read the paired X byte
1113: C6 80           ADD     A,$80               ; add half a screen across
1115: 32 36 B0        LD      ($B036),A           ; store it -- second image placed

loc_1118:
1118: 3A 39 B4        LD      A,($B439)           ; read the next slot's Y byte
111B: CB 7F           BIT     7,A                 ; test its request bit
111D: 28 19           JR      Z,$1138             ; {code.loc_1138} clear -- next slot
111F: 4F              LD      C,A                 
1120: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1123: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1124: 30 F2           JR      NC,$1118            ; {code.loc_1118} beam not past -- hold here until it is
1126: 23              INC     HL                  
1127: 23              INC     HL                  
1128: 2B              DEC     HL                  
1129: 2B              DEC     HL                  
112A: 79              LD      A,C                 
112B: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
112D: 32 39 B4        LD      ($B439),A           ; store the moved Y byte
1130: 3A 38 B0        LD      A,($B038)           ; read the paired X byte
1133: C6 80           ADD     A,$80               ; add half a screen across
1135: 32 38 B0        LD      ($B038),A           ; store it -- second image placed

loc_1138:
1138: 3A 3B B4        LD      A,($B43B)           ; read the next slot's Y byte
113B: CB 7F           BIT     7,A                 ; test its request bit
113D: 28 19           JR      Z,$1158             ; {code.loc_1158} clear -- next slot
113F: 4F              LD      C,A                 
1140: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1143: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1144: 30 F2           JR      NC,$1138            ; {code.loc_1138} beam not past -- hold here until it is
1146: 23              INC     HL                  
1147: 23              INC     HL                  
1148: 2B              DEC     HL                  
1149: 2B              DEC     HL                  
114A: 79              LD      A,C                 
114B: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
114D: 32 3B B4        LD      ($B43B),A           ; store the moved Y byte
1150: 3A 3A B0        LD      A,($B03A)           ; read the paired X byte
1153: C6 80           ADD     A,$80               ; add half a screen across
1155: 32 3A B0        LD      ($B03A),A           ; store it -- second image placed

loc_1158:
1158: 3A 3D B4        LD      A,($B43D)           ; read the next slot's Y byte
115B: CB 7F           BIT     7,A                 ; test its request bit
115D: 28 19           JR      Z,$1178             ; {code.loc_1178} clear -- next slot
115F: 4F              LD      C,A                 
1160: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1163: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1164: 30 F2           JR      NC,$1158            ; {code.loc_1158} beam not past -- hold here until it is
1166: 23              INC     HL                  
1167: 23              INC     HL                  
1168: 2B              DEC     HL                  
1169: 2B              DEC     HL                  
116A: 79              LD      A,C                 
116B: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
116D: 32 3D B4        LD      ($B43D),A           ; store the moved Y byte
1170: 3A 3C B0        LD      A,($B03C)           ; read the paired X byte
1173: C6 80           ADD     A,$80               ; add half a screen across
1175: 32 3C B0        LD      ($B03C),A           ; store it -- second image placed

loc_1178:
1178: 3A 3F B4        LD      A,($B43F)           ; read the last slot's Y byte
117B: CB 7F           BIT     7,A                 ; test its request bit
117D: 28 19           JR      Z,$1198             ; {code.loc_1198} clear -- done
117F: 4F              LD      C,A                 
1180: 3A 00 C0        LD      A,($C000)           ; read the scanline counter
1183: 81              ADD     A,C                 ; carry once the beam is past this slot's line
1184: 30 F2           JR      NC,$1178            ; {code.loc_1178} beam not past -- hold here until it is
1186: 23              INC     HL                  
1187: 23              INC     HL                  
1188: 2B              DEC     HL                  
1189: 2B              DEC     HL                  
118A: 79              LD      A,C                 
118B: E6 7F           AND     $7F                 ; clear bit 7 -- shift half a screen, clear the request
118D: 32 3F B4        LD      ($B43F),A           ; store the moved Y byte
1190: 3A 3E B0        LD      A,($B03E)           ; read the paired X byte
1193: C6 80           ADD     A,$80               ; add half a screen across
1195: 32 3E B0        LD      ($B03E),A           ; store it -- second image placed

loc_1198:
1198: C9              RET                         

; the round engine's service list (substep 7 of the phase-3 dispatch at
; 0x0f29; runs per dispatch, short of the frame count): run each subsystem
; service in fixed order, then read the player-state byte at 0xa800 and
; advance the round when it is 0xff (alive), hand a life over when it is 0
; (dead), else return
serviceRoundThenResolvePlayerState:
1199: CD B4 31        CALL    $31B4               ; {code.reaimAndAnimateEnemyCraftOnPhaseTick} re-aim and animate the enemy craft for this phase tick
119C: CD DF 1E        CALL    $1EDF               ; {code.dispatchPlayerFrameByState} update the player ship for this frame
119F: CD E3 23        CALL    $23E3               ; {code.fireAndSweepPlayerShots} fire and advance the player's shots
11A2: CD AF 36        CALL    $36AF               ; {code.driveEnemyWaveForLifePhase} drive the enemy wave for the current life phase
11A5: CD 97 0F        CALL    $0F97               ; {code.multiplexSpriteSlotsSkipping} run a sprite-doubling pass -- called repeatedly through the frame so scenery sprites redraw as the beam descends
11A8: CD B3 47        CALL    $47B3               ; {code.runParachutistSlot} run the parachutist
11AB: CD B7 43        CALL    $43B7               ; {code.armMotherShipOrStep} arm or step the mother ship
11AE: CD A1 28        CALL    $28A1               ; {code.stepSevenCraftSlots} step the seven enemy-craft slots
11B1: CD 97 0F        CALL    $0F97               ; {code.multiplexSpriteSlotsSkipping} another sprite-doubling pass
11B4: CD BC 2C        CALL    $2CBC               ; {code.runSceneryForEra} draw the scenery for the current era
11B7: CD D6 40        CALL    $40D6               ; {code.sweepEra2PlusObjectBank} sweep the era-2-and-up object bank
11BA: CD 97 0F        CALL    $0F97               ; {code.multiplexSpriteSlotsSkipping} another sprite-doubling pass
11BD: CD 5F 3B        CALL    $3B5F               ; {code.serviceEra1BomberObject} service the era-1 bomber
11C0: CD DA 3D        CALL    $3DDA               ; {code.serviceFixedSlotInEra1} service the era-1 fixed object slot
11C3: CD 36 3E        CALL    $3E36               ; {code.stepFourActorSlots} step the four actor slots
11C6: CD 97 0F        CALL    $0F97               ; {code.multiplexSpriteSlotsSkipping} another sprite-doubling pass
11C9: CD EA 3F        CALL    $3FEA               ; {code.serviceEra0BallisticObjectBank} service the era-0 ballistic object bank
11CC: CD 4F 4E        CALL    $4E4F               ; {code.dispatchCollisionPassByEra} run the collision pass for this era
11CF: CD B8 40        CALL    $40B8               ; {code.askForSoundWhileTheGroupIsClear} ask for a sound while the formation is clear
11D2: CD 97 0F        CALL    $0F97               ; {code.multiplexSpriteSlotsSkipping} another sprite-doubling pass
11D5: CD DE 4D        CALL    $4DDE               ; {code.awardBonusLifeAtScoreMark} grant a bonus life at the score mark
11D8: CD 05 52        CALL    $5205               ; {code.expireHitChain} expire the hit chain
11DB: CD 3A 4D        CALL    $4D3A               ; {code.escalateDifficultyRungOnCounterWrap} step difficulty up when the counter wraps
11DE: CD 09 08        CALL    $0809               ; {code.drawKillMeter} repaint the kill meter
11E1: CD 98 10        CALL    $1098               ; {code.multiplexSpriteSlots} a final sprite-doubling pass (the variant that waits on the beam)
11E4: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player-state byte
11E7: 3C              INC     A                   ; 0xFF (still alive) rolls to zero here
11E8: CA 71 12        JP      Z,$1271             ; {code.advanceRoundWhenFieldCleared} alive -- advance the round once the field is cleared
11EB: 3D              DEC     A                   ; back to the raw state -- zero flags a dead player
11EC: C0              RET     NZ                  ; neither alive nor dead -- nothing to resolve, return

; process a player's death: hide the sprite band, apply a pending round-
; advance when its flag is set, and queue the frame's fixed sound
; requests; then decrement LIVES_REMAINING at the head of the live 16-byte
; context block and checkpoint that block into the active player's save
; slot — on lives reaching zero it tail-calls the game-over banner,
; otherwise, when the other player's saved block still shows lives, it
; flips the active-player index, arms a delay and re-steps the sequence
; for the next life
loseLifeAndHandOver:
11ED: CD B6 15        CALL    $15B6               ; {code.hideAllSprites} blank the whole sprite band
11F0: 3A C6 AC        LD      A,($ACC6)           ; {hard.workRam+4C6} read the pending round-advance flag
11F3: A7              AND     A                   ; is it set?
11F4: C4 B8 2D        CALL    NZ,$2DB8            ; {code.startNextRound} set -- start the next round
11F7: CD 34 56        CALL    $5634               ; {code.enqueueTransitionSoundBurst} queue this frame's fixed sound requests
11FA: 21 00 AD        LD      HL,$AD00            ; point at the live context block -- its first byte is the lives count
11FD: 35              DEC     (HL)                ; drop the lives count by one
11FE: F5              PUSH    AF                  ; remember whether that reached zero
11FF: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player selector
1202: A7              AND     A                   ; which player is up?
1203: 11 10 AD        LD      DE,$AD10            ; default the save slot to player 1's
1206: 28 03           JR      Z,$120B             ; {code.loc_120b} player 1 -- keep it
1208: 11 20 AD        LD      DE,$AD20            ; player 2 -- use the other save slot

loc_120b:
120B: 21 00 AD        LD      HL,$AD00            ; source is the live context block
120E: 01 10 00        LD      BC,$0010            ; sixteen bytes
1211: ED B0           LDIR                        ; checkpoint the live block into the active player's save slot
1213: F1              POP     AF                  ; recall whether lives hit zero
1214: 28 3D           JR      Z,$1253             ; {code.postGameOverBanner} out of lives -- go post the game-over banner
1216: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player selector again
1219: A7              AND     A                   ; which player is up?
121A: 21 20 AD        LD      HL,$AD20            ; point at player 2's save slot
121D: 28 03           JR      Z,$1222             ; {code.loc_1222} player 1 up -- the other player is player 2
121F: 21 10 AD        LD      HL,$AD10            ; player 2 up -- the other player is player 1

loc_1222:
1222: 7E              LD      A,(HL)              ; read the other player's saved lives count
1223: A7              AND     A                   ; does the other player still have lives?
1224: 28 09           JR      Z,$122F             ; {code.loc_122f} no -- skip the flip and just re-arm the delay

; give the turn to the other player: flip the one-bit active-player index,
; re-arm the shared sequence delay with a fixed span, and reseat the inner
; sequence index from a byte of the program image; nothing is copied here,
; and the flip is the only effect the skipped arm does not also have
handPlayOverToOtherPlayer:
1226: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player selector
1229: 3C              INC     A                   ; flip it...
122A: E6 01           AND     $01                 ; ...to the other player (one-bit index)
122C: 32 32 AD        LD      ($AD32),A           ; {hard.workRam+532} store the new active player -- this flip is the hand-over itself

loc_122f:
122F: 3E 5A           LD      A,$5A               ; hold value 90...
1231: 32 EB A9        LD      ($A9EB),A           ; {hard.workRam+1EB} ...into the shared sequence delay
1234: 3A 52 4B        LD      A,($4B52)           ; {hard.rom+4B52} take the inner sequence step from the program image
1237: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} reseat the inner sequence step for the next life
123A: C9              RET                         

; ---- $123B-$1252: data ----
123B: 18 A7 13 A5 3B 87 F1 34 0E 34 D7 BF F1 7F 13 13
124B: 13 13 F1 88 DC ED 11 B9

; the last life is gone: queue the PLAYER-n caption and the GAME OVER
; caption, hold them for three seconds and step the sequence on; when no
; game is running it branches instead into the shared teardown
; restartAttractSequence, which hands the machine back to attract
postGameOverBanner:
1253: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} read the in-play flag
1256: A7              AND     A                   ; is a game running?
1257: CA FB 12        JP      Z,$12FB             ; {code.restartAttractSequence} not running -- hand the machine back to attract
125A: 11 09 02        LD      DE,$0209            ; caption command 2, argument 9 -- the PLAYER 1 banner
125D: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player selector
1260: A7              AND     A                   ; player 1 or 2?
1261: 28 01           JR      Z,$1264             ; {code.loc_1264} player 1 -- keep argument 9
1263: 1C              INC     E                   ; player 2 -- bump the argument to 10 (PLAYER 2)

loc_1264:
1264: FF              RST     $38                 ; queue that PLAYER-n banner command
1265: 11 0B 0A        LD      DE,$0A0B            ; caption command 10, argument 11 -- the GAME OVER banner
1268: FF              RST     $38                 ; queue the GAME OVER banner command
1269: 3E B4           LD      A,$B4               ; hold value 180 (about three seconds)...
126B: 32 EB A9        LD      ($A9EB),A           ; {hard.workRam+1EB} ...into the sequence delay, holding the banners on screen
126E: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence on

; gated two-arm state transition: fires only when 0xad02=0, 0xacc6!=0 and
; all 15 slots at 0xa810 are empty, then queues the fixed sound set and
; runs one of two arms on 0xad30 — disarm+reset a cell cluster, or clear a
; strided run and copy a 16-byte record into 0xad10/0xad20
advanceRoundWhenFieldCleared:
1271: 3A 02 AD        LD      A,($AD02)           ; {hard.workRam+502} read the round-advance guard cell
1274: A7              AND     A                   ; is it clear?
1275: C0              RET     NZ                  ; not clear -- do nothing
1276: 3A C6 AC        LD      A,($ACC6)           ; {hard.workRam+4C6} read the round-advance arm
1279: A7              AND     A                   ; is it armed?
127A: C8              RET     Z                   ; not armed -- do nothing
127B: 21 10 A8        LD      HL,$A810            ; point at the first of fifteen object slots
127E: 11 10 00        LD      DE,$0010            ; sixteen bytes per slot
1281: 06 0F           LD      B,$0F               ; fifteen slots to check

loc_1283:
1283: 7E              LD      A,(HL)              ; read this slot's head byte
1284: A7              AND     A                   ; is the slot empty?
1285: C0              RET     NZ                  ; a slot is still occupied -- the field isn't clear, return
1286: 19              ADD     HL,DE               
1287: 10 FA           DJNZ    $1283               ; {code.loc_1283} check every one of the fifteen slots
1289: CD 34 56        CALL    $5634               ; {code.enqueueTransitionSoundBurst} queue this frame's fixed sound requests
128C: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} read the in-play flag
128F: A7              AND     A                   ; is a game running?
1290: 28 29           JR      Z,$12BB             ; {code.loc_12bb} attract mode -- take the reset arm
1292: 21 43 AA        LD      HL,$AA43            ; point at a strided run of cells
1295: 06 17           LD      B,$17               ; twenty-three of them
1297: AF              XOR     A                   ; the zero to write

loc_1298:
1298: 77              LD      (HL),A              ; zero every other cell along the run
1299: 2C              INC     L                   
129A: 2C              INC     L                   
129B: 10 FB           DJNZ    $1298               ; {code.loc_1298} clear all twenty-three
129D: CD B8 2D        CALL    $2DB8               ; {code.startNextRound} start the next round
12A0: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player selector
12A3: A7              AND     A                   ; which player is up?
12A4: 11 10 AD        LD      DE,$AD10            ; default the save slot to player 1's
12A7: 28 03           JR      Z,$12AC             ; {code.loc_12ac} player 1 -- keep it
12A9: 11 20 AD        LD      DE,$AD20            ; player 2 -- use the other save slot

loc_12ac:
12AC: 21 00 AD        LD      HL,$AD00            ; source is the live context block
12AF: 01 10 00        LD      BC,$0010            ; sixteen bytes
12B2: ED B0           LDIR                        ; checkpoint the live block into the player's save slot
12B4: 3A 35 4A        LD      A,($4A35)           ; {hard.rom+4A35} take the inner sequence step from the program image
12B7: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} reseat the inner sequence step
12BA: C9              RET                         

loc_12bb:
12BB: 3A D1 07        LD      A,($07D1)           ; {hard.rom+7D1} take the round-advance arm value from the program image
12BE: 32 C6 AC        LD      ($ACC6),A           ; {hard.workRam+4C6} re-arm the round-advance flag
12C1: CD B6 15        CALL    $15B6               ; {code.hideAllSprites} blank the whole sprite band
12C4: C3 FB 12        JP      $12FB               ; {code.restartAttractSequence} hand the machine back to attract

; ---- $12C7-$12E1: data ----
12C7: 74 B1 CC EC 5C 16 39 50 67 21 7A C5 F7 BE 54 80
12D7: 2F 5F 9F 6D 44 B8 E7 BD 89 59 1A

loc_12e2:
12E2: 21 EB A9        LD      HL,$A9EB            ; point at the sequence delay counter
12E5: 35              DEC     (HL)                ; tick it down one
12E6: C0              RET     NZ                  ; still counting -- return; at zero it falls through into the turn-pass logic

; hand the turn over to the other player when that player's saved lives
; count is non-zero, and otherwise step the inner sequence index; both
; exits are tails, so this entry chooses between two continuations rather
; than returning to anything
passTurnToOtherPlayerIfLivesElseStepSequence:
12E7: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player selector
12EA: A7              AND     A                   ; which player is up?
12EB: 21 20 AD        LD      HL,$AD20            ; point at player 2's saved block
12EE: 28 03           JR      Z,$12F3             ; {code.loc_12f3} player 1 up -- the other is player 2
12F0: 21 10 AD        LD      HL,$AD10            ; player 2 up -- the other is player 1

loc_12f3:
12F3: 7E              LD      A,(HL)              ; read the other player's saved lives count
12F4: A7              AND     A                   ; does the other player still have lives?
12F5: C2 26 12        JP      NZ,$1226            ; {code.handPlayOverToOtherPlayer} yes -- hand the turn to the other player
12F8: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} no -- just step the inner sequence step on

; put the machine back at the top of the attract sequence: clear the play
; flag, the active-player index and the inner sequence step, then set the
; outer phase from a byte of the program image, and write the inner step a
; SECOND time through a fold over three more image bytes -- on an
; unaltered image that fold comes to zero and agrees with the first write,
; on an altered one it does not and the sequence restarts at some other
; step
restartAttractSequence:
12FB: AF              XOR     A                   ; clear A
12FC: 32 30 AD        LD      ($AD30),A           ; {hard.workRam+530} clear the in-play flag
12FF: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} clear the inner sequence step
1302: 32 32 AD        LD      ($AD32),A           ; {hard.workRam+532} clear the active-player index
1305: 3A D3 16        LD      A,($16D3)           ; {hard.rom+16D3} take the outer sequence phase from the program image
1308: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} set the outer sequence phase -- top of attract
130B: 3A 01 49        LD      A,($4901)           ; {hard.rom+4901} read a program-image byte as a signed offset
130E: 2A 02 49        LD      HL,($4902)          ; {hard.rom+4902} read a program-image address
1311: DF              RST     $18                 ; step that address by the signed offset
1312: AC              XOR     H                   ; fold the stepped address's high byte into the offset byte
1313: D6 9B           SUB     $9B                 ; subtract the bias -- on an untouched image this comes out zero
1315: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} write the inner step a second time -- agrees with the clear on an intact ROM, diverges if it was altered
1318: C9              RET                         

; fill a fixed-length run of character cells with one byte, stepping a
; cell at a time along the line
fillCellRun:
1319: 11 E0 FF        LD      DE,$FFE0            ; step of -32 -- one cell up the column per write
131C: 06 0D           LD      B,$0D               ; thirteen cells to fill

loc_131e:
131E: 77              LD      (HL),A              ; write the fill byte into this cell
131F: 19              ADD     HL,DE               ; back up one native row (32 cells)
1320: 10 FC           DJNZ    $131E               ; {code.loc_131e} fill all thirteen
1322: C9              RET                         

; phase-14 arm of the sequence dispatchSequenceSubStepArm dispatches off
; the 0x0F29 table (keyed on SEQUENCE_SUBSTEP & 0x0F): only on alternate
; frames (bit 1 of FRAME_TICK clear), dispatch on the animation sub-step
; at 0xA9F0 -- steps 0/1 flash the player ship and advance a scripted
; char-plane animation, steps 2/3 tick a two-colour animation and run a
; title-plane pass, step 4 floods the colour plane; the final step sets
; SEQUENCE_DELAY, hides every sprite, sets up the active player's turn
; (loadActivePlayerContextAndPostRoundHud) and reloads SEQUENCE_SUBSTEP
; from ROM byte 0x2750 (=3) to wind the outer sequence on
stepRoundStartIntroAnimation:
1323: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame tick
1326: E6 02           AND     $02                 ; act only on alternate frames (bit 1)
1328: C0              RET     NZ                  ; odd frame -- skip this frame
1329: 3A F0 A9        LD      A,($A9F0)           ; {hard.workRam+1F0} read the intro-animation step
132C: A7              AND     A                   ; step 0?
132D: 20 04           JR      NZ,$1333            ; {code.loc_1333} not step 0 -- try the next arm
132F: CD 67 13        CALL    $1367               ; {code.flashPlayerWhiteEveryOtherFrame} step 0 -- flash the player ship white
1332: C9              RET                         

loc_1333:
1333: 3D              DEC     A                   ; step 1?
1334: 20 07           JR      NZ,$133D            ; {code.loc_133d} no -- next arm
1336: CD 67 13        CALL    $1367               ; {code.flashPlayerWhiteEveryOtherFrame} flash the player ship white
1339: CD 2A 14        CALL    $142A               ; {code.advanceScriptedCharPlaneBandTo2} advance the character-plane band animation toward stage 2
133C: C9              RET                         

loc_133d:
133D: 3D              DEC     A                   ; step 2?
133E: 20 07           JR      NZ,$1347            ; {code.loc_1347} no -- next arm
1340: CD 93 13        CALL    $1393               ; {code.cyclePlayerSpriteColourThenAdvanceStepAtZero} cycle the player ship's colour
1343: CD C5 14        CALL    $14C5               ; {code.advanceScriptedCharPlaneBandTo4} advance the character-plane band animation toward stage 4
1346: C9              RET                         

loc_1347:
1347: 3D              DEC     A                   ; step 3?
1348: 20 04           JR      NZ,$134E            ; {code.loc_134e} no -- next arm
134A: CD C5 14        CALL    $14C5               ; {code.advanceScriptedCharPlaneBandTo4} advance the character-plane band animation toward stage 4
134D: C9              RET                         

loc_134e:
134E: 3D              DEC     A                   ; step 4?
134F: 20 04           JR      NZ,$1355            ; {code.loc_1355} no -- final arm
1351: CD CC 13        CALL    $13CC               ; {code.floodColourPlaneWithSavedPlayerColour} flood the colour plane with the player's saved colour
1354: C9              RET                         

loc_1355:
1355: 3E 5A           LD      A,$5A               ; hold value 90...
1357: 32 EB A9        LD      ($A9EB),A           ; {hard.workRam+1EB} ...into the sequence delay
135A: CD B6 15        CALL    $15B6               ; {code.hideAllSprites} blank the whole sprite band
135D: CD 75 4C        CALL    $4C75               ; {code.loadActivePlayerContextAndPostRoundHud} set up the active player's turn and post the round HUD
1360: 3A 50 27        LD      A,($2750)           ; {hard.rom+2750} take the sub-step reload from the program image (= 3)
1363: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} reseat the inner sequence step, winding the outer sequence on
1366: C9              RET                         

; one frame of the flash that runs the player's ship white and back: the
; two flip bits of the player's sprite control byte are kept and the
; colour under them is driven from the low bit of the animation's own
; tick, alternating between the all-white palette entry and the colour the
; ship normally wears; the tick is stepped last and wraps at eight bits,
; and on the single tick where it reads the threshold the routine also
; hands the animation on to its next step and asks for one sound
flashPlayerWhiteEveryOtherFrame:
1367: 3A F1 A9        LD      A,($A9F1)           ; {hard.workRam+1F1} read this flash animation's tick counter
136A: FE 08           CP      $08                 ; has it reached eight?
136C: 20 08           JR      NZ,$1376            ; {code.loc_1376} not yet -- just recolour
136E: 3E 01           LD      A,$01               ; value 1...
1370: 32 F0 A9        LD      ($A9F0),A           ; {hard.workRam+1F0} ...into the intro-animation step -- move it on
1373: CD 11 58        CALL    $5811               ; {code.requestPlayerSpawnFlashSound} ask for the player-spawn flash sound

loc_1376:
1376: 3A F1 A9        LD      A,($A9F1)           ; {hard.workRam+1F1} read the tick again
1379: E6 01           AND     $01                 ; take its low bit
137B: 3E 3E           LD      A,$3E               ; default colour 0x3E -- the ship's normal colour
137D: 28 02           JR      Z,$1381             ; {code.loc_1381} even tick -- keep it
137F: 3E 00           LD      A,$00               ; odd tick -- colour 0 (all white)

loc_1381:
1381: 47              LD      B,A                 ; hold the chosen colour
1382: 3A 40 AA        LD      A,($AA40)           ; {hard.workRam+240} read the player ship's sprite attribute
1385: E6 C0           AND     $C0                 ; keep only its two mirroring bits
1387: 80              ADD     A,B                 ; merge in the chosen colour
1388: 32 40 AA        LD      ($AA40),A           ; {hard.workRam+240} write it back -- flips the ship white and back
138B: 3A F1 A9        LD      A,($A9F1)           ; {hard.workRam+1F1} read the tick
138E: 3C              INC     A                   ; step it
138F: 32 F1 A9        LD      ($A9F1),A           ; {hard.workRam+1F1} store it -- wraps at eight bits
1392: C9              RET                         

; one tick of a two-colour animation inside the round engine's step-14
; sub-sequence: step a count down by one and, from a single bit of that
; count, drive the colour field of the shadow byte that the sprite
; publisher copies into the player ship's sprite attribute, so a colour
; holds for four consecutive ticks; the top two bits of that byte, which
; carry the sprite's mirroring, are left alone. The tick that finds the
; count already at zero also moves the sub-sequence's step cell on to 3,
; and the count still steps on that tick, wrapping below zero. Its one
; call site is that sub-sequence's step 2, which follows it with one other
; routine
cyclePlayerSpriteColourThenAdvanceStepAtZero:
1393: 3A F3 A9        LD      A,($A9F3)           ; {hard.workRam+1F3} read the ship-colour cycle countdown
1396: A7              AND     A                   ; is the countdown already at zero?
1397: 20 09           JR      NZ,$13A2            ; {code.loc_13a2} not yet -- pick a colour from the count
1399: 3E 03           LD      A,$03               ; value 3...
139B: 32 F0 A9        LD      ($A9F0),A           ; {hard.workRam+1F0} ...into the intro-animation step -- countdown spent, move on to step 3
139E: 3E 3F           LD      A,$3F               ; use colour 0x3F
13A0: 18 18           JR      $13BA               ; {code.loc_13ba} go apply it

loc_13a2:
13A2: E6 04           AND     $04                 ; test bit 2 of the count -- a colour holds for four ticks
13A4: 20 04           JR      NZ,$13AA            ; {code.loc_13aa} bit set -- take the alternate colour
13A6: 3E 3F           LD      A,$3F               ; bit clear -- colour 0x3F
13A8: 18 10           JR      $13BA               ; {code.loc_13ba} apply it

loc_13aa:
13AA: 3D              DEC     A                   ; walk the selector toward the alternate colour
13AB: 20 04           JR      NZ,$13B1            ; {code.loc_13b1} branch on
13AD: 3E 36           LD      A,$36               ; colour 0x36 -- an arm this path never reaches
13AF: 18 09           JR      $13BA               ; {code.loc_13ba} apply it

loc_13b1:
13B1: 3D              DEC     A                   ; walk the selector on
13B2: 20 04           JR      NZ,$13B8            ; {code.loc_13b8} branch on
13B4: 3E 3E           LD      A,$3E               ; colour 0x3E -- also unreached on this path
13B6: 18 02           JR      $13BA               ; {code.loc_13ba} apply it

loc_13b8:
13B8: 3E 37           LD      A,$37               ; the alternate colour 0x37

loc_13ba:
13BA: 47              LD      B,A                 ; hold the chosen colour
13BB: 3A 40 AA        LD      A,($AA40)           ; {hard.workRam+240} read the player ship's sprite attribute
13BE: E6 C0           AND     $C0                 ; keep only the two mirroring bits
13C0: 80              ADD     A,B                 ; merge in the colour
13C1: 32 40 AA        LD      ($AA40),A           ; {hard.workRam+240} write it back -- recolours the ship
13C4: 3A F3 A9        LD      A,($A9F3)           ; {hard.workRam+1F3} read the countdown
13C7: 3D              DEC     A                   ; step it down (wraps below zero)
13C8: 32 F3 A9        LD      ($A9F3),A           ; {hard.workRam+1F3} store it
13CB: C9              RET                         

; the step-4 arm of the round engine's step-14 sub-sequence: flood a fixed
; block of the colour plane with one byte, and hand the sub-sequence the
; step whose arm winds it up. The byte comes from one of two parallel
; cells — the same offset in each of the two per-player save blocks —
; chosen by the active-player index, so it is a saved value rather than
; the live one. The block is twenty-eight rows of twenty-seven cells:
; every row the driver leaves visible, and all but five of the plane's
; thirty-two columns. When the picture is turned round the painting runs
; from the far corner backwards, which changes the ORDER the cells are
; touched in and not WHICH, so the two directions leave the plane
; identical. A separate count is stepped down by one on the way out
floodColourPlaneWithSavedPlayerColour:
13CC: 3E 05           LD      A,$05               ; value 5...
13CE: 32 F0 A9        LD      ($A9F0),A           ; {hard.workRam+1F0} ...into the intro-animation step -- move on to step 5
13D1: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player selector
13D4: A7              AND     A                   ; which player is up?
13D5: 3A 1C AD        LD      A,($AD1C)           ; {hard.workRam+51C} read player 1's saved pen colour
13D8: 47              LD      B,A                 ; hold it as the flood colour
13D9: 28 04           JR      Z,$13DF             ; {code.loc_13df} player 1 -- use it
13DB: 3A 2C AD        LD      A,($AD2C)           ; {hard.workRam+52C} player 2 -- read player 2's saved pen colour
13DE: 47              LD      B,A                 ; hold it instead

loc_13df:
13DF: 3A 87 A9        LD      A,($A987)           ; {hard.workRam+187} read the screen-orientation flag
13E2: A7              AND     A                   ; is the screen turned round?
13E3: 78              LD      A,B                 ; put the flood colour in A
13E4: 28 22           JR      Z,$1408             ; {code.loc_1408} turned round -- paint from the far corner backwards
13E6: 21 44 A0        LD      HL,$A044            ; forward: first cell of the colour-plane rectangle
13E9: 11 45 A0        LD      DE,$A045            ; copy destination one cell along
13EC: D9              EXX                         
13ED: 06 1C           LD      B,$1C               ; twenty-eight rows

loc_13ef:
13EF: D9              EXX                         
13F0: 01 1A 00        LD      BC,$001A            ; twenty-six trailing copies per row
13F3: 77              LD      (HL),A              ; paint the row's first cell
13F4: ED B0           LDIR                        ; flood the rest of the row with the same colour
13F6: 11 06 00        LD      DE,$0006            ; skip forward six cells...
13F9: 19              ADD     HL,DE               ; ...to the start of the next row (27 painted, 32-cell stride)
13FA: 54              LD      D,H                 
13FB: 5D              LD      E,L                 
13FC: 13              INC     DE                  
13FD: D9              EXX                         
13FE: 10 EF           DJNZ    $13EF               ; {code.loc_13ef} paint all twenty-eight rows
1400: 3A F6 A9        LD      A,($A9F6)           ; {hard.workRam+1F6} read the flood countdown
1403: 3D              DEC     A                   ; step it down
1404: 32 F6 A9        LD      ($A9F6),A           ; {hard.workRam+1F6} store it
1407: C9              RET                         

loc_1408:
1408: 21 BE A3        LD      HL,$A3BE            ; backwards: last cell of the rectangle
140B: 11 BD A3        LD      DE,$A3BD            ; copy destination one cell back
140E: D9              EXX                         
140F: 06 1C           LD      B,$1C               ; twenty-eight rows

loc_1411:
1411: D9              EXX                         
1412: 01 1A 00        LD      BC,$001A            ; twenty-six trailing copies per row
1415: 77              LD      (HL),A              ; paint the row's cell
1416: ED B8           LDDR                        ; flood the rest of the row backwards with the same colour
1418: 11 FA FF        LD      DE,$FFFA            ; step back six cells...
141B: 19              ADD     HL,DE               ; ...to the previous row
141C: 54              LD      D,H                 
141D: 5D              LD      E,L                 
141E: 1B              DEC     DE                  
141F: D9              EXX                         
1420: 10 EF           DJNZ    $1411               ; {code.loc_1411} paint all twenty-eight rows
1422: 3A F6 A9        LD      A,($A9F6)           ; {hard.workRam+1F6} read the flood countdown
1425: 3D              DEC     A                   ; step it down
1426: 32 F6 A9        LD      ($A9F6),A           ; {hard.workRam+1F6} store it
1429: C9              RET                         

; advance one frame of a script-driven character-plane animation: bit 0 of
; a countdown cell alternates a blanking pass (fill two thirteen-cell
; columns and six lead cells with one tile code) with a drawing pass
; (restore the working column from its saved run, nudge four counters by
; the low bit of the next two script bytes, step the band up then back
; down, and gather the column back); a terminator byte instead clears the
; countdown, arms the next sequence step and rewinds the script pointer
; one, ending early, and every non-terminating call then decrements the
; countdown
advanceScriptedCharPlaneBandTo2:
142A: 3A F2 A9        LD      A,($A9F2)           ; {hard.workRam+1F2} read the pass countdown
142D: CB 47           BIT     0,A                 ; which pass -- odd draws, even blanks
142F: 28 6C           JR      Z,$149D             ; {code.loc_149d} even -- go blank the band
1431: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} load the script cursor
1434: 7E              LD      A,(HL)              ; read the byte under it
1435: FE FF           CP      $FF                 ; end-of-script marker (0xFF)?
1437: 20 12           JR      NZ,$144B            ; {code.loc_144b} no -- draw this frame
1439: 3E 00           LD      A,$00               ; value 0...
143B: 32 F2 A9        LD      ($A9F2),A           ; {hard.workRam+1F2} ...clears the pass countdown -- script done
143E: 3E 02           LD      A,$02               ; value 2...
1440: 32 F0 A9        LD      ($A9F0),A           ; {hard.workRam+1F0} ...into the intro-animation step -- advance to stage 2
1443: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} reload the script cursor
1446: 2B              DEC     HL                  ; step it back one
1447: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} save it -- ending early with no decrement
144A: C9              RET                         

loc_144b:
144B: CD 63 15        CALL    $1563               ; {code.restoreColumnFromSavedRun} restore the working column from its saved run
144E: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} load the script cursor
1451: 7E              LD      A,(HL)              ; read the next script byte
1452: E6 01           AND     $01                 ; take its low bit
1454: 23              INC     HL                  
1455: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} step the cursor past it
1458: 28 0F           JR      Z,$1469             ; {code.loc_1469} bit clear -- skip this nudge
145A: 11 20 00        LD      DE,$0020            ; row stride 32
145D: 21 F0 A5        LD      HL,$A5F0            ; point at the column's top counter
1460: 34              INC     (HL)                ; nudge it up
1461: 19              ADD     HL,DE               
1462: 34              INC     (HL)                ; nudge the counter one row below
1463: 21 F2 A5        LD      HL,$A5F2            ; point at another column counter
1466: 34              INC     (HL)                ; nudge it up
1467: 19              ADD     HL,DE               
1468: 34              INC     (HL)                ; nudge the counter one row below

loc_1469:
1469: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} load the cursor
146C: 7E              LD      A,(HL)              ; read the next script byte
146D: E6 01           AND     $01                 ; take its low bit
146F: 23              INC     HL                  
1470: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} step the cursor past it
1473: 28 09           JR      Z,$147E             ; {code.loc_147e} bit clear -- skip this nudge
1475: 11 20 00        LD      DE,$0020            ; row stride 32
1478: 21 F1 A5        LD      HL,$A5F1            ; point at a column counter
147B: 34              INC     (HL)                ; nudge it up
147C: 19              ADD     HL,DE               
147D: 34              INC     (HL)                ; nudge the counter one row below

loc_147e:
147E: 0E 02           LD      C,$02               ; colour set 2
1480: 11 D1 A5        LD      DE,$A5D1            ; column of glyph cells
1483: CD 9D 4A        CALL    $4A9D               ; {code.stepThirteenScriptedGlyphCells} advance thirteen scripted glyph cells down the column
1486: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} load the cursor
1489: 11 F3 FF        LD      DE,$FFF3            ; step of -13...
148C: 19              ADD     HL,DE               ; ...rewind the cursor thirteen bytes
148D: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} save it
1490: 0E 00           LD      C,$00               ; colour set 0
1492: 11 31 A6        LD      DE,$A631            ; the same column in the other plane
1495: CD 9D 4A        CALL    $4A9D               ; {code.stepThirteenScriptedGlyphCells} advance those thirteen glyph cells in the other plane
1498: CD 8C 15        CALL    $158C               ; {code.gatherCharColumnIntoBackingRun} gather the column back into its saved run
149B: 18 20           JR      $14BD               ; {code.loc_14bd} on to the decrement

loc_149d:
149D: 3E F1           LD      A,$F1               ; the blank tile
149F: 21 B1 A7        LD      HL,$A7B1            ; first column to blank
14A2: CD 19 13        CALL    $1319               ; {code.fillCellRun} blank that thirteen-cell column
14A5: 21 D1 A5        LD      HL,$A5D1            ; second column to blank
14A8: CD 19 13        CALL    $1319               ; {code.fillCellRun} blank it too
14AB: 21 10 A6        LD      HL,$A610            ; point at a lead cell
14AE: 77              LD      (HL),A              ; blank it
14AF: 19              ADD     HL,DE               
14B0: 77              LD      (HL),A              ; blank the cell one row above it
14B1: 21 11 A6        LD      HL,$A611            ; next lead cell
14B4: 77              LD      (HL),A              ; blank it
14B5: 19              ADD     HL,DE               
14B6: 77              LD      (HL),A              ; blank the cell one row above it
14B7: 21 12 A6        LD      HL,$A612            ; last lead cell
14BA: 77              LD      (HL),A              ; blank it
14BB: 19              ADD     HL,DE               
14BC: 77              LD      (HL),A              ; blank the cell one row above it

loc_14bd:
14BD: 3A F2 A9        LD      A,($A9F2)           ; {hard.workRam+1F2} read the pass countdown
14C0: 3D              DEC     A                   ; step it down
14C1: 32 F2 A9        LD      ($A9F2),A           ; {hard.workRam+1F2} store it
14C4: C9              RET                         

; one pass of a cursor-scripted character-plane animation that runs during
; the inter-round / player-change transition — NOT the title (the title
; logo is a caption strip, and this arm is dispatched only from the life-
; loss / round-advance path and is reach-0 across attract): erases two
; columns + six loose cells on even passes, refills/steps them from the
; script on odd passes, ends the script by clearing the counter, advancing
; the stage to 4 and requesting sounds; decrements the pass counter
; otherwise
advanceScriptedCharPlaneBandTo4:
14C5: 3A F4 A9        LD      A,($A9F4)           ; {hard.workRam+1F4} read the pass countdown
14C8: CB 47           BIT     0,A                 ; which pass -- odd draws, even blanks
14CA: 28 6F           JR      Z,$153B             ; {code.loc_153b} even -- go blank the band
14CC: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} load the script cursor
14CF: 7E              LD      A,(HL)              ; read the byte under it
14D0: E6 FE           AND     $FE                 ; any bit above bit 0 set (terminator)?
14D2: 28 15           JR      Z,$14E9             ; {code.loc_14e9} no -- draw this frame
14D4: 3E 00           LD      A,$00               ; value 0...
14D6: 32 F4 A9        LD      ($A9F4),A           ; {hard.workRam+1F4} ...clears the pass countdown -- script done
14D9: 3E 04           LD      A,$04               ; value 4...
14DB: 32 F0 A9        LD      ($A9F0),A           ; {hard.workRam+1F0} ...into the intro-animation step -- advance to stage 4
14DE: CD E4 56        CALL    $56E4               ; {code.requestInterRoundSoundPair} request the inter-round sound pair
14E1: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} reload the cursor
14E4: 23              INC     HL                  
14E5: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} step the cursor on -- ending early
14E8: C9              RET                         

loc_14e9:
14E9: CD 63 15        CALL    $1563               ; {code.restoreColumnFromSavedRun} restore the working column from its saved run
14EC: 0E 01           LD      C,$01               ; colour set 1
14EE: 11 51 A4        LD      DE,$A451            ; column of glyph cells
14F1: CD 9D 4A        CALL    $4A9D               ; {code.stepThirteenScriptedGlyphCells} advance thirteen scripted glyph cells down the column
14F4: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} load the cursor
14F7: 11 0D 00        LD      DE,$000D            ; step of +13...
14FA: 19              ADD     HL,DE               ; ...skip the cursor thirteen bytes forward
14FB: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} save it
14FE: 0E 03           LD      C,$03               ; colour set 3
1500: 11 B1 A7        LD      DE,$A7B1            ; the same column in the other plane
1503: CD 9D 4A        CALL    $4A9D               ; {code.stepThirteenScriptedGlyphCells} advance those thirteen glyph cells in the other plane
1506: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} load the cursor
1509: 7E              LD      A,(HL)              ; read the next script byte
150A: E6 01           AND     $01                 ; take its low bit
150C: 2B              DEC     HL                  
150D: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} step the cursor back
1510: 28 09           JR      Z,$151B             ; {code.loc_151b} bit clear -- skip this nudge
1512: 11 20 00        LD      DE,$0020            ; row stride 32
1515: 21 F1 A5        LD      HL,$A5F1            ; point at a lead counter
1518: 35              DEC     (HL)                ; lower it
1519: 19              ADD     HL,DE               
151A: 35              DEC     (HL)                ; lower the counter one row below

loc_151b:
151B: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} load the cursor
151E: 7E              LD      A,(HL)              ; read the next script byte
151F: E6 01           AND     $01                 ; take its low bit
1521: 2B              DEC     HL                  
1522: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} step the cursor back
1525: 28 0F           JR      Z,$1536             ; {code.loc_1536} bit clear -- skip this nudge
1527: 11 20 00        LD      DE,$0020            ; row stride 32
152A: 21 F0 A5        LD      HL,$A5F0            ; point at a column counter
152D: 35              DEC     (HL)                ; lower it
152E: 19              ADD     HL,DE               
152F: 35              DEC     (HL)                ; lower the counter one row below
1530: 21 F2 A5        LD      HL,$A5F2            ; point at another column counter
1533: 35              DEC     (HL)                ; lower it
1534: 19              ADD     HL,DE               
1535: 35              DEC     (HL)                ; lower the counter one row below

loc_1536:
1536: CD 8C 15        CALL    $158C               ; {code.gatherCharColumnIntoBackingRun} gather the column back into its saved run
1539: 18 20           JR      $155B               ; {code.loc_155b} on to the decrement

loc_153b:
153B: 3E F1           LD      A,$F1               ; the blank tile
153D: 21 B1 A7        LD      HL,$A7B1            ; first column to blank
1540: CD 19 13        CALL    $1319               ; {code.fillCellRun} blank the thirteen-cell column
1543: 21 D1 A5        LD      HL,$A5D1            ; second column to blank
1546: CD 19 13        CALL    $1319               ; {code.fillCellRun} blank it too
1549: 21 10 A6        LD      HL,$A610            ; point at a lead cell
154C: 77              LD      (HL),A              ; blank it
154D: 19              ADD     HL,DE               
154E: 77              LD      (HL),A              ; blank the cell one row above it
154F: 21 11 A6        LD      HL,$A611            ; next lead cell
1552: 77              LD      (HL),A              ; blank it
1553: 19              ADD     HL,DE               
1554: 77              LD      (HL),A              ; blank the cell one row above it
1555: 21 12 A6        LD      HL,$A612            ; last lead cell
1558: 77              LD      (HL),A              ; blank it
1559: 19              ADD     HL,DE               
155A: 77              LD      (HL),A              ; blank the cell one row above it

loc_155b:
155B: 3A F4 A9        LD      A,($A9F4)           ; {hard.workRam+1F4} read the pass countdown
155E: 3D              DEC     A                   ; step it down
155F: 32 F4 A9        LD      ($A9F4),A           ; {hard.workRam+1F4} store it
1562: C9              RET                         

; put a saved thirty-two cell picture back onto the character plane:
; twenty-eight bytes down one column of cells a row apart, then four into
; two two-cell columns beside it. Every address is fixed here -- the run
; it reads, the column it lays and the two stubs are all this entry's
; choice, not a caller's -- and it overwrites the cells whole rather than
; merging into them
restoreColumnFromSavedRun:
1563: 11 00 A4        LD      DE,$A400            ; point at the saved thirty-two byte run
1566: 21 51 A4        LD      HL,$A451            ; point at the column of cells to repaint
1569: 01 20 00        LD      BC,$0020            ; one cell-row stride
156C: D9              EXX                         
156D: 06 1C           LD      B,$1C               ; twenty-eight cells down the column

loc_156f:
156F: D9              EXX                         
1570: 1A              LD      A,(DE)              ; take the next saved byte
1571: 77              LD      (HL),A              ; lay it into the column cell
1572: 13              INC     DE                  ; next saved byte
1573: 09              ADD     HL,BC               ; step down one row to the next cell
1574: D9              EXX                         
1575: 10 F8           DJNZ    $156F               ; {code.loc_156f} repeat for all twenty-eight cells
1577: D9              EXX                         
1578: 21 F0 A5        LD      HL,$A5F0            ; point at the first two-cell stub column
157B: 1A              LD      A,(DE)              ; take the next saved byte
157C: 77              LD      (HL),A              ; lay it into the stub cell
157D: 09              ADD     HL,BC               ; step down one row
157E: 13              INC     DE                  ; next saved byte
157F: 1A              LD      A,(DE)              ; take the next saved byte
1580: 77              LD      (HL),A              ; lay it into the cell below
1581: 13              INC     DE                  ; next saved byte
1582: 21 F2 A5        LD      HL,$A5F2            ; point at the second stub column
1585: 1A              LD      A,(DE)              ; take the next saved byte
1586: 77              LD      (HL),A              ; lay it in
1587: 09              ADD     HL,BC               ; step down one row
1588: 13              INC     DE                  ; next saved byte
1589: 1A              LD      A,(DE)              ; take the last saved byte
158A: 77              LD      (HL),A              ; lay it into the last cell
158B: C9              RET                         

; gather one column of the character plane into a thirty-two byte run --
; the column's twenty-eight cells a row apart, then the two two-cell
; columns beside it -- overwriting the run whole rather than merging into
; it; it is the exact inverse of 0x1563 over the same cells in the same
; order
gatherCharColumnIntoBackingRun:
158C: 11 00 A4        LD      DE,$A400            ; point at the thirty-two byte backing run
158F: 21 51 A4        LD      HL,$A451            ; point at the column of cells to read
1592: 01 20 00        LD      BC,$0020            ; one cell-row stride
1595: D9              EXX                         
1596: 06 1C           LD      B,$1C               ; twenty-eight cells down the column

loc_1598:
1598: D9              EXX                         
1599: 7E              LD      A,(HL)              ; read this column cell
159A: 12              LD      (DE),A              ; store it into the run
159B: 13              INC     DE                  ; next run byte
159C: 09              ADD     HL,BC               ; step down one row to the next cell
159D: D9              EXX                         
159E: 10 F8           DJNZ    $1598               ; {code.loc_1598} repeat for all twenty-eight cells
15A0: D9              EXX                         
15A1: 21 F0 A5        LD      HL,$A5F0            ; point at the first two-cell stub column
15A4: 7E              LD      A,(HL)              ; read the stub cell
15A5: 12              LD      (DE),A              ; store it into the run
15A6: 09              ADD     HL,BC               ; step down one row
15A7: 13              INC     DE                  ; next run byte
15A8: 7E              LD      A,(HL)              ; read the cell below
15A9: 12              LD      (DE),A              ; store it
15AA: 13              INC     DE                  ; next run byte
15AB: 21 F2 A5        LD      HL,$A5F2            ; point at the second stub column
15AE: 7E              LD      A,(HL)              ; read the stub cell
15AF: 12              LD      (DE),A              ; store it
15B0: 09              ADD     HL,BC               ; step down one row
15B1: 13              INC     DE                  ; next run byte
15B2: 7E              LD      A,(HL)              ; read the last cell
15B3: 12              LD      (DE),A              ; store it
15B4: C9              RET                         

loc_15b5:
15B5: C9              RET                         

; zero every slot of the vertical sprite shadow band, which parks all of
; them above the first visible line, hiding them without retiring any
hideAllSprites:
15B6: 21 41 AA        LD      HL,$AA41            ; point at the sprite vertical-position band
15B9: 06 18           LD      B,$18               ; twenty-four sprite slots
15BB: AF              XOR     A                   ; zero -- the value that parks a slot

loc_15bc:
15BC: 77              LD      (HL),A              ; park this slot above the top line, hiding it
15BD: 2C              INC     L                   
15BE: 2C              INC     L                   ; skip two cells to the next slot's vertical byte
15BF: 10 FB           DJNZ    $15BC               ; {code.loc_15bc} over all twenty-four slots
15C1: C9              RET                         

; run the arm the LOW THREE BITS of the inner sequence step select out of
; a word table laid down inline just behind this entry; the arm is entered
; as a transfer with no place parked for it to come back to, so it returns
; past this entry and nothing here runs after it, and all eight indices
; are carried out through the machine's own arithmetic rather than assumed
; away
dispatchSequencePhase0SubStepArm:
15C2: 3A AC A9        LD      A,($A9AC)           ; {hard.workRam+1AC} take the inner sequence sub-step
15C5: E6 07           AND     $07                 ; keep its low three bits -- eight arms
15C7: F7              RST     $30                 ; jump to the selected arm through the inline word table

; ---- $15C8-$15C9: jump table ----
15C8: E2 15

loc_15ca:
15CA: 5F              LD      E,A                 
15CB: A5              AND     L                   
15CC: 13              INC     DE                  
15CD: 77              LD      (HL),A              
15CE: D7              RST     $10                 
15CF: 34              INC     (HL)                
15D0: 87              ADD     A,A                 
15D1: FD DC B9 FE     CALL    C,$FEB9             
15D5: 15              DEC     D                   
15D6: 60              LD      H,B                 
15D7: A6              AND     (HL)                
15D8: 14              INC     D                   
15D9: C4 FD 10        CALL    NZ,$10FD            ; {code.spinRemainingSpriteMultiplexSlots}
15DC: ED 77           NOP                         
15DE: 68              LD      L,B                 
15DF: D7              RST     $10                 
15E0: 34              INC     (HL)                
15E1: B9              CP      C                   

; the first arm of the sequence machine's outer phase zero: arm the whole-
; plane wipe, then hand the inner index the step that actually runs that
; wipe, then subtract a 256-byte block of the program image from the outer
; phase and exclusive-or a fixed key into the difference. Neither number
; lands as an immediate -- the inner index is read out of a program byte
; that is the low half of an address inside an instruction, and the phase
; is never assigned, only folded -- so it is a tamper test that CORRUPTS
; the sequence rather than refusing to run. The dispatch that reaches it
; masks with `and 0x03`, so arrival proves only that the phase is
; congruent to zero modulo four, which is less than it looks like: 0x04,
; 0x08 and 0x0C are not fixed points of the fold. That the phase is left
; standing rests on SEQUENCE_PHASE's own registered range of four values
; and not on anything this arrival establishes
startTheWholePlaneWipeAndFoldAnImageBlockIntoThePhase:
15E2: CD 9A 01        CALL    $019A               ; {code.armWholePlaneWipeThenDerailOnATamperedImage} arm the whole-plane wipe -- derailing if the image was altered
15E5: 3A 49 17        LD      A,($1749)           ; {hard.rom+1749} read a program byte -- the low half of a call operand, so an edit moves it
15E8: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} seat it as the inner sequence sub-step
15EB: 0E 00           LD      C,$00               ; 256 bytes to fold
15ED: 21 48 56        LD      HL,$5648            ; point at that program-image block
15F0: 3A AB A9        LD      A,($A9AB)           ; {hard.workRam+1AB} take the outer sequence phase

loc_15f3:
15F3: 96              SUB     (HL)                ; fold: subtract each image byte from the phase
15F4: 23              INC     HL                  ; next image byte
15F5: 0D              DEC     C                   
15F6: 20 FB           JR      NZ,$15F3            ; {code.loc_15f3} over all 256 bytes
15F8: EE 4E           XOR     $4E                 ; exclusive-or a fixed key into the result
15FA: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} write it back as the phase -- corrupts the sequence if the image was altered
15FD: C9              RET                         

; once a per-frame countdown lapses, arm a fresh screen: enqueue four
; fixed ring commands, seed a marker byte into two cells, patch six cells
; from a following table (value + 0x05 marker), print the six-digit
; readout, set two sub-states, and enqueue a fifth command when the gate
; cell is set
armAttractScreenShowingHighScore:
15FE: CD C2 01        CALL    $01C2               ; {code.blankNextLine} blank one line of the character plane
1601: C0              RET     NZ                  ; more lines still to blank -- leave until the block is cleared
1602: 11 05 01        LD      DE,$0105            ; command 1, argument 5
1605: FF              RST     $38                 ; queue it on the request ring
1606: 1C              INC     E                   ; argument 6
1607: FF              RST     $38                 ; queue it
1608: 1C              INC     E                   ; argument 7
1609: FF              RST     $38                 ; queue it
160A: 11 01 06        LD      DE,$0601            ; command 6, argument 1
160D: FF              RST     $38                 ; queue it
160E: 3E 13           LD      A,$13               ; marker glyph
1610: 32 01 A7        LD      ($A701),A           ; seed it into one cell
1613: 32 E1 A6        LD      ($A6E1),A           ; and into another
1616: 21 3F 16        LD      HL,$163F            ; point at the six-entry patch list that follows
1619: 06 06           LD      B,$06               ; six cells to patch

loc_161b:
161B: 5E              LD      E,(HL)              ; read the destination address low byte
161C: 23              INC     HL                  
161D: 56              LD      D,(HL)              ; and its high byte
161E: 23              INC     HL                  
161F: 7E              LD      A,(HL)              ; read the value
1620: 12              LD      (DE),A              ; write it into the destination cell
1621: 13              INC     DE                  ; the cell beside it
1622: EB              EX      DE,HL               
1623: 36 05           LD      (HL),$05            ; stamp marker 5 next to it
1625: EB              EX      DE,HL               
1626: 23              INC     HL                  ; next patch entry
1627: 10 F2           DJNZ    $161B               ; {code.loc_161b} over all six
1629: CD 6B 0D        CALL    $0D6B               ; {code.paintHighScoreReadout} print the six-digit high-score readout
162C: 3E 01           LD      A,$01               
162E: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} set the outer sequence phase to 1
1631: 3C              INC     A                   
1632: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} set the inner sub-step to 2
1635: 3A C0 A9        LD      A,($A9C0)           ; {hard.workRam+1C0} read the free-play flag
1638: A7              AND     A                   
1639: C8              RET     Z                   ; leave unless free play
163A: 11 0D 01        LD      DE,$010D            ; command 1, argument 0x0D
163D: FF              RST     $38                 ; queue it
163E: C9              RET                         

; ---- $163F-$1650: data ----
163F: FB AD FD 39 AD 68 43 AB 7C FE AB A5 BE AC 38 C7
164F: AC 3B

; the inner level of the two-level sequence machine for one outer mode:
; run the arm the RAW inner index selects out of a word table laid inline
; just after this entry, then this mode's shared tail at 0x167B; the
; doubling that turns the index into an offset wraps at eight bits, so a
; large index folds back onto the head of the table
dispatchSequencePhase1SubStepArm:
1651: 21 7B 16        LD      HL,$167B            ; point at the shared tail
1654: E5              PUSH    HL                  ; park it as the return each arm falls back to
1655: 3A AC A9        LD      A,($A9AC)           ; {hard.workRam+1AC} take the inner sequence sub-step
1658: F7              RST     $30                 ; jump to the selected arm through the inline word table

; ---- $1659-$1672: jump table ----
1659: 4B 07 34 17 3F 2D 3E 08 48 17 6A 17 8C 17 B9 17
1669: 52 32 E2 17 19 4B FB 17 30 27

; ---- $1673-$167A: data ----
1673: 26 A6 13 88 57 A5 BF B9

; a shared tail of the two-level sequence machine: when the packed-decimal
; credit count (0xA986) is nonzero, step the outer sequence phase and
; return; otherwise, only when the free-play flag (0xA9C0) is set and a
; start-button bit (0xA9AE & 0x18) is held, hide every sprite and start a
; game charging no credit
advanceSequenceElseStartFreePlayGame:
167B: 3A 86 A9        LD      A,($A986)           ; {hard.workRam+186} read the credit count
167E: A7              AND     A                   
167F: C2 11 0F        JP      NZ,$0F11            ; {code.advanceSequencePhase} credits on hand: step the outer sequence phase and leave
1682: 3A C0 A9        LD      A,($A9C0)           ; {hard.workRam+1C0} read the free-play flag
1685: A7              AND     A                   
1686: C8              RET     Z                   ; not free play: leave
1687: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the panel input mirror
168A: E6 18           AND     $18                 ; keep the two start-button bits
168C: C8              RET     Z                   ; neither start held: leave
168D: CD B6 15        CALL    $15B6               ; {code.hideAllSprites} sweep every sprite off the picture

; start a game for whichever start button the input mirror shows held --
; two players if the two-player bit is set, one if only the one-player bit
; is -- stocking each started player's block with the lives setting, and
; charging no credit
startGameOnFreePlay:
1690: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the panel input mirror
1693: CB 67           BIT     4,A                 ; is the two-player start held?
1695: 20 05           JR      NZ,$169C            ; {code.loc_169c} yes: start a two-player game
1697: CB 5F           BIT     3,A                 ; is the one-player start held?
1699: 20 7E           JR      NZ,$1719            ; {code.loc_1719} yes: start a one-player game
169B: C9              RET                         ; neither held: do nothing

loc_169c:
169C: 3E FF           LD      A,$FF               
169E: 32 30 AD        LD      ($AD30),A           ; {hard.workRam+530} raise the play-active flag
16A1: 32 31 AD        LD      ($AD31),A           ; {hard.workRam+531} raise the two-player flag
16A4: 3A C1 A9        LD      A,($A9C1)           ; {hard.workRam+1C1} read the per-game life allowance
16A7: 32 10 AD        LD      ($AD10),A           ; {hard.workRam+510} stock player one's lives
16AA: 32 20 AD        LD      ($AD20),A           ; {hard.workRam+520} stock player two's lives
16AD: 18 7B           JR      $172A               ; {code.seatSequencePhase3AndResetSubStep} seat the round-start phase

loc_16af:
16AF: 06 00           LD      B,$00               ; 256 bytes to fold
16B1: 21 9F 4D        LD      HL,$4D9F            ; point at a program-image block
16B4: 3A AB A9        LD      A,($A9AB)           ; {hard.workRam+1AB} take the outer sequence phase

loc_16b7:
16B7: 96              SUB     (HL)                ; fold: subtract each image byte from the phase
16B8: 23              INC     HL                  ; next image byte
16B9: 10 FC           DJNZ    $16B7               ; {code.loc_16b7} over all 256 bytes
16BB: EE A2           XOR     $A2                 ; exclusive-or a fixed key into the result
16BD: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} write it back as the phase -- corrupts the sequence if the image was altered
16C0: CD 97 0F        CALL    $0F97               ; {code.multiplexSpriteSlotsSkipping} run the sprite multiplexer
16C3: CD DF 1E        CALL    $1EDF               ; {code.dispatchPlayerFrameByState} advance the player this frame by its state
16C6: CD 97 0F        CALL    $0F97               ; {code.multiplexSpriteSlotsSkipping} run the sprite multiplexer again
16C9: CD BC 2C        CALL    $2CBC               ; {code.runSceneryForEra} run the scenery for this era
16CC: CD 98 10        CALL    $1098               ; {code.multiplexSpriteSlots} run the sprite multiplexer
16CF: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame counter
16D2: E6 01           AND     $01                 
16D4: 28 1C           JR      Z,$16F2             ; {code.loc_16f2} even frame: skip the delay tick
16D6: 21 EB A9        LD      HL,$A9EB            ; point at this step's delay counter
16D9: 35              DEC     (HL)                ; count it down one frame
16DA: 20 16           JR      NZ,$16F2            ; {code.loc_16f2} not expired yet
16DC: 11 09 03        LD      DE,$0309            ; on expiry: command 3, argument 9
16DF: FF              RST     $38                 ; queue it on the request ring
16E0: 1E 0E           LD      E,$0E               ; argument 0x0E
16E2: FF              RST     $38                 ; queue it
16E3: 1E 1A           LD      E,$1A               ; argument 0x1A
16E5: FF              RST     $38                 ; queue it
16E6: AF              XOR     A                   
16E7: 32 0E AD        LD      ($AD0E),A           ; {hard.workRam+50E} clear the round-armed flag
16EA: 3E 2A           LD      A,$2A               
16EC: 32 EB A9        LD      ($A9EB),A           ; {hard.workRam+1EB} reload the step-delay counter to 0x2A frames
16EF: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index and leave

loc_16f2:
16F2: 3A 0E AD        LD      A,($AD0E)           ; {hard.workRam+50E} read the round-armed flag
16F5: A7              AND     A                   
16F6: C8              RET     Z                   ; not armed: leave
16F7: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame counter
16FA: E6 0F           AND     $0F                 ; keep its low nibble
16FC: 28 09           JR      Z,$1707             ; {code.loc_1707} frame nibble 0
16FE: FE 05           CP      $05                 
1700: 28 09           JR      Z,$170B             ; {code.loc_170b} frame nibble 5
1702: FE 0A           CP      $0A                 
1704: 28 09           JR      Z,$170F             ; {code.loc_170f} frame nibble 0x0A
1706: C9              RET                         ; any other frame: leave

loc_1707:
1707: 16 02           LD      D,$02               ; command 2
1709: 18 06           JR      $1711               ; {code.loc_1711}

loc_170b:
170B: 16 0A           LD      D,$0A               ; command 0x0A
170D: 18 02           JR      $1711               ; {code.loc_1711}

loc_170f:
170F: 16 0B           LD      D,$0B               ; command 0x0B

loc_1711:
1711: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
1714: C6 1A           ADD     A,$1A               ; offset it to the caption argument
1716: 5F              LD      E,A                 
1717: FF              RST     $38                 ; queue that command onto the request ring
1718: C9              RET                         

loc_1719:
1719: AF              XOR     A                   ; zero
171A: 32 31 AD        LD      ($AD31),A           ; {hard.workRam+531} clear the two-player flag
171D: 32 20 AD        LD      ($AD20),A           ; {hard.workRam+520} clear player two's lives
1720: 3D              DEC     A                   
1721: 32 30 AD        LD      ($AD30),A           ; {hard.workRam+530} raise the play-active flag
1724: 3A C1 A9        LD      A,($A9C1)           ; {hard.workRam+1C1} read the per-game life allowance
1727: 32 10 AD        LD      ($AD10),A           ; {hard.workRam+510} stock player one's lives

; jump the sequence machine to its last outer phase and restart the inner
; index at zero; both stores are constants and neither cell is read first,
; so this is an unconditional jump to a fixed place rather than a step
seatSequencePhase3AndResetSubStep:
172A: 3E 03           LD      A,$03               
172C: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} seat the outer sequence at its last phase, 3
172F: AF              XOR     A                   
1730: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} restart the inner sub-step at zero
1733: C9              RET                         

; one interpolated-run sequence step: call drawInterpolatedPenRun to
; draw/advance one pen run and ret nz unless it reseated to a zero row
; integer, then store the two's-complement checksum of the 34-byte code
; block at 0x1748 into 0xA817 (0x00 on a clean image) and tail-jump to
; 0x0F1A (advanceSequenceSubStep) to step the sequence sub-index
advancePenRunAnimationStep:
1734: CD 01 02        CALL    $0201               ; {code.drawInterpolatedPenRun} draw and advance one interpolated pen run
1737: C0              RET     NZ                  ; not yet reseated to a zero row -- leave
1738: 21 48 17        LD      HL,$1748            ; point at the guarded code block
173B: 06 22           LD      B,$22               ; its length -- thirty-four bytes
173D: AF              XOR     A                   ; start the running total at zero

loc_173e:
173E: 96              SUB     (HL)                ; subtract each byte -- a two's-complement checksum
173F: 23              INC     HL                  ; next byte
1740: 10 FC           DJNZ    $173E               ; {code.loc_173e} over all thirty-four bytes
1742: 32 17 A8        LD      ($A817),A           ; {hard.workRam+17} store the checksum -- zero on an untampered block
1745: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index

; hold one sequence step for as long as its delay cell counts, restamping
; the copyright strip and flashing its line on every frame of the wait,
; and on the frame the delay expires queue two erase requests -- caption
; records 3 and 4, whose glyph runs read PLEASE DEPOSIT COIN and AND TRY
; THIS GAME -- then step the sequence on. A cell holding zero on arrival
; wraps to 255 and waits the long way round rather than leaving at once.
; The expiry frame also does the load-bearing thing the name drops: it
; copies the glyph showing at 0xA63C and the colour of the same cell into
; the pair at 0xACC7, and that pair is a COPYRIGHT TAMPER WITNESS rather
; than a screen save. 0xA63C is the fifth cell of the `(c) KONAMI 1982`
; caption -- the N, glyph 0x3B -- and the arm at 0x30E3 reads the pair
; back, tests the glyph against 0x3B and the colour against 0x05 or 0x10,
; and derails to 0x315B on anything else
holdCopyrightThenEraseTheCoinInvitation:
1748: CD 06 0B        CALL    $0B06               ; {code.stampCopyrightStrip} re-stamp the copyright caption strip
174B: CD 39 0B        CALL    $0B39               ; {code.flashCopyrightLine} flash the copyright line
174E: 21 EB A9        LD      HL,$A9EB            ; point at this step's delay counter
1751: 35              DEC     (HL)                ; count it down one frame
1752: C0              RET     NZ                  ; still waiting -- leave
1753: 21 3C A6        LD      HL,$A63C            ; point at the sampled copyright caption cell
1756: 11 C7 AC        LD      DE,$ACC7            ; point at the tamper-witness pair
1759: 7E              LD      A,(HL)              ; read its glyph
175A: 12              LD      (DE),A              ; save the glyph
175B: 13              INC     DE                  
175C: CB 94           RES     2,H                 ; cross to the colour plane of the same cell
175E: 7E              LD      A,(HL)              ; read its colour
175F: 12              LD      (DE),A              ; save the colour beside the glyph
1760: 11 03 03        LD      DE,$0303            ; command 3, argument 3
1763: FF              RST     $38                 ; queue it -- erase one coin-invitation caption
1764: 1C              INC     E                   ; argument 4
1765: FF              RST     $38                 ; queue it -- erase the other
1766: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index

; ---- $1769-$1769: data ----
1769: 31

loc_176a:
176A: CD DA 19        CALL    $19DA               ; {code.checkTheCopyrightLineColoursOrDerail} verify the copyright line's colours -- derail if wrong
176D: 3A 7C A6        LD      A,($A67C)           ; read a caption cell
1770: FE 7C           CP      $7C                 ; is its glyph the expected one?
1772: C2 9B 45        JP      NZ,$459B            ; wrong glyph: derail into the mother-ship warp-flash handler
1775: 11 13 01        LD      DE,$0113            ; command 1, argument 0x13
1778: FF              RST     $38                 ; queue it
1779: CD DC 4B        CALL    $4BDC               ; {code.paintFiveLabelledNumericReadouts} paint the five labelled numeric readouts
177C: 21 DC A5        LD      HL,$A5DC            ; point at a character cell
177F: 11 FB AD        LD      DE,$ADFB            ; point at a tamper-witness pair
1782: 7E              LD      A,(HL)              ; read its glyph
1783: 12              LD      (DE),A              ; save the glyph
1784: 13              INC     DE                  
1785: CB 94           RES     2,H                 ; cross to the colour plane of the same cell
1787: 7E              LD      A,(HL)              ; read its colour
1788: 12              LD      (DE),A              ; save the colour beside it
1789: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index

loc_178c:
178C: CD 06 0B        CALL    $0B06               ; {code.stampCopyrightStrip} re-stamp the copyright caption strip
178F: CD 39 0B        CALL    $0B39               ; {code.flashCopyrightLine} flash the copyright line
1792: 21 EB A9        LD      HL,$A9EB            ; point at this step's delay counter
1795: 35              DEC     (HL)                ; count it down one frame
1796: C0              RET     NZ                  ; still waiting -- leave
1797: CD DA 19        CALL    $19DA               ; {code.checkTheCopyrightLineColoursOrDerail} verify the copyright line's colours -- derail if wrong
179A: 3A B3 47        LD      A,($47B3)           ; {hard.rom+47B3} read a program byte
179D: C6 02           ADD     A,$02               ; offset it
179F: 6F              LD      L,A                 ; as the pointer low byte
17A0: C6 6A           ADD     A,$6A               ; offset it again
17A2: 67              LD      H,A                 ; as the pointer high byte
17A3: 7E              LD      A,(HL)              ; read the addressed cell
17A4: FE 3B           CP      $3B                 ; is its glyph the expected one?
17A6: C2 CA 15        JP      NZ,$15CA            ; {code.loc_15ca} wrong glyph: derail into the jump-table bytes, run as code
17A9: 21 7C A6        LD      HL,$A67C            ; point at a character cell
17AC: 11 43 AB        LD      DE,$AB43            ; point at a tamper-witness pair
17AF: 7E              LD      A,(HL)              ; read its glyph
17B0: 12              LD      (DE),A              ; save the glyph
17B1: 13              INC     DE                  
17B2: CB 94           RES     2,H                 ; cross to the colour plane of the same cell
17B4: 7E              LD      A,(HL)              ; read its colour
17B5: 12              LD      (DE),A              ; save the colour beside it
17B6: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index

; fold a block of the program image and let the sequence step on only if
; it still adds up; otherwise switch the display off and copy one
; character cell into TAMPER_WITNESS
guardBlockOrBlankDisplay:
17B9: 3A 0D 59        LD      A,($590D)           ; {hard.rom+590D} read a byte of the program image
17BC: 4F              LD      C,A                 
17BD: 3A 40 4A        LD      A,($4A40)           ; {hard.rom+4A40} seed the running total from a program byte
17C0: 21 06 0B        LD      HL,$0B06            ; point at the guarded block
17C3: 06 33           LD      B,$33               ; fifty-one bytes to add

loc_17c5:
17C5: 86              ADD     A,(HL)              ; add each byte into the total
17C6: 23              INC     HL                  ; next byte
17C7: 10 FC           DJNZ    $17C5               ; {code.loc_17c5} over all fifty-one bytes
17C9: FE EF           CP      $EF                 ; does the total match the expected signature?
17CB: CA 1A 0F        JP      Z,$0F1A             ; {code.advanceSequenceSubStep} matches: step the sequence sub-index and leave
17CE: 3A 89 4C        LD      A,($4C89)           ; {hard.rom+4C89} mismatch: take the display-off value from the image
17D1: 32 08 C3        LD      ($C308),A           ; switch the display off through the video-enable latch
17D4: 21 5C A6        LD      HL,$A65C            ; point at one character cell
17D7: 11 39 AD        LD      DE,$AD39            ; point at the tamper-witness pair
17DA: 7E              LD      A,(HL)              ; read its glyph
17DB: 12              LD      (DE),A              ; save the glyph
17DC: 13              INC     DE                  
17DD: CB 94           RES     2,H                 ; cross to the colour plane of the same cell
17DF: 7E              LD      A,(HL)              ; read its colour
17E0: 12              LD      (DE),A              ; save the colour beside it
17E1: C9              RET                         

; raise one flag cell to all bits, fold a fixed block of the program image
; into a running total seeded from an image byte and bank the result, then
; step the inner sequence index -- one step of the tamper-check sequence
foldImageBlockIntoSignatureThenAdvanceSequence:
17E2: 3E FF           LD      A,$FF               
17E4: 32 3F AA        LD      ($AA3F),A           ; {hard.workRam+23F} raise a flag cell to all bits set
17E7: 11 B9 17        LD      DE,$17B9            ; point a second pointer at a block of the program image
17EA: 0E 08           LD      C,$08               
17EC: CD D9 4B        CALL    $4BD9               ; {code.trampolineToSelectFoldBlock} select the guarded block -- its start and thirty-byte length
17EF: 3A C0 27        LD      A,($27C0)           ; {hard.rom+27C0} seed the running total from a program byte
17F2: CD 1E 29        CALL    $291E               ; {code.foldBlockIntoTotal} fold the block into the total
17F5: 32 6F AA        LD      ($AA6F),A           ; {hard.workRam+26F} bank the result as the image signature
17F8: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index

; a sequence step that does no work of its own -- it only moves the inner
; index on, so reaching it costs one turn and changes nothing else
trampolineToAdvanceSequenceSubStep:
17FB: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index

; the inner level of the two-level sequence machine for one outer mode:
; run the arm the RAW inner index selects out of a word table laid inline
; just after this entry; this mode's tail does nothing at all, which is
; why every arm here simply ends
dispatchSequencePhase2SubStepArm:
17FE: 21 1D 18        LD      HL,$181D            ; point at the mode's do-nothing tail
1801: E5              PUSH    HL                  ; park it as the arm's return
1802: 3A AC A9        LD      A,($A9AC)           ; {hard.workRam+1AC} take the inner sequence sub-step
1805: F7              RST     $30                 ; jump to the selected arm through the inline word table

; ---- $1806-$180F: jump table ----
1806: 1E 18 DB 2C 30 18 E6 07 8A 18

; ---- $1810-$181C: data ----
1810: 72 A6 14 7D A5 38 34 F1 68 0E 34 D7 B9

; an arrival point with nothing to do: no cell is read or written and no
; register moves
noOpSequencePhase2Tail:
181D: C9              RET                         ; the mode's tail -- return at once, nothing runs after the arm

; one step of a screen-clearing sequence: park every sprite out of sight,
; copy the glyph and colour showing at one fixed character cell into one
; fixed two-byte record, arm the line wipe to run from the plane's fifth
; line, and step the sequence's inner index on last; both the cell and the
; record are fixed here, so nothing a caller was holding chooses either
parkSpritesAndArmLineWipeThenAdvanceSequence:
181E: CD B6 15        CALL    $15B6               ; {code.hideAllSprites} sweep every sprite off the picture
1821: 21 FC A5        LD      HL,$A5FC            ; point at the character cell to sample
1824: 11 BE AC        LD      DE,$ACBE            ; point at the two-byte record to hold it
1827: CD FC 1A        CALL    $1AFC               ; {code.sampleCellGlyphAndColour} copy the cell's glyph and colour into the record
182A: CD B5 01        CALL    $01B5               ; {code.armLineWipeFromFifthLine} arm the line wipe from the plane's fifth line
182D: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index

; one arm of the two-level sequence machine (inner index 2 of
; dispatchSequencePhase2SubStepArm): after two setup calls it posts a
; fixed run of display codes to the writer at 0x0038 as (D=1,code) pairs
; -- 0x01,0x14,0x15, a code that flips 0x0F/0x11 on cell 0xA9C3 and its
; successor, 0x16, 0x00, and a tail 0x19/0x17 chosen by 0xA986 --
; advancing the sequence counter 0xA9AC through 0x0F1A twice on the
; 0xA986>=2 branch and once below
postAttractInfoCaptions:
1830: CD 06 0B        CALL    $0B06               ; {code.stampCopyrightStrip} re-stamp the copyright caption strip
1833: CD 39 0B        CALL    $0B39               ; {code.flashCopyrightLine} flash the copyright line
1836: 11 01 01        LD      DE,$0101            ; command 1, argument 1
1839: FF              RST     $38                 ; queue it on the request ring
183A: 1E 14           LD      E,$14               ; argument 0x14
183C: FF              RST     $38                 ; queue it
183D: 1C              INC     E                   ; argument 0x15
183E: FF              RST     $38                 ; queue it
183F: 1E 0F           LD      E,$0F               ; default caption glyph
1841: 3A C3 A9        LD      A,($A9C3)           ; {hard.workRam+1C3} read the bonus-life setting
1844: A7              AND     A                   
1845: 28 02           JR      Z,$1849             ; {code.loc_1849} setting clear: keep the default glyph
1847: 1C              INC     E                   ; setting set: step to the alternate glyph
1848: 1C              INC     E                   

loc_1849:
1849: FF              RST     $38                 ; queue the chosen caption glyph
184A: 1C              INC     E                   ; the next glyph
184B: FF              RST     $38                 ; queue it
184C: 1E 16           LD      E,$16               ; argument 0x16
184E: FF              RST     $38                 ; queue it
184F: 1E 00           LD      E,$00               ; argument 0
1851: FF              RST     $38                 ; queue it
1852: 3A 86 A9        LD      A,($A986)           ; {hard.workRam+186} read the credit count
1855: FE 02           CP      $02                 ; two or more credits?
1857: 30 07           JR      NC,$1860            ; {code.loc_1860} yes: take the two-credit tail
1859: 11 17 01        LD      DE,$0117            ; command 1, argument 0x17
185C: FF              RST     $38                 ; queue it
185D: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index and leave

loc_1860:
1860: 11 19 01        LD      DE,$0119            ; command 1, argument 0x19
1863: FF              RST     $38                 ; queue it
1864: CD 1A 0F        CALL    $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index
1867: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step it again

; ---- $186A-$1889: data ----
186A: 00 02 06 0D 00 03 07 0C 00 04 08 0B 02 06 0A 0A
187A: 04 08 0C 09 07 0A 0D 07 0B 0D 0E 05 0F 0F 0F 05

; the two-credit copyright screen's await-start step: stamp the fixed
; copyright caption strip and flash its line, then dispatch on the two
; start-button bits of IN0_MIRROR (0xA9AE) -- bit 4 tail-calls the two-
; player start, bit 3 the one-player start (bit 4 wins when both are
; held), and with neither held it returns so the screen shows again
stepTwoCreditCopyrightScreenAwaitingStart:
188A: CD 06 0B        CALL    $0B06               ; {code.stampCopyrightStrip} redraw the fixed copyright caption strip
188D: CD 39 0B        CALL    $0B39               ; {code.flashCopyrightLine} flash its line for this frame
1890: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the panel's start-button bits
1893: CB 67           BIT     4,A                 ; is two-player start held? -- bit 4
1895: C2 9E 18        JP      NZ,$189E            ; {code.startTwoPlayerGame} two-player start held: begin a two-player game
1898: CB 5F           BIT     3,A                 ; is one-player start held? -- bit 3
189A: C2 15 32        JP      NZ,$3215            ; {code.startOnePlayerGame} one-player start held: begin a one-player game
189D: C9              RET                         ; neither held: leave the copyright screen up

; start a two-player game: park the caption sprites, raise PLAY_ACTIVE and
; the flag beside it, load both players' lives from the starting-count
; settings cell, run the two-player-start arm, deduct two credits in
; packed BCD from 0xA986 and repaint the panel field, then send the
; sequence machine to its last phase
startTwoPlayerGame:
189E: CD 2B 0B        CALL    $0B2B               ; {code.hideCaptionSprites} park the caption sprites
18A1: 3E FF           LD      A,$FF               
18A3: 32 30 AD        LD      ($AD30),A           ; {hard.workRam+530} raise the play-active flag
18A6: 32 31 AD        LD      ($AD31),A           ; {hard.workRam+531} raise the two-player-game flag beside it
18A9: 3A C1 A9        LD      A,($A9C1)           ; {hard.workRam+1C1} take the starting-lives setting
18AC: 32 10 AD        LD      ($AD10),A           ; {hard.workRam+510} seat it as player one's life count
18AF: 32 20 AD        LD      ($AD20),A           ; {hard.workRam+520} and as player two's life count
18B2: CD 0E 46        CALL    $460E               ; {code.setUpTwoPlayerStartObjectOnce} run the two-player-start object arm
18B5: 21 86 A9        LD      HL,$A986            ; point at the on-screen credit count
18B8: 7E              LD      A,(HL)              
18B9: D6 02           SUB     $02                 ; take two credits off it
18BB: 27              DAA                         ; fix the packed-decimal result
18BC: 77              LD      (HL),A              
18BD: CD FB 4A        CALL    $4AFB               ; {code.paintCreditCountPanel} repaint the credit field
18C0: C3 2A 17        JP      $172A               ; {code.seatSequencePhase3AndResetSubStep} send the sequence machine to its last phase

loc_18c3:
18C3: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame counter
18C6: E6 01           AND     $01                 ; keep its low bit -- run this scan every other frame
18C8: C2 84 19        JP      NZ,$1984            ; {code.loc_1984} on the off frames, hand over to the cursor-flash and game-over arm
18CB: CD D1 1E        CALL    $1ED1               ; {code.readPlayerControls} read the entry panel's controls
18CE: 21 95 A9        LD      HL,$A995            ; point at the first of four rolling press-history bytes
18D1: 0F              RRCA                        
18D2: CB 16           RL      (HL)                ; roll the letter-back control into its history
18D4: 23              INC     HL                  
18D5: 0F              RRCA                        
18D6: CB 16           RL      (HL)                ; roll the letter-forward control into its history
18D8: 23              INC     HL                  
18D9: 0F              RRCA                        
18DA: 0F              RRCA                        
18DB: 0F              RRCA                        
18DC: CB 16           RL      (HL)                ; roll a commit button into its history
18DE: 23              INC     HL                  
18DF: 0F              RRCA                        
18E0: CB 16           RL      (HL)                ; roll the other commit button into its history
18E2: 7E              LD      A,(HL)              
18E3: E6 07           AND     $07                 ; keep the last three samples -- a fresh press reads as 001
18E5: 3D              DEC     A                   
18E6: 28 3B           JR      Z,$1923             ; {code.loc_1923} a commit button just went down: lock in the current letter
18E8: 2B              DEC     HL                  
18E9: 7E              LD      A,(HL)              
18EA: E6 07           AND     $07                 
18EC: 3D              DEC     A                   
18ED: 28 34           JR      Z,$1923             ; {code.loc_1923} the other commit button went down: lock in the letter
18EF: 2B              DEC     HL                  
18F0: 7E              LD      A,(HL)              
18F1: FE FF           CP      $FF                 ; the letter-forward control held to saturation?
18F3: CC 80 19        CALL    Z,$1980             ; {code.rearmHeldControlRepeat} if so, clear its history so a held press repeats
18F6: E6 07           AND     $07                 
18F8: 3D              DEC     A                   
18F9: 28 1B           JR      Z,$1916             ; {code.loc_1916} a fresh forward press: step the shown letter forward
18FB: 2B              DEC     HL                  
18FC: 7E              LD      A,(HL)              
18FD: FE 7F           CP      $7F                 ; the letter-back control held to saturation?
18FF: CC 80 19        CALL    Z,$1980             ; {code.rearmHeldControlRepeat} if so, clear its history so a held press repeats
1902: E6 07           AND     $07                 
1904: 3D              DEC     A                   
1905: 28 02           JR      Z,$1909             ; {code.loc_1909} a fresh back press: step the shown letter back
1907: 18 5A           JR      $1963               ; {code.loc_1963} nothing pressed: go blink the cursor

loc_1909:
1909: 21 99 A9        LD      HL,$A999            ; point at the letter index
190C: 35              DEC     (HL)                ; step the shown letter back one
190D: 7E              LD      A,(HL)              
190E: FE 80           CP      $80                 ; did the index run below the first letter?
1910: 38 3C           JR      C,$194E             ; {code.loc_194e} still in range: redraw it
1912: 36 1A           LD      (HL),$1A            ; wrapped: set it to the last letter
1914: 18 38           JR      $194E               ; {code.loc_194e}

loc_1916:
1916: 21 99 A9        LD      HL,$A999            ; point at the letter index
1919: 34              INC     (HL)                ; step the shown letter forward one
191A: 7E              LD      A,(HL)              
191B: FE 1B           CP      $1B                 ; past the last letter?
191D: 38 2F           JR      C,$194E             ; {code.loc_194e} still in range: redraw it
191F: 36 00           LD      (HL),$00            ; wrapped: back to the first letter
1921: 18 2B           JR      $194E               ; {code.loc_194e}

loc_1923:
1923: 3A 99 A9        LD      A,($A999)           ; {hard.workRam+199} take the chosen letter index
1926: 21 C7 12        LD      HL,$12C7            ; point at the letter-glyph table
1929: CF              RST     $08                 ; look up its glyph
192A: 2A 91 A9        LD      HL,($A991)          ; {hard.workRam+191} fetch the video write pointer
192D: ED 5B 93 A9     LD      DE,($A993)          ; {hard.workRam+193} fetch the colour write pointer
1931: 12              LD      (DE),A              ; stamp the glyph through the colour-side pointer
1932: 77              LD      (HL),A              ; stamp it through the video-side pointer
1933: 3A 90 A9        LD      A,($A990)           ; {hard.workRam+190} take the colour a locked-in letter wears
1936: CB 92           RES     2,D                 ; aim the pointer at the colour plane
1938: 12              LD      (DE),A              ; paint that colour under the glyph
1939: CB D2           SET     2,D                 
193B: E7              RST     $20                 ; step the write pointer on to the next cell
193C: 23              INC     HL                  
193D: 22 91 A9        LD      ($A991),HL          ; {hard.workRam+191} save the advanced video pointer
1940: ED 53 93 A9     LD      ($A993),DE          ; {hard.workRam+193} save the advanced colour pointer
1944: 21 9A A9        LD      HL,$A99A            
1947: 35              DEC     (HL)                ; one fewer initial left to enter
1948: 28 2B           JR      Z,$1975             ; {code.loc_1975} all initials in: finish the entry
194A: AF              XOR     A                   
194B: 32 99 A9        LD      ($A999),A           ; {hard.workRam+199} reset the letter index for the next slot

loc_194e:
194E: ED 5B 93 A9     LD      DE,($A993)          ; {hard.workRam+193} fetch the cursor write pointer
1952: 3A 99 A9        LD      A,($A999)           ; {hard.workRam+199} take the letter now being shown
1955: 21 C7 12        LD      HL,$12C7            
1958: CF              RST     $08                 ; look up its glyph
1959: 12              LD      (DE),A              ; draw it at the cursor cell
195A: CB 92           RES     2,D                 ; aim at the colour plane
195C: 3E 10           LD      A,$10               
195E: 12              LD      (DE),A              ; paint the bright cursor colour under it
195F: AF              XOR     A                   
1960: 32 9C A9        LD      ($A99C),A           ; {hard.workRam+19C} restart the cursor-flash counter

loc_1963:
1963: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame counter
1966: E6 07           AND     $07                 ; act one frame in eight
1968: 20 30           JR      NZ,$199A            ; {code.loc_199a} other frames: go to the flash and game-over tail
196A: 21 EB A9        LD      HL,$A9EB            
196D: 35              DEC     (HL)                ; count the cursor-blink timer down
196E: 20 2A           JR      NZ,$199A            ; {code.loc_199a} not fired yet: go to the tail
1970: 2A 93 A9        LD      HL,($A993)          ; {hard.workRam+193} fetch the cursor cell pointer
1973: 36 F1           LD      (HL),$F1            ; blank the cursor -- the blink's dark phase

loc_1975:
1975: 3E 3C           LD      A,$3C               
1977: 32 EB A9        LD      ($A9EB),A           ; {hard.workRam+1EB} reload the cursor-blink timer -- sixty frames
197A: CD 34 56        CALL    $5634               ; {code.enqueueTransitionSoundBurst}
197D: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence machine on

; clear the one-bit press history a caller points at, and hand back a
; zero. A history is a byte a control's bit is rolled into every other
; frame, and its owner acts on the frame the low three bits read 001;
; while a control stays held the byte fills and that pattern cannot recur,
; so clearing it is what lets the same press act again
rearmHeldControlRepeat:
1980: 36 00           LD      (HL),$00            ; empty the press-history byte the caller points at
1982: AF              XOR     A                   ; hand back zero
1983: C9              RET                         

loc_1984:
1984: 21 9C A9        LD      HL,$A99C            ; point at the cursor-flash counter
1987: 34              INC     (HL)                ; step it on one
1988: 2A 93 A9        LD      HL,($A993)          ; {hard.workRam+193} fetch the cursor's colour cell
198B: CB 94           RES     2,H                 ; aim at the colour plane
198D: 3A 9C A9        LD      A,($A99C)           ; {hard.workRam+19C}
1990: CB 67           BIT     4,A                 ; is the counter's slow bit set? -- picks the flash phase
1992: 28 04           JR      Z,$1998             ; {code.loc_1998}
1994: 36 14           LD      (HL),$14            ; one phase: paint the cursor its bright colour
1996: 18 02           JR      $199A               ; {code.loc_199a}

loc_1998:
1998: 36 10           LD      (HL),$10            ; the other phase: paint it its dim colour

loc_199a:
199A: 21 20 AD        LD      HL,$AD20            ; point at player two's life count
199D: 3A 10 AD        LD      A,($AD10)           ; {hard.workRam+510} take player one's life count
19A0: B6              OR      (HL)                ; fold in player two's
19A1: C0              RET     NZ                  ; either player still has a life: leave the entry running
19A2: 3A C0 A9        LD      A,($A9C0)           ; {hard.workRam+1C0} read the free-play flag
19A5: A7              AND     A                   
19A6: 20 26           JR      NZ,$19CE            ; {code.loc_19ce} free play: jump to the free-play start check
19A8: 3A 86 A9        LD      A,($A986)           ; {hard.workRam+186} read the credit count
19AB: FE 01           CP      $01                 ; is it below one?
19AD: D8              RET     C                   ; no credits: keep waiting
19AE: 28 10           JR      Z,$19C0             ; {code.loc_19c0} exactly one credit: go to the one-credit check
19B0: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the start-button bits
19B3: E6 18           AND     $18                 
19B5: C8              RET     Z                   ; none held: keep waiting
19B6: FE 08           CP      $08                 ; the one-player start alone?
19B8: 28 0E           JR      Z,$19C8             ; {code.loc_19c8} yes: begin a one-player game
19BA: CD B6 15        CALL    $15B6               ; {code.hideAllSprites} hide every sprite
19BD: C3 9E 18        JP      $189E               ; {code.startTwoPlayerGame} otherwise begin a two-player game

loc_19c0:
19C0: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the start-button bits
19C3: E6 18           AND     $18                 
19C5: FE 08           CP      $08                 ; must be the one-player start alone
19C7: C0              RET     NZ                  ; anything else: keep waiting

loc_19c8:
19C8: CD B6 15        CALL    $15B6               ; {code.hideAllSprites} hide every sprite
19CB: C3 15 32        JP      $3215               ; {code.startOnePlayerGame} begin a one-player game

loc_19ce:
19CE: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the start-button bits
19D1: E6 18           AND     $18                 
19D3: C8              RET     Z                   ; none held: keep waiting
19D4: CD B6 15        CALL    $15B6               ; {code.hideAllSprites} hide every sprite
19D7: C3 90 16        JP      $1690               ; {code.startGameOnFreePlay} begin a game charging no credit

; walk the thirteen colour cells under the copyright line and derail on
; the first one that has been changed: starting at 0xA2BC and stepping
; back 32 a cell, every cell must hold one of exactly two colours, and the
; first that holds anything else transfers into bytes that carry no
; routine and never come back. The two accepted colours are the COLOUR
; BYTES OF THE LINE'S TWO RECORDS, which differ in nothing else -- 0x10 in
; the record at 0x086B and 0x05 in the record at 0x4900, both carrying
; destination 0xA6BC and the same thirteen glyphs -- so the pair is what
; the line's own flashing writes, and not a wipe colour beside a pen
; colour. Thirteen good cells return having done nothing
checkTheCopyrightLineColoursOrDerail:
19DA: 21 BC A2        LD      HL,$A2BC            ; point at the copyright line's first colour cell
19DD: 06 0D           LD      B,$0D               ; thirteen cells to check

loc_19df:
19DF: 7E              LD      A,(HL)              ; read this cell's colour
19E0: FE 10           CP      $10                 ; is it the first accepted colour?
19E2: 28 05           JR      Z,$19E9             ; {code.loc_19e9} yes: on to the next cell
19E4: FE 05           CP      $05                 ; is it the second accepted colour?
19E6: C2 FA 49        JP      NZ,$49FA            ; anything else: the line has been tampered -- transfer away and never return

loc_19e9:
19E9: 11 E0 FF        LD      DE,$FFE0            ; the stride back one cell along the line
19EC: 19              ADD     HL,DE               ; step back to the previous cell
19ED: 10 F0           DJNZ    $19DF               ; {code.loc_19df} loop over all thirteen
19EF: C9              RET                         ; thirteen good cells: return having changed nothing

; reset the whole playfield for a new round: clear scroll/control cells,
; seat the ship sprite + shot slots, retire every object slot
; (hold/shared-cooldown/cooldown/sub-pixel variants), clear four sprite
; entries, seat the era scenery band via
; seatEraSceneryRowThenClearAndRunScenery, then scatter one era-selected
; 10-byte record from the 0x1B04 word table into the cells that arm the
; round
resetPlayfieldAndArmNewRound:
19F0: 21 00 00        LD      HL,$0000            ; clear the value to write
19F3: 22 08 A8        LD      ($A808),HL          ; {hard.workRam+8} zero the world-scroll X
19F6: 22 0A A8        LD      ($A80A),HL          ; {hard.workRam+A} zero the world-scroll Y
19F9: 22 06 AD        LD      ($AD06),HL          ; {hard.workRam+506} zero the paired scroll cell
19FC: AF              XOR     A                   
19FD: 32 0D AD        LD      ($AD0D),A           ; {hard.workRam+50D} clear the mother-ship-armed flag
1A00: 32 F7 A8        LD      ($A8F7),A           ; {hard.workRam+F7} clear the parachutist rung
1A03: 32 05 AD        LD      ($AD05),A           ; {hard.workRam+505} clear the base-sixty life-tick's low place
1A06: 3A D6 A9        LD      A,($A9D6)           ; {hard.workRam+1D6}
1A09: 32 D7 A9        LD      ($A9D7),A           ; {hard.workRam+1D7} reload the escalation-rung timer from its period
1A0C: 3A 0A AD        LD      A,($AD0A)           ; {hard.workRam+50A}
1A0F: 32 C0 AC        LD      ($ACC0),A           ; {hard.workRam+4C0} copy the round's opening difficulty rung into the live rung cell
1A12: AF              XOR     A                   
1A13: 32 81 AA        LD      ($AA81),A           ; {hard.workRam+281} clear a sprite cell
1A16: 32 C6 AC        LD      ($ACC6),A           ; {hard.workRam+4C6} clear the wave-hold flag
1A19: 3E 80           LD      A,$80               
1A1B: 32 02 A8        LD      ($A802),A           ; {hard.workRam+2} seat the player heading to its start direction
1A1E: AF              XOR     A                   
1A1F: 32 01 A8        LD      ($A801),A           ; {hard.workRam+1} clear the heading fraction
1A22: 3E FF           LD      A,$FF               
1A24: 32 00 A8        LD      ($A800),A           ; {hard.workRam} set the player state to alive
1A27: 3E 78           LD      A,$78               
1A29: 32 41 AA        LD      ($AA41),A           ; {hard.workRam+241} seat the player's sprite Y to its start row
1A2C: 3E 84           LD      A,$84               
1A2E: 32 10 AA        LD      ($AA10),A           ; {hard.workRam+210} seat the player's sprite entry to its start column
1A31: CD AF 20        CALL    $20AF               ; {code.dressPlayerSpriteForHeading} dress the player sprite for its heading
1A34: CD 55 27        CALL    $2755               ; {code.freeAllShotSlots} free every shot slot
1A37: DD 21 C0 A8     LD      IX,$A8C0            
1A3B: FD 21 28 AA     LD      IY,$AA28            
1A3F: CD 0D 3C        CALL    $3C0D               ; {code.retireObjectAndHold} retire the first object slot into hold
1A42: 06 07           LD      B,$07               ; seven sub-pixel slots to retire
1A44: DD 21 50 A8     LD      IX,$A850            
1A48: FD 21 1A AA     LD      IY,$AA1A            
1A4C: DD 21 E0 A8     LD      IX,$A8E0            
1A50: FD 21 2C AA     LD      IY,$AA2C            
1A54: CD FB 3D        CALL    $3DFB               ; {code.retireSlotIntoSharedCooldown} retire the next object slot into shared cooldown
1A57: DD 21 F0 A8     LD      IX,$A8F0            
1A5B: FD 21 2E AA     LD      IY,$AA2E            
1A5F: CD AD 48        CALL    $48AD               ; {code.retireSlotIntoCooldown} retire the parachutist slot into cooldown

loc_1a62:
1A62: CD DE 2B        CALL    $2BDE               ; {code.retireSlotAndSubPixel} retire this slot and clear its sub-pixel fraction
1A65: 11 10 00        LD      DE,$0010            ; the sixteen-byte record stride
1A68: DD 19           ADD     IX,DE               
1A6A: FD 23           INC     IY                  
1A6C: FD 23           INC     IY                  
1A6E: 10 F2           DJNZ    $1A62               ; {code.loc_1a62} loop over the seven slots
1A70: CD E4 1A        CALL    $1AE4               ; {code.freeAndNumberEveryObjectSlot} free and number every object slot
1A73: FD 21 28 AA     LD      IY,$AA28            ; point at the object sprite entries
1A77: FD 36 00 00     LD      (IY+$00),$00        ; clear eight entry cells across the two banks
1A7B: FD 36 02 00     LD      (IY+$02),$00        
1A7F: FD 36 04 00     LD      (IY+$04),$00        
1A83: FD 36 06 00     LD      (IY+$06),$00        
1A87: FD 36 31 00     LD      (IY+$31),$00        
1A8B: FD 36 33 00     LD      (IY+$33),$00        
1A8F: FD 36 35 00     LD      (IY+$35),$00        
1A93: FD 36 37 00     LD      (IY+$37),$00        
1A97: CD A5 30        CALL    $30A5               ; {code.seatEraSceneryRowThenClearAndRunScenery} seat the era's scenery band and run it

; apply the tuning row that the era and its escalation rung together
; select, scattering the row's ten bytes over twelve cells -- two spawner
; caps, two aim windows, two cooldown periods and their live countdowns,
; and two thresholds
applyEraRungSettings:
1A9A: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} take the era number
1A9D: 07              RLCA                        ; shift it up into the high nibble
1A9E: 07              RLCA                        
1A9F: 07              RLCA                        
1AA0: 07              RLCA                        
1AA1: E6 F0           AND     $F0                 ; keep just that nibble
1AA3: 47              LD      B,A                 
1AA4: 3A C0 AC        LD      A,($ACC0)           ; {hard.workRam+4C0} take the escalation rung
1AA7: 80              ADD     A,B                 ; combine them into the tuning-row index
1AA8: 21 04 1B        LD      HL,$1B04            ; point at the table of tuning-row addresses
1AAB: D7              RST     $10                 ; fetch the chosen row's address
1AAC: 1A              LD      A,(DE)              
1AAD: 32 44 A8        LD      ($A844),A           ; {hard.workRam+44} first byte: a launch-bank slot cap
1AB0: 13              INC     DE                  
1AB1: 1A              LD      A,(DE)              
1AB2: 32 37 A8        LD      ($A837),A           ; {hard.workRam+37} the bank's near-approach X half-window
1AB5: 13              INC     DE                  
1AB6: 1A              LD      A,(DE)              
1AB7: 32 27 A8        LD      ($A827),A           ; {hard.workRam+27} the bank's near-approach Y half-window
1ABA: 13              INC     DE                  
1ABB: 1A              LD      A,(DE)              
1ABC: 32 17 A8        LD      ($A817),A           ; {hard.workRam+17} the bank-launch cooldown
1ABF: 32 14 A8        LD      ($A814),A           ; {hard.workRam+14} -- into its paired reload cell too
1AC2: 13              INC     DE                  
1AC3: 1A              LD      A,(DE)              
1AC4: 32 C1 AC        LD      ($ACC1),A           ; {hard.workRam+4C1} the craft-per-round count
1AC7: 13              INC     DE                  
1AC8: 1A              LD      A,(DE)              
1AC9: 32 C4 AC        LD      ($ACC4),A           ; {hard.workRam+4C4} a script-pick threshold
1ACC: 13              INC     DE                  
1ACD: 1A              LD      A,(DE)              
1ACE: 32 C6 A8        LD      ($A8C6),A           ; {hard.workRam+C6} an attacker-spawn slot cap
1AD1: 13              INC     DE                  
1AD2: 1A              LD      A,(DE)              
1AD3: 32 D6 A8        LD      ($A8D6),A           ; {hard.workRam+D6} the attacker-spawn spread half-window
1AD6: 13              INC     DE                  
1AD7: 1A              LD      A,(DE)              
1AD8: 32 E6 A8        LD      ($A8E6),A           ; {hard.workRam+E6} the attacker-spawn aim half-window
1ADB: 13              INC     DE                  
1ADC: 1A              LD      A,(DE)              
1ADD: 32 F4 A8        LD      ($A8F4),A           ; {hard.workRam+F4} the attacker-spawn cooldown
1AE0: 32 F6 A8        LD      ($A8F6),A           ; {hard.workRam+F6} -- into its paired reload cell too
1AE3: C9              RET                         

; lay out the object array's twenty-three records, sixteen bytes apart
; from a fixed start: clear each record's occupancy byte and stamp its
; sixteenth byte with that record's position in the run, counting from
; one. Nothing is read, so the run comes out the same however it went in
freeAndNumberEveryObjectSlot:
1AE4: DD 21 10 A8     LD      IX,$A810            ; point at the first object record
1AE8: 3E 01           LD      A,$01               ; record numbers start at one
1AEA: 06 17           LD      B,$17               ; twenty-three records
1AEC: 11 10 00        LD      DE,$0010            ; sixteen bytes apart

loc_1aef:
1AEF: DD 36 00 00     LD      (IX+$00),$00        ; clear this record's occupancy byte
1AF3: DD 77 0F        LD      (IX+$0F),A          ; stamp its number into its sixteenth byte
1AF6: 3C              INC     A                   ; count on to the next number
1AF7: DD 19           ADD     IX,DE               
1AF9: 10 F4           DJNZ    $1AEF               ; {code.loc_1aef} loop over all twenty-three
1AFB: C9              RET                         

; take what is currently showing at one character cell -- its glyph byte
; and the colour byte of the same cell -- and lay the two down side by
; side as a two-byte record. One pointer reaches both planes because they
; hold the same grid at the same offset and are told apart by a single
; address bit. The cell itself is not touched, so what the caller gets is
; a reading and not a reservation
sampleCellGlyphAndColour:
1AFC: 7E              LD      A,(HL)              ; read the cell's glyph
1AFD: 12              LD      (DE),A              ; store it into the record
1AFE: 13              INC     DE                  
1AFF: CB 94           RES     2,H                 ; flip the pointer to the colour plane
1B01: 7E              LD      A,(HL)              ; read the same cell's colour
1B02: 12              LD      (DE),A              ; store it beside the glyph
1B03: C9              RET                         

; ---- $1B04-$1ED0: data ----
1B04: B1 1B BB 1B C5 1B CF 1B D9 1B E3 1B ED 1B F7 1B
1B14: 01 1C 0B 1C 15 1C 1F 1C 29 1C 33 1C 3D 1C 47 1C
1B24: 51 1C 5B 1C 65 1C 6F 1C 79 1C 83 1C 8D 1C 97 1C
1B34: A1 1C AB 1C B5 1C BF 1C C9 1C D3 1C DD 1C E7 1C
1B44: F1 1C FB 1C 05 1D 0F 1D 19 1D 23 1D 2D 1D 37 1D
1B54: 41 1D 4B 1D 55 1D 5F 1D 69 1D 73 1D 7D 1D 87 1D
1B64: 91 1D 9B 1D A5 1D AF 1D B9 1D C3 1D CD 1D D7 1D
1B74: E1 1D EB 1D F5 1D FF 1D 09 1E 13 1E 1D 1E 27 1E
1B84: 31 1E 3B 1E 45 1E 4F 1E 59 1E 63 1E 6D 1E 77 1E
1B94: 81 1E 8B 1E 95 1E 9F 1E A9 1E B3 1E BD 1E C7 1E
1BA4: 5F A5 13 00 D7 34 34 F1 88 57 A5 BF B9 00 20 50
1BB4: 3C 04 50 00 50 18 5A 01 20 4E 3C 04 50 00 4E 18
1BC4: 54 01 28 4C 32 05 60 01 4C 1C 4E 02 28 48 28 05
1BD4: 60 01 48 1C 48 02 30 46 1E 06 70 01 46 1C 42 03
1BE4: 30 44 1E 06 70 02 44 20 3C 03 38 42 1E 06 80 02
1BF4: 42 20 36 03 38 40 1E 06 80 02 40 20 30 04 40 3F
1C04: 1E 07 90 03 3F 24 2A 04 40 3E 1E 07 90 03 3E 24
1C14: 24 04 40 3D 1E 07 A0 03 3D 24 1E 04 40 3C 1E 07
1C24: B0 03 3C 28 1E 04 48 3B 1E 07 C0 03 3B 28 1E 04
1C34: 48 3A 1E 07 D0 03 3A 2C 1E 04 48 39 1E 07 E0 03
1C44: 39 30 1E 04 48 38 19 07 F0 03 38 30 19 01 28 48
1C54: 32 05 50 01 5C 00 1E 01 28 48 28 05 50 01 5A 00
1C64: 1E 02 30 48 1E 05 60 01 58 00 1E 02 30 48 1E 06
1C74: 60 01 56 00 1E 02 30 48 1E 06 70 02 54 00 1E 03
1C84: 38 40 1E 06 70 02 52 00 1E 03 38 40 1E 06 80 02
1C94: 50 00 1E 03 38 40 1E 06 80 02 4C 00 1E 04 40 40
1CA4: 1E 07 90 02 4C 00 1E 04 40 40 1E 07 90 02 48 00
1CB4: 1E 04 48 38 1E 07 A0 02 48 00 1E 04 48 38 1E 07
1CC4: B0 02 48 00 1E 04 48 38 1E 07 C0 02 48 00 1E 04
1CD4: 48 38 1E 07 D0 02 48 00 1E 04 50 38 1E 07 E0 02
1CE4: 48 00 1E 04 58 30 19 07 F0 02 48 00 19 01 20 50
1CF4: 32 03 50 01 50 08 1E 01 20 50 28 04 50 01 50 08
1D04: 1E 01 20 50 1E 04 60 01 50 0C 1E 01 28 50 1E 04
1D14: 60 02 50 0C 1E 01 28 48 1E 05 70 02 48 10 1E 01
1D24: 28 48 1E 05 80 02 48 10 1E 01 30 48 1E 05 90 03
1D34: 48 14 1E 01 30 48 1E 06 A0 03 48 14 1E 02 30 40
1D44: 1E 06 B0 03 40 18 1E 02 38 40 1E 06 C0 03 40 18
1D54: 1E 02 38 40 1E 06 D0 03 40 18 1E 02 38 40 1E 06
1D64: D0 03 40 18 1E 02 40 38 1E 06 E0 03 38 18 1E 02
1D74: 48 38 1E 06 E0 03 38 18 1E 02 50 38 1E 06 F0 03
1D84: 38 18 1E 03 58 30 19 07 F0 03 30 18 19 01 20 50
1D94: 1E 04 60 01 50 00 1E 01 20 50 1E 04 70 01 50 00
1DA4: 1E 01 28 50 1E 04 80 01 50 00 1E 01 28 50 1E 05
1DB4: 90 02 50 00 1E 01 30 48 1E 05 A0 02 48 00 1E 01
1DC4: 30 48 1E 05 B0 02 48 00 1E 01 38 48 1E 05 C0 03
1DD4: 48 00 1E 01 38 48 1E 06 D0 03 48 00 1E 01 40 40
1DE4: 1E 06 E0 03 40 00 1E 01 40 40 1E 06 F0 03 40 00
1DF4: 1E 01 48 40 1E 06 F0 03 40 00 1E 01 48 40 1E 06
1E04: F0 03 40 00 1E 01 50 38 1E 06 F0 03 38 00 1E 01
1E14: 50 38 1E 06 F0 03 38 00 1E 01 58 38 1E 06 F0 03
1E24: 38 00 1E 01 58 30 19 06 F0 03 30 00 19 01 20 50
1E34: 5A 03 00 01 58 3C 64 01 20 50 5A 03 10 01 54 46
1E44: 5A 01 28 50 50 04 20 01 52 50 50 01 28 50 46 04
1E54: 30 02 50 5A 46 01 30 48 46 04 40 02 4E 64 46 01
1E64: 30 48 3C 05 50 02 4B 6E 3C 01 38 48 3C 05 60 03
1E74: 48 78 3C 01 38 40 32 05 70 03 46 82 3C 01 40 40
1E84: 32 05 80 03 44 8C 32 01 40 40 28 05 90 03 44 96
1E94: 32 01 48 40 28 05 A0 03 42 A0 32 01 48 3C 1E 05
1EA4: B0 03 42 AA 28 01 50 3C 1E 05 C0 03 40 B4 28 01
1EB4: 50 3C 1E 05 D0 03 3C BE 28 01 58 38 1E 05 E0 03
1EC4: 38 C8 1E 01 58 30 19 05 F0 03 34 D2 19

; hand back the control word of whichever cabinet panel currently faces
; the picture
readPlayerControls:
1ED1: 3A 87 A9        LD      A,($A987)           ; {hard.workRam+187} read the screen-orientation flag
1ED4: A7              AND     A                   
1ED5: 21 AF A9        LD      HL,$A9AF            ; point at the first panel's control mirror
1ED8: 20 03           JR      NZ,$1EDD            ; {code.loc_1edd} unflipped: use that panel
1EDA: 21 B0 A9        LD      HL,$A9B0            ; flipped: use the second panel's mirror

loc_1edd:
1EDD: 7E              LD      A,(HL)              ; hand back the chosen panel's control word
1EDE: C9              RET                         

; seat the player record (ix=0xa800) and its paired sprite entry
; (iy=0xaa10), then branch on the player-state byte 0xa800: return while
; it is 0, run the tile-animation step (0x2010) while it is any other
; non-0xff value, and once it is 0xff either fly the attract demo pilot
; (0x214b when PLAY_ACTIVE 0xad30 is 0), turn the ship toward the read
; control stick (0x1f01 when the low control nibble is nonzero), or just
; scroll the world (0x1f42) when the stick is centred
dispatchPlayerFrameByState:
1EDF: DD 21 00 A8     LD      IX,$A800            ; point at the player record
1EE3: FD 21 10 AA     LD      IY,$AA10            ; and its paired sprite entry
1EE7: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player state
1EEA: A7              AND     A                   
1EEB: C8              RET     Z                   ; state clear: nothing to do this frame
1EEC: 3C              INC     A                   
1EED: C2 10 20        JP      NZ,$2010            ; {code.advancePlayerAnimationStrip} mid-count: run the multi-frame animation
1EF0: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} read the play-active flag
1EF3: A7              AND     A                   
1EF4: CA 4B 21        JP      Z,$214B             ; {code.flyDemoShipByScript} not in play: fly the attract-demo pilot
1EF7: CD D1 1E        CALL    $1ED1               ; {code.readPlayerControls} read the panel controls
1EFA: E6 0F           AND     $0F                 ; keep the stick nibble
1EFC: 20 03           JR      NZ,$1F01            ; {code.turnShipTowardTargetHeading} stick pushed: turn the ship toward it
1EFE: C3 42 1F        JP      $1F42               ; {code.scrollWorldAtTheEraPace} stick centred: just scroll the world

; steer the ship one notch toward the wanted heading a table selects
; (leave it when already there, snap on when within one notch, else step
; the short way round the compass by three notches — four once the era's
; low digit reaches three), then fall into the shared world-scroll tail
turnShipTowardTargetHeading:
1F01: 21 2E 1F        LD      HL,$1F2E            ; point at the wanted-heading table
1F04: CF              RST     $08                 ; look up the heading the stick asks for
1F05: 47              LD      B,A                 ; hold that wanted heading
1F06: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} take the ship's current heading
1F09: 90              SUB     B                   ; subtract it -- how far from the target
1F0A: CA 42 1F        JP      Z,$1F42             ; {code.scrollWorldAtTheEraPace} already there: just scroll the world
1F0D: 4F              LD      C,A                 ; hold the difference
1F0E: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era number
1F11: E6 0F           AND     $0F                 
1F13: FE 03           CP      $03                 ; from the third era on, turns step faster
1F15: 30 04           JR      NC,$1F1B            ; {code.loc_1f1b}
1F17: 16 03           LD      D,$03               ; three notches a turn
1F19: 18 02           JR      $1F1D               ; {code.loc_1f1d}

loc_1f1b:
1F1B: 16 04           LD      D,$04               ; four notches a turn

loc_1f1d:
1F1D: 79              LD      A,C                 
1F1E: C6 01           ADD     A,$01               
1F20: FE 03           CP      $03                 
1F22: DA 3E 1F        JP      C,$1F3E             ; {code.snapHeadingOntoTheTurnTarget} within one notch: snap straight onto the target
1F25: 79              LD      A,C                 
1F26: FE 80           CP      $80                 ; is the target the short way ahead?
1F28: D2 6F 1F        JP      NC,$1F6F            ; {code.loc_1f6f} ahead: step the heading up a notch
1F2B: C3 68 1F        JP      $1F68               ; {code.loc_1f68} behind: step the heading down a notch

loc_1f2e:
1F2E: 00              NOP                         
1F2F: 00              NOP                         
1F30: 80              ADD     A,B                 
1F31: 00              NOP                         
1F32: C0              RET     NZ                  
1F33: E0              RET     PO                  
1F34: A0              AND     B                   
1F35: 00              NOP                         
1F36: 40              LD      B,B                 
1F37: 20 60           JR      NZ,$1F99            ; {code.loc_1f99}
1F39: 00              NOP                         
1F3A: 00              NOP                         
1F3B: 00              NOP                         
1F3C: 00              NOP                         
1F3D: 00              NOP                         

; end a turn by writing the heading the turn was steering toward straight
; into the player's heading cell, then fall into the world scroll every
; arm of the turn reaches; the target arrives in a register and nothing is
; read, so the whole of the entry is that one store
snapHeadingOntoTheTurnTarget:
1F3E: 78              LD      A,B                 ; take the heading the turn was steering toward
1F3F: 32 02 A8        LD      ($A802),A           ; {hard.workRam+2} write it straight onto the ship's heading

; move the world past the ship at the pace the era sets, READING the
; heading rather than deciding it -- some paths in write it first, others
; arrive with whatever is already there: one of three fixed sample tables
; is picked from ERA_INDEX alone -- the opening era its own, the next two
; sharing a second, everything from the third era up sharing a third --
; and the pair that table gives for the ship's heading is handed on to be
; negated into the world scroll cells. Choosing the table is the whole of
; what this entry decides
scrollWorldAtTheEraPace:
1F42: 21 55 1F        LD      HL,$1F55            ; the negate-into-scroll tail
1F45: E5              PUSH    HL                  ; push it as the return address
1F46: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era number
1F49: A7              AND     A                   
1F4A: CA 4E 59        JP      Z,$594E             ; {code.loc_594e} opening era: use its own velocity table
1F4D: FE 03           CP      $03                 
1F4F: DA 65 59        JP      C,$5965             ; {code.loc_5965} the next two eras share a second table
1F52: C3 6B 59        JP      $596B               ; {code.loc_596b} the third era on shares the last table

; ---- $1F55-$1F67: data ----
1F55: AF 67 6F ED 52 22 08 A8 AF 67 6F ED 42 22 0A A8
1F65: C3 AF 20

loc_1f68:
1F68: 92              SUB     D                   
1F69: 80              ADD     A,B                 
1F6A: 32 02 A8        LD      ($A802),A           ; {hard.workRam+2} store the heading stepped one notch down
1F6D: 18 D3           JR      $1F42               ; {code.scrollWorldAtTheEraPace} re-run the world scroll

loc_1f6f:
1F6F: 82              ADD     A,D                 
1F70: 80              ADD     A,B                 
1F71: 32 02 A8        LD      ($A802),A           ; {hard.workRam+2} store the heading stepped one notch up
1F74: 18 CC           JR      $1F42               ; {code.scrollWorldAtTheEraPace} re-run the world scroll

; ---- $1F76-$1F98: data ----
1F76: F1 F1 F1 F1 F1 F1 F1 DD F1 F1 F1 F1 F0 F1 F1 F1
1F86: F1 C3 F1 F1 F1 F1 EA F1 F1 F1 F1 F1 F1 F1 F1 F1
1F96: B7 F1 F1

loc_1f99:
1F99: F1              POP     AF                  
1F9A: F1              POP     AF                  
1F9B: 4D              LD      C,L                 
1F9C: F1              POP     AF                  
1F9D: F1              POP     AF                  
1F9E: F1              POP     AF                  
1F9F: E5              PUSH    HL                  
1FA0: 2D              DEC     L                   
1FA1: 6E              LD      L,(HL)              
1FA2: F1              POP     AF                  
1FA3: F1              POP     AF                  
1FA4: 5E              LD      E,(HL)              
1FA5: 61              LD      H,C                 
1FA6: E6 F1           AND     $F1                 
1FA8: F1              POP     AF                  
1FA9: F1              POP     AF                  
1FAA: B2              OR      D                   
1FAB: F1              POP     AF                  

; ---- $1FAC-$200B: data ----
1FAC: F1 F1 F1 53 F1 F1 F1 F1 95 F1 F1 F1 45 CA F1 F1
1FBC: F1 C6 2C 97 F1 F1 81 69 1E F1 F1 BC A1 60 F1 F1
1FCC: F4 EB F1 F1 F1 F1 48 F1 F1 F1 E0 63 35 F1 F1 AA
1FDC: B4 8A F1 F1 51 E9 F6 F1 F1 82 92 98 F1 F1 F1 46
1FEC: F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1
1FFC: F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1 F1

; put the byte the caller has been carrying where a result is read from,
; so the verdict of an image check can be taken; on the way it walks an
; address forward twice, by a wide step and then by that same byte, and
; the address it lands on is never dereferenced by anything downstream. It
; reads and writes no memory, so the walk is arithmetic and not a fetch
presentChecksumForTamperTest:
200C: 19              ADD     HL,DE               ; walk the address on by a wide step
200D: DF              RST     $18                 ; walk it on again by the byte in hand
200E: 78              LD      A,B                 ; put the carried count where the tamper check reads its verdict
200F: C9              RET                         

; advance a phase-byte-driven tile animation: on the first frame
; (phase>=0xb4) clamp the phase, flag the paired entry, and cue sounds
; (56d2 always, 5679 past level 2) unless two game-state cells divert to
; $1F2E; else step the phase down and, on one of seven keyframe values,
; blit a 5x6 shape strip into video+colour RAM
advancePlayerAnimationStrip:
2010: DD 7E 00        LD      A,(IX+$00)          ; read the animation phase from the record
2013: FE B4           CP      $B4                 ; at or past the opening frame?
2015: 38 29           JR      C,$2040             ; {code.loc_2040} mid-animation: step the phase down
2017: DD 36 00 B4     LD      (IX+$00),$B4        ; clamp the phase to the opening frame
201B: FD 36 01 FF     LD      (IY+$01),$FF        ; flag the paired sprite entry
201F: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era number
2022: FE 02           CP      $02                 
2024: D4 79 56        CALL    NC,$5679            ; {code.requestLateEraProgressSound} past the second era: cue the extra progress sound
2027: CD D2 56        CALL    $56D2               ; {code.requestRoundIntroSoundBurst} cue the round-intro sound burst
202A: 3A FE AB        LD      A,($ABFE)           ; {hard.workRam+3FE} read a game-state cell
202D: FE A5           CP      $A5                 ; is it the running value?
202F: C2 63 20        JP      NZ,$2063            ; {code.loc_2063} no: divert to the shared exit
2032: 11 FF AB        LD      DE,$ABFF            
2035: 1A              LD      A,(DE)              ; read the next state cell
2036: FE 05           CP      $05                 
2038: CA 40 20        JP      Z,$2040             ; {code.loc_2040} one accepted value: go straight to the draw
203B: FE 10           CP      $10                 
203D: C2 63 20        JP      NZ,$2063            ; {code.loc_2063} anything but the two accepted values: divert

loc_2040:
2040: DD 35 00        DEC     (IX+$00)            ; step the phase down one
2043: DD 7E 00        LD      A,(IX+$00)          ; read the stepped phase
2046: FE B3           CP      $B3                 ; a keyframe value? -- pick its shape strip
2048: 28 1C           JR      Z,$2066             ; {code.loc_2066}
204A: FE AB           CP      $AB                 ; another keyframe value
204C: 28 1D           JR      Z,$206B             ; {code.loc_206b}
204E: FE A3           CP      $A3                 ; another keyframe value
2050: 28 1E           JR      Z,$2070             ; {code.loc_2070}
2052: FE 9B           CP      $9B                 ; another keyframe value
2054: 28 1F           JR      Z,$2075             ; {code.loc_2075}
2056: FE 93           CP      $93                 ; another keyframe value
2058: 28 20           JR      Z,$207A             ; {code.loc_207a}
205A: FE 8B           CP      $8B                 ; another keyframe value
205C: 28 21           JR      Z,$207F             ; {code.loc_207f}
205E: FE 83           CP      $83                 ; the last keyframe value
2060: 28 22           JR      Z,$2084             ; {code.loc_2084}
2062: C9              RET                         ; none matched -- between keyframes, draw nothing

loc_2063:
2063: C3 2E 1F        JP      $1F2E               ; {code.loc_1f2e} divert to the shared exit

loc_2066:
2066: 11 76 1F        LD      DE,$1F76            ; select this keyframe's shape strip
2069: 18 1E           JR      $2089               ; {code.loc_2089}

loc_206b:
206B: 11 94 1F        LD      DE,$1F94            ; select this keyframe's shape strip
206E: 18 19           JR      $2089               ; {code.loc_2089}

loc_2070:
2070: 11 B2 1F        LD      DE,$1FB2            ; select this keyframe's shape strip
2073: 18 14           JR      $2089               ; {code.loc_2089}

loc_2075:
2075: 11 D0 1F        LD      DE,$1FD0            ; select this keyframe's shape strip
2078: 18 0F           JR      $2089               ; {code.loc_2089}

loc_207a:
207A: 11 D0 1F        LD      DE,$1FD0            ; select this keyframe's shape strip
207D: 18 0A           JR      $2089               ; {code.loc_2089}

loc_207f:
207F: 11 B2 1F        LD      DE,$1FB2            ; select this keyframe's shape strip
2082: 18 05           JR      $2089               ; {code.loc_2089}

loc_2084:
2084: 11 EE 1F        LD      DE,$1FEE            ; select this keyframe's shape strip
2087: 18 00           JR      $2089               ; {code.loc_2089}

loc_2089:
2089: 21 AF A5        LD      HL,$A5AF            ; the strip's first cell in video memory
208C: 06 C1           LD      B,$C1               ; the colour-attribute bias
208E: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504}
2091: 80              ADD     A,B                 ; the era offsets the strip's colour
2092: 4F              LD      C,A                 
2093: D9              EXX                         
2094: 3A 7A 33        LD      A,($337A)           ; {hard.rom+337A} the strip's row count
2097: 47              LD      B,A                 

loc_2098:
2098: D9              EXX                         
2099: 3A 02 49        LD      A,($4902)           ; {hard.rom+4902} the tiles-per-row count
209C: 47              LD      B,A                 

loc_209d:
209D: 1A              LD      A,(DE)              ; read a tile from the strip
209E: 77              LD      (HL),A              ; write it into video memory
209F: CB 94           RES     2,H                 ; aim at the colour plane
20A1: 71              LD      (HL),C              ; lay its colour attribute alongside in colour memory
20A2: CB D4           SET     2,H                 
20A4: 23              INC     HL                  
20A5: 13              INC     DE                  
20A6: 10 F5           DJNZ    $209D               ; {code.loc_209d} across the row's tiles
20A8: 3E 1B           LD      A,$1B               ; the step from a row's end to the next row's start
20AA: DF              RST     $18                 ; carry the cursor on to the next row
20AB: D9              EXX                         
20AC: 10 EA           DJNZ    $2098               ; {code.loc_2098} down all the rows
20AE: C9              RET                         

; dress the player's own sprite entry to face the way the ship is heading:
; round the heading byte to the nearest of thirty-two equal sectors and
; write the shape and the byte beside it straight into the entry, from two
; parallel thirty-two-entry tables in the program image. The entry and
; both tables are fixed here, so nothing about which object this is comes
; from the caller
dressPlayerSpriteForHeading:
20AF: DD 21 00 A8     LD      IX,$A800            
20B3: 11 20 00        LD      DE,$0020            ; the stride to the paired attribute table
20B6: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} take the ship's heading
20B9: C6 04           ADD     A,$04               ; round it to the nearest of thirty-two sectors
20BB: 0F              RRCA                        
20BC: 0F              RRCA                        
20BD: 0F              RRCA                        
20BE: E6 1F           AND     $1F                 ; keep the five-bit sector number
20C0: 21 CE 20        LD      HL,$20CE            ; point at the shape-by-sector table
20C3: DF              RST     $18                 ; index it by the sector
20C4: 7E              LD      A,(HL)              
20C5: 32 11 AA        LD      ($AA11),A           ; {hard.workRam+211} write the sprite shape for this heading
20C8: 19              ADD     HL,DE               ; step to the paired attribute table
20C9: 7E              LD      A,(HL)              
20CA: 32 40 AA        LD      ($AA40),A           ; {hard.workRam+240} write the attribute byte beside it
20CD: C9              RET                         

; ---- $20CE-$210D: data ----
20CE: F0 F1 F2 F3 F4 F5 F6 F7 E8 F7 F6 F5 F4 F3 F2 F1
20DE: F0 EF EE ED EC EB EA E9 E8 E9 EA EB EC ED EE EF
20EE: 40 40 40 40 40 40 40 40 80 C0 C0 C0 C0 C0 C0 C0
20FE: C0 C0 C0 C0 C0 C0 C0 C0 40 40 40 40 40 40 40 40

; seeds the attract-demo autopilot: picks a heading-command script by the
; demo selector (0xad14), writes its dwell counter to 0xadf2 and little-
; endian pointer to 0xadf3/4, then on a failed tile-image tamper readback
; (0xadfb/0xadfc) tail-jumps into the trap
seedDemoAutopilotScript:
210E: 21 F3 AD        LD      HL,$ADF3            ; point at the script-pointer cell
2111: EB              EX      DE,HL               
2112: 3A 14 AD        LD      A,($AD14)           ; {hard.workRam+514} read the demo selector
2115: A7              AND     A                   
2116: 28 28           JR      Z,$2140             ; {code.loc_2140} selector 0: take the first script
2118: FE 03           CP      $03                 
211A: 28 24           JR      Z,$2140             ; {code.loc_2140} selector 3: take the first script too
211C: FE 01           CP      $01                 
211E: 28 25           JR      Z,$2145             ; {code.loc_2145} selector 1: take the second script
2120: 21 FA 22        LD      HL,$22FA            ; otherwise take the third script

loc_2123:
2123: 7E              LD      A,(HL)              ; read the script's leading byte
2124: 3C              INC     A                   
2125: 32 F2 AD        LD      ($ADF2),A           ; {hard.workRam+5F2} seat the dwell counter to one past it
2128: EB              EX      DE,HL               
2129: 73              LD      (HL),E              ; store the script pointer -- low byte
212A: 2C              INC     L                   
212B: 72              LD      (HL),D              ; -- then high byte
212C: 21 FB AD        LD      HL,$ADFB            ; point at the glyph tamper-readback cell
212F: 7E              LD      A,(HL)              
2130: FE FD           CP      $FD                 ; does the glyph readback look tampered?
2132: C2 3D 21        JP      NZ,$213D            ; {code.loc_213d} yes: drop into the trap
2135: 23              INC     HL                  
2136: 7E              LD      A,(HL)              
2137: FE 10           CP      $10                 ; an untampered colour readback returns
2139: C8              RET     Z                   
213A: FE 05           CP      $05                 ; the other accepted colour returns
213C: C8              RET     Z                   

loc_213d:
213D: C3 51 22        JP      $2251               ; {code.loc_2251} otherwise drop into the trap

loc_2140:
2140: 21 8C 21        LD      HL,$218C            ; the first script's address
2143: 18 DE           JR      $2123               ; {code.loc_2123}

loc_2145:
2145: 21 51 22        LD      HL,$2251            ; the second script's address
2148: 18 D9           JR      $2123               ; {code.loc_2123}

; ---- $214A-$214A: data ----
214A: C9

; attract demo auto-pilot step: ticks the packed dwell/turn countdown at
; 0xadf2, steps the heading-command script at 0xadf3/4 when the dwell
; expires, turns PLAYER_HEADING (0xa802) by the 2-bit command, then tail-
; jumps to the mover at 0x1f42
flyDemoShipByScript:
214B: 21 F2 AD        LD      HL,$ADF2            ; point at the demo pilot's countdown byte -- low six bits are a dwell, the top two a turn command
214E: 7E              LD      A,(HL)              ; read it
214F: 47              LD      B,A                 ; keep the whole byte so the turn command in the top bits survives the mask
2150: E6 3F           AND     $3F                 ; isolate the dwell in the low six bits
2152: 28 07           JR      Z,$215B             ; {code.loc_215b} dwell spent -- step to the next script entry
2154: 3D              DEC     A                   
2155: 28 04           JR      Z,$215B             ; {code.loc_215b} a single remaining tick counts as spent too -- step the script
2157: 05              DEC     B                   ; tick the dwell down one frame
2158: 70              LD      (HL),B              ; store the counted-down command byte back
2159: 18 0F           JR      $216A               ; {code.loc_216a} act on this frame's turn command

loc_215b:
215B: 23              INC     HL                  ; step to the script pointer that follows the countdown byte
215C: 5E              LD      E,(HL)              ; read the script pointer low
215D: 23              INC     HL                  
215E: 56              LD      D,(HL)              ; read the script pointer high
215F: 13              INC     DE                  ; advance the pointer one entry along the script
2160: 72              LD      (HL),D              ; store the pointer high back
2161: 2B              DEC     HL                  
2162: 73              LD      (HL),E              ; store the pointer low back
2163: EB              EX      DE,HL               
2164: 7E              LD      A,(HL)              ; read the next script entry
2165: 1B              DEC     DE                  
2166: 3C              INC     A                   ; bias it up by one so a fully-spent entry loops around again
2167: 12              LD      (DE),A              ; write it into the countdown byte
2168: 18 E1           JR      $214B               ; {code.flyDemoShipByScript} re-examine the countdown

loc_216a:
216A: 78              LD      A,B                 ; take the command byte
216B: D9              EXX                         ; switch to the alternate register bank the world-scroll mover runs on
216C: 07              RLCA                        
216D: 07              RLCA                        ; rotate the two turn-command bits down to the bottom
216E: E6 03           AND     $03                 ; isolate the turn command
2170: CA 42 1F        JP      Z,$1F42             ; {code.scrollWorldAtTheEraPace} no turn this frame -- hand straight to the world-scroll mover
2173: 3D              DEC     A                   
2174: 28 0B           JR      Z,$2181             ; {code.loc_2181} turn command one steers one way -- branch off to turn the heading down
2176: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} otherwise steer the other way: read the ship heading
2179: C6 03           ADD     A,$03               ; turn it by three
217B: 32 02 A8        LD      ($A802),A           ; {hard.workRam+2} store the new heading
217E: C3 42 1F        JP      $1F42               ; {code.scrollWorldAtTheEraPace} hand to the world-scroll mover

loc_2181:
2181: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the ship heading
2184: D6 03           SUB     $03                 ; turn it three the other way
2186: 32 02 A8        LD      ($A802),A           ; {hard.workRam+2} store the new heading
2189: C3 42 1F        JP      $1F42               ; {code.scrollWorldAtTheEraPace} hand to the world-scroll mover

; ---- $218C-$2249: data ----
218C: 3C 3C 3C 3C 0B 95 03 66 95 7C 59 8D 4B 8E 4A 02
219C: 8B 1A 55 0E 8A 7C 4E 05 8A 0B 86 46 03 4A 0D 7C
21AC: 5A 36 AB 08 55 08 56 01 4A 05 56 03 7C 4D BC 83
21BC: 0A 4B 07 BC 81 72 02 56 02 6A 01 95 3B 88 53 03
21CC: BC 95 46 0B 95 04 A0 0C 4A 02 56 03 55 01 95 03
21DC: 4A 04 8A 02 4A 02 8A 29 8B 06 4B 16 4A 01 95 0D
21EC: 88 53 01 6A 0F 8A 08 8B 0D 4B 08 8B 07 55 02 69
21FC: 89 03 4B 01 7C 6F 05 8B 4B 0D 8B 01 4E 83 01 8B
220C: 0F 55 05 A2 42 10 60 26 4B 02 8B 08 4B 05 8F 4F
221C: 01 95 17 4A 0E 8A 04 A0 1B 8B 11 4B 0A 52 97 4D
222C: 8F 47 06 8B 02 55 03 9D 67 8A 0A 56 05 8B 02 48
223C: 88 03 55 09 60 03 76 13 8B 24 4B 2F 8B 05

loc_224a:
224A: 8B              ADC     A,E                 
224B: 08              EX      AF,AF'              
224C: 8A              ADC     A,D                 
224D: 15              DEC     D                   
224E: 96              SUB     (HL)                
224F: 3C              INC     A                   
2250: 3C              INC     A                   

loc_2251:
2251: 3C              INC     A                   
2252: 3C              INC     A                   
2253: 3C              INC     A                   
2254: 3C              INC     A                   
2255: 0A              LD      A,(BC)              
2256: 95              SUB     L                   
2257: 60              LD      H,B                 
2258: 04              INC     B                   
2259: 9E              SBC     A,(HL)              
225A: 53              LD      D,E                 
225B: 0D              DEC     C                   
225C: 8B              ADC     A,E                 
225D: 02              LD      (BC),A              
225E: 4B              LD      C,E                 
225F: 0F              RRCA                        
2260: 93              SUB     E                   
2261: 53              LD      D,E                 
2262: 07              RLCA                        
2263: A9              XOR     C                   
2264: 54              LD      D,H                 
2265: 0A              LD      A,(BC)              
2266: 96              SUB     (HL)                
2267: 03              INC     BC                  
2268: 60              LD      H,B                 
2269: 0F              RRCA                        
226A: 8A              ADC     A,D                 
226B: 23              INC     HL                  
226C: 48              LD      C,B                 
226D: B9              CP      C                   
226E: 02              LD      (BC),A              
226F: 82              ADD     A,D                 
2270: 59              LD      E,C                 
2271: 9F              SBC     A,A                 
2272: 59              LD      E,C                 
2273: 01 8B 22        LD      BC,$228B            
2276: AB              XOR     E                   
2277: 02              LD      (BC),A              
2278: 4B              LD      C,E                 
2279: 02              LD      (BC),A              
227A: 8B              ADC     A,E                 
227B: 07              RLCA                        
227C: 55              LD      D,L                 
227D: AC              XOR     H                   
227E: 42              LD      B,D                 
227F: 01 50 90        LD      BC,$9050            
2282: 02              LD      (BC),A              
2283: 55              LD      D,L                 
2284: 35              DEC     (HL)                
2285: 90              SUB     B                   
2286: 50              LD      D,B                 
2287: 04              INC     B                   
2288: 92              SUB     D                   
2289: 5B              LD      E,E                 
228A: 89              ADC     A,C                 
228B: 1F              RRA                         
228C: 48              LD      C,B                 
228D: 88              ADC     A,B                 
228E: 05              DEC     B                   
228F: 8C              ADC     A,H                 
2290: 42              LD      B,D                 
2291: 05              DEC     B                   
2292: 4A              LD      C,D                 
2293: 3C              INC     A                   
2294: 0C              INC     C                   
2295: 46              LD      B,(HL)              
2296: 86              ADD     A,(HL)              
2297: 3C              INC     A                   
2298: 04              INC     B                   
2299: 93              SUB     E                   
229A: 5E              LD      E,(HL)              
229B: 06 4B           LD      B,$4B               
229D: 09              ADD     HL,BC               
229E: 4A              LD      C,D                 
229F: 0A              LD      A,(BC)              
22A0: 7C              LD      A,H                 
22A1: 7C              LD      A,H                 
22A2: 6F              LD      L,A                 
22A3: BC              CP      H                   
22A4: 01 8B 07        LD      BC,$078B            
22A7: 92              SUB     D                   
22A8: 48              LD      C,B                 
22A9: 07              RLCA                        
22AA: 88              ADC     A,B                 
22AB: 7C              LD      A,H                 
22AC: 7C              LD      A,H                 
22AD: 45              LD      B,L                 
22AE: 11 90 50        LD      DE,$5090            
22B1: 01 8B 07        LD      BC,$078B            
22B4: 4B              LD      C,E                 
22B5: 0C              INC     C                   
22B6: 8B              ADC     A,E                 
22B7: 0A              LD      A,(BC)              
22B8: 76              HALT                        
22B9: AB              XOR     E                   
22BA: 12              LD      (DE),A              
22BB: 87              ADD     A,A                 
22BC: 47              LD      B,A                 
22BD: 18 8B           JR      $224A               ; {code.loc_224a}

; ---- $22BF-$23E2: data ----
22BF: 03 8A 02 96 08 4B 02 8B 07 95 3C 3C 17 55 3C 05
22CF: 56 20 7C 44 06 67 BC 4D 8E 0C 56 02 4A 1A 4B 39
22DF: 55 25 56 20 55 0B 4B 03 60 06 4A 03 41 01 BC 9F
22EF: 50 04 96 0F 4B 07 8B 3C 3C 3C 3C 3C 3C 3C 3C 02
22FF: 90 45 02 4B 02 48 88 07 8A 55 01 4A 01 58 82 03
230F: 8A 5F 01 60 07 B2 52 03 46 86 1E 49 89 08 4B 01
231F: 94 49 05 8A 4A 3C 3C 0A BC 84 11 53 88 01 4A 0B
232F: 6B 06 4B 24 4A 11 56 08 4A 0E 4B 07 55 07 4B 07
233F: 7C 72 8E 01 AF 44 02 56 8B 04 5A 85 02 8A 02 90
234F: 45 09 8B 01 48 89 41 02 4B 05 B5 10 4D 83 03 B5
235F: 4B 03 A0 07 72 88 08 4B 01 50 85 03 8B 02 55 05
236F: 95 06 60 06 55 01 4B 09 48 8F 47 03 4B 01 96 07
237F: 8A 05 6A 18 4B 0A 8B 06 8A 02 44 84 06 8B 08 8B
238F: 14 BC 84 03 59 83 02 8B 03 60 08 8B 05 7C 5A 01
239F: B6 0A 48 95 4D 01 8A 09 51 BC 85 65 2D 6B 01 95
23AF: 4D 83 02 8A 4A 01 8B 02 72 85 53 01 95 02 8B 06
23BF: 95 03 8B 01 8A 01 4A 07 95 01 6B 03 97 41 05 4B
23CF: 0B 48 88 05 60 3C 3C 3C 3C 73 A6 14 7E 29 F8 9B
23DF: 13 13 96 B9

; fire and sweep the player's shots: on a fire-button rising edge arm and
; seed one shot into a free slot of the six-slot shot bank at 0xaa80 aimed
; along PLAYER_HEADING; then advance every live shot by the world scroll,
; queue its character-cell tiles, and cull any that leaves the field or
; holds a stale head
fireAndSweepPlayerShots:
23E3: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player-state marker
23E6: 3C              INC     A                   
23E7: C2 96 24        JP      NZ,$2496            ; {code.loc_2496} not alive -- skip firing and just sweep the live shots
23EA: 3A C6 AC        LD      A,($ACC6)           ; {hard.workRam+4C6} read the round-transition hold
23ED: A7              AND     A                   
23EE: C2 96 24        JP      NZ,$2496            ; {code.loc_2496} mid-transition -- skip firing and just sweep
23F1: CD D1 1E        CALL    $1ED1               ; {code.readPlayerControls} read the player controls
23F4: 07              RLCA                        ; rotate the fire-button bit out into carry -- four turns bring it around
23F5: 07              RLCA                        
23F6: 07              RLCA                        
23F7: 07              RLCA                        
23F8: 21 8E A9        LD      HL,$A98E            ; point at the fire-button edge history
23FB: CB 16           RL      (HL)                ; shift the fire bit into the two-frame history
23FD: 7E              LD      A,(HL)              
23FE: E6 03           AND     $03                 ; keep just the last two frames of it
2400: FE 01           CP      $01                 ; a value of one is a fresh press -- up last frame, down now
2402: 21 81 AA        LD      HL,$AA81            ; point at the pending-shot-burst count
2405: 20 02           JR      NZ,$2409            ; {code.loc_2409} no fresh press -- skip arming a burst
2407: 36 03           LD      (HL),$03            ; fire pressed -- arm a burst of three shots

loc_2409:
2409: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} read the play-active flag
240C: A7              AND     A                   
240D: 28 05           JR      Z,$2414             ; {code.loc_2414} attract/idle -- spawn a shot regardless
240F: 7E              LD      A,(HL)              ; in play: read the pending-burst count
2410: A7              AND     A                   
2411: CA 96 24        JP      Z,$2496             ; {code.loc_2496} nothing pending -- just sweep the live shots

loc_2414:
2414: 23              INC     HL                  ; step to the spawn cooldown
2415: 7E              LD      A,(HL)              
2416: A7              AND     A                   
2417: C2 96 24        JP      NZ,$2496            ; {code.loc_2496} still cooling down -- just sweep
241A: DD 21 80 AA     LD      IX,$AA80            ; point at the six-slot shot bank
241E: 06 06           LD      B,$06               ; six slots to scan

loc_2420:
2420: DD 7E 00        LD      A,(IX+$00)          ; read this slot's occupancy
2423: A7              AND     A                   
2424: 28 23           JR      Z,$2449             ; {code.loc_2449} free slot found -- seed a shot into it
2426: ED 5B 46 0D     LD      DE,($0D46)          ; {hard.rom+D46} take the slot stride from the program image
242A: DD 19           ADD     IX,DE               ; step to the next slot
242C: 10 F2           DJNZ    $2420               ; {code.loc_2420} scan all six
242E: C3 96 24        JP      $2496               ; {code.loc_2496} none free -- just sweep

; ---- $2431-$2448: data ----
2431: 16 A7 13 96 ED DC F1 8C 68 3B 0D ED F1 96 13 13
2441: 13 13 F1 88 DC ED 11 B9

loc_2449:
2449: CD 7E 56        CALL    $567E               ; {code.requestPlayerShotSound} ask for the player-shot sound
244C: AF              XOR     A                   
244D: 67              LD      H,A                 
244E: 6F              LD      L,A                 
244F: ED 4B 08 A8     LD      BC,($A808)          ; {hard.workRam+8} read the world scroll along one axis
2453: ED 42           SBC     HL,BC               ; negate it
2455: 29              ADD     HL,HL               
2456: 29              ADD     HL,HL               ; scale it up four times
2457: DD 75 0A        LD      (IX+$0A),L          ; seed the shot's sub-position from it
245A: DD 74 0B        LD      (IX+$0B),H          
245D: AF              XOR     A                   
245E: 67              LD      H,A                 
245F: 6F              LD      L,A                 
2460: ED 4B 0A A8     LD      BC,($A80A)          ; {hard.workRam+A} read the world scroll along the other axis
2464: ED 42           SBC     HL,BC               ; negate it
2466: 29              ADD     HL,HL               
2467: 29              ADD     HL,HL               ; scale it up four times
2468: DD 75 0C        LD      (IX+$0C),L          ; seed the shot's other sub-position
246B: DD 74 0D        LD      (IX+$0D),H          
246E: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the ship heading
2471: C6 04           ADD     A,$04               ; round the heading
2473: 0F              RRCA                        ; shift it down toward a direction index
2474: 0F              RRCA                        
2475: 0F              RRCA                        
2476: E6 1F           AND     $1F                 ; keep five bits -- one of thirty-two directions
2478: 21 71 27        LD      HL,$2771            ; point at the shot-velocity table
247B: CD 8C 01        CALL    $018C               ; {code.fetchWideTableWord} fetch the velocity word for this direction
247E: DD 35 00        DEC     (IX+$00)            ; mark the slot occupied
2481: DD 36 03 00     LD      (IX+$03),$00        
2485: DD 73 04        LD      (IX+$04),E          ; set the shot's speed along one axis
2488: DD 36 05 00     LD      (IX+$05),$00        
248C: DD 72 06        LD      (IX+$06),D          ; set the shot's speed along the other axis
248F: 21 81 AA        LD      HL,$AA81            ; point at the pending-burst count
2492: 35              DEC     (HL)                ; one shot fired -- count the burst down
2493: 23              INC     HL                  
2494: 36 06           LD      (HL),$06            ; reset the spawn cooldown to six frames

loc_2496:
2496: 3A 82 AA        LD      A,($AA82)           ; {hard.workRam+282} read the spawn cooldown
2499: A7              AND     A                   
249A: 28 04           JR      Z,$24A0             ; {code.loc_24a0} already zero -- skip the tick
249C: 3D              DEC     A                   ; count the cooldown down one frame
249D: 32 82 AA        LD      ($AA82),A           ; {hard.workRam+282}

loc_24a0:
24A0: DD 21 80 AA     LD      IX,$AA80            ; point at the six-slot shot bank
24A4: 06 06           LD      B,$06               ; six slots to sweep

loc_24a6:
24A6: D9              EXX                         
24A7: DD 7E 00        LD      A,(IX+$00)          ; read the slot's head byte
24AA: A7              AND     A                   
24AB: 28 46           JR      Z,$24F3             ; {code.loc_24f3} empty slot -- on to the next
24AD: 3C              INC     A                   
24AE: 20 4C           JR      NZ,$24FC            ; {code.loc_24fc} head is stale, not the live marker -- cull this shot
24B0: DD 6E 0A        LD      L,(IX+$0A)          ; read one coordinate of the shot
24B3: DD 66 0B        LD      H,(IX+$0B)          
24B6: ED 5B 08 A8     LD      DE,($A808)          ; {hard.workRam+8} add the world scroll to it
24BA: 19              ADD     HL,DE               
24BB: DD 56 04        LD      D,(IX+$04)          ; add the shot's stored offset
24BE: DD 5E 03        LD      E,(IX+$03)          
24C1: 19              ADD     HL,DE               
24C2: 7C              LD      A,H                 
24C3: C6 10           ADD     A,$10               ; bias the high byte for the edge test
24C5: FE 10           CP      $10                 
24C7: DA FC 24        JP      C,$24FC             ; {code.loc_24fc} off the field edge -- cull this shot
24CA: DD 74 04        LD      (IX+$04),H          ; store the advanced coordinate back
24CD: DD 75 03        LD      (IX+$03),L          
24D0: DD 6E 0C        LD      L,(IX+$0C)          ; read the other coordinate of the shot
24D3: DD 66 0D        LD      H,(IX+$0D)          
24D6: ED 5B 0A A8     LD      DE,($A80A)          ; {hard.workRam+A} add the world scroll to it
24DA: 19              ADD     HL,DE               
24DB: DD 56 06        LD      D,(IX+$06)          ; add the shot's stored offset
24DE: DD 5E 05        LD      E,(IX+$05)          
24E1: 19              ADD     HL,DE               
24E2: 7C              LD      A,H                 
24E3: C6 08           ADD     A,$08               ; bias for the edge test
24E5: FE 18           CP      $18                 
24E7: DA FC 24        JP      C,$24FC             ; {code.loc_24fc} off the field edge -- cull this shot
24EA: DD 74 06        LD      (IX+$06),H          ; store the advanced coordinate back
24ED: DD 75 05        LD      (IX+$05),L          
24F0: CD 37 53        CALL    $5337               ; {code.queueTileStampForObject} queue this shot's sprite tiles

loc_24f3:
24F3: 11 10 00        LD      DE,$0010            
24F6: DD 19           ADD     IX,DE               ; step to the next slot
24F8: D9              EXX                         
24F9: 10 AB           DJNZ    $24A6               ; {code.loc_24a6} sweep all six
24FB: C9              RET                         

loc_24fc:
24FC: AF              XOR     A                   
24FD: DD 77 00        LD      (IX+$00),A          ; clear the slot's head byte
2500: DD 77 04        LD      (IX+$04),A          ; clear its step along one axis
2503: DD 77 06        LD      (IX+$06),A          ; clear its step along the other axis
2506: C3 F3 24        JP      $24F3               ; {code.loc_24f3} on to the next slot

; ---- $2509-$2510: data ----
2509: E0 A4 14 9B 10 0D 88 B9

; cold-boot init: paints a 64-byte work-RAM block all-ones, seeds RNG /
; loads default high scores / empties the deferred lists (watchdog-kicking
; after each), then tail-jumps into the settings + cold-start chain
initColdStartRamThenSeedConfig:
2511: 21 00 AC        LD      HL,$AC00            ; point at a 64-byte work-RAM block
2514: 06 40           LD      B,$40               ; sixty-four bytes to paint

loc_2516:
2516: 36 FF           LD      (HL),$FF            ; set this byte all-ones
2518: 23              INC     HL                  
2519: 10 FB           DJNZ    $2516               ; {code.loc_2516} over all sixty-four
251B: CD 67 4B        CALL    $4B67               ; {code.seedRandomRegister} seed the random register
251E: 32 00 C2        LD      ($C200),A           ; kick the watchdog
2521: CD A5 4B        CALL    $4BA5               ; {code.loadDefaultHighScores} load the default high-score table
2524: 32 00 C2        LD      ($C200),A           ; kick the watchdog
2527: CD 6A 52        CALL    $526A               ; {code.emptyBothDeferredCellLists} empty both deferred-cell lists
252A: 32 00 C2        LD      ($C200),A           ; kick the watchdog
252D: C3 AA 52        JP      $52AA               ; {code.seedGameConfigFromDipSwitches} on into the settings and cold-start chain

loc_2530:
2530: 19              ADD     HL,DE               
2531: 01 18 01        LD      BC,$0118            
2534: 17              RLA                         
2535: 01 16 01        LD      BC,$0116            
2538: 15              DEC     D                   
2539: 01 14 01        LD      BC,$0114            
253C: 13              INC     DE                  
253D: 01 10 01        LD      BC,$0110            
2540: 0E 01           LD      C,$01               
2542: 0C              INC     C                   
2543: 01 0A 01        LD      BC,$010A            
2546: 08              EX      AF,AF'              
2547: 01 04 01        LD      BC,$0104            
254A: 01 01 FF        LD      BC,$FF01            
254D: 00              NOP                         
254E: FB              EI                          
254F: 00              NOP                         
2550: F8              RET     M                   
2551: 00              NOP                         
2552: F5              PUSH    AF                  
2553: 00              NOP                         
2554: F2 00 EE        JP      P,$EE00             
2557: 00              NOP                         
2558: EB              EX      DE,HL               
2559: 00              NOP                         
255A: E8              RET     PE                  
255B: 00              NOP                         
255C: E4 00 E1        CALL    PO,$E100            
255F: 00              NOP                         
2560: DE 00           SBC     A,$00               
2562: DA 00 D7        JP      C,$D700             
2565: 00              NOP                         
2566: D4 00 D1        CALL    NC,$D100            
2569: 00              NOP                         
256A: CD 00 CA        CALL    $CA00               
256D: 00              NOP                         
256E: C7              RST     $00                 
256F: 00              NOP                         
2570: C3 00 C0        JP      $C000               

; ---- $2573-$272F: data ----
2573: 00 BC 00 B8 00 B5 00 B1 00 AC 00 A8 00 A5 00 A0
2583: 00 9A 00 94 00 8F 00 87 00 84 00 7D 00 76 00 70
2593: 00 69 00 61 00 5B 00 53 00 4B 00 44 00 3B 00 33
25A3: 00 2C 00 23 00 1A 00 11 00 08 00 00 00 00 00 F8
25B3: FF EF FF 00 00 DD FF D4 FF CD FF C5 FF BC FF B5
25C3: FF AD FF A5 FF 9F FF 97 FF 90 FF 8A FF 83 FF 7C
25D3: FF 79 FF 7C FF 6C FF 66 FF 60 FF 5B FF 58 FF 54
25E3: FF 4F FF 4B FF 48 FF 44 FF 40 FF 3D FF 39 FF 36
25F3: FF 33 FF 33 FF 2C FF 29 FF 26 FF 22 FF 1F FF 1C
2603: FF 18 FF 15 FF 12 FF 0E FF 0B FF 08 FF 05 FF 01
2613: FF FF FE FC FE F8 FE F6 FE F4 FE F2 FE F0 FE ED
2623: FE EC FE EB FE EA FE E9 FE E8 FE E7 FE E7 FE E8
2633: FE E9 FE EA FE EB FE EC FE ED FE F0 FE F2 FE F4
2643: FE F6 FE F8 FE FC FE FF FE 01 FF 05 FF 08 FF 0B
2653: FF 0E FF 12 FF 15 FF 18 FF 1C FF 1F FF 22 FF 26
2663: FF 29 FF 2C FF 2F FF 33 FF 36 FF 39 FF 3D FF 40
2673: FF 44 FF 48 FF 4B FF 4F FF 54 FF 58 FF 5B FF 60
2683: FF 66 FF 6C FF 71 FF 79 FF 7C FF 83 FF 8A FF 90
2693: FF 97 FF 9F FF A5 FF AD FF B5 FF BC FF C5 FF CD
26A3: FF D4 FF DD FF E6 FF EF FF F8 FF 00 00 00 00 08
26B3: 00 11 00 1A 00 23 00 2C 00 33 00 3B 00 44 00 4B
26C3: 00 53 00 5B 00 61 00 69 00 70 00 76 00 7D 00 84
26D3: 00 87 00 87 00 94 00 9A 00 A0 00 A5 00 A8 00 AC
26E3: 00 B1 00 B5 00 B8 00 BC 00 C0 00 C3 00 C7 00 CA
26F3: 00 CD 00 CA 00 D4 00 D7 00 DA 00 DE 00 E1 00 E4
2703: 00 E8 00 EB 00 EE 00 F2 00 F5 00 F8 00 FB 00 FF
2713: 00 01 01 FB 00 08 01 0A 01 0C 01 0E 01 10 01 13
2723: 01 14 01 15 01 16 01 17 01 18 01 19 01

loc_2730:
2730: 3A 6F AA        LD      A,($AA6F)           ; {hard.workRam+26F}
2733: FE 76           CP      $76                 
2735: C2 30 25        JP      NZ,$2530            ; {code.loc_2530}
2738: CD 2B 0B        CALL    $0B2B               ; {code.hideCaptionSprites}
273B: CD 0E 21        CALL    $210E               ; {code.seedDemoAutopilotScript}
273E: AF              XOR     A                   
273F: 32 31 AD        LD      ($AD31),A           ; {hard.workRam+531}
2742: 32 20 AD        LD      ($AD20),A           ; {hard.workRam+520}
2745: 32 30 AD        LD      ($AD30),A           ; {hard.workRam+530}
2748: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC}
274B: 3C              INC     A                   
274C: 32 10 AD        LD      ($AD10),A           ; {hard.workRam+510}
274F: 3E 03           LD      A,$03               
2751: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB}
2754: C9              RET                         

; free all six of the player's shot slots, zeroing each record's occupancy
; byte and its second-axis coordinate but not its first; the fill byte and
; the record stride are both fetched from program space rather than
; written as immediates
freeAllShotSlots:
2755: DD 21 80 AA     LD      IX,$AA80            ; point at the first of the six shot slots
2759: 21 6E 27        LD      HL,$276E            
275C: 3A 61 08        LD      A,($0861)           ; {hard.rom+861} take the slot stride's low byte from the program image
275F: 5F              LD      E,A                 
2760: 3A 01 5C        LD      A,($5C01)           ; {hard.rom+5C01} take the fill byte from the program image -- zero on this build
2763: 57              LD      D,A                 ; the fill byte doubles as the stride's high byte
2764: 06 06           LD      B,$06               ; six slots to clear

loc_2766:
2766: DD 77 00        LD      (IX+$00),A          ; clear the slot's occupancy byte
2769: DD 77 04        LD      (IX+$04),A          ; clear the slot's second-axis byte
276C: DD 19           ADD     IX,DE               ; step to the next slot
276E: 10 F6           DJNZ    $2766               ; {code.loc_2766} clear all six
2770: C9              RET                         

; ---- $2771-$27B0: data ----
2771: 7E 84 7E 85 7E 86 7D 87 7C 88 7B 89 7A 8A 79 8A
2781: 78 8A 77 8A 76 8A 75 89 74 88 73 87 72 86 72 85
2791: 72 84 72 83 72 82 73 81 74 80 75 7F 76 7E 77 7E
27A1: 78 7E 79 7E 7A 7E 7B 7F 7C 80 7D 81 7E 82 7E 83

; round-start sequence arm: seat two player-object records (0xAD0C-0xAD2E)
; and position seeds (0xAC64=0x78,0xAC65=0x84), request a sound and load
; the difficulty record, then split on PLAY_ACTIVE(0xAD30) -- mid-game it
; queues command de=0x0400 and folds a +1 XOR checksum of 256 program
; bytes at 0x1550 into control latch 0xC308 (0xA9EB=0x96); on a fresh
; round it cycles the 1..3 stage counter at 0xA9D0, reseeds the random
; register, clears 0xAA80-0xAADF and 0xA800-0xA97F, SUB-checksums 256
; bytes at 0x3310 into 0xA9AB (xor 0x90) and paints star field
; 0xAC74-0xAC83 with 0x80 (0xA9EB=0x5A); both arms tail-advance the
; sequence sub-step
armRoundStartThenStepSequence:
27B1: CD 34 58        CALL    $5834               ; {code.requestRoundStartSound} ask for the round-start jingle
27B4: 3E 78           LD      A,$78               
27B6: 32 64 AC        LD      ($AC64),A           ; {hard.workRam+464} seed the enemy aim anchor
27B9: 3E 84           LD      A,$84               
27BB: 32 65 AC        LD      ($AC65),A           ; {hard.workRam+465} seed the enemy aim point
27BE: 21 00 00        LD      HL,$0000            
27C1: 22 16 AD        LD      ($AD16),HL          ; {hard.workRam+516} clear player 1's life-tick counter
27C4: 22 26 AD        LD      ($AD26),HL          ; {hard.workRam+526} clear player 2's life-tick counter
27C7: 3A CD A9        LD      A,($A9CD)           ; {hard.workRam+1CD} take the per-round kill quota
27CA: 32 12 AD        LD      ($AD12),A           ; {hard.workRam+512} set player 1's kills-remaining
27CD: 32 22 AD        LD      ($AD22),A           ; {hard.workRam+522} set player 2's kills-remaining
27D0: AF              XOR     A                   
27D1: 32 14 AD        LD      ($AD14),A           ; {hard.workRam+514} clear player 1's era index
27D4: 32 24 AD        LD      ($AD24),A           ; {hard.workRam+524} clear player 2's era index
27D7: 32 32 AD        LD      ($AD32),A           ; {hard.workRam+532} clear a per-round cell
27DA: 32 13 AD        LD      ($AD13),A           ; {hard.workRam+513} clear player 1's bonus-life latch
27DD: 32 23 AD        LD      ($AD23),A           ; {hard.workRam+523} clear player 2's bonus-life latch
27E0: 32 1D AD        LD      ($AD1D),A           ; {hard.workRam+51D} clear player 1's mother-ship-armed cell
27E3: 32 2D AD        LD      ($AD2D),A           ; {hard.workRam+52D} clear player 2's mother-ship-armed cell
27E6: 32 0C AD        LD      ($AD0C),A           ; {hard.workRam+50C} clear the pen colour
27E9: 3C              INC     A                   
27EA: 32 11 AD        LD      ($AD11),A           ; {hard.workRam+511} set player 1's round number to one
27ED: 32 21 AD        LD      ($AD21),A           ; {hard.workRam+521} set player 2's round number to one
27F0: 32 1E AD        LD      ($AD1E),A           ; {hard.workRam+51E} arm player 1's round
27F3: 32 2E AD        LD      ($AD2E),A           ; {hard.workRam+52E} arm player 2's round
27F6: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} read the play-active flag
27F9: A7              AND     A                   
27FA: 28 39           JR      Z,$2835             ; {code.loc_2835} fresh round -- take the full setup path
27FC: AF              XOR     A                   
27FD: 67              LD      H,A                 
27FE: 6F              LD      L,A                 
27FF: 32 33 AD        LD      ($AD33),A           ; {hard.workRam+533} clear player 1's score low byte
2802: 22 34 AD        LD      ($AD34),HL          ; {hard.workRam+534} clear player 1's score mid and high bytes
2805: 32 36 AD        LD      ($AD36),A           ; {hard.workRam+536} clear player 2's score low byte
2808: 22 37 AD        LD      ($AD37),HL          ; {hard.workRam+537} clear player 2's score mid and high bytes
280B: 11 00 04        LD      DE,$0400            ; load command word $0400
280E: FF              RST     $38                 ; post it
280F: 3A C4 A9        LD      A,($A9C4)           ; {hard.workRam+1C4} read the difficulty selector
2812: CD 7B 0F        CALL    $0F7B               ; {code.loadDifficultyRecord} load the difficulty record in force
2815: 06 00           LD      B,$00               ; two hundred fifty-six bytes to fold
2817: 21 50 15        LD      HL,$1550            ; point at the checked program-image block
281A: 97              SUB     A                   ; seed the checksum to zero

loc_281b:
281B: AE              XOR     (HL)                ; fold each byte in with exclusive-or
281C: 23              INC     HL                  
281D: 10 FC           DJNZ    $281B               ; {code.loc_281b} over all two hundred fifty-six
281F: C6 01           ADD     A,$01               ; bias the sum by one
2821: 32 08 C3        LD      ($C308),A           ; drive the result into a control latch
2824: 3A D3 A9        LD      A,($A9D3)           ; {hard.workRam+1D3} take the start rung
2827: 32 1A AD        LD      ($AD1A),A           ; {hard.workRam+51A} set player 1's start rung
282A: 32 2A AD        LD      ($AD2A),A           ; {hard.workRam+52A} set player 2's start rung
282D: 3E 96           LD      A,$96               
282F: 32 EB A9        LD      ($A9EB),A           ; {hard.workRam+1EB} mark the sequence mode
2832: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the attract/round sequence

loc_2835:
2835: 21 D0 A9        LD      HL,$A9D0            ; point at the 1..3 stage counter
2838: 7E              LD      A,(HL)              ; read it
2839: 3C              INC     A                   ; advance it
283A: FE 04           CP      $04                 ; past three?
283C: 38 02           JR      C,$2840             ; {code.loc_2840} no -- keep it
283E: 3E 01           LD      A,$01               ; wrapped -- back to one

loc_2840:
2840: 77              LD      (HL),A              ; store the stage
2841: 32 14 AD        LD      ($AD14),A           ; {hard.workRam+514} set player 1's era index from the stage
2844: 3C              INC     A                   
2845: 32 11 AD        LD      ($AD11),A           ; {hard.workRam+511} set player 1's round number to stage plus one
2848: AF              XOR     A                   
2849: 32 80 A9        LD      ($A980),A           ; {hard.workRam+180} clear a game-state cell
284C: 32 CE A9        LD      ($A9CE),A           ; {hard.workRam+1CE} clear the frame counter
284F: 32 CF A9        LD      ($A9CF),A           ; {hard.workRam+1CF} clear the script step counter
2852: CD 67 4B        CALL    $4B67               ; {code.seedRandomRegister} reseed the random register
2855: 21 80 AA        LD      HL,$AA80            ; point at the object bank
2858: 11 81 AA        LD      DE,$AA81            
285B: 36 00           LD      (HL),$00            
285D: 01 5F 00        LD      BC,$005F            
2860: ED B0           LDIR                        ; clear it up through 0xAADF
2862: 21 00 A8        LD      HL,$A800            ; point at the main work-RAM bank
2865: 11 01 A8        LD      DE,$A801            
2868: 36 00           LD      (HL),$00            
286A: 01 7F 01        LD      BC,$017F            
286D: ED B0           LDIR                        ; clear it up through 0xA97F
286F: 3E 02           LD      A,$02               ; select difficulty record two
2871: CD 7B 0F        CALL    $0F7B               ; {code.loadDifficultyRecord} load the difficulty record
2874: 3A D3 A9        LD      A,($A9D3)           ; {hard.workRam+1D3} take the start rung
2877: 32 1A AD        LD      ($AD1A),A           ; {hard.workRam+51A} set player 1's start rung
287A: 32 2A AD        LD      ($AD2A),A           ; {hard.workRam+52A} set player 2's start rung
287D: 0E 00           LD      C,$00               ; two hundred fifty-six bytes to fold
287F: 21 10 33        LD      HL,$3310            ; point at the checked program-image block
2882: 3A AB A9        LD      A,($A9AB)           ; {hard.workRam+1AB} seed the checksum

loc_2885:
2885: 96              SUB     (HL)                ; subtract each byte in turn
2886: 23              INC     HL                  
2887: 0D              DEC     C                   
2888: 20 FB           JR      NZ,$2885            ; {code.loc_2885} over all two hundred fifty-six
288A: EE 90           XOR     $90                 ; scramble the sum
288C: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} store the checksum
288F: 21 74 AC        LD      HL,$AC74            ; point at the star-field block
2892: 06 10           LD      B,$10               ; sixteen cells to paint

loc_2894:
2894: 36 80           LD      (HL),$80            ; paint a star cell
2896: 23              INC     HL                  
2897: 10 FB           DJNZ    $2894               ; {code.loc_2894} all sixteen
2899: 3E 5A           LD      A,$5A               
289B: 32 EB A9        LD      ($A9EB),A           ; {hard.workRam+1EB} mark the sequence mode
289E: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the attract/round sequence

; work seven fixed object slots in one fixed order, each through the entry
; that seats its own pair of cursors; the order is the whole of what this
; entry decides, and nothing here reads or writes a slot itself. Seven is
; the SET's size and not the per-frame count: the last two slots stand
; down while MOTHER_SHIP_ARMED is set, so on that arm only FIVE slots
; step. A resume value is laid down for each slot that will reach an arm,
; and not for the two that stand down, which reach none
stepSevenCraftSlots:
28A1: CD B7 28        CALL    $28B7               ; {code.seatCraftSlot0ThenDispatchByEra} service object slot 0
28A4: CD C2 28        CALL    $28C2               ; {code.seatCraftSlot1ThenDispatchByEra} service object slot 1
28A7: CD CD 28        CALL    $28CD               ; {code.seatCraftSlot2ThenDispatchByEra} service object slot 2
28AA: CD D8 28        CALL    $28D8               ; {code.seatCraftSlot3ThenDispatchByEra} service object slot 3
28AD: CD E3 28        CALL    $28E3               ; {code.seatCraftSlot4ThenDispatchByEra} service object slot 4
28B0: CD EE 28        CALL    $28EE               ; {code.seatMotherShipSlotThenDispatchByEraUnlessArmed} service the mother-ship slot -- skipped while its cell is armed
28B3: CD FE 28        CALL    $28FE               ; {code.seatCraftSlot6ThenDispatchByEraUnlessArmed} service object slot 6 -- skipped while the mother-ship cell is armed
28B6: C9              RET                         

; seat the record cursor and the sprite-entry cursor on one fixed object
; slot, then run the era-keyed dispatch over it; the pair of immediates is
; the whole of what distinguishes this entry from the four siblings that
; share its shape -- the two gated ones later in the chain differ by more
seatCraftSlot0ThenDispatchByEra:
28B7: DD 21 50 A8     LD      IX,$A850            ; point at slot 0's object record
28BB: FD 21 1A AA     LD      IY,$AA1A            ; point at slot 0's sprite entry
28BF: C3 0E 29        JP      $290E               ; {code.dispatchSeatedSlotByEraIndex} run the era-keyed handler over it

; seat the record cursor and the sprite-entry cursor on one fixed object
; slot, then run the era-keyed dispatch over it; the pair of immediates is
; the whole of what distinguishes this entry from the four siblings that
; share its shape -- the two gated ones later in the chain differ by more
seatCraftSlot1ThenDispatchByEra:
28C2: DD 21 60 A8     LD      IX,$A860            ; point at slot 1's object record
28C6: FD 21 1C AA     LD      IY,$AA1C            ; point at slot 1's sprite entry
28CA: C3 0E 29        JP      $290E               ; {code.dispatchSeatedSlotByEraIndex} run the era-keyed handler over it

; seat the record cursor and the sprite-entry cursor on one fixed object
; slot, then run the era-keyed dispatch over it; the pair of immediates is
; the whole of what distinguishes this entry from the four siblings that
; share its shape -- the two gated ones later in the chain differ by more
seatCraftSlot2ThenDispatchByEra:
28CD: DD 21 70 A8     LD      IX,$A870            ; point at slot 2's object record
28D1: FD 21 1E AA     LD      IY,$AA1E            ; point at slot 2's sprite entry
28D5: C3 0E 29        JP      $290E               ; {code.dispatchSeatedSlotByEraIndex} run the era-keyed handler over it

; seat the record cursor and the sprite-entry cursor on one fixed object
; slot, then run the era-keyed dispatch over it; the pair of immediates is
; the whole of what distinguishes this entry from the four siblings that
; share its shape -- the two gated ones later in the chain differ by more
seatCraftSlot3ThenDispatchByEra:
28D8: DD 21 80 A8     LD      IX,$A880            ; point at slot 3's object record
28DC: FD 21 20 AA     LD      IY,$AA20            ; point at slot 3's sprite entry
28E0: C3 0E 29        JP      $290E               ; {code.dispatchSeatedSlotByEraIndex} run the era-keyed handler over it

; seat the record cursor and the sprite-entry cursor on one fixed object
; slot, then run the era-keyed dispatch over it, with no gate in front of
; it
seatCraftSlot4ThenDispatchByEra:
28E3: DD 21 90 A8     LD      IX,$A890            ; point at slot 4's object record
28E7: FD 21 22 AA     LD      IY,$AA22            ; point at slot 4's sprite entry
28EB: C3 0E 29        JP      $290E               ; {code.dispatchSeatedSlotByEraIndex} run the era-keyed handler over it

; run the era-keyed dispatch over the mother ship's slot, but only while
; the armed cell is clear -- a set cell returns at once, leaving the slot
; unserviced for the frame
seatMotherShipSlotThenDispatchByEraUnlessArmed:
28EE: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} read the mother-ship armed cell
28F1: A7              AND     A                   
28F2: C0              RET     NZ                  ; armed -- leave this slot unserviced this frame
28F3: DD 21 A0 A8     LD      IX,$A8A0            ; point at the mother-ship object record
28F7: FD 21 24 AA     LD      IY,$AA24            ; point at its sprite entry
28FB: C3 0E 29        JP      $290E               ; {code.dispatchSeatedSlotByEraIndex} run the era-keyed handler over it

; run the era-keyed dispatch over one fixed object slot, but only while
; the mother ship's armed cell is clear -- a set cell returns at once,
; leaving the slot unserviced for the frame
seatCraftSlot6ThenDispatchByEraUnlessArmed:
28FE: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} read the mother-ship armed cell
2901: A7              AND     A                   
2902: C0              RET     NZ                  ; armed -- leave this slot unserviced this frame
2903: DD 21 B0 A8     LD      IX,$A8B0            ; point at slot 6's object record
2907: FD 21 26 AA     LD      IY,$AA26            ; point at its sprite entry
290B: C3 0E 29        JP      $290E               ; {code.dispatchSeatedSlotByEraIndex} run the era-keyed handler over it

; run the arm the LOW THREE BITS of the ERA INDEX select out of a word
; table laid down inline just behind this entry; the arm is entered as a
; transfer with no place parked for it to come back to, so it returns past
; this entry and nothing here runs after it
dispatchSeatedSlotByEraIndex:
290E: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the active era index
2911: E6 07           AND     $07                 ; keep the low three bits
2913: F7              RST     $30                 ; jump through the era table just below into the matching handler

; ---- $2914-$291D: jump table ----
2914: 27 29 4C 29 84 29 B0 29 D5 29

; fold a run of image bytes into a total the caller has already seeded,
; walking a SECOND pointer alongside it in lockstep. The second walk adds
; nothing: each step overwrites the same byte-wide holder, so only the
; last byte it passes survives, and on a genuine image its leftover went
; unread by every RAM signature the pass sampled. A count of zero means a
; full 256 bytes, the total wraps at eight bits, and no memory is written
foldBlockIntoTotal:
291E: 86              ADD     A,(HL)              ; fold the next image byte into the running total
291F: EB              EX      DE,HL               
2920: 4E              LD      C,(HL)              ; read the byte the second pointer walks past
2921: EB              EX      DE,HL               
2922: 23              INC     HL                  ; step the total pointer
2923: 13              INC     DE                  ; step the second pointer alongside it
2924: 10 F8           DJNZ    $291E               ; {code.foldBlockIntoTotal} over the whole block -- a count of zero means a full 256
2926: C9              RET                         

; era-0 per-object update dispatched by index 0 of the rst-0x30 era table
; at 0x2914: on the object status byte at (ix+0) it leaves an empty slot
; (0), releases a held object (0xFE), steps a dying one (any other value),
; or steers/flies/refreshes an active craft (0xFF) and lets it spawn,
; retiring it the frame it reaches the line
serviceEra0EnemyCraftSlot:
2927: DD 7E 00        LD      A,(IX+$00)          ; read this slot's status byte
292A: A7              AND     A                   
292B: C8              RET     Z                   ; empty slot -- nothing to do
292C: 3C              INC     A                   
292D: 28 07           JR      Z,$2936             ; {code.loc_2936} a live craft -- fly it
292F: 3C              INC     A                   
2930: CA 52 2B        JP      Z,$2B52             ; {code.releaseHeldObject} a held object -- release it
2933: C3 93 2B        JP      $2B93               ; {code.stepDyingObjectState} otherwise step the dying object

loc_2936:
2936: CD EF 2B        CALL    $2BEF               ; {code.steerTowardAimHeading} steer toward the aim heading
2939: CD 40 58        CALL    $5840               ; {code.flyAtSlowestSpeed} fly at the slowest speed
293C: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} reached the retire line?
293F: DA DE 2B        JP      C,$2BDE             ; {code.retireSlotAndSubPixel} yes -- retire the slot
2942: CD D6 3E        CALL    $3ED6               ; {code.launchBankEnemyWhenAimedNearPlayer} try a bank-enemy launch when aimed near the player
2945: CD 3C 2A        CALL    $2A3C               ; {code.refreshSpriteFromHeading} refresh the sprite from the heading
2948: CD 43 42        CALL    $4243               ; {code.launchAttackerIntoFreeSlot} try to launch an attacker into a free slot
294B: C9              RET                         

loc_294c:
294C: DD 7E 00        LD      A,(IX+$00)          ; read this slot's status byte
294F: A7              AND     A                   
2950: C8              RET     Z                   ; empty slot -- nothing to do
2951: 3C              INC     A                   
2952: 28 07           JR      Z,$295B             ; {code.loc_295b} a live craft -- fly it
2954: 3C              INC     A                   
2955: CA 52 2B        JP      Z,$2B52             ; {code.releaseHeldObject} a held object -- release it
2958: C3 93 2B        JP      $2B93               ; {code.stepDyingObjectState} otherwise step the dying object

loc_295b:
295B: CD EF 2B        CALL    $2BEF               ; {code.steerTowardAimHeading} steer toward the aim heading
295E: CD 54 58        CALL    $5854               ; {code.loc_5854} fly at this era's speed
2961: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} reached the retire line?
2964: DA DE 2B        JP      C,$2BDE             ; {code.retireSlotAndSubPixel} yes -- retire the slot
2967: CD D6 3E        CALL    $3ED6               ; {code.launchBankEnemyWhenAimedNearPlayer} try a bank-enemy launch when aimed near the player
296A: CD 47 2A        CALL    $2A47               ; {code.refreshSecondEraSpriteFromHeading} refresh the sprite from the heading -- second-era sprite set
296D: C9              RET                         

; ---- $296E-$2983: data ----
296E: 09 A7 32 82 6E 58 B5 77 E4 E8 EC 9D CB 4F 55 FE
297E: A3 31 81 5B 9A B9

; era-2 per-slot object handler (index 2 of the 0x2914 rst-0x30 era table,
; ERA_INDEX 0xad04 low three bits == 2), dispatched on the slot's state
; byte (ix+0): 0x00 idle returns; 0xFF active steers toward its aim 3
; frames in 4, flies at the slowest speed, retires the slot once it
; reaches a retire line, else dresses its sprite and runs two gated enemy-
; launch attempts; 0xFE releases the held object; any other value steps
; the dying-object state
serviceEra2EnemyCraftSlot:
2984: DD 7E 00        LD      A,(IX+$00)          ; read this slot's status byte
2987: A7              AND     A                   
2988: C8              RET     Z                   ; empty slot -- nothing to do
2989: 3C              INC     A                   
298A: 28 07           JR      Z,$2993             ; {code.loc_2993} a live craft -- fly it
298C: 3C              INC     A                   
298D: CA 52 2B        JP      Z,$2B52             ; {code.releaseHeldObject} a held object -- release it
2990: C3 93 2B        JP      $2B93               ; {code.stepDyingObjectState} otherwise step the dying object

loc_2993:
2993: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame phase counter
2996: E6 03           AND     $03                 ; keep its low two bits
2998: FE 03           CP      $03                 
299A: DC EF 2B        CALL    C,$2BEF             ; {code.steerTowardAimHeading} steer toward the aim heading -- on three frames of every four
299D: CD 40 58        CALL    $5840               ; {code.flyAtSlowestSpeed} fly at the slowest speed
29A0: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} reached the retire line?
29A3: DA DE 2B        JP      C,$2BDE             ; {code.retireSlotAndSubPixel} yes -- retire the slot
29A6: CD D6 3E        CALL    $3ED6               ; {code.launchBankEnemyWhenAimedNearPlayer} try a bank-enemy launch when aimed near the player
29A9: CD 97 2A        CALL    $2A97               ; {code.dressSpriteForFineHeading} dress the sprite for its fine heading
29AC: CD 43 42        CALL    $4243               ; {code.launchAttackerIntoFreeSlot} try to launch an attacker into a free slot
29AF: C9              RET                         

; era-3 per-object-slot step, dispatched on the slot's lifecycle byte at
; ix+0: idle does nothing; a live slot (0xff) is steered, dressed, then
; retired at the line or flown on and given a spawn attempt; 0xfe releases
; a held slot; a lower value is a death-countdown step
serviceEra3EnemyCraftSlot:
29B0: DD 7E 00        LD      A,(IX+$00)          ; read the slot's lifecycle byte
29B3: A7              AND     A                   ; is the slot free?
29B4: C8              RET     Z                   ; free: nothing to do this frame
29B5: 3C              INC     A                   ; bump -- the live code 0xff wraps to zero here
29B6: 28 07           JR      Z,$29BF             ; {code.loc_29bf} live: steer and service this slot
29B8: 3C              INC     A                   ; bump again -- the held code 0xfe wraps to zero here
29B9: CA 52 2B        JP      Z,$2B52             ; {code.releaseHeldObject} held: run its release-delay countdown
29BC: C3 93 2B        JP      $2B93               ; {code.stepDyingObjectState} any other value: step its dying animation

loc_29bf:
29BF: CD EF 2B        CALL    $2BEF               ; {code.steerTowardAimHeading} turn its heading one step toward its aim
29C2: CD A4 58        CALL    $58A4               ; {code.loc_58a4} fly the slot a step along its heading
29C5: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} has it drifted onto a retire line?
29C8: DA DE 2B        JP      C,$2BDE             ; {code.retireSlotAndSubPixel} yes: take the slot out of play
29CB: CD D6 3E        CALL    $3ED6               ; {code.launchBankEnemyWhenAimedNearPlayer} when aimed near the ship, try the bank launch
29CE: CD FC 2A        CALL    $2AFC               ; {code.dressSpriteForCoarseHeading} dress the sprite to face its heading
29D1: CD 43 42        CALL    $4243               ; {code.launchAttackerIntoFreeSlot} launch an attacker into a free slot
29D4: C9              RET                         

; era-4 (ERA_INDEX 0xad04=4) per-object slot service, index 4 of the
; 0x2914 rst-0x30 table: on the slot's lifecycle byte at (ix+0) it returns
; when free (0), releases when held (0xfe), steps the dying animation for
; any other value, and when live (0xff) steers the slot toward the ship
; then either retires it once it reaches a retire line or animates its
; shape, runs the gated launch attempt, and launches an attacker into a
; free slot
serviceEra4EnemyCraftSlot:
29D5: DD 7E 00        LD      A,(IX+$00)          ; read the slot's lifecycle byte
29D8: A7              AND     A                   ; is the slot free?
29D9: C8              RET     Z                   ; free: nothing to do this frame
29DA: 3C              INC     A                   ; bump -- the live code 0xff wraps to zero here
29DB: 28 07           JR      Z,$29E4             ; {code.loc_29e4} live: steer and service this slot
29DD: 3C              INC     A                   ; bump again -- the held code 0xfe wraps to zero here
29DE: CA 52 2B        JP      Z,$2B52             ; {code.releaseHeldObject} held: run its release-delay countdown
29E1: C3 93 2B        JP      $2B93               ; {code.stepDyingObjectState} any other value: step its dying animation

loc_29e4:
29E4: CD F7 29        CALL    $29F7               ; {code.steerEnemyTowardShip} steer toward the ship, then fly a step
29E7: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} has it drifted onto a retire line?
29EA: DA DE 2B        JP      C,$2BDE             ; {code.retireSlotAndSubPixel} yes: take the slot out of play
29ED: CD 38 2B        CALL    $2B38               ; {code.animateSelectedShapeCycle} advance its shape's animation cycle
29F0: CD D6 3E        CALL    $3ED6               ; {code.launchBankEnemyWhenAimedNearPlayer} when aimed near the ship, try the bank launch
29F3: CD 43 42        CALL    $4243               ; {code.launchAttackerIntoFreeSlot} launch an attacker into a free slot
29F6: C9              RET                         

; steer one live slot toward its aim heading then fly it a step; when the
; slot's probe cell (iy+0x31) lies within a fixed window of either
; reference point the turn runs with the shared turn-rate index forced to
; zero then reseated to four, else at the standing index, and the step
; alternates a double- and a single-velocity mover on bit 1 of the frame
; tick
steerEnemyTowardShip:
29F7: 3E 78           LD      A,$78               ; first reference point on the screen (0x78)
29F9: FD 96 31        SUB     (IY+$31)            ; distance from the slot's screen-position probe
29FC: C6 48           ADD     A,$48               ; bias by half the window
29FE: FE 90           CP      $90                 ; is the probe within the window of it?
2A00: 38 1A           JR      C,$2A1C             ; {code.loc_2a1c} near it: turn with the rate index forced low
2A02: 3E 84           LD      A,$84               ; second reference point (0x84)
2A04: FD 96 31        SUB     (IY+$31)            ; distance from the probe
2A07: C6 48           ADD     A,$48               ; bias by half the window
2A09: FE 90           CP      $90                 ; within the window of it?
2A0B: 38 0F           JR      C,$2A1C             ; {code.loc_2a1c} near it: turn with the rate index forced low
2A0D: CD EF 2B        CALL    $2BEF               ; {code.steerTowardAimHeading} otherwise turn toward aim at the standing rate

loc_2a10:
2A10: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame tick counter
2A13: 0F              RRCA                        
2A14: E6 01           AND     $01                 ; isolate bit 1 of it
2A16: CA AA 58        JP      Z,$58AA             ; {code.loc_58aa} that bit clear: fly the slot at double velocity
2A19: C3 60 58        JP      $5860               ; {code.loc_5860} otherwise fly it at single velocity

loc_2a1c:
2A1C: AF              XOR     A                   
2A1D: 32 04 AD        LD      ($AD04),A           ; {hard.workRam+504} force the shared turn-rate index to zero
2A20: CD EF 2B        CALL    $2BEF               ; {code.steerTowardAimHeading} turn toward aim at that forced rate
2A23: 3E 04           LD      A,$04               
2A25: 32 04 AD        LD      ($AD04),A           ; {hard.workRam+504} reseat the shared turn-rate index to four
2A28: 18 E6           JR      $2A10               ; {code.loc_2a10} go fly the step

; ---- $2A2A-$2A3B: data ----
2A2A: DD 7E 04 3D CA 93 2B DD 77 04 DD 36 00 FF CD BA
2A3A: 2B C9

; store the shape byte and the attribute byte that show an object pointing
; the way it is heading into that object's own sprite entry
refreshSpriteFromHeading:
2A3C: CD 57 2A        CALL    $2A57               ; {code.spriteForHeading} pick the shape and its mirror byte for this heading
2A3F: FD 71 30        LD      (IY+$30),C          ; store the mirror byte into the sprite entry
2A42: 78              LD      A,B                 
2A43: FD 77 01        LD      (IY+$01),A          ; store the shape byte into the sprite entry
2A46: C9              RET                         

; show one of the second era's enemy craft pointing the way it is heading:
; the shared heading lookup picks a shape and the byte beside it, and each
; is stored into the object's own sprite entry shifted by a fixed bias --
; sixteen on the shape, fifty-three on the attribute -- so this era's
; craft is drawn from its own block of the sprite ROM in its own colour.
; The attribute's two flip bits survive the addition because every entry
; of the lookup's attribute table carries the same low colour field, so
; the bias moves the colour and leaves the facing alone
refreshSecondEraSpriteFromHeading:
2A47: CD 57 2A        CALL    $2A57               ; {code.spriteForHeading} pick the shape and its mirror byte for this heading
2A4A: 79              LD      A,C                 ; take the mirror/attribute byte
2A4B: C6 35           ADD     A,$35               ; bias its colour by 53 into this era's block
2A4D: FD 77 30        LD      (IY+$30),A          ; store it into the sprite entry
2A50: 78              LD      A,B                 ; take the shape byte
2A51: C6 10           ADD     A,$10               ; bias it by 16 into this era's sprite block
2A53: FD 77 01        LD      (IY+$01),A          ; store it into the sprite entry
2A56: C9              RET                         

; pick the sprite shape, and the byte beside it, that show an object
; pointing the way it is heading, alternating between two shape banks as a
; frame counter's bit turns over
spriteForHeading:
2A57: 11 10 00        LD      DE,$0010            ; the mirror table sits sixteen past the shape table
2A5A: DD 7E 02        LD      A,(IX+$02)          ; read the object's heading
2A5D: C6 08           ADD     A,$08               ; add half a sector to round to nearest
2A5F: 0F              RRCA                        
2A60: 0F              RRCA                        
2A61: 0F              RRCA                        
2A62: 0F              RRCA                        
2A63: E6 0F           AND     $0F                 ; top nibble: heading snapped to one of sixteen sectors
2A65: 21 77 2A        LD      HL,$2A77            ; point at the shape-by-sector table
2A68: DF              RST     $18                 ; index it by the sector
2A69: 46              LD      B,(HL)              ; take the shape byte
2A6A: 19              ADD     HL,DE               ; step to the parallel mirror table
2A6B: 4E              LD      C,(HL)              ; take the mirror byte beside it
2A6C: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame tick counter
2A6F: CB 4F           BIT     1,A                 ; test bit 1
2A71: C8              RET     Z                   ; half the frame pairs: keep the base shape
2A72: 78              LD      A,B                 
2A73: C6 08           ADD     A,$08               ; otherwise advance the shape by eight
2A75: 47              LD      B,A                 
2A76: C9              RET                         

; ---- $2A77-$2A96: data ----
2A77: 0C 0D 0E 0F 08 0F 0E 0D 0C 0B 0A 09 08 09 0A 0B
2A87: 41 41 41 41 81 C1 C1 C1 C1 C1 C1 C1 41 41 41 41

; dress one sprite entry to face the way its object is heading, resolving
; the heading to thirty-two sectors and writing the shape code and the
; attribute beside it directly into the entry, alternating between two
; shape banks as a frame counter's bit turns over
dressSpriteForFineHeading:
2A97: DD 7E 02        LD      A,(IX+$02)          ; read the object's heading
2A9A: C6 04           ADD     A,$04               ; add half a sector (of thirty-two) to round to nearest
2A9C: E6 F8           AND     $F8                 ; drop the low three bits
2A9E: 0F              RRCA                        
2A9F: 0F              RRCA                        
2AA0: E6 3F           AND     $3F                 ; form the sector as a doubled index -- two-byte entries
2AA2: 21 BC 2A        LD      HL,$2ABC            ; point at the shape/attribute table
2AA5: DF              RST     $18                 ; index it by the doubled sector
2AA6: 46              LD      B,(HL)              ; take the shape byte
2AA7: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame tick counter
2AAA: E6 02           AND     $02                 ; take bit 1
2AAC: 20 0A           JR      NZ,$2AB8            ; {code.loc_2ab8} set: add eight to the shape

loc_2aae:
2AAE: 80              ADD     A,B                 ; combine with the base shape -- zero or eight added
2AAF: FD 77 01        LD      (IY+$01),A          ; store the shape into the sprite entry
2AB2: 23              INC     HL                  
2AB3: 7E              LD      A,(HL)              ; take the attribute byte from the next table cell
2AB4: FD 77 30        LD      (IY+$30),A          ; store it into the sprite entry
2AB7: C9              RET                         

loc_2ab8:
2AB8: 3E 08           LD      A,$08               ; the eight to add
2ABA: 18 F2           JR      $2AAE               ; {code.loc_2aae} join the store path

; ---- $2ABC-$2AFB: data ----
2ABC: 80 DC 80 DC 80 DC 80 DC 81 DC 81 DC 82 DC 83 DC
2ACC: 84 5C 84 5C 83 5C 82 5C 81 5C 81 5C 80 5C 80 5C
2ADC: 80 5C 80 5C 80 5C 80 5C 81 5C 81 5C 82 5C 83 5C
2AEC: 84 DC 84 DC 83 DC 82 DC 81 DC 81 DC 80 DC 80 DC

; point an object's sprite the way it is heading, by rounding its heading
; byte to the nearest of sixteen sectors and taking a shape pair from two
; parallel tables
dressSpriteForCoarseHeading:
2AFC: 11 10 00        LD      DE,$0010            ; the second table sits sixteen past the first
2AFF: DD 7E 02        LD      A,(IX+$02)          ; read the object's heading
2B02: C6 08           ADD     A,$08               ; add half a sector to round to nearest
2B04: 0F              RRCA                        
2B05: 0F              RRCA                        
2B06: 0F              RRCA                        
2B07: 0F              RRCA                        
2B08: E6 0F           AND     $0F                 ; top nibble: heading snapped to one of sixteen sectors
2B0A: 21 18 2B        LD      HL,$2B18            ; point at the shape table
2B0D: DF              RST     $18                 ; index it by the sector
2B0E: 7E              LD      A,(HL)              ; take the shape byte
2B0F: FD 77 01        LD      (IY+$01),A          ; store it into the sprite entry
2B12: 19              ADD     HL,DE               ; step to the parallel attribute table
2B13: 7E              LD      A,(HL)              ; take the attribute byte
2B14: FD 77 30        LD      (IY+$30),A          ; store it into the sprite entry
2B17: C9              RET                         

; ---- $2B18-$2B37: data ----
2B18: 2C 2D 2E 2F 28 2F 2E 2D 2C 2B 2A 29 28 29 2A 2B
2B28: 5B 5B 5B 5B 9B DB DB DB DB DB DB DB 5B 5B 5B 5B

; give one sprite entry the current frame of a four-frame shape cycle,
; from the block a record byte selects, and one fixed attribute beside it
animateSelectedShapeCycle:
2B38: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame tick counter
2B3B: 0F              RRCA                        
2B3C: 0F              RRCA                        
2B3D: E6 03           AND     $03                 ; two middle bits: the animation phase, turning over every fourth frame
2B3F: C6 D8           ADD     A,$D8               ; offset to the first shape in the block (0xd8)
2B41: 47              LD      B,A                 
2B42: DD 7E 04        LD      A,(IX+$04)          ; read the object's shape-block selector
2B45: D6 01           SUB     $01                 ; count it from one
2B47: 87              ADD     A,A                 
2B48: 87              ADD     A,A                 ; shift up by two -- times four, a block of four shapes per selector
2B49: 80              ADD     A,B                 ; add the phased base shape
2B4A: FD 77 01        LD      (IY+$01),A          ; store the shape into the sprite entry
2B4D: FD 36 30 61     LD      (IY+$30),$61        ; stamp the fixed attribute (0x61) beside it
2B51: C9              RET                         

; count a held object's release delay down and, when it expires, step its
; state code to the live one and re-arm the delay
releaseHeldObject:
2B52: DD 35 0E        DEC     (IX+$0E)            ; count the release delay down one
2B55: 28 01           JR      Z,$2B58             ; {code.loc_2b58} reached zero: release it
2B57: C9              RET                         

loc_2b58:
2B58: DD 34 00        INC     (IX+$00)            ; step the state code on to the live one
2B5B: DD 36 0E 80     LD      (IX+$0E),$80        ; reload the delay with 128
2B5F: C9              RET                         

; add the frame's world-scroll displacement to one object's two split
; 16-bit coordinates
driftWithWorldScroll:
2B60: FD 66 31        LD      H,(IY+$31)          ; the object's whole coordinate byte, first axis, from its sprite entry
2B63: DD 6E 03        LD      L,(IX+$03)          ; its fraction from the record
2B66: ED 5B 08 A8     LD      DE,($A808)          ; {hard.workRam+8} the frame's world-scroll step for this axis
2B6A: 19              ADD     HL,DE               ; add it into the 16-bit coordinate
2B6B: FD 74 31        LD      (IY+$31),H          ; store the whole byte back
2B6E: DD 75 03        LD      (IX+$03),L          ; store the fraction back
2B71: FD 66 00        LD      H,(IY+$00)          ; the object's whole coordinate byte, second axis
2B74: DD 6E 05        LD      L,(IX+$05)          ; its fraction from the record
2B77: ED 5B 0A A8     LD      DE,($A80A)          ; {hard.workRam+A} the frame's world-scroll step for this axis
2B7B: 19              ADD     HL,DE               ; add it into the 16-bit coordinate
2B7C: FD 74 00        LD      (IY+$00),H          ; store the whole byte back
2B7F: DD 75 05        LD      (IX+$05),L          ; store the fraction back
2B82: C9              RET                         

; answer whether an actor has drifted onto either of two fixed retire
; lines, within a narrow wrapped window, which is what makes its caller
; free the slot
hasReachedRetireLine:
2B83: FD 7E 31        LD      A,(IY+$31)          ; the object's screen row byte
2B86: C6 09           ADD     A,$09               ; line up the retire row with a three-wide window
2B88: FE 03           CP      $03                 ; within a pixel of the retire row (0xf8)?
2B8A: D8              RET     C                   ; yes: report reached, carry set
2B8B: FD 7E 00        LD      A,(IY+$00)          ; the object's screen column byte
2B8E: D6 03           SUB     $03                 ; line up the retire column with the window
2B90: FE 03           CP      $03                 ; within a pixel of the retire column (4)? -- carry now carries the answer
2B92: C9              RET                         

; per-object state-machine step: dispatch on the object's state byte —
; 0xf0 re-arms it to 0x3b and begins its death, 0x3c begins the death then
; flies it on, above 0x3c flies it on, below 0x3c counts the byte down,
; retiring the slot at zero else moving the object for the frame
stepDyingObjectState:
2B93: DD 7E 00        LD      A,(IX+$00)          ; read the object's state byte
2B96: FE F0           CP      $F0                 ; the re-arm value 0xf0?
2B98: CA AC 2B        JP      Z,$2BAC             ; {code.loc_2bac} yes: re-seat it and begin the death
2B9B: FE 3C           CP      $3C                 ; at the death-begins threshold 0x3c?
2B9D: CC BA 2B        CALL    Z,$2BBA             ; {code.countTheKillAndGrantTheSharedToken} exactly there: count the kill and grant the token
2BA0: D2 B4 2B        JP      NC,$2BB4            ; {code.decrementObjectStateThenFlyAtSlowestSpeed} at or above the threshold: fly it on
2BA3: DD 35 00        DEC     (IX+$00)            ; below it: count the state byte down
2BA6: 28 36           JR      Z,$2BDE             ; {code.retireSlotAndSubPixel} hit zero: take the slot out of play
2BA8: CD 22 2C        CALL    $2C22               ; {code.moveObjectByStateByteThenRunAppearance} else move it for the frame and run its appearance

; ---- $2BAB-$2BAB: data ----
2BAB: C9

loc_2bac:
2BAC: DD 36 00 3B     LD      (IX+$00),$3B        ; re-seat the state byte to 0x3b
2BB0: CD BA 2B        CALL    $2BBA               ; {code.countTheKillAndGrantTheSharedToken} count the kill and grant the token
2BB3: C9              RET                         

; count an object's state byte down by one and let it fly on at the
; slowest of the velocity-table speeds; the countdown wraps at a byte and
; nothing here tests it, so reaching zero is the caller's business. Both
; entries into it are on the path a slot takes once its state byte is
; neither free, live nor held
decrementObjectStateThenFlyAtSlowestSpeed:
2BB4: DD 35 00        DEC     (IX+$00)            ; count the object's state byte down one
2BB7: C3 40 58        JP      $5840               ; {code.flyAtSlowestSpeed} fly it on at the slowest table speed

; the tick a hit object's death begins: ask for the pair of death sounds
; and take one off the round's kill quota -- both UNCONDITIONAL -- and
; then, only past three guards, grant this record the single-holder token
; at 0xA821, its own slot ordinal marked with a top bit. The guards are
; the record's cooldown byte carrying its top bit, the shared arming cell
; being set, and the shared countdown beside it reaching zero on this
; step; the countdown is spent whenever the first two pass, so every
; claimant spends a tick and not only the one that wins. The quota is
; floored rather than wrapped -- a count already at zero is left alone
countTheKillAndGrantTheSharedToken:
2BBA: CD 83 56        CALL    $5683               ; {code.requestTwoSounds} ask for the pair of death sounds
2BBD: 21 02 AD        LD      HL,$AD02            ; point at the round's kill quota
2BC0: 7E              LD      A,(HL)              
2BC1: A7              AND     A                   ; already at zero?
2BC2: 28 01           JR      Z,$2BC5             ; {code.loc_2bc5} yes: leave it -- floor, do not wrap
2BC4: 35              DEC     (HL)                ; else take one kill off the quota

loc_2bc5:
2BC5: DD 7E 0E        LD      A,(IX+$0E)          ; read this record's cooldown byte
2BC8: CB 7F           BIT     7,A                 ; is its top claim bit set?
2BCA: C8              RET     Z                   ; no: not a claimant, done
2BCB: 3A 12 A8        LD      A,($A812)           ; {hard.workRam+12} read the shared arming cell
2BCE: A7              AND     A                   
2BCF: C8              RET     Z                   ; not set: done
2BD0: 21 11 A8        LD      HL,$A811            ; point at the shared kill countdown
2BD3: 35              DEC     (HL)                ; spend a tick of it
2BD4: C0              RET     NZ                  ; not zero yet: done -- every claimant spends a tick
2BD5: DD 7E 0F        LD      A,(IX+$0F)          ; this record's slot ordinal
2BD8: C6 80           ADD     A,$80               ; mark it with the top bit
2BDA: 32 21 A8        LD      ($A821),A           ; {hard.workRam+21} grant it the single-holder token
2BDD: C9              RET                         

; take an object out of play, zeroing each coordinate WHOLE — occupancy
; byte, both sub-pixel remainders, and both sprite-entry coordinates
retireSlotAndSubPixel:
2BDE: AF              XOR     A                   ; zero, to clear five cells
2BDF: DD 77 00        LD      (IX+$00),A          ; clear the occupancy byte -- free the slot
2BE2: DD 77 03        LD      (IX+$03),A          ; clear the row sub-pixel remainder
2BE5: DD 77 05        LD      (IX+$05),A          ; clear the column sub-pixel remainder
2BE8: FD 77 00        LD      (IY+$00),A          ; clear one sprite-entry coordinate
2BEB: FD 77 31        LD      (IY+$31),A          ; clear the other sprite-entry coordinate
2BEE: C9              RET                         

; turn an object's heading one step toward the heading it aims at, the
; short way round, at a rate a small table supplies for the current mode
; cell
steerTowardAimHeading:
2BEF: DD 7E 01        LD      A,(IX+$01)          ; the heading the object is turning toward
2BF2: DD 96 02        SUB     (IX+$02)            ; minus its current heading -- how far round the aim lies
2BF5: 4F              LD      C,A                 ; keep that wrapped difference
2BF6: C6 02           ADD     A,$02               ; bias for the arrival test
2BF8: FE 04           CP      $04                 ; within one step ahead or two behind? already on the aim
2BFA: D8              RET     C                   ; yes: stop turning
2BFB: DD 46 02        LD      B,(IX+$02)          ; hold the current heading
2BFE: 79              LD      A,C                 ; the difference again
2BFF: FE 80           CP      $80                 ; is the aim more than half a turn away?
2C01: 30 0C           JR      NC,$2C0F            ; {code.loc_2c0f} yes: the short way round is backward
2C03: 21 1D 2C        LD      HL,$2C1D            ; point at the turn-rate table
2C06: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} the shared turn-rate index -- the current mode
2C09: CF              RST     $08                 ; fetch this mode's step size
2C0A: 80              ADD     A,B                 ; add the step to the current heading -- turn forward
2C0B: DD 77 02        LD      (IX+$02),A          ; write the new heading
2C0E: C9              RET                         

loc_2c0f:
2C0F: 21 1D 2C        LD      HL,$2C1D            ; point at the turn-rate table
2C12: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} the shared turn-rate index
2C15: CF              RST     $08                 ; fetch this mode's step size
2C16: 90              SUB     B                   
2C17: ED 44           NEG                         ; current heading minus the step -- turn backward
2C19: DD 77 02        LD      (IX+$02),A          ; write the new heading
2C1C: C9              RET                         

; ---- $2C1D-$2C21: data ----
2C1D: 01 01 02 02 05

; move one object for the frame according to its state byte, then run the
; shared appearance step over that same object: from thirty-two up it
; counts the state byte down and flies on at the slowest table speed,
; below thirty-two it only drifts with the world and the state byte is
; left alone; the appearance step runs on both paths
moveObjectByStateByteThenRunAppearance:
2C22: 21 31 2C        LD      HL,$2C31            ; point at the shared appearance step and...
2C25: E5              PUSH    HL                  ; ...stack it as the return, so whichever move runs next falls straight on into it
2C26: DD 7E 00        LD      A,(IX+$00)          ; read this object's state byte
2C29: FE 20           CP      $20                 ; is it thirty-two or more?
2C2B: D2 B4 2B        JP      NC,$2BB4            ; {code.decrementObjectStateThenFlyAtSlowestSpeed} yes -- count the state byte down one frame and fly on at the slowest table speed
2C2E: C3 60 2B        JP      $2B60               ; {code.driftWithWorldScroll} no -- only drift with the world scroll, leaving the state byte alone

; ---- $2C31-$2CBB: data ----
2C31: DD 7E 00 FE 2A D2 71 2C FE 0A 30 45 3A 21 A8 CB
2C41: 7F CA DE 2B 3A 21 A8 CB BF DD BE 0F C2 DE 2B 3A
2C51: 80 A9 E6 07 28 03 DD 34 00 FD 36 01 FC FD 36 30
2C61: 6C DD 7E 00 FE 01 C0 11 0C 04 FF AF 32 21 A8 C9
2C71: FD 7E 30 4F E6 C0 47 3A 80 A9 E6 0F 80 FD 77 30
2C81: C9 D6 0A 0F E6 0F 47 21 94 2C CF FD 77 01 FD 36
2C91: 30 3C C9 FF FF 7D 7D 7E 7E 7D 7D 5B 5B 5A 5A 59
2CA1: 59 58 58 18 A7 13 A5 3B 87 F1 34 0E 34 D7 BF F1
2CB1: 65 13 13 13 13 F1 88 DC ED 11 B9

; seat the record cursor and the sprite-entry cursor on the first scenery
; slot, then run one of three fixed lists of parallax wrappers, chosen by
; the era index
runSceneryForEra:
2CBC: DD 21 00 A9     LD      IX,$A900            ; seat the scenery record cursor on the first slot
2CC0: FD 21 30 AA     LD      IY,$AA30            ; seat the sprite-entry cursor on the first slot
2CC4: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
2CC7: A7              AND     A                   ; is it the first era?
2CC8: 28 2B           JR      Z,$2CF5             ; {code.loc_2cf5} yes -- run the opening scenery order
2CCA: FE 04           CP      $04                 ; is it the fifth era?
2CCC: 28 34           JR      Z,$2D02             ; {code.loc_2d02} yes -- run the closing scenery order
2CCE: CD 21 2D        CALL    $2D21               ; {code.driftNearestSceneryTriTile} middle order: drift a diagonally-cornered scenery object at five quarters
2CD1: CD 36 2D        CALL    $2D36               ; {code.driftTwoTileSceneryAtThreeQuarters} drift a two-tile scenery object at three quarters
2CD4: CD 36 2D        CALL    $2D36               ; {code.driftTwoTileSceneryAtThreeQuarters} and another two-tile object at three quarters
2CD7: CD 68 2D        CALL    $2D68               ; {code.driftOneTileSceneryAtHalf} drift a one-tile object at half -- the farthest, slowest layer
2CDA: C9              RET                         

; one turn of the line wipe, and on the turn that finishes it, one tamper
; test: a single line is blanked per turn and the turn ends there while
; lines are still owed; the turn that clears the last one folds a fixed
; 1024-byte span of the program image together with exclusive-or into an
; eight-bit total and compares it against the total an untampered image
; gives. Matching steps the sequence's INNER index, so the sequence
; carries on; not matching steps the OUTER phase instead, restarting the
; inner index somewhere else entirely -- derailing the sequence rather
; than halting it
blankOneLineThenGuardBlockOrDerailSequence:
2CDB: CD C2 01        CALL    $01C2               ; {code.blankNextLine} blank the next line of the wipe; comes back saying whether any lines are still owed
2CDE: C0              RET     NZ                  ; lines still owed -- end the turn here
2CDF: 01 04 00        LD      BC,$0004            ; four passes of...
2CE2: 21 80 49        LD      HL,$4980            ; ...the fixed 1024-byte program-image block at $4980
2CE5: 97              SUB     A                   ; clear the running total

loc_2ce6:
2CE6: AE              XOR     (HL)                ; fold this byte into the total with exclusive-or
2CE7: 23              INC     HL                  ; next byte
2CE8: 10 FC           DJNZ    $2CE6               ; {code.loc_2ce6} 256 bytes per pass
2CEA: 0D              DEC     C                   ; next pass
2CEB: 20 F9           JR      NZ,$2CE6            ; {code.loc_2ce6} 1024 bytes folded in all
2CED: C6 BD           ADD     A,$BD               ; add $BD -- lands on zero only when the fold matches an untampered image
2CEF: C2 11 0F        JP      NZ,$0F11            ; {code.advanceSequencePhase} mismatch (image tampered) -- step the outer sequence phase, derailing the sequence
2CF2: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} match -- step the sequence's inner index so it carries on

loc_2cf5:
2CF5: CD 15 2D        CALL    $2D15               ; {code.driftThreeTileSceneryAtFiveQuarters} opening order: drift a three-tile scenery strip at five quarters
2CF8: CD 36 2D        CALL    $2D36               ; {code.driftTwoTileSceneryAtThreeQuarters} drift a two-tile object at three quarters
2CFB: CD 36 2D        CALL    $2D36               ; {code.driftTwoTileSceneryAtThreeQuarters} and another two-tile object at three quarters
2CFE: CD 68 2D        CALL    $2D68               ; {code.driftOneTileSceneryAtHalf} drift a one-tile object at half -- the farthest layer
2D01: C9              RET                         

loc_2d02:
2D02: CD 2D 2D        CALL    $2D2D               ; {code.stepTwoTileSceneryAtFiveQuarters} closing order: advance a two-tile scenery object at five quarters
2D05: CD 2D 2D        CALL    $2D2D               ; {code.stepTwoTileSceneryAtFiveQuarters} and another two-tile object at five quarters
2D08: CD 62 2D        CALL    $2D62               ; {code.driftOneTileSceneryAtThreeQuarters} drift a one-tile object at three quarters
2D0B: CD 62 2D        CALL    $2D62               ; {code.driftOneTileSceneryAtThreeQuarters} and another one-tile object at three quarters
2D0E: CD 68 2D        CALL    $2D68               ; {code.driftOneTileSceneryAtHalf} drift a one-tile object at half
2D11: CD 68 2D        CALL    $2D68               ; {code.driftOneTileSceneryAtHalf} and another one-tile object at half
2D14: C9              RET                         

; drift one scenery object at five quarters of the frame's world scroll,
; lay two further tiles flush against it in a straight strip, and step
; both cursors past the object so the caller lands on the next slot
driftThreeTileSceneryAtFiveQuarters:
2D15: CD 6E 2D        CALL    $2D6E               ; {code.driftAtFiveQuartersWorldScroll} drift this scenery object at five quarters of the world scroll
2D18: CD 58 30        CALL    $3058               ; {code.placeAbuttingTile} lay a tile flush against it
2D1B: CD 58 30        CALL    $3058               ; {code.placeAbuttingTile} lay a second tile flush, extending the strip
2D1E: C3 9B 30        JP      $309B               ; {code.advanceToNextSlot} step both cursors onto the next slot

; drift one scenery object with the world scroll over-travelled by a
; quarter, then lay the tile abutting it and the one cornering it
; diagonally (three corners of a square) and step both cursors one slot
; past
driftNearestSceneryTriTile:
2D21: CD 6E 2D        CALL    $2D6E               ; {code.driftAtFiveQuartersWorldScroll} drift this scenery object at five quarters of the world scroll
2D24: CD 58 30        CALL    $3058               ; {code.placeAbuttingTile} lay the tile abutting it
2D27: CD 8A 30        CALL    $308A               ; {code.placeDiagonallyAbuttingTile} lay the tile cornering it diagonally -- three corners of a square
2D2A: C3 9B 30        JP      $309B               ; {code.advanceToNextSlot} step both cursors onto the next slot

; advance one two-tile scenery object: drift it at five quarters of the
; world scroll, lay its second tile flush against the first, and step both
; cursors past the pair
stepTwoTileSceneryAtFiveQuarters:
2D2D: CD 6E 2D        CALL    $2D6E               ; {code.driftAtFiveQuartersWorldScroll} drift this scenery object at five quarters of the world scroll
2D30: CD 58 30        CALL    $3058               ; {code.placeAbuttingTile} lay its second tile flush against the first
2D33: C3 9B 30        JP      $309B               ; {code.advanceToNextSlot} step both cursors past the pair

; drift one scenery object at three quarters of the frame's world scroll,
; place a second tile flush against it, and step both cursors past the
; object so the caller lands on the next slot
driftTwoTileSceneryAtThreeQuarters:
2D36: CD 93 2D        CALL    $2D93               ; {code.driftAtThreeQuartersWorldScroll} drift this scenery object at three quarters of the world scroll
2D39: CD 58 30        CALL    $3058               ; {code.placeAbuttingTile} lay a second tile flush against it
2D3C: C3 9B 30        JP      $309B               ; {code.advanceToNextSlot} step both cursors onto the next slot

; one sequence step that puts the credit line up: while FREE_PLAY is set
; it does nothing but move the sequence's inner index on; otherwise it
; repaints the panel field from the packed-decimal credit count at 0xA986,
; queues caption record 8 -- whose glyph run reads CREDIT -- and then
; reads a guard byte that decides everything after. Anything but zero
; transfers to 0x2E3E, which carries no routine, so that transfer RAISES
; rather than running; zero stamps the copyright strip into the display
; list, asks for its line in this frame's colour, and folds the twenty-
; byte run at 0x086B into a total for the chain that judges it. What
; writes the guard byte is not established here
showCreditLine:
2D3F: 3A C0 A9        LD      A,($A9C0)           ; {hard.workRam+1C0} read the free-play switch
2D42: A7              AND     A                   ; is it set?
2D43: C2 1A 0F        JP      NZ,$0F1A            ; {code.advanceSequenceSubStep} free play -- just step the sequence's inner index and leave
2D46: CD FB 4A        CALL    $4AFB               ; {code.paintCreditCountPanel} repaint the credit-count panel
2D49: 11 08 01        LD      DE,$0108            ; caption command 1, record 8 -- the CREDIT line
2D4C: FF              RST     $38                 ; post it to the command ring
2D4D: 3A 17 A8        LD      A,($A817)           ; {hard.workRam+17} read the guard byte
2D50: A7              AND     A                   ; is it set?
2D51: C2 3E 2E        JP      NZ,$2E3E            ; {code.loc_2e3e} set -- jump to $2E3E, which holds table data, not a routine
2D54: CD 06 0B        CALL    $0B06               ; {code.stampCopyrightStrip} stamp the copyright/caption strip into the display list
2D57: CD 39 0B        CALL    $0B39               ; {code.flashCopyrightLine} request the copyright line flashed in this frame's colour
2D5A: 21 6B 08        LD      HL,$086B            ; point at the twenty-byte image run at $086B...
2D5D: 06 14           LD      B,$14               ; ...twenty bytes...
2D5F: C3 E8 43        JP      $43E8               ; {code.sumImageBlockForTheTamperCheck} ...and fold it into the tamper-check total

; drift one scenery object at three quarters of the frame's world scroll,
; lay no further tile, and step both cursors onto the next slot
driftOneTileSceneryAtThreeQuarters:
2D62: CD 93 2D        CALL    $2D93               ; {code.driftAtThreeQuartersWorldScroll} drift this scenery object at three quarters of the world scroll
2D65: C3 9B 30        JP      $309B               ; {code.advanceToNextSlot} step both cursors onto the next slot -- no further tile

; drift one scenery object at half the frame's world-scroll displacement,
; lay no further tile, and step both cursors onto the next slot -- the
; one-tile member of the parallax family, and the slowest rung, so what it
; moves reads as the farthest layer
driftOneTileSceneryAtHalf:
2D68: CD F4 2D        CALL    $2DF4               ; {code.driftAtHalfWorldScroll} drift this scenery object at half the world scroll -- the farthest, slowest layer
2D6B: C3 9B 30        JP      $309B               ; {code.advanceToNextSlot} step both cursors onto the next slot

; move one object by the frame's world-scroll displacement and a further
; quarter of it, so it over-travels the world; applied to both of its
; split coordinates, whole part in the sprite entry and fraction in the
; object record
driftAtFiveQuartersWorldScroll:
2D6E: FD 56 31        LD      D,(IY+$31)          ; whole part of the first coordinate
2D71: DD 5E 03        LD      E,(IX+$03)          ; its fraction -- together one sixteen-bit coordinate
2D74: 2A 08 A8        LD      HL,($A808)          ; {hard.workRam+8} this frame's vertical world-scroll
2D77: CD 31 2E        CALL    $2E31               ; {code.displaceByFiveQuarters} move the coordinate by five quarters of the scroll
2D7A: FD 74 31        LD      (IY+$31),H          ; store the whole part back
2D7D: DD 75 03        LD      (IX+$03),L          ; and its fraction
2D80: FD 56 00        LD      D,(IY+$00)          ; whole part of the second coordinate
2D83: DD 5E 05        LD      E,(IX+$05)          ; its fraction
2D86: 2A 0A A8        LD      HL,($A80A)          ; {hard.workRam+A} this frame's horizontal world-scroll
2D89: CD 31 2E        CALL    $2E31               ; {code.displaceByFiveQuarters} move the coordinate by five quarters of the scroll
2D8C: FD 74 00        LD      (IY+$00),H          ; store the whole part back
2D8F: DD 75 05        LD      (IX+$05),L          ; and its fraction
2D92: C9              RET                         

; move one object by three quarters of the frame's world-scroll
; displacement, applied to both of its split coordinates, whole part in
; the sprite entry and fraction in the object record
driftAtThreeQuartersWorldScroll:
2D93: FD 56 31        LD      D,(IY+$31)          ; whole part of the first coordinate
2D96: DD 5E 03        LD      E,(IX+$03)          ; its fraction
2D99: 2A 08 A8        LD      HL,($A808)          ; {hard.workRam+8} this frame's vertical world-scroll
2D9C: CD 3E 30        CALL    $303E               ; {code.displaceByThreeQuarters} move the coordinate by three quarters of the scroll
2D9F: FD 74 31        LD      (IY+$31),H          ; store the whole part back
2DA2: DD 75 03        LD      (IX+$03),L          ; and its fraction
2DA5: FD 56 00        LD      D,(IY+$00)          ; whole part of the second coordinate
2DA8: DD 5E 05        LD      E,(IX+$05)          ; its fraction
2DAB: 2A 0A A8        LD      HL,($A80A)          ; {hard.workRam+A} this frame's horizontal world-scroll
2DAE: CD 3E 30        CALL    $303E               ; {code.displaceByThreeQuarters} move the coordinate by three quarters of the scroll
2DB1: FD 74 00        LD      (IY+$00),H          ; store the whole part back
2DB4: DD 75 05        LD      (IX+$05),L          ; and its fraction
2DB7: C9              RET                         

; start the next round: step the round number, roll the era on and wrap it
; after the fifth, set the round's difficulty byte from one of three
; sources by round bracket, refill the kill quota, and clear two flags
; while arming a third
startNextRound:
2DB8: 21 01 AD        LD      HL,$AD01            ; point at the round counter
2DBB: 34              INC     (HL)                ; step to the next round
2DBC: 21 04 AD        LD      HL,$AD04            ; point at the era index
2DBF: 7E              LD      A,(HL)              ; take it
2DC0: 3C              INC     A                   ; roll it forward
2DC1: FE 05           CP      $05                 ; past the fifth era?
2DC3: 38 01           JR      C,$2DC6             ; {code.loc_2dc6} no -- keep it
2DC5: AF              XOR     A                   ; yes -- wrap back to the first era

loc_2dc6:
2DC6: 77              LD      (HL),A              ; store the era index
2DC7: 3A 01 AD        LD      A,($AD01)           ; {hard.workRam+501} read the round number
2DCA: FE 06           CP      $06                 ; rounds 1..5?
2DCC: 38 09           JR      C,$2DD7             ; {code.loc_2dd7} yes -- take the low bracket's starting rung
2DCE: FE 0B           CP      $0B                 ; rounds 6..10?
2DD0: 38 0A           JR      C,$2DDC             ; {code.loc_2ddc} yes -- take the middle bracket's starting rung
2DD2: 3A D5 A9        LD      A,($A9D5)           ; {hard.workRam+1D5} rounds 11 and up -- take the high bracket's starting rung
2DD5: 18 08           JR      $2DDF               ; {code.loc_2ddf}

loc_2dd7:
2DD7: 3A D3 A9        LD      A,($A9D3)           ; {hard.workRam+1D3} rounds 1..5 -- the low bracket's starting rung
2DDA: 18 03           JR      $2DDF               ; {code.loc_2ddf}

loc_2ddc:
2DDC: 3A D4 A9        LD      A,($A9D4)           ; {hard.workRam+1D4} rounds 6..10 -- the middle bracket's starting rung

loc_2ddf:
2DDF: 32 0A AD        LD      ($AD0A),A           ; {hard.workRam+50A} set this round's starting rung
2DE2: 3A CD A9        LD      A,($A9CD)           ; {hard.workRam+1CD} take the kill quota
2DE5: 32 02 AD        LD      ($AD02),A           ; {hard.workRam+502} refill kills-remaining from it -- the same every round
2DE8: AF              XOR     A                   ; clear the accumulator
2DE9: 32 0D AD        LD      ($AD0D),A           ; {hard.workRam+50D} clear the mother-ship-armed flag
2DEC: 32 C6 AC        LD      ($ACC6),A           ; {hard.workRam+4C6} clear the round-transition hold
2DEF: 3D              DEC     A                   ; flip to all-ones
2DF0: 32 0E AD        LD      ($AD0E),A           ; {hard.workRam+50E} arm the round with it
2DF3: C9              RET                         

; move one object by half the frame's world-scroll displacement, applied
; to both of its split coordinates, whole part in the sprite entry and
; fraction in the object record
driftAtHalfWorldScroll:
2DF4: FD 56 31        LD      D,(IY+$31)          ; whole part of the first coordinate
2DF7: DD 5E 03        LD      E,(IX+$03)          ; its fraction
2DFA: 2A 08 A8        LD      HL,($A808)          ; {hard.workRam+8} this frame's vertical world-scroll
2DFD: CD 4D 30        CALL    $304D               ; {code.displaceByHalf} move the coordinate by half the scroll
2E00: FD 74 31        LD      (IY+$31),H          ; store the whole part back
2E03: DD 75 03        LD      (IX+$03),L          ; and its fraction
2E06: FD 56 00        LD      D,(IY+$00)          ; whole part of the second coordinate
2E09: DD 5E 05        LD      E,(IX+$05)          ; its fraction
2E0C: 2A 0A A8        LD      HL,($A80A)          ; {hard.workRam+A} this frame's horizontal world-scroll
2E0F: CD 4D 30        CALL    $304D               ; {code.displaceByHalf} move the coordinate by half the scroll
2E12: FD 74 00        LD      (IY+$00),H          ; store the whole part back
2E15: DD 75 05        LD      (IX+$05),L          ; and its fraction
2E18: C9              RET                         

; open the settings block: store, whole, the byte the caller has already
; worked out from the switch port's low two bits, then peel the next two
; switch bits into a cell each, one bit per cell and nothing else in it,
; and hand the byte on rotated so the last bit spent sits lowest -- twice
; over, in both registers that carry it -- to the continuation that peels
; the rest. Nothing is read from memory and control never comes back.
; 'Switch settings' is established at the CALLER and at the three cells'
; readers, not inside a routine that reads no memory at all: the caller at
; 0x52C0-0x52CF is `ld a,(0xc200) / cpl / ld c,a / and 0x03 / add a,0x03 /
; cp 0x06 / jr nz,+2 / ld a,0xff / jp 0x2e19`, so C arrives as the
; complemented DSW port and A as 3, 4, 5 or the folded 0xFF
unpackTheFirstThreeSwitchSettings:
2E19: 32 C1 A9        LD      ($A9C1),A           ; {hard.workRam+1C1} store the starting-lives setting the caller worked out
2E1C: 79              LD      A,C                 ; take the packed switch byte
2E1D: 0F              RRCA                        ; rotate it...
2E1E: 0F              RRCA                        ; ...down two bits
2E1F: 4F              LD      C,A                 ; keep the rotated byte
2E20: E6 01           AND     $01                 ; isolate one bit -- the cabinet type (upright/cocktail)
2E22: 32 C2 A9        LD      ($A9C2),A           ; {hard.workRam+1C2} store it in its own cell
2E25: 79              LD      A,C                 ; take the rotated byte again
2E26: 0F              RRCA                        ; rotate down one more bit
2E27: 4F              LD      C,A                 ; keep it
2E28: E6 01           AND     $01                 ; isolate the next bit -- the bonus-life setting
2E2A: 32 C3 A9        LD      ($A9C3),A           ; {hard.workRam+1C3} store it in its own cell
2E2D: 79              LD      A,C                 ; hand the remaining bits on...
2E2E: C3 A8 49        JP      $49A8               ; {code.finishBootSelfTestAndColdStart} ...to the continuation that peels the rest and cold-starts

; move a coordinate by a displacement and a further quarter of it, so what
; it carries leads what moves by the whole of it; the quarter rounds down
; rather than toward zero
displaceByFiveQuarters:
2E31: 44              LD      B,H                 ; copy the displacement aside to take a quarter of it
2E32: 4D              LD      C,L                 
2E33: CB 28           SRA     B                   ; halve it, keeping its sign...
2E35: CB 19           RR      C                   
2E37: CB 28           SRA     B                   ; ...and halve again: a quarter of the displacement
2E39: CB 19           RR      C                   
2E3B: 09              ADD     HL,BC               ; displacement plus its quarter -- five quarters
2E3C: 19              ADD     HL,DE               ; add that to the coordinate
2E3D: C9              RET                         

loc_2e3e:
2E3E: 32 01 31        LD      ($3101),A           ; {hard.rom+3101}
2E41: 01 30 01        LD      BC,$0130            
2E44: 2F              CPL                         
2E45: 01 2E 01        LD      BC,$012E            
2E48: 2D              DEC     L                   
2E49: 01 2C 01        LD      BC,$012C            
2E4C: 28 01           JR      Z,$2E4F             
2E4E: 26 01           LD      H,$01               
2E50: 24              INC     H                   
2E51: 01 22 01        LD      BC,$0122            
2E54: 20 01           JR      NZ,$2E57            ; {code.loc_2e57}
2E56: 1B              DEC     DE                  

loc_2e57:
2E57: 01 18 01        LD      BC,$0118            
2E5A: 16 01           LD      D,$01               
2E5C: 11 01 0E        LD      DE,$0E01            
2E5F: 01 0B 01        LD      BC,$010B            
2E62: 08              EX      AF,AF'              
2E63: 01 03 01        LD      BC,$0103            
2E66: 00              NOP                         
2E67: 01 FD 00        LD      BC,$00FD            
2E6A: F8              RET     M                   
2E6B: 00              NOP                         
2E6C: F5              PUSH    AF                  
2E6D: 00              NOP                         
2E6E: F2 00 ED        JP      P,$ED00             
2E71: 00              NOP                         
2E72: EA 00 E7        JP      PE,$E700            
2E75: 00              NOP                         
2E76: E4 00 DF        CALL    PO,$DF00            
2E79: 00              NOP                         
2E7A: DC 00 D9        CALL    C,$D900             
2E7D: 00              NOP                         
2E7E: D4 00 D1        CALL    NC,$D100            
2E81: 00              NOP                         
2E82: CD 00 C8        CALL    $C800               
2E85: 00              NOP                         
2E86: C5              PUSH    BC                  
2E87: 00              NOP                         
2E88: C1              POP     BC                  
2E89: 00              NOP                         
2E8A: BB              CP      E                   
2E8B: 00              NOP                         
2E8C: B7              OR      A                   
2E8D: 00              NOP                         
2E8E: B4              OR      H                   
2E8F: 00              NOP                         
2E90: AE              XOR     (HL)                
2E91: 00              NOP                         
2E92: A8              XOR     B                   
2E93: 00              NOP                         
2E94: A1              AND     C                   
2E95: 00              NOP                         
2E96: 9C              SBC     A,H                 
2E97: 00              NOP                         
2E98: 93              SUB     E                   
2E99: 00              NOP                         
2E9A: 90              SUB     B                   
2E9B: 00              NOP                         
2E9C: 88              ADC     A,B                 
2E9D: 00              NOP                         
2E9E: 80              ADD     A,B                 
2E9F: 00              NOP                         
2EA0: 7A              LD      A,D                 
2EA1: 00              NOP                         
2EA2: 72              LD      (HL),D              
2EA3: 00              NOP                         
2EA4: 69              LD      L,C                 
2EA5: 00              NOP                         
2EA6: 63              LD      H,E                 
2EA7: 00              NOP                         
2EA8: 5A              LD      E,D                 
2EA9: 00              NOP                         
2EAA: 51              LD      D,C                 
2EAB: 00              NOP                         
2EAC: 4A              LD      C,D                 
2EAD: 00              NOP                         
2EAE: 40              LD      B,B                 
2EAF: 00              NOP                         
2EB0: 37              SCF                         
2EB1: 00              NOP                         
2EB2: 30 00           JR      NC,$2EB4            ; {code.loc_2eb4}

loc_2eb4:
2EB4: 26 00           LD      H,$00               
2EB6: 1C              INC     E                   
2EB7: 00              NOP                         
2EB8: 12              LD      (DE),A              
2EB9: 00              NOP                         
2EBA: 08              EX      AF,AF'              
2EBB: 00              NOP                         
2EBC: 00              NOP                         
2EBD: 00              NOP                         
2EBE: 00              NOP                         
2EBF: 00              NOP                         
2EC0: F8              RET     M                   
2EC1: FF              RST     $38                 
2EC2: EE FF           XOR     $FF                 
2EC4: 00              NOP                         
2EC5: 00              NOP                         
2EC6: DA FF D0        JP      C,$D0FF             
2EC9: FF              RST     $38                 
2ECA: C9              RET                         

; ---- $2ECB-$303D: data ----
2ECB: FF C0 FF B6 FF AF FF A6 FF 9D FF 97 FF 8E FF 86
2EDB: FF 80 FF 78 FF 70 FF 6D FF 70 FF 5F FF 58 FF 52
2EEB: FF 4C FF 49 FF 45 FF 3F FF 3B FF 38 FF 33 FF 2F
2EFB: FF 2C FF 27 FF 24 FF 21 FF 21 FF 19 FF 16 FF 13
2F0B: FF 0E FF 0B FF 08 FF 03 FF 00 FF FD FE F8 FE F5
2F1B: FE F2 FE EF FE EA FE E8 FE E5 FE E0 FE DE FE DC
2F2B: FE DA FE D8 FE D4 FE D3 FE D2 FE D1 FE D0 FE CF
2F3B: FE CE FE CE FE CF FE D0 FE D1 FE D2 FE D3 FE D4
2F4B: FE D8 FE DA FE DC FE DE FE E0 FE E5 FE E8 FE EA
2F5B: FE EF FE F2 FE F5 FE F8 FE FD FE 00 FF 03 FF 08
2F6B: FF 0B FF 0E FF 13 FF 16 FF 19 FF 1C FF 21 FF 24
2F7B: FF 27 FF 2C FF 2F FF 33 FF 38 FF 3B FF 3F FF 45
2F8B: FF 49 FF 4C FF 52 FF 58 FF 5F FF 64 FF 6D FF 70
2F9B: FF 78 FF 80 FF 86 FF 8E FF 97 FF 9D FF A6 FF AF
2FAB: FF B6 FF C0 FF C9 FF D0 FF DA FF E4 FF EE FF F8
2FBB: FF 00 00 00 00 08 00 12 00 1C 00 26 00 30 00 37
2FCB: 00 40 00 4A 00 51 00 5A 00 63 00 69 00 72 00 7A
2FDB: 00 80 00 88 00 90 00 93 00 93 00 A1 00 A8 00 AE
2FEB: 00 B4 00 B7 00 BB 00 C1 00 C5 00 C8 00 CD 00 D1
2FFB: 00 D4 00 D9 00 DC 00 DF 00 DC 00 E7 00 EA 00 ED
300B: 00 F2 00 F5 00 F8 00 FD 00 00 01 03 01 08 01 0B
301B: 01 0E 01 11 01 16 01 18 01 11 01 20 01 22 01 24
302B: 01 26 01 28 01 2C 01 2D 01 2E 01 2F 01 30 01 31
303B: 01 32 01

; move a coordinate by three quarters of a displacement, so what it
; carries trails what moves by the whole of it
displaceByThreeQuarters:
303E: 44              LD      B,H                 ; copy the displacement aside to take a quarter of it
303F: 4D              LD      C,L                 
3040: CB 28           SRA     B                   ; halve it, keeping its sign...
3042: CB 19           RR      C                   
3044: CB 28           SRA     B                   ; ...and halve again: a quarter of the displacement
3046: CB 19           RR      C                   
3048: A7              AND     A                   ; clear the carry for the subtract
3049: ED 42           SBC     HL,BC               ; displacement minus its quarter -- three quarters
304B: 19              ADD     HL,DE               ; add that to the coordinate
304C: C9              RET                         

; move a coordinate by half a displacement, so what it carries keeps half
; the pace of what moves by the whole of it
displaceByHalf:
304D: 44              LD      B,H                 ; copy the displacement into a scratch pair to halve it
304E: 4D              LD      C,L                 
304F: CB 28           SRA     B                   ; arithmetic-shift the copy right one, halving it and keeping its sign
3051: CB 19           RR      C                   
3053: A7              AND     A                   ; clear carry before the subtract
3054: ED 42           SBC     HL,BC               ; displacement minus its half leaves the complementary half
3056: 19              ADD     HL,DE               ; add that to the coordinate, so it advances at half the pace, the fraction carrying up into the whole
3057: C9              RET                         

; place an object's next sprite tile flush against the current one and
; step both cursors onto it
placeAbuttingTile:
3058: FD 46 31        LD      B,(IY+$31)          ; read one coordinate byte of the current sprite entry
305B: FD 4E 00        LD      C,(IY+$00)          ; read the other coordinate byte
305E: 3E 10           LD      A,$10               ; a sprite's width in pixels...
3060: 80              ADD     A,B                 ; ...advances the first coordinate one tile on
3061: FD 77 33        LD      (IY+$33),A          ; write it into the next sprite entry
3064: FD 71 02        LD      (IY+$02),C          ; copy the other coordinate into the next entry unchanged
3067: C3 9B 30        JP      $309B               ; {code.advanceToNextSlot} step both cursors onto the entry just written

; ---- $306A-$3073: data ----
306A: FD 46 31 FD 4E 00 26 08 2E 6E

loc_3074:
3074: 7E              LD      A,(HL)              ; read a byte at the pointer
3075: 81              ADD     A,C                 ; add the running coordinate
3076: FD 70 33        LD      (IY+$33),B          ; write one coordinate byte into the next sprite entry
3079: FD 77 02        LD      (IY+$02),A          ; and the summed one into its other field
307C: C3 9B 30        JP      $309B               ; {code.advanceToNextSlot} step both cursors onto the entry just written

loc_307f:
307F: 73              LD      (HL),E              ; store the coordinate through the pointer
3080: A6              AND     (HL)                ; fold it into the accumulator
3081: 10 F1           DJNZ    $3074               ; {code.loc_3074} more slots to place: loop back
3083: D7              RST     $10                 ; fetch a two-byte entry from the following table
3084: 34              INC     (HL)                ; step the byte past the entry
3085: A5              AND     L                   
3086: 87              ADD     A,A                 
3087: BF              CP      A                   
3088: F1              POP     AF                  ; drop a word off the stack into the accumulator and flags
3089: B9              CP      C                   

; carry an object diagonally onto one more sprite entry, cornering off the
; one it already occupies: a pitch back along the high axis and a pitch on
; along the low one, in one 16-bit add so the low axis's wrap borrows
placeDiagonallyAbuttingTile:
308A: FD 46 31        LD      B,(IY+$31)          ; read the current entry's high-axis coordinate
308D: FD 4E 00        LD      C,(IY+$00)          ; read its low-axis coordinate
3090: 26 F0           LD      H,$F0               ; a pitch back along the high axis (-16 in the high byte)...
3092: 2E 10           LD      L,$10               ; ...and a pitch on along the low axis (+16)
3094: 09              ADD     HL,BC               ; apply both in one add, so a low-axis wrap borrows into the high axis
3095: FD 74 33        LD      (IY+$33),H          ; write the high-axis coordinate into the next entry
3098: FD 75 02        LD      (IY+$02),L          ; write the low-axis coordinate into the next entry

; step the record cursor and the parallel sprite-entry cursor on to the
; next object slot
advanceToNextSlot:
309B: 11 10 00        LD      DE,$0010            ; one record stride...
309E: DD 19           ADD     IX,DE               ; ...steps the record cursor onto the next slot
30A0: FD 23           INC     IY                  ; step the entry cursor...
30A2: FD 23           INC     IY                  ; ...by its two-byte stride onto the next slot
30A4: C9              RET                         

; sum a fixed 16-byte run against a constant as a discarded tamper
; tripwire, copy eight bytes of the ERA_INDEX-keyed row from the 0x3176
; table into the stride-two run at 0xAA31, then tail into the scenery
; clear+run carrying the era in C and the fill byte 0x28 at era four else
; 0xCC
seatEraSceneryRowThenClearAndRunScenery:
30A5: 21 6B 08        LD      HL,$086B            ; point at a fixed program run to checksum
30A8: 0E 22           LD      C,$22               ; the value it must sum to -- a tamper tripwire
30AA: 06 10           LD      B,$10               ; sixteen bytes to fold
30AC: CD 4C 0B        CALL    $0B4C               ; {code.sumByteRunAndCompareToExpected} fold the run and compare -- the answer is discarded here
30AF: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the current era
30B2: 87              ADD     A,A                 ; scale the era up by eight -- one row of eight bytes per era
30B3: 87              ADD     A,A                 
30B4: 87              ADD     A,A                 
30B5: 4F              LD      C,A                 
30B6: 21 76 31        LD      HL,$3176            ; point at the era-keyed scenery-row table
30B9: DF              RST     $18                 ; index it by the era offset -- pointer at the row start
30BA: 11 31 AA        LD      DE,$AA31            ; point at the object-code cells to seat (stride two)
30BD: 06 08           LD      B,$08               ; eight bytes to copy

loc_30bf:
30BF: 7E              LD      A,(HL)              ; take a row byte
30C0: 12              LD      (DE),A              ; seat it into the object cell
30C1: 23              INC     HL                  
30C2: 13              INC     DE                  ; advance to the next object cell -- two apart
30C3: 13              INC     DE                  
30C4: 10 F9           DJNZ    $30BF               ; {code.loc_30bf} repeat for all eight
30C6: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era again
30C9: FE 04           CP      $04                 ; is it era four?
30CB: 4F              LD      C,A                 ; keep the era for the tail
30CC: CA 56 31        JP      Z,$3156             ; {code.seatSceneryFillByte0x28ThenClearEraScenery} era four: hand on with the 0x28 fill byte
30CF: 3E CC           LD      A,$CC               ; otherwise use fill byte 0xCC

; clear a stride-two run of eight object cells to the fill byte carried in
; A, then branch on the era in C: below four, seat and run the frame's
; scenery through the four-object seat path; at four and up, when two
; work-RAM guards read their expected values seat eight entries from a
; packed table before running the scenery, and on a wrong guard transfer
; into a data table and fault
clearSceneryEntriesThenRunEraScenery:
30D1: 21 60 AA        LD      HL,$AA60            ; point at the object attribute cells
30D4: 11 02 00        LD      DE,$0002            ; stride of two
30D7: 06 08           LD      B,$08               ; eight cells

loc_30d9:
30D9: 77              LD      (HL),A              ; clear this cell to the fill byte
30DA: 19              ADD     HL,DE               ; step two on
30DB: 10 FC           DJNZ    $30D9               ; {code.loc_30d9} repeat for all eight
30DD: 79              LD      A,C                 ; recall the era
30DE: FE 04           CP      $04                 ; below era four?
30E0: DA 17 31        JP      C,$3117             ; {code.seedSceneryEntriesThenRunScenery} yes: seed four objects and run the scenery
30E3: 21 C7 AC        LD      HL,$ACC7            ; point at the first runtime guard cell
30E6: 7E              LD      A,(HL)              ; read it
30E7: FE 3B           CP      $3B                 ; is it the expected value?
30E9: C2 5B 31        JP      NZ,$315B            ; {code.loc_315b} no: derail into the data table
30EC: 23              INC     HL                  ; step to the second guard byte
30ED: 7E              LD      A,(HL)              ; read it
30EE: FE 05           CP      $05                 
30F0: CA F8 30        JP      Z,$30F8             ; {code.loc_30f8} value 5 is allowed: continue
30F3: FE 10           CP      $10                 
30F5: C2 5B 31        JP      NZ,$315B            ; {code.loc_315b} not 5 or 16: derail into the data table

loc_30f8:
30F8: 06 08           LD      B,$08               ; eight entries to seat
30FA: FD 21 30 AA     LD      IY,$AA30            ; point at the entry-bank cells
30FE: 21 5E 31        LD      HL,$315E            ; point at the packed entry table

loc_3101:
3101: 7E              LD      A,(HL)              ; take a table byte
3102: FD 77 31        LD      (IY+$31),A          ; seat it into the entry's code field
3105: 23              INC     HL                  
3106: 7E              LD      A,(HL)              ; take the next table byte
3107: FD 77 00        LD      (IY+$00),A          ; seat it into the entry's shadow field
310A: 23              INC     HL                  
310B: FD 23           INC     IY                  ; step to the next entry...
310D: FD 23           INC     IY                  ; ...two bytes on
310F: 10 F0           DJNZ    $3101               ; {code.loc_3101} repeat for all eight
3111: C3 BC 2C        JP      $2CBC               ; {code.runSceneryForEra} run the frame's scenery

; a bare transfer to 0x307F and no return; no cell is read or written and
; no register moves
trampolineToLoc_307f:
3114: C3 7F 30        JP      $307F               ; {code.loc_307f} hand off to the fill path at 0x307F

; when a sentinel pair reads 0x68 then 0x10-or-0x05, seat four objects
; from a packed table into the sprite cell and shadow of the first four
; entry-bank slots and hand on to the frame's scenery run; otherwise
; transfer to the caption path
seedSceneryEntriesThenRunScenery:
3117: 21 39 AD        LD      HL,$AD39            ; point at the first sentinel byte
311A: 7E              LD      A,(HL)              ; read it
311B: FE 68           CP      $68                 ; is it the expected 0x68?
311D: C2 14 31        JP      NZ,$3114            ; {code.trampolineToLoc_307f} no: seat nothing, hand off to the derail path
3120: 23              INC     HL                  ; step to the second sentinel byte
3121: 7E              LD      A,(HL)              ; read it
3122: FE 10           CP      $10                 ; is it 16?
3124: CA 2C 31        JP      Z,$312C             ; {code.loc_312c} yes: seat the objects
3127: FE 05           CP      $05                 ; or 5?
3129: C2 14 31        JP      NZ,$3114            ; {code.trampolineToLoc_307f} neither: seat nothing, hand off to the derail path

loc_312c:
312C: 21 6E 31        LD      HL,$316E            ; point at the packed four-object table
312F: 06 04           LD      B,$04               ; four objects
3131: FD 21 30 AA     LD      IY,$AA30            ; point at the entry-bank cells

loc_3135:
3135: 7E              LD      A,(HL)              ; take the object's tint byte
3136: FD 77 31        LD      (IY+$31),A          ; seat it into the entry's code field
3139: C6 10           ADD     A,$10               ; one tile on...
313B: FD 77 33        LD      (IY+$33),A          ; ...into the abutting code field
313E: 23              INC     HL                  
313F: 7E              LD      A,(HL)              ; take the object's shape byte
3140: FD 77 00        LD      (IY+$00),A          ; seat it into the entry's shadow field
3143: FD 77 02        LD      (IY+$02),A          ; and its neighbour
3146: 23              INC     HL                  
3147: 11 10 00        LD      DE,$0010            ; one record stride...
314A: DD 19           ADD     IX,DE               ; ...steps the record cursor
314C: 11 04 00        LD      DE,$0004            ; four-byte entry stride...
314F: FD 19           ADD     IY,DE               ; ...steps the entry cursor a row
3151: 10 E2           DJNZ    $3135               ; {code.loc_3135} repeat for all four
3153: C3 BC 2C        JP      $2CBC               ; {code.runSceneryForEra} run the frame's scenery

; fix the fill byte and transfer to 0x30D1 without returning; choosing
; that one constant is the entire content of the entry, so whatever the
; caller carried in its place is discarded
seatSceneryFillByte0x28ThenClearEraScenery:
3156: 3E 28           LD      A,$28               ; force the fill byte to 0x28
3158: C3 D1 30        JP      $30D1               ; {code.clearSceneryEntriesThenRunEraScenery} hand on to clear the entries and run the era's scenery

loc_315b:
315B: C3 76 31        JP      $3176               ; {code.loc_3176} derail into the scenery-row data table when a guard reads wrong

; ---- $315E-$3175: data ----
315E: 40 68 38 62 60 70 68 D8 88 58 99 B0 37 43 CF 78
316E: 20 D0 50 60 A0 A0 D0 60

loc_3176:
3176: 60              LD      H,B                 
3177: 68              LD      L,B                 
3178: 61              LD      H,C                 
3179: 60              LD      H,B                 
317A: 61              LD      H,C                 
317B: 62              LD      H,D                 
317C: 63              LD      H,E                 
317D: 5C              LD      E,H                 
317E: 74              LD      (HL),H              
317F: 75              LD      (HL),L              
3180: 76              HALT                        
3181: 60              LD      H,B                 
3182: 61              LD      H,C                 
3183: 64              LD      H,H                 
3184: 65              LD      H,L                 
3185: 5D              LD      E,L                 
3186: 77              LD      (HL),A              
3187: 78              LD      A,B                 
3188: 79              LD      A,C                 
3189: 66              LD      H,(HL)              
318A: 67              LD      H,A                 
318B: 64              LD      H,H                 
318C: 65              LD      H,L                 
318D: 5E              LD      E,(HL)              
318E: 7A              LD      A,D                 
318F: 7B              LD      A,E                 
3190: 7C              LD      A,H                 
3191: 60              LD      H,B                 
3192: 61              LD      H,C                 
3193: 62              LD      H,D                 
3194: 63              LD      H,E                 
3195: 5F              LD      E,A                 
3196: 31 30 33        LD      SP,$3330            
3199: 32 85 86        LD      ($8685),A           
319C: 87              ADD     A,A                 
319D: 85              ADD     A,L                 
319E: 08              EX      AF,AF'              
319F: A7              AND     A                   
31A0: 32 CA 7E        LD      ($7ECA),A           
31A3: C8              RET     Z                   
31A4: FF              RST     $38                 
31A5: 5F              LD      E,A                 
31A6: 93              SUB     E                   
31A7: FB              EI                          
31A8: C4 AF D8        CALL    NZ,$D8AF            
31AB: 2A 6C E1        LD      HL,($E16C)          
31AE: 7A              LD      A,D                 
31AF: 42              LD      B,D                 
31B0: BD              CP      L                   
31B1: B0              OR      B                   
31B2: 5A              LD      E,D                 
31B3: B9              CP      C                   

; on the 00s and 30s tenths of the packed-decimal life counter 0xad05,
; service enemy-craft slot (units digit, only slots 0-6 whose record head
; at 0xa850 reads 0xff): advance that record's shape animation, then
; unless the state byte at ix+8 is 0x10 re-aim its heading toward a point
; the state byte indexes out of the aim table at 0xac65 -- state 0x11 aims
; at the table base, stores heading+0x80 into ix+1 and resets the record
; to state 0x10, every other state stores the heading straight into ix+1;
; on every other tenth hand off to layOutEnemyAimPointsFromScrollAngle
reaimAndAnimateEnemyCraftOnPhaseTick:
31B4: 3A 05 AD        LD      A,($AD05)           ; {hard.workRam+505} read the packed-decimal life-tick
31B7: 4F              LD      C,A                 ; keep it
31B8: E6 F0           AND     $F0                 ; look at the tens digit
31BA: 28 0D           JR      Z,$31C9             ; {code.loc_31c9} tens 0: service a craft slot
31BC: FE 30           CP      $30                 ; tens 3?
31BE: C2 6C 32        JP      NZ,$326C            ; {code.layOutEnemyAimPointsFromScrollAngle} any other tens: lay out the aim points instead
31C1: 3A 03 49        LD      A,($4903)           ; {hard.rom+4903} read a fixed program-image byte as a guard
31C4: FE 30           CP      $30                 ; expect it to read 0x30
31C6: C2 C9 31        JP      NZ,$31C9            ; {code.loc_31c9} on to servicing the slot either way

loc_31c9:
31C9: 79              LD      A,C                 ; recall the life-tick
31CA: E6 0F           AND     $0F                 ; take the units digit as a slot number
31CC: FE 07           CP      $07                 ; seven or more?
31CE: D0              RET     NC                  ; no such craft slot: leave
31CF: DD 21 50 A8     LD      IX,$A850            ; point at the craft records
31D3: FD 21 1A AA     LD      IY,$AA1A            ; point at the parallel craft entries
31D7: 87              ADD     A,A                 ; double the slot for the two-byte entry stride
31D8: 4F              LD      C,A                 
31D9: 06 00           LD      B,$00               
31DB: FD 09           ADD     IY,BC               ; step the entry cursor onto this slot
31DD: 87              ADD     A,A                 ; double three more times for the sixteen-byte record stride
31DE: 87              ADD     A,A                 
31DF: 87              ADD     A,A                 
31E0: 4F              LD      C,A                 
31E1: DD 09           ADD     IX,BC               ; step the record cursor onto this slot
31E3: DD 7E 00        LD      A,(IX+$00)          ; read the record's head byte
31E6: 3C              INC     A                   ; is it 0xFF -- occupied?
31E7: C0              RET     NZ                  ; empty slot: leave
31E8: CD 3A 32        CALL    $323A               ; {code.stepShapeAnimation} advance the craft's shape animation
31EB: DD 7E 08        LD      A,(IX+$08)          ; read its state byte
31EE: FE 10           CP      $10                 ; held?
31F0: C8              RET     Z                   ; held: nothing more to do
31F1: FE 11           CP      $11                 ; the re-aim-then-hold state?
31F3: 28 0C           JR      Z,$3201             ; {code.loc_3201} yes: aim at the table base and latch to held
31F5: 87              ADD     A,A                 ; state x 2 to index the aim table
31F6: 21 65 AC        LD      HL,$AC65            ; point at the aim-point table
31F9: DF              RST     $18                 ; index it by the state
31FA: CD B8 33        CALL    $33B8               ; {code.headingToward} compute the heading toward that aim point
31FD: DD 77 01        LD      (IX+$01),A          ; store it as the craft's heading
3200: C9              RET                         

loc_3201:
3201: 21 65 AC        LD      HL,$AC65            ; point at the aim-point table base
3204: CD B8 33        CALL    $33B8               ; {code.headingToward} compute the heading toward it
3207: C6 80           ADD     A,$80               ; turn it a half-circle
3209: DD 77 01        LD      (IX+$01),A          ; store as the craft's heading
320C: DD 36 08 10     LD      (IX+$08),$10        ; set the record to the held state
3210: DD 36 09 00     LD      (IX+$09),$00        ; clear its step timer
3214: C9              RET                         

; stock the machine for a game with only the FIRST player's context filled
; in: park the caption sprites, raise PLAY_ACTIVE, clear PLAYER_TWO_LIVES
; and the flag beside PLAY_ACTIVE, load PLAYER_ONE_LIVES from the settings
; cell carrying the starting count, TAKE ONE CREDIT off the packed-decimal
; count at 0xA986 and repaint the panel field from it, copy a fixed set of
; tilemap cells into their keeps, and send the sequence machine to its
; last phase. The subtract is decimal-corrected the way the hardware does
; it, so a byte that was never valid packed decimal still lands where the
; hardware would put it
startOnePlayerGame:
3215: CD 2B 0B        CALL    $0B2B               ; {code.hideCaptionSprites} park the caption sprites off-screen
3218: AF              XOR     A                   ; zero
3219: 32 31 AD        LD      ($AD31),A           ; {hard.workRam+531} clear the two-player-game flag
321C: 32 20 AD        LD      ($AD20),A           ; {hard.workRam+520} clear player two's life count
321F: 3D              DEC     A                   ; all bits set
3220: 32 30 AD        LD      ($AD30),A           ; {hard.workRam+530} raise the play-active flag
3223: 3A C1 A9        LD      A,($A9C1)           ; {hard.workRam+1C1} read the starting life count from the settings
3226: 32 10 AD        LD      ($AD10),A           ; {hard.workRam+510} seat it as player one's lives
3229: 21 86 A9        LD      HL,$A986            ; point at the packed-decimal credit count
322C: 7E              LD      A,(HL)              ; read it
322D: D6 01           SUB     $01                 ; take one credit
322F: 27              DAA                         ; decimal-adjust so it stays valid packed decimal
3230: 77              LD      (HL),A              ; store the reduced count
3231: CD FB 4A        CALL    $4AFB               ; {code.paintCreditCountPanel} repaint the credit count on the panel
3234: CD 30 4B        CALL    $4B30               ; {code.copyThreeTilemapCellsFromBothPlanes} copy three tilemap cells from both planes into their keeps
3237: C3 2A 17        JP      $172A               ; {code.seatSequencePhase3AndResetSubStep} send the sequence machine to its last phase

; count one record's step timer down and refresh that record's shape byte
; from the entry the NEW count selects, in the run its own selector byte
; points at; a timer already at zero is left alone
stepShapeAnimation:
323A: DD 7E 09        LD      A,(IX+$09)          ; read the record's step timer
323D: A7              AND     A                   ; is it already zero?
323E: C8              RET     Z                   ; yes: leave the animation stopped
323F: 3D              DEC     A                   ; count the timer down one
3240: DD 77 09        LD      (IX+$09),A          ; store it
3243: 4F              LD      C,A                 ; hold the new count as the step index
3244: DD 7E 0A        LD      A,(IX+$0A)          ; read the record's run selector
3247: 21 38 34        LD      HL,$3438            ; point at the table of shape-run pointers
324A: D7              RST     $10                 ; fetch this record's run pointer
324B: EB              EX      DE,HL               
324C: 79              LD      A,C                 ; recall the step index
324D: CF              RST     $08                 ; fetch the shape byte for this step
324E: DD 77 08        LD      (IX+$08),A          ; store it as the record's shape
3251: C9              RET                         

; fold a fixed span of the program image and let the sequence's inner step
; go on if it still adds up; a span that does not fold to the expected
; value throws the sequence a whole phase forward instead, which derails
; it rather than halting it
guardBlockOrDerailSequence:
3252: 01 00 03        LD      BC,$0300            ; 768 bytes to fold
3255: 21 08 00        LD      HL,$0008            ; starting at the program image
3258: 1E 00           LD      E,$00               ; clear the running exclusive-or

loc_325a:
325A: 7B              LD      A,E                 
325B: AE              XOR     (HL)                ; fold the next byte into the running exclusive-or
325C: 23              INC     HL                  
325D: 0B              DEC     BC                  ; count it off
325E: 5F              LD      E,A                 
325F: 79              LD      A,C                 
3260: B0              OR      B                   ; loop until the whole span is folded
3261: 20 F7           JR      NZ,$325A            ; {code.loc_325a}
3263: 3E 52           LD      A,$52               ; the expected complement
3265: 83              ADD     A,E                 ; add it to the fold
3266: C2 11 0F        JP      NZ,$0F11            ; {code.advanceSequencePhase} a tampered span nets non-zero: throw the sequence a phase forward
3269: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} otherwise step the sequence's sub-step

; when the mode byte in C selects sub-mode 7 (low nibble == 7), fill
; sprite object 0xac64's twelve coordinate fields (0x10-0x1b) with six XY
; pairs around centre (0x78 across, 0x84 down): the scroll angle +0x40 and
; the scroll angle itself, each drawn through the velocity table (via
; 0x59d1) at x8 and x16 radii, the +0x40 direction also mirrored to its
; negatives; other sub-modes return without writing
layOutEnemyAimPointsFromScrollAngle:
326C: 79              LD      A,C                 ; recall the mode byte
326D: E6 0F           AND     $0F                 ; its sub-mode nibble
326F: FE 07           CP      $07                 ; sub-mode 7?
3271: C0              RET     NZ                  ; any other sub-mode: leave without writing
3272: DD 21 64 AC     LD      IX,$AC64            ; point at the sprite object to fill
3276: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the scroll angle
3279: C6 40           ADD     A,$40               ; turn it a quarter-circle
327B: CD D1 59        CALL    $59D1               ; {code.loc_59d1} look up the velocity vector for that direction
327E: EB              EX      DE,HL               
327F: 29              ADD     HL,HL               ; scale the vector left three places to an x8 radius
3280: 29              ADD     HL,HL               
3281: 29              ADD     HL,HL               
3282: 7C              LD      A,H                 
3283: C6 78           ADD     A,$78               ; offset the across component from screen centre
3285: DD 77 10        LD      (IX+$10),A          ; store the first aim point's X
3288: 7C              LD      A,H                 
3289: ED 44           NEG                         ; flip the component's sign to mirror it...
328B: C6 78           ADD     A,$78               ; ...the same distance the other side of centre
328D: DD 77 14        LD      (IX+$14),A          ; store the mirrored aim point's X
3290: 29              ADD     HL,HL               ; double again to an x16 radius
3291: 7C              LD      A,H                 
3292: C6 78           ADD     A,$78               ; offset from centre
3294: DD 77 12        LD      (IX+$12),A          ; store the second aim point's X
3297: 7C              LD      A,H                 
3298: ED 44           NEG                         ; mirror across centre...
329A: C6 78           ADD     A,$78               ; ...back from centre
329C: DD 77 16        LD      (IX+$16),A          ; store its mirror's X
329F: 60              LD      H,B                 ; take the down component of the vector
32A0: 69              LD      L,C                 
32A1: 29              ADD     HL,HL               ; scale left three places to an x8 radius
32A2: 29              ADD     HL,HL               
32A3: 29              ADD     HL,HL               
32A4: 7C              LD      A,H                 
32A5: C6 84           ADD     A,$84               ; offset from screen centre down
32A7: DD 77 11        LD      (IX+$11),A          ; store the first aim point's Y
32AA: 7C              LD      A,H                 
32AB: ED 44           NEG                         ; mirror across centre...
32AD: C6 84           ADD     A,$84               ; ...back from centre
32AF: DD 77 15        LD      (IX+$15),A          ; store the mirrored Y
32B2: 29              ADD     HL,HL               ; double to an x16 radius
32B3: 7C              LD      A,H                 
32B4: C6 84           ADD     A,$84               ; offset from centre
32B6: DD 77 13        LD      (IX+$13),A          ; store the second aim point's Y
32B9: 7C              LD      A,H                 
32BA: ED 44           NEG                         ; mirror across centre...
32BC: C6 84           ADD     A,$84               ; ...back from centre
32BE: DD 77 17        LD      (IX+$17),A          ; store its mirror's Y
32C1: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the scroll angle again -- not turned this time
32C4: CD D1 59        CALL    $59D1               ; {code.loc_59d1} look up its velocity vector
32C7: EB              EX      DE,HL               
32C8: 29              ADD     HL,HL               ; scale left three places to an x8 radius
32C9: 29              ADD     HL,HL               
32CA: 29              ADD     HL,HL               
32CB: 7C              LD      A,H                 
32CC: C6 78           ADD     A,$78               ; offset from centre across
32CE: DD 77 18        LD      (IX+$18),A          ; store the fifth aim point's X
32D1: 29              ADD     HL,HL               ; double to an x16 radius
32D2: 7C              LD      A,H                 
32D3: C6 78           ADD     A,$78               ; offset from centre
32D5: DD 77 1A        LD      (IX+$1A),A          ; store the sixth aim point's X
32D8: 60              LD      H,B                 ; take the down component
32D9: 69              LD      L,C                 
32DA: 29              ADD     HL,HL               ; scale left three places to an x8 radius
32DB: 29              ADD     HL,HL               
32DC: 29              ADD     HL,HL               
32DD: 7C              LD      A,H                 
32DE: C6 84           ADD     A,$84               ; offset from centre down
32E0: DD 77 19        LD      (IX+$19),A          ; store the fifth aim point's Y
32E3: 29              ADD     HL,HL               ; double to an x16 radius
32E4: 7C              LD      A,H                 
32E5: C6 84           ADD     A,$84               ; offset from centre
32E7: DD 77 1B        LD      (IX+$1B),A          ; store the sixth aim point's Y
32EA: C9              RET                         

; hold the machine still at power-on and then hand it over: count twelve
; passes down in a work-RAM cell, petting the watchdog 256 times inside
; each so the board is never reset while nothing happens, leave the cell
; and the two counting registers at zero and the pointer on the cell, tell
; the audio processor to go quiet, pick up the byte that decides the
; interrupt-enable bit, and fall into the routine that starts the machine
petWatchdogThroughStartupDelayThenStartMachine:
32EB: 32 00 C2        LD      ($C200),A           ; kick the watchdog
32EE: 21 EB A9        LD      HL,$A9EB            ; point at the startup-delay cell
32F1: 36 0C           LD      (HL),$0C            ; set it to twelve passes

loc_32f3:
32F3: 01 00 00        LD      BC,$0000            ; reset the inner and outer tick counters

loc_32f6:
32F6: 10 FE           DJNZ    $32F6               ; {code.loc_32f6} spin the inner counter down -- a pure time delay
32F8: 32 00 C2        LD      ($C200),A           ; kick the watchdog
32FB: 0D              DEC     C                   ; count the outer loop
32FC: 20 F8           JR      NZ,$32F6            ; {code.loc_32f6} 256 kicks per pass
32FE: 35              DEC     (HL)                ; count one pass off the startup-delay cell
32FF: 20 F2           JR      NZ,$32F3            ; {code.loc_32f3} twelve passes in all
3301: AF              XOR     A                   ; command 0...
3302: CD F8 55        CALL    $55F8               ; {code.sendSoundCommand} ...tell the audio processor to go quiet
3305: 3A 87 4C        LD      A,($4C87)           ; {hard.rom+4C87} pick up the byte that sets the interrupt-enable bit
3308: C3 A8 00        JP      $00A8               ; {code.enableInterruptAndEnterForegroundLoop} enable interrupts and drop into the foreground loop

loc_330b:
330B: 21 EB A9        LD      HL,$A9EB            ; point at the delay cell
330E: 35              DEC     (HL)                ; count it down
330F: C0              RET     NZ                  ; not yet elapsed: leave
3310: CD C3 4C        CALL    $4CC3               ; {code.fileScoreIntoHighScoreTable} try to file the score into the high-score table
3313: D2 26 33        JP      NC,$3326            ; {code.loc_3326} it did not place: branch away
3316: 11 09 03        LD      DE,$0309            
3319: FF              RST     $38                 ; queue ring command 3 / argument 9
331A: 1E 0B           LD      E,$0B               
331C: FF              RST     $38                 ; queue ring command 3 / argument 11
331D: 3A 43 08        LD      A,($0843)           ; {hard.rom+843} take a fixed byte from the program image
3320: 32 AC A9        LD      ($A9AC),A           ; {hard.workRam+1AC} seat it
3323: C3 E7 12        JP      $12E7               ; {code.passTurnToOtherPlayerIfLivesElseStepSequence} pass the turn to the other player if lives remain, else step the sequence

loc_3326:
3326: CD 3A 58        CALL    $583A               ; {code.loc_583a}
3329: 3E 00           LD      A,$00               ; zero...
332B: 32 0C AD        LD      ($AD0C),A           ; {hard.workRam+50C} ...clear the pen colour
332E: 3E F1           LD      A,$F1               ; 0xF1...
3330: 32 0B AD        LD      ($AD0B),A           ; {hard.workRam+50B} ...set the pen glyph
3333: CD E1 01        CALL    $01E1               ; {code.armThePenRouteThenColdStartOnATamperedImage} re-arm the pen route
3336: 06 00           LD      B,$00               ; 256 bytes to fold
3338: 21 F1 01        LD      HL,$01F1            ; starting at this program run
333B: AF              XOR     A                   ; clear the running sum

loc_333c:
333C: 86              ADD     A,(HL)              ; fold the next byte in
333D: 23              INC     HL                  
333E: 10 FC           DJNZ    $333C               ; {code.loc_333c} over all 256 bytes
3340: D6 19           SUB     $19                 ; subtract the expected sum
3342: C4 11 0F        CALL    NZ,$0F11            ; {code.advanceSequencePhase} a tampered run: throw the sequence a phase forward
3345: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} then step the sequence's sub-step

; ---- $3348-$335D: data ----
3348: 11 A7 13 68 3B 34 F1 68 D7 F1 DC 0F 68 F1 88 57
3358: A5 BF 34 D7 ED B9

; sequence-machine arm: fold a fixed image run into the sequence-phase
; cell as a tamper tripwire (net-zero on a genuine image), then seat the
; caption pen (glyph 0xAD0B / colour 0xAD0C, and the active player's save
; block) from a two-byte glyph/colour record indexed by that player's era;
; steps the sub-step an extra time if the pen colour was unchanged, re-
; arms the pen route, then steps the sub-step again as a tail
seatCaptionPenFromEraFoldingTamperIntoPhase:
335E: 3A AB A9        LD      A,($A9AB)           ; {hard.workRam+1AB} read the sequence-phase cell -- the tamper accumulator
3361: 21 8C 17        LD      HL,$178C            ; point at the image block to fold
3364: 06 1E           LD      B,$1E               ; thirty bytes

loc_3366:
3366: 86              ADD     A,(HL)              ; fold the next byte in
3367: 23              INC     HL                  
3368: 10 FC           DJNZ    $3366               ; {code.loc_3366} over all thirty
336A: C6 2C           ADD     A,$2C               ; add the genuine-image bias
336C: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} store back into the phase cell -- nets to leave the phase standing on a genuine image
336F: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read which player is up
3372: A7              AND     A                   ; is it player one?
3373: 11 1B AD        LD      DE,$AD1B            ; point at player one's saved-pen record
3376: 3A 14 AD        LD      A,($AD14)           ; {hard.workRam+514} read player one's era
3379: 28 06           JR      Z,$3381             ; {code.loc_3381} player one: use those
337B: 11 2B AD        LD      DE,$AD2B            ; otherwise point at player two's saved-pen record
337E: 3A 24 AD        LD      A,($AD24)           ; {hard.workRam+524} read player two's era

loc_3381:
3381: 87              ADD     A,A                 ; era x 2 to index the glyph/colour table
3382: 21 8D 0F        LD      HL,$0F8D            ; point at the glyph/colour table
3385: CF              RST     $08                 ; fetch the era's glyph
3386: 12              LD      (DE),A              ; write it into the saved-pen record
3387: 32 0B AD        LD      ($AD0B),A           ; {hard.workRam+50B} and onto the live pen glyph
338A: 23              INC     HL                  
338B: 13              INC     DE                  
338C: 7E              LD      A,(HL)              ; fetch the era's colour
338D: 12              LD      (DE),A              ; write it into the saved-pen record
338E: 21 0C AD        LD      HL,$AD0C            ; point at the live pen colour
3391: BE              CP      (HL)                ; did the pen colour already hold this?
3392: 77              LD      (HL),A              ; set the live pen colour
3393: CC 1A 0F        CALL    Z,$0F1A             ; {code.advanceSequenceSubStep} if it was unchanged, step the sub-step an extra time
3396: CD E1 01        CALL    $01E1               ; {code.armThePenRouteThenColdStartOnATamperedImage} re-arm the pen route
3399: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sub-step as a tail

; seed the pen the active player's SAVED context block will hand back —
; the glyph and the colour a caption is stamped in — from the era recorded
; in that same block, both halves coming as one two-byte record out of an
; inline table the era indexes; the live pen is left alone, where the
; nearer arm at 0x335E sets it too, sums a run of image bytes into a
; tamper cell before doing any of it, and can repaint
setSavedPenFromEra:
339C: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read which player is up
339F: A7              AND     A                   ; player one?
33A0: 11 1B AD        LD      DE,$AD1B            ; point at player one's saved-pen record
33A3: 3A 14 AD        LD      A,($AD14)           ; {hard.workRam+514} read player one's round index
33A6: 28 06           JR      Z,$33AE             ; {code.loc_33ae} player one: use those
33A8: 11 2B AD        LD      DE,$AD2B            ; otherwise player two's saved-pen record
33AB: 3A 24 AD        LD      A,($AD24)           ; {hard.workRam+524} read player two's round index

loc_33ae:
33AE: 87              ADD     A,A                 ; round x 2 to index the table
33AF: 21 8D 0F        LD      HL,$0F8D            ; point at the glyph/colour table
33B2: DF              RST     $18                 ; index it by the round
33B3: ED A0           LDI                         ; copy the glyph into the saved-pen record
33B5: ED A0           LDI                         ; copy the colour after it
33B7: C9              RET                         

; return the heading from an object to a point as a byte of a 256-step
; circle: the signs and relative sizes of the two axis differences pick
; one of eight octants, and the shorter leg over the longer places the
; answer at one of thirty-two rungs inside it
headingToward:
33B8: 0E 00           LD      C,$00               ; start the sector code at zero
33BA: FD 46 31        LD      B,(IY+$31)          ; the object's second-axis position
33BD: 5E              LD      E,(HL)              ; the point's first-axis coordinate -- kept for later
33BE: 2D              DEC     L                   ; step to the point's second-axis coordinate
33BF: 7E              LD      A,(HL)              ; read it
33C0: 90              SUB     B                   ; reach to the point along the second axis
33C1: 30 04           JR      NC,$33C7            ; {code.loc_33c7} already positive
33C3: ED 44           NEG                         ; take its magnitude
33C5: CB C1           SET     0,C                 ; mark the second axis as running negative

loc_33c7:
33C7: 57              LD      D,A                 ; hold the second-axis distance
33C8: FD 46 00        LD      B,(IY+$00)          ; the object's first-axis position
33CB: 7B              LD      A,E                 ; recall the point's first-axis coordinate
33CC: 90              SUB     B                   ; reach along the first axis
33CD: 30 04           JR      NC,$33D3            ; {code.loc_33d3} already positive
33CF: ED 44           NEG                         ; take its magnitude
33D1: CB C9           SET     1,C                 ; mark the first axis as running negative

loc_33d3:
33D3: 5F              LD      E,A                 ; hold the first-axis distance
33D4: 08              EX      AF,AF'              
33D5: 7B              LD      A,E                 
33D6: 08              EX      AF,AF'              
33D7: 92              SUB     D                   ; compare the two distances
33D8: 28 35           JR      Z,$340F             ; {code.loc_340f} equal: read a fixed diagonal heading
33DA: 30 02           JR      NC,$33DE            ; {code.loc_33de} first axis is the longer
33DC: CB D1           SET     2,C                 ; first axis is the shorter

loc_33de:
33DE: 2E 00           LD      L,$00               ; clear the low byte of the dividend
33E0: CB 51           BIT     2,C                 ; which leg is the shorter?
33E2: 20 03           JR      NZ,$33E7            ; {code.loc_33e7}
33E4: 62              LD      H,D                 ; shorter = second-axis distance
33E5: 18 02           JR      $33E9               ; {code.loc_33e9}

loc_33e7:
33E7: 63              LD      H,E                 ; shorter = first-axis distance
33E8: 5A              LD      E,D                 ; longer = second-axis distance, the divisor

loc_33e9:
33E9: 06 08           LD      B,$08               ; eight quotient bits
33EB: AF              XOR     A                   ; clear the remainder

loc_33ec:
33EC: ED 6A           ADC     HL,HL               ; shift the dividend up, carrying a quotient bit
33EE: 7C              LD      A,H                 
33EF: 38 03           JR      C,$33F4             ; {code.loc_33f4}
33F1: BB              CP      E                   ; does the divisor go into the running remainder?
33F2: 38 03           JR      C,$33F7             ; {code.loc_33f7}

loc_33f4:
33F4: 93              SUB     E                   ; subtract the divisor
33F5: 67              LD      H,A                 
33F6: AF              XOR     A                   

loc_33f7:
33F7: 3F              CCF                         ; shift the quotient bit in
33F8: 10 F2           DJNZ    $33EC               ; {code.loc_33ec} eight bits in all
33FA: 45              LD      B,L                 ; the quotient is the rung within the sector
33FB: 79              LD      A,C                 ; the sector code
33FC: 21 15 34        LD      HL,$3415            ; point at the sector-heading table
33FF: DF              RST     $18                 ; index it by the sector
3400: 78              LD      A,B                 ; the rung...
3401: 0F              RRCA                        ; ...scaled down to one of thirty-two rungs
3402: 0F              RRCA                        
3403: E6 1F           AND     $1F                 
3405: CB 6E           BIT     5,(HL)              ; does this sector count its rungs backwards?
3407: 28 04           JR      Z,$340D             ; {code.loc_340d}
3409: 47              LD      B,A                 
340A: 3E 1F           LD      A,$1F               
340C: 90              SUB     B                   ; reverse the rung within the sector

loc_340d:
340D: 86              ADD     A,(HL)              ; add the sector's base heading
340E: C9              RET                         

loc_340f:
340F: 21 1D 34        LD      HL,$341D            ; point at the diagonal-heading table
3412: 79              LD      A,C                 ; the sector code
3413: CF              RST     $08                 ; read the fixed heading for this diagonal
3414: C9              RET                         

; ---- $3415-$36AE: data ----
3415: 20 40 C0 A0 00 60 E0 80 20 60 E0 A0 21 50 0C CD
3425: 8C 01 EB 5E 23 56 23 23 3A 0C AD C6 05 E6 0F 4F
3435: C3 FF 0B 6F 34 8F 34 AF 34 CF 34 EF 34 0F 35 2F
3445: 35 4F 35 6F 35 8F 35 AF 35 CF 35 EF 35 0F 36 2F
3455: 36 4F 36 6F 36 8F 36 11 A7 13 68 3B 34 F1 88 57
3465: A5 BF 34 D7 F1 68 3B 57 BF B9 11 09 09 09 09 09
3475: 09 09 09 09 09 09 09 09 09 09 09 09 09 09 09 09
3485: 09 09 09 09 09 09 09 09 09 09 11 08 08 08 08 08
3495: 08 08 08 08 08 08 08 08 08 08 09 08 08 08 08 08
34A5: 08 08 08 08 08 08 08 08 08 08 11 00 00 00 00 00
34B5: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
34C5: 00 00 00 00 00 00 00 00 00 00 11 0A 0A 0A 0A 0A
34D5: 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A
34E5: 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 11 0B 0B 0B 0B 0B
34F5: 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B
3505: 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 11 10 10 10 10 10
3515: 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
3525: 10 10 10 10 10 10 10 10 10 10 11 10 10 10 10 10
3535: 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
3545: 10 10 10 10 10 10 10 10 10 0D 11 10 10 10 10 10
3555: 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
3565: 10 10 10 10 10 10 10 10 0C 0D 11 10 10 10 10 10
3575: 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
3585: 10 10 10 10 10 10 10 0C 0D 0D 11 09 09 09 09 09
3595: 09 09 09 09 09 09 09 09 09 09 09 09 09 09 09 09
35A5: 09 09 09 09 09 09 09 10 10 10 11 08 08 08 08 08
35B5: 08 08 08 08 08 08 08 08 08 08 08 08 08 08 08 08
35C5: 08 08 08 08 08 08 08 10 10 10 11 00 00 00 00 00
35D5: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
35E5: 00 00 00 00 00 00 00 10 10 10 11 0A 0A 0A 0A 0A
35F5: 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A 0A
3605: 0A 0A 0A 0A 0A 0A 0A 10 10 10 11 0B 0B 0B 0B 0B
3615: 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B 0B
3625: 0B 0B 0B 0B 0B 0B 0B 10 10 10 11 10 10 10 10 10
3635: 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
3645: 10 10 10 10 10 10 10 10 10 10 11 10 10 10 10 10
3655: 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
3665: 10 10 10 10 10 10 0D 10 10 10 11 10 10 10 10 10
3675: 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
3685: 10 10 10 10 10 10 10 10 10 10 11 10 10 10 10 10
3695: 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
36A5: 10 10 10 10 10 10 0D 10 10 10

; enemy-wave substep: while the wave-hold cell 0xacc6 is clear, dispatch
; by era and life-phase -- era 4 to spawnEnemyWaveIntoFreeSlots, phase 7
; to stopFiveSlotAnimations, phase below 7 to
; gateTheFreeSlotSearchAndPickItsRun, phase 8 to
; spawnEnemyCraftWhenBandUnderTwo; at phase 9+ with the low life-tick
; 0xad05 spent, spawn a fresh wave inline across the 0xa850/0xaa1a craft
; band from a heading-biased shape run, then request a sound once enough
; of the five slots filled
driveEnemyWaveForLifePhase:
36AF: 3A C6 AC        LD      A,($ACC6)           ; {hard.workRam+4C6} read the wave-hold cell
36B2: A7              AND     A                   ; test it
36B3: C0              RET     NZ                  ; a wave is being held: nothing to do this frame
36B4: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era number
36B7: FE 04           CP      $04                 ; is this era 4?
36B9: CA 6E 38        JP      Z,$386E             ; {code.spawnEnemyWaveIntoFreeSlots} era 4: spawn the wave straight into the free slots
36BC: 21 05 AD        LD      HL,$AD05            ; point at the low life-tick byte -- the phase tails all read it
36BF: 3A 06 AD        LD      A,($AD06)           ; {hard.workRam+506} read the life-phase byte
36C2: E6 0F           AND     $0F                 ; keep its low nibble -- the phase
36C4: FE 07           CP      $07                 ; phase 7?
36C6: CA 55 38        JP      Z,$3855             ; {code.stopFiveSlotAnimations} phase 7: settle the five slot animations
36C9: DA BD 37        JP      C,$37BD             ; {code.gateTheFreeSlotSearchAndPickItsRun} below 7: gate the free-slot search and pick its run
36CC: FE 09           CP      $09                 ; phase 8?
36CE: DA 9F 37        JP      C,$379F             ; {code.spawnEnemyCraftWhenBandUnderTwo} phase 8: spawn a craft while the band is under two
36D1: 7E              LD      A,(HL)              ; read the low life-tick
36D2: A7              AND     A                   ; test it
36D3: C0              RET     NZ                  ; not spent yet: wait
36D4: CD 4B 4B        CALL    $4B4B               ; {code.drawRandomByte} draw a random byte
36D7: 0F              RRCA                        ; roll its low bit into carry
36D8: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era number
36DB: 8F              ADC     A,A                 ; double it and fold the random bit in as the low bit -- the wave descriptor index
36DC: 21 C2 AC        LD      HL,$ACC2            
36DF: 36 FF           LD      (HL),$FF            ; raise the wave mark
36E1: 23              INC     HL                  
36E2: 77              LD      (HL),A              ; store the wave descriptor index
36E3: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the player heading
36E6: C6 08           ADD     A,$08               ; bias it by 8 -- round to the nearest sector
36E8: 0F              RRCA                        ; shift the biased heading down four to a 0-15 sector index
36E9: 0F              RRCA                        
36EA: 0F              RRCA                        
36EB: 0F              RRCA                        
36EC: E6 0F           AND     $0F                 ; mask to the sixteen-sector index
36EE: 21 D9 38        LD      HL,$38D9            ; point at the heading-bias table
36F1: DF              RST     $18                 ; index it by the sector
36F2: 4E              LD      C,(HL)              ; take the shape bias for this heading
36F3: 3A C3 AC        LD      A,($ACC3)           ; {hard.workRam+4C3} read the wave descriptor index
36F6: 87              ADD     A,A                 ; times sixteen -- a sixteen-byte descriptor entry
36F7: 87              ADD     A,A                 
36F8: 87              ADD     A,A                 
36F9: 87              ADD     A,A                 
36FA: 21 7B 39        LD      HL,$397B            ; point at the wave-descriptor table
36FD: DF              RST     $18                 ; index it by the descriptor number
36FE: EB              EX      DE,HL               ; keep the descriptor pointer aside
36FF: 3A C1 AC        LD      A,($ACC1)           ; {hard.workRam+4C1} read the round's craft count
3702: 47              LD      B,A                 ; use it as the slot loop count
3703: 3A 02 AD        LD      A,($AD02)           ; {hard.workRam+502} read the kills still owed
3706: A7              AND     A                   ; test it
3707: 20 02           JR      NZ,$370B            ; {code.loc_370b} some owed: keep the craft count
3709: 06 05           LD      B,$05               ; none owed: fill a fixed five slots instead

loc_370b:
370B: AF              XOR     A                   
370C: 32 11 A8        LD      ($A811),A           ; {hard.workRam+11} zero the filled-slot counter
370F: DD 21 50 A8     LD      IX,$A850            ; point at the first craft record
3713: FD 21 1A AA     LD      IY,$AA1A            ; point at its sprite entry

loc_3717:
3717: DD 7E 00        LD      A,(IX+$00)          ; read this slot's head byte
371A: A7              AND     A                   ; test it
371B: C2 68 37        JP      NZ,$3768            ; {code.loc_3768} slot busy: step to the next one
371E: 1A              LD      A,(DE)              ; read the descriptor's shape offset
371F: 81              ADD     A,C                 ; add the heading bias
3720: 87              ADD     A,A                 ; double it -- two-byte shape entries
3721: 21 E9 38        LD      HL,$38E9            ; point at the shape-run table
3724: CF              RST     $08                 ; fetch the shape byte
3725: FD 77 31        LD      (IY+$31),A          ; write the shape into the sprite entry
3728: 23              INC     HL                  
3729: 7E              LD      A,(HL)              ; read the paired attribute byte
372A: FD 77 00        LD      (IY+$00),A          ; write it to the entry head
372D: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the player heading
3730: C6 80           ADD     A,$80               ; flip it half a turn
3732: DD 77 01        LD      (IX+$01),A          ; store it as the craft's heading
3735: DD 77 02        LD      (IX+$02),A          ; and as its facing
3738: CD 2D 38        CALL    $382D               ; {code.pickScriptAtRandomOrInTurn} pick a script at random or in turn
373B: C6 09           ADD     A,$09               ; offset the script number by nine
373D: DD 77 0A        LD      (IX+$0A),A          ; store the script index
3740: 13              INC     DE                  ; advance to the descriptor's second field
3741: 1A              LD      A,(DE)              ; read the descriptor tail byte
3742: DD 77 0E        LD      (IX+$0E),A          ; store it as the slot's tail
3745: 13              INC     DE                  ; advance the descriptor pointer for the next slot
3746: DD 36 03 00     LD      (IX+$03),$00        ; clear the sub-position
374A: DD 36 05 00     LD      (IX+$05),$00        ; clear the second sub-position
374E: DD 36 09 20     LD      (IX+$09),$20        ; prime the step counter
3752: D9              EXX                         ; set the working registers aside across the animation step
3753: CD 3A 32        CALL    $323A               ; {code.stepShapeAnimation} step the shape animation once
3756: D9              EXX                         ; restore them
3757: DD 36 00 FE     LD      (IX+$00),$FE        ; mark the slot live (0xFE)
375B: DD 7E 0E        LD      A,(IX+$0E)          ; read the slot's tail byte
375E: A7              AND     A                   ; test it
375F: 20 03           JR      NZ,$3764            ; {code.loc_3764} non-zero tail: leave the slot at 0xFE
3761: DD 34 00        INC     (IX+$00)            ; clear tail: bump the head to 0xFF -- fully settled

loc_3764:
3764: 21 11 A8        LD      HL,$A811            ; point at the filled-slot counter
3767: 34              INC     (HL)                ; count this filled slot

loc_3768:
3768: EB              EX      DE,HL               
3769: 11 10 00        LD      DE,$0010            ; a sixteen-byte record stride
376C: DD 19           ADD     IX,DE               ; advance to the next craft record
376E: FD 23           INC     IY                  ; advance to the next two-byte sprite entry
3770: FD 23           INC     IY                  
3772: EB              EX      DE,HL               
3773: 10 A2           DJNZ    $3717               ; {code.loc_3717} loop over the slots
3775: AF              XOR     A                   
3776: 32 C2 AC        LD      ($ACC2),A           ; {hard.workRam+4C2} clear the wave mark
3779: 3E E4           LD      A,$E4               
377B: 32 12 A8        LD      ($A812),A           ; {hard.workRam+12} stamp the wave-claim timer ready (0xE4)
377E: 21 11 A8        LD      HL,$A811            ; point at the filled-slot counter
3781: 7E              LD      A,(HL)              ; read how many filled
3782: FE 05           CP      $05                 ; five or more?
3784: D2 17 58        JP      NC,$5817            ; {code.requestEnemyWaveSound} enough filled: request the enemy-wave sound
3787: 21 C1 AC        LD      HL,$ACC1            ; point at the round's craft count
378A: BE              CP      (HL)                ; compare the filled count against it
378B: 7E              LD      A,(HL)              ; take the craft count
378C: 32 11 A8        LD      ($A811),A           ; {hard.workRam+11} store it as the filled count
378F: D2 17 58        JP      NC,$5817            ; {code.requestEnemyWaveSound} filled met the count: request the enemy-wave sound
3792: C9              RET                         

loc_3793:
3793: 06 05           LD      B,$05               ; a fixed run of five slots
3795: DD 21 90 A8     LD      IX,$A890            ; point at the fifth craft record
3799: FD 21 22 AA     LD      IY,$AA22            ; point at its sprite entry
379D: 18 37           JR      $37D6               ; {code.spawnEnemyIntoFreeSlotElseStepSearch} fill the first free one

; gate a spawn tick on the packed-decimal phase byte the caller points at
; (return unless it is 0x00 or 0x30), count the busy heads across the
; seven-record enemy-craft band at 0xa850, and while fewer than two are
; busy run the free-slot search -- the cleared run via $3793 when the
; owed-kills cell 0xad02 is zero, else the owed run (b from the round's
; craft count 0xacc1, seated at 0xa8b0/0xaa26) via
; spawnEnemyIntoFreeSlotElseStepSearch; stages nothing when the gate is
; shut or two heads are busy
spawnEnemyCraftWhenBandUnderTwo:
379F: 7E              LD      A,(HL)              ; read the phase byte the caller points at
37A0: A7              AND     A                   ; test it
37A1: 28 03           JR      Z,$37A6             ; {code.loc_37a6} zero: an idle tick, go count the band
37A3: FE 30           CP      $30                 ; the open phase?
37A5: C0              RET     NZ                  ; any other value: not a spawning tick

loc_37a6:
37A6: 21 50 A8        LD      HL,$A850            ; point at the first craft record
37A9: 11 10 00        LD      DE,$0010            ; the record stride
37AC: 01 00 07        LD      BC,$0700            ; seven slots to scan, busy count starts at zero

loc_37af:
37AF: 7E              LD      A,(HL)              ; read this slot's head byte
37B0: A7              AND     A                   ; test it
37B1: 28 01           JR      Z,$37B4             ; {code.loc_37b4} free: skip
37B3: 0C              INC     C                   ; busy: count it

loc_37b4:
37B4: 19              ADD     HL,DE               ; step to the next record
37B5: 10 F8           DJNZ    $37AF               ; {code.loc_37af} scan all seven
37B7: 79              LD      A,C                 ; take the busy count
37B8: FE 02           CP      $02                 ; two or more busy?
37BA: D0              RET     NC                  ; band already full enough: stage nothing
37BB: 18 07           JR      $37C4               ; {code.loc_37c4} fewer than two: pick the search run

; decide whether this is a spawning tick and, if it is, choose which run
; of object slots the free-slot search walks: the caller points at a
; counter cell and only two of its values open the gate, every other value
; ending the entry with nothing staged; past the gate the count of kills
; still owed picks between two runs of the one slot file -- while any are
; owed the run starts two records higher and is as long as the round's
; craft count asks, and once none are owed a fixed run of five starts
; lower -- and control leaves for the search without coming back. The role
; names no address for the gate byte on purpose: it is read through a
; pointer, so the routine itself cannot know what it is
gateTheFreeSlotSearchAndPickItsRun:
37BD: 7E              LD      A,(HL)              ; read the gate byte the caller points at
37BE: A7              AND     A                   ; test it
37BF: 28 03           JR      Z,$37C4             ; {code.loc_37c4} zero: a spawning tick
37C1: FE 30           CP      $30                 ; the other open value?
37C3: C0              RET     NZ                  ; anything else: gate shut, stage nothing

loc_37c4:
37C4: 3A 02 AD        LD      A,($AD02)           ; {hard.workRam+502} read the kills still owed
37C7: A7              AND     A                   ; test it
37C8: 28 C9           JR      Z,$3793             ; {code.loc_3793} none owed: run the fixed five-slot search
37CA: 3A C1 AC        LD      A,($ACC1)           ; {hard.workRam+4C1} read the round's craft count
37CD: 47              LD      B,A                 ; use it as the search length
37CE: DD 21 B0 A8     LD      IX,$A8B0            ; point at the seventh craft record
37D2: FD 21 26 AA     LD      IY,$AA26            ; point at its sprite entry

; work one slot in a downward free-slot search: a busy slot passes the
; turn to the search tail, a free slot is claimed and stocked with a
; random heading-derived velocity, facing, script and fresh animation (at
; most one slot filled per turn); this fills the green enemy-craft band
; (0xA850) one slot at a time
spawnEnemyIntoFreeSlotElseStepSearch:
37D6: DD 7E 00        LD      A,(IX+$00)          ; read this slot's head byte
37D9: A7              AND     A                   ; test it
37DA: C2 47 38        JP      NZ,$3847            ; {code.closeOneTurnOfTheFreeSlotSearch} busy: hand the turn to the search tail
37DD: DD 35 00        DEC     (IX+$00)            ; claim the free slot -- head to 0xFF
37E0: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the scroll angle
37E3: 0F              RRCA                        ; shift it down two
37E4: 0F              RRCA                        
37E5: E6 3F           AND     $3F                 ; keep a 0-63 heading base
37E7: 4F              LD      C,A                 ; hold the base
37E8: CD 4B 4B        CALL    $4B4B               ; {code.drawRandomByte} draw a random byte
37EB: E6 0F           AND     $0F                 ; keep a 0-15 jitter
37ED: D6 08           SUB     $08                 ; centre it about zero
37EF: 81              ADD     A,C                 ; jitter the heading base
37F0: E6 3F           AND     $3F                 ; wrap to 0-63
37F2: 21 FB 39        LD      HL,$39FB            ; point at the heading table
37F5: CF              RST     $08                 ; fetch the heading's velocity index
37F6: 87              ADD     A,A                 ; times four -- four-byte velocity entries
37F7: 87              ADD     A,A                 
37F8: 21 3B 3A        LD      HL,$3A3B            ; point at the velocity table
37FB: CF              RST     $08                 ; fetch the first velocity byte
37FC: FD 77 31        LD      (IY+$31),A          ; write it into the sprite entry
37FF: 23              INC     HL                  
3800: 7E              LD      A,(HL)              ; read the paired velocity byte
3801: FD 77 00        LD      (IY+$00),A          ; write it to the entry head
3804: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the scroll angle
3807: C6 80           ADD     A,$80               ; flip it half a turn -- the craft's heading
3809: DD 77 01        LD      (IX+$01),A          ; store the heading
380C: DD 77 02        LD      (IX+$02),A          ; and the facing
380F: CD 2D 38        CALL    $382D               ; {code.pickScriptAtRandomOrInTurn} pick a script at random or in turn
3812: DD 77 0A        LD      (IX+$0A),A          ; store the script index
3815: AF              XOR     A                   
3816: 32 C5 AC        LD      ($ACC5),A           ; {hard.workRam+4C5} clear the shared zero cell
3819: DD 36 03 00     LD      (IX+$03),$00        ; clear the sub-position
381D: DD 36 05 00     LD      (IX+$05),$00        ; clear the second sub-position
3821: DD 36 09 20     LD      (IX+$09),$20        ; prime the step counter
3825: CD 3A 32        CALL    $323A               ; {code.stepShapeAnimation} step the shape animation once
3828: DD 36 0E 00     LD      (IX+$0E),$00        ; clear the slot's tail byte
382C: C9              RET                         

; draw a byte and let one comparison against a threshold cell decide which
; of two entirely different answers the caller gets: a draw at or above
; the threshold is folded down to one of four values and handed straight
; back, writing nothing; a draw below it ignores the drawn byte completely
; and instead steps a five-long cycle counter on, wrapping it to zero once
; it would leave the cycle, stores it and hands THAT back. The two arms
; draw from DISJOINT halves rather than sampling one pool two ways: the
; random arm can only answer 5 through 8, the rotation only 0 through 4,
; so which arm ran is recoverable from the answer alone
pickScriptAtRandomOrInTurn:
382D: CD 4B 4B        CALL    $4B4B               ; {code.drawRandomByte} draw a random byte
3830: 21 C4 AC        LD      HL,$ACC4            ; point at the script-pick threshold
3833: BE              CP      (HL)                ; compare the draw against it
3834: 30 0C           JR      NC,$3842            ; {code.loc_3842} at or above: take the random arm
3836: 21 CF A9        LD      HL,$A9CF            ; below: point at the script cycle counter
3839: 7E              LD      A,(HL)              ; read it
383A: 3C              INC     A                   ; step it on
383B: FE 05           CP      $05                 ; past the five-long cycle?
383D: 38 01           JR      C,$3840             ; {code.loc_3840} still in range: keep it
383F: AF              XOR     A                   ; wrapped: back to zero

loc_3840:
3840: 77              LD      (HL),A              ; store the stepped counter
3841: C9              RET                         ; hand it back

loc_3842:
3842: E6 03           AND     $03                 ; fold the random draw to 0-3
3844: C6 05           ADD     A,$05               ; lift it into the 5-8 band
3846: C9              RET                         ; hand it back

; close one turn of the search for a free object slot and decide whether
; there is another: step the record cursor back one whole sixteen-byte
; record and the sprite-entry cursor back one two-byte entry, so the
; search walks its bank downward, strike one off the turn count, and while
; any remain transfer back to the body that tries one slot; when the last
; is struck off the search ends having filled nothing and this entry
; simply returns. The wide scratch pair the backward step is built from is
; left standing on the way out
closeOneTurnOfTheFreeSlotSearch:
3847: 11 F0 FF        LD      DE,$FFF0            ; a backward record stride (minus sixteen)
384A: DD 19           ADD     IX,DE               ; step the record cursor back one slot
384C: FD 2B           DEC     IY                  ; step the entry cursor back one two-byte entry
384E: FD 2B           DEC     IY                  
3850: 05              DEC     B                   ; strike one off the turn count
3851: C2 D6 37        JP      NZ,$37D6            ; {code.spawnEnemyIntoFreeSlotElseStepSearch} turns left: try the next slot
3854: C9              RET                         ; last turn: the search ends, nothing filled

; leave five consecutive object records standing on the shape a finished
; animation ends on, with their step bytes cleared so nothing walks them
; again — but only while the byte the caller points at still reads zero,
; so it is a guarded settling and not a step
stopFiveSlotAnimations:
3855: 7E              LD      A,(HL)              ; read the guard byte the caller points at
3856: A7              AND     A                   ; test it
3857: C0              RET     NZ                  ; non-zero: touch nothing
3858: DD 21 50 A8     LD      IX,$A850            ; point at the first craft record
385C: 11 10 00        LD      DE,$0010            ; the record stride
385F: 06 05           LD      B,$05               ; five records to settle

loc_3861:
3861: DD 36 08 11     LD      (IX+$08),$11        ; set the resting shape
3865: DD 36 09 00     LD      (IX+$09),$00        ; clear the step timer -- freeze the animation
3869: DD 19           ADD     IX,DE               ; step to the next record
386B: 10 F4           DJNZ    $3861               ; {code.loc_3861} settle all five
386D: C9              RET                         

; spawn a wave across a fixed bank of object slots: fill each free slot
; from a randomly-drawn shape record (shape index + two fields), prime its
; step counter, step its animation once, mark it live; store a fixed
; status byte when the pass ends
spawnEnemyWaveIntoFreeSlots:
386E: DD 21 50 A8     LD      IX,$A850            ; point at the first craft record
3872: FD 21 1A AA     LD      IY,$AA1A            ; point at its sprite entry
3876: 3A C1 AC        LD      A,($ACC1)           ; {hard.workRam+4C1} read the round's craft count
3879: 47              LD      B,A                 ; the wave size
387A: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} read the boss-craft flag
387D: A7              AND     A                   ; test it
387E: 28 02           JR      Z,$3882             ; {code.loc_3882} clear: keep the configured size
3880: 06 05           LD      B,$05               ; boss present: fill a fixed five

loc_3882:
3882: C5              PUSH    BC                  ; save the count and the ordinal
3883: DD 7E 00        LD      A,(IX+$00)          ; read this slot's head byte
3886: A7              AND     A                   ; test it
3887: C2 C0 38        JP      NZ,$38C0            ; {code.loc_38c0} busy: skip to the next slot
388A: CD 4B 4B        CALL    $4B4B               ; {code.drawRandomByte} draw a random byte
388D: E6 FC           AND     $FC                 ; mask it to a four-byte shape record
388F: 21 3B 3A        LD      HL,$3A3B            ; point at the shape-record table
3892: CF              RST     $08                 ; fetch the shape index
3893: FD 77 31        LD      (IY+$31),A          ; write it into the sprite entry
3896: 23              INC     HL                  
3897: 7E              LD      A,(HL)              ; read the entry attribute byte
3898: FD 77 00        LD      (IY+$00),A          ; write it to the entry head
389B: 23              INC     HL                  
389C: 7E              LD      A,(HL)              ; read the slot field byte
389D: DD 77 01        LD      (IX+$01),A          ; store it as the heading
38A0: DD 77 02        LD      (IX+$02),A          ; and as the facing
38A3: 3A C1 AC        LD      A,($ACC1)           ; {hard.workRam+4C1} read the round's craft count
38A6: 90              SUB     B                   ; subtract the remaining count -- the ordinal within the pass
38A7: 21 D2 38        LD      HL,$38D2            ; point at the ordinal table
38AA: CF              RST     $08                 ; fetch this slot's per-slot byte
38AB: DD 77 0A        LD      (IX+$0A),A          ; store the script index
38AE: DD 36 09 20     LD      (IX+$09),$20        ; prime the step counter
38B2: CD 3A 32        CALL    $323A               ; {code.stepShapeAnimation} step the shape animation once
38B5: DD 36 04 01     LD      (IX+$04),$01        ; set the slot's active flag
38B9: DD 36 0E 00     LD      (IX+$0E),$00        ; clear the slot's tail byte
38BD: DD 35 00        DEC     (IX+$00)            ; mark the slot live -- head to 0xFF

loc_38c0:
38C0: 11 10 00        LD      DE,$0010            ; the record stride
38C3: DD 19           ADD     IX,DE               ; step to the next record
38C5: FD 23           INC     IY                  ; step to the next sprite entry
38C7: FD 23           INC     IY                  
38C9: C1              POP     BC                  ; restore the count and ordinal
38CA: 10 B6           DJNZ    $3882               ; {code.loc_3882} walk the whole bank
38CC: 3E E4           LD      A,$E4               
38CE: 32 12 A8        LD      ($A812),A           ; {hard.workRam+12} stamp the wave-claim timer ready (0xE4)
38D1: C9              RET                         

; ---- $38D2-$3B5E: data ----
38D2: 0A 0B 0D 0E 0F 09 0C 08 0C 0F 13 16 1A 1D 21 24
38E2: 28 2B 2F 33 37 3A 3D F0 10 F0 20 F0 30 F0 40 F0
38F2: 50 F0 60 F0 70 F0 80 F0 90 F0 A0 F0 B0 F0 C0 F0
3902: D0 F0 E0 F0 F0 E0 F8 D0 F8 C0 F8 B0 F8 A0 F8 90
3912: F8 80 F8 70 F8 60 F8 50 F8 40 F8 30 F8 20 F8 10
3922: F8 00 F0 00 E0 00 D0 00 C0 00 B0 00 A0 00 90 00
3932: 80 00 70 00 60 00 50 00 40 00 30 00 20 00 10 10
3942: 10 20 10 30 10 40 10 50 10 60 10 70 10 80 10 90
3952: 10 A0 10 B0 10 C0 10 D0 10 E0 10 F0 10 F0 20 F0
3962: 30 F0 40 F0 50 F0 60 F0 70 F0 80 F0 90 F0 A0 F0
3972: B0 F0 C0 F0 D0 F0 E0 F0 F0 00 01 01 11 FF 11 02
3982: 21 FE 21 03 31 FD 31 00 00 00 11 01 01 FF 01 02
3992: 11 FE 11 03 21 FD 21 00 00 00 01 02 11 FE 11 03
39A2: 21 FD 21 04 31 FC 31 00 00 00 31 03 01 FD 01 04
39B2: 11 FC 11 03 11 FD 11 00 00 00 01 03 01 FD 01 04
39C2: 11 FC 11 05 21 FB 21 00 00 00 01 03 11 FD 11 00
39D2: 21 03 21 FD 21 00 31 00 00 03 01 FD 01 03 11 FD
39E2: 11 05 11 FB 11 00 29 00 00 00 01 03 11 FD 11 05
39F2: 21 FB 21 03 31 FD 31 00 00 08 09 0A 0B 0C 0D 0D
3A02: 0E 0F 10 11 12 13 14 14 15 16 17 18 19 1A 1B 1B
3A12: 1C 1D 1E 1F 20 21 22 22 23 24 25 26 27 28 29 29
3A22: 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35 36 37 38 38
3A32: 39 00 01 02 03 04 05 06 07 F0 10 60 00 F0 20 80
3A42: 00 F0 30 80 00 F0 40 80 00 F0 50 80 00 F0 60 80
3A52: 00 F0 70 80 00 F0 80 80 00 F0 90 80 00 F0 A0 80
3A62: 00 F0 B0 80 00 F0 C0 80 00 F0 D0 80 00 F0 E0 80
3A72: 00 F0 F0 A0 00 E0 F8 C0 00 D0 F8 C0 00 C0 F8 C0
3A82: 00 B0 F8 C0 00 A0 F8 C0 00 90 F8 C0 00 80 F8 C0
3A92: 00 70 F8 C0 00 60 F8 C0 00 50 F8 C0 00 40 F8 C0
3AA2: 00 30 F8 C0 00 20 F8 C0 00 10 F8 C0 00 00 F0 E0
3AB2: 00 00 E0 00 00 00 D0 00 00 00 C0 00 00 00 B0 00
3AC2: 00 00 A0 00 00 00 90 00 00 00 80 00 00 00 70 00
3AD2: 00 00 60 00 00 00 50 00 00 00 40 00 00 00 30 00
3AE2: 00 00 20 00 00 00 10 20 00 10 10 40 00 20 10 40
3AF2: 00 30 10 40 00 40 10 40 00 50 10 40 00 60 10 40
3B02: 00 70 10 40 00 80 10 40 00 90 10 40 00 A0 10 40
3B12: 00 B0 10 40 00 C0 10 40 00 D0 10 40 00 E0 10 40
3B22: 00 F0 10 60 00 F0 20 80 00 F0 30 80 00 F0 40 80
3B32: 00 F0 50 80 00 F0 60 80 00 F0 70 80 00 F0 80 80
3B42: 00 F0 90 80 00 F0 A0 80 00 F0 B0 80 00 F0 C0 80
3B52: 00 F0 D0 80 00 F0 E0 80 00 F0 F0 A0 00

; era-1 only: dispatch the single object at record 0xa8c0 by its head byte
; -- 0 arms its fire timer (armBomberSlotWhenTimerFires), 0xff runs the
; two-tile move (advanceTwoTileObjectThenTryAimedSpawn), any other value
; advances a hit-soaking object toward death
; (advanceHitSoakingObjectThenAnimateDeath); returns untouched outside era
; 1
serviceEra1BomberObject:
3B5F: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era number
3B62: 3D              DEC     A                   ; is it era 1?
3B63: C0              RET     NZ                  ; outside era 1: leave the object untouched
3B64: DD 21 C0 A8     LD      IX,$A8C0            ; point at the era-1 object record
3B68: FD 21 28 AA     LD      IY,$AA28            ; point at its sprite entry
3B6C: DD 7E 00        LD      A,(IX+$00)          ; read the record head byte
3B6F: A7              AND     A                   ; test it
3B70: CA 25 3C        JP      Z,$3C25             ; {code.armBomberSlotWhenTimerFires} empty: arm its fire timer
3B73: 3C              INC     A                   ; is the head 0xFF (fully live)?
3B74: C2 94 3B        JP      NZ,$3B94            ; {code.advanceHitSoakingObjectThenAnimateDeath} a partial count: soak hits toward death -- 0xFF runs the two-tile move

; advance a two-tile object one frame: fly it along its stored velocity,
; then seat its second tile directly under the first (same X, Y+0x10); if
; hasReachedBoundaryBandSelectedByHeading answers it has reached a
; boundary retire it, otherwise dress the pair by heading and run the
; aimed-spawn attempt
advanceTwoTileObjectThenTryAimedSpawn:
3B77: CD 05 3E        CALL    $3E05               ; {code.flyAlongStoredVelocity} fly the object along its stored velocity
3B7A: FD 7E 31        LD      A,(IY+$31)          ; read the top tile's Y
3B7D: C6 10           ADD     A,$10               ; drop sixteen -- one tile down
3B7F: FD 77 33        LD      (IY+$33),A          ; place the second tile's Y under it
3B82: FD 7E 00        LD      A,(IY+$00)          ; read the top tile's X
3B85: FD 77 02        LD      (IY+$02),A          ; give the second tile the same X
3B88: CD C4 3C        CALL    $3CC4               ; {code.hasReachedBoundaryBandSelectedByHeading} has it reached a heading-selected boundary?
3B8B: DA 0D 3C        JP      C,$3C0D             ; {code.retireObjectAndHold} reached: retire it and hold the slot
3B8E: CD E9 3C        CALL    $3CE9               ; {code.mirrorTwoTileObjectByHeading} dress the pair by heading
3B91: C3 25 3D        JP      $3D25               ; {code.spawnAimedEnemyIntoEraBankWhenInWindow} run the aimed-spawn attempt

; advance one hit-soaking object: while HITS_REMAINING (0xa8dc) is left,
; spend one, force the record head live (0xff) and re-request its sound
; pair before the ordinary two-tile move; once no hits remain, run the
; record head down (capped at 0x61) toward a retire-and-hold at 0, drift
; it with the world scroll, and at head 0x40 post a command / on 8-step
; boundaries above 0x40 reseat the sprite shape from the 0x3c09 table
advanceHitSoakingObjectThenAnimateDeath:
3B94: 3D              DEC     A                   ; recover the record head byte
3B95: 4F              LD      C,A                 
3B96: 21 DC A8        LD      HL,$A8DC            ; point at the hits-remaining count
3B99: 7E              LD      A,(HL)              ; read it
3B9A: A7              AND     A                   ; test it
3B9B: CA A9 3B        JP      Z,$3BA9             ; {code.loc_3ba9} no hits left: begin the death sequence
3B9E: 35              DEC     (HL)                ; spend one hit
3B9F: DD 36 00 FF     LD      (IX+$00),$FF        ; force the record head live
3BA3: CD 83 56        CALL    $5683               ; {code.requestTwoSounds} re-request the craft's two sounds
3BA6: C3 77 3B        JP      $3B77               ; {code.advanceTwoTileObjectThenTryAimedSpawn} run the ordinary two-tile move

loc_3ba9:
3BA9: 79              LD      A,C                 ; take the record head
3BAA: FE 61           CP      $61                 ; at or past the death cap?
3BAC: 38 0F           JR      C,$3BBD             ; {code.loc_3bbd} below: run it down
3BAE: DD 36 00 61     LD      (IX+$00),$61        ; cap the head at 0x61
3BB2: CD 83 56        CALL    $5683               ; {code.requestTwoSounds} request the craft's two sounds
3BB5: FD 36 30 3D     LD      (IY+$30),$3D        ; set the death attribute on tile one
3BB9: FD 36 32 3D     LD      (IY+$32),$3D        ; and on tile two

loc_3bbd:
3BBD: DD 35 00        DEC     (IX+$00)            ; count the death animation down one
3BC0: 28 4B           JR      Z,$3C0D             ; {code.retireObjectAndHold} reached zero: retire and hold the slot
3BC2: CD 60 2B        CALL    $2B60               ; {code.driftWithWorldScroll} drift the object with the world scroll
3BC5: FD 7E 31        LD      A,(IY+$31)          ; read tile one's Y
3BC8: C6 10           ADD     A,$10               ; drop sixteen
3BCA: FD 77 33        LD      (IY+$33),A          ; place tile two's Y under it
3BCD: FD 7E 00        LD      A,(IY+$00)          ; read tile one's X
3BD0: FD 77 02        LD      (IY+$02),A          ; give tile two the same X
3BD3: DD 7E 00        LD      A,(IX+$00)          ; read the record head
3BD6: D6 40           SUB     $40                 ; measure it past 0x40
3BD8: CA F1 3B        JP      Z,$3BF1             ; {code.loc_3bf1} exactly at 0x40: post the burst command
3BDB: D8              RET     C                   ; below 0x40: nothing more this frame
3BDC: 4F              LD      C,A                 
3BDD: E6 07           AND     $07                 ; on an eight-step boundary?
3BDF: C0              RET     NZ                  ; not a boundary: wait
3BE0: 79              LD      A,C                 ; take the distance past 0x40
3BE1: 0F              RRCA                        ; divide it by eight
3BE2: 0F              RRCA                        
3BE3: 0F              RRCA                        
3BE4: 3D              DEC     A                   ; step back one -- the death-shape index
3BE5: 21 09 3C        LD      HL,$3C09            ; point at the death-shape table
3BE8: CF              RST     $08                 ; fetch the shape byte
3BE9: FD 77 03        LD      (IY+$03),A          ; write it to tile two
3BEC: 3C              INC     A                   ; the next shape
3BED: FD 77 01        LD      (IY+$01),A          ; write it to tile one
3BF0: C9              RET                         

loc_3bf1:
3BF1: 11 0B 04        LD      DE,$040B            ; burst command 4, argument 0x0B
3BF4: FF              RST     $38                 ; queue the sound-ring burst command
3BF5: FD 36 03 FA     LD      (IY+$03),$FA        ; set the burst shape on tile two
3BF9: FD 36 01 FB     LD      (IY+$01),$FB        ; and on tile one
3BFD: FD 36 30 6C     LD      (IY+$30),$6C        ; set the burst attribute on tile one
3C01: FD 36 32 6C     LD      (IY+$32),$6C        ; and on tile two
3C05: DD 35 00        DEC     (IX+$00)            ; step the head past 0x40
3C08: C9              RET                         

; ---- $3C09-$3C0C: data ----
3C09: 96 94 92 90

; take an object and the slot one stride on out of play -- both record
; heads, both coordinates of the caller's sprite entry and of one fixed
; entry -- then set a further byte of the caller's record to a non-zero
; constant instead of clearing it
retireObjectAndHold:
3C0D: AF              XOR     A                   
3C0E: DD 77 00        LD      (IX+$00),A          ; clear this record's head
3C11: DD 77 10        LD      (IX+$10),A          ; clear the next record's head too
3C14: FD 77 00        LD      (IY+$00),A          ; clear the sprite entry's first coordinate
3C17: FD 77 31        LD      (IY+$31),A          ; clear its second coordinate
3C1A: 32 5B AA        LD      ($AA5B),A           ; {hard.workRam+25B} clear a fixed entry's second coordinate
3C1D: 32 2A AA        LD      ($AA2A),A           ; {hard.workRam+22A} clear that fixed entry's first coordinate
3C20: DD 36 0E 80     LD      (IX+$0E),$80        ; hold the slot -- set its hold byte non-zero
3C24: C9              RET                         

; on even frames tick a slot's arming countdown at ix+0x0e; when it fires
; and MOTHER_SHIP_ARMED (0xad0d) is clear, arm the slot -- pick a shape
; record from PLAYER_HEADING (0xa802) via the table at 0x3c84, snap the
; heading to a facing bit, look up the velocity pair, write
; shape/facing/velocity into the record, set HITS_REMAINING (0xa8dc)=3,
; and mark the slot live (ix+0=0xff); the era-1 large multi-hit craft
; (removed by a negative control). mechanisms.md identifies this counter-3
; era-1 craft as the 1940 bomber (absorbs three, dies on the fourth hit)
; -- NOT the counter-7 Mother-Ship; the MOTHER_SHIP_ARMED gate names the
; 0xAD0D boss class, and 3c25's sole caller serviceEra1BomberObject
; dispatches it only in era 1
armBomberSlotWhenTimerFires:
3C25: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame counter
3C28: E6 01           AND     $01                 ; odd frame?
3C2A: C0              RET     NZ                  ; odd frame: only tick on even ones
3C2B: DD 35 0E        DEC     (IX+$0E)            ; count the arming timer down
3C2E: CA 32 3C        JP      Z,$3C32             ; {code.loc_3c32} fired: arm the slot
3C31: C9              RET                         ; not yet

loc_3c32:
3C32: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} read the boss-craft flag
3C35: A7              AND     A                   ; test it
3C36: C0              RET     NZ                  ; boss already present: do not arm
3C37: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the player heading
3C3A: 47              LD      B,A                 
3C3B: C6 08           ADD     A,$08               ; bias by 8
3C3D: E6 7F           AND     $7F                 ; within the half-circle
3C3F: FE 10           CP      $10                 ; near a quadrant edge?
3C41: 38 32           JR      C,$3C75             ; {code.loc_3c75} near the edge: nudge the heading toward the axis
3C43: 78              LD      A,B                 ; take the heading

loc_3c44:
3C44: 0F              RRCA                        ; rotate the heading down two
3C45: 0F              RRCA                        
3C46: E6 3E           AND     $3E                 ; to an even shape-table offset
3C48: 21 84 3C        LD      HL,$3C84            ; point at the bomber shape/velocity table
3C4B: CF              RST     $08                 ; fetch the shape byte
3C4C: FD 77 31        LD      (IY+$31),A          ; write the shape into the sprite entry
3C4F: 23              INC     HL                  
3C50: 7E              LD      A,(HL)              ; read the paired attribute byte
3C51: FD 77 00        LD      (IY+$00),A          ; write it to the entry head
3C54: 78              LD      A,B                 ; take the heading again
3C55: C6 C0           ADD     A,$C0               ; rotate three quarters
3C57: E6 80           AND     $80                 ; keep the facing bit
3C59: DD 77 02        LD      (IX+$02),A          ; store the facing
3C5C: CD 42 59        CALL    $5942               ; {code.loc_5942} look up the velocity pair for this facing
3C5F: DD 73 0A        LD      (IX+$0A),E          ; store a velocity byte
3C62: DD 72 0B        LD      (IX+$0B),D          ; store a velocity byte
3C65: DD 71 0C        LD      (IX+$0C),C          ; store a velocity byte
3C68: DD 70 0D        LD      (IX+$0D),B          ; store a velocity byte
3C6B: 3E 03           LD      A,$03               
3C6D: 32 DC A8        LD      ($A8DC),A           ; {hard.workRam+DC} set the hits-remaining count to three
3C70: DD 36 00 FF     LD      (IX+$00),$FF        ; mark the slot live
3C74: C9              RET                         

loc_3c75:
3C75: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame counter
3C78: 4F              LD      C,A                 
3C79: 3E 10           LD      A,$10               ; a quarter-step nudge
3C7B: CB 59           BIT     3,C                 ; pick the nudge direction from the frame counter
3C7D: 20 02           JR      NZ,$3C81            ; {code.loc_3c81} one way: keep +0x10
3C7F: ED 44           NEG                         ; the other way: negate to -0x10

loc_3c81:
3C81: 80              ADD     A,B                 ; nudge the heading
3C82: 18 C0           JR      $3C44               ; {code.loc_3c44} back to the shape lookup

; ---- $3C84-$3CC3: data ----
3C84: EC 80 EC 88 EC 90 EC A0 EC B0 EC C0 EC D0 EC E0
3C94: F0 EC F0 EC F0 E0 F0 D0 F0 C0 F0 B0 F0 A0 F0 90
3CA4: F0 80 F0 78 F0 70 F0 60 F0 50 F0 40 F0 30 F0 28
3CB4: F0 20 EC 20 EC 30 EC 40 EC 50 EC 60 EC 70 EC 78

; answer, in the carry flag, whether an object has reached a boundary, the
; heading choosing which of two adjacent and disjoint three-wide bands is
; the one tested
hasReachedBoundaryBandSelectedByHeading:
3CC4: DD 7E 02        LD      A,(IX+$02)          ; read the object's heading
3CC7: C6 40           ADD     A,$40               ; rotate a quarter turn
3CC9: CB 7F           BIT     7,A                 ; which half of the compass?
3CCB: C2 D9 3C        JP      NZ,$3CD9            ; {code.hasDriftedOffTheField} one half: test the vertical drift band
3CCE: FD 7E 31        LD      A,(IY+$31)          ; read the entry's second coordinate
3CD1: C6 13           ADD     A,$13               ; bias toward the wrap
3CD3: FE 03           CP      $03                 ; inside the three-wide band?
3CD5: D8              RET     C                   ; inside: reached the boundary -- carry set
3CD6: C3 E1 3C        JP      $3CE1               ; {code.hasReachedHorizontalEdgeWindow} outside: test the horizontal edge window

; answer whether an object has drifted onto the boundary its caller frees
; the slot at: the vertical window this arm owns is tested here, and when
; it is not met the same question is handed on to the horizontal one, so
; the answer is an OR of two windows on two axes and only the first is
; decided here
hasDriftedOffTheField:
3CD9: FD 7E 31        LD      A,(IY+$31)          ; read the entry's second coordinate
3CDC: C6 10           ADD     A,$10               ; bias toward the wrap
3CDE: FE 03           CP      $03                 ; inside the three-wide band?
3CE0: D8              RET     C                   ; inside: reached -- carry set; else fall to the horizontal test

; answer whether the byte at the head of a sprite entry has reached its
; wrap point, testing a four-wide window that straddles zero -- so it
; measures a wrapped distance rather than bounding a range, which is what
; lets a byte stepping several units at a time land inside the window
; instead of over it
hasReachedHorizontalEdgeWindow:
3CE1: FD 7E 00        LD      A,(IY+$00)          ; read the entry's head coordinate
3CE4: C6 02           ADD     A,$02               ; bias across the wrap
3CE6: FE 04           CP      $04                 ; inside the four-wide window straddling zero?
3CE8: C9              RET                         ; carry answers whether it reached the edge

; dress two adjacent sprite entries with a consecutive pair of shape codes
; from the block HITS_REMAINING selects, so the object wears its damage,
; and mirror the pair -- swapping which entry takes the lower code, and
; flipping both -- on whichever half of the heading circle it is in
mirrorTwoTileObjectByHeading:
3CE9: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame counter
3CEC: E6 02           AND     $02                 ; take one alternating bit -- flicker between two shapes
3CEE: 47              LD      B,A                 
3CEF: 3A DC A8        LD      A,($A8DC)           ; {hard.workRam+DC} read the hits remaining
3CF2: 4F              LD      C,A                 
3CF3: 3E 03           LD      A,$03               ; the most hits it can take
3CF5: 91              SUB     C                   ; subtract the hits left -- the damage taken
3CF6: 87              ADD     A,A                 ; times four -- four shapes per damage step
3CF7: 87              ADD     A,A                 
3CF8: C6 A0           ADD     A,$A0               ; the first damage shape
3CFA: 80              ADD     A,B                 ; plus the flicker bit
3CFB: 4F              LD      C,A                 ; the pair's lower shape code
3CFC: DD 7E 02        LD      A,(IX+$02)          ; read the object's heading
3CFF: C6 40           ADD     A,$40               ; rotate a quarter turn
3D01: FE 80           CP      $80                 ; which half of the compass?
3D03: 38 10           JR      C,$3D15             ; {code.loc_3d15} one half: swap which entry takes the lower code
3D05: FD 71 01        LD      (IY+$01),C          ; one entry takes the lower shape
3D08: 0C              INC     C                   ; the next shape
3D09: FD 71 03        LD      (IY+$03),C          ; the other entry takes the upper shape
3D0C: FD 36 30 ED     LD      (IY+$30),$ED        ; set the forward attribute on tile one
3D10: FD 36 32 ED     LD      (IY+$32),$ED        ; and on tile two
3D14: C9              RET                         

loc_3d15:
3D15: FD 71 03        LD      (IY+$03),C          ; the other entry takes the lower shape
3D18: 0C              INC     C                   ; the next shape
3D19: FD 71 01        LD      (IY+$01),C          ; one entry takes the upper shape
3D1C: FD 36 30 6D     LD      (IY+$30),$6D        ; set the reversed attribute on tile one
3D20: FD 36 32 6D     LD      (IY+$32),$6D        ; and on tile two
3D24: C9              RET                         

; spawn one aimed enemy when the spawn slot is free, the cooldown at
; 0xa8f4 is clear, the era count at 0xa8c6 is live, and an object in the
; caller's two-slot bank sits inside a doubled window: seat the found
; slot's coords, the doubled velocity pair aimed toward the player at
; 0xac7f (aim side alternated each spawn via 0xa8d4), a script and a shape
; into the era's fixed record+sprite bank (0xa840/0xaa18 or
; 0xa8e0/0xaa2c), decrement the new record head, and reload the cooldown
; from 0xa8f6
spawnAimedEnemyIntoEraBankWhenInWindow:
3D25: DD 7E 00        LD      A,(IX+$00)          ; read the candidate spawn slot's head byte
3D28: 3C              INC     A                   
3D29: C0              RET     NZ                  ; return unless that slot is free ($FF)
3D2A: 3A F4 A8        LD      A,($A8F4)           ; {hard.workRam+F4} read the attacker-spawn cooldown timer
3D2D: A7              AND     A                   
3D2E: C0              RET     NZ                  ; return while the cooldown is still counting
3D2F: 3A C6 A8        LD      A,($A8C6)           ; {hard.workRam+C6} read how many attackers this era still owes
3D32: A7              AND     A                   
3D33: C8              RET     Z                   ; return if none are due
3D34: FE 01           CP      $01                 ; is exactly one attacker due?
3D36: CA 40 3D        JP      Z,$3D40             ; {code.loc_3d40} one due -- require the primary attacker record free
3D39: 3A E0 A8        LD      A,($A8E0)           ; {hard.workRam+E0} read the second era-object record's head
3D3C: A7              AND     A                   
3D3D: CA 45 3D        JP      Z,$3D45             ; {code.loc_3d45} free -- go find a windowed object to launch from

loc_3d40:
3D40: 3A 40 A8        LD      A,($A840)           ; {hard.workRam+40} read the primary attacker record's head
3D43: A7              AND     A                   
3D44: C0              RET     NZ                  ; return unless it too is free

loc_3d45:
3D45: 06 02           LD      B,$02               ; two bank slots to scan
3D47: 3A D6 A8        LD      A,($A8D6)           ; {hard.workRam+D6} read the spawn-window half-width
3D4A: 57              LD      D,A                 
3D4B: 87              ADD     A,A                 ; double it -- the full window width
3D4C: 5F              LD      E,A                 

loc_3d4d:
3D4D: 3E 84           LD      A,$84               ; screen X reference ($84)
3D4F: FD 96 00        SUB     (IY+$00)            ; minus this object's X
3D52: 82              ADD     A,D                 ; re-centre by the half-width
3D53: BB              CP      E                   ; within the doubled X window?
3D54: D2 6F 3D        JP      NC,$3D6F            ; {code.loc_3d6f} object reaches the launch window on X -- go launch from it
3D57: 3E 78           LD      A,$78               ; screen Y reference ($78)
3D59: FD 96 31        SUB     (IY+$31)            ; minus this object's Y
3D5C: 82              ADD     A,D                 ; re-centre by the half-width
3D5D: BB              CP      E                   ; within the doubled Y window?
3D5E: D2 6F 3D        JP      NC,$3D6F            ; {code.loc_3d6f} object reaches the launch window on Y -- go launch from it
3D61: D9              EXX                         
3D62: 11 10 00        LD      DE,$0010            ; record stride ($10)
3D65: DD 19           ADD     IX,DE               ; step to the next bank record
3D67: FD 23           INC     IY                  ; step to the next sprite entry (two bytes)
3D69: FD 23           INC     IY                  
3D6B: D9              EXX                         
3D6C: 10 DF           DJNZ    $3D4D               ; {code.loc_3d4d} try the other slot
3D6E: C9              RET                         ; none in the window -- nothing to spawn

loc_3d6f:
3D6F: CD 5F 56        CALL    $565F               ; {code.requestEnemyLaunchSound} request the enemy-launch sound
3D72: 21 7F AC        LD      HL,$AC7F            ; point at the player's aim reference cell
3D75: CD B8 33        CALL    $33B8               ; {code.headingToward} find the heading that points at the player
3D78: 67              LD      H,A                 
3D79: 3E 18           LD      A,$18               ; prepare the turn offset ($18)
3D7B: EB              EX      DE,HL               
3D7C: 21 D4 A8        LD      HL,$A8D4            ; point at the aim-side toggle
3D7F: 34              INC     (HL)                ; flip the aim side for this spawn
3D80: 46              LD      B,(HL)              ; read the toggle
3D81: CB 40           BIT     0,B                 ; test its low bit
3D83: 20 02           JR      NZ,$3D87            ; {code.loc_3d87} odd -- turn one way
3D85: ED 44           NEG                         ; even -- turn the other way (negate)

loc_3d87:
3D87: EB              EX      DE,HL               
3D88: 84              ADD     A,H                 ; add the turn onto the heading -- the aimed angle
3D89: 08              EX      AF,AF'              ; stash the aimed angle
3D8A: FD 46 31        LD      B,(IY+$31)          ; take the object's Y
3D8D: FD 4E 00        LD      C,(IY+$00)          ; take the object's X
3D90: 3A C6 A8        LD      A,($A8C6)           ; {hard.workRam+C6} read the attackers-due count again
3D93: FE 01           CP      $01                 ; exactly one due?
3D95: CA 9F 3D        JP      Z,$3D9F             ; {code.loc_3d9f} then seat into the primary era bank
3D98: 3A E0 A8        LD      A,($A8E0)           ; {hard.workRam+E0} read the second era-object record's head
3D9B: A7              AND     A                   
3D9C: CA CF 3D        JP      Z,$3DCF             ; {code.loc_3dcf} free -- seat into the second era bank

loc_3d9f:
3D9F: DD 21 40 A8     LD      IX,$A840            ; point at the primary attacker record
3DA3: FD 21 18 AA     LD      IY,$AA18            ; and its sprite entry

loc_3da7:
3DA7: FD 70 31        LD      (IY+$31),B          ; seat the object's Y into the new entry
3DAA: FD 71 00        LD      (IY+$00),C          ; seat the object's X
3DAD: 08              EX      AF,AF'              ; recover the aimed angle
3DAE: CD C5 59        CALL    $59C5               ; {code.loc_59c5} look up the doubled velocity pair for that angle
3DB1: DD 73 0A        LD      (IX+$0A),E          ; stock the record with the aimed velocity pair -- four bytes
3DB4: DD 72 0B        LD      (IX+$0B),D          
3DB7: DD 71 0C        LD      (IX+$0C),C          
3DBA: DD 70 0D        LD      (IX+$0D),B          
3DBD: FD 36 01 4D     LD      (IY+$01),$4D        ; set the launch script/animation code
3DC1: FD 36 30 62     LD      (IY+$30),$62        ; set the launch sprite shape
3DC5: DD 35 00        DEC     (IX+$00)            ; count the record head down one -- mark it live
3DC8: 3A F6 A8        LD      A,($A8F6)           ; {hard.workRam+F6} read the cooldown reload period
3DCB: 32 F4 A8        LD      ($A8F4),A           ; {hard.workRam+F4} reload the attacker-spawn cooldown
3DCE: C9              RET                         

loc_3dcf:
3DCF: DD 21 E0 A8     LD      IX,$A8E0            ; point at the second era-object record
3DD3: FD 21 2C AA     LD      IY,$AA2C            ; and its sprite entry
3DD7: C3 A7 3D        JP      $3DA7               ; {code.loc_3da7} seat and stock it the same way

; guard on the era index and, when it passes, hand two fixed bases to the
; shared slot servicer; the guard is the whole of the decision, and the
; bases are constants rather than anything a caller chose
serviceFixedSlotInEra1:
3DDA: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
3DDD: 3D              DEC     A                   
3DDE: C0              RET     NZ                  ; service only in era 1
3DDF: DD 21 E0 A8     LD      IX,$A8E0            ; point at the fixed era-object record
3DE3: FD 21 2C AA     LD      IY,$AA2C            ; and its sprite entry
3DE7: CD EB 3D        CALL    $3DEB               ; {code.serviceSlotByHeadByte} service that slot by its head byte
3DEA: C9              RET                         

; service one slot, splitting three ways on the head byte of its record:
; zero does nothing at all, all-ones flies the object one step along the
; velocity it carries and retires it into the shared cooldown only once
; that step has put it on a retire line, and any OTHER value retires it on
; the spot without moving it first
serviceSlotByHeadByte:
3DEB: DD 7E 00        LD      A,(IX+$00)          ; read the slot's head byte
3DEE: A7              AND     A                   
3DEF: C8              RET     Z                   ; empty slot -- nothing to do
3DF0: 3C              INC     A                   
3DF1: C2 FB 3D        JP      NZ,$3DFB            ; {code.retireSlotIntoSharedCooldown} any value but $FF -- retire the slot on the spot
3DF4: CD 05 3E        CALL    $3E05               ; {code.flyAlongStoredVelocity} $FF -- fly the object one step along its velocity
3DF7: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} has it reached a retire line?
3DFA: D0              RET     NC                  ; not yet -- leave it flying

; retire a slot the way retireSlot does and then arm its delay byte from
; one shared address instead of leaving it clear, so every slot retired
; here goes out holding the same value
retireSlotIntoSharedCooldown:
3DFB: CD AB 40        CALL    $40AB               ; {code.retireSlot} take the slot out of play
3DFE: 3A F6 A8        LD      A,($A8F6)           ; {hard.workRam+F6} read the shared cooldown period
3E01: DD 77 0E        LD      (IX+$0E),A          ; stock the retired record's delay byte with it
3E04: C9              RET                         

; fly one object a single step along the velocity held in its own record,
; and in the same add carry it with the world; each coordinate gains its
; stored word plus the shared per-frame scroll
flyAlongStoredVelocity:
3E05: DD 66 0B        LD      H,(IX+$0B)          ; take the object's stored Y velocity, high byte
3E08: DD 6E 0A        LD      L,(IX+$0A)          ; and its low byte
3E0B: ED 5B 08 A8     LD      DE,($A808)          ; {hard.workRam+8} read the shared per-frame world scroll (Y)
3E0F: 19              ADD     HL,DE               ; add the scroll onto the velocity
3E10: FD 56 31        LD      D,(IY+$31)          ; take the object's whole Y
3E13: DD 5E 03        LD      E,(IX+$03)          ; and its Y fraction
3E16: 19              ADD     HL,DE               ; advance the split Y coordinate
3E17: FD 74 31        LD      (IY+$31),H          ; store the new whole Y
3E1A: DD 75 03        LD      (IX+$03),L          ; store the new Y fraction
3E1D: DD 66 0D        LD      H,(IX+$0D)          ; take the object's stored X velocity, high byte
3E20: DD 6E 0C        LD      L,(IX+$0C)          ; and its low byte
3E23: ED 5B 0A A8     LD      DE,($A80A)          ; {hard.workRam+A} read the shared per-frame world scroll (X)
3E27: 19              ADD     HL,DE               ; add the scroll onto the velocity
3E28: FD 56 00        LD      D,(IY+$00)          ; take the object's whole X
3E2B: DD 5E 05        LD      E,(IX+$05)          ; and its X fraction
3E2E: 19              ADD     HL,DE               ; advance the split X coordinate
3E2F: FD 74 00        LD      (IY+$00),H          ; store the new whole X
3E32: DD 75 05        LD      (IX+$05),L          ; store the new X fraction
3E35: C9              RET                         

; put four named actor slots through the shared per-slot step, in a fixed
; order, one after another, without asking first whether any of them holds
; anything — so the four are serviced as a group and the group's
; membership is fixed here rather than by the caller
stepFourActorSlots:
3E36: DD 21 10 A8     LD      IX,$A810            ; point at actor record slot 0
3E3A: FD 21 12 AA     LD      IY,$AA12            ; and its sprite entry
3E3E: CD 63 3E        CALL    $3E63               ; {code.dispatchObjectSlotByHeadByte} step that slot by its head byte
3E41: DD 21 20 A8     LD      IX,$A820            ; actor record slot 1
3E45: FD 21 14 AA     LD      IY,$AA14            ; and its sprite entry
3E49: CD 63 3E        CALL    $3E63               ; {code.dispatchObjectSlotByHeadByte} step it
3E4C: DD 21 30 A8     LD      IX,$A830            ; actor record slot 2
3E50: FD 21 16 AA     LD      IY,$AA16            ; and its sprite entry
3E54: CD 63 3E        CALL    $3E63               ; {code.dispatchObjectSlotByHeadByte} step it
3E57: DD 21 40 A8     LD      IX,$A840            ; actor record slot 3
3E5B: FD 21 18 AA     LD      IY,$AA18            ; and its sprite entry
3E5F: CD 63 3E        CALL    $3E63               ; {code.dispatchObjectSlotByHeadByte} step it
3E62: C9              RET                         

; split three ways on the head byte of the record an index register points
; at: zero returns with nothing done, all-ones hands over to one
; continuation and every other value to another. One byte read, nothing
; written, and neither continuation is given anything this entry computed
dispatchObjectSlotByHeadByte:
3E63: DD 7E 00        LD      A,(IX+$00)          ; read the slot's head byte
3E66: A7              AND     A                   
3E67: C8              RET     Z                   ; empty slot -- nothing to do
3E68: 3C              INC     A                   
3E69: C2 8E 3E        JP      NZ,$3E8E            ; {code.runSlotCountdownDriftAndAnimateElseRetire} any value but $FF -- run its countdown/animate branch

; fly one object a step along the velocity it carries and retire its slot
; once that step has put it on a retire line; in one era of the game, and
; only that one, the object is also given the next frame of a fixed shape
; cycle before it moves, and the retire is last so a shape written this
; tick may go out in the same breath
flyAndRetireSlotCyclingShapeInEra4:
3E6C: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
3E6F: FE 04           CP      $04                 ; is it the last era (4)?
3E71: CC 7E 3E        CALL    Z,$3E7E             ; {code.animateFixedShapeCycle} in that era, cycle the object's shape first
3E74: CD 05 3E        CALL    $3E05               ; {code.flyAlongStoredVelocity} fly the object one step along its velocity
3E77: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} has it reached a retire line?
3E7A: D0              RET     NC                  ; not yet -- leave it flying
3E7B: C3 AB 40        JP      $40AB               ; {code.retireSlot} reached the line -- retire the slot

; give a sprite entry the next frame of an eight-frame cycle from a fixed
; shape base, and one fixed control byte beside it; nothing of the object
; is read, so two entries written in one tick get the same shape
animateFixedShapeCycle:
3E7E: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the free-running frame tick
3E81: 0F              RRCA                        ; halve it -- advance every other tick
3E82: E6 07           AND     $07                 ; take it modulo eight -- one of eight frames
3E84: C6 40           ADD     A,$40               ; offset to the shape-code base ($40)
3E86: FD 77 01        LD      (IY+$01),A          ; write the shape into the sprite entry
3E89: FD 36 30 44     LD      (IY+$30),$44        ; set the fixed control byte beside it
3E8D: C9              RET                         

; run one slot's counter down for a frame and take the slot out of play as
; soon as it has nothing left to run; the era cell not standing at the
; last era, or the counter already sitting one above the floor, ends it
; outright, and otherwise the counter drops by one and the slot drifts
; with the world
runSlotCountdownDriftAndAnimateElseRetire:
3E8E: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
3E91: FE 04           CP      $04                 ; the last era (4)?
3E93: 28 03           JR      Z,$3E98             ; {code.loc_3e98} yes -- run the countdown
3E95: C3 AB 40        JP      $40AB               ; {code.retireSlot} any other era -- retire the slot at once

loc_3e98:
3E98: DD 7E 00        LD      A,(IX+$00)          ; read the slot's countdown
3E9B: FE 01           CP      $01                 ; down to one above the floor?
3E9D: CA AB 40        JP      Z,$40AB             ; {code.retireSlot} then retire the slot
3EA0: DD 35 00        DEC     (IX+$00)            ; otherwise drop the countdown by one
3EA3: FE 3C           CP      $3C                 ; was the count at or above $3C?
3EA5: D4 CB 3E        CALL    NC,$3ECB            ; {code.stampObjectStateByte3bThenRequestTwoSounds} if so, clamp the slot's state and ask for two sounds
3EA8: CD 60 2B        CALL    $2B60               ; {code.driftWithWorldScroll} drift the object with the world scroll
3EAB: DD 7E 00        LD      A,(IX+$00)          ; re-read the countdown -- the clamp may have moved it
3EAE: FE 1C           CP      $1C                 ; below the animate threshold ($1C)?
3EB0: D8              RET     C                   ; yes -- leave the shape as it is
3EB1: D6 1C           SUB     $1C                 ; offset above the threshold
3EB3: 0F              RRCA                        ; shift down by two -- four counts per shape
3EB4: 0F              RRCA                        
3EB5: E6 07           AND     $07                 ; one of eight shapes
3EB7: 21 C3 3E        LD      HL,$3EC3            ; point at the shape table
3EBA: CF              RST     $08                 ; fetch the shape byte for this count
3EBB: FD 77 01        LD      (IY+$01),A          ; write it into the sprite entry
3EBE: FD 36 30 03     LD      (IY+$30),$03        ; set the control byte beside it
3EC2: C9              RET                         

; ---- $3EC3-$3ECA: data ----
3EC3: FF E6 E7 E7 E6 E6 E5 E4

; force the head byte of the record the index register points at to one
; fixed value and hand over; what that byte held is discarded unread, so
; this is a clamp and not a step
stampObjectStateByte3bThenRequestTwoSounds:
3ECB: DD 36 00 3B     LD      (IX+$00),$3B        ; force the slot's head byte to $3B
3ECF: C3 83 56        JP      $5683               ; {code.requestTwoSounds} request the two sounds

; ---- $3ED2-$3ED5: data ----
3ED2: 92 A6 14 B9

; one gated attempt to launch an enemy into the object bank: past a phase-
; key match, an arm flag, a non-empty flight count, and a strided scan for
; a free record, three margin windows must place the aim point near the
; player entry and the scroll; only then does it request the launch sound,
; copy the entry's two coordinates into the found record's paired entry,
; look up a doubled velocity pair from the heading via one of two tables
; chosen by a select cell, stock the record with that velocity, stamp two
; entry constants, re-arm the flag from its source, and count the record
; head down one
launchBankEnemyWhenAimedNearPlayer:
3ED6: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the free-running frame tick
3ED9: E6 07           AND     $07                 ; take its low three bits
3EDB: C6 05           ADD     A,$05               ; form this frame's bank-phase key
3EDD: DD BE 0F        CP      (IX+$0F)            ; does it match this bank's phase key?
3EE0: C0              RET     NZ                  ; wrong phase this frame -- nothing to do
3EE1: 3A 17 A8        LD      A,($A817)           ; {hard.workRam+17} read the launch arm/cooldown flag
3EE4: A7              AND     A                   
3EE5: C0              RET     NZ                  ; return while a launch is still armed
3EE6: 21 10 A8        LD      HL,$A810            ; point at the first actor record
3EE9: 11 12 AA        LD      DE,$AA12            ; and its sprite entry
3EEC: 3A 44 A8        LD      A,($A844)           ; {hard.workRam+44} read the count of craft in flight
3EEF: A7              AND     A                   
3EF0: C8              RET     Z                   ; return if none are flying
3EF1: 47              LD      B,A                 ; that count bounds the free-slot scan

loc_3ef2:
3EF2: 7E              LD      A,(HL)              ; read this record's head
3EF3: A7              AND     A                   
3EF4: 28 09           JR      Z,$3EFF             ; {code.loc_3eff} free record found -- launch into it
3EF6: 7D              LD      A,L                 
3EF7: C6 10           ADD     A,$10               ; advance to the next record (stride $10)
3EF9: 6F              LD      L,A                 
3EFA: 1C              INC     E                   ; advance the sprite entry (two bytes)
3EFB: 1C              INC     E                   
3EFC: 10 F4           DJNZ    $3EF2               ; {code.loc_3ef2} keep scanning the bank
3EFE: C9              RET                         ; bank full -- nothing to launch

loc_3eff:
3EFF: 22 91 A9        LD      ($A991),HL          ; {hard.workRam+191} remember the free record pointer
3F02: ED 53 93 A9     LD      ($A993),DE          ; {hard.workRam+193} and its sprite entry pointer
3F06: 3A 27 A8        LD      A,($A827)           ; {hard.workRam+27} read the near half-width for Y
3F09: 47              LD      B,A                 
3F0A: 87              ADD     A,A                 ; double it -- the full near band
3F0B: 4F              LD      C,A                 
3F0C: 3E 78           LD      A,$78               ; screen Y reference ($78)
3F0E: FD 96 31        SUB     (IY+$31)            ; minus the player entry's Y
3F11: 80              ADD     A,B                 ; re-centre by the half-width
3F12: B9              CP      C                   ; player entry within the near Y band?
3F13: 30 08           JR      NC,$3F1D            ; {code.loc_3f1d} outside it -- this launch clears, go on
3F15: 3E 84           LD      A,$84               ; within Y -- also test X: screen X reference ($84)
3F17: FD 96 00        SUB     (IY+$00)            ; minus the player entry's X
3F1A: 80              ADD     A,B                 ; re-centre by the half-width
3F1B: B9              CP      C                   ; within the near X band too?
3F1C: D8              RET     C                   ; too close on both axes -- reject this launch

loc_3f1d:
3F1D: 3A 37 A8        LD      A,($A837)           ; {hard.workRam+37} read the near half-width for the scroll axis
3F20: 47              LD      B,A                 
3F21: 87              ADD     A,A                 ; double it -- the full band
3F22: 4F              LD      C,A                 
3F23: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} read the scroll reference
3F26: DD 96 02        SUB     (IX+$02)            ; minus the object's X
3F29: 80              ADD     A,B                 ; re-centre by the half-width
3F2A: B9              CP      C                   ; within the scroll band?
3F2B: D0              RET     NC                  ; outside it -- reject this launch
3F2C: 7A              LD      A,D                 ; read the found entry's page byte
3F2D: FE 02           CP      $02                 ; is the entry page $02?
3F2F: CA 9E 3F        JP      Z,$3F9E             ; {code.loc_3f9e} if so, take the extra window check

loc_3f32:
3F32: 21 7F AC        LD      HL,$AC7F            ; point at the player's aim reference
3F35: CD B8 33        CALL    $33B8               ; {code.headingToward} compute the heading toward the player
3F38: 4F              LD      C,A                 ; keep the heading
3F39: DD 96 02        SUB     (IX+$02)            ; measure it against the object's own heading
3F3C: C6 10           ADD     A,$10               ; centre the difference
3F3E: FE 20           CP      $20                 ; within a sector either way?
3F40: D0              RET     NC                  ; not aligned -- give up this frame
3F41: CD 93 3F        CALL    $3F93               ; {code.requestEraKeyedLaunchSound} request the era-keyed launch sound
3F44: DD E5           PUSH    IX                  
3F46: FD E5           PUSH    IY                  
3F48: FD 56 31        LD      D,(IY+$31)          ; take the player entry's Y
3F4B: FD 5E 00        LD      E,(IY+$00)          ; and its X
3F4E: DD 2A 91 A9     LD      IX,($A991)          ; {hard.workRam+191} point at the free record found earlier
3F52: FD 2A 93 A9     LD      IY,($A993)          ; {hard.workRam+193} and its sprite entry
3F56: FD 72 31        LD      (IY+$31),D          ; seat the player entry's Y into the new entry
3F59: FD 73 00        LD      (IY+$00),E          ; seat its X
3F5C: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
3F5F: A7              AND     A                   
3F60: 79              LD      A,C                 ; load the heading for the velocity lookup
3F61: 20 05           JR      NZ,$3F68            ; {code.loc_3f68} past era 0 -- use the later-era velocity table
3F63: CD CB 59        CALL    $59CB               ; {code.loc_59cb} era 0 -- look up the velocity pair for the heading
3F66: 18 03           JR      $3F6B               ; {code.loc_3f6b}

loc_3f68:
3F68: CD D1 59        CALL    $59D1               ; {code.loc_59d1} later eras -- look up the velocity pair for the heading

loc_3f6b:
3F6B: DD 73 0A        LD      (IX+$0A),E          ; stock the record with the velocity pair -- four bytes
3F6E: DD 72 0B        LD      (IX+$0B),D          
3F71: DD 71 0C        LD      (IX+$0C),C          
3F74: DD 70 0D        LD      (IX+$0D),B          
3F77: FD 7E 31        LD      A,(IY+$31)          
3F7A: FD 7E 00        LD      A,(IY+$00)          
3F7D: FD 36 01 4D     LD      (IY+$01),$4D        ; set the launch script/animation code
3F81: FD 36 30 62     LD      (IY+$30),$62        ; set the launch sprite shape
3F85: 3A 14 A8        LD      A,($A814)           ; {hard.workRam+14} read the arm-flag reload source
3F88: 32 17 A8        LD      ($A817),A           ; {hard.workRam+17} re-arm the launch flag
3F8B: DD 35 00        DEC     (IX+$00)            ; count the new record head down one -- mark it live
3F8E: FD E1           POP     IY                  
3F90: DD E1           POP     IX                  
3F92: C9              RET                         

; request the sound of a craft launching, taking the code from one of two
; program bytes according to whether the era has reached the fourth; both
; go through the play-gated door, so the attract demo stays silent
requestEraKeyedLaunchSound:
3F93: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
3F96: FE 03           CP      $03                 ; before the third era?
3F98: DA 5F 56        JP      C,$565F             ; {code.requestEnemyLaunchSound} yes -- request the early-era launch sound
3F9B: C3 69 56        JP      $5669               ; {code.requestEnemyLaunchSoundLateEra} third era on -- request the late-era launch sound

loc_3f9e:
3F9E: 3A E6 A8        LD      A,($A8E6)           ; {hard.workRam+E6} read a near half-width
3FA1: 47              LD      B,A                 
3FA2: 87              ADD     A,A                 ; double it -- the full band
3FA3: 4F              LD      C,A                 
3FA4: 3E 84           LD      A,$84               ; screen X reference ($84)
3FA6: FD 96 00        SUB     (IY+$00)            ; minus the player entry's X
3FA9: 80              ADD     A,B                 ; re-centre by the half-width
3FAA: B9              CP      C                   ; within the band?
3FAB: D0              RET     NC                  ; outside it -- reject this launch
3FAC: C3 32 3F        JP      $3F32               ; {code.loc_3f32} within it -- carry on to the aim check

; point an object's sprite the way it is heading, from a different pair of
; sector tables to the sibling that does the same rounding
dressSpriteShapeAndAttributeForHeadingSector:
3FAF: DD 7E 02        LD      A,(IX+$02)          ; read the object's heading byte
3FB2: C6 08           ADD     A,$08               ; add half a sector -- round to the nearest
3FB4: 0F              RRCA                        
3FB5: 0F              RRCA                        
3FB6: 0F              RRCA                        
3FB7: 0F              RRCA                        ; shift the top nibble down -- one of sixteen heading sectors
3FB8: E6 0F           AND     $0F                 ; keep the sector index
3FBA: 21 CA 3F        LD      HL,$3FCA            ; point at the shape table
3FBD: CF              RST     $08                 ; fetch the shape for this sector
3FBE: FD 77 01        LD      (IY+$01),A          ; write the shape into the sprite entry
3FC1: 11 10 00        LD      DE,$0010            ; step sixteen entries on --
3FC4: 19              ADD     HL,DE               ; to the parallel attribute table
3FC5: 7E              LD      A,(HL)              ; fetch the attribute byte for this sector
3FC6: FD 77 30        LD      (IY+$30),A          ; write it beside the shape
3FC9: C9              RET                         

; ---- $3FCA-$3FE9: data ----
3FCA: 48 49 4A 4B 4C 4B 4A 49 48 49 4A 4B 4C 4B 4A 49
3FDA: F4 B4 B4 B4 B4 34 34 34 34 74 74 74 74 F4 F4 F4

; era-zero-gated top-of-frame entry to the three-slot ballistic-object
; bank (dispatched as serviceRoundThenResolvePlayerState's substep 7):
; returns at once unless ERA_INDEX 0xad04 is 0, else seats the cursors
; (record ix=0xa8c0, sprite iy=0xaa28, count b=3) and routes the first
; slot by its marker byte -- step an empty slot via
; advanceSlotThenSweepObjectBankByHead, fly a ballistic (0xFF) slot then
; step it, else hand any other marker to
; sweepObjectSlotBankServicingFirstSlot
serviceEra0BallisticObjectBank:
3FEA: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
3FED: A7              AND     A                   
3FEE: C0              RET     NZ                  ; run only in era 0
3FEF: DD 21 C0 A8     LD      IX,$A8C0            ; point at the ballistic bank's first record
3FF3: FD 21 28 AA     LD      IY,$AA28            ; and its first sprite entry
3FF7: 06 03           LD      B,$03               ; three slots in the bank

; sweep a fixed bank of object slots for a frame, servicing each by its
; head byte -- fly a ballistic slot (0xFF) a frame along its arc, run the
; shape-cycle countdown service on any other nonzero, skip an empty (0) --
; striding one 0x10 record and two sprite-entry bytes per slot for the
; caller's count
sweepObjectSlotBankByHead:
3FF9: DD 7E 00        LD      A,(IX+$00)          ; read this slot's head byte
3FFC: A7              AND     A                   
3FFD: CA 0B 40        JP      Z,$400B             ; {code.advanceSlotThenSweepObjectBankByHead} empty slot -- step over it
4000: 3C              INC     A                   
4001: 20 05           JR      NZ,$4008            ; {code.sweepObjectSlotBankServicingFirstSlot} any value but $FF -- run its animate service
4003: CD 17 40        CALL    $4017               ; {code.flyAlongBallisticArc} $FF -- fly the ballistic object a frame along its arc
4006: 18 03           JR      $400B               ; {code.advanceSlotThenSweepObjectBankByHead} then step to the next slot

; sweep the fixed three-slot object bank for one frame from the seated
; cursors (record cursor +0x10, sprite cursor +2 per slot, count bounding
; the pass): service the first slot's shape-cycle unconditionally, then
; route each following slot by its marker byte -- skip an empty (0x00)
; slot, fly a ballistic (0xFF) slot a step, and service any other marker's
; shape-cycle
sweepObjectSlotBankServicingFirstSlot:
4008: CD 6C 40        CALL    $406C               ; {code.runOneShotAnimatedObjectSlot} service the first slot's shape-cycle

; advance-step entry of the object-bank sweep: stride one slot forward
; (record +0x10, sprite entry +2) and return when the count runs out; step
; over an empty slot, fly a ballistic (0xFF) slot a frame and step over
; it, and hand the first slot bearing any other marker to the servicing
; sweep for the rest of the bank
advanceSlotThenSweepObjectBankByHead:
400B: 11 10 00        LD      DE,$0010            ; the record stride -- sixteen bytes per slot
400E: DD 19           ADD     IX,DE               ; step the record cursor to the next slot
4010: FD 23           INC     IY                  ; step the sprite-entry cursor two bytes to match
4012: FD 23           INC     IY                  
4014: 10 E3           DJNZ    $3FF9               ; {code.sweepObjectSlotBankByHead} strike one off the slot count and, while slots remain, loop back to the sweep head
4016: C9              RET                         

; fly one object a frame along a ballistic arc -- a constant sideways step
; whose sign the record's own flag fixes, and a stored velocity on the
; other axis that gains a fixed amount every frame -- carrying it with the
; world scroll in both axes, and retiring the slot outright once it leaves
; the field on either
flyAlongBallisticArc:
4017: FD 56 31        LD      D,(IY+$31)          ; take the whole part of the object's position from the sprite entry
401A: DD 5E 03        LD      E,(IX+$03)          ; and its fraction from the record -- one 16-bit coordinate
401D: DD 7E 01        LD      A,(IX+$01)          ; read the record's across-direction flag
4020: A7              AND     A                   
4021: 28 05           JR      Z,$4028             ; {code.loc_4028} flag zero: step this axis the positive way
4023: 21 80 FE        LD      HL,$FE80            ; non-zero: a fixed negative step across
4026: 18 03           JR      $402B               ; {code.loc_402b}

loc_4028:
4028: 21 80 01        LD      HL,$0180            ; a fixed positive step across

loc_402b:
402B: 19              ADD     HL,DE               ; add the step onto the object's position
402C: ED 5B 08 A8     LD      DE,($A808)          ; {hard.workRam+8} the frame's world scroll on this axis
4030: 19              ADD     HL,DE               ; carry the object along with the world too
4031: FD 74 31        LD      (IY+$31),H          ; store the new position back -- whole to the entry, fraction to the record
4034: DD 75 03        LD      (IX+$03),L          
4037: DD 6E 07        LD      L,(IX+$07)          ; take the object's accumulated speed's low byte from the record
403A: DD 66 08        LD      H,(IX+$08)          ; and its high byte -- a 16-bit speed
403D: 11 09 00        LD      DE,$0009            ; the per-frame speed gain
4040: 19              ADD     HL,DE               ; the object accelerates: add nine to its stored speed
4041: DD 75 07        LD      (IX+$07),L          ; keep the grown speed in the record for next frame
4044: DD 74 08        LD      (IX+$08),H          
4047: FD 56 00        LD      D,(IY+$00)          ; the whole part of the object's other-axis position
404A: DD 5E 05        LD      E,(IX+$05)          ; and its fraction
404D: 19              ADD     HL,DE               ; move that axis by the just-grown speed
404E: ED 5B 0A A8     LD      DE,($A80A)          ; {hard.workRam+A} the world scroll on that axis
4052: 19              ADD     HL,DE               ; carry it along with the world as well
4053: FD 74 00        LD      (IY+$00),H          ; store the new position back to entry and record
4056: DD 75 05        LD      (IX+$05),L          
4059: FD 7E 31        LD      A,(IY+$31)          ; read the first axis's whole part
405C: C6 10           ADD     A,$10               ; shift the wrap point into view
405E: FE 20           CP      $20                 ; inside a 32-wide band at the edge?
4060: DA AB 40        JP      C,$40AB             ; {code.retireSlot} yes -- it has left the field: retire the slot
4063: FD 7E 00        LD      A,(IY+$00)          ; read the other axis's whole part
4066: FE F8           CP      $F8                 ; past the far limit (248)?
4068: D2 AB 40        JP      NC,$40AB            ; {code.retireSlot} yes: retire the slot
406B: C9              RET                         

; service one animated slot for a frame: rearm it (stamp the countdown to
; 59 and request the paired sound) when the countdown at (ix+0) is >=0x3c,
; count the countdown down, retire the sprite (zero iy+0 and iy+0x31) when
; it reaches zero, otherwise drift the object with the world scroll and,
; once the countdown is >=0x1c, drive the sprite shape (iy+1) from the
; 9-byte table at 0x4094 indexed by (countdown-0x1c)>>2 and set its
; attribute (iy+0x30) to 0x0e
runOneShotAnimatedObjectSlot:
406C: DD 7E 00        LD      A,(IX+$00)          ; read the slot's countdown
406F: FE 3C           CP      $3C                 ; at or above the reset mark (60)?
4071: D4 9D 40        CALL    NC,$409D            ; {code.stampObjectStateByte3bThenRequestSound} yes -- re-stamp its state and ask for the paired sound
4074: DD 35 00        DEC     (IX+$00)            ; count the slot down one frame
4077: 28 32           JR      Z,$40AB             ; {code.retireSlot} reached zero: retire the slot
4079: CD 60 2B        CALL    $2B60               ; {code.driftWithWorldScroll} drift the object with the world scroll
407C: DD 7E 00        LD      A,(IX+$00)          ; read the countdown again
407F: FE 1C           CP      $1C                 ; below the animation window floor (28)?
4081: D8              RET     C                   ; yes: nothing more to draw this frame
4082: D6 1C           SUB     $1C                 ; measure how far into the window it is
4084: 0F              RRCA                        ; divide that distance by four
4085: 0F              RRCA                        
4086: E6 0F           AND     $0F                 ; keep the low nibble as a shape-table index
4088: 21 94 40        LD      HL,$4094            ; point at the shape-cycle table
408B: CF              RST     $08                 ; fetch the shape byte for this frame
408C: FD 77 01        LD      (IY+$01),A          ; write it as the sprite's shape code
408F: FD 36 30 0E     LD      (IY+$30),$0E        ; set the sprite's attribute
4093: C9              RET                         

; ---- $4094-$409C: data ----
4094: FF 9A 99 98 98 99 99 9A 9B

; stamp one object's state byte to fifty-nine and ask for the sound that
; goes with it; the stamp is unconditional -- nothing here reads the byte
; first, and the ROM's test at this entry sends both of its answers to the
; same address
stampObjectStateByte3bThenRequestSound:
409D: DD 36 00 3B     LD      (IX+$00),$3B        ; stamp the object's state byte to fifty-nine
40A1: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
40A4: A7              AND     A                   
40A5: CA 8E 56        JP      Z,$568E             ; {code.loc_568e} ask for the accompanying sound
40A8: C3 8E 56        JP      $568E               ; {code.loc_568e} the other arm asks for it too -- the test above changes nothing

; retire an object, zeroing only the INTEGER halves — occupancy byte and
; both sprite-entry coordinates — leaving the sub-pixel remainders
; standing
retireSlot:
40AB: DD 36 00 00     LD      (IX+$00),$00        ; clear the slot's occupancy byte
40AF: FD 36 00 00     LD      (IY+$00),$00        ; zero one whole coordinate in the sprite entry
40B3: FD 36 31 00     LD      (IY+$31),$00        ; and the other -- the object leaves the screen
40B7: C9              RET                         

; ask for one sound on every thirty-second frame from the third era on,
; and only while none of the three records at 0xA8C0, 0xA8D0 and 0xA8E0 is
; live; any one of those four tests failing ends the entry having done
; nothing at all
askForSoundWhileTheGroupIsClear:
40B8: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
40BB: FE 02           CP      $02                 ; below the third era (index 2)?
40BD: D8              RET     C                   ; yes: ask for nothing
40BE: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the free-running frame counter
40C1: E6 1F           AND     $1F                 ; keep its low five bits
40C3: C0              RET     NZ                  ; not the one frame in thirty-two: do nothing
40C4: 3A C0 A8        LD      A,($A8C0)           ; {hard.workRam+C0} first of the three era-object records
40C7: 3C              INC     A                   
40C8: C8              RET     Z                   ; holds a live object (0xFF): ask for nothing
40C9: 3A D0 A8        LD      A,($A8D0)           ; {hard.workRam+D0} second era-object record
40CC: 3C              INC     A                   
40CD: C8              RET     Z                   ; holds a live object: ask for nothing
40CE: 3A E0 A8        LD      A,($A8E0)           ; {hard.workRam+E0} third era-object record
40D1: 3C              INC     A                   
40D2: C8              RET     Z                   ; holds a live object: ask for nothing
40D3: C3 79 56        JP      $5679               ; {code.requestLateEraProgressSound} all clear from the third era on: ask for the progress sound

; entry to the per-slot sweep over an object bank: return early below era
; 2 (ERA_INDEX 0xad04) or when the bank's slot count (0xa8c6) is zero,
; else seat the record cursor (0xa8c0), the sprite-entry cursor (0xaa28)
; and the turn count, and run the sweep body at 0x40ea
sweepEra2PlusObjectBank:
40D6: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
40D9: FE 02           CP      $02                 ; below the third era (index 2)?
40DB: D8              RET     C                   ; yes: this bank is idle before then
40DC: DD 21 C0 A8     LD      IX,$A8C0            ; seat the record cursor at the first bank slot
40E0: FD 21 28 AA     LD      IY,$AA28            ; seat the sprite-entry cursor to match
40E4: 3A C6 A8        LD      A,($A8C6)           ; {hard.workRam+C6} read the bank's slot count
40E7: A7              AND     A                   
40E8: C8              RET     Z                   ; no slots: nothing to do
40E9: 47              LD      B,A                 ; use the count as the sweep's turn count

loc_40ea:
40EA: DD 7E 00        LD      A,(IX+$00)          ; read this slot's marker byte
40ED: A7              AND     A                   
40EE: CA 0B 41        JP      Z,$410B             ; {code.closeOneTurnOfTheSlotSweep} empty: skip to the next slot
40F1: 3C              INC     A                   ; test for the ballistic marker (0xFF)
40F2: 20 14           JR      NZ,$4108            ; {code.loc_4108} any other marker: handle the drifting-countdown object
40F4: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} ballistic slot -- read the era index
40F7: FE 04           CP      $04                 ; the final era (index 4)?
40F9: CA 94 41        JP      Z,$4194             ; {code.stepSlotApproachThenBreakawayRetire} yes: run the approach-then-breakaway handler
40FC: DD 7E 0E        LD      A,(IX+$0E)          ; read the slot's own countdown at +0x0e
40FF: A7              AND     A                   
4100: C2 8B 41        JP      NZ,$418B            ; {code.flyLiveSlotAndTickCountdown} still running: fly the live slot and tick that countdown
4103: CD 17 41        CALL    $4117               ; {code.chaseOneAimPointAndRetireAtTheLine} else chase the aim point and retire at the line
4106: 18 03           JR      $410B               ; {code.closeOneTurnOfTheSlotSweep} then close this turn of the sweep

loc_4108:
4108: CD 3C 41        CALL    $413C               ; {code.stepDriftingCountdownObjectByEraFrames} otherwise step the drifting countdown object for its era

; close one turn of the per-slot sweep over an object bank: step the
; record cursor on one whole sixteen-byte record and the sprite-entry
; cursor on one two-byte entry, strike one off the turn count and go round
; again while any remain, ending the sweep when the count runs out;
; several arms of the sweep's body converge here rather than one, and the
; record stride is left standing in the wide scratch pair on the way out
closeOneTurnOfTheSlotSweep:
410B: 11 10 00        LD      DE,$0010            ; the record stride -- sixteen bytes
410E: DD 19           ADD     IX,DE               ; step the record cursor to the next slot
4110: FD 23           INC     IY                  ; step the sprite-entry cursor two bytes to match
4112: FD 23           INC     IY                  
4114: 10 D4           DJNZ    $40EA               ; {code.loc_40ea} strike one off the turn count and loop to the sweep head while slots remain
4116: C9              RET                         

; run one object through a whole frame of chasing: re-aim it, turn it,
; move it, dress its sprite, and retire it once it has drifted onto a
; retire line. Re-aiming is RATIONED rather than done every frame -- the
; object carries a phase byte and the aim is recomputed only on the frames
; whose low four bits match it, which spreads a crowd across sixteen
; frames and leaves each object a stale aim in between; a phase byte above
; 15 can never match FRAME_TICK's low four bits at all, so such an object
; is never re-aimed. The point is neither the only one nor a constant: it
; is one of SIX two-byte points packed at 0xAC74-0xAC7F, and those twelve
; bytes are rewritten as a block. The turn, the move and the dressing run
; every frame regardless, and the counter pair the caller holds is put
; back before the retire test
chaseOneAimPointAndRetireAtTheLine:
4117: C5              PUSH    BC                  ; save the sweep's turn count across the object work
4118: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the free-running frame counter
411B: E6 0F           AND     $0F                 ; its low four bits
411D: DD BE 0F        CP      (IX+$0F)            ; do they match this object's phase byte?
4120: 20 09           JR      NZ,$412B            ; {code.loc_412b} no: keep last frame's aim, just turn and move
4122: 21 7F AC        LD      HL,$AC7F            ; point at the shared aim point
4125: CD B8 33        CALL    $33B8               ; {code.headingToward} compute the heading toward it
4128: DD 77 01        LD      (IX+$01),A          ; store it as the heading to turn toward

loc_412b:
412B: CD 01 42        CALL    $4201               ; {code.steerTowardAimOneUnitAFrame} turn one step toward the aim
412E: CD AA 58        CALL    $58AA               ; {code.loc_58aa} move the object a frame
4131: CD AF 3F        CALL    $3FAF               ; {code.dressSpriteShapeAndAttributeForHeadingSector} dress the sprite's shape and attribute for its heading
4134: C1              POP     BC                  ; restore the sweep's turn count
4135: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} has it drifted onto a retire line?
4138: D0              RET     NC                  ; no: keep it in play
4139: C3 AB 40        JP      $40AB               ; {code.retireSlot} yes: retire the slot

; advance one countdown-driven object per frame: re-stamp+sound at the
; reset cap, drift with world scroll, decrement, retire the slot at zero,
; else animate the sprite from an era-selected frame table above the
; window floor
stepDriftingCountdownObjectByEraFrames:
413C: DD 7E 00        LD      A,(IX+$00)          ; read the object's countdown
413F: FE 3C           CP      $3C                 ; at or above the reset mark (60)?
4141: D4 9D 40        CALL    NC,$409D            ; {code.stampObjectStateByte3bThenRequestSound} yes: re-stamp its state and ask for the paired sound
4144: CD 60 2B        CALL    $2B60               ; {code.driftWithWorldScroll} drift the object with the world scroll
4147: DD 35 00        DEC     (IX+$00)            ; count it down one frame
414A: CA AB 40        JP      Z,$40AB             ; {code.retireSlot} reached zero: retire the slot
414D: DD 7E 00        LD      A,(IX+$00)          ; read the countdown again
4150: FE 1C           CP      $1C                 ; below the animation window floor (28)?
4152: D8              RET     C                   ; yes: draw nothing more this frame
4153: D6 1C           SUB     $1C                 ; measure how far into the window it is
4155: 0F              RRCA                        ; divide that distance by four
4156: 0F              RRCA                        
4157: E6 07           AND     $07                 ; keep three bits -- a frame index 0..7
4159: 57              LD      D,A                 ; hold the frame index
415A: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
415D: FE 04           CP      $04                 ; the final era (index 4)?
415F: 30 15           JR      NC,$4176            ; {code.loc_4176} yes: use the far-era frame table
4161: 21 6E 41        LD      HL,$416E            ; the near-era frame table
4164: 7A              LD      A,D                 ; the frame index
4165: CF              RST     $08                 ; fetch the frame's shape byte
4166: FD 77 01        LD      (IY+$01),A          ; write it as the sprite's shape code
4169: FD 36 30 0D     LD      (IY+$30),$0D        ; set the sprite's attribute (near)
416D: C9              RET                         

; ---- $416E-$4175: data ----
416E: FF 9E 9F 9F 9E 9E 9D 9C

loc_4176:
4176: 21 83 41        LD      HL,$4183            ; the far-era frame table
4179: 7A              LD      A,D                 ; the frame index
417A: CF              RST     $08                 ; fetch the frame's shape byte
417B: FD 77 01        LD      (IY+$01),A          ; write it as the sprite's shape code
417E: FD 36 30 02     LD      (IY+$30),$02        ; set the sprite's attribute (far)
4182: C9              RET                         

; ---- $4183-$418A: data ----
4183: FF E2 E3 E3 E2 E2 E1 E0

; service one live slot of the per-slot object sweep: fly the slot's
; object a step along its stored velocity (retiring it once it crosses a
; retire line), tick down the slot's own countdown at record offset 0x0e,
; then close the turn of the sweep; reached only for a slot whose marker
; byte reads 0xFF with a nonzero countdown, outside the fourth era
flyLiveSlotAndTickCountdown:
418B: CD 6C 3E        CALL    $3E6C               ; {code.flyAndRetireSlotCyclingShapeInEra4} fly the object a step and retire it if it crossed the retire line
418E: DD 35 0E        DEC     (IX+$0E)            ; tick this slot's countdown at +0x0e down one
4191: C3 0B 41        JP      $410B               ; {code.closeOneTurnOfTheSlotSweep} close this turn of the sweep

; one slot's per-frame handler in an object sweep: while the record's
; approach countdown at +4 runs, decrement it and drive the object through
; its chased-object frame; the tick it hits zero, fly the object at double
; velocity, animate its shape cycle, and retire the slot only if it has
; reached a retire line, then step the sweep onto the next slot
stepSlotApproachThenBreakawayRetire:
4194: DD 7E 04        LD      A,(IX+$04)          ; read the slot's approach countdown at +0x04
4197: A7              AND     A                   
4198: CA A4 41        JP      Z,$41A4             ; {code.loc_41a4} it has expired: break away
419B: DD 35 04        DEC     (IX+$04)            ; still approaching: count it down one
419E: CD B8 41        CALL    $41B8               ; {code.flyTowardShipStandoffThenEndApproach} fly it toward the standoff point
41A1: C3 0B 41        JP      $410B               ; {code.closeOneTurnOfTheSlotSweep} close this turn of the sweep

loc_41a4:
41A4: C5              PUSH    BC                  ; save the sweep's turn count
41A5: CD B6 58        CALL    $58B6               ; {code.loc_58b6} move the object
41A8: CD F1 41        CALL    $41F1               ; {code.animateFixedShapeCycleAtHalfRate} animate its shape from the frame counter
41AB: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} has it reached a retire line?
41AE: C1              POP     BC                  ; restore the turn count
41AF: D2 0B 41        JP      NC,$410B            ; {code.closeOneTurnOfTheSlotSweep} no: leave it and close the turn
41B2: CD AB 40        CALL    $40AB               ; {code.retireSlot} yes: retire the slot
41B5: C3 0B 41        JP      $410B               ; {code.closeOneTurnOfTheSlotSweep} close the turn

; run one chased object through a frame: every sixteenth frame re-aim it
; at one of two fixed points a record bit selects, cut its approach
; countdown to zero once both axis gaps to that point fall under sixteen,
; then turn, move and dress it every frame; the carry answers whether it
; reached a retire line
flyTowardShipStandoffThenEndApproach:
41B8: C5              PUSH    BC                  ; save the sweep's turn count
41B9: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the free-running frame counter
41BC: E6 0F           AND     $0F                 ; its low four bits
41BE: 20 1F           JR      NZ,$41DF            ; {code.loc_41df} not the sixteenth frame: skip re-aiming
41C0: 21 75 AC        LD      HL,$AC75            ; the default aim point
41C3: DD CB 0F 46     BIT     0,(IX+$0F)          ; test bit 0 of the slot's identity byte
41C7: 20 03           JR      NZ,$41CC            ; {code.loc_41cc} set: keep that point
41C9: 21 79 AC        LD      HL,$AC79            ; clear: the other aim point

loc_41cc:
41CC: CD B8 33        CALL    $33B8               ; {code.headingToward} compute the heading toward the chosen point
41CF: 47              LD      B,A                 ; hold the heading
41D0: 7A              LD      A,D                 ; the first axis's distance to the aim point
41D1: FE 10           CP      $10                 ; within sixteen of it?
41D3: 30 07           JR      NC,$41DC            ; {code.loc_41dc} no: still approaching, just store the heading
41D5: 08              EX      AF,AF'              ; recover the second axis's distance
41D6: FE 10           CP      $10                 ; within sixteen on that axis too?
41D8: DC EC 41        CALL    C,$41EC             ; {code.endApproachNow} both close: it has arrived -- cut the approach countdown to zero
41DB: 08              EX      AF,AF'              

loc_41dc:
41DC: DD 70 01        LD      (IX+$01),B          ; store the new heading to turn toward

loc_41df:
41DF: CD 1F 42        CALL    $421F               ; {code.steerTowardAimAtFixedRate} turn toward the aim at the fixed rate
41E2: CD B6 58        CALL    $58B6               ; {code.loc_58b6} move the object
41E5: CD F1 41        CALL    $41F1               ; {code.animateFixedShapeCycleAtHalfRate} animate its shape
41E8: C1              POP     BC                  
41E9: C3 83 2B        JP      $2B83               ; {code.hasReachedRetireLine} answer whether it reached a retire line

; make the countdown at +0x04 of the record a caller points at read zero,
; so that record's handler takes its expired arm on the next frame instead
; of counting the rest of the delay down; one store and nothing else
endApproachNow:
41EC: DD 36 04 00     LD      (IX+$04),$00        ; zero the approach countdown at +0x04, so the slot retires next frame
41F0: C9              RET                         

; give one sprite entry the current frame of an eight-frame shape cycle
; from a fixed base, and one fixed byte beside it; the frame is picked
; from bits one to three of the free-running counter, so the cycle turns
; over once every sixteen counts. Nothing about the object is read, so two
; entries written in one tick get the same shape
animateFixedShapeCycleAtHalfRate:
41F1: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the free-running frame counter
41F4: 0F              RRCA                        ; halve it
41F5: E6 07           AND     $07                 ; keep three bits -- a frame 0..7
41F7: C6 50           ADD     A,$50               ; offset into the eight-shape run at 0x50
41F9: FD 77 01        LD      (IY+$01),A          ; write it as the sprite's shape code
41FC: FD 36 30 0A     LD      (IY+$30),$0A        ; set the sprite's attribute
4200: C9              RET                         

; turn an object's heading one unit toward the heading it aims at, on
; every dispatch, standing still once the heading sits on the aim or one
; unit past it; the direction test is taken on the gap PLUS ONE, so a gap
; of exactly 127 turns the LONG way round and the standing band is off
; centre
steerTowardAimOneUnitAFrame:
4201: DD 7E 01        LD      A,(IX+$01)          ; read the heading the object aims toward
4204: DD 96 02        SUB     (IX+$02)            ; subtract its current heading -- the gap around the circle
4207: C6 01           ADD     A,$01               ; bias the gap by one
4209: FE 02           CP      $02                 ; within one step of the aim either side?
420B: D8              RET     C                   ; yes: hold the heading still
420C: FE 80           CP      $80                 ; is the shorter way round to increase or decrease?
420E: DD 7E 02        LD      A,(IX+$02)          ; the current heading
4211: 30 06           JR      NC,$4219            ; {code.loc_4219} turn the decreasing way
4213: C6 01           ADD     A,$01               ; turn one step up toward the aim
4215: DD 77 02        LD      (IX+$02),A          ; store the new heading
4218: C9              RET                         

loc_4219:
4219: D6 01           SUB     $01                 ; turn one step down toward the aim
421B: DD 77 02        LD      (IX+$02),A          ; store the new heading
421E: C9              RET                         

; turn an object's heading two units toward the heading it aims at, on the
; three frames in four when the frame counter's low two bits are not both
; clear; a fixed step, where its sibling steerTowardAimHeading takes its
; rate from a table
steerTowardAimAtFixedRate:
421F: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the free-running frame counter
4222: E6 03           AND     $03                 ; its low two bits
4224: C8              RET     Z                   ; one frame in four: do not turn
4225: DD 7E 01        LD      A,(IX+$01)          ; the heading the object aims toward
4228: DD 96 02        SUB     (IX+$02)            ; minus its current heading -- the gap
422B: C6 01           ADD     A,$01               ; bias the gap by one
422D: FE 02           CP      $02                 ; within one step of the aim?
422F: D8              RET     C                   ; yes: hold still
4230: FE 80           CP      $80                 ; shorter way up or down?
4232: DD 7E 02        LD      A,(IX+$02)          ; the current heading
4235: 30 06           JR      NC,$423D            ; {code.loc_423d} turn the decreasing way
4237: C6 02           ADD     A,$02               ; turn two steps up toward the aim
4239: DD 77 02        LD      (IX+$02),A          ; store the new heading
423C: C9              RET                         

loc_423d:
423D: D6 02           SUB     $02                 ; turn two steps down toward the aim
423F: DD 77 02        LD      (IX+$02),A          ; store the new heading
4242: C9              RET                         

; on this object's turn of the eight-frame round, once the shared spawn
; cooldown (0xA8F4) has expired, walk the object-record bank for a free
; slot, stash its record/entry pointers at 0xA991/0xA993, and if the new
; object clears the two fixed lines hand the caller's facing (C=IX+0x02)
; to the era-0 aim launcher (0x429C) or the heading-follows launcher
; (0x42B7); otherwise tick the cooldown down or leave everything untouched
launchAttackerIntoFreeSlot:
4243: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame counter
4246: E6 07           AND     $07                 ; keep its low three bits -- which of the eight frames of the round this is
4248: C6 05           ADD     A,$05               ; bias it by five to form this object's spawn turn
424A: DD BE 0F        CP      (IX+$0F)            ; is it this object's turn to try a spawn?
424D: C0              RET     NZ                  ; not its turn: leave
424E: 21 F4 A8        LD      HL,$A8F4            ; point at the shared spawn cooldown
4251: 7E              LD      A,(HL)              ; read the cooldown
4252: A7              AND     A                   ; is it still running?
4253: 28 02           JR      Z,$4257             ; {code.loc_4257} cooldown spent: go hunt a free slot
4255: 35              DEC     (HL)                ; still cooling down: tick it down one
4256: C9              RET                         

loc_4257:
4257: 21 C0 A8        LD      HL,$A8C0            ; point at the first record in the spawn bank
425A: 11 28 AA        LD      DE,$AA28            ; point at its paired sprite entry
425D: 3A C6 A8        LD      A,($A8C6)           ; {hard.workRam+C6} how many slots the bank holds
4260: A7              AND     A                   ; any at all?
4261: C8              RET     Z                   ; none: leave
4262: 47              LD      B,A                 ; set the loop count to the slot total

loc_4263:
4263: 7E              LD      A,(HL)              ; read this record's occupancy byte
4264: A7              AND     A                   ; is the slot free?
4265: CA 71 42        JP      Z,$4271             ; {code.loc_4271} free: take it
4268: 7D              LD      A,L                 
4269: C6 10           ADD     A,$10               ; step on to the next record -- records lie 0x10 apart
426B: 6F              LD      L,A                 
426C: 13              INC     DE                  ; step the paired sprite-entry pointer along too
426D: 13              INC     DE                  
426E: 10 F3           DJNZ    $4263               ; {code.loc_4263} try the next slot
4270: C9              RET                         

loc_4271:
4271: 22 91 A9        LD      ($A991),HL          ; {hard.workRam+191} stash the free record pointer
4274: ED 53 93 A9     LD      ($A993),DE          ; {hard.workRam+193} stash its paired entry pointer
4278: 3A D6 A8        LD      A,($A8D6)           ; {hard.workRam+D6} read the spawn-window half-width
427B: 57              LD      D,A                 
427C: 87              ADD     A,A                 ; double it to the full window width
427D: 4F              LD      C,A                 
427E: 3E 78           LD      A,$78               ; how far the spawner sits from the fixed line 0x78, offset into the window
4280: FD 96 31        SUB     (IY+$31)            
4283: 82              ADD     A,D                 
4284: B9              CP      C                   ; inside the window on this axis?
4285: 30 08           JR      NC,$428F            ; {code.loc_428f} far enough on the first axis: go ahead and launch
4287: 3E 84           LD      A,$84               ; else measure its distance from the fixed line 0x84 on the other axis
4289: FD 96 00        SUB     (IY+$00)            
428C: 82              ADD     A,D                 
428D: B9              CP      C                   ; inside that window too?
428E: D8              RET     C                   ; too close on both axes: abandon the launch

loc_428f:
428F: DD 4E 02        LD      C,(IX+$02)          ; hand the spawner's facing to the launcher
4292: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
4295: A7              AND     A                   ; era zero?
4296: CA 9C 42        JP      Z,$429C             ; {code.setTheLaunchFacingInsideOneAimWindow} era 0: launch on the aligned-facing path
4299: C3 B7 42        JP      $42B7               ; {code.commissionStagedAttackerByEra} else launch with the heading-follows path

; the last gate in front of a launch, and the one thing the launcher is
; told: on one of the two coordinates the sprite entry carries, the firing
; object must lie inside a window centred on a fixed line whose half-width
; is READ FROM 0xA8E6 rather than baked in, and outside it this entry ends
; and nothing is launched; inside it the OTHER coordinate is compared
; against a second fixed line, and which side it falls on is handed to the
; launcher at 0x42B7 in the narrow scratch byte as a plain zero or one,
; which that routine turns into a mirroring of the NEW object's sprite
; rather than of the firing one's. 0xA8E6 is one of the two aim windows
; applyEraRungSettings scatters, which is why the name says 'one' and not
; 'the'; the cell also has a NON-WINDOW reader at 0x43AE (`ld a,(0xa8e6) /
; ld (ix+0x04),a`, seeding a record countdown), and mechanisms.md marks
; what each of those twelve scattered cells governs as not fully settled
setTheLaunchFacingInsideOneAimWindow:
429C: 3A E6 A8        LD      A,($A8E6)           ; {hard.workRam+E6} read the aim-window half-width
429F: 57              LD      D,A                 
42A0: 87              ADD     A,A                 ; double it to the full window width
42A1: 4F              LD      C,A                 
42A2: 3E 84           LD      A,$84               ; how far the spawner sits from the fixed line 0x84, offset into the window
42A4: FD 96 00        SUB     (IY+$00)            
42A7: 82              ADD     A,D                 
42A8: B9              CP      C                   ; inside the window on this axis?
42A9: D0              RET     NC                  ; outside: abandon the launch
42AA: 3E 78           LD      A,$78               ; measure its distance from the fixed line 0x78 on the other axis
42AC: FD 96 31        SUB     (IY+$31)            
42AF: 38 04           JR      C,$42B5             ; {code.loc_42b5} past the line one way: mark the mirror flag
42B1: 0E 00           LD      C,$00               ; the other way: mirror flag clear
42B3: 18 02           JR      $42B7               ; {code.commissionStagedAttackerByEra} go commission the launch

loc_42b5:
42B5: 0E 01           LD      C,$01               ; mirror flag set -- the new sprite is drawn mirrored

; commission the object the free-slot finder staged, whose record/entry
; pointers wait at 0xA991/0xA993: copy the spawner's two coordinate pairs
; and the caller's facing (C) into the new slot, then fit it out one of
; four ways chosen by the era cell 0xAD04 -- era 0 an unaimed drift with a
; mirror flag (IY+0x01=0x4F) and slow-fall marker; eras 1-2 a heading
; toward the fixed point 0xAC7F skewed by a stored half-turn from
; (IX+0x0F); era 3 a doubled velocity vector for a heading offset +/-0x1A
; from the facing; era 4 a straight aim at 0xAC7F plus a seeded (IX+0x04);
; each way winds the new slot's active count (IX+0x00) down, re-arms the
; spawn cooldown (0xA8F4 from 0xA8F6), restores the spawner's own IX/IY,
; and hands off to one era-specific sound request
commissionStagedAttackerByEra:
42B7: FD 56 31        LD      D,(IY+$31)          ; grab the spawner's first coordinate
42BA: DD 5E 03        LD      E,(IX+$03)          ; and that axis's low byte
42BD: FD 66 00        LD      H,(IY+$00)          ; grab its second coordinate
42C0: DD 6E 05        LD      L,(IX+$05)          ; and that axis's low byte
42C3: D9              EXX                         ; tuck the copied coordinates into the alternate registers
42C4: DD E5           PUSH    IX                  ; save the spawner's record pointer
42C6: FD E5           PUSH    IY                  ; save the spawner's entry pointer
42C8: DD 2A 91 A9     LD      IX,($A991)          ; {hard.workRam+191} point at the staged free record
42CC: FD 2A 93 A9     LD      IY,($A993)          ; {hard.workRam+193} point at its paired entry
42D0: D9              EXX                         ; bring the copied coordinates back
42D1: DD 73 03        LD      (IX+$03),E          ; seat the first coordinate's low byte in the new record
42D4: FD 72 31        LD      (IY+$31),D          ; and its high byte in the new entry
42D7: DD 75 05        LD      (IX+$05),L          ; seat the second coordinate's low byte
42DA: FD 74 00        LD      (IY+$00),H          ; and its high byte
42DD: DD 71 01        LD      (IX+$01),C          ; store the facing in the new record
42E0: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
42E3: FE 04           CP      $04                 ; the final era?
42E5: CA AE 43        JP      Z,$43AE             ; {code.loc_43ae} era 4: seed the extra byte first, then aim
42E8: A7              AND     A                   ; era zero?
42E9: C2 13 43        JP      NZ,$4313            ; {code.loc_4313} other eras: the aimed / heading paths
42EC: FD 36 01 4F     LD      (IY+$01),$4F        ; era 0: give the new sprite its fixed shape code
42F0: 79              LD      A,C                 ; take the facing
42F1: 0F              RRCA                        ; spread its low bit up into the top bits
42F2: CB 2F           SRA     A                   
42F4: E6 C0           AND     $C0                 ; keep the two top bits
42F6: C6 0B           ADD     A,$0B               ; form the sprite's attribute code
42F8: FD 77 30        LD      (IY+$30),A          ; store it
42FB: DD 36 07 00     LD      (IX+$07),$00        ; clear the sub-pixel remainder
42FF: DD 36 08 FF     LD      (IX+$08),$FF        ; seed the slow-fall marker
4303: DD 35 00        DEC     (IX+$00)            ; wind the new slot's active count down -- brings it live
4306: 3A F6 A8        LD      A,($A8F6)           ; {hard.workRam+F6} read the spawn-cooldown reload
4309: 32 F4 A8        LD      ($A8F4),A           ; {hard.workRam+F4} re-arm the shared spawn cooldown
430C: FD E1           POP     IY                  ; restore the spawner's entry pointer
430E: DD E1           POP     IX                  ; and its record pointer
4310: C3 64 56        JP      $5664               ; {code.requestAttackerSpawnSoundEra0} ask for the era-0 spawn sound and return

loc_4313:
4313: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index again
4316: FE 03           CP      $03                 ; era three?
4318: CA 6F 43        JP      Z,$436F             ; {code.loc_436f} era 3: the doubled-velocity offset path
431B: D2 4C 43        JP      NC,$434C            ; {code.loc_434c} era 4: the straight-aim path
431E: 21 7F AC        LD      HL,$AC7F            ; point at the fixed aim point -- eras 1-2
4321: CD B8 33        CALL    $33B8               ; {code.headingToward} work out the heading toward it
4324: DD 77 01        LD      (IX+$01),A          ; store that heading
4327: DD 7E 0F        LD      A,(IX+$0F)          ; take the stored half-turn phase
432A: 0F              RRCA                        ; keep its sign
432B: E6 80           AND     $80                 
432D: C6 40           ADD     A,$40               ; skew the heading by a half-turn either way
432F: DD 86 01        ADD     A,(IX+$01)          
4332: DD 77 02        LD      (IX+$02),A          ; store the skewed heading as the object's facing
4335: CD AF 3F        CALL    $3FAF               ; {code.dressSpriteShapeAndAttributeForHeadingSector} dress the sprite's shape and colour for that heading
4338: DD 35 00        DEC     (IX+$00)            ; wind the new slot live
433B: 3A F6 A8        LD      A,($A8F6)           ; {hard.workRam+F6} read the spawn-cooldown reload
433E: 32 F4 A8        LD      ($A8F4),A           ; {hard.workRam+F4} re-arm the shared spawn cooldown
4341: DD 36 0E 00     LD      (IX+$0E),$00        ; clear the slot's delay byte
4345: FD E1           POP     IY                  ; restore the spawner's entry pointer
4347: DD E1           POP     IX                  ; and its record pointer
4349: C3 6E 56        JP      $566E               ; {code.requestTwoSoundsWhilePlaying} ask for the in-play spawn sounds and return

loc_434c:
434C: 21 7F AC        LD      HL,$AC7F            ; point at the fixed aim point
434F: CD B8 33        CALL    $33B8               ; {code.headingToward} work out the heading toward it
4352: DD 77 01        LD      (IX+$01),A          ; store it as the object's heading
4355: DD 77 02        LD      (IX+$02),A          ; and as its facing, unskewed
4358: CD AF 3F        CALL    $3FAF               ; {code.dressSpriteShapeAndAttributeForHeadingSector} dress the sprite for that heading
435B: DD 35 00        DEC     (IX+$00)            ; wind the new slot live
435E: 3A F6 A8        LD      A,($A8F6)           ; {hard.workRam+F6} read the spawn-cooldown reload
4361: 32 F4 A8        LD      ($A8F4),A           ; {hard.workRam+F4} re-arm the shared spawn cooldown
4364: DD 36 0E 00     LD      (IX+$0E),$00        ; clear the slot's delay byte
4368: FD E1           POP     IY                  ; restore the spawner's entry pointer
436A: DD E1           POP     IX                  ; and its record pointer
436C: C3 74 56        JP      $5674               ; {code.requestAttackerSpawnSoundLateEra} ask for the late-era spawn sound and return

loc_436f:
436F: C5              PUSH    BC                  ; save the facing
4370: 79              LD      A,C                 ; which half of the compass the facing lies in
4371: C6 40           ADD     A,$40               
4373: E6 80           AND     $80                 
4375: 79              LD      A,C                 ; reload the facing
4376: 20 07           JR      NZ,$437F            ; {code.loc_437f} back half: subtract the offset
4378: C6 1A           ADD     A,$1A               ; front half: add a fixed heading offset
437A: DD 77 02        LD      (IX+$02),A          ; store the offset heading
437D: 18 05           JR      $4384               ; {code.loc_4384} go build its velocity

loc_437f:
437F: D6 1A           SUB     $1A                 ; subtract the fixed heading offset
4381: DD 77 02        LD      (IX+$02),A          ; store the offset heading

loc_4384:
4384: CD 8E 59        CALL    $598E               ; {code.loc_598e} look up the doubled velocity vector for that heading
4387: DD 73 0A        LD      (IX+$0A),E          ; file the first velocity word
438A: DD 72 0B        LD      (IX+$0B),D          
438D: DD 71 0C        LD      (IX+$0C),C          ; file the second velocity word
4390: DD 70 0D        LD      (IX+$0D),B          
4393: C1              POP     BC                  ; recover the facing
4394: DD 71 02        LD      (IX+$02),C          ; restore the true facing over the offset one
4397: CD AF 3F        CALL    $3FAF               ; {code.dressSpriteShapeAndAttributeForHeadingSector} dress the sprite for the heading
439A: DD 36 0E 20     LD      (IX+$0E),$20        ; seed the slot's delay byte
439E: DD 35 00        DEC     (IX+$00)            ; wind the new slot live
43A1: 3A F6 A8        LD      A,($A8F6)           ; {hard.workRam+F6} read the spawn-cooldown reload
43A4: 32 F4 A8        LD      ($A8F4),A           ; {hard.workRam+F4} re-arm the shared spawn cooldown
43A7: FD E1           POP     IY                  ; restore the spawner's entry pointer
43A9: DD E1           POP     IX                  ; and its record pointer
43AB: C3 6E 56        JP      $566E               ; {code.requestTwoSoundsWhilePlaying} ask for the in-play spawn sounds and return

loc_43ae:
43AE: 3A E6 A8        LD      A,($A8E6)           ; {hard.workRam+E6} read the aim-window half-width
43B1: DD 77 04        LD      (IX+$04),A          ; seed it as the new slot's countdown byte
43B4: C3 13 43        JP      $4313               ; {code.loc_4313} then take the aim path

; once-in-eight-frames gate for the Mother-Ship: while the wave-hold flag
; 0xacc6 is clear, defer to the deep-state stepper (stepMotherShip) if it
; is already live (MOTHER_SHIP_ARMED 0xad0d != 0), else -- only when the
; kill quota (KILLS_REMAINING 0xad02) is spent and both records of its
; two-slot bank (0xa8a0/0xa8b0) read empty -- arm it (0xad0d=0xff), seed
; the lead record's seven-hit counter (ix+0x04=0x07), and retire the
; matching entry pair into cooldown to spawn it
armMotherShipOrStep:
43B7: 3A C6 AC        LD      A,($ACC6)           ; {hard.workRam+4C6} read the round-transition hold flag
43BA: 3C              INC     A                   ; is it holding?
43BB: C8              RET     Z                   ; held between rounds: do nothing
43BC: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} read the mother-ship armed flag
43BF: A7              AND     A                   ; already active?
43C0: 20 2E           JR      NZ,$43F0            ; {code.loc_43f0} yes: step its live sequence
43C2: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} which frame of the eight-frame round
43C5: E6 07           AND     $07                 
43C7: FE 05           CP      $05                 ; only on frame five
43C9: C0              RET     NZ                  ; other frames: leave
43CA: DD 21 A0 A8     LD      IX,$A8A0            ; point at the mother-ship record bank
43CE: FD 21 24 AA     LD      IY,$AA24            ; and its sprite entry
43D2: 3A 02 AD        LD      A,($AD02)           ; {hard.workRam+502} read the kills-remaining quota
43D5: DD B6 00        OR      (IX+$00)            ; fold in the first bank record
43D8: DD B6 10        OR      (IX+$10)            ; and the second record
43DB: C0              RET     NZ                  ; quota unspent or a slot still busy: not yet
43DC: 3E FF           LD      A,$FF               ; raise the mother-ship armed flag
43DE: 32 0D AD        LD      ($AD0D),A           ; {hard.workRam+50D}
43E1: DD 36 04 07     LD      (IX+$04),$07        ; seed its seven-hit counter
43E5: C3 DB 46        JP      $46DB               ; {code.retireEntryPairIntoCooldown} clear its entry pair and set its spawn cooldown to bring it on

; add a run of program-image bytes into one eight-bit total and hand it
; down the tail chain that compares it against the value a genuine image
; gives, so the machine leaves either on the ordinary path or into the
; trap; a length of zero means a full 256 bytes and the total wraps
sumImageBlockForTheTamperCheck:
43E8: AF              XOR     A                   ; start the running total at zero

loc_43e9:
43E9: 86              ADD     A,(HL)              ; add this program-image byte into the total
43EA: 23              INC     HL                  ; step to the next byte
43EB: 10 FC           DJNZ    $43E9               ; {code.loc_43e9} sum the whole block -- a length of zero means all 256 bytes
43ED: C3 AD 07        JP      $07AD               ; {code.parkTheImageTotalForTheTamperVerdict} hand the total to the tamper-verdict check

loc_43f0:
43F0: DD 21 A0 A8     LD      IX,$A8A0            ; point at the mother-ship record
43F4: FD 21 24 AA     LD      IY,$AA24            ; and its sprite entry
43F8: DD 7E 00        LD      A,(IX+$00)          ; read its state byte
43FB: A7              AND     A                   ; in the idle / placement state?
43FC: CA 35 45        JP      Z,$4535             ; {code.loc_4535} state zero: tick its spawn delay or place it
43FF: 3C              INC     A                   ; is the state 0xFF -- in flight?
4400: C2 40 45        JP      NZ,$4540            ; {code.loc_4540} other states: the hit-countdown handling

loc_4403:
4403: DD 66 0C        LD      H,(IX+$0C)          ; take the object's first velocity word
4406: DD 6E 0D        LD      L,(IX+$0D)          
4409: ED 5B 08 A8     LD      DE,($A808)          ; {hard.workRam+8} read the world-scroll for that axis
440D: 19              ADD     HL,DE               ; add the scroll to the velocity
440E: FD 56 31        LD      D,(IY+$31)          ; take the object's current coordinate
4411: DD 5E 03        LD      E,(IX+$03)          
4414: 19              ADD     HL,DE               ; advance it
4415: FD 74 31        LD      (IY+$31),H          ; store the new coordinate back
4418: DD 75 03        LD      (IX+$03),L          
441B: DD 66 1C        LD      H,(IX+$1C)          ; take the second velocity word
441E: DD 6E 1D        LD      L,(IX+$1D)          
4421: ED 5B 0A A8     LD      DE,($A80A)          ; {hard.workRam+A} read the world-scroll for the other axis
4425: 19              ADD     HL,DE               ; add the scroll
4426: FD 56 00        LD      D,(IY+$00)          ; take the other coordinate
4429: DD 5E 05        LD      E,(IX+$05)          
442C: 19              ADD     HL,DE               ; advance it
442D: FD 74 00        LD      (IY+$00),H          ; store it back
4430: DD 75 05        LD      (IX+$05),L          
4433: FD 7E 31        LD      A,(IY+$31)          ; take the first coordinate
4436: C6 10           ADD     A,$10               ; bias it for the hardware sprite
4438: FD 77 33        LD      (IY+$33),A          ; write it to the hardware sprite slot
443B: FD 7E 00        LD      A,(IY+$00)          ; take the second coordinate
443E: FD 77 02        LD      (IY+$02),A          ; copy it to the hardware sprite slot
4441: CD 47 44        CALL    $4447               ; {code.dressSpriteForHeadingOrRetireAtEdge} dress the sprite for its heading, or retire it at the edge
4444: C3 F0 46        JP      $46F0               ; {code.loc_46f0} then try to fire a mother-ship shot at the player

; dress an object's sprite entry to face its heading (heading-quadrant
; picks a shape pair, era picks a colour, one heading half swaps the pair
; and the other biases the colour by half a page), unless the object has
; reached the field edge, in which case retire the entry pair; on the
; flutter era instead give a two-frame flutter and step/cap/close-out the
; wind-down counter
dressSpriteForHeadingOrRetireAtEdge:
4447: CD C4 3C        CALL    $3CC4               ; {code.hasReachedBoundaryBandSelectedByHeading} has the object reached the field-edge band its heading faces?
444A: DA DB 46        JP      C,$46DB             ; {code.retireEntryPairIntoCooldown} at the edge: retire its entry pair into cooldown
444D: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
4450: 57              LD      D,A                 
4451: FE 04           CP      $04                 ; the flutter era?
4453: CA A2 44        JP      Z,$44A2             ; {code.loc_44a2} era 4: give it the flutter animation instead
4456: 7A              LD      A,D                 ; multiply the era by sixteen -- the shape-table row base
4457: 87              ADD     A,A                 
4458: 87              ADD     A,A                 
4459: 87              ADD     A,A                 
445A: 87              ADD     A,A                 
445B: 47              LD      B,A                 
445C: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} take one bit of the frame counter -- the two-frame animation tick
445F: E6 02           AND     $02                 
4461: 80              ADD     A,B                 ; fold it into the row base
4462: 47              LD      B,A                 
4463: 3E 07           LD      A,$07               ; seven minus the object's phase byte
4465: DD 96 04        SUB     (IX+$04)            
4468: 0F              RRCA                        ; fold that to a two-bit heading quadrant
4469: E6 03           AND     $03                 
446B: 5F              LD      E,A                 
446C: 87              ADD     A,A                 ; index = quadrant*4 + row base
446D: 87              ADD     A,A                 
446E: 80              ADD     A,B                 
446F: 21 F1 44        LD      HL,$44F1            ; point at the shape-pair table
4472: DF              RST     $18                 ; offset into it by the index
4473: 46              LD      B,(HL)              ; read the pair's two shape codes
4474: 23              INC     HL                  
4475: 4E              LD      C,(HL)              
4476: 21 31 45        LD      HL,$4531            ; point at the per-era colour table
4479: 7A              LD      A,D                 ; index by era
447A: DF              RST     $18                 ; offset into it
447B: 56              LD      D,(HL)              ; read this era's colour code
447C: DD 7E 02        LD      A,(IX+$02)          ; which half of the compass the heading lies in
447F: C6 40           ADD     A,$40               
4481: FE 80           CP      $80                 
4483: 38 10           JR      C,$4495             ; {code.loc_4495} one half: swap the pair, keep the plain colour
4485: FD 70 01        LD      (IY+$01),B          ; seat the shape codes in order
4488: FD 71 03        LD      (IY+$03),C          
448B: 7A              LD      A,D                 ; take the colour
448C: C6 80           ADD     A,$80               ; bias it by half a page
448E: FD 77 30        LD      (IY+$30),A          ; seat the biased colour in both sprite slots
4491: FD 77 32        LD      (IY+$32),A          
4494: C9              RET                         

loc_4495:
4495: FD 71 01        LD      (IY+$01),C          ; seat the shape codes swapped
4498: FD 70 03        LD      (IY+$03),B          
449B: FD 72 30        LD      (IY+$30),D          ; seat the plain colour in both slots
449E: FD 72 32        LD      (IY+$32),D          
44A1: C9              RET                         

loc_44a2:
44A2: DD 7E 04        LD      A,(IX+$04)          ; read the object's wind-down seed
44A5: 5F              LD      E,A                 
44A6: FE 07           CP      $07                 ; already settled?
44A8: CA BF 44        JP      Z,$44BF             ; {code.loc_44bf} settled: just dress the flutter
44AB: DD 34 06        INC     (IX+$06)            ; step the wind-down counter
44AE: DD 4E 06        LD      C,(IX+$06)          ; read it
44B1: CB 79           BIT     7,C                 ; has it wrapped past the top?
44B3: 20 14           JR      NZ,$44C9            ; {code.restartAnimationCounterThenDressFlutterSprite} overrun: restart the counter and dress the flutter
44B5: 7B              LD      A,E                 ; has the counter reached the seed plus two?
44B6: C6 02           ADD     A,$02               
44B8: B9              CP      C                   
44B9: 30 04           JR      NC,$44BF            ; {code.loc_44bf} not yet: dress the flutter
44BB: DD 36 06 80     LD      (IX+$06),$80        ; mark the counter closed out

loc_44bf:
44BF: FD 36 30 70     LD      (IY+$30),$70        ; set the flutter colour code in both slots
44C3: FD 36 32 70     LD      (IY+$32),$70        
44C7: 18 13           JR      $44DC               ; {code.dressSpriteFlutterShapesByFrameTickBit} go dress the flutter's two shapes

; close out one object's animation and dress its sprite entry: the counter
; the caller carries is read without the top bit that selected this path,
; and once what is left has reached three the counter cell in the object's
; record is put back to zero -- below three it is left alone. Either way
; both attribute slots of the sprite entry take the one code fixed here,
; and the two shape codes are then chosen by the flutter this entry hands
; on to
restartAnimationCounterThenDressFlutterSprite:
44C9: 79              LD      A,C                 ; drop the top marker bit from the counter
44CA: E6 7F           AND     $7F                 
44CC: FE 03           CP      $03                 ; reached three?
44CE: 38 04           JR      C,$44D4             ; {code.loc_44d4} below three: leave the counter alone
44D0: DD 36 06 00     LD      (IX+$06),$00        ; at three or more: restart the wind-down counter

loc_44d4:
44D4: FD 36 30 51     LD      (IY+$30),$51        ; set the sprite's attribute code in both slots
44D8: FD 36 32 51     LD      (IY+$32),$51        

; give an object the two shapes of a two-frame flutter, the pair picked by
; one bit of a counter cell and nothing the object holds
dressSpriteFlutterShapesByFrameTickBit:
44DC: 11 02 02        LD      DE,$0202            ; the step between the two flutter shape pairs
44DF: 21 D5 D4        LD      HL,$D4D5            ; the first shape pair
44E2: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} test one bit of the frame counter -- which flutter frame
44E5: CB 57           BIT     2,A                 
44E7: 20 01           JR      NZ,$44EA            ; {code.loc_44ea} one phase: keep the first pair
44E9: 19              ADD     HL,DE               ; other phase: take the second pair

loc_44ea:
44EA: FD 75 01        LD      (IY+$01),L          ; seat the two shape codes in the sprite entry
44ED: FD 74 03        LD      (IY+$03),H          
44F0: C9              RET                         

; ---- $44F1-$4534: data ----
44F1: 39 38 39 38 3B 3A 3D 3C 3B 3A 3D 3C 3D 3C 3F 3E
4501: B0 B1 B2 B3 B4 B5 B6 B7 B8 B9 BA BB BC BD BE BF
4511: C0 C1 C2 C3 C4 C5 C6 C7 C6 C7 C8 C9 C8 C9 CA CB
4521: CC CD CC CD CE CF D0 D1 CE CF D0 D1 D0 D1 D2 D3
4531: E9 58 6F 6E

loc_4535:
4535: DD 7E 0E        LD      A,(IX+$0E)          ; read the mother-ship's spawn delay
4538: A7              AND     A                   ; counted out?
4539: CA 63 46        JP      Z,$4663             ; {code.loc_4663} time to place it: go position it
453C: DD 35 0E        DEC     (IX+$0E)            ; else tick the delay down
453F: C9              RET                         

loc_4540:
4540: 4F              LD      C,A                 ; keep the raised state value
4541: DD 7E 04        LD      A,(IX+$04)          ; read its remaining hit count
4544: A7              AND     A                   ; any hits left?
4545: 28 0D           JR      Z,$4554             ; {code.loc_4554} none: it is destroyed -- run the round-clear
4547: DD 35 04        DEC     (IX+$04)            ; take one off the hit count
454A: DD 36 00 FF     LD      (IX+$00),$FF        ; keep it in flight
454E: CD 83 56        CALL    $5683               ; {code.requestTwoSounds} play its hit sound
4551: C3 03 44        JP      $4403               ; {code.loc_4403} and fly it on

loc_4554:
4554: 79              LD      A,C                 ; recall the state value
4555: FE F0           CP      $F0                 ; is the flash sequence over?
4557: C2 B3 45        JP      NZ,$45B3            ; {code.stepMotherShipWarpFlashFrame} not yet: step the warp/flash frame
455A: AF              XOR     A                   ; clear the mother-ship progress cell
455B: 32 DC A8        LD      ($A8DC),A           ; {hard.workRam+DC}
455E: CD 34 56        CALL    $5634               ; {code.enqueueTransitionSoundBurst} quiet the running sound
4561: CD D2 56        CALL    $56D2               ; {code.requestRoundIntroSoundBurst} sound the round-clear fanfare
4564: 21 10 A8        LD      HL,$A810            ; point at the object bank
4567: 11 10 00        LD      DE,$0010            ; record stride
456A: 06 0F           LD      B,$0F               ; fifteen records to sweep
456C: 0E 14           LD      C,$14               ; first fill value

loc_456e:
456E: 7E              LD      A,(HL)              ; is this record empty?
456F: 3C              INC     A                   
4570: 20 22           JR      NZ,$4594            ; {code.loc_4594} occupied: handle it differently
4572: 71              LD      (HL),C              ; stamp the record with the sweep value
4573: D9              EXX                         
4574: 11 02 04        LD      DE,$0402            
4577: FF              RST     $38                 ; queue a display command for it
4578: D9              EXX                         

loc_4579:
4579: 19              ADD     HL,DE               ; step to the next record
457A: 79              LD      A,C                 ; bump the fill value
457B: C6 0A           ADD     A,$0A               
457D: 4F              LD      C,A                 
457E: 10 EE           DJNZ    $456E               ; {code.loc_456e} sweep the rest of the bank
4580: 0E 3C           LD      C,$3C               
4582: 3E FE           LD      A,$FE               ; set the round-transition hold
4584: 32 C6 AC        LD      ($ACC6),A           ; {hard.workRam+4C6}
4587: DD 36 00 E4     LD      (IX+$00),$E4        ; set the mother-ship's exit state
458B: FD 36 30 3D     LD      (IY+$30),$3D        ; set its exit colour in both slots
458F: FD 36 32 3D     LD      (IY+$32),$3D        
4593: C9              RET                         

loc_4594:
4594: 3C              INC     A                   ; was the record 0xFE?
4595: 20 E2           JR      NZ,$4579            ; {code.loc_4579} no: move on
4597: 36 00           LD      (HL),$00            ; clear it
4599: 18 DE           JR      $4579               ; {code.loc_4579} move on

; reached only via the "wrong-glyph" derail ($1772) and the loop-back
; ($4660); the bytes run as harmless NOPs and stray-stack POPs. The real
; routine is at $45B3.
; ---- $459B-$45B2: misaligned anti-tamper entry ----
459B: 16 A7 13 96 ED DC F1 8C 68 3B 0D ED F1 9B 13 13
45AB: 13 13 F1 88 DC ED 11 B9

; step one object's timed warp/flash sequence: drift it with the world,
; seed the sprite's heading and shape from angle/Y-gated tables, then
; count a state byte down — the 0xB4 frame flags the sprite, bumps the
; 0xA800 sentinel (which requests the warp sound at 0x580B when it wraps)
; and posts command 0x04/0x0D to the ring, above-trigger frames step an
; eight-shape ROM cycle, and a spent counter resets to idle then loops or
; returns on two program-image gates; reached through a misaligned
; prologue (two POP AF, DEC SP) whose stray carry can fold in a life-loss
stepMotherShipWarpFlashFrame:
45B3: CD 60 2B        CALL    $2B60               ; {code.driftWithWorldScroll} drift the object along with the world scroll
45B6: FD 7E 31        LD      A,(IY+$31)          ; take its first coordinate
45B9: 47              LD      B,A                 
45BA: C6 13           ADD     A,$13               ; is it inside the top screen band?
45BC: FE 03           CP      $03                 
45BE: 38 15           JR      C,$45D5             ; {code.loc_45d5} off the top: blank its shapes
45C0: 78              LD      A,B                 ; bias the coordinate for the hardware sprite
45C1: C6 10           ADD     A,$10               
45C3: FD 77 33        LD      (IY+$33),A          ; write it to the hardware sprite slot
45C6: FD 7E 00        LD      A,(IY+$00)          ; take its second coordinate
45C9: 47              LD      B,A                 
45CA: C6 08           ADD     A,$08               ; inside the edge band on that axis?
45CC: FE 28           CP      $28                 
45CE: 38 05           JR      C,$45D5             ; {code.loc_45d5} off that edge: blank its shapes
45D0: FD 70 02        LD      (IY+$02),B          ; write the second coordinate to the hardware sprite slot
45D3: 18 08           JR      $45DD               ; {code.loc_45dd} carry on to the shape step

loc_45d5:
45D5: FD 36 01 FF     LD      (IY+$01),$FF        ; blank the sprite's two shapes -- off-screen
45D9: FD 36 03 FF     LD      (IY+$03),$FF        

loc_45dd:
45DD: DD 7E 00        LD      A,(IX+$00)          ; read the sequence counter
45E0: FE B4           CP      $B4                 ; is this the flash-trigger frame?
45E2: 28 3F           JR      Z,$4623             ; {code.loc_4623} the trigger frame: fire the warp/flash
45E4: 38 13           JR      C,$45F9             ; {code.loc_45f9} below the trigger: skip the shape step
45E6: D6 B4           SUB     $B4                 ; turn the frame number into a 0-7 shape index
45E8: 0F              RRCA                        
45E9: 0F              RRCA                        
45EA: 0F              RRCA                        
45EB: 3D              DEC     A                   
45EC: E6 07           AND     $07                 
45EE: 21 1B 46        LD      HL,$461B            ; point at the eight-frame warp animation
45F1: CF              RST     $08                 ; read this frame's shape
45F2: FD 77 03        LD      (IY+$03),A          ; seat it as one shape
45F5: 3C              INC     A                   ; seat the next code as the other shape
45F6: FD 77 01        LD      (IY+$01),A          

loc_45f9:
45F9: DD 35 00        DEC     (IX+$00)            ; count the sequence down one frame
45FC: CA 46 46        JP      Z,$4646             ; {code.loc_4646} sequence spent: end it
45FF: DD 7E 00        LD      A,(IX+$00)          ; reached the halfway mark?
4602: FE 5A           CP      $5A                 
4604: C0              RET     NZ                  ; not yet: leave
4605: FD 36 01 FF     LD      (IY+$01),$FF        ; blank its shapes at the halfway point
4609: FD 36 03 FF     LD      (IY+$03),$FF        
460D: C9              RET                         

; two-player-start setup arm (called from 0x189E): when the video cell
; 0xA67C and work cell 0xAB43 disagree, decrement the counter at (IX+0),
; seat 0xFE/0xFD and 0x6C/0x6C into the object slot at
; (IY+1/+3/+0x30/+0x32), request sound 0x580B when 0xA800 is 0xFF, and
; queue ring command 0x04/0x0D; a no-op when the two cells agree
setUpTwoPlayerStartObjectOnce:
460E: 21 7C A6        LD      HL,$A67C            ; point at the watched video cell
4611: 7E              LD      A,(HL)              ; read it
4612: 4F              LD      C,A                 
4613: 3A 43 AB        LD      A,($AB43)           ; {hard.workRam+343} compare against the mirror cell
4616: 91              SUB     C                   
4617: C2 43 46        JP      NZ,$4643            ; {code.loc_4643} they disagree: run the start-object setup
461A: C9              RET                         

loc_461b:
461B: 94              SUB     H                   ; eight warp-flash shape codes -- also run off as harmless register churn when the start-object path jumps here and drops into 0x4623
461C: 96              SUB     (HL)                
461D: 96              SUB     (HL)                
461E: 94              SUB     H                   
461F: 92              SUB     D                   
4620: 90              SUB     B                   
4621: 90              SUB     B                   
4622: 94              SUB     H                   

loc_4623:
4623: DD 35 00        DEC     (IX+$00)            ; step the sequence counter
4626: FD 36 01 FE     LD      (IY+$01),$FE        ; set the flash shapes
462A: FD 36 03 FD     LD      (IY+$03),$FD        
462E: FD 36 30 6C     LD      (IY+$30),$6C        ; set the flash colour in both slots
4632: FD 36 32 6C     LD      (IY+$32),$6C        
4636: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} is the warp sentinel armed?
4639: 3C              INC     A                   ; if so, sound the mother-ship warp
463A: CC 0B 58        CALL    Z,$580B             ; {code.requestMotherShipWarpSound}
463D: 11 0D 04        LD      DE,$040D            ; the display command
4640: C3 38 00        JP      $0038               ; {code.postCommand} queue it and return

loc_4643:
4643: C3 1B 46        JP      $461B               ; {code.loc_461b} jump on to the start-object setup

loc_4646:
4646: 3E FF           LD      A,$FF               ; raise the round-transition hold
4648: 32 C6 AC        LD      ($ACC6),A           ; {hard.workRam+4C6}
464B: DD 36 00 00     LD      (IX+$00),$00        ; reset the object's state to idle
464F: 21 43 AB        LD      HL,$AB43            ; point at the mode cell
4652: 7E              LD      A,(HL)              ; is it the expected value?
4653: FE 7C           CP      $7C                 
4655: C2 60 46        JP      NZ,$4660            ; {code.loc_4660} no: loop the warp/flash stepper
4658: 23              INC     HL                  ; read the following cell
4659: 7E              LD      A,(HL)              
465A: FE 10           CP      $10                 ; one accepted value?
465C: C8              RET     Z                   ; yes: end here
465D: FE 05           CP      $05                 ; the other accepted value?
465F: C8              RET     Z                   ; yes: end here

loc_4660:
4660: C3 9B 45        JP      $459B               ; run the warp/flash stepper again

loc_4663:
4663: 3A C6 AC        LD      A,($ACC6)           ; {hard.workRam+4C6} is a round transition holding?
4666: A7              AND     A                   
4667: C0              RET     NZ                  ; yes: wait
4668: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} take the world angle
466B: 47              LD      B,A                 
466C: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} take the frame counter
466F: 4F              LD      C,A                 
4670: 3E 10           LD      A,$10               ; base step
4672: CB 59           BIT     3,C                 ; test a frame-counter bit
4674: 20 02           JR      NZ,$4678            ; {code.loc_4678} one way: keep it positive
4676: ED 44           NEG                         ; other way: negate the step

loc_4678:
4678: 80              ADD     A,B                 ; add it to the angle
4679: 0F              RRCA                        ; fold to an even table index
467A: 0F              RRCA                        
467B: E6 3E           AND     $3E                 
467D: 21 84 3C        LD      HL,$3C84            ; point at the entry-position table
4680: CF              RST     $08                 ; read the first coordinate
4681: FD 77 31        LD      (IY+$31),A          ; seat it
4684: 23              INC     HL                  ; read the second coordinate
4685: 7E              LD      A,(HL)              
4686: FD 77 00        LD      (IY+$00),A          ; seat it
4689: 78              LD      A,B                 ; which half of the compass the angle faces
468A: C6 C0           ADD     A,$C0               
468C: E6 80           AND     $80                 
468E: DD 77 02        LD      (IX+$02),A          ; store it as the mother-ship's facing
4691: CD BA 46        CALL    $46BA               ; {code.setMotherShipVelocityFromHeading} give it the velocity its heading picks
4694: DD 7E 04        LD      A,(IX+$04)          ; is its hit count already high enough?
4697: FE 06           CP      $06                 
4699: 30 04           JR      NC,$469F            ; {code.loc_469f} yes: leave it
469B: DD 36 04 05     LD      (IX+$04),$05        ; else seed a minimum hit count

loc_469f:
469F: DD 36 00 FF     LD      (IX+$00),$FF        ; mark the mother ship in flight
46A3: C3 F7 57        JP      $57F7               ; {code.requestCurrentEraSound} ask for the current-era sound and return

; ---- $46A6-$46B9: data ----
46A6: 3A 80 A9 4F E6 1C CB 41 20 02 ED 44 80 0F 0F E6
46B6: 3E C3 7D 46

; give the Mother-Ship the two velocity words its current heading picks
; out of the velocity table the era selects -- the word at the heading and
; the word a quarter turn behind it -- and park them at +0x0C and +0x1C of
; the record pair, which is where its motion reads them
setMotherShipVelocityFromHeading:
46BA: 21 CE 46        LD      HL,$46CE            ; set the return to the record-filing step
46BD: E5              PUSH    HL                  ; lay it on the stack for the arm to return through
46BE: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} the era index picks which velocity arm
46C1: E6 07           AND     $07                 
46C3: F7              RST     $30                 ; jump through the arm table below

; ---- $46C4-$46CD: jump table ----
46C4: 42 59 4E 59 4E 59 65 59 6B 59

; file two register pairs into an object's record as four bytes, each pair
; high byte first and so stored the opposite way round from a word
fileTwoPairsIntoObjectRecordHighByteFirst:
46CE: DD 72 0C        LD      (IX+$0C),D          ; file the first pair's high byte
46D1: DD 73 0D        LD      (IX+$0D),E          ; and its low byte
46D4: DD 70 1C        LD      (IX+$1C),B          ; file the second pair's high byte
46D7: DD 71 1D        LD      (IX+$1D),C          ; and its low byte
46DA: C9              RET                         

; clear a record's occupancy byte and both coordinates of TWO neighbouring
; sprite entries, then arm the record's delay byte with a fixed value
; rather than leaving it clear
retireEntryPairIntoCooldown:
46DB: AF              XOR     A                   ; zero
46DC: DD 77 00        LD      (IX+$00),A          ; clear the record's occupancy byte
46DF: FD 77 00        LD      (IY+$00),A          ; clear the first entry's coordinate
46E2: FD 77 02        LD      (IY+$02),A          ; and its hardware copy
46E5: FD 77 31        LD      (IY+$31),A          ; clear the paired entry's coordinate
46E8: FD 77 33        LD      (IY+$33),A          ; and its hardware copy
46EB: DD 36 0E 5F     LD      (IX+$0E),$5F        ; arm the record's cooldown delay
46EF: C9              RET                         

loc_46f0:
46F0: DD 7E 00        LD      A,(IX+$00)          ; is the object fully in flight?
46F3: 3C              INC     A                   
46F4: C0              RET     NZ                  ; not yet: leave
46F5: 3A 17 A8        LD      A,($A817)           ; {hard.workRam+17} is a mother-ship shot already out?
46F8: A7              AND     A                   
46F9: C0              RET     NZ                  ; yes: only one at a time
46FA: 06 02           LD      B,$02               ; two entry slots to consider
46FC: 3A 27 A8        LD      A,($A827)           ; {hard.workRam+27} read the fire-window half-width
46FF: 57              LD      D,A                 
4700: 87              ADD     A,A                 ; double it to the full window
4701: 5F              LD      E,A                 

loc_4702:
4702: FD 7E 00        LD      A,(IY+$00)          ; is the target within the vertical band?
4705: C6 08           ADD     A,$08               
4707: FE 28           CP      $28                 
4709: 38 1B           JR      C,$4726             ; {code.loc_4726} off that band: skip this slot
470B: FD 7E 31        LD      A,(IY+$31)          ; within the horizontal band?
470E: C6 10           ADD     A,$10               
4710: FE 20           CP      $20                 
4712: 38 12           JR      C,$4726             ; {code.loc_4726} off it: skip this slot
4714: 3E 84           LD      A,$84               ; within the aim window on one axis?
4716: FD 96 00        SUB     (IY+$00)            
4719: 82              ADD     A,D                 
471A: BB              CP      E                   
471B: 30 17           JR      NC,$4734            ; {code.loc_4734} yes: fire from this slot
471D: 3E 78           LD      A,$78               ; within the window on the other axis?
471F: FD 96 31        SUB     (IY+$31)            
4722: 82              ADD     A,D                 
4723: BB              CP      E                   
4724: 30 0E           JR      NC,$4734            ; {code.loc_4734} yes: fire from this slot

loc_4726:
4726: D9              EXX                         ; step to the next record
4727: 11 10 00        LD      DE,$0010            
472A: DD 19           ADD     IX,DE               
472C: FD 23           INC     IY                  ; step its paired entry
472E: FD 23           INC     IY                  
4730: D9              EXX                         
4731: 10 CF           DJNZ    $4702               ; {code.loc_4702} try the other slot
4733: C9              RET                         

loc_4734:
4734: 21 30 A8        LD      HL,$A830            ; point at the shot record bank
4737: D9              EXX                         
4738: 21 16 AA        LD      HL,$AA16            ; and its sprite entries
473B: 06 02           LD      B,$02               ; two shot slots to search

loc_473d:
473D: D9              EXX                         
473E: 7E              LD      A,(HL)              ; is this shot slot free?
473F: A7              AND     A                   
4740: 28 0A           JR      Z,$474C             ; {code.loc_474c} free: launch from it
4742: 11 10 00        LD      DE,$0010            ; step to the next shot record
4745: 19              ADD     HL,DE               
4746: D9              EXX                         
4747: 23              INC     HL                  ; and its entry
4748: 23              INC     HL                  
4749: 10 F2           DJNZ    $473D               ; {code.loc_473d} try the other slot
474B: C9              RET                         

loc_474c:
474C: 22 91 A9        LD      ($A991),HL          ; {hard.workRam+191} stash the free shot record
474F: D9              EXX                         
4750: 22 93 A9        LD      ($A993),HL          ; {hard.workRam+193} and its entry
4753: CD 5F 56        CALL    $565F               ; {code.requestEnemyLaunchSound} play the enemy launch sound
4756: 21 7F AC        LD      HL,$AC7F            ; the fixed aim point -- the player
4759: CD B8 33        CALL    $33B8               ; {code.headingToward} work out the heading toward it
475C: 67              LD      H,A                 ; keep the heading
475D: EB              EX      DE,HL               
475E: 21 B4 A8        LD      HL,$A8B4            ; step the alternating spread counter
4761: 34              INC     (HL)                
4762: 3E 18           LD      A,$18               ; one bit of it picks the spread direction
4764: CB 46           BIT     0,(HL)              
4766: 20 02           JR      NZ,$476A            ; {code.loc_476a} one way: keep the spread positive
4768: ED 44           NEG                         ; other way: negate it

loc_476a:
476A: EB              EX      DE,HL               
476B: 84              ADD     A,H                 ; skew the heading by the spread
476C: FD 46 31        LD      B,(IY+$31)          ; take the firer's coordinates
476F: FD 4E 00        LD      C,(IY+$00)          
4772: DD 2A 91 A9     LD      IX,($A991)          ; {hard.workRam+191} point at the new shot's record and entry
4776: FD 2A 93 A9     LD      IY,($A993)          ; {hard.workRam+193}
477A: DD 77 02        LD      (IX+$02),A          ; store the shot's heading
477D: FD 70 31        LD      (IY+$31),B          ; place it at the firer's position
4780: FD 71 00        LD      (IY+$00),C          
4783: 21 95 47        LD      HL,$4795            ; set the return to the velocity-store step
4786: E5              PUSH    HL                  
4787: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} the era index picks the shot's velocity arm
478A: F7              RST     $30                 

; ---- $478B-$4794: jump table ----
478B: 8E 59 8E 59 94 59 94 59 94 59

loc_4795:
4795: DD 73 0A        LD      (IX+$0A),E          ; file the first velocity word
4798: DD 72 0B        LD      (IX+$0B),D          
479B: DD 71 0C        LD      (IX+$0C),C          ; file the second velocity word
479E: DD 70 0D        LD      (IX+$0D),B          
47A1: FD 36 01 4D     LD      (IY+$01),$4D        ; set the shot's shape code
47A5: FD 36 30 62     LD      (IY+$30),$62        ; and its colour
47A9: DD 35 00        DEC     (IX+$00)            ; bring the shot live
47AC: 3A 14 A8        LD      A,($A814)           ; {hard.workRam+14} mark that a mother-ship shot is now out
47AF: 32 17 A8        LD      ($A817),A           ; {hard.workRam+17}
47B2: C9              RET                         

; per-frame manager of the single parachutist slot (record 0xa8f0, sprite
; 0xaa2e): idle in era 4, else branch on the slot's state byte — free
; spawns it at the edge ahead, in-flight (0xff) flies it and retires it
; once it reaches a retire line else steps its shape from the frame tick,
; 0x10 posts its bonus, >=0x3c shows its award, and any lower value drifts
; it with the world then counts down and retires it at zero; the
; parachutist rescue object (canopy + 1000 bonus), removed by a negative
; control
runParachutistSlot:
47B3: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
47B6: FE 04           CP      $04                 ; the final era, which has no parachutist?
47B8: C8              RET     Z                   ; yes: nothing to run
47B9: DD 21 F0 A8     LD      IX,$A8F0            ; point at the parachutist record
47BD: FD 21 2E AA     LD      IY,$AA2E            ; and its sprite entry
47C1: DD 7E 00        LD      A,(IX+$00)          ; is the slot free?
47C4: A7              AND     A                   
47C5: CA 53 48        JP      Z,$4853             ; {code.spawnAtEdgeAhead} free: spawn one at the edge ahead
47C8: 3C              INC     A                   ; is its state in flight -- 0xFF?
47C9: C2 F2 47        JP      NZ,$47F2            ; {code.loc_47f2} other states: the drift / award handling
47CC: CD 05 3E        CALL    $3E05               ; {code.flyAlongStoredVelocity} fly it along its stored velocity
47CF: CD 83 2B        CALL    $2B83               ; {code.hasReachedRetireLine} has it reached the retire line?
47D2: DA AD 48        JP      C,$48AD             ; {code.retireSlotIntoCooldown} yes: retire the slot into cooldown
47D5: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} turn the frame tick into a 0-7 shape index
47D8: 0F              RRCA                        
47D9: 0F              RRCA                        
47DA: 0F              RRCA                        
47DB: 0F              RRCA                        
47DC: E6 07           AND     $07                 
47DE: 21 EA 47        LD      HL,$47EA            ; point at the canopy-sway shape table
47E1: CF              RST     $08                 ; read this frame's shape
47E2: FD 77 01        LD      (IY+$01),A          ; seat it
47E5: FD 36 30 75     LD      (IY+$30),$75        ; set the canopy colour
47E9: C9              RET                         

; ---- $47EA-$47F1: data ----
47EA: 00 01 02 03 03 02 01 00

loc_47f2:
47F2: CD 60 2B        CALL    $2B60               ; {code.driftWithWorldScroll} drift the parachutist with the world
47F5: DD 7E 00        LD      A,(IX+$00)          ; is it at the post-bonus state?
47F8: FE 10           CP      $10                 
47FA: CA 31 48        JP      Z,$4831             ; {code.postNextParachutistBonus} yes: post its next bonus value
47FD: FE 3C           CP      $3C                 ; is it at or above the award state?
47FF: D2 09 48        JP      NC,$4809            ; {code.showParachutistAward} yes: show its award glyph
4802: DD 35 00        DEC     (IX+$00)            ; else count its dying timer down
4805: C0              RET     NZ                  ; still counting: leave
4806: C3 AD 48        JP      $48AD               ; {code.retireSlotIntoCooldown} timer spent: retire the slot into cooldown

; start the parachutist slot's exit: put its state byte at the top of the
; dying countdown, ask for the sound that goes with collecting it, and
; swap its sprite tile to the glyph for the award the slot's own rung byte
; selects -- with one fixed glyph once the rung passes the four the table
; holds, so the lookup never reads on past the table
showParachutistAward:
4809: DD 36 00 3B     LD      (IX+$00),$3B        ; put the slot into its award / exit state
480D: CD FF 57        CALL    $57FF               ; {code.requestParachutistAwardSound} play the parachutist award sound
4810: DD 7E 07        LD      A,(IX+$07)          ; is the award index within the table?
4813: FE 04           CP      $04                 
4815: D2 24 48        JP      NC,$4824            ; {code.loc_4824} past the table: use the fixed award glyph
4818: 21 2D 48        LD      HL,$482D            ; read the award glyph for this rung
481B: CF              RST     $08                 
481C: FD 77 01        LD      (IY+$01),A          ; seat it as the sprite shape
481F: FD 36 30 6C     LD      (IY+$30),$6C        ; set its colour
4823: C9              RET                         

loc_4824:
4824: FD 36 01 8F     LD      (IY+$01),$8F        ; use the fixed top-award glyph
4828: FD 36 30 6C     LD      (IY+$30),$6C        ; set its colour
482C: C9              RET                         

; ---- $482D-$4830: data ----
482D: F9 FC 8D 8E

; post the next rung of the rescue award to the command ring and step the
; per-life rung count on; the first four rungs each take their own value
; from a four-entry table and every rung after them takes the same top
; value, so the ladder rises and then caps
postNextParachutistBonus:
4831: DD 35 00        DEC     (IX+$00)            ; count the slot's timer down
4834: DD 7E 07        LD      A,(IX+$07)          ; read the rung number
4837: DD 34 07        INC     (IX+$07)            ; step it on for next time
483A: FE 04           CP      $04                 ; past the four table rungs?
483C: D2 49 48        JP      NC,$4849            ; {code.loc_4849} yes: post the fixed top value
483F: 21 4F 48        LD      HL,$484F            ; index the rung-value table by the rung
4842: DF              RST     $18                 
4843: 5E              LD      E,(HL)              ; take this rung's value
4844: 16 04           LD      D,$04               ; command 0x04
4846: C3 38 00        JP      $0038               ; {code.postCommand} queue the bonus command and return

loc_4849:
4849: 11 0F 04        LD      DE,$040F            ; the fixed top command and value
484C: C3 38 00        JP      $0038               ; {code.postCommand} queue it and return

; ---- $484F-$4852: data ----
484F: 0A 0C 0D 0E

; on a cooldown, and only on alternate frames, place a free slot at the
; field-edge position the player's current heading selects, clear its sub-
; pixel remainders and mark it live
spawnAtEdgeAhead:
4853: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} is the mother ship armed?
4856: A7              AND     A                   
4857: C0              RET     NZ                  ; yes: hold this spawn off
4858: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} only act on alternate frames
485B: E6 01           AND     $01                 
485D: C8              RET     Z                   ; this frame: skip
485E: DD 35 0E        DEC     (IX+$0E)            ; tick the slot's spawn delay down
4861: C0              RET     NZ                  ; not yet zero: wait
4862: 3A 02 A8        LD      A,($A802)           ; {hard.workRam+2} take the player's heading, rounded
4865: C6 08           ADD     A,$08               
4867: 0F              RRCA                        ; fold it to one of sixteen edge sectors -- an even index
4868: 0F              RRCA                        
4869: 0F              RRCA                        
486A: E6 1E           AND     $1E                 
486C: 21 8D 48        LD      HL,$488D            ; point at the edge-position table
486F: CF              RST     $08                 ; read the sector's first coordinate
4870: FD 77 31        LD      (IY+$31),A          ; seat it
4873: 23              INC     HL                  ; read the second coordinate
4874: 7E              LD      A,(HL)              
4875: FD 77 00        LD      (IY+$00),A          ; seat it
4878: DD 36 0A 00     LD      (IX+$0A),$00        ; clear its velocity sub-pixel
487C: DD 36 0B 00     LD      (IX+$0B),$00        
4880: DD 36 0C 40     LD      (IX+$0C),$40        ; set its downward drift speed
4884: DD 36 0D 00     LD      (IX+$0D),$00        
4888: DD 36 00 FF     LD      (IX+$00),$FF        ; mark the slot live last, so it never runs with stale contents
488C: C9              RET                         

; ---- $488D-$48AC: data ----
488D: F0 40 F0 80 F0 F8 60 F8 80 F8 A0 F8 10 F8 00 80
489D: 00 90 10 10 30 10 60 10 80 10 A0 10 C0 10 F0 28

; take an object out of play -- occupancy byte and both of its sprite
; entry's coordinates -- and then arm the record's delay byte instead of
; leaving it clear, so the slot is held rather than freed
retireSlotIntoCooldown:
48AD: DD 36 00 00     LD      (IX+$00),$00        ; clear the record's occupancy byte -- the object leaves play
48B1: FD 36 00 00     LD      (IY+$00),$00        ; clear the sprite entry's first coordinate
48B5: FD 36 31 00     LD      (IY+$31),$00        ; clear its second coordinate
48B9: DD 36 0E F0     LD      (IX+$0E),$F0        ; load the record's delay byte with 0xF0 -- hold the slot on a cooldown rather than freeing it at once
48BD: C9              RET                         

; one frame of coin-input service: run the two coin-slot debounce/accept
; handlers and the phase-gated credit drip in turn, then pulse each
; mechanical coin counter once per coin still owed; dead unless an input
; edge or a pending debt is present
serviceCoinInputs:
48BE: CD E7 48        CALL    $48E7               ; {code.awardOneCreditOnDebouncedInputEdge} debounce the service-credit line and award a credit on its edge
48C1: CD 41 49        CALL    $4941               ; {code.tallyCoinSlot1AndAwardCredit} run coin slot 1's accept-and-tally
48C4: CD 11 49        CALL    $4911               ; {code.meterCoinageTowardCreditOnEdge} run the phase-gated credit drip
48C7: CD 84 49        CALL    $4984               ; {code.pulseSlot1CoinCounter} pulse coin slot 1's mechanical counter for each coin still owed
48CA: CD D6 49        CALL    $49D6               ; {code.pulseSlot2CoinCounter} pulse coin slot 2's mechanical counter for each coin still owed
48CD: C9              RET                         

; ---- $48CE-$48E6: data ----
48CE: 2C A7 13 FD 3B 88 0D DC F1 BF 68 0D D7 F1 FD 3B
48DE: FD DC FD A5 57 ED F1 52 B9

; per-frame debounce of IN0 bit 2 (port mirror 0xA9AE): rotate that bit
; into the bottom of the rolling history at 0xA983 (rl (hl)), fire only on
; a clean leading edge — the low three history bits reading 001 (idle,
; idle, pressed) — else return; on the edge request a sound (0x57F1) and
; award exactly one credit outright (C=1 into
; awardCoinCreditThenPulseCoinCounter, which folds it into the BCD credit
; count at 0xA986 and pulses the coin counter), a flat-credit path
; distinct from the coinage-metered coin-1 handler at 0x4941
awardOneCreditOnDebouncedInputEdge:
48E7: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the input-port mirror
48EA: 0F              RRCA                        ; rotate it right three times, dropping bit 2 -- the service-credit line -- into the carry
48EB: 0F              RRCA                        
48EC: 0F              RRCA                        
48ED: 21 83 A9        LD      HL,$A983            ; point at the service-credit debounce history
48F0: CB 16           RL      (HL)                ; shift that bit into the bottom of the rolling history
48F2: 7E              LD      A,(HL)              
48F3: E6 07           AND     $07                 ; keep the last three samples
48F5: FE 01           CP      $01                 ; a clean leading edge reads idle, idle, pressed
48F7: C0              RET     NZ                  ; not an edge -- nothing to do
48F8: CD F1 57        CALL    $57F1               ; {code.requestCoinSound} blip the coin sound
48FB: 0E 01           LD      C,$01               ; award exactly one credit
48FD: C3 6E 49        JP      $496E               ; {code.awardCoinCreditThenPulseCoinCounter} fold it into the credit count and pulse the counter

; ---- $4900-$4910: data ----
4900: BC A6 05 30 F1 7C 68 3B A5 38 FD F1 96 5D 17 9B
4910: B9

; phase-gated credit drip: rotate a selector bit (from 0xA9AE) into the
; phase cell 0xA9CA and act only when its low 3 bits read 1 -- request a
; sound, bump the counter at 0xA982, step the low byte at 0xA9CB up by
; 0x10; once the high byte at 0xA9CC still trails the raised low byte,
; pull the low byte back by (high&0xF0)+0x10 and tail into
; awardCoinCreditThenPulseCoinCounter with C = the high byte
meterCoinageTowardCreditOnEdge:
4911: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the input-port mirror
4914: 21 CA A9        LD      HL,$A9CA            ; point at coin slot 2's debounce history
4917: 0F              RRCA                        ; rotate the slot-2 selector bit toward the carry
4918: 0F              RRCA                        
4919: CB 16           RL      (HL)                
491B: 7E              LD      A,(HL)              ; shift it into the bottom of the history
491C: E6 07           AND     $07                 ; keep the last three samples
491E: FE 01           CP      $01                 ; act only on a clean leading edge
4920: C0              RET     NZ                  ; otherwise nothing this frame
4921: EB              EX      DE,HL               
4922: CD F1 57        CALL    $57F1               ; {code.requestCoinSound} blip the coin sound
4925: 21 82 A9        LD      HL,$A982            
4928: 34              INC     (HL)                ; bump the slot-2 coins-accepted count
4929: EB              EX      DE,HL               
492A: 23              INC     HL                  
492B: 7E              LD      A,(HL)              
492C: C6 10           ADD     A,$10               ; step the coins-inserted accumulator up by one coin's worth (0x10)
492E: 77              LD      (HL),A              ; store it back
492F: 47              LD      B,A                 
4930: 23              INC     HL                  
4931: 7E              LD      A,(HL)              ; read the coinage ratio byte
4932: 90              SUB     B                   ; compare the raised accumulator against it
4933: D0              RET     NC                  ; ratio not yet reached -- wait for more
4934: 7E              LD      A,(HL)              
4935: 4F              LD      C,A                 ; carry the whole ratio byte for crediting
4936: E6 F0           AND     $F0                 ; take its coins-per-credit high nibble
4938: C6 10           ADD     A,$10               ; plus one coin's worth
493A: 2B              DEC     HL                  
493B: ED 44           NEG                         ; negate
493D: 86              ADD     A,(HL)              ; pull the accumulator back by that much, carrying the overshoot forward
493E: 77              LD      (HL),A              ; store the reduced accumulator
493F: 18 2D           JR      $496E               ; {code.awardCoinCreditThenPulseCoinCounter} award the credit and pulse the counter

; one frame of coin slot 1 accounting: clock the raw coin line into a
; debounce shift register and, on a clean rising edge, count the coin --
; blip the coin sound, bump the tally, add a unit to the coins-inserted
; accumulator; once it passes the coinage threshold (coins-per-credit high
; nibble, credits awarded low) carry the overshoot forward and, unless the
; no-credit flag is set, add the low nibble to the packed-decimal credit
; count (saturated at 99) and repaint its panel; either overshoot path
; then pulses the mechanical coin counter
tallyCoinSlot1AndAwardCredit:
4941: 3A AE A9        LD      A,($A9AE)           ; {hard.workRam+1AE} read the input-port mirror
4944: 21 C7 A9        LD      HL,$A9C7            ; point at coin slot 1's debounce shift register
4947: 0F              RRCA                        ; rotate the coin-1 line toward the carry
4948: CB 16           RL      (HL)                ; clock it into the debounce register
494A: 7E              LD      A,(HL)              
494B: E6 07           AND     $07                 ; keep the last three samples
494D: FE 01           CP      $01                 ; a clean rising edge counts as one coin
494F: C0              RET     NZ                  ; no edge -- done
4950: EB              EX      DE,HL               
4951: CD F1 57        CALL    $57F1               ; {code.requestCoinSound} blip the coin sound
4954: 21 81 A9        LD      HL,$A981            
4957: 34              INC     (HL)                ; bump the count of coins slot 1 still owes its mechanical counter
4958: EB              EX      DE,HL               
4959: 23              INC     HL                  
495A: 7E              LD      A,(HL)              
495B: C6 10           ADD     A,$10               ; step the coins-inserted accumulator up by one coin (0x10)
495D: 77              LD      (HL),A              ; store it
495E: 47              LD      B,A                 
495F: 23              INC     HL                  
4960: 7E              LD      A,(HL)              ; read the coinage ratio byte
4961: 90              SUB     B                   ; compare the raised accumulator against it
4962: D0              RET     NC                  ; still short of a credit
4963: 7E              LD      A,(HL)              
4964: 4F              LD      C,A                 ; carry the coinage byte for crediting -- its low nibble is the credits awarded
4965: E6 F0           AND     $F0                 ; take the coins-per-credit high nibble
4967: C6 10           ADD     A,$10               ; plus one coin's worth
4969: 2B              DEC     HL                  
496A: ED 44           NEG                         ; negate
496C: 86              ADD     A,(HL)              ; pull the accumulator back, carrying the overshoot past the threshold forward
496D: 77              LD      (HL),A              ; store the reduced accumulator

; outside free play, fold C's low decimal digit into the packed-decimal
; credit count at 0xa986 (decimal add, clamp to 99) and repaint that
; field, then run the coin-counter pulse
awardCoinCreditThenPulseCoinCounter:
496E: 3A C0 A9        LD      A,($A9C0)           ; {hard.workRam+1C0} read the free-play flag
4971: A7              AND     A                   
4972: 20 10           JR      NZ,$4984            ; {code.pulseSlot1CoinCounter} free play -- skip crediting, just pulse the counter
4974: 79              LD      A,C                 ; take the low decimal digit of the award
4975: E6 0F           AND     $0F                 
4977: 21 86 A9        LD      HL,$A986            ; point at the packed-decimal credit count
497A: 86              ADD     A,(HL)              ; add the digit in
497B: 27              DAA                         ; decimal-adjust the sum
497C: 77              LD      (HL),A              ; store the new credit count
497D: 30 02           JR      NC,$4981            ; {code.loc_4981} no overflow -- keep it
497F: 36 99           LD      (HL),$99            ; clamp the credit count at 99

loc_4981:
4981: CD FB 4A        CALL    $4AFB               ; {code.paintCreditCountPanel} repaint the credit panel

; drive coin slot 1's mechanical counter through one pulse for each coin
; the machine still owes it -- energise the line, release it at the half-
; way count, and take one off the debt as the pulse ends -- so a debt of
; two comes out as two separate pulses; with nothing owed it does nothing
pulseSlot1CoinCounter:
4984: 3A 81 A9        LD      A,($A981)           ; {hard.workRam+181} read how many coins slot 1 still owes its mechanical counter
4987: A7              AND     A                   
4988: C8              RET     Z                   ; nothing owed -- do nothing
4989: 21 84 A9        LD      HL,$A984            ; point at the pulse timer
498C: 7E              LD      A,(HL)              
498D: A7              AND     A                   
498E: 20 07           JR      NZ,$4997            ; {code.loc_4997} a pulse already under way -- fall through to its countdown
4990: 36 30           LD      (HL),$30            ; arm the pulse for its full length (48 frames)
4992: 3C              INC     A                   
4993: 32 0A C3        LD      ($C30A),A           ; drive the coin-counter line high
4996: C9              RET                         

loc_4997:
4997: 35              DEC     (HL)                ; count the pulse timer down one frame
4998: 28 09           JR      Z,$49A3             ; {code.loc_49a3} timer expired -- retire one coin from the debt
499A: 7E              LD      A,(HL)              
499B: FE 18           CP      $18                 ; at the half-way count (24)
499D: C0              RET     NZ                  ; not yet
499E: AF              XOR     A                   
499F: 32 0A C3        LD      ($C30A),A           ; drop the coin-counter line low again
49A2: C9              RET                         

loc_49a3:
49A3: 21 81 A9        LD      HL,$A981            ; point at the debt count
49A6: 35              DEC     (HL)                ; take one coin off it so the next pulse can start
49A7: C9              RET                         

; tail of power-on config decode + self-test: slices two bits of the
; rolled config byte into work-RAM 0xa9c4/0xa9c6, kicks the watchdog,
; drives LS259 line 1 from ROM byte 0x0c3e, tiles the character plane,
; sums the 256-byte ROM block at 0x27de and derails a tampered image into
; the frame handler, else cold-starts
finishBootSelfTestAndColdStart:
49A8: 0F              RRCA                        ; rotate the decoded configuration byte
49A9: 4F              LD      C,A                 
49AA: E6 07           AND     $07                 ; take three configuration bits
49AC: 32 C4 A9        LD      ($A9C4),A           ; {hard.workRam+1C4} store them
49AF: 79              LD      A,C                 
49B0: 0F              RRCA                        ; shift down to the next configuration bit
49B1: 0F              RRCA                        
49B2: 0F              RRCA                        
49B3: E6 01           AND     $01                 
49B5: 32 C6 A9        LD      ($A9C6),A           ; {hard.workRam+1C6} store the attract-sound enable flag
49B8: 32 00 C2        LD      ($C200),A           ; kick the watchdog
49BB: 3A 3E 0C        LD      A,($0C3E)           ; {hard.rom+C3E} take a fixed byte from the program image
49BE: 32 02 C3        LD      ($C302),A           ; drive a control-latch line from it
49C1: CD B1 00        CALL    $00B1               ; {code.tileCharPlaneWithBoxLattice} tile the character plane with the box lattice
49C4: 06 00           LD      B,$00               ; 256 bytes to sum
49C6: 21 DE 27        LD      HL,$27DE            ; point at the block to checksum
49C9: AF              XOR     A                   ; clear the running total

loc_49ca:
49CA: 86              ADD     A,(HL)              ; add this byte into the sum
49CB: 23              INC     HL                  
49CC: 10 FC           DJNZ    $49CA               ; {code.loc_49ca} over all 256 bytes
49CE: D6 C5           SUB     $C5                 ; compare the sum against its expected total (0xC5)
49D0: C4 D8 00        CALL    NZ,$00D8            ; {code.saveAccumulatorForFrameInterrupt} a tampered image derails into the frame handler
49D3: C3 EB 32        JP      $32EB               ; {code.petWatchdogThroughStartupDelayThenStartMachine} a good image cold-starts the machine and does not return

; drive one hardware output line as a train of square pulses, one pulse
; per unit of a pending count
pulseSlot2CoinCounter:
49D6: 3A 82 A9        LD      A,($A982)           ; {hard.workRam+182} read how many coins slot 2 still owes its mechanical counter
49D9: A7              AND     A                   
49DA: C8              RET     Z                   ; nothing owed -- do nothing
49DB: 21 85 A9        LD      HL,$A985            ; point at the slot-2 pulse timer
49DE: 7E              LD      A,(HL)              
49DF: A7              AND     A                   
49E0: 20 07           JR      NZ,$49E9            ; {code.loc_49e9} a pulse already running -- fall through to its countdown
49E2: 36 30           LD      (HL),$30            ; arm the pulse for its full length (48 frames)
49E4: 3C              INC     A                   
49E5: 32 0C C3        LD      ($C30C),A           ; drive the slot-2 coin-counter line high
49E8: C9              RET                         

loc_49e9:
49E9: 35              DEC     (HL)                ; count the pulse timer down one frame
49EA: 28 09           JR      Z,$49F5             ; {code.loc_49f5} timer expired -- retire one coin from the debt
49EC: 7E              LD      A,(HL)              
49ED: FE 18           CP      $18                 ; at the half-way count (24)
49EF: C0              RET     NZ                  ; not yet
49F0: AF              XOR     A                   
49F1: 32 0C C3        LD      ($C30C),A           ; drop the slot-2 line low again
49F4: C9              RET                         

loc_49f5:
49F5: 21 82 A9        LD      HL,$A982            ; point at the slot-2 debt count
49F8: 35              DEC     (HL)                ; take one coin off it so the next pulse can start
49F9: C9              RET                         

; reached only via the "wrong-glyph" derail ($19E6); the bytes run as
; harmless NOPs and stray-stack POPs. The real routine is at $4A0F.
; ---- $49FA-$4A0E: misaligned anti-tamper entry ----
49FA: EE A6 14 A5 3B 87 F1 DC D7 BF F1 DC C4 FD ED F1
4A0A: 7D A5 38 34 B9

; lay out one phase of the sequenced intro/self-test screen: stock an
; 8-byte control block at 0xA9F0 (ROM shape byte 0x3213, fixed fields,
; parked ROM pointer 0x56F1), write a fixed attribute run at 0xA400,
; colour three colour-plane rows and a small block by adding the base
; colour at 0xAD0C to fixed offsets, seed the active player's saved pen
; from its era, then tail-step the sequence sub-step; unreached by either
; tape
paintSelfTestScreenPhaseThenStepSequence:
4A0F: 3A 13 32        LD      A,($3213)           ; {hard.rom+3213} take a shape byte from the program image
4A12: 32 F0 A9        LD      ($A9F0),A           ; {hard.workRam+1F0} drop it into the head of an eight-byte display control block
4A15: 3E 00           LD      A,$00               
4A17: 32 F1 A9        LD      ($A9F1),A           ; {hard.workRam+1F1} clear the next field
4A1A: 3E FF           LD      A,$FF               
4A1C: 32 F2 A9        LD      ($A9F2),A           ; {hard.workRam+1F2} fixed field
4A1F: 3E 04           LD      A,$04               
4A21: 32 F3 A9        LD      ($A9F3),A           ; {hard.workRam+1F3} fixed field
4A24: 3E FF           LD      A,$FF               
4A26: 32 F4 A9        LD      ($A9F4),A           ; {hard.workRam+1F4} fixed field
4A29: 3E 08           LD      A,$08               
4A2B: 32 F6 A9        LD      ($A9F6),A           ; {hard.workRam+1F6} a count field
4A2E: 21 F1 56        LD      HL,$56F1            ; the script pointer 0x56F1
4A31: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} park it as the shared glyph-script cursor
4A34: 06 0D           LD      B,$0D               ; thirteen attribute cells to fill
4A36: 21 00 A4        LD      HL,$A400            ; point at the attribute run
4A39: 0E 14           LD      C,$14               ; the fill value

loc_4a3b:
4A3B: 71              LD      (HL),C              ; lay one attribute cell
4A3C: 23              INC     HL                  
4A3D: 10 FC           DJNZ    $4A3B               ; {code.loc_4a3b} fill all thirteen
4A3F: 3E 00           LD      A,$00               
4A41: 77              LD      (HL),A              ; then one blank cell -- the run continues in the shared band painter

; continue a caption's colour band from the caller's HL cursor: lay the
; caller's A over one cell, a 13-cell run of the caller's C and a 4-cell
; tail (0x0e), then fill two colour-RAM rows and six scattered colour
; cells from the base colour at 0xAD0C (each value base+offset), then seed
; the saved pen from the era and step the sequence sub-step; A/C/HL/DE
; left scratch
paintCaptionColourBandAndStepSequence:
4A42: 23              INC     HL                  
4A43: 77              LD      (HL),A              ; lay the head colour over one cell
4A44: 23              INC     HL                  
4A45: 06 0D           LD      B,$0D               ; a thirteen-cell run

loc_4a47:
4A47: 71              LD      (HL),C              ; fill each with the band colour
4A48: 23              INC     HL                  
4A49: 10 FC           DJNZ    $4A47               ; {code.loc_4a47}
4A4B: 3E 0E           LD      A,$0E               ; the tail colour
4A4D: 06 04           LD      B,$04               ; a four-cell tail

loc_4a4f:
4A4F: 77              LD      (HL),A              ; lay each tail cell
4A50: 23              INC     HL                  
4A51: 10 FC           DJNZ    $4A4F               ; {code.loc_4a4f}
4A53: 21 B1 A7        LD      HL,$A7B1            ; a tilemap address...
4A56: CB 94           RES     2,H                 ; ...folded down into colour RAM
4A58: 3A 0C AD        LD      A,($AD0C)           ; {hard.workRam+50C} read the base pen colour
4A5B: 4F              LD      C,A                 ; keep it
4A5C: 3E A0           LD      A,$A0               
4A5E: 81              ADD     A,C                 ; base plus a fixed offset
4A5F: CD 19 13        CALL    $1319               ; {code.fillCellRun} fill a colour-RAM row with it
4A62: 21 D1 A5        LD      HL,$A5D1            
4A65: CB 94           RES     2,H                 ; fold to colour RAM
4A67: 3E 20           LD      A,$20               
4A69: 81              ADD     A,C                 ; base plus a fixed offset
4A6A: CD 19 13        CALL    $1319               ; {code.fillCellRun} fill a second colour-RAM row
4A6D: 21 10 A6        LD      HL,$A610            
4A70: CB 94           RES     2,H                 ; fold to colour RAM
4A72: 3E A0           LD      A,$A0               
4A74: 81              ADD     A,C                 ; base plus an offset
4A75: 77              LD      (HL),A              ; colour one cell
4A76: 19              ADD     HL,DE               ; step one row up
4A77: 3E 20           LD      A,$20               
4A79: 81              ADD     A,C                 ; base plus an offset
4A7A: 77              LD      (HL),A              ; colour the cell above it
4A7B: 21 12 A6        LD      HL,$A612            
4A7E: CB 94           RES     2,H                 ; fold to colour RAM
4A80: 3E E0           LD      A,$E0               
4A82: 81              ADD     A,C                 ; base plus an offset
4A83: 77              LD      (HL),A              ; colour a cell
4A84: 19              ADD     HL,DE               ; step one row up
4A85: 3E 60           LD      A,$60               
4A87: 81              ADD     A,C                 ; base plus an offset
4A88: 77              LD      (HL),A              ; colour the cell above it
4A89: 21 11 A6        LD      HL,$A611            
4A8C: CB 94           RES     2,H                 ; fold to colour RAM
4A8E: 3E A0           LD      A,$A0               
4A90: 81              ADD     A,C                 ; base plus an offset
4A91: 77              LD      (HL),A              ; colour a cell
4A92: 19              ADD     HL,DE               ; step one row up
4A93: 3E 20           LD      A,$20               
4A95: 81              ADD     A,C                 ; base plus an offset
4A96: 77              LD      (HL),A              ; colour the cell above it
4A97: CD 9C 33        CALL    $339C               ; {code.setSavedPenFromEra} seed the active player's saved pen from its era
4A9A: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-step on

; step thirteen cells of the character plane on by one shape each, but
; only where a script says so, walking that script through one shared
; cursor cell that is left wherever the walk ended; two bits of one
; incoming byte set the directions independently -- the low bit reads the
; script backwards and steps the shape DOWN, the next bit takes the cells
; a row up instead of a row down
stepThirteenScriptedGlyphCells:
4A9D: 06 0D           LD      B,$0D               ; thirteen cells to step
4A9F: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} load the shared glyph-script cursor

loc_4aa2:
4AA2: 7E              LD      A,(HL)              ; read this script byte
4AA3: A7              AND     A                   
4AA4: EB              EX      DE,HL               
4AA5: 28 09           JR      Z,$4AB0             ; {code.loc_4ab0} a zero leaves this cell's shape alone
4AA7: 7E              LD      A,(HL)              ; read the plane cell's shape
4AA8: 3C              INC     A                   ; step the shape up one
4AA9: CB 41           BIT     0,C                 ; the low direction bit
4AAB: 28 02           JR      Z,$4AAF             ; {code.loc_4aaf} forward -- keep the step up
4AAD: 3D              DEC     A                   
4AAE: 3D              DEC     A                   ; backward -- step the shape down instead

loc_4aaf:
4AAF: 77              LD      (HL),A              ; write the stepped shape back

loc_4ab0:
4AB0: CB 49           BIT     1,C                 ; the row-direction bit
4AB2: 11 20 00        LD      DE,$0020            ; one row down
4AB5: 28 03           JR      Z,$4ABA             ; {code.loc_4aba} forward
4AB7: 11 E0 FF        LD      DE,$FFE0            ; or one row up

loc_4aba:
4ABA: 19              ADD     HL,DE               ; move to the next plane cell
4ABB: EB              EX      DE,HL               
4ABC: 2A F7 A9        LD      HL,($A9F7)          ; {hard.workRam+1F7} reload the script cursor
4ABF: 23              INC     HL                  ; step the script forward...
4AC0: CB 41           BIT     0,C                 ; the low direction bit
4AC2: 28 02           JR      Z,$4AC6             ; {code.loc_4ac6}
4AC4: 2B              DEC     HL                  ; ...or backward when it is set
4AC5: 2B              DEC     HL                  

loc_4ac6:
4AC6: 22 F7 A9        LD      ($A9F7),HL          ; {hard.workRam+1F7} leave the cursor where the walk ended
4AC9: 10 D7           DJNZ    $4AA2               ; {code.loc_4aa2} over all thirteen cells
4ACB: C9              RET                         

; turn the two four-bit coinage settings into the byte each coin slot's
; accept arm works from, and raise the free-play flag when either of them
; reads free play
unpackCoinage:
4ACC: 3A B1 A9        LD      A,($A9B1)           ; {hard.workRam+1B1} read the packed coinage settings
4ACF: E6 0F           AND     $0F                 ; take the low nibble -- coin slot 1's setting
4AD1: FE 0F           CP      $0F                 ; is it the free-play code?
4AD3: 20 05           JR      NZ,$4ADA            ; {code.loc_4ada}
4AD5: 21 C0 A9        LD      HL,$A9C0            
4AD8: 36 FF           LD      (HL),$FF            ; raise the free-play flag

loc_4ada:
4ADA: 21 95 4B        LD      HL,$4B95            ; point at the coinage value table
4ADD: CF              RST     $08                 ; look the setting's value up
4ADE: 32 C9 A9        LD      ($A9C9),A           ; {hard.workRam+1C9} store it as coin slot 1's ratio byte
4AE1: 3A B1 A9        LD      A,($A9B1)           ; {hard.workRam+1B1} re-read the coinage settings
4AE4: 0F              RRCA                        ; rotate the high nibble down -- coin slot 2's setting
4AE5: 0F              RRCA                        
4AE6: 0F              RRCA                        
4AE7: 0F              RRCA                        
4AE8: E6 0F           AND     $0F                 ; isolate that nibble
4AEA: FE 0F           CP      $0F                 ; free-play code?
4AEC: 20 05           JR      NZ,$4AF3            ; {code.loc_4af3}
4AEE: 21 C0 A9        LD      HL,$A9C0            
4AF1: 36 FF           LD      (HL),$FF            ; raise the same free-play flag

loc_4af3:
4AF3: 21 95 4B        LD      HL,$4B95            ; point at the coinage value table
4AF6: CF              RST     $08                 ; look the setting's value up
4AF7: 32 CC A9        LD      ($A9CC),A           ; {hard.workRam+1CC} store it as coin slot 2's ratio byte
4AFA: C9              RET                         

; set the pen colour, the destination cell and the source byte, then paint
; them through the packed-digit painter; every one of the three is fixed
; here, so a caller chooses none of them
paintCreditCountPanel:
4AFB: 0E 10           LD      C,$10               ; select the panel pen colour
4AFD: 11 7F A4        LD      DE,$A47F            ; the cell the first digit lands in
4B00: 21 86 A9        LD      HL,$A986            ; read the packed-decimal credit count
4B03: CD 81 0D        CALL    $0D81               ; {code.paintTwoUnsuppressedDigitsFromByte} paint its two digits
4B06: C9              RET                         

; ---- $4B07-$4B18: data ----
4B07: 2A 41 AB 7D AC 2F 87 87 ED 6A 22 41 AB ED 5F 85
4B17: AC C9

; step the sequence's inner sub-step on, folding a block of the program
; image on the way; a total that does not match advances the outer phase
; instead, which derails the sequence rather than halting it
stepSequenceUnderChecksum:
4B19: 11 CC 0B        LD      DE,$0BCC            ; point at the program block to sum
4B1C: 01 89 00        LD      BC,$0089            ; 256 bytes, starting the total at 0x89
4B1F: 3A 50 1A        LD      A,($1A50)           ; {hard.rom+1A50} read the expected total from the program image
4B22: 67              LD      H,A                 ; keep it

loc_4b23:
4B23: 1A              LD      A,(DE)              ; take a block byte
4B24: 81              ADD     A,C                 ; fold it into the running total
4B25: 4F              LD      C,A                 
4B26: 13              INC     DE                  
4B27: 10 FA           DJNZ    $4B23               ; {code.loc_4b23} over all 256 bytes
4B29: 94              SUB     H                   ; compare against the expected total
4B2A: C4 11 0F        CALL    NZ,$0F11            ; {code.advanceSequencePhase} a mismatch advances the outer sequence phase -- derailing the sequence
4B2D: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-step on

; copy three tilemap cells into three two-byte keeps, reading each cell
; twice because its two planes sit a fixed distance apart
copyThreeTilemapCellsFromBothPlanes:
4B30: 21 1B 0D        LD      HL,$0D1B            ; point at a table of three address records
4B33: 06 03           LD      B,$03               ; three cells to copy

loc_4b35:
4B35: 5E              LD      E,(HL)              ; read the source address low...
4B36: 23              INC     HL                  
4B37: 56              LD      D,(HL)              ; ...and high
4B38: 23              INC     HL                  
4B39: 1A              LD      A,(DE)              ; read the cell on the first plane
4B3A: 08              EX      AF,AF'              
4B3B: 3E 04           LD      A,$04               
4B3D: 82              ADD     A,D                 ; step the source high byte to the other plane -- a fixed distance apart
4B3E: 57              LD      D,A                 
4B3F: 1A              LD      A,(DE)              ; read the same cell on the second plane
4B40: 5E              LD      E,(HL)              ; read the destination keep low...
4B41: 23              INC     HL                  
4B42: 56              LD      D,(HL)              ; ...and high
4B43: 23              INC     HL                  
4B44: 12              LD      (DE),A              ; store the second-plane byte
4B45: 1C              INC     E                   ; next byte of the keep -- low half only, so it wraps in its own page
4B46: 08              EX      AF,AF'              
4B47: 12              LD      (DE),A              ; store the first-plane byte beside it
4B48: 10 EB           DJNZ    $4B35               ; {code.loc_4b35} over all three cells
4B4A: C9              RET                         

; draw the next pseudo-random byte: advance the seventeen-byte shift
; register one place, fill the vacated head with the exclusive-or of two
; taps, and hand back that feedback plus the frame counter, so two draws
; at different moments differ even where the register has not moved
drawRandomByte:
4B4B: D9              EXX                         
4B4C: 21 3F AB        LD      HL,$AB3F            ; source: the register's second-from-top byte
4B4F: 11 40 AB        LD      DE,$AB40            ; destination: the top byte
4B52: 01 10 00        LD      BC,$0010            ; sixteen bytes to move
4B55: ED B8           LDDR                        ; shift the whole shift register one place along
4B57: 21 40 AB        LD      HL,$AB40            
4B5A: 3A 37 AB        LD      A,($AB37)           ; {hard.workRam+337} read one feedback tap
4B5D: AE              XOR     (HL)                ; exclusive-or it with the other tap
4B5E: 32 30 AB        LD      ($AB30),A           ; {hard.workRam+330} drop the feedback into the vacated head
4B61: 21 80 A9        LD      HL,$A980            
4B64: 86              ADD     A,(HL)              ; add the free-running frame counter to the result
4B65: D9              EXX                         
4B66: C9              RET                         

; copy a fixed seventeen-byte run of program space at 0x4B84 into the
; random register block, then check the image that run came out of: three
; bytes taken from two fixed words of program space are added to one
; constant, and any total but zero means the program space being read is
; not the one the constant was picked for -- on that outcome control
; transfers to 0x6000, outside the image, so it raises rather than
; running. The copy is unconditional and COMPLETE before the check runs,
; so nothing this entry wrote is gated by it
seedRandomRegister:
4B67: 21 84 4B        LD      HL,$4B84            ; point at the seventeen seed bytes in program space
4B6A: 11 30 AB        LD      DE,$AB30            ; point at the random register
4B6D: 01 11 00        LD      BC,$0011            ; seventeen bytes to copy
4B70: ED B0           LDIR                        ; seed the random register from the fixed run
4B72: DD 2A 6D 08     LD      IX,($086D)          ; {hard.rom+86D} take a word of program space for the image check
4B76: 2A 70 08        LD      HL,($0870)          ; {hard.rom+870} take a second word of program space
4B79: DD 7D           LD      A,IXL               ; start the check total with the first word's low byte
4B7B: DD 84           ADD     A,IXH               ; add the first word's high byte
4B7D: 85              ADD     A,L                 ; add the second word's low byte
4B7E: C6 44           ADD     A,$44               ; add the fixed bias -- a sound program image brings the total to zero
4B80: C2 00 60        JP      NZ,$6000            ; any other total: this is not the image the constant was picked for, so jump outside the image -- never taken on a good board
4B83: C9              RET                         

; ---- $4B84-$4BA4: data ----
4B84: FF 05 F6 80 32 17 9C C9 DD 21 74 98 FD BF 24 AE
4B94: 46 01 02 03 04 05 06 07 11 13 15 21 22 24 31 33
4BA4: 01

; copy forty bytes of program space into the five-entry high-score table,
; which is the only way that table is ever initialised
loadDefaultHighScores:
4BA5: 21 B1 4B        LD      HL,$4BB1            ; point at the default high-score block in program space
4BA8: 11 08 AB        LD      DE,$AB08            ; point at the five-entry high-score table
4BAB: 01 28 00        LD      BC,$0028            ; forty bytes -- the whole table
4BAE: ED B0           LDIR                        ; stamp the default high scores in -- the only thing that ever fills the table
4BB0: C9              RET                         

; ---- $4BB1-$4BD8: data ----
4BB1: 00 00 00 01 7C 11 68 F1 01 00 88 00 3B 11 A5 F1
4BC1: 02 60 84 00 38 11 FD F1 03 20 65 00 68 11 68 F1
4BD1: 04 00 43 00 BF 11 A5 F1

; a bare transfer to 0x08AE and no return; no cell is read or written and
; no register moves
trampolineToSelectFoldBlock:
4BD9: C3 AE 08        JP      $08AE               ; {code.selectFoldBlock} hand on to the routine that picks a program block to fold

; paint five labelled numeric readouts up the tile plane: seat each of
; five source records (0xab08, stride 8), its tile-plane cursor cell
; (0xa711, stride 2) and its pen colour, then hand to the column painter
; paintLabelledNumericReadoutColumn; writes tile/colour cells
; 0xa0f1-0xa719
paintFiveLabelledNumericReadouts:
4BDC: 21 08 AB        LD      HL,$AB08            ; first score record
4BDF: 11 11 A7        LD      DE,$A711            ; its cursor cell in the tile plane
4BE2: 0E 14           LD      C,$14               ; pen colour for this readout
4BE4: CD 1F 4C        CALL    $4C1F               ; {code.paintLabelledNumericReadoutColumn} paint it as an upward column
4BE7: 21 10 AB        LD      HL,$AB10            ; second score record
4BEA: 11 13 A7        LD      DE,$A713            ; its cursor cell
4BED: 0E 16           LD      C,$16               ; pen colour
4BEF: CD 1F 4C        CALL    $4C1F               ; {code.paintLabelledNumericReadoutColumn} paint it
4BF2: 21 18 AB        LD      HL,$AB18            ; third score record
4BF5: 11 15 A7        LD      DE,$A715            ; its cursor cell
4BF8: 0E 12           LD      C,$12               ; pen colour
4BFA: CD 1F 4C        CALL    $4C1F               ; {code.paintLabelledNumericReadoutColumn} paint it
4BFD: 21 20 AB        LD      HL,$AB20            ; fourth score record
4C00: 11 17 A7        LD      DE,$A717            ; its cursor cell
4C03: 0E 15           LD      C,$15               ; pen colour
4C05: CD 1F 4C        CALL    $4C1F               ; {code.paintLabelledNumericReadoutColumn} paint it
4C08: 21 28 AB        LD      HL,$AB28            ; fifth score record
4C0B: 11 19 A7        LD      DE,$A719            ; its cursor cell
4C0E: 0E 13           LD      C,$13               ; pen colour
4C10: CD 1F 4C        CALL    $4C1F               ; {code.paintLabelledNumericReadoutColumn} paint it
4C13: C9              RET                         

; ---- $4C14-$4C1E: data ----
4C14: 73 A6 14 7E 29 F8 96 5D F3 13 B9

; paint a labelled numeric readout as one upward tile-plane column: a
; table-indexed three-tile pictogram (source lead byte x3 into 0x4cb4), a
; six-digit field, then a three-tile suffix, each cell paired into the
; colour plane with the caller's pen colour
paintLabelledNumericReadoutColumn:
4C1F: E5              PUSH    HL                  ; save the source record pointer
4C20: 7E              LD      A,(HL)              ; read the record's lead byte
4C21: 87              ADD     A,A                 ; times two
4C22: 86              ADD     A,(HL)              ; times three -- three tiles per pictogram, so the lead byte selects the pictogram
4C23: 21 B4 4C        LD      HL,$4CB4            ; point at the pictogram table
4C26: CF              RST     $08                 ; fetch the indexed pictogram tile
4C27: 12              LD      (DE),A              ; stamp the tile
4C28: CB 92           RES     2,D                 ; drop to the paired colour cell
4C2A: 79              LD      A,C                 ; pen colour
4C2B: 12              LD      (DE),A              ; write the colour
4C2C: CB D2           SET     2,D                 ; back to the tile cell
4C2E: 23              INC     HL                  ; next pictogram tile
4C2F: E7              RST     $20                 ; step the cursor up one cell
4C30: 7E              LD      A,(HL)              ; read the tile
4C31: 12              LD      (DE),A              ; stamp it
4C32: CB 92           RES     2,D                 ; drop to the colour cell
4C34: 79              LD      A,C                 ; pen colour
4C35: 12              LD      (DE),A              ; write the colour
4C36: CB D2           SET     2,D                 ; back to the tile cell
4C38: 23              INC     HL                  ; next pictogram tile
4C39: E7              RST     $20                 ; step the cursor up one cell
4C3A: 7E              LD      A,(HL)              ; read the third pictogram tile
4C3B: 12              LD      (DE),A              ; stamp it
4C3C: CB 92           RES     2,D                 ; drop to the colour cell
4C3E: 79              LD      A,C                 ; pen colour
4C3F: 12              LD      (DE),A              ; write the colour
4C40: CB D2           SET     2,D                 ; back to the tile cell
4C42: 21 80 FF        LD      HL,$FF80            ; drop the cursor 0x80 down to the six-digit field
4C45: 19              ADD     HL,DE               
4C46: EB              EX      DE,HL               
4C47: E1              POP     HL                  ; restore the source record pointer
4C48: 23              INC     HL                  ; step the source past its lead bytes to the digit field
4C49: 23              INC     HL                  
4C4A: 23              INC     HL                  
4C4B: CD 73 0D        CALL    $0D73               ; {code.paintSixDigitFieldSuppressingLeadingZeros} paint the six-digit score field, leading zeros suppressed
4C4E: E5              PUSH    HL                  ; save the cursor
4C4F: 21 A0 FF        LD      HL,$FFA0            ; drop the cursor 0x60 down to the suffix
4C52: 19              ADD     HL,DE               
4C53: EB              EX      DE,HL               
4C54: E1              POP     HL                  ; restore the source pointer
4C55: 23              INC     HL                  ; step the source to the suffix bytes
4C56: 23              INC     HL                  
4C57: 23              INC     HL                  
4C58: 7E              LD      A,(HL)              ; read the first suffix tile
4C59: 12              LD      (DE),A              ; stamp it
4C5A: CB 92           RES     2,D                 ; drop to the colour cell
4C5C: 79              LD      A,C                 ; pen colour
4C5D: 12              LD      (DE),A              ; write the colour
4C5E: CB D2           SET     2,D                 ; back to the tile cell
4C60: 23              INC     HL                  ; next suffix tile
4C61: E7              RST     $20                 ; step the cursor up one cell
4C62: 7E              LD      A,(HL)              ; read the tile
4C63: 12              LD      (DE),A              ; stamp it
4C64: CB 92           RES     2,D                 ; drop to the colour cell
4C66: 79              LD      A,C                 ; pen colour
4C67: 12              LD      (DE),A              ; write the colour
4C68: CB D2           SET     2,D                 ; back to the tile cell
4C6A: 23              INC     HL                  ; next suffix tile
4C6B: E7              RST     $20                 ; step the cursor up one cell
4C6C: 7E              LD      A,(HL)              ; read the third suffix tile
4C6D: 12              LD      (DE),A              ; stamp it
4C6E: CB 92           RES     2,D                 ; drop to the colour cell
4C70: 79              LD      A,C                 ; pen colour
4C71: 12              LD      (DE),A              ; write the colour
4C72: CB D2           SET     2,D                 ; back to the tile cell
4C74: C9              RET                         

; sequence arm (computed-dispatch entry 3 of the table at 0x0F29): blank a
; fixed character-cell run, copy the active player's saved 16-byte context
; block into the live block at 0xAD00, step the sequence sub-index; when
; play is active it also posts the round number (cmd 6) and lives-less-one
; (cmd 5) to the command ring and folds a fixed program span (0x5B50, 256
; bytes) into an XOR whose low bit less one drives the picture-enable
; latch 0xC308 -- a tamper guard
loadActivePlayerContextAndPostRoundHud:
4C75: CD D2 07        CALL    $07D2               ; {code.blankFourteenCharCells} blank the fixed run of character cells
4C78: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player flag
4C7B: A7              AND     A                   ; test it
4C7C: 21 10 AD        LD      HL,$AD10            ; default to player one's saved context block
4C7F: 28 03           JR      Z,$4C84             ; {code.loc_4c84} player one: keep it
4C81: 21 20 AD        LD      HL,$AD20            ; otherwise player two's saved context block

loc_4c84:
4C84: 11 00 AD        LD      DE,$AD00            ; point at the live context block
4C87: 01 10 00        LD      BC,$0010            ; sixteen bytes -- the whole context
4C8A: ED B0           LDIR                        ; copy the saved context into the live block
4C8C: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} read the play-active flag
4C8F: A7              AND     A                   ; test it
4C90: CA 1A 0F        JP      Z,$0F1A             ; {code.advanceSequenceSubStep} not in play: just step the sequence sub-index and return
4C93: 3A 01 AD        LD      A,($AD01)           ; {hard.workRam+501} read the round number
4C96: 16 06           LD      D,$06               ; command 6 -- the round number
4C98: 5F              LD      E,A                 ; as its argument
4C99: FF              RST     $38                 ; post it to the command ring
4C9A: 3A 00 AD        LD      A,($AD00)           ; {hard.workRam+500} read the lives-remaining count
4C9D: 3D              DEC     A                   ; less one
4C9E: 16 05           LD      D,$05               ; command 5 -- lives less one
4CA0: 5F              LD      E,A                 ; as its argument
4CA1: FF              RST     $38                 ; post it to the command ring
4CA2: 06 00           LD      B,$00               ; two hundred fifty-six bytes to fold
4CA4: 21 50 5B        LD      HL,$5B50            ; point at the fixed program span to fold
4CA7: 97              SUB     A                   ; start the fold at zero

loc_4ca8:
4CA8: AE              XOR     (HL)                ; fold the next byte into the running total
4CA9: 23              INC     HL                  
4CAA: 10 FC           DJNZ    $4CA8               ; {code.loc_4ca8} loop over the whole span
4CAC: C6 FF           ADD     A,$FF               ; less one
4CAE: 32 08 C3        LD      ($C308),A           ; drive the picture-enable latch with it -- a tampered image blanks the picture
4CB1: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index and return

; ---- $4CB4-$4CC2: data ----
4CB4: 96 ED DC 9B 3B 87 CD D7 87 F3 DC C4 7F DC C4

; file the active player's finished score into the five-record high-score
; board: walk the standing scores top-down comparing each (isScoreBelow)
; to find the first the new score is not below, slide the records beneath
; down one slot (lddr), write the new score with blank 0xf1 name-cell
; sentinels, look up its initial-glyph row pointer, and renumber the rank
; column 0..4; carry returns clear when filed, set when the score beat
; none
fileScoreIntoHighScoreTable:
4CC3: 21 0B AB        LD      HL,$AB0B            ; point at the top standing score's high byte
4CC6: 06 05           LD      B,$05               ; five records to consider
4CC8: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player flag
4CCB: A7              AND     A                   ; test it
4CCC: 11 35 AD        LD      DE,$AD35            ; default to player one's finished score
4CCF: 28 03           JR      Z,$4CD4             ; {code.loc_4cd4} player one: keep it
4CD1: 11 38 AD        LD      DE,$AD38            ; otherwise player two's finished score

loc_4cd4:
4CD4: E5              PUSH    HL                  ; save the standing pointer
4CD5: D5              PUSH    DE                  ; save the score pointer
4CD6: CD 2B 4D        CALL    $4D2B               ; {code.isScoreBelow} is the new score below this standing score?
4CD9: 30 09           JR      NC,$4CE4            ; {code.loc_4ce4} not below: this is its slot
4CDB: D1              POP     DE                  ; restore the score pointer
4CDC: E1              POP     HL                  ; restore the standing pointer
4CDD: 3E 08           LD      A,$08               ; record stride is eight
4CDF: CF              RST     $08                 ; walk the standing pointer down one record
4CE0: 10 F2           DJNZ    $4CD4               ; {code.loc_4cd4} try the next standing score
4CE2: 37              SCF                         ; beat none -- set carry to say so
4CE3: C9              RET                         

loc_4ce4:
4CE4: 05              DEC     B                   ; how many records lie below the slot
4CE5: 28 3F           JR      Z,$4D26             ; {code.loc_4d26} slot is the bottom record: nothing to slide
4CE7: 21 27 AB        LD      HL,$AB27            ; last byte of the block to slide
4CEA: 11 2F AB        LD      DE,$AB2F            ; last byte of its destination one slot down
4CED: 78              LD      A,B                 ; record count
4CEE: 87              ADD     A,A                 ; times two
4CEF: 87              ADD     A,A                 ; times four
4CF0: 87              ADD     A,A                 ; times eight -- eight cells per record
4CF1: 4F              LD      C,A                 ; that many bytes
4CF2: 06 00           LD      B,$00               
4CF4: ED B8           LDDR                        ; slide the lower records down one slot
4CF6: EB              EX      DE,HL               ; point at the freed slot

loc_4cf7:
4CF7: 2B              DEC     HL                  ; back up one cell
4CF8: 36 F1           LD      (HL),$F1            ; blank a name cell
4CFA: 2B              DEC     HL                  ; back up one cell
4CFB: 36 F1           LD      (HL),$F1            ; blank a name cell
4CFD: 2B              DEC     HL                  ; back up one cell
4CFE: 36 F1           LD      (HL),$F1            ; blank a name cell
4D00: 22 91 A9        LD      ($A991),HL          ; {hard.workRam+191} remember where the three name cells start
4D03: 2B              DEC     HL                  ; back up to the score field
4D04: D1              POP     DE                  ; restore the finished-score pointer
4D05: 01 03 00        LD      BC,$0003            ; three score bytes
4D08: EB              EX      DE,HL               ; make the finished score the copy source
4D09: ED B8           LDDR                        ; copy the new score into the slot
4D0B: 1A              LD      A,(DE)              ; read the rank byte the copy uncovered
4D0C: E1              POP     HL                  ; discard the saved standing pointer
4D0D: 21 31 A5        LD      HL,$A531            ; point at the initial-glyph row table
4D10: 87              ADD     A,A                 ; rank times two -- two bytes per entry
4D11: CF              RST     $08                 ; look up this rank's initial-glyph row pointer
4D12: 22 93 A9        LD      ($A993),HL          ; {hard.workRam+193} remember it
4D15: 21 08 AB        LD      HL,$AB08            ; point at the high-score table base
4D18: 11 08 00        LD      DE,$0008            ; record stride is eight
4D1B: 06 05           LD      B,$05               ; five records
4D1D: AF              XOR     A                   ; start the rank at zero

loc_4d1e:
4D1E: 77              LD      (HL),A              ; write this record's rank number
4D1F: 19              ADD     HL,DE               ; next record
4D20: 3C              INC     A                   ; next rank
4D21: 10 FB           DJNZ    $4D1E               ; {code.loc_4d1e} renumber all five ranks top to bottom
4D23: 37              SCF                         ; set carry
4D24: 3F              CCF                         ; then clear it -- carry clear says the score was filed
4D25: C9              RET                         

loc_4d26:
4D26: 21 2F AB        LD      HL,$AB2F            ; slot is the bottom record: point at its last byte
4D29: 18 CC           JR      $4CF7               ; {code.loc_4cf7} go blank the name cells and write the score -- nothing to slide

; answer whether one three-byte score is below another, both read most
; significant byte first from the two addresses given and DOWNWARD, all
; three equal counting as not below; nothing is written -- the answer,
; mirrored into carry for the caller to branch on, is the whole product
isScoreBelow:
4D2B: 0E 03           LD      C,$03               ; three bytes to compare, most significant first

loc_4d2d:
4D2D: 1A              LD      A,(DE)              ; read the candidate byte
4D2E: BE              CP      (HL)                ; compare with the standing byte
4D2F: D8              RET     C                   ; candidate lower: below -- return with carry set
4D30: 20 05           JR      NZ,$4D37            ; {code.loc_4d37} they differ but candidate is higher: not below
4D32: 1B              DEC     DE                  ; same so far: step both down to the next byte
4D33: 2B              DEC     HL                  
4D34: 0D              DEC     C                   ; one fewer byte
4D35: 20 F6           JR      NZ,$4D2D            ; {code.loc_4d2d} compare the next byte

loc_4d37:
4D37: 37              SCF                         ; set carry
4D38: 3F              CCF                         ; then clear it -- carry clear says not below
4D39: C9              RET                         

; step a three-place base-sixty tick counter at 0xAD05, carrying into the
; next place only while a place rolls over; only on a full roll-over count
; down the reload timer at 0xA9D7, and each time it fires rearm it from
; 0xA9D6, climb the escalation rung at 0xACC0 one step (held at 15), and
; apply that rung's tuning row
escalateDifficultyRungOnCounterWrap:
4D3A: 21 05 AD        LD      HL,$AD05            ; point at the ones place of the base-sixty tick counter
4D3D: CD 67 4D        CALL    $4D67               ; {code.advanceSexagesimalDigit} step it on by one
4D40: D8              RET     C                   ; no roll-over: the whole pass ends here
4D41: 2C              INC     L                   ; move to the next place
4D42: CD 67 4D        CALL    $4D67               ; {code.advanceSexagesimalDigit} step it on by one
4D45: 38 04           JR      C,$4D4B             ; {code.loc_4d4b} it did not roll over: skip the top place
4D47: 2C              INC     L                   ; move to the top place
4D48: CD 67 4D        CALL    $4D67               ; {code.advanceSexagesimalDigit} step it on by one

loc_4d4b:
4D4B: 21 D7 A9        LD      HL,$A9D7            ; point at the reload timer
4D4E: 7E              LD      A,(HL)              ; read it
4D4F: A7              AND     A                   ; test it
4D50: C8              RET     Z                   ; timer already spent: nothing more to do
4D51: 35              DEC     (HL)                ; count the timer down one
4D52: C0              RET     NZ                  ; not yet zero: done
4D53: 3A D6 A9        LD      A,($A9D6)           ; {hard.workRam+1D6} read the reload value
4D56: 77              LD      (HL),A              ; rearm the timer with it
4D57: 3A C0 AC        LD      A,($ACC0)           ; {hard.workRam+4C0} read the difficulty-escalation rung
4D5A: 3C              INC     A                   ; climb one step
4D5B: FE 10           CP      $10                 ; past the top rung?
4D5D: 38 02           JR      C,$4D61             ; {code.loc_4d61} no: keep it
4D5F: 3E 0F           LD      A,$0F               ; clamp it to the top rung -- fifteen

loc_4d61:
4D61: 32 C0 AC        LD      ($ACC0),A           ; {hard.workRam+4C0} store the escalation rung
4D64: C3 9A 1A        JP      $1A9A               ; {code.applyEraRungSettings} apply this rung's tuning row and return

; advance one two-digit packed-decimal place of a base-sixty counter,
; storing the stepped value before testing it and replacing it with zero
; once it reaches sixty; the answer comes back in the carry, inverted, so
; a set carry means it did NOT wrap
advanceSexagesimalDigit:
4D67: 7E              LD      A,(HL)              ; read the packed-decimal place
4D68: C6 01           ADD     A,$01               ; add one
4D6A: 27              DAA                         ; decimal-correct the result
4D6B: 77              LD      (HL),A              ; store the stepped value
4D6C: FE 60           CP      $60                 ; reached sixty?
4D6E: D8              RET     C                   ; no: return with carry set -- did not roll over
4D6F: 36 00           LD      (HL),$00            ; rolled over: store zero
4D71: C9              RET                         

; ---- $4D72-$4DDD: data ----
4D72: 4F 3A 30 AD A7 C8 11 83 A7 79 FE 07 38 02 3E 06
4D82: A7 28 0C 06 09 0E 18 08 CD AF 4D 08 3D 20 F8 01
4D92: 10 F1 21 DD 59 19 30 05 CD CF 4D 18 F5 06 00 21
4DA2: 11 07 97 AE 23 10 FC C6 19 C2 B1 4B C9 78 C6 03
4DB2: 12 3D 1B 12 E7 78 12 3C 13 12 21 00 FC 19 E7 71
4DC2: 2B 71 7D C6 20 6F 30 01 24 71 23 71 C9 EB 70 2B
4DD2: 36 F1 CB 94 71 23 71 CB D4 EB E7 C9

; award an extra life when the active player's score reaches one of the
; bonus marks, once per mark. It returns immediately unless PLAY_ACTIVE is
; set; picks one of the two mark tables at ROM 0x4E1B and 0x4E30 on bit 0
; of the settings byte at 0xA9C3; and searches the chosen table with cpir
; for an EXACT match on the top byte of the active player's six-digit
; packed-decimal score -- 0xAD35 or 0xAD38, selected on ACTIVE_PLAYER --
; so only a score standing on a mark matches, never one compared against
; it. Bit 0 of 0xAD03 makes the award one-shot: a match while that bit is
; already set does nothing, and the first call that does not match clears
; it again. On a fresh match it sets the bit, increments LIVES_REMAINING,
; posts ring command 5 with the count from BEFORE the increment, and tail-
; jumps into requestBonusLifeSound for the sound, so
; requestBonusLifeSound's ret returns to this routine's caller. Its one
; call site in the image is serviceRoundThenResolvePlayerState, the round
; engine's straight-line block of calls, which reaches it once per
; dispatch of that block
awardBonusLifeAtScoreMark:
4DDE: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} read the play-active flag
4DE1: A7              AND     A                   ; test it
4DE2: C8              RET     Z                   ; not in play: award nothing
4DE3: 3A C3 A9        LD      A,($A9C3)           ; {hard.workRam+1C3} read the bonus-life setting
4DE6: E6 01           AND     $01                 ; keep bit 0 -- picks which mark list
4DE8: 21 1B 4E        LD      HL,$4E1B            ; default to the first mark list
4DEB: 28 03           JR      Z,$4DF0             ; {code.loc_4df0} bit 0 clear: use it
4DED: 21 30 4E        LD      HL,$4E30            ; otherwise the second mark list

loc_4df0:
4DF0: 4E              LD      C,(HL)              ; read the list length into the count
4DF1: 06 00           LD      B,$00               
4DF3: 23              INC     HL                  ; step past the length byte to the marks
4DF4: 3A 32 AD        LD      A,($AD32)           ; {hard.workRam+532} read the active-player flag
4DF7: A7              AND     A                   ; test it
4DF8: 3A 35 AD        LD      A,($AD35)           ; {hard.workRam+535} default to player one's score top byte
4DFB: 28 03           JR      Z,$4E00             ; {code.loc_4e00} player one: keep it
4DFD: 3A 38 AD        LD      A,($AD38)           ; {hard.workRam+538} otherwise player two's score top byte

loc_4e00:
4E00: ED B1           CPIR                        ; scan the list for an exact match on that top byte
4E02: 21 03 AD        LD      HL,$AD03            ; point at the bonus-life latch
4E05: 20 11           JR      NZ,$4E18            ; {code.loc_4e18} no match: go clear the one-shot latch below
4E07: CB 46           BIT     0,(HL)              ; matched: is the latch already set?
4E09: C0              RET     NZ                  ; already awarded this mark: do nothing
4E0A: CB C6           SET     0,(HL)              ; set the one-shot latch
4E0C: 21 00 AD        LD      HL,$AD00            ; point at the lives-remaining count
4E0F: 7E              LD      A,(HL)              ; read it
4E10: 34              INC     (HL)                ; add one life
4E11: 16 05           LD      D,$05               ; command 5 -- the award
4E13: 5F              LD      E,A                 ; argument is the count before the increment
4E14: FF              RST     $38                 ; post it to the command ring
4E15: C3 05 58        JP      $5805               ; {code.requestBonusLifeSound} request the bonus-life sound and return through it

loc_4e18:
4E18: CB 86           RES     0,(HL)              ; no match: clear the one-shot latch
4E1A: C9              RET                         

; ---- $4E1B-$4E4E: data ----
4E1B: 14 01 06 11 16 21 26 31 36 41 46 51 56 61 66 71
4E2B: 76 81 86 91 96 11 02 08 14 20 26 32 38 44 50 56
4E3B: 62 68 74 80 86 92 98 6F A6 14 88 57 A5 BF 34 D7
4E4B: F1 9B F1 B9

; dispatch one round's per-frame collision pass by ERA_INDEX (0xad04): era
; 4 to dispatchEra4CollisionByFrameParity, era 1 to
; splitCollisionWorkByFrameParity, every other era split on FRAME_TICK's
; (0xa980) low bit to dispatchShotSweepByMotherShipArmed (odd) else
; runAllCollisionSweepsThisFrame (even); reached from the substep-7
; dispatcher 0x1199
dispatchCollisionPassByEra:
4E4F: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era of play
4E52: FE 04           CP      $04                 ; era 4?
4E54: CA 2A 4F        JP      Z,$4F2A             ; {code.dispatchEra4CollisionByFrameParity} yes: take the era-4 collision path
4E57: 3D              DEC     A                   ; era 1? -- test by decrement
4E58: CA BC 4E        JP      Z,$4EBC             ; {code.splitCollisionWorkByFrameParity} yes: take the era-1 collision path
4E5B: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame tick
4E5E: E6 01           AND     $01                 ; its low bit -- frame parity
4E60: C2 35 4F        JP      NZ,$4F35            ; {code.dispatchShotSweepByMotherShipArmed} odd frame: run the shot sweeps; even frame runs the full pass below

; run one round's collision-and-destruction pass: sweep the player's shots
; against targets, then the player against a run of objects, then --
; picked by whether the mother-ship is armed -- either the player-vs-slots
; contact sweep plus the mother-ship mutual-kill box, or a wider player-
; vs-slots sweep; then a three-target attacker sweep and a final mark of
; objects touching the player. The object/slot cursor pair threads through
; DE/IY across the chain, each stage continuing where the last left off
runAllCollisionSweepsThisFrame:
4E63: CD 5D 4F        CALL    $4F5D               ; {code.stagePlayerShotSweepAgainstTargetsAndRun} sweep the player's shots against their targets
4E66: 06 04           LD      B,$04               ; four objects
4E68: 11 10 A8        LD      DE,$A810            ; point the record cursor at the object run
4E6B: FD 21 12 AA     LD      IY,$AA12            ; point the entry cursor at the object run
4E6F: 2E 05           LD      L,$05               ; collision box near bound
4E71: 26 0B           LD      H,$0B               ; collision box far bound
4E73: CD 85 51        CALL    $5185               ; {code.destroyPlayerAndObjectsTouchingIt} destroy the player and the objects it is touching
4E76: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} read the mother-ship-armed flag
4E79: A7              AND     A                   ; test it
4E7A: 20 1B           JR      NZ,$4E97            ; {code.loc_4e97} armed: take the wider mother-ship branch
4E7C: 06 07           LD      B,$07               ; seven slots
4E7E: 2E 07           LD      L,$07               ; collision box near bound
4E80: 26 0F           LD      H,$0F               ; collision box far bound
4E82: CD 52 51        CALL    $5152               ; {code.destroySlotsAndPlayerOnContact} destroy the slots and the player on contact
4E85: 06 03           LD      B,$03               ; three targets
4E87: 2E 06           LD      L,$06               ; collision box near bound
4E89: 26 0D           LD      H,$0D               ; collision box far bound
4E8B: CD 21 51        CALL    $5121               ; {code.destroyTargetsReachedByFixedAttacker} destroy the targets a fixed attacker has reached
4E8E: 06 01           LD      B,$01               ; one object
4E90: 2E 08           LD      L,$08               ; collision box near bound
4E92: 26 11           LD      H,$11               ; collision box far bound
4E94: C3 B3 51        JP      $51B3               ; {code.markObjectsTouchingPlayer} mark the objects touching the player and return

loc_4e97:
4E97: 06 05           LD      B,$05               ; armed branch: five slots
4E99: 2E 07           LD      L,$07               ; collision box near bound
4E9B: 26 0F           LD      H,$0F               ; collision box far bound
4E9D: CD 52 51        CALL    $5152               ; {code.destroySlotsAndPlayerOnContact} destroy the slots and the player on contact
4EA0: CD B1 50        CALL    $50B1               ; {code.ramTestPlayerVsMotherShip} the mother-ship mutual-kill box
4EA3: 06 03           LD      B,$03               ; three targets
4EA5: 11 C0 A8        LD      DE,$A8C0            ; point the record cursor at the era-object run
4EA8: FD 21 28 AA     LD      IY,$AA28            ; point the entry cursor at the era-object run
4EAC: 2E 06           LD      L,$06               ; collision box near bound
4EAE: 26 0D           LD      H,$0D               ; collision box far bound
4EB0: CD 21 51        CALL    $5121               ; {code.destroyTargetsReachedByFixedAttacker} destroy the targets a fixed attacker has reached
4EB3: 06 01           LD      B,$01               ; one object
4EB5: 2E 08           LD      L,$08               ; collision box near bound
4EB7: 26 11           LD      H,$11               ; collision box far bound
4EB9: C3 B3 51        JP      $51B3               ; {code.markObjectsTouchingPlayer} mark the objects touching the player and return

; split the per-frame collision work by frame parity: on odd frames run
; the shot-vs-target sweeps (dispatchShotSweepByMotherShipArmed); on even
; frames run the player-vs-object collision chain, adding the mother-ship
; mutual-kill check (ramTestPlayerVsMotherShip) only while the mother ship
; is armed
splitCollisionWorkByFrameParity:
4EBC: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame tick
4EBF: E6 01           AND     $01                 ; its low bit -- frame parity
4EC1: C2 35 4F        JP      NZ,$4F35            ; {code.dispatchShotSweepByMotherShipArmed} odd frame: run the shot sweeps and return
4EC4: CD 7E 4F        CALL    $4F7E               ; {code.destroyFixedTargetHitByShots} even frame: destroy the fixed target the shots have reached
4EC7: 06 04           LD      B,$04               ; four objects
4EC9: 11 10 A8        LD      DE,$A810            ; point the record cursor at the object run
4ECC: FD 21 12 AA     LD      IY,$AA12            ; point the entry cursor at the object run
4ED0: 2E 05           LD      L,$05               ; collision box near bound
4ED2: 26 0B           LD      H,$0B               ; collision box far bound
4ED4: CD 85 51        CALL    $5185               ; {code.destroyPlayerAndObjectsTouchingIt} destroy the player and the objects it is touching
4ED7: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} read the mother-ship-armed flag
4EDA: A7              AND     A                   ; test it
4EDB: 20 25           JR      NZ,$4F02            ; {code.loc_4f02} armed: take the mother-ship branch
4EDD: 06 07           LD      B,$07               ; seven slots
4EDF: 2E 07           LD      L,$07               ; collision box near bound
4EE1: 26 0F           LD      H,$0F               ; collision box far bound
4EE3: CD 52 51        CALL    $5152               ; {code.destroySlotsAndPlayerOnContact} destroy the slots and the player on contact
4EE6: CD 7E 50        CALL    $507E               ; {code.destroyFixedTargetReachedByPlayer} destroy the fixed target the player has reached
4EE9: 06 01           LD      B,$01               ; one object
4EEB: 11 E0 A8        LD      DE,$A8E0            ; point the record cursor at the second era-object run
4EEE: FD 21 2C AA     LD      IY,$AA2C            ; point the entry cursor at the second era-object run
4EF2: 2E 05           LD      L,$05               ; collision box near bound
4EF4: 26 0B           LD      H,$0B               ; collision box far bound
4EF6: CD 85 51        CALL    $5185               ; {code.destroyPlayerAndObjectsTouchingIt} destroy the player and the objects it is touching
4EF9: 06 01           LD      B,$01               ; one object
4EFB: 2E 08           LD      L,$08               ; collision box near bound
4EFD: 26 11           LD      H,$11               ; collision box far bound
4EFF: C3 B3 51        JP      $51B3               ; {code.markObjectsTouchingPlayer} mark the objects touching the player and return

loc_4f02:
4F02: 06 05           LD      B,$05               ; armed branch: five slots
4F04: 2E 07           LD      L,$07               ; collision box near bound
4F06: 26 0F           LD      H,$0F               ; collision box far bound
4F08: CD 52 51        CALL    $5152               ; {code.destroySlotsAndPlayerOnContact} destroy the slots and the player on contact
4F0B: CD B1 50        CALL    $50B1               ; {code.ramTestPlayerVsMotherShip} the mother-ship mutual-kill box
4F0E: CD 7E 50        CALL    $507E               ; {code.destroyFixedTargetReachedByPlayer} destroy the fixed target the player has reached
4F11: 06 01           LD      B,$01               ; one object
4F13: 11 E0 A8        LD      DE,$A8E0            ; point the record cursor at the second era-object run
4F16: FD 21 2C AA     LD      IY,$AA2C            ; point the entry cursor at the second era-object run
4F1A: 2E 05           LD      L,$05               ; collision box near bound
4F1C: 26 0B           LD      H,$0B               ; collision box far bound
4F1E: CD 85 51        CALL    $5185               ; {code.destroyPlayerAndObjectsTouchingIt} destroy the player and the objects it is touching
4F21: 06 01           LD      B,$01               ; one object
4F23: 2E 08           LD      L,$08               ; collision box near bound
4F25: 26 11           LD      H,$11               ; collision box far bound
4F27: C3 B3 51        JP      $51B3               ; {code.markObjectsTouchingPlayer} mark the objects touching the player and return

; era-4 (ERA_INDEX 0xad04=4) per-frame collision dispatch split by frame
; parity (FRAME_TICK 0xa980), reached only as dispatchCollisionPassByEra's
; era-4 tail: even frames run the whole player-vs-object collision-and-
; destruction pass; odd frames stage one shot-vs-target sweep over the
; object-slot run at 0xa810/0xaa12 (six shots, box l=7/h=0x0f), restaging
; the shared body's two reload cursors 0xa991/0xa993 first -- while
; MOTHER_SHIP_ARMED (0xad0d) is set the run is nine long and a mother-ship
; mutual-kill pass (0x4fe0) follows, while clear the run is eleven long
; and none does
dispatchEra4CollisionByFrameParity:
4F2A: 3A 80 A9        LD      A,($A980)           ; {hard.workRam+180} read the frame tick
4F2D: E6 01           AND     $01                 ; its low bit -- frame parity
4F2F: CA 63 4E        JP      Z,$4E63             ; {code.runAllCollisionSweepsThisFrame} even frame: run the whole collision pass
4F32: C3 32 50        JP      $5032               ; {code.loc_5032} odd frame: run the era-4 shot sweep

; choose between the round's two shot sweeps and, on one of the two arms
; only, stage the full seven-target run: while MOTHER_SHIP_ARMED is set
; the sweep that also covers the standing object runs instead, and that
; sweep stages its own runs, so this entry gives it nothing but the
; branch; while the cell is clear the two cursor cells the shared sweep
; reloads between passes are staged here first, so every pass restarts on
; the run chosen here, and the shared sweep then runs six shots against
; seven targets inside one box. Both counts handed over are seven, so the
; first pass is no shorter than the rest
dispatchShotSweepByMotherShipArmed:
4F35: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} read the mother-ship-armed flag
4F38: A7              AND     A                   ; test it
4F39: C2 BF 4F        JP      NZ,$4FBF            ; {code.destroyCraftAndMotherShipHitByShots} armed: run the sweep that also covers the standing craft, and return
4F3C: 11 50 A8        LD      DE,$A850            ; point the record cursor at the craft run
4F3F: FD 21 1A AA     LD      IY,$AA1A            ; point the entry cursor at the craft run
4F43: DD 21 80 AA     LD      IX,$AA80            ; point at the player-shot array
4F47: 08              EX      AF,AF'              
4F48: 3E 07           LD      A,$07               ; seven targets
4F4A: 47              LD      B,A                 ; stage the per-pass target count
4F4B: 08              EX      AF,AF'              ; keep seven as the first-pass count aside
4F4C: 0E 06           LD      C,$06               ; six shots
4F4E: ED 53 93 A9     LD      ($A993),DE          ; {hard.workRam+193} stage the record cursor the sweep reloads between passes
4F52: FD 22 91 A9     LD      ($A991),IY          ; {hard.workRam+191} stage the entry cursor the sweep reloads between passes
4F56: 2E 07           LD      L,$07               ; collision box near bound
4F58: 26 0F           LD      H,$0F               ; collision box far bound
4F5A: C3 11 52        JP      $5211               ; {code.destroyTargetsHitByShots} run the sweep of shots against the seven targets

; stage the two cursor cells and the eight fixed arguments -- the six-slot
; player shot run, a three-slot target run at a sixteen-byte stride, and a
; box seven by fifteen -- then tail-jump into destroyTargetsHitByShots,
; which does the destroying; choosing the runs is the whole of what this
; entry contributes
stagePlayerShotSweepAgainstTargetsAndRun:
4F5D: 11 C0 A8        LD      DE,$A8C0            ; point the record cursor at the era-object run
4F60: FD 21 28 AA     LD      IY,$AA28            ; point the entry cursor at the era-object run
4F64: DD 21 80 AA     LD      IX,$AA80            ; point at the player-shot array
4F68: 08              EX      AF,AF'              
4F69: 3E 03           LD      A,$03               ; three targets
4F6B: 47              LD      B,A                 ; stage the per-pass target count
4F6C: 08              EX      AF,AF'              ; keep three as the first-pass count aside
4F6D: 0E 06           LD      C,$06               ; six shots
4F6F: ED 53 93 A9     LD      ($A993),DE          ; {hard.workRam+193} stage the record cursor the sweep reloads between passes
4F73: FD 22 91 A9     LD      ($A991),IY          ; {hard.workRam+191} stage the entry cursor the sweep reloads between passes
4F77: 2E 07           LD      L,$07               ; collision box near bound
4F79: 26 0F           LD      H,$0F               ; collision box far bound
4F7B: C3 11 52        JP      $5211               ; {code.destroyTargetsHitByShots} run the sweep of six shots against the three targets

; destroy the one fixed target the player's shots have reached, spending
; each shot that reached it and posting the score for each; the target's
; liveness is tested ONCE, ahead of the sweep, so several shots can be
; spent on it in a single pass
destroyFixedTargetHitByShots:
4F7E: 2E 06           LD      L,$06               ; the target's hit window -- first-axis slack
4F80: 26 0D           LD      H,$0D               ; first-axis window width
4F82: 1E 17           LD      E,$17               ; second-axis slack
4F84: 16 1F           LD      D,$1F               ; second-axis window width
4F86: FD 21 80 AA     LD      IY,$AA80            ; point at the player-shot array
4F8A: 06 06           LD      B,$06               ; six shot slots to sweep
4F8C: 3A C0 A8        LD      A,($A8C0)           ; {hard.workRam+C0} read the target's occupancy
4F8F: 3C              INC     A                   ; is it live?
4F90: C0              RET     NZ                  ; target already gone: nothing to do

loc_4f91:
4F91: FD 7E 00        LD      A,(IY+$00)          ; read this shot slot's occupancy
4F94: 3C              INC     A                   ; is the shot live?
4F95: 20 1F           JR      NZ,$4FB6            ; {code.loc_4fb6} empty slot: skip to the next
4F97: 3A 28 AA        LD      A,($AA28)           ; {hard.workRam+228} target's first-axis position
4F9A: FD 96 06        SUB     (IY+$06)            ; minus the shot's first-axis position
4F9D: 85              ADD     A,L                 ; plus the first-axis slack
4F9E: BC              CP      H                   ; within the first-axis window?
4F9F: 30 15           JR      NC,$4FB6            ; {code.loc_4fb6} outside: skip this shot
4FA1: 3A 59 AA        LD      A,($AA59)           ; {hard.workRam+259} target's second-axis position
4FA4: FD 96 04        SUB     (IY+$04)            ; minus the shot's second-axis position
4FA7: 83              ADD     A,E                 ; plus the second-axis slack
4FA8: BA              CP      D                   ; within the second-axis window?
4FA9: 30 0B           JR      NC,$4FB6            ; {code.loc_4fb6} outside: skip this shot
4FAB: 3E F0           LD      A,$F0               ; hit -- destroyed marker
4FAD: 32 C0 A8        LD      ($A8C0),A           ; {hard.workRam+C0} mark the target destroyed
4FB0: FD 77 00        LD      (IY+$00),A          ; spend the shot that hit it
4FB3: CD DE 51        CALL    $51DE               ; {code.postChainedHitScore} post the score for this hit

loc_4fb6:
4FB6: FD 7D           LD      A,IYL               ; step to the next shot slot -- low half of the cursor only, so a wide array wraps in its page
4FB8: C6 10           ADD     A,$10               
4FBA: FD 6F           LD      IYL,A               
4FBC: 10 D3           DJNZ    $4F91               ; {code.loc_4f91} loop over all six shots
4FBE: C9              RET                         

; run the shot sweeps for the stretch of a round in which the Mother-Ship
; is on the field: stage the two cursor cells, sweep the six player shots
; against FIVE ordinary craft rather than the usual seven, then fall
; through into the sweep that runs the same six shots against the Mother-
; Ship's own state byte and screen position. Choosing the shorter craft
; run is the whole of what this entry adds
destroyCraftAndMotherShipHitByShots:
4FBF: 11 50 A8        LD      DE,$A850            ; point at the five ordinary craft's state records
4FC2: FD 21 1A AA     LD      IY,$AA1A            ; point at those craft's sprite entries
4FC6: DD 21 80 AA     LD      IX,$AA80            ; point at the six player-shot records
4FCA: 08              EX      AF,AF'              
4FCB: 3E 05           LD      A,$05               ; five craft to test per shot -- also stashed in the alternate accumulator to reload the count each pass
4FCD: 47              LD      B,A                 
4FCE: 08              EX      AF,AF'              
4FCF: 0E 06           LD      C,$06               ; six shots to sweep through the run
4FD1: ED 53 93 A9     LD      ($A993),DE          ; {hard.workRam+193} stash the target-record pointer so each shot pass reloads it
4FD5: FD 22 91 A9     LD      ($A991),IY          ; {hard.workRam+191} stash the sprite-entry pointer likewise
4FD9: 2E 07           LD      L,$07               ; box half-reach 7 on the first axis
4FDB: 26 0F           LD      H,$0F               ; box span 15 on the first axis
4FDD: CD 11 52        CALL    $5211               ; {code.destroyTargetsHitByShots} sweep the six shots against the five craft, destroying and scoring each hit -- then fall into the mother-ship sweep

; sweep the six player-shot slots for one that has reached the single
; fixed two-slot target, mark both destroyed and post the score for each;
; the first-axis window is widened for two of the era values, by a data
; swap rather than a second body
destroyMotherShipAndShotOnMutualHit:
4FE0: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
4FE3: A7              AND     A                   ; era 0?
4FE4: 28 45           JR      Z,$502B             ; {code.loc_502b} era 0: use the wider first-axis box
4FE6: FE 04           CP      $04                 ; era 4?
4FE8: 28 41           JR      Z,$502B             ; {code.loc_502b} era 4: use the wider box too
4FEA: 2E 06           LD      L,$06               ; narrow first-axis half-reach 6
4FEC: 26 0D           LD      H,$0D               ; narrow first-axis span 13

loc_4fee:
4FEE: 1E 17           LD      E,$17               ; second-axis half-reach 23
4FF0: 16 1F           LD      D,$1F               ; second-axis span 31
4FF2: FD 21 80 AA     LD      IY,$AA80            ; point at the six player-shot records
4FF6: 06 06           LD      B,$06               ; six shots to sweep
4FF8: 3A A0 A8        LD      A,($A8A0)           ; {hard.workRam+A0} read the mother ship's state
4FFB: 3C              INC     A                   
4FFC: C0              RET     NZ                  ; return unless the mother ship is live (0xFF)

loc_4ffd:
4FFD: FD 7E 00        LD      A,(IY+$00)          ; read this shot's state
5000: 3C              INC     A                   
5001: 20 1F           JR      NZ,$5022            ; {code.loc_5022} dead shot -- skip
5003: 3A 24 AA        LD      A,($AA24)           ; {hard.workRam+224} the mother ship's first-axis coordinate
5006: FD 96 06        SUB     (IY+$06)            ; minus this shot's first-axis
5009: 85              ADD     A,L                 ; add the first-axis half-reach
500A: BC              CP      H                   ; inside the first-axis span?
500B: 30 15           JR      NC,$5022            ; {code.loc_5022} outside -- skip
500D: 3A 55 AA        LD      A,($AA55)           ; {hard.workRam+255} the mother ship's second-axis coordinate
5010: FD 96 04        SUB     (IY+$04)            ; minus this shot's second-axis
5013: 83              ADD     A,E                 ; add the second-axis half-reach
5014: BA              CP      D                   ; inside the second-axis span?
5015: 30 0B           JR      NC,$5022            ; {code.loc_5022} outside -- skip
5017: 3E F0           LD      A,$F0               ; the destroyed code
5019: 32 A0 A8        LD      ($A8A0),A           ; {hard.workRam+A0} destroy the mother ship
501C: FD 77 00        LD      (IY+$00),A          ; destroy this shot
501F: CD DE 51        CALL    $51DE               ; {code.postChainedHitScore} post the chained hit score

loc_5022:
5022: FD 7D           LD      A,IYL               
5024: C6 10           ADD     A,$10               ; advance to the next shot record -- low byte only, so it wraps inside the page
5026: FD 6F           LD      IYL,A               
5028: 10 D3           DJNZ    $4FFD               ; {code.loc_4ffd} loop the six shots
502A: C9              RET                         

loc_502b:
502B: 2E 08           LD      L,$08               ; wider first-axis half-reach 8
502D: 26 11           LD      H,$11               ; wider first-axis span 17
502F: C3 EE 4F        JP      $4FEE               ; {code.loc_4fee} run the sweep with the wider box

loc_5032:
5032: 3A 0D AD        LD      A,($AD0D)           ; {hard.workRam+50D} read the flag that the mother ship is out
5035: A7              AND     A                   ; set?
5036: C2 5A 50        JP      NZ,$505A            ; {code.loc_505a} mother ship out: run the nine-target sweep, then the mutual-hit pass
5039: 11 10 A8        LD      DE,$A810            ; point at the enemy-target state records
503C: FD 21 12 AA     LD      IY,$AA12            ; point at their sprite entries
5040: DD 21 80 AA     LD      IX,$AA80            ; point at the six player-shot records
5044: 08              EX      AF,AF'              
5045: 3E 0B           LD      A,$0B               ; eleven targets per shot -- also stashed in the alternate accumulator to reload each pass
5047: 47              LD      B,A                 
5048: 08              EX      AF,AF'              
5049: 0E 06           LD      C,$06               ; six shots to sweep
504B: ED 53 93 A9     LD      ($A993),DE          ; {hard.workRam+193} stash the target-record pointer for reload
504F: FD 22 91 A9     LD      ($A991),IY          ; {hard.workRam+191} stash the sprite-entry pointer likewise
5053: 2E 07           LD      L,$07               ; box half-reach 7
5055: 26 0F           LD      H,$0F               ; box span 15
5057: C3 11 52        JP      $5211               ; {code.destroyTargetsHitByShots} sweep the shots against the eleven targets, destroying and scoring each

loc_505a:
505A: 11 10 A8        LD      DE,$A810            ; point at the enemy-target state records
505D: FD 21 12 AA     LD      IY,$AA12            ; point at their sprite entries
5061: DD 21 80 AA     LD      IX,$AA80            ; point at the six player-shot records
5065: 08              EX      AF,AF'              
5066: 3E 09           LD      A,$09               ; nine targets per shot -- also stashed in the alternate accumulator to reload each pass
5068: 47              LD      B,A                 
5069: 08              EX      AF,AF'              
506A: 0E 06           LD      C,$06               ; six shots to sweep
506C: ED 53 93 A9     LD      ($A993),DE          ; {hard.workRam+193} stash the target-record pointer for reload
5070: FD 22 91 A9     LD      ($A991),IY          ; {hard.workRam+191} stash the sprite-entry pointer likewise
5074: 2E 07           LD      L,$07               ; box half-reach 7
5076: 26 0F           LD      H,$0F               ; box span 15
5078: CD 11 52        CALL    $5211               ; {code.destroyTargetsHitByShots} sweep the shots against the nine targets, destroying and scoring each
507B: C3 E0 4F        JP      $4FE0               ; {code.destroyMotherShipAndShotOnMutualHit} then run the mother-ship-and-shot mutual-hit sweep

; destroy one fixed target and the player with it when the two touch, zero
; the target's HITS_REMAINING so the contact kills it outright rather than
; costing it a hit, and tail-transfer to the scoring routine; four tests
; must all pass, so nothing at all is written unless every one of them
; does
destroyFixedTargetReachedByPlayer:
507E: DD 21 10 AA     LD      IX,$AA10            ; point at the player's sprite entry
5082: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player's state
5085: 3C              INC     A                   
5086: C0              RET     NZ                  ; player gone -- nothing to do
5087: 3A C0 A8        LD      A,($A8C0)           ; {hard.workRam+C0} read the fixed target's state
508A: 3C              INC     A                   
508B: C0              RET     NZ                  ; target gone -- nothing to do
508C: 3A 28 AA        LD      A,($AA28)           ; {hard.workRam+228} the fixed target's first-axis coordinate
508F: DD 96 00        SUB     (IX+$00)            ; minus the player's first-axis
5092: C6 06           ADD     A,$06               ; add the first-axis slack (6)
5094: FE 0D           CP      $0D                 ; inside the first-axis window (13)?
5096: D0              RET     NC                  ; outside -- no contact
5097: 3A 59 AA        LD      A,($AA59)           ; {hard.workRam+259} the fixed target's second-axis coordinate
509A: DD 96 31        SUB     (IX+$31)            ; minus the player's second-axis
509D: C6 18           ADD     A,$18               ; add the second-axis slack (24)
509F: FE 21           CP      $21                 ; inside the second-axis window (33)?
50A1: D0              RET     NC                  ; outside -- no contact
50A2: 3E F0           LD      A,$F0               ; the destroyed code
50A4: 32 00 A8        LD      ($A800),A           ; {hard.workRam} destroy the player
50A7: 32 C0 A8        LD      ($A8C0),A           ; {hard.workRam+C0} destroy the fixed target
50AA: AF              XOR     A                   
50AB: 32 DC A8        LD      ($A8DC),A           ; {hard.workRam+DC} clear the target's remaining-hits count so the contact kills it outright rather than costing it a hit
50AE: C3 DE 51        JP      $51DE               ; {code.postChainedHitScore} post the chained hit score

; select the collision box for the mutual kill of the player and one fixed
; two-slot target by ERA_INDEX: eras 0 and 4 transfer to the wider first-
; axis check (destroyPlayerAndMotherShipOnContact), the rest run the same
; destruction inline with a narrower first-axis window; when both are live
; and their coordinates fall in the box, mark both destroyed, clear the
; cell beside them, and tail-post the chained hit score
ramTestPlayerVsMotherShip:
50B1: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the era index
50B4: A7              AND     A                   ; era 0?
50B5: 28 37           JR      Z,$50EE             ; {code.destroyPlayerAndMotherShipOnContact} era 0: use the wider-box mutual-kill check
50B7: FE 04           CP      $04                 ; era 4?
50B9: 28 33           JR      Z,$50EE             ; {code.destroyPlayerAndMotherShipOnContact} era 4: use the wider-box check too
50BB: DD 21 10 AA     LD      IX,$AA10            ; point at the player's sprite entry
50BF: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player's state
50C2: 3C              INC     A                   
50C3: C0              RET     NZ                  ; player gone -- nothing to do
50C4: 3A A0 A8        LD      A,($A8A0)           ; {hard.workRam+A0} read the mother ship's state
50C7: 3C              INC     A                   
50C8: C0              RET     NZ                  ; mother ship gone -- nothing to do
50C9: 3A 24 AA        LD      A,($AA24)           ; {hard.workRam+224} the mother ship's first-axis coordinate
50CC: DD 96 00        SUB     (IX+$00)            ; minus the player's first-axis
50CF: C6 06           ADD     A,$06               ; add the narrow first-axis slack (6)
50D1: FE 0D           CP      $0D                 ; inside the first-axis window (13)?
50D3: D0              RET     NC                  ; outside -- no contact
50D4: 3A 55 AA        LD      A,($AA55)           ; {hard.workRam+255} the mother ship's second-axis coordinate
50D7: DD 96 31        SUB     (IX+$31)            ; minus the player's second-axis
50DA: C6 19           ADD     A,$19               ; add the second-axis slack (25)
50DC: FE 23           CP      $23                 ; inside the second-axis window (35)?
50DE: D0              RET     NC                  ; outside -- no contact
50DF: 3E F0           LD      A,$F0               ; the destroyed code
50E1: 32 00 A8        LD      ($A800),A           ; {hard.workRam} destroy the player
50E4: 32 A0 A8        LD      ($A8A0),A           ; {hard.workRam+A0} destroy the mother ship
50E7: AF              XOR     A                   
50E8: 32 A4 A8        LD      ($A8A4),A           ; {hard.workRam+A4} clear the mother ship's hold counter, the cell beside its state
50EB: C3 DE 51        JP      $51DE               ; {code.postChainedHitScore} post the chained hit score

; destroy the player and one fixed two-slot target together when they
; touch, zero that target's hit counter so the contact kills it outright
; instead of costing it one hit, and tail-transfer to the chained hit
; score; this is the wider of two first-axis windows, and the arm its
; caller selects for two of the era values
destroyPlayerAndMotherShipOnContact:
50EE: DD 21 10 AA     LD      IX,$AA10            ; point at the player's sprite entry
50F2: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player's state
50F5: 3C              INC     A                   
50F6: C0              RET     NZ                  ; player gone -- nothing to do
50F7: 3A A0 A8        LD      A,($A8A0)           ; {hard.workRam+A0} read the mother ship's state
50FA: 3C              INC     A                   
50FB: C0              RET     NZ                  ; mother ship gone -- nothing to do
50FC: 3A 24 AA        LD      A,($AA24)           ; {hard.workRam+224} the mother ship's first-axis coordinate
50FF: DD 96 00        SUB     (IX+$00)            ; minus the player's first-axis
5102: C6 08           ADD     A,$08               ; add the wider first-axis slack (8)
5104: FE 11           CP      $11                 ; inside the wider first-axis window (17)?
5106: D0              RET     NC                  ; outside -- no contact
5107: 3A 55 AA        LD      A,($AA55)           ; {hard.workRam+255} the mother ship's second-axis coordinate
510A: DD 96 31        SUB     (IX+$31)            ; minus the player's second-axis
510D: C6 19           ADD     A,$19               ; add the second-axis slack (25)
510F: FE 23           CP      $23                 ; inside the second-axis window (35)?
5111: D0              RET     NC                  ; outside -- no contact
5112: 3E F0           LD      A,$F0               ; the destroyed code
5114: 32 00 A8        LD      ($A800),A           ; {hard.workRam} destroy the player
5117: 32 A0 A8        LD      ($A8A0),A           ; {hard.workRam+A0} destroy the mother ship
511A: AF              XOR     A                   
511B: 32 A4 A8        LD      ($A8A4),A           ; {hard.workRam+A4} clear the mother ship's hold counter, the cell beside its state
511E: C3 DE 51        JP      $51DE               ; {code.postChainedHitScore} post the chained hit score

; destroy every target of a caller's run that one fixed attacker -- the
; player's own ship -- has reached, marking both destroyed and posting the
; chained score for each; the attacker's state is tested once, so one pass
; can take several
destroyTargetsReachedByFixedAttacker:
5121: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player's state -- the fixed attacker
5124: 3C              INC     A                   
5125: C0              RET     NZ                  ; player gone -- nothing to do

loc_5126:
5126: 1A              LD      A,(DE)              ; read this target's state
5127: 3C              INC     A                   
5128: 20 1D           JR      NZ,$5147            ; {code.loc_5147} dead target -- skip
512A: 3A 10 AA        LD      A,($AA10)           ; {hard.workRam+210} the player's first-axis coordinate
512D: FD 96 00        SUB     (IY+$00)            ; minus this target's first-axis
5130: 85              ADD     A,L                 ; add the caller's slack
5131: BC              CP      H                   ; inside the caller's window?
5132: 30 13           JR      NC,$5147            ; {code.loc_5147} outside -- skip
5134: 3A 41 AA        LD      A,($AA41)           ; {hard.workRam+241} the player's second-axis coordinate
5137: FD 96 31        SUB     (IY+$31)            ; minus this target's second-axis
513A: 85              ADD     A,L                 ; add the same slack
513B: BC              CP      H                   ; inside the same window?
513C: 30 09           JR      NC,$5147            ; {code.loc_5147} outside -- skip
513E: 3E F0           LD      A,$F0               ; the destroyed code
5140: 32 00 A8        LD      ($A800),A           ; {hard.workRam} destroy the player
5143: 12              LD      (DE),A              ; destroy this target
5144: CD DE 51        CALL    $51DE               ; {code.postChainedHitScore} post the chained hit score

loc_5147:
5147: 7B              LD      A,E                 
5148: C6 10           ADD     A,$10               ; advance to the next target record -- low byte only, so it wraps inside the page
514A: 5F              LD      E,A                 
514B: FD 23           INC     IY                  ; step to the next sprite entry (two bytes on)
514D: FD 23           INC     IY                  
514F: 10 D5           DJNZ    $5126               ; {code.loc_5126} loop the run
5151: C9              RET                         

; sweep a run of slots against the player's own sprite entry and, for
; every overlap, write the destroyed marker into both the slot and the
; player and post the score; the sweep does not stop at the first
destroySlotsAndPlayerOnContact:
5152: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player's state
5155: 3C              INC     A                   
5156: C0              RET     NZ                  ; player already hit -- nothing to do

loc_5157:
5157: 1A              LD      A,(DE)              ; read this slot's state
5158: 3C              INC     A                   
5159: 20 1F           JR      NZ,$517A            ; {code.loc_517a} slot already hit -- skip
515B: 3A 10 AA        LD      A,($AA10)           ; {hard.workRam+210} the player's first-axis coordinate
515E: FD 96 00        SUB     (IY+$00)            ; minus this slot's first-axis
5161: 85              ADD     A,L                 ; add the caller's first-axis bias
5162: BC              CP      H                   ; inside the caller's first-axis width?
5163: 30 15           JR      NC,$517A            ; {code.loc_517a} outside -- skip
5165: 3A 41 AA        LD      A,($AA41)           ; {hard.workRam+241} the player's second-axis coordinate
5168: FD 96 31        SUB     (IY+$31)            ; minus this slot's second-axis
516B: C6 08           ADD     A,$08               ; add the fixed second-axis bias (8)
516D: FE 11           CP      $11                 ; inside the fixed second-axis width (17)?
516F: 30 09           JR      NC,$517A            ; {code.loc_517a} outside -- skip
5171: 3E F0           LD      A,$F0               ; the hit code
5173: 32 00 A8        LD      ($A800),A           ; {hard.workRam} mark the player hit
5176: 12              LD      (DE),A              ; mark this slot hit
5177: CD DE 51        CALL    $51DE               ; {code.postChainedHitScore} post the chained hit score

loc_517a:
517A: 7B              LD      A,E                 
517B: C6 10           ADD     A,$10               ; advance to the next slot record -- low byte only, so it wraps inside the page
517D: 5F              LD      E,A                 
517E: FD 23           INC     IY                  ; step to the next sprite entry (two bytes on)
5180: FD 23           INC     IY                  
5182: 10 D3           DJNZ    $5157               ; {code.loc_5157} loop the run
5184: C9              RET                         

; destroy the player and every object of a caller's run that lies inside a
; wrapped box around the player's sprite entry, while the player is alive;
; one window width serves both axes, nothing is scored, and the sweep runs
; on past the first
destroyPlayerAndObjectsTouchingIt:
5185: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player's state
5188: 3C              INC     A                   
5189: C0              RET     NZ                  ; player gone -- nothing to do

loc_518a:
518A: 1A              LD      A,(DE)              ; read this object's state
518B: 3C              INC     A                   
518C: 20 1A           JR      NZ,$51A8            ; {code.loc_51a8} dead object -- skip
518E: 3A 10 AA        LD      A,($AA10)           ; {hard.workRam+210} the player's first-axis coordinate
5191: FD 96 00        SUB     (IY+$00)            ; minus this object's first-axis
5194: 85              ADD     A,L                 ; add the caller's slack
5195: BC              CP      H                   ; inside the caller's window?
5196: 30 10           JR      NC,$51A8            ; {code.loc_51a8} outside -- skip
5198: 3A 41 AA        LD      A,($AA41)           ; {hard.workRam+241} the player's second-axis coordinate
519B: FD 96 31        SUB     (IY+$31)            ; minus this object's second-axis
519E: 85              ADD     A,L                 ; add the same slack
519F: BC              CP      H                   ; inside the same window?
51A0: 30 06           JR      NC,$51A8            ; {code.loc_51a8} outside -- skip
51A2: 3E F0           LD      A,$F0               ; the destroyed code
51A4: 32 00 A8        LD      ($A800),A           ; {hard.workRam} destroy the player
51A7: 12              LD      (DE),A              ; destroy this object

loc_51a8:
51A8: 7B              LD      A,E                 
51A9: C6 10           ADD     A,$10               ; advance to the next object record -- low byte only, so it wraps inside the page
51AB: 5F              LD      E,A                 
51AC: FD 23           INC     IY                  ; step to the next sprite entry (two bytes on)
51AE: FD 23           INC     IY                  
51B0: 10 D8           DJNZ    $518A               ; {code.loc_518a} loop the run
51B2: C9              RET                         

; replace the state byte of every object in a caller's run that lies
; inside a wrapped box around the player's sprite entry, while the player
; is alive; the box is the caller's, the player's own state is untouched
; and nothing is scored
markObjectsTouchingPlayer:
51B3: 3A 00 A8        LD      A,($A800)           ; {hard.workRam} read the player's state
51B6: 3C              INC     A                   
51B7: C0              RET     NZ                  ; player gone -- nothing to do

loc_51b8:
51B8: 1A              LD      A,(DE)              ; read this object's state
51B9: 3C              INC     A                   
51BA: 20 17           JR      NZ,$51D3            ; {code.loc_51d3} dead object -- skip
51BC: 3A 10 AA        LD      A,($AA10)           ; {hard.workRam+210} the player's first-axis coordinate
51BF: FD 96 00        SUB     (IY+$00)            ; minus this object's first-axis
51C2: 85              ADD     A,L                 ; add the caller's offset
51C3: BC              CP      H                   ; inside the caller's width?
51C4: 30 0D           JR      NC,$51D3            ; {code.loc_51d3} outside -- skip
51C6: 3A 41 AA        LD      A,($AA41)           ; {hard.workRam+241} the player's second-axis coordinate
51C9: FD 96 31        SUB     (IY+$31)            ; minus this object's second-axis
51CC: 85              ADD     A,L                 ; add the same offset
51CD: BC              CP      H                   ; inside the same width?
51CE: 30 03           JR      NC,$51D3            ; {code.loc_51d3} outside -- skip
51D0: 3E F0           LD      A,$F0               ; the marked code
51D2: 12              LD      (DE),A              ; mark this object -- the only cell written

loc_51d3:
51D3: 7B              LD      A,E                 
51D4: C6 10           ADD     A,$10               ; advance to the next object state byte -- low byte only, so it wraps inside the page
51D6: 5F              LD      E,A                 
51D7: FD 23           INC     IY                  ; step to the next sprite entry (two bytes on)
51D9: FD 23           INC     IY                  
51DB: 10 DB           DJNZ    $51B8               ; {code.loc_51b8} loop the run
51DD: C9              RET                         

; post a scoring command to the ring, stepping the award up while
; consecutive hits keep landing inside the chain window and wrapping back
; round after the eighth
postChainedHitScore:
51DE: D5              PUSH    DE                  ; save the caller's DE across the post
51DF: 3A 9D A9        LD      A,($A99D)           ; {hard.workRam+19D} read the chain window
51E2: A7              AND     A                   ; has it run out?
51E3: 28 15           JR      Z,$51FA             ; {code.loc_51fa} window closed -- post the first step
51E5: 3A 9E A9        LD      A,($A99E)           ; {hard.workRam+19E} read the chain step
51E8: 3C              INC     A                   ; climb it one
51E9: 32 9E A9        LD      ($A99E),A           ; {hard.workRam+19E} store the climbed step
51EC: E6 07           AND     $07                 ; wrap it within the eight-long chain
51EE: 3C              INC     A                   ; the argument is that step plus one
51EF: 5F              LD      E,A                 
51F0: 16 04           LD      D,$04               ; scoring command group 4
51F2: FF              RST     $38                 ; queue the score request onto the command ring
51F3: D1              POP     DE                  ; restore the caller's DE
51F4: 3E 1E           LD      A,$1E               ; reload value 30
51F6: 32 9D A9        LD      ($A99D),A           ; {hard.workRam+19D} re-arm the chain window
51F9: C9              RET                         

loc_51fa:
51FA: 11 01 04        LD      DE,$0401            ; scoring command 4, argument 1 -- the first step
51FD: FF              RST     $38                 ; queue it onto the command ring
51FE: D1              POP     DE                  ; restore the caller's DE
51FF: 3E 1E           LD      A,$1E               ; reload value 30
5201: 32 9D A9        LD      ($A99D),A           ; {hard.workRam+19D} re-arm the chain window
5204: C9              RET                         

; run the chained-hit window down by one and, on every frame after it has
; reached zero, clear the chain step so the next hit starts the award
; ladder from the bottom again
expireHitChain:
5205: 21 9D A9        LD      HL,$A99D            ; point at the chain window
5208: 7E              LD      A,(HL)              ; read it
5209: A7              AND     A                   ; already zero?
520A: 28 02           JR      Z,$520E             ; {code.loc_520e} run out -- clear the chain step instead
520C: 35              DEC     (HL)                ; count the window down one
520D: C9              RET                         

loc_520e:
520E: 2C              INC     L                   ; point at the next byte -- the chain step
520F: 77              LD      (HL),A              ; clear it, so the next hit starts the award from the bottom
5210: C9              RET                         

; destroy every target a live shot has reached, spending the shot with
; them, and post the score for each; the sweep does not stop at the first,
; so one shot can take several in a pass
destroyTargetsHitByShots:
5211: DD 7E 00        LD      A,(IX+$00)          ; read this shot's state
5214: 3C              INC     A                   
5215: 20 3D           JR      NZ,$5254            ; {code.loc_5254} dead shot -- on to the next shot

loc_5217:
5217: 1A              LD      A,(DE)              ; read this target's state
5218: 3C              INC     A                   
5219: 20 2F           JR      NZ,$524A            ; {code.loc_524a} dead target -- skip
521B: FD 7E 00        LD      A,(IY+$00)          ; the target's first-axis coordinate
521E: C6 08           ADD     A,$08               ; shift the low end above zero
5220: FE 19           CP      $19                 ; in the dead band a blank slot leaves near zero?
5222: 38 26           JR      C,$524A             ; {code.loc_524a} yes -- no real target here, skip
5224: FD 7E 31        LD      A,(IY+$31)          ; the target's second-axis coordinate
5227: C6 10           ADD     A,$10               ; shift the low end above zero
5229: FE 11           CP      $11                 ; in the near-zero dead band?
522B: 38 1D           JR      C,$524A             ; {code.loc_524a} yes -- skip
522D: DD 7E 06        LD      A,(IX+$06)          ; the shot's first-axis coordinate
5230: FD 96 00        SUB     (IY+$00)            ; minus the target's first-axis
5233: 85              ADD     A,L                 ; add the half-reach
5234: BC              CP      H                   ; inside the span?
5235: 30 13           JR      NC,$524A            ; {code.loc_524a} outside -- skip
5237: DD 7E 04        LD      A,(IX+$04)          ; the shot's second-axis coordinate
523A: FD 96 31        SUB     (IY+$31)            ; minus the target's second-axis
523D: 85              ADD     A,L                 ; add the half-reach
523E: BC              CP      H                   ; inside the span?
523F: 30 09           JR      NC,$524A            ; {code.loc_524a} outside -- skip
5241: 3E F0           LD      A,$F0               ; the destroyed code
5243: DD 77 00        LD      (IX+$00),A          ; destroy the shot
5246: 12              LD      (DE),A              ; destroy the target
5247: CD DE 51        CALL    $51DE               ; {code.postChainedHitScore} post the chained hit score

loc_524a:
524A: 7B              LD      A,E                 
524B: C6 10           ADD     A,$10               ; advance to the next target record -- low byte only, so it wraps inside the page
524D: 5F              LD      E,A                 
524E: FD 23           INC     IY                  ; step to the next target entry (two bytes on)
5250: FD 23           INC     IY                  
5252: 10 C3           DJNZ    $5217               ; {code.loc_5217} loop the targets for this shot

loc_5254:
5254: FD 2A 91 A9     LD      IY,($A991)          ; {hard.workRam+191} reload the sprite-entry cursor for the next shot
5258: ED 5B 93 A9     LD      DE,($A993)          ; {hard.workRam+193} reload the target-record cursor for the next shot
525C: 08              EX      AF,AF'              
525D: 47              LD      B,A                 ; reload the per-shot target count from the alternate accumulator
525E: 08              EX      AF,AF'              
525F: DD 7D           LD      A,IXL               
5261: C6 10           ADD     A,$10               ; advance to the next shot record -- low byte only, so it wraps inside the page
5263: DD 6F           LD      IXL,A               
5265: 0D              DEC     C                   ; one shot done
5266: C2 11 52        JP      NZ,$5211            ; {code.destroyTargetsHitByShots} loop the shots
5269: C9              RET                         

; put both deferred character-cell lists back to empty, parking each
; cursor four bytes past its own head
emptyBothDeferredCellLists:
526A: 21 84 AE        LD      HL,$AE84            ; point at the erase list's first entry
526D: 22 80 AE        LD      ($AE80),HL          ; {hard.workRam+680} park the erase cursor there -- list emptied
5270: 21 04 AE        LD      HL,$AE04            ; point at the pending list's first entry
5273: 22 00 AE        LD      ($AE00),HL          ; {hard.workRam+600} park the pending cursor there -- list emptied
5276: C9              RET                         

; ---- $5277-$5285: data ----
5277: 06 00 21 DE 27 AF 86 23 10 FC D6 C5 C4 D4 53

; one pass of the deferred cell machinery: blank the cells the erase list
; names, paint the cells the pending list names, then copy the pending
; list wholesale onto the erase list and park the pending cursor back on
; its own first entry. The copy length is the pending cursor's own byte,
; cursor included, so it lands the pending count on top of the erase
; cursor and the line after replaces that with the same count plus a mark
; in the top bit; where nothing is pending both cursors are parked instead
; and no copy happens; and a cursor of ZERO is not nothing pending -- the
; count is a block-copy length, and a length of zero means the whole
; address space. NOT a double buffer: the copy runs one way, 0xAE00 onto
; 0xAE80, on every pass, and the two lists hold different jobs rather than
; alternating ones
drainBothDeferredCellLists:
5286: CD 0E 53        CALL    $530E               ; {code.blankCellsPaintedLastPass} blank the cells the previous pass painted
5289: CD D2 52        CALL    $52D2               ; {code.paintDeferredCells} paint the cells now pending
528C: 3A 00 AE        LD      A,($AE00)           ; {hard.workRam+600} read the pending list's fill count -- its cursor's low byte
528F: FE 04           CP      $04                 ; still at the first entry -- nothing pending?
5291: 28 D7           JR      Z,$526A             ; {code.emptyBothDeferredCellLists} nothing pending -- park both cursors and return
5293: 4F              LD      C,A                 ; set the block-copy length to the pending fill count
5294: 06 00           LD      B,$00               ; high byte zero -- a length of zero would copy the whole address space
5296: 21 00 AE        LD      HL,$AE00            ; source: the pending list from its cursor
5299: 11 80 AE        LD      DE,$AE80            ; destination: the erase list
529C: ED B0           LDIR                        ; copy the pending list wholesale onto the erase list
529E: C6 80           ADD     A,$80               ; flag the copied count with the top bit...
52A0: 32 80 AE        LD      ($AE80),A           ; {hard.workRam+680} ...and write it as the erase cursor, marking the list copied
52A3: 21 04 AE        LD      HL,$AE04            ; point at the pending list's first entry
52A6: 22 00 AE        LD      ($AE00),HL          ; {hard.workRam+600} park the pending cursor there -- pending list emptied
52A9: C9              RET                         

; boot-time DIP seed: copy two ROM defaults into their cells
; (0x08c9->0xa98d, 0x0874->KILL_QUOTA), store DSW0 complemented as
; COINAGE_SETTINGS and unpack the coin ratios, then turn DSW1's low two
; bits into a lives count (3/4/5, or 0xff when they fold to none) and
; tail-jump with it plus the whole complemented bank into the switch-
; settings peeler; never returns
seedGameConfigFromDipSwitches:
52AA: 3A C9 08        LD      A,($08C9)           ; {hard.rom+8C9} take the boot default for the high-score high byte
52AD: 32 8D A9        LD      ($A98D),A           ; {hard.workRam+18D} seed it into its cell
52B0: 3A 74 08        LD      A,($0874)           ; {hard.rom+874} take the boot default for the kill quota
52B3: 32 CD A9        LD      ($A9CD),A           ; {hard.workRam+1CD} seed it into its cell
52B6: 3A 60 C3        LD      A,($C360)           ; read the first DIP-switch bank
52B9: 2F              CPL                         ; complement it -- the switches read active-low
52BA: 32 B1 A9        LD      ($A9B1),A           ; {hard.workRam+1B1} store it as the coin settings
52BD: CD CC 4A        CALL    $4ACC               ; {code.unpackCoinage} unpack the coin ratios from it
52C0: 3A 00 C2        LD      A,($C200)           ; read the second DIP-switch bank
52C3: 2F              CPL                         ; complement it
52C4: 4F              LD      C,A                 ; keep the whole complemented bank for the peeler
52C5: E6 03           AND     $03                 ; take the low two switch bits
52C7: C6 03           ADD     A,$03               ; turn them into a lives count of 3, 4, 5 or 6
52C9: FE 06           CP      $06                 ; the setting that would give six...
52CB: 20 02           JR      NZ,$52CF            ; {code.loc_52cf} ...otherwise carry the lives count on
52CD: 3E FF           LD      A,$FF               ; ...folds to all-ones (no starting lives)

loc_52cf:
52CF: C3 19 2E        JP      $2E19               ; {code.unpackTheFirstThreeSwitchSettings} hand the lives count and the whole bank to the switch-settings peeler

; paint the deferred cell list into the character plane and its colour
; plane: each four-byte entry gives a colour-plane address, the shape to
; put a plane above it and the colour to put at it, with one shared bias
; added to every colour. How many are pending comes off the low half of
; the list's own write cursor, so the whole list lives inside one page; an
; entry whose colour cell already has the high-priority bit set is passed
; over untouched, and a cursor that scales to a count of zero is not empty
; -- the loop runs 256 times
paintDeferredCells:
52D2: 3A 0C AD        LD      A,($AD0C)           ; {hard.workRam+50C} read the pen colour
52D5: E6 0F           AND     $0F                 ; keep its low nibble as the shared tint bias
52D7: 4F              LD      C,A                 
52D8: 2A 00 AE        LD      HL,($AE00)          ; {hard.workRam+600} read the pending list cursor
52DB: 7D              LD      A,L                 ; take its low byte
52DC: D6 04           SUB     $04                 ; drop the four-byte header -- how many bytes are filled
52DE: C8              RET     Z                   ; nothing pending -- done
52DF: 0F              RRCA                        ; divide the byte count by four -- four bytes per entry -- into an entry count
52E0: 0F              RRCA                        
52E1: E6 1F           AND     $1F                 ; keep it within one page (at most 31 entries)
52E3: 47              LD      B,A                 
52E4: 21 04 AE        LD      HL,$AE04            ; point at the list's first entry

loc_52e7:
52E7: 5E              LD      E,(HL)              ; take the entry's colour-plane address low byte
52E8: 2C              INC     L                   
52E9: 56              LD      D,(HL)              ; and its high byte
52EA: 2C              INC     L                   
52EB: 1A              LD      A,(DE)              ; read the colour cell there
52EC: E6 10           AND     $10                 ; is it flagged as drawn above the sprites?
52EE: 20 0E           JR      NZ,$52FE            ; {code.loc_52fe} yes -- leave this cell alone
52F0: 7E              LD      A,(HL)              ; take the entry's shape
52F1: CB D2           SET     2,D                 ; aim one plane up -- the character plane
52F3: 12              LD      (DE),A              ; write the shape into the character plane
52F4: CB 92           RES     2,D                 
52F6: 2C              INC     L                   
52F7: 7E              LD      A,(HL)              ; take the entry's colour
52F8: 2C              INC     L                   
52F9: 81              ADD     A,C                 ; add the shared tint bias
52FA: 12              LD      (DE),A              ; write the colour into the colour cell
52FB: 10 EA           DJNZ    $52E7               ; {code.loc_52e7} loop the pending entries
52FD: C9              RET                         

loc_52fe:
52FE: 2C              INC     L                   ; skip this passed-over entry's shape and colour bytes
52FF: 2C              INC     L                   
5300: 10 E5           DJNZ    $52E7               ; {code.loc_52e7} loop the pending entries
5302: C9              RET                         

; run the image-checksum tamper test and relay by its verdict: present the
; carried checksum, step the attract sequence on the one genuine value,
; else spring the tamper trap
advanceSequenceUnlessImageTampered:
5303: CD 0C 20        CALL    $200C               ; {code.presentChecksumForTamperTest} run the image-checksum tamper test, returning the checksum
5306: FE 67           CP      $67                 ; is it the one value a genuine image gives?
5308: C2 8D 0F        JP      NZ,$0F8D            ; {code.loc_0f8d} tampered -- spring the tamper trap
530B: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} genuine -- step the attract sequence on

; blank the character-plane cells the previous pass painted: walk the
; second deferred cell list, which the shared caller filled by copying the
; paint list wholesale after draining it, and write the blank shape a
; plane above each entry's address, leaving the colour byte exactly as it
; was. The pending count comes off the masked low half of that list's own
; cursor -- the mask drops the top bit the caller sets when it copies --
; and an entry whose colour cell already has the high-priority bit set is
; passed over
blankCellsPaintedLastPass:
530E: 2A 80 AE        LD      HL,($AE80)          ; {hard.workRam+680} read the deferred-blank list's write cursor
5311: 7D              LD      A,L                 ; take its low byte -- how far the list has filled
5312: E6 7F           AND     $7F                 ; mask off the top bit the filler sets
5314: D6 04           SUB     $04                 ; subtract the four-byte header -- leaves the bytes actually queued
5316: C8              RET     Z                   ; still at the first entry: nothing pending, done
5317: 0F              RRCA                        ; turn the byte count into an entry count -- four bytes each
5318: 0F              RRCA                        
5319: E6 1F           AND     $1F                 ; keep it within the list's page
531B: 47              LD      B,A                 ; loop that many entries
531C: 21 84 AE        LD      HL,$AE84            ; point at the first list entry

loc_531f:
531F: 5E              LD      E,(HL)              ; this entry's target colour cell, low byte of the address
5320: 2C              INC     L                   
5321: 56              LD      D,(HL)              ; and its high byte
5322: 2C              INC     L                   
5323: 1A              LD      A,(DE)              ; read that colour cell
5324: E6 10           AND     $10                 ; test its high-priority bit
5326: 20 0A           JR      NZ,$5332            ; {code.loc_5332} already high-priority: leave this cell, on to the next entry
5328: 2C              INC     L                   ; step past this entry's two spare bytes to the next
5329: 2C              INC     L                   
532A: CB D2           SET     2,D                 ; aim the same address at the character plane (+$400)
532C: 3E 20           LD      A,$20               ; the blank glyph
532E: 12              LD      (DE),A              ; stamp it into the character cell, colour left as-is
532F: 10 EE           DJNZ    $531F               ; {code.loc_531f} next queued entry
5331: C9              RET                         

loc_5332:
5332: 2C              INC     L                   ; step over the skipped entry's two spare bytes
5333: 2C              INC     L                   
5334: 10 E9           DJNZ    $531F               ; {code.loc_531f} on to the next entry
5336: C9              RET                         

; queue a two-by-two block of character cells for an object's position
; onto the deferred write list, one four-byte entry per cell, skipping a
; pair whose glyph is zero
queueTileStampForObject:
5337: DD 7E 04        LD      A,(IX+$04)          ; the object's first pixel coordinate
533A: C6 07           ADD     A,$07               ; bias by seven -- centres the block on the object
533C: 47              LD      B,A                 ; keep the biased coordinate
533D: 16 28           LD      D,$28               ; seed the tile-plane address high byte
533F: 07              RLCA                        
5340: CB 12           RL      D                   
5342: 07              RLCA                        
5343: CB 12           RL      D                   ; fold the coordinate's top bits into that high byte
5345: E6 E0           AND     $E0                 ; its tile-row bits for the address low byte
5347: 5F              LD      E,A                 
5348: DD 7E 06        LD      A,(IX+$06)          ; the object's second pixel coordinate
534B: C6 07           ADD     A,$07               ; bias by seven
534D: 4F              LD      C,A                 ; keep it
534E: 0F              RRCA                        
534F: 0F              RRCA                        
5350: 0F              RRCA                        
5351: E6 1F           AND     $1F                 ; its tile column
5353: 83              ADD     A,E                 ; combine row and column -- the block's top-left cell, low byte
5354: 5F              LD      E,A                 
5355: 79              LD      A,C                 ; back to the second coordinate
5356: 07              RLCA                        
5357: 07              RLCA                        
5358: 07              RLCA                        
5359: E6 38           AND     $38                 ; its low three bits, the sub-cell shift
535B: 4F              LD      C,A                 
535C: 78              LD      A,B                 ; the first coordinate again
535D: 06 00           LD      B,$00               
535F: CB 57           BIT     2,A                 ; its bit that overflows the record index into the high byte
5361: 28 01           JR      Z,$5364             ; {code.loc_5364}
5363: 04              INC     B                   ; set that high bit of the index

loc_5364:
5364: 0F              RRCA                        
5365: 0F              RRCA                        
5366: E6 C0           AND     $C0                 ; the first coordinate's low bits for the index
5368: 81              ADD     A,C                 ; add the second coordinate's -- picks one of sixty-four sub-cell records
5369: 4F              LD      C,A                 
536A: 21 D4 53        LD      HL,$53D4            ; the table of pre-shifted tile records
536D: 09              ADD     HL,BC               ; index the chosen record -- four glyph/attribute pairs, one per cell
536E: 7E              LD      A,(HL)              ; first cell's glyph
536F: 23              INC     HL                  
5370: 46              LD      B,(HL)              ; its colour attribute
5371: 23              INC     HL                  
5372: A7              AND     A                   ; glyph zero?
5373: 28 10           JR      Z,$5385             ; {code.loc_5385} transparent: skip this cell
5375: E5              PUSH    HL                  
5376: 2A 00 AE        LD      HL,($AE00)          ; {hard.workRam+600} the deferred-write list's tail
5379: 73              LD      (HL),E              ; write the cell address low byte
537A: 2C              INC     L                   
537B: 72              LD      (HL),D              ; the high byte
537C: 2C              INC     L                   
537D: 77              LD      (HL),A              ; the glyph
537E: 2C              INC     L                   
537F: 70              LD      (HL),B              ; the attribute
5380: 2C              INC     L                   
5381: 22 00 AE        LD      ($AE00),HL          ; {hard.workRam+600} store the advanced tail -- stays inside its page
5384: E1              POP     HL                  

loc_5385:
5385: 13              INC     DE                  ; step the cell across one column
5386: 7E              LD      A,(HL)              ; second cell's glyph
5387: 23              INC     HL                  
5388: 46              LD      B,(HL)              ; its attribute
5389: 23              INC     HL                  
538A: A7              AND     A                   ; glyph zero?
538B: 28 10           JR      Z,$539D             ; {code.loc_539d} transparent: skip it
538D: E5              PUSH    HL                  
538E: 2A 00 AE        LD      HL,($AE00)          ; {hard.workRam+600} the list tail
5391: 73              LD      (HL),E              ; cell address low byte
5392: 2C              INC     L                   
5393: 72              LD      (HL),D              ; high byte
5394: 2C              INC     L                   
5395: 77              LD      (HL),A              ; glyph
5396: 2C              INC     L                   
5397: 70              LD      (HL),B              ; attribute
5398: 2C              INC     L                   
5399: 22 00 AE        LD      ($AE00),HL          ; {hard.workRam+600} store the advanced tail
539C: E1              POP     HL                  

loc_539d:
539D: 7B              LD      A,E                 
539E: C6 1F           ADD     A,$1F               ; step the cell down one row to the second row's first column
53A0: 5F              LD      E,A                 
53A1: 30 01           JR      NC,$53A4            ; {code.loc_53a4}
53A3: 14              INC     D                   

loc_53a4:
53A4: 7E              LD      A,(HL)              ; third cell's glyph
53A5: 23              INC     HL                  
53A6: 46              LD      B,(HL)              ; its attribute
53A7: 23              INC     HL                  
53A8: A7              AND     A                   ; glyph zero?
53A9: 28 10           JR      Z,$53BB             ; {code.loc_53bb} transparent: skip it
53AB: E5              PUSH    HL                  
53AC: 2A 00 AE        LD      HL,($AE00)          ; {hard.workRam+600} the list tail
53AF: 73              LD      (HL),E              ; cell address low byte
53B0: 2C              INC     L                   
53B1: 72              LD      (HL),D              ; high byte
53B2: 2C              INC     L                   
53B3: 77              LD      (HL),A              ; glyph
53B4: 2C              INC     L                   
53B5: 70              LD      (HL),B              ; attribute
53B6: 2C              INC     L                   
53B7: 22 00 AE        LD      ($AE00),HL          ; {hard.workRam+600} store the advanced tail
53BA: E1              POP     HL                  

loc_53bb:
53BB: 13              INC     DE                  ; step the cell across one column
53BC: 7E              LD      A,(HL)              ; fourth cell's glyph
53BD: 23              INC     HL                  
53BE: 46              LD      B,(HL)              ; its attribute
53BF: 23              INC     HL                  
53C0: A7              AND     A                   ; glyph zero?
53C1: 28 10           JR      Z,$53D3             ; {code.loc_53d3} transparent: skip it
53C3: E5              PUSH    HL                  
53C4: 2A 00 AE        LD      HL,($AE00)          ; {hard.workRam+600} the list tail
53C7: 73              LD      (HL),E              ; cell address low byte
53C8: 2C              INC     L                   
53C9: 72              LD      (HL),D              ; high byte
53CA: 2C              INC     L                   
53CB: 77              LD      (HL),A              ; glyph
53CC: 2C              INC     L                   
53CD: 70              LD      (HL),B              ; attribute
53CE: 2C              INC     L                   
53CF: 22 00 AE        LD      ($AE00),HL          ; {hard.workRam+600} store the advanced tail
53D2: E1              POP     HL                  

loc_53d3:
53D3: C9              RET                         

; ---- $53D4-$55D3: data ----
53D4: 24 20 00 00 00 00 00 00 DD 20 00 00 00 00 00 00
53E4: 61 20 00 00 00 00 00 00 3C 20 00 00 00 00 00 00
53F4: 61 60 00 00 00 00 00 00 DD 60 00 00 00 00 00 00
5404: 24 60 00 00 00 00 00 00 39 20 39 60 00 00 00 00
5414: 30 20 00 00 00 00 00 00 A1 20 00 00 00 00 00 00
5424: B7 20 00 00 00 00 00 00 D0 20 00 00 00 00 00 00
5434: B7 60 00 00 00 00 00 00 A1 60 00 00 00 00 00 00
5444: 30 60 00 00 00 00 00 00 6D 20 6D 60 00 00 00 00
5454: 40 20 00 00 00 00 00 00 34 20 00 00 00 00 00 00
5464: 2B 20 00 00 00 00 00 00 B1 20 00 00 00 00 00 00
5474: 2B 60 00 00 00 00 00 00 34 60 00 00 00 00 00 00
5484: 40 60 00 00 00 00 00 00 8E 20 8E 60 00 00 00 00
5494: 74 20 00 00 00 00 00 00 54 20 00 00 00 00 00 00
54A4: 4C 20 00 00 00 00 00 00 2D 20 00 00 00 00 00 00
54B4: 4C 60 00 00 00 00 00 00 54 60 00 00 00 00 00 00
54C4: 74 60 00 00 00 00 00 00 D5 20 D5 60 00 00 00 00
54D4: 40 A0 00 00 00 00 00 00 34 A0 00 00 00 00 00 00
54E4: 2B A0 00 00 00 00 00 00 B1 A0 00 00 00 00 00 00
54F4: 2B E0 00 00 00 00 00 00 34 E0 00 00 00 00 00 00
5504: 40 E0 00 00 00 00 00 00 8E A0 8E E0 00 00 00 00
5514: 30 A0 00 00 00 00 00 00 A1 A0 00 00 00 00 00 00
5524: B7 A0 00 00 00 00 00 00 D0 A0 00 00 00 00 00 00
5534: B7 E0 00 00 00 00 00 00 A1 E0 00 00 00 00 00 00
5544: 30 E0 00 00 00 00 00 00 6D A0 6D E0 00 00 00 00
5554: 24 A0 00 00 00 00 00 00 DD A0 00 00 00 00 00 00
5564: 61 A0 00 00 00 00 00 00 3C A0 00 00 00 00 00 00
5574: 61 E0 00 00 00 00 00 00 DD E0 00 00 00 00 00 00
5584: 24 E0 00 00 00 00 00 00 39 A0 39 E0 00 00 00 00
5594: 3A 20 00 00 3A A0 00 00 8F 20 00 00 8F A0 00 00
55A4: 70 20 00 00 70 A0 00 00 66 20 00 00 66 A0 00 00
55B4: 70 60 00 00 70 E0 00 00 8F 60 00 00 8F E0 00 00
55C4: 3A 60 00 00 3A E0 00 00 C7 20 C7 60 C7 A0 C7 E0

; send the byte at the head of the pending-sound queue, then close the gap
; it left: a count cell at 0xAC43 says how many bytes are waiting and the
; bytes follow it from 0xAC44, and a count of zero is left untouched with
; nothing going out. Otherwise the count comes down by one, the head byte
; goes out, and every byte still waiting slides one place down so the head
; slot always holds the next one. The send happens whether or not anything
; is left to slide, so emptying the queue costs no slide; and nothing
; bounds the count, so a large one slides bytes in from past the queue's
; own cells
sendOldestQueuedSoundCommand:
55D4: 21 43 AC        LD      HL,$AC43            ; point at the pending-sound queue's count
55D7: 7E              LD      A,(HL)              ; how many are waiting
55D8: A7              AND     A                   ; any?
55D9: C8              RET     Z                   ; none: nothing to send
55DA: 35              DEC     (HL)                ; drop the count by one
55DB: F5              PUSH    AF                  ; remember whether that emptied the queue
55DC: 23              INC     HL                  ; point at the head byte
55DD: 7E              LD      A,(HL)              ; the oldest queued sound code
55DE: CD F8 55        CALL    $55F8               ; {code.sendSoundCommand} hand it to the audio processor
55E1: F1              POP     AF                  ; recover the emptied-queue flag
55E2: C8              RET     Z                   ; that was the last: nothing to slide, done
55E3: 3D              DEC     A                   ; one fewer byte still queued
55E4: 06 00           LD      B,$00               
55E6: 4F              LD      C,A                 ; that many bytes to slide
55E7: 5D              LD      E,L                 ; destination is the head slot
55E8: 54              LD      D,H                 
55E9: 23              INC     HL                  ; source is the byte after it
55EA: ED B0           LDIR                        ; slide every remaining byte down one, so the head holds the next code
55EC: C9              RET                         

; ---- $55ED-$55F7: data ----
55ED: 73 A6 14 7E 29 F8 96 5D 17 9B B9

; hand one byte to the audio processor: write it into the one-byte latch
; that processor reads, then drive its attention line high and back low,
; the edge that makes it look
sendSoundCommand:
55F8: 32 00 C0        LD      ($C000),A           ; drop the byte into the audio processor's command latch
55FB: 3E 01           LD      A,$01               ; raise
55FD: 32 04 C3        LD      ($C304),A           ; the audio processor's attention line
5600: 00              NOP                         ; idle -- widen the attention pulse
5601: 00              NOP                         
5602: 00              NOP                         
5603: 00              NOP                         
5604: 00              NOP                         
5605: 00              NOP                         
5606: 3E 00           LD      A,$00               ; then drive
5608: 32 04 C3        LD      ($C304),A           ; the attention line back low -- the high-to-low edge is what it notices
560B: C9              RET                         

; queue a sound code, but only while a game is being played; with the play
; flag clear the request is dropped and nothing is left behind for a later
; frame
enqueueSoundIfGameInProgress:
560C: E5              PUSH    HL                  ; save the caller's pointer
560D: F5              PUSH    AF                  ; hold the requested sound code
560E: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} the play-in-progress flag
5611: A7              AND     A                   ; is a game running?
5612: 20 16           JR      NZ,$562A            ; {code.loc_562a} running: go queue the code
5614: F1              POP     AF                  ; not running: drop the request silently and return
5615: E1              POP     HL                  
5616: C9              RET                         

; queue a sound code when either the play flag or the cell at 0xA9C6 is
; set; only with both clear is the request dropped
enqueueSoundIfGameOrAttract:
5617: E5              PUSH    HL                  ; save the caller's pointer
5618: F5              PUSH    AF                  ; hold the requested sound code
5619: 3A 30 AD        LD      A,($AD30)           ; {hard.workRam+530} the play-in-progress flag
561C: A7              AND     A                   ; is a game running?
561D: 20 0B           JR      NZ,$562A            ; {code.loc_562a} running: go queue the code
561F: 3A C6 A9        LD      A,($A9C6)           ; {hard.workRam+1C6} the attract-loop sound-enable flag
5622: A7              AND     A                   ; set?
5623: 20 05           JR      NZ,$562A            ; {code.loc_562a} set: queue it even with no game running
5625: F1              POP     AF                  ; neither: drop the request and return
5626: E1              POP     HL                  
5627: C9              RET                         

; queue a sound code with no permission test, so it is queued whether or
; not a game is being played
enqueueSoundUnconditional:
5628: E5              PUSH    HL                  
5629: F5              PUSH    AF                  ; hold the sound code, then fall into the shared queue tail

loc_562a:
562A: 21 43 AC        LD      HL,$AC43            ; the pending-sound queue's count
562D: 34              INC     (HL)                ; one more entry
562E: 7E              LD      A,(HL)              ; the new count
562F: CF              RST     $08                 ; index that many past the count -- the new tail slot
5630: F1              POP     AF                  ; recover the code
5631: 77              LD      (HL),A              ; store it at the tail
5632: E1              POP     HL                  
5633: C9              RET                         

; queue seven sound codes back to back with no play test: six fetched one
; each from its own cell of the program image, so an edit to the image
; changes what is asked for, and a seventh formed by adding the era index
; to a fixed base
enqueueTransitionSoundBurst:
5634: 3A 7C 16        LD      A,($167C)           ; {hard.rom+167C} a sound code from the program image
5637: CD 28 56        CALL    $5628               ; {code.enqueueSoundUnconditional} queue it, no permission test
563A: 3A 9C 0A        LD      A,($0A9C)           ; {hard.rom+A9C} the next code
563D: CD 28 56        CALL    $5628               ; {code.enqueueSoundUnconditional} queue it
5640: 3A 84 14        LD      A,($1484)           ; {hard.rom+1484} the next code
5643: CD 28 56        CALL    $5628               ; {code.enqueueSoundUnconditional} queue it
5646: 3A 78 0C        LD      A,($0C78)           ; {hard.rom+C78} the next code
5649: CD 28 56        CALL    $5628               ; {code.enqueueSoundUnconditional} queue it
564C: 3A D3 07        LD      A,($07D3)           ; {hard.rom+7D3} the next code
564F: CD 28 56        CALL    $5628               ; {code.enqueueSoundUnconditional} queue it
5652: 3A B4 33        LD      A,($33B4)           ; {hard.rom+33B4} the next code
5655: CD 28 56        CALL    $5628               ; {code.enqueueSoundUnconditional} queue it
5658: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} the current era index
565B: C6 8C           ADD     A,$8C               ; offset it to an era-specific code
565D: 18 C9           JR      $5628               ; {code.enqueueSoundUnconditional} queue that one too

; read the byte at 0x07A2 and request it as a sound code, only while a
; game is being played
requestEnemyLaunchSound:
565F: 3A A2 07        LD      A,($07A2)           ; {hard.rom+7A2} a sound code from the program image
5662: 18 A8           JR      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; read the byte at 0x16DE and request it as a sound code, only while a
; game is being played
requestAttackerSpawnSoundEra0:
5664: 3A DE 16        LD      A,($16DE)           ; {hard.rom+16DE} a sound code from the program image
5667: 18 A3           JR      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; read the byte at 0x4C9F and request it as a sound code, only while a
; game is being played
requestEnemyLaunchSoundLateEra:
5669: 3A 9F 4C        LD      A,($4C9F)           ; {hard.rom+4C9F} a sound code from the program image
566C: 18 9E           JR      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; ask for two sounds in a row, each code fetched from its own byte of the
; program image, both admitted only while a game is being played
requestTwoSoundsWhilePlaying:
566E: 3A D8 07        LD      A,($07D8)           ; {hard.rom+7D8} first sound code from the program image
5671: CD 0C 56        CALL    $560C               ; {code.enqueueSoundIfGameInProgress} request it while a game runs, then fall into the next request

; read the byte at 0x276B and request it as a sound code, only while a
; game is being played
requestAttackerSpawnSoundLateEra:
5674: 3A 6B 27        LD      A,($276B)           ; {hard.rom+276B} a sound code from the program image
5677: 18 93           JR      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; read the byte at 0x07FE and request it as a sound code, only while a
; game is being played
requestLateEraProgressSound:
5679: 3A FE 07        LD      A,($07FE)           ; {hard.rom+7FE} a sound code from the program image
567C: 18 8E           JR      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; read the byte at 0x3270 and request it as a sound code, admitted while a
; game is being played or the cell at 0xA9C6 is set
requestPlayerShotSound:
567E: 3A 70 32        LD      A,($3270)           ; {hard.rom+3270} a sound code from the program image
5681: 18 94           JR      $5617               ; {code.enqueueSoundIfGameOrAttract} request it while a game runs or attract sound is enabled

; request two sounds in a row, each code fetched from its own byte of the
; program image, both admitted by the shared play-or-demo permission
requestTwoSounds:
5683: 3A A6 07        LD      A,($07A6)           ; {hard.rom+7A6} first sound code from the program image
5686: CD 17 56        CALL    $5617               ; {code.enqueueSoundIfGameOrAttract} request it -- game or attract sound
5689: 3A DA 4C        LD      A,($4CDA)           ; {hard.rom+4CDA} second sound code from the program image
568C: 18 89           JR      $5617               ; {code.enqueueSoundIfGameOrAttract} request it -- game or attract sound

loc_568e:
568E: 3A 87 2D        LD      A,($2D87)           ; {hard.rom+2D87} a sound code from the program image
5691: C3 0C 56        JP      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

loc_5694:
5694: 0E 00           LD      C,$00               
5696: 21 31 08        LD      HL,$0831            ; a block of the program image
5699: 3A AB A9        LD      A,($A9AB)           ; {hard.workRam+1AB} start from the current sequence phase

loc_569c:
569C: 96              SUB     (HL)                ; subtract each image byte in turn
569D: 23              INC     HL                  
569E: 0D              DEC     C                   
569F: 20 FB           JR      NZ,$569C            ; {code.loc_569c}
56A1: EE C2           XOR     $C2                 ; fold in a trailing constant -- on an intact image this nets to the phase the sequence wants
56A3: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} store it back as the sequence phase -- a patched image lands in a different phase instead of failing
56A6: CD 97 0F        CALL    $0F97               ; {code.multiplexSpriteSlotsSkipping} multiplex the object list onto the eight hardware sprite slots
56A9: CD DF 1E        CALL    $1EDF               ; {code.dispatchPlayerFrameByState} advance the player by its state
56AC: CD 97 0F        CALL    $0F97               ; {code.multiplexSpriteSlotsSkipping} multiplex the sprite slots again
56AF: CD BC 2C        CALL    $2CBC               ; {code.runSceneryForEra} run the era's scrolling scenery
56B2: CD E3 23        CALL    $23E3               ; {code.fireAndSweepPlayerShots} advance the player's shots
56B5: CD 98 10        CALL    $1098               ; {code.multiplexSpriteSlots} multiplex the sprite slots once more
56B8: 21 EB A9        LD      HL,$A9EB            ; the sequence delay counter
56BB: 35              DEC     (HL)                ; count down one frame
56BC: C0              RET     NZ                  ; not expired yet: done
56BD: 0E 00           LD      C,$00               
56BF: 21 A7 12        LD      HL,$12A7            ; a second block of the program image
56C2: 3A AB A9        LD      A,($A9AB)           ; {hard.workRam+1AB} the sequence phase again

loc_56c5:
56C5: 96              SUB     (HL)                ; subtract each byte
56C6: 23              INC     HL                  
56C7: 0D              DEC     C                   
56C8: 20 FB           JR      NZ,$56C5            ; {code.loc_56c5}
56CA: EE 59           XOR     $59                 ; fold in its trailing constant
56CC: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} store back to the sequence phase
56CF: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence to its next sub-step

; ask for three sounds whose codes come from bytes of the program image,
; all three refused unless a game is being played, then leave through the
; two-request tail whose permission is looser -- so a state that drops the
; three can still admit the pair
requestRoundIntroSoundBurst:
56D2: 3A 5B 0C        LD      A,($0C5B)           ; {hard.rom+C5B} first sound code from the program image
56D5: CD 0C 56        CALL    $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress
56D8: 3A 55 08        LD      A,($0855)           ; {hard.rom+855} second sound code from the program image
56DB: CD 0C 56        CALL    $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress
56DE: 3A 75 16        LD      A,($1675)           ; {hard.rom+1675} third sound code from the program image
56E1: CD 0C 56        CALL    $560C               ; {code.enqueueSoundIfGameInProgress} request it while a game runs, then fall into the inter-round pair

; read the byte at 0x27CB and request it as a sound code, then do the same
; with the byte at 0x33A0; each request goes through the door at 0x5617,
; which admits it while a game is being played or while the cell at 0xA9C6
; is set. It is reached two ways -- as a call from
; advanceScriptedCharPlaneBandTo4, in the arm that steps that routine's
; script pointer on, and by falling out of the bottom of
; requestRoundIntroSoundBurst, which has just asked for three other codes
; through the play-only door at 0x560C -- and it is the same two-load,
; two-request shape as requestTwoSounds at 0x5683 with a different pair of
; program bytes
requestInterRoundSoundPair:
56E4: 3A CB 27        LD      A,($27CB)           ; {hard.rom+27CB} first sound code from the program image
56E7: CD 17 56        CALL    $5617               ; {code.enqueueSoundIfGameOrAttract} request it -- game or attract sound
56EA: 3A A0 33        LD      A,($33A0)           ; {hard.rom+33A0} second sound code from the program image
56ED: C3 17 56        JP      $5617               ; {code.enqueueSoundIfGameOrAttract} request it -- game or attract sound

; ---- $56F0-$57F0: data ----
56F0: FF 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00
5700: 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00
5710: 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00
5720: 00 01 00 00 00 00 00 00 00 00 00 00 00 00 01 00
5730: 00 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00
5740: 00 00 01 01 00 00 00 00 00 00 00 00 01 00 00 00
5750: 00 00 00 01 01 01 00 00 00 00 00 00 00 00 00 00
5760: 00 00 00 00 00 01 01 01 01 00 01 00 00 00 00 00
5770: 00 00 00 00 00 00 00 00 00 01 01 00 00 00 00 00
5780: 00 00 00 00 00 00 00 00 01 00 01 00 00 00 00 00
5790: 00 00 00 00 00 00 00 01 00 00 01 01 00 00 00 00
57A0: 00 00 00 00 00 00 01 01 00 00 00 01 01 01 00 00
57B0: 00 00 00 00 01 01 00 01 01 00 00 00 00 01 01 00
57C0: 00 00 00 01 01 01 00 00 01 01 01 00 00 00 00 00
57D0: 00 00 01 01 00 01 01 00 00 00 00 00 00 00 00 00
57E0: 00 01 00 01 00 00 00 00 00 00 00 00 00 00 00 00
57F0: FF

; read the byte at 0x322E and request it as a sound code, with no
; permission test
requestCoinSound:
57F1: 3A 2E 32        LD      A,($322E)           ; {hard.rom+322E} fetch the coin sound code from the program image
57F4: C3 28 56        JP      $5628               ; {code.enqueueSoundUnconditional} request it with no permission test -- it sounds whether or not a game is running

; request the sound code that the era index selects out of a run beginning
; twelve codes up, only while a game is being played; the sum is not
; clamped
requestCurrentEraSound:
57F7: 3A 04 AD        LD      A,($AD04)           ; {hard.workRam+504} read the current era index
57FA: C6 0C           ADD     A,$0C               ; offset it twelve codes up -- each era selects its own sound
57FC: C3 0C 56        JP      $560C               ; {code.enqueueSoundIfGameInProgress} request that sound, only while a game is in progress

; read the byte at 0x079B and request it as a sound code, only while a
; game is being played
requestParachutistAwardSound:
57FF: 3A 9B 07        LD      A,($079B)           ; {hard.rom+79B} fetch the parachutist-award sound code from the program image
5802: C3 0C 56        JP      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; read the byte at 0x2D4E and request it as a sound code, only while a
; game is being played
requestBonusLifeSound:
5805: 3A 4E 2D        LD      A,($2D4E)           ; {hard.rom+2D4E} fetch the bonus-life sound code from the program image
5808: C3 0C 56        JP      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; read the byte at 0x49EE and request it as a sound code, only while a
; game is being played
requestMotherShipWarpSound:
580B: 3A EE 49        LD      A,($49EE)           ; {hard.rom+49EE} fetch the mother-ship warp sound code from the program image
580E: C3 0C 56        JP      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; read the byte at 0x07A9 and request it as a sound code, only while a
; game is being played
requestPlayerSpawnFlashSound:
5811: 3A A9 07        LD      A,($07A9)           ; {hard.rom+7A9} fetch the player-spawn flash sound code from the program image
5814: C3 0C 56        JP      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; read the byte at 0x273A and request it as a sound code, only while a
; game is being played
requestEnemyWaveSound:
5817: 3A 3A 27        LD      A,($273A)           ; {hard.rom+273A} fetch the enemy-wave sound code from the program image
581A: C3 0C 56        JP      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; ---- $581D-$5833: data ----
581D: 0C A7 13 88 57 34 A5 ED 34 F1 87 34 88 68 ED FD
582D: DC F1 77 68 FD 3B B9

; read the byte at 0x1767 and request it as a sound code, only while a
; game is being played
requestRoundStartSound:
5834: 3A 67 17        LD      A,($1767)           ; {hard.rom+1767} fetch the round-start sound code from the program image
5837: C3 0C 56        JP      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

loc_583a:
583A: 3A FA 18        LD      A,($18FA)           ; {hard.rom+18FA} fetch another sound code from the program image
583D: C3 0C 56        JP      $560C               ; {code.enqueueSoundIfGameInProgress} request it, only while a game is in progress

; fly one object a single step at the slowest of the velocity-table
; speeds, choosing that table for the flier and deciding nothing else;
; reached as a call from two per-slot actor handlers and as a tail jump
; from a third
flyAtSlowestSpeed:
5840: 21 D7 59        LD      HL,$59D7            ; point at the slowest velocity table
5843: C3 BC 58        JP      $58BC               ; {code.flyAlongHeading} fly the object one step along its heading using that table

; ---- $5846-$5853: data ----
5846: 21 00 5C C3 BC 58 60 A7 14 96 10 0D 88 B9

loc_5854:
5854: 21 00 5E        LD      HL,$5E00            ; point at a velocity table
5857: C3 BC 58        JP      $58BC               ; {code.flyAlongHeading} fly the object one step along its heading using that table

; ---- $585A-$585F: data ----
585A: 21 30 25 C3 BC 58

loc_5860:
5860: 21 3E 2E        LD      HL,$2E3E            ; point at a velocity table
5863: C3 BC 58        JP      $58BC               ; {code.flyAlongHeading} fly the object one step along its heading using that table

; cold-start clear then ROM tamper check: fill colour RAM 0xA000-0xA3FF
; with 0x10 and video RAM 0xA400-0xA7FF with 0xf1 (bases from ROM pointers
; at 0x2581/0x4A37), sum the whole program ROM 0x0000-0x5FFF and test the
; total against 0xAF, kicking the watchdog after the first fill and once
; per summed byte; a genuine image tail-calls cold-start init, a tampered
; one derails into data at 0x59D7
clearScreenRamAndVerifyImageThenColdInit:
5866: 2A 81 25        LD      HL,($2581)          ; {hard.rom+2581} take the colour-RAM base from the program image
5869: 01 00 04        LD      BC,$0400            ; 0x400 bytes to fill
586C: 16 10           LD      D,$10               ; the colour fill value

loc_586e:
586E: 72              LD      (HL),D              ; store the fill byte
586F: 23              INC     HL                  
5870: 0B              DEC     BC                  ; count one cell down
5871: 79              LD      A,C                 
5872: B0              OR      B                   ; test the 16-bit count for zero
5873: 20 F9           JR      NZ,$586E            ; {code.loc_586e} loop until colour RAM is filled
5875: 32 00 C2        LD      ($C200),A           ; kick the watchdog -- colour fill done
5878: 2A 37 4A        LD      HL,($4A37)          ; {hard.rom+4A37} take the video-RAM base from the program image
587B: 01 00 04        LD      BC,$0400            ; 0x400 bytes to fill
587E: 16 F1           LD      D,$F1               ; the video fill value -- a blank tile

loc_5880:
5880: 72              LD      (HL),D              ; store the fill byte
5881: 23              INC     HL                  
5882: 0B              DEC     BC                  ; count one cell down
5883: 79              LD      A,C                 
5884: B0              OR      B                   ; test the 16-bit count for zero
5885: 20 F9           JR      NZ,$5880            ; {code.loc_5880} loop until video RAM is filled
5887: 21 00 00        LD      HL,$0000            ; point at the start of the program image
588A: 3A 00 00        LD      A,($0000)           ; {hard.rom} seed the running total with the first program byte

loc_588d:
588D: 86              ADD     A,(HL)              ; add this program byte into the total
588E: 23              INC     HL                  
588F: 08              EX      AF,AF'              ; keep the total safe while the pointer is tested
5890: 7C              LD      A,H                 ; take the pointer's high byte
5891: FE 60           CP      $60                 ; past the last program page (0x60)?
5893: 30 06           JR      NC,$589B            ; {code.loc_589b} image exhausted: go check the total
5895: 08              EX      AF,AF'              ; bring the total back
5896: 32 00 C2        LD      ($C200),A           ; kick the watchdog -- once per summed byte
5899: 18 F2           JR      $588D               ; {code.loc_588d} keep summing

loc_589b:
589B: 08              EX      AF,AF'              ; bring the total back
589C: D6 AF           SUB     $AF                 ; subtract the value a genuine image sums to
589E: C2 D7 59        JP      NZ,$59D7            ; {code.loc_59d7} a tampered image derails into the velocity-table data
58A1: C3 11 25        JP      $2511               ; {code.initColdStartRamThenSeedConfig} a genuine image hands on to cold-start init

loc_58a4:
58A4: 21 FA 08        LD      HL,$08FA            ; point at a velocity table
58A7: C3 BC 58        JP      $58BC               ; {code.flyAlongHeading} fly the object one step along its heading using that table

loc_58aa:
58AA: 21 D7 59        LD      HL,$59D7            ; point at the slowest velocity table
58AD: C3 FE 58        JP      $58FE               ; {code.flyAlongHeadingAtDoubleVelocity} fly the object one step at double velocity using that table

; ---- $58B0-$58B5: data ----
58B0: 21 00 5C C3 FE 58

loc_58b6:
58B6: 21 00 5E        LD      HL,$5E00            ; point at a velocity table
58B9: C3 FE 58        JP      $58FE               ; {code.flyAlongHeadingAtDoubleVelocity} fly the object one step at double velocity using that table

; fly one object a single step along the heading it holds, and in the same
; add carry it with the world: each coordinate gains its own velocity
; component PLUS the shared per-frame scroll pair, so nothing else may
; drift this object
flyAlongHeading:
58BC: DD 7E 02        LD      A,(IX+$02)          ; read this object's heading
58BF: 4F              LD      C,A                 ; hold the heading for the perpendicular sample
58C0: 87              ADD     A,A                 ; double the heading -- two bytes per table entry
58C1: 30 01           JR      NC,$58C4            ; {code.loc_58c4}
58C3: 24              INC     H                   

loc_58c4:
58C4: 85              ADD     A,L                 
58C5: 6F              LD      L,A                 
58C6: 30 01           JR      NC,$58C9            ; {code.loc_58c9}
58C8: 24              INC     H                   

loc_58c9:
58C9: 5E              LD      E,(HL)              ; read the low byte of the velocity component at the heading
58CA: 23              INC     HL                  
58CB: 56              LD      D,(HL)              ; read its high byte
58CC: 79              LD      A,C                 ; recall the heading
58CD: C6 C0           ADD     A,$C0               ; step a quarter turn back -- the perpendicular partner
58CF: 01 80 01        LD      BC,$0180            ; offset to that perpendicular sample
58D2: 30 03           JR      NC,$58D7            ; {code.loc_58d7}
58D4: 01 80 FF        LD      BC,$FF80            ; or offset back when the quarter-turn index wrapped

loc_58d7:
58D7: 09              ADD     HL,BC               ; reach the perpendicular sample
58D8: 46              LD      B,(HL)              ; read its high byte
58D9: 2B              DEC     HL                  
58DA: 4E              LD      C,(HL)              ; read its low byte -- the second component
58DB: 2A 08 A8        LD      HL,($A808)          ; {hard.workRam+8} take the shared per-frame vertical world-scroll
58DE: 19              ADD     HL,DE               ; add this object's first-axis component
58DF: DD 5E 03        LD      E,(IX+$03)          ; read the fraction of the first coordinate
58E2: FD 56 31        LD      D,(IY+$31)          ; read its whole part from the sprite entry
58E5: 19              ADD     HL,DE               ; add the displacement onto the coordinate
58E6: DD 75 03        LD      (IX+$03),L          ; store the new fraction
58E9: FD 74 31        LD      (IY+$31),H          ; store the new whole part into the sprite entry
58EC: 2A 0A A8        LD      HL,($A80A)          ; {hard.workRam+A} take the shared per-frame horizontal world-scroll
58EF: 09              ADD     HL,BC               ; add this object's second-axis component
58F0: DD 5E 05        LD      E,(IX+$05)          ; read the fraction of the second coordinate
58F3: FD 56 00        LD      D,(IY+$00)          ; read its whole part from the sprite entry
58F6: 19              ADD     HL,DE               ; add the displacement onto the coordinate
58F7: DD 75 05        LD      (IX+$05),L          ; store the new fraction
58FA: FD 74 00        LD      (IY+$00),H          ; store the new whole part into the sprite entry
58FD: C9              RET                         

; fly one object a single step along the heading it holds, with TWICE its
; own velocity component and the shared world scroll added once, so
; nothing else may drift this object
flyAlongHeadingAtDoubleVelocity:
58FE: DD 7E 02        LD      A,(IX+$02)          ; read this object's heading
5901: 4F              LD      C,A                 ; hold the heading for the perpendicular sample
5902: 87              ADD     A,A                 ; double the heading -- two bytes per table entry
5903: 30 01           JR      NC,$5906            ; {code.loc_5906}
5905: 24              INC     H                   

loc_5906:
5906: 85              ADD     A,L                 
5907: 6F              LD      L,A                 
5908: 30 01           JR      NC,$590B            ; {code.loc_590b}
590A: 24              INC     H                   

loc_590b:
590B: 5E              LD      E,(HL)              ; read the low byte of the velocity component at the heading
590C: 23              INC     HL                  
590D: 56              LD      D,(HL)              ; read its high byte
590E: 79              LD      A,C                 ; recall the heading
590F: C6 C0           ADD     A,$C0               ; step a quarter turn back -- the perpendicular partner
5911: 01 80 01        LD      BC,$0180            ; offset to that perpendicular sample
5914: 30 03           JR      NC,$5919            ; {code.loc_5919}
5916: 01 80 FF        LD      BC,$FF80            ; or offset back when the quarter-turn index wrapped

loc_5919:
5919: 09              ADD     HL,BC               ; reach the perpendicular sample
591A: 46              LD      B,(HL)              ; read its high byte
591B: 2B              DEC     HL                  
591C: 4E              LD      C,(HL)              ; read its low byte -- the second component
591D: 2A 08 A8        LD      HL,($A808)          ; {hard.workRam+8} take the shared per-frame vertical world-scroll
5920: 19              ADD     HL,DE               ; add this object's first-axis component
5921: 19              ADD     HL,DE               ; add it again -- twice this object's own speed
5922: DD 5E 03        LD      E,(IX+$03)          ; read the fraction of the first coordinate
5925: FD 56 31        LD      D,(IY+$31)          ; read its whole part from the sprite entry
5928: 19              ADD     HL,DE               ; add the displacement onto the coordinate
5929: DD 75 03        LD      (IX+$03),L          ; store the new fraction
592C: FD 74 31        LD      (IY+$31),H          ; store the new whole part into the sprite entry
592F: 2A 0A A8        LD      HL,($A80A)          ; {hard.workRam+A} take the shared per-frame horizontal world-scroll
5932: 09              ADD     HL,BC               ; add this object's second-axis component
5933: 09              ADD     HL,BC               ; add it again -- twice this object's own speed
5934: DD 5E 05        LD      E,(IX+$05)          ; read the fraction of the second coordinate
5937: FD 56 00        LD      D,(IY+$00)          ; read its whole part from the sprite entry
593A: 19              ADD     HL,DE               ; add the displacement onto the coordinate
593B: DD 75 05        LD      (IX+$05),L          ; store the new fraction
593E: FD 74 00        LD      (IY+$00),H          ; store the new whole part into the sprite entry
5941: C9              RET                         

loc_5942:
5942: 21 D7 59        LD      HL,$59D7            ; point at the slowest velocity table
5945: C3 6E 59        JP      $596E               ; {code.velocityForHeading} look up the velocity vector for the heading using that table

; ---- $5948-$594D: data ----
5948: 21 00 5C C3 6E 59

loc_594e:
594E: 21 00 5E        LD      HL,$5E00            ; point at a velocity table
5951: C3 6E 59        JP      $596E               ; {code.velocityForHeading} look up the velocity vector for the heading using that table

; ---- $5954-$5964: data ----
5954: 73 A6 14 7E 29 F8 96 5D 02 13 B9 21 30 25 C3 6E
5964: 59

loc_5965:
5965: 21 3E 2E        LD      HL,$2E3E            ; point at a velocity table
5968: C3 6E 59        JP      $596E               ; {code.velocityForHeading} look up the velocity vector for the heading using that table

loc_596b:
596B: 21 FA 08        LD      HL,$08FA            ; point at a velocity table, then look up the velocity vector for the heading

; look up the velocity vector for a heading: two perpendicular components
; a quarter turn apart, read from the table the caller supplies
velocityForHeading:
596E: DD 7E 02        LD      A,(IX+$02)          ; read this object's heading
5971: 4F              LD      C,A                 ; hold the heading for the perpendicular sample
5972: 87              ADD     A,A                 ; double the heading -- two bytes per table entry
5973: 30 01           JR      NC,$5976            ; {code.loc_5976}
5975: 24              INC     H                   

loc_5976:
5976: 85              ADD     A,L                 
5977: 6F              LD      L,A                 
5978: 30 01           JR      NC,$597B            ; {code.loc_597b}
597A: 24              INC     H                   

loc_597b:
597B: 5E              LD      E,(HL)              ; read the low byte of the velocity component at the heading
597C: 23              INC     HL                  
597D: 56              LD      D,(HL)              ; read its high byte -- the component at the heading
597E: 79              LD      A,C                 ; recall the heading
597F: C6 C0           ADD     A,$C0               ; step a quarter turn back -- the perpendicular partner
5981: 01 80 01        LD      BC,$0180            ; offset to that perpendicular sample
5984: 30 03           JR      NC,$5989            ; {code.loc_5989}
5986: 01 80 FF        LD      BC,$FF80            ; or offset back when the quarter-turn index wrapped

loc_5989:
5989: 09              ADD     HL,BC               ; reach the perpendicular sample
598A: 46              LD      B,(HL)              ; read its high byte
598B: 2B              DEC     HL                  
598C: 4E              LD      C,(HL)              ; read its low byte -- the perpendicular component
598D: C9              RET                         

loc_598e:
598E: 21 D7 59        LD      HL,$59D7            ; point at the slowest velocity table
5991: C3 9D 59        JP      $599D               ; {code.loc_599d} read that table's doubled velocity for this object's heading

loc_5994:
5994: 21 00 5C        LD      HL,$5C00            ; point at a velocity table
5997: C3 9D 59        JP      $599D               ; {code.loc_599d} read that table's doubled velocity for this object's heading

; ---- $599A-$599C: data ----
599A: 21 00 5E

loc_599d:
599D: DD 7E 02        LD      A,(IX+$02)          ; read this object's heading, then take the doubled velocity for it

; turn a heading handed straight in into the velocity pair the caller's
; table gives for it, doubled; the doubling wraps at sixteen bits and
; nothing is written
doubledVelocityForHeading:
59A0: 4F              LD      C,A                 ; hold the heading for the perpendicular sample
59A1: 87              ADD     A,A                 ; double the heading -- two bytes per table entry
59A2: 30 01           JR      NC,$59A5            ; {code.loc_59a5}
59A4: 24              INC     H                   

loc_59a5:
59A5: 85              ADD     A,L                 
59A6: 6F              LD      L,A                 
59A7: 30 01           JR      NC,$59AA            ; {code.loc_59aa}
59A9: 24              INC     H                   

loc_59aa:
59AA: 5E              LD      E,(HL)              ; read the low byte of the velocity component at the heading
59AB: 23              INC     HL                  
59AC: 56              LD      D,(HL)              ; read its high byte -- the component at the heading
59AD: CB 23           SLA     E                   ; double the component low byte
59AF: CB 12           RL      D                   ; carry into the high byte -- twice the table's length
59B1: 79              LD      A,C                 ; recall the heading
59B2: C6 C0           ADD     A,$C0               ; step a quarter turn back -- the perpendicular partner
59B4: 01 80 01        LD      BC,$0180            ; offset to that perpendicular sample
59B7: 30 03           JR      NC,$59BC            ; {code.loc_59bc}
59B9: 01 80 FF        LD      BC,$FF80            ; or offset back when the quarter-turn index wrapped

loc_59bc:
59BC: 09              ADD     HL,BC               ; reach the perpendicular sample
59BD: 46              LD      B,(HL)              ; read its high byte
59BE: 2B              DEC     HL                  
59BF: 4E              LD      C,(HL)              ; read its low byte -- the perpendicular component
59C0: CB 21           SLA     C                   ; double the component low byte
59C2: CB 10           RL      B                   ; carry into the high byte -- twice the table's length
59C4: C9              RET                         

loc_59c5:
59C5: 21 D7 59        LD      HL,$59D7            ; point at the slowest velocity table
59C8: C3 A0 59        JP      $59A0               ; {code.doubledVelocityForHeading} take that table's doubled velocity for the heading in A

loc_59cb:
59CB: 21 00 5C        LD      HL,$5C00            ; point at a velocity table
59CE: C3 A0 59        JP      $59A0               ; {code.doubledVelocityForHeading} take that table's doubled velocity for the heading in A

loc_59d1:
59D1: 21 00 5E        LD      HL,$5E00            ; point at a velocity table
59D4: C3 A0 59        JP      $59A0               ; {code.doubledVelocityForHeading} take that table's doubled velocity for the heading in A

loc_59d7:
59D7: CE 00           ADC     A,$00               
59D9: CD 00 CC        CALL    $CC00               
59DC: 00              NOP                         
59DD: CB 00           RLC     B                   
59DF: CA 00 C9        JP      Z,$C900             
59E2: 00              NOP                         
59E3: C8              RET     Z                   
59E4: 00              NOP                         
59E5: C8              RET     Z                   
59E6: 00              NOP                         
59E7: C6 00           ADD     A,$00               
59E9: C4 00 C2        CALL    NZ,$C200            
59EC: 00              NOP                         
59ED: C0              RET     NZ                  
59EE: 00              NOP                         
59EF: BF              CP      A                   
59F0: 00              NOP                         
59F1: BC              CP      H                   
59F2: 00              NOP                         
59F3: BA              CP      D                   
59F4: 00              NOP                         
59F5: B9              CP      C                   
59F6: 00              NOP                         
59F7: B6              OR      (HL)                
59F8: 00              NOP                         
59F9: B3              OR      E                   
59FA: 00              NOP                         
59FB: B0              OR      B                   
59FC: 00              NOP                         
59FD: AF              XOR     A                   
59FE: 00              NOP                         
59FF: AC              XOR     H                   
5A00: 00              NOP                         
5A01: A9              XOR     C                   
5A02: 00              NOP                         
5A03: A8              XOR     B                   
5A04: 00              NOP                         
5A05: A5              AND     L                   
5A06: 00              NOP                         
5A07: A2              AND     D                   
5A08: 00              NOP                         
5A09: A1              AND     C                   
5A0A: 00              NOP                         
5A0B: 9E              SBC     A,(HL)              
5A0C: 00              NOP                         
5A0D: 9B              SBC     A,E                 
5A0E: 00              NOP                         
5A0F: 98              SBC     A,B                 
5A10: 00              NOP                         
5A11: 97              SUB     A                   
5A12: 00              NOP                         
5A13: 94              SUB     H                   
5A14: 00              NOP                         
5A15: 91              SUB     C                   
5A16: 00              NOP                         
5A17: 90              SUB     B                   
5A18: 00              NOP                         
5A19: 8D              ADC     A,L                 
5A1A: 00              NOP                         
5A1B: 89              ADC     A,C                 
5A1C: 00              NOP                         
5A1D: 88              ADC     A,B                 
5A1E: 00              NOP                         
5A1F: 85              ADD     A,L                 
5A20: 00              NOP                         
5A21: 81              ADD     A,C                 
5A22: 00              NOP                         
5A23: 7F              LD      A,A                 
5A24: 00              NOP                         
5A25: 7B              LD      A,E                 
5A26: 00              NOP                         
5A27: 78              LD      A,B                 
5A28: 00              NOP                         
5A29: 76              HALT                        
5A2A: 00              NOP                         
5A2B: 70              LD      (HL),B              
5A2C: 00              NOP                         
5A2D: 6D              LD      L,L                 
5A2E: 00              NOP                         
5A2F: 68              LD      L,B                 
5A30: 00              NOP                         
5A31: 63              LD      H,E                 
5A32: 00              NOP                         
5A33: 60              LD      H,B                 
5A34: 00              NOP                         
5A35: 5C              LD      E,H                 
5A36: 00              NOP                         
5A37: 58              LD      E,B                 
5A38: 00              NOP                         
5A39: 52              LD      D,D                 
5A3A: 00              NOP                         
5A3B: 4E              LD      C,(HL)              
5A3C: 00              NOP                         
5A3D: 49              LD      C,C                 
5A3E: 00              NOP                         
5A3F: 43              LD      B,E                 
5A40: 00              NOP                         
5A41: 3E 00           LD      A,$00               
5A43: 39              ADD     HL,SP               
5A44: 00              NOP                         
5A45: 32 00 2C        LD      ($2C00),A           ; {hard.rom+2C00}
5A48: 00              NOP                         
5A49: 27              DAA                         
5A4A: 00              NOP                         
5A4B: 20 00           JR      NZ,$5A4D            ; {code.loc_5a4d}

loc_5a4d:
5A4D: 1A              LD      A,(DE)              
5A4E: 00              NOP                         
5A4F: 14              INC     D                   
5A50: 00              NOP                         
5A51: 0E 00           LD      C,$00               
5A53: 08              EX      AF,AF'              
5A54: 00              NOP                         
5A55: 00              NOP                         
5A56: 00              NOP                         
5A57: 00              NOP                         
5A58: 00              NOP                         
5A59: F8              RET     M                   
5A5A: FF              RST     $38                 
5A5B: F2 FF 00        JP      P,$00FF             
5A5E: 00              NOP                         
5A5F: E6 FF           AND     $FF                 
5A61: E0              RET     PO                  
5A62: FF              RST     $38                 
5A63: D9              EXX                         
5A64: FF              RST     $38                 
5A65: D4 FF CE        CALL    NC,$CEFF            
5A68: FF              RST     $38                 
5A69: C7              RST     $00                 
5A6A: FF              RST     $38                 
5A6B: C2 FF BD        JP      NZ,$BDFF            
5A6E: FF              RST     $38                 
5A6F: B7              OR      A                   
5A70: FF              RST     $38                 
5A71: B2              OR      D                   
5A72: FF              RST     $38                 
5A73: AE              XOR     (HL)                
5A74: FF              RST     $38                 
5A75: A8              XOR     B                   
5A76: FF              RST     $38                 
5A77: A4              AND     H                   
5A78: FF              RST     $38                 
5A79: A0              AND     B                   
5A7A: FF              RST     $38                 
5A7B: 9D              SBC     A,L                 
5A7C: FF              RST     $38                 
5A7D: A0              AND     B                   
5A7E: FF              RST     $38                 
5A7F: 93              SUB     E                   
5A80: FF              RST     $38                 
5A81: 90              SUB     B                   
5A82: FF              RST     $38                 
5A83: 8A              ADC     A,D                 
5A84: FF              RST     $38                 
5A85: 88              ADC     A,B                 
5A86: FF              RST     $38                 
5A87: 85              ADD     A,L                 
5A88: FF              RST     $38                 
5A89: 81              ADD     A,C                 
5A8A: FF              RST     $38                 
5A8B: 7F              LD      A,A                 
5A8C: FF              RST     $38                 
5A8D: 7B              LD      A,E                 
5A8E: FF              RST     $38                 
5A8F: 78              LD      A,B                 
5A90: FF              RST     $38                 
5A91: 77              LD      (HL),A              
5A92: FF              RST     $38                 
5A93: 73              LD      (HL),E              
5A94: FF              RST     $38                 
5A95: 70              LD      (HL),B              
5A96: FF              RST     $38                 
5A97: 6F              LD      L,A                 
5A98: FF              RST     $38                 
5A99: 6C              LD      L,H                 
5A9A: FF              RST     $38                 
5A9B: 69              LD      L,C                 
5A9C: FF              RST     $38                 
5A9D: 69              LD      L,C                 
5A9E: FF              RST     $38                 
5A9F: 65              LD      H,L                 
5AA0: FF              RST     $38                 
5AA1: 62              LD      H,D                 
5AA2: FF              RST     $38                 
5AA3: 5F              LD      E,A                 
5AA4: FF              RST     $38                 
5AA5: 5E              LD      E,(HL)              
5AA6: FF              RST     $38                 
5AA7: 5B              LD      E,E                 
5AA8: FF              RST     $38                 
5AA9: 58              LD      E,B                 
5AAA: FF              RST     $38                 
5AAB: 57              LD      D,A                 
5AAC: FF              RST     $38                 
5AAD: 54              LD      D,H                 
5AAE: FF              RST     $38                 
5AAF: 51              LD      D,C                 
5AB0: FF              RST     $38                 
5AB1: 50              LD      D,B                 
5AB2: FF              RST     $38                 
5AB3: 4D              LD      C,L                 
5AB4: FF              RST     $38                 
5AB5: 4A              LD      C,D                 
5AB6: FF              RST     $38                 
5AB7: 47              LD      B,A                 
5AB8: FF              RST     $38                 
5AB9: 46              LD      B,(HL)              
5ABA: FF              RST     $38                 
5ABB: 44              LD      B,H                 
5ABC: FF              RST     $38                 
5ABD: 41              LD      B,C                 
5ABE: FF              RST     $38                 
5ABF: 40              LD      B,B                 
5AC0: FF              RST     $38                 
5AC1: 3E FF           LD      A,$FF               
5AC3: 3C              INC     A                   
5AC4: FF              RST     $38                 
5AC5: 3A FF 38        LD      A,($38FF)           ; {hard.rom+38FF}
5AC8: FF              RST     $38                 
5AC9: 38 FF           JR      C,$5ACA             
5ACB: 37              SCF                         
5ACC: FF              RST     $38                 
5ACD: 36 FF           LD      (HL),$FF            
5ACF: 35              DEC     (HL)                
5AD0: FF              RST     $38                 
5AD1: 34              INC     (HL)                
5AD2: FF              RST     $38                 
5AD3: 33              INC     SP                  
5AD4: FF              RST     $38                 
5AD5: 32 FF 32        LD      ($32FF),A           ; {hard.rom+32FF}
5AD8: FF              RST     $38                 
5AD9: 33              INC     SP                  
5ADA: FF              RST     $38                 
5ADB: 34              INC     (HL)                
5ADC: FF              RST     $38                 
5ADD: 35              DEC     (HL)                
5ADE: FF              RST     $38                 
5ADF: 36 FF           LD      (HL),$FF            
5AE1: 37              SCF                         
5AE2: FF              RST     $38                 
5AE3: 38 FF           JR      C,$5AE4             
5AE5: 38 FF           JR      C,$5AE6             
5AE7: 3A FF 3C        LD      A,($3CFF)           ; {hard.rom+3CFF}
5AEA: FF              RST     $38                 
5AEB: 3E FF           LD      A,$FF               
5AED: 40              LD      B,B                 
5AEE: FF              RST     $38                 
5AEF: 41              LD      B,C                 
5AF0: FF              RST     $38                 
5AF1: 44              LD      B,H                 
5AF2: FF              RST     $38                 
5AF3: 46              LD      B,(HL)              
5AF4: FF              RST     $38                 
5AF5: 47              LD      B,A                 
5AF6: FF              RST     $38                 
5AF7: 4A              LD      C,D                 
5AF8: FF              RST     $38                 
5AF9: 4D              LD      C,L                 
5AFA: FF              RST     $38                 
5AFB: 50              LD      D,B                 
5AFC: FF              RST     $38                 
5AFD: 51              LD      D,C                 
5AFE: FF              RST     $38                 
5AFF: 54              LD      D,H                 
5B00: FF              RST     $38                 
5B01: 57              LD      D,A                 
5B02: FF              RST     $38                 
5B03: 58              LD      E,B                 
5B04: FF              RST     $38                 
5B05: 5B              LD      E,E                 
5B06: FF              RST     $38                 
5B07: 5E              LD      E,(HL)              
5B08: FF              RST     $38                 
5B09: 5F              LD      E,A                 
5B0A: FF              RST     $38                 
5B0B: 62              LD      H,D                 
5B0C: FF              RST     $38                 
5B0D: 65              LD      H,L                 
5B0E: FF              RST     $38                 
5B0F: 68              LD      L,B                 
5B10: FF              RST     $38                 
5B11: 69              LD      L,C                 
5B12: FF              RST     $38                 
5B13: 6C              LD      L,H                 
5B14: FF              RST     $38                 
5B15: 6F              LD      L,A                 
5B16: FF              RST     $38                 
5B17: 70              LD      (HL),B              
5B18: FF              RST     $38                 
5B19: 73              LD      (HL),E              
5B1A: FF              RST     $38                 
5B1B: 77              LD      (HL),A              
5B1C: FF              RST     $38                 
5B1D: 78              LD      A,B                 
5B1E: FF              RST     $38                 
5B1F: 7B              LD      A,E                 
5B20: FF              RST     $38                 
5B21: 7F              LD      A,A                 
5B22: FF              RST     $38                 
5B23: 81              ADD     A,C                 
5B24: FF              RST     $38                 
5B25: 85              ADD     A,L                 
5B26: FF              RST     $38                 
5B27: 88              ADC     A,B                 
5B28: FF              RST     $38                 
5B29: 8A              ADC     A,D                 
5B2A: FF              RST     $38                 
5B2B: 90              SUB     B                   
5B2C: FF              RST     $38                 
5B2D: 93              SUB     E                   
5B2E: FF              RST     $38                 
5B2F: 98              SBC     A,B                 
5B30: FF              RST     $38                 
5B31: 9D              SBC     A,L                 
5B32: FF              RST     $38                 
5B33: A0              AND     B                   
5B34: FF              RST     $38                 
5B35: A4              AND     H                   
5B36: FF              RST     $38                 
5B37: A8              XOR     B                   
5B38: FF              RST     $38                 
5B39: AE              XOR     (HL)                
5B3A: FF              RST     $38                 
5B3B: B2              OR      D                   
5B3C: FF              RST     $38                 
5B3D: B7              OR      A                   
5B3E: FF              RST     $38                 
5B3F: BD              CP      L                   
5B40: FF              RST     $38                 
5B41: C2 FF C7        JP      NZ,$C7FF            
5B44: FF              RST     $38                 
5B45: CE FF           ADC     A,$FF               
5B47: D4 FF D9        CALL    NC,$D9FF            
5B4A: FF              RST     $38                 
5B4B: E0              RET     PO                  
5B4C: FF              RST     $38                 
5B4D: E6 FF           AND     $FF                 
5B4F: EC FF F2        CALL    PE,$F2FF            
5B52: FF              RST     $38                 
5B53: F8              RET     M                   
5B54: FF              RST     $38                 
5B55: 00              NOP                         
5B56: 00              NOP                         
5B57: 00              NOP                         
5B58: 00              NOP                         
5B59: 08              EX      AF,AF'              
5B5A: 00              NOP                         
5B5B: 0E 00           LD      C,$00               
5B5D: 14              INC     D                   
5B5E: 00              NOP                         
5B5F: 1A              LD      A,(DE)              
5B60: 00              NOP                         
5B61: 20 00           JR      NZ,$5B63            ; {code.loc_5b63}

loc_5b63:
5B63: 27              DAA                         
5B64: 00              NOP                         
5B65: 2C              INC     L                   
5B66: 00              NOP                         
5B67: 32 00 39        LD      ($3900),A           ; {hard.rom+3900}
5B6A: 00              NOP                         
5B6B: 3E 00           LD      A,$00               
5B6D: 43              LD      B,E                 
5B6E: 00              NOP                         
5B6F: 49              LD      C,C                 
5B70: 00              NOP                         
5B71: 4E              LD      C,(HL)              
5B72: 00              NOP                         
5B73: 52              LD      D,D                 
5B74: 00              NOP                         
5B75: 58              LD      E,B                 
5B76: 00              NOP                         
5B77: 5C              LD      E,H                 
5B78: 00              NOP                         
5B79: 60              LD      H,B                 
5B7A: 00              NOP                         
5B7B: 63              LD      H,E                 
5B7C: 00              NOP                         
5B7D: 63              LD      H,E                 
5B7E: 00              NOP                         
5B7F: 6D              LD      L,L                 
5B80: 00              NOP                         
5B81: 70              LD      (HL),B              
5B82: 00              NOP                         
5B83: 76              HALT                        
5B84: 00              NOP                         
5B85: 78              LD      A,B                 
5B86: 00              NOP                         
5B87: 7B              LD      A,E                 
5B88: 00              NOP                         
5B89: 7F              LD      A,A                 
5B8A: 00              NOP                         
5B8B: 81              ADD     A,C                 
5B8C: 00              NOP                         
5B8D: 85              ADD     A,L                 
5B8E: 00              NOP                         
5B8F: 88              ADC     A,B                 
5B90: 00              NOP                         
5B91: 89              ADC     A,C                 
5B92: 00              NOP                         
5B93: 8D              ADC     A,L                 
5B94: 00              NOP                         
5B95: 90              SUB     B                   
5B96: 00              NOP                         
5B97: 91              SUB     C                   
5B98: 00              NOP                         
5B99: 94              SUB     H                   
5B9A: 00              NOP                         
5B9B: 97              SUB     A                   
5B9C: 00              NOP                         
5B9D: 94              SUB     H                   
5B9E: 00              NOP                         
5B9F: 9B              SBC     A,E                 
5BA0: 00              NOP                         
5BA1: 9E              SBC     A,(HL)              
5BA2: 00              NOP                         
5BA3: A1              AND     C                   
5BA4: 00              NOP                         
5BA5: A2              AND     D                   
5BA6: 00              NOP                         
5BA7: A5              AND     L                   
5BA8: 00              NOP                         
5BA9: A8              XOR     B                   
5BAA: 00              NOP                         
5BAB: A9              XOR     C                   
5BAC: 00              NOP                         
5BAD: AC              XOR     H                   
5BAE: 00              NOP                         
5BAF: AF              XOR     A                   
5BB0: 00              NOP                         
5BB1: B0              OR      B                   
5BB2: 00              NOP                         
5BB3: B3              OR      E                   
5BB4: 00              NOP                         
5BB5: B6              OR      (HL)                
5BB6: 00              NOP                         
5BB7: B9              CP      C                   
5BB8: 00              NOP                         
5BB9: BA              CP      D                   
5BBA: 00              NOP                         
5BBB: BC              CP      H                   
5BBC: 00              NOP                         
5BBD: B9              CP      C                   
5BBE: 00              NOP                         
5BBF: C0              RET     NZ                  
5BC0: 00              NOP                         
5BC1: C2 00 C4        JP      NZ,$C400            
5BC4: 00              NOP                         
5BC5: C6 00           ADD     A,$00               
5BC7: C8              RET     Z                   
5BC8: 00              NOP                         
5BC9: C8              RET     Z                   
5BCA: 00              NOP                         
5BCB: C9              RET                         

; ---- $5BCC-$5BD6: data ----
5BCC: 00 CA 00 CB 00 CC 00 CD 00 CE 00

; inner sequence-dispatch arm (table 0x0f29 index 2): blank a fixed
; character run, advance the interpolated pen run, and bail unless it
; reseated to a zero row integer; on the full path fold two guarded code
; blocks (an anti-tamper XOR check that raises the sequence phase on
; mismatch, and a self-cancelling add-checksum over a work cell) then step
; the sequence sub-index
blankCaptionThenAdvancePenRunStep:
5BD7: CD D2 07        CALL    $07D2               ; {code.blankFourteenCharCells} blank a fixed run of fourteen character cells
5BDA: CD 01 02        CALL    $0201               ; {code.drawInterpolatedPenRun} advance the interpolated pen run one step
5BDD: C0              RET     NZ                  ; return unless the pen run reseated to a whole row
5BDE: 21 DD 0B        LD      HL,$0BDD            ; point at a 256-byte program block to fold
5BE1: 97              SUB     A                   ; clear the running fold
5BE2: 47              LD      B,A                 ; 256 bytes to fold -- a zero count runs the full round

loc_5be3:
5BE3: AE              XOR     (HL)                ; fold this byte into the running exclusive-or
5BE4: 23              INC     HL                  
5BE5: 10 FC           DJNZ    $5BE3               ; {code.loc_5be3} loop over all 256 bytes
5BE7: C6 E4           ADD     A,$E4               ; test the fold against its expected value
5BE9: C4 11 0F        CALL    NZ,$0F11            ; {code.advanceSequencePhase} on a mismatch, raise the sequence phase -- anti-tamper
5BEC: 3A AB A9        LD      A,($A9AB)           ; {hard.workRam+1AB} read the guard work cell
5BEF: 21 34 17        LD      HL,$1734            ; point at a 20-byte program block to sum
5BF2: 06 14           LD      B,$14               ; 20 bytes to sum

loc_5bf4:
5BF4: 86              ADD     A,(HL)              ; add this byte into the running total
5BF5: 23              INC     HL                  
5BF6: 10 FC           DJNZ    $5BF4               ; {code.loc_5bf4} loop over all 20 bytes
5BF8: C6 77           ADD     A,$77               ; add the bias -- on a clean image this returns the cell to its old value
5BFA: 32 AB A9        LD      ($A9AB),A           ; {hard.workRam+1AB} write the guard work cell back
5BFD: C3 1A 0F        JP      $0F1A               ; {code.advanceSequenceSubStep} step the sequence sub-index

; ---- $5C00-$5FFF: data ----
5C00: E7 00 E6 00 E5 00 E4 00 E3 00 E2 00 E1 00 E0 00
5C10: DE 00 DC 00 DA 00 D8 00 D6 00 D3 00 D1 00 CF 00
5C20: CC 00 C9 00 C6 00 C4 00 C1 00 BE 00 BC 00 B9 00
5C30: B6 00 B4 00 B1 00 AE 00 AB 00 A9 00 A6 00 A3 00
5C40: A1 00 9E 00 9A 00 98 00 95 00 91 00 8E 00 8A 00
5C50: 87 00 84 00 7E 00 7A 00 75 00 6F 00 6C 00 67 00
5C60: 62 00 5C 00 57 00 51 00 4B 00 45 00 3F 00 38 00
5C70: 31 00 2B 00 24 00 1D 00 16 00 0F 00 08 00 00 00
5C80: 00 00 F8 FF F1 FF 00 00 E3 FF DC FF D5 FF CF FF
5C90: C8 FF C1 FF BB FF B5 FF AF FF A9 FF A4 FF 9E FF
5CA0: 99 FF 94 FF 91 FF 94 FF 86 FF 82 FF 7C FF 79 FF
5CB0: 76 FF 72 FF 6F FF 6B FF 68 FF 66 FF 62 FF 5F FF
5CC0: 5D FF 5A FF 57 FF 57 FF 52 FF 4F FF 4C FF 4A FF
5CD0: 47 FF 44 FF 42 FF 3F FF 3C FF 3A FF 37 FF 34 FF
5CE0: 31 FF 2F FF 2D FF 2A FF 28 FF 26 FF 24 FF 22 FF
5CF0: 20 FF 1F FF 1E FF 1D FF 1C FF 1B FF 1A FF 19 FF
5D00: 19 FF 1A FF 1B FF 1C FF 1D FF 1E FF 1F FF 20 FF
5D10: 22 FF 24 FF 26 FF 28 FF 2A FF 2D FF 2F FF 31 FF
5D20: 34 FF 37 FF 3A FF 3C FF 3F FF 42 FF 44 FF 47 FF
5D30: 4A FF 4C FF 4F FF 52 FF 55 FF 57 FF 5A FF 5D FF
5D40: 5F FF 62 FF 66 FF 68 FF 6B FF 6F FF 72 FF 76 FF
5D50: 79 FF 7C FF 82 FF 86 FF 8B FF 91 FF 94 FF 99 FF
5D60: 9E FF A4 FF A9 FF AF FF B5 FF BB FF C1 FF C8 FF
5D70: CF FF D5 FF DC FF E3 FF EA FF F1 FF F8 FF 00 00
5D80: 00 00 08 00 0F 00 16 00 1D 00 24 00 2B 00 31 00
5D90: 38 00 3F 00 45 00 4B 00 51 00 57 00 5C 00 62 00
5DA0: 67 00 6C 00 6F 00 6F 00 7A 00 7E 00 84 00 87 00
5DB0: 8A 00 8E 00 91 00 95 00 98 00 9A 00 9E 00 A1 00
5DC0: A3 00 A6 00 A9 00 A6 00 AE 00 B1 00 B4 00 B6 00
5DD0: B9 00 BC 00 BE 00 C1 00 C4 00 C6 00 C9 00 CC 00
5DE0: CF 00 D1 00 D3 00 CF 00 D8 00 DA 00 DC 00 DE 00
5DF0: E0 00 E1 00 E2 00 E3 00 E4 00 E5 00 E6 00 E7 00
5E00: 00 01 FF 00 FE 00 FD 00 FC 00 FB 00 FA 00 F8 00
5E10: F6 00 F4 00 F2 00 F0 00 ED 00 EA 00 E8 00 E5 00
5E20: E2 00 DF 00 DC 00 D9 00 D6 00 D3 00 D0 00 CD 00
5E30: CA 00 C7 00 C4 00 C1 00 BE 00 BB 00 B8 00 B5 00
5E40: B2 00 AF 00 AB 00 A8 00 A5 00 A1 00 9D 00 99 00
5E50: 96 00 92 00 8C 00 87 00 82 00 7B 00 78 00 72 00
5E60: 6C 00 66 00 60 00 59 00 53 00 4C 00 45 00 3E 00
5E70: 36 00 2F 00 28 00 20 00 18 00 10 00 08 00 00 00
5E80: 00 00 F8 FF F0 FF 00 00 E0 FF D8 FF D1 FF CA FF
5E90: C2 FF BB FF B4 FF AD FF A7 FF A0 FF 9A FF 94 FF
5EA0: 8E FF 88 FF 85 FF 88 FF 79 FF 74 FF 6E FF 6A FF
5EB0: 67 FF 63 FF 5F FF 5B FF 58 FF 55 FF 51 FF 4E FF
5EC0: 4B FF 48 FF 45 FF 45 FF 3F FF 3C FF 39 FF 36 FF
5ED0: 33 FF 30 FF 2D FF 2A FF 27 FF 24 FF 21 FF 1E FF
5EE0: 1B FF 18 FF 16 FF 13 FF 10 FF 0E FF 0C FF 0A FF
5EF0: 08 FF 06 FF 05 FF 04 FF 03 FF 02 FF 01 FF 00 FF
5F00: 00 FF 01 FF 02 FF 03 FF 04 FF 05 FF 06 FF 08 FF
5F10: 0A FF 0C FF 0E FF 10 FF 13 FF 16 FF 18 FF 1B FF
5F20: 1E FF 21 FF 24 FF 27 FF 2A FF 2D FF 30 FF 33 FF
5F30: 36 FF 39 FF 3C FF 3F FF 42 FF 45 FF 48 FF 4B FF
5F40: 4E FF 51 FF 55 FF 58 FF 5B FF 5F FF 63 FF 67 FF
5F50: 6A FF 6E FF 74 FF 79 FF 7E FF 85 FF 88 FF 8E FF
5F60: 94 FF 9A FF A0 FF A7 FF AD FF B4 FF BB FF C2 FF
5F70: CA FF D1 FF D8 FF E0 FF E8 FF F0 FF F8 FF 00 00
5F80: 00 00 08 00 10 00 18 00 20 00 28 00 2F 00 36 00
5F90: 3E 00 45 00 4C 00 53 00 59 00 60 00 66 00 6C 00
5FA0: 72 00 78 00 7B 00 7B 00 87 00 8C 00 92 00 96 00
5FB0: 99 00 9D 00 A1 00 A5 00 A8 00 AB 00 AF 00 B2 00
5FC0: B5 00 B8 00 BB 00 B8 00 C1 00 C4 00 C7 00 CA 00
5FD0: CD 00 D0 00 D3 00 D6 00 D9 00 DC 00 DF 00 E2 00
5FE0: E5 00 E8 00 EA 00 E5 00 F0 00 F2 00 F4 00 F6 00
5FF0: F8 00 FA 00 FB 00 FC 00 FD 00 FE 00 FF 00 00 01
```
