![Donkey Kong](dkong.jpg)

# Donkey Kong Main CPU (Z80)

>>> cpu Z80

>>> binary 0000:roms/c_5et_g.bin + roms/c_5ct_g.bin + roms/c_5bt_g.bin + roms/c_5at_g.bin

>>> memoryTable hard

[Hardware Info](Hardware.md)

>>> memoryTable ram

[RAM Usage](RAMUse.md)

```code
; Reset entry: run the power-on initialisation, then fall into the forever main loop.
boot:
0000: 3E 00           LD      A,$00               
0002: 32 84 7D        LD      ($7D84),A           ; {hard.nmiEnable} mask the vblank NMI before initialising
0005: C3 66 02        JP      $0266               ; {code.clearRamAndInitHardware} power-on setup, then the main loop

; Caller-skip guard: proceed only while a credited game is in play. It reads bit 0 of
; attract -- non-zero while no credited game is running, zero once a coin has been taken
; -- and tells its caller to run its body or skip the rest of it. Mind the polarity: this
; one proceeds while the bit is CLEAR, the opposite of the guard keyed on Mario being
; alive. A leaf: reads one byte, writes none.
gameActiveGuard:
0008: 3A 07 60        LD      A,($6007)           ; {hard.workRam+7} read the attract flag
000B: 0F              RRCA                        ; shift the attract bit into carry
000C: D0              RET     NC                  ; clear: a game is credited, let the caller run
000D: 33              INC     SP                  ; no game: step over the caller's return address
000E: 33              INC     SP                  
000F: C9              RET                         ; so the caller's remaining work is abandoned

; Answer "is Mario alive?" for the caller. Reads marioActive, where bit 0 set means alive
; and being processed. If it is clear the routine steps over the caller's return address
; so the caller's remaining work is abandoned. The player-motion, hammer and bonus
; updates all open with this test.
marioActiveGuard:
0010: 3A 00 62        LD      A,($6200)           ; {hard.workRam+200} read the player-alive flag
0013: 0F              RRCA                        
0014: D8              RET     C                   ; Mario is alive, let the caller run
0015: 33              INC     SP                  ; dead: discard the caller's return address
0016: 33              INC     SP                  
0017: C9              RET                         ; abandon the rest of the caller's frame

; The shared "wait N frames, then act" gate. Counts substateTimer down by one in place
; and reports whether that tick is the one that brought it to zero. On expiry the caller
; goes on and does its work; while the counter is still above zero the caller abandons
; the rest of its frame. A leaf: it reads and writes substateTimer and nothing else.
tickSubstateTimer:
0018: 21 09 60        LD      HL,$6009            ; point at the sub-state frame countdown
001B: 35              DEC     (HL)                ; tick one frame off the wait
001C: C8              RET     Z                   ; the wait just expired, let the caller act
001D: 33              INC     SP                  ; still waiting: skip the caller's remainder
001E: 33              INC     SP                  
001F: C9              RET                         

; Fast half of the two-level sub-state countdown. Every call takes one off
; substateTimerLo; while that is still counting the caller is skipped. Only on its
; underflow does control chain into the slow half, which steps substateTimer and reports
; ITS expiry -- so the caller's remainder runs only on the frame both counters expire
; together.
tickSubstatePrescaler:
0020: 21 08 60        LD      HL,$6008            ; the fast half of the sub-state timer
0023: 35              DEC     (HL)                ; tick the prescaler
0024: 28 F2           JR      Z,$0018             ; {code.tickSubstateTimer} on underflow, chain into the slow half

loc_0026:
0026: E1              POP     HL                  ; still counting: discard the caller's return
0027: C9              RET                         

; The inline-jump-table trampoline. A caller arrives through a one-byte restart with the
; target index in A, having laid a list of 2-byte little-endian addresses immediately
; after that opcode -- so the pushed return address points AT the table. This recovers
; that base off the stack, reads the word at table[index], and jumps there. The index
; doubling is an 8-bit result, so the address is base + (2*index & 0xff) and an index of
; 0x80 wraps back to entry 0. Every computed dispatch in the game comes through here: the
; per-frame game-state table, the in-game sub-state table, the opening cutscene, the
; difficulty guards.
dispatchInlineJumpTable:
0028: 87              ADD     A,A                 ; two bytes per table entry
0029: E1              POP     HL                  ; the return address IS the table base
002A: 5F              LD      E,A                 
002B: 16 00           LD      D,$00               
002D: C3 32 00        JP      $0032               ; {code.loc_0032}

; The "does THIS board want it?" gate. The caller passes a per-board mask -- bit 0 for
; 25m through bit 3 for 100m -- and this rotates the mask right by the current board
; number so the board's own bit falls into carry. Set, and the caller carries on; clear,
; and the caller's return is stepped over so its next action never runs. It rotates
; rather than shifts, so a board number of 0 would come back holding bit 7.
boardBitGate:
0030: 18 12           JR      $0044               ; {code.loc_0044} restart vector for the per-board gate

loc_0032:
0032: 19              ADD     HL,DE               ; index the entry for this dispatch value
0033: 5E              LD      E,(HL)              ; fetch the target address, low byte
0034: 23              INC     HL                  
0035: 56              LD      D,(HL)              ; then its high byte
0036: EB              EX      DE,HL               
0037: E9              JP      (HL)                ; enter the selected handler

; Add one signed delta into the SAME field of all ten sprite-object records at once,
; shifting a whole column of them together. It fixes the two numbers that make the
; general strided add specific to this block -- a stride of 4, one record, and a count
; of 10 -- and runs the shared loop. Aimed at a record's first byte it slides the
; group's X; three bytes in, its Y. Board and cutscene setup use it to reposition a row
; of scenery or a staged figure by one number.
addToSpriteObjectColumn:
0038: 11 04 00        LD      DE,$0004            ; four bytes per sprite-object record
003B: 06 0A           LD      B,$0A               ; ten records in the block

; Add a signed byte into each of a run of bytes spaced at a fixed stride. Its usual job
; is nudging one column of the sprite shadow buffer -- the X or the Y field of ten
; records, four bytes apart -- by a single delta during board and cutscene setup; the
; heaviest use passes -4, so it decrements. Each add is 8-bit and wraps. The count is
; tested after a pass rather than before the first, so a count of 0 on entry means 256
; passes, not none.
addStrided:
003D: 79              LD      A,C                 ; the caller's signed delta
003E: 86              ADD     A,(HL)              ; add it into this record's field
003F: 77              LD      (HL),A              
0040: 19              ADD     HL,DE               ; step to the same field of the next record
0041: 10 FA           DJNZ    $003D               ; {code.addStrided}
0043: C9              RET                         

loc_0044:
0044: 21 27 62        LD      HL,$6227            ; point at the current board number
0047: 46              LD      B,(HL)              ; rotate the mask by the board number

loc_0048:
0048: 0F              RRCA                        
0049: 10 FD           DJNZ    $0048               ; {code.loc_0048} so this board's bit lands in carry
004B: D8              RET     C                   ; this board wants it: let the caller run
004C: E1              POP     HL                  ; not this board: discard the caller's return
004D: C9              RET                         

; Copy 40 bytes -- ten 4-byte sprite records -- from the caller's source pointer into
; spriteObjBlock. Destination and length are hard-wired; the source is whatever scene
; template the caller points at, board decor or cutscene props. The copy runs forward
; byte by byte, so it stays correct when source and destination overlap.
loadSpriteObjectBlock:
004E: 11 08 69        LD      DE,$6908            ; destination: the ten sprite-object records
0051: 01 28 00        LD      BC,$0028            ; forty bytes, ten 4-byte records
0054: ED B0           LDIR                        ; copy the scene template into the block
0056: C9              RET                         

; Stir the pseudo-random seed, once per vblank. The machine has no random source, so
; entropy is manufactured by summing two counters that advance at unrelated rates: random
; takes random + frame + spinCount, wrapping at 8 bits. frame is decremented once per
; vblank and spinCount incremented once per main-loop pass, so spinCount's rate depends
; on how much work the frame actually did -- that jitter is what makes the sum
; unpredictable enough to drive spawns and difficulty coin-flips.
stirRandomSeed:
0057: 3A 18 60        LD      A,($6018)           ; {hard.workRam+18} read the pseudo-random seed
005A: 21 1A 60        LD      HL,$601A            ; point at the frame counter
005D: 86              ADD     A,(HL)              ; mix in the frame counter
005E: 21 19 60        LD      HL,$6019            ; point at the main-loop spin counter
0061: 86              ADD     A,(HL)              ; mix in the spin counter, whose rate jitters
0062: 32 18 60        LD      ($6018),A           ; {hard.workRam+18} store the stirred seed
0065: C9              RET                         

; The vblank NMI -- the per-frame service, and where everything time-critical happens.
; In order: clear nmiEnable, which IS the acknowledge and also blocks re-entry until the
; tail turns it back on; read in2, which is what feeds the watchdog once a frame, and
; test the SERVICE switch; blit the sprite shadow buffer into sprite RAM through the
; i8257 from a 9-byte setup block; read and edge-debounce the joystick, but only while a
; credited game is in play, since attract skips input entirely; then the frame tail --
; decrement frame, stir random, drain the sound and task schedulers, dispatch on
; gameState -- and finally restore the six saved register pairs and re-enable the NMI.
serviceVblankNmi:
0066: F5              PUSH    AF                  ; save the interrupted code's registers
0067: C5              PUSH    BC                  
0068: D5              PUSH    DE                  
0069: E5              PUSH    HL                  
006A: DD E5           PUSH    IX                  
006C: FD E5           PUSH    IY                  
006E: AF              XOR     A                   
006F: 32 84 7D        LD      ($7D84),A           ; {hard.nmiEnable} acknowledge the NMI and block re-entry
0072: 3A 00 7D        LD      A,($7D00)           ; {hard.in2} read IN2; the read is the watchdog kick
0075: E6 01           AND     $01                 ; isolate the SERVICE switch
0077: C2 00 40        JP      NZ,$4000            ; SERVICE switch held: leave the game ROM
007A: 21 38 01        LD      HL,$0138            ; point at the DMA setup block
007D: CD 41 01        CALL    $0141               ; {code.blitSpritesViaDma} blit the sprite buffer to sprite RAM
0080: 3A 07 60        LD      A,($6007)           ; {hard.workRam+7} attract skips the control read entirely
0083: A7              AND     A                   
0084: C2 B5 00        JP      NZ,$00B5            ; {code.perFrame} no credited game: on to the frame tail

; Read the joystick and cook it into p1Input. An upright cabinet always reads IN0; a
; cocktail reads IN1 while player 2 is up. The direction nibble is taken live every
; frame, so a held direction registers continuously, but JUMP is EDGE-detected against
; last frame's p1InputRaw and lifted into bit 7 -- set for exactly one frame per press,
; so a held jump does not repeat. The raw port goes to p1InputRaw as next frame's
; comparison. Raw bit 6 is a service / soft-reset line. Skipped entirely while attract
; is set.
readControls:
0087: 3A 26 60        LD      A,($6026)           ; {hard.workRam+26} an upright cabinet always reads IN0
008A: A7              AND     A                   
008B: C2 98 00        JP      NZ,$0098            ; {code.loc_0098} upright: read IN0
008E: 3A 0E 60        LD      A,($600E)           ; {hard.workRam+E} cocktail: is player 2 the one up?
0091: A7              AND     A                   
0092: 3A 80 7C        LD      A,($7C80)           ; {hard.in1} read player 2's joystick port
0095: C2 9B 00        JP      NZ,$009B            ; {code.loc_009b} player 2 up on a cocktail: keep IN1

loc_0098:
0098: 3A 00 7C        LD      A,($7C00)           ; {hard.in0} read player 1's joystick port

loc_009b:
009B: 47              LD      B,A                 ; keep the raw port byte
009C: E6 0F           AND     $0F                 ; the direction nibble: right, left, up, down
009E: 4F              LD      C,A                 
009F: 3A 11 60        LD      A,($6011)           ; {hard.workRam+11} last frame's raw port, for the edge test
00A2: 2F              CPL                         
00A3: A0              AND     B                   ; keep only bits that went from 0 to 1
00A4: E6 10           AND     $10                 ; isolate the JUMP button's press edge
00A6: 17              RLA                         
00A7: 17              RLA                         
00A8: 17              RLA                         ; lift the jump edge into bit 7
00A9: B1              OR      C                   ; merge it with the direction nibble
00AA: 60              LD      H,B                 
00AB: 6F              LD      L,A                 
00AC: 22 10 60        LD      ($6010),HL          ; {hard.workRam+10} store the cooked word and the raw port
00AF: 78              LD      A,B                 
00B0: CB 77           BIT     6,A                 ; test the service / soft-reset line
00B2: C2 00 00        JP      NZ,$0000            ; {code.boot} soft-reset the machine

; The tail of the vblank NMI: the once-a-frame service, then the game-state dispatch.
; First it decrements frame. That is the beat the whole game keeps time to -- the main
; loop spins comparing frame against its saved copy, so this decrement is what releases
; the loop for the new frame, and every periodic event keys off it. Then the three
; service routines: stir the random seed, debounce the coin line and award credits, drain
; the sound-trigger countdowns. Then dispatch gameState to its handler -- 0 power-on, 1
; attract, 2 credited, 3 in-game. Finally re-enable the NMI mask and return to the
; interrupted main loop.
perFrame:
00B5: 21 1A 60        LD      HL,$601A            ; point at the frame counter
00B8: 35              DEC     (HL)                ; advance the frame clock; this frees the main loop
00B9: CD 57 00        CALL    $0057               ; {code.stirRandomSeed} stir the pseudo-random seed
00BC: CD 7B 01        CALL    $017B               ; {code.serviceCoinInput} debounce the coin line, award credits
00BF: CD E0 00        CALL    $00E0               ; {code.soundDriverTick} push the sound shadows to the hardware
00C2: 21 D2 00        LD      HL,$00D2            ; push the epilogue as the dispatch's return
00C5: E5              PUSH    HL                  
00C6: 3A 05 60        LD      A,($6005)           ; {hard.workRam+5} 0 power-on, 1 attract, 2 credited, 3 in-game
00C9: EF              RST     $28                 ; dispatch through the table that follows

; ---- $00CA-$00D1: jump table ----
00CA: C3 01 3C 07 B2 08 FE 06

loc_00d2:
00D2: FD E1           POP     IY                  ; restore the interrupted code's registers
00D4: DD E1           POP     IX                  
00D6: E1              POP     HL                  
00D7: D1              POP     DE                  
00D8: C1              POP     BC                  
00D9: 3E 01           LD      A,$01               
00DB: 32 84 7D        LD      ($7D84),A           ; {hard.nmiEnable} re-enable the vblank NMI for the next frame
00DE: F1              POP     AF                  
00DF: C9              RET                         ; return to the interrupted main loop

; Re-drive the audio hardware from its work-RAM shadows, once per vblank. The sound
; latches are write-only, so game code stores into shadow bytes and this driver pushes
; them out every frame. It returns at once when attract is non-zero -- the driver is
; silent with no credited game. Otherwise it walks the eight sndTrigger bytes in lockstep
; with the eight bits of the addressable sound latch: a non-zero shadow is a frame
; countdown, decremented with its bit driven high; a zero shadow drives its bit low. So
; storing N into a trigger holds that sound asserted for N frames. Then the tune latch
; takes sndPriority while sndPriorityFrames is still running and the looping sndBgm
; otherwise, and sndIrqTrigger counts down the same way onto the sound-CPU interrupt
; line.
soundDriverTick:
00E0: 21 80 60        LD      HL,$6080            ; point at the eight sound-trigger shadows
00E3: 11 00 7D        LD      DE,$7D00            ; and at the eight sound-latch bits
00E6: 3A 07 60        LD      A,($6007)           ; {hard.workRam+7} the driver is silent during attract
00E9: A7              AND     A                   
00EA: C0              RET     NZ                  ; no credited game: leave the latches alone
00EB: 06 08           LD      B,$08               ; eight triggers, one per latch bit

loc_00ed:
00ED: 7E              LD      A,(HL)              ; read this trigger's frame countdown
00EE: A7              AND     A                   
00EF: CA F5 00        JP      Z,$00F5             ; {code.loc_00f5} zero: release this sound's bit
00F2: 35              DEC     (HL)                ; count the assert down one frame
00F3: 3E 01           LD      A,$01               ; and hold the latch bit asserted

loc_00f5:
00F5: 12              LD      (DE),A              ; drive the addressable latch bit
00F6: 1C              INC     E                   ; next latch bit
00F7: 2C              INC     L                   ; next trigger shadow
00F8: 10 F3           DJNZ    $00ED               ; {code.loc_00ed}
00FA: 21 8B 60        LD      HL,$608B            ; point at the priority-tune countdown
00FD: 7E              LD      A,(HL)              
00FE: A7              AND     A                   
00FF: C2 08 01        JP      NZ,$0108            ; {code.loc_0108} a priority tune is still running
0102: 2D              DEC     L                   
0103: 2D              DEC     L                   ; step back to the background tune index
0104: 7E              LD      A,(HL)              ; no priority tune: play the looping theme
0105: C3 0B 01        JP      $010B               ; {code.loc_010b}

loc_0108:
0108: 35              DEC     (HL)                ; tick the priority tune's frame count
0109: 2D              DEC     L                   ; step back to the priority tune index
010A: 7E              LD      A,(HL)              ; it overrides the background tune

loc_010b:
010B: 32 00 7C        LD      ($7C00),A           ; {hard.in0} hand the tune index to the sound CPU
010E: 21 88 60        LD      HL,$6088            ; the sound-CPU interrupt countdown
0111: AF              XOR     A                   
0112: BE              CP      (HL)                
0113: CA 18 01        JP      Z,$0118             ; {code.loc_0118} nothing queued: drop the interrupt line
0116: 35              DEC     (HL)                ; count the queued interrupt down
0117: 3C              INC     A                   ; and raise the line this frame

loc_0118:
0118: 32 80 7D        LD      ($7D80),A           ; {hard.dsw1} drive the sound-CPU interrupt line
011B: C9              RET                         

; Silence everything at once. Writes 0 to the eight soundLatch bits at 0x7D00-0x7D07 and
; to their readable work-RAM shadow sndTrigger, cleared as a pair per index; to the
; four-byte control block sndIrqTrigger / sndBgm / sndPriority / sndPriorityFrames; and
; to the sound-CPU interrupt line and the tune latch. The hardware latches are
; write-only, which is why the shadow exists at all. It reads nothing -- every store is
; a constant it produces itself. Reached at boot with the NMI still masked, and on
; reset, game-over and new-life.
silenceSound:
011C: 06 08           LD      B,$08               ; eight latch bits and their shadows
011E: AF              XOR     A                   
011F: 21 00 7D        LD      HL,$7D00            ; the addressable sound latch
0122: 11 80 60        LD      DE,$6080            ; and its readable work-RAM shadow

loc_0125:
0125: 77              LD      (HL),A              ; release the latch bit
0126: 12              LD      (DE),A              ; and clear its shadow to match
0127: 2C              INC     L                   
0128: 1C              INC     E                   
0129: 10 FA           DJNZ    $0125               ; {code.loc_0125}
012B: 06 04           LD      B,$04               ; then the four-byte tune control block

loc_012d:
012D: 12              LD      (DE),A              ; clear the tune and priority controls
012E: 1C              INC     E                   
012F: 10 FC           DJNZ    $012D               ; {code.loc_012d}
0131: 32 80 7D        LD      ($7D80),A           ; {hard.dsw1} drop the sound-CPU interrupt line
0134: 32 00 7C        LD      ($7C00),A           ; {hard.in0} and silence the tune latch
0137: C9              RET                         

; ---- $0138-$0140: data ----
0138: 53 00 69 80 41 00 70 80 81

; Program the i8257 and blit the sprite shadow buffer into sprite RAM. Sprites never
; reach the screen by CPU writes: the CPU fills spriteBuffer and this runs once a
; vblank, copying nine setup bytes into the controller in the order it expects -- mode
; register first, which also resets its internal byte flip-flop, then source,
; destination and counts, each 16-bit register being two stores to the SAME address --
; and then pulsing DRQ. The rising edge IS the blit: 385 transfers, 96 records of four
; bytes. Program the controller without the pulse and sprite RAM is left stale.
blitSpritesViaDma:
0141: AF              XOR     A                   
0142: 32 85 7D        LD      ($7D85),A           ; {hard.dmaRequest} DRQ low before touching the controller
0145: 7E              LD      A,(HL)              
0146: 32 08 78        LD      ($7808),A           ; {hard.dma8257+8} mode register; this resets the byte flip-flop
0149: 23              INC     HL                  
014A: 7E              LD      A,(HL)              
014B: 32 00 78        LD      ($7800),A           ; {hard.dma8257} source address low: the sprite buffer
014E: 23              INC     HL                  
014F: 7E              LD      A,(HL)              
0150: 32 00 78        LD      ($7800),A           ; {hard.dma8257} and its high byte, same register
0153: 23              INC     HL                  
0154: 7E              LD      A,(HL)              
0155: 32 01 78        LD      ($7801),A           ; {hard.dma8257+1} the source channel's transfer count
0158: 23              INC     HL                  
0159: 7E              LD      A,(HL)              
015A: 32 01 78        LD      ($7801),A           ; {hard.dma8257+1} and its high byte
015D: 23              INC     HL                  
015E: 7E              LD      A,(HL)              
015F: 32 02 78        LD      ($7802),A           ; {hard.dma8257+2} destination address low: sprite RAM
0162: 23              INC     HL                  
0163: 7E              LD      A,(HL)              
0164: 32 02 78        LD      ($7802),A           ; {hard.dma8257+2} and its high byte
0167: 23              INC     HL                  
0168: 7E              LD      A,(HL)              
0169: 32 03 78        LD      ($7803),A           ; {hard.dma8257+3} the destination channel's count
016C: 23              INC     HL                  
016D: 7E              LD      A,(HL)              
016E: 32 03 78        LD      ($7803),A           ; {hard.dma8257+3} and its high byte
0171: 3E 01           LD      A,$01               
0173: 32 85 7D        LD      ($7D85),A           ; {hard.dmaRequest} the DRQ rising edge IS the blit
0176: AF              XOR     A                   
0177: 32 85 7D        LD      ($7D85),A           ; {hard.dmaRequest} drop DRQ again
017A: C9              RET                         

; Debounce the coin line, tally pulses, and award credits. coinEdge is a one-bit latch
; held at 1 while no coin is present; a coin counts only when it finds the latch armed,
; and counting clears it, so holding the coin line cannot repeat-credit. A fresh
; insertion also silences whatever is playing and fires the coin chime, unless a game is
; already running, then clears the latch and bumps coinsPartial. Once the tally reaches
; dipCoinsPerCredit it is a full group: reset the tally, add dipCreditsPerCoin to credits
; as a BCD sum unless credits is already at its 0x90 cap, and post a deferred credit
; task.
serviceCoinInput:
017B: 3A 00 7D        LD      A,($7D00)           ; {hard.in2} read the coin/start input port
017E: CB 7F           BIT     7,A                 ; COIN1 is bit 7
0180: 21 03 60        LD      HL,$6003            ; point at the coin edge latch
0183: C2 89 01        JP      NZ,$0189            ; {code.loc_0189} a coin is on the line
0186: 36 01           LD      (HL),$01            ; line idle: re-arm the latch
0188: C9              RET                         

loc_0189:
0189: 7E              LD      A,(HL)              ; was the latch still armed?
018A: A7              AND     A                   
018B: C8              RET     Z                   ; already counted; a held line cannot repeat
018C: E5              PUSH    HL                  
018D: 3A 05 60        LD      A,($6005)           ; {hard.workRam+5} a game in play keeps its own audio
0190: FE 03           CP      $03                 
0192: CA 9D 01        JP      Z,$019D             ; {code.loc_019d} in-game: no chime
0195: CD 1C 01        CALL    $011C               ; {code.silenceSound} cut whatever is playing
0198: 3E 03           LD      A,$03               ; assert the chime for three frames
019A: 32 83 60        LD      ($6083),A           ; {hard.workRam+83} fire the coin-insert chime

loc_019d:
019D: E1              POP     HL                  
019E: 36 00           LD      (HL),$00            ; consume the edge latch
01A0: 2B              DEC     HL                  ; step to the partial-coin tally
01A1: 34              INC     (HL)                ; count this coin pulse
01A2: 11 24 60        LD      DE,$6024            ; point at the coins-per-credit setting
01A5: 1A              LD      A,(DE)              
01A6: 96              SUB     (HL)                ; is the tally a full coin group yet?
01A7: C0              RET     NZ                  ; not yet; leave the tally standing
01A8: 77              LD      (HL),A              ; full group: reset the tally to zero
01A9: 13              INC     DE                  ; point at the credits-per-coin setting
01AA: 2B              DEC     HL                  ; and at the credit count
01AB: EB              EX      DE,HL               
01AC: 1A              LD      A,(DE)              ; read the current credit count
01AD: FE 90           CP      $90                 ; credits are capped at ninety
01AF: D0              RET     NC                  ; at the cap: award nothing further
01B0: 86              ADD     A,(HL)              ; add the credits this group buys
01B1: 27              DAA                         ; keep the count in packed decimal
01B2: 12              LD      (DE),A              ; store the new credit count
01B3: 11 00 04        LD      DE,$0400            ; the deferred credit task, opcode 4
01B6: CD 9F 30        CALL    $309F               ; {code.enqueueTask} onto the task ring
01B9: C9              RET                         

; ---- $01BA-$01C2: data ----
01BA: 00 37 00 AA AA AA 50 76 00

; Game state 0: the one-time power-on setup. gameState is 0 only at reset, and this
; handler's next-to-last act steps it to 1, which is what keeps it from ever running
; again. In order: blank the playfield and the sprite shadow buffer; seed p1Score,
; p2Score and highScore from a nine-byte template in program data (player 1 zero, player
; 2 the attract placeholder, highScore the factory default); set attract = level = lives
; = 1 and repaint the lives and level indicator; decode the DIP bank into the settings
; block; raise the flip-screen latch, advance gameState to 1 (attract), select the 25m
; board and clear gameSubstate; stamp player 1's static "1UP" marker; and post three
; opening tasks onto the task ring.
powerOnInit:
01C3: CD 74 08        CALL    $0874               ; {code.clearPlayfieldAndSprites} blank the screen
01C6: 21 BA 01        LD      HL,$01BA            ; the nine-byte score template in program data
01C9: 11 B2 60        LD      DE,$60B2            ; the three score slots: P1, P2 and high
01CC: 01 09 00        LD      BC,$0009            
01CF: ED B0           LDIR                        ; P1 zero, P2 placeholder, factory high score
01D1: 3E 01           LD      A,$01               
01D3: 32 07 60        LD      ($6007),A           ; {hard.workRam+7} start in attract
01D6: 32 29 62        LD      ($6229),A           ; {hard.workRam+229} level 1
01D9: 32 28 62        LD      ($6228),A           ; {hard.workRam+228} one life, for the indicator
01DC: CD B8 06        CALL    $06B8               ; {code.drawLivesAndLevel} repaint the lives and level panel

loc_01df:
01DF: CD 07 02        CALL    $0207               ; {code.decodeDipSwitches} unpack the operator settings
01E2: 3E 01           LD      A,$01               
01E4: 32 82 7D        LD      ($7D82),A           ; {hard.flipScreen} raise the flip-screen latch
01E7: 32 05 60        LD      ($6005),A           ; {hard.workRam+5} advance to state 1, attract
01EA: 32 27 62        LD      ($6227),A           ; {hard.workRam+227} select the 25m board
01ED: AF              XOR     A                   
01EE: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} clear the in-game sub-state selector
01F1: CD 53 0A        CALL    $0A53               ; {code.draw1UpLabel} stamp player 1's static 1UP marker
01F4: 11 04 03        LD      DE,$0304            ; the first of three opening task messages
01F7: CD 9F 30        CALL    $309F               ; {code.enqueueTask} post it onto the task ring
01FA: 11 02 02        LD      DE,$0202            ; draw-score task for the high score
01FD: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0200: 11 00 02        LD      DE,$0200            ; draw-score task for player 1's score
0203: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0206: C9              RET                         

; Read the cabinet's dsw1 bank once at power-on and fan the one byte out into every
; operator-selectable setting:
;   bits 0-1  lives      -> dipLives, the bits plus 3, so 3 to 6
;   bits 2-3  bonus life -> dipBonusLife, packed decimal 07/10/15/20 = 7000..20000 points
;   bits 4-6  coinage    -> dipCoinsFor1P, dipCoinsFor2P, dipCoinsPerCredit and
;                           dipCreditsPerCoin. With no coinage bit set all four take
;                           their defaults; otherwise bits 5-6 form a 0..3 selector and
;                           bit 4 chooses how it is spread across the four counters
;   bit 7     cabinet    -> dipUpright, 1 upright / 0 cocktail
; Then it copies a fixed 170-byte option table into work RAM. That copy is constant and
; does not depend on the switches at all.
decodeDipSwitches:
0207: 3A 80 7D        LD      A,($7D80)           ; {hard.dsw1} read the operator dip-switch bank
020A: 4F              LD      C,A                 ; keep the switch byte
020B: 21 20 60        LD      HL,$6020            ; point at the settings block
020E: E6 03           AND     $03                 ; bits 0-1 select the lives count
0210: C6 03           ADD     A,$03               ; three to six lives
0212: 77              LD      (HL),A              
0213: 23              INC     HL                  ; on to the bonus-life threshold
0214: 79              LD      A,C                 
0215: 0F              RRCA                        
0216: 0F              RRCA                        ; bits 2-3 select the bonus-life threshold
0217: E6 03           AND     $03                 
0219: 47              LD      B,A                 ; use it as a repeat count
021A: 3E 07           LD      A,$07               ; setting 0 is 7000 points
021C: CA 26 02        JP      Z,$0226             ; {code.loc_0226} take that default
021F: 3E 05           LD      A,$05               ; the others start at 5 and step by 5000

loc_0221:
0221: C6 05           ADD     A,$05               ; add five thousand per step
0223: 27              DAA                         ; the threshold is packed decimal
0224: 10 FB           DJNZ    $0221               ; {code.loc_0221}

loc_0226:
0226: 77              LD      (HL),A              ; store 7/10/15/20 thousand
0227: 23              INC     HL                  ; on to the four coinage counters
0228: 79              LD      A,C                 
0229: 01 01 01        LD      BC,$0101            ; defaults: one coin per credit, one credit
022C: 11 02 01        LD      DE,$0102            ; and one coin for 1P, two for 2P
022F: E6 70           AND     $70                 ; bits 4-6 hold the coinage setting
0231: 17              RLA                         
0232: 17              RLA                         
0233: 17              RLA                         
0234: 17              RLA                         ; leaves the 0..3 selector in A, bit 4 in carry
0235: CA 47 02        JP      Z,$0247             ; {code.loc_0247} no coinage bits set: keep the defaults
0238: DA 41 02        JP      C,$0241             ; {code.loc_0241} bit 4 picks how the selector is spread
023B: 3C              INC     A                   ; one coin buys selector+1 credits
023C: 4F              LD      C,A                 
023D: 5A              LD      E,D                 ; a 2-player game costs the same as 1-player
023E: C3 47 02        JP      $0247               ; {code.loc_0247}

loc_0241:
0241: C6 02           ADD     A,$02               ; a credit costs selector+2 coins
0243: 47              LD      B,A                 
0244: 57              LD      D,A                 
0245: 87              ADD     A,A                 ; and a 2-player game costs twice that
0246: 5F              LD      E,A                 

loc_0247:
0247: 72              LD      (HL),D              ; coins for a 1-player game
0248: 23              INC     HL                  
0249: 73              LD      (HL),E              ; coins for a 2-player game
024A: 23              INC     HL                  
024B: 70              LD      (HL),B              ; coins swallowed per credit group
024C: 23              INC     HL                  
024D: 71              LD      (HL),C              ; credits awarded per completed group
024E: 23              INC     HL                  ; on to the cabinet setting
024F: 3A 80 7D        LD      A,($7D80)           ; {hard.dsw1} read the switch bank again
0252: 07              RLCA                        ; bit 7 is the cabinet type
0253: 3E 01           LD      A,$01               
0255: DA 59 02        JP      C,$0259             ; {code.loc_0259} set means upright
0258: 3D              DEC     A                   ; clear means cocktail

loc_0259:
0259: 77              LD      (HL),A              
025A: 21 65 35        LD      HL,$3565            ; a fixed option table in program data
025D: 11 00 61        LD      DE,$6100            
0260: 01 AA 00        LD      BC,$00AA            ; 170 bytes, the same whatever the switches say
0263: ED B0           LDIR                        
0265: C9              RET                         

; Power-on setup. Zeroes the whole 4K work-RAM page (real RAM stops short of the end, so
; the tail of the wipe lands on nothing), clears sprite RAM, fills video RAM with the
; BLANK tile rather than zero, which is a real glyph, marks every task-ring slot free
; and parks taskHead and taskTail at the ring base, clears the sprite and both palette
; banks, turns flip-screen on, points the stack just past the top of work RAM, silences
; the sound, and unmasks the vblank interrupt. It reads no RAM and stores only
; constants, so what it leaves behind cannot depend on what was there before.
clearRamAndInitHardware:
0266: 06 10           LD      B,$10               ; sixteen passes of 256 bytes: the whole page
0268: 21 00 60        LD      HL,$6000            ; the base of work RAM
026B: AF              XOR     A                   

loc_026c:
026C: 4F              LD      C,A                 ; 256 bytes per pass

loc_026d:
026D: 77              LD      (HL),A              
026E: 23              INC     HL                  
026F: 0D              DEC     C                   
0270: 20 FB           JR      NZ,$026D            ; {code.loc_026d}
0272: 10 F8           DJNZ    $026C               ; {code.loc_026c} real RAM ends early; the tail lands on nothing
0274: 06 04           LD      B,$04               ; four passes: one kilobyte of sprite RAM
0276: 21 00 70        LD      HL,$7000            ; the base of sprite RAM

loc_0279:
0279: 4F              LD      C,A                 

loc_027a:
027A: 77              LD      (HL),A              
027B: 23              INC     HL                  
027C: 0D              DEC     C                   
027D: 20 FB           JR      NZ,$027A            ; {code.loc_027a}
027F: 10 F8           DJNZ    $0279               ; {code.loc_0279}
0281: 06 04           LD      B,$04               ; four passes: one kilobyte of video RAM
0283: 3E 10           LD      A,$10               ; fill with the BLANK tile; zero is a real glyph
0285: 21 00 74        LD      HL,$7400            ; the base of the tilemap

loc_0288:
0288: 0E 00           LD      C,$00               

loc_028a:
028A: 77              LD      (HL),A              
028B: 23              INC     HL                  
028C: 0D              DEC     C                   
028D: 20 FB           JR      NZ,$028A            ; {code.loc_028a}
028F: 10 F7           DJNZ    $0288               ; {code.loc_0288}
0291: 21 C0 60        LD      HL,$60C0            ; the base of the 32-slot task ring
0294: 06 40           LD      B,$40               ; sixty-four bytes, two per slot
0296: 3E FF           LD      A,$FF               ; 0xFF marks a slot free

loc_0298:
0298: 77              LD      (HL),A              
0299: 23              INC     HL                  
029A: 10 FC           DJNZ    $0298               ; {code.loc_0298}
029C: 3E C0           LD      A,$C0               
029E: 32 B0 60        LD      ($60B0),A           ; {hard.workRam+B0} park the enqueue pointer at the ring base
02A1: 32 B1 60        LD      ($60B1),A           ; {hard.workRam+B1} and the dequeue pointer: an empty queue
02A4: AF              XOR     A                   
02A5: 32 83 7D        LD      ($7D83),A           ; {hard.spriteBank} sprite bank off
02A8: 32 86 7D        LD      ($7D86),A           ; {hard.paletteBank0} both palette banks off
02AB: 32 87 7D        LD      ($7D87),A           ; {hard.paletteBank1}
02AE: 3C              INC     A                   
02AF: 32 82 7D        LD      ($7D82),A           ; {hard.flipScreen} flip-screen on
02B2: 31 00 6C        LD      SP,$6C00            ; the first push lands on the last byte of RAM
02B5: CD 1C 01        CALL    $011C               ; {code.silenceSound} silence the audio hardware
02B8: 3E 01           LD      A,$01               
02BA: 32 84 7D        LD      ($7D84),A           ; {hard.nmiEnable} unmask the vblank NMI; from here it can fire

; The task-scheduler main loop, and it runs forever. Each pass reads the current task
; byte out of the scheduler's small table in page 0x60, indexed by a pointer byte the
; table itself supplies, and tests bit 7. Clear: dispatch that task, then wait for
; vblank. Set: run the per-frame work -- repaint the player-up marker, award a bonus life
; if the score has crossed the threshold, bump a frame-work counter -- then compare frame
; against the last frame this loop handled. Unchanged means the frame has not turned over
; yet, so wait. Changed means a new frame arrived: record it, ramp the difficulty, step
; the fixed-hazard animation and its fire release, and wait.
mainLoop:
02BD: 26 60           LD      H,$60               ; the scheduler's table lives in page 0x60
02BF: 3A B1 60        LD      A,($60B1)           ; {hard.workRam+B1} the dequeue pointer
02C2: 6F              LD      L,A                 
02C3: 7E              LD      A,(HL)              ; read the task opcode at the queue head
02C4: 87              ADD     A,A                 ; double for the table; bit 7 marks it free
02C5: 30 1C           JR      NC,$02E3            ; {code.loc_02e3} a real task: dispatch it
02C7: CD 15 03        CALL    $0315               ; {code.redrawPlayerUpIndicator} blink the player-up marker
02CA: CD 50 03        CALL    $0350               ; {code.awardBonusLifeAtThreshold} grant the score bonus life
02CD: 21 19 60        LD      HL,$6019            ; the spin counter that jitters the seed
02D0: 34              INC     (HL)                ; one per pass, however long the frame took
02D1: 21 83 63        LD      HL,$6383            ; the last frame this loop serviced
02D4: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} has the vblank moved the frame counter on?
02D7: BE              CP      (HL)                
02D8: 28 E3           JR      Z,$02BD             ; {code.mainLoop} unchanged: this spin IS the vblank wait
02DA: 77              LD      (HL),A              ; a new frame arrived; remember it
02DB: CD 7F 03        CALL    $037F               ; {code.rampDifficulty} ramp the difficulty
02DE: CD A2 03        CALL    $03A2               ; {code.animateFixedHazardAndReleaseFire} step the fixed hazard
02E1: 18 DA           JR      $02BD               ; {code.mainLoop}

loc_02e3:
02E3: E6 1F           AND     $1F                 ; the doubled opcode as a table offset
02E5: 5F              LD      E,A                 
02E6: 16 00           LD      D,$00               
02E8: 36 FF           LD      (HL),$FF            ; mark the opcode slot free again
02EA: 2C              INC     L                   
02EB: 4E              LD      C,(HL)              ; take the task's argument byte
02EC: 36 FF           LD      (HL),$FF            ; and free that slot too
02EE: 2C              INC     L                   
02EF: 7D              LD      A,L                 
02F0: FE C0           CP      $C0                 ; wrap the dequeue pointer to the ring base
02F2: 30 02           JR      NC,$02F6            ; {code.loc_02f6}
02F4: 3E C0           LD      A,$C0               

loc_02f6:
02F6: 32 B1 60        LD      ($60B1),A           ; {hard.workRam+B1} store the advanced dequeue pointer
02F9: 79              LD      A,C                 ; the handler takes its argument here
02FA: 21 BD 02        LD      HL,$02BD            ; the main loop is the handler's return address
02FD: E5              PUSH    HL                  
02FE: 21 07 03        LD      HL,$0307            ; the table of task handlers
0301: 19              ADD     HL,DE               
0302: 5E              LD      E,(HL)              
0303: 23              INC     HL                  
0304: 56              LD      D,(HL)              
0305: EB              EX      DE,HL               
0306: E9              JP      (HL)                ; enter the task handler

; ---- $0307-$0314: data ----
0307: 1C 05 9B 05 C6 05 E9 05 11 06 2A 06 B8 06

; Blink the "player up" marker column, on every sixteenth frame only -- any other frame
; returns at once, and so does any frame with attract set, so no indicator shows during
; attract. Bit 4 of frame picks the phase. Clear paints the current player's three-cell
; column: the player-number tile (currentPlayer + 1) at the base cell, then two fixed
; tiles, one screen row back each. Set blanks that column and then, in a two-player game
; only, paints the OTHER player's column instead -- so two players alternate markers
; while a lone player's single marker simply blinks.
redrawPlayerUpIndicator:
0315: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} read the frame counter
0318: 47              LD      B,A                 ; keep it; bit 4 is the blink phase
0319: E6 0F           AND     $0F                 ; repaint only on every sixteenth frame
031B: C0              RET     NZ                  
031C: CF              RST     $08                 ; no indicator during attract
031D: 3A 0D 60        LD      A,($600D)           ; {hard.workRam+D} which player is up
0320: CD 47 03        CALL    $0347               ; {code.selectPlayerIndicatorColumnBase} that player's column
0323: 11 E0 FF        LD      DE,$FFE0            ; one tilemap row back between cells
0326: CB 60           BIT     4,B                 ; the blink phase
0328: 28 14           JR      Z,$033E             ; {code.loc_033e} clear: paint the marker
032A: 3E 10           LD      A,$10               ; the blank tile
032C: 77              LD      (HL),A              ; blank the three-cell column
032D: 19              ADD     HL,DE               
032E: 77              LD      (HL),A              
032F: 19              ADD     HL,DE               
0330: 77              LD      (HL),A              
0331: 3A 0F 60        LD      A,($600F)           ; {hard.workRam+F} a lone player's marker just blinks
0334: A7              AND     A                   
0335: C8              RET     Z                   
0336: 3A 0D 60        LD      A,($600D)           ; {hard.workRam+D} two players: show the other one instead
0339: EE 01           XOR     $01                 ; the other player's index
033B: CD 47 03        CALL    $0347               ; {code.selectPlayerIndicatorColumnBase} its column

loc_033e:
033E: 3C              INC     A                   ; the number tile: 1 for P1, 2 for P2
033F: 77              LD      (HL),A              
0340: 19              ADD     HL,DE               
0341: 36 25           LD      (HL),$25            ; then two fixed tiles up the column
0343: 19              ADD     HL,DE               
0344: 36 20           LD      (HL),$20            
0346: C9              RET                         

; A two-way selector: given a player index (0 = player 1, anything else = player 2),
; return the video-RAM base of that player's on-screen indicator column. The caller
; stamps the indicator tiles through it, stepping one tilemap row back per cell, and
; calls again with the other index in a two-player game. Pure: it reads only its input
; and writes nothing.
selectPlayerIndicatorColumnBase:
0347: 21 40 77        LD      HL,$7740            ; player 1's indicator column
034A: A7              AND     A                   
034B: C8              RET     Z                   
034C: 21 E0 74        LD      HL,$74E0            ; player 2's indicator column
034F: C9              RET                         

; Grant the once-per-player bonus life the first time the running score reaches the
; operator-set threshold, then repaint the lives and level panel. bonusLifeAwarded
; latches it, so the award happens at most once per player per game. dipBonusLife holds
; the threshold as a single BCD byte in thousands (0x15 = 15000), and the score's
; thousands and ten-thousands digits are packed into a matching byte to compare against
; it. On a match the latch is set and lives is bumped. The score slot is the one for the
; player up.
awardBonusLifeAtThreshold:
0350: 3A 2D 62        LD      A,($622D)           ; {hard.workRam+22D} already granted this player?
0353: A7              AND     A                   
0354: C0              RET     NZ                  ; at most one bonus life per player per game
0355: 21 B3 60        LD      HL,$60B3            ; player 1's hundreds/thousands digit pair
0358: 3A 0D 60        LD      A,($600D)           ; {hard.workRam+D} the player up owns the score
035B: A7              AND     A                   
035C: 28 03           JR      Z,$0361             ; {code.loc_0361}
035E: 21 B6 60        LD      HL,$60B6            ; player 2's instead

loc_0361:
0361: 7E              LD      A,(HL)              
0362: E6 F0           AND     $F0                 ; the thousands digit
0364: 47              LD      B,A                 
0365: 23              INC     HL                  
0366: 7E              LD      A,(HL)              
0367: E6 0F           AND     $0F                 ; the ten-thousands digit
0369: B0              OR      B                   ; pack the score's thousands into one byte
036A: 0F              RRCA                        
036B: 0F              RRCA                        
036C: 0F              RRCA                        
036D: 0F              RRCA                        ; line it up with the threshold's format
036E: 21 21 60        LD      HL,$6021            ; the operator-set bonus-life threshold
0371: BE              CP      (HL)                
0372: D8              RET     C                   ; not there yet
0373: 3E 01           LD      A,$01               
0375: 32 2D 62        LD      ($622D),A           ; {hard.workRam+22D} latch it so it happens only once
0378: 21 28 62        LD      HL,$6228            ; the player's lives count
037B: 34              INC     (HL)                ; award the extra life
037C: C3 B8 06        JP      $06B8               ; {code.drawLivesAndLevel} repaint the lives panel

; Raise difficulty with the level and with time spent on the board. Two nested dividers
; gate the work: difficultyPrescaler counts every call and the body proceeds only once in
; 256; difficultyClock then advances one step on each of those ticks, and the recompute
; fires on every 8th of those -- once per 2048 calls. On that beat, difficulty =
; min(level + (difficultyClock >> 3), 5). Board setup clears the clock, which is why
; difficulty drops back at the start of every board and then ramps up again.
rampDifficulty:
037F: 21 84 63        LD      HL,$6384            ; the outer rate divider
0382: 7E              LD      A,(HL)              
0383: 34              INC     (HL)                ; counts every serviced frame
0384: A7              AND     A                   
0385: C0              RET     NZ                  ; the body runs once in 256 frames
0386: 21 81 63        LD      HL,$6381            ; the board's difficulty clock
0389: 7E              LD      A,(HL)              
038A: 47              LD      B,A                 
038B: 34              INC     (HL)                ; one step per outer tick
038C: E6 07           AND     $07                 
038E: C0              RET     NZ                  ; recompute only on every eighth step
038F: 78              LD      A,B                 
0390: 0F              RRCA                        
0391: 0F              RRCA                        
0392: 0F              RRCA                        ; how far the clock has run this board
0393: 47              LD      B,A                 
0394: 3A 29 62        LD      A,($6229)           ; {hard.workRam+229} difficulty rises with the level too
0397: 80              ADD     A,B                 
0398: FE 05           CP      $05                 
039A: 38 02           JR      C,$039E             ; {code.loc_039e}
039C: 3E 05           LD      A,$05               ; clamped at five

loc_039e:
039E: 32 80 63        LD      ($6380),A           ; {hard.workRam+380} the barrel and fire behaviour read this
03A1: C9              RET                         

; Animate the board's fixed hazard and, when its counter runs out, ask for a new fire.
; Three gates first: the board mask 0x03, so only 25m and 50m run it at all; Mario must
; be alive; and an event-gate byte's bit 0 must be clear. Then a 4-frame prescaler, so
; the body runs one pass in four. The body needs bit 0 of the hazard's phase byte set --
; the same bit that keeps the drum alight on screen -- and bit 1 then picks one of two
; near-identical arms. Both set the hazard record's X hit extent to 2 and store a sprite
; byte jittered by one on the low bit of spinCount; they differ in the Y extent (0 or 2)
; and the sprite byte (0x40 or 0x42). The bit-1 arm also counts a second timer down and,
; on its underflow, re-sets the phase bit and raises eventReq313c -- which is what makes
; a fire come out a step later.
animateFixedHazardAndReleaseFire:
03A2: 3E 03           LD      A,$03               ; the mask: 25m and 50m only
03A4: F7              RST     $30                 ; the board gate; 75m and 100m skip it all
03A5: D7              RST     $10                 ; and Mario must be alive
03A6: 3A 50 63        LD      A,($6350)           ; {hard.workRam+350} an event gate; bit 0 set suppresses this pass
03A9: 0F              RRCA                        
03AA: D8              RET     C                   
03AB: 21 B8 62        LD      HL,$62B8            ; a 4-frame prescaler
03AE: 35              DEC     (HL)                
03AF: C0              RET     NZ                  ; the body runs one pass in four
03B0: 36 04           LD      (HL),$04            ; reload it
03B2: 3A B9 62        LD      A,($62B9)           ; {hard.workRam+2B9} the hazard's phase byte
03B5: 0F              RRCA                        
03B6: D0              RET     NC                  ; bit 0 clear: nothing to animate this pass
03B7: 21 29 6A        LD      HL,$6A29            ; where the jittered sprite byte lands
03BA: 06 40           LD      B,$40               ; the sprite byte for this arm
03BC: DD 21 A0 66     LD      IX,$66A0            ; the fixed hazard's object record
03C0: 0F              RRCA                        ; bit 1 picks one of two arms
03C1: D2 E4 03        JP      NC,$03E4            ; {code.loc_03e4}
03C4: DD 36 09 02     LD      (IX+$09),$02        ; the record's X hit extent
03C8: DD 36 0A 02     LD      (IX+$0A),$02        ; and its Y hit extent
03CC: 04              INC     B                   
03CD: 04              INC     B                   ; sprite byte 0x42 on this arm
03CE: CD F2 03        CALL    $03F2               ; {code.loc_03f2}
03D1: 21 BA 62        LD      HL,$62BA            ; the release counter
03D4: 35              DEC     (HL)                
03D5: C0              RET     NZ                  
03D6: 3E 01           LD      A,$01               
03D8: 32 B9 62        LD      ($62B9),A           ; {hard.workRam+2B9} re-arm the hazard's phase bit
03DB: 32 A0 63        LD      ($63A0),A           ; {hard.workRam+3A0} ask for a new fire to be released

loc_03de:
03DE: 3E 10           LD      A,$10               
03E0: 32 BA 62        LD      ($62BA),A           ; {hard.workRam+2BA} reload the release counter to sixteen
03E3: C9              RET                         

loc_03e4:
03E4: DD 36 09 02     LD      (IX+$09),$02        ; the record's X hit extent
03E8: DD 36 0A 00     LD      (IX+$0A),$00        ; no Y extent on this arm
03EC: CD F2 03        CALL    $03F2               ; {code.loc_03f2}
03EF: C3 DE 03        JP      $03DE               ; {code.loc_03de}

loc_03f2:
03F2: 70              LD      (HL),B              ; store the sprite byte
03F3: 3A 19 60        LD      A,($6019)           ; {hard.workRam+19} jitter it on the spin counter's low bit
03F6: 0F              RRCA                        
03F7: D8              RET     C                   
03F8: 04              INC     B                   ; nudge the sprite one frame on
03F9: 70              LD      (HL),B              
03FA: C9              RET                         

; Once a frame, service the colour cycle -- with a 50m-only preamble in front of it. On
; any board but the conveyors it simply drives the cycle. On 50m it first shifts the X
; of all ten spriteObjBlock records by m50Obj1Step, sliding the whole row of props by
; that signed delta, then takes the now-shifted third record's X less a fixed anchor and
; stores it as m50ObjRowShift, the delta the 50m column painter later adds back into
; that same column. What those ten sprite-objects depict is not established: the
; template stamped into the block is the same on every board, so it carries no per-board
; identity.
slide50mSpriteRowAndServiceColorCycle:
03FB: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} the 50m conveyor board has a preamble
03FE: FE 02           CP      $02                 
0400: C2 13 04        JP      NZ,$0413            ; {code.serviceColorCycle} any other board: straight to the cycle
0403: 21 08 69        LD      HL,$6908            ; the X field of the ten sprite-objects
0406: 3A A3 63        LD      A,($63A3)           ; {hard.workRam+3A3} the 50m object's signed step this frame
0409: 4F              LD      C,A                 
040A: FF              RST     $38                 ; slide the whole row of props by it
040B: 3A 10 69        LD      A,($6910)           ; {hard.workRam+910} the third record's shifted X
040E: D6 3B           SUB     $3B                 ; measure it against a fixed anchor
0410: 32 B7 63        LD      ($63B7),A           ; {hard.workRam+3B7} the 50m column painter adds this back

; The once-a-frame entry to the attract colour cycle, picking one of three things to do.
; A sweep already running (colourCycleActive set) is stepped on and this frame's colour
; work painted; with no sweep and frame not at its wrap, only the colour column is
; repainted; with no sweep and frame just wrapped to zero, colourCycleActive is set and
; a fresh sweep advanced at once. So a sweep starts once every 256 frames and then runs
; for its own lifetime. Setting that flag is the only write made here.
serviceColorCycle:
0413: 3A 91 63        LD      A,($6391)           ; {hard.workRam+391} is a sweep already running?
0416: A7              AND     A                   
0417: C2 26 04        JP      NZ,$0426            ; {code.advanceColorCycleSweep} step it on
041A: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} a sweep starts at the frame-counter wrap
041D: A7              AND     A                   
041E: C2 86 04        JP      NZ,$0486            ; {code.dispatchColorCyclePaint} not yet: repaint only
0421: 3E 01           LD      A,$01               
0423: 32 91 63        LD      ($6391),A           ; {hard.workRam+391} arm a fresh sweep

; The per-frame driver of the attract-screen colour cycle. It bumps the sweep counter by
; one and routes the frame's colour work four ways on the new value: the counter reaching
; its top ends the sweep (clearing the counter and the active flag) and paints; a
; non-zero reload gate, or a frame that is not a 32-frame boundary, gives the repaint
; alone; a 32-frame boundary with the gate open reloads the 40-byte sprite-object block
; from a fixed template, asserts a 3-frame sound beat, and runs the full colour cascade.
; Bit 5 of the counter alternates the template, so the two swap every 32 frames.
advanceColorCycleSweep:
0426: 21 90 63        LD      HL,$6390            ; the sweep counter
0429: 34              INC     (HL)                ; one step per frame
042A: 7E              LD      A,(HL)              
042B: FE 80           CP      $80                 
042D: CA 64 04        JP      Z,$0464             ; {code.resetColorCycleSweep} the sweep has topped out
0430: 3A 93 63        LD      A,($6393)           ; {hard.workRam+393} a gate that suppresses the reload
0433: A7              AND     A                   
0434: C2 86 04        JP      NZ,$0486            ; {code.dispatchColorCyclePaint} gate shut: repaint only
0437: 7E              LD      A,(HL)              
0438: 47              LD      B,A                 
0439: E6 1F           AND     $1F                 ; act only on a 32-frame boundary
043B: C2 86 04        JP      NZ,$0486            ; {code.dispatchColorCyclePaint} in between: repaint only
043E: 21 CF 39        LD      HL,$39CF            ; one of two sprite-object templates
0441: CB 68           BIT     5,B                 ; bit 5 alternates them every 32 frames
0443: 20 03           JR      NZ,$0448            ; {code.loc_0448}
0445: 21 F7 39        LD      HL,$39F7            ; the other template

loc_0448:
0448: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock} reload the ten records
044B: 3E 03           LD      A,$03               ; a three-frame sound beat
044D: 32 82 60        LD      ($6082),A           ; {hard.workRam+82} assert it on the cascade's trigger

; The per-frame colour-cascade dispatcher: route by the current board into one of the
; colour-cycle arms. board bit 0 clear (the even boards, 50m and 100m) takes the
; even-board arm, which shifts the sprite-object block's X column by a board-specific
; delta before the colour repaint. 75m goes straight into the repaint with no sprite
; shift. 25m first nudges the whole ten-record block's Y column up 4 pixels, then
; repaints. This routine writes no memory of its own -- the sprite and colour writes all
; belong to the arms.
dispatchColorCascadeByBoard:
0450: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} route the cascade by board
0453: 0F              RRCA                        
0454: D2 78 04        JP      NC,$0478            ; {code.shiftEvenBoardSpriteColumn} the even boards shift X
0457: 0F              RRCA                        
0458: DA 86 04        JP      C,$0486             ; {code.dispatchColorCyclePaint} 75m repaints with no sprite shift
045B: 21 0B 69        LD      HL,$690B            ; 25m: the Y field of the ten records
045E: 0E FC           LD      C,$FC               ; nudge the whole row up four pixels
0460: FF              RST     $38                 
0461: C3 86 04        JP      $0486               ; {code.dispatchColorCyclePaint}

; Ends the colour-cycle sweep on the frame its counter tops out at 0x80: clear the
; counter back to 0 and lower colourCycleActive, then continue into the frame's colour
; work. With the sprite-object reload gate set it goes straight to the colour repaint;
; with the gate clear it first reloads the 40-byte sprite-object block from its template
; and then runs the full per-board colour cascade. It is the end half only -- what
; STARTS the next sweep is a re-arm at the frame-counter wrap, elsewhere.
resetColorCycleSweep:
0464: AF              XOR     A                   
0465: 77              LD      (HL),A              ; restart the sweep counter
0466: 23              INC     HL                  
0467: 77              LD      (HL),A              ; and lower the active flag
0468: 3A 93 63        LD      A,($6393)           ; {hard.workRam+393} the reload gate again
046B: A7              AND     A                   
046C: C2 86 04        JP      NZ,$0486            ; {code.dispatchColorCyclePaint} shut: repaint only
046F: 21 5C 38        LD      HL,$385C            ; re-seed the block from its template
0472: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock}
0475: C3 50 04        JP      $0450               ; {code.dispatchColorCascadeByBoard}

; The even-board arm of the per-frame colour cascade, reached when board's low bit is
; clear -- 50m and 100m. It shifts the X field of all ten spriteObjBlock records by one
; delta, repositioning the whole staged row with a single number: on 50m the delta comes
; from m50ObjRowShift, the byte staged for that board; on the other even board it is a
; fixed +0x44. Control then continues into the per-frame colour-cycle repaint.
shiftEvenBoardSpriteColumn:
0478: 21 08 69        LD      HL,$6908            ; the X field of the ten sprite-objects
047B: 0E 44           LD      C,$44               ; 100m's fixed shift
047D: 0F              RRCA                        ; which even board?
047E: D2 85 04        JP      NC,$0485            ; {code.loc_0485} 100m keeps the fixed shift
0481: 3A B7 63        LD      A,($63B7)           ; {hard.workRam+3B7} 50m uses its own staged delta
0484: 4F              LD      C,A                 

loc_0485:
0485: FF              RST     $38                 ; slide the whole row by one delta

; Decide each frame how the flashing colour column is repainted, and let the right
; painter do it. It takes the sweep counter as this frame's phase, sets up the one-row
; descending stride the painters walk, and hands off to exactly one of three: on the 100m
; rivet board, that board's own two-column blink block; elsewhere, the painter that
; forces the HIGH colour code while bit 6 of the counter is set, and the LOW-code painter
; while it is clear. So bit 6 is the colour toggle and the column flashes as the counter
; advances. It writes nothing itself.
dispatchColorCyclePaint:
0486: 3A 90 63        LD      A,($6390)           ; {hard.workRam+390} the sweep counter is this frame's phase
0489: 4F              LD      C,A                 
048A: 11 20 00        LD      DE,$0020            ; the painters step one tilemap row
048D: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} the rivet board has its own painter
0490: FE 04           CP      $04                 
0492: CA BE 04        JP      Z,$04BE             ; {code.runRivetColorCycleBlink} 100m
0495: 79              LD      A,C                 
0496: A7              AND     A                   
0497: CA A1 04        JP      Z,$04A1             ; {code.paintColorColumnWithLowCode} phase 0: the low code
049A: 3E EF           LD      A,$EF               ; the high colour code
049C: CB 71           BIT     6,C                 ; bit 6 of the counter is the colour toggle
049E: C2 A3 04        JP      NZ,$04A3            ; {code.paintColorColumnAndHoldBlink} set: paint high

; The colour-cycle blink driver's LOW-CODE arm. Its only act of its own is to preset the
; fill code to 0x10; it then falls into the shared 3-cell colour-column paint, which lays
; 0x10 / 0x0F / 0x0E down a column at a stride of 0x20 and holds the sprite blink. The
; sibling arm supplies 0xEF instead (0xEF / 0xEE / 0xED), and the driver picks between
; them on its sweep counter, so the element flashes between the two colour sets as it
; advances.
paintColorColumnWithLowCode:
04A1: 3E 10           LD      A,$10               ; the low colour code

; The plain, non-rivet arm of the colour-cycle blink driver. It repaints a 3-cell
; descending colour-memory column, laying A, A-1 and A-2 one stride apart, with both the
; fill value and the stride handed in live by the driver -- so the cell cycles between
; two attribute bytes as the sweep counter advances. It then reloads sprite record #1's
; CURRENT code byte and passes it to the shared blink store UNCHANGED: its sibling arms
; force the blink bit on or off, this one never sets or clears it. Four cells written,
; then return.
paintColorColumnAndHoldBlink:
04A3: 21 C4 75        LD      HL,$75C4            ; the top of the flashing colour column
04A6: CD 14 05        CALL    $0514               ; {code.fillDescendingColumn} lay three descending codes down it
04A9: 3A 05 69        LD      A,($6905)           ; {hard.workRam+905} sprite record 1's code byte, unchanged

; The shared store tail of the blink driver behind the attract and how-high screens,
; which blinks two decorative sprites by toggling bit 7 of their code bytes. All three
; of its arms work out sprite record 1's finished code byte and fall in here, the one
; place that stores it. Once per colour-cycle sweep -- when the sweep counter has bit 6
; set and its low three bits clear -- it also flips that code's two low bits, advancing
; the sprite to its alternate animation cell. At any other counter value the byte is
; stored unchanged.
storeBlinkSpriteCode:
04AC: 32 05 69        LD      ($6905),A           ; {hard.workRam+905} commit the blink sprite's code byte
04AF: CB 71           BIT     6,C                 
04B1: C8              RET     Z                   
04B2: 47              LD      B,A                 
04B3: 79              LD      A,C                 
04B4: E6 07           AND     $07                 ; only every eighth counter value
04B6: C0              RET     NZ                  
04B7: 78              LD      A,B                 
04B8: EE 03           XOR     $03                 ; step the sprite to its alternate cell
04BA: 32 05 69        LD      ($6905),A           ; {hard.workRam+905} store the advanced code
04BD: C9              RET                         

; The 100m branch of the colour cycle: repaint two decorative colour columns, then blink
; a sprite pair. Column A takes colour codes 16/15/14 and column B continues the SAME
; descending run with 13/12/11, both stepping one tilemap row apart, so the six cells
; read as one continuous gradient that cycles with the sweep counter. Then, on the
; counter's phase bit: clear, blink the first two sprite records purely by which half of
; the screen Mario is in; set, repaint column B (Mario right) or column A in the brighter
; band starting at 223 (Mario left), and force the pair's blink off or on to match.
runRivetColorCycleBlink:
04BE: 3E 10           LD      A,$10               ; the run starts at colour code 16
04C0: 21 23 76        LD      HL,$7623            ; the top of the first colour column
04C3: CD 14 05        CALL    $0514               ; {code.fillDescendingColumn} 16, 15, 14 down the column
04C6: 21 83 75        LD      HL,$7583            ; the second column continues the run
04C9: CD 14 05        CALL    $0514               ; {code.fillDescendingColumn} 13, 12, 11: one continuous gradient
04CC: CB 71           BIT     6,C                 ; the slow blink phase
04CE: CA 09 05        JP      Z,$0509             ; {code.blinkSpritePairByX} blink purely on Mario's screen half
04D1: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} which half of the screen is Mario in?
04D4: FE 80           CP      $80                 
04D6: D2 F1 04        JP      NC,$04F1            ; {code.paintColorColumnAndBlinkOff} right half
04D9: 3E DF           LD      A,$DF               ; the brighter band
04DB: 21 23 76        LD      HL,$7623            ; repaint the first column in it
04DE: CD 14 05        CALL    $0514               ; {code.fillDescendingColumn}

; The colour-cycle driver's "blink ON" arm: raise bit 7 -- the flip/visibility bit -- in
; the code bytes of both decorative blink sprites, records 0 and 1 of the sprite shadow
; buffer. Record 0 is set in place; record 1's result goes to the shared blink-store
; tail, which commits it and may apply its once-per-sweep low-two-bit tile toggle.
; Reached on the rivet board only, selected by Mario's X and the sweep counter's bit 6.
; Its exact mirror is the "blink OFF" arm.
blinkSpritePairOn:
04E1: 3A 01 69        LD      A,($6901)           ; {hard.workRam+901} the first decorative sprite's code byte
04E4: F6 80           OR      $80                 ; raise the flip/visibility bit
04E6: 32 01 69        LD      ($6901),A           ; {hard.workRam+901}
04E9: 3A 05 69        LD      A,($6905)           ; {hard.workRam+905} the second sprite's code byte
04EC: F6 80           OR      $80                 
04EE: C3 AC 04        JP      $04AC               ; {code.storeBlinkSpriteCode} the shared store tail commits it

; The rivet-board colour-cycle arm, taken when Mario is in the right half of the screen.
; It presets the fill value to 0xEF and lays a 3-cell descending colour column -- 0xEF,
; 0xEE, 0xED into the top cell and the two cells below it, the stride handed in by the
; driver -- then blinks the decorative sprite pair OFF, forcing the flip/visibility bit
; clear on both records' code bytes. Five cells written.
paintColorColumnAndBlinkOff:
04F1: 3E EF           LD      A,$EF               ; the high colour code
04F3: 21 83 75        LD      HL,$7583            ; repaint the second column
04F6: CD 14 05        CALL    $0514               ; {code.fillDescendingColumn} 0xEF, 0xEE, 0xED down it

; The "blink off" arm of the colour-cycle blink driver: force bit 7, the flip/visibility
; bit, clear on both decorative sprites -- records 0 and 1 of the sprite shadow buffer.
; Record 0 is masked and committed here; record 1 is masked and handed to the shared
; store tail, which commits it and applies the once-per-sweep tile toggle. The off phase
; is taken on 100m and on specific colour paths, so it is not a per-frame arm.
blinkSpritePairOff:
04F9: 3A 01 69        LD      A,($6901)           ; {hard.workRam+901} the first decorative sprite's code byte
04FC: E6 7F           AND     $7F                 ; force the flip/visibility bit clear
04FE: 32 01 69        LD      ($6901),A           ; {hard.workRam+901}
0501: 3A 05 69        LD      A,($6905)           ; {hard.workRam+905} the second sprite's code byte
0504: E6 7F           AND     $7F                 
0506: C3 AC 04        JP      $04AC               ; {code.storeBlinkSpriteCode} the shared store tail commits it

; Blink the rivet board's two decorative sprites by which half of the screen Mario is on.
; It drives the top bit -- the flip/visibility bit -- of both sprite code bytes: marioX
; in the right half forces it clear (blink off), the left half forces it set (blink on).
; The split is the screen midpoint and the test is inclusive on the right, so exactly
; midway counts as the right half. Both arms write both bytes.
blinkSpritePairByX:
0509: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} Mario's position picks the blink phase
050C: FE 80           CP      $80                 ; the screen midpoint
050E: D2 F9 04        JP      NC,$04F9            ; {code.blinkSpritePairOff} right half: blink off
0511: C3 E1 04        JP      $04E1               ; {code.blinkSpritePairOn} left half: blink on

; Write three descending bytes at a caller-supplied stride. From the caller's pointer it
; stores the caller's value, steps the pointer by the stride and drops the value by one,
; exactly three times -- v, v-1, v-2 at p, p+stride, p+2*stride. The trip count is fixed,
; so there is no data-dependent branch. Every caller hands it a tilemap column with a
; one-row stride, so in practice it lays a run of three descending TILE CODES down a
; column, during the attract cycle and during board init. This hardware has no writable
; colour RAM -- the whole 7400:77ff window is the tilemap -- so nothing here is coloured.
fillDescendingColumn:
0514: 06 03           LD      B,$03               ; always three cells

loc_0516:
0516: 77              LD      (HL),A              ; lay the colour code
0517: 19              ADD     HL,DE               ; step by the caller's stride
0518: 3D              DEC     A                   ; the next cell is one code lower
0519: 10 FB           DJNZ    $0516               ; {code.loc_0516}
051B: C9              RET                         

; Task opcode 0: add to the score of the player up, redraw it, and promote it to the
; high score if it now leads. The task payload indexes a table of 3-byte packed-BCD
; addends (payload 1 -> +100, 5 -> +500, 11 -> +1000; 0 and 10 add nothing). The whole
; task is skipped while no credited game is in progress. The add runs least-significant
; byte first, rippling the carry upward and BCD-correcting each byte, and the readout is
; repainted from the result. The high-score compare then walks the other way, from the
; top byte DOWN, and stops as soon as a byte is lower or all three prove equal. On a
; byte that is greater the score leads: only the bytes not yet proven equal are copied
; over highScore -- reloading a width of three would clobber bytes the compare already
; matched -- and the on-screen high score is repainted.
addToScoreTask:
051C: 4F              LD      C,A                 ; the task payload picks the amount
051D: CF              RST     $08                 ; no score awarded during attract
051E: CD 5F 05        CALL    $055F               ; {code.selectCurrentPlayerScoreCounter} the player-up's counter
0521: 79              LD      A,C                 
0522: 81              ADD     A,C                 
0523: 81              ADD     A,C                 ; three bytes per table entry
0524: 4F              LD      C,A                 
0525: 21 29 35        LD      HL,$3529            ; the table of packed-BCD addends
0528: 06 00           LD      B,$00               
052A: 09              ADD     HL,BC               ; index the amount this payload awards
052B: A7              AND     A                   ; start the add with a clear carry
052C: 06 03           LD      B,$03               ; three bytes of packed decimal

loc_052e:
052E: 1A              LD      A,(DE)              
052F: 8E              ADC     A,(HL)              ; add, rippling the carry upward
0530: 27              DAA                         ; and keep the result decimal
0531: 12              LD      (DE),A              
0532: 13              INC     DE                  
0533: 23              INC     HL                  
0534: 10 F8           DJNZ    $052E               ; {code.loc_052e}
0536: D5              PUSH    DE                  ; save the end of the counter
0537: 1B              DEC     DE                  ; point at its most significant pair
0538: 3A 0D 60        LD      A,($600D)           ; {hard.workRam+D} the player's own score column
053B: CD 6B 05        CALL    $056B               ; {code.loc_056b} repaint the six digits
053E: D1              POP     DE                  
053F: 1B              DEC     DE                  ; back to the top pair for the compare
0540: 21 BA 60        LD      HL,$60BA            ; the high score's top byte
0543: 06 03           LD      B,$03               

loc_0545:
0545: 1A              LD      A,(DE)              
0546: BE              CP      (HL)                
0547: D8              RET     C                   ; a lower byte: the record stands
0548: C2 50 05        JP      NZ,$0550            ; {code.loc_0550} a greater byte: the score leads
054B: 1B              DEC     DE                  ; equal so far; walk both down a byte
054C: 2B              DEC     HL                  
054D: 10 F6           DJNZ    $0545               ; {code.loc_0545}
054F: C9              RET                         ; all three equal: nothing to promote

loc_0550:
0550: CD 5F 05        CALL    $055F               ; {code.selectCurrentPlayerScoreCounter} the winning counter
0553: 21 B8 60        LD      HL,$60B8            ; the high-score record's base

loc_0556:
0556: 1A              LD      A,(DE)              
0557: 77              LD      (HL),A              ; copy only the bytes not proven equal
0558: 13              INC     DE                  
0559: 23              INC     HL                  
055A: 10 FA           DJNZ    $0556               ; {code.loc_0556}
055C: C3 DA 05        JP      $05DA               ; {code.drawHighScore} repaint the high score on screen

; Hand back the base address of the score counter for the player up -- p1Score when
; currentPlayer is zero, p2Score otherwise. The score-award and high-score compare paths
; call this to learn which counter to touch, then work from the address returned.
selectCurrentPlayerScoreCounter:
055F: 11 B2 60        LD      DE,$60B2            ; player 1's score counter
0562: 3A 0D 60        LD      A,($600D)           ; {hard.workRam+D} which player is up
0565: A7              AND     A                   
0566: C8              RET     Z                   
0567: 11 B5 60        LD      DE,$60B5            ; player 2's score counter
056A: C9              RET                         

loc_056b:
056B: DD 21 81 77     LD      IX,$7781            ; one of the two score columns
056F: A7              AND     A                   
0570: 28 0A           JR      Z,$057C             ; {code.renderBcdColumn} selector zero takes this one
0572: DD 21 21 75     LD      IX,$7521            ; the other column
0576: 18 04           JR      $057C               ; {code.renderBcdColumn}

; Draw a packed 3-byte BCD counter as six digits climbing a fixed video column. The
; caller hands over the source pointer -- three bytes, two digits each -- and this entry
; hard-wires the destination cell, sets the per-digit stride to minus one tilemap row,
; sets the count to 3 bytes, and falls into the shared expansion loop, which emits the
; HIGH then the LOW nibble of each source byte while walking the source backwards. A
; second caller enters one instruction later with a column of its own, skipping the
; fixed-cell store. Which counter the fixed cell displays is not established here.
renderBcdColumnFixedCell:
0578: DD 21 41 76     LD      IX,$7641            ; the fixed destination cell

; Draw a packed 3-byte BCD value as six digits climbing a video column. The caller
; supplies the source pointer (three bytes, two digits each) and the destination cell.
; This is the fixed-cell score renderer entered one instruction later, so the caller's
; destination survives where that entry's is hard-wired -- which is how the score column
; and the on-board bonus-item value share one renderer. It sets the per-digit stride to
; -0x20 (back one tilemap row, so digits climb) and the source count to 3, then falls
; into the shared expansion loop, which emits the high nibble then the low of each source
; byte while walking the source backwards.
renderBcdColumn:
057C: EB              EX      DE,HL               ; the caller's source counter
057D: 11 E0 FF        LD      DE,$FFE0            ; back one tilemap row, so digits climb
0580: 01 04 03        LD      BC,$0304            ; three source bytes, six digits

; Turn a packed counter into the individual digit cells that draw it on screen. Per
; source byte it emits the HIGH nibble first and then the LOW one, pushing both through
; a shared store-and-advance step that masks a nibble, writes it at the destination
; cursor and moves the cursor on by the caller's stride. The source pointer walks
; BACKWARDS while the cursor walks forwards: that reversal is what turns a counter held
; least-significant-byte-first into digits laid out in reading order. Getting the high
; digit out is a nibble SWAP, not a shift, so one store serves both digits and there is
; no separate high-digit variant.
expandBcdDigits:
0583: 7E              LD      A,(HL)              
0584: 0F              RRCA                        
0585: 0F              RRCA                        
0586: 0F              RRCA                        
0587: 0F              RRCA                        ; bring the high digit down into place
0588: CD 93 05        CALL    $0593               ; {code.storeDigitAndAdvance} emit the high digit
058B: 7E              LD      A,(HL)              ; the low digit is already in place
058C: CD 93 05        CALL    $0593               ; {code.storeDigitAndAdvance} emit it too
058F: 2B              DEC     HL                  ; walk the source back, the cells forward
0590: 10 F1           DJNZ    $0583               ; {code.expandBcdDigits}
0592: C9              RET                         

; The innermost leaf of the BCD counter renderer: mask the value to its low nibble --
; one digit, the caller loop having already rotated the wanted nibble down -- store it
; into the tilemap cell the cursor points at, and step the cursor by the caller's
; stride. The caller owns the direction and the spacing, so the same leaf draws a column
; of digits either way.
storeDigitAndAdvance:
0593: E6 0F           AND     $0F                 ; one digit
0595: DD 77 00        LD      (IX+$00),A          ; write it into the tilemap cell
0598: DD 19           ADD     IX,DE               ; step the cursor by the caller's stride
059A: C9              RET                         

; Zero one of the three score counters, then repaint it. The task ring dispatches this
; with a payload naming the counter: 0 = p1Score, 2 = highScore, anything else below 3 =
; p2Score. Each is a 3-byte little-endian packed-BCD counter; all three bytes are zeroed
; and the score-draw task then repaints that column, now reading 000000. This is the
; clear-first twin of that draw task, and it is the reset that happens when a game starts
; -- nothing resets a score during attract, which only redraws.
resetScoreCounter:
059B: FE 03           CP      $03                 
059D: D2 BD 05        JP      NC,$05BD            ; {code.loc_05bd} payload 3 and up clears the lower ones too
05A0: F5              PUSH    AF                  ; the draw task needs the payload back
05A1: 21 B2 60        LD      HL,$60B2            ; payload 0: player 1's score
05A4: A7              AND     A                   
05A5: CA AB 05        JP      Z,$05AB             ; {code.loc_05ab}
05A8: 21 B5 60        LD      HL,$60B5            ; otherwise player 2's

loc_05ab:
05AB: FE 02           CP      $02                 
05AD: C2 B3 05        JP      NZ,$05B3            ; {code.loc_05b3}
05B0: 21 B8 60        LD      HL,$60B8            ; payload 2: the high score

loc_05b3:
05B3: AF              XOR     A                   
05B4: 77              LD      (HL),A              ; zero all three packed-BCD bytes
05B5: 23              INC     HL                  
05B6: 77              LD      (HL),A              
05B7: 23              INC     HL                  
05B8: 77              LD      (HL),A              
05B9: F1              POP     AF                  
05BA: C3 C6 05        JP      $05C6               ; {code.drawScoreTask} repaint it, now reading 000000

loc_05bd:
05BD: 3D              DEC     A                   ; step down to the next counter
05BE: F5              PUSH    AF                  
05BF: CD 9B 05        CALL    $059B               ; {code.resetScoreCounter} clear that one
05C2: F1              POP     AF                  
05C3: C8              RET     Z                   
05C4: 18 F7           JR      $05BD               ; {code.loc_05bd} and keep going down to zero

; Repaint one of the three on-screen score readouts, chosen by the task's payload: 0 is
; p1Score, 1 is p2Score, 2 is highScore. Any other non-zero value falls in with p2Score,
; because the arms are single equality tests. Each score is three packed digit-pairs
; stored least-significant first and the renderer walks it from the TOP, so the source
; pointer is set to the counter's base plus two before the hand-off; the high-score arm's
; own tail knows where its record is. Payload 3 selects a clear-and-redraw arm.
drawScoreTask:
05C6: FE 03           CP      $03                 
05C8: CA E0 05        JP      Z,$05E0             ; {code.loc_05e0} payload 3 redraws every counter
05CB: 11 B4 60        LD      DE,$60B4            ; player 1's most significant digit pair
05CE: A7              AND     A                   
05CF: CA D5 05        JP      Z,$05D5             ; {code.loc_05d5}
05D2: 11 B7 60        LD      DE,$60B7            ; player 2's, for any other payload

loc_05d5:
05D5: FE 02           CP      $02                 
05D7: C2 6B 05        JP      NZ,$056B            ; {code.loc_056b} paint the six digits up that column

; Repaint the on-screen high-score readout from highScore. It points the render source
; at the counter's most-significant pair, so the fixed-column BCD renderer walks the
; three packed bytes top-down and the six digits paint in reading order up the column.
; It is the shared tail of the two score tasks that need the record redrawn, and it
; overrides whatever source the caller left -- that unconditional override is why it
; exists as a shared tail.
drawHighScore:
05DA: 11 BA 60        LD      DE,$60BA            ; the high score's most significant pair
05DD: C3 78 05        JP      $0578               ; {code.renderBcdColumnFixedCell} paint it up its fixed column

loc_05e0:
05E0: 3D              DEC     A                   ; step down to the next readout
05E1: F5              PUSH    AF                  
05E2: CD C6 05        CALL    $05C6               ; {code.drawScoreTask} repaint that one
05E5: F1              POP     AF                  
05E6: C8              RET     Z                   
05E7: 18 F7           JR      $05E0               ; {code.loc_05e0} and keep going down to zero

; Draw one of the game's canned strings, or wipe it off again. A payload byte selects
; the string through two indirections: doubled into a pointer table, whose entry is a
; string DESCRIPTOR -- first word the screen cell to start at, then the characters, then
; a sentinel. Characters go one per cell, stepping the destination back a whole tilemap
; row each time, so the run is vertical in tilemap terms, which is what reads as
; horizontal text on a monitor rotated a quarter turn. Bit 7 of the payload is a
; per-call ERASE flag: every cell gets its character and is then immediately overwritten
; with the blank tile, clearing the string's footprint. It does not change which string
; is selected.
drawStringVertical:
05E9: 21 4B 36        LD      HL,$364B            ; base of the canned-string pointer table
05EC: 87              ADD     A,A                 ; double the payload into a word index; bit 7 falls into carry
05ED: F5              PUSH    AF                  ; hold the erase flag across the whole run
05EE: E6 7F           AND     $7F                 ; drop what the erase flag left in the index
05F0: 5F              LD      E,A                 
05F1: 16 00           LD      D,$00               
05F3: 19              ADD     HL,DE               ; index the pointer table
05F4: 5E              LD      E,(HL)              
05F5: 23              INC     HL                  
05F6: 56              LD      D,(HL)              ; the entry is the string's descriptor address
05F7: EB              EX      DE,HL               
05F8: 5E              LD      E,(HL)              
05F9: 23              INC     HL                  
05FA: 56              LD      D,(HL)              ; descriptor word 0 is the cell to start at
05FB: 23              INC     HL                  ; the characters follow the descriptor word
05FC: 01 E0 FF        LD      BC,$FFE0            ; step back one tilemap row per character
05FF: EB              EX      DE,HL               

loc_0600:
0600: 1A              LD      A,(DE)              ; the next character
0601: FE 3F           CP      $3F                 ; the sentinel that ends the string
0603: CA 26 00        JP      Z,$0026             ; {code.loc_0026} done: drop the saved flag word and return
0606: 77              LD      (HL),A              ; put the character in its cell
0607: F1              POP     AF                  ; recover the erase flag
0608: 30 02           JR      NC,$060C            ; {code.loc_060c} not erasing, so the character stands
060A: 36 10           LD      (HL),$10            ; erase mode: overwrite it with the blank tile

loc_060c:
060C: F5              PUSH    AF                  
060D: 13              INC     DE                  ; next character
060E: 09              ADD     HL,BC               ; and one tilemap row back
060F: 18 EF           JR      $0600               ; {code.loc_0600}

; Repaint the "CREDIT nn" line, but only while no credited game is in progress. It tests
; bit 0 of attract: set (attract) repaints the whole line, the label plus the current
; credit count; clear (a game in play) leaves the line alone. So the credit line is
; refreshed only on the attract and idle screens, which is where it is shown.
drawCreditLineInAttract:
0611: 3A 07 60        LD      A,($6007)           ; {hard.workRam+7} non-zero while no credited game is running
0614: 0F              RRCA                        
0615: D0              RET     NC                  ; bit clear means a game is in play, so leave the line alone

; Paint the "CREDIT nn" line. First draw canned string 5 -- the letters CREDIT -- down
; its tilemap column through the shared vertical string renderer. Then render credits,
; one packed-BCD byte, as its two digits into the display column, stepping one tilemap
; row UP between the high and low digit. The digit expander is entered in tail position,
; so its return goes to this routine's caller.
drawCreditDisplay:
0616: 3E 05           LD      A,$05               ; canned string 5 is the word CREDIT
0618: CD E9 05        CALL    $05E9               ; {code.drawStringVertical} draw the CREDIT label down its column
061B: 21 01 60        LD      HL,$6001            ; the credit count is the source byte
061E: 11 E0 FF        LD      DE,$FFE0            ; step one tilemap row up between the two digits
0621: DD 21 BF 74     LD      IX,$74BF            ; the credit readout's digit cells
0625: 06 01           LD      B,$01               ; one packed byte, so two digits
0627: C3 83 05        JP      $0583               ; {code.expandBcdDigits} returns to this routine's caller

loc_062a:
062A: A7              AND     A                   ; a task payload of 0 means cash the readout in
062B: CA 91 06        JP      Z,$0691             ; {code.awardRemainingBonusToScore}
062E: 3A 8C 63        LD      A,($638C)           ; {hard.workRam+38C} how much is showing on the readout
0631: A7              AND     A                   
0632: C2 A8 06        JP      NZ,$06A8            ; {code.stepBonusDisplayDown} still counting: take one notch off it
0635: 3A B8 63        LD      A,($63B8)           ; {hard.workRam+3B8} already bottomed out, so nothing to do
0638: A7              AND     A                   
0639: C0              RET     NZ                  
063A: 3A B0 62        LD      A,($62B0)           ; {hard.workRam+2B0} the board's starting bonus
063D: 01 0A 00        LD      BC,$000A            ; divide it by ten by repeated subtraction

loc_0640:
0640: 04              INC     B                   
0641: 91              SUB     C                   
0642: C2 40 06        JP      NZ,$0640            ; {code.loc_0640}
0645: 78              LD      A,B                 ; the quotient is the tens digit
0646: 07              RLCA                        ; swap it into the high nibble of the packed byte
0647: 07              RLCA                        
0648: 07              RLCA                        
0649: 07              RLCA                        
064A: 32 8C 63        LD      ($638C),A           ; {hard.workRam+38C} seed the readout with it
064D: 21 4A 38        LD      HL,$384A            ; the tile block that frames the readout
0650: 11 65 74        LD      DE,$7465            ; the first of six columns
0653: 3E 06           LD      A,$06               ; six columns of three cells each

loc_0655:
0655: DD 21 1D 00     LD      IX,$001D            ; three written plus 0x1D reaches the next column
0659: 01 03 00        LD      BC,$0003            
065C: ED B0           LDIR                        
065E: DD 19           ADD     IX,DE               
0660: DD E5           PUSH    IX                  
0662: D1              POP     DE                  
0663: 3D              DEC     A                   
0664: C2 55 06        JP      NZ,$0655            ; {code.loc_0655}
0667: 3A 8C 63        LD      A,($638C)           ; {hard.workRam+38C} render the freshly seeded value

; Draw a packed two-digit BCD byte into its on-screen field, suppressing a leading zero.
; The low nibble is the units digit and the high nibble the tens; both become tiles and
; go to a shared two-cell stamp that places tens in the high field cell and units one
; column earlier. With the tens digit ZERO the leading digit is suppressed: the high
; cell gets a blank tile instead of a "0", the units digit is shifted into a second tile
; row, a background-music command is latched into sndBgm and a fixed tile is painted
; into two more field cells. It only SHOWS the value -- it does not change the bonus.
renderBonusDisplay:
066A: 4F              LD      C,A                 
066B: E6 0F           AND     $0F                 ; the low nibble is the units digit
066D: 47              LD      B,A                 
066E: 79              LD      A,C                 
066F: 0F              RRCA                        
0670: 0F              RRCA                        
0671: 0F              RRCA                        
0672: 0F              RRCA                        
0673: E6 0F           AND     $0F                 ; the high nibble is the tens digit
0675: C2 89 06        JP      NZ,$0689            ; {code.stampTwoDigitField} tens digit present: stamp both tiles
0678: 3E 03           LD      A,$03               
067A: 32 89 60        LD      ($6089),A           ; {hard.workRam+89} latch the background-music command
067D: 3E 70           LD      A,$70               ; a fixed tile into two more field cells
067F: 32 86 74        LD      ($7486),A           ; {hard.videoRam+86}
0682: 32 A6 74        LD      ($74A6),A           ; {hard.videoRam+A6}
0685: 80              ADD     A,B                 ; shift the units digit into the second tile row
0686: 47              LD      B,A                 
0687: 3E 10           LD      A,$10               ; a blank tile in place of the suppressed leading zero

; Stamp a two-digit number's tile pair into the bonus readout: the high-digit tile into
; one cell and the low-digit tile into the cell one screen column over, the two being 32
; bytes apart on the rotated tilemap. Both arms of the writer funnel through here -- the
; ordinary one and the leading-zero-suppress one, which enters with the high tile forced
; to a blank -- so only the tile values differ; the two writes are the same.
stampTwoDigitField:
0689: 32 E6 74        LD      ($74E6),A           ; {hard.videoRam+E6} the high digit's field cell
068C: 78              LD      A,B                 
068D: 32 C6 74        LD      ($74C6),A           ; {hard.videoRam+C6} the low digit, one screen column earlier
0690: C9              RET                         

; Cash the bonus readout in: pay one score award per digit. bonusDisplay holds two
; digits, one per nibble, and each buys an award off a table of fixed amounts. The
; add-to-score task runs twice -- the LOW digit indexes the table directly, the HIGH
; digit at an offset of ten -- so the tens digit is worth an order of magnitude more than
; the units digit, making this a payout of the readout's face value. Index 0 and index 10
; are the two do-nothing entries, so a digit of 0 costs nothing and pays nothing.
awardRemainingBonusToScore:
0691: 3A 8C 63        LD      A,($638C)           ; {hard.workRam+38C} two digits, one per nibble
0694: 47              LD      B,A                 
0695: E6 0F           AND     $0F                 ; the low digit indexes the award table directly
0697: C5              PUSH    BC                  
0698: CD 1C 05        CALL    $051C               ; {code.addToScoreTask}
069B: C1              POP     BC                  
069C: 78              LD      A,B                 
069D: 0F              RRCA                        ; now the high digit
069E: 0F              RRCA                        
069F: 0F              RRCA                        
06A0: 0F              RRCA                        
06A1: E6 0F           AND     $0F                 
06A3: C6 0A           ADD     A,$0A               ; offset by ten, so it is worth ten times as much
06A5: C3 1C 05        JP      $051C               ; {code.addToScoreTask}

; Take one notch off the bonus readout the player watches count down. bonusDisplay is a
; single byte holding two decimal digits. The current value arrives in the accumulator,
; already known non-zero, and this subtracts one and decimal-adjusts it back into valid
; packed decimal (00 wraps to 99) before storing it and handing the new value to the
; shared two-digit field renderer. When the readout has just reached zero -- it held 01
; -- bonusDisplayZeroed is latched BEFORE the adjust, so a reader can tell "bottomed out"
; from "merely wrapped". It steps the READOUT byte only; the bonus quantity itself is a
; separate cell with its own writers.
stepBonusDisplayDown:
06A8: D6 01           SUB     $01                 ; take one notch off the packed counter
06AA: 20 05           JR      NZ,$06B1            ; {code.loc_06b1}
06AC: 21 B8 63        LD      HL,$63B8            ; it held 01, so the readout has bottomed out
06AF: 36 01           LD      (HL),$01            

loc_06b1:
06B1: 27              DAA                         ; correct the decrement back into packed decimal
06B2: 32 8C 63        LD      ($638C),A           ; {hard.workRam+38C}
06B5: C3 6A 06        JP      $066A               ; {code.renderBonusDisplay} show the new value

; Repaint the top-of-screen HUD: the spare-Mario markers and the level number. A guard
; skips the whole body during attract. It blanks all six marker slots stepping one
; tilemap row UP from the bottom slot, then fills one marker per RESERVE life -- lives
; minus the caller's count of lives in play, which is 1 in practice -- from the bottom
; up, stamps two fixed furniture tiles beside the indicator, and clamps level to 99
; (writing the clamp back only when it exceeds) before splitting it into two decimal
; digits by repeated subtraction of ten. The marker count is 8-bit, so a caller passing
; a count above lives would wrap and paint far past the six slots.
drawLivesAndLevel:
06B8: 4F              LD      C,A                 ; keep the caller's count of lives in play
06B9: CF              RST     $08                 ; skip the whole HUD redraw during attract
06BA: 06 06           LD      B,$06               ; six marker slots
06BC: 11 E0 FF        LD      DE,$FFE0            ; step one tilemap row up per slot
06BF: 21 83 77        LD      HL,$7783            ; the bottom marker slot

loc_06c2:
06C2: 36 10           LD      (HL),$10            ; blank tile
06C4: 19              ADD     HL,DE               
06C5: 10 FB           DJNZ    $06C2               ; {code.loc_06c2}
06C7: 3A 28 62        LD      A,($6228)           ; {hard.workRam+228}
06CA: 91              SUB     C                   ; reserve lives are lives minus those in play
06CB: CA D7 06        JP      Z,$06D7             ; {code.loc_06d7} none in reserve, so draw no markers
06CE: 47              LD      B,A                 
06CF: 21 83 77        LD      HL,$7783            ; back to the bottom slot to fill markers

loc_06d2:
06D2: 36 FF           LD      (HL),$FF            ; one marker tile per reserve life
06D4: 19              ADD     HL,DE               
06D5: 10 FB           DJNZ    $06D2               ; {code.loc_06d2}

loc_06d7:
06D7: 21 03 75        LD      HL,$7503            
06DA: 36 1C           LD      (HL),$1C            ; fixed furniture tile beside the indicator
06DC: 21 E3 74        LD      HL,$74E3            
06DF: 36 34           LD      (HL),$34            ; and a second one
06E1: 3A 29 62        LD      A,($6229)           ; {hard.workRam+229}
06E4: FE 64           CP      $64                 ; the level number is clamped to 99
06E6: 38 05           JR      C,$06ED             ; {code.loc_06ed}
06E8: 3E 63           LD      A,$63               
06EA: 32 29 62        LD      ($6229),A           ; {hard.workRam+229} write the clamp back

loc_06ed:
06ED: 01 0A FF        LD      BC,$FF0A            ; split the level into digits by subtracting ten

loc_06f0:
06F0: 04              INC     B                   
06F1: 91              SUB     C                   
06F2: D2 F0 06        JP      NC,$06F0            ; {code.loc_06f0}
06F5: 81              ADD     A,C                 ; undo the last subtraction to leave the units
06F6: 32 A3 74        LD      ($74A3),A           ; {hard.videoRam+A3} the level's units digit
06F9: 78              LD      A,B                 
06FA: 32 C3 74        LD      ($74C3),A           ; {hard.videoRam+C3} and its tens digit
06FD: C9              RET                         

; The per-frame dispatcher for a credited game: read gameSubstate and vector through a
; 29-entry jump table. The occupied slots run, in table order, the opening Kong-climb
; cutscene, the how-high interlude, board setup, gameplay, the death sequence and the
; board-cleared advance. The death sequence takes the three slots straight after
; gameplay: Mario's death ANIMATION, then the player-1 life-loss handler, then player
; 2's. The life is decremented in those last two, not in the animation, and the
; animation picks between them by advancing gameSubstate one for player 1 and two for
; player 2. Six slots are null and the selector is NOT range-checked, so a null or
; out-of-range value vectors to address zero or off the end. The index is an 8-bit
; double, so 128 or more wraps back to the start of the table rather than reading past
; it.
dispatchInGameSubstate:
06FE: 3A 0A 60        LD      A,($600A)           ; {hard.workRam+A} which step of the credited game this frame runs
0701: EF              RST     $28                 ; vector through the 29-entry table that follows

; ---- $0702-$073B: jump table ----
0702: 86 09 AB 09 D6 09 FE 09 1B 0A 37 0A 63 0A 76 0A
0712: DA 0B 00 00 91 0C 3C 12 7A 19 7C 12 F2 12 44 13
0722: 8F 13 A1 13 AA 13 BB 13 1E 14 86 14 15 16 6B 19
0732: 00 00 00 00 00 00 00 00 00 00

; Service the attract state once per vblank. Two jobs, chosen on the credit count. If a
; credit is present a coin has been accepted: reset gameSubstate and step gameState on
; from attract to credited, which is the move that walks the machine out of attract.
; Otherwise run the current attract sub-state, dispatched from a ten-entry table -- the
; attract-screen draw, the timed-advance gates and, through slot 3, the entire
; demo-gameplay cascade. Over a full attract loop the demo plays a whole game, so all
; eight used slots are reached; the two empty slots are unused indices and are never
; dispatched.
runAttractState:
073C: 21 0A 60        LD      HL,$600A            ; the attract sub-state byte, used by both arms
073F: 3A 01 60        LD      A,($6001)           ; {hard.workRam+1} an accepted coin shows up as a credit
0742: A7              AND     A                   
0743: C2 5C 07        JP      NZ,$075C            ; {code.loc_075c} a credit is waiting: leave attract
0746: 7E              LD      A,(HL)              ; the current attract sub-state
0747: EF              RST     $28                 ; vector through the ten-entry table that follows

; ---- $0748-$075B: jump table ----
0748: 79 07 63 07 3C 12 77 19 7C 12 C3 07 CB 07 4B 08
0758: 00 00 00 00

loc_075c:
075C: 36 00           LD      (HL),$00            ; restart the sub-state sequence for the credit screen
075E: 21 05 60        LD      HL,$6005            
0761: 34              INC     (HL)                ; step the game state on, attract to credited
0762: C9              RET                         

; Reseed the live context for a fresh attract round and rebuild the board. It is gated by
; the two-level sub-state timer: every pass ticks the prescaler and the body runs only on
; the pass where both halves expire together. Then it clears the object-insert request
; and a paired scratch byte, reseeds board 1 (25m girders), level 1 and one life, and
; hands off to the board builder. ONE life is the detail that names it: no DIP setting
; produces a starting life count of one -- they decode to three, four, five and six -- so
; a credited game can never enter a board through here.
restartAttractDemoAt25m:
0763: E7              RST     $20                 ; the body runs only when both halves of the timer expire
0764: AF              XOR     A                   
0765: 32 92 63        LD      ($6392),A           ; {hard.workRam+392} clear the paired scratch byte
0768: 32 A0 63        LD      ($63A0),A           ; {hard.workRam+3A0} clear the object-insert request
076B: 3E 01           LD      A,$01               
076D: 32 27 62        LD      ($6227),A           ; {hard.workRam+227} board 1, the 25m girders
0770: 32 29 62        LD      ($6229),A           ; {hard.workRam+229} level 1
0773: 32 28 62        LD      ($6228),A           ; {hard.workRam+228} one life, which no dip setting can produce
0776: C3 92 0C        JP      $0C92               ; {code.buildBoard} lay out the fresh board

; The first attract sub-state: compose the title screen -- the 1UP / HIGH SCORE / 2UP
; score row and the coins-per-credit readout -- then arm a short wait and step attract
; on. It clears paletteBank0 and paletteBank1 (selecting bank 0), posts the two title
; strings and then the fixed title-screen task batch onto the ring, sets substateTimer
; to 2 and advances gameSubstate by one, blanks the playfield and sprite buffer, draws
; the 1UP label and (only in a two-player game) the 2UP label, and finally stamps the
; coins-per-credit readout from dipCoinsFor1P and dipCoinsFor2P. THE DIGIT WRITER RUNS
; TWICE and the second run is not a copy-paste: the first pass's own tail leaves the
; inputs the second consumes, which stamp the literal "1 2" further down the screen.
; There is no counter -- it is a two-iteration loop written as a call that falls through
; into itself.
composeAttractTitleScreen:
0779: 21 86 7D        LD      HL,$7D86            ; the two-bit palette-bank latch
077C: 36 00           LD      (HL),$00            
077E: 23              INC     HL                  
077F: 36 00           LD      (HL),$00            ; both bits clear selects bank 0
0781: 11 1B 03        LD      DE,$031B            ; draw-string task for the first title string
0784: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0787: 1C              INC     E                   ; and the second title string
0788: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
078B: CD 65 09        CALL    $0965               ; {code.enqueueTaskBatch}
078E: 21 09 60        LD      HL,$6009            
0791: 36 02           LD      (HL),$02            ; wait two frames
0793: 23              INC     HL                  
0794: 34              INC     (HL)                ; then step attract to its next sub-state
0795: CD 74 08        CALL    $0874               ; {code.clearPlayfieldAndSprites}
0798: CD 53 0A        CALL    $0A53               ; {code.draw1UpLabel}
079B: 3A 0F 60        LD      A,($600F)           ; {hard.workRam+F} 2UP is drawn only in a two-player game
079E: FE 01           CP      $01                 
07A0: CC EE 09        CALL    Z,$09EE             ; {code.draw2UpLabel}
07A3: ED 5B 22 60     LD      DE,($6022)          ; {hard.workRam+22} both coinage settings, read as one word
07A7: 21 6C 75        LD      HL,$756C            ; the coins-per-credit readout cell
07AA: CD AD 07        CALL    $07AD               ; {code.writeDigitPairWithCarry} its tail sets up the second pass

; Stamp two digit tiles side by side, two cells apart -- a column is 2 bytes in this
; layout. The left value goes straight in; the right one too, EXCEPT at exactly 10,
; which no single tile can show, so it is split: a 0 into the cell two along and a 1
; into a fixed tens cell elsewhere on screen. Tile codes and digit values coincide here.
; In play this draws the coins-per-credit readout, the left digit the one-player price
; and the right the two-player one. The tail deliberately OVERWRITES the caller's target
; cell and digit pair with a second fixed set, because the caller falls straight back
; into the same code with no loop counter and the second pass runs on exactly the values
; this tail leaves behind.
writeDigitPairWithCarry:
07AD: 73              LD      (HL),E              ; the one-player price digit
07AE: 23              INC     HL                  
07AF: 23              INC     HL                  ; two cells along is one screen column
07B0: 72              LD      (HL),D              ; the two-player price digit
07B1: 7A              LD      A,D                 
07B2: D6 0A           SUB     $0A                 ; a price of exactly ten needs two tiles
07B4: C2 BC 07        JP      NZ,$07BC            ; {code.loc_07bc}
07B7: 77              LD      (HL),A              ; the ones digit of ten
07B8: 3C              INC     A                   
07B9: 32 8E 75        LD      ($758E),A           ; {hard.videoRam+18E} its tens digit, in a fixed cell elsewhere

loc_07bc:
07BC: 11 01 02        LD      DE,$0201            ; hand the second pass its digits, 1 and 2
07BF: 21 8C 76        LD      HL,$768C            ; and its target cell further down the screen
07C2: C9              RET                         

; Blank the screen and move on. It clears the tilemap playfield, the two side columns and
; the sprite shadow buffer, readying the display for whatever the next sub-state draws,
; then adds one to gameSubstate so the next dispatch selects the following step. No
; inputs; both effects land on fixed memory.
clearScreenAndAdvanceSubstate:
07C3: CD 74 08        CALL    $0874               ; {code.clearPlayfieldAndSprites}
07C6: 21 0A 60        LD      HL,$600A            
07C9: 34              INC     (HL)                ; step to the next sub-state of this state
07CA: C9              RET                         

loc_07cb:
07CB: 3A 8A 63        LD      A,($638A)           ; {hard.workRam+38A} frames left in the current animation run
07CE: FE 00           CP      $00                 
07D0: C2 2D 08        JP      NZ,$082D            ; {code.loc_082d} a run is already going, so tick it instead
07D3: 3E 60           LD      A,$60               
07D5: 32 8A 63        LD      ($638A),A           ; {hard.workRam+38A} arm a fresh 96-frame run
07D8: 0E 5F           LD      C,$5F               ; seed the bit pattern this run streams out

loc_07da:
07DA: FE 00           CP      $00                 
07DC: CA 3B 08        JP      Z,$083B             ; {code.loc_083b} the tick that reached zero ends the run
07DF: 21 86 7D        LD      HL,$7D86            ; the first of the two pattern latches
07E2: 36 00           LD      (HL),$00            
07E4: 79              LD      A,C                 
07E5: CB 07           RLC     A                   ; shift the pattern's top bit into carry
07E7: 30 02           JR      NC,$07EB            ; {code.loc_07eb}
07E9: 36 01           LD      (HL),$01            ; the bit was set, so raise the latch

loc_07eb:
07EB: 23              INC     HL                  
07EC: 36 00           LD      (HL),$00            
07EE: CB 07           RLC     A                   ; the next pattern bit drives the second latch
07F0: 30 02           JR      NC,$07F4            ; {code.loc_07f4}
07F2: 36 01           LD      (HL),$01            

loc_07f4:
07F4: 32 8B 63        LD      ($638B),A           ; {hard.workRam+38B} store the pattern rotated on by two bits
07F7: 21 08 3D        LD      HL,$3D08            ; the table of fill spans, count then destination

loc_07fa:
07FA: 3E B0           LD      A,$B0               ; the tile stamped across every span
07FC: 46              LD      B,(HL)              ; this span's cell count
07FD: 23              INC     HL                  
07FE: 5E              LD      E,(HL)              
07FF: 23              INC     HL                  
0800: 56              LD      D,(HL)              ; and where it starts

loc_0801:
0801: 12              LD      (DE),A              
0802: 13              INC     DE                  
0803: 10 FC           DJNZ    $0801               ; {code.loc_0801}
0805: 23              INC     HL                  
0806: 7E              LD      A,(HL)              
0807: FE 00           CP      $00                 
0809: C2 FA 07        JP      NZ,$07FA            ; {code.loc_07fa} a zero count terminates the table
080C: 11 1E 03        LD      DE,$031E            ; queue two follow-up draw tasks
080F: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0812: 13              INC     DE                  
0813: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0816: 21 CF 39        LD      HL,$39CF            ; the sprite-object template for this screen
0819: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock}
081C: CD 24 3F        CALL    $3F24               ; {code.stampFixedTilePair}
081F: 00              NOP                         
0820: 21 08 69        LD      HL,$6908            ; the sprite-object block's X column
0823: 0E 44           LD      C,$44               
0825: FF              RST     $38                 
0826: 21 0B 69        LD      HL,$690B            ; and its Y column
0829: 0E 78           LD      C,$78               
082B: FF              RST     $38                 
082C: C9              RET                         

loc_082d:
082D: 3A 8B 63        LD      A,($638B)           ; {hard.workRam+38B} carry on with the pattern this run is streaming
0830: 4F              LD      C,A                 
0831: 3A 8A 63        LD      A,($638A)           ; {hard.workRam+38A}
0834: 3D              DEC     A                   ; take one frame off the countdown
0835: 32 8A 63        LD      ($638A),A           ; {hard.workRam+38A}
0838: C3 DA 07        JP      $07DA               ; {code.loc_07da}

loc_083b:
083B: 21 09 60        LD      HL,$6009            
083E: 36 02           LD      (HL),$02            ; wait two frames
0840: 23              INC     HL                  
0841: 34              INC     (HL)                ; then move to the next sub-state
0842: 21 8A 63        LD      HL,$638A            
0845: 36 00           LD      (HL),$00            ; the run is over: clear its timer
0847: 23              INC     HL                  
0848: 36 00           LD      (HL),$00            ; and its pattern byte
084A: C9              RET                         

; Park on a timed attract sub-state, then release it. Each frame it runs the two-level
; sub-state countdown -- substateTimerLo ticks, and on that byte's underflow
; substateTimer above it. While either half is still counting the routine does nothing
; more, so the sub-state stays parked. Only when both expire on the same frame does it
; clear gameSubstate to 0, so the state's sub-sequence restarts from index 0 on the next
; dispatch.
clearSubstateWhenTimerExpires:
084B: E7              RST     $20                 ; nothing more happens until both halves expire
084C: 21 0A 60        LD      HL,$600A            
084F: 36 00           LD      (HL),$00            ; both expired: restart the sub-sequence at 0
0851: C9              RET                         

; A blunt full-screen wipe for a mode or phase transition. Writes the blank tile 0x10
; across ALL 1024 cells of the tilemap as one uninterrupted sweep -- unlike the narrower
; wipe used elsewhere, which fills only the playfield and side columns -- then zeroes
; the 384-byte spriteBuffer, the DMA source blitted to sprite RAM each vblank.
; Straight-line and constant: every operand is an immediate, so it reads no register and
; no RAM.
clearTilemapAndSprites:
0852: 21 00 74        LD      HL,$7400            ; the first tilemap cell
0855: 0E 04           LD      C,$04               ; four passes of 256 cover all 1024 cells

loc_0857:
0857: 06 00           LD      B,$00               
0859: 3E 10           LD      A,$10               ; the blank tile

loc_085b:
085B: 77              LD      (HL),A              
085C: 23              INC     HL                  
085D: 10 FC           DJNZ    $085B               ; {code.loc_085b}
085F: 0D              DEC     C                   
0860: C2 57 08        JP      NZ,$0857            ; {code.loc_0857}
0863: 21 00 69        LD      HL,$6900            ; the sprite shadow buffer
0866: 0E 02           LD      C,$02               ; two passes of 192 clear its 384 bytes

loc_0868:
0868: 06 C0           LD      B,$C0               
086A: AF              XOR     A                   ; zeroing it takes every sprite off the screen

loc_086b:
086B: 77              LD      (HL),A              
086C: 23              INC     HL                  
086D: 10 FC           DJNZ    $086B               ; {code.loc_086b}
086F: 0D              DEC     C                   
0870: C2 68 08        JP      NZ,$0868            ; {code.loc_0868}
0873: C9              RET                         

; Blank the screen for a board build or for power-on. Writes the blank tile across the
; central 28 columns of all 32 tilemap rows (896 cells, each row advancing 28 written
; and 4 skipped), then down two 14-cell vertical runs beside the playfield, then zeroes
; all 384 bytes of spriteBuffer -- which takes every sprite off the screen, that block
; being what the DMA feeds the sprite hardware each vblank. Every value written is a
; constant.
clearPlayfieldAndSprites:
0874: 21 04 74        LD      HL,$7404            ; the first playfield cell
0877: 0E 20           LD      C,$20               ; all 32 tilemap rows

loc_0879:
0879: 06 1C           LD      B,$1C               ; the playfield is the central 28 columns
087B: 3E 10           LD      A,$10               ; the blank tile
087D: 11 04 00        LD      DE,$0004            ; skip the four off-playfield cells at the row's end

loc_0880:
0880: 77              LD      (HL),A              
0881: 23              INC     HL                  
0882: 10 FC           DJNZ    $0880               ; {code.loc_0880}
0884: 19              ADD     HL,DE               
0885: 0D              DEC     C                   
0886: C2 79 08        JP      NZ,$0879            ; {code.loc_0879}
0889: 21 22 75        LD      HL,$7522            ; the first side column
088C: 11 20 00        LD      DE,$0020            ; one whole tilemap row per cell
088F: 0E 02           LD      C,$02               ; two side columns
0891: 3E 10           LD      A,$10               

loc_0893:
0893: 06 0E           LD      B,$0E               ; fourteen cells each

loc_0895:
0895: 77              LD      (HL),A              
0896: 19              ADD     HL,DE               
0897: 10 FC           DJNZ    $0895               ; {code.loc_0895}
0899: 21 23 75        LD      HL,$7523            ; the second side column
089C: 0D              DEC     C                   
089D: C2 93 08        JP      NZ,$0893            ; {code.loc_0893}
08A0: 21 00 69        LD      HL,$6900            ; the sprite shadow buffer
08A3: 06 00           LD      B,$00               
08A5: 3E 00           LD      A,$00               

loc_08a7:
08A7: 77              LD      (HL),A              
08A8: 23              INC     HL                  
08A9: 10 FC           DJNZ    $08A7               ; {code.loc_08a7}
08AB: 06 80           LD      B,$80               ; 128 more bytes makes the full 384

loc_08ad:
08AD: 77              LD      (HL),A              
08AE: 23              INC     HL                  
08AF: 10 FC           DJNZ    $08AD               ; {code.loc_08ad}
08B1: C9              RET                         

; Run the right step of the credited game, once a frame. "Credited" is the short stretch
; after a coin has been accepted and before play begins, and it is a two-step machine.
; Step 0 sets the credited game up: clear the playfield, mark that the credit has been
; taken, queue the intro, move on to step 1. Step 1 waits for the start button; when it
; comes it records whether the game is one player or two and hands over to play. The
; selector is not range-checked and the table has only those two slots, so a byte outside
; 0..1 would vector into whatever data follows -- but nothing ever writes anything else
; there.
dispatchCreditedSubstate:
08B2: 3A 0A 60        LD      A,($600A)           ; {hard.workRam+A} credited step 0 sets up, step 1 waits for start
08B5: EF              RST     $28                 ; vector through the two-entry table that follows

; ---- $08B6-$08B9: jump table ----
08B6: BA 08 F8 08

; The first credited frame: accept the coin and compose the credit / "PUSH START" screen,
; once. It blanks the playfield tilemap and zeroes the sprite shadow buffer; clears
; attract, the byte that marks a credit accepted, so this is the frame the machine leaves
; attract mode; posts the credit-screen text task onto the task ring; steps gameSubstate
; 0 to 1, so from the next frame the wait-for-start handler runs instead of this setup;
; posts the rest of the screen's text tasks; and selects palette bank 0 by zeroing both
; bits of the two-bit palette-bank latch. It then falls through into the start-button
; read.
enterCreditScreen:
08BA: CD 74 08        CALL    $0874               ; {code.clearPlayfieldAndSprites}
08BD: AF              XOR     A                   
08BE: 32 07 60        LD      ($6007),A           ; {hard.workRam+7} clearing this is what leaves attract mode
08C1: 11 0C 03        LD      DE,$030C            ; the credit-screen text task
08C4: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
08C7: 21 0A 60        LD      HL,$600A            
08CA: 34              INC     (HL)                ; step to the wait-for-start sub-state
08CB: CD 65 09        CALL    $0965               ; {code.enqueueTaskBatch} the rest of the screen's text
08CE: AF              XOR     A                   
08CF: 21 86 7D        LD      HL,$7D86            
08D2: 77              LD      (HL),A              
08D3: 2C              INC     L                   
08D4: 77              LD      (HL),A              ; both palette-bank bits clear: bank 0

; Runs every frame while a game is CREDITED -- coins in, nobody started yet. It builds a
; start-button mask and a prompt-string index from credits: exactly one credit gives
; mask 0x04 (START1 only) and prompt string 9, any other count gives 0x0C
; (START1|START2) and string 10, so a lone credit only honours the 1-player start. Once
; every 8 frames ((frame & 7) == 0) it redraws the prompt string and then the CREDIT
; line. It returns in2's start bits masked to the allowed set; the credit-screen state
; machine starts a 1-player game on 0x04 and a 2-player game on 0x08 and otherwise keeps
; waiting. A quirk: on the draw frames the two draws clobber the mask register before it
; is used, so the byte returned then is the port masked with whatever the draws left.
; Harmless, because only a clean 0x04 / 0x08 is acted on and those land on the seven
; skip frames in eight.
readStartButtonSelector:
08D5: 06 04           LD      B,$04               ; one credit honours the 1-player start only
08D7: 1E 09           LD      E,$09               ; and shows the 1-player prompt
08D9: 3A 01 60        LD      A,($6001)           ; {hard.workRam+1}
08DC: FE 01           CP      $01                 ; exactly one credit?
08DE: CA E4 08        JP      Z,$08E4             ; {code.loc_08e4}
08E1: 06 0C           LD      B,$0C               ; otherwise both start buttons are live
08E3: 1C              INC     E                   ; and the two-player prompt

loc_08e4:
08E4: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A}
08E7: E6 07           AND     $07                 ; redraw only one frame in eight
08E9: C2 F3 08        JP      NZ,$08F3            ; {code.loc_08f3}
08EC: 7B              LD      A,E                 
08ED: CD E9 05        CALL    $05E9               ; {code.drawStringVertical} put up the start prompt
08F0: CD 16 06        CALL    $0616               ; {code.drawCreditDisplay}

loc_08f3:
08F3: 3A 00 7D        LD      A,($7D00)           ; {hard.in2} read the start buttons
08F6: A0              AND     B                   ; keep only the buttons this credit count allows
08F7: C9              RET                         

; Commit a credited game start. Dispatched every frame while gameState is 2 and
; gameSubstate is 1, it reads which start button is down. 0x04, one player: spend one
; credit and CLEAR p2Context, since there is no player 2 this game. 0x08, two players:
; spend two credits, seed p2Context (byte 0 the starting lives from dipLives, bytes 1-7
; a fixed template) and post the "bring player 2 in" task. Neither button, or both held
; at once, does nothing at all -- which is why this re-runs every frame from the credit
; until exactly one is seen. The shared tail then records the 1P/2P flag, wipes the
; playfield and sprites, seeds p1Context the same way, posts player 1's task, and ends
; the sub-state machine with gameSubstate = 0 and gameState = 3, the advance into
; gameplay. activePlayerIndex and twoPlayerGame are adjacent bytes written as one 16-bit
; store.
commitGameStart:
08F8: CD D5 08        CALL    $08D5               ; {code.readStartButtonSelector}
08FB: FE 04           CP      $04                 ; the 1-player button
08FD: CA 06 09        JP      Z,$0906             ; {code.loc_0906}
0900: FE 08           CP      $08                 ; the 2-player button
0902: CA 19 09        JP      Z,$0919             ; {code.loc_0919}
0905: C9              RET                         ; neither, or both at once: keep waiting

loc_0906:
0906: CD 77 09        CALL    $0977               ; {code.spendCredit} one credit for the one player
0909: 21 48 60        LD      HL,$6048            ; no player 2, so clear its saved context
090C: 06 08           LD      B,$08               
090E: AF              XOR     A                   

loc_090f:
090F: 77              LD      (HL),A              
0910: 2C              INC     L                   
0911: 10 FC           DJNZ    $090F               ; {code.loc_090f}
0913: 21 00 00        LD      HL,$0000            ; player 1 up, one-player game
0916: C3 38 09        JP      $0938               ; {code.loc_0938}

loc_0919:
0919: CD 77 09        CALL    $0977               ; {code.spendCredit} two players cost two credits
091C: CD 77 09        CALL    $0977               ; {code.spendCredit}
091F: 11 48 60        LD      DE,$6048            ; seed player 2's saved context
0922: 3A 20 60        LD      A,($6020)           ; {hard.workRam+20} byte 0 is the starting life count
0925: 12              LD      (DE),A              
0926: 1C              INC     E                   
0927: 21 5E 09        LD      HL,$095E            ; bytes 1-7 are a fixed template
092A: 01 07 00        LD      BC,$0007            
092D: ED B0           LDIR                        
092F: 11 01 01        LD      DE,$0101            ; post the bring-player-2-in task
0932: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0935: 21 00 01        LD      HL,$0100            ; player 1 up, two-player game

loc_0938:
0938: 22 0E 60        LD      ($600E),HL          ; {hard.workRam+E} active player and 1P/2P flag, one store
093B: CD 74 08        CALL    $0874               ; {code.clearPlayfieldAndSprites}
093E: 11 40 60        LD      DE,$6040            ; seed player 1's context the same way
0941: 3A 20 60        LD      A,($6020)           ; {hard.workRam+20}
0944: 12              LD      (DE),A              
0945: 1C              INC     E                   
0946: 21 5E 09        LD      HL,$095E            
0949: 01 07 00        LD      BC,$0007            
094C: ED B0           LDIR                        
094E: 11 00 01        LD      DE,$0100            ; post the bring-player-1-in task
0951: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0954: AF              XOR     A                   
0955: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} the credited sub-state machine is done
0958: 3E 03           LD      A,$03               
095A: 32 05 60        LD      ($6005),A           ; {hard.workRam+5} state 3 is gameplay
095D: C9              RET                         

; ---- $095E-$0964: data ----
095E: 01 65 3A 01 00 00 00

; Post a fixed batch of seven messages onto the task ring: one [0x04, 0x00], then six
; [0x03, 0x14] through [0x03, 0x19]. The dispatcher masks the opcode to its low five bits
; to index its handler table, so this posts handler 4 once and handler 3 -- the
; screen-text draw -- six times with successive string ids. What handler 4 does, and
; which strings those ids name, is not established here. A one-shot screen-composition
; helper; it does nothing else.
enqueueTaskBatch:
0965: 11 00 04        LD      DE,$0400            ; one message for handler 4
0968: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
096B: 11 14 03        LD      DE,$0314            ; then handler 3 with the first string id
096E: 06 06           LD      B,$06               ; six string ids in a row

loc_0970:
0970: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0973: 1C              INC     E                   ; step to the next string id
0974: 10 FA           DJNZ    $0970               ; {code.loc_0970}
0976: C9              RET                         

; Spend one credit as a game starts -- called once per player being brought in, so a
; two-player start spends two. credits is BCD-decremented by the ten's-complement idiom
; (add the BCD of minus one, then apply the decimal-adjust correction), wrapping 0x00
; back to 0x99, and the deferred "credit changed" task is enqueued -- the same task the
; coin handler posts on an award -- for the main loop to drain and redraw the count.
spendCredit:
0977: 21 01 60        LD      HL,$6001            ; the credit count
097A: 3E 99           LD      A,$99               ; adding this is adding BCD minus one
097C: 86              ADD     A,(HL)              
097D: 27              DAA                         ; decimal-adjust it, so 00 wraps to 99
097E: 77              LD      (HL),A              
097F: 11 00 04        LD      DE,$0400            ; post the credit-changed redraw task
0982: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0985: C9              RET                         

; The first in-game frame's start-up step, run right after a coin and start commit hand
; control to the in-game state. It blanks every tilemap cell and the sprite shadow
; buffer, zeroes every sound output and its shadow, then turns flipScreen ON
; unconditionally and picks what runs next from activePlayerIndex: zero, a 1-player
; start, selects gameSubstate 1 with flip left on; non-zero, a 2-player start, selects
; gameSubstate 3, and there the cabinet decides -- an upright keeps flip on, a cocktail
; clears it so player 2 sees the mirrored screen.
configureFlipScreenAndSelectSubstate:
0986: CD 52 08        CALL    $0852               ; {code.clearTilemapAndSprites}
0989: CD 1C 01        CALL    $011C               ; {code.silenceSound}
098C: 11 82 7D        LD      DE,$7D82            ; the flip-screen latch
098F: 3E 01           LD      A,$01               
0991: 12              LD      (DE),A              ; flip is on by default
0992: 21 0A 60        LD      HL,$600A            
0995: 3A 0E 60        LD      A,($600E)           ; {hard.workRam+E} zero for a one-player start
0998: A7              AND     A                   
0999: C2 9F 09        JP      NZ,$099F            ; {code.loc_099f}
099C: 36 01           LD      (HL),$01            ; one player: sub-state 1, flip left on
099E: C9              RET                         

loc_099f:
099F: 3A 26 60        LD      A,($6026)           ; {hard.workRam+26} an upright cabinet keeps the flip
09A2: 3D              DEC     A                   
09A3: CA A8 09        JP      Z,$09A8             ; {code.loc_09a8}
09A6: AF              XOR     A                   
09A7: 12              LD      (DE),A              ; cocktail: clear it so player 2 sees it mirrored

loc_09a8:
09A8: 36 03           LD      (HL),$03            ; two players: sub-state 3
09AA: C9              RET                         

; Run at the start of player 1's turn. Copy p1Context over the live 8-byte context whose
; first cell is lives, then re-derive board by following the just-restored boardSeqPtr
; and copying the byte it points at (1 = 25m, 2 = 50m, 3 = 75m, 4 = 100m). The order is
; load-bearing: the copy spans the pointer itself, so the deref must read the fresh one.
; Then arm the next sub-state from twoPlayerGame -- a two-player game gets the
; player-alternation screen on a 120-frame hold, a one-player game a 1-frame hold.
restorePlayer1Context:
09AB: 21 40 60        LD      HL,$6040            ; player 1's saved context
09AE: 11 28 62        LD      DE,$6228            ; the live context block, lives first
09B1: 01 08 00        LD      BC,$0008            ; eight bytes: lives, level, sequence pointer, progress
09B4: ED B0           LDIR                        
09B6: 2A 2A 62        LD      HL,($622A)          ; {hard.workRam+22A} the pointer just restored, not the old one
09B9: 7E              LD      A,(HL)              ; the board it names: 1 = 25m through 4 = 100m
09BA: 32 27 62        LD      ($6227),A           ; {hard.workRam+227}
09BD: 3A 0F 60        LD      A,($600F)           ; {hard.workRam+F}
09C0: A7              AND     A                   
09C1: 21 09 60        LD      HL,$6009            
09C4: 11 0A 60        LD      DE,$600A            
09C7: CA D0 09        JP      Z,$09D0             ; {code.loc_09d0}
09CA: 36 78           LD      (HL),$78            ; two players: hold 120 frames
09CC: EB              EX      DE,HL               
09CD: 36 02           LD      (HL),$02            ; on the player-alternation screen
09CF: C9              RET                         

loc_09d0:
09D0: 36 01           LD      (HL),$01            ; one player: proceed on the next frame
09D2: EB              EX      DE,HL               
09D3: 36 05           LD      (HL),$05            ; straight to sub-state 5
09D5: C9              RET                         

; The two-player arm of the board-setup step, and it dispatches exactly once, at the
; start of a two-player game -- the one-player path advances straight past it.
; Straight-line, with no branch of its own: clear the two board control latches, post
; draw tasks [3, 2] and [2, 1] onto the task ring, advance gameSubstate from 2 to 5, then
; fall through into the shared 3-cell column painter, which writes three tilemap cells
; one row apart.
armTwoPlayerBoardSetup:
09D6: AF              XOR     A                   
09D7: 32 86 7D        LD      ($7D86),A           ; {hard.paletteBank0}
09DA: 32 87 7D        LD      ($7D87),A           ; {hard.paletteBank1} clearing both bits selects palette bank 0
09DD: 11 02 03        LD      DE,$0302            ; post this step's two draw tasks
09E0: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
09E3: 11 01 02        LD      DE,$0201            
09E6: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
09E9: 3E 05           LD      A,$05               
09EB: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} advance the board setup, 2 to 5

; Stamp the three fixed video-RAM cells of player 2's "2UP" score marker: the player
; digit, then two fixed glyph tiles the font decodes as U and P, one tilemap row apart up
; the screen. Straight-line, input-independent, force-written unconditionally. It is
; drawn only when a second player exists -- attract setup calls it behind a two-player
; guard, and it is the unconditional tail of the player-alternation setup. The same three
; cells are afterwards maintained and blinked every sixteenth frame by the marker
; refresh.
draw2UpLabel:
09EE: 3E 02           LD      A,$02               
09F0: 32 E0 74        LD      ($74E0),A           ; {hard.videoRam+E0} the player digit of the 2UP marker
09F3: 3E 25           LD      A,$25               
09F5: 32 C0 74        LD      ($74C0),A           ; {hard.videoRam+C0} 'U', one tilemap row up
09F8: 3E 20           LD      A,$20               
09FA: 32 A0 74        LD      ($74A0),A           ; {hard.videoRam+A0} 'P', one row further up
09FD: C9              RET                         

; Hand the turn to player 2. Copies p2Context over the live 8-byte context block based
; at lives, then re-derives board from the byte the just-restored boardSeqPtr points at
; -- which is what makes the board follow player 2's own progress rather than whatever
; the other player left behind. Finally it arms the turn with the "wait N frames, then
; run sub-state M" idiom: substateTimer = 120 frames, gameSubstate = 4. Branchless, with
; every write unconditional, so no saved context can steer it.
restorePlayer2Context:
09FE: 21 48 60        LD      HL,$6048            ; player 2's saved context
0A01: 11 28 62        LD      DE,$6228            ; the live context block, lives first
0A04: 01 08 00        LD      BC,$0008            
0A07: ED B0           LDIR                        
0A09: 2A 2A 62        LD      HL,($622A)          ; {hard.workRam+22A} player 2's own place in the board order
0A0C: 7E              LD      A,(HL)              
0A0D: 32 27 62        LD      ($6227),A           ; {hard.workRam+227} cache the board it names
0A10: 3E 78           LD      A,$78               
0A12: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} hold 120 frames before player 2's turn
0A15: 3E 04           LD      A,$04               
0A17: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} then sub-state 4
0A1A: C9              RET                         

loc_0a1b:
0A1B: AF              XOR     A                   
0A1C: 32 86 7D        LD      ($7D86),A           ; {hard.paletteBank0}
0A1F: 32 87 7D        LD      ($7D87),A           ; {hard.paletteBank1} clearing both bits selects palette bank 0
0A22: 11 03 03        LD      DE,$0303            ; post this step's two draw tasks
0A25: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0A28: 11 01 02        LD      DE,$0201            
0A2B: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0A2E: CD EE 09        CALL    $09EE               ; {code.draw2UpLabel}
0A31: 3E 05           LD      A,$05               
0A33: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} chain the setup cascade on to sub-state 5
0A36: C9              RET                         

; One step of the pre-gameplay screen build that runs before each board. It posts a
; fixed four-message batch of (opcode, argument) pairs onto the task ring, which the
; main loop drains and dispatches as deferred draw work; advances gameSubstate by one so
; the next frame selects the following step; and stamps player 1's static "1UP" score
; marker into three tilemap cells. It takes no input at all.
composeScreenAndAdvanceSubstate:
0A37: 11 04 03        LD      DE,$0304            ; post the four fixed screen-build tasks
0A3A: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0A3D: 11 02 02        LD      DE,$0202            
0A40: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0A43: 11 00 02        LD      DE,$0200            
0A46: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0A49: 11 00 06        LD      DE,$0600            
0A4C: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0A4F: 21 0A 60        LD      HL,$600A            
0A52: 34              INC     (HL)                ; step to the next sub-state

; Stamp the three video-RAM cells of player 1's "1UP" score marker -- the player digit,
; then 'U', then 'P', climbing one tilemap row per cell. This is the one-shot static
; draw, done while the top-of-screen furniture is built; a separate per-frame routine
; blinks the same three cells afterwards. It force-writes all three whatever they held,
; and every value is an immediate. The digit tile is corroborated by that blink routine,
; which writes the player number plus one into the same cell; the two letter codes are
; the conventional font reading.
draw1UpLabel:
0A53: 3E 01           LD      A,$01               
0A55: 32 40 77        LD      ($7740),A           ; {hard.videoRam+340} the player digit of the 1UP marker
0A58: 3E 25           LD      A,$25               
0A5A: 32 20 77        LD      ($7720),A           ; {hard.videoRam+320} 'U', one tilemap row up
0A5D: 3E 20           LD      A,$20               
0A5F: 32 00 77        LD      ($7700),A           ; {hard.videoRam+300} 'P', one row further up
0A62: C9              RET                         

; The board-start step that wipes the previous scene and decides whether the opening
; cutscene plays. Dispatched once a frame on gameSubstate, it opens with the shared
; sub-state timer tick and is skipped entirely until that timer reaches 0. Then it blanks
; the tilemap playfield, the two side columns and the 384-byte sprite shadow buffer;
; reloads substateTimer to 1 so the sub-state selected next proceeds on the very next
; frame; and steps gameSubstate forward -- by 1 into the opening Kong-climb cutscene, or
; by 2 straight past it to the "how high can you get?" interlude when playIntro is clear,
; which is why a board replayed after a death skips the intro (both death handlers zero
; that flag).
clearScreenAndSelectIntro:
0A63: DF              RST     $18                 ; nothing happens until the sub-state timer expires
0A64: CD 74 08        CALL    $0874               ; {code.clearPlayfieldAndSprites}
0A67: 21 09 60        LD      HL,$6009            
0A6A: 36 01           LD      (HL),$01            ; re-arm for one frame so the next step runs at once
0A6C: 2C              INC     L                   
0A6D: 34              INC     (HL)                ; advance to the opening cutscene
0A6E: 11 2C 62        LD      DE,$622C            ; the play-intro flag
0A71: 1A              LD      A,(DE)              
0A72: A7              AND     A                   
0A73: C0              RET     NZ                  ; the intro is wanted, so stop here
0A74: 34              INC     (HL)                ; intro suppressed after a death: skip to the how-high screen
0A75: C9              RET                         

; The per-frame dispatcher for the opening Kong-climb cutscene, the short animated intro
; at the head of a board. It reads introStep and vectors through the 8-entry inline
; table: 0 seeds the cutscene's walk pointers; 1 and 2 advance Kong's climb; 3 and 5 are
; the shared gated tick, a metered pause that bumps the step once substateTimer expires;
; 4 and 6 are further beats; 7 is the final beat, which fires the roar. introStep walks
; 0 to 7 across the cutscene, each arm normally advancing it for the next frame.
; Doubling the index into a table offset is 8-BIT, so a selector of 0x80 wraps the
; offset back to the table's start.
dispatchIntroCutsceneStep:
0A76: 3A 85 63        LD      A,($6385)           ; {hard.workRam+385} which beat of the cutscene this frame runs
0A79: EF              RST     $28                 ; vector through the eight-entry table that follows

; ---- $0A7A-$0A89: jump table ----
0A7A: 8A 0A BF 0A E8 0A 69 30 06 0B 69 30 68 0B B3 0B

; Step 0 of the opening Kong-climb cutscene -- the one-time setup, run while
; gameSubstate is the cutscene value and introStep is still 0. Selects palette bank 1,
; draws the cutscene's static playfield by walking the terminated girder-and-ladder
; segment table into video RAM, stamps three fixed tiles, clears the cutscene
; bookkeeping byte, seeds introWalkPtrA and introWalkPtrB for the later steps, arms
; substateTimer to a 64-frame countdown the following step gates on, and steps introStep
; to 1 so the next dispatch runs that phase instead of re-running this setup.
; Straight-line, with no work-RAM inputs.
setupIntroCutsceneStep:
0A8A: AF              XOR     A                   
0A8B: 32 86 7D        LD      ($7D86),A           ; {hard.paletteBank0}
0A8E: 3C              INC     A                   
0A8F: 32 87 7D        LD      ($7D87),A           ; {hard.paletteBank1} palette bank 1 for the cutscene
0A92: 11 0D 38        LD      DE,$380D            ; the cutscene's girder-and-ladder segment table
0A95: CD A7 0D        CALL    $0DA7               ; {code.drawBoardLayout}
0A98: 3E 10           LD      A,$10               ; the blank tile, into two cells of the drawn layout
0A9A: 32 A3 76        LD      ($76A3),A           ; {hard.videoRam+2A3}
0A9D: 32 63 76        LD      ($7663),A           ; {hard.videoRam+263}
0AA0: 3E D4           LD      A,$D4               ; one more fixed tile for the cutscene screen
0AA2: 32 AA 75        LD      ($75AA),A           ; {hard.videoRam+1AA}
0AA5: AF              XOR     A                   
0AA6: 32 AF 62        LD      ($62AF),A           ; {hard.workRam+2AF} clear the cutscene's tick counter
0AA9: 21 B4 38        LD      HL,$38B4            
0AAC: 22 C2 63        LD      ($63C2),HL          ; {hard.workRam+3C2} seed the first walk pointer
0AAF: 21 CB 38        LD      HL,$38CB            
0AB2: 22 C4 63        LD      ($63C4),HL          ; {hard.workRam+3C4} and the second
0AB5: 3E 40           LD      A,$40               
0AB7: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} arm the 64-frame gate the next beat waits on
0ABA: 21 85 63        LD      HL,$6385            
0ABD: 34              INC     (HL)                ; step the cutscene to beat 1
0ABE: C9              RET                         

; One phase of the opening Kong-climb cutscene that plays at the head of every board. A
; one-shot timer gate -- an earlier phase armed the cutscene countdown, and every frame
; this ticks it and does nothing else until it expires. On the single expiry frame it
; copies this phase's 40-byte sprite-object template over spriteObjBlock, nudges all ten
; records into scene position with two strided add passes, seeds introScrollIndex and
; record 1's first field (which must come after both add passes, since it overwrites what
; they wrote), queues the intro tune as a three-frame priority pulse, and steps the
; cutscene on.
runIntroClimbStep:
0ABF: DF              RST     $18                 ; do nothing until that 64-frame gate expires
0AC0: 21 8C 38        LD      HL,$388C            ; the ten-record sprite template for this beat
0AC3: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock}
0AC6: 21 08 69        LD      HL,$6908            
0AC9: 0E 30           LD      C,$30               ; nudge every record's X into scene position
0ACB: FF              RST     $38                 
0ACC: 21 0B 69        LD      HL,$690B            
0ACF: 0E 99           LD      C,$99               ; and every record's Y
0AD1: FF              RST     $38                 
0AD2: 3E 1F           LD      A,$1F               
0AD4: 32 8E 63        LD      ($638E),A           ; {hard.workRam+38E} seed the climb's scroll index
0AD7: AF              XOR     A                   
0AD8: 32 0C 69        LD      ($690C),A           ; {hard.workRam+90C} overwrite what the X pass left in record 1
0ADB: 21 8A 60        LD      HL,$608A            
0ADE: 36 01           LD      (HL),$01            ; queue the intro tune
0AE0: 23              INC     HL                  
0AE1: 36 03           LD      (HL),$03            ; held for three frames
0AE3: 21 85 63        LD      HL,$6385            
0AE6: 34              INC     (HL)                ; step the cutscene on
0AE7: C9              RET                         

; Step 2 of the opening Kong-climb cutscene: run the climb, one frame at a time. Every
; frame it advances the ten-record sprite-object block one animation frame -- which
; scrolls the climbing figures up 4px on every eighth call -- and bumps the cutscene's
; own tick counter; on every sixteenth tick it also slides the climb-graphic strip up one
; tilemap row. It then reads record 0's Y, which walks upward as the sprite scrolls, and
; returns while it is still at or above the top-out row. On the frame that Y passes the
; row the climb is finished: arm substateTimer to 32 frames, step introStep from 2 to 3,
; and point seqAdvancePtr at introStep so the shared gated tick advances it again once
; that timer expires.
animateIntroClimbStep:
0AE8: CD 6F 30        CALL    $306F               ; {code.animateSpriteObjectBlock}
0AEB: 3A AF 62        LD      A,($62AF)           ; {hard.workRam+2AF} the cutscene's own tick counter
0AEE: E6 0F           AND     $0F                 ; every sixteenth tick
0AF0: CC 4A 30        CALL    Z,$304A             ; {code.scrollClimbGraphicStep} slide the climb strip up a row
0AF3: 3A 0B 69        LD      A,($690B)           ; {hard.workRam+90B} the climbing figure's Y, which walks upward
0AF6: FE 5D           CP      $5D                 ; has it passed the top-out row?
0AF8: D0              RET     NC                  ; not yet, so climb again next frame
0AF9: 3E 20           LD      A,$20               
0AFB: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} topped out: arm a 32-frame pause
0AFE: 21 85 63        LD      HL,$6385            
0B01: 34              INC     (HL)                ; step the cutscene on
0B02: 22 C0 63        LD      ($63C0),HL          ; {hard.workRam+3C0} let the shared gated tick advance it next
0B05: C9              RET                         

loc_0b06:
0B06: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A}
0B09: 0F              RRCA                        
0B0A: D8              RET     C                   ; odd frames idle, so the walk runs at half rate
0B0B: 2A C2 63        LD      HL,($63C2)          ; {hard.workRam+3C2} the walk cursor into the delta table
0B0E: 7E              LD      A,(HL)              
0B0F: FE 7F           CP      $7F                 ; the sentinel that ends the walk
0B11: CA 1E 0B        JP      Z,$0B1E             ; {code.loc_0b1e}
0B14: 23              INC     HL                  
0B15: 22 C2 63        LD      ($63C2),HL          ; {hard.workRam+3C2} advance the cursor one byte
0B18: 4F              LD      C,A                 ; the signed Y delta
0B19: 21 0B 69        LD      HL,$690B            ; add it into every record's Y
0B1C: FF              RST     $38                 
0B1D: C9              RET                         

loc_0b1e:
0B1E: 21 5C 38        LD      HL,$385C            ; walk done: load the next sprite template
0B21: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock}
0B24: 11 00 69        LD      DE,$6900            ; copy eight more bytes into the sprite buffer's head
0B27: 01 08 00        LD      BC,$0008            
0B2A: ED B0           LDIR                        
0B2C: 21 08 69        LD      HL,$6908            
0B2F: 0E 50           LD      C,$50               ; shift the fresh row along X
0B31: FF              RST     $38                 
0B32: 21 0B 69        LD      HL,$690B            
0B35: 0E FC           LD      C,$FC               ; and up four on Y
0B37: FF              RST     $38                 

loc_0b38:
0B38: CD 4A 30        CALL    $304A               ; {code.scrollClimbGraphicStep}
0B3B: 3A 8E 63        LD      A,($638E)           ; {hard.workRam+38E}
0B3E: FE 0A           CP      $0A                 ; scroll the climb strip until the index reaches ten
0B40: C2 38 0B        JP      NZ,$0B38            ; {code.loc_0b38}
0B43: 3E 03           LD      A,$03               
0B45: 32 82 60        LD      ($6082),A           ; {hard.workRam+82} assert this beat's sound for three frames
0B48: 11 2C 39        LD      DE,$392C            ; draw the next layout segment table
0B4B: CD A7 0D        CALL    $0DA7               ; {code.drawBoardLayout}
0B4E: 3E 10           LD      A,$10               ; the blank tile, into two cells of the drawn layout
0B50: 32 AA 74        LD      ($74AA),A           ; {hard.videoRam+AA}
0B53: 32 8A 74        LD      ($748A),A           ; {hard.videoRam+8A}
0B56: 3E 05           LD      A,$05               
0B58: 32 8D 63        LD      ($638D),A           ; {hard.workRam+38D} five bands still to stamp
0B5B: 3E 20           LD      A,$20               
0B5D: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} arm the 32-frame pause
0B60: 21 85 63        LD      HL,$6385            
0B63: 34              INC     (HL)                ; step the cutscene on
0B64: 22 C0 63        LD      ($63C0),HL          ; {hard.workRam+3C0} let the gated tick advance it
0B67: C9              RET                         

loc_0b68:
0B68: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A}
0B6B: 0F              RRCA                        
0B6C: D8              RET     C                   ; odd frames idle, so the scroll runs every other frame
0B6D: 2A C4 63        LD      HL,($63C4)          ; {hard.workRam+3C4} the walk cursor into the delta table
0B70: 7E              LD      A,(HL)              
0B71: FE 7F           CP      $7F                 ; the sentinel means the scroll path has wrapped
0B73: CA 86 0B        JP      Z,$0B86             ; {code.loc_0b86}
0B76: 23              INC     HL                  
0B77: 22 C4 63        LD      ($63C4),HL          ; {hard.workRam+3C4} advance the cursor one byte
0B7A: 21 0B 69        LD      HL,$690B            
0B7D: 4F              LD      C,A                 
0B7E: FF              RST     $38                 ; add the signed delta into every record's Y
0B7F: 21 08 69        LD      HL,$6908            
0B82: 0E FF           LD      C,$FF               
0B84: FF              RST     $38                 ; and slide every record one pixel left
0B85: C9              RET                         

loc_0b86:
0B86: 21 CB 38        LD      HL,$38CB            
0B89: 22 C4 63        LD      ($63C4),HL          ; {hard.workRam+3C4} rewind the cursor to the table start
0B8C: 3E 03           LD      A,$03               
0B8E: 32 82 60        LD      ($6082),A           ; {hard.workRam+82} assert the band's sound for three frames
0B91: 21 DC 38        LD      HL,$38DC            ; the band record table
0B94: 3A 8D 63        LD      A,($638D)           ; {hard.workRam+38D}
0B97: 3D              DEC     A                   
0B98: 07              RLCA                        ; scale the remaining band count by sixteen
0B99: 07              RLCA                        
0B9A: 07              RLCA                        
0B9B: 07              RLCA                        
0B9C: 5F              LD      E,A                 
0B9D: 16 00           LD      D,$00               
0B9F: 19              ADD     HL,DE               
0BA0: EB              EX      DE,HL               
0BA1: CD A7 0D        CALL    $0DA7               ; {code.drawBoardLayout} draw that band's girders and ladders
0BA4: 21 8D 63        LD      HL,$638D            
0BA7: 35              DEC     (HL)                ; one band placed
0BA8: C0              RET     NZ                  ; more bands go down on later wraps
0BA9: 3E B0           LD      A,$B0               
0BAB: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} all bands placed: hold 176 frames
0BAE: 21 85 63        LD      HL,$6385            
0BB1: 34              INC     (HL)                ; step on to the final beat
0BB2: C9              RET                         

; The last step of the opening cutscene. Everything keys off substateTimer as the frame
; begins: at 144 frames remaining Kong ROARS -- sndPriority takes the roar tune and
; sndPriorityFrames holds it for 3 frames -- and one of the cutscene's sprite-object
; bytes is bumped up by one; at 24 remaining that same byte is bumped back down; at any
; other count neither cue is touched. The countdown is then ticked every frame, and on
; the frame it expires the cutscene ENDS: introStep wraps back to its first step and
; gameSubstate moves on to the how-high screen.
runIntroRoarStep:
0BB3: 21 8A 60        LD      HL,$608A            ; the sound-priority pair
0BB6: 3A 09 60        LD      A,($6009)           ; {hard.workRam+9} the phase countdown as the frame begins
0BB9: FE 90           CP      $90                 ; at 144 frames left, Kong roars
0BBB: 20 0B           JR      NZ,$0BC8            ; {code.loc_0bc8}
0BBD: 36 0F           LD      (HL),$0F            ; the roar tune
0BBF: 23              INC     HL                  
0BC0: 36 03           LD      (HL),$03            ; held for three frames
0BC2: 21 19 69        LD      HL,$6919            
0BC5: 34              INC     (HL)                ; bump the cutscene sprite byte up
0BC6: 18 09           JR      $0BD1               ; {code.loc_0bd1}

loc_0bc8:
0BC8: FE 18           CP      $18                 ; at 24 frames left
0BCA: 20 05           JR      NZ,$0BD1            ; {code.loc_0bd1}
0BCC: 21 19 69        LD      HL,$6919            
0BCF: 35              DEC     (HL)                ; bump that same byte back down
0BD0: 00              NOP                         

loc_0bd1:
0BD1: DF              RST     $18                 ; tick the countdown; nothing more until it expires
0BD2: AF              XOR     A                   
0BD3: 32 85 63        LD      ($6385),A           ; {hard.workRam+385} the cutscene is over: wrap the step sequence
0BD6: 34              INC     (HL)                ; re-arm the timer to 1 for the next screen
0BD7: 23              INC     HL                  
0BD8: 34              INC     (HL)                ; move the sub-state on to the how-high screen
0BD9: C9              RET                         

; Build the "HOW HIGH CAN YOU GET?" screen -- a diagonal stack of girders with a small
; climbing figure on each, one girder taller each time the player advances a board,
; which is what makes it read as a height. The sound channels are silenced first,
; unconditionally, then everything below is gated on substateTimer expiring. On that
; frame: clear the playfield and sprite buffer, post the lives-marker redraw, seed
; palette bank 1 and the level-start tune, then set the height -- howHighIndex is
; clamped to at most 5 and raised by one if boardSeqPtr has moved since howHighLastSeq,
; which is exactly the case where a board was cleared. That index IS the girder count.
; Each row lays six 4-tile girder groups backwards through video RAM and copies a 3-byte
; climb-figure record into the next sprite slot. The row loop tests at the bottom, so a
; height of 0 paints 256 rows, not none.
buildHowHighScreen:
0BDA: CD 1C 01        CALL    $011C               ; {code.silenceSound} unconditional, ahead of the frame gate
0BDD: DF              RST     $18                 ; everything below runs only on the expiry frame
0BDE: CD 74 08        CALL    $0874               ; {code.clearPlayfieldAndSprites}
0BE1: 16 06           LD      D,$06               ; task 6 redraws the lives markers
0BE3: 3A 00 62        LD      A,($6200)           ; {hard.workRam+200} passed as the count of lives in play
0BE6: 5F              LD      E,A                 
0BE7: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0BEA: 21 86 7D        LD      HL,$7D86            
0BED: 36 01           LD      (HL),$01            ; palette bank 1 for the how-high screen
0BEF: 23              INC     HL                  
0BF0: 36 00           LD      (HL),$00            
0BF2: 21 8A 60        LD      HL,$608A            
0BF5: 36 02           LD      (HL),$02            ; the level-start tune
0BF7: 23              INC     HL                  
0BF8: 36 03           LD      (HL),$03            ; held for three frames
0BFA: 21 A7 63        LD      HL,$63A7            
0BFD: 36 00           LD      (HL),$00            ; reset the climb-figure record index
0BFF: 21 DC 76        LD      HL,$76DC            
0C02: 22 A8 63        LD      ($63A8),HL          ; {hard.workRam+3A8} seed the sprite-slot walk pointer
0C05: 3A 2E 62        LD      A,($622E)           ; {hard.workRam+22E}
0C08: FE 06           CP      $06                 ; the height is clamped to five girders
0C0A: 38 05           JR      C,$0C11             ; {code.loc_0c11}
0C0C: 3E 05           LD      A,$05               
0C0E: 32 2E 62        LD      ($622E),A           ; {hard.workRam+22E} write the clamp back

loc_0c11:
0C11: 3A 2F 62        LD      A,($622F)           ; {hard.workRam+22F} the board-order pointer as it was last time
0C14: 47              LD      B,A                 
0C15: 3A 2A 62        LD      A,($622A)           ; {hard.workRam+22A} and where it is now
0C18: B8              CP      B                   
0C19: 28 04           JR      Z,$0C1F             ; {code.loc_0c1f} unchanged, so the same height as before
0C1B: 21 2E 62        LD      HL,$622E            
0C1E: 34              INC     (HL)                ; a board was cleared: one girder taller

loc_0c1f:
0C1F: 32 2F 62        LD      ($622F),A           ; {hard.workRam+22F} remember it for next time
0C22: 3A 2E 62        LD      A,($622E)           ; {hard.workRam+22E}
0C25: 47              LD      B,A                 ; the height index is the girder-row count
0C26: 21 BC 75        LD      HL,$75BC            ; the first girder cell

loc_0c29:
0C29: 0E 50           LD      C,$50               ; the first girder tile code of the row

loc_0c2b:
0C2B: 71              LD      (HL),C              
0C2C: 0C              INC     C                   
0C2D: 2B              DEC     HL                  
0C2E: 71              LD      (HL),C              
0C2F: 0C              INC     C                   
0C30: 2B              DEC     HL                  
0C31: 71              LD      (HL),C              
0C32: 0C              INC     C                   
0C33: 2B              DEC     HL                  
0C34: 71              LD      (HL),C              
0C35: 79              LD      A,C                 
0C36: FE 67           CP      $67                 ; the last girder tile code ends the row
0C38: CA 43 0C        JP      Z,$0C43             ; {code.loc_0c43}
0C3B: 0C              INC     C                   
0C3C: 11 23 00        LD      DE,$0023            ; step to the next four-tile group
0C3F: 19              ADD     HL,DE               
0C40: C3 2B 0C        JP      $0C2B               ; {code.loc_0c2b}

loc_0c43:
0C43: 3A A7 63        LD      A,($63A7)           ; {hard.workRam+3A7} the climb-figure record index
0C46: 3C              INC     A                   
0C47: 32 A7 63        LD      ($63A7),A           ; {hard.workRam+3A7} step it for the next row
0C4A: 3D              DEC     A                   
0C4B: CB 27           SLA     A                   ; four bytes per figure record
0C4D: CB 27           SLA     A                   
0C4F: E5              PUSH    HL                  ; keep the girder cursor across the figure copy
0C50: 21 F0 3C        LD      HL,$3CF0            ; the climb-figure record table
0C53: C5              PUSH    BC                  
0C54: DD 2A A8 63     LD      IX,($63A8)          ; {hard.workRam+3A8} the sprite slot this row's figure goes in
0C58: 4F              LD      C,A                 
0C59: 06 00           LD      B,$00               
0C5B: 09              ADD     HL,BC               
0C5C: 7E              LD      A,(HL)              
0C5D: DD 77 60        LD      (IX+$60),A          ; copy the record's three bytes into the sprite slot
0C60: 23              INC     HL                  
0C61: 7E              LD      A,(HL)              
0C62: DD 77 40        LD      (IX+$40),A          
0C65: 23              INC     HL                  
0C66: 7E              LD      A,(HL)              
0C67: DD 77 20        LD      (IX+$20),A          
0C6A: DD 36 E0 8B     LD      (IX-$20),$8B        ; a fixed tile just below the figure
0C6E: C1              POP     BC                  
0C6F: DD E5           PUSH    IX                  
0C71: E1              POP     HL                  
0C72: 11 FC FF        LD      DE,$FFFC            ; the next figure sits four slots back
0C75: 19              ADD     HL,DE               
0C76: 22 A8 63        LD      ($63A8),HL          ; {hard.workRam+3A8}
0C79: E1              POP     HL                  
0C7A: 11 5F FF        LD      DE,$FF5F            ; back up to the next girder row
0C7D: 19              ADD     HL,DE               
0C7E: 05              DEC     B                   
0C7F: C2 29 0C        JP      NZ,$0C29            ; {code.loc_0c29} one row per unit of height
0C82: 11 07 03        LD      DE,$0307            ; post the screen's composition task
0C85: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
0C88: 21 09 60        LD      HL,$6009            
0C8B: 36 A0           LD      (HL),$A0            ; hold the finished screen 160 frames
0C8D: 23              INC     HL                  
0C8E: 34              INC     (HL)                
0C8F: 34              INC     (HL)                ; advance the sub-state by two
0C90: C9              RET                         

; The gated board build. Every frame it counts substateTimer down by one and, while the
; timer is still above zero, does nothing else; only on the tick that brings it to zero
; does the full board build run -- which includes writing the palette-bank latch the
; display reads to pick its colour set. The polarity matters: the build fires on EXPIRY,
; not while counting. The board builder also has a second, ungated entry, used for the
; timed advance into 25m.
buildBoardWhenTimerExpires:
0C91: DF              RST     $18                 ; build the board only on the frame the timer expires

; Build a board. Clear the tilemap playfield and the sprite shadow buffer, reset
; bonusDisplay to 0, post the opening deferred task (opcode 5, argument 1), and select
; palette bank 2 by clearing bit 0 and setting bit 1 of the two-bit palette-bank latch.
; Then read board and hand off to the matching per-board setup arm: 1 = 25m girders, 2 =
; 50m conveyors, 3 = 75m elevators. Any other value -- in play, board 4 -- falls into the
; inline 100m rivet arm, which clears the sprite rows, raises the palette bank to 3,
; queues the rivet background tune into sndBgm, points at the rivet layout table, and
; runs the same shared draw/setup tail the other three arms converge on.
buildBoard:
0C92: CD 74 08        CALL    $0874               ; {code.clearPlayfieldAndSprites} wipe the previous board
0C95: AF              XOR     A                   
0C96: 32 8C 63        LD      ($638C),A           ; {hard.workRam+38C} start the bonus readout at zero
0C99: 11 01 05        LD      DE,$0501            ; the opening task: opcode 5, argument 1
0C9C: CD 9F 30        CALL    $309F               ; {code.enqueueTask} post it onto the deferred-work queue
0C9F: 21 86 7D        LD      HL,$7D86            ; point at the two palette-bank latches
0CA2: 36 00           LD      (HL),$00            ; bit 0 clear
0CA4: 23              INC     HL                  
0CA5: 36 01           LD      (HL),$01            ; bit 1 set: colour bank 2 for the build
0CA7: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} which board is being built
0CAA: 3D              DEC     A                   
0CAB: CA D4 0C        JP      Z,$0CD4             ; {code.setup25mGirderBoard} board 1: the 25m girders
0CAE: 3D              DEC     A                   
0CAF: CA DF 0C        JP      Z,$0CDF             ; {code.setup50mConveyorBoard} board 2: the 50m conveyors
0CB2: 3D              DEC     A                   
0CB3: CA F2 0C        JP      Z,$0CF2             ; {code.setUp75mBoard} board 3: the 75m elevators
0CB6: CD 43 0D        CALL    $0D43               ; {code.stampRivetBoardBands} board 4 falls through: the rivets
0CB9: 21 86 7D        LD      HL,$7D86            ; back to the palette-bank latches
0CBC: 36 01           LD      (HL),$01            ; raise bit 0: colour bank 3 for the rivets
0CBE: 3E 0B           LD      A,$0B               
0CC0: 32 89 60        LD      ($6089),A           ; {hard.workRam+89} start the rivet-board background tune
0CC3: 11 8B 3C        LD      DE,$3C8B            ; select the 100m rivet layout table

loc_0cc6:
0CC6: CD A7 0D        CALL    $0DA7               ; {code.drawBoardLayout} walk the layout table into the playfield
0CC9: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227}
0CCC: FE 04           CP      $04                 ; the rivet board has extra decoration
0CCE: CC 00 0D        CALL    Z,$0D00             ; {code.stampRivetBoardTiles} only on the rivet board
0CD1: C3 A0 3F        JP      $3FA0               ; {code.loc_3fa0} on into the rest of board setup

; The 25m arm of the four-way board-setup dispatch. It points the layout selector at the
; 25m girder layout -- the sentinel-terminated list of girder and ladder segment records
; the shared tail walks into the playfield -- queues tune 8 into sndBgm, then falls into
; the tail all four arms share, whose return is this routine's return.
setup25mGirderBoard:
0CD4: 11 E4 3A        LD      DE,$3AE4            ; select the 25m girder layout table
0CD7: 3E 08           LD      A,$08               
0CD9: 32 89 60        LD      ($6089),A           ; {hard.workRam+89} start the 25m background tune
0CDC: C3 C6 0C        JP      $0CC6               ; {code.loc_0cc6} join the shared board-setup tail

; The board-setup arm for 50m, the conveyor board. Selects the 50m colour set by writing
; 1 and 0 to the two hardware palette-bank latches the display reads, selects background
; tune 0x09 (the boards take consecutive tune slots and 50m takes the middle one), then
; points at the 50m conveyor layout table and runs the shared tail that walks it into
; video RAM and finishes board setup.
setup50mConveyorBoard:
0CDF: 11 5D 3B        LD      DE,$3B5D            ; select the 50m conveyor layout table
0CE2: 21 86 7D        LD      HL,$7D86            
0CE5: 36 01           LD      (HL),$01            ; bit 0 set
0CE7: 23              INC     HL                  
0CE8: 36 00           LD      (HL),$00            ; bit 1 clear: colour bank 1 for 50m
0CEA: 3E 09           LD      A,$09               
0CEC: 32 89 60        LD      ($6089),A           ; {hard.workRam+89} the 50m tune, the middle of the four slots
0CEF: C3 C6 0C        JP      $0CC6               ; {code.loc_0cc6} join the shared board-setup tail

; The 75m (elevators) board-setup arm, one of four the board build branches to on board.
; Each arm makes its board's three fixed choices and hands off to the shared draw tail.
; This one plants the elevator board's fixed decorative tile motifs into the background
; tilemap -- the extra step the flat 25m and 50m boards do not have -- selects the 75m
; background tune (the four arms write consecutive tune slots, and this is the third),
; then points at the 75m elevator layout table and runs the tail, which walks that table
; into video RAM.
setUp75mBoard:
0CF2: CD 27 0D        CALL    $0D27               ; {code.stamp75mBoardTiles} the elevator board's fixed scenery
0CF5: 3E 0A           LD      A,$0A               
0CF7: 32 89 60        LD      ($6089),A           ; {hard.workRam+89} start the 75m background tune
0CFA: 11 E5 3B        LD      DE,$3BE5            ; select the 75m elevator layout table
0CFD: C3 C6 0C        JP      $0CC6               ; {code.loc_0cc6} join the shared board-setup tail

; Stamp a fixed two-tile motif into eight video-RAM cells during 100m rivet-board setup.
; It walks an eight-entry little-endian pointer table and writes tile codes 0xB8 then
; 0xB7 into each destination pair -- two groups of four cells at a stride of five
; columns. It takes no argument and every stored value is a constant, so the sixteen
; writes are identical on every call.
stampRivetBoardTiles:
0D00: 06 08           LD      B,$08               ; eight destinations to stamp
0D02: 21 17 0D        LD      HL,$0D17            ; the table of video-RAM destinations

loc_0d05:
0D05: 3E B8           LD      A,$B8               ; the first of the two tile codes
0D07: 0E 02           LD      C,$02               ; two cells per destination
0D09: 5E              LD      E,(HL)              ; read the little-endian destination pointer
0D0A: 23              INC     HL                  
0D0B: 56              LD      D,(HL)              
0D0C: 23              INC     HL                  

loc_0d0d:
0D0D: 12              LD      (DE),A              ; stamp the tile
0D0E: 3D              DEC     A                   ; the second cell takes the next code down
0D0F: 13              INC     DE                  
0D10: 0D              DEC     C                   
0D11: C2 0D 0D        JP      NZ,$0D0D            ; {code.loc_0d0d}
0D14: 10 EF           DJNZ    $0D05               ; {code.loc_0d05} on to the next destination
0D16: C9              RET                         

; ---- $0D17-$0D26: data ----
0D17: CA 76 CF 76 D4 76 D9 76 2A 75 2F 75 34 75 39 75

; Part of the static background of the elevator board, planted before its layout table
; is chosen. It calls the shared two-row filler at two hard-coded tilemap positions,
; each laying 17 cells of one tile code along a row and 17 cells of a second code on the
; row directly below; the second motif sits eight tilemap rows above the first, and the
; two are disjoint -- 68 background cells in all. Every value and destination is a baked
; constant, so it reads no memory and repaints identically on every call. The writes
; land in the background tilemap, not the sprite buffer, and they set tile codes rather
; than blanking anything.
stamp75mBoardTiles:
0D27: 21 0D 77        LD      HL,$770D            ; top-left cell of the first two-row motif
0D2A: CD 30 0D        CALL    $0D30               ; {code.fillTileRowPair}
0D2D: 21 0D 76        LD      HL,$760D            ; the second motif, eight tilemap rows on

; Lay a fixed two-row scenery motif into the background tilemap from the caller's
; top-left cell: 17 consecutive cells of one tile, then skip 15, then 17 cells of a
; second tile directly beneath the first run. The tilemap is 32 cells wide, so 17
; written plus 15 skipped is exactly one row and the walk lands on the same column one
; row on. Both tile codes and both counts are fixed here; only the start cell is the
; caller's.
fillTileRowPair:
0D30: 06 11           LD      B,$11               ; 17 cells in each row of the motif

loc_0d32:
0D32: 36 FD           LD      (HL),$FD            ; row one's tile code
0D34: 23              INC     HL                  
0D35: 10 FB           DJNZ    $0D32               ; {code.loc_0d32}
0D37: 11 0F 00        LD      DE,$000F            ; the 15 cells left in the 32-wide row
0D3A: 19              ADD     HL,DE               ; land on the same column, one row on
0D3B: 06 11           LD      B,$11               

loc_0d3d:
0D3D: 36 FC           LD      (HL),$FC            ; row two's tile, directly beneath row one
0D3F: 23              INC     HL                  
0D40: 10 FB           DJNZ    $0D3D               ; {code.loc_0d3d}
0D42: C9              RET                         

; Stamp the two-band tile motif into two fixed tilemap rows during 100m setup. A thin
; wrapper over the shared two-band filler, run once per row base: each pass lays tile
; 0xFD across four consecutive cells, steps over a 28-cell gap, and lays tile 0xFC across
; four more -- sixteen cells in all, eight per row. Both row bases are constants and it
; takes no argument.
stampRivetBoardBands:
0D43: 21 87 76        LD      HL,$7687            ; the first of two tilemap row bases
0D46: CD 4C 0D        CALL    $0D4C               ; {code.stampTwoTileBands}
0D49: 21 47 75        LD      HL,$7547            ; the second row base, then fall through

; Lay two four-cell tile bands into a tilemap row. From the row base in HL it writes tile
; 0xFD across four consecutive cells, steps forward over a 28-cell gap, and writes tile
; 0xFC across four more -- eight cells in all, ending 36 past the base. Both run lengths
; and both tile codes are constants, so the only input is the base pointer. Called twice
; from the 100m rivet-board setup, at two fixed row bases.
stampTwoTileBands:
0D4C: 06 04           LD      B,$04               ; four cells in the first band

loc_0d4e:
0D4E: 36 FD           LD      (HL),$FD            ; the first band's tile code
0D50: 23              INC     HL                  
0D51: 10 FB           DJNZ    $0D4E               ; {code.loc_0d4e}
0D53: 11 1C 00        LD      DE,$001C            ; the 28-cell gap between the two bands
0D56: 19              ADD     HL,DE               
0D57: 06 04           LD      B,$04               

loc_0d59:
0D59: 36 FC           LD      (HL),$FC            ; the second band's tile code
0D5B: 23              INC     HL                  
0D5C: 10 FB           DJNZ    $0D59               ; {code.loc_0d59}
0D5E: C9              RET                         

loc_0d5f:
0D5F: CD 56 0F        CALL    $0F56               ; {code.initBoardState} reset the board's work RAM and objects

loc_0d62:
0D62: CD 41 24        CALL    $2441               ; {code.loadBoardObjectRecords}

loc_0d65:
0D65: 21 09 60        LD      HL,$6009            
0D68: 36 40           LD      (HL),$40            ; hold the built board for 64 frames
0D6A: 23              INC     HL                  
0D6B: 34              INC     (HL)                ; then step on to the next sub-state
0D6C: 21 5C 38        LD      HL,$385C            ; the sprite-object template in program data
0D6F: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock} it leaves its source pointer advanced
0D72: 11 00 69        LD      DE,$6900            ; the head of the sprite shadow buffer
0D75: 01 08 00        LD      BC,$0008            ; two more records from the same stream
0D78: ED B0           LDIR                        
0D7A: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227}
0D7D: FE 04           CP      $04                 ; the rivet board shifts its sprites
0D7F: 28 0A           JR      Z,$0D8B             ; {code.loc_0d8b}
0D81: 0F              RRCA                        
0D82: 0F              RRCA                        ; test bit 1 of the board number
0D83: D8              RET     C                   ; 50m and 75m need no offset at all
0D84: 21 0B 69        LD      HL,$690B            ; the Y byte of the first sprite record
0D87: 0E FC           LD      C,$FC               ; shift the whole Y column up by four
0D89: FF              RST     $38                 ; apply it across all ten records
0D8A: C9              RET                         

loc_0d8b:
0D8B: 21 08 69        LD      HL,$6908            ; the X byte of the first sprite record
0D8E: 0E 44           LD      C,$44               ; shift the whole X column right by 0x44
0D90: FF              RST     $38                 ; apply it across all ten records
0D91: 11 04 00        LD      DE,$0004            ; stride four: one byte per sprite record
0D94: 01 10 02        LD      BC,$0210            ; two records, each nudged up by 0x10
0D97: 21 00 69        LD      HL,$6900            ; from the first sprite record's X
0D9A: CD 3D 00        CALL    $003D               ; {code.addStrided}
0D9D: 01 F8 02        LD      BC,$02F8            ; two more, each nudged down by eight
0DA0: 21 03 69        LD      HL,$6903            ; from the first sprite record's Y
0DA3: CD 3D 00        CALL    $003D               ; {code.addStrided}
0DA6: C9              RET                         

; The head of the playfield walk: draw the whole static board from its segment table.
; Each record is at least five bytes -- kind, then the y and x of the first point and
; the y and x of the second -- and the table ends on the terminator kind 0xAA. Per
; record it converts the first point to a tile address into segAddr1, saves the sub-tile
; remainders the conversion discards into segSubtileY1 and segSubtile1, stashes the kind
; in segKind, computes the height as the ABSOLUTE difference of the two y values (an
; unsigned extent, so either ordering gives the same magnitude), and hands the second
; point and that height to the per-segment step. That step converts the second point and
; dispatches the girder or ladder drawer, whose renderer tail advances the table pointer
; past the record and comes back, so the walk continues to the terminator.
drawBoardLayout:
0DA7: 1A              LD      A,(DE)              ; read the next record's kind byte
0DA8: 32 B3 63        LD      ($63B3),A           ; {hard.workRam+3B3} stash it for the drawers to dispatch on
0DAB: FE AA           CP      $AA                 ; the table's terminator
0DAD: C8              RET     Z                   ; no records left, the board is drawn
0DAE: 13              INC     DE                  
0DAF: 1A              LD      A,(DE)              ; the first point's y
0DB0: 67              LD      H,A                 
0DB1: 44              LD      B,H                 ; keep y for the sub-tile remainder
0DB2: 13              INC     DE                  
0DB3: 1A              LD      A,(DE)              ; the first point's x
0DB4: 6F              LD      L,A                 
0DB5: 4D              LD      C,L                 ; keep x for the run and the remainder
0DB6: D5              PUSH    DE                  ; the conversion clobbers the table cursor
0DB7: CD F0 2F        CALL    $2FF0               ; {code.tileAddrForPixel}
0DBA: D1              POP     DE                  
0DBB: 22 AB 63        LD      ($63AB),HL          ; {hard.workRam+3AB} the cell the first point falls in
0DBE: 78              LD      A,B                 
0DBF: E6 07           AND     $07                 ; the low bits the conversion dropped
0DC1: 32 B4 63        LD      ($63B4),A           ; {hard.workRam+3B4}
0DC4: 79              LD      A,C                 
0DC5: E6 07           AND     $07                 ; the same for x
0DC7: 32 AF 63        LD      ($63AF),A           ; {hard.workRam+3AF}
0DCA: 13              INC     DE                  
0DCB: 1A              LD      A,(DE)              ; the second point's y
0DCC: 67              LD      H,A                 
0DCD: 90              SUB     B                   ; the segment's height, either ordering
0DCE: D2 D3 0D        JP      NC,$0DD3            ; {code.loc_0dd3}
0DD1: ED 44           NEG                         ; make it an unsigned extent

loc_0dd3:
0DD3: 32 B1 63        LD      ($63B1),A           ; {hard.workRam+3B1}
0DD6: 13              INC     DE                  
0DD7: 1A              LD      A,(DE)              ; the second point's x
0DD8: 6F              LD      L,A                 
0DD9: 91              SUB     C                   ; the horizontal run between the points
0DDA: 32 B2 63        LD      ($63B2),A           ; {hard.workRam+3B2}
0DDD: 1A              LD      A,(DE)              
0DDE: E6 07           AND     $07                 ; the second point's sub-tile x
0DE0: 32 B0 63        LD      ($63B0),A           ; {hard.workRam+3B0}
0DE3: D5              PUSH    DE                  ; save the cursor across the conversion
0DE4: CD F0 2F        CALL    $2FF0               ; {code.tileAddrForPixel}
0DE7: D1              POP     DE                  
0DE8: 22 AD 63        LD      ($63AD),HL          ; {hard.workRam+3AD} the cell the far end falls in
0DEB: 3A B3 63        LD      A,($63B3)           ; {hard.workRam+3B3}
0DEE: FE 02           CP      $02                 ; kinds are compared as signed here
0DF0: F2 4F 0E        JP      P,$0E4F             ; {code.drawGirderSpan} kind 2 and up: the girder drawer
0DF3: 3A B2 63        LD      A,($63B2)           ; {hard.workRam+3B2} kinds 0 and 1: the ladders
0DF6: D6 10           SUB     $10                 
0DF8: 47              LD      B,A                 
0DF9: 3A AF 63        LD      A,($63AF)           ; {hard.workRam+3AF}
0DFC: 80              ADD     A,B                 ; fold the sub-tile offset into the run
0DFD: 32 B2 63        LD      ($63B2),A           ; {hard.workRam+3B2}
0E00: 3A AF 63        LD      A,($63AF)           ; {hard.workRam+3AF}
0E03: C6 F0           ADD     A,$F0               ; the near-end cap tile for that offset
0E05: 2A AB 63        LD      HL,($63AB)          ; {hard.workRam+3AB}
0E08: 77              LD      (HL),A              ; stamp it at the first point
0E09: 2C              INC     L                   
0E0A: D6 30           SUB     $30                 
0E0C: 77              LD      (HL),A              ; and its partner in the next cell
0E0D: 3A B3 63        LD      A,($63B3)           ; {hard.workRam+3B3}
0E10: FE 01           CP      $01                 
0E12: C2 19 0E        JP      NZ,$0E19            ; {code.drawLadder} kind 0 keeps its body run
0E15: AF              XOR     A                   
0E16: 32 B2 63        LD      ($63B2),A           ; {hard.workRam+3B2} kind 1 is caps only: no body run

; Fill a board-layout segment's body run with the uniform ladder tile 0xC0, then draw
; its end cap. The layout walk hands over a write pointer already aimed at the segment's
; first cell and segRun holding the run's pixel extent; each step stamps one cell and
; pays segRun down by 8 pixels, storing the final borrowed value too. The pointer
; advances along the raw tilemap COLUMN axis, which the quarter-turn display makes the
; DISPLAYED VERTICAL -- so these are short vertical runs on screen, the opposite of what
; the raw axis suggests. What it lays down is the ladders: the two full-height ones
; beside Kong plus eight shorter segments. It touches no girder pixel. The pointer
; advances by its low byte only, so the walk wraps inside the 256-cell page and never
; crosses into the next row's high byte.
drawLadder:
0E19: 3A B2 63        LD      A,($63B2)           ; {hard.workRam+3B2}
0E1C: D6 08           SUB     $08                 ; pay one tile, eight pixels, off the run
0E1E: 32 B2 63        LD      ($63B2),A           ; {hard.workRam+3B2}
0E21: DA 2A 0E        JP      C,$0E2A             ; {code.drawSegmentEndCap} run spent: cap the far end
0E24: 2C              INC     L                   ; next cell along the ladder
0E25: 36 C0           LD      (HL),$C0            ; the uniform ladder body tile
0E27: C3 19 0E        JP      $0E19               ; {code.drawLadder}

; Close a layout segment at its far endpoint, then step the table cursor on. The
; board-layout renderer walks a table of segment records -- girders and the like --
; filling each run with body tile 0xC0; this is the end cap that runs right after that
; fill. At the pointer in segAddr2 it always writes segSubtile2 + 0xD0. If segKind is 1,
; a single-cell segment, it also writes 0xC0 one cell BACK; and if the sub-tile remainder
; is non-zero, a partial-cell overhang, it writes remainder + 0xE0 one cell FORWARD. Both
; neighbours move the LOW byte only, so a segment ending at a page edge stays on its row.
drawSegmentEndCap:
0E2A: 3A B0 63        LD      A,($63B0)           ; {hard.workRam+3B0}
0E2D: C6 D0           ADD     A,$D0               ; the far-end tile for that sub-tile offset
0E2F: 2A AD 63        LD      HL,($63AD)          ; {hard.workRam+3AD}
0E32: 77              LD      (HL),A              ; always stamped, at the second point
0E33: 3A B3 63        LD      A,($63B3)           ; {hard.workRam+3B3}
0E36: FE 01           CP      $01                 ; a single-cell segment closes behind too
0E38: C2 3F 0E        JP      NZ,$0E3F            ; {code.loc_0e3f}
0E3B: 2D              DEC     L                   
0E3C: 36 C0           LD      (HL),$C0            ; the ladder body tile one cell back
0E3E: 2C              INC     L                   

loc_0e3f:
0E3F: 3A B0 63        LD      A,($63B0)           ; {hard.workRam+3B0}
0E42: FE 00           CP      $00                 ; a non-zero remainder overhangs a cell
0E44: CA 4B 0E        JP      Z,$0E4B             ; {code.loc_0e4b}
0E47: C6 E0           ADD     A,$E0               ; the partial-cell tile for the overhang
0E49: 2C              INC     L                   
0E4A: 77              LD      (HL),A              ; stamp it one cell forward

loc_0e4b:
0E4B: 13              INC     DE                  ; step the cursor past this record
0E4C: C3 A7 0D        JP      $0DA7               ; {code.drawBoardLayout} back to the walk for the next one

; Draw a girder: stamp a run of slope-band tiles for a kind-2 board-layout record.
; Stepping the write pointer by 32 walks the raw tilemap row axis, but the screen is
; turned a quarter turn, so on the glass this lays long sloped HORIZONTAL runs, about 25
; cells long and 2 to 4 thick; the ladders are the layout walk's other drawer. segHeight
; is paid down 8px per row until it borrows, and each row stamps segTile (the segment's
; 0-7 sub-tile offset biased by -0x10, one tile per phase of the 0xF0-0xF7 band) plus the
; paired half-tile beside it, skipping the pair when
; the cell wrapped off the row's right edge or, on the leading row, on the 0xF0 sentinel.
; segRun selects the slant: 0 redraws the same column, positive walks the tile code up
; through the 0xF0-0xF8 band and shifts a column on at the wrap, negative the reverse.
; Any other kind goes to the capped-column drawer.
drawGirderSpan:
0E4F: 3A B3 63        LD      A,($63B3)           ; {hard.workRam+3B3}
0E52: FE 02           CP      $02                 ; only kind 2 belongs to this drawer
0E54: C2 E8 0E        JP      NZ,$0EE8            ; {code.drawCappedTileColumn} kinds 3 and up go elsewhere
0E57: 3A AF 63        LD      A,($63AF)           ; {hard.workRam+3AF}
0E5A: C6 F0           ADD     A,$F0               ; the slope tile for that sub-tile offset
0E5C: 32 B5 63        LD      ($63B5),A           ; {hard.workRam+3B5} the live tile code lives in this cell
0E5F: 2A AB 63        LD      HL,($63AB)          ; {hard.workRam+3AB} start at the girder's first cell

loc_0e62:
0E62: 3A B5 63        LD      A,($63B5)           ; {hard.workRam+3B5}
0E65: 77              LD      (HL),A              ; stamp this row's slope tile
0E66: 23              INC     HL                  
0E67: 7D              LD      A,L                 
0E68: E6 1F           AND     $1F                 ; did that run off the row's edge?
0E6A: CA 78 0E        JP      Z,$0E78             ; {code.loc_0e78}
0E6D: 3A B5 63        LD      A,($63B5)           ; {hard.workRam+3B5}
0E70: FE F0           CP      $F0                 ; the band's first tile has no partner
0E72: CA 78 0E        JP      Z,$0E78             ; {code.loc_0e78}
0E75: D6 10           SUB     $10                 
0E77: 77              LD      (HL),A              ; the paired half-tile beside it

loc_0e78:
0E78: 01 1F 00        LD      BC,$001F            
0E7B: 09              ADD     HL,BC               ; on to the next tilemap row
0E7C: 3A B1 63        LD      A,($63B1)           ; {hard.workRam+3B1}
0E7F: D6 08           SUB     $08                 ; pay eight pixels of height per row
0E81: DA CF 0E        JP      C,$0ECF             ; {code.loc_0ecf} height spent: the girder is drawn
0E84: 32 B1 63        LD      ($63B1),A           ; {hard.workRam+3B1}
0E87: 3A B2 63        LD      A,($63B2)           ; {hard.workRam+3B2}
0E8A: FE 00           CP      $00                 ; a zero run means a level girder
0E8C: CA 62 0E        JP      Z,$0E62             ; {code.loc_0e62}
0E8F: 3A B5 63        LD      A,($63B5)           ; {hard.workRam+3B5}
0E92: 77              LD      (HL),A              ; sloping: a second row at the same code
0E93: 23              INC     HL                  
0E94: 7D              LD      A,L                 
0E95: E6 1F           AND     $1F                 
0E97: CA A0 0E        JP      Z,$0EA0             ; {code.loc_0ea0}
0E9A: 3A B5 63        LD      A,($63B5)           ; {hard.workRam+3B5}
0E9D: D6 10           SUB     $10                 
0E9F: 77              LD      (HL),A              ; its paired half-tile

loc_0ea0:
0EA0: 01 1F 00        LD      BC,$001F            
0EA3: 09              ADD     HL,BC               ; on to the next row
0EA4: 3A B1 63        LD      A,($63B1)           ; {hard.workRam+3B1}
0EA7: D6 08           SUB     $08                 
0EA9: DA CF 0E        JP      C,$0ECF             ; {code.loc_0ecf}
0EAC: 32 B1 63        LD      ($63B1),A           ; {hard.workRam+3B1}
0EAF: 3A B2 63        LD      A,($63B2)           ; {hard.workRam+3B2}
0EB2: CB 7F           BIT     7,A                 ; which way does the girder slope?
0EB4: C2 D3 0E        JP      NZ,$0ED3            ; {code.loc_0ed3} a negative run slopes the other way
0EB7: 3A B5 63        LD      A,($63B5)           ; {hard.workRam+3B5}
0EBA: 3C              INC     A                   ; step one tile up the slope band
0EBB: 32 B5 63        LD      ($63B5),A           ; {hard.workRam+3B5}
0EBE: FE F8           CP      $F8                 ; stepped past the end of the band?
0EC0: C2 C9 0E        JP      NZ,$0EC9            ; {code.loc_0ec9}
0EC3: 23              INC     HL                  ; shift a column on
0EC4: 3E F0           LD      A,$F0               ; and wrap back to the band's first tile
0EC6: 32 B5 63        LD      ($63B5),A           ; {hard.workRam+3B5}

loc_0ec9:
0EC9: 7D              LD      A,L                 
0ECA: E6 1F           AND     $1F                 ; stop if that shift left the row
0ECC: C2 62 0E        JP      NZ,$0E62            ; {code.loc_0e62}

loc_0ecf:
0ECF: 13              INC     DE                  ; step the cursor past this record
0ED0: C3 A7 0D        JP      $0DA7               ; {code.drawBoardLayout} back to the walk

loc_0ed3:
0ED3: 3A B5 63        LD      A,($63B5)           ; {hard.workRam+3B5}
0ED6: 3D              DEC     A                   ; step one tile down the slope band
0ED7: 32 B5 63        LD      ($63B5),A           ; {hard.workRam+3B5}
0EDA: FE F0           CP      $F0                 ; dropped below the band?
0EDC: F2 E5 0E        JP      P,$0EE5             ; {code.loc_0ee5}
0EDF: 2B              DEC     HL                  ; shift a column back
0EE0: 3E F7           LD      A,$F7               ; and re-seat on the band's last tile
0EE2: 32 B5 63        LD      ($63B5),A           ; {hard.workRam+3B5}

loc_0ee5:
0EE5: C3 62 0E        JP      $0E62               ; {code.loc_0e62}

; The kind-3 arm of the board-layout drawer chain: lay a CAPPED vertical tile run down
; the tilemap from the record's converted address segAddr1, sized by segHeight. A top
; cap 0xB3 at the address, then body tiles 0xB1 each one whole tilemap row (0x20)
; further down, then a bottom cap 0xB2 on the row where the extent subtraction borrows.
; The extent is paid down 16 pixels on the first step -- the top cap is two tiles tall
; -- and 8 per body row after, and it lives IN segHeight, reloaded, decremented and
; stored every row rather than in a hidden local. Kind 4 and up is handed straight on to
; the uniform column fill, which draws one tile with a flat 8-pixel step and no caps.
; Either way the record pointer ends one past this record and the walk resumes at the
; next one.
drawCappedTileColumn:
0EE8: 3A B3 63        LD      A,($63B3)           ; {hard.workRam+3B3}
0EEB: FE 03           CP      $03                 ; only kind 3 belongs to this one
0EED: C2 1B 0F        JP      NZ,$0F1B            ; {code.fillTileColumn} kind 4 and up: the plain column fill
0EF0: 2A AB 63        LD      HL,($63AB)          ; {hard.workRam+3AB} start at the cell the record falls in
0EF3: 3E B3           LD      A,$B3               
0EF5: 77              LD      (HL),A              ; the top cap tile
0EF6: 01 20 00        LD      BC,$0020            
0EF9: 09              ADD     HL,BC               ; step one whole tilemap row
0EFA: 3A B1 63        LD      A,($63B1)           ; {hard.workRam+3B1}
0EFD: D6 10           SUB     $10                 ; the top cap is two tiles tall

loc_0eff:
0EFF: DA 14 0F        JP      C,$0F14             ; {code.loc_0f14} extent spent: lay the bottom cap
0F02: 32 B1 63        LD      ($63B1),A           ; {hard.workRam+3B1}
0F05: 3E B1           LD      A,$B1               
0F07: 77              LD      (HL),A              ; a body tile
0F08: 01 20 00        LD      BC,$0020            
0F0B: 09              ADD     HL,BC               
0F0C: 3A B1 63        LD      A,($63B1)           ; {hard.workRam+3B1}
0F0F: D6 08           SUB     $08                 ; each body row spends eight pixels
0F11: C3 FF 0E        JP      $0EFF               ; {code.loc_0eff}

loc_0f14:
0F14: 3E B2           LD      A,$B2               
0F16: 77              LD      (HL),A              ; the bottom cap tile
0F17: 13              INC     DE                  ; step the cursor past this record
0F18: C3 A7 0D        JP      $0DA7               ; {code.drawBoardLayout}

; The board-layout renderer's arm for segment records of kind 4, 5 and 6: draw a solid
; vertical run of one tile. The kind picks the fill code -- 4 and 5 each have their own,
; 6 and anything else take the default -- and it is stashed in segTile. The fill runs
; down from segAddr1, the cell the record's corner fell in, laying a tile, stepping one
; whole tilemap row, and paying segHeight down by one tile's worth of pixels; at least
; one tile is always laid. Kind 7 or more bails without drawing. Both exits step the
; record pointer one byte past this record, and control returns to the walk stepping
; through them.
fillTileColumn:
0F1B: 3A B3 63        LD      A,($63B3)           ; {hard.workRam+3B3}
0F1E: FE 07           CP      $07                 ; a sign test, not an unsigned compare
0F20: F2 CF 0E        JP      P,$0ECF             ; {code.loc_0ecf} kind 7 and up draws nothing at all
0F23: FE 04           CP      $04                 
0F25: CA 4C 0F        JP      Z,$0F4C             ; {code.loc_0f4c} kind 4 has its own fill tile
0F28: FE 05           CP      $05                 
0F2A: CA 51 0F        JP      Z,$0F51             ; {code.loc_0f51} so does kind 5
0F2D: 3E FE           LD      A,$FE               ; kind 6 takes the default fill tile

loc_0f2f:
0F2F: 32 B5 63        LD      ($63B5),A           ; {hard.workRam+3B5}
0F32: 2A AB 63        LD      HL,($63AB)          ; {hard.workRam+3AB} start at the cell the record falls in

; Fill a tilemap column downward from the layout cursor, then resume the walk. It lays
; segTile at the cursor, steps one whole tilemap row (the map is 32 cells wide) and pays
; segHeight down 8 pixels -- one tile -- per row, laying at least one tile and continuing
; while the height holds out. It then steps the record pointer past this record and draws
; the remaining ones.
fillColumnAndContinueWalk:
0F35: 3A B5 63        LD      A,($63B5)           ; {hard.workRam+3B5}
0F38: 77              LD      (HL),A              ; lay the fill tile
0F39: 01 20 00        LD      BC,$0020            
0F3C: 09              ADD     HL,BC               ; step one whole tilemap row
0F3D: 3A B1 63        LD      A,($63B1)           ; {hard.workRam+3B1}
0F40: D6 08           SUB     $08                 ; pay one tile of height
0F42: 32 B1 63        LD      ($63B1),A           ; {hard.workRam+3B1}
0F45: D2 35 0F        JP      NC,$0F35            ; {code.fillColumnAndContinueWalk} while height remains
0F48: 13              INC     DE                  ; step the cursor past this record
0F49: C3 A7 0D        JP      $0DA7               ; {code.drawBoardLayout}

loc_0f4c:
0F4C: 3E E0           LD      A,$E0               ; kind 4's fill tile
0F4E: C3 2F 0F        JP      $0F2F               ; {code.loc_0f2f}

loc_0f51:
0F51: 3E B0           LD      A,$B0               ; kind 5's fill tile
0F53: C3 2F 0F        JP      $0F2F               ; {code.loc_0f2f}

; Reset the per-board work RAM, compute the board's bonus and timer values, seed the
; shared top sprites, then dispatch to the board's own object setup. It zeroes the
; 39-byte player/motion block and the whole object-record plus sprite-buffer span, then
; copies a 64-byte board-object template out of program data over the head of it.
; bonusStart = bonus = bonusEventMark = min(level*10 + 40, 80), all at byte width -- the
; multiply was never widened, which is what gives the level-22 kill screen, where 260
; wraps to 4. bonusPeriod = bonusTick = max(220 - 2*bonus, 40). Two constant hit-box
; copies are set to 4 and 8. Unless board is the rivet board it seeds three 4-byte sprite
; records near the top of the sprite buffer. Finally it tail-dispatches on board to the
; per-board object seeding, 1 = 25m through 4 = 100m.
initBoardState:
0F56: 06 27           LD      B,$27               ; 39 bytes of player and motion state
0F58: 21 00 62        LD      HL,$6200            
0F5B: AF              XOR     A                   

loc_0f5c:
0F5C: 77              LD      (HL),A              ; wiped for the fresh board
0F5D: 2C              INC     L                   
0F5E: 10 FC           DJNZ    $0F5C               ; {code.loc_0f5c}
0F60: 0E 11           LD      C,$11               ; 17 blocks to clear
0F62: 16 80           LD      D,$80               ; 128 bytes each
0F64: 21 80 62        LD      HL,$6280            ; the object records and the sprite buffer

loc_0f67:
0F67: 42              LD      B,D                 

loc_0f68:
0F68: 77              LD      (HL),A              
0F69: 23              INC     HL                  
0F6A: 10 FC           DJNZ    $0F68               ; {code.loc_0f68}
0F6C: 0D              DEC     C                   
0F6D: 20 F8           JR      NZ,$0F67            ; {code.loc_0f67}
0F6F: 21 9C 3D        LD      HL,$3D9C            ; the 64-byte board-object template
0F72: 11 80 62        LD      DE,$6280            
0F75: 01 40 00        LD      BC,$0040            
0F78: ED B0           LDIR                        ; laid over the head of the cleared span
0F7A: 3A 29 62        LD      A,($6229)           ; {hard.workRam+229} the bonus scales with the level
0F7D: 47              LD      B,A                 
0F7E: A7              AND     A                   ; clear the carry before each shift
0F7F: 17              RLA                         
0F80: A7              AND     A                   
0F81: 17              RLA                         
0F82: A7              AND     A                   
0F83: 17              RLA                         ; level times eight
0F84: 80              ADD     A,B                 
0F85: 80              ADD     A,B                 ; level times ten
0F86: C6 28           ADD     A,$28               ; plus 40; the readout shows 100 times this
0F88: FE 51           CP      $51                 
0F8A: 38 02           JR      C,$0F8E             ; {code.loc_0f8e}
0F8C: 3E 50           LD      A,$50               ; clamped at 80

loc_0f8e:
0F8E: 21 B0 62        LD      HL,$62B0            ; the three bonus cells sit together
0F91: 06 03           LD      B,$03               

loc_0f93:
0F93: 77              LD      (HL),A              ; start, current and event mark, all alike
0F94: 2C              INC     L                   
0F95: 10 FC           DJNZ    $0F93               ; {code.loc_0f93}
0F97: 87              ADD     A,A                 ; twice the bonus
0F98: 47              LD      B,A                 
0F99: 3E DC           LD      A,$DC               
0F9B: 90              SUB     B                   ; 220 - 2*bonus: the bonus tick period
0F9C: FE 28           CP      $28                 
0F9E: 30 02           JR      NC,$0FA2            ; {code.loc_0fa2}
0FA0: 3E 28           LD      A,$28               ; floored at 40 frames

loc_0fa2:
0FA2: 77              LD      (HL),A              ; the tick period
0FA3: 2C              INC     L                   
0FA4: 77              LD      (HL),A              ; and the live countdown, seeded alike
0FA5: 21 09 62        LD      HL,$6209            
0FA8: 36 04           LD      (HL),$04            ; the two constant hit-box sizes
0FAA: 2C              INC     L                   
0FAB: 36 08           LD      (HL),$08            
0FAD: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227}
0FB0: 4F              LD      C,A                 ; kept for the dispatch below
0FB1: CB 57           BIT     2,A                 ; only the rivet board has bit 2 set
0FB3: 20 16           JR      NZ,$0FCB            ; {code.loc_0fcb} the rivet board skips these three
0FB5: 21 00 6A        LD      HL,$6A00            ; three decorative sprite records
0FB8: 3E 4F           LD      A,$4F               ; the first one's X
0FBA: 06 03           LD      B,$03               

loc_0fbc:
0FBC: 77              LD      (HL),A              
0FBD: 2C              INC     L                   
0FBE: 36 3A           LD      (HL),$3A            ; tile code
0FC0: 2C              INC     L                   
0FC1: 36 0F           LD      (HL),$0F            ; colour attribute
0FC3: 2C              INC     L                   
0FC4: 36 18           LD      (HL),$18            ; Y, the same for all three
0FC6: 2C              INC     L                   
0FC7: C6 10           ADD     A,$10               ; space the next one 16 across
0FC9: 10 F1           DJNZ    $0FBC               ; {code.loc_0fbc}

loc_0fcb:
0FCB: 79              LD      A,C                 
0FCC: EF              RST     $28                 ; vector to this board's own object setup

; ---- $0FCD-$0FD6: jump table ----
0FCD: 00 00 D7 0F 1F 10 87 10 31 11

; Build the 25m board's initial object records and their sprite shadows from fixed
; templates. It runs after the board-setup head has cleared that whole region, so it is
; pure initialisation: every byte comes from a template and none of its inputs come from
; prior work RAM. Straight-line, seven steps, no branches -- copy a 16-byte
; sprite-buffer block; stamp a 4-byte group into 5 strided records on the first object
; page; scatter a 6-byte template into one object record and a 4-byte sprite array; copy
; a 4-byte sprite record; seed an object pair from a position table and emit their two
; sprite records; stamp a 4-byte group into 8 strided records on the barrel page; then
; the SAME group into 2 records on the next page with only the destination and count
; reloaded. That last reuse is the one subtlety: the group replicator preserves its
; source pointer and stride across a call, and this relies on it.
seed25mBoardObjects:
0FD7: 21 DC 3D        LD      HL,$3DDC            ; a 16-byte sprite-record template
0FDA: 11 A8 69        LD      DE,$69A8            
0FDD: 01 10 00        LD      BC,$0010            
0FE0: ED B0           LDIR                        
0FE2: 21 EC 3D        LD      HL,$3DEC            ; a 4-byte group to broadcast
0FE5: 11 07 64        LD      DE,$6407            ; field +7 of the first fire record
0FE8: 0E 1C           LD      C,$1C               ; records 0x20 apart
0FEA: 06 05           LD      B,$05               ; five of them
0FEC: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
0FEF: 21 F4 3D        LD      HL,$3DF4            ; a 6-byte record template
0FF2: CD FA 11        CALL    $11FA               ; {code.loc_11fa}
0FF5: 21 00 3E        LD      HL,$3E00            ; a single 4-byte sprite record
0FF8: 11 FC 69        LD      DE,$69FC            
0FFB: 01 04 00        LD      BC,$0004            
0FFE: ED B0           LDIR                        
1000: 21 0C 3E        LD      HL,$3E0C            ; the pair's two start positions
1003: CD A6 11        CALL    $11A6               ; {code.seedSpriteObjectPair}
1006: 21 1B 10        LD      HL,$101B            ; the group is the four bytes just below
1009: 11 07 67        LD      DE,$6707            ; field +7 of the first barrel record
100C: 01 1C 08        LD      BC,$081C            ; eight records, 0x20 apart
100F: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
1012: 11 07 68        LD      DE,$6807            ; the same group into the next page
1015: 06 02           LD      B,$02               ; two records; source and stride carry over
1017: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
101A: C9              RET                         

; ---- $101B-$101E: data ----
101B: 00 00 02 02

; Board-object setup for 50m, tail-jumped to when board is 2. A one-shot with no inputs
; of its own -- every pointer, count and stride is an immediate, so it always seeds the
; same board -- and straight-line: five setup helpers, four block copies of fixed
; tables, and a close that sets the board-object marker to 1. It stamps 4-byte groups
; into records of the objArray64 and objArray65a0 blocks, seeds a ten-record block's
; shared sprite field from a template and gathers each record's permuted (X, code,
; attribute, Y) into the sprite areas, scatters a 6-byte record, copies three fixed
; tables into the shadow buffer, seeds an object pair from a position table, and copies
; the last table into the collision sprite records. What the individual records depict
; is not established; the mechanism is.
seed50mBoardObjects:
101F: 21 EC 3D        LD      HL,$3DEC            ; a 4-byte group to broadcast
1022: 11 07 64        LD      DE,$6407            ; field +7 of the first fire record
1025: 01 1C 05        LD      BC,$051C            ; five records, 0x20 apart
1028: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
102B: CD 86 11        CALL    $1186               ; {code.seedObjectBlockSprites}
102E: 21 18 3E        LD      HL,$3E18            ; another 4-byte group
1031: 11 A7 65        LD      DE,$65A7            ; field +7 of the first 50m object
1034: 01 0C 06        LD      BC,$060C            ; six records, 0x10 apart
1037: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
103A: DD 21 A0 65     LD      IX,$65A0            ; read those same six records back
103E: 21 B8 69        LD      HL,$69B8            ; their six hardware sprite records
1041: 11 10 00        LD      DE,$0010            ; records 0x10 apart
1044: 06 06           LD      B,$06               
1046: CD D3 11        CALL    $11D3               ; {code.gatherSpriteRecords}
1049: 21 FA 3D        LD      HL,$3DFA            ; a 6-byte record template
104C: CD FA 11        CALL    $11FA               ; {code.loc_11fa}
104F: 21 04 3E        LD      HL,$3E04            ; a 4-byte sprite record
1052: 11 FC 69        LD      DE,$69FC            
1055: 01 04 00        LD      BC,$0004            
1058: ED B0           LDIR                        
105A: 21 1C 3E        LD      HL,$3E1C            ; an 8-byte sprite block
105D: 11 44 69        LD      DE,$6944            
1060: 01 08 00        LD      BC,$0008            
1063: ED B0           LDIR                        
1065: 21 24 3E        LD      HL,$3E24            ; a 24-byte sprite block
1068: 11 E4 69        LD      DE,$69E4            
106B: 01 18 00        LD      BC,$0018            
106E: ED B0           LDIR                        
1070: 21 10 3E        LD      HL,$3E10            ; the pair's two start positions
1073: CD A6 11        CALL    $11A6               ; {code.seedSpriteObjectPair}
1076: 21 3C 3E        LD      HL,$3E3C            ; the three collision sprite records
1079: 11 0C 6A        LD      DE,$6A0C            
107C: 01 0C 00        LD      BC,$000C            
107F: ED B0           LDIR                        
1081: 3E 01           LD      A,$01               ; mark this board's objects set up
1083: 32 B9 62        LD      ($62B9),A           ; {hard.workRam+2B9}
1086: C9              RET                         

; Lay down the 75m board's object records and their sprite mirror from fixed templates.
; It takes no inputs -- every pointer, count and constant is an immediate -- so the
; elevator board always starts from the same object and sprite state. Ten steps:
; broadcast a 4-byte template into the +7 field of 5 records of objArray64; seed the
; actor array's sprite field and build its ten sprite records; mark 6 records of
; objArray66 active and put the first three into the spawn state; scatter six X/Y pairs
; into those records and gather their six sprite records; copy a 12-byte template into
; the object-collision sprite slot; activate the board's two fires at fixed coordinates;
; and copy a 16-byte table sitting immediately after this routine's own code into a
; further sprite-buffer slot.
seed75mBoardObjects:
1087: 21 EC 3D        LD      HL,$3DEC            ; a 4-byte group to broadcast
108A: 11 07 64        LD      DE,$6407            ; field +7 of the first fire record
108D: 01 1C 05        LD      BC,$051C            ; five records, 0x20 apart
1090: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
1093: CD 86 11        CALL    $1186               ; {code.seedObjectBlockSprites}
1096: 21 00 66        LD      HL,$6600            ; the board's own six-record array
1099: 11 10 00        LD      DE,$0010            ; records 0x10 apart
109C: 3E 01           LD      A,$01               
109E: 06 06           LD      B,$06               

loc_10a0:
10A0: 77              LD      (HL),A              ; mark each one active
10A1: 19              ADD     HL,DE               
10A2: 10 FC           DJNZ    $10A0               ; {code.loc_10a0}
10A4: 0E 02           LD      C,$02               ; the state fill runs twice
10A6: 3E 08           LD      A,$08               ; the spawn state

loc_10a8:
10A8: 06 03           LD      B,$03               ; the first three records only
10AA: 21 0D 66        LD      HL,$660D            ; their state field

loc_10ad:
10AD: 77              LD      (HL),A              
10AE: 19              ADD     HL,DE               
10AF: 10 FC           DJNZ    $10AD               ; {code.loc_10ad}
10B1: 3E 08           LD      A,$08               
10B3: 0D              DEC     C                   
10B4: C2 A8 10        JP      NZ,$10A8            ; {code.loc_10a8} the second pass rewrites the same cells
10B7: 21 64 3E        LD      HL,$3E64            ; six X/Y pairs from a fixed table
10BA: 11 03 66        LD      DE,$6603            ; into fields +3 and +5 of each record
10BD: 01 0E 06        LD      BC,$060E            ; six records, 0x10 apart
10C0: CD EC 11        CALL    $11EC               ; {code.copyBytePairsStrided}
10C3: 21 60 3E        LD      HL,$3E60            ; a 4-byte appearance group
10C6: 11 07 66        LD      DE,$6607            ; field +7 of those same six records
10C9: 01 0C 06        LD      BC,$060C            
10CC: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
10CF: DD 21 00 66     LD      IX,$6600            ; read those six records back
10D3: 21 58 69        LD      HL,$6958            ; their six hardware sprite records
10D6: 06 06           LD      B,$06               
10D8: 11 10 00        LD      DE,$0010            
10DB: CD D3 11        CALL    $11D3               ; {code.gatherSpriteRecords}
10DE: 21 48 3E        LD      HL,$3E48            ; a 12-byte collision-sprite template
10E1: 11 0C 6A        LD      DE,$6A0C            
10E4: 01 0C 00        LD      BC,$000C            
10E7: ED B0           LDIR                        
10E9: DD 21 00 64     LD      IX,$6400            ; the fire records
10ED: DD 36 00 01     LD      (IX+$00),$01        ; the first fire, marked active
10F1: DD 36 03 58     LD      (IX+$03),$58        ; its X, written to both X fields
10F5: DD 36 0E 58     LD      (IX+$0E),$58        
10F9: DD 36 05 80     LD      (IX+$05),$80        ; its Y, written to both Y fields
10FD: DD 36 0F 80     LD      (IX+$0F),$80        
1101: DD 36 20 01     LD      (IX+$20),$01        ; the second fire, one record on
1105: DD 36 23 EB     LD      (IX+$23),$EB        ; its X, both fields
1109: DD 36 2E EB     LD      (IX+$2E),$EB        
110D: DD 36 25 60     LD      (IX+$25),$60        ; its Y, both fields
1111: DD 36 2F 60     LD      (IX+$2F),$60        
1115: 11 70 69        LD      DE,$6970            
1118: 21 21 11        LD      HL,$1121            ; a 16-byte table sitting just below
111B: 01 10 00        LD      BC,$0010            
111E: ED B0           LDIR                        ; into a slot in the sprite buffer
1120: C9              RET                         

; ---- $1121-$1130: data ----
1121: 37 45 0F 60 37 45 8F F7 77 45 0F 60 77 45 8F F7

; Build the 100m rivet board's object records and their hardware sprite mirror from fixed
; templates. Like its three sibling arms it takes no input -- every pointer, count and
; stride is a constant. It broadcasts a four-byte template into five object records at a
; 32-byte stride; seeds a sprite-object pair from a position table and emits their two
; sprite records; block-copies a twelve-byte table into objectCollisionSprites; scatters
; a position table into the X and Y fields of two further records and broadcasts a
; four-byte group into those two records' appearance fields; then marks both active and
; gathers each one's permuted fields into a hardware sprite record. Those two extra
; records are FIRES, which is why the rivet board's collision arm sweeps seven records
; where every spawn and service path still walks five.
seed100mBoardObjects:
1131: 21 F0 3D        LD      HL,$3DF0            ; a 4-byte group to broadcast
1134: 11 07 64        LD      DE,$6407            ; field +7 of the first fire record
1137: 01 1C 05        LD      BC,$051C            ; five records, 0x20 apart
113A: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
113D: 21 14 3E        LD      HL,$3E14            ; the pair's two start positions
1140: CD A6 11        CALL    $11A6               ; {code.seedSpriteObjectPair}
1143: 21 54 3E        LD      HL,$3E54            ; a 12-byte collision-sprite template
1146: 11 0C 6A        LD      DE,$6A0C            
1149: 01 0C 00        LD      BC,$000C            
114C: ED B0           LDIR                        
114E: 21 82 11        LD      HL,$1182            ; two X/Y pairs from the table just below
1151: 11 A3 64        LD      DE,$64A3            ; into fields +3 and +5 of two records
1154: 01 1E 02        LD      BC,$021E            ; two records, 0x20 apart
1157: CD EC 11        CALL    $11EC               ; {code.copyBytePairsStrided}
115A: 21 7E 11        LD      HL,$117E            ; their shared appearance group
115D: 11 A7 64        LD      DE,$64A7            ; field +7 of those same two records
1160: 01 1C 02        LD      BC,$021C            
1163: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
1166: DD 21 A0 64     LD      IX,$64A0            ; these two records are the rivet fires
116A: DD 36 00 01     LD      (IX+$00),$01        ; the first one, marked active
116E: DD 36 20 01     LD      (IX+$20),$01        ; the second, one record on
1172: 21 50 69        LD      HL,$6950            ; their two hardware sprite records
1175: 06 02           LD      B,$02               
1177: 11 20 00        LD      DE,$0020            
117A: CD D3 11        CALL    $11D3               ; {code.gatherSpriteRecords}
117D: C9              RET                         

; ---- $117E-$1185: data ----
117E: 3F 0C 08 08 73 50 8D 50

; Board setup for one 10-record object block, with no inputs of its own -- every pointer
; and count is a baked immediate. First it stamps a 4-byte template into the sprite-code
; field (+7) of the ten objArray65 records, each 0x10 apart, seeding every record with
; the common sprite code and attribute. Then it gathers the permuted fields +3/+7/+8/+5
; out of those same records into ten consecutive 4-byte hardware sprite records at
; actorSprites: X <- +3, code <- +7, attribute <- +8, Y <- +5. Only the record count is
; reloaded between the two. The name describes the MECHANISM; what the ten objects are
; is not established here.
seedObjectBlockSprites:
1186: 21 A2 11        LD      HL,$11A2            ; the 4-byte template just below
1189: 11 07 65        LD      DE,$6507            ; field +7 of the first of ten records
118C: 01 0C 0A        LD      BC,$0A0C            ; ten records, 0x10 apart
118F: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
1192: DD 21 00 65     LD      IX,$6500            ; read those same ten records back
1196: 21 80 69        LD      HL,$6980            ; ten consecutive sprite records
1199: 06 0A           LD      B,$0A               
119B: 11 10 00        LD      DE,$0010            
119E: CD D3 11        CALL    $11D3               ; {code.gatherSpriteRecords}
11A1: C9              RET                         

; ---- $11A2-$11A5: data ----
11A2: 3B 00 02 02

; Place a pair of sprite objects at two caller-given positions and emit their hardware
; sprite records. It scatters the caller's four-byte position table as [record 0 X,
; record 0 Y, record 1 X, record 1 Y], stamps the SAME 4-byte appearance template into
; both records so the two always look alike, marks both active, and gathers (X, code,
; attribute, Y) from each into two consecutive sprite-buffer records. Every count is a
; fixed two; only the position table varies, and the three call sites pass three
; adjacent tables. What the two objects ARE is not established -- the tables themselves
; were not decoded.
seedSpriteObjectPair:
11A6: 11 83 66        LD      DE,$6683            ; the caller's table fills X and Y here
11A9: 01 0E 02        LD      BC,$020E            ; two records, 0x10 apart
11AC: CD EC 11        CALL    $11EC               ; {code.copyBytePairsStrided}
11AF: 21 08 3E        LD      HL,$3E08            ; one shared look for both objects
11B2: 11 87 66        LD      DE,$6687            ; their sprite-code field
11B5: 01 0C 02        LD      BC,$020C            
11B8: CD 2A 12        CALL    $122A               ; {code.replicateGroupStrided}
11BB: DD 21 80 66     LD      IX,$6680            ; the pair of object records
11BF: DD 36 00 01     LD      (IX+$00),$01        ; mark the first record active
11C3: DD 36 10 01     LD      (IX+$10),$01        ; and the second
11C7: 21 18 6A        LD      HL,$6A18            ; the two hardware sprite records
11CA: 06 02           LD      B,$02               
11CC: 11 10 00        LD      DE,$0010            
11CF: CD D3 11        CALL    $11D3               ; {code.gatherSpriteRecords}
11D2: C9              RET                         

; Build a run of hardware sprite records by gathering four permuted fields out of each
; object record. For each of a caller-supplied count of records -- base, base + stride,
; and so on -- it reads offsets +3, +7, +8, +5 IN THAT ORDER and stores them into four
; consecutive destination bytes, so the sprite record's X comes from the object's +3, its
; code from +7, its attribute from +8 and its Y from +5. A permuting gather, not a block
; copy: +4 and +6 are never read. The destination advances in its low byte only, so it
; wraps within its 256-byte page, and a count of zero means 256 records rather than none.
gatherSpriteRecords:
11D3: DD 7E 03        LD      A,(IX+$03)          ; the object's X
11D6: 77              LD      (HL),A              
11D7: 2C              INC     L                   
11D8: DD 7E 07        LD      A,(IX+$07)          ; its sprite code
11DB: 77              LD      (HL),A              
11DC: 2C              INC     L                   
11DD: DD 7E 08        LD      A,(IX+$08)          ; its colour attribute
11E0: 77              LD      (HL),A              
11E1: 2C              INC     L                   
11E2: DD 7E 05        LD      A,(IX+$05)          ; its Y, read last
11E5: 77              LD      (HL),A              
11E6: 2C              INC     L                   
11E7: DD 19           ADD     IX,DE               ; on to the next object record
11E9: 10 E8           DJNZ    $11D3               ; {code.gatherSpriteRecords}
11EB: C9              RET                         

; Scatter a run of consecutive source byte-pairs into strided destination records. Each
; pass reads two adjacent source bytes and stores them at offsets +0 and +2 of the
; current record; +1 is never written, the destination pointer stepping straight past it.
; The source advances cumulatively, two bytes a pass, as a full 16-bit walk that may
; cross a page; the destination advance touches the low byte only, so it wraps inside its
; own 256 bytes and can never carry out. A pass count of zero means 256 passes, not none.
; Its near-twin copies groups of four and re-reads the same group every pass, which makes
; that one a broadcast where this is a scatter.
copyBytePairsStrided:
11EC: 7E              LD      A,(HL)              ; the first byte of the pair
11ED: 12              LD      (DE),A              ; into the record's +0
11EE: 23              INC     HL                  
11EF: 1C              INC     E                   
11F0: 1C              INC     E                   ; step past +1, which is never written
11F1: 7E              LD      A,(HL)              
11F2: 12              LD      (DE),A              ; the second byte, into +2
11F3: 23              INC     HL                  
11F4: 7B              LD      A,E                 
11F5: 81              ADD     A,C                 ; the record gap, low byte only
11F6: 5F              LD      E,A                 
11F7: 10 F3           DJNZ    $11EC               ; {code.copyBytePairsStrided}
11F9: C9              RET                         

loc_11fa:
11FA: DD 21 A0 66     LD      IX,$66A0            ; the record this fills
11FE: 11 28 6A        LD      DE,$6A28            ; and a 4-byte array in the sprite buffer
1201: DD 36 00 01     LD      (IX+$00),$01        ; mark it active
1205: 7E              LD      A,(HL)              
1206: DD 77 03        LD      (IX+$03),A          ; X
1209: 12              LD      (DE),A              ; mirrored into the array
120A: 1C              INC     E                   
120B: 23              INC     HL                  
120C: 7E              LD      A,(HL)              
120D: DD 77 07        LD      (IX+$07),A          ; sprite code
1210: 12              LD      (DE),A              
1211: 1C              INC     E                   
1212: 23              INC     HL                  
1213: 7E              LD      A,(HL)              
1214: DD 77 08        LD      (IX+$08),A          ; colour attribute
1217: 12              LD      (DE),A              
1218: 1C              INC     E                   
1219: 23              INC     HL                  
121A: 7E              LD      A,(HL)              
121B: DD 77 05        LD      (IX+$05),A          ; Y, written out of order
121E: 12              LD      (DE),A              
121F: 23              INC     HL                  
1220: 7E              LD      A,(HL)              
1221: DD 77 09        LD      (IX+$09),A          ; two more fields, not mirrored
1224: 23              INC     HL                  
1225: 7E              LD      A,(HL)              
1226: DD 77 0A        LD      (IX+$0A),A          
1229: C9              RET                         

; A struct-field initialiser, NOT a blitter: stamp ONE 4-byte source group into a run of
; strided destination records, seeding them all with a common header or value. The
; source is re-read from the same place on every pass and never advances, so the last
; pass copies exactly what the first did, and both it and the gap size survive the call
; unchanged -- which is what lets a caller run it again by reloading only the
; destination and the count. Destination addressing is 8-BIT and confined to one page:
; the low half of the pointer is what steps, so the offset WRAPS inside its own 256
; bytes rather than crossing pages. A near-identical routine copies PAIRS and lets its
; source advance cumulatively; the two look mergeable and are not.
replicateGroupStrided:
122A: E5              PUSH    HL                  ; the group is re-read on every pass
122B: C5              PUSH    BC                  
122C: 06 04           LD      B,$04               ; four bytes to a group

loc_122e:
122E: 7E              LD      A,(HL)              
122F: 12              LD      (DE),A              
1230: 23              INC     HL                  
1231: 1C              INC     E                   ; the destination steps its low byte only
1232: 10 FA           DJNZ    $122E               ; {code.loc_122e}
1234: C1              POP     BC                  
1235: E1              POP     HL                  ; restore the source: it never advances
1236: 7B              LD      A,E                 
1237: 81              ADD     A,C                 ; step over the gap to the next record
1238: 5F              LD      E,A                 
1239: 10 EF           DJNZ    $122A               ; {code.replicateGroupStrided}
123B: C9              RET                         

; Spawn Mario's actor record for the board. Gated on substateTimer, so the body fires
; only on the frame that countdown expires. The start position comes from board: on 75m
; X = 0x16 and Y = 0xE0, on every other board X = 0x3F and Y = 0xF0. It seeds his actor
; record (active flag, X, Y, sprite code 0x80, attribute 0x02, move-step timer 0x01) and
; its 4-byte sprite mirror, advances gameSubstate so the next vblank dispatches the
; following setup step, and enqueues the follow-up task [opcode 6, argument 1].
seedMarioActorRecord:
123C: DF              RST     $18                 ; act only when the countdown expires
123D: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227}
1240: FE 03           CP      $03                 ; 75m starts Mario somewhere else
1242: 01 16 E0        LD      BC,$E016            ; the 75m start: X 0x16, Y 0xE0
1245: CA 4B 12        JP      Z,$124B             ; {code.loc_124b}
1248: 01 3F F0        LD      BC,$F03F            ; every other board: X 0x3F, Y 0xF0

loc_124b:
124B: DD 21 00 62     LD      IX,$6200            ; Mario's actor record
124F: 21 4C 69        LD      HL,$694C            ; and its hardware sprite record
1252: DD 36 00 01     LD      (IX+$00),$01        ; he is alive and being processed
1256: DD 71 03        LD      (IX+$03),C          ; his start X
1259: 71              LD      (HL),C              
125A: 2C              INC     L                   
125B: DD 36 07 80     LD      (IX+$07),$80        ; his standing sprite code
125F: 36 80           LD      (HL),$80            
1261: 2C              INC     L                   
1262: DD 36 08 02     LD      (IX+$08),$02        ; his colour attribute
1266: 36 02           LD      (HL),$02            
1268: 2C              INC     L                   
1269: DD 70 05        LD      (IX+$05),B          ; his start Y
126C: 70              LD      (HL),B              
126D: DD 36 0F 01     LD      (IX+$0F),$01        ; arm the move-step timer
1271: 21 0A 60        LD      HL,$600A            
1274: 34              INC     (HL)                ; on to the next setup step
1275: 11 01 06        LD      DE,$0601            ; the follow-up task: opcode 6, argument 1
1278: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
127B: C9              RET                         

; The sub-state that plays Mario's death animation. It does exactly two things, back to
; back: service the effect-sprite state machine, routing effectState to its per-state
; handler, then vector deathAnimPhase through its jump table to the current phase --
; seed, step, or hand-off. One episode runs a fixed 296 frames. It sits in BOTH sub-state
; tables: in the attract table it is the death the demo ends on, in the credited-game
; table it is what gameplay hands over to on the frame Mario dies. It does not decrement
; the life count -- the next sub-state does. And it is named by effect, not by cause: the
; bonus-timer death reaches the same sequence with marioActive still set, entering past
; the alive test entirely.
runDeathAnimationSubstate:
127C: CD BD 1D        CALL    $1DBD               ; {code.dispatchEffectState} service the effect sprites first

; Vector Mario's death animation to its current-phase handler, through a four-entry table
; of little-endian targets indexed by deathAnimPhase. Phase 0 seeds it: rewrite
; marioSpriteCode to the first death tile keeping its old high bit, prime
; deathAnimTicksLeft to 13, step the phase, re-arm the frame gate to 8, clear the sprite
; runs and fire the death sound line. Phase 1 runs on each expiry of that 8-frame gate,
; ticking the counter down and stepping the sprite through four orientations; at 0 it
; settles the final tile, steps to phase 2 and re-arms the gate to 0x80. Phase 2 advances
; gameSubstate -- by 2 for player 2, 1 for player 1 -- handing off to the life-loss
; handler. Slot 3 is padding: the selector has three writers and none can produce 3. The
; index is doubled in 8 bits, so the address is base + (2*phase & 0xff).
dispatchDeathAnimationPhase:
127F: 3A 9D 63        LD      A,($639D)           ; {hard.workRam+39D} which phase of the death animation
1282: EF              RST     $28                 ; vector through the table just below

; ---- $1283-$128A: jump table ----
1283: 8B 12 AC 12 DE 12 00 00

; The seed arm of Mario's death animation, gated so it acts only on the frame
; substateTimer expires. It rewrites marioSpriteCode to the fixed tile 0x78 while
; preserving bit 7, his facing -- the first of the four orientations the next arm
; cycles. It advances deathAnimPhase 0 -> 1, primes deathAnimTicksLeft to 13 and re-arms
; substateTimer to 8, the tick cadence the next arm runs on; clears four disjoint runs
; of sprite records; and fires the death sound by holding sndIrqTrigger for three
; frames. "Begin" names the START of the animation, not the cause of the death: nothing
; here detects or decides a kill and the life is not taken -- that happens in the
; following sub-state. The animation is not conditional on marioActive being clear; the
; bonus-expiry death reaches the same sequence with it set.
beginMarioDeathAnimation:
128B: DF              RST     $18                 ; act only when the countdown expires
128C: 21 4D 69        LD      HL,$694D            ; Mario's sprite-code byte
128F: 3E F0           LD      A,$F0               ; the first death tile, pre-shifted
1291: CB 16           RL      (HL)                ; carry out his old facing bit
1293: 1F              RRA                         ; shift it back in: tile 0x78, facing kept
1294: 77              LD      (HL),A              
1295: 21 9D 63        LD      HL,$639D            
1298: 34              INC     (HL)                ; on to the cycling phase
1299: 3E 0D           LD      A,$0D               
129B: 32 9E 63        LD      ($639E),A           ; {hard.workRam+39E} thirteen ticks to run
129E: 3E 08           LD      A,$08               
12A0: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} the eight-frame tick cadence
12A3: CD BD 30        CALL    $30BD               ; {code.clearSpriteColumns}
12A6: 3E 03           LD      A,$03               
12A8: 32 88 60        LD      ($6088),A           ; {hard.workRam+88} fire the death sound, held three frames
12AB: C9              RET                         

; The cycling arm of Mario's death animation. It is gated by substateTimer, which
; reloads to 8 on each expiry -- a fixed eight-frame tick. On each tick it takes one off
; deathAnimTicksLeft and steps his sprite: bit 0 of marioSpriteCode flips every tick, so
; the tile alternates between two codes, and on the tick that bit falls back to 0 it
; also flips bit 7 of marioSpriteCode and bit 7 of marioSpriteAttr together. Those two
; are the vertical and horizontal mirror flags, so flipping both is a 180-degree
; ROTATION. When the count reaches zero it instead writes a fixed settle tile,
; preserving the old mirror bit, bumps deathAnimPhase, and reloads the gate long -- 128
; ticks -- so the next arm waits. Primed at 13 ticks, the record takes four (code,
; attribute) pairs cycled three times. This arm does not end the life; the following
; sub-state does.
stepMarioDeathAnimation:
12AC: DF              RST     $18                 ; act only on the frames the gate expires
12AD: 3E 08           LD      A,$08               
12AF: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} re-arm the eight-frame tick
12B2: 21 9E 63        LD      HL,$639E            
12B5: 35              DEC     (HL)                ; one tick off the thirteen
12B6: CA CB 12        JP      Z,$12CB             ; {code.loc_12cb} the cycle is over: settle him
12B9: 21 4D 69        LD      HL,$694D            ; Mario's sprite-code byte
12BC: 7E              LD      A,(HL)              
12BD: 1F              RRA                         ; carry out its old bit 0
12BE: 3E 02           LD      A,$02               
12C0: 1F              RRA                         ; a mask: bit 0 always, bit 7 if it was set
12C1: 47              LD      B,A                 
12C2: AE              XOR     (HL)                ; flip the tile, and the mirror every other
12C3: 77              LD      (HL),A              
12C4: 2C              INC     L                   ; on to the attribute byte
12C5: 78              LD      A,B                 
12C6: E6 80           AND     $80                 
12C8: AE              XOR     (HL)                ; flip its mirror bit on the same tick
12C9: 77              LD      (HL),A              
12CA: C9              RET                         

loc_12cb:
12CB: 21 4D 69        LD      HL,$694D            
12CE: 3E F4           LD      A,$F4               ; the settle tile, pre-shifted
12D0: CB 16           RL      (HL)                ; carry out his old mirror bit
12D2: 1F              RRA                         ; shift it back in: tile 0x7A, mirror kept
12D3: 77              LD      (HL),A              
12D4: 21 9D 63        LD      HL,$639D            
12D7: 34              INC     (HL)                ; on to the hand-off phase
12D8: 3E 80           LD      A,$80               
12DA: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} a long pause before the hand-off
12DD: C9              RET                         

loc_12de:
12DE: DF              RST     $18                 ; wait out that pause
12DF: CD DB 30        CALL    $30DB               ; {code.loc_30db} clear the sprite scratch this state used

loc_12e2:
12E2: 21 0A 60        LD      HL,$600A            
12E5: 3A 0E 60        LD      A,($600E)           ; {hard.workRam+E} which player just died
12E8: A7              AND     A                   
12E9: CA ED 12        JP      Z,$12ED             ; {code.loc_12ed}
12EC: 34              INC     (HL)                ; player 2 skips on to his own handler

loc_12ed:
12ED: 34              INC     (HL)                ; on to the life-loss handler
12EE: 2B              DEC     HL                  
12EF: 36 01           LD      (HL),$01            ; so it runs on the very next frame
12F1: C9              RET                         

; Spend one of player 1's lives and decide what happens next, in a fixed order: silence
; every sound; clear playIntro, so the next life starts without the opening cutscene;
; take one off lives; then copy the live 8-byte player context into p1Context, which the
; next turn restores from. The two clears happen BEFORE the copy, so the saved slot
; carries the reduced life count and the cleared intro flag. Then it branches. Lives
; remaining go to the between-turns interlude -- a different sub-state in a one-player
; game than in a two-player one, where it is the player-alternation screen. None
; remaining means player 1 is finished: format the final score for display and ranking,
; stamp the game-over banner across the screen, queue the render task, and arm a
; 0xC0-frame wait before the game-over sub-state.
losePlayer1Life:
12F2: CD 1C 01        CALL    $011C               ; {code.silenceSound} everything goes quiet as the life ends
12F5: AF              XOR     A                   
12F6: 32 2C 62        LD      ($622C),A           ; {hard.workRam+22C} the next life skips the opening cutscene
12F9: 21 28 62        LD      HL,$6228            ; the life count, first of the context
12FC: 35              DEC     (HL)                ; spend one life
12FD: 7E              LD      A,(HL)              ; how many are left
12FE: 11 40 60        LD      DE,$6040            ; player 1's save slot
1301: 01 08 00        LD      BC,$0008            
1304: ED B0           LDIR                        ; saved with the life already gone
1306: A7              AND     A                   
1307: C2 34 13        JP      NZ,$1334            ; {code.loc_1334} lives remain: back for another turn
130A: 3E 01           LD      A,$01               ; player 1's slot for the ranking
130C: 21 B2 60        LD      HL,$60B2            ; his final score
130F: CD CA 13        CALL    $13CA               ; {code.loc_13ca} format it and rank it in the table
1312: 21 D4 76        LD      HL,$76D4            ; where the game-over banner starts
1315: 3A 0F 60        LD      A,($600F)           ; {hard.workRam+F}
1318: A7              AND     A                   
1319: 28 07           JR      Z,$1322             ; {code.loc_1322}
131B: 11 02 03        LD      DE,$0302            ; a two-player game queues an extra render
131E: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
1321: 2B              DEC     HL                  ; and starts the banner one column left

loc_1322:
1322: CD 26 18        CALL    $1826               ; {code.fillTileBlock} stamp the banner across the screen
1325: 11 00 03        LD      DE,$0300            ; queue the game-over render task
1328: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
132B: 21 09 60        LD      HL,$6009            
132E: 36 C0           LD      (HL),$C0            ; hold it for 192 frames
1330: 23              INC     HL                  
1331: 36 10           LD      (HL),$10            ; then run the game-over sub-state
1333: C9              RET                         

loc_1334:
1334: 0E 08           LD      C,$08               ; one player: the between-turns interlude
1336: 3A 0F 60        LD      A,($600F)           ; {hard.workRam+F}
1339: A7              AND     A                   
133A: CA 3F 13        JP      Z,$133F             ; {code.loc_133f}
133D: 0E 17           LD      C,$17               ; two players: the alternation screen

loc_133f:
133F: 79              LD      A,C                 
1340: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} that is the next sub-state
1343: C9              RET                         

loc_1344:
1344: CD 1C 01        CALL    $011C               ; {code.silenceSound} everything goes quiet as the life ends
1347: AF              XOR     A                   
1348: 32 2C 62        LD      ($622C),A           ; {hard.workRam+22C} the next life skips the opening cutscene
134B: 21 28 62        LD      HL,$6228            ; the life count, first of the context
134E: 35              DEC     (HL)                ; spend one life; unguarded, so 0 wraps
134F: 7E              LD      A,(HL)              ; how many are left
1350: 11 48 60        LD      DE,$6048            ; player 2's save slot
1353: 01 08 00        LD      BC,$0008            
1356: ED B0           LDIR                        ; saved with the life already gone
1358: A7              AND     A                   
1359: C2 7F 13        JP      NZ,$137F            ; {code.loc_137f} lives remain: back for another turn
135C: 3E 03           LD      A,$03               ; player 2's slot for the ranking
135E: 21 B5 60        LD      HL,$60B5            ; his final score
1361: CD CA 13        CALL    $13CA               ; {code.loc_13ca} format it and rank it in the table
1364: 11 03 03        LD      DE,$0303            ; two game-over render tasks
1367: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
136A: 11 00 03        LD      DE,$0300            
136D: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
1370: 21 D3 76        LD      HL,$76D3            ; where the game-over banner starts
1373: CD 26 18        CALL    $1826               ; {code.fillTileBlock} stamp it across the screen
1376: 21 09 60        LD      HL,$6009            
1379: 36 C0           LD      (HL),$C0            ; hold it for 192 frames
137B: 23              INC     HL                  
137C: 36 11           LD      (HL),$11            ; then run the game-over sub-state
137E: C9              RET                         

loc_137f:
137F: 0E 17           LD      C,$17               ; the player-alternation screen
1381: 3A 40 60        LD      A,($6040)           ; {hard.workRam+40} player 1's saved life count
1384: A7              AND     A                   
1385: C2 8A 13        JP      NZ,$138A            ; {code.loc_138a}
1388: 0E 08           LD      C,$08               ; player 1 is out too: the plain interlude

loc_138a:
138A: 79              LD      A,C                 
138B: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} that is the next sub-state
138E: C9              RET                         

loc_138f:
138F: DF              RST     $18                 ; hold this sub-state until the frame timer expires
1390: 0E 17           LD      C,$17               ; the sub-state to run if player 2 still has a game
1392: 3A 48 60        LD      A,($6048)           ; {hard.workRam+48} read player 2's saved life count

loc_1395:
1395: 34              INC     (HL)                ; re-arm the just-expired timer to one frame
1396: A7              AND     A                   
1397: C2 9C 13        JP      NZ,$139C            ; {code.loc_139c} a game still in progress keeps the first choice
139A: 0E 14           LD      C,$14               ; none left, so take the other sub-state

loc_139c:
139C: 79              LD      A,C                 
139D: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} publish the chosen follow-on sub-state
13A0: C9              RET                         

loc_13a1:
13A1: DF              RST     $18                 ; hold this sub-state until the frame timer expires
13A2: 0E 17           LD      C,$17               ; the sub-state to run if player 1 still has a game
13A4: 3A 40 60        LD      A,($6040)           ; {hard.workRam+40} read player 1's saved life count
13A7: C3 95 13        JP      $1395               ; {code.loc_1395} share the twin handler's re-arm and choice

loc_13aa:
13AA: 3A 26 60        LD      A,($6026)           ; {hard.workRam+26} read the cabinet orientation switch
13AD: 32 82 7D        LD      ($7D82),A           ; {hard.flipScreen} mirror it into the flip-screen latch
13B0: AF              XOR     A                   
13B1: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} restart the in-state sub-sequence
13B4: 21 01 01        LD      HL,$0101            ; 1 into both halves of the player-index pair
13B7: 22 0D 60        LD      ($600D),HL          ; {hard.workRam+D} currentPlayer and activePlayerIndex together
13BA: C9              RET                         

; Reset the live player/display context to player 1. Four fixed stores and no reads:
; currentPlayer = 0 and activePlayerIndex = 0, so player 1 is up -- that second byte is
; the low half of a 16-bit pair and doubles as the "one-player start" marker a later
; reader tests for zero, and it is NOT the two-player flag, which is the pair's high byte
; and is left untouched; gameSubstate = 0, restarting the in-state sub-sequence; and the
; flip-screen latch = 1, upright, since player 1 never sees the cocktail mirror. The
; player-2 counterpart writes 1 into the two player bytes and takes the flip latch from
; the cabinet orientation switch.
selectPlayer1Context:
13BB: AF              XOR     A                   
13BC: 32 0D 60        LD      ($600D),A           ; {hard.workRam+D} player 1 is up
13BF: 32 0E 60        LD      ($600E),A           ; {hard.workRam+E} player 1 is the active player
13C2: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} restart the in-game sub-state sequence
13C5: 3C              INC     A                   
13C6: 32 82 7D        LD      ($7D82),A           ; {hard.flipScreen} upright: player 1 never sees the mirror
13C9: C9              RET                         

loc_13ca:
13CA: 11 C6 61        LD      DE,$61C6            ; the score staging area
13CD: 12              LD      (DE),A              ; stash the caller's player tag
13CE: CF              RST     $08                 ; in attract, stop here
13CF: 13              INC     DE                  
13D0: 01 03 00        LD      BC,$0003            
13D3: ED B0           LDIR                        ; copy in the player's 3 packed-BCD score bytes
13D5: 06 03           LD      B,$03               ; three bytes to unpack
13D7: 21 B1 61        LD      HL,$61B1            ; where the six display digits go

loc_13da:
13DA: 1B              DEC     DE                  ; walk the score back to front, top pair first
13DB: 1A              LD      A,(DE)              
13DC: 0F              RRCA                        ; rotate the high digit down
13DD: 0F              RRCA                        
13DE: 0F              RRCA                        
13DF: 0F              RRCA                        
13E0: E6 0F           AND     $0F                 ; isolate the high digit
13E2: 77              LD      (HL),A              ; write it as the first display digit
13E3: 23              INC     HL                  
13E4: 1A              LD      A,(DE)              
13E5: E6 0F           AND     $0F                 ; isolate the low digit
13E7: 77              LD      (HL),A              ; write it as the next display digit
13E8: 23              INC     HL                  
13E9: 10 EF           DJNZ    $13DA               ; {code.loc_13da} on to the next score byte
13EB: 06 0E           LD      B,$0E               ; fourteen blanks pad the field out

loc_13ed:
13ED: 36 10           LD      (HL),$10            ; a blank tile
13EF: 23              INC     HL                  
13F0: 10 FB           DJNZ    $13ED               ; {code.loc_13ed}
13F2: 36 3F           LD      (HL),$3F            ; terminator closing the 21-byte field
13F4: 06 05           LD      B,$05               ; at most five records to bubble past
13F6: 21 A5 61        LD      HL,$61A5            ; the key of the record above
13F9: 11 C7 61        LD      DE,$61C7            ; the new record's own key

loc_13fc:
13FC: 1A              LD      A,(DE)              
13FD: 96              SUB     (HL)                ; compare the two 3-byte keys, low byte first
13FE: 23              INC     HL                  
13FF: 13              INC     DE                  
1400: 1A              LD      A,(DE)              
1401: 9E              SBC     A,(HL)              ; middle byte of the same compare
1402: 23              INC     HL                  
1403: 13              INC     DE                  
1404: 1A              LD      A,(DE)              
1405: 9E              SBC     A,(HL)              ; top byte of the same compare
1406: D8              RET     C                   ; the new key is smaller: its slot is found
1407: C5              PUSH    BC                  
1408: 06 19           LD      B,$19               ; 25 bytes, one whole record

loc_140a:
140A: 4E              LD      C,(HL)              
140B: 1A              LD      A,(DE)              
140C: 77              LD      (HL),A              ; exchange the two records byte by byte
140D: 79              LD      A,C                 
140E: 12              LD      (DE),A              
140F: 2B              DEC     HL                  
1410: 1B              DEC     DE                  
1411: 10 F7           DJNZ    $140A               ; {code.loc_140a}
1413: 01 F5 FF        LD      BC,$FFF5            ; step both keys back to the next-higher pair
1416: 09              ADD     HL,BC               
1417: EB              EX      DE,HL               
1418: 09              ADD     HL,BC               
1419: EB              EX      DE,HL               
141A: C1              POP     BC                  
141B: 10 DF           DJNZ    $13FC               ; {code.loc_13fc} try the record above this one
141D: C9              RET                         

; The game-over sub-state handler. Each frame it redraws the "CREDIT nn" line and counts
; substateTimer down, doing nothing else while that is still running. When it expires
; the screen is blanked, currentPlayer and activePlayerIndex are both cleared, and the
; five playerSlotRecords (stride 0x22) are scanned to decide what comes up next: a
; record holding 1 means player 1 is still up, so compose player 1's screen with the
; flip key set; else a record holding 3 means player 2 is still up, so select player 2
; and compose with flip key 0; else neither is left in play and the machine goes back to
; attract. The scan stops at the FIRST match and which of the five slots matched is
; never read. What the record values 1 and 3 mean in themselves is read back from the
; three outcomes, not established on its own.
selectPlayerScreenOrAttract:
141E: CD 16 06        CALL    $0616               ; {code.drawCreditDisplay} repaint the CREDIT line
1421: DF              RST     $18                 ; hold the game-over screen until it expires
1422: CD 74 08        CALL    $0874               ; {code.clearPlayfieldAndSprites} wipe the screen before composing
1425: 3E 00           LD      A,$00               
1427: 32 0E 60        LD      ($600E),A           ; {hard.workRam+E} clear both bytes of the player index
142A: 32 0D 60        LD      ($600D),A           ; {hard.workRam+D}
142D: 21 1C 61        LD      HL,$611C            ; base of the five player slot records
1430: 11 22 00        LD      DE,$0022            ; record stride
1433: 06 05           LD      B,$05               ; five records to scan
1435: 3E 01           LD      A,$01               ; look for a record still marked player 1

loc_1437:
1437: BE              CP      (HL)                
1438: CA 59 14        JP      Z,$1459             ; {code.configureFlipScreenAndComposeScreen} player 1 is still up
143B: 19              ADD     HL,DE               
143C: 10 F9           DJNZ    $1437               ; {code.loc_1437} on to the next record
143E: 21 1C 61        LD      HL,$611C            ; rescan from the first record
1441: 06 05           LD      B,$05               
1443: 3E 03           LD      A,$03               ; now look for one still marked player 2

loc_1445:
1445: BE              CP      (HL)                
1446: CA 4F 14        JP      Z,$144F             ; {code.selectPlayer2AndComposeScreen} player 2 is still up
1449: 19              ADD     HL,DE               
144A: 10 F9           DJNZ    $1445               ; {code.loc_1445}
144C: C3 75 14        JP      $1475               ; {code.enterAttractMode} neither player is left in play

; The player-2 arm of the game-over scan over the player slot records. Its own
; contribution is exactly "select player 2": write 1 to both currentPlayer and
; activePlayerIndex, which is what makes player 2 the player up -- score awards and the
; per-player context slot key off it. It then delegates to the shared compose tail with
; the key 0. The tail ORs that key into the flip-screen latch, so 0 lets the cabinet
; orientation switch alone decide flip, where the player-1 arm forces flip on with a key
; of 1. The tail then clears substateTimer, advances gameSubstate, and posts the twelve
; screen-draw tasks.
selectPlayer2AndComposeScreen:
144F: 3E 01           LD      A,$01               
1451: 32 0E 60        LD      ($600E),A           ; {hard.workRam+E} player 2 is the active player
1454: 32 0D 60        LD      ($600D),A           ; {hard.workRam+D} player 2 is up; scoring keys off this
1457: 3E 00           LD      A,$00               ; compose with key 0, letting the cabinet decide

; Orient the display for the player who is up, then compose their screen. It is entered
; with a player key -- 1 for the player whose screen is the flipped one, 0 for the other
; -- and writes that key OR'd with dipUpright to the flip-screen latch. So the key alone
; can force the flip on, and an upright cabinet forces it on regardless; only key 0 on a
; cocktail leaves it off, which is the mechanism that mirrors the screen for the second
; player of a cocktail game. It then clears substateTimer (the "wait zero" form, so the
; new sub-state proceeds next frame), advances gameSubstate by one, and posts twelve
; screen-text messages onto the task ring with the argument counting up across a fixed
; range. Which string each argument selects is not established here.
configureFlipScreenAndComposeScreen:
1459: 21 26 60        LD      HL,$6026            ; the cabinet orientation switch
145C: B6              OR      (HL)                ; an upright cabinet forces the flip on too
145D: 32 82 7D        LD      ($7D82),A           ; {hard.flipScreen} orient the display for the player up
1460: 3E 00           LD      A,$00               
1462: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} no wait: the new sub-state runs next frame
1465: 21 0A 60        LD      HL,$600A            
1468: 34              INC     (HL)                ; advance the sub-state selector
1469: 11 0D 03        LD      DE,$030D            ; screen-text task, first of twelve arguments
146C: 06 0C           LD      B,$0C               ; twelve draw messages to post

loc_146e:
146E: CD 9F 30        CALL    $309F               ; {code.enqueueTask} post one screen-text message
1471: 13              INC     DE                  ; next argument in the range
1472: 10 FA           DJNZ    $146E               ; {code.loc_146e}
1474: C9              RET                         

; Put the cabinet back into its idle attract demo. It is the tail of the player-record
; search: that scan looks over the player slot records for one still marked as a game in
; play, and when neither is found it falls through here for four unconditional stores --
; the flip-screen latch := 1, gameState := 1 so the next vblank dispatches the attract
; handler, attract := 1, and gameSubstate := 0. It reads nothing at all, so its effect is
; the same whatever state it is entered from; it is the same attract-entry write set the
; power-on path issues.
enterAttractMode:
1475: 3E 01           LD      A,$01               
1477: 32 82 7D        LD      ($7D82),A           ; {hard.flipScreen} attract display orientation
147A: 32 05 60        LD      ($6005),A           ; {hard.workRam+5} state 1 is attract, dispatched next vblank
147D: 32 07 60        LD      ($6007),A           ; {hard.workRam+7} no credited game in progress
1480: 3E 00           LD      A,$00               
1482: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} clear the sub-dispatch index
1485: C9              RET                         

; The per-frame handler of a sub-state given over to an on-screen item: its position
; walk, its animated sprite, and a point value counting down beside it. substateTimer is
; re-used here as a three-way MODE LATCH, not a countdown. At 0 it does one-shot setup
; -- clear paletteBank0 and paletteBank1, mark running, seed the item's state block
; (value 30, the timers, the position index), point a video cursor at the top of the
; value's column, find the item's row in playerSlotRecords keyed on
; 2*activePlayerIndex+1, and draw it -- then falls through. Running, each frame: tick
; the display timer and on its wrap tick the value and stamp its two digits, a value of
; 0 exiting; step the position from p1Input, bit 7 held running a video-column walk and
; bit 7 clear a frame-divided move through the 0..0x1D wrap; then animate. Whether the
; item is the prize a player collects is NOT settled here.
runBonusItemValueDisplay:
1486: CD 16 06        CALL    $0616               ; {code.drawCreditDisplay} repaint the CREDIT line
1489: 21 09 60        LD      HL,$6009            
148C: 7E              LD      A,(HL)              
148D: A7              AND     A                   ; a three-way mode latch here, not a countdown
148E: C2 DC 14        JP      NZ,$14DC            ; {code.loc_14dc} already running: skip the one-shot setup
1491: 32 86 7D        LD      ($7D86),A           ; {hard.paletteBank0} clear both palette-bank latches
1494: 32 87 7D        LD      ($7D87),A           ; {hard.paletteBank1}
1497: 36 01           LD      (HL),$01            ; mark the display running
1499: 21 30 60        LD      HL,$6030            ; seed the item's state block
149C: 36 0A           LD      (HL),$0A            ; frame divider between position steps
149E: 23              INC     HL                  
149F: 36 00           LD      (HL),$00            ; digit-source toggle
14A1: 23              INC     HL                  
14A2: 36 10           LD      (HL),$10            ; frames to the next sprite animate
14A4: 23              INC     HL                  
14A5: 36 1E           LD      (HL),$1E            ; the point value starts at thirty
14A7: 23              INC     HL                  
14A8: 36 3E           LD      (HL),$3E            ; frames between value ticks
14AA: 23              INC     HL                  
14AB: 36 00           LD      (HL),$00            ; grid position index starts at zero
14AD: 21 E8 75        LD      HL,$75E8            ; top of the value's video column
14B0: 22 36 60        LD      ($6036),HL          ; {hard.workRam+36} park the column cursor there
14B3: 21 1C 61        LD      HL,$611C            ; base of the player slot records
14B6: 3A 0E 60        LD      A,($600E)           ; {hard.workRam+E}
14B9: 07              RLCA                        
14BA: 3C              INC     A                   ; search key is twice the player index plus one
14BB: 4F              LD      C,A                 
14BC: 11 22 00        LD      DE,$0022            ; record stride
14BF: 06 04           LD      B,$04               ; four rows to scan

loc_14c1:
14C1: 7E              LD      A,(HL)              
14C2: B9              CP      C                   
14C3: CA C9 14        JP      Z,$14C9             ; {code.loc_14c9} found the item's row
14C6: 19              ADD     HL,DE               
14C7: 10 F8           DJNZ    $14C1               ; {code.loc_14c1} next row; an unmatched key stops at the last

loc_14c9:
14C9: 22 38 60        LD      ($6038),HL          ; {hard.workRam+38} remember the item's slot row
14CC: 11 F3 FF        LD      DE,$FFF3            ; thirteen bytes back
14CF: 19              ADD     HL,DE               
14D0: 22 3A 60        LD      ($603A),HL          ; {hard.workRam+3A} where the exit copy will land
14D3: 06 00           LD      B,$00               
14D5: 3A 35 60        LD      A,($6035)           ; {hard.workRam+35} the item's grid position
14D8: 4F              LD      C,A                 
14D9: CD FA 15        CALL    $15FA               ; {code.positionBonusItemSprite} draw the item at its cell

loc_14dc:
14DC: 21 34 60        LD      HL,$6034            ; the value's display timer
14DF: 35              DEC     (HL)                
14E0: C2 FC 14        JP      NZ,$14FC            ; {code.loc_14fc} not time to tick the value yet
14E3: 36 3E           LD      (HL),$3E            ; reload the display timer
14E5: 2B              DEC     HL                  ; the point value sits just below
14E6: 35              DEC     (HL)                ; count the value down one
14E7: CA C6 15        JP      Z,$15C6             ; {code.loc_15c6} value exhausted: tear the item down
14EA: 7E              LD      A,(HL)              
14EB: 06 FF           LD      B,$FF               

loc_14ed:
14ED: 04              INC     B                   
14EE: D6 0A           SUB     $0A                 ; split the value into tens and ones
14F0: D2 ED 14        JP      NC,$14ED            ; {code.loc_14ed}
14F3: C6 0A           ADD     A,$0A               ; recover the ones digit
14F5: 32 52 75        LD      ($7552),A           ; {hard.videoRam+152} stamp the ones digit on screen
14F8: 78              LD      A,B                 
14F9: 32 72 75        LD      ($7572),A           ; {hard.videoRam+172} stamp the tens digit on screen

loc_14fc:
14FC: 21 30 60        LD      HL,$6030            ; the position-step divider
14FF: 46              LD      B,(HL)              ; keep this frame's count
1500: 36 0A           LD      (HL),$0A            ; reload the divider
1502: 3A 10 60        LD      A,($6010)           ; {hard.workRam+10} the item's walk is driven by the control word
1505: CB 7F           BIT     7,A                 
1507: C2 46 15        JP      NZ,$1546            ; {code.loc_1546} bit 7 runs the video-column walk instead
150A: E6 03           AND     $03                 ; is any direction held?
150C: C2 14 15        JP      NZ,$1514            ; {code.loc_1514}
150F: 3C              INC     A                   ; idle: reset the divider to one
1510: 77              LD      (HL),A              
1511: C3 8A 15        JP      $158A               ; {code.loc_158a}

loc_1514:
1514: 05              DEC     B                   ; count the divider down
1515: CA 1D 15        JP      Z,$151D             ; {code.loc_151d} expired, so the item moves this frame
1518: 78              LD      A,B                 
1519: 77              LD      (HL),A              ; still counting; no move this frame
151A: C3 8A 15        JP      $158A               ; {code.loc_158a}

loc_151d:
151D: CB 4F           BIT     1,A                 ; bit 1 steps the position backwards
151F: C2 39 15        JP      NZ,$1539            ; {code.loc_1539}
1522: 3A 35 60        LD      A,($6035)           ; {hard.workRam+35} the current grid position
1525: 3C              INC     A                   ; step forward one cell
1526: FE 1E           CP      $1E                 ; past the last cell?
1528: C2 2D 15        JP      NZ,$152D            ; {code.loc_152d}
152B: 3E 00           LD      A,$00               ; wrap round to the first

loc_152d:
152D: 32 35 60        LD      ($6035),A           ; {hard.workRam+35} publish the new position
1530: 4F              LD      C,A                 
1531: 06 00           LD      B,$00               
1533: CD FA 15        CALL    $15FA               ; {code.positionBonusItemSprite} redraw the item at the new cell
1536: C3 8A 15        JP      $158A               ; {code.loc_158a}

loc_1539:
1539: 3A 35 60        LD      A,($6035)           ; {hard.workRam+35}
153C: D6 01           SUB     $01                 ; step back one cell
153E: F2 2D 15        JP      P,$152D             ; {code.loc_152d} still in range
1541: 3E 1D           LD      A,$1D               ; underflowed: wrap to the last cell
1543: C3 2D 15        JP      $152D               ; {code.loc_152d}

loc_1546:
1546: 3A 35 60        LD      A,($6035)           ; {hard.workRam+35} the column walk keys off the same position
1549: FE 1C           CP      $1C                 ; at 0x1c the cursor advances a column
154B: CA 6D 15        JP      Z,$156D             ; {code.loc_156d}
154E: FE 1D           CP      $1D                 
1550: CA C6 15        JP      Z,$15C6             ; {code.loc_15c6} the walk has run out: tear the item down
1553: 2A 36 60        LD      HL,($6036)          ; {hard.workRam+36} the column cursor
1556: 01 88 75        LD      BC,$7588            ; the column floor
1559: A7              AND     A                   
155A: ED 42           SBC     HL,BC               
155C: CA 8A 15        JP      Z,$158A             ; {code.loc_158a} already at the floor: stamp nothing
155F: 09              ADD     HL,BC               ; restore the cursor
1560: C6 11           ADD     A,$11               ; turn the position into its glyph
1562: 77              LD      (HL),A              ; stamp it into the column
1563: 01 E0 FF        LD      BC,$FFE0            ; one tilemap row
1566: 09              ADD     HL,BC               ; retreat the cursor a column

loc_1567:
1567: 22 36 60        LD      ($6036),HL          ; {hard.workRam+36} store the cursor back
156A: C3 8A 15        JP      $158A               ; {code.loc_158a}

loc_156d:
156D: 2A 36 60        LD      HL,($6036)          ; {hard.workRam+36}
1570: 01 20 00        LD      BC,$0020            ; one tilemap row
1573: 09              ADD     HL,BC               ; advance the cursor a column
1574: A7              AND     A                   
1575: 01 08 76        LD      BC,$7608            ; the column ceiling
1578: ED 42           SBC     HL,BC               
157A: C2 86 15        JP      NZ,$1586            ; {code.loc_1586}
157D: 21 E8 75        LD      HL,$75E8            ; past it: wrap to the top of the column

loc_1580:
1580: 3E 10           LD      A,$10               ; a blank tile
1582: 77              LD      (HL),A              ; clear the cell the cursor now sits on
1583: C3 67 15        JP      $1567               ; {code.loc_1567}

loc_1586:
1586: 09              ADD     HL,BC               ; restore the advanced cursor
1587: C3 80 15        JP      $1580               ; {code.loc_1580}

loc_158a:
158A: 21 32 60        LD      HL,$6032            ; the sprite animation timer
158D: 35              DEC     (HL)                
158E: C2 F9 15        JP      NZ,$15F9            ; {code.loc_15f9} nothing to animate yet
1591: 3A 31 60        LD      A,($6031)           ; {hard.workRam+31} which digit source was used last time
1594: A7              AND     A                   
1595: C2 B8 15        JP      NZ,$15B8            ; {code.loc_15b8}
1598: 3E 01           LD      A,$01               
159A: 32 31 60        LD      ($6031),A           ; {hard.workRam+31} flip the source to the canned template
159D: 11 BF 01        LD      DE,$01BF            ; the canned digit template

loc_15a0:
15A0: FD 2A 38 60     LD      IY,($6038)          ; {hard.workRam+38} the item's slot row
15A4: FD 6E 04        LD      L,(IY+$04)          ; the destination cell that row holds
15A7: FD 66 05        LD      H,(IY+$05)          
15AA: E5              PUSH    HL                  
15AB: DD E1           POP     IX                  
15AD: CD 7C 05        CALL    $057C               ; {code.renderBcdColumn} paint the six value digits up the column
15B0: 3E 10           LD      A,$10               
15B2: 32 32 60        LD      ($6032),A           ; {hard.workRam+32} reload the animation timer
15B5: C3 F9 15        JP      $15F9               ; {code.loc_15f9}

loc_15b8:
15B8: AF              XOR     A                   
15B9: 32 31 60        LD      ($6031),A           ; {hard.workRam+31} flip the source back to the slot record
15BC: ED 5B 38 60     LD      DE,($6038)          ; {hard.workRam+38}
15C0: 13              INC     DE                  ; the digits start three bytes into it
15C1: 13              INC     DE                  
15C2: 13              INC     DE                  
15C3: C3 A0 15        JP      $15A0               ; {code.loc_15a0}

loc_15c6:
15C6: ED 5B 38 60     LD      DE,($6038)          ; {hard.workRam+38} the item's slot row
15CA: AF              XOR     A                   
15CB: 12              LD      (DE),A              ; clear the item's slot
15CC: 21 09 60        LD      HL,$6009            
15CF: 36 80           LD      (HL),$80            ; mark the display done
15D1: 23              INC     HL                  
15D2: 35              DEC     (HL)                ; step the sub-state back one, ending the phase
15D3: 06 0C           LD      B,$0C               ; twelve cells to copy
15D5: 21 E8 75        LD      HL,$75E8            ; from the top of the value's column
15D8: FD 2A 3A 60     LD      IY,($603A)          ; {hard.workRam+3A} into the item's slot record
15DC: 11 E0 FF        LD      DE,$FFE0            ; walking one tilemap row up each time

loc_15df:
15DF: 7E              LD      A,(HL)              
15E0: FD 77 00        LD      (IY+$00),A          
15E3: FD 23           INC     IY                  
15E5: 19              ADD     HL,DE               
15E6: 10 F7           DJNZ    $15DF               ; {code.loc_15df}
15E8: 06 05           LD      B,$05               ; five follow-up tasks
15EA: 11 14 03        LD      DE,$0314            ; first task argument

loc_15ed:
15ED: CD 9F 30        CALL    $309F               ; {code.enqueueTask} post one
15F0: 13              INC     DE                  
15F1: 10 FA           DJNZ    $15ED               ; {code.loc_15ed}
15F3: 11 1A 03        LD      DE,$031A            ; and one more task after them
15F6: CD 9F 30        CALL    $309F               ; {code.enqueueTask}

loc_15f9:
15F9: C9              RET                         

; Redraw the on-board prize sprite at its current grid cell -- once at spawn, then after
; every position step. The item's position index runs 0..0x1d over a stored grid of
; thirty two-byte (X, Y) entries laid out as 10 columns by 3 rows, X stepping 0x10
; across a row and Y taking 0x5C / 0x6C / 0x7C down them. The indexed pair is stamped
; into sprite record 29: +0 X and +3 Y from the table, +1 the fixed glyph 0x72, +2 the
; fixed attribute 0x0C. The vblank DMA carries that record to sprite RAM.
positionBonusItemSprite:
15FA: D5              PUSH    DE                  
15FB: E5              PUSH    HL                  
15FC: CB 21           SLA     C                   ; two bytes per grid entry
15FE: 21 0F 36        LD      HL,$360F            ; the stored 30-cell position grid
1601: 09              ADD     HL,BC               ; index the entry for this cell
1602: EB              EX      DE,HL               
1603: 21 74 69        LD      HL,$6974            ; the item's sprite record
1606: 1A              LD      A,(DE)              
1607: 13              INC     DE                  
1608: 77              LD      (HL),A              ; X from the grid entry
1609: 23              INC     HL                  
160A: 36 72           LD      (HL),$72            ; the item's tile code
160C: 23              INC     HL                  
160D: 36 0C           LD      (HL),$0C            ; its colour attribute
160F: 23              INC     HL                  
1610: 1A              LD      A,(DE)              
1611: 77              LD      (HL),A              ; Y from the grid entry
1612: E1              POP     HL                  
1613: D1              POP     DE                  
1614: C9              RET                         

; The top dispatcher for the board-advance state, keyed on the board type. It first parks
; the moving sprite groups off-screen, then routes boardAdvanceStep to the handler for
; the current board: bit 0 of board set (25m or 75m) vectors through a 6-entry table of
; targets; bit 1 set (50m) through a 5-entry table; neither bit (100m) falls through to
; the rivet-board interlude frame, which runs the effect-sprite machine first and then
; dispatches its own table. The "HOW HIGH CAN YOU GET?" screen is painted from the
; board-setup state, not from this one, and nothing here establishes what the arms
; depict.
dispatchBoardClearedInterlude:
1615: CD BD 30        CALL    $30BD               ; {code.clearSpriteColumns} park the moving sprite rows off-screen
1618: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} route on the board just cleared
161B: 0F              RRCA                        ; bit 0 marks 25m and 75m
161C: D2 2F 16        JP      NC,$162F            ; {code.loc_162f}
161F: 3A 88 63        LD      A,($6388)           ; {hard.workRam+388} which step of the interlude this frame is
1622: EF              RST     $28                 ; vector through the six-entry table below

; ---- $1623-$162E: jump table ----
1623: 54 16 70 16 8A 16 32 17 57 17 8E 17

loc_162f:
162F: 0F              RRCA                        ; bit 1 marks the 50m board
1630: D2 41 16        JP      NC,$1641            ; {code.runRivetBoardInterludeFrame} neither bit set means 100m
1633: 3A 88 63        LD      A,($6388)           ; {hard.workRam+388} which step of the interlude this frame is
1636: EF              RST     $28                 ; vector through the five-entry table below

; ---- $1637-$1640: jump table ----
1637: A3 16 BB 16 32 17 57 17 8E 17

; The rivet board's arm of the board-cleared interlude, run once a frame. It chains two
; independent things in order: one frame of the effect-sprite state machine -- a four-way
; router on effectState that either idles, arms and spawns the effect, or counts it down
; -- and then the rivet-board interlude dispatch, which reads boardAdvanceStep and
; vectors to the handler that paints or animates that step. Each callee reads its own
; inputs from memory, so nothing is threaded between them here.
runRivetBoardInterludeFrame:
1641: CD BD 1D        CALL    $1DBD               ; {code.dispatchEffectState} one frame of the effect-sprite machine

dispatchRivetBoardInterludeStep:
1644: 3A 88 63        LD      A,($6388)           ; {hard.workRam+388} which step of the rivet finale runs now
1647: EF              RST     $28                 ; vector through the six-entry table below

; ---- $1648-$1653: jump table ----
1648: B6 17 69 30 39 18 6F 18 80 18 C6 18

; Step 0 of the interlude that plays once a board is cleared, on the odd boards, so it
; runs exactly once. It spawns the opening tableau -- sound silenced, the whole-heart
; sprite record and its companion blink code seeded, three tilemap cells blanked, the
; sound-priority pair set -- then stages the scene's first pose by copying a fixed
; 40-byte, ten-record template into spriteObjBlock, arms a 32-frame pose hold in
; substateTimer, and falls into the shared tail that steps the sequence on and, on 25m
; only, raises all ten records by 4 pixels. The template is one large figure rather than
; a row of props: four of its ten records are parked off to the side carrying the blank
; sprite code, and the six that draw sit in a single block roughly 40 by 32 pixels.
; "Kong" is read off the drawn figure; nothing here identifies whose figure is carried
; away, as the other character's records were never separated out.
beginKongRecaptureInterlude:
1654: CD 08 17        CALL    $1708               ; {code.spawnInterludeHeart} silence sound, put the heart on screen
1657: 21 5C 38        LD      HL,$385C            ; the scene's first ten-record pose template
165A: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock} stamp it over the object block
165D: 3E 20           LD      A,$20               
165F: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} hold the pose 32 frames

; The shared tail two of the board-cleared interlude's step handlers end in.
; boardAdvanceStep is incremented unconditionally, whichever board is being played.
; Then, on the 25m board only, 4 is subtracted from the Y byte of all ten spriteObjBlock
; records at once, a strided walk four bytes apart. A smaller Y is higher up the screen,
; so the whole staged figure rises 4 pixels. The subtraction is 8-bit and wraps, and it
; touches only the Y column -- every record's X, sprite code and attribute are left
; exactly as staged.
advanceInterludeStepAndLiftKongFigure:
1662: 21 88 63        LD      HL,$6388            ; the interlude's step selector
1665: 34              INC     (HL)                ; move the sequence on, whatever the board
1666: 3E 01           LD      A,$01               ; mask bit 0: the 25m board only
1668: F7              RST     $30                 ; board gate; other boards stop here
1669: 21 0B 69        LD      HL,$690B            ; the Y byte of sprite-object record 0
166C: 0E FC           LD      C,$FC               ; minus four
166E: FF              RST     $38                 ; raise all ten records four pixels
166F: C9              RET                         

; One timer-gated step of the board-cleared interlude on the odd boards, 25m and 75m:
; hold the current pose for a fixed number of frames, then stage the next one. Every
; frame it ticks substateTimer and returns. On the single expiry frame it copies this
; step's 40-byte sprite-object template over spriteObjBlock, re-arms substateTimer to
; 0x20 to hold the new pose 32 frames, advances boardAdvanceStep, and -- on 75m only --
; adds +4 to the Y column of all ten records, dropping the whole figure 4 pixels. What is
; in the bytes is that the new template's silhouette is wider (48 px against 40) and its
; records sit 4 px higher; reading a particular pose into that is a reading of the
; screen.
stageNextKongPoseWhenHoldExpires:
1670: DF              RST     $18                 ; hold the current pose until the timer expires
1671: 21 32 39        LD      HL,$3932            ; this step's ten-record pose template
1674: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock} swap it in over the staged pose
1677: 3E 20           LD      A,$20               
1679: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} hold the new pose 32 frames
167C: 21 88 63        LD      HL,$6388            
167F: 34              INC     (HL)                ; advance the interlude's step selector
1680: 3E 04           LD      A,$04               ; mask bit 2: the 75m board only
1682: F7              RST     $30                 ; board gate; other boards stop here
1683: 21 0B 69        LD      HL,$690B            ; the Y byte of sprite-object record 0
1686: 0E 04           LD      C,$04               ; plus four
1688: FF              RST     $38                 ; drop all ten records four pixels
1689: C9              RET                         

; A timer-gated step of the board-cleared interlude: hold the pose, then re-seed the
; sprite-object block from a fixed template. Every frame it ticks substateTimer and
; returns while it is still counting, so the pose is HELD. On the single expiry frame it
; copies a 40-byte template -- ten 4-byte sprite records -- over spriteObjBlock,
; re-stamps record 1's X back to 0x66, and clears three bytes: the X of records 7 and 9,
; parking those two sprites for the whole of the next step, and the byte the next step
; uses as its climb animation phase counter. Zeroing that counter is what makes this the
; frame that STAGES a climb rather than one that animates it. It then tails into the
; shared board-advance tail, which steps the interlude's step selector, runs the
; per-board gate, and on 25m subtracts 4 from field 3 of every sprite-object record.
stageKongClimbPose:
168A: DF              RST     $18                 ; hold the pose until the timer expires
168B: 21 8C 38        LD      HL,$388C            ; this step's ten-record template
168E: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock} stamp it over the object block
1691: 3E 66           LD      A,$66               
1693: 32 0C 69        LD      ($690C),A           ; {hard.workRam+90C} record 1's X back to its fixed value
1696: AF              XOR     A                   
1697: 32 24 69        LD      ($6924),A           ; {hard.workRam+924} park record 7 for the whole next step
169A: 32 2C 69        LD      ($692C),A           ; {hard.workRam+92C} park record 9 with it
169D: 32 AF 62        LD      ($62AF),A           ; {hard.workRam+2AF} zero the counter the climb animates on
16A0: C3 62 16        JP      $1662               ; {code.advanceInterludeStepAndLiftKongFigure} the shared step tail

; Step 0 of the even-board branch of the same board-cleared interlude. It spawns the
; opening tableau, then RE-ANCHORS the figure: record 2's CURRENT X is read out of
; spriteObjBlock BEFORE the copy overwrites that byte, the fixed ten-record figure
; template is stamped over the block, and the difference between that old X and the
; template's own anchor is added into the X of all ten records -- so record 2 lands back
; on its previous X and the whole figure is carried with it. The re-anchor is here and
; not on the odd boards because a per-frame slide keeps shifting this same X column
; during 50m play, so a raw stamp would teleport the figure. Then boardAdvanceStep is
; bumped so the next frame runs the next step. Which record of the ten is which is not
; established; the name says who is re-stamped.
begin50mKongRecaptureInterlude:
16A3: CD 08 17        CALL    $1708               ; {code.spawnInterludeHeart} silence sound, put the heart on screen
16A6: 3A 10 69        LD      A,($6910)           ; {hard.workRam+910} record 2's current X, read before the copy
16A9: D6 3B           SUB     $3B                 ; how far it sits from the template's anchor
16AB: 21 5C 38        LD      HL,$385C            ; the fixed ten-record figure template
16AE: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock} stamp it over the object block
16B1: 21 08 69        LD      HL,$6908            ; the X byte of sprite-object record 0
16B4: 4F              LD      C,A                 
16B5: FF              RST     $38                 ; carry all ten records back to that X
16B6: 21 88 63        LD      HL,$6388            
16B9: 34              INC     (HL)                ; move the sequence on
16BA: C9              RET                         

; The first-stage dispatcher for a horizontally moving group of ten sprites that walks
; back and forth between two rails. It runs first every frame and clears
; m50Obj1ReverseTimer, which is the "keep travelling" default: on an even frame the
; motion tick then decrements it from 0 to 0xFF, which is non-zero, so no reversal is
; taken. Only the bounce arm writes 1 there, so that the same decrement lands on ZERO --
; the case that reloads the period and REVERSES -- in that very frame. It then reads
; sprite record 2's X and the published signed step m50Obj1Step and routes: X at or
; above 90 has reached the rail, so hand to the second-stage dispatcher; X below the
; rail with a NEGATIVE step schedules a reversal and slides, which is the bounce; X
; below with a positive step just slides. A reversal is scheduled only while the group
; is still travelling INTO the edge nearest it.
dispatchKongWalkFrame:
16BB: AF              XOR     A                   
16BC: 32 A0 62        LD      ($62A0),A           ; {hard.workRam+2A0} clear the reversal flag: keep going
16BF: 3A A3 63        LD      A,($63A3)           ; {hard.workRam+3A3} the published signed per-frame step
16C2: 4F              LD      C,A                 
16C3: 3A 10 69        LD      A,($6910)           ; {hard.workRam+910} record 2's X, the group's leading edge
16C6: FE 5A           CP      $5A                 ; has it reached the rail region?
16C8: D2 E1 16        JP      NC,$16E1            ; {code.endKongWalkAndAdvanceInterlude} at the rail region
16CB: CB 79           BIT     7,C                 ; is the step heading into the near edge?
16CD: CA D5 16        JP      Z,$16D5             ; {code.stepKongWalk} heading away, so just slide

loc_16d0:
16D0: 3E 01           LD      A,$01               
16D2: 32 A0 62        LD      ($62A0),A           ; {hard.workRam+2A0} schedule a reversal on the next tick

; Slide the interlude's ten-record figure one step along X. Three acts: advance the first
; timed board object -- ticking its even-frame countdown, reloading it and reversing its
; step direction on the decrement that REACHES zero, republishing its signed per-frame
; step, and every 32nd frame advancing its mirrored sprite-animation pair -- take that
; freshly published step, and add it to the X field of all ten records of spriteObjBlock.
; The step is 0 on even frames, so the figure holds still while the object's own state
; advances, and slides one pixel either way on odd frames. The block it slides is the
; figure the preceding interlude step stamped there; nothing in the motion identifies who
; that figure is.
stepKongWalk:
16D5: CD 02 26        CALL    $2602               ; {code.loc_2602} advance the object's timers and direction
16D8: 3A A3 63        LD      A,($63A3)           ; {hard.workRam+3A3} take the freshly published step
16DB: 4F              LD      C,A                 
16DC: 21 08 69        LD      HL,$6908            ; the X byte of sprite-object record 0
16DF: FF              RST     $38                 ; slide all ten records one step along X
16E0: C9              RET                         

; The second stage of the pair that walks a horizontally-moving group of ten sprites back
; and forth during a between-boards interlude. The first stage runs every frame and, once
; the group's leading record X has climbed to the rail region, hands that X and the
; object's published signed per-frame step over here. Three outcomes. X still short of
; 93: the group has arrived, so reinitialise its object block -- recopy the sprite
; template, clear the per-object scratch -- and advance the interlude's step counter. X
; at or past 93 with a POSITIVE step, still travelling into the rail: schedule a
; direction reversal for the next tick and slide this frame, which is the bounce. X at or
; past 93 with a NEGATIVE step, already moving away: just slide. This stage touches no
; memory; it tests its two inputs and tail-calls the chosen handler.
endKongWalkAndAdvanceInterlude:
16E1: FE 5D           CP      $5D                 ; short of the rail threshold?
16E3: DA EE 16        JP      C,$16EE             ; {code.reloadObjectBlockAndAdvanceStep} arrived, so reinitialise
16E6: CB 79           BIT     7,C                 ; still travelling into the rail?
16E8: CA D0 16        JP      Z,$16D0             ; {code.loc_16d0} yes: bounce off it
16EB: C3 D5 16        JP      $16D5               ; {code.stepKongWalk} already moving away, just slide

; One phase of the board-cleared interlude. It reloads the 40-byte (ten-record)
; sprite-object block from its stored template -- the same template the opening climb
; cutscene loads -- then patches three record field-0 bytes AFTER the copy: record 1 <-
; 0x66, records 7 and 9 <- 0. Each target sits inside the block the copy just filled, so
; the copy must run first or the patch is lost, and none of the three template bytes
; already holds the patched value. It then clears a board-object bookkeeping byte and
; advances boardAdvanceStep. A sibling handler does the identical reload and patch under
; a timer gate and a different tail.
reloadObjectBlockAndAdvanceStep:
16EE: 21 8C 38        LD      HL,$388C            ; the stored ten-record template
16F1: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock} reload the sprite-object block
16F4: 3E 66           LD      A,$66               
16F6: 32 0C 69        LD      ($690C),A           ; {hard.workRam+90C} patch record 1's X after the copy
16F9: AF              XOR     A                   
16FA: 32 24 69        LD      ($6924),A           ; {hard.workRam+924} park record 7
16FD: 32 2C 69        LD      ($692C),A           ; {hard.workRam+92C} park record 9
1700: 32 AF 62        LD      ($62AF),A           ; {hard.workRam+2AF} clear the board-object bookkeeping byte
1703: 21 88 63        LD      HL,$6388            
1706: 34              INC     (HL)                ; advance the interlude's step selector
1707: C9              RET                         

; The board-cleared interlude's opening tableau. Straight-line and input-independent --
; it reads no memory and every store is a constant. It zeroes every sound output and its
; work RAM shadow, seeds a fixed 4-byte record in spriteBuffer to [X 0x80, code 0x76,
; attribute 0x09, Y 0x20] -- code 0x76 is the whole heart -- seeds the blink sprite's
; code byte to 0x13, the byte whose bit 7 the colour cycle toggles to make it blink,
; lays the descending codes 0x10 / 0x0F / 0x0E down three cells of one tilemap column,
; and finally sets sndPriority and sndPriorityFrames to 7 and 3, re-writing what the
; silencing zeroed. All three of those tile codes are blank glyphs, so that step BLANKS
; three cells rather than drawing anything; what it clears off the screen is not
; established.
spawnInterludeHeart:
1708: CD 1C 01        CALL    $011C               ; {code.silenceSound} zero every sound output before the scene
170B: 21 20 6A        LD      HL,$6A20            ; the heart's sprite record
170E: 36 80           LD      (HL),$80            ; X
1710: 23              INC     HL                  
1711: 36 76           LD      (HL),$76            ; the whole-heart tile code
1713: 23              INC     HL                  
1714: 36 09           LD      (HL),$09            ; colour attribute
1716: 23              INC     HL                  
1717: 36 20           LD      (HL),$20            ; Y
1719: 21 05 69        LD      HL,$6905            ; the blink sprite's code byte
171C: 36 13           LD      (HL),$13            ; the colour cycle toggles bit 7 to blink it
171E: 21 C4 75        LD      HL,$75C4            ; one tilemap column
1721: 11 20 00        LD      DE,$0020            ; one row apart
1724: 3E 10           LD      A,$10               ; blank tiles, so the three cells are cleared
1726: CD 14 05        CALL    $0514               ; {code.fillDescendingColumn} write 0x10, 0x0F and 0x0E down them
1729: 21 8A 60        LD      HL,$608A            ; the sound-priority pair
172C: 36 07           LD      (HL),$07            ; restore the priority the silencing zeroed
172E: 23              INC     HL                  
172F: 36 03           LD      (HL),$03            ; hold it three frames
1731: C9              RET                         

; Hold the interlude while the figure climbs, then break the heart and move the sequence
; on. Where its sibling steps hold on a frame timer, this one holds on a POSITION. It
; ticks the sprite-object block's animation, which on every eighth call scrolls the whole
; ten-record group up four pixels and animates its code bytes, and holds while the probed
; record's Y is still at or below the top threshold -- so most frames just tick the phase
; counter. Once that record clears the threshold the step finishes: park three sprite X
; bytes at zero, restore two more to their template X (an earlier step parked them for
; the climb), step the heart record's sprite code on by one -- the same shape with a
; jagged split through it -- and advance boardAdvanceStep. That one figure climbs and the
; heart breaks as it clears the top; which records of the block belong to which character
; is not established.
climbKongFigureAndBreakHeart:
1732: CD 6F 30        CALL    $306F               ; {code.animateSpriteObjectBlock} every eighth call it climbs 4px
1735: 3A 13 69        LD      A,($6913)           ; {hard.workRam+913} the probed record's Y
1738: FE 2C           CP      $2C                 ; has it cleared the top threshold?
173A: D0              RET     NC                  ; still climbing: hold this step
173B: AF              XOR     A                   
173C: 32 00 69        LD      ($6900),A           ; {hard.workRam+900} park a sprite X at the left edge
173F: 32 04 69        LD      ($6904),A           ; {hard.workRam+904} and its neighbour
1742: 32 0C 69        LD      ($690C),A           ; {hard.workRam+90C} and object record 1's X
1745: 3E 6B           LD      A,$6B               
1747: 32 24 69        LD      ($6924),A           ; {hard.workRam+924} record 7 back to its template X
174A: 3D              DEC     A                   
174B: 32 2C 69        LD      ($692C),A           ; {hard.workRam+92C} record 9 back to its template X
174E: 21 21 6A        LD      HL,$6A21            ; the heart's tile code
1751: 34              INC     (HL)                ; step it on one: the heart breaks
1752: 21 88 63        LD      HL,$6388            
1755: 34              INC     (HL)                ; move the interlude on
1756: C9              RET                         

; One arm of the board-advance sequence: march the sprite-object block off the top of the
; screen and, once it is empty, move the sequence on. Dispatched from inside the vblank
; interrupt while a board is being torn down. Each frame it runs the block animation --
; every eighth call, scroll the whole ten-record block up 4px and flip a few records --
; then zeroes the X of any record that has risen above the top line (Y < 0x19), then
; scans all ten record X bytes for zero. If a slot is still occupied the arm aborts and
; tries again next frame with boardAdvanceStep left alone. If every slot is clear it arms
; substateTimer to 64 frames and increments boardAdvanceStep, so the next interrupt
; dispatches the following arm.
advanceBoardStepWhenSpritesCleared:
1757: CD 6F 30        CALL    $306F               ; {code.animateSpriteObjectBlock} march the block up the screen
175A: CD 6C 17        CALL    $176C               ; {code.cullSpriteObjectsAtTop} park records risen off the top
175D: 23              INC     HL                  ; bump the returned pointer and stride into shape
175E: 13              INC     DE                  
175F: CD 83 17        CALL    $1783               ; {code.allSlotsClear} abandon the frame unless all ten are clear
1762: 3E 40           LD      A,$40               
1764: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} dwell 64 frames before the next sub-state
1767: 21 88 63        LD      HL,$6388            
176A: 34              INC     (HL)                ; step to the next arm of the sequence
176B: C9              RET                         

; Sweep the ten 4-byte spriteObjBlock records and, for each whose Y has risen above the
; top line (smaller Y is higher on this screen), zero that record's X, parking the
; sprite at the left edge. Nothing else in any record is touched and each is decided on
; its own, so the pass is order-independent. It also leaves behind a scan pointer and a
; record stride each ONE SHORT of the value that will be used: the caller bumps both by
; one before handing them to the follow-up scan that decides whether every sprite has
; now been swept off.
cullSpriteObjectsAtTop:
176C: 11 03 00        LD      DE,$0003            
176F: 21 2F 69        LD      HL,$692F            ; the Y byte of the last record
1772: 06 0A           LD      B,$0A               ; ten records to sweep

loc_1774:
1774: A7              AND     A                   
1775: 7E              LD      A,(HL)              ; read this record's Y
1776: ED 52           SBC     HL,DE               ; back up to the record's X
1778: FE 19           CP      $19                 ; has it risen above the top line?
177A: D2 7F 17        JP      NC,$177F            ; {code.loc_177f}
177D: 36 00           LD      (HL),$00            ; park it at the left edge

loc_177f:
177F: 2B              DEC     HL                  ; on to the record below
1780: 10 F2           DJNZ    $1774               ; {code.loc_1774}
1782: C9              RET                         

; Are ten object slots all empty? Walks ten cells from a caller-given base at a
; caller-given stride and reports whether every one is zero, stopping at the first
; non-zero. Only the count, ten, is hard-wired. Its caller drives it over spriteObjBlock
; with a stride of four, so in practice it answers "are all ten object sprites cleared?"
; before arming the next interlude phase. On a non-zero cell it discards the caller's
; return address and returns past it, aborting the caller mid-flow.
allSlotsClear:
1783: 06 0A           LD      B,$0A               ; ten slots to check

loc_1785:
1785: 7E              LD      A,(HL)              
1786: A7              AND     A                   
1787: C2 26 00        JP      NZ,$0026            ; {code.loc_0026} an occupied slot aborts the caller
178A: 19              ADD     HL,DE               ; next slot
178B: 10 F8           DJNZ    $1785               ; {code.loc_1785}
178D: C9              RET                         ; all ten empty

; Move the board order on and enter the "HOW HIGH CAN YOU GET?" interlude that introduces
; the next board. It ticks substateTimer and does nothing at all while that is still
; running. On the frame it expires, it walks boardSeqPtr one entry forward through the
; board-order table and reads the board waiting there; the table ends in a terminator
; byte, and reaching it puts the pointer back to the start of the repeating group rather
; than stopping, which is how the game keeps handing out boards forever once a player is
; past the fixed opening order. The result is published to board. It then posts a
; deferred task, clears boardAdvanceStep so the next board-cleared run starts from its
; own first step, and arms a 48-frame wait before the how-high interlude.
advanceToNextBoard:
178E: DF              RST     $18                 ; hold until the sub-state timer expires
178F: 2A 2A 62        LD      HL,($622A)          ; {hard.workRam+22A} the board-order pointer
1792: 23              INC     HL                  ; step one entry forward
1793: 7E              LD      A,(HL)              ; the board waiting there
1794: FE 7F           CP      $7F                 ; the table's end marker?
1796: C2 9D 17        JP      NZ,$179D            ; {code.loc_179d}
1799: 21 73 3A        LD      HL,$3A73            ; wrap to the start of the repeating group
179C: 7E              LD      A,(HL)              ; and take the board there instead

loc_179d:
179D: 22 2A 62        LD      ($622A),HL          ; {hard.workRam+22A} store the advanced pointer
17A0: 32 27 62        LD      ($6227),A           ; {hard.workRam+227} publish the board coming up
17A3: 11 00 05        LD      DE,$0500            
17A6: CD 9F 30        CALL    $309F               ; {code.enqueueTask} post its deferred task
17A9: AF              XOR     A                   
17AA: 32 88 63        LD      ($6388),A           ; {hard.workRam+388} the next cleared-board run starts at 0
17AD: 21 09 60        LD      HL,$6009            
17B0: 36 30           LD      (HL),$30            ; wait 48 frames
17B2: 23              INC     HL                  
17B3: 36 08           LD      (HL),$08            ; then the how-high interlude sub-state
17B5: C9              RET                         

loc_17b6:
17B6: 00              NOP                         
17B7: CD 1C 01        CALL    $011C               ; {code.silenceSound} cut every sound line before the scene
17BA: 21 8A 60        LD      HL,$608A            ; the sound-priority pair
17BD: 36 0E           LD      (HL),$0E            ; the tune this scene opens with
17BF: 23              INC     HL                  
17C0: 36 03           LD      (HL),$03            ; hold it three frames
17C2: 3E 10           LD      A,$10               ; the blank code the two runs count down from
17C4: 11 20 00        LD      DE,$0020            ; one tilemap row between cells
17C7: 21 23 76        LD      HL,$7623            ; three cells near the top of the screen
17CA: CD 14 05        CALL    $0514               ; {code.fillDescendingColumn} blank them
17CD: 21 83 75        LD      HL,$7583            ; three more, the codes carrying on down from the first run
17D0: CD 14 05        CALL    $0514               ; {code.fillDescendingColumn}
17D3: 21 DA 76        LD      HL,$76DA            ; the first of four bands -- the board's structure is erased
17D6: CD 26 18        CALL    $1826               ; {code.fillTileBlock}
17D9: 11 47 3A        LD      DE,$3A47            ; a bare girder low on the screen
17DC: CD A7 0D        CALL    $0DA7               ; {code.drawBoardLayout}
17DF: 21 D5 76        LD      HL,$76D5            ; the next band up
17E2: CD 26 18        CALL    $1826               ; {code.fillTileBlock}
17E5: 11 4D 3A        LD      DE,$3A4D            ; a second girder eight pixels above it
17E8: CD A7 0D        CALL    $0DA7               ; {code.drawBoardLayout}
17EB: 21 D0 76        LD      HL,$76D0            ; and the next
17EE: CD 26 18        CALL    $1826               ; {code.fillTileBlock}
17F1: 11 53 3A        LD      DE,$3A53            ; a third girder
17F4: CD A7 0D        CALL    $0DA7               ; {code.drawBoardLayout}
17F7: 21 CB 76        LD      HL,$76CB            ; and the last
17FA: CD 26 18        CALL    $1826               ; {code.fillTileBlock}
17FD: 11 59 3A        LD      DE,$3A59            ; a fourth: the top of the heap Kong lands on
1800: CD A7 0D        CALL    $0DA7               ; {code.drawBoardLayout}
1803: 21 5C 38        LD      HL,$385C            ; Kong's ten-record figure, as the board build stamps it
1806: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock}
1809: 21 08 69        LD      HL,$6908            ; the X byte of sprite-object record 0
180C: 0E 44           LD      C,$44               
180E: FF              RST     $38                 ; carry all ten records to where the board build puts them
180F: 21 05 69        LD      HL,$6905            ; the blink sprite's code byte
1812: 36 13           LD      (HL),$13            ; the code the colour cycle toggles to blink it
1814: 3E 20           LD      A,$20               
1816: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} hold the tableau 32 frames
1819: 3E 80           LD      A,$80               
181B: 32 90 63        LD      ($6390),A           ; {hard.workRam+390} seed the counter the next step animates on
181E: 21 88 63        LD      HL,$6388            
1821: 34              INC     (HL)                ; move the finale on a step
1822: 22 C0 63        LD      ($63C0),HL          ; {hard.workRam+3C0} aim the shared timed advancer at that byte
1825: C9              RET                         

; Stamp a fixed 5-wide by 14-tall block of tile 0x10 into the tilemap at the caller's
; address. Each row writes five cells and then steps the pointer back by 0x25 -- a net
; -0x20, one tilemap row up at the same left edge. The fill value, the width, the height
; and the row step are all constants baked in; the destination address is the only input,
; and no memory is read at all. Used by the game-over and player-switch render sequences
; and by the board-start intro setup.
fillTileBlock:
1826: 11 DB FF        LD      DE,$FFDB            ; row step: back to the left edge one row up
1829: 0E 0E           LD      C,$0E               ; fourteen rows tall
182B: 3E 10           LD      A,$10               ; the blank tile to stamp

loc_182d:
182D: 06 05           LD      B,$05               ; five cells across

loc_182f:
182F: 77              LD      (HL),A              
1830: 23              INC     HL                  
1831: 10 FC           DJNZ    $182F               ; {code.loc_182f}
1833: 19              ADD     HL,DE               ; step to the next row up
1834: 0D              DEC     C                   
1835: C2 2D 18        JP      NZ,$182D            ; {code.loc_182d}
1838: C9              RET                         

stepSpriteAnimationSequence:
1839: 21 90 63        LD      HL,$6390            ; the scene's frame counter, seeded to 0x80 by the opening step
183C: 34              INC     (HL)                
183D: CA 59 18        JP      Z,$1859             ; {code.loc_1859} it wraps 128 frames later: the pose is done
1840: 7E              LD      A,(HL)              
1841: E6 07           AND     $07                 ; only every eighth frame changes the pose
1843: C0              RET     NZ                  
1844: 11 CF 39        LD      DE,$39CF            ; one of two poses
1847: CB 5E           BIT     3,(HL)              ; bit 3 turns over every eight frames, so the two alternate
1849: 20 03           JR      NZ,$184E            ; {code.loc_184e}
184B: 11 F7 39        LD      DE,$39F7            ; the other pose

loc_184e:
184E: EB              EX      DE,HL               
184F: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock} swap it in
1852: 21 08 69        LD      HL,$6908            
1855: 0E 44           LD      C,$44               
1857: FF              RST     $38                 ; and shift the fresh copy back into place
1858: C9              RET                         

loc_1859:
1859: 21 5C 38        LD      HL,$385C            ; back to the pose the scene opened with
185C: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock}
185F: 21 08 69        LD      HL,$6908            
1862: 0E 44           LD      C,$44               
1864: FF              RST     $38                 ; shifted into place as before
1865: 3E 20           LD      A,$20               
1867: 32 09 60        LD      ($6009),A           ; {hard.workRam+9} hold it 32 frames
186A: 21 88 63        LD      HL,$6388            
186D: 34              INC     (HL)                ; then move the finale on
186E: C9              RET                         

loc_186f:
186F: DF              RST     $18                 ; hold the pose until the frame timer expires
1870: 21 1F 3A        LD      HL,$3A1F            ; the same figure inverted and 0x20 lower: Kong topples
1873: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock}
1876: 3E 03           LD      A,$03               
1878: 32 84 60        LD      ($6084),A           ; {hard.workRam+84} cue the falling sound for three frames
187B: 21 88 63        LD      HL,$6388            
187E: 34              INC     (HL)                ; move the finale on to the fall itself
187F: C9              RET                         

loc_1880:
1880: 21 0B 69        LD      HL,$690B            ; the Y byte of sprite-object record 0
1883: 0E 01           LD      C,$01               
1885: FF              RST     $38                 ; drop the whole figure a pixel: the fall, one pixel a frame
1886: 3A 1B 69        LD      A,($691B)           ; {hard.workRam+91B} record 4's Y, the probe for the landing
1889: FE D0           CP      $D0                 ; the row it lands on
188B: C0              RET     NZ                  ; still falling: nothing more this frame
188C: 3E 20           LD      A,$20               
188E: 32 19 69        LD      ($6919),A           ; {hard.workRam+919} record 4 takes its landed sprite code
1891: 21 24 6A        LD      HL,$6A24            ; a sprite record at the foot of the screen
1894: 36 7F           LD      (HL),$7F            ; X, mid-screen
1896: 2C              INC     L                   
1897: 36 39           LD      (HL),$39            ; its tile code
1899: 2C              INC     L                   
189A: 36 01           LD      (HL),$01            ; colour attribute
189C: 2C              INC     L                   
189D: 36 D8           LD      (HL),$D8            ; Y, level with the topmost girder of the heap
189F: 21 C6 76        LD      HL,$76C6            ; wipe the last band of playfield left standing
18A2: CD 26 18        CALL    $1826               ; {code.fillTileBlock}
18A5: 11 5F 3A        LD      DE,$3A5F            ; and draw the girder the scene ends on
18A8: CD A7 0D        CALL    $0DA7               ; {code.drawBoardLayout}
18AB: 11 04 00        LD      DE,$0004            
18AE: 01 28 02        LD      BC,$0228            ; two records, plus 0x28
18B1: 21 03 69        LD      HL,$6903            ; the Y byte of sprite records 0 and 1
18B4: CD 3D 00        CALL    $003D               ; {code.addStrided} drop that pair onto the new girder
18B7: 3E 00           LD      A,$00               
18B9: 32 AF 62        LD      ($62AF),A           ; {hard.workRam+2AF} zero the counter the last step winds down
18BC: 3E 03           LD      A,$03               
18BE: 32 82 60        LD      ($6082),A           ; {hard.workRam+82} ring the impact sound: Kong has landed
18C1: 21 88 63        LD      HL,$6388            
18C4: 34              INC     (HL)                ; on to the last step of the finale
18C5: C9              RET                         

runRivetBoardFinaleThenAdvanceLevel:
18C6: 21 AF 62        LD      HL,$62AF            ; the finale's countdown, left at zero by the landing step
18C9: 35              DEC     (HL)                ; the first tick wraps it to 0xFF, so the scene runs 256 frames
18CA: CA 3D 19        JP      Z,$193D             ; {code.loc_193d} at zero the scene is over and the board moves on
18CD: 7E              LD      A,(HL)              
18CE: E6 07           AND     $07                 ; the animation below steps every eighth frame
18D0: C0              RET     NZ                  
18D1: 21 25 6A        LD      HL,$6A25            ; the code byte of the sprite at the foot of the screen
18D4: 7E              LD      A,(HL)              
18D5: EE 80           XOR     $80                 ; mirror it, so it rocks back and forth
18D7: 77              LD      (HL),A              
18D8: 21 19 69        LD      HL,$6919            ; record 4's sprite code
18DB: 46              LD      B,(HL)              
18DC: CB A8           RES     5,B                 ; mask off the bit the lookup must not see
18DE: AF              XOR     A                   
18DF: CD 09 30        CALL    $3009               ; {code.nextAnimationStep} step the pose round its cycle
18E2: F6 20           OR      $20                 ; put the bit back
18E4: 77              LD      (HL),A              
18E5: 21 AF 62        LD      HL,$62AF            
18E8: 7E              LD      A,(HL)              
18E9: FE E0           CP      $E0                 ; 32 frames into the scene
18EB: C2 10 19        JP      NZ,$1910            ; {code.loc_1910}
18EE: 3E 50           LD      A,$50               
18F0: 32 4F 69        LD      ($694F),A           ; {hard.workRam+94F} stand Mario on the girder left at the top
18F3: 3E 00           LD      A,$00               
18F5: 32 4D 69        LD      ($694D),A           ; {hard.workRam+94D} the scene's pose, unmirrored
18F8: 3E 9F           LD      A,$9F               
18FA: 32 4C 69        LD      ($694C),A           ; {hard.workRam+94C} at a fixed X to one side of mid-screen
18FD: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} unless he finished on the other side
1900: FE 80           CP      $80                 ; the screen midpoint
1902: D2 0F 19        JP      NC,$190F            ; {code.loc_190f}
1905: 3E 80           LD      A,$80               
1907: 32 4D 69        LD      ($694D),A           ; {hard.workRam+94D} then the mirrored pose
190A: 3E 5F           LD      A,$5F               
190C: 32 4C 69        LD      ($694C),A           ; {hard.workRam+94C} and the mirror-image X

loc_190f:
190F: 7E              LD      A,(HL)              ; recover the countdown the position test overwrote

loc_1910:
1910: FE C0           CP      $C0                 ; 64 frames in
1912: C0              RET     NZ                  
1913: 21 8A 60        LD      HL,$608A            ; the sound-priority pair again
1916: 36 0C           LD      (HL),$0C            ; the closing tune for an odd level number
1918: 3A 29 62        LD      A,($6229)           ; {hard.workRam+229} which of the two depends on the level's low bit
191B: 0F              RRCA                        
191C: 38 02           JR      C,$1920             ; {code.loc_1920}
191E: 36 05           LD      (HL),$05            ; an even level gets the other one

loc_1920:
1920: 23              INC     HL                  
1921: 36 03           LD      (HL),$03            ; held three frames
1923: 21 23 6A        LD      HL,$6A23            ; the heart's sprite record, filled backwards
1926: 36 40           LD      (HL),$40            ; Y, a little above Mario
1928: 2B              DEC     HL                  
1929: 36 09           LD      (HL),$09            ; colour attribute
192B: 2B              DEC     HL                  
192C: 36 76           LD      (HL),$76            ; the whole-heart tile code
192E: 2B              DEC     HL                  
192F: 36 8F           LD      (HL),$8F            ; X, between him and mid-screen
1931: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} which side he finished on, once more
1934: FE 80           CP      $80                 
1936: D0              RET     NC                  
1937: 3E 6F           LD      A,$6F               
1939: 32 20 6A        LD      ($6A20),A           ; {hard.workRam+A20} the mirror-image X, keeping the heart inboard
193C: C9              RET                         

loc_193d:
193D: 2A 2A 62        LD      HL,($622A)          ; {hard.workRam+22A} the board-order pointer
1940: 23              INC     HL                  ; step one entry forward
1941: 7E              LD      A,(HL)              ; the board waiting there
1942: FE 7F           CP      $7F                 ; the table's end marker
1944: C2 4B 19        JP      NZ,$194B            ; {code.loc_194b}
1947: 21 73 3A        LD      HL,$3A73            ; wrap back to the head of the repeating group
194A: 7E              LD      A,(HL)              ; and take the board there instead

loc_194b:
194B: 22 2A 62        LD      ($622A),HL          ; {hard.workRam+22A} store the advanced pointer
194E: 32 27 62        LD      ($6227),A           ; {hard.workRam+227} publish the board coming up
1951: 21 29 62        LD      HL,$6229            
1954: 34              INC     (HL)                ; one more level -- the only place the count moves
1955: 11 00 05        LD      DE,$0500            
1958: CD 9F 30        CALL    $309F               ; {code.enqueueTask} post the new board's deferred task
195B: AF              XOR     A                   
195C: 32 2E 62        LD      ($622E),A           ; {hard.workRam+22E} the how-high height starts over
195F: 32 88 63        LD      ($6388),A           ; {hard.workRam+388} the next cleared-board run starts at 0
1962: 21 09 60        LD      HL,$6009            
1965: 36 E0           LD      (HL),$E0            ; wait 224 frames
1967: 23              INC     HL                  
1968: 36 08           LD      (HL),$08            ; then the how-high interlude sub-state
196A: C9              RET                         

; A phase hand-off arm of the in-game sub-state table: blank every tilemap cell and zero
; the 384-byte sprite shadow buffer, then re-point the sub-state machine into a later
; phase group with gameSubstate = activePlayerIndex + 0x12, an 8-bit add. The base is
; deliberately not folded into a single constant -- the target sub-state really is
; computed from the player index. It reads exactly that one input byte.
clearScreenAndSelectSubstate:
196B: CD 52 08        CALL    $0852               ; {code.clearTilemapAndSprites} blank the screen and sprite shadow
196E: 3A 0E 60        LD      A,($600E)           ; {hard.workRam+E} the player who is up
1971: C6 12           ADD     A,$12               ; select that player's later phase group
1973: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} hand the sub-state machine on
1976: C9              RET                         

; The attract demo's per-frame entry, and only two steps: write this frame's canned
; control word over the cooked player input, then run the same per-frame update cascade
; a played game runs, which reads that word as if a joystick had produced it. The order
; is the whole of it -- run the cascade first and it consumes the previous frame's input
; instead of this one's. A demo frame is an ordinary frame whose input was canned. The
; in-game path enters the same cascade one instruction later, skipping only the script
; step.
runAttractDemoFrame:
1977: CD EE 21        CALL    $21EE               ; {code.advanceAttractDemoInput} lay down this frame's canned input

; One frame of play. Twenty-four subsystem updates run in a fixed sequence with nothing
; passed between them; what this routine contributes is the ORDER, three gates that can
; abandon the rest of the frame, and the death hand-off at the end. The three gates are
; the effect latch (an effect is playing, so the frame belongs to it), the board-won
; check (the win path already committed the advance), and the bonus-expired step machine.
; The tail reads marioActive: Mario can be alive at entry and dead by the time the
; updates finish, since the collision and hazard updates above are what kill him. Still
; active and the frame is simply over; zero, and this silences every sound output, fires
; the death sound trigger, and steps gameSubstate on. The attract demo enters this same
; body one instruction earlier, after its input-script call.
runGameplayFrame:
197A: CD BD 1D        CALL    $1DBD               ; {code.dispatchEffectState} one frame of the effect-sprite machine

loc_197d:
197D: CD 8C 1E        CALL    $1E8C               ; {code.runHitEffectInsteadOfPlay} an effect playing owns the frame

loc_1980:
1980: CD C3 1A        CALL    $1AC3               ; {code.dispatchMarioMovement} Mario's movement for this frame
1983: CD 72 1F        CALL    $1F72               ; {code.update25mBarrels} walk the ten barrel slots, 25m only
1986: CD 8F 2C        CALL    $2C8F               ; {code.driveBarrelRelease} step a barrel on its way out
1989: CD 03 2C        CALL    $2C03               ; {code.scheduleBarrelRelease} decide whether a release is due
198C: CD ED 30        CALL    $30ED               ; {code.updateFires} the fireballs
198F: CD 04 2E        CALL    $2E04               ; {code.update75mActorObjects} 75m only, while Mario is alive
1992: CD EA 24        CALL    $24EA               ; {code.update50mMovingObjects} 50m only: the travelling objects
1995: CD DB 2D        CALL    $2DDB               ; {code.raisePeriodicObjectSpawnRequests} 50m and 100m only
1998: CD D4 2E        CALL    $2ED4               ; {code.driveHammerSprite} the hammer object, and its tune
199B: CD 07 22        CALL    $2207               ; {code.dispatch50mObjectState} 50m only: one of two, by parity
199E: CD 33 1A        CALL    $1A33               ; {code.collectEdgeRivet} 100m: a rivet he has stepped off
19A1: CD 85 2A        CALL    $2A85               ; {code.startMarioFallWhenGroundGivesWay} is his footing level?
19A4: CD 46 1F        CALL    $1F46               ; {code.beginMarioFall} and if it armed one, start the fall
19A7: CD FA 26        CALL    $26FA               ; {code.service75mBoard} 75m; the screen bottom kills him
19AA: CD F2 25        CALL    $25F2               ; {code.update50mConveyorObjects} and carry Mario along his row
19AD: CD DA 19        CALL    $19DA               ; {code.scanObjectsAtMarioX} an object at Mario's exact X?
19B0: CD FB 03        CALL    $03FB               ; {code.slide50mSpriteRowAndServiceColorCycle}
19B3: CD 08 28        CALL    $2808               ; {code.killMarioOnObjectCollision} did a hazard just reach him?
19B6: CD 1D 28        CALL    $281D               ; {code.recordHammerHitOnObject} the same test for his hammer
19B9: CD 57 1E        CALL    $1E57               ; {code.checkBoardWonByType} has the board just been won?
19BC: CD 07 1A        CALL    $1A07               ; {code.dispatchBonusExpiredStep} the bonus-ran-out kill sequence
19BF: CD CB 2F        CALL    $2FCB               ; {code.tickTimedBoardBonus} count the bonus down (not on 25m)
19C2: 00              NOP                         ; three spare bytes -- exactly the width of one more call
19C3: 00              NOP                         
19C4: 00              NOP                         
19C5: 3A 00 62        LD      A,($6200)           ; {hard.workRam+200} the death hand-off: did he survive the frame?
19C8: A7              AND     A                   
19C9: C0              RET     NZ                  ; still alive, and the frame is simply over
19CA: CD 1C 01        CALL    $011C               ; {code.silenceSound} he did not: cut every sound output off
19CD: 21 82 60        LD      HL,$6082            ; the death sound trigger
19D0: 36 03           LD      (HL),$03            ; assert it for three frames, then run on into the sub-state step

; Advance to the next sub-state after a delay: bump gameSubstate by one, stepping the
; sub-state dispatch index to the next handler within the current game state, and reload
; substateTimer with 64 so the new sub-state waits 64 frames before it may proceed. This
; is the shared closing act of an in-state update -- the "wait N frames then go to state
; M" idiom with M = current + 1.
advanceSubstateAndArmTimer:
19D2: 21 0A 60        LD      HL,$600A            
19D5: 34              INC     (HL)                ; step to the next sub-state handler
19D6: 2B              DEC     HL                  ; the sub-state timer sits just below
19D7: 36 40           LD      (HL),$40            ; make the new sub-state wait 64 frames
19D9: C9              RET                         

; The broad phase of the per-frame object-collision check, run once a frame from the
; update cascade. It walks the three 4-byte objectCollisionSprites records comparing
; each record's X against marioX, and on the FIRST whose X matches it hands that record
; to the narrow phase -- which checks the Y alignment and the record's eligibility
; before registering a hit -- and stops scanning. With no match it touches nothing. The
; X test is exact equality, not a range, so a record has to line up with Mario to the
; pixel before the narrow phase is consulted.
scanObjectsAtMarioX:
19DA: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} Mario's X, the key for the broad phase
19DD: 06 03           LD      B,$03               ; three collision records
19DF: 21 0C 6A        LD      HL,$6A0C            ; base of the collision records

loc_19e2:
19E2: BE              CP      (HL)                ; exact X equality, not a range
19E3: CA ED 19        JP      Z,$19ED             ; {code.confirmObjectHit} lined up: consult the narrow phase
19E6: 2C              INC     L                   ; on to the next record
19E7: 2C              INC     L                   
19E8: 2C              INC     L                   
19E9: 2C              INC     L                   
19EA: 10 F6           DJNZ    $19E2               ; {code.loc_19e2}
19EC: C9              RET                         

; The confirm half of the object-slot collision scan. The scan walks a 3-entry, stride-4
; table of collision records comparing each record's X (+0) against marioX, and on a
; match branches here with that record's base. This finishes the test: marioY must equal
; the record's Y byte (+3), and bit 3 of its flag byte (+1) must be CLEAR, i.e. the
; object has not already been consumed. Either check failing returns having touched
; nothing. Both passing registers the hit for the effect machine -- effectParamPtr = the
; record base, effectSelect = 0, effectState = 1 -- which services it on later frames.
confirmObjectHit:
19ED: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} the Y half of the test
19F0: 2C              INC     L                   ; step to the record's Y byte
19F1: 2C              INC     L                   
19F2: 2C              INC     L                   
19F3: BE              CP      (HL)                ; must match Mario's row exactly
19F4: C0              RET     NZ                  ; wrong row, no hit
19F5: 2D              DEC     L                   ; back to the record's flag byte
19F6: 2D              DEC     L                   
19F7: CB 5E           BIT     3,(HL)              ; bit 3 marks an object already consumed
19F9: C0              RET     NZ                  ; nothing left to collect here
19FA: 2D              DEC     L                   ; back to the record base
19FB: 22 43 63        LD      ($6343),HL          ; {hard.workRam+343} hand the record to the effect machine
19FE: AF              XOR     A                   
19FF: 32 42 63        LD      ($6342),A           ; {hard.workRam+342} effect kind 0
1A02: 3C              INC     A                   
1A03: 32 40 63        LD      ($6340),A           ; {hard.workRam+340} arm the effect for later frames
1A06: C9              RET                         

; Run whichever step of the bonus-expired sequence is current. When the on-screen bonus
; counter runs down to zero the player is killed for it, and that does not happen in one
; frame: bonusExpiredStep is the four-state machine that carries it out. Step 0 idle, the
; bonus has not expired; step 1 clears the delay counter and moves on; step 2 counts that
; delay down; step 3 holds until Mario is back on the ground and then takes the death
; exit. The answer it returns says whether the rest of the frame's gameplay work should
; still run -- only step 3 can ever say no, and only on the arm that takes the death
; exit.
dispatchBonusExpiredStep:
1A07: 3A 86 63        LD      A,($6386)           ; {hard.workRam+386} which step of the sequence is current
1A0A: EF              RST     $28                 ; vector through the step table below

; ---- $1A0B-$1A14: jump table ----
1A0B: 1E 1A 15 1A 1F 1A 2A 1A 00 00

; Arm the DELAY phase of the bonus-expired death sequence. bonusExpiredStep is a
; four-state machine the per-frame gameplay cascade dispatches every frame: state 0 does
; nothing while bonus is still above 0; both bonus-decrement sites write 1 the moment the
; readout reaches 0; state 1 is this routine; state 2 counts bonusExpiredDelay down and
; at 0 goes to state 3; and state 3 waits until Mario is no longer airborne and then
; takes the death exit. As state 1 this does two constant stores -- clear
; bonusExpiredDelay to 0, and advance bonusExpiredStep to 2. State 2 decrements before it
; tests, so that zero wraps to 255 and the delay is 256 frames.
startBonusExpiredDelay:
1A15: AF              XOR     A                   
1A16: 32 87 63        LD      ($6387),A           ; {hard.workRam+387} clear it; the first tick wraps it to 255
1A19: 3E 02           LD      A,$02               
1A1B: 32 86 63        LD      ($6386),A           ; {hard.workRam+386} on to the counting step

; The idle arm of the bonus-expired sequence, selected while its step selector holds 0
; -- that is, for as long as the on-screen bonus has not yet counted down to zero. It
; takes no inputs, reads and writes no memory, and returns, so the sequence stays
; dormant on those frames and nothing on screen or in memory changes.
bonusExpiredIdle:
1A1E: C9              RET                         ; bonus still above zero: nothing to do

; The pause in the bonus-expired sequence, which runs once a board's bonus reaches zero.
; Every frame it takes one off bonusExpiredDelay; while that is still non-zero the
; sequence stays parked here, and only on the frame it reaches zero does
; bonusExpiredStep move on. The delay starts at zero, so the first decrement wraps it to
; 255 -- the pause is a full 256-frame roll, not a configured length.
advanceBonusExpiredStepWhenDelayExpires:
1A1F: 21 87 63        LD      HL,$6387            
1A22: 35              DEC     (HL)                ; one frame off the pause
1A23: C0              RET     NZ                  ; still pausing
1A24: 3E 03           LD      A,$03               
1A26: 32 86 63        LD      ($6386),A           ; {hard.workRam+386} on to the wait-for-landing step
1A29: C9              RET                         

; The wait-and-exit step of the bonus-expired sequence: hold this sub-state until Mario
; has landed, then advance. While marioAirborne is non-zero he is still jumping or
; falling, so this does nothing and the frame's update cascade runs to completion; the
; step waits again next frame. Once it is zero he has landed: step gameSubstate on to the
; next handler, re-arm its 64-frame wait, and report back that the rest of this frame's
; cascade must be abandoned.
advanceSubstateWhenGrounded:
1A2A: 3A 16 62        LD      A,($6216)           ; {hard.workRam+216} wait until Mario has landed
1A2D: A7              AND     A                   
1A2E: C0              RET     NZ                  ; still airborne, try again next frame
1A2F: E1              POP     HL                  ; drop the rest of this frame's cascade
1A30: C3 D2 19        JP      $19D2               ; {code.advanceSubstateAndArmTimer} take the death exit

; The 100m rivet pickup, and it is a two-frame edge rather than a contact test. Its first
; act is the board gate with the 100m bit, so on the other three boards it does nothing
; at all. If Mario is standing on one of the two screen-edge rivet columns it merely
; raises edgeRivetArmed and stops -- nothing is collected on the frame he is on it. On a
; later frame, once he has stepped off, the latch is disarmed and the rivet removed: a
; 3-bit slot index is built from position bits (two bits of marioY pick the row band,
; with an extra seam case folded into the middle bit, and marioX's high bit picks the
; side); if that slot's rivetPresent flag is already clear it stops, otherwise it clears
; the flag, counts one off rivetsLeft, blanks the rivet's three tilemap cells, and raises
; effectState, effectSelect and itemCollected.
collectEdgeRivet:
1A33: 3E 08           LD      A,$08               ; mask bit 3: the 100m rivet board only
1A35: F7              RST     $30                 ; board gate; nothing to do elsewhere
1A36: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203}
1A39: FE 4B           CP      $4B                 ; the left-edge rivet column
1A3B: CA 4B 1A        JP      Z,$1A4B             ; {code.armEdgeRivetPickup} standing on it: only arm
1A3E: FE B3           CP      $B3                 ; the right-edge rivet column
1A40: CA 4B 1A        JP      Z,$1A4B             ; {code.armEdgeRivetPickup} standing on it: only arm
1A43: 3A 91 62        LD      A,($6291)           ; {hard.workRam+291} was he on an edge last frame?
1A46: 3D              DEC     A                   
1A47: CA 51 1A        JP      Z,$1A51             ; {code.loc_1a51} he has stepped off, so collect
1A4A: C9              RET                         

; Raise edgeRivetArmed. This is the "arm" half of a two-pass, set-then-consume latch:
; the edge-item pickup runs every in-game frame, reads Mario's X and, when he is
; standing on one of the two screen-EDGE columns, comes here and raises the flag
; unconditionally -- the edge test itself lives upstream. On a LATER frame, once he is
; no longer on the exact edge, the pickup takes its other path and collects only if the
; flag is up, and the collect handler's first act is to write 0 back. That is where a
; rivet slot is cleared and rivetsLeft decremented, so the latch is a rivet-scoped
; one-shot.
armEdgeRivetPickup:
1A4B: 3E 01           LD      A,$01               
1A4D: 32 91 62        LD      ($6291),A           ; {hard.workRam+291} arm; nothing is collected this frame
1A50: C9              RET                         

loc_1a51:
1A51: 32 91 62        LD      ($6291),A           ; {hard.workRam+291} disarm the latch
1A54: 47              LD      B,A                 ; start the slot index at zero
1A55: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1A58: 3D              DEC     A                   
1A59: FE D0           CP      $D0                 ; off the rivet field entirely?
1A5B: D0              RET     NC                  
1A5C: 07              RLCA                        
1A5D: D2 62 1A        JP      NC,$1A62            ; {code.loc_1a62}
1A60: CB D0           SET     2,B                 ; top bit of the row band

loc_1a62:
1A62: 07              RLCA                        
1A63: 07              RLCA                        
1A64: D2 69 1A        JP      NC,$1A69            ; {code.loc_1a69}
1A67: CB C8           SET     1,B                 ; middle bit of the row band

loc_1a69:
1A69: E6 07           AND     $07                 
1A6B: FE 06           CP      $06                 ; the band seam counts as that bit too
1A6D: C2 72 1A        JP      NZ,$1A72            ; {code.loc_1a72}
1A70: CB C8           SET     1,B                 ; so set it as well

loc_1a72:
1A72: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203}
1A75: 07              RLCA                        ; his X high bit picks the side
1A76: D2 7B 1A        JP      NC,$1A7B            ; {code.loc_1a7b}
1A79: CB C0           SET     0,B                 ; the right-hand half

loc_1a7b:
1A7B: 21 92 62        LD      HL,$6292            ; the eight rivet-present flags
1A7E: 78              LD      A,B                 
1A7F: 85              ADD     A,L                 ; index this slot's flag
1A80: 6F              LD      L,A                 
1A81: 7E              LD      A,(HL)              
1A82: A7              AND     A                   
1A83: C8              RET     Z                   ; that rivet is already gone
1A84: 36 00           LD      (HL),$00            ; clear the rivet's present flag
1A86: 21 90 62        LD      HL,$6290            ; the rivets-left count
1A89: 35              DEC     (HL)                ; one fewer rivet on the board
1A8A: 78              LD      A,B                 
1A8B: 01 05 00        LD      BC,$0005            ; five cells per row band
1A8E: 1F              RRA                         ; the low bit picks the half
1A8F: DA BD 1A        JP      C,$1ABD             ; {code.loc_1abd}
1A92: 21 CB 02        LD      HL,$02CB            ; the left half's column base

loc_1a95:
1A95: A7              AND     A                   
1A96: CA 9E 1A        JP      Z,$1A9E             ; {code.loc_1a9e}

loc_1a99:
1A99: 09              ADD     HL,BC               ; step down one band per row
1A9A: 3D              DEC     A                   
1A9B: C2 99 1A        JP      NZ,$1A99            ; {code.loc_1a99}

loc_1a9e:
1A9E: 01 00 74        LD      BC,$7400            
1AA1: 09              ADD     HL,BC               ; into the tilemap
1AA2: 3E 10           LD      A,$10               ; the blank tile
1AA4: 77              LD      (HL),A              ; erase the rivet's middle cell
1AA5: 2D              DEC     L                   
1AA6: 77              LD      (HL),A              ; and the cell before it
1AA7: 2C              INC     L                   
1AA8: 2C              INC     L                   
1AA9: 77              LD      (HL),A              ; and the cell after it
1AAA: 3E 01           LD      A,$01               
1AAC: 32 40 63        LD      ($6340),A           ; {hard.workRam+340} arm the pickup effect
1AAF: 32 42 63        LD      ($6342),A           ; {hard.workRam+342} the pickup effect kind
1AB2: 32 25 62        LD      ($6225),A           ; {hard.workRam+225} flag the collection
1AB5: 3A 16 62        LD      A,($6216)           ; {hard.workRam+216}
1AB8: A7              AND     A                   
1AB9: CC 95 1D        CALL    Z,$1D95             ; {code.loc_1d95} on his feet: run the pickup follow-up
1ABC: C9              RET                         

loc_1abd:
1ABD: 21 2B 01        LD      HL,$012B            ; the right half's column base
1AC0: C3 95 1A        JP      $1A95               ; {code.loc_1a95}

; The movement machine's router. It writes no memory of its own: it is five tests in a
; fixed priority order, and the ORDER IS THE MECHANIC -- the first that fires takes the
; frame and nothing below it is consulted.
;   1. marioAirborne set -> the airborne handler. A jump or fall owns the whole frame
;      and no input below is looked at, so a jump cannot be steered onto a ladder.
;   2. marioFreezeTimer non-zero -> the post-landing freeze tick, Mario unresponsive.
;   3. marioHammerActive set -> the ground walk. Note WHERE this enters: above both
;      the ladder and the jump test, so a held hammer cannot climb or jump at all.
;   4. marioOnLadder set -> the climb dispatch, the up/down half of the machine.
;   5. bit 7 of p1Input, the jump press-edge -> the jump launcher.
;   otherwise the ground walk: ordinary walking, and stepping onto a ladder.
; The three flag tests fire on the value 1 alone, not on any non-zero value.
dispatchMarioMovement:
1AC3: 3A 16 62        LD      A,($6216)           ; {hard.workRam+216}
1AC6: 3D              DEC     A                   ; airborne outranks everything
1AC7: CA B2 1B        JP      Z,$1BB2             ; {code.advanceMarioAirborneFrame} a jump or fall owns the frame
1ACA: 3A 1E 62        LD      A,($621E)           ; {hard.workRam+21E}
1ACD: A7              AND     A                   
1ACE: C2 55 1B        JP      NZ,$1B55            ; {code.tickPostLandingFreeze} still frozen from the last landing
1AD1: 3A 17 62        LD      A,($6217)           ; {hard.workRam+217}
1AD4: 3D              DEC     A                   
1AD5: CA E6 1A        JP      Z,$1AE6             ; {code.walkRightWhileHeld} hammer in hand means walking only
1AD8: 3A 15 62        LD      A,($6215)           ; {hard.workRam+215}
1ADB: 3D              DEC     A                   
1ADC: CA 38 1B        JP      Z,$1B38             ; {code.climbDownWhileHeld} on a ladder: the climb dispatch
1ADF: 3A 10 60        LD      A,($6010)           ; {hard.workRam+10}
1AE2: 17              RLA                         ; bit 7, the jump press-edge
1AE3: DA 6E 1B        JP      C,$1B6E             ; {code.initMarioJump} a fresh jump press this frame

; The shared setup of Mario's on-foot movement dispatch, plus its RIGHT arm. Reached on
; any frame Mario is neither airborne, nor frozen, nor mid-jump-press. It asks the
; horizontal position gate for its two-flag verdict, one flag per limit, reads p1Input
; once for every arm downstream, and then spends the frame on a rightward walk step only
; if the right-limit flag is clear AND control bit 0 is held. The limit is tested BEFORE
; the button, so a player leaning on Right at the far edge simply gets no step. Anything
; else falls through to the LEFT arm, which asks the same two questions of bit 1 and then
; falls into the ladder/climb handler -- so movement priority is fixed: right beats left
; beats climb. The left arm recomputes neither the verdict nor the control word; it reads
; what this routine left behind.
walkRightWhileHeld:
1AE6: CD 1F 24        CALL    $241F               ; {code.limitMarioHorizontalTravel} the horizontal limit flags
1AE9: 3A 10 60        LD      A,($6010)           ; {hard.workRam+10} read once for every arm below
1AEC: 1D              DEC     E                   ; the right-limit verdict
1AED: CA F5 1A        JP      Z,$1AF5             ; {code.walkLeftWhileHeld} at the right limit, so no step
1AF0: CB 47           BIT     0,A                 ; is Right held?
1AF2: C2 8F 1C        JP      NZ,$1C8F            ; {code.walkMarioRight} spend the frame on one step right

; The LEFT arm of Mario's ground-movement direction dispatch, reached every frame the
; movement machine has decided he is on his feet and has already declined the rightward
; step. Two things are handed down from the arm above: the frame's cooked control word
; p1Input (bit 0 right, bit 1 left, bit 2 up, bit 3 down, bit 7 jump press-edge) and the
; LEFT half of the horizontal position gate's verdict. Mario walks one frame left only
; when Left is held AND the gate has not blocked leftward motion -- and that block is not
; only the screen edge; the same verdict fires for an interior wall at the left end of
; the top platform on the odd boards. Any other frame falls THROUGH to the ladder/climb
; handler, where Up and Down are serviced -- which is what keeps a refused frame
; available to the climb path.
walkLeftWhileHeld:
1AF5: 15              DEC     D                   ; the left-limit verdict
1AF6: CA FE 1A        JP      Z,$1AFE             ; {code.armMarioClimbAtLadderEnd} blocked left, so try the ladder
1AF9: CB 4F           BIT     1,A                 ; is Left held?
1AFB: C2 AB 1C        JP      NZ,$1CAB            ; {code.walkMarioLeft} spend the frame on one step left

; At a ladder end, stamp the ladder-standing pose and this frame's climb-limit pair,
; ARMING a climb the movement code may then perform. It is gated on marioHammerActive:
; unless that differs from 1 nothing happens -- the hammer state only FORBIDS the arm
; here, it never starts one. Two probes come off Mario's position: a grid-aligned X (low
; two bits forced set, the 0x04 bit forced clear) as the search key, and (marioY + 8) as
; both discriminator and climb-limit value. The key is looked up in objParamTable0; a
; miss returns having done nothing. On a hit it stamps marioSpriteCode's low bits to the
; ladder-STANDING pose 0x06, keeping the facing bit -- the same code written when a
; climb ENDS, which is what makes "arms a climb" rather than "drives one" the honest
; reading -- and records whether the match sat among the last few entries scanned. Tag 0
; commits marioClimbLimitA and marioClimbLimitB the ordinary way and drives the
; up-climb; tag 1 commits the SAME pair in the OPPOSITE order and hands the frame to the
; down/up climb dispatch, unless the match was near the scan's end.
armMarioClimbAtLadderEnd:
1AFE: 3A 17 62        LD      A,($6217)           ; {hard.workRam+217}
1B01: 3D              DEC     A                   ; a held hammer forbids arming a climb
1B02: C8              RET     Z                   
1B03: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1B06: C6 08           ADD     A,$08               ; Y+8, the discriminator and climb limit
1B08: 57              LD      D,A                 
1B09: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203}
1B0C: F6 03           OR      $03                 ; grid-align the X search key
1B0E: CB 97           RES     2,A                 
1B10: 01 15 00        LD      BC,$0015            ; at most twenty-one entries to scan
1B13: CD 6E 23        CALL    $236E               ; {code.findOppositeLadderEnd} look the key up in the ladder table
1B16: F5              PUSH    AF                  ; keep which paired slot matched
1B17: 21 07 62        LD      HL,$6207            ; Mario's sprite code
1B1A: 7E              LD      A,(HL)              
1B1B: E6 80           AND     $80                 ; keep only the facing bit
1B1D: F6 06           OR      $06                 ; the ladder-standing pose
1B1F: 77              LD      (HL),A              
1B20: 21 1A 62        LD      HL,$621A            
1B23: 3E 04           LD      A,$04               
1B25: B9              CP      C                   ; did the match sit near the end of the scan?
1B26: 36 01           LD      (HL),$01            
1B28: D2 2C 1B        JP      NC,$1B2C            ; {code.loc_1b2c}
1B2B: 35              DEC     (HL)                ; no: clear the flag again

loc_1b2c:
1B2C: F1              POP     AF                  
1B2D: A7              AND     A                   
1B2E: CA 4E 1B        JP      Z,$1B4E             ; {code.loc_1b4e} tag 0 commits the limits the ordinary way
1B31: 7E              LD      A,(HL)              
1B32: A7              AND     A                   
1B33: C0              RET     NZ                  ; near the end of the scan: nothing more
1B34: 2C              INC     L                   
1B35: 72              LD      (HL),D              ; commit the pair in the opposite order
1B36: 2C              INC     L                   
1B37: 70              LD      (HL),B              

; The Down half of the ladder-climb input dispatch. It tests bit 3 of p1Input first:
; with Down held it hands the frame to the climb-down driver and stops -- notably
; WITHOUT checking marioOnLadder, so holding Down drives the descent directly. With Down
; clear it falls through to the up-climb guard, which does insist on marioOnLadder and
; climbs only while Up is held. Why the two arms differ on that guard is not settled
; here.
climbDownWhileHeld:
1B38: 3A 10 60        LD      A,($6010)           ; {hard.workRam+10}
1B3B: CB 5F           BIT     3,A                 ; is Down held?
1B3D: C2 F2 1C        JP      NZ,$1CF2            ; {code.climbMarioDown} drive the descent, no on-ladder check
1B40: 3A 15 62        LD      A,($6215)           ; {hard.workRam+215}
1B43: A7              AND     A                   
1B44: C8              RET     Z                   ; the up-climb needs him on a ladder

; The Up half of the ladder-climb input dispatch. It reads p1Input and tests bit 2; if Up
; is held this frame it hands off to the climb-up driver, which paces and advances
; Mario's ladder climb, and otherwise it does nothing. A pure input guard in front of
; that driver -- it writes no memory of its own. The Down half tests bit 3 and falls
; through to here.
climbUpWhileHeld:
1B45: 3A 10 60        LD      A,($6010)           ; {hard.workRam+10}
1B48: CB 57           BIT     2,A                 ; is Up held?
1B4A: C2 03 1D        JP      NZ,$1D03            ; {code.climbMarioUp} advance the upward climb this frame
1B4D: C9              RET                         

loc_1b4e:
1B4E: 2C              INC     L                   
1B4F: 70              LD      (HL),B              ; commit the first climb limit
1B50: 2C              INC     L                   
1B51: 72              LD      (HL),D              ; and the second
1B52: C3 45 1B        JP      $1B45               ; {code.climbUpWhileHeld} then climb if Up is held

; Count Mario's post-landing freeze down and unfreeze him when it expires. Landing from a
; jump loads marioFreezeTimer with four, so he is unresponsive for four frames; on each
; of those the routine steps the timer down and, while it is still non-zero, returns at
; once, so Mario stays put. On the frame it reaches zero the one-shot unfreeze runs:
; marioHammerActive takes marioHammerPending, so a hammer touched only during the
; airborne frames is committed now he is settled; marioSpriteCode keeps just its top bit,
; the facing flag, stripping the tile and animation bits so he resumes from a clean
; standing pose; marioWalkAnim is cleared, restarting the walk cycle; and his hardware
; sprite record is refreshed from that cleaned state.
tickPostLandingFreeze:
1B55: 21 1E 62        LD      HL,$621E            ; the post-landing freeze timer
1B58: 35              DEC     (HL)                
1B59: C0              RET     NZ                  ; still frozen, so Mario stays put
1B5A: 3A 18 62        LD      A,($6218)           ; {hard.workRam+218}
1B5D: 32 17 62        LD      ($6217),A           ; {hard.workRam+217} commit a hammer touched while airborne
1B60: 21 07 62        LD      HL,$6207            ; Mario's sprite code
1B63: 7E              LD      A,(HL)              
1B64: E6 80           AND     $80                 ; keep the facing bit, drop the pose bits
1B66: 77              LD      (HL),A              
1B67: AF              XOR     A                   
1B68: 32 02 62        LD      ($6202),A           ; {hard.workRam+202} restart the walk cycle
1B6B: C3 A6 1D        JP      $1DA6               ; {code.writeMarioSpriteRecord} refresh his sprite record

; Begin Mario's jump, on the frame a jump press is accepted. It sets marioAirborne = 1,
; so the movement machine's first per-frame test now routes him through the ballistic
; handler instead of the ground handler, and picks the horizontal launch velocity from
; p1Input: bit 0 Right gives +128, bit 1 Left gives -128, holding neither gives zero --
; a straight-up jump -- and Right wins if both are held, being tested first. The
; velocity is a big-endian 16-bit pair: high byte 0x00 for Right and 0xFF for Left, low
; byte 0x80 in both, and both zero for neither. It then hands that to the launch tail,
; which writes the rest of the airborne record: velocities, cleared fractions and frame
; count, jump pose, take-off Y, jump sound.
initMarioJump:
1B6E: 3E 01           LD      A,$01               
1B70: 32 16 62        LD      ($6216),A           ; {hard.workRam+216} route him through the ballistic handler
1B73: 21 10 62        LD      HL,$6210            ; the airborne motion record
1B76: 3A 10 60        LD      A,($6010)           ; {hard.workRam+10}
1B79: 01 80 00        LD      BC,$0080            ; +128: a jump to the right
1B7C: 1F              RRA                         ; Right is tested first, so it wins
1B7D: DA 8A 1B        JP      C,$1B8A             ; {code.launchMarioJump} launch with the rightward velocity
1B80: 01 80 FF        LD      BC,$FF80            ; -128: a jump to the left
1B83: 1F              RRA                         ; is Left held?
1B84: DA 8A 1B        JP      C,$1B8A             ; {code.launchMarioJump}
1B87: 01 00 00        LD      BC,$0000            ; neither held: a straight-up jump

; Commit Mario's ballistic jump. Jump-init has already flagged him airborne and chosen a
; horizontal launch velocity from the held direction -- +128 right, -128 left, 0
; straight up, in 1/256 pixel per frame -- and hands it over. This writes the whole
; airborne state the ballistic integrator then reads every frame: marioAirVxHi/Lo take
; that velocity; marioAirVyHi/Lo take 328, the fixed upward impulse from which gravity
; is later derived; marioAirFrames, marioXFrac and marioYFrac are cleared, so the arc
; starts at frame 0 with no accumulated remainder; marioSpriteCode keeps its facing bit
; and takes jump code 0x0E; marioAirStartY snapshots marioY as the take-off height the
; fall-fatality test measures against; and sndTrigger bit 1 is asserted for three frames
; for the jump sound.
launchMarioJump:
1B8A: AF              XOR     A                   
1B8B: 70              LD      (HL),B              ; stash the horizontal launch velocity, high byte
1B8C: 2C              INC     L                   
1B8D: 71              LD      (HL),C              ; and its low byte
1B8E: 2C              INC     L                   
1B8F: 36 01           LD      (HL),$01            ; the fixed upward impulse, 328, high byte
1B91: 2C              INC     L                   
1B92: 36 48           LD      (HL),$48            ; and its low byte
1B94: 2C              INC     L                   
1B95: 77              LD      (HL),A              ; start the arc at frame zero
1B96: 32 04 62        LD      ($6204),A           ; {hard.workRam+204} clear the accumulated horizontal remainder
1B99: 32 06 62        LD      ($6206),A           ; {hard.workRam+206} and the vertical one
1B9C: 3A 07 62        LD      A,($6207)           ; {hard.workRam+207}
1B9F: E6 80           AND     $80                 ; keep only the facing bit
1BA1: F6 0E           OR      $0E                 ; stamp in the jump pose
1BA3: 32 07 62        LD      ($6207),A           ; {hard.workRam+207} commit the jump sprite
1BA6: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1BA9: 32 0E 62        LD      ($620E),A           ; {hard.workRam+20E} the take-off height the fall test measures
1BAC: 21 81 60        LD      HL,$6081            
1BAF: 36 03           LD      (HL),$03            ; hold the jump sound three frames
1BB1: C9              RET                         

; The head of every airborne frame -- every frame of a jump or a fall. First it copies
; marioX and marioY into marioAirPrevX / marioAirPrevY, so this frame's STARTING position
; survives the motion below: the collision code reads that pair back to test the swept
; segment rather than only the new point. Then the ballistic step integrates one frame of
; the arc -- X drifts by the horizontal velocity, Y takes the vertical velocity plus the
; ramping gravity term. Then the horizontal travel limit classifies the new position into
; a two-flag verdict, which picks how he is steered: at the left limit -- an interior
; wall on 25m and 75m, not the screen edge -- the horizontal velocity is forced to +0.5
; px/frame and the sprite's facing bit is set; the other arm mirrors that at the
; far-right limit. Both converge on the landing / fatal-fall tail.
advanceMarioAirborneFrame:
1BB2: DD 21 00 62     LD      IX,$6200            ; point at Mario's motion record
1BB6: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203}
1BB9: DD 77 0B        LD      (IX+$0B),A          ; save this frame's starting X for the swept collision test
1BBC: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1BBF: DD 77 0C        LD      (IX+$0C),A          ; and its starting Y
1BC2: CD 9C 23        CALL    $239C               ; {code.stepBallisticMotion} integrate one frame of the arc
1BC5: CD 1F 24        CALL    $241F               ; {code.limitMarioHorizontalTravel} classify the new X position
1BC8: 15              DEC     D                   ; a verdict of 1 here is the left limit
1BC9: C2 F2 1B        JP      NZ,$1BF2            ; {code.loc_1bf2} not the left limit, try the right one
1BCC: DD 36 10 00     LD      (IX+$10),$00        ; force a drift of +0.5 px/frame back inside
1BD0: DD 36 11 80     LD      (IX+$11),$80        
1BD4: DD CB 07 FE     SET     7,(IX+$07)          ; face him right, the way he is now pushed

; Re-base Mario's vertical arc where he is standing now, so a jump reflects off a
; playfield limit instead of carrying through it. Reached only from the airborne
; handler's two limit arms, which have already stamped a horizontal velocity pushing him
; back inside plus the matching facing bit; this is the vertical half. The ballistic
; integrator stores an arc as a CONSTANT launch velocity plus a count of elapsed frames,
; moving Mario down by (16*frames + 8 - velocity) each frame, so the velocity field is
; not the current speed and cannot simply be negated. Instead marioAirVyHi/Lo becomes
; 16*frames - velocity and marioAirFrames restarts at zero, re-basing the same parabola
; at his present position with its vertical step negated. A fall already latched lethal
; in marioFatalFall is exempt, so a killing fall keeps its arc.
reverseMarioVerticalArc:
1BD8: 3A 20 62        LD      A,($6220)           ; {hard.workRam+220} is this fall already condemned?
1BDB: 3D              DEC     A                   
1BDC: CA EC 1B        JP      Z,$1BEC             ; {code.loc_1bec} a killing fall keeps its arc, skip the re-base
1BDF: CD 07 24        CALL    $2407               ; {code.loc_2407} reflect the arc: 16*frames minus the velocity
1BE2: DD 74 12        LD      (IX+$12),H          ; re-base the vertical velocity on that reflection
1BE5: DD 75 13        LD      (IX+$13),L          
1BE8: DD 36 14 00     LD      (IX+$14),$00        ; restart the frame count, re-basing the parabola here

loc_1bec:
1BEC: CD 9C 23        CALL    $239C               ; {code.stepBallisticMotion} step the re-based arc one frame
1BEF: C3 05 1C        JP      $1C05               ; {code.loc_1c05}

loc_1bf2:
1BF2: 1D              DEC     E                   ; a verdict of 1 here is the right limit
1BF3: C2 05 1C        JP      NZ,$1C05            ; {code.loc_1c05} inside both limits, an ordinary airborne frame
1BF6: DD 36 10 FF     LD      (IX+$10),$FF        ; force a drift of -0.5 px/frame back inside
1BFA: DD 36 11 80     LD      (IX+$11),$80        
1BFE: DD CB 07 BE     RES     7,(IX+$07)          ; face him left, the way he is now pushed
1C02: C3 D8 1B        JP      $1BD8               ; {code.reverseMarioVerticalArc}

loc_1c05:
1C05: CD 1C 2B        CALL    $2B1C               ; {code.loc_2b1c} probe for a landing under Mario's feet

loc_1c08:
1C08: 3D              DEC     A                   ; a verdict of 1 means he has touched down
1C09: CA 3A 1C        JP      Z,$1C3A             ; {code.loc_1c3a} touched down: go tick the landing counter
1C0C: 3A 1F 62        LD      A,($621F)           ; {hard.workRam+21F}
1C0F: 3D              DEC     A                   ; is the fall-height test already armed?
1C10: CA 76 1C        JP      Z,$1C76             ; {code.markFatalFallByHeight} armed: re-run it this frame
1C13: 3A 14 62        LD      A,($6214)           ; {hard.workRam+214}
1C16: D6 14           SUB     $14                 ; how far the arc is from frame 20
1C18: C2 33 1C        JP      NZ,$1C33            ; {code.loc_1c33} not that frame, take the ordinary airborne tail
1C1B: 3E 01           LD      A,$01               
1C1D: 32 1F 62        LD      ($621F),A           ; {hard.workRam+21F} arm the fall-height test for this arc
1C20: CD 53 28        CALL    $2853               ; {code.searchPlayerObjectOverlap} one overlap search per arc
1C23: A7              AND     A                   ; how many objects he cleared with that jump, graded 0, 1, 3 or 7
1C24: CA A6 1D        JP      Z,$1DA6             ; {code.writeMarioSpriteRecord} cleared nothing -- just draw him
1C27: 32 42 63        LD      ($6342),A           ; {hard.workRam+342} the count picks the score award
1C2A: 3E 01           LD      A,$01               
1C2C: 32 40 63        LD      ($6340),A           ; {hard.workRam+340} raise the effect that pays it out
1C2F: 32 25 62        LD      ($6225),A           ; {hard.workRam+225} and flag it; the landing consumes it
1C32: 00              NOP                         

loc_1c33:
1C33: 3C              INC     A                   ; only the frame before the trigger wraps this to zero
1C34: CC 54 29        CALL    Z,$2954             ; {code.latchHammerTouch} one hammer test per jump, not per frame
1C37: C3 A6 1D        JP      $1DA6               ; {code.writeMarioSpriteRecord}

loc_1c3a:
1C3A: 05              DEC     B                   ; tick the airborne counter
1C3B: CA 4F 1C        JP      Z,$1C4F             ; {code.settleMarioOnLanding} it reached zero: he has landed
1C3E: 3C              INC     A                   
1C3F: 32 1F 62        LD      ($621F),A           ; {hard.workRam+21F} arm the land-check phase
1C42: AF              XOR     A                   
1C43: 21 10 62        LD      HL,$6210            ; point at the ballistic block
1C46: 06 05           LD      B,$05               ; five bytes: both velocities and the frame count

loc_1c48:
1C48: 77              LD      (HL),A              ; clear the arc's velocity and frame state
1C49: 2C              INC     L                   
1C4A: 10 FC           DJNZ    $1C48               ; {code.loc_1c48}
1C4C: C3 A6 1D        JP      $1DA6               ; {code.writeMarioSpriteRecord}

; Settle Mario's state the instant he lands from a jump or fall. It stores the caller's
; landing flag (0 in play) into marioAirborne so the airborne handler stops driving him;
; sets marioActive to marioFatalFall flipped, so a clean landing leaves him alive and a
; lethal one leaves him inert for the death sequence; snaps marioSpriteCode to the
; standing/landing pose while preserving the facing bit; arms marioFreezeTimer to 4
; frames, holding him briefly still on touchdown, and clears marioAirLandcheck. If
; itemCollected is latched to 1 the pickup is committed, which stores the cleared flag
; back and, off 25m, queues the pickup tune. Finally it refreshes marioSpriteRecord from
; his just-settled fields.
settleMarioOnLanding:
1C4F: 32 16 62        LD      ($6216),A           ; {hard.workRam+216} stop the airborne handler driving him
1C52: 3A 20 62        LD      A,($6220)           ; {hard.workRam+220} read back whether the fall was condemned
1C55: EE 01           XOR     $01                 ; invert it: a clean landing leaves him alive
1C57: 32 00 62        LD      ($6200),A           ; {hard.workRam+200} a lethal one leaves him inert for the death
1C5A: 21 07 62        LD      HL,$6207            
1C5D: 7E              LD      A,(HL)              
1C5E: E6 80           AND     $80                 ; keep the facing bit
1C60: F6 0F           OR      $0F                 ; snap to the standing pose
1C62: 77              LD      (HL),A              
1C63: 3E 04           LD      A,$04               
1C65: 32 1E 62        LD      ($621E),A           ; {hard.workRam+21E} hold him still four frames on touchdown
1C68: AF              XOR     A                   
1C69: 32 1F 62        LD      ($621F),A           ; {hard.workRam+21F} the fall-height test is finished with
1C6C: 3A 25 62        LD      A,($6225)           ; {hard.workRam+225} was a pickup latched during the jump?
1C6F: 3D              DEC     A                   
1C70: CC 95 1D        CALL    Z,$1D95             ; {code.loc_1d95} commit it, and off 25m cue the pickup tune
1C73: C3 A6 1D        JP      $1DA6               ; {code.writeMarioSpriteRecord}

; Condemn the fall in progress as lethal once Mario has dropped far enough below the
; height he left the ground at. It runs on each airborne frame while the fall-height
; check is armed, comparing marioAirStartY against marioY with 15 pixels of survivable
; slack taken off the current reading. Height grows downward here, so once that
; slack-adjusted reading has reached the take-off height he is 15 or more pixels below
; where he started and the drop is deadly: marioFatalFall is latched -- the landing
; turns that into his death -- and the fall sound cued. A shallower drop leaves both
; alone. Either way it finishes through the movement machine's shared tail, which
; refreshes Mario's sprite record from his position and pose.
markFatalFallByHeight:
1C76: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1C79: 21 0E 62        LD      HL,$620E            ; point at the take-off height
1C7C: D6 0F           SUB     $0F                 ; allow 15 pixels of survivable drop
1C7E: BE              CP      (HL)                ; has he fallen further than that?
1C7F: DA A6 1D        JP      C,$1DA6             ; {code.writeMarioSpriteRecord} a shallow drop, he survives it
1C82: 3E 01           LD      A,$01               
1C84: 32 20 62        LD      ($6220),A           ; {hard.workRam+220} latch the fall lethal; the landing kills him
1C87: 21 84 60        LD      HL,$6084            
1C8A: 36 03           LD      (HL),$03            ; cue the falling sound for three frames
1C8C: C3 A6 1D        JP      $1DA6               ; {code.writeMarioSpriteRecord}

; The rightward arm of Mario's per-frame walk, reached on a frame Right is held and he is
; on foot. The walk is paced in two tiers by marioMoveStepTimer. While the pacer is still
; running, the frame goes to the horizontal step with a +1 delta: Mario slides one pixel
; right and, on the girder board, his Y re-snaps to the sloped girder under the new X. On
; the frame the pacer expires, marioWalkAnim is pushed one step through a packed
; permutation table keyed by the byte 5 -- the leftward twin keys the same lookup with 1
; -- and the result's low two bits, the walk tile, are committed with bit 7 SET, the
; sprite-code flag that faces Mario right. That commit rings the footstep on the odd tile
; and re-arms the pacer. The cycle is 0 -> 2 -> 4 -> 1 -> 0, giving the repeating tile
; run 2, 0, 1, 0.
walkMarioRight:
1C8F: 06 01           LD      B,$01               ; one pixel per frame, rightward
1C91: 3A 0F 62        LD      A,($620F)           ; {hard.workRam+20F} read the walk pacer
1C94: A7              AND     A                   
1C95: C2 D2 1C        JP      NZ,$1CD2            ; {code.advanceMarioWalkX} step still in progress, just slide him
1C98: 3A 02 62        LD      A,($6202)           ; {hard.workRam+202}
1C9B: 47              LD      B,A                 
1C9C: 3E 05           LD      A,$05               ; key the walk-cycle table for the rightward order
1C9E: CD 09 30        CALL    $3009               ; {code.nextAnimationStep} advance the walk cycle one place

loc_1ca1:
1CA1: 32 02 62        LD      ($6202),A           ; {hard.workRam+202} store the new walk-cycle index
1CA4: E6 03           AND     $03                 ; its low two bits are the walk tile
1CA6: F6 80           OR      $80                 ; set the facing-right bit
1CA8: C3 C2 1C        JP      $1CC2               ; {code.beginWalkStep}

; Drive one frame of Mario's leftward ground walk -- the mirror of the rightward stepper,
; differing in exactly three constants. It is paced by marioMoveStepTimer. While that is
; still running a step is already in progress, so this frame only shifts Mario one pixel
; further along it: a delta of -1 goes to the walk-X mover, which moves marioX, re-snaps
; marioY to the sloped girder on 25m, ticks the timer down and refreshes the sprite
; record. When the timer has expired the next step begins: marioWalkAnim advances one
; place round its four-value ring -- this selector walks 0, 1, 4, 2 and the rightward
; stepper walks it the other way, so the two directions give the same values reversed --
; and the new index's low two bits become the walk tile. marioSpriteCode's top bit, the
; facing flag, is left CLEAR here: that is what makes this the left arm.
walkMarioLeft:
1CAB: 06 FF           LD      B,$FF               ; one pixel per frame, leftward
1CAD: 3A 0F 62        LD      A,($620F)           ; {hard.workRam+20F} read the walk pacer
1CB0: A7              AND     A                   
1CB1: C2 D2 1C        JP      NZ,$1CD2            ; {code.advanceMarioWalkX} step still in progress, just slide him
1CB4: 3A 02 62        LD      A,($6202)           ; {hard.workRam+202}
1CB7: 47              LD      B,A                 
1CB8: 3E 01           LD      A,$01               ; key the same table for the leftward order
1CBA: CD 09 30        CALL    $3009               ; {code.nextAnimationStep} advance the walk cycle one place

loc_1cbd:
1CBD: 32 02 62        LD      ($6202),A           ; {hard.workRam+202} store the new walk-cycle index
1CC0: E6 03           AND     $03                 ; the walk tile, with the facing bit left clear

; Start a new walk-animation step. The two horizontal walk steppers, one per direction,
; reach here on the frame their sub-step timer expires, handing over the sprite-code
; byte they just built -- the walk-cycle tile in the low bits plus the facing-right flag
; in bit 7. This publishes that byte as marioSpriteCode, rings the footstep sound only
; when the walk-cycle counter's low bit is set, so a step clicks every OTHER step rather
; than every one, re-arms marioMoveStepTimer for the next two 1px shift frames, and
; refreshes marioSpriteRecord.
beginWalkStep:
1CC2: 21 07 62        LD      HL,$6207            
1CC5: 77              LD      (HL),A              ; publish the walk tile and facing bit
1CC6: 1F              RRA                         ; test the walk counter's low bit
1CC7: DC 8F 1D        CALL    C,$1D8F             ; {code.triggerWalkSound} a footstep every other step, not each one
1CCA: 3E 02           LD      A,$02               
1CCC: 32 0F 62        LD      ($620F),A           ; {hard.workRam+20F} re-arm the pacer for two 1px slide frames
1CCF: C3 A6 1D        JP      $1DA6               ; {code.writeMarioSpriteRecord}

; Advance Mario one pixel along a horizontal walk step. The signed delta handed in by
; the walk stepper -- 1 moving right, 255 (that is, -1) moving left, 0 for a held frame
; -- is added to marioX as a byte, wrapping the way the hardware does. On 25m ONLY,
; marioY is then re-snapped to the sloped girder now under his new X, stepping one unit
; as that X crosses a girder cell edge; on the conveyor, elevator and rivet boards Y is
; left as it was. Both paths tail into the walk-step continuation, which spends one
; frame of the move and refreshes his sprite record.
advanceMarioWalkX:
1CD2: 21 03 62        LD      HL,$6203            
1CD5: 7E              LD      A,(HL)              
1CD6: 80              ADD     A,B                 ; apply the signed one-pixel step
1CD7: 77              LD      (HL),A              ; commit his new column
1CD8: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227}
1CDB: 3D              DEC     A                   
1CDC: C2 EB 1C        JP      NZ,$1CEB            ; {code.continueWalkStep} off 25m the girders are flat: leave Y be
1CDF: 66              LD      H,(HL)              
1CE0: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1CE3: 6F              LD      L,A                 
1CE4: CD 33 23        CALL    $2333               ; {code.snapYToGirder} re-snap him to the slope under the new X

loc_1ce7:
1CE7: 7D              LD      A,L                 
1CE8: 32 05 62        LD      ($6205),A           ; {hard.workRam+205} commit the slope-corrected row

; Carry an in-progress walk step one frame further. Reached as the tail of the shared X
; advance while Mario's sub-step timer is still running: knock marioMoveStepTimer down by
; one, then refresh his four sprite-record bytes. When the timer reaches zero on a later
; frame the walk advances to its next animation frame and re-arms the timer instead of
; coming here.
continueWalkStep:
1CEB: 21 0F 62        LD      HL,$620F            
1CEE: 35              DEC     (HL)                ; spend one frame of the step in progress
1CEF: C3 A6 1D        JP      $1DA6               ; {code.writeMarioSpriteRecord}

; Per-frame driver for Mario's downward ladder climb, pacing the descent one animation
; sub-step at a time. While marioMoveStepTimer is still running it just knocks the pacer
; down by one and holds the current sub-step for this frame. On the frame the pacer
; reaches 0 it reloads it to the climb pace of 3 frames and advances one sub-step
; downward -- a +2 nudge to Mario's Y -- through the shared climb stepper. The upward
; twin feeds that same stepper a -2 step at the walk/climb reload; the fixed +2 and the
; reload of 3 are the whole of what makes this the DOWN direction.
climbMarioDown:
1CF2: 3A 0F 62        LD      A,($620F)           ; {hard.workRam+20F} read the climb pacer
1CF5: A7              AND     A                   
1CF6: C2 8A 1D        JP      NZ,$1D8A            ; {code.tickMoveStepTimer} mid sub-step: hold the pose this frame
1CF9: 3E 03           LD      A,$03               
1CFB: 32 0F 62        LD      ($620F),A           ; {hard.workRam+20F} down-climb pace: three frames a sub-step
1CFE: 3E 02           LD      A,$02               ; step of +2: two pixels DOWN the screen
1D00: C3 11 1D        JP      $1D11               ; {code.advanceClimbStep}

; Drive Mario's upward climb one animation step per frame, paced by marioMoveStepTimer
; so the animation advances every few frames rather than every frame. While the timer is
; still running it hands off to the hold step, which decides whether to tick it down
; this frame, holding Mario between animation sub-steps without moving him. On expiry it
; reloads the timer to 4 and advances the climb one step UP: the shared climb stepper is
; handed a step of -2, so marioY decreases by two -- two pixels up the screen. The -2 is
; what makes this the climb-UP driver; the mirror-image climb-DOWN driver hands the same
; stepper +2.
climbMarioUp:
1D03: 3A 0F 62        LD      A,($620F)           ; {hard.workRam+20F} read the climb pacer
1D06: A7              AND     A                   
1D07: C2 76 1D        JP      NZ,$1D76            ; {code.loc_1d76} mid sub-step: decide whether to tick the pacer
1D0A: 3E 04           LD      A,$04               
1D0C: 32 0F 62        LD      ($620F),A           ; {hard.workRam+20F} up-climb pace: four frames a sub-step
1D0F: 3E FE           LD      A,$FE               ; step of -2: two pixels UP the screen

; One climb-animation step, and the shared body both climb steppers fall into -- the up
; stepper enters with a -2 step, the down stepper with +2, so the per-frame vertical
; step is the caller's. It nudges marioY by that step, then flips a two-phase
; ladder-centring counter. On the phase that flips it non-zero it finalises through the
; centring path: snap Mario onto the ladder column, tick the footstep, commit his
; sprite. On the other phase it decides the outcome from where the new height sits
; against marioClimbLimitA and marioClimbLimitB, measured in (Y + 8) units: at either
; limit the climb has reached a ladder end and dismounts; otherwise it picks the climb
; sprite frame by how far above the near limit he sits -- 8 units up is frame 5, 12 up
; is frame 4, anything else frame 3.
advanceClimbStep:
1D11: 21 05 62        LD      HL,$6205            
1D14: 86              ADD     A,(HL)              
1D15: 77              LD      (HL),A              ; move him the caller's two pixels along the ladder
1D16: 47              LD      B,A                 
1D17: 3A 22 62        LD      A,($6222)           ; {hard.workRam+222}
1D1A: EE 01           XOR     $01                 ; flip the climb's two-phase counter
1D1C: 32 22 62        LD      ($6222),A           ; {hard.workRam+222}
1D1F: C2 51 1D        JP      NZ,$1D51            ; {code.centerMarioAndCommitClimbStep} the step's centring phase
1D22: 78              LD      A,B                 
1D23: C6 08           ADD     A,$08               ; measure the new height in (Y+8) units
1D25: 21 1C 62        LD      HL,$621C            ; point at the far climb limit
1D28: BE              CP      (HL)                ; reached the end of the ladder?
1D29: CA 67 1D        JP      Z,$1D67             ; {code.endClimbAtLadderLimit} yes: dismount
1D2C: 2D              DEC     L                   
1D2D: 96              SUB     (HL)                ; how far he sits above the near limit
1D2E: CA 67 1D        JP      Z,$1D67             ; {code.endClimbAtLadderLimit} sitting on it: dismount
1D31: 06 05           LD      B,$05               ; climb frame 5
1D33: D6 08           SUB     $08                 ; exactly 8 units up?
1D35: CA 3F 1D        JP      Z,$1D3F             ; {code.setClimbSpriteFrame}
1D38: 05              DEC     B                   ; climb frame 4
1D39: D6 04           SUB     $04                 ; 12 units up?
1D3B: CA 3F 1D        JP      Z,$1D3F             ; {code.setClimbSpriteFrame}
1D3E: 05              DEC     B                   ; otherwise climb frame 3

; Stamp Mario's climb-animation sprite for one climb step. marioSpriteCode packs his
; horizontal-mirror flag in the top bit and an animation code in the low bits; this
; toggles the mirror flag -- the left/right leg wiggle that reads as climbing -- while
; dropping the previous step's code, and stamps in the new climb frame the caller chose.
; The climb codes are 3, 4 and 5, cycled by how far up the ladder he has got. It then
; falls into the shared climb tail, which re-asserts the on-ladder flag and copies his
; position and sprite code into his sprite record.
setClimbSpriteFrame:
1D3F: 3E 80           LD      A,$80               
1D41: 21 07 62        LD      HL,$6207            
1D44: A6              AND     (HL)                ; isolate the sprite mirror bit
1D45: EE 80           XOR     $80                 ; toggle it: the leg wiggle that reads as climbing
1D47: B0              OR      B                   ; stamp in the climb frame the caller chose
1D48: 77              LD      (HL),A              

; The tail of a climb step: set marioOnLadder := 1, re-asserted on every climb step and
; cleared back to 0 only by the ladder-end handler, then copy Mario's just-computed
; position and sprite code into his four-byte hardware sprite record. Reached from the
; arm that has just rewritten his facing/climb sprite code and from the climb-sound arm.
; The record write is a tail hand-off, so its return is this routine's return.
markOnLadderAndCommitSprite:
1D49: 3E 01           LD      A,$01               
1D4B: 32 15 62        LD      ($6215),A           ; {hard.workRam+215} on a ladder; only the dismount clears this
1D4E: C3 A6 1D        JP      $1DA6               ; {code.writeMarioSpriteRecord}

; The ladder-centering phase of a climb step. It snaps marioX onto the ladder column by
; forcing the low three bits to 3: ladders sit on an 8-pixel grid, so this re-glues
; Mario to the column each centering step and corrects horizontal drift left over from
; walking before he mounted. It then toggles marioClimbSoundToggle and, on the frame it
; flips to 0, requests the footstep sound, so a step blips every other frame. Finally it
; re-asserts marioOnLadder and copies his updated position and sprite code into
; marioSpriteRecord, which is what picks up the just-centred X.
centerMarioAndCommitClimbStep:
1D51: 2D              DEC     L                   ; back up to Mario's column
1D52: 2D              DEC     L                   
1D53: 7E              LD      A,(HL)              
1D54: F6 03           OR      $03                 ; force the low bits to 3: the ladder's 8px grid
1D56: CB 97           RES     2,A                 
1D58: 77              LD      (HL),A              
1D59: 3A 24 62        LD      A,($6224)           ; {hard.workRam+224}
1D5C: EE 01           XOR     $01                 ; flip the climb-step toggle
1D5E: 32 24 62        LD      ($6224),A           ; {hard.workRam+224}
1D61: CC 8F 1D        CALL    Z,$1D8F             ; {code.triggerWalkSound} a footstep every other centring step
1D64: C3 49 1D        JP      $1D49               ; {code.markOnLadderAndCommitSprite}

; Finish a ladder climb that has reached either end -- he has climbed onto the girder at
; the top, or stepped off at the bottom. Three fixed stores and a sprite refresh,
; reading nothing at all: marioSpriteCode takes the ladder-end pose written FLAT, the
; facing bit deliberately dropped because at a ladder end Mario faces front; the climb
; half-step toggle is cleared; and marioOnLadder is cleared, which is the one bit
; distinguishing a dismount from a climb that continues. The shared refresh then copies
; his X, code, attribute and Y into his hardware sprite record, which is how the pose
; just stored reaches the screen.
endClimbAtLadderLimit:
1D67: 3E 06           LD      A,$06               ; the ladder-end pose, written flat: he faces front
1D69: 32 07 62        LD      ($6207),A           ; {hard.workRam+207}
1D6C: AF              XOR     A                   
1D6D: 32 19 62        LD      ($6219),A           ; {hard.workRam+219} clear the climb half-step toggle
1D70: 32 15 62        LD      ($6215),A           ; {hard.workRam+215} he is off the ladder now
1D73: C3 A6 1D        JP      $1DA6               ; {code.writeMarioSpriteRecord}

loc_1d76:
1D76: 3A 1A 62        LD      A,($621A)           ; {hard.workRam+21A} read the climb gate flag
1D79: A7              AND     A                   
1D7A: CA 8A 1D        JP      Z,$1D8A             ; {code.tickMoveStepTimer} flag clear: just tick the pacer down
1D7D: 32 19 62        LD      ($6219),A           ; {hard.workRam+219} mirror it into the neighbouring byte
1D80: 3A 1C 62        LD      A,($621C)           ; {hard.workRam+21C}
1D83: D6 13           SUB     $13                 ; take 19 off the far climb limit
1D85: 21 05 62        LD      HL,$6205            
1D88: BE              CP      (HL)                ; compare that against his row
1D89: D0              RET     NC                  ; still short of it: hold the pacer where it is

; Knock marioMoveStepTimer down by one, and that is all it does. It is the pacer that
; decides how long Mario holds each frame of his walking and climbing animation: while
; the timer is above zero the mover keeps showing its current sub-step, and on the frame
; it reaches zero the stepper reloads it and moves on to the next. Nothing here reloads
; it and nothing branches on the result -- the expiry decision is made later, by reading
; the timer back. It wraps if it was already zero.
tickMoveStepTimer:
1D8A: 21 0F 62        LD      HL,$620F            
1D8D: 35              DEC     (HL)                ; spend one frame of the current walk or climb sub-step
1D8E: C9              RET                         

; Ask for Mario's footstep sound. The walk sound is a discrete analog circuit behind a
; write-only latch, so game code asks for it through a work-RAM shadow instead: it stores
; a small frame count into the walk slot of sndTrigger and the per-vblank sound driver
; counts that value down, holding the latch asserted while it stays non-zero. This leaf
; stores 3 -- a three-frame hold, one short footstep blip. Whether a footstep happens at
; all was decided before the call.
triggerWalkSound:
1D8F: 3E 03           LD      A,$03               
1D91: 32 80 60        LD      ($6080),A           ; {hard.workRam+80} hold the footstep latch three frames
1D94: C9              RET                         

loc_1d95:
1D95: 32 25 62        LD      ($6225),A           ; {hard.workRam+225} commit the collection flag; callers pass 0
1D98: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227}
1D9B: 3D              DEC     A                   ; which board is this?
1D9C: C8              RET     Z                   ; 25m plays no pickup sound
1D9D: 21 8A 60        LD      HL,$608A            
1DA0: 36 0D           LD      (HL),$0D            ; queue the pickup tune
1DA2: 2C              INC     L                   
1DA3: 36 03           LD      (HL),$03            ; for three frames, over the background music
1DA5: C9              RET                         

; The convergence tail of the movement machine -- grounded, airborne, climbing, hammer
; and landed paths all finish here, so this is the single place Mario's just-computed
; state reaches the sprite shadow buffer. It fills marioSpriteRecord in the RECORD's
; field order: +0 <- marioX, +1 <- marioSpriteCode (tile plus the facing bit 7), +2 <-
; marioSpriteAttr, +3 <- marioY. That is not the order the sources sit at in memory --
; marioY comes before the sprite code and attribute -- so the reads are deliberately out
; of source order. A leaf.
writeMarioSpriteRecord:
1DA6: 21 4C 69        LD      HL,$694C            ; point at Mario's hardware sprite record
1DA9: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203}
1DAC: 77              LD      (HL),A              ; sprite X from his column
1DAD: 3A 07 62        LD      A,($6207)           ; {hard.workRam+207}
1DB0: 2C              INC     L                   
1DB1: 77              LD      (HL),A              ; sprite code: tile plus the facing bit
1DB2: 3A 08 62        LD      A,($6208)           ; {hard.workRam+208}
1DB5: 2C              INC     L                   
1DB6: 77              LD      (HL),A              ; his colour attribute
1DB7: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1DBA: 2C              INC     L                   
1DBB: 77              LD      (HL),A              ; sprite Y from his row
1DBC: C9              RET                         

; The router for the score-effect state machine held in effectState, writing nothing of
; its own -- pure control flow, a four-way branch on a small enum.
;   0 -- idle; the machine is dormant and nothing happens this frame.
;   1 -- the one-shot: arm effectTimer, spawn the effect sprite, advance the state to 2.
;   2 -- the countdown: work effectTimer down and, on expiry, tear the effect down and
;        return the machine to 0.
;   3 -- the machine's cold-start address, a defensive slot. No handler ever writes
;        it, so play never produces it; reaching it would restart the machine.
; The state byte only ever holds 0, 1 or 2 in play. What the effect DEPICTS is not
; established here -- the name is taken from the selector cell.
dispatchEffectState:
1DBD: 3A 40 63        LD      A,($6340)           ; {hard.workRam+340} read the effect machine's state
1DC0: EF              RST     $28                 ; branch through the four-slot table below

; ---- $1DC1-$1DC8: jump table ----
1DC1: 49 1E C9 1D 4A 1E 00 00

; The arm step of the score-popup machine -- the small points figure that appears on
; screen when the player earns an award. Two writes happen first and on EVERY path,
; before any choice is made: effectTimer is loaded with the count the display state will
; work back down, and effectState is stepped on to that display state, so entering here
; always commits the popup. Then exactly one award value is staged, by handing control to
; one of five setters chosen by the FIRST set bit of effectSelect's low three bits. Bit 0
; derives the tier from the remaining select bits; bit 1 is a fixed award; bit 2 draws
; its tier from random, so that award varies from event to event. With no bit set an
; award sound is cued and the tier comes from level -- level 1 the low award, level 2 the
; middle, every other level the high one.
armScorePopupAndSelectAward:
1DC9: 3E 40           LD      A,$40               
1DCB: 32 41 63        LD      ($6341),A           ; {hard.workRam+341} arm the 64-frame hold of the display state
1DCE: 3E 02           LD      A,$02               
1DD0: 32 40 63        LD      ($6340),A           ; {hard.workRam+340} step the machine on to that display state
1DD3: 3A 42 63        LD      A,($6342)           ; {hard.workRam+342} read the award selector
1DD6: 1F              RRA                         
1DD7: DA 70 3E        JP      C,$3E70             ; {code.pickAwardTierByObjectCount} bit 0: tier from the other bits
1DDA: 1F              RRA                         
1DDB: DA 00 1E        JP      C,$1E00             ; {code.stageAward300Popup} bit 1: the fixed 300 award
1DDE: 1F              RRA                         
1DDF: DA F5 1D        JP      C,$1DF5             ; {code.pickRandomAwardTier} bit 2: draw the tier from random
1DE2: 21 85 60        LD      HL,$6085            
1DE5: 36 03           LD      (HL),$03            ; no bit set: cue the award sound
1DE7: 3A 29 62        LD      A,($6229)           ; {hard.workRam+229} and take the tier from the level instead
1DEA: 3D              DEC     A                   
1DEB: CA 00 1E        JP      Z,$1E00             ; {code.stageAward300Popup} level 1 awards 300
1DEE: 3D              DEC     A                   
1DEF: CA 08 1E        JP      Z,$1E08             ; {code.stageAward500Popup} level 2 awards 500
1DF2: C3 10 1E        JP      $1E10               ; {code.stageAward800Popup} every later level awards 800

; Pick one of three score-popup tiers from two bits of random -- the random tail of the
; effect machine's arm-timer state. Bit 0 of random set selects the 500 tier; bit 0 clear
; with bit 1 set, the 800 tier; both clear, the 300 tier. The three sibling setters
; differ ONLY in the fixed pair each stages -- a sprite code and a deferred-task message
; -- before delegating to the shared popup feeder. This routine reads random and writes
; no memory of its own.
pickRandomAwardTier:
1DF5: 3A 18 60        LD      A,($6018)           ; {hard.workRam+18} read the rolling random byte
1DF8: 1F              RRA                         
1DF9: DA 08 1E        JP      C,$1E08             ; {code.stageAward500Popup} bit 0 set: the 500 tier
1DFC: 1F              RRA                         
1DFD: DA 10 1E        JP      C,$1E10             ; {code.stageAward800Popup} bit 1 instead: the 800 tier

; One of three sibling setters the award draw picks between on two bits of the rolling
; random byte; this is the arm both bits clear select. Its whole contribution is two
; constants -- sprite code 0x7D, stamped into the effect record's code byte, and the
; deferred-task message opcode 0 with argument 3 -- after which the shared handler does
; every observable thing: post the task and stamp the effect sprite's record. What the
; sprite code draws, and what the posted task does with its argument, are not
; established here.
stageAward300Popup:
1E00: 06 7D           LD      B,$7D               ; the 300 glyph tile
1E02: 11 03 00        LD      DE,$0003            ; score-add task, payload 3
1E05: C3 15 1E        JP      $1E15               ; {code.stageAwardPopupAtHitObject}

; The middle of three sibling award setters, each staging its own two constants before
; the shared effect handler runs. This one stages sprite code 0x7E and the task message
; (opcode 0, argument 5) -- opcode 0 is the score-add task and payload 5 is 500 points.
; The sprite code is stamped into the effect record by the handler's tail and the
; message posted onto the task ring; every memory write happens downstream. Staging the
; two constants is all this routine does.
stageAward500Popup:
1E08: 06 7E           LD      B,$7E               ; the 500 glyph tile
1E0A: 11 05 00        LD      DE,$0005            ; score-add task, payload 5
1E0D: C3 15 1E        JP      $1E15               ; {code.stageAwardPopupAtHitObject}

; The 800-point effect-sprite setter: load this award's fixed sprite code and its
; deferred task message (opcode 0, argument 8), then hand off to the shared award-popup
; feeder, which posts the task, reads the sprite's X and Y out of the effect parameter
; block, and stamps the 4-byte sprite record. The third of three constant setters in the
; same family -- the 300, 500 and 800 popups -- each loading its own pair and jumping
; into the same feeder. It reads nothing: it overwrites both parameters with constants
; whatever they held on entry.
stageAward800Popup:
1E10: 06 7F           LD      B,$7F               ; the 800 glyph tile
1E12: 11 08 00        LD      DE,$0008            ; score-add task, payload 8

; Where the fixed-value award setters converge: post the caller's deferred message, take
; the score popup's screen position out of a parameter block, and hand both on to the
; sprite stamp. The message goes onto the task ring fire-and-forget, and both it and the
; sprite code survive the post untouched. A pointer is then loaded from effectParamPtr;
; the popup's X is read from the block's first byte and that byte is CLEARED in place --
; a consume-once read, so the same block cannot place a second popup -- and the Y from
; the block's fourth byte. Control then goes to the sprite stamp, which turns the
; position and the sprite code into the popup's hardware sprite record and cues the
; accompanying sound.
stageAwardPopupAtHitObject:
1E15: CD 9F 30        CALL    $309F               ; {code.enqueueTask} post the score-add onto the task ring
1E18: 2A 43 63        LD      HL,($6343)          ; {hard.workRam+343} point at the effect's parameter block
1E1B: 7E              LD      A,(HL)              ; the popup's X
1E1C: 36 00           LD      (HL),$00            ; consume it, so the block cannot place a second popup
1E1E: 2C              INC     L                   
1E1F: 2C              INC     L                   
1E20: 2C              INC     L                   
1E21: 4E              LD      C,(HL)              ; the popup's Y, from the block's fourth byte
1E22: C3 36 1E        JP      $1E36               ; {code.stampScorePopupSprite}

; ---- $1E25-$1E27: data ----
1E25: 11 01 00

; Award points and stage the floating score glyph over Mario. It is entered with a
; MATCHED PAIR already chosen -- an award-table index and the glyph tile depicting the
; same amount -- so a bigger award always brings the bigger number sprite, which is what
; makes this a score POPUP and not a bare award. Three acts: enqueue a task carrying the
; opcode/index pair, so the score is credited later off the ring rather than here; write
; a 4-byte sprite record (X = marioX, code = the glyph tile, attribute 7, Y = marioY +
; 0x14) so the number appears just below Mario in his own column; and consult the board
; gate with a mask selecting 25m and 75m -- on those two, sndTrigger slot 5 is held for
; three frames, on the other two it returns silent.
awardScorePopup:
1E28: CD 9F 30        CALL    $309F               ; {code.enqueueTask} post the score-add for the matched award
1E2B: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1E2E: C6 14           ADD     A,$14               ; place the glyph 20 pixels below Mario
1E30: 4F              LD      C,A                 
1E31: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} and in his own column
1E34: 00              NOP                         
1E35: 00              NOP                         

; The shared tail of the effect machine: commit one 4-byte record into popupSprite from
; three caller-supplied bytes plus a hard-coded attribute -- +0 the X byte, +1 the
; sprite code, +2 a fixed 0x07, +3 the Y byte -- then assert a sound latch, but ONLY on
; the boards whose bit is set in the mask 0x05, that is 25m and 75m. On 50m and 100m the
; cue is simply not issued; the four record bytes are stored unconditionally on every
; board. popupSprite is a transient slot -- the companion state of the same machine
; blanks it again once the hold expires -- so what this stamps is on screen for a
; bounded stretch and then gone. Which sound the latch plays, and why only two of the
; four boards cue it, are not established here.
stampScorePopupSprite:
1E36: 21 30 6A        LD      HL,$6A30            ; point at the popup's sprite record
1E39: 77              LD      (HL),A              ; its X
1E3A: 2C              INC     L                   
1E3B: 70              LD      (HL),B              ; the number glyph's tile
1E3C: 2C              INC     L                   
1E3D: 36 07           LD      (HL),$07            ; fixed colour attribute
1E3F: 2C              INC     L                   
1E40: 71              LD      (HL),C              ; its Y
1E41: 3E 05           LD      A,$05               ; board mask: 25m and 75m
1E43: F7              RST     $30                 ; on 50m and 100m the cue below is skipped
1E44: 21 85 60        LD      HL,$6085            
1E47: 36 03           LD      (HL),$03            ; hold the award sound three frames

; The idle arm of the effect router, taken while effectState is 0: it does nothing at
; all. No inputs, no memory read or written, no branches -- the effect simply does not
; advance on such a frame. What the effect depicts is not established here.
effectStateIdle:
1E49: C9              RET                         ; the machine is dormant; nothing happens this frame

; The effect machine's state-2 arm: hold the effect on screen, then reset the machine.
; effectState is a four-way router -- 0 idle, 1 arm-timer, 2 this countdown, 3 reset. The
; arm-timer state loads effectTimer with 64 and advances the router to 2; this then
; decrements effectTimer once a frame and, while it is still non-zero, does nothing else.
; On the frame it reaches 0 the hold ends: clear popupSprite and drop effectState back to
; 0. A full hold is exactly 64 dispatches.
tickDispatcherCountdown:
1E4A: 21 41 63        LD      HL,$6341            
1E4D: 35              DEC     (HL)                ; work the 64-frame hold down
1E4E: C0              RET     NZ                  ; still holding, leave the effect on screen
1E4F: AF              XOR     A                   
1E50: 32 30 6A        LD      ($6A30),A           ; {hard.workRam+A30} blank the popup sprite
1E53: 32 40 63        LD      ($6340),A           ; {hard.workRam+340} and return the machine to idle
1E56: C9              RET                         

; Mario's per-frame board-won check, routed by board, which defers to the arm that
; stamps the win on the frame the condition is met. On 100m the win is the rivet count,
; not his position, so that arm defers entirely and his coordinates are never even read.
; On the ODD boards -- 25m AND 75m together, since the selector is board bit 0, not 25m
; alone -- the win is positional, tested against marioY at the rescue row near Pauline.
; On the remaining board, 50m, it is won once he has climbed above a fixed line; screen
; Y DECREASES as he climbs, so "above" means a Y below 0x51, and at or below it nothing
; changes this frame. On that won arm Mario's X high bit picks the sprite facing he is
; left standing in. The return is a protocol: true means the board is not won and the
; movement cascade continues, false means it was won and the cascade has already
; unwound, so the caller must NOT continue.
checkBoardWonByType:
1E57: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} read the board being played
1E5A: CB 57           BIT     2,A                 ; board 4, where the win is the rivets
1E5C: C2 80 1E        JP      NZ,$1E80            ; {code.completeRivetBoardWhenCleared} his position is never read
1E5F: 1F              RRA                         ; board bit 0 picks the odd boards, 25m and 75m
1E60: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1E63: DA 7A 1E        JP      C,$1E7A             ; {code.completeBoardWhenMarioReachesRescueRow} 25m and 75m
1E66: FE 51           CP      $51                 ; 50m: has he climbed above the win line?
1E68: D0              RET     NC                  ; not yet; the movement cascade carries on
1E69: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} his X's high bit picks the facing he is left in
1E6C: 17              RLA                         

loc_1e6d:
1E6D: 3E 00           LD      A,$00               
1E6F: DA 74 1E        JP      C,$1E74             ; {code.loc_1e74}
1E72: 3E 80           LD      A,$80               

loc_1e74:
1E74: 32 4D 69        LD      ($694D),A           ; {hard.workRam+94D} stamp the facing he is left standing in
1E77: C3 85 1E        JP      $1E85               ; {code.enterBoardAdvanceAndUnwind}

; The rescue-row test inside Mario's per-frame position check, and it serves 25m AND 75m
; -- not the girder board alone. The dispatcher above peels 100m off to the rivet arm
; first, then routes on the LOW BIT of board, which selects the two ODD boards; 50m
; falls through to a different threshold test entirely. It is reached once the earlier
; column and row checks have narrowed Mario to the situation near Pauline, and it is
; handed his screen Y. Y DECREASES as he climbs and 0x31 is the rescue-row line: at or
; below that line nothing changes this frame; above it the board is WON, and control
; falls into the board-won tail, which stamps Mario's sprite facing, commits the
; board-advance sub-state, and unwinds out of the movement cascade so nothing else runs
; that frame.
completeBoardWhenMarioReachesRescueRow:
1E7A: FE 31           CP      $31                 ; is he above the rescue row near Pauline?
1E7C: D0              RET     NC                  ; not yet; carry on with the frame
1E7D: C3 6D 1E        JP      $1E6D               ; {code.loc_1e6d}

; On the rivet board, win the board the frame its last rivet is gone. Reached only while
; 100m is the board being played, from Mario's per-frame position check. It reads
; rivetsLeft: while any remain the board is not won, so it reports "carry on" and the
; movement cascade continues normally; on the frame the count reaches zero it hands off
; to the board-advance step, which commits the board-cleared sub-state and unwinds out of
; the cascade. It writes nothing of its own -- the rivet count is only read.
completeRivetBoardWhenCleared:
1E80: 3A 90 62        LD      A,($6290)           ; {hard.workRam+290} how many rivets are still standing?
1E83: A7              AND     A                   
1E84: C0              RET     NZ                  ; any left and the board is not won

; Commit "this board is complete". One store -- gameSubstate := the board-cleared/advance
; sub-state, which plays the board-advance interlude and steps on to the next board --
; and then an unwind that returns one extra level up, straight out of the movement
; cascade, so no further movement is processed on the frame the board is won. Reached
; from either board-clear condition: a rivet board whose last rivet has been collected,
; or any non-rivet board where Mario has climbed to the rescue row near Pauline.
enterBoardAdvanceAndUnwind:
1E85: 3E 16           LD      A,$16               
1E87: 32 0A 60        LD      ($600A),A           ; {hard.workRam+A} enter the board-cleared sub-state
1E8A: E1              POP     HL                  ; drop a level: abandon the rest of the movement cascade
1E8B: C9              RET                         

; The per-frame gate on the hit-effect latch, called near the head of the shared update
; cascade. With the latch clear the caller runs its ordinary frame -- the long run of
; updates starting with the movement machine. With it set the frame is spent on ONE beat
; of the effect animation instead, and the caller is told to abandon everything else, so
; the latch suspends gameplay for the effect's duration and play resumes on the frame
; the effect tears itself down. ANY nonzero value counts as set: this is a plain zero
; test, not a bit test and not a comparison against 1, and the distinction is real
; because the cell's other reader tests only bit 0. The latch is raised when the swung
; hammer strikes a hazard, by a routine that runs LATER in the same cascade -- so a hit
; recorded on one frame first suspends play on the NEXT -- and it is cleared on the
; effect sequence's teardown beat, the only way this gate reopens.
runHitEffectInsteadOfPlay:
1E8C: 3A 50 63        LD      A,($6350)           ; {hard.workRam+350} read the hit-effect latch
1E8F: A7              AND     A                   
1E90: C8              RET     Z                   ; clear: let the caller run its ordinary frame
1E91: CD 96 1E        CALL    $1E96               ; {code.dispatchEffectSequenceStep} set: spend the frame on it

loc_1e94:
1E94: E1              POP     HL                  ; and make the caller abandon the rest of its update
1E95: C9              RET                         

; The router for the effect-sequence step machine in effectSeqState, run once a frame
; while the effect is armed. It hands the frame to that step's handler and writes
; nothing itself.
;   0 -- the one-shot that consumes the collision record, builds the effect sprite,
;        fires its priority sound, and advances to 1.
;   1 -- the two-stage rate divider that flashes the sprite's tile between two codes
;        and, after four beats, advances to 2.
;   2 -- the divider that marches the tile forward and, when it runs out, resets to 0
;        and re-arms the parent effect machine.
; The step index is doubled at 8 bits to reach a two-byte table slot, so 128, 129 and
; 130 alias steps 0, 1 and 2 -- unreachable in play, since the counters only produce
; 0-2.
dispatchEffectSequenceStep:
1E96: 3A 45 63        LD      A,($6345)           ; {hard.workRam+345} read the effect sequence's step
1E99: EF              RST     $28                 ; branch through the three-slot table below

; ---- $1E9A-$1E9F: jump table ----
1E9A: A0 1E 09 1F 23 1F

; Step 0 of the effect sequence: spawn the hit-effect sprite from the record the board
; collision search left behind -- collidedObjectBase, collidedObjectStride and
; collidedObjectIndex. Four acts. Classify the array by the high byte of its base, i.e.
; by which page it lives on, and pick the matching group of source sprite records. Walk
; both records out to the hit index, the object by its own stride and the sprite by the
; fixed 4-byte one. Deactivate the object that was hit and read its +0x15 field to pick
; the effect variant into effectSelect -- zero selects 2, anything else 4. Then build
; effectSprite out of the source record, taking its +0 and +3 fields and blanking +0 in
; place so the source sprite stops being drawn, stamp the fixed effect tile and
; attribute, advance the sequence, reload its inner and outer counters, and fire the
; priority sound for three frames.
buildEffectSprite:
1EA0: 3A 52 63        LD      A,($6352)           ; {hard.workRam+352} which page the hit object's array lives on
1EA3: FE 65           CP      $65                 
1EA5: 21 B8 69        LD      HL,$69B8            ; the page-0x65 array's sprite group
1EA8: CA B4 1E        JP      Z,$1EB4             ; {code.loc_1eb4}
1EAB: 21 D0 69        LD      HL,$69D0            ; a lower page's sprite group
1EAE: DA B4 1E        JP      C,$1EB4             ; {code.loc_1eb4}
1EB1: 21 80 69        LD      HL,$6980            ; a higher page: the barrel sprites

loc_1eb4:
1EB4: DD 2A 51 63     LD      IX,($6351)          ; {hard.workRam+351} the hit object's array base
1EB8: 16 00           LD      D,$00               
1EBA: 3A 53 63        LD      A,($6353)           ; {hard.workRam+353} that array's record stride
1EBD: 5F              LD      E,A                 
1EBE: 01 04 00        LD      BC,$0004            ; sprite records are a fixed four bytes
1EC1: 3A 54 63        LD      A,($6354)           ; {hard.workRam+354} the hit record's index within the array
1EC4: A7              AND     A                   
1EC5: CA CF 1E        JP      Z,$1ECF             ; {code.loc_1ecf} index 0: both cursors are already there

loc_1ec8:
1EC8: 09              ADD     HL,BC               ; walk the sprite cursor out to the hit index
1EC9: DD 19           ADD     IX,DE               ; and the object cursor by its own stride
1ECB: 3D              DEC     A                   
1ECC: C2 C8 1E        JP      NZ,$1EC8            ; {code.loc_1ec8}

loc_1ecf:
1ECF: DD 36 00 00     LD      (IX+$00),$00        ; deactivate the object that was hit
1ED3: DD 7E 15        LD      A,(IX+$15)          ; its kind field picks the effect variant
1ED6: A7              AND     A                   
1ED7: 3E 02           LD      A,$02               ; zero there selects variant 2
1ED9: CA DE 1E        JP      Z,$1EDE             ; {code.loc_1ede}
1EDC: 3E 04           LD      A,$04               ; anything else selects variant 4

loc_1ede:
1EDE: 32 42 63        LD      ($6342),A           ; {hard.workRam+342} stage the variant for the award setter
1EE1: 01 2C 6A        LD      BC,$6A2C            ; point at the effect sprite's record
1EE4: 7E              LD      A,(HL)              ; take the hit sprite's X
1EE5: 36 00           LD      (HL),$00            ; blank it, so the source stops being drawn
1EE7: 02              LD      (BC),A              ; the effect appears where the object was
1EE8: 0C              INC     C                   
1EE9: 2C              INC     L                   
1EEA: 3E 60           LD      A,$60               
1EEC: 02              LD      (BC),A              ; the effect's tile code
1EED: 0C              INC     C                   
1EEE: 2C              INC     L                   
1EEF: 3E 0C           LD      A,$0C               
1EF1: 02              LD      (BC),A              ; its colour attribute
1EF2: 0C              INC     C                   
1EF3: 2C              INC     L                   
1EF4: 7E              LD      A,(HL)              ; the hit sprite's Y
1EF5: 02              LD      (BC),A              ; copied across too
1EF6: 21 45 63        LD      HL,$6345            
1EF9: 34              INC     (HL)                ; advance the sequence to its flashing step
1EFA: 2C              INC     L                   
1EFB: 36 06           LD      (HL),$06            ; reload the inner beat divider
1EFD: 2C              INC     L                   
1EFE: 36 05           LD      (HL),$05            ; and the outer step counter
1F00: 21 8A 60        LD      HL,$608A            
1F03: 36 06           LD      (HL),$06            ; queue the hit tune over the music
1F05: 2C              INC     L                   
1F06: 36 03           LD      (HL),$03            ; for three frames
1F08: C9              RET                         

; Effect-sequence step 1: a two-stage rate divider that flashes a sprite on most beats
; and hands the sequence on every fourth. effectSeqInner counts down on every dispatch
; and the routine returns until it drains, once every six calls. On that beat it reloads
; the inner counter to 6 and ticks effectSeqOuter: while the outer counter is still
; running it XORs the low bit of the effect sprite's tile-code byte, so the tile
; oscillates between two consecutive codes; once every four beats, when the outer counter
; drains instead, it reloads that counter to 4 and advances effectSeqState, moving the
; sequence on to its next step. So the sprite blinks at one-sixth of the dispatch rate
; and the sequence steps forward at one twenty-fourth. What the effect depicts on screen
; is not established here.
flashEffectSpriteThenAdvanceSequence:
1F09: 21 46 63        LD      HL,$6346            
1F0C: 35              DEC     (HL)                ; one beat in six
1F0D: C0              RET     NZ                  
1F0E: 36 06           LD      (HL),$06            ; reload the beat divider
1F10: 2C              INC     L                   
1F11: 35              DEC     (HL)                ; tick the outer step counter
1F12: CA 1D 1F        JP      Z,$1F1D             ; {code.loc_1f1d} four beats done: hand the sequence on
1F15: 21 2D 6A        LD      HL,$6A2D            ; point at the effect sprite's tile code
1F18: 7E              LD      A,(HL)              
1F19: EE 01           XOR     $01                 ; flip between the two tiles of the pair
1F1B: 77              LD      (HL),A              
1F1C: C9              RET                         

loc_1f1d:
1F1D: 36 04           LD      (HL),$04            ; reload the outer counter
1F1F: 2D              DEC     L                   
1F20: 2D              DEC     L                   
1F21: 34              INC     (HL)                ; advance the sequence to its next step
1F22: C9              RET                         

; Step 2 of the effect sequence: a two-stage rate divider. effectSeqInner ticks down on
; every dispatch and the routine returns until it drains -- one beat in twelve. On a
; beat it reloads effectSeqInner to 12 and ticks effectSeqOuter down: while that is
; still running it increments the effect sprite's code byte, so the tile MARCHES forward
; one step per beat, which is what distinguishes this step from its sibling, which
; flashes between two tiles. When effectSeqOuter drains it is NOT reloaded; instead the
; sequence is torn down -- effectSeqState back to 0, effectState re-armed to 1,
; effectParamPtr aimed back at effectSprite, and a shared scratch cell cleared, which is
; what hands the per-frame cascade back to ordinary play. What the effect DEPICTS is not
; claimed -- only the byte-level animation and the teardown.
animateEffectSpriteThenRearmEffect:
1F23: 21 46 63        LD      HL,$6346            
1F26: 35              DEC     (HL)                ; one beat in twelve
1F27: C0              RET     NZ                  
1F28: 36 0C           LD      (HL),$0C            ; reload the beat divider
1F2A: 2C              INC     L                   
1F2B: 35              DEC     (HL)                ; tick the outer step counter
1F2C: CA 34 1F        JP      Z,$1F34             ; {code.loc_1f34} the counter drains: tear the effect down
1F2F: 21 2D 6A        LD      HL,$6A2D            ; point at the effect sprite's tile code
1F32: 34              INC     (HL)                ; march the tile forward one step
1F33: C9              RET                         

loc_1f34:
1F34: 2D              DEC     L                   
1F35: 2D              DEC     L                   
1F36: AF              XOR     A                   
1F37: 77              LD      (HL),A              ; reset the sequence to its first step
1F38: 32 50 63        LD      ($6350),A           ; {hard.workRam+350} drop the latch, handing the frame back to play
1F3B: 3C              INC     A                   
1F3C: 32 40 63        LD      ($6340),A           ; {hard.workRam+340} re-arm the parent effect machine
1F3F: 21 2C 6A        LD      HL,$6A2C            
1F42: 22 43 63        LD      ($6343),HL          ; {hard.workRam+343} point it back at the effect sprite
1F45: C9              RET                         

; When marioStartFall is set -- the slope and ledge contact check raises it the moment
; there is no girder under Mario's foot -- this consumes the trigger and rebuilds his
; motion state for a fall that starts from rest: marioXFrac and marioYFrac and the whole
; airborne velocity and elapsed-frame block are cleared, so the fall begins at zero
; speed; marioAirborne is set, which is what the movement machine reads next frame;
; marioAirLandcheck is armed at once, so the drop is evaluated from the very next
; airborne frame rather than waiting for a jump to near its apex; and marioY is
; snapshotted into marioAirStartY, the value the landing code measures the depth
; against. The trigger is a one-shot cleared here, and any non-zero value launches the
; same fall. With it clear this does nothing at all.
beginMarioFall:
1F46: 3A 21 62        LD      A,($6221)           ; {hard.workRam+221} read the fall trigger
1F49: A7              AND     A                   
1F4A: C8              RET     Z                   ; no ground went away this frame
1F4B: AF              XOR     A                   
1F4C: 32 04 62        LD      ($6204),A           ; {hard.workRam+204} the fall starts from a whole pixel
1F4F: 32 06 62        LD      ($6206),A           ; {hard.workRam+206}
1F52: 32 21 62        LD      ($6221),A           ; {hard.workRam+221} consume the one-shot trigger
1F55: 32 10 62        LD      ($6210),A           ; {hard.workRam+210} no horizontal speed: he drops straight down
1F58: 32 11 62        LD      ($6211),A           ; {hard.workRam+211}
1F5B: 32 12 62        LD      ($6212),A           ; {hard.workRam+212} and no vertical speed: gravity alone
1F5E: 32 13 62        LD      ($6213),A           ; {hard.workRam+213}
1F61: 32 14 62        LD      ($6214),A           ; {hard.workRam+214} arc frame count back to zero
1F64: 3C              INC     A                   
1F65: 32 16 62        LD      ($6216),A           ; {hard.workRam+216} the mover drives him airborne from next frame
1F68: 32 1F 62        LD      ($621F),A           ; {hard.workRam+21F} evaluate the drop from the first frame
1F6B: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
1F6E: 32 0E 62        LD      ($620E),A           ; {hard.workRam+20E} remember the height he fell from
1F71: C9              RET                         

; The head of the 25m barrel engine. One test, then a hand-off: if board is not the
; girder board it returns at once, which is why three quarters of the game never runs the
; walk and why objArray67 stays identically zero elsewhere. On 25m it seeds the walk's
; four working values -- the record it starts on, the sprite cursor, the record stride,
; and the count of ten -- and falls into the walk. The walk advances the record pointer
; by one stride and the sprite cursor by four bytes each pass, so over the ten iterations
; the cursor sweeps exactly the ten stride-4 records at actorSprites; only its low byte
; is incremented, so the sweep cannot leave that page.
update25mBarrels:
1F72: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} read the board being played
1F75: 3D              DEC     A                   
1F76: C0              RET     NZ                  ; barrels only roll on 25m
1F77: DD 21 00 67     LD      IX,$6700            ; the first of the ten barrel records
1F7B: 21 80 69        LD      HL,$6980            ; the sprite staging cursor
1F7E: 11 20 00        LD      DE,$0020            ; records are 32 bytes apart
1F81: 06 0A           LD      B,$0A               ; ten slots to service

; The barrel walk's per-slot gate, at the head of every pass round the loop. It reads one
; byte, the record's active flag, and either hands the whole record to the motion
; dispatch -- which takes the sprite staging cursor over with it -- or skips the slot,
; the skip's whole job being to step that cursor over the four bytes this slot did not
; write. It moves three of them; the fourth belongs to the between-slots step both halves
; converge on, so the cursor lands on a record boundary whichever half ran. THE TEST IS
; EQUALITY WITH 1, not a bit test, and the difference is a mechanic: the byte takes three
; values live -- 0 empty, 1 running, 2 claimed -- so a record the release path has
; stamped with 2 is skipped exactly as an empty one is, and does not reach the motion
; dispatch until it is actually running.
serviceBarrelSlotIfLive:
1F83: DD 7E 00        LD      A,(IX+$00)          ; the slot's active flag
1F86: 3D              DEC     A                   
1F87: CA 93 1F        JP      Z,$1F93             ; {code.advanceBarrelMotion} only 1 runs; 2 is claimed and skipped
1F8A: 2C              INC     L                   ; step the cursor over the bytes this slot did not write
1F8B: 2C              INC     L                   
1F8C: 2C              INC     L                   

loc_1f8d:
1F8D: 2C              INC     L                   ; the fourth step, landing on the next record
1F8E: DD 19           ADD     IX,DE               ; on to the next barrel record
1F90: 10 F1           DJNZ    $1F83               ; {code.serviceBarrelSlotIfLive} round again while slots remain
1F92: C9              RET                         

; Send a live barrel to its motion arm for this frame. It reads two record bytes, writes
; nothing, and jumps to one of five arms, each of which does the record's actual
; movement and rejoins the walk; every arm is a tail jump, so this routine's result IS
; the moved barrel. TWO FIELDS, AND THE FIRST OUTRANKS THE SECOND: the select byte
; (record +1) is tested first and for EQUALITY WITH 1, and only if that fails are the
; low three bits of the mode byte (record +2) tested, lowest first, first set bit wins.
; A record can arrive with the select byte at 1 over an already-set mode byte, and that
; priority is the only thing deciding which arm it gets. The mode byte's bits above bit
; 2 are never examined, so a record with mode 8 and one with mode 0 are
; indistinguishable here.
advanceBarrelMotion:
1F93: DD 7E 01        LD      A,(IX+$01)          ; the select byte, which outranks the mode bits
1F96: 3D              DEC     A                   
1F97: CA EC 20        JP      Z,$20EC             ; {code.advanceFallingBarrel} 1: it is falling between girders
1F9A: DD 7E 02        LD      A,(IX+$02)          ; otherwise the mode bits, lowest first
1F9D: 1F              RRA                         
1F9E: DA AC 1F        JP      C,$1FAC             ; {code.loc_1fac} bit 0: it is walking down a ladder
1FA1: 1F              RRA                         
1FA2: DA E5 1F        JP      C,$1FE5             ; {code.stepBarrelRight} bit 1: roll one pixel right
1FA5: 1F              RRA                         
1FA6: DA EF 1F        JP      C,$1FEF             ; {code.stepBarrelLeft} bit 2: roll one pixel left
1FA9: C3 53 20        JP      $2053               ; {code.loc_2053} no bit set: carry it along its arc

loc_1fac:
1FAC: D9              EXX                         ; the arms work in the alternate bank; the tail swaps back
1FAD: DD 34 05        INC     (IX+$05)            ; one row further down the ladder
1FB0: DD 7E 17        LD      A,(IX+$17)          ; the row this descent stops on
1FB3: DD BE 05        CP      (IX+$05)            
1FB6: C2 CE 1F        JP      NZ,$1FCE            ; {code.advanceBarrelTileAnimation} not there yet, so just animate
1FB9: DD 7E 15        LD      A,(IX+$15)          
1FBC: 07              RLCA                        
1FBD: 07              RLCA                        
1FBE: C6 15           ADD     A,$15               
1FC0: DD 77 07        LD      (IX+$07),A          ; stamp the arrival sprite code on the frame it lands
1FC3: DD 7E 02        LD      A,(IX+$02)          
1FC6: EE 07           XOR     $07                 ; flip the arm-select bits: hand it to a roll arm
1FC8: DD 77 02        LD      (IX+$02),A          
1FCB: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

; Step one barrel record's animation prescaler (+0x0f) and, on the visit it runs out,
; flip the LOWEST bit of the barrel's sprite code -- swapping it to the other tile of an
; adjacent pair -- and reload the prescaler to 4. The walk above visits an active record
; once a frame, so each tile is held four frames. The prescaler is stepped as a byte, so
; a value of 0 goes to 255 rather than expiring; only exactly zero is expiry. That
; lowest bit is a CHOICE OF TILE, not a way of drawing one: the raster flip lives in bit
; 7 of the same byte and is never touched here. What the two tiles of a pair depict is
; not established.
advanceBarrelTileAnimation:
1FCE: DD 7E 0F        LD      A,(IX+$0F)          ; the tile-hold prescaler
1FD1: 3D              DEC     A                   
1FD2: C2 DF 1F        JP      NZ,$1FDF            ; {code.loc_1fdf} still holding this tile
1FD5: DD 7E 07        LD      A,(IX+$07)          
1FD8: EE 01           XOR     $01                 ; swap to the other tile of the pair
1FDA: DD 77 07        LD      (IX+$07),A          
1FDD: 3E 04           LD      A,$04               ; hold the new tile four frames

loc_1fdf:
1FDF: DD 77 0F        LD      (IX+$0F),A          ; store the prescaler back
1FE2: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

; The +X motion arm of the barrel walk: bank the register file, load the two values the
; shared roll tail consumes, and increment the record's X by one -- the sign of that
; increment is the direction in the name. The staged step selector reaches the girder
; snap, and 1 is the value that snaps on the offset-0 edge of a 16-pixel girder cell,
; which is the edge a barrel walking X upwards crosses first; the mirror arm passes the
; offset-15 value instead. The second value folds into a packed sprite-orientation
; lookup; all that is derived here is that this arm passes 0. Every motion arm works in
; the alternate bank and none swaps back -- the swap happens where the arms converge, and
; it is what restores the walk's own loop state.
stepBarrelRight:
1FE5: D9              EXX                         ; into the arms' own register bank
1FE6: 01 00 01        LD      BC,$0100            ; snap on the offset-0 cell edge; direction code 0
1FE9: DD 34 03        INC     (IX+$03)            ; one pixel right
1FEC: C3 F6 1F        JP      $1FF6               ; {code.advanceRollingBarrel}

; The -X motion arm of the barrel walk: bank the register file, stage the two direction
; constants the shared roll tail consumes, and decrement this barrel's X. The walk keeps
; its loop state in the main bank, so every motion arm works in the alternate one. The
; first constant, 255, is the girder snap's step selector: the snap moves Y one pixel
; along the slope only on the frame X lands on a 16-pixel cell boundary, and the selector
; picks which edge counts -- 1 fires at cell offset 0, any other value at offset 15 -- so
; a barrel walking X downwards, which enters a new cell at offset 15, wants the not-1
; selector. The mirror arm is this routine with the increment and the constants 1 and 0;
; the second constant is a direction code the sprite-orientation refresh folds into its
; lookup selector as 3 OR code.
stepBarrelLeft:
1FEF: D9              EXX                         
1FF0: 01 04 FF        LD      BC,$FF04            ; snap on the offset-15 cell edge; direction code 4
1FF3: DD 35 03        DEC     (IX+$03)            ; one pixel left

; The shared tail of the two roll arms: carry the barrel one step along its current run,
; then route it. Both entry arms have already moved the record's X by one. One X value
; in eight (X = 3 mod 8) goes straight out to the LADDER DETOUR before any of the work
; below, which is why this tail must not be described as "along the girder". Otherwise
; the barrel is re-glued to the girder slope, its sprite orientation is refreshed, and
; the bottom-of-playfield gate decides: below the low edge (28) the low-end arm stamps
; the leftward step; inside the window it goes straight to the shared sprite publish,
; which is the overwhelming majority of passes; at or past the high edge (228) the
; mirrored rightward step of +96, in the record's 1/256-pixel units, is stamped into its
; own step bytes. The slope snap is handed a coordinate three pixels off the record's Y
; and the three go back on afterwards; what those three pixels are is not determined
; here.
advanceRollingBarrel:
1FF6: DD 66 03        LD      H,(IX+$03)          ; the barrel's column
1FF9: DD 6E 05        LD      L,(IX+$05)          ; and its row
1FFC: 7C              LD      A,H                 
1FFD: E6 07           AND     $07                 
1FFF: FE 03           CP      $03                 ; one column in eight is a ladder position
2001: CA 5F 21        JP      Z,$215F             ; {code.loc_215f} take the ladder detour before the work below
2004: 2D              DEC     L                   ; the snap works three pixels off the record's row
2005: 2D              DEC     L                   
2006: 2D              DEC     L                   
2007: CD 33 23        CALL    $2333               ; {code.snapYToGirder} re-glue the barrel to the girder slope

loc_200a:
200A: 2C              INC     L                   ; put the three pixels back on
200B: 2C              INC     L                   
200C: 2C              INC     L                   
200D: 7D              LD      A,L                 
200E: DD 77 05        LD      (IX+$05),A          ; commit the slope-corrected row
2011: CD DE 23        CALL    $23DE               ; {code.advanceBarrelSpriteOrientation} the two sprite mirror bits
2014: CD B4 24        CALL    $24B4               ; {code.retireBarrelIntoOilDrum} it can take the record over
2017: DD 7E 03        LD      A,(IX+$03)          
201A: FE 1C           CP      $1C                 ; past the low edge of the playfield?
201C: DA 2F 20        JP      C,$202F             ; {code.loc_202f} yes: stamp the leftward step
201F: FE E4           CP      $E4                 ; still short of the high edge?
2021: DA BA 21        JP      C,$21BA             ; {code.publishBarrelSprite} mid-playfield: just publish the sprite
2024: AF              XOR     A                   
2025: DD 77 10        LD      (IX+$10),A          ; at the high edge: stamp the rightward step, +96
2028: DD 36 11 60     LD      (IX+$11),$60        
202C: C3 38 20        JP      $2038               ; {code.loc_2038}

loc_202f:
202F: AF              XOR     A                   ; at the low edge instead
2030: DD 36 10 FF     LD      (IX+$10),$FF        ; stamp the leftward step, -96
2034: DD 36 11 A0     LD      (IX+$11),$A0        

loc_2038:
2038: DD 36 12 FF     LD      (IX+$12),$FF        ; arm the fall: initial vertical velocity -16
203C: DD 36 13 F0     LD      (IX+$13),$F0        
2040: DD 77 14        LD      (IX+$14),A          ; arc frame count back to zero
2043: DD 77 0E        LD      (IX+$0E),A          ; and the arm's sub-state counter
2046: DD 77 04        LD      (IX+$04),A          ; clear both coordinate fractions
2049: DD 77 06        LD      (IX+$06),A          
204C: DD 36 02 08     LD      (IX+$02),$08        ; no arm-select bit set: the arc arm takes it next
2050: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

loc_2053:
2053: D9              EXX                         
2054: CD 9C 23        CALL    $239C               ; {code.stepBallisticMotion} carry the barrel a frame along its arc
2057: CD 2F 2A        CALL    $2A2F               ; {code.loc_2a2f} probe the girder under it

loc_205a:
205A: A7              AND     A                   
205B: C2 83 20        JP      NZ,$2083            ; {code.loc_2083} contact: it has landed on a girder
205E: DD 7E 03        LD      A,(IX+$03)          
2061: C6 08           ADD     A,$08               ; within eight pixels of X = 0, either side of the wrap?
2063: FE 10           CP      $10                 
2065: DA 79 20        JP      C,$2079             ; {code.loc_2079} yes: retire the record
2068: CD B4 24        CALL    $24B4               ; {code.retireBarrelIntoOilDrum} it can take the record over
206B: DD 7E 10        LD      A,(IX+$10)          
206E: E6 01           AND     $01                 ; the step's direction bit
2070: 07              RLCA                        
2071: 07              RLCA                        ; becomes the orientation selector, 0 or 4
2072: 4F              LD      C,A                 
2073: CD DE 23        CALL    $23DE               ; {code.advanceBarrelSpriteOrientation} the two sprite mirror bits
2076: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

loc_2079:
2079: AF              XOR     A                   
207A: DD 77 00        LD      (IX+$00),A          ; free the slot
207D: DD 77 03        LD      (IX+$03),A          ; park it at X = 0, so it is not drawn where it died
2080: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

loc_2083:
2083: DD 34 0E        INC     (IX+$0E)            ; count one step further into the landing sub-state
2086: DD 7E 0E        LD      A,(IX+$0E)          
2089: 3D              DEC     A                   
208A: CA A2 20        JP      Z,$20A2             ; {code.loc_20a2} first step: decide whether it turns round
208D: 3D              DEC     A                   
208E: CA C3 20        JP      Z,$20C3             ; {code.loc_20c3} second step: bounce it
2091: DD 7E 10        LD      A,(IX+$10)          ; the whole-pixel half of its horizontal step
2094: 3D              DEC     A                   
2095: 3E 04           LD      A,$04               ; select the left-walk arm
2097: C2 9C 20        JP      NZ,$209C            ; {code.loc_209c}
209A: 3E 02           LD      A,$02               ; a rightward whole pixel: select the right-walk arm

loc_209c:
209C: DD 77 02        LD      (IX+$02),A          ; put it on a one-pixel-a-frame walk next frame
209F: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

loc_20a2:
20A2: DD 7E 15        LD      A,(IX+$15)          ; the barrel's kind
20A5: A7              AND     A                   
20A6: C2 B5 20        JP      NZ,$20B5            ; {code.loc_20b5} the alternate kind turns round unasked
20A9: 21 05 62        LD      HL,$6205            ; point at Mario's row
20AC: DD 7E 05        LD      A,(IX+$05)          
20AF: D6 16           SUB     $16                 ; 22 rows of clearance below him
20B1: BE              CP      (HL)                
20B2: D2 C3 20        JP      NC,$20C3            ; {code.loc_20c3} come to rest well below him: let it carry on

loc_20b5:
20B5: DD 7E 10        LD      A,(IX+$10)          ; the whole-pixel half of its horizontal step
20B8: A7              AND     A                   
20B9: C2 E1 20        JP      NZ,$20E1            ; {code.loc_20e1} anything but a sub-pixel rightward step goes right
20BC: DD 77 11        LD      (IX+$11),A          
20BF: DD 36 10 FF     LD      (IX+$10),$FF        ; send it off leftward at one pixel a frame

loc_20c3:
20C3: CD 07 24        CALL    $2407               ; {code.loc_2407} reflect the arc: 16*frames minus the launch speed
20C6: CB 3C           SRL     H                   
20C8: CB 1D           RR      L                   
20CA: CB 3C           SRL     H                   ; a quarter of it: it comes back slower than it arrived
20CC: CB 1D           RR      L                   
20CE: DD 74 12        LD      (IX+$12),H          ; the damped speed becomes the new launch speed
20D1: DD 75 13        LD      (IX+$13),L          
20D4: AF              XOR     A                   
20D5: DD 77 14        LD      (IX+$14),A          ; restart the arc's frame count
20D8: DD 77 04        LD      (IX+$04),A          ; and clear both coordinate fractions
20DB: DD 77 06        LD      (IX+$06),A          
20DE: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

loc_20e1:
20E1: DD 36 10 01     LD      (IX+$10),$01        ; send it off rightward at one pixel a frame
20E5: DD 36 11 00     LD      (IX+$11),$00        
20E9: C3 C3 20        JP      $20C3               ; {code.loc_20c3}

; Carry a barrel one frame further down its fall between girders, and decide whether
; this is a frame on which it may test the girder underneath it. The record keeps a
; snapshot of where the barrel was when it last registered a girder contact, and the
; probe is held off until its Y has moved 26 past that snapshot -- a re-arm distance, so
; a barrel cannot immediately re-detect the girder it just landed on. Under that
; distance control goes to the end-of-range retirement check, which only asks whether
; the barrel has run off the edge; past it, a slope tile underneath takes the contact
; arm and no contact the other. The gravity ramp restarts at each landing, which is what
; makes this a fall and not a bounce. The re-arm subtraction is 8-bit, so a barrel whose
; Y is under 26 wraps to a large value and PASSES the gate instead of failing it.
advanceFallingBarrel:
20EC: D9              EXX                         
20ED: CD 9C 23        CALL    $239C               ; {code.stepBallisticMotion} carry the barrel one frame further down
20F0: 7C              LD      A,H                 ; the freshly stepped row
20F1: D6 1A           SUB     $1A                 ; the 26-pixel contact re-arm distance
20F3: DD 46 19        LD      B,(IX+$19)          ; the row of its last girder contact
20F6: B8              CP      B                   
20F7: DA 04 21        JP      C,$2104             ; {code.retireBarrelAtEndOfRange} too close to re-probe the girder
20FA: CD 2F 2A        CALL    $2A2F               ; {code.loc_2a2f} probe the girder under it

loc_20fd:
20FD: A7              AND     A                   
20FE: C2 18 21        JP      NZ,$2118            ; {code.loc_2118} contact: set up the next arc
2101: CD B4 24        CALL    $24B4               ; {code.retireBarrelIntoOilDrum} no contact this frame

; Retire a barrel once its X has run down to the bottom of its travel range; otherwise
; hand the record on unchanged. The test is on X + 8 taken at eight-bit width, not on X,
; so an X that has run PAST zero and wrapped to the top of the byte counts as retired
; just as a small positive X does -- without that wrap a barrel whose X had gone negative
; would be treated as if it were at the far end of the range. On the retire arm the
; record's active flag and its X are both zeroed: the flag frees the slot, and the zeroed
; X stops the freed slot from being drawn where it died. Either way the record's four
; sprite fields are still gathered this pass.
retireBarrelAtEndOfRange:
2104: DD 7E 03        LD      A,(IX+$03)          
2107: C6 08           ADD     A,$08               ; within eight pixels of X = 0, either side of the wrap?
2109: FE 10           CP      $10                 
210B: D2 CE 1F        JP      NC,$1FCE            ; {code.advanceBarrelTileAnimation} still in range, so just animate
210E: AF              XOR     A                   
210F: DD 77 00        LD      (IX+$00),A          ; free the slot
2112: DD 77 03        LD      (IX+$03),A          ; and stop it being drawn where it died
2115: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

loc_2118:
2118: DD 7E 05        LD      A,(IX+$05)          
211B: FE E0           CP      $E0                 ; has it reached the bottom line of the screen?
211D: DA 46 21        JP      C,$2146             ; {code.loc_2146} no: seed it a fresh trajectory
2120: DD 7E 07        LD      A,(IX+$07)          
2123: E6 FC           AND     $FC                 
2125: F6 01           OR      $01                 ; force the sprite code's low two bits to 01
2127: DD 77 07        LD      (IX+$07),A          
212A: AF              XOR     A                   
212B: DD 77 01        LD      (IX+$01),A          ; clear the select byte
212E: DD 77 02        LD      (IX+$02),A          ; and the mode byte
2131: DD 36 10 FF     LD      (IX+$10),$FF        ; a fixed leftward step of one pixel a frame
2135: DD 77 11        LD      (IX+$11),A          
2138: DD 77 12        LD      (IX+$12),A          
213B: DD 36 13 B0     LD      (IX+$13),$B0        ; launch vertical speed 176
213F: DD 36 0E 01     LD      (IX+$0E),$01        ; start its sub-state counter at one
2143: C3 53 21        JP      $2153               ; {code.loc_2153}

loc_2146:
2146: CD 07 24        CALL    $2407               ; {code.loc_2407}
2149: CD CB 22        CALL    $22CB               ; {code.loc_22cb} seed the two step fields by mode and difficulty

loc_214c:
214C: DD 7E 05        LD      A,(IX+$05)          
214F: DD 77 19        LD      (IX+$19),A          ; remember this row as the contact reference
2152: AF              XOR     A                   

loc_2153:
2153: DD 77 14        LD      (IX+$14),A          ; restart the arc's frame count
2156: DD 77 04        LD      (IX+$04),A          ; and clear both coordinate fractions
2159: DD 77 06        LD      (IX+$06),A          
215C: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

loc_215f:
215F: 7D              LD      A,L                 
2160: C6 05           ADD     A,$05               ; the discriminator sits five rows below the barrel
2162: 57              LD      D,A                 
2163: 7C              LD      A,H                 ; the search key is the barrel's column
2164: 01 15 00        LD      BC,$0015            ; one column of the ladder table, 21 entries
2167: CD 6D 21        CALL    $216D               ; {code.startBarrelDescentAtLadder} does it take the ladder down?
216A: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite}

; Decide whether a rolling barrel takes a ladder down -- the "wild" barrel. The caller
; hands over a search key, a discriminator and a scan count. A miss in the
; ladder-endpoint table unwinds on the caller's behalf, and a hit tagged 0 rather than 1
; is rejected. A tag-1 hit ALWAYS stamps the record's descent-target field with (paired
; slot - 5), then runs the gates that decide whether the barrel also starts moving. A
; clear spawn-mode gate byte starts it immediately. Otherwise: reject unless Mario has
; descended far enough that (his Y - 4) reaches the discriminator, then unless a
; difficulty-weighted random throttle passes; then by Mario's column against the key --
; exactly on it always goes, past it if Left is held, before it if Right is held, else a
; final random gate decides. Which ladder a barrel takes is a function of Mario.
startBarrelDescentAtLadder:
216D: CD 6E 23        CALL    $236E               ; {code.findOppositeLadderEnd} look the column up in the table
2170: 3D              DEC     A                   
2171: C0              RET     NZ                  ; only a near-end hit is processed
2172: 78              LD      A,B                 ; the paired slot at the other end of the ladder
2173: D6 05           SUB     $05                 
2175: DD 77 17        LD      (IX+$17),A          ; stamp the row the descent stops on
2178: 3A 48 63        LD      A,($6348)           ; {hard.workRam+348} read the spawn-mode gate
217B: A7              AND     A                   
217C: CA B2 21        JP      Z,$21B2             ; {code.loc_21b2} clear: start the descent at once
217F: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205}
2182: D6 04           SUB     $04                 ; Mario must have descended past the discriminator
2184: BA              CP      D                   
2185: D8              RET     C                   ; he has not come far enough yet
2186: 3A 80 63        LD      A,($6380)           ; {hard.workRam+380} weight the throttle by difficulty
2189: 1F              RRA                         
218A: 3C              INC     A                   
218B: 47              LD      B,A                 ; half the difficulty, plus one
218C: 3A 18 60        LD      A,($6018)           ; {hard.workRam+18} read the rolling random byte
218F: 4F              LD      C,A                 
2190: E6 03           AND     $03                 
2192: B8              CP      B                   ; two random bits against that throttle
2193: D0              RET     NC                  ; the draw rejects this attempt
2194: 21 10 60        LD      HL,$6010            ; point at the cooked control word
2197: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203}
219A: BB              CP      E                   ; compare Mario's column with the ladder's
219B: CA B2 21        JP      Z,$21B2             ; {code.loc_21b2} standing right on it: the barrel takes it
219E: D2 A9 21        JP      NC,$21A9            ; {code.loc_21a9} he is past the ladder
21A1: CB 46           BIT     0,(HL)              ; before it: is Right held, toward it?
21A3: CA AE 21        JP      Z,$21AE             ; {code.loc_21ae}
21A6: C3 B2 21        JP      $21B2               ; {code.loc_21b2} coming toward it: take the ladder

loc_21a9:
21A9: CB 4E           BIT     1,(HL)              ; past it: is Left held, back toward it?
21AB: C2 B2 21        JP      NZ,$21B2            ; {code.loc_21b2} coming toward it: take the ladder

loc_21ae:
21AE: 79              LD      A,C                 
21AF: E6 18           AND     $18                 ; otherwise a last random gate decides
21B1: C0              RET     NZ                  ; the draw says roll on past

loc_21b2:
21B2: DD 34 07        INC     (IX+$07)            ; bump the barrel's sprite code
21B5: DD CB 02 C6     SET     0,(IX+$02)          ; put the barrel on the ladder-travel arm
21B9: C9              RET                         

; The join every motion arm of the barrel walk arrives at, and where the record's four
; sprite bytes are actually written. Its first act is an unconditional register
; exchange: the arms that jump here swapped the walk's registers out for a working set
; of their own and none swaps back, so from this point the staging cursor, record
; pointer, stride and remaining-slot count are the walk's again. It then gathers four
; record fields into the sprite buffer in the sprite record's own field order -- X,
; code, attribute, Y. It is a PERMUTING gather and not a block copy: the record's Y is
; read after the two sprite bytes, and the two fields lying between them are never read.
; That permutation is the whole point, because it turns a barrel record into the byte
; layout the sprite hardware reads. Three of the four cursor steps happen here and the
; fourth in the between-slots step it hands on to; only the cursor's low byte moves, so
; it can never leave its page.
publishBarrelSprite:
21BA: D9              EXX                         ; the walk's cursors and slot count are the live set again
21BB: DD 7E 03        LD      A,(IX+$03)          
21BE: 77              LD      (HL),A              ; sprite X from the barrel's column
21BF: 2C              INC     L                   
21C0: DD 7E 07        LD      A,(IX+$07)          
21C3: 77              LD      (HL),A              ; its tile code
21C4: 2C              INC     L                   
21C5: DD 7E 08        LD      A,(IX+$08)          
21C8: 77              LD      (HL),A              ; its colour attribute
21C9: 2C              INC     L                   
21CA: DD 7E 05        LD      A,(IX+$05)          
21CD: 77              LD      (HL),A              ; sprite Y from the barrel's row
21CE: C3 8D 1F        JP      $1F8D               ; {code.loc_1f8d}

; ---- $21D1-$21ED: data ----
21D1: 80 FE 01 C0 04 50 02 10 82 60 02 10 82 CA 01 10
21E1: 81 FF 02 38 01 80 02 FF 04 80 04 60 80

; Advance the canned input script that drives the attract demo, called once per demo
; frame immediately before the shared per-frame update. The script is a table of
; two-byte (input, duration) pairs: demoScriptIndex picks the pair -- the entry offset
; being the index doubled, low byte only, so the table page never carries -- and that
; step's input byte is written straight over p1Input, the same cooked control word the
; joystick fills, so the demo plays itself. demoScriptCountdown is then read and
; decremented, and its value BEFORE the decrement decides: still non-zero means keep
; holding this step; zero means reload the countdown from the duration byte and step the
; index to the next pair. A duration of N holds its input for N+1 frames, and the input
; byte is re-issued on every frame it is held.
advanceAttractDemoInput:
21EE: 11 D1 21        LD      DE,$21D1            ; the demo script: pairs of input byte and duration
21F1: 21 CC 63        LD      HL,$63CC            ; the script cursor
21F4: 7E              LD      A,(HL)              
21F5: 07              RLCA                        ; two bytes per entry
21F6: 83              ADD     A,E                 
21F7: 5F              LD      E,A                 ; index the current pair; the page never carries
21F8: 1A              LD      A,(DE)              ; this step's input byte
21F9: 32 10 60        LD      ($6010),A           ; {hard.workRam+10} overwrite the control word: the demo plays itself
21FC: 2C              INC     L                   
21FD: 7E              LD      A,(HL)              ; read the hold countdown
21FE: 35              DEC     (HL)                ; and spend one frame of it
21FF: A7              AND     A                   
2200: C0              RET     NZ                  ; the step is still being held
2201: 1C              INC     E                   
2202: 1A              LD      A,(DE)              ; the duration byte of the pair just finished
2203: 77              LD      (HL),A              ; reload the countdown from it
2204: 2D              DEC     L                   
2205: 34              INC     (HL)                ; step the script on to the next pair
2206: C9              RET                         

; The 50m board-object state machine. A board gate opens the body ONLY on 50m; elsewhere
; it is dispatched every pass and does nothing. Frame parity picks which of the two
; 8-byte boardObjScratch records is serviced -- odd frame the first, even frame the
; second -- and the record's state byte, held in 0..3, selects one of four arms. The
; record's travel counter IS a screen Y, and larger is lower, so its minimum of 0x68 is
; the object's HIGHEST point and its maximum of 0x78 the lowest. State 0 parks at the top
; for a 256-frame dwell, stamping a shared flag on a Mario hit; state 1 steps the counter
; UP, moving the object DOWN the screen; state 2 is a randomised dwell at the lowest
; point; state 3 steps back up and re-parks at state 0. What these two objects ARE is
; open: their sprite reads as a ladder graphic and the four arms would fit a moving
; ladder, but that is reading a picture, not the code.
dispatch50mObjectState:
2207: 3E 02           LD      A,$02               ; board mask: 50m only
2209: F7              RST     $30                 ; on the other three boards the body below is skipped
220A: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} frame parity picks which record is serviced
220D: 1F              RRA                         
220E: 21 80 62        LD      HL,$6280            ; the first object record
2211: 7E              LD      A,(HL)              ; its state byte
2212: DA 19 22        JP      C,$2219             ; {code.loc_2219}
2215: 21 88 62        LD      HL,$6288            ; the second object record
2218: 7E              LD      A,(HL)              ; its state byte

loc_2219:
2219: E5              PUSH    HL                  ; hand the record base to the arm
221A: EF              RST     $28                 ; branch through the four-slot table below

; ---- $221B-$2226: jump table ----
221B: 27 22 59 22 99 22 A2 22 00 00 00 00

; The PARKED arm of the 50m board-object state machine: hold the object still while its
; dwell timer runs down. The record is 8 bytes -- +0 its state, +1 the dwell timer, +2
; the object's column -- and this is the arm taken while the state byte is 0. Nothing
; moves; the object's position counter is not touched anywhere here, which is what
; "parked" means. Every pass counts the dwell timer down by one. If the timer just
; reached zero the state is advanced -- which is what sets the object moving -- and Mario
; is hit-tested against the object's column, stamping a shared flag with 1 on a hit. If
; the timer is still running the same hit test stamps the flag with 0. A MISS unwinds two
; levels instead of returning, so only the stamp is skipped. Which 50m object the record
; drives is not established.
hold50mObjectParked:
2227: E1              POP     HL                  ; the record base the dispatcher pushed
2228: 2C              INC     L                   
2229: 35              DEC     (HL)                ; count the dwell timer down
222A: C2 3A 22        JP      NZ,$223A            ; {code.loc_223a} still parked
222D: 2D              DEC     L                   
222E: 34              INC     (HL)                ; dwell over: advance the state, setting it moving
222F: 2C              INC     L                   
2230: 2C              INC     L                   ; point at the object's column
2231: CD 43 22        CALL    $2243               ; {code.marioReachedTargetColumn} is Mario standing on it?
2234: 3E 01           LD      A,$01               
2236: 32 1A 62        LD      ($621A),A           ; {hard.workRam+21A} on a hit, stamp the shared flag set
2239: C9              RET                         

loc_223a:
223A: 2C              INC     L                   ; point at the object's column
223B: CD 43 22        CALL    $2243               ; {code.marioReachedTargetColumn} is Mario standing on it?
223E: AF              XOR     A                   
223F: 32 1A 62        LD      ($621A),A           ; {hard.workRam+21A} still parked: stamp the shared flag clear
2242: C9              RET                         

; Has Mario reached the target position? Three conditions must ALL hold for a hit:
; marioY is numerically under 122 -- larger Y is LOWER on screen, so the reach band is
; the rows ABOVE that one and at or below it the hit never registers; marioAirborne is
; clear, so the hit only counts with Mario grounded and not mid jump or fall; and marioX
; exactly equals the object's target X, the byte whose address the caller supplies. On a
; hit the caller runs its own tail; on any miss it hands off to the shared no-hit tail,
; whose result unwinds two levels up. A pure predicate over Mario's position and
; airborne state: it writes no memory and claims no game purpose beyond the test itself.
marioReachedTargetColumn:
2243: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read Mario's row
2246: FE 7A           CP      $7A                 ; the reach band is the rows above this one
2248: D2 57 22        JP      NC,$2257            ; {code.reportNoHitAndSkipCaller} too low on screen: no hit
224B: 3A 16 62        LD      A,($6216)           ; {hard.workRam+216} is he mid jump or fall?
224E: A7              AND     A                   
224F: C2 57 22        JP      NZ,$2257            ; {code.reportNoHitAndSkipCaller} airborne does not count
2252: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203}
2255: BE              CP      (HL)                ; is he exactly on the target column?
2256: C8              RET     Z                   ; a hit; the caller runs its own tail

; The "no hit" tail of the target-column hit test. That test asks whether Mario is
; standing on the target column -- marioY below 0x7A, marioAirborne clear, and marioX
; equal to the byte at a caller-supplied pointer -- and on a HIT returns normally, so
; its caller, one of the 50m object-state arms, runs its own tail. On NO HIT control
; reaches here, which discards the parent's return address and returns past it: the
; caller's tail never runs and control resumes two levels up. Pure control flow -- it
; reads nothing and writes nothing.
reportNoHitAndSkipCaller:
2257: E1              POP     HL                  ; discard the caller's return: unwind two levels
2258: C9              RET                         

; The descend arm of that machine, and the exact mirror of its raise arm. It counts the
; record's per-tick timer down by one, and until that underflows the object just idles.
; On the tick it does: reload the timer, step the position counter UP by one -- one pixel
; DOWN the screen -- and mirror the new counter into the object's on-screen sprite cell;
; when the counter reaches the bottom of its travel, advance the object's state. It then
; hit-tests Mario against the object's column, and on a miss the shared no-hit path
; unwinds two levels up. On a hit it settles Mario's climb downward: while he is still
; above the settle line, or on an odd pixel row, he is stepped one pixel down held in the
; climb pose; once his Y reaches the line on an even row, the climb-centring toggle is
; published from bit 1 of his Y so it alternates as he climbs.
slide50mObjectDown:
2259: E1              POP     HL                  ; the record base the dispatcher pushed
225A: 2C              INC     L                   ; walk out to the object's per-tick timer
225B: 2C              INC     L                   
225C: 2C              INC     L                   
225D: 2C              INC     L                   
225E: 35              DEC     (HL)                ; tick it down
225F: C0              RET     NZ                  ; the object idles until it underflows
2260: 3E 04           LD      A,$04               
2262: 77              LD      (HL),A              ; reload the timer
2263: 2D              DEC     L                   
2264: 34              INC     (HL)                ; step the counter up: one pixel DOWN the screen
2265: CD BD 22        CALL    $22BD               ; {code.publish50mObjectYToSprite} mirror the new position on screen
2268: 3E 78           LD      A,$78               
226A: BE              CP      (HL)                ; reached the bottom of its travel?
226B: C2 75 22        JP      NZ,$2275            ; {code.loc_2275}
226E: 2D              DEC     L                   
226F: 2D              DEC     L                   
2270: 2D              DEC     L                   
2271: 34              INC     (HL)                ; at the bottom: advance the object's state
2272: 2C              INC     L                   
2273: 2C              INC     L                   
2274: 2C              INC     L                   

loc_2275:
2275: 2D              DEC     L                   ; point at the object's column byte
2276: CD 43 22        CALL    $2243               ; {code.marioReachedTargetColumn} hit-test Mario against the column
2279: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read Mario's screen row
227C: FE 68           CP      $68                 ; compare against the climb settle line
227E: D2 8A 22        JP      NC,$228A            ; {code.loc_228a} at or past the line, check the row parity

; Step Mario down one pixel, held in the climb-down pose. The Y-descend tail of the
; conveyor board's descend arm, reached when Mario's screen Y is still numerically above
; the centring line -- that is, still higher on screen, since larger Y is lower -- or on
; an odd row. Each call increments marioY, so the logical position drops a pixel; pins
; his hardware sprite to a fixed climb frame and takes back a pointer to that record's Y
; field; then increments that Y, so the drawn sprite drops a pixel to match. Pose codes 3
; to 5 are the climb frames, and the pin forces the first of them with the mirror flag
; clear.
stepMarioDownInClimbPose:
2281: 21 05 62        LD      HL,$6205            ; point at Mario's screen row
2284: 34              INC     (HL)                ; drop him one pixel down the screen
2285: CD C0 3F        CALL    $3FC0               ; {code.pinMarioClimbPose} pin the climb pose and take the sprite Y
2288: 34              INC     (HL)                ; drop the drawn sprite a pixel to match
2289: C9              RET                         

loc_228a:
228A: 1F              RRA                         ; row parity: odd rows keep him stepping
228B: DA 81 22        JP      C,$2281             ; {code.stepMarioDownInClimbPose} odd row -- step him down again
228E: 1F              RRA                         ; now bit 1 of the row decides the toggle
228F: 3E 01           LD      A,$01               
2291: DA 95 22        JP      C,$2295             ; {code.loc_2295}
2294: AF              XOR     A                   

loc_2295:
2295: 32 22 62        LD      ($6222),A           ; {hard.workRam+222} publish the climb-centring toggle
2298: C9              RET                         

; Let a 50m board object move on to its next state, but only on a randomly chosen frame,
; so it dwells an unpredictable length of time in the one it is in. The caller picks
; which object's record to work on and hands over its base address; the state byte sits
; at the front of the record. random is sampled and the state is stepped ONLY when four
; selected bits of it happen to be clear -- about one frame in sixteen -- and on every
; other frame the object simply stays where it is. The effect is that it holds a state
; for a random spell instead of advancing on a fixed cadence, so its behaviour does not
; look metronomic.
advance50mObjectStateOnRandomGate:
2299: E1              POP     HL                  ; take the object record's base off the stack
229A: 3A 18 60        LD      A,($6018)           ; {hard.workRam+18} sample the random accumulator
229D: E6 3C           AND     $3C                 ; four selected bits -- about one frame in sixteen
229F: C0              RET     NZ                  ; not the chosen frame, hold this state
22A0: 34              INC     (HL)                ; step the object on to its next state
22A1: C9              RET                         

; One idle-then-retract tick for one of the two 50m travelling objects in
; boardObjScratch, the dispatcher choosing between the two eight-byte records by frame
; parity. Field +4 is a per-tick countdown: it is stepped down every time this arm runs,
; and until it underflows the object simply idles. On the tick it does, the countdown
; reloads and the position counter at +3 steps DOWN by one, and that new position is
; mirrored into the object's on-screen sprite cell. That counter is a SCREEN Y published
; straight into a sprite record's Y byte, and larger Y is lower, so stepping it down
; moves the object UP the screen. Reaching the top of travel parks it: field +1 takes a
; fixed value and the state byte at +0 is cleared, back to state 0. Across the four
; states the cycle is park at the top, extend down, dwell at the bottom, retract, park
; -- the motion of a retracting ladder, though the object is unidentified.
raise50mObjectAndPark:
22A2: E1              POP     HL                  ; take the object record's base off the stack
22A3: 2C              INC     L                   ; walk out to the per-tick countdown at +4
22A4: 2C              INC     L                   
22A5: 2C              INC     L                   
22A6: 2C              INC     L                   
22A7: 35              DEC     (HL)                ; tick the countdown
22A8: C0              RET     NZ                  ; not yet time to move, idle this frame
22A9: 36 02           LD      (HL),$02            ; reload the countdown
22AB: 2D              DEC     L                   ; back to the position counter at +3
22AC: 35              DEC     (HL)                ; step it down -- one pixel UP the screen
22AD: CD BD 22        CALL    $22BD               ; {code.publish50mObjectYToSprite} mirror the position to its sprite
22B0: 3E 68           LD      A,$68               ; the top of the object's travel
22B2: BE              CP      (HL)                
22B3: C0              RET     NZ                  ; not at the top yet, keep going
22B4: AF              XOR     A                   
22B5: 06 80           LD      B,$80               ; the parked value for the dwell field
22B7: 2D              DEC     L                   ; back to the dwell field at +1
22B8: 2D              DEC     L                   
22B9: 70              LD      (HL),B              ; park the object
22BA: 2D              DEC     L                   ; back to the state byte at +0
22BB: 77              LD      (HL),A              ; return it to state 0
22BC: C9              RET                         

; Mirror the byte at a source pointer into one of two sprite slots, chosen by bit 3 of
; the pointer's low byte -- clear picks the lower-addressed cell, set the higher. Both
; targets are the Y field of a 4-byte record inside spriteBuffer, records 17 and 18, the
; two slots just below Mario's, so the store refreshes an on-screen sprite's Y straight
; from the source byte; larger Y is lower on screen, so raising the copied byte drops the
; sprite down the display. Its two callers are the moving arms of the 50m object machine,
; each handing it a pointer to an object record's position counter, and the selector
; works because the two records' bases differ by 8. The sprite therefore holds the
; record's value as of the PREVIOUS frame, not this one.
publish50mObjectYToSprite:
22BD: 7E              LD      A,(HL)              ; read the object's position counter
22BE: CB 5D           BIT     3,L                 ; which of the two object records is this?
22C0: 11 4B 69        LD      DE,$694B            ; the Y field of the higher sprite slot
22C3: C2 C9 22        JP      NZ,$22C9            ; {code.loc_22c9}
22C6: 11 47 69        LD      DE,$6947            ; the Y field of the lower slot

loc_22c9:
22C9: 12              LD      (DE),A              ; refresh the sprite's Y from the counter
22CA: C9              RET                         

loc_22cb:
22CB: 3A 48 63        LD      A,($6348)           ; {hard.workRam+348} read the velocity-source mode latch
22CE: A7              AND     A                   
22CF: CA E1 22        JP      Z,$22E1             ; {code.loc_22e1} latch clear -- pick the magnitude by level
22D2: 3A 80 63        LD      A,($6380)           ; {hard.workRam+380} otherwise the difficulty picks the source
22D5: 3D              DEC     A                   ; difficulty 1 indexes entry 0
22D6: EF              RST     $28                 ; vector into the four-arm table below

; ---- $22D7-$22E0: jump table ----
22D7: F6 22 F6 22 03 23 03 23 1A 23

loc_22e1:
22E1: 3A 29 62        LD      A,($6229)           ; {hard.workRam+229} read the level
22E4: 47              LD      B,A                 
22E5: 05              DEC     B                   
22E6: 3E 01           LD      A,$01               ; level 1's magnitude
22E8: CA F9 22        JP      Z,$22F9             ; {code.loc_22f9}
22EB: 05              DEC     B                   
22EC: 3E B1           LD      A,$B1               ; level 2's magnitude
22EE: CA F9 22        JP      Z,$22F9             ; {code.loc_22f9}
22F1: 3E E9           LD      A,$E9               ; every later level shares this one
22F3: C3 F9 22        JP      $22F9               ; {code.loc_22f9}

loc_22f6:
22F6: 3A 18 60        LD      A,($6018)           ; {hard.workRam+18} difficulty 1-2: magnitude straight from chance

loc_22f9:
22F9: DD 77 11        LD      (IX+$11),A          ; store it as the object's step magnitude
22FC: E6 01           AND     $01                 ; its low bit picks the direction
22FE: 3D              DEC     A                   ; odd gives 00, even gives ff
22FF: DD 77 10        LD      (IX+$10),A          ; store the signed direction byte
2302: C9              RET                         

loc_2303:
2303: 3A 18 60        LD      A,($6018)           ; {hard.workRam+18} difficulty 3-4: a random step magnitude
2306: DD 77 11        LD      (IX+$11),A          
2309: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} steer the step toward Mario
230C: DD BE 03        CP      (IX+$03)            ; compare him against the object's column
230F: 3E 01           LD      A,$01               ; step right by default
2311: D2 16 23        JP      NC,$2316            ; {code.loc_2316} Mario at or right of it -- keep +1
2314: 3D              DEC     A                   ; Mario to the left -- step -1 instead
2315: 3D              DEC     A                   

loc_2316:
2316: DD 77 10        LD      (IX+$10),A          ; store the toward-Mario direction
2319: C9              RET                         

loc_231a:
231A: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} difficulty 5: derive both fields from the offset
231D: DD 96 03        SUB     (IX+$03)            ; signed horizontal offset out to Mario
2320: 0E FF           LD      C,$FF               ; sign fill for Mario on the left
2322: DA 26 23        JP      C,$2326             ; {code.loc_2326}
2325: 0C              INC     C                   ; Mario at or right of it -- no sign fill

loc_2326:
2326: 07              RLCA                        ; rotate the offset's top two bits down
2327: CB 11           RL      C                   
2329: 07              RLCA                        
232A: CB 11           RL      C                   
232C: DD 71 10        LD      (IX+$10),C          ; store the toward-Mario step code
232F: DD 77 11        LD      (IX+$11),A          ; store the offset-derived step delta
2332: C9              RET                         

; Nudge a coordinate one pixel along the 25m girder slope. The 25m girders are not flat
; -- each runs a shallow diagonal -- so a body walking or rolling across one has to shift
; its Y by one pixel every time its X crosses into a new 16-pixel girder cell to stay
; glued to the slope. Given the mover's X, the Y being corrected and a step selector, it
; moves Y ONLY at the instant X lands on a cell boundary: pixel offset 0 within the cell
; when the selector is 1, offset 15 otherwise. Anywhere mid-cell Y comes back unchanged.
; Direction is read from Y itself: a single bit of Y picks +1 against -1 in the general
; band, with two hard-coded band-seam rails, Y == 240 and Y == 76, that flip on X
; instead. Which physical girder runs those two rails join is not established.
snapYToGirder:
2333: 3E 0F           LD      A,$0F               
2335: A4              AND     H                   ; the mover's offset within its 16-pixel cell
2336: 05              DEC     B                   ; selector 1 picks the cell-entry test
2337: CA 42 23        JP      Z,$2342             ; {code.loc_2342}
233A: FE 0F           CP      $0F                 ; otherwise Y only moves at offset 15
233C: D8              RET     C                   ; mid-cell -- leave Y alone
233D: 06 FF           LD      B,$FF               ; nudge of one pixel, the other way
233F: C3 47 23        JP      $2347               ; {code.loc_2347}

loc_2342:
2342: FE 01           CP      $01                 ; selector 1: Y only moves at offset 0
2344: D0              RET     NC                  ; mid-cell -- leave Y alone
2345: 06 01           LD      B,$01               ; nudge of one pixel

loc_2347:
2347: 3E F0           LD      A,$F0               
2349: BD              CP      L                   ; Y == 240 is a band-seam rail
234A: CA 60 23        JP      Z,$2360             ; {code.loc_2360}
234D: 3E 4C           LD      A,$4C               
234F: BD              CP      L                   ; Y == 76 is the other rail
2350: CA 66 23        JP      Z,$2366             ; {code.loc_2366}
2353: 7D              LD      A,L                 
2354: CB 6F           BIT     5,A                 ; a bit of Y picks which way the girder slopes
2356: CA 5C 23        JP      Z,$235C             ; {code.loc_235c}

loc_2359:
2359: 90              SUB     B                   ; step Y one pixel against the nudge

loc_235a:
235A: 6F              LD      L,A                 ; hand the corrected Y back
235B: C9              RET                         

loc_235c:
235C: 80              ADD     A,B                 ; step Y one pixel with the nudge
235D: C3 5A 23        JP      $235A               ; {code.loc_235a}

loc_2360:
2360: CB 7C           BIT     7,H                 ; at the 240 rail, X decides instead
2362: C2 59 23        JP      NZ,$2359            ; {code.loc_2359}
2365: C9              RET                         ; left half of the screen -- Y unchanged

loc_2366:
2366: 7C              LD      A,H                 
2367: FE 98           CP      $98                 ; at the 76 rail, only X past 152 shifts
2369: D8              RET     C                   ; short of the seam -- Y unchanged
236A: 7D              LD      A,L                 
236B: C3 5C 23        JP      $235C               ; {code.loc_235c}

; Find a key in the ladder (object-parameter) table and hand back the paired slot at the
; OTHER end of that ladder, tagged with which end the caller started from. It scans
; objParamTable0 for the first byte equal to the search key; a matched entry carries two
; slots at a fixed +0x15 and +0x2A past it, and the routine returns whichever slot the
; discriminator did NOT match -- discriminator equal to the +0x15 byte gives tag 1 and
; the +0x2A byte, equal to the +0x2A byte gives tag 0 and the +0x15 byte, and if neither
; matches the scan resumes past that entry. A key never found before the count runs out
; is a MISS, and a miss is a DOUBLE unwind: the caller must return too. It writes no
; work RAM. That the records are LADDERS is not derivable from this body; what is, is
; the shape -- a keyed lookup into fixed-stride records, returning the far member of a
; pair and saying which end it came from.
findOppositeLadderEnd:
236E: 21 00 63        LD      HL,$6300            ; scan from the head of the parameter table

loc_2371:
2371: ED B1           CPIR                        ; search for the first entry matching the key
2373: C2 9A 23        JP      NZ,$239A            ; {code.loc_239a} not found before the count ran out -- a miss
2376: E5              PUSH    HL                  ; remember where the scan had got to
2377: C5              PUSH    BC                  
2378: 01 14 00        LD      BC,$0014            
237B: 09              ADD     HL,BC               ; step out to this entry's paired slot at +0x15
237C: 0C              INC     C                   
237D: 5F              LD      E,A                 
237E: 7A              LD      A,D                 ; the discriminator names the caller's own end
237F: BE              CP      (HL)                
2380: CA 8F 23        JP      Z,$238F             ; {code.loc_238f} that end matched -- take the far one
2383: 09              ADD     HL,BC               ; try the slot at +0x2A instead
2384: BE              CP      (HL)                
2385: CA 95 23        JP      Z,$2395             ; {code.loc_2395}
2388: 57              LD      D,A                 
2389: 7B              LD      A,E                 
238A: C1              POP     BC                  
238B: E1              POP     HL                  
238C: C3 71 23        JP      $2371               ; {code.loc_2371} neither end matched -- resume the scan

loc_238f:
238F: 09              ADD     HL,BC               ; take the +0x2A slot
2390: 3E 01           LD      A,$01               ; tag 1: the caller started at the near end
2392: C3 98 23        JP      $2398               ; {code.loc_2398}

loc_2395:
2395: AF              XOR     A                   ; tag 0: the caller started at the far end
2396: ED 42           SBC     HL,BC               ; take the +0x15 slot instead

loc_2398:
2398: C1              POP     BC                  
2399: 46              LD      B,(HL)              ; hand back the slot at the other end

loc_239a:
239A: E1              POP     HL                  ; reclaim the scan pointer -- or, on a miss, the return
239B: C9              RET                         

; Advance an airborne actor one frame along its ballistic arc, on whatever record the
; caller points at. Two of its fields are 16-bit fixed-point coordinates, big-endian
; with the high byte at the lower offset, each with its own signed 16-bit per-frame
; velocity, plus a one-byte airborne-frame counter t that drives a ramping gravity term:
;   +03:+04  coordinate A (horizontal)  += velocity A at +10:+11
;   +05:+06  coordinate B (vertical)    -= velocity B at +12:+13, then += gravity(t)
;   +14      t, incremented after use
; gravity(t) = (2t + 1) * 8 = 16t + 8, the discrete integral of a constant downward
; acceleration -- so coordinate B follows a parabola, velocity B first carrying it one
; way and the accumulating gravity term overtaking it, while A drifts at constant
; velocity. The same shape serves Mario and the airborne objects alike; no fixed address
; is referenced.
stepBallisticMotion:
239C: DD 7E 04        LD      A,(IX+$04)          ; low byte of the horizontal coordinate
239F: DD 86 11        ADD     A,(IX+$11)          ; add the low byte of its per-frame velocity
23A2: DD 77 04        LD      (IX+$04),A          
23A5: DD 7E 03        LD      A,(IX+$03)          
23A8: DD 8E 10        ADC     A,(IX+$10)          ; carry into the high byte
23AB: DD 77 03        LD      (IX+$03),A          
23AE: DD 7E 06        LD      A,(IX+$06)          ; low byte of the vertical coordinate
23B1: DD 96 13        SUB     (IX+$13)            ; subtract its own per-frame velocity
23B4: 6F              LD      L,A                 
23B5: DD 7E 05        LD      A,(IX+$05)          
23B8: DD 9E 12        SBC     A,(IX+$12)          
23BB: 67              LD      H,A                 
23BC: DD 7E 14        LD      A,(IX+$14)          ; frames elapsed since the actor left the ground
23BF: A7              AND     A                   
23C0: 17              RLA                         
23C1: 3C              INC     A                   ; form 2t + 1, the gravity ramp's multiplier
23C2: 06 00           LD      B,$00               
23C4: CB 10           RL      B                   
23C6: CB 27           SLA     A                   ; scale it by eight into a 16-bit gravity term
23C8: CB 10           RL      B                   
23CA: CB 27           SLA     A                   
23CC: CB 10           RL      B                   
23CE: CB 27           SLA     A                   
23D0: CB 10           RL      B                   
23D2: 4F              LD      C,A                 
23D3: 09              ADD     HL,BC               ; add the ramping gravity term
23D4: DD 74 05        LD      (IX+$05),H          ; store the new vertical coordinate
23D7: DD 75 06        LD      (IX+$06),L          
23DA: DD 34 14        INC     (IX+$14)            ; one more airborne frame
23DD: C9              RET                         

; Refresh a barrel's two sprite MIRROR bits from a packed direction lookup, one call in
; four. Almost every call just steps the record's own down-counter at +0x0F and returns;
; only the call that finds it at 1 does the work and reloads the counter to 4. On that
; beat it rewrites the top bit of two record bytes and leaves their low seven bits alone:
; bit 7 of the sprite code is the VERTICAL mirror, bit 7 of the attribute the HORIZONTAL
; one. The new pair comes from a packed 4x2-bit lookup keyed by the barrel's current
; orientation -- its two existing top bits as a 2-bit selector -- together with the
; direction code, so the facing advances one step through a table while the tile and the
; colour in the low bits are preserved. Two mirror bits do not by themselves make a
; rotation, and the barrel artwork is not decoded here.
advanceBarrelSpriteOrientation:
23DE: DD 7E 0F        LD      A,(IX+$0F)          ; read this barrel's orientation countdown
23E1: 3D              DEC     A                   
23E2: C2 03 24        JP      NZ,$2403            ; {code.loc_2403} not the beat -- just store the ticked counter
23E5: AF              XOR     A                   
23E6: DD CB 07 26     SLA     (IX+$07)            ; shift the vertical-mirror bit out of the code
23EA: 17              RLA                         ; collect it as the top bit of the selector
23EB: DD CB 08 26     SLA     (IX+$08)            ; and the horizontal mirror out of the attribute
23EF: 17              RLA                         
23F0: 47              LD      B,A                 ; the barrel's current orientation, two bits
23F1: 3E 03           LD      A,$03               
23F3: B1              OR      C                   ; key the lookup with the direction code
23F4: CD 09 30        CALL    $3009               ; {code.nextAnimationStep} advance the orientation one step
23F7: 1F              RRA                         ; shift the new mirror bits back in
23F8: DD CB 08 1E     RR      (IX+$08)            
23FC: 1F              RRA                         
23FD: DD CB 07 1E     RR      (IX+$07)            
2401: 3E 04           LD      A,$04               ; reload the countdown -- one call in four

loc_2403:
2403: DD 77 0F        LD      (IX+$0F),A          ; store the countdown back
2406: C9              RET                         

loc_2407:
2407: DD 7E 14        LD      A,(IX+$14)          ; the record's packed pair of 4-bit digits
240A: 07              RLCA                        ; swap the two digits
240B: 07              RLCA                        
240C: 07              RLCA                        
240D: 07              RLCA                        
240E: 4F              LD      C,A                 
240F: E6 0F           AND     $0F                 ; the high digit is the whole-number part
2411: 67              LD      H,A                 
2412: 79              LD      A,C                 
2413: E6 F0           AND     $F0                 ; the low digit becomes the fraction
2415: 6F              LD      L,A                 
2416: DD 4E 13        LD      C,(IX+$13)          ; the 16-bit operand carried in the record
2419: DD 46 12        LD      B,(IX+$12)          
241C: ED 42           SBC     HL,BC               ; the fixed-point difference the callers use
241E: C9              RET                         

; The horizontal position gate: classify Mario's X into a two-flag verdict the movement
; code turns into a restraint on his X. It reads marioX, marioY and board and writes no
; memory. The tests run in order, all unsigned, first to fire deciding: X < 0x16 gives
; (1,0), far left; X >= 0xEA gives (0,1), the right edge; an even board gives (0,0), so
; the gate never opens on 50m or 100m; Y >= 0x58 gives (0,0); X >= 0x6C gives (0,0), past
; the mid column; anything else gives (1,0). So the left verdict also covers an INTERIOR
; wall at the left end of the top platform on the odd boards, not just the screen edge.
; The walk step reads the right flag as "a rightward step is refused"; the airborne step
; reads the left flag as a push back inward, a rightward drift of half a pixel a frame
; rather than a stop; and the X clamp uses both.
limitMarioHorizontalTravel:
241F: 11 00 01        LD      DE,$0100            ; start from the far-left verdict
2422: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} read Mario's column
2425: FE 16           CP      $16                 ; is he left of the far-left limit?
2427: D8              RET     C                   ; yes -- the left flag stands
2428: 15              DEC     D                   ; switch to the right-edge verdict
2429: 1C              INC     E                   
242A: FE EA           CP      $EA                 ; at or past the right edge?
242C: D0              RET     NC                  ; yes -- refuse a rightward step
242D: 1D              DEC     E                   ; otherwise no restraint at all
242E: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} the gate never opens on 50m or 100m
2431: 0F              RRCA                        
2432: D0              RET     NC                  
2433: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read his screen row
2436: FE 58           CP      $58                 ; below the top platform -- no restraint
2438: D0              RET     NC                  
2439: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} read his column again
243C: FE 6C           CP      $6C                 ; past the mid column -- no restraint
243E: D0              RET     NC                  
243F: 14              INC     D                   ; left of the top platform's interior wall
2440: C9              RET                         

; Scatter this board's object-init records into two parallel work-RAM attribute arrays,
; once per board. Two heads run first. One forms an 8-bit modular checksum, seeded with
; 0x5E, over six bytes of program data and uses it to pick the second group's base --
; zero selects the base, anything else one byte past it. The shipped image sums to
; exactly zero, so the alternate base never happens in practice: it is a data-integrity
; guard. The other head picks the record table from board, 25m / 50m / 75m each having
; their own and everything else taking the default. The walk then reads fixed 5-byte
; records [type, fieldA, fieldB, unused, fieldC]: type 0 de-interleaves into
; objParamTable0 and type 1 into objParamTable1, the three fields landing in three
; parallel arrays a fixed stride apart. Type 0xAA ends the walk and is the ONLY exit;
; any other type is skipped whole and the walk continues.
loadBoardObjectRecords:
2441: 21 0C 3F        LD      HL,$3F0C            ; the six program bytes the integrity sum covers
2444: 3E 5E           LD      A,$5E               ; checksum seed
2446: 06 06           LD      B,$06               

loc_2448:
2448: 86              ADD     A,(HL)              ; sum the six bytes
2449: 23              INC     HL                  
244A: 10 FC           DJNZ    $2448               ; {code.loc_2448}
244C: FD 21 10 63     LD      IY,$6310            ; base of the type-1 attribute array
2450: A7              AND     A                   
2451: CA 56 24        JP      Z,$2456             ; {code.loc_2456} sum zero -- use that base
2454: FD 23           INC     IY                  ; a non-zero sum shifts it one byte on

loc_2456:
2456: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} pick the record table for this board
2459: 3D              DEC     A                   
245A: 21 E4 3A        LD      HL,$3AE4            ; 25m's records
245D: CA 71 24        JP      Z,$2471             ; {code.loc_2471}
2460: 3D              DEC     A                   
2461: 21 5D 3B        LD      HL,$3B5D            ; 50m's records
2464: CA 71 24        JP      Z,$2471             ; {code.loc_2471}
2467: 3D              DEC     A                   
2468: 21 E5 3B        LD      HL,$3BE5            ; 75m's records
246B: CA 71 24        JP      Z,$2471             ; {code.loc_2471}
246E: 21 8B 3C        LD      HL,$3C8B            ; the default table for every other board

loc_2471:
2471: DD 21 00 63     LD      IX,$6300            ; base of the type-0 attribute array
2475: 11 05 00        LD      DE,$0005            ; records are five bytes long

loc_2478:
2478: 7E              LD      A,(HL)              ; read the record's type byte
2479: A7              AND     A                   
247A: CA 88 24        JP      Z,$2488             ; {code.loc_2488} type 0 -- scatter into the first array
247D: 3D              DEC     A                   
247E: CA 9E 24        JP      Z,$249E             ; {code.loc_249e} type 1 -- into the parallel array
2481: FE A9           CP      $A9                 ; aa ends the walk, the only exit
2483: C8              RET     Z                   
2484: 19              ADD     HL,DE               ; any other type is skipped whole
2485: C3 78 24        JP      $2478               ; {code.loc_2478}

loc_2488:
2488: 23              INC     HL                  
2489: 7E              LD      A,(HL)              ; first field
248A: DD 77 00        LD      (IX+$00),A          ; into the base of the type-0 array
248D: 23              INC     HL                  
248E: 7E              LD      A,(HL)              ; second field
248F: DD 77 15        LD      (IX+$15),A          ; one stride on
2492: 23              INC     HL                  ; step over the record's unused byte
2493: 23              INC     HL                  
2494: 7E              LD      A,(HL)              ; third field
2495: DD 77 2A        LD      (IX+$2A),A          ; two strides on
2498: DD 23           INC     IX                  ; on to the next slot
249A: 23              INC     HL                  
249B: C3 78 24        JP      $2478               ; {code.loc_2478}

loc_249e:
249E: 23              INC     HL                  
249F: 7E              LD      A,(HL)              ; first field
24A0: FD 77 00        LD      (IY+$00),A          ; into the base of the type-1 array
24A3: 23              INC     HL                  
24A4: 7E              LD      A,(HL)              ; second field
24A5: FD 77 15        LD      (IY+$15),A          ; one stride on
24A8: 23              INC     HL                  ; step over the record's unused byte
24A9: 23              INC     HL                  
24AA: 7E              LD      A,(HL)              ; third field
24AB: FD 77 2A        LD      (IY+$2A),A          ; two strides on
24AE: FD 23           INC     IY                  ; on to the next slot
24B0: 23              INC     HL                  
24B1: C3 78 24        JP      $2478               ; {code.loc_2478}

; Retire a barrel that has reached the bottom of the playfield inside the oil drum's
; column band. Three gates in a row, each an ordinary return that leaves everything
; alone: the record's Y must have reached the bottom row (larger Y is lower on this
; screen), and its X must lie inside the band, both ends tested against the SAME loaded
; byte, so it is one range and not two independent limits. Past them the record's active
; flag and X are both zeroed -- the slot freed and the column blanked -- the impact
; sound latch is asserted for three frames, and control is handed to the shared sprite
; publish INSTEAD of returning, so the caller's remaining code must not run. Two latches
; are armed here, and they are why this is more than a bounds check: for a barrel whose
; kind byte is non-zero the fixed hazard's phase byte is set to bits 0 and 1, the pair
; that lets the hazard machine run AND take the arm that counts down and eventually
; raises an object-insert request -- so retiring one kind of barrel is what ARMS a fire
; release, the fire itself being spawned later and capped by a live count. And a
; one-shot difficulty latch is set the first time this ever fires and never touched
; again: both its readers take CLEAR as the simple early-game behaviour and SET as the
; difficulty-graded one, so this is a one-way switch into the graded behaviour.
retireBarrelIntoOilDrum:
24B4: DD 7E 05        LD      A,(IX+$05)          ; the barrel's screen row
24B7: FE E8           CP      $E8                 ; has it reached the bottom row?
24B9: D8              RET     C                   ; not down yet -- leave it running
24BA: DD 7E 03        LD      A,(IX+$03)          ; its column
24BD: FE 2A           CP      $2A                 ; right of the drum's band?
24BF: D0              RET     NC                  
24C0: FE 20           CP      $20                 ; left of the band?
24C2: D8              RET     C                   
24C3: DD 7E 15        LD      A,(IX+$15)          ; the barrel's kind byte
24C6: A7              AND     A                   
24C7: CA D0 24        JP      Z,$24D0             ; {code.loc_24d0} ordinary barrel -- just free the slot
24CA: 3E 03           LD      A,$03               ; bits 0 and 1: run the hazard AND arm a fire
24CC: 32 B9 62        LD      ($62B9),A           ; {hard.workRam+2B9}
24CF: AF              XOR     A                   ; the value that frees the record below

loc_24d0:
24D0: DD 77 00        LD      (IX+$00),A          ; clear the record's active flag
24D3: DD 77 03        LD      (IX+$03),A          ; and blank the column it died in
24D6: 21 82 60        LD      HL,$6082            ; the impact sound line
24D9: 36 03           LD      (HL),$03            ; assert it for three frames
24DB: E1              POP     HL                  ; drop the return: the publish returns in its place
24DC: 3A 48 63        LD      A,($6348)           ; {hard.workRam+348} the one-shot mode latch
24DF: A7              AND     A                   
24E0: C2 BA 21        JP      NZ,$21BA            ; {code.publishBarrelSprite} already set -- just publish the sprite
24E3: 3C              INC     A                   
24E4: 32 48 63        LD      ($6348),A           ; {hard.workRam+348} the first retirement switches the mode on
24E7: C3 BA 21        JP      $21BA               ; {code.publishBarrelSprite} publish the blanked sprite, and return

update50mMovingObjects:
24EA: 3E 02           LD      A,$02               ; board mask: 50m only
24EC: F7              RST     $30                 ; closed on any other board -- skip the whole body
24ED: CD 23 25        CALL    $2523               ; {code.service50mObjectSpawnRequest} spawn one if one is due
24F0: CD 91 25        CALL    $2591               ; {code.advance50mObjectRow} move them, cull the ones that ran out
24F3: DD 21 A0 65     LD      IX,$65A0            ; the six 50m object records
24F7: 06 06           LD      B,$06               
24F9: 21 B8 69        LD      HL,$69B8            ; and their six four-byte sprite records

loc_24fc:
24FC: DD 7E 00        LD      A,(IX+$00)          ; is this record live?
24FF: A7              AND     A                   
2500: CA 1C 25        JP      Z,$251C             ; {code.loc_251c} dormant -- step past its sprite slot untouched
2503: DD 7E 03        LD      A,(IX+$03)          ; the object's column
2506: 77              LD      (HL),A              
2507: 2C              INC     L                   
2508: DD 7E 07        LD      A,(IX+$07)          ; its sprite
250B: 77              LD      (HL),A              
250C: 2C              INC     L                   
250D: DD 7E 08        LD      A,(IX+$08)          ; its colour and flip attribute
2510: 77              LD      (HL),A              
2511: 2C              INC     L                   
2512: DD 7E 05        LD      A,(IX+$05)          ; and its row -- it is on screen this frame
2515: 77              LD      (HL),A              
2516: 2C              INC     L                   

loc_2517:
2517: DD 19           ADD     IX,DE               ; on to the next record; the stride came back from the row advance
2519: 10 E1           DJNZ    $24FC               ; {code.loc_24fc}
251B: C9              RET                         

loc_251c:
251C: 7D              LD      A,L                 ; leave the slot showing whatever the cull left there
251D: C6 04           ADD     A,$04               
251F: 6F              LD      L,A                 
2520: C3 17 25        JP      $2517               ; {code.loc_2517}

service50mObjectSpawnRequest:
2523: 21 9B 63        LD      HL,$639B            ; the spawn cooldown
2526: 7E              LD      A,(HL)              
2527: A7              AND     A                   
2528: C2 8F 25        JP      NZ,$258F            ; {code.loc_258f} still cooling down -- just tick it and stop
252B: 3A 9A 63        LD      A,($639A)           ; {hard.workRam+39A} is a spawn actually being asked for?
252E: A7              AND     A                   
252F: C8              RET     Z                   ; nothing asked -- nothing to do
2530: 06 06           LD      B,$06               
2532: 11 10 00        LD      DE,$0010            
2535: DD 21 A0 65     LD      IX,$65A0            ; hunt the six records for a free slot

loc_2539:
2539: DD CB 00 46     BIT     0,(IX+$00)          ; a free slot has this bit clear
253D: CA 45 25        JP      Z,$2545             ; {code.loc_2545}
2540: DD 19           ADD     IX,DE               
2542: 10 F5           DJNZ    $2539               ; {code.loc_2539}
2544: C9              RET                         ; every slot busy -- no spawn this pass

loc_2545:
2545: CD 57 00        CALL    $0057               ; {code.stirRandomSeed} roll the seed to place the new one
2548: FE 60           CP      $60                 
254A: DD 36 05 7C     LD      (IX+$05),$7C        ; put it on the upper row by default
254E: DA 58 25        JP      C,$2558             ; {code.loc_2558} a low roll sends it to the lower row
2551: 3A A3 62        LD      A,($62A3)           ; {hard.workRam+2A3} otherwise object 2's heading decides
2554: 3D              DEC     A                   
2555: C2 6E 25        JP      NZ,$256E            ; {code.loc_256e} not that way -- re-roll, just for the side

loc_2558:
2558: DD 36 05 CC     LD      (IX+$05),$CC        ; the lower row
255C: 3A A6 62        LD      A,($62A6)           ; {hard.workRam+2A6} object 3's heading picks the side
255F: 07              RLCA                        

loc_2560:
2560: DD 36 03 07     LD      (IX+$03),$07        ; start it at the low end of its travel
2564: D2 76 25        JP      NC,$2576            ; {code.loc_2576}
2567: DD 36 03 F8     LD      (IX+$03),$F8        ; or the high end
256B: C3 76 25        JP      $2576               ; {code.loc_2576}

loc_256e:
256E: CD 57 00        CALL    $0057               ; {code.stirRandomSeed} a second roll, this time only for the side
2571: FE 68           CP      $68                 
2573: C3 60 25        JP      $2560               ; {code.loc_2560}

loc_2576:
2576: DD 36 00 01     LD      (IX+$00),$01        ; bring the record to life
257A: DD 36 07 4B     LD      (IX+$07),$4B        ; its sprite
257E: DD 36 09 08     LD      (IX+$09),$08        ; its hit box: eight across
2582: DD 36 0A 03     LD      (IX+$0A),$03        ; and three down
2586: 3E 7C           LD      A,$7C               
2588: 32 9B 63        LD      ($639B),A           ; {hard.workRam+39B} no other may spawn for 124 frames
258B: AF              XOR     A                   
258C: 32 9A 63        LD      ($639A),A           ; {hard.workRam+39A} the request is consumed

loc_258f:
258F: 35              DEC     (HL)                ; tick the cooldown -- or, from the spawn path, the spin counter
2590: C9              RET                         

advance50mObjectRow:
2591: DD 21 A0 65     LD      IX,$65A0            ; the same six records
2595: 11 10 00        LD      DE,$0010            ; the record stride, which the caller reuses after this returns
2598: 06 06           LD      B,$06               

loc_259a:
259A: DD CB 00 46     BIT     0,(IX+$00)          ; only live records move
259E: CA BB 25        JP      Z,$25BB             ; {code.loc_25bb}
25A1: DD 7E 03        LD      A,(IX+$03)          ; the object's column
25A4: 67              LD      H,A                 
25A5: C6 07           ADD     A,$07               
25A7: FE 0E           CP      $0E                 ; within seven of column zero, wrapping through it?
25A9: DA D6 25        JP      C,$25D6             ; {code.loc_25d6} it has run off the end -- retire it
25AC: DD 7E 05        LD      A,(IX+$05)          ; which row it was spawned on
25AF: FE 7C           CP      $7C                 
25B1: CA C0 25        JP      Z,$25C0             ; {code.loc_25c0} the upper row's object splits at mid-screen
25B4: 3A A6 63        LD      A,($63A6)           ; {hard.workRam+3A6} everything else rides object 3's step
25B7: 84              ADD     A,H                 
25B8: DD 77 03        LD      (IX+$03),A          ; move it

loc_25bb:
25BB: DD 19           ADD     IX,DE               
25BD: 10 DB           DJNZ    $259A               ; {code.loc_259a}
25BF: C9              RET                         

loc_25c0:
25C0: 7C              LD      A,H                 
25C1: FE 80           CP      $80                 ; the exact middle of its travel
25C3: CA D6 25        JP      Z,$25D6             ; {code.loc_25d6} it reached the middle -- retire it
25C6: 3A A5 63        LD      A,($63A5)           ; {hard.workRam+3A5} past the middle, object 2's step
25C9: D2 CF 25        JP      NC,$25CF            ; {code.loc_25cf}
25CC: 3A A4 63        LD      A,($63A4)           ; {hard.workRam+3A4} short of it, the mirror of that step

loc_25cf:
25CF: 84              ADD     A,H                 
25D0: DD 77 03        LD      (IX+$03),A          ; move it
25D3: C3 BB 25        JP      $25BB               ; {code.loc_25bb}

loc_25d6:
25D6: 21 B8 69        LD      HL,$69B8            ; retiring: walk to this record's sprite slot
25D9: 3E 06           LD      A,$06               
25DB: 90              SUB     B                   ; how many records in, four sprite bytes each

loc_25dc:
25DC: CA E7 25        JP      Z,$25E7             ; {code.loc_25e7}
25DF: 2C              INC     L                   
25E0: 2C              INC     L                   
25E1: 2C              INC     L                   
25E2: 2C              INC     L                   
25E3: 3D              DEC     A                   
25E4: C3 DC 25        JP      $25DC               ; {code.loc_25dc}

loc_25e7:
25E7: AF              XOR     A                   
25E8: DD 77 00        LD      (IX+$00),A          ; free the record
25EB: DD 77 03        LD      (IX+$03),A          ; blank the column it died in
25EE: 77              LD      (HL),A              ; and blank its sprite, so it leaves the screen
25EF: C3 BB 25        JP      $25BB               ; {code.loc_25bb}

; The 50m board's per-frame object update. A board gate with mask 0x02 opens it ONLY on
; 50m; on any other board it is dispatched constantly and the body never runs. When it
; does run it drives the board's object state in the fixed order the mover depends on:
; conveyor object 1's reverse-timer / step-direction driver, object 2's (gated by Mario's
; vertical position), object 3's, and then the carry -- read which conveyor row Mario is
; standing on and move his X by that row's freshly published step, so he rides the
; platform. The three drivers MUST run before the carry, because each publishes the
; signed step the carry consumes.
update50mConveyorObjects:
25F2: 3E 02           LD      A,$02               ; board mask: 50m only
25F4: F7              RST     $30                 ; closed on any other board -- skip the body
25F5: CD 02 26        CALL    $2602               ; {code.loc_2602} conveyor object 1's step driver
25F8: CD 2F 26        CALL    $262F               ; {code.loc_262f} object 2's
25FB: CD 79 26        CALL    $2679               ; {code.loc_2679} object 3's
25FE: CD D3 2A        CALL    $2AD3               ; {code.carryMarioOnConveyorRow} carry Mario along his conveyor row
2601: C9              RET                         

loc_2602:
2602: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} read the frame counter
2605: 0F              RRCA                        
2606: DA 16 26        JP      C,$2616             ; {code.loc_2616} odd frame -- skip the turnaround timer
2609: 21 A0 62        LD      HL,$62A0            ; object 1's reversal timer
260C: 35              DEC     (HL)                
260D: C2 16 26        JP      NZ,$2616            ; {code.loc_2616}
2610: 36 80           LD      (HL),$80            ; reload the full period
2612: 2C              INC     L                   ; point at the step-direction latch
2613: CD DE 26        CALL    $26DE               ; {code.reverseStepDirection} flip which way the object travels

loc_2616:
2616: 21 A1 62        LD      HL,$62A1            ; object 1's step-direction latch
2619: CD E9 26        CALL    $26E9               ; {code.signStepHalfRate} reduce it to a 0 / +-1 step
261C: 32 A3 63        LD      ($63A3),A           ; {hard.workRam+3A3} publish the step the mover reads
261F: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A}
2622: E6 1F           AND     $1F                 ; only every 32nd frame animates
2624: FE 01           CP      $01                 
2626: C0              RET     NZ                  
2627: 11 E4 69        LD      DE,$69E4            ; object 1's mirrored sprite-code pair
262A: EB              EX      DE,HL               
262B: CD A6 26        CALL    $26A6               ; {code.loc_26a6} advance the pair one walk frame
262E: C9              RET                         

loc_262f:
262F: 21 A3 62        LD      HL,$62A3            ; object 2's step-direction latch
2632: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read Mario's screen row
2635: FE C0           CP      $C0                 ; is he high on the screen?
2637: DA 6F 26        JP      C,$266F             ; {code.loc_266f} yes -- force this object's step negative
263A: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} read the frame counter
263D: 0F              RRCA                        
263E: DA 4C 26        JP      C,$264C             ; {code.loc_264c} odd frame -- skip the timer
2641: 2D              DEC     L                   ; back to object 2's reversal timer
2642: 35              DEC     (HL)                
2643: C2 4C 26        JP      NZ,$264C            ; {code.loc_264c}
2646: 36 C0           LD      (HL),$C0            ; reload object 2's period
2648: 2C              INC     L                   ; on to the step-direction latch
2649: CD DE 26        CALL    $26DE               ; {code.reverseStepDirection} reverse which way it travels

loc_264c:
264C: 21 A3 62        LD      HL,$62A3            ; object 2's step-direction latch
264F: CD E9 26        CALL    $26E9               ; {code.signStepHalfRate} reduce it to a 0 / +-1 step
2652: 32 A5 63        LD      ($63A5),A           ; {hard.workRam+3A5} publish the positive-going step
2655: ED 44           NEG                         ; negate it
2657: 32 A4 63        LD      ($63A4),A           ; {hard.workRam+3A4} publish the other polarity too
265A: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} read the frame counter
265D: E6 1F           AND     $1F                 
265F: C0              RET     NZ                  ; animate only on every 32nd frame
2660: 2D              DEC     L                   ; the reversal timer doubles as arm select
2661: 11 EC 69        LD      DE,$69EC            ; object 2's mirrored sprite-code pair
2664: EB              EX      DE,HL               
2665: CD A6 26        CALL    $26A6               ; {code.loc_26a6} advance the pair one walk frame
2668: E6 7F           AND     $7F                 ; drop the horizontal-flip bit
266A: 21 ED 69        LD      HL,$69ED            
266D: 77              LD      (HL),A              ; re-stamp the pair's low cell
266E: C9              RET                         

loc_266f:
266F: CB 7E           BIT     7,(HL)              ; is it already stepping negative?
2671: C2 4C 26        JP      NZ,$264C            ; {code.loc_264c}
2674: 36 FF           LD      (HL),$FF            ; force the latch negative
2676: C3 4C 26        JP      $264C               ; {code.loc_264c}

loc_2679:
2679: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} read the frame counter
267C: 0F              RRCA                        
267D: DA 8D 26        JP      C,$268D             ; {code.loc_268d} odd frame -- skip the timer
2680: 21 A5 62        LD      HL,$62A5            ; object 3's reversal timer
2683: 35              DEC     (HL)                
2684: C2 8D 26        JP      NZ,$268D            ; {code.loc_268d}
2687: 36 FF           LD      (HL),$FF            ; reload object 3's period
2689: 2C              INC     L                   ; on to the step-direction latch
268A: CD DE 26        CALL    $26DE               ; {code.reverseStepDirection} reverse which way it travels

loc_268d:
268D: 21 A6 62        LD      HL,$62A6            ; object 3's step-direction latch
2690: CD E9 26        CALL    $26E9               ; {code.signStepHalfRate} reduce it to a 0 / +-1 step
2693: 32 A6 63        LD      ($63A6),A           ; {hard.workRam+3A6} publish object 3's step
2696: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} read the frame counter
2699: E6 1F           AND     $1F                 
269B: FE 02           CP      $02                 ; animate only on every 32nd frame
269D: C0              RET     NZ                  
269E: 11 F4 69        LD      DE,$69F4            ; object 3's mirrored sprite-code pair
26A1: EB              EX      DE,HL               
26A2: CD A6 26        CALL    $26A6               ; {code.loc_26a6} advance the pair one walk frame
26A5: C9              RET                         

loc_26a6:
26A6: 2C              INC     L                   ; step to the pair's low counter
26A7: 1A              LD      A,(DE)              ; the caller's direction-select byte
26A8: 17              RLA                         
26A9: DA C5 26        JP      C,$26C5             ; {code.loc_26c5} select bit set -- run the mirrored arm
26AC: 7E              LD      A,(HL)              
26AD: 3C              INC     A                   ; count the low counter up
26AE: FE 53           CP      $53                 ; past the last of its three frames?
26B0: C2 B5 26        JP      NZ,$26B5            ; {code.loc_26b5}
26B3: 3E 50           LD      A,$50               ; wrap back to the first

loc_26b5:
26B5: 77              LD      (HL),A              
26B6: 7D              LD      A,L                 ; the mirrored counter sits four bytes on
26B7: C6 04           ADD     A,$04               
26B9: 6F              LD      L,A                 
26BA: 7E              LD      A,(HL)              
26BB: 3D              DEC     A                   ; count that one the other way
26BC: FE CF           CP      $CF                 ; past the end of its three frames?
26BE: C2 C3 26        JP      NZ,$26C3            ; {code.loc_26c3}
26C1: 3E D2           LD      A,$D2               ; wrap it, mirror bit set

loc_26c3:
26C3: 77              LD      (HL),A              
26C4: C9              RET                         

loc_26c5:
26C5: 7E              LD      A,(HL)              
26C6: 3D              DEC     A                   ; count the low counter down
26C7: FE 4F           CP      $4F                 ; below the first of its three frames?
26C9: C2 CE 26        JP      NZ,$26CE            ; {code.loc_26ce}
26CC: 3E 52           LD      A,$52               ; wrap round to the last

loc_26ce:
26CE: 77              LD      (HL),A              
26CF: 7D              LD      A,L                 ; the mirrored counter, four bytes on
26D0: C6 04           ADD     A,$04               
26D2: 6F              LD      L,A                 
26D3: 7E              LD      A,(HL)              
26D4: 3C              INC     A                   ; count that one the other way
26D5: FE D3           CP      $D3                 ; past the end of its three frames?
26D7: C2 DC 26        JP      NZ,$26DC            ; {code.loc_26dc}
26DA: 3E D0           LD      A,$D0               ; wrap it, mirror bit set

loc_26dc:
26DC: 77              LD      (HL),A              
26DD: C9              RET                         

; Reverse a timed sprite object's travel by flipping the sign of the one-byte signed step
; that steers it. The caller hands over a pointer to that byte; bit 7 is the direction.
; The byte is rewritten to +2 when it was negative and to -2 when it was not, so the sign
; always comes out opposite to what went in. The MAGNITUDE is reset to 2 whatever it was,
; and no reader looks at it -- the readers take the sign alone, to choose which of two
; movement offsets to apply and which way to publish the object's step -- so the
; observable effect is a direction reversal and nothing else.
reverseStepDirection:
26DE: CB 7E           BIT     7,(HL)              ; which way is it travelling now?
26E0: CA E6 26        JP      Z,$26E6             ; {code.loc_26e6}
26E3: 36 02           LD      (HL),$02            ; it was negative -- make it positive
26E5: C9              RET                         

loc_26e6:
26E6: 36 FE           LD      (HL),$FE            ; it was positive -- make it negative
26E8: C9              RET                         

; Collapse a direction byte to a unit step, every other frame. The caller keeps a signed
; direction byte per moving channel and hands over its address. On an EVEN frame the
; routine returns a step of zero and writes nothing, so the channel stands still. On an
; ODD frame the byte's sign bit decides -- negative gives -1, anything else +1 -- and
; the step is written back over the byte as well as returned. So the byte is a
; persistent direction LATCH whose magnitude is thrown away, and what the caller
; publishes pulses 0 / +-1 across frames: a fixed direction delivered at HALF the frame
; rate. Reversing the direction is done elsewhere.
signStepHalfRate:
26E9: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} read the frame counter
26EC: E6 01           AND     $01                 
26EE: C8              RET     Z                   ; even frame -- a zero step, the channel holds
26EF: CB 7E           BIT     7,(HL)              ; the latch's sign picks the direction
26F1: 3E FF           LD      A,$FF               
26F3: C2 F8 26        JP      NZ,$26F8            ; {code.loc_26f8}
26F6: 3E 01           LD      A,$01               

loc_26f8:
26F8: 77              LD      (HL),A              ; write the unit step back and hand it out
26F9: C9              RET                         

; The 75m per-frame service router, and the clearest difficulty ramp in the game. A
; board gate opens the whole routine on board 3 only. First, marioY at or above 240 --
; larger Y is lower, so this is Mario at the very bottom of the display -- kills him.
; The test is on marioY alone, with NO X-band test, so he need not be on a lift at all.
; Otherwise it services on a cadence keyed to the frame counter, and the cadence DOUBLES
; after level 1: at level 1 it advances and spawns the board objects on one frame in
; four, runs the vertical-reposition machine on another of the four, and idles the
; remaining two -- and since the frame counter counts DOWN, the reposition frame comes
; round before the object frame, not after it; at
; every other level it alternates every frame with no idle at all. So both run twice as
; often from level 2 on. The test is level != 1, not level >= 2, so level 0 takes the
; fast cadence too.
service75mBoard:
26FA: 3E 04           LD      A,$04               ; board mask: 75m only
26FC: F7              RST     $30                 ; closed on any other board -- skip the body
26FD: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read Mario's screen row
2700: FE F0           CP      $F0                 ; off the bottom of the display?
2702: D2 7F 27        JP      NC,$277F            ; {code.killMarioAtEndOfLiftTravel} yes -- that kills him
2705: 3A 29 62        LD      A,($6229)           ; {hard.workRam+229} read the level
2708: 3D              DEC     A                   
2709: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} read the frame counter
270C: C2 1A 27        JP      NZ,$271A            ; {code.loc_271a} past level 1 -- take the faster cadence
270F: E6 03           AND     $03                 ; level 1 services one frame in four
2711: FE 01           CP      $01                 
2713: CA 1E 27        JP      Z,$271E             ; {code.loc_271e} this frame runs the lift-ride machine
2716: DA 22 27        JP      C,$2722             ; {code.serviceBoardObjects} and this one the board objects
2719: C9              RET                         ; the other two frames idle

loc_271a:
271A: 0F              RRCA                        
271B: DA 22 27        JP      C,$2722             ; {code.serviceBoardObjects} alternate every frame, no idle at all

loc_271e:
271E: CD 45 27        CALL    $2745               ; {code.dispatchElevatorRideByColumn} run the lift-ride machine
2721: C9              RET                         

; Service the six 16-byte records of objArray66 for one pass, then publish them. Three
; things, in order. ADVANCE: step every active object one pixel toward its limit, landing
; or deactivating it on arrival. SPAWN: on the spawn cadence, claim a free slot and seed
; a new object; otherwise just tick the cadence timer. PUBLISH: walk all six records and
; copy each object's X and Y into its own 4-byte sprite record in the shadow buffer, X at
; the record's first byte and Y at its fourth, the six sitting consecutively from
; spriteBuffer + 88. The order matters -- advance and spawn are what MOVE the objects,
; and the publish walk reads the positions they just produced.
serviceBoardObjects:
2722: CD 97 27        CALL    $2797               ; {code.advanceBoardObjectTravel} step every active object one pixel
2725: CD DA 27        CALL    $27DA               ; {code.spawnBoardObject} spawn a new one on the cadence
2728: 06 06           LD      B,$06               ; six records to publish
272A: 11 10 00        LD      DE,$0010            ; 16 bytes per object record
272D: 21 58 69        LD      HL,$6958            ; the six sprite records that draw them
2730: DD 21 00 66     LD      IX,$6600            ; the object array

loc_2734:
2734: DD 7E 03        LD      A,(IX+$03)          ; the object's X
2737: 77              LD      (HL),A              ; into the sprite record's first byte
2738: 2C              INC     L                   
2739: 2C              INC     L                   
273A: 2C              INC     L                   
273B: DD 7E 05        LD      A,(IX+$05)          ; the object's Y
273E: 77              LD      (HL),A              ; into the sprite record's fourth byte
273F: 2C              INC     L                   
2740: DD 19           ADD     IX,DE               ; on to the next object record
2742: 10 F0           DJNZ    $2734               ; {code.loc_2734}
2744: C9              RET                         

; While Mario is riding a lift, route him to the up-column or the down-column carry by
; his X. Two guards drop the whole routine: the standing-on-a-lift flag clear, or Mario
; airborne, leaving the carry for a grounded frame. Past both it reads marioX and routes
; by band, one band per lift column: the lower band is the RISING column and carries him
; up, the higher band the DESCENDING one and carries him down. Each carry steps his Y one
; pixel with the lift, mirrors that to his sprite record, and hands off to a check that
; KILLS Mario -- clearing marioActive -- once his Y crosses that column's own fixed row
; limit, read without reference to where the lift has got to. The bands are the columns
; because a lift is spawned at X 55 and teleported to X 119 the instant it finishes
; rising, dead centre of one band each. A third arm covers every other X.
dispatchElevatorRideByColumn:
2745: 3A 98 63        LD      A,($6398)           ; {hard.workRam+398} the lift flag: is he riding one?
2748: A7              AND     A                   
2749: C8              RET     Z                   ; no -- nothing to carry
274A: 3A 16 62        LD      A,($6216)           ; {hard.workRam+216} is he airborne?
274D: A7              AND     A                   
274E: C0              RET     NZ                  ; yes -- carry him only on a grounded frame
274F: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} read his column
2752: FE 2C           CP      $2C                 ; left of both lift columns
2754: DA 66 27        JP      C,$2766             ; {code.loc_2766}
2757: FE 43           CP      $43                 ; in the rising column -- carry him up
2759: DA 6F 27        JP      C,$276F             ; {code.carryMarioUpWithLift}
275C: FE 6C           CP      $6C                 ; between the two columns
275E: DA 66 27        JP      C,$2766             ; {code.loc_2766}
2761: FE 83           CP      $83                 ; in the descending column -- carry him down
2763: DA 87 27        JP      C,$2787             ; {code.carryMarioDownWithLift}

loc_2766:
2766: AF              XOR     A                   
2767: 32 98 63        LD      ($6398),A           ; {hard.workRam+398} clear the lift flag
276A: 3C              INC     A                   
276B: 32 21 62        LD      ($6221),A           ; {hard.workRam+221} and start him falling
276E: C9              RET                         

; The rising arm of the lift ride. Once marioY has come up past the limit row 0x71 --
; smaller Y is higher on this screen -- it hands off to the kill, which clears
; marioActive; the death animation runs and a life is lost. Otherwise it takes one off
; marioY, moving him a single pixel up, and mirrors the new value into the Y field of
; marioSpriteRecord so the sprite follows the same frame. The limit is an ABSOLUTE row
; of Mario's, not the lift's end of travel: this arm never reads an object record, and
; since he rides eleven or twelve pixels above the platform he is standing on, he
; crosses the limit row while the platform still has climb left and it carries on past
; him.
carryMarioUpWithLift:
276F: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read Mario's screen row
2772: FE 71           CP      $71                 ; has he risen past the top limit row?
2774: DA 7F 27        JP      C,$277F             ; {code.killMarioAtEndOfLiftTravel} yes -- the ride kills him
2777: 3D              DEC     A                   ; one pixel up the screen
2778: 32 05 62        LD      ($6205),A           ; {hard.workRam+205}
277B: 32 4F 69        LD      ($694F),A           ; {hard.workRam+94F} mirror it into his sprite record's Y
277E: C9              RET                         

; Kill Mario at the end of his run on a 75m lift. Both carries tail in here the moment
; his Y leaves the band their arm allows: the up-carry steps Y down one a frame, which
; is UP the screen, and arrives once his row is below 113; the down-carry steps it up
; and arrives at row 232 or beyond. This then unconditionally clears marioActive and
; edgeRepositionFlag and returns -- no inputs, no branches, always the same two zeros.
; Zeroing marioActive IS the game's kill primitive, not merely switching the mover off:
; it freezes Mario and runs the death animation, then the life decrement, then the
; respawn. Both carries compare an ABSOLUTE Mario row against a constant and read no
; lift record, so the two limits do not coincide with the platform's -- on the up arm
; the rising column runs on another 27-28 pixels after he is dead. A third caller
; reaches the same write: Mario dropping off the bottom of a 75m board.
killMarioAtEndOfLiftTravel:
277F: AF              XOR     A                   
2780: 32 00 62        LD      ($6200),A           ; {hard.workRam+200} clear the alive flag -- he dies here
2783: 32 98 63        LD      ($6398),A           ; {hard.workRam+398} and the lift flag with it
2786: C9              RET                         

; Carry Mario one pixel DOWN the screen while he rides a descending lift, or kill him
; once he reaches the bottom of his own run. On the lift board the lifts run in two
; columns, one rising and one descending, and this is the arm the ride handler picks
; while Mario stands in the descending column. marioY is the sole input: still above the
; bottom-of-run row and his Y is advanced by one -- a single pixel down, since larger Y
; is lower -- and mirrored into the Y field of his sprite record so the drawn sprite
; tracks the move; at or past that row his run is over and control passes to the kill,
; which clears the flag keeping him active. The limit is an absolute screen row for
; MARIO, not the lift's end of travel: no object record is read here at all, and the lift
; itself keeps going a few pixels past the row that kills him.
carryMarioDownWithLift:
2787: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read Mario's screen row
278A: FE E8           CP      $E8                 ; reached the bottom of his run?
278C: D2 7F 27        JP      NC,$277F            ; {code.killMarioAtEndOfLiftTravel} yes -- the ride kills him
278F: 3C              INC     A                   ; one pixel down the screen
2790: 32 05 62        LD      ($6205),A           ; {hard.workRam+205}
2793: 32 4F 69        LD      ($694F),A           ; {hard.workRam+94F} mirror it into his sprite record's Y
2796: C9              RET                         

; Advance the six board objects in the 0x6600 array: each active object drifts one pixel
; vertically toward its limit, then lands or deactivates on arrival. The array is 75m-only
; and the drift matches the moving platforms, but nothing in the code names these objects,
; so this describes what they DO rather than what they are. The array is six 16-byte records, all
; six walked once per board-object service pass, and a record is processed only while bit
; 0 of its active flag is set. Bit 3 of the state byte picks the direction, and larger Y
; is lower on screen. Bit 3 set means rising, so Y decreases, and on reaching row 96 the
; object LANDS -- X snaps to column 119 and the state byte becomes 4, which clears bit 3
; so the next pass falls. Bit 3 clear means falling, so Y increases, and on reaching row
; 248 the object DEACTIVATES. The 16-byte stride is RETURNED, and load-bearing: the spawn
; walk that runs next in the same pass reuses it without reloading.
advanceBoardObjectTravel:
2797: 06 06           LD      B,$06               ; six records to walk
2799: 11 10 00        LD      DE,$0010            ; 16-byte stride -- the spawn walk reuses it
279C: DD 21 00 66     LD      IX,$6600            ; the object array

loc_27a0:
27A0: DD CB 00 46     BIT     0,(IX+$00)          ; skip an inactive slot
27A4: CA C2 27        JP      Z,$27C2             ; {code.loc_27c2}
27A7: DD CB 0D 5E     BIT     3,(IX+$0D)          ; bit 3 of the state picks rising or falling
27AB: CA C7 27        JP      Z,$27C7             ; {code.loc_27c7} clear -- this one is falling
27AE: DD 7E 05        LD      A,(IX+$05)          
27B1: 3D              DEC     A                   ; rising: one pixel up the screen
27B2: DD 77 05        LD      (IX+$05),A          
27B5: FE 60           CP      $60                 ; reached the landing row?
27B7: C2 C2 27        JP      NZ,$27C2            ; {code.loc_27c2}
27BA: DD 36 03 77     LD      (IX+$03),$77        ; snap it to the landing column
27BE: DD 36 0D 04     LD      (IX+$0D),$04        ; clear bit 3, so the next pass falls

loc_27c2:
27C2: DD 19           ADD     IX,DE               ; on to the next record
27C4: 10 DA           DJNZ    $27A0               ; {code.loc_27a0}
27C6: C9              RET                         

loc_27c7:
27C7: DD 7E 05        LD      A,(IX+$05)          
27CA: 3C              INC     A                   ; falling: one pixel down the screen
27CB: DD 77 05        LD      (IX+$05),A          
27CE: FE F8           CP      $F8                 ; off the bottom of its travel?
27D0: C2 C2 27        JP      NZ,$27C2            ; {code.loc_27c2}
27D3: DD 36 00 00     LD      (IX+$00),$00        ; deactivate the slot
27D7: C3 C2 27        JP      $27C2               ; {code.loc_27c2}

; The periodic allocator behind the objArray66 board objects, called once per pass from
; the object service after the live ones have been animated. While spawnTimer is nonzero
; nothing spawns -- the timer is simply ticked down one and it returns. At zero it scans
; the six records for the first whose active flag's low bit is clear, claims it, marks
; it active and stamps a fixed spawn position (X 0x37, Y 0xF8, near the bottom of the
; screen) with initial state 0x08, then reloads the cooldown to 0x34 and ticks it once,
; so it lands at reload minus one. If every slot is busy it gives up WITHOUT reloading
; or ticking, leaving the timer at zero so it retries every following pass. What kind of
; object this seeds is not claimed here.
spawnBoardObject:
27DA: 21 A7 62        LD      HL,$62A7            ; the spawn-cadence timer
27DD: 7E              LD      A,(HL)              
27DE: A7              AND     A                   
27DF: C2 06 28        JP      NZ,$2806            ; {code.decrementByteAt} still cooling down -- just tick it
27E2: 06 06           LD      B,$06               ; six slots to try
27E4: DD 21 00 66     LD      IX,$6600            

loc_27e8:
27E8: DD CB 00 46     BIT     0,(IX+$00)          ; look for a free slot
27EC: CA F4 27        JP      Z,$27F4             ; {code.loc_27f4}
27EF: DD 19           ADD     IX,DE               
27F1: 10 F5           DJNZ    $27E8               ; {code.loc_27e8} on to the next slot
27F3: C9              RET                         ; every slot busy -- retry next pass

loc_27f4:
27F4: DD 36 00 01     LD      (IX+$00),$01        ; claim the slot
27F8: DD 36 03 37     LD      (IX+$03),$37        ; seed its column
27FC: DD 36 05 F8     LD      (IX+$05),$F8        ; and its row, near the bottom of the screen
2800: DD 36 0D 08     LD      (IX+$0D),$08        ; state 8: bit 3 set, so it starts rising
2804: 36 34           LD      (HL),$34            ; reload the cooldown

; Take one off the byte at the address handed in -- load, subtract one (0 wrapping back
; to 255), store it back, and nothing else. The target is a parameter, not a fixed cell.
decrementByteAt:
2806: 35              DEC     (HL)                ; tick the caller's byte down by one
2807: C9              RET                         

; Kill Mario when a board object overlaps his hitbox. Once a frame it asks the current
; board's collision handler whether any active object -- barrel, fireball, oil flame --
; overlaps him. The test is a bounding box centred on Mario: his Y goes in as the compare
; coordinate, his X is read by the handler out of his context block, and the half-extents
; are 4 wide and 7 tall. The handler sweeps its arrays and reports 1 or 0. On 0 nothing
; happens; on 1 that byte minus one, i.e. 0, goes into marioActive, which the movement
; machine reads as death and turns into the death, life-loss and respawn cycle.
killMarioOnObjectCollision:
2808: FD 21 00 62     LD      IY,$6200            ; Mario's record is the reference point
280C: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read his screen row
280F: 4F              LD      C,A                 
2810: 21 07 04        LD      HL,$0407            ; half-extents: 4 across and 7 down
2813: CD 6F 28        CALL    $286F               ; {code.dispatchBoardCollision} ask this board's collision handler

loc_2816:
2816: A7              AND     A                   
2817: C8              RET     Z                   ; nothing overlapped him
2818: 3D              DEC     A                   ; a hit reports 1; one less is 0
2819: 32 00 62        LD      ($6200),A           ; {hard.workRam+200} clear the alive flag -- he dies
281C: C9              RET                         

recordHammerHitOnObject:
281D: 06 02           LD      B,$02               ; the hammer pair: two records
281F: 11 10 00        LD      DE,$0010            
2822: FD 21 80 66     LD      IY,$6680            

loc_2826:
2826: FD CB 01 46     BIT     0,(IY+$01)          ; which one is in play?
282A: C2 32 28        JP      NZ,$2832            ; {code.loc_2832}
282D: FD 19           ADD     IY,DE               
282F: 10 F5           DJNZ    $2826               ; {code.loc_2826}
2831: C9              RET                         ; no hammer in play -- nothing to test

loc_2832:
2832: FD 4E 05        LD      C,(IY+$05)          ; the hammer's own row
2835: FD 66 09        LD      H,(IY+$09)          ; and its hit box, re-stamped each frame from the swing pose
2838: FD 6E 0A        LD      L,(IY+$0A)          
283B: CD 6F 28        CALL    $286F               ; {code.dispatchBoardCollision} what is the hammer touching?
283E: A7              AND     A                   
283F: C8              RET     Z                   ; it struck nothing this frame
2840: 32 50 63        LD      ($6350),A           ; {hard.workRam+350} raise the hit-effect latch: play is suspended
2843: 3A B9 63        LD      A,($63B9)           ; {hard.workRam+3B9} the count the sweep started with
2846: 90              SUB     B                   ; less the ones still to go: which record was struck
2847: 32 54 63        LD      ($6354),A           ; {hard.workRam+354}
284A: 7B              LD      A,E                 ; the stride the board's sweep was walking
284B: 32 53 63        LD      ($6353),A           ; {hard.workRam+353}
284E: DD 22 51 63     LD      ($6351),IX          ; {hard.workRam+351} and the array it came from
2852: C9              RET                         

; Run the current board's object-overlap search for Mario and hand its severity code
; back. A thin setup-and-dispatch step: it stages the object-record base the board's arm
; walks, a search bound taken from Mario's Y plus a fixed offset of 12 -- so the probe
; point is twelve pixels BELOW him, not on him -- and an overlap-threshold word chosen by
; whether a left/right direction is held, whose low and high bytes become the two
; per-axis thresholds. The dispatch is a genuine tail call. The board's arm counts how
; many active objects overlap and grades the total into 0, 1, 3 or 7 -- not a scale but a
; unary thermometer, zero to three bits set, because the consumer walks those low bits
; one at a time. This is the "how many did he jump over?" search, not the "did something
; hit him?" one.
searchPlayerObjectOverlap:
2853: FD 21 00 62     LD      IY,$6200            ; Mario's record is the reference point
2857: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read his screen row
285A: C6 0C           ADD     A,$0C               ; probe twelve pixels below him
285C: 4F              LD      C,A                 
285D: 3A 10 60        LD      A,($6010)           ; {hard.workRam+10} read the control word
2860: E6 03           AND     $03                 ; is left or right being held?
2862: 21 08 05        LD      HL,$0508            ; the standing search window
2865: CA 6B 28        JP      Z,$286B             ; {code.loc_286b}
2868: 21 08 13        LD      HL,$1308            ; a wider window across while he moves

loc_286b:
286B: CD 88 3E        CALL    $3E88               ; {code.dispatchBoardOverlapSearch} run this board's overlap sweep
286E: C9              RET                         

; Vector a collision test to the current board's handler. It reads board and vectors
; through a six-entry jump table -- 1 = 25m girders, 2 = 50m, 3 = 75m, 4 = 100m rivets,
; with entries 0 and 5 null guard slots -- and board is never range-checked, so a stray
; value vectors off the table. The caller's position is genuine DATA, not call plumbing:
; it is PUSHED first, beneath the dispatch's own frame, and every handler recovers it
; with a pop as its opening act; drop the push and each handler pops the wrong stack
; word. The table index is an 8-BIT double of the board number, so 128 or more wraps the
; offset back into the start of the table rather than reading past its end. Each handler
; sweeps its board's object records for one overlapping the caller's position and leaves
; the hit/miss result its callers read back.
dispatchBoardCollision:
286F: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} read the current board
2872: E5              PUSH    HL                  ; the tolerance pair, for the handler to pop
2873: EF              RST     $28                 ; vector through the per-board table below

; ---- $2874-$287F: jump table ----
2874: 00 00 80 28 B0 28 E0 28 01 29 00 00

; The 25m arm of the per-board collision search, reached through the dispatcher's board
; table with the per-axis search tolerances already pushed. It recovers that pair and
; runs the shared bounding-box search over three object arrays in turn: ten objArray67
; barrel records at stride 0x20, then five objArray64 records at the same stride, then a
; single record with stride zero. Before each sweep it stamps that sweep's record count
; into objSearchCount, where the hit handler reads it back to recover the matched
; record's index. The FIRST sweep to find an overlapping record wins and stops the
; remaining sweeps; all three coming up empty reaches the same place the normal way.
; This is the only collision arm that sweeps the barrel array, which is why the board
; table vectors here for exactly this board.
search25mObjectOverlap:
2880: E1              POP     HL                  ; recover the per-axis tolerances
2881: 06 0A           LD      B,$0A               ; ten barrel records
2883: 78              LD      A,B                 
2884: 32 B9 63        LD      ($63B9),A           ; {hard.workRam+3B9} stamp the count, for index recovery
2887: 11 20 00        LD      DE,$0020            ; stride between barrel records
288A: DD 21 00 67     LD      IX,$6700            ; the barrel array
288E: CD 13 29        CALL    $2913               ; {code.findCollidingObject} first sweep -- a hit unwinds past here
2891: 06 05           LD      B,$05               ; five fire records
2893: 78              LD      A,B                 
2894: 32 B9 63        LD      ($63B9),A           ; {hard.workRam+3B9} stamp this sweep's count
2897: 1E 20           LD      E,$20               
2899: DD 21 00 64     LD      IX,$6400            ; the fire array
289D: CD 13 29        CALL    $2913               ; {code.findCollidingObject} second sweep
28A0: 06 01           LD      B,$01               ; one record: the board's fixed hazard
28A2: 78              LD      A,B                 
28A3: 32 B9 63        LD      ($63B9),A           ; {hard.workRam+3B9} stamp this sweep's count
28A6: 1E 00           LD      E,$00               
28A8: DD 21 A0 66     LD      IX,$66A0            ; the oil drum
28AC: CD 13 29        CALL    $2913               ; {code.findCollidingObject} third sweep
28AF: C9              RET                         

; The 50m arm of the board collision dispatch: three bounding-box sweeps in order,
; stopping at the first overlap. The dispatcher pushes the per-axis tolerances before
; jumping here; this recovers that pair and then runs the shared collision search three
; times, each time pointing it at a different object array and stamping that sweep's
; record count into objSearchCount, from which the found-handler recovers the matched
; record's index. Sweep 1 is the five-record array at stride 0x20, sweep 2 the six-record
; array of this board's own movers at stride 0x10, sweep 3 a single record at stride
; zero. A hit splices control straight back to the dispatch site and abandons the
; remaining sweeps, so the stored count is whichever sweep terminated the routine.
search50mObjectOverlap:
28B0: E1              POP     HL                  ; recover the per-axis tolerances
28B1: 06 05           LD      B,$05               ; five fire records
28B3: 78              LD      A,B                 
28B4: 32 B9 63        LD      ($63B9),A           ; {hard.workRam+3B9} stamp the count, for index recovery
28B7: 11 20 00        LD      DE,$0020            
28BA: DD 21 00 64     LD      IX,$6400            ; the fire array
28BE: CD 13 29        CALL    $2913               ; {code.findCollidingObject} first sweep -- a hit unwinds past here
28C1: 06 06           LD      B,$06               ; six of this board's travelling objects
28C3: 78              LD      A,B                 
28C4: 32 B9 63        LD      ($63B9),A           ; {hard.workRam+3B9} stamp this sweep's count
28C7: 1E 10           LD      E,$10               
28C9: DD 21 A0 65     LD      IX,$65A0            ; the 50m moving-object array
28CD: CD 13 29        CALL    $2913               ; {code.findCollidingObject} second sweep
28D0: 06 01           LD      B,$01               ; one record: the board's fixed hazard
28D2: 78              LD      A,B                 
28D3: 32 B9 63        LD      ($63B9),A           ; {hard.workRam+3B9} stamp this sweep's count
28D6: 1E 00           LD      E,$00               
28D8: DD 21 A0 66     LD      IX,$66A0            
28DC: CD 13 29        CALL    $2913               ; {code.findCollidingObject} third sweep
28DF: C9              RET                         

; The 75m arm of the board-overlap-search dispatch: two bounding-box sweeps, stopping at
; the first hit. It recovers the caller's per-axis tolerances from the stack and points
; the shared bounding-box search at two object arrays in turn -- first objArray64, 0x20
; stride, 5 records, then objArray65, 0x10 stride, 10 records. Before each sweep it
; records that sweep's object count in objSearchCount, where the found-handler reads it
; back to recover the matched record's index as the count minus the search's residual B.
; The short-circuit is what distinguishes this from the single-sweep arms: if sweep 1
; hits, the search takes its caller-skip return and unwinds PAST this routine, so sweep 2
; never runs and objSearchCount is left holding 5, not 10.
search75mObjectOverlap:
28E0: E1              POP     HL                  ; recover the per-axis tolerances
28E1: 06 05           LD      B,$05               ; five fire records
28E3: 78              LD      A,B                 
28E4: 32 B9 63        LD      ($63B9),A           ; {hard.workRam+3B9} stamp the count, for index recovery
28E7: 11 20 00        LD      DE,$0020            
28EA: DD 21 00 64     LD      IX,$6400            ; the fire array
28EE: CD 13 29        CALL    $2913               ; {code.findCollidingObject} first sweep -- a hit unwinds past here
28F1: 06 0A           LD      B,$0A               ; ten spring records
28F3: 78              LD      A,B                 
28F4: 32 B9 63        LD      ($63B9),A           ; {hard.workRam+3B9} stamp this sweep's count
28F7: 1E 10           LD      E,$10               
28F9: DD 21 00 65     LD      IX,$6500            ; the spring array
28FD: CD 13 29        CALL    $2913               ; {code.findCollidingObject} second sweep, only reached on a miss
2900: C9              RET                         

; The 100m arm of the board-overlap dispatch: one bounding-box collision sweep over
; objArray64, the hazard array 100m uses. It recovers the per-axis search tolerances the
; dispatcher pushed, records the sweep's object count in objSearchCount where the
; found-handler reads it back, and points the shared bounding-box search at objArray64
; with seven records at a 0x20 stride for a single scan. A hit sets the result byte to 1
; and leaves the count-minus-index residue behind so the matched record's index can be
; recovered; an exhausted scan leaves the result byte 0. It is the single-sweep member
; of a family -- the other boards run two or three sweeps over different arrays.
search100mObjectOverlap:
2901: E1              POP     HL                  ; recover the per-axis tolerances
2902: 06 07           LD      B,$07               ; seven fire records on this board
2904: 78              LD      A,B                 
2905: 32 B9 63        LD      ($63B9),A           ; {hard.workRam+3B9} stamp the count, for index recovery
2908: 11 20 00        LD      DE,$0020            
290B: DD 21 00 64     LD      IX,$6400            ; the fire array
290F: CD 13 29        CALL    $2913               ; {code.findCollidingObject} the single sweep
2912: C9              RET                         

; The collision primitive: scan an object list for the first record whose bounding box
; overlaps a reference point on both axes. A board collision handler points it at one of
; its arrays and hands it a reference coordinate pair -- in practice Mario's position --
; plus a per-axis base tolerance. For each ACTIVE record:
;   axis 1: |reference - record+5| + 1 must fall inside the base window, or past that
;           inside the record's own extra span at +0x0a;
;   axis 2: |reference - record+3|     must fall inside the base window, or past that
;           inside the record's own extra span at +9.
; A record with bit 0 of its flag byte (+0) clear is inactive and skipped, as is one
; that fails either axis. The FIRST record passing both is a hit and the scan stops
; there, the caller's post-call code being skipped so its own caller resumes; the result
; byte is 1 on a hit and 0 on exhaustion, with the count less the matched index left for
; the caller to recover that index. A count of zero on entry is NOT guarded: it scans
; 256 records.
findCollidingObject:
2913: DD E5           PUSH    IX                  ; save the array base for the exit

loc_2915:
2915: DD CB 00 46     BIT     0,(IX+$00)          ; skip an inactive record
2919: CA 4C 29        JP      Z,$294C             ; {code.loc_294c}
291C: 79              LD      A,C                 ; the reference point on the first axis
291D: DD 96 05        SUB     (IX+$05)            ; distance out to this record
2920: D2 25 29        JP      NC,$2925            ; {code.loc_2925}
2923: ED 44           NEG                         ; take it unsigned

loc_2925:
2925: 3C              INC     A                   
2926: 95              SUB     L                   ; inside the base window?
2927: DA 30 29        JP      C,$2930             ; {code.loc_2930} yes -- try the other axis
292A: DD 96 0A        SUB     (IX+$0A)            ; otherwise allow the record's own extra span
292D: D2 4C 29        JP      NC,$294C            ; {code.loc_294c} still outside -- this record misses

loc_2930:
2930: FD 7E 03        LD      A,(IY+$03)          ; the reference point on the second axis
2933: DD 96 03        SUB     (IX+$03)            ; distance out to this record
2936: D2 3B 29        JP      NC,$293B            ; {code.loc_293b}
2939: ED 44           NEG                         ; take it unsigned

loc_293b:
293B: 94              SUB     H                   ; inside the base window?
293C: DA 45 29        JP      C,$2945             ; {code.loc_2945}
293F: DD 96 09        SUB     (IX+$09)            ; otherwise the record's own extra span
2942: D2 4C 29        JP      NC,$294C            ; {code.loc_294c} still outside -- this record misses

loc_2945:
2945: 3E 01           LD      A,$01               ; both axes overlap -- report a hit
2947: DD E1           POP     IX                  
2949: 33              INC     SP                  ; step over the caller's return, skipping it
294A: 33              INC     SP                  
294B: C9              RET                         

loc_294c:
294C: DD 19           ADD     IX,DE               ; on to the next record
294E: 10 C5           DJNZ    $2915               ; {code.loc_2915}
2950: AF              XOR     A                   ; the list is exhausted -- no overlap
2951: DD E1           POP     IX                  
2953: C9              RET                         

; Latch whether Mario is touching one of the two hammer records, and mark which one. A
; board gate comes first, with a mask naming exactly the boards a hammer appears on --
; 25m, 50m and 100m; 75m is the one hammer-free board. Then a search tests his position
; against the two-record pair and leaves an overlap flag plus an index naming the matched
; record. The flag is stored UNCONDITIONALLY into marioHammerPending and drives the item
; sound trigger -- asserted for 64 frames on a touch, silenced on a miss -- so a run with
; no overlap clears a latch and a sound a previous run set. On an overlap only, the
; touched record's in-play field is set to 1, and both the hammer-hit collision scan and
; the hammer sprite driver read that mark to find the right record. Nothing here puts the
; hammer in Mario's hands: the movement machine transfers the pending flag into the
; held-hammer flag once the post-landing freeze expires.
latchHammerTouch:
2954: 3E 0B           LD      A,$0B               ; board mask: 25m, 50m and 100m carry hammers
2956: F7              RST     $30                 ; closed on 75m -- skip the body
2957: CD 74 29        CALL    $2974               ; {code.findHammerOverlappingMario} is Mario touching either hammer?
295A: 32 18 62        LD      ($6218),A           ; {hard.workRam+218} publish the touch; a miss clears it
295D: 0F              RRCA                        ; turn a touch into 0x40
295E: 0F              RRCA                        
295F: 32 85 60        LD      ($6085),A           ; {hard.workRam+85} hold the pickup sound line for 64 frames
2962: 78              LD      A,B                 ; which record did the search match?
2963: A7              AND     A                   
2964: C8              RET     Z                   ; nothing overlapped -- nothing to mark
2965: FE 01           CP      $01                 ; a residue of 1 means the second record
2967: CA 6F 29        JP      Z,$296F             ; {code.loc_296f}
296A: DD 36 01 01     LD      (IX+$01),$01        ; mark the first hammer as the one in play
296E: C9              RET                         

loc_296f:
296F: DD 36 11 01     LD      (IX+$11),$01        ; mark the second hammer instead
2973: C9              RET                         

; Test whether Mario overlaps either of the two hammer objects, and report which one. A
; thin front end over the shared object-list bounding-box search, fixing its parameters
; for this one query: the records are the two-object hammer pair at the object-record
; stride; the reference point is Mario, his Y as the first axis and his X as the second,
; reached by aiming the reference pointer at the base of his live block; and the per-axis
; base tolerances are 8 and 4. The search stops at the first active record whose box
; overlaps him on both axes. This routine writes no memory at all and only reports the
; overlap -- the caller records a "touched but not yet held" hammer from the result and
; triggers the hammer-grab sound. Which of the two records is which hammer is not
; established.
findHammerOverlappingMario:
2974: FD 21 00 62     LD      IY,$6200            ; Mario's record supplies the reference X
2978: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read his screen row
297B: 4F              LD      C,A                 
297C: 21 08 04        LD      HL,$0408            ; allow 8 on the row and 4 across
297F: 06 02           LD      B,$02               ; the two hammer records
2981: 11 10 00        LD      DE,$0010            ; 16 bytes apart
2984: DD 21 80 66     LD      IX,$6680            ; the hammer pair
2988: CD 13 29        CALL    $2913               ; {code.findCollidingObject}
298B: C9              RET                         

; Report that a fire has reached the edge of the ground it is walking on. The answer is
; the SOLE thing its caller uses to decide to turn the fire around. It takes the record
; objIterPtr points at and probes the tile 12 pixels BELOW the fire -- the same axis and
; offset Mario's own ground test uses. It does NOT look ahead of the fire, and the axis
; the fire travels along is left exactly as the record holds it. The verdict is a plain
; predicate on the tile found there: below 0xB0 is OUT of band; at or above 0xB0 with
; the low nibble 8 or more is OUT; at or above 0xB0 with the low nibble under 8 is IN.
; So the accepted band is the high half of the tile set with the low nibble kept under
; 8, and ground ends where that band ends, which is why an out-of-band answer is an EDGE
; and not just a different tile. It writes no memory.
turnFireAtGroundEdge:
298C: 2A C8 63        LD      HL,($63C8)          ; {hard.workRam+3C8} the record the fire driver is walking
298F: 7D              LD      A,L                 ; step out to the record's position pair
2990: C6 0E           ADD     A,$0E               
2992: 6F              LD      L,A                 
2993: 56              LD      D,(HL)              ; the fire's column
2994: 2C              INC     L                   
2995: 7E              LD      A,(HL)              
2996: C6 0C           ADD     A,$0C               ; twelve pixels below it -- the ground beneath
2998: 5F              LD      E,A                 
2999: EB              EX      DE,HL               
299A: CD F0 2F        CALL    $2FF0               ; {code.tileAddrForPixel} find the tile that contains that point
299D: 7E              LD      A,(HL)              ; read the tile there
299E: FE B0           CP      $B0                 ; below the ground band -- not ground
29A0: DA AC 29        JP      C,$29AC             ; {code.loc_29ac}
29A3: E6 0F           AND     $0F                 ; within the band, the low nibble decides
29A5: FE 08           CP      $08                 ; 8 or more is outside it too
29A7: D2 AC 29        JP      NC,$29AC            ; {code.loc_29ac}
29AA: AF              XOR     A                   ; still on ground -- keep the fire walking
29AB: C9              RET                         

loc_29ac:
29AC: 3E 01           LD      A,$01               ; the ground has ended -- turn the fire round
29AE: C9              RET                         

loc_29af:
29AF: 3E 04           LD      A,$04               ; board mask: 75m only
29B1: F7              RST     $30                 ; closed on any other board -- skip the body
29B2: FD 21 00 62     LD      IY,$6200            ; Mario's record is the reference point
29B6: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} read his screen row
29B9: 4F              LD      C,A                 
29BA: 21 08 04        LD      HL,$0408            ; allow 8 on the row and 4 across
29BD: CD 22 2A        CALL    $2A22               ; {code.loc_2a22} does he touch any of the six objects?
29C0: A7              AND     A                   
29C1: CA 20 2A        JP      Z,$2A20             ; {code.loc_2a20} no contact -- nothing to resolve
29C4: 3E 06           LD      A,$06               ; the record count the search started with
29C6: 90              SUB     B                   ; less its residue: the matched record's index

loc_29c7:
29C7: CA D0 29        JP      Z,$29D0             ; {code.loc_29d0}
29CA: DD 19           ADD     IX,DE               ; walk out to that record
29CC: 3D              DEC     A                   
29CD: C3 C7 29        JP      $29C7               ; {code.loc_29c7}

loc_29d0:
29D0: DD 7E 05        LD      A,(IX+$05)          ; the object's own row
29D3: D6 04           SUB     $04                 ; its contact line sits four above it
29D5: 57              LD      D,A                 
29D6: 3A 0C 62        LD      A,($620C)           ; {hard.workRam+20C} where he was before this frame's motion
29D9: C6 05           ADD     A,$05               
29DB: BA              CP      D                   
29DC: D2 EE 29        JP      NC,$29EE            ; {code.loc_29ee} not clearly above the line -- try below
29DF: 7A              LD      A,D                 ; he lands: a standing height above the line
29E0: D6 08           SUB     $08                 
29E2: 32 05 62        LD      ($6205),A           ; {hard.workRam+205} place him there
29E5: 3E 01           LD      A,$01               
29E7: 47              LD      B,A                 
29E8: 32 98 63        LD      ($6398),A           ; {hard.workRam+398} raise the just-repositioned one-shot
29EB: 33              INC     SP                  ; skip the caller -- the handler above resumes
29EC: 33              INC     SP                  
29ED: C9              RET                         

loc_29ee:
29EE: 3A 0C 62        LD      A,($620C)           ; {hard.workRam+20C} where Mario was before this frame's motion
29F1: D6 0E           SUB     $0E                 ; clearance for the below-the-line test
29F3: BA              CP      D                   ; against the object's contact line
29F4: D2 1B 2A        JP      NC,$2A1B            ; {code.loc_2a1b} clearly below it -- Mario is killed
29F7: 3A 10 62        LD      A,($6210)           ; {hard.workRam+210} route selector: airborne horizontal speed
29FA: A7              AND     A                   
29FB: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} his X, the value both routes snap
29FE: CA 08 2A        JP      Z,$2A08             ; {code.loc_2a08} no speed: take the sibling snap arm
2A01: F6 07           OR      $07                 ; reach the right edge of his 8-pixel cell
2A03: D6 04           SUB     $04                 ; and step back to its middle
2A05: C3 0E 2A        JP      $2A0E               ; {code.loc_2a0e}

loc_2a08:
2A08: D6 08           SUB     $08                 ; the other route to the same snapped X
2A0A: F6 07           OR      $07                 
2A0C: C6 04           ADD     A,$04               

loc_2a0e:
2A0E: 32 03 62        LD      ($6203),A           ; {hard.workRam+203} side-on contact: put him in the cell middle
2A11: 32 4C 69        LD      ($694C),A           ; {hard.workRam+94C} so the sprite follows him
2A14: 3E 01           LD      A,$01               ; report the contact
2A16: 06 00           LD      B,$00               ; 0 tells the airborne handler to keep him falling
2A18: 33              INC     SP                  ; discard the caller's return so it is skipped
2A19: 33              INC     SP                  
2A1A: C9              RET                         

loc_2a1b:
2A1B: AF              XOR     A                   
2A1C: 32 00 62        LD      ($6200),A           ; {hard.workRam+200} struck from below -- Mario dies
2A1F: C9              RET                         

loc_2a20:
2A20: 47              LD      B,A                 
2A21: C9              RET                         

loc_2a22:
2A22: 06 06           LD      B,$06               ; six records in this board's object array
2A24: 11 10 00        LD      DE,$0010            ; 16 bytes apart
2A27: DD 21 00 66     LD      IX,$6600            ; the array to search
2A2B: CD 13 29        CALL    $2913               ; {code.findCollidingObject} does Mario overlap any of the six?
2A2E: C9              RET                         

loc_2a2f:
2A2F: DD 7E 03        LD      A,(IX+$03)          ; the object's X
2A32: 67              LD      H,A                 
2A33: DD 7E 05        LD      A,(IX+$05)          ; the object's Y
2A36: C6 04           ADD     A,$04               ; probe 4 pixels below it
2A38: 6F              LD      L,A                 
2A39: E5              PUSH    HL                  ; keep the probe pixel; the lookup destroys it
2A3A: CD F0 2F        CALL    $2FF0               ; {code.tileAddrForPixel} find the tilemap cell under the probe
2A3D: D1              POP     DE                  ; recover the probe pixel
2A3E: 7E              LD      A,(HL)              ; the tile the object is over
2A3F: FE B0           CP      $B0                 ; below the girder band: nothing to stand on
2A41: DA 7B 2A        JP      C,$2A7B             ; {code.loc_2a7b} report no contact
2A44: E6 0F           AND     $0F                 
2A46: FE 08           CP      $08                 ; a low nibble of 8+ is the tile pair's far half
2A48: D2 7B 2A        JP      NC,$2A7B            ; {code.loc_2a7b}
2A4B: 7E              LD      A,(HL)              ; re-read the tile unmasked
2A4C: FE C0           CP      $C0                 ; the plain 0xC0 tile is not a girder surface
2A4E: CA 7B 2A        JP      Z,$2A7B             ; {code.loc_2a7b}
2A51: DA 69 2A        JP      C,$2A69             ; {code.loc_2a69} 0xB0-0xBF: surface one pixel above the cell
2A54: FE D0           CP      $D0                 
2A56: DA 6E 2A        JP      C,$2A6E             ; {code.loc_2a6e} 0xC1-0xCF: offset is the nibble less 9
2A59: FE E0           CP      $E0                 
2A5B: DA 63 2A        JP      C,$2A63             ; {code.loc_2a63} 0xD0-0xDF: offset is the nibble less 1
2A5E: FE F0           CP      $F0                 
2A60: DA 6E 2A        JP      C,$2A6E             ; {code.loc_2a6e} 0xE0-0xEF: the nibble less 9 again

loc_2a63:
2A63: E6 0F           AND     $0F                 
2A65: 3D              DEC     A                   ; the nibble less 1 -- this cell's surface row
2A66: C3 72 2A        JP      $2A72               ; {code.loc_2a72}

loc_2a69:
2A69: 3E FF           LD      A,$FF               ; surface sits one pixel above the cell edge
2A6B: C3 72 2A        JP      $2A72               ; {code.loc_2a72}

loc_2a6e:
2A6E: E6 0F           AND     $0F                 
2A70: D6 09           SUB     $09                 ; the nibble less 9 -- this cell's surface row

loc_2a72:
2A72: 4F              LD      C,A                 
2A73: 7B              LD      A,E                 ; the probe's own row
2A74: E6 F8           AND     $F8                 ; rounded back to its 8-pixel cell boundary
2A76: 81              ADD     A,C                 ; plus the slope offset: the girder surface
2A77: BB              CP      E                   ; has the object reached it?
2A78: DA 7D 2A        JP      C,$2A7D             ; {code.loc_2a7d} surface above the probe -- it has landed

loc_2a7b:
2A7B: AF              XOR     A                   ; report no contact
2A7C: C9              RET                         

loc_2a7d:
2A7D: D6 04           SUB     $04                 ; undo the 4-pixel probe nudge
2A7F: DD 77 05        LD      (IX+$05),A          ; snap the object up onto the girder
2A82: 3E 01           LD      A,$01               ; report contact
2A84: C9              RET                         

; While Mario is in plain standing or walking contact, look at the tile under his foot
; and, if the girder there is not level, defer to the slope-footing fall check. It
; early-outs if marioOnLadder, if marioAirborne, or while an edge-reposition runs. Past
; those three gates it samples the tilemap cell just under his foot -- 3 pixels back
; along his X, 12 along his Y. A solid flat girder there, a tile code at or above 0xB0
; whose low nibble is under 8, means level footing and there is nothing to do. Anything
; else -- a slope tile, or a girder tile whose low nibble is 8 or more -- means the
; ground may be angled or gone, and it hands off to the slope decision, which chooses
; between keeping his footing and starting a fall. The whole cascade below here has
; exactly ONE memory effect, raising marioStartFall, so starting a fall is all it can
; cause; nothing in it writes marioY.
startMarioFallWhenGroundGivesWay:
2A85: 3A 15 62        LD      A,($6215)           ; {hard.workRam+215} footing is not in question while on a ladder
2A88: A7              AND     A                   
2A89: C0              RET     NZ                  
2A8A: 3A 16 62        LD      A,($6216)           ; {hard.workRam+216} nor while he is already in the air
2A8D: A7              AND     A                   
2A8E: C0              RET     NZ                  
2A8F: 3A 98 63        LD      A,($6398)           ; {hard.workRam+398} nor while an edge reposition is running
2A92: FE 01           CP      $01                 
2A94: C8              RET     Z                   
2A95: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} foot probe: 3 pixels back along his X
2A98: D6 03           SUB     $03                 
2A9A: 67              LD      H,A                 
2A9B: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} and 12 along his Y
2A9E: C6 0C           ADD     A,$0C               
2AA0: 6F              LD      L,A                 
2AA1: E5              PUSH    HL                  ; keep the probe pixel for the slope decision
2AA2: CD F0 2F        CALL    $2FF0               ; {code.tileAddrForPixel} the tilemap cell just under his foot
2AA5: D1              POP     DE                  
2AA6: 7E              LD      A,(HL)              ; the tile he is standing on
2AA7: FE B0           CP      $B0                 ; not a girder tile at all
2AA9: DA B4 2A        JP      C,$2AB4             ; {code.decideSlopeGirderFooting} the ground may be angled or gone
2AAC: E6 0F           AND     $0F                 
2AAE: FE 08           CP      $08                 ; a low nibble of 8+ means it is not flat
2AB0: D2 B4 2A        JP      NC,$2AB4            ; {code.decideSlopeGirderFooting}
2AB3: C9              RET                         ; flat girder underfoot: nothing to do

; Decide whether Mario keeps his footing on an angled girder or the ground has run out
; and he starts to fall. Reached from the foot-contact cascade once his foot-probe tile
; is a slope tile. Two ways the ground is judged to have gone, each starting a fall: he
; is exactly column-aligned (his sub-tile X offset is zero), so there is no girder edge
; to catch him; or the NEIGHBOURING tile -- one tilemap row back from the foot cell,
; which is a step of 8 pixels along his X rather than a vertical one, since the row term
; is built from X and mirrored -- is not a solid girder tile, code at or above 0xB0 with
; a low nibble under 8. A girder tile there means he is standing on the angled girder
; and keeps his footing. Starting the fall is a single
; one-shot request; the keeps-footing case writes nothing.
decideSlopeGirderFooting:
2AB4: 7A              LD      A,D                 ; the probe's offset within its tile
2AB5: E6 07           AND     $07                 
2AB7: CA CD 2A        JP      Z,$2ACD             ; {code.triggerMarioFall} column-aligned: no edge to catch him
2ABA: 01 20 00        LD      BC,$0020            ; one tilemap row
2ABD: ED 42           SBC     HL,BC               ; step to the cell one row back
2ABF: 7E              LD      A,(HL)              ; the tile there
2AC0: FE B0           CP      $B0                 ; no girder there -- the ground has run out
2AC2: DA CD 2A        JP      C,$2ACD             ; {code.triggerMarioFall}
2AC5: E6 0F           AND     $0F                 
2AC7: FE 08           CP      $08                 ; a far-half tile is not solid ground either
2AC9: D2 CD 2A        JP      NC,$2ACD            ; {code.triggerMarioFall}
2ACC: C9              RET                         ; girder found: he keeps his footing on the slope

; Raise the one-shot "start falling" trigger, because the ground under Mario went away.
; Reached from the slope/ledge contact check on the branches that find no girder under
; his foot. One store to marioStartFall, no callees and no return value; the player-state
; reset picks the trigger up on the next frame, puts Mario airborne with zero initial
; velocity, snapshots his height and clears the trigger -- so this single flag is what
; actually launches the fall.
triggerMarioFall:
2ACD: 3E 01           LD      A,$01               
2ACF: 32 21 62        LD      ($6221),A           ; {hard.workRam+221} raise the one-shot that launches the fall
2AD2: C9              RET                         

; Carry Mario along whichever 50m conveyor row he is standing on. The board runs three
; horizontally-drifting platform objects, one per row, each publishing a signed X-step
; for the frame; those three step publishers run just before this in the object update.
; The row is picked by EXACT marioY -- 0x50, 0x78 and 0xC8, one height per object rather
; than a band. Rows 1 and 3 carry him by m50Obj1Step and m50Obj3Step; row 2's object
; publishes a plus/minus pair and that row's own arm selects between them by Mario's X
; before carrying him. On any other Y he is on no moving row and is not carried at all.
carryMarioOnConveyorRow:
2AD3: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} his X, the value each mover adds its step to
2AD6: 47              LD      B,A                 
2AD7: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} which platform row is he standing on?
2ADA: FE 50           CP      $50                 ; the object-1 row
2ADC: CA EA 2A        JP      Z,$2AEA             ; {code.loc_2aea}
2ADF: FE 78           CP      $78                 ; the object-2 row
2AE1: CA F6 2A        JP      Z,$2AF6             ; {code.selectConveyorStepAndMoveMario}
2AE4: FE C8           CP      $C8                 ; the object-3 row
2AE6: CA F0 2A        JP      Z,$2AF0             ; {code.loc_2af0}
2AE9: C9              RET                         ; on no moving row: he is not carried

loc_2aea:
2AEA: 3A A3 63        LD      A,($63A3)           ; {hard.workRam+3A3} that row's published drift step
2AED: C3 02 2B        JP      $2B02               ; {code.moveMarioX} carry him by it

loc_2af0:
2AF0: 3A A6 63        LD      A,($63A6)           ; {hard.workRam+3A6} that row's published drift step
2AF3: C3 02 2B        JP      $2B02               ; {code.moveMarioX}

; The moving-platform row arm for the row Mario stands on at Y 0x78. Object 2's signed
; drift step is published as two shadow bytes, m50Obj2StepPos and m50Obj2StepNeg, and
; marioX selects which applies: from the far-right half of the range (X >= 0x80) the
; positive step, otherwise the negative one. The chosen step goes to the shared X mover
; as the drift velocity, which advances marioX by it and holds him inside the horizontal
; limits. 50m is the conveyor board, so what this does on screen is carry Mario along a
; running conveyor.
selectConveyorStepAndMoveMario:
2AF6: 78              LD      A,B                 ; Mario's X picks the sign of this row's step
2AF7: FE 80           CP      $80                 
2AF9: 3A A5 63        LD      A,($63A5)           ; {hard.workRam+3A5} the positive-drift shadow
2AFC: D2 02 2B        JP      NC,$2B02            ; {code.moveMarioX} far-right half of the range: drift positive
2AFF: 3A A4 63        LD      A,($63A4)           ; {hard.workRam+3A4} otherwise the negative-drift shadow

; Advance Mario's X by the current velocity, then hold it inside the horizontal limits.
; It runs on the moving-platform boards, called from the platform-row mover, which is
; what picks the row's drift velocity for a Mario riding an elevator or a conveyor. The
; new X is stamped into BOTH marioX and the mirror of it in his sprite record, so the
; sprite tracks the move. The horizontal position gate then classifies that X: run off
; the far-right edge and it is nudged one pixel back left; at the far-left, or on the
; in-band default, one pixel right; on a blocked verdict it stays exactly where the
; velocity put it. The nudge lands on marioX ONLY -- the sprite-record mirror keeps the
; pre-nudge value.
moveMarioX:
2B02: 80              ADD     A,B                 ; new X = drift step + prior X
2B03: 32 03 62        LD      ($6203),A           ; {hard.workRam+203} move Mario
2B06: 32 4C 69        LD      ($694C),A           ; {hard.workRam+94C} and the sprite record that draws him
2B09: CD 1F 24        CALL    $241F               ; {code.limitMarioHorizontalTravel} test the new X against the edges
2B0C: 21 03 62        LD      HL,$6203            
2B0F: 1D              DEC     E                   
2B10: CA 18 2B        JP      Z,$2B18             ; {code.loc_2b18} off the far right: nudge one pixel back
2B13: 15              DEC     D                   
2B14: CA 1A 2B        JP      Z,$2B1A             ; {code.loc_2b1a} at the left, or in band: nudge one right
2B17: C9              RET                         ; blocked: leave him where the step put him

loc_2b18:
2B18: 35              DEC     (HL)                ; pull him back left (the sprite keeps the old X)
2B19: C9              RET                         

loc_2b1a:
2B1A: 34              INC     (HL)                ; push him right
2B1B: C9              RET                         

loc_2b1c:
2B1C: DD 21 00 62     LD      IX,$6200            ; the probe works off Mario's own record
2B20: CD 29 2B        CALL    $2B29               ; {code.probeMarioDescentLanding} run the descent probe
2B23: CD AF 29        CALL    $29AF               ; {code.loc_29af} then the board-gated object-collision check
2B26: AF              XOR     A                   
2B27: 47              LD      B,A                 ; hand the airborne handler a zeroed result
2B28: C9              RET                         

; The board split at the head of the player-versus-tilemap descent probe. On any board
; but 25m this routine does nothing itself: the whole probe belongs to the two-point form
; and its result is passed straight back. On 25m it probes a single point, (marioX,
; marioY + 7), through the tile classifier, with three outcomes. LANDED -- the classifier
; has already snapped marioY and unwound the collision walk, so this just propagates it.
; NO SURFACE -- nothing landable under the probe point, so abort carrying a zeroed
; result. SURFACE BUT STILL CLEAR OF IT -- measure how far the point sits past the
; boundary the classifier computed; four or more pixels is too far, but under four snap
; marioY to seven above the boundary and report landed. So the 25m arm lands Mario from
; up to three pixels short of the boundary the classifier itself waits for.
probeMarioDescentLanding:
2B29: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} 25m takes the single-point probe below
2B2C: 3D              DEC     A                   
2B2D: C2 53 2B        JP      NZ,$2B53            ; {code.loc_2b53} every other board uses the two-point form
2B30: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} probe point: straight under Mario
2B33: 67              LD      H,A                 
2B34: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} seven pixels below his feet
2B37: C6 07           ADD     A,$07               
2B39: 6F              LD      L,A                 
2B3A: CD 9B 2B        CALL    $2B9B               ; {code.probeTileForLanding} classify the tile there

loc_2b3d:
2B3D: A7              AND     A                   
2B3E: CA 51 2B        JP      Z,$2B51             ; {code.loc_2b51} nothing landable: abandon the walk
2B41: 7B              LD      A,E                 
2B42: 91              SUB     C                   ; how far the probe sits past the surface
2B43: FE 04           CP      $04                 ; four pixels or more is too far to land
2B45: D2 74 2B        JP      NC,$2B74            ; {code.loc_2b74}
2B48: 79              LD      A,C                 
2B49: D6 07           SUB     $07                 ; stand him seven above the surface
2B4B: 32 05 62        LD      ($6205),A           ; {hard.workRam+205} land Mario
2B4E: 3E 01           LD      A,$01               
2B50: 47              LD      B,A                 ; report the landing

loc_2b51:
2B51: E1              POP     HL                  ; drop a return level: the walk is over
2B52: C9              RET                         

loc_2b53:
2B53: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} first probe: 3 pixels back along his X
2B56: D6 03           SUB     $03                 
2B58: 67              LD      H,A                 
2B59: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} and seven below his feet
2B5C: C6 07           ADD     A,$07               
2B5E: 6F              LD      L,A                 
2B5F: CD 9B 2B        CALL    $2B9B               ; {code.probeTileForLanding} classify the tile there
2B62: FE 02           CP      $02                 ; surface found but not reached: snap his column
2B64: CA 7A 2B        JP      Z,$2B7A             ; {code.loc_2b7a}
2B67: 7A              LD      A,D                 ; second probe, seven further along X
2B68: C6 07           ADD     A,$07               
2B6A: 67              LD      H,A                 
2B6B: 6B              LD      L,E                 
2B6C: CD 9B 2B        CALL    $2B9B               ; {code.probeTileForLanding} classify that point too
2B6F: A7              AND     A                   
2B70: C8              RET     Z                   ; nothing under either: he keeps falling
2B71: C3 7A 2B        JP      $2B7A               ; {code.loc_2b7a}

loc_2b74:
2B74: 3E 00           LD      A,$00               ; no result this pass
2B76: 06 00           LD      B,$00               
2B78: E1              POP     HL                  ; drop a return level and abandon the walk
2B79: C9              RET                         

loc_2b7a:
2B7A: 3A 10 62        LD      A,($6210)           ; {hard.workRam+210} route selector: airborne horizontal speed
2B7D: A7              AND     A                   
2B7E: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} the X both routes snap
2B81: CA 8B 2B        JP      Z,$2B8B             ; {code.loc_2b8b} no speed: the sibling snap arm
2B84: F6 07           OR      $07                 ; reach the right edge of his 8-pixel cell
2B86: D6 04           SUB     $04                 ; and step back to its middle
2B88: C3 91 2B        JP      $2B91               ; {code.loc_2b91}

loc_2b8b:
2B8B: D6 08           SUB     $08                 ; the other route to the same snapped X
2B8D: F6 07           OR      $07                 
2B8F: C6 04           ADD     A,$04               

loc_2b91:
2B91: 32 03 62        LD      ($6203),A           ; {hard.workRam+203} put Mario on the snapped column
2B94: 32 4C 69        LD      ($694C),A           ; {hard.workRam+94C} so the sprite jumps there this frame
2B97: 3E 01           LD      A,$01               ; report the accept
2B99: E1              POP     HL                  ; drop a return level: the walk is over
2B9A: C9              RET                         

; The tile gate at the head of the airborne-descent collision probe. Given a pixel
; coordinate (y in the high byte, x in the low) it looks up the tile under that pixel
; and decides whether the pixel sits on a landable surface. It REJECTS a tile below
; 0xB0, a low nibble of 8 or more (the right half of the tile pair), and the tile 0xC0
; exactly. A tile below 0xC0 is a HIT on the "silent" boundary, x's 8-pixel column minus
; one. Above 0xC0 the tile band picks a column offset from its low nibble -- bands
; 0xC1..0xCF and 0xE0..0xEF subtract 9, bands 0xD0..0xDF and 0xF0..0xFF subtract 1 --
; and the boundary is x's column plus that offset, a HIT only when it lands strictly
; left of x. On a hit it hands off to the descent resolver, which measures the fall
; against that boundary and either keeps Mario airborne or snaps him onto the surface.
; The result code is 0 reject / 1 landed / 2 airborne, and a landing aborts the whole
; multi-probe collision walk.
probeTileForLanding:
2B9B: E5              PUSH    HL                  ; keep the pixel; its column is the reference
2B9C: CD F0 2F        CALL    $2FF0               ; {code.tileAddrForPixel} the tilemap cell under the probe pixel
2B9F: D1              POP     DE                  
2BA0: 7E              LD      A,(HL)              ; the tile there
2BA1: FE B0           CP      $B0                 ; below the surface band: reject
2BA3: DA D9 2B        JP      C,$2BD9             ; {code.loc_2bd9}
2BA6: E6 0F           AND     $0F                 
2BA8: FE 08           CP      $08                 ; the tile pair's far half is no surface
2BAA: D2 D9 2B        JP      NC,$2BD9            ; {code.loc_2bd9}
2BAD: 7E              LD      A,(HL)              ; re-read the tile unmasked
2BAE: FE C0           CP      $C0                 ; the plain 0xC0 tile is excluded
2BB0: CA D9 2B        JP      Z,$2BD9             ; {code.loc_2bd9}
2BB3: DA DC 2B        JP      C,$2BDC             ; {code.loc_2bdc} 0xB0-0xBF: the silent boundary
2BB6: FE D0           CP      $D0                 
2BB8: DA CB 2B        JP      C,$2BCB             ; {code.loc_2bcb} 0xC1-0xCF: offset is the nibble less 9
2BBB: FE E0           CP      $E0                 
2BBD: DA C5 2B        JP      C,$2BC5             ; {code.loc_2bc5} 0xD0-0xDF: offset is the nibble less 1
2BC0: FE F0           CP      $F0                 
2BC2: DA CB 2B        JP      C,$2BCB             ; {code.loc_2bcb} 0xE0-0xEF: the nibble less 9 again

loc_2bc5:
2BC5: E6 0F           AND     $0F                 
2BC7: 3D              DEC     A                   ; the nibble less 1 -- this band's offset
2BC8: C3 CF 2B        JP      $2BCF               ; {code.loc_2bcf}

loc_2bcb:
2BCB: E6 0F           AND     $0F                 
2BCD: D6 09           SUB     $09                 ; the nibble less 9 -- this band's offset

loc_2bcf:
2BCF: 4F              LD      C,A                 
2BD0: 7B              LD      A,E                 ; the probe's own column
2BD1: E6 F8           AND     $F8                 ; rounded down to its 8-pixel column
2BD3: 81              ADD     A,C                 ; plus the band offset: the surface boundary
2BD4: 4F              LD      C,A                 ; the resolver reads the boundary from here
2BD5: BB              CP      E                   ; a hit only if it lands left of the probe
2BD6: DA E1 2B        JP      C,$2BE1             ; {code.resolveAirborneTileLanding}

loc_2bd9:
2BD9: AF              XOR     A                   ; reject: nothing landable here
2BDA: 47              LD      B,A                 
2BDB: C9              RET                         

loc_2bdc:
2BDC: 7B              LD      A,E                 ; the silent boundary, one left of the column
2BDD: E6 F8           AND     $F8                 
2BDF: 3D              DEC     A                   
2BE0: 4F              LD      C,A                 

; Resolve whether Mario's airborne descent has reached a tile surface. Entered once the
; tile classifier has built the tile column's surface boundary, it measures how far he
; has descended as
;   probe = marioAirPrevY - (the object record's Y at +5) + the classifier's row offset
; against that boundary. Probe ABOVE the boundary means he is still clear of this tile:
; report code 2, "still airborne, keep probing", and return so the collision walk
; continues. Probe at or below it means he has reached the surface: snap marioY to the
; boundary less 7, report code 1, and unwind two levels -- the landing aborts the whole
; multi-probe walk, not just this classifier call.
resolveAirborneTileLanding:
2BE1: 3A 0C 62        LD      A,($620C)           ; {hard.workRam+20C} where he was before this frame's motion
2BE4: DD 96 05        SUB     (IX+$05)            ; measured against the record's current Y
2BE7: 83              ADD     A,E                 ; and the probe's own row
2BE8: B9              CP      C                   ; against the surface boundary
2BE9: CA EF 2B        JP      Z,$2BEF             ; {code.loc_2bef} exactly on it: he has landed
2BEC: D2 F8 2B        JP      NC,$2BF8            ; {code.loc_2bf8} still clear of the tile: keep falling

loc_2bef:
2BEF: 79              LD      A,C                 
2BF0: D6 07           SUB     $07                 ; stand him seven above the surface
2BF2: 32 05 62        LD      ($6205),A           ; {hard.workRam+205} land Mario on this tile
2BF5: C3 FD 2B        JP      $2BFD               ; {code.loc_2bfd}

loc_2bf8:
2BF8: 3E 02           LD      A,$02               ; report still airborne so the walk goes on
2BFA: 06 00           LD      B,$00               
2BFC: C9              RET                         

loc_2bfd:
2BFD: 3E 01           LD      A,$01               ; report the landing
2BFF: 47              LD      B,A                 
2C00: E1              POP     HL                  ; drop two return levels: the walk is over
2C01: E1              POP     HL                  
2C02: C9              RET                         

; The 25m release scheduler: decide, this pass, whether to dispatch into the slot-claim
; cluster that sends a barrel out, and by which route. Three gates first -- only on 25m,
; only while Mario is alive, and only while bit 0 of the cluster's event-gate scratch is
; clear -- and a live bonus of zero ends the pass. Then, with the bonus in hand: if
; bonusStart minus 2 has fallen below the live bonus, hand straight to the stepped-value
; entry; else if bit 1 of barrelClaimMode is set, hand to the clear-then-mode-3 entry;
; else run a periodic phase test, matching the low five bits of frame against a countdown
; of length difficulty, so the throw rate rises with difficulty. On a match, dispatch the
; cluster head if half of bonusStart has fallen below the live bonus, and otherwise fire
; only on odd spinCount frames. So the throws are paced against the bonus, not against a
; clock.
scheduleBarrelRelease:
2C03: 3E 01           LD      A,$01               ; board mask: 25m only
2C05: F7              RST     $30                 ; skip the routine on the other boards
2C06: D7              RST     $10                 ; and while Mario is dead
2C07: 3A 93 63        LD      A,($6393)           ; {hard.workRam+393} the cluster's in-progress latch
2C0A: 0F              RRCA                        
2C0B: D8              RET     C                   ; one already went out this pass
2C0C: 3A B1 62        LD      A,($62B1)           ; {hard.workRam+2B1} the live bonus is what paces the throws
2C0F: A7              AND     A                   
2C10: C8              RET     Z                   ; no bonus left: nothing to schedule
2C11: 4F              LD      C,A                 
2C12: 3A B0 62        LD      A,($62B0)           ; {hard.workRam+2B0} the board's starting bonus
2C15: D6 02           SUB     $02                 ; one notch short of it
2C17: B9              CP      C                   
2C18: DA 7B 2C        JP      C,$2C7B             ; {code.loc_2c7b} the first throws take the stepped-value route
2C1B: 3A 82 63        LD      A,($6382)           ; {hard.workRam+382} the slot-claim mode byte
2C1E: CB 4F           BIT     1,A                 
2C20: C2 86 2C        JP      NZ,$2C86            ; {code.loc_2c86} bit 1 set: the clear-then-mode-3 entry
2C23: 3A 80 63        LD      A,($6380)           ; {hard.workRam+380} the countdown's length is the difficulty
2C26: 47              LD      B,A                 
2C27: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} phase test on the frame counter
2C2A: E6 1F           AND     $1F                 

loc_2c2c:
2C2C: B8              CP      B                   ; match the phase against the countdown
2C2D: CA 33 2C        JP      Z,$2C33             ; {code.loc_2c33}
2C30: 10 FA           DJNZ    $2C2C               ; {code.loc_2c2c} harder boards match more phases, so throw faster
2C32: C9              RET                         ; no match this frame

loc_2c33:
2C33: 3A B0 62        LD      A,($62B0)           ; {hard.workRam+2B0} half the starting bonus
2C36: CB 3F           SRL     A                   
2C38: B9              CP      C                   
2C39: DA 41 2C        JP      C,$2C41             ; {code.loc_2c41} past halfway: fire on every matching frame
2C3C: 3A 19 60        LD      A,($6019)           ; {hard.workRam+19} earlier, fire only on odd spin-counter frames
2C3F: 0F              RRCA                        
2C40: D0              RET     NC                  

loc_2c41:
2C41: CD 57 00        CALL    $0057               ; {code.stirRandomSeed} a 1-in-16 coin flip picks the claim mode
2C44: E6 0F           AND     $0F                 
2C46: C2 86 2C        JP      NZ,$2C86            ; {code.loc_2c86} 15 of 16: the mode-3 entry

loc_2c49:
2C49: 3E 01           LD      A,$01               ; 1 of 16: mode 1

loc_2c4b:
2C4B: 32 82 63        LD      ($6382),A           ; {hard.workRam+382} record the claim mode
2C4E: 3C              INC     A                   ; the scratch copy sits one above it

; One entry of the bonus-event slot-claim cluster: stash the caller's mode byte and a 1
; into a companion flag, then, once the bonus counter has reached its scheduled mark,
; step the mark and claim a free object slot. Unlike the cluster's other entries this one
; does NOT stamp the paired barrel-claim mode byte up front -- that byte is touched only
; later, and only if a slot is claimed. The periodic gate proceeds only when the
; next-event mark equals the bonus value passed in; otherwise it returns having done just
; the two scratch writes. On a hit it schedules the next fire by stepping the mark down
; by 8, then scans the five records of objArray64 for the first whose active byte is zero
; and, on finding one, raises the barrel-kind bit in barrelClaimMode. If all five are
; occupied it does nothing further.
armBarrelRelease:
2C4F: 32 8F 63        LD      ($638F),A           ; {hard.workRam+38F} stash the mode byte in engine scratch
2C52: 3E 01           LD      A,$01               
2C54: 32 92 63        LD      ($6392),A           ; {hard.workRam+392} raise the release-armed flag
2C57: 3A B2 62        LD      A,($62B2)           ; {hard.workRam+2B2} the bonus value this event is scheduled at
2C5A: B9              CP      C                   
2C5B: C0              RET     NZ                  ; not yet: only the two scratch writes happen
2C5C: D6 08           SUB     $08                 ; schedule the next event eight notches down
2C5E: 32 B2 62        LD      ($62B2),A           ; {hard.workRam+2B2}
2C61: 11 20 00        LD      DE,$0020            
2C64: 21 00 64        LD      HL,$6400            ; look for a free record in the object array
2C67: 06 05           LD      B,$05               ; five of them

loc_2c69:
2C69: 7E              LD      A,(HL)              
2C6A: A7              AND     A                   
2C6B: CA 72 2C        JP      Z,$2C72             ; {code.markNextBarrelAsAltKind} one free: tag the next barrel
2C6E: 19              ADD     HL,DE               
2C6F: 10 F8           DJNZ    $2C69               ; {code.loc_2c69}
2C71: C9              RET                         ; all five in use: no tag

; Raise bit 7 of barrelClaimMode, leaving the low bits alone -- a mode-1 claim reads
; back as 0x81 afterwards. Bit 7 selects the barrel's KIND: the barrel released after
; this fires is stamped with a different sprite code, a different attribute and so a
; different palette, and a different family index, and that index is read again on
; several later paths, so the choice reaches behaviour and not only the picture. Both
; kinds can be on the board at the same time. It is NOT what makes a barrel drop
; straight down instead of rolling along the girders -- that is BIT 0 of the same byte,
; independent of bit 7 and left exactly as found here. Which named object either kind is
; has not been established.
markNextBarrelAsAltKind:
2C72: 3A 82 63        LD      A,($6382)           ; {hard.workRam+382} the slot-claim mode byte
2C75: F6 80           OR      $80                 ; bit 7 selects the alternate barrel kind
2C77: 32 82 63        LD      ($6382),A           ; {hard.workRam+382} the mode value in the low bits survives
2C7A: C9              RET                         

loc_2c7b:
2C7B: C6 02           ADD     A,$02               ; step the caller's value back up
2C7D: B9              CP      C                   
2C7E: CA 49 2C        JP      Z,$2C49             ; {code.loc_2c49} on the mark: claim with mode 1
2C81: 3E 02           LD      A,$02               ; otherwise mode 2
2C83: C3 4B 2C        JP      $2C4B               ; {code.loc_2c4b}

loc_2c86:
2C86: AF              XOR     A                   
2C87: 32 82 63        LD      ($6382),A           ; {hard.workRam+382} wipe it, so nothing stale carries over
2C8A: 3E 03           LD      A,$03               ; ask for the release with mode 3
2C8C: C3 4F 2C        JP      $2C4F               ; {code.armBarrelRelease}

; The release half of the 25m barrel engine: while a barrel is already on its way out,
; step the release animation; otherwise, if a release is armed, find a free barrel
; record and hand the claim on. Four gates decide, and three of them simply end the
; frame's work here -- a board mask that admits the girder board only; Mario must be
; alive; an in-progress latch set means a barrel already went out this pass, so control
; goes straight to the release animation and NOTHING is scanned; and an armed latch
; clear means there is nothing to place. With all four open it walks the ten objArray67
; records and stops at the first whose active byte has BOTH low bits clear -- neither
; already in motion nor already claimed -- handing that record and the countdown to the
; claim. The walk COUNTS DOWN because the loop variable is not a cursor but the
; argument: the claim derives the record's slot index from what is LEFT.
driveBarrelRelease:
2C8F: 3E 01           LD      A,$01               ; board mask: the girder board only
2C91: F7              RST     $30                 
2C92: D7              RST     $10                 ; and only while Mario is alive
2C93: 3A 93 63        LD      A,($6393)           ; {hard.workRam+393} is a barrel already on its way out?
2C96: 0F              RRCA                        
2C97: DA 15 2D        JP      C,$2D15             ; {code.loc_2d15} then only step its release animation
2C9A: 3A 92 63        LD      A,($6392)           ; {hard.workRam+392} is a release armed?
2C9D: 0F              RRCA                        
2C9E: D0              RET     NC                  ; nothing armed: nothing to place
2C9F: DD 21 00 67     LD      IX,$6700            ; the ten barrel records
2CA3: 11 20 00        LD      DE,$0020            
2CA6: 06 0A           LD      B,$0A               ; the count doubles as the slot index

loc_2ca8:
2CA8: DD 7E 00        LD      A,(IX+$00)          ; this record's state byte
2CAB: 0F              RRCA                        
2CAC: DA B3 2C        JP      C,$2CB3             ; {code.loc_2cb3} bit 0: already rolling
2CAF: 0F              RRCA                        
2CB0: D2 B8 2C        JP      NC,$2CB8            ; {code.releaseBarrelIntoFreeSlot} free: take this record

loc_2cb3:
2CB3: DD 19           ADD     IX,DE               
2CB5: 10 F1           DJNZ    $2CA8               ; {code.loc_2ca8}
2CB7: C9              RET                         ; all ten in use

; Claim the free barrel slot the scan above stopped on and send a barrel out. The scan
; walks the ten records counting down and jumps here the moment it finds one whose low
; two flag bits are both clear. This publishes that record as renderObjPtr; stamps its
; active field with 2, meaning "occupied", which is what stops the next pass re-claiming
; it and which the movement code later replaces with 1, "active", when the barrel starts
; moving; works out the slot index -- the scan counts ten down to one across records
; 0..9, so ten minus the count is the index -- and stores the matching slot of
; actorSprites into renderDstPtr, so barrel record k renders into sprite slot k. It sets
; bit 0 of the cluster's event gate, a one-shot latch the renderer's terminator clears
; again. Finally it charges the release: post the deferred task that takes one notch off
; the on-screen readout, then decrement bonus itself. ON 25m THIS ROUTINE IS THE BONUS
; CLOCK -- the other boards run the counter down on a timer, but on the girder board the
; bonus falls per barrel released. A decrement that reaches zero raises bonusExpiredStep.
releaseBarrelIntoFreeSlot:
2CB8: DD 22 AA 62     LD      ($62AA),IX          ; {hard.workRam+2AA} publish the claimed record
2CBC: DD 36 00 02     LD      (IX+$00),$02        ; mark it occupied so the next scan skips it
2CC0: 16 00           LD      D,$00               
2CC2: 3E 0A           LD      A,$0A               ; ten minus the count is the record's index
2CC4: 90              SUB     B                   
2CC5: 87              ADD     A,A                 
2CC6: 87              ADD     A,A                 ; times the 4-byte sprite-record stride
2CC7: 5F              LD      E,A                 
2CC8: 21 80 69        LD      HL,$6980            ; the sprite group the barrels draw into
2CCB: 19              ADD     HL,DE               
2CCC: 22 AC 62        LD      ($62AC),HL          ; {hard.workRam+2AC} barrel k renders into sprite slot k
2CCF: 3E 01           LD      A,$01               
2CD1: 32 93 63        LD      ($6393),A           ; {hard.workRam+393} latch: a barrel went out this pass
2CD4: 11 01 05        LD      DE,$0501            ; task: take one notch off the bonus readout
2CD7: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
2CDA: 21 B1 62        LD      HL,$62B1            
2CDD: 35              DEC     (HL)                ; charge the release -- on 25m the bonus falls per barrel
2CDE: C2 E6 2C        JP      NZ,$2CE6            ; {code.loc_2ce6}
2CE1: 3E 01           LD      A,$01               
2CE3: 32 86 63        LD      ($6386),A           ; {hard.workRam+386} bonus exhausted: start the expiry sequence

loc_2ce6:
2CE6: 7E              LD      A,(HL)              ; the bonus after the charge
2CE7: FE 04           CP      $04                 ; below four, retire one decoration sprite a notch
2CE9: D2 F6 2C        JP      NC,$2CF6            ; {code.stampReleasedBarrelKind}
2CEC: 21 A8 69        LD      HL,$69A8            ; the four-record sprite group
2CEF: 87              ADD     A,A                 
2CF0: 87              ADD     A,A                 
2CF1: 5F              LD      E,A                 
2CF2: 16 00           LD      D,$00               
2CF4: 19              ADD     HL,DE               
2CF5: 72              LD      (HL),D              ; zeroing a record's X takes it off the display

; Preset a freshly-claimed barrel record's appearance, then fall into the frame-gated
; renderer tick. With the record base in IX it stamps three of the record's fields with
; one of two presets, chosen by bit 7 of barrelClaimMode. Bit 7 clear gives sprite code
; 0x15, attribute 0x0B, mode 0x00 -- the ROLLING kind, whose code stays in the 0x15 /
; 0x16 / 0x17 family while X sweeps along the girders and Y creeps down. Bit 7 set gives
; 0x19, 0x0C, 0x01 -- the DROPPING kind, whose code walks 0x19, 0x1A, 0x1B while it
; descends with its X PINNED, a straight vertical fall down one column. The differing
; attribute selects a different palette, so the two are visually distinct, and both kinds
; can be active at once. Which named Donkey Kong object either kind is has not been
; established.
stampReleasedBarrelKind:
2CF6: DD 36 07 15     LD      (IX+$07),$15        ; the rolling barrel's sprite code
2CFA: DD 36 08 0B     LD      (IX+$08),$0B        ; and its palette
2CFE: DD 36 15 00     LD      (IX+$15),$00        ; kind 0: rolls along the girders
2D02: 3A 82 63        LD      A,($6382)           ; {hard.workRam+382} bit 7 selects the barrel kind
2D05: 07              RLCA                        
2D06: D2 15 2D        JP      NC,$2D15            ; {code.loc_2d15} clear: keep the rolling preset
2D09: DD 36 07 19     LD      (IX+$07),$19        ; the dropping barrel's sprite code
2D0D: DD 36 08 0C     LD      (IX+$08),$0C        ; a different palette, so the two look apart
2D11: DD 36 15 01     LD      (IX+$15),$01        ; kind 1: descends with its X pinned

; The frame-gated step of a sprite waypoint walker. A down-counter is decremented on
; every entry and the routine returns until it underflows, so the body acts only once
; every 24 frames. On the acting frame it reloads that gate to 0x18 and reads an
; animation sub-counter: at zero it simply steps the object to the next waypoint and stops.
; Non-zero, it selects a 40-byte record from the animation table -- bit 0 of
; barrelClaimMode decides whether the record index is the sub-counter itself or one less
; -- and copies it into the sprite-object block. The sub-counter is then stepped down;
; while it stays non-zero the object steps to the next waypoint, and when it reaches zero the
; gate is shortened to a single frame and that same parity bit branches: set restarts
; the fixed table, clear steps to the next waypoint. Which barrel kind the
; record being dressed belongs to is not claimed; bit 0 is read only as a parity
; selector.
loc_2d15:
2D15: 21 AF 62        LD      HL,$62AF            
2D18: 35              DEC     (HL)                ; the frame gate -- the body acts once in 24
2D19: C0              RET     NZ                  
2D1A: 36 18           LD      (HL),$18            ; reload the gate for the next cycle
2D1C: 3A 8F 63        LD      A,($638F)           ; {hard.workRam+38F} the animation sub-counter
2D1F: A7              AND     A                   
2D20: CA 51 2D        JP      Z,$2D51             ; {code.loc_2d51} zero: just take the next waypoint
2D23: 4F              LD      C,A                 
2D24: 21 32 39        LD      HL,$3932            ; the animation table, 40 bytes per record
2D27: 3A 82 63        LD      A,($6382)           ; {hard.workRam+382} bit 0 picks which record index
2D2A: 0F              RRCA                        
2D2B: DA 2F 2D        JP      C,$2D2F             ; {code.loc_2d2f}
2D2E: 0D              DEC     C                   ; clear: one record earlier

loc_2d2f:
2D2F: 79              LD      A,C                 
2D30: 87              ADD     A,A                 
2D31: 87              ADD     A,A                 
2D32: 87              ADD     A,A                 
2D33: 4F              LD      C,A                 
2D34: 87              ADD     A,A                 
2D35: 87              ADD     A,A                 
2D36: 81              ADD     A,C                 ; index times forty
2D37: 5F              LD      E,A                 
2D38: 16 00           LD      D,$00               
2D3A: 19              ADD     HL,DE               
2D3B: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock} copy it into the sprite-object block
2D3E: 21 8F 63        LD      HL,$638F            
2D41: 35              DEC     (HL)                ; step the sub-counter
2D42: C2 51 2D        JP      NZ,$2D51            ; {code.loc_2d51} still running: take the next waypoint
2D45: 3E 01           LD      A,$01               
2D47: 32 AF 62        LD      ($62AF),A           ; {hard.workRam+2AF} last record: act again on the next frame
2D4A: 3A 82 63        LD      A,($6382)           ; {hard.workRam+382} the same bit 0 picks the ending
2D4D: 0F              RRCA                        
2D4E: DA 83 2D        JP      C,$2D83             ; {code.loc_2d83} set: restart the one-waypoint table

loc_2d51:
2D51: 2A A8 62        LD      HL,($62A8)          ; {hard.workRam+2A8} reload the path cursor

; Move a barrel to its next waypoint on the release path and publish that pose as a
; hardware sprite record, or, at the end of the path, hand off to release completion.
; The table it walks is (x, y) waypoint PAIRS, not text, and nothing here touches video
; RAM. One call consumes one pair: sprite X takes the first byte with its top bit
; stripped; the sprite code is the barrel's own, with its low two bits flipped first if
; that top bit was SET -- and the flipped value is written BACK into the barrel record,
; so the animation step persists into the following waypoints rather than being a
; one-frame pose; the attribute is copied straight through; and sprite Y takes the
; second byte. The cursor then advances two bytes and is stored back. A first byte of
; 0x7F ends the path, which is why the same 0x7F doubles as the mask that strips the
; flag bit off every other X.
stepBarrelAlongReleasePath:
2D54: 7E              LD      A,(HL)              ; this waypoint's X byte, flag bit and all
2D55: DD 2A AA 62     LD      IX,($62AA)          ; {hard.workRam+2AA} the barrel being moved
2D59: ED 5B AC 62     LD      DE,($62AC)          ; {hard.workRam+2AC} the sprite slot it publishes into
2D5D: FE 7F           CP      $7F                 ; 0x7F ends the path
2D5F: CA 8C 2D        JP      Z,$2D8C             ; {code.activateReleasedBarrel}
2D62: 4F              LD      C,A                 ; keep the flag bit
2D63: E6 7F           AND     $7F                 ; strip it off to get the sprite X
2D65: 12              LD      (DE),A              
2D66: DD 7E 07        LD      A,(IX+$07)          ; the barrel's own sprite code
2D69: CB 79           BIT     7,C                 ; the waypoint asks for the next frame
2D6B: CA 70 2D        JP      Z,$2D70             ; {code.loc_2d70}
2D6E: EE 03           XOR     $03                 ; flip the two animation bits

loc_2d70:
2D70: 13              INC     DE                  
2D71: 12              LD      (DE),A              ; publish the sprite code
2D72: DD 77 07        LD      (IX+$07),A          ; and keep it, so the flip persists
2D75: DD 7E 08        LD      A,(IX+$08)          
2D78: 13              INC     DE                  
2D79: 12              LD      (DE),A              ; the barrel's palette, copied straight through
2D7A: 23              INC     HL                  
2D7B: 7E              LD      A,(HL)              ; the pair's second byte is the sprite Y
2D7C: 13              INC     DE                  
2D7D: 12              LD      (DE),A              
2D7E: 23              INC     HL                  
2D7F: 22 A8 62        LD      ($62A8),HL          ; {hard.workRam+2A8} advance the cursor past this waypoint
2D82: C9              RET                         

loc_2d83:
2D83: 21 CC 39        LD      HL,$39CC            ; the one-waypoint path
2D86: 22 A8 62        LD      ($62A8),HL          ; {hard.workRam+2A8} restart the walk at its head
2D89: C3 54 2D        JP      $2D54               ; {code.stepBarrelAlongReleasePath}

; The release renderer's 0x7F terminator: close out the barrel record it was building.
; The renderer above walks a byte string writing 4-byte sprite records until it meets the
; terminator, and that jump lands here. It rewinds renderStrPtr back to the string's
; start; stamps the record's control fields -- an enable/mode byte at +1 chosen from bit
; 0 of barrelClaimMode (set keeps mode 1, clear selects mode 0 and marks +2 with 2), a
; fixed 1 in the active field and at +0x0F, a zeroed sub-block at +0x10..+0x14, and two
; cleared scratch bytes; copies the destination sprite record's X and Y into the record's
; own X and Y; then reloads the whole ten-record sprite-object block from its stored
; template and adds -4 to every record's Y. Which barrel the two mode arms produce is not
; established here.
activateReleasedBarrel:
2D8C: 21 C3 39        LD      HL,$39C3            ; rewind to the head of the four-waypoint path
2D8F: 22 A8 62        LD      ($62A8),HL          ; {hard.workRam+2A8}
2D92: DD 36 01 01     LD      (IX+$01),$01        ; the record's select byte
2D96: 3A 82 63        LD      A,($6382)           ; {hard.workRam+382} bit 0 chose which path was walked
2D99: 0F              RRCA                        
2D9A: DA A5 2D        JP      C,$2DA5             ; {code.loc_2da5}
2D9D: DD 36 01 00     LD      (IX+$01),$00        ; clear: select 0
2DA1: DD 36 02 02     LD      (IX+$02),$02        ; and the mode bit that starts it rolling

loc_2da5:
2DA5: DD 36 00 01     LD      (IX+$00),$01        ; the barrel is running now, not just claimed
2DA9: DD 36 0F 01     LD      (IX+$0F),$01        
2DAD: AF              XOR     A                   
2DAE: DD 77 10        LD      (IX+$10),A          ; clear the record's motion sub-block
2DB1: DD 77 11        LD      (IX+$11),A          
2DB4: DD 77 12        LD      (IX+$12),A          
2DB7: DD 77 13        LD      (IX+$13),A          
2DBA: DD 77 14        LD      (IX+$14),A          
2DBD: 32 93 63        LD      ($6393),A           ; {hard.workRam+393} clear the went-out latch
2DC0: 32 92 63        LD      ($6392),A           ; {hard.workRam+392} and the armed latch
2DC3: 1A              LD      A,(DE)              ; the sprite's final X...
2DC4: DD 77 03        LD      (IX+$03),A          ; ...becomes the barrel's own X
2DC7: 13              INC     DE                  
2DC8: 13              INC     DE                  
2DC9: 13              INC     DE                  
2DCA: 1A              LD      A,(DE)              ; and its final Y...
2DCB: DD 77 05        LD      (IX+$05),A          ; ...likewise
2DCE: 21 5C 38        LD      HL,$385C            ; reload the sprite-object block from its template
2DD1: CD 4E 00        CALL    $004E               ; {code.loadSpriteObjectBlock}
2DD4: 21 0B 69        LD      HL,$690B            ; aim at the block's Y fields
2DD7: 0E FC           LD      C,$FC               ; and lift every record four pixels
2DD9: FF              RST     $38                 
2DDA: C9              RET                         

; On 50m and 100m, while Mario is alive, raise two one-shot spawn-request latches on a
; difficulty-scaled period. Two gates open it: a board test against the mask 0x0A, so 25m
; and 75m skip the routine entirely, and an alive test. The trigger is a low-bit mask on
; the frame counter that NARROWS as difficulty rises, so the requests come more often the
; harder the board. steps = (difficulty + 1) >> 1, plus one more on 50m, which is 1 to 4
; steps over the in-play range; the mask's run of set low bits folds down once per step,
; giving 0xFF, 0x7F, 0x3F, 0x1F; and the request fires on the frames where the frame
; counter lands zero under the mask, every 2^(9 - steps) frames. It only RAISES the
; latches -- never clears them, never checks whether the last one was serviced -- so an
; unconsumed request is simply re-asserted.
raisePeriodicObjectSpawnRequests:
2DDB: 3E 0A           LD      A,$0A               ; board mask: 50m and 100m
2DDD: F7              RST     $30                 
2DDE: D7              RST     $10                 ; and only while Mario is alive
2DDF: 3A 80 63        LD      A,($6380)           ; {hard.workRam+380} the period narrows as difficulty rises
2DE2: 3C              INC     A                   
2DE3: A7              AND     A                   ; clear carry so the halving shifts in a zero
2DE4: 1F              RRA                         ; steps = (difficulty + 1) / 2
2DE5: 47              LD      B,A                 
2DE6: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} 50m gets one extra step, so it fires twice as often
2DE9: FE 02           CP      $02                 
2DEB: 20 01           JR      NZ,$2DEE            ; {code.loc_2dee}
2DED: 04              INC     B                   

loc_2dee:
2DEE: 3E FE           LD      A,$FE               ; the trigger mask, seeded
2DF0: 37              SCF                         ; the first fold brings in a set bit, giving 0xFF

loc_2df1:
2DF1: 1F              RRA                         ; fold one more low bit away per step
2DF2: A7              AND     A                   ; and clear carry so later folds bring in zeros
2DF3: 10 FC           DJNZ    $2DF1               ; {code.loc_2df1}
2DF5: 47              LD      B,A                 
2DF6: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} fire on the frames that land zero under the mask
2DF9: A0              AND     B                   
2DFA: C0              RET     NZ                  
2DFB: 3E 01           LD      A,$01               
2DFD: 32 A0 63        LD      ($63A0),A           ; {hard.workRam+3A0} raise the insert request
2E00: 32 9A 63        LD      ($639A),A           ; {hard.workRam+39A} and the request that moves with it
2E03: C9              RET                         

; The actor-object scan loop. Two skip gates open it: the shared per-board gate with
; mask 0x04, which is the current board's bit only on board 3 (75m), so 25m, 50m and
; 100m skip the whole routine; and the shared alive gate, requiring Mario to be alive
; and being processed. With both open it seeds two scan cursors at objArray65 and
; actorSprites and calls the per-object updater ten times; that updater reads the
; current object and its paired sprite record through the cursors and, in its shared
; advance tail, steps the object cursor by 16 and the sprite cursor by 4, so ten calls
; sweep the whole array one object per pass. The board half is derivable right here --
; mask 0x04 is board 3 and nothing else. WHICH characters the ten records are is not
; identified.
update75mActorObjects:
2E04: 3E 04           LD      A,$04               ; board mask: 75m only
2E06: F7              RST     $30                 
2E07: D7              RST     $10                 ; and only while Mario is alive
2E08: DD 21 00 65     LD      IX,$6500            ; the ten spring records
2E0C: FD 21 80 69     LD      IY,$6980            ; and their paired sprite records
2E10: 06 0A           LD      B,$0A               ; one pass per record

; Advance ONE 75m spring by a frame, called once per slot by the ten-slot sweep with the
; spring's record and its paired sprite record already addressed. Four arms, in order:
; an INACTIVE slot goes to the spawn arm, which is what puts a new spring in it;
; otherwise, once every sixteen frames the low three bits of the paired sprite's tile
; code are flipped, a flicker on the drawn sprite only; state 4 goes to the retire arm;
; anything else is ordinary travel, inline here. THE TRAVEL ARM IS THE BOUNCE: X
; advances by a FIXED two pixels, so the horizontal crossing is constant and carries no
; shape at all, and everything the eye reads as a bounce comes from the vertical side,
; where the next byte of a signed delta string is ACCUMULATED into Y -- added, not
; stored. A walk pointer in the record picks that byte; its terminator sends control to
; the rewind handler, which is what makes the bounce a repeating cycle rather than a
; single arc.
advanceSpring:
2E12: DD 7E 00        LD      A,(IX+$00)          ; is this slot live?
2E15: 0F              RRCA                        
2E16: D2 A7 2E        JP      NC,$2EA7            ; {code.spawnObjectIntoInactiveSlot} no: the spawn arm fills it
2E19: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} once every sixteen frames...
2E1C: E6 0F           AND     $0F                 
2E1E: C2 29 2E        JP      NZ,$2E29            ; {code.loc_2e29}
2E21: FD 7E 01        LD      A,(IY+$01)          ; ...flicker the drawn sprite
2E24: EE 07           XOR     $07                 
2E26: FD 77 01        LD      (IY+$01),A          

loc_2e29:
2E29: DD 7E 0D        LD      A,(IX+$0D)          ; the spring's state
2E2C: FE 04           CP      $04                 ; state 4 is the retire arm
2E2E: CA 84 2E        JP      Z,$2E84             ; {code.loc_2e84}
2E31: DD 34 03        INC     (IX+$03)            ; travel: X advances a fixed two pixels a frame
2E34: DD 34 03        INC     (IX+$03)            
2E37: DD 6E 0E        LD      L,(IX+$0E)          ; the walk pointer into its height string
2E3A: DD 66 0F        LD      H,(IX+$0F)          
2E3D: 7E              LD      A,(HL)              ; the next signed height delta
2E3E: 4F              LD      C,A                 
2E3F: FE 7F           CP      $7F                 ; the terminator wraps the bounce
2E41: CA 9C 2E        JP      Z,$2E9C             ; {code.loc_2e9c}
2E44: 23              INC     HL                  
2E45: DD 86 05        ADD     A,(IX+$05)          ; the delta is ADDED to Y -- this is the bounce
2E48: DD 77 05        LD      (IX+$05),A          

; Carry one spring along its bounce arc, and drop it off the end of its travel. A
; convergence point inside the spring loop, reached once the loop has advanced this
; spring one step along its animation string -- either from the mid-string fall-through
; or from the arm that has just wrapped the string at its terminator. It first stores the
; current string pointer back into the record at +0x0E / +0x0F so the next pass resumes
; where this one left off: that is what continues the arc. Then a single end-of-travel
; test, taken only when BOTH halves hold -- the spring has reached the far X limit AND
; the last string byte read was the terminator. On that frame it is dropped: handed to
; the next state and given a transition sound, one latch cleared and another asserted for
; three frames. If either half is unmet the spring simply keeps going. Every path then
; mirrors the spring's position into its paired sprite record and advances both cursors.
advanceSpringArcAndDropAtTravelEnd:
2E4B: DD 75 0E        LD      (IX+$0E),L          ; store the walk pointer so the arc continues
2E4E: DD 74 0F        LD      (IX+$0F),H          
2E51: DD 7E 03        LD      A,(IX+$03)          ; has it crossed to the far side?
2E54: FE B7           CP      $B7                 
2E56: DA 6C 2E        JP      C,$2E6C             ; {code.mirrorObjectPositionToSprite}
2E59: 79              LD      A,C                 ; and did the height string just wrap?
2E5A: FE 7F           CP      $7F                 
2E5C: C2 6C 2E        JP      NZ,$2E6C            ; {code.mirrorObjectPositionToSprite}
2E5F: DD 36 0D 04     LD      (IX+$0D),$04        ; both: hand the spring to its retire state
2E63: AF              XOR     A                   
2E64: 32 83 60        LD      ($6083),A           ; {hard.workRam+83} silence the bounce sound line
2E67: 3E 03           LD      A,$03               
2E69: 32 84 60        LD      ($6084),A           ; {hard.workRam+84} and play the drop sound for three frames

; Copy the current object's X and Y into its paired sprite record -- so the hardware
; draws the object's sprite where the object currently IS -- then fall straight into the
; shared cursor advance, which steps both scan cursors on to the next object. A
; convergence tail of the per-object update loop, reached from two of that loop's state
; arms; the object record is addressed by the object-scan cursor and the sprite record by
; the paired sprite-scan cursor.
mirrorObjectPositionToSprite:
2E6C: DD 7E 03        LD      A,(IX+$03)          ; draw the object where it now is
2E6F: FD 77 00        LD      (IY+$00),A          
2E72: DD 7E 05        LD      A,(IX+$05)          
2E75: FD 77 03        LD      (IY+$03),A          

; The shared tail of the per-object update loop. However an object was processed --
; active, inactive, or in its rise/deactivate state -- every path converges here to move
; both scan cursors on by one record: the object-record cursor by its 16-byte stride and
; the paired sprite/animation cursor by its 4-byte stride. It writes NO memory. The
; cursors and the remaining-object count are handed back in registers, the same way the
; loop supplies them, and the 4 it leaves behind as the step amount is loop scratch
; nothing downstream reads.
advanceToNextObject:
2E78: 11 10 00        LD      DE,$0010            ; object records are 16 bytes apart
2E7B: DD 19           ADD     IX,DE               
2E7D: 1E 04           LD      E,$04               ; sprite records are 4
2E7F: FD 19           ADD     IY,DE               
2E81: 10 8F           DJNZ    $2E12               ; {code.advanceSpring} on to the next of the ten
2E83: C9              RET                         

loc_2e84:
2E84: 3E 03           LD      A,$03               ; the retire arm steps Y three a frame
2E86: DD 86 05        ADD     A,(IX+$05)          
2E89: DD 77 05        LD      (IX+$05),A          
2E8C: FE F8           CP      $F8                 ; off the bottom of its travel?
2E8E: DA 6C 2E        JP      C,$2E6C             ; {code.mirrorObjectPositionToSprite}
2E91: DD 36 03 00     LD      (IX+$03),$00        ; retire it: X zeroed, so it stops being drawn
2E95: DD 36 00 00     LD      (IX+$00),$00        ; and it stops being processed
2E99: C3 6C 2E        JP      $2E6C               ; {code.mirrorObjectPositionToSprite}

loc_2e9c:
2E9C: 21 AA 39        LD      HL,$39AA            ; rewind the walk to the string base
2E9F: 3E 03           LD      A,$03               
2EA1: 32 83 60        LD      ($6083),A           ; {hard.workRam+83} play the wrap sound for three frames
2EA4: C3 4B 2E        JP      $2E4B               ; {code.advanceSpringArcAndDropAtTravelEnd}

; The inactive-slot arm of the per-object update loop. It tests the one-shot spawn
; request, bit 0 of spawnRequest. With no spawn pending the slot stays inactive and the
; scan simply advances. With one pending it CONSUMES the request -- clearing it so no
; other inactive slot also spawns this pass -- and seeds the slot: a fixed initial Y, an
; initial X drawn from the freshly stirred random seed, its animation-string pointer
; aimed at the string base, and its state and active flags set. Either way it ends by
; advancing both scan cursors to the next object. Which object this spawns, and what it
; does in the game, are not established here.
spawnObjectIntoInactiveSlot:
2EA7: 3A 96 63        LD      A,($6396)           ; {hard.workRam+396} is a spawn pending?
2EAA: 0F              RRCA                        
2EAB: D2 78 2E        JP      NC,$2E78            ; {code.advanceToNextObject} no: leave the slot empty
2EAE: AF              XOR     A                   
2EAF: 32 96 63        LD      ($6396),A           ; {hard.workRam+396} consume it, so only one slot fills this pass
2EB2: DD 36 05 50     LD      (IX+$05),$50        ; fixed starting height
2EB6: DD 36 0D 01     LD      (IX+$0D),$01        ; its first state
2EBA: CD 57 00        CALL    $0057               ; {code.stirRandomSeed} the starting column is random
2EBD: E6 0F           AND     $0F                 
2EBF: C6 F8           ADD     A,$F8               ; spread over a 16-wide window around zero
2EC1: DD 77 03        LD      (IX+$03),A          
2EC4: DD 36 00 01     LD      (IX+$00),$01        ; bring the slot to life
2EC8: 21 AA 39        LD      HL,$39AA            ; aim its walk at the height-string base
2ECB: DD 75 0E        LD      (IX+$0E),L          
2ECE: DD 74 0F        LD      (IX+$0F),H          
2ED1: C3 78 2E        JP      $2E78               ; {code.advanceToNextObject}

; The per-frame hammer sprite and background-tune driver. Two skip gates first: the board
; gate, mask bits 0, 1 and 3 -- 25m, 50m and 100m, never 75m -- and the Mario-alive gate.
; It then picks which of the two hammer records to drive from bit 0 of the FIRST record's
; in-play field (set keeps object 1, clear picks object 2) and seeds that object's sprite
; displacement. If Mario is not holding a hammer it hands off to the pending-hammer build
; arm and stops. If he is, it clears the pending flag, switches the background tune to
; the hammer theme, stamps the object's collision half-extents, and builds the sprite
; from Mario's current pose -- the hammer tile faces the way he faces, and a swing code
; is derived from his pose. Bit 3 of hammerTimerLo selects between two swing poses, and
; the two poses stamp DIFFERENT half-extents, 0x06/0x03 and 0x05/0x06, which the board's
; hit check takes as its per-axis tolerances -- so the box the hammer smashes with
; changes shape frame to frame with the swing, and this is what changes it.
driveHammerSprite:
2ED4: 3E 0B           LD      A,$0B               ; board mask: 25m, 50m and 100m -- never 75m
2ED6: F7              RST     $30                 
2ED7: D7              RST     $10                 ; and only while Mario is alive
2ED8: 11 18 6A        LD      DE,$6A18            ; object 1's sprite slot
2EDB: DD 21 80 66     LD      IX,$6680            ; and its record
2EDF: DD 7E 01        LD      A,(IX+$01)          ; which of the two hammers is in play?
2EE2: 0F              RRCA                        
2EE3: DA ED 2E        JP      C,$2EED             ; {code.loc_2eed}
2EE6: 11 1C 6A        LD      DE,$6A1C            ; the other hammer's sprite slot
2EE9: DD 21 90 66     LD      IX,$6690            ; and its record

loc_2eed:
2EED: DD 36 0E 00     LD      (IX+$0E),$00        ; this frame's offset from Mario
2EF1: DD 36 0F F0     LD      (IX+$0F),$F0        
2EF5: 3A 17 62        LD      A,($6217)           ; {hard.workRam+217} is a hammer in his hands?
2EF8: 0F              RRCA                        
2EF9: D2 97 2F        JP      NC,$2F97            ; {code.buildPendingHammerSprite}
2EFC: AF              XOR     A                   
2EFD: 32 18 62        LD      ($6218),A           ; {hard.workRam+218} in hand now, so no longer merely pending
2F00: 21 89 60        LD      HL,$6089            
2F03: 36 04           LD      (HL),$04            ; switch the background tune to the hammer theme
2F05: DD 36 09 06     LD      (IX+$09),$06        ; the swing's hit box, half-width...
2F09: DD 36 0A 03     LD      (IX+$0A),$03        ; ...and half-height
2F0D: 06 1E           LD      B,$1E               ; the hammer tile
2F0F: 3A 07 62        LD      A,($6207)           ; {hard.workRam+207} the hammer faces the way Mario faces
2F12: CB 27           SLA     A                   
2F14: D2 1B 2F        JP      NC,$2F1B            ; {code.loc_2f1b}
2F17: F6 80           OR      $80                 ; restore his facing bit onto the swing code
2F19: CB F8           SET     7,B                 ; and onto the hammer tile

loc_2f1b:
2F1B: F6 08           OR      $08                 ; the fixed flag every swing code carries
2F1D: 4F              LD      C,A                 
2F1E: 3A 94 63        LD      A,($6394)           ; {hard.workRam+394} bit 3 alternates the two swing poses
2F21: CB 5F           BIT     3,A                 
2F23: CA 43 2F        JP      Z,$2F43             ; {code.updateActiveHammer}
2F26: CB C0           SET     0,B                 ; the alternate pose's tiles
2F28: CB C1           SET     0,C                 
2F2A: DD 36 09 05     LD      (IX+$09),$05        ; and its differently shaped hit box
2F2E: DD 36 0A 06     LD      (IX+$0A),$06        
2F32: DD 36 0F 00     LD      (IX+$0F),$00        ; this pose sits at a different offset
2F36: DD 36 0E F0     LD      (IX+$0E),$F0        
2F3A: CB 79           BIT     7,C                 ; on his facing bit, offset the other way
2F3C: CA 43 2F        JP      Z,$2F43             ; {code.updateActiveHammer}
2F3F: DD 36 0E 10     LD      (IX+$0E),$10        ; swing to his other side

; Advance a held hammer one tick and lay down this frame's hammer sprite; end the hammer
; when its lifetime runs out. It stamps the caller's hammer tile code into Mario's sprite
; record, sets the record's attribute to the shared value, then ticks the 16-bit hammer
; duration counter and routes on how far it has run. Low byte advanced without wrapping:
; hand off to the arm that lays the record down. Low byte wrapped, high byte non-zero but
; short of the expiry value: hand off to the arm that flashes the attribute first. High
; byte at the expiry value: END the hammer -- zero the counter's high byte, clear
; marioHammerActive, deactivate the object, park its sprite at the screen origin by
; setting its X displacement to minus marioX, and restore Mario's sprite code and the
; tune saved in hammerSavedBgm. The limit is 512 frames: the updater runs once per frame.
updateActiveHammer:
2F43: 79              LD      A,C                 
2F44: 32 4D 69        LD      ($694D),A           ; {hard.workRam+94D} stamp the swing tile into Mario's sprite record
2F47: 0E 07           LD      C,$07               ; the attribute the record write stores
2F49: 21 94 63        LD      HL,$6394            
2F4C: 34              INC     (HL)                ; tick the hammer's duration counter
2F4D: C2 B7 2F        JP      NZ,$2FB7            ; {code.selectHammerSpriteBlinkByTimer}
2F50: 21 95 63        LD      HL,$6395            
2F53: 34              INC     (HL)                ; the low byte wrapped: carry into the high
2F54: 7E              LD      A,(HL)              
2F55: FE 02           CP      $02                 ; 512 counts is the hammer's whole life
2F57: C2 BE 2F        JP      NZ,$2FBE            ; {code.blinkHammerSpriteOnFramePhase} not yet: flash and carry on
2F5A: AF              XOR     A                   
2F5B: 32 95 63        LD      ($6395),A           ; {hard.workRam+395} the hammer's time is up
2F5E: 32 17 62        LD      ($6217),A           ; {hard.workRam+217} it leaves his hands
2F61: DD 77 01        LD      (IX+$01),A          
2F64: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203}
2F67: ED 44           NEG                         ; minus Mario's X...
2F69: DD 77 0E        LD      (IX+$0E),A          ; ...parks the hammer sprite at the origin
2F6C: 3A 07 62        LD      A,($6207)           ; {hard.workRam+207} give Mario his ordinary pose back
2F6F: 32 4D 69        LD      ($694D),A           ; {hard.workRam+94D}
2F72: DD 36 00 00     LD      (IX+$00),$00        ; and deactivate the hammer object
2F76: 3A 89 63        LD      A,($6389)           ; {hard.workRam+389} restore the tune the hammer interrupted
2F79: 32 89 60        LD      ($6089),A           ; {hard.workRam+89}

; The convergence point of the hammer/object sprite updater: write the finished sprite
; record, positioned at a fixed offset from Mario, and mirror that position back into
; the object record. X is Mario's X plus the object's X-displacement field, stored into
; the sprite record's X byte and mirrored into the object record's own X field, so the
; sprite tracks Mario at a constant horizontal offset; then the caller's tile code and
; attribute bytes; then Y is Mario's Y plus the object's Y-displacement field, likewise
; stored and mirrored. Nothing about it is hammer-specific -- the hammer arms merely
; happen to be its current callers. A leaf.
commitSpriteRecordAtMarioOffset:
2F7C: EB              EX      DE,HL               
2F7D: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} the sprite sits at a fixed offset from Mario
2F80: DD 86 0E        ADD     A,(IX+$0E)          
2F83: 77              LD      (HL),A              
2F84: DD 77 03        LD      (IX+$03),A          ; mirror the position into the object record
2F87: 23              INC     HL                  
2F88: 70              LD      (HL),B              ; the caller's tile code
2F89: 23              INC     HL                  
2F8A: 71              LD      (HL),C              ; and its attribute
2F8B: 23              INC     HL                  
2F8C: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} the other axis, likewise offset
2F8F: DD 86 0F        ADD     A,(IX+$0F)          
2F92: 77              LD      (HL),A              
2F93: DD 77 05        LD      (IX+$05),A          ; mirrored back too
2F96: C9              RET                         

; Put an un-taken hammer on screen. It gates on bit 0 of marioHammerPending: clear, and
; it does nothing at all. Set, and it prepares the object record the caller points at,
; then falls into the shared record write. The object's collision half-extents on X and
; Y are set to fixed values, which is the box Mario has to walk into to pick it up; its
; sprite is a fixed base tile carrying MARIO's current horizontal-facing bit plus a
; fixed attribute, so the waiting hammer is drawn facing the same way he is; and the
; current background tune is copied into hammerSavedBgm, so whatever swaps in the hammer
; theme can put the old one back afterwards. The shared write then lays the 4-byte
; sprite record down at Mario's position plus the object's displacement and mirrors that
; position back into the object record.
buildPendingHammerSprite:
2F97: 3A 18 62        LD      A,($6218)           ; {hard.workRam+218} is a hammer waiting to be picked up?
2F9A: 0F              RRCA                        
2F9B: D0              RET     NC                  ; no: draw nothing
2F9C: DD 36 09 06     LD      (IX+$09),$06        ; the pickup box Mario must walk into...
2FA0: DD 36 0A 03     LD      (IX+$0A),$03        ; ...half-width and half-height
2FA4: 3A 07 62        LD      A,($6207)           ; {hard.workRam+207} take Mario's facing bit
2FA7: 07              RLCA                        
2FA8: 3E 3C           LD      A,$3C               
2FAA: 1F              RRA                         ; so the waiting hammer faces the way he does
2FAB: 47              LD      B,A                 
2FAC: 0E 07           LD      C,$07               ; its attribute
2FAE: 3A 89 60        LD      A,($6089)           ; {hard.workRam+89} remember the current tune...
2FB1: 32 89 63        LD      ($6389),A           ; {hard.workRam+389} ...so it can come back when the hammer ends
2FB4: C3 7C 2F        JP      $2F7C               ; {code.commitSpriteRecordAtMarioOffset}

; Pick which sprite-build path lays down this frame's hammer record, from how far the
; hammer's duration counter has run. It reads the counter's high byte and splits: zero,
; still inside the first 256 counts, commits the record directly with the caller's
; attribute unchanged, no blink; non-zero routes through the blink arm, which flashes the
; sprite's colour attribute on the frame counter's blink phase before committing the same
; record. The high byte sets at the halfway point of the hammer's roughly 512-count life.
; Either path lays down the same 4-byte record -- this arm only selects whether the
; attribute blinks, and the record's inputs pass through untouched.
selectHammerSpriteBlinkByTimer:
2FB7: 3A 95 63        LD      A,($6395)           ; {hard.workRam+395} how far the hammer's life has run
2FBA: A7              AND     A                   
2FBB: CA 7C 2F        JP      Z,$2F7C             ; {code.commitSpriteRecordAtMarioOffset} first half: no flash

; Flash the hammer sprite by overriding its colour on half of the frame counter's cycle.
; It reads frame and, on the half where bit 3 is set, forces the sprite record's
; attribute byte to 1; on the other half the caller's own attribute passes through
; untouched. Either way it then lays the finished record down. On screen that is the
; hammer sprite changing colour every 8 frames. This arm is only reached once the
; hammer's timer has run most of its course, but nothing here establishes that the flash
; is an about-to-expire warning.
blinkHammerSpriteOnFramePhase:
2FBE: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} the flash runs off the frame counter
2FC1: CB 5F           BIT     3,A                 ; eight frames on, eight off
2FC3: CA 7C 2F        JP      Z,$2F7C             ; {code.commitSpriteRecordAtMarioOffset} off half: keep the colour
2FC6: 0E 01           LD      C,$01               ; on half: force the sprite's colour
2FC8: C3 7C 2F        JP      $2F7C               ; {code.commitSpriteRecordAtMarioOffset}

; Run the clock down on the boards whose bonus is timed, once per frame. A per-board
; skip gate has the bits for boards 2, 3 and 4 set, so it opens on the 50m conveyor, 75m
; elevator and 100m rivet boards and closes on 25m, which paces its own bonus from
; barrel releases instead. bonusTick then counts down one per frame; until it reaches
; zero the current bonus period is still running and there is nothing more to do. When a
; period elapses it posts that period's deferred work -- a board-object spawn request
; written to spawnRequest and the bookkeeping byte that moves with it, plus a task-ring
; message -- and reloads bonusTick from bonusPeriod. bonus, the value the player sees,
; then drops by one; while it is still positive the board keeps its bonus, and when it
; reaches zero bonusExpiredStep is set to 1, which kicks off the bonus-expired sequence.
tickTimedBoardBonus:
2FCB: 3E 0E           LD      A,$0E               ; board mask: the three timed boards, not 25m
2FCD: F7              RST     $30                 
2FCE: 21 B4 62        LD      HL,$62B4            
2FD1: 35              DEC     (HL)                ; one tick off the current bonus period
2FD2: C0              RET     NZ                  ; period still running
2FD3: 3E 03           LD      A,$03               
2FD5: 32 B9 62        LD      ($62B9),A           ; {hard.workRam+2B9} post this period's deferred work...
2FD8: 32 96 63        LD      ($6396),A           ; {hard.workRam+396} ...and request a board object
2FDB: 11 01 05        LD      DE,$0501            ; task: take one notch off the bonus readout
2FDE: CD 9F 30        CALL    $309F               ; {code.enqueueTask}
2FE1: 3A B3 62        LD      A,($62B3)           ; {hard.workRam+2B3} reload the tick for the next period
2FE4: 77              LD      (HL),A              
2FE5: 21 B1 62        LD      HL,$62B1            
2FE8: 35              DEC     (HL)                ; step the on-screen bonus down one
2FE9: C0              RET     NZ                  ; still positive: the board keeps its bonus
2FEA: 3E 01           LD      A,$01               
2FEC: 32 86 63        LD      ($6386),A           ; {hard.workRam+386} bonus exhausted: start the expiry sequence
2FEF: C9              RET                         

; Map a screen pixel (y, x) to the video-RAM address of the tile that CONTAINS it, so
; every tile probe and tile write can address "the cell under this pixel" without
; repeating the arithmetic:
;   col = (x >> 3) & 0x1f;   row = (255 - y) >> 3;   address = vram base + row*32 + col
; THE COMPLEMENT IS THE INTERESTING PART: y is complemented before the divide, so the
; game's OWN address arithmetic is vertically MIRRORED. The 180-degree rotation the
; video path renders is not something imposed on top of a conventionally addressed
; tilemap -- the game computes flipped addresses itself. The divide on x is a rotate
; rather than a shift, so the low three bits of x wrap into the top of the byte and are
; masked off, which is why the mask is five column bits and not six.
tileAddrForPixel:
2FF0: 7D              LD      A,L                 ; the pixel's column coordinate
2FF1: 0F              RRCA                        
2FF2: 0F              RRCA                        
2FF3: 0F              RRCA                        ; divide by eight -- a rotate, so low bits wrap up
2FF4: E6 1F           AND     $1F                 ; and are masked off, leaving five column bits
2FF6: 6F              LD      L,A                 
2FF7: 7C              LD      A,H                 ; the other coordinate
2FF8: 2F              CPL                         ; complemented: the game's own addressing is mirrored
2FF9: E6 F8           AND     $F8                 ; drop the sub-cell bits
2FFB: 5F              LD      E,A                 
2FFC: AF              XOR     A                   
2FFD: 67              LD      H,A                 
2FFE: CB 13           RL      E                   
3000: 17              RLA                         
3001: CB 13           RL      E                   
3003: 17              RLA                         ; scale the row up to 32 cells per row
3004: C6 74           ADD     A,$74               ; the tilemap page
3006: 57              LD      D,A                 
3007: 19              ADD     HL,DE               ; base + row*32 + column: the cell holding the pixel
3008: C9              RET                         

; A bit-field lookup over a packed table of four 2-bit fields, keyed by an input byte and
; a 2-bit selector. Bit 0 of the input picks a family of two packed bytes and bit 2 picks
; within it; on the bit-0-set family only, a selector with bit 2 set is decremented
; first. It then rotates the packed byte right two bits at a time until its low two bits
; match the selector, and returns the field AFTER the match, carry set. A next-field of 3
; instead clears bit 2 of the original input, decrements it, and returns 3 while that is
; still non-zero or 4 otherwise, carry clear. Three of the four packed bytes are
; permutations of {0,1,2,3}; the fourth is {0,0,1,2} and has no 3, so a selector of 3
; against it -- or any selector above 3 -- never matches and the rotate loops forever. A
; leaf, and pure: it reads and writes no memory. Nothing here says the result is an
; ANIMATION step; that reading comes from how callers consume it.
nextAnimationStep:
3009: 57              LD      D,A                 ; keep the input for the exit test
300A: 0F              RRCA                        ; bit 0 of the input picks the family
300B: DA 22 30        JP      C,$3022             ; {code.loc_3022}
300E: 0E 93           LD      C,$93               ; this family's first packed byte
3010: 0F              RRCA                        
3011: 0F              RRCA                        ; bit 2 picks within the family
3012: D2 17 30        JP      NC,$3017            ; {code.loc_3017}
3015: 0E 6C           LD      C,$6C               ; the other packed byte of this family

loc_3017:
3017: 07              RLCA                        
3018: DA 31 30        JP      C,$3031             ; {code.loc_3031}
301B: 79              LD      A,C                 
301C: E6 F0           AND     $F0                 ; 0x93 is used as 0x90 -- fields 0, 0, 1, 2
301E: 4F              LD      C,A                 
301F: C3 31 30        JP      $3031               ; {code.loc_3031}

loc_3022:
3022: 0E B4           LD      C,$B4               ; the other family's first packed byte
3024: 0F              RRCA                        
3025: 0F              RRCA                        
3026: D2 2B 30        JP      NC,$302B            ; {code.loc_302b}
3029: 0E 1E           LD      C,$1E               ; its second packed byte

loc_302b:
302B: CB 50           BIT     2,B                 ; only this family adjusts the selector
302D: CA 31 30        JP      Z,$3031             ; {code.loc_3031}
3030: 05              DEC     B                   

loc_3031:
3031: 79              LD      A,C                 
3032: 0F              RRCA                        
3033: 0F              RRCA                        ; walk the packed byte one 2-bit field on
3034: 4F              LD      C,A                 
3035: E6 03           AND     $03                 
3037: B8              CP      B                   ; stop on the field matching the selector
3038: C2 31 30        JP      NZ,$3031            ; {code.loc_3031} no match yet -- 0x90 has no 3, so this can hang
303B: 79              LD      A,C                 
303C: 0F              RRCA                        
303D: 0F              RRCA                        
303E: E6 03           AND     $03                 ; the field AFTER the match is the answer
3040: FE 03           CP      $03                 
3042: C0              RET     NZ                  ; under 3: return it with carry set
3043: CB 92           RES     2,D                 ; a 3 takes the two-stage exit on the input
3045: 15              DEC     D                   
3046: C0              RET     NZ                  ; still counting: report 3
3047: 3E 04           LD      A,$04               ; exhausted: report 4
3049: C9              RET                         

; Slide one indexed pair of playfield cells up a row, for the opening Kong-climb intro --
; the intro animates by sliding a strip of the playfield up the screen a tilemap row at a
; time, and this is one cell-pair of that slide. It reads introScrollIndex and uses it as
; the offset into two fixed video cell columns two rows apart, copying each indexed cell
; to the cell one 32-column row above it, then steps the index down. Calling it
; repeatedly walks the index down and slides a whole run of cells up a row, cell by cell.
; Both copies go through a shared displaced-copy primitive that leaves the index and the
; displacement alone, so they are set once here and reused.
scrollClimbGraphicStep:
304A: 11 E0 FF        LD      DE,$FFE0            ; minus one tilemap row -- the slide's step
304D: 3A 8E 63        LD      A,($638E)           ; {hard.workRam+38E} which cell of the strip moves this call
3050: 4F              LD      C,A                 
3051: 06 00           LD      B,$00               
3053: 21 00 76        LD      HL,$7600            ; the first of the two cell columns
3056: CD 64 30        CALL    $3064               ; {code.copyByteDisplaced} slide that cell one row up
3059: 21 C0 75        LD      HL,$75C0            ; the strip's other column, two rows away
305C: CD 64 30        CALL    $3064               ; {code.copyByteDisplaced}
305F: 21 8E 63        LD      HL,$638E            
3062: 35              DEC     (HL)                ; step the index down for the next call
3063: C9              RET                         

; A generic addressing primitive. Three values arrive from the caller -- a base address,
; an index to add to it, and a signed displacement -- and the byte at base-plus-index is
; copied to base-plus-index-plus-displacement, so the destination is simply the source
; moved by the displacement. Both additions are 16-bit and WRAP. In play it slides a
; tilemap cell by one row, by being handed minus one row's worth of cells; the display
; is rotated a quarter turn, so a tilemap row is not a row on the glass. The routine
; itself knows nothing about rows or the screen -- which is why it is
; named for the addressing it does rather than for the effect the caller gets out of it.
copyByteDisplaced:
3064: 09              ADD     HL,BC               ; source = base plus the caller's index
3065: 7E              LD      A,(HL)              ; read the byte to be moved
3066: 19              ADD     HL,DE               ; destination = source plus the displacement
3067: 77              LD      (HL),A              ; drop the copy at the displaced address
3068: C9              RET                         

; A gated INDIRECT increment, and the small indirection that lets several sequences
; share one timer. Each call ticks substateTimer down by one; only on the frame it
; reaches zero does the body run and bump a step byte. The target is reached indirectly:
; the WORD in seqAdvancePtr names an address, and the byte at THAT address is
; incremented, the pointer cell itself left untouched. Setup routines re-point it at
; whichever sequence is running -- introStep during the opening cutscene,
; boardAdvanceStep during the board-cleared interlude -- so this one helper advances
; whichever is currently armed. The increment wraps at 8 bits. This is the single-level
; gate: it ticks substateTimer alone, not the prescaler its sibling runs through.
advanceSequenceStepWhenTimerExpires:
3069: DF              RST     $18                 ; tick the sub-state timer; nothing else until it expires
306A: 2A C0 63        LD      HL,($63C0)          ; {hard.workRam+3C0} the word names whichever step is armed
306D: 34              INC     (HL)                ; advance that sequence one step
306E: C9              RET                         

; Advance one animation frame of the ten-record spriteObjBlock, once every eight calls.
; Every call bumps a private 1-in-8 phase counter, and seven of eight return at once. On
; the eighth it edits the ten 4-byte records: scroll the whole group up 4 pixels by
; adding -4 to all ten Y bytes; flip and animate four of them by exclusive-oring 0x81 --
; bit 7 the horizontal flip, bit 0 the tile's low bit -- into the code bytes of records 0
; and 1, and of records 5 and 6; then stir the random seed and exclusive-or bit 7 of the
; fresh value into record 9's code byte, so that one sprite's flip toggles on a coin-flip
; at each animation step.
animateSpriteObjectBlock:
306F: 21 AF 62        LD      HL,$62AF            ; the private 1-in-8 animation phase counter
3072: 34              INC     (HL)                ; bump it on every call
3073: 7E              LD      A,(HL)              
3074: E6 07           AND     $07                 
3076: C0              RET     NZ                  ; seven calls in eight stop here
3077: 21 0B 69        LD      HL,$690B            ; the Y byte of the first of the ten records
307A: 0E FC           LD      C,$FC               ; minus four: scroll the whole group up 4 pixels
307C: FF              RST     $38                 ; add it into all ten Y bytes; leaves the stride at 4
307D: 0E 81           LD      C,$81               ; mask: bit 7 the flip, bit 0 the tile's low bit
307F: 21 09 69        LD      HL,$6909            ; code byte of record 0 -- the pair 0 and 1
3082: CD 96 30        CALL    $3096               ; {code.xorMaskStridedPair} toggle flip and tile bit in both
3085: 21 1D 69        LD      HL,$691D            ; code byte of record 5 -- the pair 5 and 6
3088: CD 96 30        CALL    $3096               ; {code.xorMaskStridedPair}
308B: CD 57 00        CALL    $0057               ; {code.stirRandomSeed} fresh entropy for the coin flip below
308E: E6 80           AND     $80                 ; keep only the flip bit of the fresh value
3090: 21 2D 69        LD      HL,$692D            ; record 9's code byte
3093: AE              XOR     (HL)                
3094: 77              LD      (HL),A              ; that sprite's flip toggles on a coin flip
3095: C9              RET                         

; Toggle the same bit pattern in two bytes a fixed distance apart. It reads a byte, XORs
; the caller's mask into it, writes it back, steps forward by the caller's stride and
; does it once more; the count is fixed at two. Because it XORs rather than stores it
; flips exactly the bits the mask selects and leaves the rest of each byte alone, so
; running it twice on the same pair restores them. Address, mask and stride all come from
; the caller, and the stride in particular is INHERITED -- nothing on the way in reloads
; it, so a caller that has not set it gets whatever the last routine to touch it left
; behind.
xorMaskStridedPair:
3096: 06 02           LD      B,$02               ; always exactly two bytes

loc_3098:
3098: 79              LD      A,C                 
3099: AE              XOR     (HL)                ; flip the bits the caller's mask selects
309A: 77              LD      (HL),A              
309B: 19              ADD     HL,DE               ; step to the second byte by the caller's stride
309C: 10 FA           DJNZ    $3098               ; {code.loc_3098}
309E: C9              RET                         

; Post a two-byte [opcode, argument] message onto the task ring, the game's
; deferred-work queue. Anything that wants a unit of work done later -- add to the
; score, start a sound, bump a counter -- posts it here instead of doing it inline, and
; the main loop drains the ring and dispatches each message; dozens of call sites feed
; it. The ring is 32 two-byte slots, all inside one page, and taskTail holds only the
; LOW byte of the next slot to write. A slot is FREE only while bit 7 of its opcode byte
; is SET: the empty marker is 0xFF, not zero, and boot fills the whole ring with it. If
; the slot at the tail is occupied the ring is full there and the post is silently
; DROPPED -- nothing is written and the tail does not move. Otherwise the pair goes into
; the slot and the tail advances by two, pinned back to the ring's first slot when it
; steps past the end.
enqueueTask:
309F: E5              PUSH    HL                  
30A0: 21 C0 60        LD      HL,$60C0            ; base of the 32-slot task ring
30A3: 3A B0 60        LD      A,($60B0)           ; {hard.workRam+B0} low byte of the next slot to write
30A6: 6F              LD      L,A                 ; address that slot
30A7: CB 7E           BIT     7,(HL)              ; a slot is free only while its opcode's bit 7 is set
30A9: CA BB 30        JP      Z,$30BB             ; {code.loc_30bb} ring full here -- drop the message
30AC: 72              LD      (HL),D              ; store the message opcode
30AD: 2C              INC     L                   
30AE: 73              LD      (HL),E              ; and its argument
30AF: 2C              INC     L                   
30B0: 7D              LD      A,L                 
30B1: FE C0           CP      $C0                 ; did the tail step off the end of the ring?
30B3: D2 B8 30        JP      NC,$30B8            ; {code.loc_30b8}
30B6: 3E C0           LD      A,$C0               ; it wrapped -- pin it back to the first slot

loc_30b8:
30B8: 32 B0 60        LD      ($60B0),A           ; {hard.workRam+B0} publish the advanced tail

loc_30bb:
30BB: E1              POP     HL                  
30BC: C9              RET                         

; Zero the X byte of four fixed groups of sprite records, parking those sprites at the
; left edge. Four back-to-back stride-4 zero fills, every target on a record boundary so
; each run blanks field +0:
;   spriteBuffer+0x50,  2 records   -- records 20-21
;   spriteBuffer+0x80,  10 records  -- records 32-41
;   spriteBuffer+0xb8,  11 records  -- records 46-56
;   spriteBuffer+0x10c, 5 records   -- records 67-71
; 28 records' X byte in all. It runs at two moments in play: as Mario's death animation
; is seeded, and from the board-advance interlude once a board is cleared. The mechanism
; is exact; that the intent is to hide those particular sprite groups is inference, and
; the record identities are not pinned here.
clearSpriteColumns:
30BD: 21 50 69        LD      HL,$6950            ; first group: sprite records 20-21
30C0: 06 02           LD      B,$02               
30C2: CD E4 30        CALL    $30E4               ; {code.clearStridedBytes} zero their X byte
30C5: 2E 80           LD      L,$80               ; second group: records 32-41
30C7: 06 0A           LD      B,$0A               
30C9: CD E4 30        CALL    $30E4               ; {code.clearStridedBytes}
30CC: 2E B8           LD      L,$B8               ; third group: records 46-56
30CE: 06 0B           LD      B,$0B               
30D0: CD E4 30        CALL    $30E4               ; {code.clearStridedBytes}
30D3: 21 0C 6A        LD      HL,$6A0C            ; fourth group: records 67-71
30D6: 06 05           LD      B,$05               
30D8: C3 E4 30        JP      $30E4               ; {code.clearStridedBytes} tail-clear the last group

loc_30db:
30DB: 21 4C 69        LD      HL,$694C            ; the X byte of Mario's sprite record
30DE: 36 00           LD      (HL),$00            ; blank it, parking that sprite at the left edge
30E0: 2E 58           LD      L,$58               ; then six more records of the shadow buffer
30E2: 06 06           LD      B,$06               

; Zero B bytes at stride 4, starting at HL. The +4 step is applied to the LOW address
; byte alone, never as a 16-bit add, so an overflow wraps within the current 256-byte
; page and never carries into the high byte -- the clear is confined to one page, and
; that confinement is the routine's defining property. The count is decremented then
; tested, so the body always runs at least once and B = 0 on entry means 256 passes
; rather than none. Every target the game hands it lies inside the sprite shadow buffer,
; so in practice it blanks a stride-4 column -- one field of each 4-byte sprite record --
; across a run of records, during board and cutscene setup and when a player dies.
clearStridedBytes:
30E4: 7D              LD      A,L                 ; walk the LOW address byte only -- the clear stays in one page

loc_30e5:
30E5: 36 00           LD      (HL),$00            ; blank this record's field
30E7: C6 04           ADD     A,$04               ; step on one record, stride 4
30E9: 6F              LD      L,A                 
30EA: 10 F9           DJNZ    $30E5               ; {code.loc_30e5}
30EC: C9              RET                         

; One frame of the fire service, in four steps. It computes nothing itself; what it
; contributes is the ORDER and the two gates that can end the frame's fire work early.
; First the difficulty gate: a frame that fails it is simply not one of the frames the
; fires move on, and nothing below runs -- which is how the fires get faster as the game
; gets harder without any of the code below knowing about difficulty. Then the census:
; sweep the five fire records, tally the live ones and admit at most one pending spawn;
; an empty array ends the frame here too. Then the state walk, visiting the same five
; records and running the per-fire body on each occupied one. Then the publish, gathering
; the five records into their five drawn sprite records. Both early exits are taken
; inside the callee that decides them.
updateFires:
30ED: CD FA 30        CALL    $30FA               ; {code.gateFireUpdateByDifficulty} difficulty paces the pass

loc_30f0:
30F0: CD 3C 31        CALL    $313C               ; {code.spawnRequestedFireAndRecolorLiveFires}
30F3: CD B1 31        CALL    $31B1               ; {code.advanceLiveFires} advance each live fire one frame
30F6: CD F3 34        CALL    $34F3               ; {code.publishFireSprites} gather the five records into sprites
30F9: C9              RET                         

; Pick this difficulty's frame gate and hand its proceed/skip decision straight back to
; the caller. It reads difficulty, clamps it to the six slots the table has, and runs
; the gate that slot names; each gate reads the low bits of the frame counter, so the
; pair paces the caller to a duty cycle that widens as difficulty climbs -- 0 and 1
; every other frame, 2 five frames in eight, 3 and 4 three in four, 5 and up seven in
; eight. Two of the six slots are DUPLICATES, which is why four gates cover six
; difficulties; that is the table's own shape. The clamp is a genuine guard but never
; fires in normal play, since difficulty's own writer already caps it at 5. It writes no
; memory at all -- its entire output is a decision it does not itself use.
gateFireUpdateByDifficulty:
30FA: 3A 80 63        LD      A,($6380)           ; {hard.workRam+380} which frame gate paces the fires
30FD: FE 06           CP      $06                 ; the table holds only six slots
30FF: 38 02           JR      C,$3103             ; {code.loc_3103}
3101: 3E 05           LD      A,$05               ; anything higher shares the last, widest gate

loc_3103:
3103: EF              RST     $28                 ; run that gate; its answer is the caller's

; ---- $3104-$310F: jump table ----
3104: 10 31 10 31 1B 31 26 31 26 31 31 31

loc_3110:
3110: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} the frame counter drives the duty cycle
3113: E6 01           AND     $01                 ; one bit -- a two-frame cycle
3115: FE 01           CP      $01                 
3117: C8              RET     Z                   ; odd frame -- run the fire pass
3118: 33              INC     SP                  ; even frame: unwind past the whole pass
3119: 33              INC     SP                  
311A: C9              RET                         

loc_311b:
311B: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A}
311E: E6 07           AND     $07                 ; the low three bits -- an eight-frame cycle
3120: FE 05           CP      $05                 ; the first five phases of eight proceed
3122: F8              RET     M                   ; in the window -- run the fire pass
3123: 33              INC     SP                  ; otherwise unwind past the whole pass
3124: 33              INC     SP                  
3125: C9              RET                         

loc_3126:
3126: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A}
3129: E6 03           AND     $03                 ; the low two bits of the frame counter
312B: FE 03           CP      $03                 ; both set on one frame in four
312D: F8              RET     M                   ; the other three run the fire pass
312E: 33              INC     SP                  ; on the fourth, unwind past the whole pass
312F: 33              INC     SP                  
3130: C9              RET                         

loc_3131:
3131: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A}
3134: E6 07           AND     $07                 ; the low three bits of the frame counter
3136: FE 07           CP      $07                 ; all set on one frame in eight
3138: F8              RET     M                   ; the other seven run the fire pass
3139: 33              INC     SP                  ; on the eighth, unwind past the whole pass
313A: 33              INC     SP                  
313B: C9              RET                         

; Sweep the five objArray64 fire records at stride 0x20 and tally the live ones into
; objLiveCount. Each LIVE record has its sprite-attribute byte flagged on -- or off
; while marioHammerActive is set, so the hammer visibly recolours every live fire. Each
; EMPTY record may honour a pending insert request in eventReq313c: off 50m, or on 50m
; while difficulty does not EQUAL the running count, a raised request activates that
; free slot, consumes the request and bumps the count. That 50m early exit is an EXACT
; EQUALITY, not a population cap: it is tested only at empty records while the count is
; bumped at live ones, so the count can step straight PAST difficulty without the test
; ever seeing the boundary. On that exit the request is deliberately NOT cleared. After
; the scan the request is cleared and the count inspected: non-zero returns normally,
; zero discards the caller's return address and returns a level up, skipping the rest of
; the object pass. This is the only routine that spawns one of these during play --
; records are also activated outright at board build.
spawnRequestedFireAndRecolorLiveFires:
313C: DD 21 00 64     LD      IX,$6400            ; the first of the five fire records
3140: AF              XOR     A                   
3141: 32 A1 63        LD      ($63A1),A           ; {hard.workRam+3A1} start the live tally at zero
3144: 06 05           LD      B,$05               ; five records to sweep
3146: 11 20 00        LD      DE,$0020            ; the stride between them

loc_3149:
3149: DD 7E 00        LD      A,(IX+$00)          ; the record's occupancy flag
314C: FE 00           CP      $00                 
314E: CA 7C 31        JP      Z,$317C             ; {code.loc_317c} empty slot -- go and see if a spawn is pending
3151: 3A A1 63        LD      A,($63A1)           ; {hard.workRam+3A1} live record: the running tally
3154: 3C              INC     A                   
3155: 32 A1 63        LD      ($63A1),A           ; {hard.workRam+3A1} count it
3158: 3E 01           LD      A,$01               
315A: DD 77 08        LD      (IX+$08),A          ; flag the fire's sprite attribute on
315D: 3A 17 62        LD      A,($6217)           ; {hard.workRam+217} is Mario swinging a hammer?
3160: FE 01           CP      $01                 
3162: C2 6A 31        JP      NZ,$316A            ; {code.loc_316a}
3165: 3E 00           LD      A,$00               
3167: DD 77 08        LD      (IX+$08),A          ; hammer up: recolour every live fire

loc_316a:
316A: DD 19           ADD     IX,DE               ; on to the next record
316C: 10 DB           DJNZ    $3149               ; {code.loc_3149}
316E: 21 A0 63        LD      HL,$63A0            ; the pending insert request
3171: 36 00           LD      (HL),$00            ; consume it, honoured or not
3173: 3A A1 63        LD      A,($63A1)           ; {hard.workRam+3A1} the finished tally
3176: FE 00           CP      $00                 
3178: C0              RET     NZ                  ; something is live -- carry on with the pass
3179: 33              INC     SP                  ; array empty: unwind past the rest of the pass
317A: 33              INC     SP                  
317B: C9              RET                         

loc_317c:
317C: 3A A1 63        LD      A,($63A1)           ; {hard.workRam+3A1} empty slot: how many are live so far
317F: FE 05           CP      $05                 
3181: CA 6A 31        JP      Z,$316A             ; {code.loc_316a} array already full -- nothing can go in
3184: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} 50m is the only board that caps spawns here
3187: FE 02           CP      $02                 
3189: C2 95 31        JP      NZ,$3195            ; {code.loc_3195}
318C: 3A A1 63        LD      A,($63A1)           ; {hard.workRam+3A1}
318F: 4F              LD      C,A                 
3190: 3A 80 63        LD      A,($6380)           ; {hard.workRam+380}
3193: B9              CP      C                   ; on 50m stop the moment the tally equals difficulty
3194: C8              RET     Z                   ; and leave the request standing for a later frame

loc_3195:
3195: 3A A0 63        LD      A,($63A0)           ; {hard.workRam+3A0} is an insert being asked for?
3198: FE 01           CP      $01                 
319A: C2 6A 31        JP      NZ,$316A            ; {code.loc_316a} no request -- leave the slot empty
319D: DD 77 00        LD      (IX+$00),A          ; activate the slot
31A0: DD 77 18        LD      (IX+$18),A          ; mark it for the board-keyed insert walker
31A3: AF              XOR     A                   
31A4: 32 A0 63        LD      ($63A0),A           ; {hard.workRam+3A0} consume the request -- one insert per sweep
31A7: 3A A1 63        LD      A,($63A1)           ; {hard.workRam+3A1}
31AA: 3C              INC     A                   
31AB: 32 A1 63        LD      ($63A1),A           ; {hard.workRam+3A1} count the new fire
31AE: C3 6A 31        JP      $316A               ; {code.loc_316a}

; Walk the five records of objArray64 once a frame and advance each live one. It decides
; which records get a turn and nothing about what happens to one. First the
; difficulty-and-entropy gated arm runs, stamping a field on two records of this same
; array. Then the sweep index is zeroed and objIterPtr is seeded one stride BELOW the
; array base -- the pointer is advanced before each record is read, so the first record
; visited is the array base itself and the seeded value is never read. Five iterations
; follow: advance the pointer and store it back, then, when that record's active flag is
; non-zero, run the per-object advance. An empty record is skipped but still consumes an
; iteration, so the five map one-to-one onto the five records. The pointer lives in
; memory because that is how the record base reaches the per-object advance, which loads
; its record pointer back out of objIterPtr.
advanceLiveFires:
31B1: CD DD 31        CALL    $31DD               ; {code.armAlternateFireModeAtHighDifficulty}
31B4: AF              XOR     A                   
31B5: 32 A2 63        LD      ($63A2),A           ; {hard.workRam+3A2} start the sweep index at zero
31B8: 21 E0 63        LD      HL,$63E0            ; one stride BELOW the array base
31BB: 22 C8 63        LD      ($63C8),HL          ; {hard.workRam+3C8} where the per-fire body finds its record

loc_31be:
31BE: 2A C8 63        LD      HL,($63C8)          ; {hard.workRam+3C8} re-read it -- a callee may have moved it
31C1: 01 20 00        LD      BC,$0020            
31C4: 09              ADD     HL,BC               ; step on to the next record
31C5: 22 C8 63        LD      ($63C8),HL          ; {hard.workRam+3C8} publish it before the body is entered
31C8: 7E              LD      A,(HL)              ; the record's occupancy flag
31C9: A7              AND     A                   
31CA: CA D0 31        JP      Z,$31D0             ; {code.loc_31d0} empty slot -- it still costs an iteration
31CD: CD 02 32        CALL    $3202               ; {code.advanceFire} advance this one fire

loc_31d0:
31D0: 3A A2 63        LD      A,($63A2)           ; {hard.workRam+3A2}
31D3: 3C              INC     A                   
31D4: 32 A2 63        LD      ($63A2),A           ; {hard.workRam+3A2}
31D7: FE 05           CP      $05                 ; five records to a sweep
31D9: C2 BE 31        JP      NZ,$31BE            ; {code.loc_31be}
31DC: C9              RET                         

; Stamp mode 2 into one field of two fire records, but only on a hard board and only on a
; rare entropy draw. Two gates, both of which must open on the same pass. First,
; difficulty at least 3: the test is a SIGNED one on (difficulty - 3), so in play it
; means 3, 4 or 5, and faithfully it closes again once difficulty reaches 131, where the
; signed difference turns negative -- a value normal play never reaches. Second, an
; entropy draw that comes up exactly 1: the draw is the low two bits of random, or the
; frame counter substituted in when those two bits are exactly 1, so the draw is 1 only
; when both are. Past both gates the constant 2 is stamped into field +0x19 of records 1
; and 3 of objArray64, and nothing else is written on any path. What mode 2 makes a fire
; DO is not established -- no reader of that field appears here.
armAlternateFireModeAtHighDifficulty:
31DD: 3A 80 63        LD      A,($6380)           ; {hard.workRam+380} difficulty gates this arming pass
31E0: FE 03           CP      $03                 
31E2: F8              RET     M                   ; below difficulty 3 nothing is armed
31E3: CD F6 31        CALL    $31F6               ; {code.loc_31f6} take the entropy draw
31E6: FE 01           CP      $01                 
31E8: C0              RET     NZ                  ; only a draw of exactly 1 opens the second gate
31E9: 21 39 64        LD      HL,$6439            ; field +0x19 of fire record 1
31EC: 3E 02           LD      A,$02               
31EE: 77              LD      (HL),A              ; stamp mode 2 into it
31EF: 21 79 64        LD      HL,$6479            ; the same field of record 3
31F2: 3E 02           LD      A,$02               
31F4: 77              LD      (HL),A              
31F5: C9              RET                         

loc_31f6:
31F6: 3A 18 60        LD      A,($6018)           ; {hard.workRam+18} the entropy draw's first source
31F9: E6 03           AND     $03                 
31FB: FE 01           CP      $01                 
31FD: C0              RET     NZ                  ; 0, 2 or 3 is the draw itself
31FE: 3A 1A 60        LD      A,($601A)           ; {hard.workRam+1A} exactly 1 substitutes the frame counter
3201: C9              RET                         

; Advance ONE fire by a frame. The record arrives through objIterPtr and is deliberately
; re-read at three points, because a callee may have moved it on. ROUTING: a record
; whose insert-requested field is 1 is not a live fire yet and belongs to the
; board-keyed insert walker. Otherwise a record on the LOW side of the state split gets
; one of two timer ticks, chosen by a record field. BOTH arms reach the heading state
; machine, by different routes: the arm the field selects with 2 ticks a dwell counter and
; rejoins PAST the random gate, unconditionally. Only the other arm -- the reroll timer --
; passes through the gate, and then only on a pass that finds the low two bits of random
; clear. THAT IS THE REROLL: the timer decides a new heading is due and the random gate
; keeps the rerolls on that arm off a fixed cadence. MOVEMENT: the working X steps ONE pixel the way the
; state field points, and the tile 12px below the new position is judged -- out of band
; and the step is UNDONE and the heading reversed; in band, only the X edges 16 and 240
; can re-arm it. PUBLISH: the working X becomes the drawn X and the working Y plus a
; table byte the drawn Y, the table index counting down every pass and reloading at 0.
; What that table holds is not established.
advanceFire:
3202: DD 2A C8 63     LD      IX,($63C8)          ; {hard.workRam+3C8} the record the walk is pointing at
3206: DD 7E 18        LD      A,(IX+$18)          ; is this record still waiting to be inserted?
3209: FE 01           CP      $01                 
320B: CA 7A 32        JP      Z,$327A             ; {code.loc_327a} not a live fire yet -- the insert walker takes it
320E: DD 7E 0D        LD      A,(IX+$0D)          ; the fire's state
3211: FE 04           CP      $04                 
3213: F2 30 32        JP      P,$3230             ; {code.loc_3230} the climbing states skip the timers below
3216: DD 7E 19        LD      A,(IX+$19)          ; which of the two timer ticks this record uses
3219: FE 02           CP      $02                 
321B: CA 7E 32        JP      Z,$327E             ; {code.loc_327e} the dwell-counter arm
321E: CD 0F 33        CALL    $330F               ; {code.tickFireTimerAndRerollDirection} reroll the heading

loc_3221:
3221: 3A 18 60        LD      A,($6018)           ; {hard.workRam+18} keep the rerolls off a fixed cadence
3224: E6 03           AND     $03                 
3226: C2 33 32        JP      NZ,$3233            ; {code.loc_3233} not a reroll pass -- straight on to the step

loc_3229:
3229: DD 7E 0D        LD      A,(IX+$0D)          
322C: A7              AND     A                   
322D: CA 57 32        JP      Z,$3257             ; {code.loc_3257} a fire back at state 0 has nothing to move

loc_3230:
3230: CD 3D 33        CALL    $333D               ; {code.driveFireLadderClimb} decide about leaving for a ladder

loc_3233:
3233: DD 7E 0D        LD      A,(IX+$0D)          
3236: FE 04           CP      $04                 
3238: F2 91 32        JP      P,$3291             ; {code.loc_3291} on a ladder -- the vertical arm instead
323B: CD AD 33        CALL    $33AD               ; {code.walkFireOneStep} one pixel along the current heading
323E: CD 8C 29        CALL    $298C               ; {code.turnFireAtGroundEdge} has the ground below run out?
3241: FE 01           CP      $01                 
3243: CA 97 32        JP      Z,$3297             ; {code.loc_3297} at an edge -- undo the step and turn round
3246: DD 2A C8 63     LD      IX,($63C8)          ; {hard.workRam+3C8} re-read the record; the probe may have moved it
324A: DD 7E 0E        LD      A,(IX+$0E)          ; the working X after the step
324D: FE 10           CP      $10                 
324F: DA 8C 32        JP      C,$328C             ; {code.loc_328c} past the low bound -- send it back the other way
3252: FE F0           CP      $F0                 
3254: D2 84 32        JP      NC,$3284            ; {code.loc_3284} past the high bound -- likewise

loc_3257:
3257: DD 7E 13        LD      A,(IX+$13)          ; index into the drawn-Y offset table
325A: FE 00           CP      $00                 
325C: C2 B9 32        JP      NZ,$32B9            ; {code.loc_32b9}
325F: 3E 11           LD      A,$11               ; the index reloads at 17 when it runs out

loc_3261:
3261: DD 77 13        LD      (IX+$13),A          ; store the stepped index
3264: 16 00           LD      D,$00               
3266: 5F              LD      E,A                 
3267: 21 7A 3A        LD      HL,$3A7A            ; the table the offset comes from
326A: 19              ADD     HL,DE               
326B: 7E              LD      A,(HL)              ; this pass's Y offset
326C: DD 46 0E        LD      B,(IX+$0E)          
326F: DD 70 03        LD      (IX+$03),B          ; the working X becomes the drawn X
3272: DD 4E 0F        LD      C,(IX+$0F)          
3275: 81              ADD     A,C                 
3276: DD 77 05        LD      (IX+$05),A          ; working Y plus the offset becomes the drawn Y
3279: C9              RET                         

loc_327a:
327A: CD BD 32        CALL    $32BD               ; {code.loc_32bd} hand the record to the board-keyed insert walker
327D: C9              RET                         

loc_327e:
327E: CD D6 32        CALL    $32D6               ; {code.loc_32d6} the other arm: the dwell counter
3281: C3 29 32        JP      $3229               ; {code.loc_3229} rejoin past the random gate

loc_3284:
3284: 3E 02           LD      A,$02               ; the heading that steps the working X down

loc_3286:
3286: DD 77 0D        LD      (IX+$0D),A          ; store the new heading
3289: C3 57 32        JP      $3257               ; {code.loc_3257}

loc_328c:
328C: 3E 01           LD      A,$01               ; the heading that steps the working X up
328E: C3 86 32        JP      $3286               ; {code.loc_3286}

loc_3291:
3291: CD E7 33        CALL    $33E7               ; {code.loc_33e7} climbing: animate and step the height
3294: C3 57 32        JP      $3257               ; {code.loc_3257}

loc_3297:
3297: DD 2A C8 63     LD      IX,($63C8)          ; {hard.workRam+3C8} re-read the record after the ground probe
329B: DD 7E 0D        LD      A,(IX+$0D)          
329E: FE 01           CP      $01                 
32A0: C2 B1 32        JP      NZ,$32B1            ; {code.loc_32b1}
32A3: 3E 02           LD      A,$02               ; it was heading one way -- reverse it
32A5: DD 35 0E        DEC     (IX+$0E)            ; and undo the pixel just taken

loc_32a8:
32A8: DD 77 0D        LD      (IX+$0D),A          ; store the reversed heading
32AB: CD C3 33        CALL    $33C3               ; {code.settleFireOnGirderSlope} re-settle onto the girder slope
32AE: C3 57 32        JP      $3257               ; {code.loc_3257}

loc_32b1:
32B1: 3E 01           LD      A,$01               ; the other heading, reversed the same way
32B3: DD 34 0E        INC     (IX+$0E)            ; undo the pixel
32B6: C3 A8 32        JP      $32A8               ; {code.loc_32a8}

loc_32b9:
32B9: 3D              DEC     A                   ; step the table index down one
32BA: C3 61 32        JP      $3261               ; {code.loc_3261}

loc_32bd:
32BD: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} which board decides the walker
32C0: FE 01           CP      $01                 
32C2: CA CE 32        JP      Z,$32CE             ; {code.loc_32ce} 25m: the flat-table walk
32C5: FE 02           CP      $02                 
32C7: CA D2 32        JP      Z,$32D2             ; {code.loc_32d2} 50m: its direction-selected twin
32CA: CD B9 34        CALL    $34B9               ; {code.loc_34b9} any other board: seed the record from a template
32CD: C9              RET                         

loc_32ce:
32CE: CD 2C 34        CALL    $342C               ; {code.loc_342c}
32D1: C9              RET                         

loc_32d2:
32D2: CD 78 34        CALL    $3478               ; {code.loc_3478}
32D5: C9              RET                         

loc_32d6:
32D6: DD 7E 1C        LD      A,(IX+$1C)          ; the record's interval down-counter
32D9: FE 00           CP      $00                 
32DB: C2 FD 32        JP      NZ,$32FD            ; {code.loc_32fd} still counting -- just step it down
32DE: DD 7E 1D        LD      A,(IX+$1D)          ; run out: is the position compare armed?
32E1: FE 01           CP      $01                 
32E3: C2 0B 33        JP      NZ,$330B            ; {code.loc_330b} not armed -- hand on to the periodic timer
32E6: DD 36 1D 00     LD      (IX+$1D),$00        ; disarm it; the compare happens once
32EA: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} where Mario's row is now
32ED: DD 46 0F        LD      B,(IX+$0F)          
32F0: 90              SUB     B                   ; against the object's own limit
32F1: DA 03 33        JP      C,$3303             ; {code.loc_3303} Mario short of it -- let the counter drain
32F4: DD 36 1C FF     LD      (IX+$1C),$FF        ; otherwise reload the counter to its maximum

loc_32f8:
32F8: DD 36 0D 00     LD      (IX+$0D),$00        ; and hold the object in state 0
32FC: C9              RET                         

loc_32fd:
32FD: DD 35 1C        DEC     (IX+$1C)            ; tick the interval down
3300: C2 F8 32        JP      NZ,$32F8            ; {code.loc_32f8} still running -- hold state 0 and stop

loc_3303:
3303: DD 36 19 00     LD      (IX+$19),$00        ; spent: clear the two exit fields
3307: DD 36 1C 00     LD      (IX+$1C),$00        

loc_330b:
330B: CD 0F 33        CALL    $330F               ; {code.tickFireTimerAndRerollDirection} tick the periodic timer
330E: C9              RET                         

; Tick one fire's periodic timer, the record's countdown field at +0x16. While that is
; still counting, the decrement is the whole routine. On the pass that finds it already
; at zero the timer is reloaded and the record's state field at +0x0d is reset to 0;
; then, ONLY when the low bit of random is set, the state is advanced to 1. The shared
; decrement then runs on the freshly reloaded value, leaving the timer at 42, so the
; cycle repeats every 43 passes -- a coin flip at each expiry moving the state between
; its only two values, the erratic half of the object's motion. The original also
; carries a branch that would set the state to 2, guarded by "state == 1"; the reset to
; 0 happens immediately before that test, so it can never match.
tickFireTimerAndRerollDirection:
330F: DD 7E 16        LD      A,(IX+$16)          ; the fire's periodic countdown
3312: FE 00           CP      $00                 
3314: C2 32 33        JP      NZ,$3332            ; {code.loc_3332} still counting -- only the tick below happens
3317: DD 36 16 2B     LD      (IX+$16),$2B        ; expired: reload 43 ticks
331B: DD 36 0D 00     LD      (IX+$0D),$00        ; and reset the heading to 0
331F: 3A 18 60        LD      A,($6018)           ; {hard.workRam+18} a coin flip decides the new heading
3322: 0F              RRCA                        
3323: D2 32 33        JP      NC,$3332            ; {code.loc_3332} tails -- leave the heading at 0
3326: DD 7E 0D        LD      A,(IX+$0D)          
3329: FE 01           CP      $01                 
332B: CA 36 33        JP      Z,$3336             ; {code.loc_3336} the reset just above makes this unreachable
332E: DD 36 0D 01     LD      (IX+$0D),$01        ; heads -- the other heading

loc_3332:
3332: DD 35 16        DEC     (IX+$16)            ; every path ends by ticking the timer down
3335: C9              RET                         

loc_3336:
3336: DD 36 0D 02     LD      (IX+$0D),$02        ; the arm that can never be entered
333A: C3 32 33        JP      $3332               ; {code.loc_3332}

; Decide when a fire leaves a girder for a ladder, and watch for its arrival. It never
; moves the fire itself -- it only chooses a destination and a direction; the fire's
; state byte picks which half runs. ON FOOT: a height guard comes first, and on the three
; lower boards a fire that has risen above that line abandons the climb decision
; outright, while on the top board the height test does not apply at all. Past it the
; fire's X is looked up in the type-0 object table, whose entries pair each key with TWO
; bytes; the discriminator is the fire's own Y base, so the lookup returns whichever of
; the pair it is NOT standing on. That byte becomes the destination and the tag becomes
; the direction. The descent is conditional where the ascent is not: it is taken only
; while the fire's row is above Mario's, so a fire level with him or below never sets off
; downward. TRAVELLING: both states poll the biased Y base against the stored destination
; and drop back to on-foot on the nose. The ascent alone, and only in one mode, raises an
; arrival mark.
driveFireLadderClimb:
333D: DD 7E 0D        LD      A,(IX+$0D)          ; the fire's state picks which half runs
3340: FE 08           CP      $08                 
3342: CA 71 33        JP      Z,$3371             ; {code.loc_3371} already climbing -- just watch for arrival
3345: FE 04           CP      $04                 
3347: CA 8A 33        JP      Z,$338A             ; {code.loc_338a} already descending -- likewise
334A: CD A1 33        CALL    $33A1               ; {code.loc_33a1} on foot: the board gate and height guard
334D: DD 7E 0F        LD      A,(IX+$0F)          ; the fire's own height
3350: C6 08           ADD     A,$08               ; biased the way the table's heights are
3352: 57              LD      D,A                 ; the end it is standing on, for the lookup
3353: DD 7E 0E        LD      A,(IX+$0E)          ; its X is the key into the ladder table
3356: 01 15 00        LD      BC,$0015            ; twenty-one entries to search
3359: CD 6E 23        CALL    $236E               ; {code.findOppositeLadderEnd} the other end of this ladder
335C: A7              AND     A                   ; the tag says which end it started from
335D: CA 99 33        JP      Z,$3399             ; {code.loc_3399} the far end -- set off upward
3360: DD 70 1F        LD      (IX+$1F),B          ; the height this climb ends at
3363: 3A 05 62        LD      A,($6205)           ; {hard.workRam+205} Mario's row
3366: 47              LD      B,A                 
3367: DD 7E 0F        LD      A,(IX+$0F)          
336A: 90              SUB     B                   ; is the fire's row above Mario's?
336B: D0              RET     NC                  ; level with him or below -- never head down
336C: DD 36 0D 04     LD      (IX+$0D),$04        ; above him -- start descending
3370: C9              RET                         

loc_3371:
3371: DD 7E 0F        LD      A,(IX+$0F)          ; climbing: where the fire has got to
3374: C6 08           ADD     A,$08               
3376: DD 46 1F        LD      B,(IX+$1F)          ; against the height it set off for
3379: B8              CP      B                   
337A: C0              RET     NZ                  ; not there yet
337B: DD 36 0D 00     LD      (IX+$0D),$00        ; arrived -- back on foot
337F: DD 7E 19        LD      A,(IX+$19)          
3382: FE 02           CP      $02                 
3384: C0              RET     NZ                  
3385: DD 36 1D 01     LD      (IX+$1D),$01        ; an arriving ascent in mode 2 raises its mark
3389: C9              RET                         

loc_338a:
338A: DD 7E 0F        LD      A,(IX+$0F)          ; descending: where the fire has got to
338D: C6 08           ADD     A,$08               
338F: DD 46 1F        LD      B,(IX+$1F)          
3392: B8              CP      B                   
3393: C0              RET     NZ                  ; not on the destination yet
3394: DD 36 0D 00     LD      (IX+$0D),$00        ; arrived -- back on foot, and no mark
3398: C9              RET                         

loc_3399:
3399: DD 70 1F        LD      (IX+$1F),B          ; the height above to climb to
339C: DD 36 0D 08     LD      (IX+$0D),$08        ; set off up the ladder
33A0: C9              RET                         

loc_33a1:
33A1: 3E 07           LD      A,$07               ; mask: 25m, 50m and 75m -- not the rivet board
33A3: F7              RST     $30                 ; closed on 100m -- skip the height test and carry on
33A4: DD 7E 0F        LD      A,(IX+$0F)          ; the fire's height
33A7: FE 59           CP      $59                 ; against the 89-pixel line
33A9: D0              RET     NC                  ; at or past it -- the climb decision goes ahead
33AA: 33              INC     SP                  ; risen above the line: abandon the climb decision
33AB: 33              INC     SP                  
33AC: C9              RET                         

; Step one fire a single position along its current heading. Its state byte picks the
; heading, and the same branch does two things at once: it steps the fire's working X one
; pixel and it sets or clears the sprite tile code's flip bit, so the mirrored sprite
; always faces the way the fire is moving. The "step up" state steps X up and sets the
; flip bit; every other state steps X down and clears it. The animation clock then runs
; over the SAME sprite code byte and a per-fire down-counter, so the ORDER matters -- the
; flip bit is written first and the animation step lands on top of it. Control then falls
; into the slope tail, which on the girder board re-snaps the working Y to the sloped
; girder under the fire's new X and does nothing elsewhere. The stepped coordinate is the
; WORKING X, one stage upstream of the drawn X it is copied into.
walkFireOneStep:
33AD: DD 7E 0D        LD      A,(IX+$0D)          ; the heading the state field carries
33B0: FE 01           CP      $01                 
33B2: CA D9 33        JP      Z,$33D9             ; {code.loc_33d9} the one state that steps the working X up
33B5: DD 7E 07        LD      A,(IX+$07)          ; the fire's sprite tile code
33B8: E6 7F           AND     $7F                 ; clear the flip bit to face this way
33BA: DD 77 07        LD      (IX+$07),A          
33BD: DD 35 0E        DEC     (IX+$0E)            ; step the working X down one pixel

loc_33c0:
33C0: CD 09 34        CALL    $3409               ; {code.stepObjectSpriteFrame} advance the sprite animation

; A short tail, guarded on board being the girder board: re-step one coordinate of the
; fire the caller pointed at, so its height settles onto the slope of the girder it is
; standing on. It reads the companion coordinate, the coordinate to be stepped and the
; record's state field, hands them to the girder-slope single-step, and stores the
; result back into the same field. On any other board it does nothing at all -- the
; caller's own field work still happens, but this step is gated.
settleFireOnGirderSlope:
33C3: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} only the girder board has a slope to settle onto
33C6: FE 01           CP      $01                 
33C8: C0              RET     NZ                  ; anywhere else this tail does nothing
33C9: DD 66 0E        LD      H,(IX+$0E)          ; the fire's X, which the slope is keyed to
33CC: DD 6E 0F        LD      L,(IX+$0F)          ; the height to be settled
33CF: DD 46 0D        LD      B,(IX+$0D)          
33D2: CD 33 23        CALL    $2333               ; {code.snapYToGirder} one step along the girder slope
33D5: DD 75 0F        LD      (IX+$0F),L          ; store the settled height back
33D8: C9              RET                         

loc_33d9:
33D9: DD 7E 07        LD      A,(IX+$07)          ; the sprite tile code
33DC: F6 80           OR      $80                 ; set the flip bit for this heading
33DE: DD 77 07        LD      (IX+$07),A          
33E1: DD 34 0E        INC     (IX+$0E)            ; step the working X up one pixel
33E4: C3 C0 33        JP      $33C0               ; {code.loc_33c0} join the animation step and the slope tail

loc_33e7:
33E7: CD 09 34        CALL    $3409               ; {code.stepObjectSpriteFrame} advance the sprite animation first
33EA: DD 7E 0D        LD      A,(IX+$0D)          ; the object's state
33ED: FE 08           CP      $08                 
33EF: C2 05 34        JP      NZ,$3405            ; {code.loc_3405} any state but 8 steps the counter up
33F2: DD 7E 14        LD      A,(IX+$14)          ; state 8: the sub-timer that paces the down-step
33F5: A7              AND     A                   
33F6: C2 01 34        JP      NZ,$3401            ; {code.loc_3401} still running -- only tick it
33F9: DD 36 14 02     LD      (IX+$14),$02        ; reload 2 -- the counter falls once in three calls
33FD: DD 35 0F        DEC     (IX+$0F)            ; and step the counter down
3400: C9              RET                         

loc_3401:
3401: DD 35 14        DEC     (IX+$14)            ; tick the sub-timer
3404: C9              RET                         

loc_3405:
3405: DD 34 0F        INC     (IX+$0F)            ; step the counter up
3408: C9              RET                         

; Advance an object's animation sprite tile on a period-3 timer. A per-object
; down-counter at record byte +0x15 counts every call, and while it is still running the
; routine only ticks it down and stops. When it reaches 0 it is reloaded to 2 and the
; object's sprite code at +0x07 is stepped forward by one; that path returns WITHOUT also
; decrementing, so the counter runs 0 -> 2 -> 1 -> 0 and the sprite advances once every
; three calls, not every other one. On the steps whose sprite code comes up with an all-ones low
; nibble, once every sixteen, bit 1 of the code is TOGGLED; because the nibble is all
; ones at that point the bit is set, so the toggle clears it -- a flip, not a blind set.
; Which object this services is not established here.
stepObjectSpriteFrame:
3409: DD 7E 15        LD      A,(IX+$15)          ; the per-object animation down-counter
340C: A7              AND     A                   
340D: C2 28 34        JP      NZ,$3428            ; {code.loc_3428} still counting -- the sprite holds this frame
3410: DD 36 15 02     LD      (IX+$15),$02        ; reload 2 -- the sprite steps once in three calls
3414: DD 34 07        INC     (IX+$07)            ; step the sprite tile code on one frame
3417: DD 7E 07        LD      A,(IX+$07)          
341A: E6 0F           AND     $0F                 
341C: FE 0F           CP      $0F                 ; only the all-ones low nibble carries on
341E: C0              RET     NZ                  
341F: DD 7E 07        LD      A,(IX+$07)          
3422: EE 02           XOR     $02                 ; once every sixteen steps, clear bit 1 of the code
3424: DD 77 07        LD      (IX+$07),A          
3427: C9              RET                         

loc_3428:
3428: DD 35 15        DEC     (IX+$15)            ; tick the animation counter down
342B: C9              RET                         

loc_342c:
342C: DD 6E 1A        LD      L,(IX+$1A)          ; the saved walk pointer, low byte
342F: DD 66 1B        LD      H,(IX+$1B)          ; and high
3432: AF              XOR     A                   
3433: 01 00 00        LD      BC,$0000            
3436: ED 4A           ADC     HL,BC               ; test the saved pointer for zero
3438: C2 42 34        JP      NZ,$3442            ; {code.loc_3442} non-zero -- resume where the last pass stopped
343B: 21 8C 3A        LD      HL,$3A8C            ; a fresh walk: the start of the path table
343E: DD 36 03 26     LD      (IX+$03),$26        ; and stamp the object's starting X

loc_3442:
3442: DD 34 03        INC     (IX+$03)            ; march the X one step this frame

loc_3445:
3445: 7E              LD      A,(HL)              ; the next entry of the path table
3446: FE AA           CP      $AA                 
3448: CA 56 34        JP      Z,$3456             ; {code.loc_3456} the end-of-table marker finishes the walk
344B: DD 77 05        LD      (IX+$05),A          ; an ordinary entry becomes the object's Y
344E: 23              INC     HL                  
344F: DD 75 1A        LD      (IX+$1A),L          ; save the advanced pointer for the next pass
3452: DD 74 1B        LD      (IX+$1B),H          
3455: C9              RET                         

loc_3456:
3456: AF              XOR     A                   
3457: DD 77 13        LD      (IX+$13),A          ; walk finished: clear the animation-state bytes
345A: DD 77 18        LD      (IX+$18),A          
345D: DD 77 0D        LD      (IX+$0D),A          
3460: DD 77 1C        LD      (IX+$1C),A          
3463: DD 7E 03        LD      A,(IX+$03)          
3466: DD 77 0E        LD      (IX+$0E),A          ; latch the final X
3469: DD 7E 05        LD      A,(IX+$05)          
346C: DD 77 0F        LD      (IX+$0F),A          ; and the final Y
346F: DD 36 1A 00     LD      (IX+$1A),$00        ; rewind the pointer -- the next pass reads as fresh
3473: DD 36 1B 00     LD      (IX+$1B),$00        
3477: C9              RET                         

loc_3478:
3478: DD 6E 1A        LD      L,(IX+$1A)          ; the saved walk pointer, low byte
347B: DD 66 1B        LD      H,(IX+$1B)          ; and high
347E: AF              XOR     A                   
347F: 01 00 00        LD      BC,$0000            
3482: ED 4A           ADC     HL,BC               ; test it for zero
3484: C2 9A 34        JP      NZ,$349A            ; {code.loc_349a} already walking -- keep the direction it chose
3487: 21 AC 3A        LD      HL,$3AAC            ; a fresh walk: this twin's own path table
348A: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} the context byte the direction comes from
348D: CB 7F           BIT     7,A                 
348F: CA A8 34        JP      Z,$34A8             ; {code.loc_34a8}
3492: DD 36 0D 01     LD      (IX+$0D),$01        ; bit set: mark the walk forward
3496: DD 36 03 7E     LD      (IX+$03),$7E        ; and seed the X it starts from

loc_349a:
349A: DD 7E 0D        LD      A,(IX+$0D)          ; the direction mark
349D: FE 01           CP      $01                 
349F: C2 B3 34        JP      NZ,$34B3            ; {code.loc_34b3}
34A2: DD 34 03        INC     (IX+$03)            ; forward -- march the X up
34A5: C3 45 34        JP      $3445               ; {code.loc_3445} the shared tail supplies the Y

loc_34a8:
34A8: DD 36 0D 02     LD      (IX+$0D),$02        ; bit clear: mark the walk backward
34AC: DD 36 03 80     LD      (IX+$03),$80        ; with the other starting X
34B0: C3 9A 34        JP      $349A               ; {code.loc_349a}

loc_34b3:
34B3: DD 35 03        DEC     (IX+$03)            ; backward -- march the X down
34B6: C3 45 34        JP      $3445               ; {code.loc_3445}

loc_34b9:
34B9: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227}
34BC: FE 03           CP      $03                 
34BE: C8              RET     Z                   ; 75m seeds nothing here
34BF: 3A 03 62        LD      A,($6203)           ; {hard.workRam+203} Mario's screen half picks the template
34C2: CB 7F           BIT     7,A                 
34C4: C2 ED 34        JP      NZ,$34ED            ; {code.loc_34ed}
34C7: 21 C4 3A        LD      HL,$3AC4            ; the template table for one half

loc_34ca:
34CA: 06 00           LD      B,$00               
34CC: 3A 19 60        LD      A,($6019)           ; {hard.workRam+19} the spin counter picks one of its four entries
34CF: E6 06           AND     $06                 
34D1: 4F              LD      C,A                 
34D2: 09              ADD     HL,BC               ; index the two-byte entry
34D3: 7E              LD      A,(HL)              
34D4: DD 77 03        LD      (IX+$03),A          ; stamp it as the object's X
34D7: DD 77 0E        LD      (IX+$0E),A          ; and into the working X beside it
34DA: 23              INC     HL                  
34DB: 7E              LD      A,(HL)              
34DC: DD 77 05        LD      (IX+$05),A          ; the second byte is the object's Y
34DF: DD 77 0F        LD      (IX+$0F),A          ; and its working Y
34E2: AF              XOR     A                   
34E3: DD 77 0D        LD      (IX+$0D),A          ; clear the state
34E6: DD 77 18        LD      (IX+$18),A          ; and the two trailing fields
34E9: DD 77 1C        LD      (IX+$1C),A          
34EC: C9              RET                         

loc_34ed:
34ED: 21 D4 3A        LD      HL,$3AD4            ; the other half's template table
34F0: C3 CA 34        JP      $34CA               ; {code.loc_34ca}

; Publish the five records of objArray64 into five 4-byte sprite records in the shadow
; buffer. For each record whose occupancy flag is non-zero it copies four fields in a
; fixed order -- X to +0, sprite code to +1, attribute to +2, Y to +3 -- which is the
; object-to-sprite mapping used across this game. The occupancy flag itself is not
; copied. An EMPTY record is skipped but STILL consumes a destination record, so
; destinations stay aligned one-to-one with sources: five objects always produce five
; destination records, and an empty one simply leaves its four bytes untouched. The
; destination sits inside spriteBuffer, the block the DMA copies into sprite RAM every
; vblank, so these twenty bytes are what the video hardware reads.
publishFireSprites:
34F3: 21 00 64        LD      HL,$6400            ; the first of the five fire records
34F6: 11 D0 69        LD      DE,$69D0            ; and the five sprite records they publish into
34F9: 06 05           LD      B,$05               

loc_34fb:
34FB: 7E              LD      A,(HL)              ; the record's occupancy flag
34FC: A7              AND     A                   
34FD: CA 1E 35        JP      Z,$351E             ; {code.loc_351e} empty -- its destination is left untouched
3500: 2C              INC     L                   
3501: 2C              INC     L                   
3502: 2C              INC     L                   ; step to the record's X field
3503: 7E              LD      A,(HL)              
3504: 12              LD      (DE),A              ; X into the sprite record's first byte
3505: 3E 04           LD      A,$04               ; plus four lands on the record's sprite tile code
3507: 85              ADD     A,L                 
3508: 6F              LD      L,A                 
3509: 1C              INC     E                   
350A: 7E              LD      A,(HL)              
350B: 12              LD      (DE),A              ; the tile code
350C: 2C              INC     L                   
350D: 1C              INC     E                   
350E: 7E              LD      A,(HL)              
350F: 12              LD      (DE),A              ; the attribute byte
3510: 2D              DEC     L                   
3511: 2D              DEC     L                   
3512: 2D              DEC     L                   ; back to the record's Y field
3513: 1C              INC     E                   
3514: 7E              LD      A,(HL)              
3515: 12              LD      (DE),A              ; and the Y
3516: 13              INC     DE                  ; on to the next sprite record

loc_3517:
3517: 3E 1B           LD      A,$1B               ; and on from the Y field to the next fire record
3519: 85              ADD     A,L                 
351A: 6F              LD      L,A                 
351B: 10 DE           DJNZ    $34FB               ; {code.loc_34fb}
351D: C9              RET                         

loc_351e:
351E: 3E 05           LD      A,$05               ; empty record: step the source past it
3520: 85              ADD     A,L                 
3521: 6F              LD      L,A                 
3522: 3E 04           LD      A,$04               ; and the destination on by one sprite record
3524: 83              ADD     A,E                 
3525: 5F              LD      E,A                 
3526: C3 17 35        JP      $3517               ; {code.loc_3517}

; ---- $3529-$3E6F: data ----
3529: 00 00 00 00 01 00 00 02 00 00 03 00 00 04 00 00
3539: 05 00 00 06 00 00 07 00 00 08 00 00 09 00 00 00
3549: 00 00 10 00 00 20 00 00 30 00 00 40 00 00 50 00
3559: 00 60 00 00 70 00 00 80 00 00 90 00 94 77 01 23
3569: 24 10 10 00 00 07 06 05 00 10 10 10 10 10 10 10
3579: 10 10 10 10 10 10 10 3F 00 50 76 00 F4 76 96 77
3589: 02 1E 14 10 10 00 00 06 01 00 00 10 10 10 10 10
3599: 10 10 10 10 10 10 10 10 10 3F 00 00 61 00 F6 76
35A9: 98 77 03 22 14 10 10 00 00 05 09 05 00 10 10 10
35B9: 10 10 10 10 10 10 10 10 10 10 10 3F 00 50 59 00
35C9: F8 76 9A 77 04 24 18 10 10 00 00 05 00 05 00 10
35D9: 10 10 10 10 10 10 10 10 10 10 10 10 10 3F 00 50
35E9: 50 00 FA 76 9C 77 05 24 18 10 10 00 00 04 03 00
35F9: 00 10 10 10 10 10 10 10 10 10 10 10 10 10 10 3F
3609: 00 00 43 00 FC 76 3B 5C 4B 5C 5B 5C 6B 5C 7B 5C
3619: 8B 5C 9B 5C AB 5C BB 5C CB 5C 3B 6C 4B 6C 5B 6C
3629: 6B 6C 7B 6C 8B 6C 9B 6C AB 6C BB 6C CB 6C 3B 7C
3639: 4B 7C 5B 7C 6B 7C 7B 7C 8B 7C 9B 7C AB 7C BB 7C
3649: CB 7C 8B 36 01 00 98 36 A5 36 B2 36 BF 36 06 00
3659: CC 36 08 00 E6 36 FD 36 0B 00 15 37 1C 37 30 37
3669: 38 37 47 37 5D 37 73 37 8B 37 00 61 22 61 44 61
3679: 66 61 88 61 9E 37 B6 37 D2 37 E1 37 1D 00 00 3F
3689: 09 3F 96 76 17 11 1D 15 10 10 1F 26 15 22 3F 94
3699: 76 20 1C 11 29 15 22 10 30 32 31 3F 94 76 20 1C
36A9: 11 29 15 22 10 30 33 31 3F 80 76 18 19 17 18 10
36B9: 23 13 1F 22 15 3F 9F 75 13 22 15 14 19 24 10 10
36C9: 10 10 3F 5E 77 18 1F 27 10 18 19 17 18 10 13 11
36D9: 1E 10 29 1F 25 10 17 15 24 10 FB 10 3F 29 77 1F
36E9: 1E 1C 29 10 01 10 20 1C 11 29 15 22 10 12 25 24
36F9: 24 1F 1E 3F 29 77 01 10 1F 22 10 02 10 20 1C 11
3709: 29 15 22 23 10 12 25 24 24 1F 1E 3F 27 76 20 25
3719: 23 18 3F 06 77 1E 11 1D 15 10 22 15 17 19 23 24
3729: 22 11 24 19 1F 1E 3F 88 76 1E 11 1D 15 2E 3F E9
3739: 75 2D 2D 2D 10 10 10 10 10 10 10 10 10 3F 0B 77
3749: 11 10 12 10 13 10 14 10 15 10 16 10 17 10 18 10
3759: 19 10 1A 3F 0D 77 1B 10 1C 10 1D 10 1E 10 1F 10
3769: 20 10 21 10 22 10 23 10 24 3F 0F 77 25 10 26 10
3779: 27 10 28 10 29 10 2A 10 2B 10 2C 44 45 46 47 48
3789: 10 3F F2 76 22 15 17 19 10 24 19 1D 15 10 10 30
3799: 03 00 31 10 3F 92 77 22 11 1E 1B 10 10 23 13 1F
37A9: 22 15 10 10 1E 11 1D 15 10 10 10 10 3F 72 77 29
37B9: 1F 25 22 10 1E 11 1D 15 10 27 11 23 10 22 15 17
37C9: 19 23 24 15 22 15 14 42 3F A7 76 19 1E 23 15 22
37D9: 24 10 13 1F 19 1E 10 3F 0A 77 10 10 20 1C 11 29
37E9: 15 22 10 10 10 10 13 1F 19 1E 3F FC 76 49 4A 10
37F9: 1E 19 1E 24 15 1E 14 1F 10 10 10 10 3F 7C 75 01
3809: 09 08 01 3F 02 97 38 68 38 02 DF 54 10 54 02 EF
3819: 6D 20 6D 02 DF 8E 10 8E 02 EF AF 20 AF 02 DF D0
3829: 10 D0 02 EF F1 10 F1 00 53 18 53 54 00 63 18 63
3839: 54 00 93 38 93 54 00 83 54 83 F1 00 93 54 93 F1
3849: AA 8D 7D 8C 6F 00 7C 6E 00 7C 6D 00 7C 6C 00 7C
3859: 8F 7F 8E 47 27 08 50 2F A7 08 50 3B 25 08 50 00
3869: 70 08 48 3B 23 07 40 46 A9 08 44 00 70 08 48 30
3879: 29 08 44 00 70 08 48 00 70 0A 48 6F 10 09 23 6F
3889: 11 0A 33 50 34 08 3C 00 35 08 3C 53 32 08 40 63
3899: 33 08 40 00 70 08 48 53 36 08 50 63 37 08 50 6B
38A9: 31 08 41 00 70 08 48 6A 14 0A 48 FD FD FD FD FD
38B9: FD FD FE FE FE FE FE FE FF FF FF FF 00 00 01 01
38C9: 01 7F FF FF FF FF FF 00 FF 00 00 01 00 01 01 01
38D9: 01 01 7F 04 7F F0 10 F0 02 DF F2 70 F8 02 6F F8
38E9: 10 F8 AA 04 DF D0 90 D0 02 DF DC 20 D1 AA FF FF
38F9: FF FF FF 04 DF A8 20 A8 04 5F B0 20 B0 02 DF B0
3909: 20 BB AA 04 DF 88 30 88 04 DF 90 B0 90 02 DF 9A
3919: 20 8F AA 04 BF 68 20 68 04 3F 70 20 70 02 DF 6E
3929: 20 79 AA 02 DF 58 A0 55 AA 00 70 08 44 2B AC 08
3939: 4C 3B AE 08 4C 3B AF 08 3C 4B B0 07 3C 4B AD 08
3949: 4C 00 70 08 44 00 70 08 44 00 70 08 44 00 70 0A
3959: 44 47 27 08 4C 2F A7 08 4C 3B 25 08 4C 00 70 08
3969: 44 3B 23 07 3C 4B 2A 08 3C 4B 2B 08 4C 2B AA 08
3979: 3C 2B AB 08 4C 00 70 0A 44 00 70 08 44 4B 2C 08
3989: 4C 3B 2E 08 4C 3B 2F 08 3C 2B 30 07 3C 2B 2D 08
3999: 4C 00 70 08 44 00 70 08 44 00 70 08 44 00 70 0A
39A9: 44 FD FD FD FE FE FE FE FF FF 00 FF 00 00 01 00
39B9: 01 01 02 02 02 02 03 03 03 7F 1E 4E BB 4C D8 4E
39C9: 59 4E 7F BB 4D 7F 47 27 08 50 2D 26 08 50 3B 25
39D9: 08 50 00 70 08 48 3B 24 07 40 4B 28 08 40 00 70
39E9: 08 48 30 29 08 44 00 70 08 48 00 70 0A 48 49 A6
39F9: 08 50 2F A7 08 50 3B 25 08 50 00 70 08 48 3B 24
3A09: 07 40 46 A9 08 44 00 70 08 48 2B A8 08 40 00 70
3A19: 08 48 00 70 0A 48 73 A7 88 60 8B 27 88 60 7F 25
3A29: 88 60 00 70 88 68 7F 24 87 70 74 29 88 6C 00 70
3A39: 88 68 8A A9 88 6C 00 70 88 68 00 70 8A 68 05 AF
3A49: F0 50 F0 AA 05 AF E8 50 E8 AA 05 AF E0 50 E0 AA
3A59: 05 AF D8 50 D8 AA 05 B7 58 48 58 AA 01 04 01 03
3A69: 04 01 02 03 04 01 02 01 03 04 01 02 01 03 01 04
3A79: 7F FF 00 FF FF FE FE FE FE FE FE FE FE FE FE FE
3A89: FF FF 00 E8 E5 E3 E2 E1 E0 DF DE DD DD DC DC DC
3A99: DC DC DC DD DD DE DF E0 E1 E2 E3 E4 E5 E7 E9 EB
3AA9: ED F0 AA 80 7B 78 76 74 73 72 71 70 70 6F 6F 6F
3AB9: 70 70 71 72 73 74 75 76 77 78 AA EE F0 DB A0 E6
3AC9: C8 D6 78 EB F0 DB A0 E6 C8 E6 C8 1B C8 23 A0 2B
3AD9: 78 12 F0 1B C8 23 A0 12 F0 1B C8 02 97 38 68 38
3AE9: 02 9F 54 10 54 02 DF 58 A0 55 02 EF 6D 20 79 02
3AF9: DF 9A 10 8E 02 EF AF 20 BB 02 DF DC 10 D0 02 FF
3B09: F0 80 F7 02 7F F8 00 F8 00 CB 57 CB 6F 00 CB 99
3B19: CB B1 00 CB DB CB F3 00 63 18 63 54 01 63 D5 63
3B29: F8 00 33 78 33 90 00 33 BA 33 D2 00 53 18 53 54
3B39: 01 53 92 53 B8 00 5B 76 5B 92 00 73 B6 73 D6 00
3B49: 83 95 83 B5 00 93 38 93 54 01 BB 70 BB 98 01 6B
3B59: 54 6B 75 AA 06 8F 90 70 90 06 8F 98 70 98 06 8F
3B69: A0 70 A0 00 63 18 63 58 00 63 80 63 A8 00 63 D0
3B79: 63 F8 00 53 18 53 58 00 53 A8 53 D0 00 9B 80 9B
3B89: A8 00 9B D0 9B F8 01 23 58 23 80 01 DB 58 DB 80
3B99: 00 2B 80 2B A8 00 D3 80 D3 A8 00 A3 A8 A3 D0 00
3BA9: 2B D0 2B F8 00 D3 D0 D3 F8 00 93 38 93 58 02 97
3BB9: 38 68 38 03 EF 58 10 58 03 F7 80 88 80 03 77 80
3BC9: 08 80 02 A7 A8 50 A8 02 E7 A8 B8 A8 02 3F A8 18
3BD9: A8 03 EF D0 10 D0 02 EF F8 10 F8 AA 00 63 18 63
3BE9: 58 00 63 88 63 D0 00 53 18 53 58 00 53 88 53 D0
3BF9: 00 E3 68 E3 90 00 E3 B8 E3 D0 00 CB 90 CB B0 00
3C09: B3 58 B3 78 00 9B 80 9B A0 00 93 38 93 58 00 23
3C19: 88 23 C0 00 1B C0 1B E8 02 97 38 68 38 02 B7 58
3C29: 10 58 02 EF 68 E0 68 02 D7 70 C8 70 02 BF 78 B0
3C39: 78 02 A7 80 90 80 02 67 88 48 88 02 27 88 10 88
3C49: 02 EF 90 C8 90 02 A7 A0 98 A0 02 BF A8 B0 A8 02
3C59: D7 B0 C8 B0 02 EF B8 E0 B8 02 27 C0 10 C0 02 EF
3C69: D0 D8 D0 02 67 D0 50 D0 02 CF D8 C0 D8 02 B7 E0
3C79: A8 E0 02 9F E8 88 E8 02 27 E8 10 E8 02 EF F8 10
3C89: F8 AA 00 7B 80 7B A8 00 7B D0 7B F8 00 33 58 33
3C99: 80 00 53 58 53 80 00 AB 58 AB 80 00 CB 58 CB 80
3CA9: 00 2B 80 2B A8 00 D3 80 D3 A8 00 23 A8 23 D0 00
3CB9: 5B A8 5B D0 00 A3 A8 A3 D0 00 DB A8 DB D0 00 1B
3CC9: D0 1B F8 00 E3 D0 E3 F8 05 B7 30 48 30 05 CF 58
3CD9: 30 58 05 D7 80 28 80 05 DF A8 20 A8 05 E7 D0 18
3CE9: D0 05 EF F8 10 F8 AA 10 82 85 8B 10 85 80 8B 10
3CF9: 87 85 8B 81 80 80 8B 81 82 85 8B 81 85 80 8B 05
3D09: 88 77 01 68 77 01 6C 77 03 49 77 05 08 77 01 E8
3D19: 76 01 EC 76 05 C8 76 05 88 76 02 69 76 02 4A 76
3D29: 05 28 76 05 E8 75 01 CA 75 03 A9 75 01 88 75 01
3D39: 8C 75 05 48 75 01 28 75 01 2A 75 01 2C 75 01 08
3D49: 75 01 0A 75 01 0C 75 03 C8 74 03 AA 74 03 88 74
3D59: 05 2F 77 05 0F 77 02 F0 76 02 CF 76 02 D2 76 05
3D69: 8F 76 05 6F 76 01 4F 76 01 53 76 05 2F 76 05 EF
3D79: 75 02 D0 75 02 B1 75 05 8F 75 03 50 75 05 2F 75
3D89: 01 0F 75 01 13 75 01 EF 74 01 F1 74 01 F3 74 02
3D99: D1 74 00 00 00 23 68 01 11 00 00 00 10 DB 68 01
3DA9: 40 00 00 08 01 01 01 01 01 01 01 01 01 00 00 00
3DB9: 00 00 00 80 01 C0 FF 01 FF FF 34 C3 39 00 67 80
3DC9: 69 1A 01 00 00 00 00 00 00 00 00 04 00 10 00 00
3DD9: 00 00 00 1E 18 0B 4B 14 18 0B 4B 1E 18 0B 3B 14
3DE9: 18 0B 3B 3D 01 03 02 4D 01 04 01 27 70 01 E0 00
3DF9: 00 7F 40 01 78 02 00 27 49 0C F0 7F 49 0C 88 1E
3E09: 07 03 09 24 64 BB C0 23 8D 7B B4 1B 8C 7C 64 4B
3E19: 0E 04 02 23 46 03 68 DB 46 03 68 17 50 00 5C E7
3E29: D0 00 5C 8C 50 00 84 73 D0 00 84 17 50 00 D4 E7
3E39: D0 00 D4 53 73 0A A0 8B 74 0A F0 DB 75 0A A0 5B
3E49: 73 0A C8 E3 74 0A 60 1B 75 0A 80 DB 73 0A C8 93
3E59: 74 0A F0 33 75 0A 50 44 03 08 04 37 F4 37 C0 37
3E69: 8C 77 70 77 A4 77 D8

; Pick one of three score-popup awards from the low bits of the accumulator -- the "how
; many did he jump over at once" tier. It is reached with the overlap thermometer already
; shifted right once, and is a small first-clear-bit-wins encoder: bit 0 clear takes task
; argument 1 and sprite code 0x7B; else bit 1 clear takes argument 3 and code 0x7D; else
; argument 5 and code 0x7F. Against the score table those three arguments are 100, 300
; and 500 points. It then tail-jumps into the shared stamp, which enqueues the task,
; stamps a 4-byte sprite record anchored on Mario's position, and cues a board-gated
; sound.
pickAwardTierByObjectCount:
3E70: 11 01 00        LD      DE,$0001            ; the 100-point award: task argument 1
3E73: 06 7B           LD      B,$7B               ; and the glyph the popup shows
3E75: 1F              RRA                         ; shift the next bit of the overlap tally out
3E76: D2 28 1E        JP      NC,$1E28            ; {code.awardScorePopup} bit clear -- a single overlap, award 100
3E79: 1E 03           LD      E,$03               ; argument 3 -- the 300-point award
3E7B: 06 7D           LD      B,$7D               ; its glyph
3E7D: 1F              RRA                         
3E7E: D2 28 1E        JP      NC,$1E28            ; {code.awardScorePopup} two at once -- award 300
3E81: 1E 05           LD      E,$05               ; argument 5 -- the 500-point award
3E83: 06 7F           LD      B,$7F               ; its glyph
3E85: C3 28 1E        JP      $1E28               ; {code.awardScorePopup} three or more at once -- award 500

; Vector to the current board's collision-search arm, handing it the caller's bounds
; word across the dispatch. It reads board and vectors through a six-entry inline table:
; entries 0 and 5 are reset-vector guards for an out-of-range board; 2, 3 and 4 are
; those boards' collision arms; and 1, the 25m arm, COUNTS object overlaps rather than
; running the plain girder collision, which is what makes this dispatch worth having as
; its own routine. THE BOUNDS WORD IS HANDED OVER THROUGH THE STACK, not a register: the
; shared dispatch trampoline clobbers the register pair while it recovers its own table
; base, so the word is stacked first and the arm's opening move lifts it back off as its
; collision bounds. That hand-off is genuine data, not call plumbing -- dropping it
; feeds the arm a garbage bounds word.
dispatchBoardOverlapSearch:
3E88: 3A 27 62        LD      A,($6227)           ; {hard.workRam+227} the board picks the collision arm
3E8B: E5              PUSH    HL                  ; stack the caller's bounds word -- the arm lifts it back
3E8C: EF              RST     $28                 ; vector through the table that follows

; ---- $3E8D-$3E98: jump table ----
3E8D: 00 00 99 3E B0 28 E0 28 01 29 00 00

loc_3e99:
3E99: E1              POP     HL                  ; lift the bounds word: the search window
3E9A: AF              XOR     A                   
3E9B: 32 60 60        LD      ($6060),A           ; {hard.workRam+60} both scans share one tally
3E9E: 06 0A           LD      B,$0A               ; ten barrel records
3EA0: 11 20 00        LD      DE,$0020            ; the stride between them
3EA3: DD 21 00 67     LD      IX,$6700            ; the barrel array
3EA7: CD C3 3E        CALL    $3EC3               ; {code.countObjectOverlaps} count the ones crowding the probe

loc_3eaa:
3EAA: 06 05           LD      B,$05               ; then the five fire records
3EAC: DD 21 00 64     LD      IX,$6400            
3EB0: CD C3 3E        CALL    $3EC3               ; {code.countObjectOverlaps} add them to the same tally
3EB3: 3A 60 60        LD      A,($6060)           ; {hard.workRam+60} the total across both arrays
3EB6: A7              AND     A                   
3EB7: C8              RET     Z                   ; nothing near him -- code 0
3EB8: FE 01           CP      $01                 
3EBA: C8              RET     Z                   ; exactly one -- code 1
3EBB: FE 03           CP      $03                 ; is the total under three?
3EBD: 3E 03           LD      A,$03               ; two -- code 3, two bits of the thermometer
3EBF: D8              RET     C                   
3EC0: 3E 07           LD      A,$07               ; three or more -- code 7, the top of the scale
3EC2: C9              RET                         

; Count how many objects in an array overlap a probe point, within a per-object
; rectangular window. Walks a run of fixed-stride records, skipping any whose field +0
; has bit 0 clear. For an active record:
;   first axis:  |probeA - record+5| + 1 must be under the first threshold, or past that
;                still under the record's own window at +0x0a;
;   second axis: tried only if the first overlapped -- |probe+3 - record+3| must be
;                under the second threshold, or past it under the record's window at +9.
; Both axes overlapping bumps overlapCount. The caller clears that counter first and
; reads it back afterwards as an overlap-severity code, so the counter is this routine's
; only observable effect. Each distance is the subtract-then-negate-on-borrow idiom,
; byte-wide, so the unsigned distance falls out without a signed compare. A count of 0
; scans 256 records.
countObjectOverlaps:
3EC3: DD CB 00 46     BIT     0,(IX+$00)          ; the record's active flag
3EC7: CA FA 3E        JP      Z,$3EFA             ; {code.loc_3efa} inactive -- nothing to test
3ECA: 79              LD      A,C                 ; the probe's first-axis coordinate
3ECB: DD 96 05        SUB     (IX+$05)            ; distance from the record's own position
3ECE: D2 D3 3E        JP      NC,$3ED3            ; {code.loc_3ed3}
3ED1: ED 44           NEG                         ; negate on borrow -- the unsigned distance

loc_3ed3:
3ED3: 3C              INC     A                   ; the test is written on distance plus one
3ED4: 95              SUB     L                   ; against the caller's window on this axis
3ED5: DA DE 3E        JP      C,$3EDE             ; {code.loc_3ede} inside it -- try the second axis
3ED8: DD 96 0A        SUB     (IX+$0A)            ; past it: try the record's own extent
3EDB: D2 FA 3E        JP      NC,$3EFA            ; {code.loc_3efa} outside that too -- this record misses

loc_3ede:
3EDE: FD 7E 03        LD      A,(IY+$03)          ; the probe's second-axis coordinate
3EE1: DD 96 03        SUB     (IX+$03)            ; distance from the record's
3EE4: D2 E9 3E        JP      NC,$3EE9            ; {code.loc_3ee9}
3EE7: ED 44           NEG                         ; unsigned distance again

loc_3ee9:
3EE9: 94              SUB     H                   ; against the caller's window on this axis
3EEA: DA F3 3E        JP      C,$3EF3             ; {code.loc_3ef3} inside it -- both axes overlap
3EED: DD 96 09        SUB     (IX+$09)            ; past it: the record's own extent
3EF0: D2 FA 3E        JP      NC,$3EFA            ; {code.loc_3efa} outside -- no overlap

loc_3ef3:
3EF3: 3A 60 60        LD      A,($6060)           ; {hard.workRam+60}
3EF6: 3C              INC     A                   
3EF7: 32 60 60        LD      ($6060),A           ; {hard.workRam+60} both axes overlapped -- tally this object

loc_3efa:
3EFA: DD 19           ADD     IX,DE               ; on to the next record
3EFC: 10 C5           DJNZ    $3EC3               ; {code.countObjectOverlaps}
3EFE: C9              RET                         

; ---- $3EFF-$3F23: data ----
3EFF: 00 5C 76 49 4A 01 09 08 01 3F 7D 77 1E 19 1E 24
3F0F: 15 1E 14 1F 10 1F 16 10 11 1D 15 22 19 13 11 10
3F1F: 19 1E 13 2B 3F

; Paint a fixed two-tile decoration into the tilemap: tile code 0x9F into one video-RAM
; cell and 0x9E into the cell 0x20 lower in address, unconditionally. The two are one
; screen row apart and the lower-addressed one sits BELOW the other, so the pair is a
; two-tall glyph stamped at a fixed spot. No inputs at all -- it reads no register and no
; memory. A leaf.
stampFixedTilePair:
3F24: 21 AF 74        LD      HL,$74AF            ; the upper cell of the two-tall glyph
3F27: 11 E0 FF        LD      DE,$FFE0            ; minus one screen row
3F2A: 36 9F           LD      (HL),$9F            ; paint the top tile
3F2C: 19              ADD     HL,DE               ; step to the cell below it on screen
3F2D: 36 9E           LD      (HL),$9E            ; and the bottom tile
3F2F: C9              RET                         

; ---- $3F30-$3F9F: data ----
3F30: 50 52 4F 47 52 41 4D 2C 57 45 20 57 4F 55 4C 44
3F40: 20 54 45 41 43 48 20 59 4F 55 2E 2A 2A 2A 2A 2A
3F50: 54 45 4C 2E 54 4F 4B 59 4F 2D 4A 41 50 41 4E 20
3F60: 30 34 34 28 32 34 34 29 32 31 35 31 20 20 20 20
3F70: 45 58 54 45 4E 54 49 4F 4E 20 33 30 34 20 20 20
3F80: 53 59 53 54 45 4D 20 44 45 53 49 47 4E 20 20 20
3F90: 49 4B 45 47 41 4D 49 20 43 4F 2E 20 4C 49 4D 2E

loc_3fa0:
3FA0: CD A6 3F        CALL    $3FA6               ; {code.stamp50mBoardTiles} 50m only; nothing stamped elsewhere
3FA3: C3 5F 0D        JP      $0D5F               ; {code.loc_0d5f} then the common board-setup continuation

; During board setup, stamp four tilemap cells -- but only on the 50m conveyor board. It
; is reached unconditionally from every board's setup pass, and its first act is the
; per-board gate with the mask 0x02, which opens only when the current board is 2; off
; 50m it writes nothing at all. On 50m it stamps a fixed two-tile motif into two
; video-RAM cell pairs, tile 0x10 then tile 0xC0 in each pair. The two cells of a pair
; are two bytes apart because tilemap columns are stride 2 in this address layout. Every
; stored value is a constant.
stamp50mBoardTiles:
3FA6: 3E 02           LD      A,$02               ; mask bit 1 -- the 50m conveyor board
3FA8: F7              RST     $30                 ; off 50m the gate closes and nothing is stamped
3FA9: 06 02           LD      B,$02               ; two cell pairs to stamp
3FAB: 21 6C 77        LD      HL,$776C            ; the first pair

loc_3fae:
3FAE: 36 10           LD      (HL),$10            ; the first tile of the motif
3FB0: 23              INC     HL                  
3FB1: 23              INC     HL                  ; tilemap columns are two bytes apart here
3FB2: 36 C0           LD      (HL),$C0            ; and the second tile
3FB4: 21 8C 74        LD      HL,$748C            ; the second pair, loaded inside the loop
3FB7: 10 F5           DJNZ    $3FAE               ; {code.loc_3fae}
3FB9: C9              RET                         

; ---- $3FBA-$3FBF: data ----
3FBA: 00 00 00 00 00 00

; Force the CODE byte of marioSpriteRecord to a fixed value of 3, and hand back a
; pointer to that record's Y field. Mario's sprite code packs a horizontal-mirror flag
; in the top bit and an animation code in the low bits, so a bare 3 is one of the
; climb-frame codes with the mirror flag cleared: it pins one specific climb pose
; whatever the byte held before. The attribute byte in between is deliberately stepped
; over and never written, and the returned pointer is consumed on the very next step. It
; claims no direction -- nothing here moves Mario, and whether the climb is up or down
; was decided before the call.
pinMarioClimbPose:
3FC0: 21 4D 69        LD      HL,$694D            ; the code byte of Mario's sprite record
3FC3: 36 03           LD      (HL),$03            ; pin one climb pose, mirror flag clear
3FC5: 2C              INC     L                   ; step over the attribute byte, left untouched
3FC6: 2C              INC     L                   ; leaving a pointer to the record's Y field
3FC7: C9              RET                         

; ---- $3FC8-$3FFF: data ----
3FC8: 00 00 41 7F 7F 41 00 00 00 7F 7F 18 3C 76 63 41
3FD8: 00 00 7F 7F 49 49 49 41 00 1C 3E 63 41 49 79 79
3FE8: 00 7C 7E 13 11 13 7E 7C 00 7F 7F 0E 1C 0E 7F 7F
3FF8: 00 00 41 7F 7F 41 00 00
```

