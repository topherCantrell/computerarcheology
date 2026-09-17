![Centipede](centiped.jpg)

# Centipede

>>> cpu 6502

>>> binary 2000:roms/136001-307.d1 + roms/136001-308.e1 + roms/136001-309.fh1 + roms/136001-310.j1

>>> memoryTable hard

[Hardware Info](Hardware.md)

>>> memoryTable ram

[RAM Usage](RAMUse.md)

```code
; Centipede (Atari, 1981).
;
; What follows is the code reached from the reset and interrupt entry points,
; shown as instructions; spans never reached appear as data (the "---- data
; ----" blocks).


; ---- $2000-$200D: data ----
2000: 4C 04 3B 1B 31 39 38 30 20 41 54 41 52 C9

loc_200e:
200E: 20 72 28        JSR     $2872               ; {code.initRoundState} call the round-setup entry to seed a fresh board's working cells
2011: 58              CLI                         ; enable interrupts so the frame heartbeat can start firing
2012: 20 5C 2D        JSR     $2D5C               ; {code.plotRecordFieldColumns} lay down the record-field scaffolding the round is played on

mainLoop:
2015: 46 8A           LSR     $8A                 ; {hard.workRam+8A} consume the frame-ready bit by shifting the heartbeat latch 0x8a
2017: 90 FC           BCC     $2015               ; {code.mainLoop} no frame yet -- block here at the top of the loop until the heartbeat lands
2019: 8D 00 20        STA     $2000               ; {hard.rom / watchdog} kick the watchdog with the sampled port value so the board isn't reset mid-frame
201C: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read input port IN0 (vblank edge and service-switch bits)
201F: 29 20           AND     #$20                ; isolate the service-switch bit (bit 5)

loc_2021:
2021: F0 FE           BEQ     $2021               ; {code.loc_2021} spin here while that bit reads clear
2023: 20 61 25        JSR     $2561               ; {code.loc_2561} run the per-frame wave/board-start service
2026: 20 68 30        JSR     $3068               ; {code.updateSoundChannels} push one frame's worth of bytes into the four POKEY channels
2029: 20 41 27        JSR     $2741               ; {code.loc_2741} run the spawn-and-move dispatcher and inspect its answer
202C: 10 E7           BPL     $2015               ; {code.mainLoop} dispatcher says skip the rest of this frame -- loop back to the heartbeat wait
202E: 20 C0 3A        JSR     $3AC0               ; {code.tickEaromWriteback} flush one pending high-score cell out to the EAROM
2031: 20 19 21        JSR     $2119               ; {code.loc_2119} run the per-frame layout and coordinate pass
2034: 20 FE 32        JSR     $32FE               ; {code.plotObjectCoordinates} render the current object coordinates as decimal
2037: 20 51 29        JSR     $2951               ; {code.beginCentipedeSegmentSweep} open the centipede segment sweep
203A: 20 FD 26        JSR     $26FD               ; {code.serviceTimerBank} age the bank of countdown timers gating periodic events
203D: 20 CE 2A        JSR     $2ACE               ; {code.loc_2ace} advance the movement sub-step accumulator for the 63 axis
2040: 20 02 22        JSR     $2202               ; {code.advanceColumnHeadingState} progress the column heading/dwell state
2043: 20 C6 2E        JSR     $2EC6               ; {code.stepHeadSegment} step the centipede head segment forward
2046: 20 D9 2B        JSR     $2BD9               ; {code.spawnActorOnTimer} release a new secondary actor when its interval timer expires
2049: 20 0B 2E        JSR     $2E0B               ; {code.steerHeadAndSeedVelocity} pick the head's heading and lay down a fresh velocity seed
204C: 20 59 20        JSR     $2059               ; {code.loc_2059} continue the per-object grid-stamp state step
204F: 20 DA 23        JSR     $23DA               ; {code.advanceDeathRespawnSequence} step the death-and-respawn state machine one tick
2052: 20 EF 2C        JSR     $2CEF               ; {code.scanForRangedCellAndSeed} walk the playfield cell stream for a ripe cell to seed
2055: 4C 15 20        JMP     $2015               ; {code.mainLoop} loop back to the top of the frame for the next heartbeat

; ---- $2058-$2058: data ----
2058: 4F

loc_2059:
2059: A5 43           LDA     $43                 ; {hard.workRam+43} read the mode/state gate 0x43
205B: 29 AF           AND     #$AF                ; mask off its mode bits
205D: D0 08           BNE     $2067               ; {code.loc_2067} mode bits set -- bail out of the object step
205F: A5 40           LDA     $40                 ; {hard.workRam+40} read the object's X-attribute cell 0x40
2061: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it against the orientation mask 0xef
2063: C9 20           CMP     #$20                ; test the folded X against its low band bound
2065: 90 01           BCC     $2068               ; {code.loc_2068} inside the band -- go run the state step

loc_2067:
2067: 60              RTS                         ; out of band -- return

loc_2068:
2068: A5 70           LDA     $70                 ; {hard.workRam+70} read the object's Y cell 0x70
206A: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it against orientation byte 0xf0
206C: C9 F8           CMP     #$F8                ; test the folded Y against the high band bound
206E: 90 20           BCC     $2090               ; {code.loc_2090} Y in range -- skip the per-slot bounds test and go to the step
2070: A6 88           LDX     $88                 ; {hard.workRam+88} load the active-object slot index 0x88
2072: B5 9A           LDA     $9A,X               ; {hard.workRam+9A} read the slot's length/phase byte from the 0x9a array
2074: C9 0C           CMP     #$0C                ; compare against the full length 0x0c
2076: B0 6B           BCS     $20E3               ; {code.loc_20e3} slot at or over full length -- bail
2078: B5 AB           LDA     $AB,X               ; {hard.workRam+AB} read the slot's gate/count byte from the 0xab array
207A: C9 02           CMP     #$02                ; compare that count against 2
207C: A0 05           LDY     #$05                ; default bound index 5
207E: 90 02           BCC     $2082               ; {code.loc_2082} count below 2 -- keep bound index 5
2080: A0 09           LDY     #$09                ; else use bound index 9

loc_2082:
2082: C9 12           CMP     #$12                ; compare the count against 0x12
2084: 90 05           BCC     $208B               ; {code.loc_208b} below 0x12 -- use the index as-is
2086: 4A              LSR     A                   ; halve the count
2087: 18              CLC                         ; clear carry for the bias add
2088: 69 06           ADC     #$06                ; bias the halved count by 6
208A: A8              TAY                         ; move the derived bound into Y

loc_208b:
208B: 98              TYA                         ; bring the bound index into A
208C: D5 D7           CMP     $D7,X               ; {hard.workRam+D7} compare it against the slot's per-column tally in the 0xd7 array
208E: 90 53           BCC     $20E3               ; {code.loc_20e3} still within the column bound -- bail

loc_2090:
2090: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter 0x00
2092: 29 03           AND     #$03                ; keep its low two bits
2094: D0 0F           BNE     $20A5               ; {code.loc_20a5} not the fourth frame -- skip the attribute cycle
2096: E6 40           INC     $40                 ; {hard.workRam+40} advance the object's X-attribute cell 0x40
2098: A5 40           LDA     $40                 ; {hard.workRam+40} read it back
209A: 18              CLC                         ; clear carry for the add
209B: 69 01           ADC     #$01                ; add one
209D: 29 03           AND     #$03                ; wrap into a two-bit phase
209F: 09 1C           ORA     #$1C                ; fold in the fixed 0x1c base
20A1: 45 EF           EOR     $EF                 ; {hard.workRam+EF} mirror the attribute for orientation
20A3: 85 40           STA     $40                 ; {hard.workRam+40} store the cycled attribute back to 0x40

loc_20a5:
20A5: A5 60           LDA     $60                 ; {hard.workRam+60} read the running velocity/limit cell 0x60
20A7: 85 8B           STA     $8B                 ; {hard.workRam+8B} stash it into scratch 0x8b
20A9: A5 70           LDA     $70                 ; {hard.workRam+70} read the object Y cell 0x70
20AB: A4 EF           LDY     $EF                 ; {hard.workRam+EF} read the orientation selector 0xef
20AD: F0 06           BEQ     $20B5               ; {code.loc_20b5} orientation zero -- take the subtract branch
20AF: 18              CLC                         ; clear carry for the add
20B0: 65 80           ADC     $80                 ; {hard.workRam+80} add the column step 0x80 to Y
20B2: 4C B8 20        JMP     $20B8               ; {code.stampGridCellAtObject} join the store

loc_20b5:
20B5: 38              SEC                         ; set carry for the subtract
20B6: E5 80           SBC     $80                 ; {hard.workRam+80} subtract the column step 0x80 from Y

stampGridCellAtObject:
20B8: 85 70           STA     $70                 ; {hard.workRam+70} store the stepped Y back into the object cell 0x70
20BA: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it against orientation 0xf0
20BC: C9 04           CMP     #$04                ; test whether it has reached the edge (below 4)
20BE: 90 24           BCC     $20E4               ; {code.loc_20e4} at the edge -- go re-seed the wave instead of stamping
20C0: A2 0C           LDX     #$0C                ; target the head slot index 0x0c
20C2: 20 96 2C        JSR     $2C96               ; {code.armSlotWhenObjectInRange} range/collision-check the object against the reference point
20C5: 90 1C           BCC     $20E3               ; {code.loc_20e3} object in range of another -- bail without stamping
20C7: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter 0x00
20C9: 29 03           AND     #$03                ; keep its low two bits
20CB: D0 16           BNE     $20E3               ; {code.loc_20e3} not the fourth frame -- bail
20CD: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
20D0: 29 03           AND     #$03                ; keep its low two bits
20D2: D0 0F           BNE     $20E3               ; {code.loc_20e3} RNG gate fails -- bail
20D4: A9 04           LDA     #$04                ; base column code 4
20D6: 45 F3           EOR     $F3                 ; {hard.workRam+F3} fold it for orientation through 0xf3
20D8: 18              CLC                         ; clear carry for the add
20D9: 65 70           ADC     $70                 ; {hard.workRam+70} add the object's Y to form the target column
20DB: A0 00           LDY     #$00                ; row 0
20DD: 20 2B 2C        JSR     $2C2B               ; {code.resolveTileCellAtXY} position the grid pointer at that cell
20E0: 20 A8 2B        JSR     $2BA8               ; {code.stampEmptyTileCell} stamp a mushroom there if the cell is empty

loc_20e3:
20E3: 60              RTS                         ; return

loc_20e4:
20E4: 20 E8 20        JSR     $20E8               ; {code.seedWaveState} object hit the edge -- re-seed the wave state
20E7: 60              RTS                         ; return

seedWaveState:
20E8: A9 1C           LDA     #$1C                ; load the fixed X seed constant 0x1c
20EA: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it against orientation 0xef
20EC: 85 40           STA     $40                 ; {hard.workRam+40} seed the object X cell 0x40
20EE: A9 F8           LDA     #$F8                ; load the fixed Y seed constant 0xf8
20F0: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it against orientation 0xf0
20F2: 85 70           STA     $70                 ; {hard.workRam+70} seed the object Y cell 0x70

loc_20f4:
20F4: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
20F7: 29 F8           AND     #$F8                ; keep the top five bits
20F9: F0 F9           BEQ     $20F4               ; {code.loc_20f4} all-zero draw -- re-roll
20FB: C9 10           CMP     #$10                ; require the value to be at least 0x10
20FD: 90 F5           BCC     $20F4               ; {code.loc_20f4} too small -- re-roll
20FF: 38              SEC                         ; set carry for the subtract
2100: E9 04           SBC     #$04                ; subtract 4 from the accepted value
2102: 85 60           STA     $60                 ; {hard.workRam+60} seed the velocity/limit cell 0x60 in its bounded band
2104: A0 03           LDY     #$03                ; default per-wave count 3
2106: A6 88           LDX     $88                 ; {hard.workRam+88} load the active slot index 0x88
2108: B5 AB           LDA     $AB,X               ; {hard.workRam+AB} read that slot's gate byte from the 0xab array
210A: C9 06           CMP     #$06                ; compare it against 6
210C: B0 02           BCS     $2110               ; {code.loc_2110} 6 or more -- keep per-wave count 3
210E: A0 02           LDY     #$02                ; else per-wave count 2

loc_2110:
2110: 84 80           STY     $80                 ; {hard.workRam+80} store the chosen per-wave count into 0x80
2112: A9 00           LDA     #$00                ; zero
2114: 85 50           STA     $50                 ; {hard.workRam+50} clear the head-velocity seed 0x50
2116: 85 B8           STA     $B8                 ; {hard.workRam+B8} clear 0xb8 so no velocity carries into the new wave
2118: 60              RTS                         ; return

loc_2119:
2119: A5 86           LDA     $86                 ; {hard.workRam+86} read the master enable/round flag 0x86
211B: 10 6F           BPL     $218C               ; {code.loc_218c} bit 7 clear -- nothing to lay out this pass, return
211D: 20 95 21        JSR     $2195               ; {code.plotConfigTableRow} draw the config-selected banner line
2120: A9 03           LDA     #$03                ; layout constant 3
2122: 85 93           STA     $93                 ; {hard.workRam+93} seed layout-draw cell 0x93
2124: A9 20           LDA     #$20                ; layout constant 0x20
2126: 85 94           STA     $94                 ; {hard.workRam+94} seed layout-draw cell 0x94
2128: A9 40           LDA     #$40                ; layout constant 0x40
212A: 85 91           STA     $91                 ; {hard.workRam+91} seed the draw cursor low byte 0x91
212C: A9 05           LDA     #$05                ; layout constant 5
212E: 85 92           STA     $92                 ; {hard.workRam+92} seed the draw cursor high byte 0x92
2130: 20 25 38        JSR     $3825               ; {code.redrawPointerTableRowUnblanked} redraw a pointer-table layout row, unblanked
2133: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter 0x00
2135: D0 05           BNE     $213C               ; {code.loc_213c} not frame zero -- skip the extra row
2137: A9 84           LDA     #$84                ; row selector 0x84
2139: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw that pointer-table row

loc_213c:
213C: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter 0x00
213E: AE 00 06        LDX     $0600               ; {hard.videoRam+200} load a byte from the object page 0x0600
2141: 86 FF           STX     $FF                 ; {hard.workRam+FF} stash it into scratch 0xff
2143: 29 80           AND     #$80                ; test the frame counter's high bit
2145: D0 45           BNE     $218C               ; {code.loc_218c} high bit set -- skip the target stepping and return
2147: A5 43           LDA     $43                 ; {hard.workRam+43} read the mode/state gate 0x43
2149: 29 AF           AND     #$AF                ; mask its mode bits
214B: D0 30           BNE     $217D               ; {code.loc_217d} mode bits set -- skip the target clamps, go to the tail-writer
214D: A5 63           LDA     $63                 ; {hard.workRam+63} read the 63-axis coordinate
214F: A0 01           LDY     #$01                ; default target step +1
2151: C9 1C           CMP     #$1C                ; compare against the low band edge 0x1c
2153: 90 08           BCC     $215D               ; {code.loc_215d} below the low edge -- keep +1
2155: A0 FF           LDY     #$FF                ; else set target step -1
2157: C9 E4           CMP     #$E4                ; compare against the high band edge 0xe4
2159: B0 02           BCS     $215D               ; {code.loc_215d} at or above the high edge -- keep -1
215B: A4 53           LDY     $53                 ; {hard.workRam+53} in-band -- reuse the stored 0x53 target step

loc_215d:
215D: 98              TYA                         ; bring the chosen step into A
215E: 84 53           STY     $53                 ; {hard.workRam+53} store the new 0x53 target
2160: 18              CLC                         ; clear carry for the coordinate step
2161: 20 EB 2A        JSR     $2AEB               ; {code.loc_2aeb} step the 73-axis coordinate integrator with it
2164: A5 73           LDA     $73                 ; {hard.workRam+73} read the 73-axis coordinate
2166: 85 8D           STA     $8D                 ; {hard.workRam+8D} snapshot it into 0x8d
2168: A0 FF           LDY     #$FF                ; default target step -1
216A: C9 30           CMP     #$30                ; compare against the low band edge 0x30
216C: B0 08           BCS     $2176               ; {code.loc_2176} at or above it -- keep step -1
216E: A0 01           LDY     #$01                ; else target step +1
2170: C9 09           CMP     #$09                ; compare against 0x09
2172: 90 02           BCC     $2176               ; {code.loc_2176} below it -- keep +1
2174: A4 83           LDY     $83                 ; {hard.workRam+83} in-band -- reuse the stored 0x83 target step

loc_2176:
2176: 98              TYA                         ; bring the chosen step into A
2177: 84 83           STY     $83                 ; {hard.workRam+83} store the new 0x83 target
2179: 18              CLC                         ; clear carry for the coordinate step
217A: 20 24 2B        JSR     $2B24               ; {code.clampCoordToBand} step the 73 coordinate and clamp it into its band

loc_217d:
217D: 20 60 2B        JSR     $2B60               ; {code.routeByCoordDelta} run the tail-writer's coord-delta routing
2180: A2 13           LDX     #$13                ; index 0x13 -- top of the 20-byte block
2182: A9 FA           LDA     #$FA                ; seed the checksum accumulator with 0xfa

loc_2184:
2184: 5D 20 21        EOR     $2120,X             ; {hard.rom+120} fold in one byte of the 20-byte block at 0x2120
2187: CA              DEX                         ; step to the previous byte
2188: 10 FA           BPL     $2184               ; {code.loc_2184} loop across the whole block
218A: 85 FE           STA     $FE                 ; {hard.workRam+FE} store the folded checksum into 0xfe

loc_218c:
218C: 60              RTS                         ; return

; ---- $218D-$2194: data ----
218D: 02 BB 5A 30 5F EE 7D A8

plotConfigTableRow:
2195: 20 B3 21        JSR     $21B3               ; {code.readFdBitsTableByte} fetch the config-indexed table byte (index returned in Y)
2198: 85 AE           STA     $AE                 ; {hard.workRam+AE} stash that first byte into 0xae
219A: B9 C0 21        LDA     $21C0,Y             ; {hard.rom+1C0} read the parallel-table byte at the same index
219D: 85 B0           STA     $B0                 ; {hard.workRam+B0} stash it into 0xb0
219F: A9 06           LDA     #$06                ; row selector 6
21A1: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw the fixed layout row
21A4: A5 B0           LDA     $B0                 ; {hard.workRam+B0} reload the parallel byte
21A6: 20 5C 38        JSR     $385C               ; {code.plotNormalizedCharCode} plot it as a glyph
21A9: A5 AE           LDA     $AE                 ; {hard.workRam+AE} reload the first table byte
21AB: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as a two-digit number
21AE: A9 00           LDA     #$00                ; trailing zero
21B0: 4C 4F 38        JMP     $384F               ; {code.plotByteAsTwoDigits} plot the trailing zero as two digits and return

readFdBitsTableByte:
21B3: A5 FD           LDA     $FD                 ; {hard.workRam+FD} read the config/mode byte 0xfd
21B5: 29 30           AND     #$30                ; isolate bits 5-4, the ROM-table selector
21B7: 4A              LSR     A                   ; shift it down toward an even index
21B8: 4A              LSR     A                   ; shift again
21B9: 4A              LSR     A                   ; shift again -- giving 0, 2, 4, or 6
21BA: A8              TAY                         ; move the index into Y
21BB: B9 BF 21        LDA     $21BF,Y             ; {hard.rom+1BF} read that byte from the ROM table at 0x21bf
21BE: 60              RTS                         ; return with the byte in A and the index in Y

; ---- $21BF-$21C6: data ----
21BF: 00 01 20 01 50 01 00 02

seedSegmentSpawnState:
21C7: A6 88           LDX     $88                 ; {hard.workRam+88} load the active-object slot index 0x88
21C9: A0 02           LDY     #$02                ; default steer selector 2
21CB: B5 AB           LDA     $AB,X               ; {hard.workRam+AB} read that slot's gate byte from the 0xab array
21CD: D0 0C           BNE     $21DB               ; {code.loc_21db} gate nonzero -- keep selector 2
21CF: A5 FD           LDA     $FD                 ; {hard.workRam+FD} read the config/mode byte 0xfd
21D1: 29 40           AND     #$40                ; isolate bit 6
21D3: 09 10           ORA     #$10                ; fold in the 0x10 threshold base
21D5: D5 A9           CMP     $A9,X               ; {hard.workRam+A9} compare against the slot's 0xa9 entry
21D7: 90 02           BCC     $21DB               ; {code.loc_21db} threshold below the slot value -- keep selector 2
21D9: A0 01           LDY     #$01                ; else drop the steer selector to 1

loc_21db:
21DB: 84 81           STY     $81                 ; {hard.workRam+81} store the selector into the Y-steer cell 0x81
21DD: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
21E0: 29 04           AND     #$04                ; test bit 2
21E2: F0 05           BEQ     $21E9               ; {code.loc_21e9} bit clear -- skip the sign mirror
21E4: 98              TYA                         ; bring the selector into A
21E5: 20 2D 38        JSR     $382D               ; {code.negateA} two's-complement negate it
21E8: A8              TAY                         ; move the negated value back into Y

loc_21e9:
21E9: 84 51           STY     $51                 ; {hard.workRam+51} stash the (possibly mirrored) horizontal drift seed into the object's drift cell
21EB: A9 60           LDA     #$60                ; load the base heading constant 0x60
21ED: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it against the orientation mask so it mirrors for a flipped cabinet
21EF: 85 71           STA     $71                 ; {hard.workRam+71} seed the object's heading cell with the folded key
21F1: A9 FF           LDA     #$FF                ; load 0xff
21F3: 85 61           STA     $61                 ; {hard.workRam+61} seed the object's row cell to 0xff
21F5: A9 F8           LDA     #$F8                ; load 0xf8
21F7: 85 41           STA     $41                 ; {hard.workRam+41} seed the column heading cell
21F9: A9 60           LDA     #$60                ; load the dwell interval 0x60
21FB: 85 A1           STA     $A1                 ; {hard.workRam+A1} arm the column dwell timer
21FD: A9 00           LDA     #$00                ; load zero
21FF: 85 B5           STA     $B5                 ; {hard.workRam+B5} silence the channel-4 SFX timer
2201: 60              RTS                         ; spawn cells seeded -- return

advanceColumnHeadingState:
2202: A5 43           LDA     $43                 ; {hard.workRam+43} read the state/mode flag
2204: 29 AF           AND     #$AF                ; keep only its mode bits
2206: F0 01           BEQ     $2209               ; {code.loc_2209} if none are set, go advance the column heading this frame

loc_2208:
2208: 60              RTS                         ; otherwise nothing to do this frame -- return

loc_2209:
2209: A2 0D           LDX     #$0D                ; set the slot index to the head slot 0x0d
220B: A5 41           LDA     $41                 ; {hard.workRam+41} read the column heading
220D: A8              TAY                         ; keep a copy in Y
220E: 29 20           AND     #$20                ; test the high-branch bit of the heading
2210: F0 07           BEQ     $2219               ; {code.loc_2219} bit clear -- take the low branch and step the heading
2212: C0 F8           CPY     #$F8                ; high branch: compare the heading against the far edge 0xf8
2214: 90 F2           BCC     $2208               ; {code.loc_2208} not at the far edge yet -- bail and wait
2216: 4C FA 22        JMP     $22FA               ; {code.tickColumnCountdown} reached the far edge -- jump to re-arm the heading countdown

loc_2219:
2219: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter
221B: 29 03           AND     #$03                ; mask to every fourth frame
221D: D0 10           BNE     $222F               ; {code.loc_222f} not this frame -- skip the heading step
221F: E6 41           INC     $41                 ; {hard.workRam+41} step the column heading forward
2221: A5 41           LDA     $41                 ; {hard.workRam+41} re-read the heading
2223: 45 F2           EOR     $F2                 ; {hard.workRam+F2} fold it against the wrap-boundary orientation byte
2225: C9 1C           CMP     #$1C                ; compare against the fold boundary 0x1c
2227: 90 06           BCC     $222F               ; {code.loc_222f} still inside the range -- skip the wrap
2229: A9 14           LDA     #$14                ; load the wrap-around heading 0x14
222B: 45 F2           EOR     $F2                 ; {hard.workRam+F2} fold it against the wrap-boundary orientation byte
222D: 85 41           STA     $41                 ; {hard.workRam+41} wrap the column heading back to its start

loc_222f:
222F: C6 A1           DEC     $A1                 ; {hard.workRam+A1} tick the column dwell timer down
2231: D0 35           BNE     $2268               ; {code.loc_2268} still counting -- skip the wrap-through-zero work and go fold the drift
2233: AD 0A 10        LDA     $100A               ; {hard.pokey+A} timer expired: read the hardware random register
2236: 29 80           AND     #$80                ; test its top bit
2238: F0 18           BEQ     $2252               ; {code.loc_2252} bit clear -- skip the drift pause/resume swap
223A: A5 51           LDA     $51                 ; {hard.workRam+51} read the current horizontal drift
223C: F0 10           BEQ     $224E               ; {code.loc_224e} drift is zero (paused) -- go restore it from the stash
223E: A4 61           LDY     $61                 ; {hard.workRam+61} drift is live: read the object's row cell
2240: C0 FB           CPY     #$FB                ; compare against the high band edge 0xfb
2242: B0 0E           BCS     $2252               ; {code.loc_2252} too near the top -- skip the swap
2244: C0 05           CPY     #$05                ; compare against the low band edge 0x05
2246: 90 0A           BCC     $2252               ; {code.loc_2252} too near the bottom -- skip the swap
2248: 85 BE           STA     $BE                 ; {hard.workRam+BE} in-band: stash the live drift away
224A: A9 00           LDA     #$00                ; load zero
224C: F0 02           BEQ     $2250               ; {code.loc_2250} always taken -- store zero into the drift (pause the horizontal drift)

loc_224e:
224E: A5 BE           LDA     $BE                 ; {hard.workRam+BE} restore the horizontal drift from its stash (resume it)

loc_2250:
2250: 85 51           STA     $51                 ; {hard.workRam+51} write the chosen drift value back

loc_2252:
2252: A5 FD           LDA     $FD                 ; {hard.workRam+FD} read the config/mode byte
2254: 29 40           AND     #$40                ; keep its config bit 6
2256: 09 20           ORA     #$20                ; force bit 5 on
2258: 2D 0A 10        AND     $100A               ; {hard.pokey+A} gate the result through the hardware random register
225B: F0 07           BEQ     $2264               ; {code.loc_2264} zero -- skip flipping the vertical steer
225D: A5 81           LDA     $81                 ; {hard.workRam+81} read the vertical steer delta
225F: 20 2D 38        JSR     $382D               ; {code.negateA} negate it
2262: 85 81           STA     $81                 ; {hard.workRam+81} store the flipped vertical steer back

loc_2264:
2264: A9 30           LDA     #$30                ; load the re-arm interval 0x30
2266: 85 A1           STA     $A1                 ; {hard.workRam+A1} re-arm the column dwell timer

loc_2268:
2268: A5 61           LDA     $61                 ; {hard.workRam+61} read the object's row cell
226A: 38              SEC                         ; prepare a borrowless subtract
226B: E5 51           SBC     $51                 ; {hard.workRam+51} subtract the horizontal drift out of the row cell
226D: 85 61           STA     $61                 ; {hard.workRam+61} store the drifted row back
226F: 85 8B           STA     $8B                 ; {hard.workRam+8B} mirror the row into scratch
2271: A5 71           LDA     $71                 ; {hard.workRam+71} read the object's heading
2273: A4 EF           LDY     $EF                 ; {hard.workRam+EF} read the direction selector
2275: F0 06           BEQ     $227D               ; {code.loc_227d} selector zero -- take the subtract branch
2277: 18              CLC                         ; clear carry for the add
2278: 65 81           ADC     $81                 ; {hard.workRam+81} add the vertical steer onto the heading
227A: 4C 80 22        JMP     $2280               ; {code.steerObjectRowTarget} jump into the row-target steerer with the summed heading

loc_227d:
227D: 38              SEC                         ; prepare a borrowless subtract
227E: E5 81           SBC     $81                 ; {hard.workRam+81} subtract the vertical steer from the heading

steerObjectRowTarget:
2280: 85 71           STA     $71                 ; {hard.workRam+71} commit the computed heading as the new row target
2282: A0 00           LDY     #$00                ; select row 0 for the cell probe
2284: 20 2B 2C        JSR     $2C2B               ; {code.resolveTileCellAtXY} resolve the tile cell at the target coordinate
2287: F0 13           BEQ     $229C               ; {code.loc_229c} empty cell -- skip the mushroom-consume
2289: A0 00           LDY     #$00                ; index 0 for the cell read
228B: B1 32           LDA     ($32),Y             ; {hard.workRam+32} read the tile at the target through the working pointer
228D: 29 3F           AND     #$3F                ; keep only the tile code
228F: C9 38           CMP     #$38                ; compare against the high tile class 0x38
2291: 90 09           BCC     $229C               ; {code.loc_229c} below it -- not consumable, skip
2293: A9 00           LDA     #$00                ; load a blank
2295: 91 32           STA     ($32),Y             ; {hard.workRam+32} clear the cell -- the object consumes the mushroom there
2297: 20 91 2B        JSR     $2B91               ; {code.maybeDecrementTableEntry} decrement the matching per-column tally for the eaten mushroom
229A: A2 0D           LDX     #$0D                ; restore the head slot index 0x0d

loc_229c:
229C: A5 61           LDA     $61                 ; {hard.workRam+61} read the object's row cell
229E: C9 FF           CMP     #$FF                ; is the column retired (0xff)?
22A0: B0 54           BCS     $22F6               ; {code.loc_22f6} retired -- go reseed the spawn state and return
22A2: A5 71           LDA     $71                 ; {hard.workRam+71} read the row target
22A4: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it against the orientation mask
22A6: C9 09           CMP     #$09                ; compare against the near-top edge 0x09
22A8: B0 06           BCS     $22B0               ; {code.loc_22b0} far enough from the edge -- run the distance test
22AA: A5 81           LDA     $81                 ; {hard.workRam+81} near the top: read the vertical steer
22AC: 10 3D           BPL     $22EB               ; {code.loc_22eb} steer positive -- go straight to the store step
22AE: 30 32           BMI     $22E2               ; {code.loc_22e2} steer negative -- take the flip-and-fold path

loc_22b0:
22B0: A6 88           LDX     $88                 ; {hard.workRam+88} load the active-object selector
22B2: B5 AB           LDA     $AB,X               ; {hard.workRam+AB} read that object's per-object counter
22B4: F8              SED                         ; switch to decimal mode
22B5: 38              SEC                         ; prepare a borrowless subtract
22B6: E9 06           SBC     #$06                ; knock the counter down by 6 in BCD
22B8: D8              CLD                         ; back to binary mode
22B9: 10 02           BPL     $22BD               ; {code.loc_22bd} result still non-negative -- keep it
22BB: A9 00           LDA     #$00                ; underflowed -- floor the distance at zero

loc_22bd:
22BD: 4A              LSR     A                   ; halve the reduced counter
22BE: C9 06           CMP     #$06                ; compare against the clamp 6
22C0: 90 02           BCC     $22C4               ; {code.loc_22c4} below the clamp -- keep it
22C2: A9 05           LDA     #$05                ; clamp the distance to 5

loc_22c4:
22C4: 0A              ASL     A                   ; scale the distance up (x2)
22C5: 0A              ASL     A                   ; scale it (x4)
22C6: 0A              ASL     A                   ; scale it (x8)
22C7: 85 8D           STA     $8D                 ; {hard.workRam+8D} store the scaled distance
22C9: A9 60           LDA     #$60                ; load the base coordinate 0x60
22CB: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it against the orientation mask
22CD: 38              SEC                         ; prepare a borrowless subtract
22CE: E5 8D           SBC     $8D                 ; {hard.workRam+8D} subtract the scaled distance to get the target coordinate
22D0: A6 EF           LDX     $EF                 ; {hard.workRam+EF} read the direction selector
22D2: F0 06           BEQ     $22DA               ; {code.loc_22da} selector zero -- take the mirrored compare
22D4: C5 71           CMP     $71                 ; {hard.workRam+71} compare the target coordinate against the row target
22D6: 90 0A           BCC     $22E2               ; {code.loc_22e2} target below -- take the flip-and-fold path
22D8: B0 04           BCS     $22DE               ; {code.loc_22de} target at or above -- go to the steer test

loc_22da:
22DA: C5 71           CMP     $71                 ; {hard.workRam+71} compare the target coordinate against the row target
22DC: B0 04           BCS     $22E2               ; {code.loc_22e2} target at or above -- take the flip-and-fold path

loc_22de:
22DE: A5 81           LDA     $81                 ; {hard.workRam+81} read the vertical steer
22E0: 30 09           BMI     $22EB               ; {code.loc_22eb} steer negative -- go straight to the store step

loc_22e2:
22E2: A2 0D           LDX     #$0D                ; set the slot index to the head slot 0x0d
22E4: 20 6B 2C        JSR     $2C6B               ; {code.detectColumnCollision} test whether another object shares this column nearby
22E7: 90 07           BCC     $22F0               ; {code.loc_22f0} no neighbour -- skip the flip
22E9: A5 81           LDA     $81                 ; {hard.workRam+81} neighbour present: read the vertical steer

loc_22eb:
22EB: 20 2D 38        JSR     $382D               ; {code.negateA} flip the vertical steer
22EE: 85 81           STA     $81                 ; {hard.workRam+81} store the flipped steer back

loc_22f0:
22F0: A2 0D           LDX     #$0D                ; set the slot index to the head slot 0x0d
22F2: 20 96 2C        JSR     $2C96               ; {code.armSlotWhenObjectInRange} arm the slot and dispatch the distance-fold step
22F5: 60              RTS                         ; steering done -- return

loc_22f6:
22F6: 20 C7 21        JSR     $21C7               ; {code.seedSegmentSpawnState} retired column -- reseed the segment spawn state
22F9: 60              RTS                         ; return

tickColumnCountdown:
22FA: C6 A1           DEC     $A1                 ; {hard.workRam+A1} tick the column dwell timer down
22FC: D0 11           BNE     $230F               ; {code.loc_230f} still counting -- return
22FE: AD 0A 10        LDA     $100A               ; {hard.pokey+A} timer expired: read the hardware random register
2301: 29 2F           AND     #$2F                ; mask the raw random value
2303: 09 0F           ORA     #$0F                ; force in the low bits -- a fresh interval of 0x0f or 0x2f
2305: 85 A1           STA     $A1                 ; {hard.workRam+A1} reload the column dwell timer
2307: A9 14           LDA     #$14                ; load 0x14
2309: 85 B5           STA     $B5                 ; {hard.workRam+B5} re-arm the channel-4 companion SFX timer
230B: 45 F2           EOR     $F2                 ; {hard.workRam+F2} fold 0x14 against the wrap-boundary orientation byte
230D: 85 41           STA     $41                 ; {hard.workRam+41} re-arm the column heading

loc_230f:
230F: 60              RTS                         ; return

loadObjectTileInputs:
2310: B5 54           LDA     $54,X               ; {hard.workRam+54} read the object slot's base byte
2312: 85 8B           STA     $8B                 ; {hard.workRam+8B} copy it into scratch
2314: A0 FF           LDY     #$FF                ; default the step to -1
2316: B5 44           LDA     $44,X               ; {hard.workRam+44} read the slot's heading byte
2318: 30 02           BMI     $231C               ; {code.loc_231c} heading points negative -- keep the -1 step
231A: A0 01           LDY     #$01                ; else set the step to +1

loc_231c:
231C: B5 64           LDA     $64,X               ; {hard.workRam+64} load the slot's coordinate byte for the tile probe
231E: 60              RTS                         ; inputs packaged -- return

rebuildSegmentSpriteTables:
231F: A6 88           LDX     $88                 ; {hard.workRam+88} load the active-object selector
2321: B5 94           LDA     $94,X               ; {hard.workRam+94} read this object's rebuild gate
2323: D0 20           BNE     $2345               ; {code.loc_2345} gate already set -- skip the length-counter maintenance
2325: B5 C2           LDA     $C2,X               ; {hard.workRam+C2} read the slot's busy/flag byte
2327: 09 80           ORA     #$80                ; set its busy (high) bit
2329: 95 C2           STA     $C2,X               ; {hard.workRam+C2} store the flag byte back
232B: B5 9C           LDA     $9C,X               ; {hard.workRam+9C} read the slot's spawn counter
232D: C9 03           CMP     #$03                ; is it at least 3?
232F: 90 14           BCC     $2345               ; {code.loc_2345} below 3 -- skip the length wrap
2331: D6 9A           DEC     $9A,X               ; {hard.workRam+9A} tick the length counter down
2333: D0 04           BNE     $2339               ; {code.loc_2339} still nonzero -- skip the wrap
2335: A9 0C           LDA     #$0C                ; load the wrap value 0x0c
2337: 95 9A           STA     $9A,X               ; {hard.workRam+9A} wrap the length counter back to 0x0c

loc_2339:
2339: A9 02           LDA     #$02                ; default the new spawn count to 2
233B: B4 AB           LDY     $AB,X               ; {hard.workRam+AB} read this object's per-object counter
233D: C0 04           CPY     #$04                ; compare against 4
233F: B0 02           BCS     $2343               ; {code.loc_2343} counter high enough -- keep the count of 2
2341: A9 01           LDA     #$01                ; else drop the new count to 1

loc_2343:
2343: 95 9C           STA     $9C,X               ; {hard.workRam+9C} store the new spawn counter

loc_2345:
2345: A9 03           LDA     #$03                ; load the head-entry length 3
2347: 85 34           STA     $34                 ; {hard.workRam+34} seed the [0] length entry
2349: B5 9C           LDA     $9C,X               ; {hard.workRam+9C} read the slot's spawn counter
234B: 85 74           STA     $74                 ; {hard.workRam+74} seed the [0] length field
234D: A8              TAY                         ; keep the length in Y
234E: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter
2350: 29 02           AND     #$02                ; test its negate-select bit
2352: D0 05           BNE     $2359               ; {code.loc_2359} bit set -- keep the length unnegated
2354: 98              TYA                         ; move the length into A
2355: 20 2D 38        JSR     $382D               ; {code.negateA} negate the length
2358: A8              TAY                         ; move it back to Y

loc_2359:
2359: 84 44           STY     $44                 ; {hard.workRam+44} seed the [0] heading with the signed length
235B: A9 F8           LDA     #$F8                ; load the base coordinate 0xf8
235D: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it against the orientation mask
235F: 85 64           STA     $64                 ; {hard.workRam+64} seed the [0] coordinate cell
2361: A9 80           LDA     #$80                ; load the midline 0x80
2363: 85 54           STA     $54                 ; {hard.workRam+54} seed the [0] coordinate-row cell
2365: B5 9A           LDA     $9A,X               ; {hard.workRam+9A} read the length counter
2367: 85 8B           STA     $8B                 ; {hard.workRam+8B} copy it into scratch as the copy-loop length
2369: C9 01           CMP     #$01                ; is the centipede just one segment long?
236B: F0 35           BEQ     $23A2               ; {code.loc_23a2} single segment -- skip the descriptor-copy loop
236D: A0 42           LDY     #$42                ; seed the descriptor source index 0x42
236F: A2 01           LDX     #$01                ; start the copy at destination slot 1

loc_2371:
2371: 94 34           STY     $34,X               ; {hard.workRam+34} store the descriptor index into this slot's phase cell
2373: A9 F8           LDA     #$F8                ; load the base coordinate 0xf8
2375: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it against the orientation mask
2377: 95 64           STA     $64,X               ; {hard.workRam+64} seed this slot's coordinate cell
2379: B5 73           LDA     $73,X               ; {hard.workRam+73} read the descriptor's row byte
237B: 95 74           STA     $74,X               ; {hard.workRam+74} copy it into this slot's row table
237D: B5 43           LDA     $43,X               ; {hard.workRam+43} read the descriptor's heading byte
237F: 95 44           STA     $44,X               ; {hard.workRam+44} copy it into this slot's heading table
2381: 10 04           BPL     $2387               ; {code.loc_2387} descriptor positive -- use the 0xf8 coordinate base
2383: A9 08           LDA     #$08                ; descriptor negative -- use the 0x08 coordinate base
2385: D0 02           BNE     $2389               ; {code.loc_2389} always taken -- go add the row offset

loc_2387:
2387: A9 F8           LDA     #$F8                ; positive descriptor -- use the 0xf8 coordinate base

loc_2389:
2389: 18              CLC                         ; clear carry for the add
238A: 75 53           ADC     $53,X               ; {hard.workRam+53} add this slot's descriptor row offset
238C: 95 54           STA     $54,X               ; {hard.workRam+54} store the slot's coordinate-row cell
238E: 88              DEY                         ; step the descriptor source index down
238F: C0 3F           CPY     #$3F                ; reached the descriptor wrap boundary 0x3f?
2391: D0 02           BNE     $2395               ; {code.loc_2395} no -- continue the copy loop
2393: A0 47           LDY     #$47                ; wrap the descriptor source index up to 0x47

loc_2395:
2395: E8              INX                         ; step to the next segment sprite-table slot
2396: E4 8B           CPX     $8B                 ; {hard.workRam+8B} compare the slot index against the length limit in $8b
2398: 90 D7           BCC     $2371               ; {code.loc_2371} loop back to fill the next slot while still under the length
239A: A6 88           LDX     $88                 ; {hard.workRam+88} reload the object-slot selector
239C: B5 9A           LDA     $9A,X               ; {hard.workRam+9A} read this object's segment length counter
239E: C9 0C           CMP     #$0C                ; is the length already at the full 0x0c segments?
23A0: F0 2D           BEQ     $23CF               ; {code.loc_23cf} full-length -- skip the random fill and go mark the slot rebuilt

loc_23a2:
23A2: A9 F8           LDA     #$F8                ; build the orientation-folded coordinate base 0xf8 ^ $f0
23A4: 45 F0           EOR     $F0                 ; {hard.workRam+F0}
23A6: A6 8B           LDX     $8B                 ; {hard.workRam+8B} start the fill index at the length limit

loc_23a8:
23A8: 95 64           STA     $64,X               ; {hard.workRam+64} write the folded base into the segment's vertical coordinate row
23AA: A9 00           LDA     #$00                ; load a zero
23AC: 95 34           STA     $34,X               ; {hard.workRam+34} clear the segment's phase byte
23AE: A9 02           LDA     #$02                ; default the heading magnitude to 2
23B0: A4 F4           LDY     $F4                 ; {hard.workRam+F4} read the wave step value $f4
23B2: F0 01           BEQ     $23B5               ; {code.loc_23b5} if it is zero keep the default magnitude
23B4: 98              TYA                         ; otherwise use $f4 as the heading magnitude

loc_23b5:
23B5: 95 74           STA     $74,X               ; {hard.workRam+74} store the heading delta for this segment
23B7: 2C 0A 10        BIT     $100A               ; {hard.pokey+A} test bit 7 of the POKEY random register
23BA: 10 03           BPL     $23BF               ; {code.loc_23bf} if clear skip the negate
23BC: 20 2D 38        JSR     $382D               ; {code.negateA} mirror the value via two's complement to flip its sign

loc_23bf:
23BF: 95 44           STA     $44,X               ; {hard.workRam+44} store the signed heading delta for this segment
23C1: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
23C4: 29 F8           AND     #$F8                ; keep only the high five bits
23C6: 95 54           STA     $54,X               ; {hard.workRam+54} seed the segment's coordinate with that random value
23C8: B5 64           LDA     $64,X               ; {hard.workRam+64} reload the folded coordinate base
23CA: E8              INX                         ; advance to the next segment slot
23CB: E0 0C           CPX     #$0C                ; reached the full twelve slots?
23CD: 90 D9           BCC     $23A8               ; {code.loc_23a8} loop back to fill the remaining slots

loc_23cf:
23CF: A9 0C           LDA     #$0C                ; load the rebuilt marker 0x0c
23D1: A6 88           LDX     $88                 ; {hard.workRam+88} reload the object-slot selector
23D3: 95 94           STA     $94,X               ; {hard.workRam+94} mark this object's segment slot rebuilt
23D5: A5 FE           LDA     $FE                 ; {hard.workRam+FE} read the flip source byte $fe
23D7: 85 97           STA     $97                 ; {hard.workRam+97} copy it into the spawn-enable byte $97
23D9: 60              RTS                         ; done rebuilding this segment's sprite tables

advanceDeathRespawnSequence:
23DA: A5 87           LDA     $87                 ; {hard.workRam+87} read the death/respawn countdown $87
23DC: D0 01           BNE     $23DF               ; {code.loc_23df} nonzero -- the sequence is active, keep going

loc_23de:
23DE: 60              RTS                         ; countdown at zero -- nothing to do this frame

loc_23df:
23DF: A5 DB           LDA     $DB                 ; {hard.workRam+DB} read the field-scan pointer high byte
23E1: D0 FB           BNE     $23DE               ; {code.loc_23de} scan pointer busy -- the sequence is paused, return
23E3: C6 87           DEC     $87                 ; {hard.workRam+87} tick the death countdown down by one
23E5: D0 F7           BNE     $23DE               ; {code.loc_23de} still counting -- act only on the frame it hits zero
23E7: A5 D6           LDA     $D6                 ; {hard.workRam+D6} read the blank-a-cell flag $d6
23E9: F0 0F           BEQ     $23FA               ; {code.loc_23fa} flag clear -- skip the cell-blank action
23EB: A9 80           LDA     #$80                ; load selector 0x80 for the row redraw
23ED: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} redraw a status row
23F0: A9 00           LDA     #$00                ; load a zero to erase with
23F2: A8              TAY                         ; index zero for the cursor write
23F3: 91 91           STA     ($91),Y             ; {hard.workRam+91} blank the cell the draw cursor points at -- erase the dying glyph
23F5: 85 D6           STA     $D6                 ; {hard.workRam+D6} clear the blank-a-cell flag
23F7: 4C 32 29        JMP     $2932               ; {code.seedPlayerShotStartCells} reseed the player-shot start cells

loc_23fa:
23FA: A5 43           LDA     $43                 ; {hard.workRam+43} read the $43 mode/state byte
23FC: 29 AF           AND     #$AF                ; mask off its mode bits
23FE: D0 03           BNE     $2403               ; {code.loc_2403} any mode bit set -- continue the dispatcher
2400: 4C 05 25        JMP     $2505               ; {code.loc_2505} no mode bits -- forward to the sprite-table rebuild

loc_2403:
2403: 20 32 29        JSR     $2932               ; {code.seedPlayerShotStartCells} reseed the player-shot start cells
2406: A5 86           LDA     $86                 ; {hard.workRam+86} read the pending-wave/life sign byte $86
2408: 10 11           BPL     $241B               ; {code.loc_241b} non-negative -- take the object-count branch
240A: A5 01           LDA     $01                 ; {hard.workRam+1} read the $01 high-bit flag
240C: 10 0A           BPL     $2418               ; {code.loc_2418} bit 7 clear -- skip the screen transpose
240E: 29 7F           AND     #$7F                ; strip the high bit
2410: 85 01           STA     $01                 ; {hard.workRam+1} store $01 with its high bit cleared
2412: 20 D5 31        JSR     $31D5               ; {code.transposeScreenBitmap} rotate the tile grid a column
2415: 20 5C 2D        JSR     $2D5C               ; {code.plotRecordFieldColumns} relay out the sorted-object record field

loc_2418:
2418: 4C FF 24        JMP     $24FF               ; {code.reseedSegmentSpawnState} hand off to the segment-spawn reseed

loc_241b:
241B: A5 A5           LDA     $A5                 ; {hard.workRam+A5} read object-present cell $a5
241D: 05 A6           ORA     $A6                 ; {hard.workRam+A6} fold with $a6 -- is any object still on screen?
241F: D0 46           BNE     $2467               ; {code.loc_2467} an object remains -- take the step-a-slot branch
2421: C6 86           DEC     $86                 ; {hard.workRam+86} no object left -- decrement the life/round counter
2423: 20 3E 32        JSR     $323E               ; {code.buildSortedObjectTable} rebuild the sorted object table
2426: A5 EF           LDA     $EF                 ; {hard.workRam+EF} read the spawn-pending flag $ef
2428: F0 18           BEQ     $2442               ; {code.loc_2442} clear -- skip the state-block broadcast
242A: A5 C2           LDA     $C2                 ; {hard.workRam+C2} read object-active flag $c2
242C: 10 14           BPL     $2442               ; {code.loc_2442} non-negative -- skip the broadcast
242E: A9 80           LDA     #$80                ; load 0x80
2430: 85 EE           STA     $EE                 ; {hard.workRam+EE} mark a broadcast/screen-setup pending in $ee
2432: 20 09 25        JSR     $2509               ; {code.broadcastByteToStateBlock} fan the flip byte across the whole state block
2435: 20 32 29        JSR     $2932               ; {code.seedPlayerShotStartCells} reseed the player-shot start cells
2438: 20 D5 31        JSR     $31D5               ; {code.transposeScreenBitmap} rotate the tile grid a column
243B: A5 C1           LDA     $C1                 ; {hard.workRam+C1} read object-active flag $c1
243D: 10 03           BPL     $2442               ; {code.loc_2442} non-negative -- skip the record redraw
243F: 20 5C 2D        JSR     $2D5C               ; {code.plotRecordFieldColumns} relay out the sorted-object record field

loc_2442:
2442: 20 C7 21        JSR     $21C7               ; {code.seedSegmentSpawnState} seed the segment spawn state for the fresh wave
2445: 20 1F 23        JSR     $231F               ; {code.rebuildSegmentSpriteTables} rebuild the segment sprite tables
2448: 20 E8 20        JSR     $20E8               ; {code.seedWaveState} seed the per-wave working values
244B: A9 01           LDA     #$01                ; load 1
244D: 85 00           STA     $00                 ; {hard.workRam} set the frame counter $00 to 1
244F: A9 04           LDA     #$04                ; load selector 4 for the row draw
2451: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw a pointer-table row
2454: A6 89           LDX     $89                 ; {hard.workRam+89} load the slot index $89
2456: A9 FF           LDA     #$FF                ; load 0xff
2458: 9D 02 1C        STA     $1C02,X             ; {hard.outLatch+2} clear the per-slot output latch at $1c02+slot
245B: 20 08 3A        JSR     $3A08               ; {code.foldHighScoreChecksum} fold the high-score checksum
245E: A9 3D           LDA     #$3D                ; load writeback cursor value 0x3d
2460: 85 F9           STA     $F9                 ; {hard.workRam+F9} arm the EAROM writeback cursor $f9
2462: A9 00           LDA     #$00                ; load zero
2464: 85 FA           STA     $FA                 ; {hard.workRam+FA} clear the EAROM writeback phase $fa
2466: 60              RTS                         ; wave restart done

loc_2467:
2467: A6 89           LDX     $89                 ; {hard.workRam+89} load the slot count $89
2469: CA              DEX                         ; drop it by one
246A: D0 03           BNE     $246F               ; {code.loc_246f} more than one slot -- keep going
246C: 4C F8 24        JMP     $24F8               ; {code.decrementSlotAndRedrawBorders} exactly one slot left -- close it out and redraw borders

loc_246f:
246F: A6 88           LDX     $88                 ; {hard.workRam+88} load the object-slot selector $88
2471: B5 A4           LDA     $A4,X               ; {hard.workRam+A4} read this slot's timer $a4+x
2473: D0 24           BNE     $2499               ; {code.loc_2499} slot occupied -- switch to the mirror slot
2475: A5 A7           LDA     $A7                 ; {hard.workRam+A7} empty slot -- read the arm/pass counter $a7
2477: D0 1E           BNE     $2497               ; {code.loc_2497} already armed on a prior pass -- decrement it
2479: E6 A7           INC     $A7                 ; {hard.workRam+A7} first empty pass -- bump the arm counter
247B: A9 80           LDA     #$80                ; load death-countdown reload 0x80
247D: 85 87           STA     $87                 ; {hard.workRam+87} reload the death countdown $87
247F: A9 F9           LDA     #$F9                ; load 0xf9
2481: 85 43           STA     $43                 ; {hard.workRam+43} set mode byte $43 to 0xf9
2483: 85 42           STA     $42                 ; {hard.workRam+42} set companion $42 to 0xf9
2485: A9 04           LDA     #$04                ; load selector 4 for the row draw
2487: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw a pointer-table row
248A: A9 00           LDA     #$00                ; load selector 0 for the row draw
248C: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw a second pointer-table row
248F: A5 88           LDA     $88                 ; {hard.workRam+88} read the slot selector $88
2491: 09 20           ORA     #$20                ; fold in the slot glyph bit 0x20
2493: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} paint the slot's glyph and advance the cursor
2496: 60              RTS                         ; slot armed -- return

loc_2497:
2497: C6 A7           DEC     $A7                 ; {hard.workRam+A7} later empty pass -- decrement the arm counter

loc_2499:
2499: A5 88           LDA     $88                 ; {hard.workRam+88} read the current slot selector
249B: 49 03           EOR     #$03                ; flip to the mirror slot index
249D: AA              TAX                         ; move it into the index register
249E: B5 A4           LDA     $A4,X               ; {hard.workRam+A4} read the mirror slot's timer $a4+x
24A0: F0 56           BEQ     $24F8               ; {code.decrementSlotAndRedrawBorders} mirror also empty -- abandon into the close-slot tail
24A2: 86 88           STX     $88                 ; {hard.workRam+88} commit to the mirror slot: store its index in $88
24A4: A9 80           LDA     #$80                ; load the high-bit mask 0x80
24A6: 25 EE           AND     $EE                 ; {hard.workRam+EE} keep only the top bit of $ee
24A8: 05 88           ORA     $88                 ; {hard.workRam+88} fold in the new slot selector
24AA: 85 EE           STA     $EE                 ; {hard.workRam+EE} store the combined flag back into $ee
24AC: C9 82           CMP     #$82                ; did it land on 0x82?
24AE: D0 03           BNE     $24B3               ; {code.loc_24b3} no -- skip the constant reseed
24B0: 20 2A 25        JSR     $252A               ; {code.seedStateBlockConstants} reseed the state-block constants

loc_24b3:
24B3: B5 A1           LDA     $A1,X               ; {hard.workRam+A1} read the spawn-timer reload from the $a1 table
24B5: 85 A0           STA     $A0                 ; {hard.workRam+A0} arm the spawn timer $a0
24B7: A6 88           LDX     $88                 ; {hard.workRam+88} reload the slot selector
24B9: E0 01           CPX     #$01                ; is this slot 1?
24BB: D0 03           BNE     $24C0               ; {code.loc_24c0} no -- skip the broadcast
24BD: 20 09 25        JSR     $2509               ; {code.broadcastByteToStateBlock} fan the flip byte across the state block for slot 1

loc_24c0:
24C0: 20 D5 31        JSR     $31D5               ; {code.transposeScreenBitmap} rotate the tile grid a column
24C3: A6 88           LDX     $88                 ; {hard.workRam+88} reload the slot selector
24C5: E0 02           CPX     #$02                ; is this slot 2?
24C7: D0 11           BNE     $24DA               ; {code.loc_24da} no -- skip the playfield-reset special case
24C9: B5 A4           LDA     $A4,X               ; {hard.workRam+A4} read this slot's timer
24CB: C5 A4           CMP     $A4                 ; {hard.workRam+A4} compare it against slot 0's timer
24CD: D0 0B           BNE     $24DA               ; {code.loc_24da} differ -- skip
24CF: A5 AD           LDA     $AD                 ; {hard.workRam+AD} read $ad
24D1: D0 07           BNE     $24DA               ; {code.loc_24da} nonzero -- skip
24D3: A9 0C           LDA     #$0C                ; load the rebuilt marker 0x0c
24D5: 95 94           STA     $94,X               ; {hard.workRam+94} write 0x0c into this slot's $94 cell
24D7: 20 BF 28        JSR     $28BF               ; {code.resetPlayfieldAndSeedMushrooms} clear the field and lay a fresh mushroom carpet

loc_24da:
24DA: B5 C2           LDA     $C2,X               ; {hard.workRam+C2} read the slot's active flag $c2+x
24DC: 09 40           ORA     #$40                ; set the busy bit 0x40
24DE: 95 C2           STA     $C2,X               ; {hard.workRam+C2} mark the slot busy
24E0: A9 A0           LDA     #$A0                ; load death-countdown reload 0xa0
24E2: 85 87           STA     $87                 ; {hard.workRam+87} reload the death countdown $87
24E4: A9 00           LDA     #$00                ; load selector 0 for the row draw
24E6: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw a pointer-table row
24E9: A5 88           LDA     $88                 ; {hard.workRam+88} read the slot selector $88
24EB: 09 20           ORA     #$20                ; fold in the slot glyph bit 0x20
24ED: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} paint the slot's glyph and advance the cursor
24F0: A9 F9           LDA     #$F9                ; load 0xf9
24F2: 85 43           STA     $43                 ; {hard.workRam+43} set mode byte $43 to 0xf9
24F4: 85 42           STA     $42                 ; {hard.workRam+42} set companion $42 to 0xf9
24F6: 85 D6           STA     $D6                 ; {hard.workRam+D6} set the blank-a-cell flag $d6 to 0xf9

decrementSlotAndRedrawBorders:
24F8: A6 88           LDX     $88                 ; {hard.workRam+88} load the slot selector $88
24FA: D6 A4           DEC     $A4,X               ; {hard.workRam+A4} count this slot's $a4 timer down by one
24FC: 20 B8 26        JSR     $26B8               ; {code.drawGridSideBorders} repaint the two vertical grid side-borders

reseedSegmentSpawnState:
24FF: 20 C7 21        JSR     $21C7               ; {code.seedSegmentSpawnState} seed the segment spawn state
2502: 20 E8 20        JSR     $20E8               ; {code.seedWaveState} seed the per-wave working values

loc_2505:
2505: 20 1F 23        JSR     $231F               ; {code.rebuildSegmentSpriteTables} rebuild the segment sprite tables
2508: 60              RTS                         ; return

broadcastByteToStateBlock:
2509: A5 FE           LDA     $FE                 ; {hard.workRam+FE} read the broadcast source byte $fe
250B: 85 BD           STA     $BD                 ; {hard.workRam+BD} fan it into $bd
250D: 85 BF           STA     $BF                 ; {hard.workRam+BF} fan it into $bf
250F: 8D 07 1C        STA     $1C07               ; {hard.outLatch+7} drive the flip-screen latch from bit 7 of the value
2512: 8D 00 24        STA     $2400               ; {hard.rom+400} mirror the same write to the ignored $2400 store
2515: 85 F5           STA     $F5                 ; {hard.workRam+F5} fan the value into flip byte $f5
2517: 85 F7           STA     $F7                 ; {hard.workRam+F7} fan into $f7
2519: 85 F6           STA     $F6                 ; {hard.workRam+F6} fan into $f6
251B: 85 F0           STA     $F0                 ; {hard.workRam+F0} fan into orientation mask $f0
251D: 85 EF           STA     $EF                 ; {hard.workRam+EF} fan into mask $ef
251F: 85 F1           STA     $F1                 ; {hard.workRam+F1} fan into $f1
2521: 85 F2           STA     $F2                 ; {hard.workRam+F2} fan into $f2
2523: 85 F3           STA     $F3                 ; {hard.workRam+F3} fan into $f3
2525: 85 F4           STA     $F4                 ; {hard.workRam+F4} fan into $f4
2527: 85 F8           STA     $F8                 ; {hard.workRam+F8} fan into $f8
2529: 60              RTS                         ; broadcast done

seedStateBlockConstants:
252A: A9 F8           LDA     #$F8                ; load 0xf8
252C: 85 F0           STA     $F0                 ; {hard.workRam+F0} seed orientation mask $f0
252E: A9 FF           LDA     #$FF                ; load 0xff
2530: 85 F3           STA     $F3                 ; {hard.workRam+F3} seed $f3
2532: A9 FE           LDA     #$FE                ; load 0xfe
2534: 85 F4           STA     $F4                 ; {hard.workRam+F4} seed $f4
2536: A9 FC           LDA     #$FC                ; load 0xfc
2538: 85 F8           STA     $F8                 ; {hard.workRam+F8} seed $f8
253A: A9 E0           LDA     #$E0                ; load 0xe0
253C: 85 F1           STA     $F1                 ; {hard.workRam+F1} seed $f1
253E: A9 C0           LDA     #$C0                ; load 0xc0
2540: 85 EF           STA     $EF                 ; {hard.workRam+EF} seed mask $ef
2542: A9 40           LDA     #$40                ; load 0x40
2544: 85 F2           STA     $F2                 ; {hard.workRam+F2} seed $f2
2546: A9 BF           LDA     #$BF                ; load 0xbf
2548: 85 F5           STA     $F5                 ; {hard.workRam+F5} seed flip byte $f5
254A: A9 03           LDA     #$03                ; load 0x03
254C: 85 F7           STA     $F7                 ; {hard.workRam+F7} seed $f7
254E: A9 3F           LDA     #$3F                ; load 0x3f
2550: 85 F6           STA     $F6                 ; {hard.workRam+F6} seed $f6
2552: A9 80           LDA     #$80                ; load 0x80
2554: 8D 07 1C        STA     $1C07               ; {hard.outLatch+7} set the flip-screen latch bit 7
2557: 8D 00 24        STA     $2400               ; {hard.rom+400} mirror the write to the ignored $2400 store
255A: A9 00           LDA     #$00                ; load zero
255C: 85 BD           STA     $BD                 ; {hard.workRam+BD} clear $bd
255E: 85 BF           STA     $BF                 ; {hard.workRam+BF} clear $bf
2560: 60              RTS                         ; state-block seeded

loc_2561:
2561: AD 01 08        LDA     $0801               ; {hard.dsw2} read the DSW2 config source byte
2564: 85 D3           STA     $D3                 ; {hard.workRam+D3} stash it into $d3
2566: 29 03           AND     #$03                ; keep the low two bits
2568: 85 8D           STA     $8D                 ; {hard.workRam+8D} store the wave-select selector into $8d
256A: D0 04           BNE     $2570               ; {code.loc_2570} nonzero selector -- skip the default
256C: A9 02           LDA     #$02                ; load 2
256E: 85 C8           STA     $C8                 ; {hard.workRam+C8} selector zero -- set the object limit $c8 to 2

loc_2570:
2570: A5 FD           LDA     $FD                 ; {hard.workRam+FD} read the mode/DIP config byte
2572: 29 0C           AND     #$0C                ; keep bits 3-2, the difficulty selector
2574: 4A              LSR     A                   ; shift the difficulty bits down one
2575: 4A              LSR     A                   ; shift them down again, into the low two bits
2576: 69 02           ADC     #$02                ; add 2 to form the difficulty-scaled count
2578: 85 A4           STA     $A4                 ; {hard.workRam+A4} stash that difficulty count in $a4
257A: A5 86           LDA     $86                 ; {hard.workRam+86} read the pending-wave-start flag $86
257C: 30 01           BMI     $257F               ; {code.loc_257f} bit7 set means a wave start is pending -- go service the banner
257E: 60              RTS                         ; no wave pending -- return (the common frame)

loc_257f:
257F: A5 8D           LDA     $8D                 ; {hard.workRam+8D} read the wave-select code $8d
2581: F0 03           BEQ     $2586               ; {code.loc_2586} zero -- skip the banner status row
2583: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} lay down a banner status row

loc_2586:
2586: A5 00           LDA     $00                 ; {hard.workRam} read the frame/tick cell
2588: 29 20           AND     #$20                ; isolate bit5 of the tick
258A: 0A              ASL     A                   ; shift it up
258B: 0A              ASL     A                   ; shift it up again, into bit7
258C: 85 8D           STA     $8D                 ; {hard.workRam+8D} store the reshaped bit as the wave-select code $8d
258E: A5 C8           LDA     $C8                 ; {hard.workRam+C8} read the banner countdown counter $c8
2590: 05 C9           ORA     $C9                 ; {hard.workRam+C9} fold in the segment-movement accumulator so either keeps the count alive
2592: F0 10           BEQ     $25A4               ; {code.loc_25a4} both counters spent -- draw the finished banner row and return
2594: A6 DC           LDX     $DC                 ; {hard.workRam+DC} read the banner flip byte $dc
2596: 10 27           BPL     $25BF               ; {code.loc_25bf} non-negative -- jump straight to drawing the count digits
2598: C9 02           CMP     #$02                ; compare the folded count against 2
259A: 90 1C           BCC     $25B8               ; {code.loc_25b8} below 2 -- take the low-count banner branch
259C: A9 00           LDA     #$00                ; clear value
259E: 85 DC           STA     $DC                 ; {hard.workRam+DC} clear the banner flip byte $dc
25A0: A9 8A           LDA     #$8A                ; load banner row code 0x8a
25A2: D0 18           BNE     $25BC               ; {code.loc_25bc} always taken -- draw that row

loc_25a4:
25A4: A5 FD           LDA     $FD                 ; {hard.workRam+FD} read the mode/DIP config byte
25A6: 29 80           AND     #$80                ; isolate its top bit
25A8: 85 DC           STA     $DC                 ; {hard.workRam+DC} latch that bit into the banner flip byte $dc
25AA: 49 8A           EOR     #$8A                ; fold it into a banner row code
25AC: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} lay down that banner row
25AF: A2 FF           LDX     #$FF                ; all-ones
25B1: 8E 03 1C        STX     $1C03               ; {hard.outLatch+3} drive the per-slot output latch 0x1c03 high
25B4: 8E 04 1C        STX     $1C04               ; {hard.outLatch+4} drive the per-slot output latch 0x1c04 high

loc_25b7:
25B7: 60              RTS                         ; return

loc_25b8:
25B8: A9 0A           LDA     #$0A                ; low-count banner row base
25BA: 05 8D           ORA     $8D                 ; {hard.workRam+8D} fold in the wave-select code $8d

loc_25bc:
25BC: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} lay down the banner row

loc_25bf:
25BF: A9 09           LDA     #$09                ; row code 9
25C1: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} lay down the banner row
25C4: A5 C8           LDA     $C8                 ; {hard.workRam+C8} read the banner countdown counter $c8
25C6: C9 0A           CMP     #$0A                ; compare against ten
25C8: 90 0A           BCC     $25D4               ; {code.loc_25d4} below ten -- single digit, skip the tens
25CA: A9 21           LDA     #$21                ; tens-digit glyph
25CC: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot the tens digit and step the cursor
25CF: A5 C8           LDA     $C8                 ; {hard.workRam+C8} reload the countdown counter
25D1: 38              SEC                         ; prepare for subtraction
25D2: E9 0A           SBC     #$0A                ; strip off the ten, leaving the units

loc_25d4:
25D4: 09 20           ORA     #$20                ; set the glyph bit on the units value
25D6: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot the units digit and step the cursor
25D9: A5 C9           LDA     $C9                 ; {hard.workRam+C9} read the segment-movement accumulator
25DB: F0 02           BEQ     $25DF               ; {code.loc_25df} zero -- keep the current glyph
25DD: A9 1E           LDA     #$1E                ; otherwise use the alternate glyph

loc_25df:
25DF: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot it and step the cursor
25E2: A6 C8           LDX     $C8                 ; {hard.workRam+C8} read the banner countdown counter $c8
25E4: F0 D1           BEQ     $25B7               ; {code.loc_25b7} zero -- return
25E6: A5 DC           LDA     $DC                 ; {hard.workRam+DC} read the banner flip byte $dc
25E8: 30 CD           BMI     $25B7               ; {code.loc_25b7} negative -- return
25EA: A5 8D           LDA     $8D                 ; {hard.workRam+8D} read the wave-select code $8d
25EC: 8D 03 1C        STA     $1C03               ; {hard.outLatch+3} write it to the per-slot output latch 0x1c03
25EF: E0 02           CPX     #$02                ; is the counter below 2?
25F1: 90 14           BCC     $2607               ; {code.loc_2607} below 2 -- skip ahead
25F3: 8D 04 1C        STA     $1C04               ; {hard.outLatch+4} write the code to the output latch 0x1c04 as well
25F6: A2 02           LDX     #$02                ; default slot index 2
25F8: AD 01 0C        LDA     $0C01               ; {hard.in1} read input port IN1
25FB: 29 02           AND     #$02                ; test bit1
25FD: D0 08           BNE     $2607               ; {code.loc_2607} set -- a held input defers the commit
25FF: A5 A4           LDA     $A4                 ; {hard.workRam+A4} read the difficulty count $a4
2601: 85 A6           STA     $A6                 ; {hard.workRam+A6} seed the slot timer $a6 with it
2603: C6 C8           DEC     $C8                 ; {hard.workRam+C8} tick the banner countdown counter down
2605: 10 08           BPL     $260F               ; {code.loc_260f} go commit the wave

loc_2607:
2607: AD 01 0C        LDA     $0C01               ; {hard.in1} read input port IN1
260A: A6 FF           LDX     $FF                 ; {hard.workRam+FF} take the fallback slot index from $ff
260C: 4A              LSR     A                   ; shift IN1 bit0 into carry
260D: B0 A8           BCS     $25B7               ; {code.loc_25b7} set -- a held input aborts, return

loc_260f:
260F: C6 C8           DEC     $C8                 ; {hard.workRam+C8} tick the banner countdown counter down
2611: A9 FF           LDA     #$FF                ; all-ones
2613: 8D 03 1C        STA     $1C03               ; {hard.outLatch+3} drive the per-slot output latch 0x1c03 high
2616: 8D 04 1C        STA     $1C04               ; {hard.outLatch+4} drive the per-slot output latch 0x1c04 high
2619: A9 00           LDA     #$00                ; zero
261B: 85 FB           STA     $FB                 ; {hard.workRam+FB} clear working cell $fb
261D: 85 FC           STA     $FC                 ; {hard.workRam+FC} clear working cell $fc
261F: 85 9A           STA     $9A                 ; {hard.workRam+9A} clear the phase accumulator $9a
2621: 85 CB           STA     $CB                 ; {hard.workRam+CB} clear the segment row-crossing counter
2623: 85 CA           STA     $CA                 ; {hard.workRam+CA} clear the shared segment-movement accumulator
2625: 86 89           STX     $89                 ; {hard.workRam+89} store the chosen slot index in $89
2627: 9D 02 1C        STA     $1C02,X             ; {hard.outLatch+2} clear this slot's output latch at 0x1c02
262A: A6 A4           LDX     $A4                 ; {hard.workRam+A4} read the difficulty count $a4
262C: CA              DEX                         ; minus one
262D: 86 A5           STX     $A5                 ; {hard.workRam+A5} store it as the slot count $a5
262F: E6 86           INC     $86                 ; {hard.workRam+86} bump the round/wave flag $86
2631: 20 A0 26        JSR     $26A0               ; {code.copyZpStateToSnapshot} snapshot the low working cells and refold the checksum
2634: 20 B3 21        JSR     $21B3               ; {code.readFdBitsTableByte} read the config-selected table byte
2637: 85 AE           STA     $AE                 ; {hard.workRam+AE} seed object cell $ae with it
2639: 85 AF           STA     $AF                 ; {hard.workRam+AF} mirror it into $af
263B: B9 C0 21        LDA     $21C0,Y             ; {hard.rom+1C0} read the per-config parallel table byte
263E: 85 B0           STA     $B0                 ; {hard.workRam+B0} seed object cell $b0 with it
2640: 85 B1           STA     $B1                 ; {hard.workRam+B1} mirror it into $b1
2642: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read input port IN0
2645: 29 10           AND     #$10                ; test bit4
2647: F0 07           BEQ     $2650               ; {code.loc_2650} clear -- skip the state-block broadcast
2649: A9 80           LDA     #$80                ; value 0x80
264B: 85 EE           STA     $EE                 ; {hard.workRam+EE} set the pending flag $ee to it
264D: 20 09 25        JSR     $2509               ; {code.broadcastByteToStateBlock} broadcast that byte through the state block

loc_2650:
2650: 20 72 28        JSR     $2872               ; {code.initRoundState} run the full round setup
2653: 4C B8 26        JMP     $26B8               ; {code.drawGridSideBorders} go draw the grid side borders

loadPaletteRecordPair:
2656: BD 76 26        LDA     $2676,X             ; {hard.rom+676} read palette record byte b0 from the ROM table
2659: 48              PHA                         ; save b0 on the stack
265A: BD 77 26        LDA     $2677,X             ; {hard.rom+677} read palette record byte b1
265D: A8              TAY                         ; hold b1 in Y
265E: BD 78 26        LDA     $2678,X             ; {hard.rom+678} read palette record byte b2
2661: AA              TAX                         ; hold b2 in X
2662: 68              PLA                         ; recover b0
2663: 8E 0E 14        STX     $140E               ; {hard.paletteRam+E} write b2 into palette cell 0x0E
2666: 8E 06 14        STX     $1406               ; {hard.paletteRam+6} write b2 into palette cell 0x06
2669: 8D 0F 14        STA     $140F               ; {hard.paletteRam+F} write b0 into palette cell 0x0F
266C: 8D 05 14        STA     $1405               ; {hard.paletteRam+5} write b0 into palette cell 0x05
266F: 8C 0D 14        STY     $140D               ; {hard.paletteRam+D} write b1 into palette cell 0x0D
2672: 8C 07 14        STY     $1407               ; {hard.paletteRam+7} write b1 into palette cell 0x07
2675: 60              RTS                         ; return

; ---- $2676-$269F: data ----
2676: 0D 00 0E 02 04 01 0E 01 0C 04 01 0B 01 0C 0A 09
2686: 0B 04 0C 0D 0A 09 0C 0E 0A 0E 01 0B 01 04 01 00
2696: 06 0D 0E 0A 0E 0C 0B 00 0D 02

copyZpStateToSnapshot:
26A0: A9 FF           LDA     #$FF                ; all-ones
26A2: 85 C1           STA     $C1                 ; {hard.workRam+C1} mark object slot $c1 idle
26A4: 85 C2           STA     $C2                 ; {hard.workRam+C2} mark object slot $c2 idle
26A6: A2 08           LDX     #$08                ; nine cells to copy

loc_26a8:
26A8: B5 02           LDA     $02,X               ; {hard.workRam+2} read working cell $02+x
26AA: 9D 78 01        STA     $0178,X             ; {hard.workRam+178} copy it into the high-score table mirror at 0x178+x
26AD: B5 1A           LDA     $1A,X               ; {hard.workRam+1A} read working cell $1a+x
26AF: 9D 81 01        STA     $0181,X             ; {hard.workRam+181} copy it into the high-score mirror at 0x181+x
26B2: CA              DEX                         ; step the index down
26B3: 10 F3           BPL     $26A8               ; {code.loc_26a8} loop over the block
26B5: 4C 08 3A        JMP     $3A08               ; {code.foldHighScoreChecksum} fold the high-score checksum and return

drawGridSideBorders:
26B8: A9 06           LDA     #$06                ; six rows to draw
26BA: 85 8B           STA     $8B                 ; {hard.workRam+8B} set the row loop count in $8b
26BC: A9 04           LDA     #$04                ; base high byte
26BE: 45 F7           EOR     $F7                 ; {hard.workRam+F7} fold with the flip byte $f7
26C0: 29 06           AND     #$06                ; keep the low bits
26C2: 85 92           STA     $92                 ; {hard.workRam+92} set the draw cursor high byte $92
26C4: A9 DF           LDA     #$DF                ; base low byte
26C6: 45 F6           EOR     $F6                 ; {hard.workRam+F6} fold with the flip byte $f6
26C8: 85 91           STA     $91                 ; {hard.workRam+91} set the draw cursor low byte $91
26CA: A6 A5           LDX     $A5                 ; {hard.workRam+A5} load the slot count $a5 as the row index

loc_26cc:
26CC: A9 1F           LDA     #$1F                ; left-border glyph
26CE: CA              DEX                         ; step the index down
26CF: 10 02           BPL     $26D3               ; {code.loc_26d3} still in range -- draw the border glyph
26D1: A9 00           LDA     #$00                ; past the count -- blank this cell instead

loc_26d3:
26D3: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot the cell and advance the cursor
26D6: C6 8B           DEC     $8B                 ; {hard.workRam+8B} tick the row counter down
26D8: D0 F2           BNE     $26CC               ; {code.loc_26cc} loop the left border column
26DA: A9 06           LDA     #$06                ; base high byte
26DC: 45 F7           EOR     $F7                 ; {hard.workRam+F7} fold with the flip byte $f7
26DE: 85 92           STA     $92                 ; {hard.workRam+92} set the draw cursor high byte $92
26E0: A9 5F           LDA     #$5F                ; base low byte
26E2: 45 F6           EOR     $F6                 ; {hard.workRam+F6} fold with the flip byte $f6
26E4: 85 91           STA     $91                 ; {hard.workRam+91} set the draw cursor low byte $91
26E6: A9 06           LDA     #$06                ; six rows again
26E8: 85 8B           STA     $8B                 ; {hard.workRam+8B} set the row loop count in $8b
26EA: 38              SEC                         ; prepare for subtraction
26EB: E5 A6           SBC     $A6                 ; {hard.workRam+A6} subtract the slot timer $a6
26ED: AA              TAX                         ; use the result as the row index

loc_26ee:
26EE: A9 00           LDA     #$00                ; blank cell
26F0: CA              DEX                         ; step the index down
26F1: 10 02           BPL     $26F5               ; {code.loc_26f5} still in range -- blank this cell
26F3: A9 1F           LDA     #$1F                ; past the count -- draw the right-border glyph

loc_26f5:
26F5: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot the cell and advance the cursor
26F8: C6 8B           DEC     $8B                 ; {hard.workRam+8B} tick the row counter down
26FA: D0 F2           BNE     $26EE               ; {code.loc_26ee} loop the right border column
26FC: 60              RTS                         ; return

serviceTimerBank:
26FD: A2 0D           LDX     #$0D                ; start at the top timer slot 0x0d

loc_26ff:
26FF: B4 34           LDY     $34,X               ; {hard.workRam+34} read the countdown byte $34+x
2701: C0 F9           CPY     #$F9                ; compare against 0xF9
2703: 90 18           BCC     $271D               ; {code.loc_271d} below it -- this timer is resting, skip it
2705: C0 FA           CPY     #$FA                ; compare against 0xFA
2707: 90 04           BCC     $270D               ; {code.loc_270d} exactly 0xF9 -- just expired, don't decrement
2709: D6 34           DEC     $34,X               ; {hard.workRam+34} live countdown -- tick it down one step toward the 0xf9 expiry marker
270B: D0 10           BNE     $271D               ; {code.loc_271d} not expired this pass -- skip

loc_270d:
270D: E0 0D           CPX     #$0D                ; is this the master slot?
270F: D0 0C           BNE     $271D               ; {code.loc_271d} not the master -- skip the re-arm
2711: A5 43           LDA     $43                 ; {hard.workRam+43} read the frame/step counter $43
2713: 29 AF           AND     #$AF                ; mask it
2715: D0 06           BNE     $271D               ; {code.loc_271d} busy -- skip the re-arm
2717: A5 D7           LDA     $D7                 ; {hard.workRam+D7} read $d7
2719: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it with $ef
271B: 85 41           STA     $41                 ; {hard.workRam+41} refresh the shared timing key $41

loc_271d:
271D: CA              DEX                         ; step to the next timer slot
271E: 10 DF           BPL     $26FF               ; {code.loc_26ff} loop the timer bank
2720: A5 43           LDA     $43                 ; {hard.workRam+43} read the frame/step counter $43
2722: 29 AF           AND     #$AF                ; mask it
2724: F0 1A           BEQ     $2740               ; {code.loc_2740} inactive -- stop here
2726: A5 00           LDA     $00                 ; {hard.workRam} read the frame cell $00
2728: 29 03           AND     #$03                ; only every fourth frame
272A: D0 14           BNE     $2740               ; {code.loc_2740} not this frame -- stop
272C: A5 43           LDA     $43                 ; {hard.workRam+43} read the step counter $43
272E: C9 28           CMP     #$28                ; compare against the 0x28 ceiling
2730: B0 0E           BCS     $2740               ; {code.loc_2740} reached the ceiling -- stop
2732: E6 43           INC     $43                 ; {hard.workRam+43} advance the step counter
2734: C9 27           CMP     #$27                ; was the pre-step value the 0x27 top?
2736: D0 08           BNE     $2740               ; {code.loc_2740} not the top -- done
2738: A9 00           LDA     #$00                ; zero
273A: 85 DA           STA     $DA                 ; {hard.workRam+DA} seed the field-scan pointer low byte
273C: A9 04           LDA     #$04                ; page 4
273E: 85 DB           STA     $DB                 ; {hard.workRam+DB} seed the field-scan pointer high byte, aiming the scan at 0x0400

loc_2740:
2740: 60              RTS                         ; return

loc_2741:
2741: A5 C1           LDA     $C1                 ; {hard.workRam+C1} read object-active flag $c1
2743: 25 C2           AND     $C2                 ; {hard.workRam+C2} AND it with object-active flag $c2
2745: 10 01           BPL     $2748               ; {code.loc_2748} at least one object is live -- go do the frame's work
2747: 60              RTS                         ; both objects idle -- return, telling the caller to run the full chain

loc_2748:
2748: A5 C2           LDA     $C2                 ; {hard.workRam+C2} read object-active flag $c2
274A: 30 18           BMI     $2764               ; {code.loc_2764} no live object in this slot ($c2 idle) -- branch onward
274C: A5 EE           LDA     $EE                 ; {hard.workRam+EE} read the pending flag $ee
274E: 10 14           BPL     $2764               ; {code.loc_2764} not pending -- branch onward
2750: A5 EF           LDA     $EF                 ; {hard.workRam+EF} read the pending flag $ef
2752: D0 10           BNE     $2764               ; {code.loc_2764} set -- branch onward
2754: A9 82           LDA     #$82                ; value 0x82
2756: 85 EE           STA     $EE                 ; {hard.workRam+EE} set the pending flag $ee to it, kicking a fresh screen/wave setup
2758: 20 2A 25        JSR     $252A               ; {code.seedStateBlockConstants} seed the state-block constants
275B: 20 D5 31        JSR     $31D5               ; {code.transposeScreenBitmap} transpose the screen bitmap
275E: 20 FE 32        JSR     $32FE               ; {code.plotObjectCoordinates} plot the object coordinates
2761: 20 32 29        JSR     $2932               ; {code.seedPlayerShotStartCells} reseed the player-shot start cells

loc_2764:
2764: A5 89           LDA     $89                 ; {hard.workRam+89} read the slot count/index
2766: 4A              LSR     A                   ; shift it right, testing the low bit
2767: F0 14           BEQ     $277D               ; {code.loc_277d} nothing there -- skip painting the slot glyph
2769: A9 00           LDA     #$00                ; pick layout-row selector 0
276B: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw that status row
276E: A0 02           LDY     #$02                ; default the glyph index to 2
2770: A6 C2           LDX     $C2                 ; {hard.workRam+C2} read the object's angle/active cell
2772: 10 01           BPL     $2775               ; {code.loc_2775} positive -- keep index 2
2774: 88              DEY                         ; negative object -- drop the index to 1

loc_2775:
2775: 84 88           STY     $88                 ; {hard.workRam+88} stash the chosen slot selector
2777: 98              TYA                         ; move it into A
2778: 09 20           ORA     #$20                ; fold in bit 5 to make it a glyph code
277A: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot that slot glyph through the draw cursor

loc_277d:
277D: A9 08           LDA     #$08                ; pick layout-row selector 8
277F: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw that status row
2782: A9 05           LDA     #$05                ; pick layout-row selector 5
2784: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw that status row
2787: A9 89           LDA     #$89                ; start from constant 0x89
2789: 45 F5           EOR     $F5                 ; {hard.workRam+F5} mirror it against the flip byte
278B: 85 91           STA     $91                 ; {hard.workRam+91} seat the draw cursor low byte
278D: A9 05           LDA     #$05                ; start from constant 0x05
278F: 45 F7           EOR     $F7                 ; {hard.workRam+F7} mirror it against the other flip byte
2791: 85 92           STA     $92                 ; {hard.workRam+92} seat the draw cursor high byte
2793: A6 88           LDX     $88                 ; {hard.workRam+88} load the slot selector
2795: B4 C0           LDY     $C0,X               ; {hard.workRam+C0} read this slot's spawn-column counter
2797: 84 8D           STY     $8D                 ; {hard.workRam+8D} stash it as the record index
2799: 98              TYA                         ; move it into A
279A: 18              CLC                         ; clear carry for the add
279B: 65 C0           ADC     $C0                 ; {hard.workRam+C0} add the counter base
279D: 85 8E           STA     $8E                 ; {hard.workRam+8E} store the record's base offset
279F: 20 33 38        JSR     $3833               ; {code.plotZpTableByteAtCursor} plot the record's first field byte
27A2: A4 8D           LDY     $8D                 ; {hard.workRam+8D} reload the record index
27A4: C8              INY                         ; step to the next field
27A5: 20 33 38        JSR     $3833               ; {code.plotZpTableByteAtCursor} plot the record's second field byte
27A8: A4 8D           LDY     $8D                 ; {hard.workRam+8D} reload the record index
27AA: C8              INY                         ; step past the first field
27AB: C8              INY                         ; step to the third field
27AC: 20 33 38        JSR     $3833               ; {code.plotZpTableByteAtCursor} plot the record's third field byte
27AF: AD 01 0C        LDA     $0C01               ; {hard.in1} read the IN1 control port
27B2: A6 EF           LDX     $EF                 ; {hard.workRam+EF} check the spawn-pending/orientation flag
27B4: F0 01           BEQ     $27B7               ; {code.loc_27b7} no pending -- leave the bit where it is
27B6: 4A              LSR     A                   ; shift once to bring bit 2 into place

loc_27b7:
27B7: 4A              LSR     A                   ; shift the input bit down
27B8: 4A              LSR     A                   ; shift again
27B9: 4A              LSR     A                   ; shift again into carry
27BA: 26 9A           ROL     $9A                 ; {hard.workRam+9A} roll that input bit into the phase accumulator
27BC: A5 9A           LDA     $9A                 ; {hard.workRam+9A} read the phase accumulator back
27BE: 29 1F           AND     #$1F                ; keep its low five phase bits
27C0: C9 18           CMP     #$18                ; compare against the top of the phase cycle
27C2: D0 46           BNE     $280A               ; {code.loc_280a} not at the top -- skip the column advance
27C4: E6 C0           INC     $C0                 ; {hard.workRam+C0} advance this object's spawn-column counter
27C6: A5 C0           LDA     $C0                 ; {hard.workRam+C0} read the counter
27C8: C9 03           CMP     #$03                ; compare it to three
27CA: 90 32           BCC     $27FE               ; {code.loc_27fe} still below the wrap -- re-arm one lane cell

loc_27cc:
27CC: A6 88           LDX     $88                 ; {hard.workRam+88} load the slot selector
27CE: A9 FF           LDA     #$FF                ; value 0xff
27D0: 95 C0           STA     $C0,X               ; {hard.workRam+C0} mark this spawn-column counter spent
27D2: A5 EF           LDA     $EF                 ; {hard.workRam+EF} read the spawn-pending flag
27D4: F0 1D           BEQ     $27F3               ; {code.loc_27f3} nothing pending -- skip the full respawn
27D6: A9 80           LDA     #$80                ; value 0x80
27D8: 85 EE           STA     $EE                 ; {hard.workRam+EE} raise the pending-spawn flag
27DA: 20 09 25        JSR     $2509               ; {code.broadcastByteToStateBlock} broadcast 0x80 across the state block
27DD: 20 D5 31        JSR     $31D5               ; {code.transposeScreenBitmap} rotate the tile grid
27E0: 20 32 29        JSR     $2932               ; {code.seedPlayerShotStartCells} reseed the player-shot start cells
27E3: 20 FE 32        JSR     $32FE               ; {code.plotObjectCoordinates} redraw the object coordinates
27E6: 20 1F 23        JSR     $231F               ; {code.rebuildSegmentSpriteTables} rebuild the segment sprite tables
27E9: 20 C7 21        JSR     $21C7               ; {code.seedSegmentSpawnState} seed the segment spawn state
27EC: 20 E8 20        JSR     $20E8               ; {code.seedWaveState} seed the wave state
27EF: A5 C1           LDA     $C1                 ; {hard.workRam+C1} read the object-active flag
27F1: 30 32           BMI     $2825               ; {code.loc_2825} object idle -- jump to the frame tail

loc_27f3:
27F3: A5 C1           LDA     $C1                 ; {hard.workRam+C1} read the object-active flag
27F5: 25 C2           AND     $C2                 ; {hard.workRam+C2} AND with the second active flag
27F7: 30 17           BMI     $2810               ; {code.loc_2810} both idle -- take the setup branch

loc_27f9:
27F9: A2 00           LDX     #$00                ; index zero
27FB: 86 C0           STX     $C0                 ; {hard.workRam+C0} clear this spawn-column counter
27FD: 60              RTS                         ; return

loc_27fe:
27FE: E6 8E           INC     $8E                 ; {hard.workRam+8E} bump the record offset
2800: A6 8E           LDX     $8E                 ; {hard.workRam+8E} load it as the lane index
2802: A9 F4           LDA     #$F4                ; value 0xf4
2804: 85 01           STA     $01                 ; {hard.workRam+1} stash it in the run flag
2806: A9 01           LDA     #$01                ; value 1
2808: 95 1A           STA     $1A,X               ; {hard.workRam+1A} re-arm this lane cell to 1

loc_280a:
280A: A5 01           LDA     $01                 ; {hard.workRam+1} read the run flag
280C: F0 BE           BEQ     $27CC               ; {code.loc_27cc} clear -- loop back to mark the slot spent
280E: D0 2E           BNE     $283E               ; {code.loc_283e} set -- jump into the per-frame move body

loc_2810:
2810: A9 88           LDA     #$88                ; pick layout-row selector 0x88
2812: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw that status row
2815: A9 85           LDA     #$85                ; pick layout-row selector 0x85
2817: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw that status row
281A: A9 00           LDA     #$00                ; value 0
281C: 8D 89 05        STA     $0589               ; {hard.videoRam+189} clear the first sprite-shadow cell
281F: 8D A9 05        STA     $05A9               ; {hard.videoRam+1A9} clear the second sprite-shadow cell
2822: 8D C9 05        STA     $05C9               ; {hard.videoRam+1C9} clear the third sprite-shadow cell

loc_2825:
2825: 20 A0 26        JSR     $26A0               ; {code.copyZpStateToSnapshot} refresh the state snapshot for the checksum
2828: 20 5C 2D        JSR     $2D5C               ; {code.plotRecordFieldColumns} redraw the sorted-object record columns
282B: A6 89           LDX     $89                 ; {hard.workRam+89} read the slot count
282D: 86 01           STX     $01                 ; {hard.workRam+1} store it in the run flag
282F: CA              DEX                         ; decrement it
2830: F0 C7           BEQ     $27F9               ; {code.loc_27f9} only one slot left -- return
2832: A9 80           LDA     #$80                ; pick layout-row selector 0x80
2834: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw that status row
2837: A9 00           LDA     #$00                ; value 0
2839: A8              TAY                         ; clear the row index
283A: 91 91           STA     ($91),Y             ; {hard.workRam+91} write a blank through the draw cursor
283C: F0 BB           BEQ     $27F9               ; {code.loc_27f9} return

loc_283e:
283E: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter
2840: 29 07           AND     #$07                ; keep its low three bits
2842: D0 2B           BNE     $286F               ; {code.loc_286f} not this frame -- exit with nothing to do
2844: A2 FF           LDX     #$FF                ; direction sign 0xff (negative)
2846: A9 00           LDA     #$00                ; value 0
2848: A4 B9           LDY     $B9                 ; {hard.workRam+B9} read the trackball accumulator
284A: 85 B9           STA     $B9                 ; {hard.workRam+B9} clear the accumulator
284C: 10 07           BPL     $2855               ; {code.loc_2855} positive -- keep the positive direction
284E: A2 01           LDX     #$01                ; direction sign 1 (positive)
2850: 98              TYA                         ; move the accumulator into A
2851: 20 2D 38        JSR     $382D               ; {code.negateA} take its magnitude
2854: A8              TAY                         ; back into the magnitude index

loc_2855:
2855: C0 04           CPY     #$04                ; compare the magnitude to four
2857: 90 16           BCC     $286F               ; {code.loc_286f} too small -- no lane nudge this pass
2859: 8A              TXA                         ; move the direction sign into A
285A: 45 F4           EOR     $F4                 ; {hard.workRam+F4} mirror it against the flip byte
285C: A6 8E           LDX     $8E                 ; {hard.workRam+8E} load the lane record offset
285E: 18              CLC                         ; clear carry for the add
285F: 75 1A           ADC     $1A,X               ; {hard.workRam+1A} add the object's current lane value
2861: 30 08           BMI     $286B               ; {code.loc_286b} wrapped below zero -- go set the lane to the top of the band (0x1a)
2863: C9 1B           CMP     #$1B                ; compare against the high rail
2865: 90 06           BCC     $286D               ; {code.loc_286d} inside the band -- store it
2867: A9 00           LDA     #$00                ; past the top -- clamp to 0
2869: F0 02           BEQ     $286D               ; {code.loc_286d} go store the clamp

loc_286b:
286B: A9 1A           LDA     #$1A                ; past the bottom -- clamp to 0x1a

loc_286d:
286D: 95 1A           STA     $1A,X               ; {hard.workRam+1A} store the object's new lane value

loc_286f:
286F: A9 00           LDA     #$00                ; return value 0 (skip the rest of the frame)
2871: 60              RTS                         ; return

initRoundState:
2872: A9 20           LDA     #$20                ; value 0x20
2874: 8D 08 10        STA     $1008               ; {hard.pokey+8} arm the POKEY audio-control latch for a fresh round
2877: A9 0C           LDA     #$0C                ; value 0x0c
2879: 85 9B           STA     $9B                 ; {hard.workRam+9B} seed the first round countdown
287B: 85 9C           STA     $9C                 ; {hard.workRam+9C} seed the second round countdown
287D: A5 FF           LDA     $FF                 ; {hard.workRam+FF} take one random snapshot byte
287F: 85 88           STA     $88                 ; {hard.workRam+88} seed the slot index from it
2881: 85 53           STA     $53                 ; {hard.workRam+53} mirror that seed to its first consumer
2883: 85 83           STA     $83                 ; {hard.workRam+83} mirror that seed to its second consumer
2885: A9 02           LDA     #$02                ; value 2
2887: 85 9D           STA     $9D                 ; {hard.workRam+9D} seed the first round step
2889: 85 9E           STA     $9E                 ; {hard.workRam+9E} seed the second round step
288B: A2 06           LDX     #$06                ; sweep index for seven timer cells
288D: A9 00           LDA     #$00                ; value 0
288F: 8D 0F 10        STA     $100F               ; {hard.pokey+F} silence the POKEY serial/keyboard-control register

loc_2892:
2892: 95 B2           STA     $B2,X               ; {hard.workRam+B2} clear one SFX timer-bank cell
2894: CA              DEX                         ; step the sweep index down
2895: 10 FB           BPL     $2892               ; {code.loc_2892} loop for the whole SFX timer bank
2897: A2 05           LDX     #$05                ; sweep index for six slot-table cells

loc_2899:
2899: 95 A8           STA     $A8,X               ; {hard.workRam+A8} clear one slot-table cell
289B: CA              DEX                         ; step the sweep index down
289C: 10 FB           BPL     $2899               ; {code.loc_2899} loop for the whole slot table
289E: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
28A1: 4D 0A 10        EOR     $100A               ; {hard.pokey+A} XOR a second read (self-cancelling mix)
28A4: 18              CLC                         ; clear carry for the add
28A5: 65 C8           ADC     $C8                 ; {hard.workRam+C8} fold it into the object counter
28A7: 85 C8           STA     $C8                 ; {hard.workRam+C8} store the object counter
28A9: A9 03           LDA     #$03                ; value 3
28AB: 8D 0F 10        STA     $100F               ; {hard.pokey+F} bring the POKEY serial-control register back up
28AE: 20 1F 23        JSR     $231F               ; {code.rebuildSegmentSpriteTables} rebuild the segment sprite tables
28B1: A9 C0           LDA     #$C0                ; value 0xc0
28B3: 85 A0           STA     $A0                 ; {hard.workRam+A0} arm the spawn timer
28B5: 85 A2           STA     $A2                 ; {hard.workRam+A2} arm its first companion timer
28B7: 85 A3           STA     $A3                 ; {hard.workRam+A3} arm its second companion timer
28B9: 20 C7 21        JSR     $21C7               ; {code.seedSegmentSpawnState} seed the segment spawn state
28BC: 20 E8 20        JSR     $20E8               ; {code.seedWaveState} seed the wave state

resetPlayfieldAndSeedMushrooms:
28BF: A9 0F           LDA     #$0F                ; value 0x0f
28C1: 8D 04 14        STA     $1404               ; {hard.paletteRam+4} write the fixed playfield colour value
28C4: A6 88           LDX     $88                 ; {hard.workRam+88} load the slot selector
28C6: A9 00           LDA     #$00                ; value 0
28C8: 95 C2           STA     $C2,X               ; {hard.workRam+C2} clear this slot's angle/active cell
28CA: AA              TAX                         ; zero the palette-record index
28CB: 20 56 26        JSR     $2656               ; {code.loadPaletteRecordPair} fan the first palette record into the palette cells
28CE: A2 00           LDX     #$00                ; zero the video-page index
28D0: 8A              TXA                         ; value 0 to store

loc_28d1:
28D1: 9D 00 04        STA     $0400,X             ; {hard.videoRam} blank one byte of the first video page
28D4: 9D 00 05        STA     $0500,X             ; {hard.videoRam+100} blank the matching byte of the second page
28D7: 9D 00 06        STA     $0600,X             ; {hard.videoRam+200} blank the matching byte of the third page
28DA: 9D 00 07        STA     $0700,X             ; {hard.videoRam+300} blank the matching byte of the fourth page
28DD: E8              INX                         ; step to the next byte
28DE: D0 F1           BNE     $28D1               ; {code.loc_28d1} loop across all 256 bytes of the four pages
28E0: A6 88           LDX     $88                 ; {hard.workRam+88} load the slot selector
28E2: 95 D7           STA     $D7,X               ; {hard.workRam+D7} clear this slot's per-column mushroom tally
28E4: A2 1B           LDX     #$1B                ; value 0x1b
28E6: 86 8B           STX     $8B                 ; {hard.workRam+8B} seed the cycling column stride
28E8: A2 2D           LDX     #$2D                ; outer counter -- 46 columns to seed

loc_28ea:
28EA: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
28ED: 29 E0           AND     #$E0                ; keep its top three bits
28EF: 05 8B           ORA     $8B                 ; {hard.workRam+8B} fold in the cycling column stride
28F1: 85 8D           STA     $8D                 ; {hard.workRam+8D} store the mushroom cell pointer low byte
28F3: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register again
28F6: 29 03           AND     #$03                ; keep its low two bits
28F8: 09 04           ORA     #$04                ; force the video-page bits
28FA: 85 8E           STA     $8E                 ; {hard.workRam+8E} store the mushroom cell pointer high byte
28FC: 86 8F           STX     $8F                 ; {hard.workRam+8F} stash the outer column counter
28FE: A0 00           LDY     #$00                ; clear the cell index
2900: A5 8D           LDA     $8D                 ; {hard.workRam+8D} read the pointer low byte
2902: 29 1F           AND     #$1F                ; keep its low five column bits
2904: A6 EF           LDX     $EF                 ; {hard.workRam+EF} check the orientation flag
2906: F0 06           BEQ     $290E               ; {code.loc_290e} upright -- take the low-threshold test
2908: C9 14           CMP     #$14                ; compare the column against 0x14
290A: 90 0E           BCC     $291A               ; {code.loc_291a} below it -- skip the tally bump
290C: B0 04           BCS     $2912               ; {code.loc_2912} at or above -- go test the cell

loc_290e:
290E: C9 0C           CMP     #$0C                ; compare the column against 0x0c
2910: B0 08           BCS     $291A               ; {code.loc_291a} at or above -- skip the tally bump

loc_2912:
2912: B1 8D           LDA     ($8D),Y             ; {hard.workRam+8D} read the cell at the mushroom pointer
2914: D0 04           BNE     $291A               ; {code.loc_291a} already occupied -- skip the tally bump
2916: A6 88           LDX     $88                 ; {hard.workRam+88} load the slot selector
2918: F6 D7           INC     $D7,X               ; {hard.workRam+D7} bump this slot's per-column mushroom tally

loc_291a:
291A: A9 3F           LDA     #$3F                ; load the mushroom glyph base 0x3f
291C: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold in the orientation mask $ef so the mushroom mirrors for a flipped cabinet
291E: 91 8D           STA     ($8D),Y             ; {hard.workRam+8D} stamp the mushroom into the cell the random field pointer $8d/$8e is sitting on
2920: A5 8B           LDA     $8B                 ; {hard.workRam+8B} read the cycling column-stride byte $8b
2922: 38              SEC                         ; set carry for the subtract
2923: E9 01           SBC     #$01                ; step the stride down by one
2925: C9 02           CMP     #$02                ; has the stride fallen below 0x02?
2927: B0 02           BCS     $292B               ; {code.loc_292b} still 0x02 or more -- keep it
2929: A9 1B           LDA     #$1B                ; wrapped -- reload the stride to 0x1b

loc_292b:
292B: 85 8B           STA     $8B                 ; {hard.workRam+8B} store the column stride back
292D: A6 8F           LDX     $8F                 ; {hard.workRam+8F} load the outer mushroom-column counter $8f
292F: CA              DEX                         ; step to the previous column
2930: 10 B8           BPL     $28EA               ; {code.loc_28ea} more columns left -- loop back to the top of the mushroom sweep

seedPlayerShotStartCells:
2932: A9 10           LDA     #$10                ; load the shot-start seed 0x10
2934: 45 F2           EOR     $F2                 ; {hard.workRam+F2} fold in orientation byte $f2 so the launch coord mirrors for a flipped cabinet
2936: 85 43           STA     $43                 ; {hard.workRam+43} seed the player/shot start cell $43
2938: A9 80           LDA     #$80                ; load the screen-midline coordinate 0x80
293A: 85 63           STA     $63                 ; {hard.workRam+63} seed the $63-axis coordinate to the midline
293C: 85 62           STA     $62                 ; {hard.workRam+62} mirror the midline into $62
293E: A9 08           LDA     #$08                ; load the shot-start seed 0x08
2940: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold in orientation byte $f0
2942: 85 73           STA     $73                 ; {hard.workRam+73} seed the $73-axis start cell
2944: A9 0C           LDA     #$0C                ; load the start seed 0x0c
2946: 45 F1           EOR     $F1                 ; {hard.workRam+F1} fold in orientation byte $f1
2948: 85 72           STA     $72                 ; {hard.workRam+72} seed start cell $72
294A: A9 11           LDA     #$11                ; load the start seed 0x11
294C: 45 F2           EOR     $F2                 ; {hard.workRam+F2} fold in orientation byte $f2
294E: 85 42           STA     $42                 ; {hard.workRam+42} seed start cell $42
2950: 60              RTS                         ; return from the shot/start seeding

beginCentipedeSegmentSweep:
2951: A5 87           LDA     $87                 ; {hard.workRam+87} read the death/respawn countdown gate $87
2953: F0 01           BEQ     $2956               ; {code.loc_2956} gate clear -- run the centipede segment sweep
2955: 60              RTS                         ; still counting down -- skip the sweep this frame

loc_2956:
2956: A2 0B           LDX     #$0B                ; seed the segment cursor at the last slot 0x0b
2958: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter $00
295A: 29 0F           AND     #$0F                ; keep its low nibble
295C: D0 04           BNE     $2962               ; {code.moveCentipedeSegment} not a footstep frame -- drop straight into the mover
295E: A9 07           LDA     #$07                ; load the marching-footstep interval 0x07
2960: 85 B3           STA     $B3                 ; {hard.workRam+B3} arm the channel-2 SFX timer with the footstep tick

moveCentipedeSegment:
2962: B5 34           LDA     $34,X               ; {hard.workRam+34} read this slot's phase/state byte loc_34+x
2964: 10 03           BPL     $2969               ; {code.loc_2969} live segment (bit 7 clear) -- move it
2966: 4C C7 2A        JMP     $2AC7               ; {code.advanceSegmentLoopIndex} retired slot -- jump to the loop tail

loc_2969:
2969: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter $00
296B: 29 01           AND     #$01                ; keep its low bit
296D: D0 09           BNE     $2978               ; {code.loc_2978} odd frame -- skip the phase bump
296F: B5 34           LDA     $34,X               ; {hard.workRam+34} read the phase byte again
2971: 18              CLC                         ; clear carry for the add
2972: 69 01           ADC     #$01                ; bump the segment phase by one
2974: 29 F7           AND     #$F7                ; keep phase bit 3 clear
2976: 95 34           STA     $34,X               ; {hard.workRam+34} store the advanced phase

loc_2978:
2978: A0 01           LDY     #$01                ; set Y to 1, the on-home-column marker value
297A: B5 64           LDA     $64,X               ; {hard.workRam+64} read the segment's coordinate loc_64+x
297C: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold in orientation $f0
297E: C9 09           CMP     #$09                ; is the coordinate near the edge (below 0x09)?
2980: B0 0A           BCS     $298C               ; {code.loc_298c} not near the edge -- skip the edge classification
2982: B5 34           LDA     $34,X               ; {hard.workRam+34} read the phase byte
2984: C9 10           CMP     #$10                ; is the phase below 0x10?
2986: B0 02           BCS     $298A               ; {code.loc_298a} phase already 0x10 or more -- skip the flag
2988: 84 97           STY     $97                 ; {hard.workRam+97} flag this near-edge low-phase segment into loc_97

loc_298a:
298A: B5 64           LDA     $64,X               ; {hard.workRam+64} reload the coordinate loc_64+x

loc_298c:
298C: 29 07           AND     #$07                ; keep the low 3 bits of the coordinate
298E: D0 73           BNE     $2A03               ; {code.loc_2a03} not grid-aligned -- take the coordinate-advance path
2990: 98              TYA                         ; A = the home marker value 1
2991: A4 88           LDY     $88                 ; {hard.workRam+88} load the active object slot index $88
2993: D9 94 00        CMP     $0094,Y             ; {hard.workRam+94} compare with the home-column flag loc_94 for this slot
2996: D0 14           BNE     $29AC               ; {code.loc_29ac} not on its home column -- skip the heading re-seed
2998: A9 02           LDA     #$02                ; default heading delta +2
299A: B4 44           LDY     $44,X               ; {hard.workRam+44} test the current delta loc_44+x sign
299C: 10 02           BPL     $29A0               ; {code.loc_29a0} positive -- keep +2
299E: A9 FE           LDA     #$FE                ; negative -- use -2 instead

loc_29a0:
29A0: 95 44           STA     $44,X               ; {hard.workRam+44} store the re-seeded heading delta loc_44+x
29A2: A9 02           LDA     #$02                ; default +2 for the other axis
29A4: B4 74           LDY     $74,X               ; {hard.workRam+74} test the link/delta loc_74+x sign
29A6: 10 02           BPL     $29AA               ; {code.loc_29aa} positive -- keep +2
29A8: A9 FE           LDA     #$FE                ; negative -- use -2 instead

loc_29aa:
29AA: 95 74           STA     $74,X               ; {hard.workRam+74} store the re-seeded link loc_74+x

loc_29ac:
29AC: B5 34           LDA     $34,X               ; {hard.workRam+34} read the phase byte
29AE: 29 40           AND     #$40                ; test bit 6, the distance-check branch flag
29B0: F0 0F           BEQ     $29C1               ; {code.loc_29c1} bit 6 clear -- take the wall-band branch
29B2: B5 63           LDA     $63,X               ; {hard.workRam+63} read the reference coordinate loc_63+x
29B4: 38              SEC                         ; set carry for the subtract
29B5: F5 64           SBC     $64,X               ; {hard.workRam+64} distance = loc_63+x minus loc_64+x
29B7: 20 2B 38        JSR     $382B               ; {code.foldSignedMagnitude} fold the distance to its magnitude
29BA: C9 08           CMP     #$08                ; is the distance 8 or more?
29BC: B0 45           BCS     $2A03               ; {code.loc_2a03} too far -- take the coordinate-advance path

loc_29be:
29BE: 4C 92 2A        JMP     $2A92               ; {code.advanceSegmentCoordAndArm} near -- jump to advance the coordinate and arm

loc_29c1:
29C1: B5 34           LDA     $34,X               ; {hard.workRam+34} read the phase byte
29C3: 29 20           AND     #$20                ; test bit 5, the straight-to-edge shortcut flag
29C5: D0 3C           BNE     $2A03               ; {code.loc_2a03} shortcut set -- take the coordinate-advance path
29C7: B5 54           LDA     $54,X               ; {hard.workRam+54} read the segment coordinate loc_54+x
29C9: C9 F0           CMP     #$F0                ; near the high wall (0xf0 or more)?
29CB: 90 0A           BCC     $29D7               ; {code.loc_29d7} below it -- check the low wall band
29CD: B4 74           LDY     $74,X               ; {hard.workRam+74} read the link loc_74+x
29CF: F0 0E           BEQ     $29DF               ; {code.loc_29df} no link -- jump to reverse the delta and turn
29D1: B4 44           LDY     $44,X               ; {hard.workRam+44} read the delta loc_44+x
29D3: 10 2E           BPL     $2A03               ; {code.loc_2a03} delta positive -- take the coordinate-advance path
29D5: 30 0F           BMI     $29E6               ; {code.loc_29e6} delta negative -- probe the tile ahead

loc_29d7:
29D7: C9 10           CMP     #$10                ; near the low wall (below 0x10)?
29D9: B0 0B           BCS     $29E6               ; {code.loc_29e6} not near a wall -- probe the tile ahead
29DB: B4 74           LDY     $74,X               ; {hard.workRam+74} read the link loc_74+x
29DD: D0 03           BNE     $29E2               ; {code.loc_29e2} link set -- check the delta sign

loc_29df:
29DF: 4C A6 2A        JMP     $2AA6               ; {code.reverseSegmentDeltaAndStepCoord} jump to reverse the delta and step the coordinate

loc_29e2:
29E2: B4 44           LDY     $44,X               ; {hard.workRam+44} read the delta loc_44+x
29E4: 30 1D           BMI     $2A03               ; {code.loc_2a03} delta negative -- take the coordinate-advance path

loc_29e6:
29E6: 20 10 23        JSR     $2310               ; {code.loadObjectTileInputs} marshal this object's tile-probe inputs
29E9: 20 2B 2C        JSR     $2C2B               ; {code.resolveTileCellAtXY} resolve the tile cell the segment faces
29EC: F0 10           BEQ     $29FE               ; {code.loc_29fe} empty cell -- run the column-collision check
29EE: C9 38           CMP     #$38                ; occupied: below the solid band (below 0x38)?
29F0: 90 11           BCC     $2A03               ; {code.loc_2a03} not a wall tile -- take the coordinate-advance path
29F2: C9 3C           CMP     #$3C                ; is the tile at or above 0x3c?
29F4: B0 0D           BCS     $2A03               ; {code.loc_2a03} above the mushroom band -- take the coordinate-advance path
29F6: B5 34           LDA     $34,X               ; {hard.workRam+34} mushroom-band tile: read the phase byte
29F8: 09 20           ORA     #$20                ; mark bit 5, the blocked-band diversion flag
29FA: 95 34           STA     $34,X               ; {hard.workRam+34} store the phase
29FC: 90 05           BCC     $2A03               ; {code.loc_2a03} take the coordinate-advance path

loc_29fe:
29FE: 20 6B 2C        JSR     $2C6B               ; {code.detectColumnCollision} test for another object blocking the column ahead
2A01: 90 BB           BCC     $29BE               ; {code.loc_29be} no collision -- jump to advance the coordinate and arm

loc_2a03:
2A03: B5 64           LDA     $64,X               ; {hard.workRam+64} read the coordinate loc_64+x
2A05: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold in orientation $f0
2A07: B4 74           LDY     $74,X               ; {hard.workRam+74} read the link loc_74+x
2A09: F0 D4           BEQ     $29DF               ; {code.loc_29df} no link -- jump to reverse the delta and turn
2A0B: 10 12           BPL     $2A1F               ; {code.loc_2a1f} link positive -- take the forward-edge test
2A0D: A4 EF           LDY     $EF                 ; {hard.workRam+EF} read the direction selector $ef
2A0F: F0 08           BEQ     $2A19               ; {code.loc_2a19} $ef zero -- take the plain band test
2A11: 45 F0           EOR     $F0                 ; {hard.workRam+F0} re-fold the coordinate with $f0
2A13: C9 C9           CMP     #$C9                ; compare the folded coordinate against 0xc9
2A15: 90 63           BCC     $2A7A               ; {code.loc_2a7a} below -- take the link-negate tail
2A17: B0 68           BCS     $2A81               ; {code.loc_2a81} at or above -- take the coordinate-commit path

loc_2a19:
2A19: C9 30           CMP     #$30                ; compare the folded coordinate against 0x30
2A1B: B0 5D           BCS     $2A7A               ; {code.loc_2a7a} 0x30 or more -- take the link-negate tail
2A1D: 90 62           BCC     $2A81               ; {code.loc_2a81} below -- take the coordinate-commit path

loc_2a1f:
2A1F: C9 09           CMP     #$09                ; folded coordinate near the edge (below 0x09)?
2A21: B0 5E           BCS     $2A81               ; {code.loc_2a81} not near the edge -- take the coordinate-commit path
2A23: B5 34           LDA     $34,X               ; {hard.workRam+34} read the phase byte
2A25: 29 40           AND     #$40                ; test bit 6
2A27: D0 51           BNE     $2A7A               ; {code.loc_2a7a} bit 6 set -- take the link-negate tail
2A29: B5 34           LDA     $34,X               ; {hard.workRam+34} read the phase byte
2A2B: 29 DF           AND     #$DF                ; clear bit 5
2A2D: 95 34           STA     $34,X               ; {hard.workRam+34} store the phase
2A2F: E0 0B           CPX     #$0B                ; is this the last slot 0x0b?
2A31: F0 47           BEQ     $2A7A               ; {code.loc_2a7a} yes -- take the link-negate tail
2A33: 8A              TXA                         ; A = this slot index
2A34: A8              TAY                         ; Y = this slot index
2A35: C8              INY                         ; step Y to the trailing neighbour slot
2A36: B9 34 00        LDA     $0034,Y             ; {hard.workRam+34} read the neighbour's phase loc_34[y]
2A39: 30 3F           BMI     $2A7A               ; {code.loc_2a7a} neighbour retired -- take the link-negate tail
2A3B: 29 40           AND     #$40                ; test the neighbour's bit 6
2A3D: F0 3B           BEQ     $2A7A               ; {code.loc_2a7a} clear -- take the link-negate tail

loc_2a3f:
2A3F: C0 0B           CPY     #$0B                ; scanned all the way to the last slot?
2A41: F0 09           BEQ     $2A4C               ; {code.loc_2a4c} yes -- fold this neighbour back
2A43: B9 35 00        LDA     $0035,Y             ; {hard.workRam+35} peek the slot-after-next's phase loc_35[y]
2A46: 30 04           BMI     $2A4C               ; {code.loc_2a4c} it is retired -- fold this neighbour back
2A48: 29 40           AND     #$40                ; test its bit 6
2A4A: D0 29           BNE     $2A75               ; {code.loc_2a75} bit 6 set -- skip to the next neighbour

loc_2a4c:
2A4C: B9 64 00        LDA     $0064,Y             ; {hard.workRam+64} read the neighbour's coordinate loc_64[y]
2A4F: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold in orientation $f0
2A51: C9 09           CMP     #$09                ; neighbour clear of the edge (0x09 or more)?
2A53: B0 25           BCS     $2A7A               ; {code.loc_2a7a} too far -- take the link-negate tail
2A55: B9 34 00        LDA     $0034,Y             ; {hard.workRam+34} read the neighbour's phase loc_34[y]
2A58: 29 07           AND     #$07                ; keep only its low 3 bits, clearing the flags
2A5A: 99 34 00        STA     $0034,Y             ; {hard.workRam+34} store the cleared neighbour phase
2A5D: B9 44 00        LDA     $0044,Y             ; {hard.workRam+44} read the neighbour's heading delta loc_44[y]
2A60: 20 2D 38        JSR     $382D               ; {code.negateA} negate the delta
2A63: 99 44 00        STA     $0044,Y             ; {hard.workRam+44} store the negated neighbour delta
2A66: B9 64 00        LDA     $0064,Y             ; {hard.workRam+64} read the neighbour's coordinate loc_64[y]
2A69: 29 F8           AND     #$F8                ; snap it to the grid (clear the low 3 bits)
2A6B: 99 64 00        STA     $0064,Y             ; {hard.workRam+64} store the snapped coordinate
2A6E: A9 00           LDA     #$00                ; load zero
2A70: 99 74 00        STA     $0074,Y             ; {hard.workRam+74} clear the neighbour's link loc_74[y]
2A73: F0 05           BEQ     $2A7A               ; {code.loc_2a7a} always -- take the link-negate tail

loc_2a75:
2A75: C8              INY                         ; step to the next neighbour slot
2A76: C0 0C           CPY     #$0C                ; past the last slot 0x0c?
2A78: 90 C5           BCC     $2A3F               ; {code.loc_2a3f} still in range -- keep scanning neighbours

loc_2a7a:
2A7A: B5 74           LDA     $74,X               ; {hard.workRam+74} read this segment's link loc_74+x
2A7C: 20 2D 38        JSR     $382D               ; {code.negateA} negate the link
2A7F: 95 74           STA     $74,X               ; {hard.workRam+74} store the negated link

loc_2a81:
2A81: B5 64           LDA     $64,X               ; {hard.workRam+64} read the coordinate loc_64+x
2A83: A4 EF           LDY     $EF                 ; {hard.workRam+EF} read the direction selector $ef
2A85: F0 06           BEQ     $2A8D               ; {code.loc_2a8d} $ef zero -- subtract the link
2A87: 18              CLC                         ; clear carry for the add
2A88: 75 74           ADC     $74,X               ; {hard.workRam+74} add the link loc_74+x into the coordinate
2A8A: 4C 90 2A        JMP     $2A90               ; {code.commitSegmentCoord} jump to commit the coordinate

loc_2a8d:
2A8D: 38              SEC                         ; set carry for the subtract
2A8E: F5 74           SBC     $74,X               ; {hard.workRam+74} subtract the link loc_74+x from the coordinate

commitSegmentCoord:
2A90: 95 64           STA     $64,X               ; {hard.workRam+64} commit the new coordinate loc_64+x

advanceSegmentCoordAndArm:
2A92: B5 44           LDA     $44,X               ; {hard.workRam+44} read the heading delta loc_44+x
2A94: 18              CLC                         ; clear carry for the add
2A95: 75 54           ADC     $54,X               ; {hard.workRam+54} add the delta into the segment coordinate loc_54+x
2A97: 95 54           STA     $54,X               ; {hard.workRam+54} store the advanced coordinate
2A99: 20 96 2C        JSR     $2C96               ; {code.armSlotWhenObjectInRange} probe whether the segment is now in range to arm the slot
2A9C: 90 2F           BCC     $2ACD               ; {code.returnImmediately} slot armed -- this segment is done
2A9E: B5 64           LDA     $64,X               ; {hard.workRam+64} read the state field loc_64+x
2AA0: 29 07           AND     #$07                ; keep its low 3 bits
2AA2: C9 04           CMP     #$04                ; is it the aligned value 4?
2AA4: D0 21           BNE     $2AC7               ; {code.advanceSegmentLoopIndex} not aligned -- step to the next segment

reverseSegmentDeltaAndStepCoord:
2AA6: B5 44           LDA     $44,X               ; {hard.workRam+44} read the heading delta loc_44+x
2AA8: 20 2D 38        JSR     $382D               ; {code.negateA} negate it in place
2AAB: 95 44           STA     $44,X               ; {hard.workRam+44} store the flipped delta
2AAD: B4 74           LDY     $74,X               ; {hard.workRam+74} read the link loc_74+x
2AAF: D0 16           BNE     $2AC7               ; {code.advanceSegmentLoopIndex} link already set -- step to the next segment
2AB1: 09 00           ORA     #$00                ; set the flags from the flipped delta
2AB3: 30 03           BMI     $2AB8               ; {code.loc_2ab8} delta negative -- skip the negate
2AB5: 20 2D 38        JSR     $382D               ; {code.negateA} take the negative magnitude of the delta

loc_2ab8:
2AB8: 95 74           STA     $74,X               ; {hard.workRam+74} seed the link loc_74+x with the negative magnitude
2ABA: A9 04           LDA     #$04                ; default coordinate nudge +4
2ABC: B4 44           LDY     $44,X               ; {hard.workRam+44} test the flipped delta sign
2ABE: 10 02           BPL     $2AC2               ; {code.loc_2ac2} positive -- keep +4
2AC0: A9 FC           LDA     #$FC                ; negative -- nudge by -4 instead

loc_2ac2:
2AC2: 18              CLC                         ; clear carry for the add
2AC3: 75 54           ADC     $54,X               ; {hard.workRam+54} nudge the coordinate loc_54+x by the chosen step
2AC5: 95 54           STA     $54,X               ; {hard.workRam+54} store the nudged coordinate

advanceSegmentLoopIndex:
2AC7: CA              DEX                         ; step the segment cursor to the previous slot
2AC8: 30 03           BMI     $2ACD               ; {code.returnImmediately} ran past the first slot -- end the walk
2ACA: 4C 62 29        JMP     $2962               ; {code.moveCentipedeSegment} otherwise move the next segment

returnImmediately:
2ACD: 60              RTS                         ; return from the segment sweep

loc_2ace:
2ACE: A5 86           LDA     $86                 ; {hard.workRam+86} read the master enable $86
2AD0: 10 01           BPL     $2AD3               ; {code.loc_2ad3} non-negative -- run the axis integrator

loc_2ad2:
2AD2: 60              RTS                         ; disabled -- return

loc_2ad3:
2AD3: A5 43           LDA     $43                 ; {hard.workRam+43} read the $43 control byte
2AD5: 29 AF           AND     #$AF                ; test its mode bits (mask 0xaf)
2AD7: D0 F9           BNE     $2AD2               ; {code.loc_2ad2} any mode bit set -- return without integrating
2AD9: A5 73           LDA     $73                 ; {hard.workRam+73} read the $73-axis coordinate
2ADB: 85 8D           STA     $8D                 ; {hard.workRam+8D} snapshot it into $8d
2ADD: A4 FE           LDY     $FE                 ; {hard.workRam+FE} read $fe
2ADF: A5 B9           LDA     $B9                 ; {hard.workRam+B9} read the old $b9 delta
2AE1: 84 B9           STY     $B9                 ; {hard.workRam+B9} swap $fe into $b9
2AE3: 20 26 32        JSR     $3226               ; {code.clampAndHalveSignedDelta} clamp and halve the old delta toward the playfield rails
2AE6: 65 84           ADC     $84                 ; {hard.workRam+84} fold the halved magnitude into the $63-axis sub-step accumulator $84
2AE8: 85 84           STA     $84                 ; {hard.workRam+84} store the sub-step accumulator $84
2AEA: 98              TYA                         ; A = the halved delta, falling into the $73-axis companion integrator

loc_2aeb:
2AEB: 65 63           ADC     $63                 ; {hard.workRam+63} fold the integer carry from the sub-step accumulator into the $63 coordinate
2AED: AA              TAX                         ; hold the new $63 coordinate in x
2AEE: 85 8B           STA     $8B                 ; {hard.workRam+8B} stash the coordinate into scratch $8b for the tile lookup
2AF0: A0 00           LDY     #$00                ; row index zero for the lookup
2AF2: A5 73           LDA     $73                 ; {hard.workRam+73} load the other-axis coordinate $73
2AF4: 20 2B 2C        JSR     $2C2B               ; {code.resolveTileCellAtXY} resolve the tile cell the object would move onto
2AF7: D0 11           BNE     $2B0A               ; {code.loc_2b0a} destination occupied -- keep the old $63 coordinate
2AF9: 8A              TXA                         ; recall the freshly computed $63 coordinate
2AFA: C9 F4           CMP     #$F4                ; test it against the upper playfield wall band
2AFC: 90 04           BCC     $2B02               ; {code.loc_2b02} below the wall -- go check the lower clamp
2AFE: A9 F4           LDA     #$F4                ; pin the coordinate to the upper limit 0xf4
2B00: D0 0A           BNE     $2B0C               ; {code.loc_2b0c} go store the clamped coordinate

loc_2b02:
2B02: C9 0B           CMP     #$0B                ; test it against the lower playfield edge
2B04: B0 06           BCS     $2B0C               ; {code.loc_2b0c} at or above the edge -- store as-is
2B06: A9 0B           LDA     #$0B                ; pin the coordinate to the lower limit 0x0b
2B08: D0 02           BNE     $2B0C               ; {code.loc_2b0c} go store the clamped coordinate

loc_2b0a:
2B0A: A5 63           LDA     $63                 ; {hard.workRam+63} blocked path -- reload the unchanged $63 coordinate

loc_2b0c:
2B0C: 85 63           STA     $63                 ; {hard.workRam+63} write the settled $63 coordinate back
2B0E: A4 86           LDY     $86                 ; {hard.workRam+86} read the pending-wave/round flag $86
2B10: 10 01           BPL     $2B13               ; {code.loc_2b13} still counting a round -- keep going
2B12: 60              RTS                         ; wave teardown pending -- drop out here

loc_2b13:
2B13: A0 00           LDY     #$00                ; row index zero
2B15: A5 BB           LDA     $BB                 ; {hard.workRam+BB} read the carried delta $bb
2B17: 84 BB           STY     $BB                 ; {hard.workRam+BB} clear $bb so the delta is consumed once
2B19: 20 2D 38        JSR     $382D               ; {code.negateA} negate the delta magnitude
2B1C: 20 26 32        JSR     $3226               ; {code.clampAndHalveSignedDelta} clamp and halve the signed delta
2B1F: 65 85           ADC     $85                 ; {hard.workRam+85} add it into the $73-axis sub-step accumulator $85
2B21: 85 85           STA     $85                 ; {hard.workRam+85} store the accumulator back
2B23: 98              TYA                         ; move the whole-step carry into a for the coordinate add

clampCoordToBand:
2B24: 65 73           ADC     $73                 ; {hard.workRam+73} fold the integer carry into the $73 coordinate
2B26: AA              TAX                         ; hold the new $73 coordinate in x
2B27: A4 63           LDY     $63                 ; {hard.workRam+63} load the $63 coordinate
2B29: 84 8B           STY     $8B                 ; {hard.workRam+8B} stash it into scratch $8b for the tile lookup
2B2B: A0 00           LDY     #$00                ; row index zero for the lookup
2B2D: 20 2B 2C        JSR     $2C2B               ; {code.resolveTileCellAtXY} resolve the tile cell the object would move onto
2B30: D0 25           BNE     $2B57               ; {code.loc_2b57} destination occupied -- keep the old $73 coordinate
2B32: 8A              TXA                         ; recall the freshly computed $73 coordinate
2B33: C9 08           CMP     #$08                ; test against the low wall band
2B35: 90 1C           BCC     $2B53               ; {code.loc_2b53} below 0x08 -- pin to the low edge
2B37: C9 F1           CMP     #$F1                ; test against the high wall band
2B39: B0 14           BCS     $2B4F               ; {code.loc_2b4f} at or above 0xf1 -- pin to the high edge
2B3B: C9 80           CMP     #$80                ; is it in the lower half of the field
2B3D: 90 08           BCC     $2B47               ; {code.loc_2b47} yes -- go check the lower dead-band clamp
2B3F: C9 C8           CMP     #$C8                ; upper half -- test the central dead band
2B41: B0 16           BCS     $2B59               ; {code.loc_2b59} clear of the dead band -- store as-is
2B43: A9 C8           LDA     #$C8                ; snap up past the central dead band to 0xc8
2B45: D0 12           BNE     $2B59               ; {code.loc_2b59} go store the clamped coordinate

loc_2b47:
2B47: C9 31           CMP     #$31                ; lower-half dead-band edge test
2B49: 90 0E           BCC     $2B59               ; {code.loc_2b59} below the dead band -- store as-is
2B4B: A9 30           LDA     #$30                ; snap down to the dead-band edge 0x30
2B4D: D0 0A           BNE     $2B59               ; {code.loc_2b59} go store the clamped coordinate

loc_2b4f:
2B4F: A9 F0           LDA     #$F0                ; pin to the high edge 0xf0
2B51: D0 06           BNE     $2B59               ; {code.loc_2b59} go store the clamped coordinate

loc_2b53:
2B53: A9 08           LDA     #$08                ; pin to the low edge 0x08
2B55: D0 02           BNE     $2B59               ; {code.loc_2b59} go store the clamped coordinate

loc_2b57:
2B57: A5 73           LDA     $73                 ; {hard.workRam+73} blocked path -- reload the unchanged $73 coordinate

loc_2b59:
2B59: 85 73           STA     $73                 ; {hard.workRam+73} write the settled $73 coordinate back
2B5B: A4 86           LDY     $86                 ; {hard.workRam+86} read the pending-wave/round flag $86
2B5D: 10 01           BPL     $2B60               ; {code.routeByCoordDelta} still counting a round -- keep going
2B5F: 60              RTS                         ; wave teardown pending -- drop out here

routeByCoordDelta:
2B60: A5 72           LDA     $72                 ; {hard.workRam+72} load the head coordinate $72
2B62: A6 EF           LDX     $EF                 ; {hard.workRam+EF} read the direction selector $ef
2B64: F0 07           BEQ     $2B6D               ; {code.loc_2b6d} selector zero -- take the other subtract path
2B66: 38              SEC                         ; prepare a clean subtract
2B67: E5 8D           SBC     $8D                 ; {hard.workRam+8D} subtract the step $8d from the head coordinate
2B69: B0 0E           BCS     $2B79               ; {code.loc_2b79} no borrow -- retarget the head
2B6B: 90 05           BCC     $2B72               ; {code.loc_2b72} borrowed -- go measure the distance

loc_2b6d:
2B6D: 38              SEC                         ; prepare a clean subtract
2B6E: E5 8D           SBC     $8D                 ; {hard.workRam+8D} subtract the step $8d from the head coordinate
2B70: 90 07           BCC     $2B79               ; {code.loc_2b79} borrowed -- retarget the head

loc_2b72:
2B72: 20 2B 38        JSR     $382B               ; {code.foldSignedMagnitude} fold the signed distance to a magnitude
2B75: C9 05           CMP     #$05                ; compare the distance to the retarget threshold
2B77: B0 0D           BCS     $2B86               ; {code.loc_2b86} far enough -- skip the retarget

loc_2b79:
2B79: A9 04           LDA     #$04                ; start from a step of 4
2B7B: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it with the direction sign $f0
2B7D: 18              CLC                         ; clear carry for the add
2B7E: 65 73           ADC     $73                 ; {hard.workRam+73} add the $73 coordinate
2B80: 85 72           STA     $72                 ; {hard.workRam+72} set the head target coordinate $72
2B82: A5 63           LDA     $63                 ; {hard.workRam+63} load the $63 coordinate
2B84: 85 62           STA     $62                 ; {hard.workRam+62} copy it into the $62 companion coordinate

loc_2b86:
2B86: A5 43           LDA     $43                 ; {hard.workRam+43} read the movement state flag $43
2B88: 29 AF           AND     #$AF                ; mask the active-state bits
2B8A: F0 04           BEQ     $2B90               ; {code.loc_2b90} none set -- nothing to arm
2B8C: A9 28           LDA     #$28                ; arm value 0x28
2B8E: 85 42           STA     $42                 ; {hard.workRam+42} load it into the $42 timer cell

loc_2b90:
2B90: 60              RTS                         ; done

maybeDecrementTableEntry:
2B91: A5 32           LDA     $32                 ; {hard.workRam+32} load the working tile pointer low byte
2B93: 29 1F           AND     #$1F                ; keep the column within the row (low five bits)
2B95: A6 EF           LDX     $EF                 ; {hard.workRam+EF} read the direction selector $ef
2B97: F0 06           BEQ     $2B9F               ; {code.loc_2b9f} selector zero -- take the other range test
2B99: C9 14           CMP     #$14                ; compare the column to the mid-row split 0x14
2B9B: 90 0A           BCC     $2BA7               ; {code.loc_2ba7} before the split -- nothing to do
2B9D: B0 04           BCS     $2BA3               ; {code.loc_2ba3} past the split -- decrement the shot-origin cell

loc_2b9f:
2B9F: C9 0C           CMP     #$0C                ; compare the column to the near-edge limit 0x0c
2BA1: B0 04           BCS     $2BA7               ; {code.loc_2ba7} past it -- nothing to do

loc_2ba3:
2BA3: A6 88           LDX     $88                 ; {hard.workRam+88} load the slot index $88
2BA5: D6 D7           DEC     $D7,X               ; {hard.workRam+D7} step the shot-origin cell $d7+slot down by one

loc_2ba7:
2BA7: 60              RTS                         ; done

stampEmptyTileCell:
2BA8: A0 00           LDY     #$00                ; row index zero
2BAA: B1 32           LDA     ($32),Y             ; {hard.workRam+32} read the tile cell through the working pointer
2BAC: D0 2A           BNE     $2BD8               ; {code.loc_2bd8} cell already occupied -- leave it
2BAE: A5 32           LDA     $32                 ; {hard.workRam+32} take the tile pointer low byte
2BB0: 29 1F           AND     #$1F                ; keep the column within the row
2BB2: F0 24           BEQ     $2BD8               ; {code.loc_2bd8} column at the left edge -- leave it
2BB4: C9 1F           CMP     #$1F                ; compare against the right edge column
2BB6: F0 20           BEQ     $2BD8               ; {code.loc_2bd8} column at the right edge -- leave it
2BB8: A6 EF           LDX     $EF                 ; {hard.workRam+EF} read the direction selector $ef
2BBA: F0 0A           BEQ     $2BC6               ; {code.loc_2bc6} selector zero -- take the other edge test
2BBC: C9 1E           CMP     #$1E                ; compare against the inner-edge column 0x1e
2BBE: F0 18           BEQ     $2BD8               ; {code.loc_2bd8} on that edge -- leave it
2BC0: C9 14           CMP     #$14                ; compare against the mid-row split 0x14
2BC2: 90 0E           BCC     $2BD2               ; {code.loc_2bd2} before the split -- go stamp a mushroom
2BC4: B0 08           BCS     $2BCE               ; {code.loc_2bce} past the split -- bump the shot-origin cell

loc_2bc6:
2BC6: C9 01           CMP     #$01                ; compare against column 1
2BC8: F0 0E           BEQ     $2BD8               ; {code.loc_2bd8} on column 1 -- leave it
2BCA: C9 0C           CMP     #$0C                ; compare against the near-edge limit 0x0c
2BCC: B0 04           BCS     $2BD2               ; {code.loc_2bd2} past it -- go stamp a mushroom

loc_2bce:
2BCE: A6 88           LDX     $88                 ; {hard.workRam+88} load the slot index $88
2BD0: F6 D7           INC     $D7,X               ; {hard.workRam+D7} bump the shot-origin cell $d7+slot up by one

loc_2bd2:
2BD2: A9 3F           LDA     #$3F                ; start from the mushroom glyph 0x3f
2BD4: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it with the direction/colour $ef
2BD6: 91 32           STA     ($32),Y             ; {hard.workRam+32} stamp the mushroom into the tile cell

loc_2bd8:
2BD8: 60              RTS                         ; done

spawnActorOnTimer:
2BD9: A5 97           LDA     $97                 ; {hard.workRam+97} read the spawner enable byte $97
2BDB: F0 4D           BEQ     $2C2A               ; {code.loc_2c2a} spawner disabled -- return
2BDD: A5 87           LDA     $87                 ; {hard.workRam+87} read the busy byte $87
2BDF: D0 49           BNE     $2C2A               ; {code.loc_2c2a} busy this frame -- return
2BE1: A5 A0           LDA     $A0                 ; {hard.workRam+A0} read the spawn interval timer
2BE3: F0 03           BEQ     $2BE8               ; {code.loc_2be8} timer expired -- run the spawn
2BE5: C6 A0           DEC     $A0                 ; {hard.workRam+A0} still counting -- tick the spawn timer down
2BE7: 60              RTS                         ; nothing spawns mid-interval -- return

loc_2be8:
2BE8: A6 88           LDX     $88                 ; {hard.workRam+88} load the channel selector $88
2BEA: A0 0B           LDY     #$0B                ; scan the actor slots from the top slot 0x0b

loc_2bec:
2BEC: B9 34 00        LDA     $0034,Y             ; {hard.workRam+34} read this actor slot's phase byte
2BEF: 30 04           BMI     $2BF5               ; {code.loc_2bf5} sign set -- this slot is free, claim it
2BF1: 88              DEY                         ; step down to the next slot
2BF2: 10 F8           BPL     $2BEC               ; {code.loc_2bec} keep scanning for a free slot
2BF4: 60              RTS                         ; field full -- nothing spawns, return

loc_2bf5:
2BF5: A9 00           LDA     #$00                ; clear value
2BF7: 99 34 00        STA     $0034,Y             ; {hard.workRam+34} claim the slot by zeroing its phase byte
2BFA: A9 40           LDA     #$40                ; orientation base 0x40
2BFC: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it with the direction sign $f0
2BFE: 99 64 00        STA     $0064,Y             ; {hard.workRam+64} seed the new actor's coordinate field
2C01: A9 FC           LDA     #$FC                ; motion seed 0xfc
2C03: 99 54 00        STA     $0054,Y             ; {hard.workRam+54} seed the new actor's row field
2C06: A9 02           LDA     #$02                ; motion seed 0x02
2C08: 99 74 00        STA     $0074,Y             ; {hard.workRam+74} seed the new actor's step field
2C0B: B5 A1           LDA     $A1,X               ; {hard.workRam+A1} read this channel's spawn-interval reload value
2C0D: C9 60           CMP     #$60                ; still above the ratchet floor 0x60
2C0F: 90 04           BCC     $2C15               ; {code.loc_2c15} at or below the floor -- keep the reload as-is
2C11: E9 08           SBC     #$08                ; ratchet the interval shorter by 8
2C13: 95 A1           STA     $A1,X               ; {hard.workRam+A1} write the shortened reload back

loc_2c15:
2C15: 85 A0           STA     $A0                 ; {hard.workRam+A0} load the new interval into the spawn timer
2C17: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the hardware random register
2C1A: 29 02           AND     #$02                ; take its variant bit
2C1C: D0 07           BNE     $2C25               ; {code.loc_2c25} bit set -- take actor variant A
2C1E: A9 04           LDA     #$04                ; variant B step 0x04
2C20: 99 54 00        STA     $0054,Y             ; {hard.workRam+54} override the actor's row field for variant B
2C23: A9 FE           LDA     #$FE                ; variant B mirrored delta 0xfe

loc_2c25:
2C25: 99 44 00        STA     $0044,Y             ; {hard.workRam+44} seed the actor's delta field
2C28: F6 94           INC     $94,X               ; {hard.workRam+94} bump this channel's spawn count

loc_2c2a:
2C2A: 60              RTS                         ; done

resolveTileCellAtXY:
2C2B: 4A              LSR     A                   ; shift the coordinate right one
2C2C: 4A              LSR     A                   ; shift it right again
2C2D: 4A              LSR     A                   ; shift it a third time to divide by eight into a column
2C2E: 69 00           ADC     #$00                ; round with the shifted-out carry
2C30: 85 32           STA     $32                 ; {hard.workRam+32} store it as the tile pointer low byte
2C32: A9 01           LDA     #$01                ; page base 1
2C34: 85 33           STA     $33                 ; {hard.workRam+33} store it as the tile pointer high byte
2C36: 98              TYA                         ; move the passed row index into a
2C37: 0A              ASL     A                   ; shift it left once
2C38: 0A              ASL     A                   ; shift it left again
2C39: 0A              ASL     A                   ; shift it a third time to scale the row by eight
2C3A: 18              CLC                         ; clear carry for the add
2C3B: 65 8B           ADC     $8B                 ; {hard.workRam+8B} add the stashed column offset $8b
2C3D: 85 8B           STA     $8B                 ; {hard.workRam+8B} store the combined row/column offset back
2C3F: A9 F7           LDA     #$F7                ; top-of-screen constant 0xf7
2C41: 38              SEC                         ; prepare a clean subtract
2C42: E5 8B           SBC     $8B                 ; {hard.workRam+8B} invert the offset for screen orientation
2C44: B0 02           BCS     $2C48               ; {code.loc_2c48} no borrow -- keep the inverted offset
2C46: A9 00           LDA     #$00                ; underflowed -- floor the offset to zero

loc_2c48:
2C48: 29 F8           AND     #$F8                ; keep the row's high bits
2C4A: 0A              ASL     A                   ; shift the row bits toward the pointer high byte
2C4B: 26 33           ROL     $33                 ; {hard.workRam+33} rotate the carry into the pointer high byte
2C4D: 0A              ASL     A                   ; shift again
2C4E: 26 33           ROL     $33                 ; {hard.workRam+33} rotate the carry into the pointer high byte
2C50: 05 32           ORA     $32                 ; {hard.workRam+32} fold the column back into the pointer low byte
2C52: A4 33           LDY     $33                 ; {hard.workRam+33} load the pointer high byte
2C54: C0 07           CPY     #$07                ; is the pointer in the last page (7)
2C56: D0 08           BNE     $2C60               ; {code.loc_2c60} no -- pointer is ready
2C58: C9 C0           CMP     #$C0                ; within page 7, above the status region
2C5A: 90 04           BCC     $2C60               ; {code.loc_2c60} below it -- pointer is ready
2C5C: 29 1F           AND     #$1F                ; wrap the low byte within page 7
2C5E: 09 A0           ORA     #$A0                ; steer it into the page-7 wrap window

loc_2c60:
2C60: 85 32           STA     $32                 ; {hard.workRam+32} store the final tile pointer low byte
2C62: A0 00           LDY     #$00                ; row index zero
2C64: B1 32           LDA     ($32),Y             ; {hard.workRam+32} read the tile cell at the pointer
2C66: F0 02           BEQ     $2C6A               ; {code.loc_2c6a} cell empty -- return zero
2C68: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold the occupied cell with the direction $ef

loc_2c6a:
2C6A: 60              RTS                         ; return the cell reading

detectColumnCollision:
2C6B: 86 8B           STX     $8B                 ; {hard.workRam+8B} stash object index x into $8b
2C6D: 86 8C           STX     $8C                 ; {hard.workRam+8C} stash it into $8c as well
2C6F: E6 8C           INC     $8C                 ; {hard.workRam+8C} step $8c to the next slot index
2C71: A0 0C           LDY     #$0C                ; scan the object slots from the top slot 0x0c

loc_2c73:
2C73: B9 64 00        LDA     $0064,Y             ; {hard.workRam+64} read the other slot's column $64+y
2C76: D5 64           CMP     $64,X               ; {hard.workRam+64} compare it to this object's column
2C78: D0 17           BNE     $2C91               ; {code.loc_2c91} different column -- skip this slot
2C7A: B9 34 00        LDA     $0034,Y             ; {hard.workRam+34} read the other slot's phase byte
2C7D: C9 F4           CMP     #$F4                ; compare against the retired marker 0xf4
2C7F: B0 10           BCS     $2C91               ; {code.loc_2c91} retired slot -- skip it
2C81: C4 8B           CPY     $8B                 ; {hard.workRam+8B} is this the object itself
2C83: F0 0C           BEQ     $2C91               ; {code.loc_2c91} yes -- skip it
2C85: B5 54           LDA     $54,X               ; {hard.workRam+54} read this object's row $54+x
2C87: 38              SEC                         ; prepare a clean subtract
2C88: F9 54 00        SBC     $0054,Y             ; {hard.workRam+54} subtract the other slot's row $54+y
2C8B: 55 44           EOR     $44,X               ; {hard.workRam+44} fold the gap with this object's delta sign
2C8D: C9 F4           CMP     #$F4                ; compare the folded row gap to the band 0xf4
2C8F: B0 04           BCS     $2C95               ; {code.loc_2c95} within the band -- report a collision in this column

loc_2c91:
2C91: 88              DEY                         ; step the scan index down to the next slot and keep hunting a same-column neighbour
2C92: 10 DF           BPL     $2C73               ; {code.loc_2c73} loop back while more slots remain to check
2C94: 18              CLC                         ; no neighbouring object shares this column -- clear carry

loc_2c95:
2C95: 60              RTS                         ; return

armSlotWhenObjectInRange:
2C96: B5 54           LDA     $54,X               ; {hard.workRam+54} read object X's horizontal coordinate
2C98: 38              SEC                         ; set carry for the subtract
2C99: E5 63           SBC     $63                 ; {hard.workRam+63} subtract the reference point's horizontal position
2C9B: 20 2B 38        JSR     $382B               ; {code.foldSignedMagnitude} take the absolute value of the horizontal distance
2C9E: E0 0D           CPX     #$0D                ; is this the special last slot 0x0d?
2CA0: D0 05           BNE     $2CA7               ; {code.loc_2ca7} other slot -- use the ordinary horizontal bound
2CA2: C9 0A           CMP     #$0A                ; slot 0x0d: horizontal magnitude must be under 0x0a
2CA4: 90 05           BCC     $2CAB               ; {code.loc_2cab} within reach horizontally -- go test the vertical distance

loc_2ca6:
2CA6: 60              RTS                         ; out of range -- return with carry set, no arming

loc_2ca7:
2CA7: C9 07           CMP     #$07                ; other slots: horizontal magnitude against the 0x07 bound
2CA9: B0 FB           BCS     $2CA6               ; {code.loc_2ca6} too far horizontally -- bail

loc_2cab:
2CAB: 85 8D           STA     $8D                 ; {hard.workRam+8D} stash the horizontal magnitude
2CAD: B5 64           LDA     $64,X               ; {hard.workRam+64} read object X's vertical coordinate
2CAF: 38              SEC                         ; set carry for the subtract
2CB0: E5 73           SBC     $73                 ; {hard.workRam+73} subtract the reference point's vertical position
2CB2: 20 2B 38        JSR     $382B               ; {code.foldSignedMagnitude} take the absolute value of the vertical distance
2CB5: C9 07           CMP     #$07                ; vertical magnitude must clear 0x07
2CB7: B0 ED           BCS     $2CA6               ; {code.loc_2ca6} too far vertically -- bail
2CB9: 18              CLC                         ; clear carry for the add
2CBA: 65 8D           ADC     $8D                 ; {hard.workRam+8D} add the horizontal magnitude to form the summed distance
2CBC: E0 0D           CPX     #$0D                ; is this the special last slot 0x0d?
2CBE: F0 2A           BEQ     $2CEA               ; {code.enterArmBlockUnlessValueHigh} slot 0x0d -- route through the value-gated arm entry
2CC0: C9 0C           CMP     #$0C                ; other slots: carry set when the summed distance is 0x0c or more

armSlotState:
2CC2: B0 E2           BCS     $2CA6               ; {code.loc_2ca6} caller gate: carry set means do not arm -- return
2CC4: A9 30           LDA     #$30                ; load the countdown constant
2CC6: 85 87           STA     $87                 ; {hard.workRam+87} stamp 0x30 into the slot countdown timer
2CC8: A9 20           LDA     #$20                ; load the state-cell constant
2CCA: 85 43           STA     $43                 ; {hard.workRam+43} stamp 0x20 into the mode/state cell
2CCC: A9 FF           LDA     #$FF                ; load the free marker
2CCE: 95 34           STA     $34,X               ; {hard.workRam+34} retire slot X's row byte to 0xff (slot free)
2CD0: A9 28           LDA     #$28                ; load the arm constant
2CD2: 85 42           STA     $42                 ; {hard.workRam+42} stamp 0x28 into the arm cell
2CD4: A5 86           LDA     $86                 ; {hard.workRam+86} read the master sign/enable cell
2CD6: 30 04           BMI     $2CDC               ; {code.loc_2cdc} negative -- skip arming the channel-1 priority tone
2CD8: A9 13           LDA     #$13                ; load the tone-timer value
2CDA: 85 B7           STA     $B7                 ; {hard.workRam+B7} arm the channel-1 priority SFX timer to 0x13

loc_2cdc:
2CDC: A9 00           LDA     #$00                ; zero out the working cells that follow
2CDE: 85 B2           STA     $B2                 ; {hard.workRam+B2} clear the channel-1 background SFX timer
2CE0: 85 B3           STA     $B3                 ; {hard.workRam+B3} clear the channel-2 SFX timer
2CE2: 85 B4           STA     $B4                 ; {hard.workRam+B4} clear the channel-3 SFX timer
2CE4: 85 B5           STA     $B5                 ; {hard.workRam+B5} clear the channel-4 SFX timer
2CE6: 85 B8           STA     $B8                 ; {hard.workRam+B8} clear the sweep counter
2CE8: 18              CLC                         ; signal armed -- carry clear
2CE9: 60              RTS                         ; return

enterArmBlockUnlessValueHigh:
2CEA: C9 0E           CMP     #$0E                ; slot 0x0d gate: arm only when the summed distance is below 0x0e
2CEC: 4C C2 2C        JMP     $2CC2               ; {code.armSlotState} fall into the arm block (carry set here blocks the arm)

scanForRangedCellAndSeed:
2CEF: A0 00           LDY     #$00                ; clear Y as the indirect scan offset
2CF1: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter
2CF3: 29 07           AND     #$07                ; keep only the low three bits -- every eighth frame
2CF5: D0 14           BNE     $2D0B               ; {code.loc_2d0b} not this frame -- return
2CF7: A5 B7           LDA     $B7                 ; {hard.workRam+B7} check the channel-1 priority SFX timer
2CF9: D0 10           BNE     $2D0B               ; {code.loc_2d0b} priority tone busy -- skip the field scan

loc_2cfb:
2CFB: A5 DB           LDA     $DB                 ; {hard.workRam+DB} read the field-scan pointer high byte
2CFD: F0 0C           BEQ     $2D0B               ; {code.loc_2d0b} zero high byte -- scan pass is over, return
2CFF: C9 07           CMP     #$07                ; sitting on the last video page (0x07)?
2D01: D0 09           BNE     $2D0C               ; {code.loc_2d0c} not the top page -- go read the cell
2D03: A5 DA           LDA     $DA                 ; {hard.workRam+DA} top page: read the scan pointer low byte
2D05: C9 C0           CMP     #$C0                ; past the fold point 0xc0?
2D07: 90 03           BCC     $2D0C               ; {code.loc_2d0c} below the fold -- go read the cell
2D09: 84 DB           STY     $DB                 ; {hard.workRam+DB} top-of-page reached -- zero the high byte, ending the pass

loc_2d0b:
2D0B: 60              RTS                         ; return

loc_2d0c:
2D0C: B1 DA           LDA     ($DA),Y             ; {hard.workRam+DA} read the playfield cell at the scan pointer
2D0E: 29 3F           AND     #$3F                ; keep the low six bits (the tile code)
2D10: C9 38           CMP     #$38                ; is the tile in the ripe band (0x38 or above)?
2D12: 90 40           BCC     $2D54               ; {code.loc_2d54} below the band -- advance to the next cell
2D14: C9 3F           CMP     #$3F                ; upper edge of the ripe band
2D16: B0 3C           BCS     $2D54               ; {code.loc_2d54} at or above 0x3f -- skip, advance
2D18: A9 3F           LDA     #$3F                ; load the base glyph 0x3f
2D1A: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold the base glyph 0x3f through the $ef mask to build the mushroom glyph
2D1C: 91 DA           STA     ($DA),Y             ; {hard.workRam+DA} stamp the full mushroom glyph 0x3f (folded through $ef) into the scanned cell
2D1E: A9 00           LDA     #$00                ; load zero
2D20: 85 8B           STA     $8B                 ; {hard.workRam+8B} clear the path-accumulator step seed
2D22: A9 05           LDA     #$05                ; load the step magnitude 0x05
2D24: 20 B6 2D        JSR     $2DB6               ; {code.advancePathAccumulator} fold the step into the path accumulator
2D27: A9 FF           LDA     #$FF                ; load 0xff
2D29: 85 3F           STA     $3F                 ; {hard.workRam+3F} set loc_3f to 0xff
2D2B: A5 DB           LDA     $DB                 ; {hard.workRam+DB} read the scan pointer high byte
2D2D: 85 8B           STA     $8B                 ; {hard.workRam+8B} seed loc_8b with it
2D2F: A5 DA           LDA     $DA                 ; {hard.workRam+DA} read the scan pointer low byte
2D31: 0A              ASL     A                   ; shift the address up one bit...
2D32: 26 8B           ROL     $8B                 ; {hard.workRam+8B} ...rolling into the high part
2D34: 0A              ASL     A                   ; shift up another bit...
2D35: 26 8B           ROL     $8B                 ; {hard.workRam+8B} ...rolling into the high part
2D37: 0A              ASL     A                   ; shift up a third bit...
2D38: 26 8B           ROL     $8B                 ; {hard.workRam+8B} ...rolling into the high part
2D3A: 85 6F           STA     $6F                 ; {hard.workRam+6F} stash the folded low part as a seed coordinate
2D3C: A5 8B           LDA     $8B                 ; {hard.workRam+8B} take the folded high part
2D3E: 29 1F           AND     #$1F                ; keep the low five bits (the column)
2D40: 49 1F           EOR     #$1F                ; invert the column bits
2D42: 0A              ASL     A                   ; scale the column up...
2D43: 0A              ASL     A                   ; ...by eight...
2D44: 0A              ASL     A                   ; ...three shifts left
2D45: E9 03           SBC     #$03                ; bias the result down by three
2D47: 85 5F           STA     $5F                 ; {hard.workRam+5F} store the seed vertical coordinate
2D49: E6 DA           INC     $DA                 ; {hard.workRam+DA} advance the scan pointer low byte
2D4B: D0 02           BNE     $2D4F               ; {code.loc_2d4f} no carry -- skip the high-byte bump
2D4D: E6 DB           INC     $DB                 ; {hard.workRam+DB} carry into the pointer high byte

loc_2d4f:
2D4F: A9 13           LDA     #$13                ; load the timer value 0x13
2D51: 85 B2           STA     $B2                 ; {hard.workRam+B2} arm the channel-1 background SFX timer to 0x13
2D53: 60              RTS                         ; return

loc_2d54:
2D54: E6 DA           INC     $DA                 ; {hard.workRam+DA} advance the scan pointer low byte
2D56: D0 A3           BNE     $2CFB               ; {code.loc_2cfb} no carry -- loop back to test the next cell
2D58: E6 DB           INC     $DB                 ; {hard.workRam+DB} carry into the pointer high byte
2D5A: D0 B0           BNE     $2D0C               ; {code.loc_2d0c} keep scanning the next cell

plotRecordFieldColumns:
2D5C: A9 07           LDA     #$07                ; load the header row selector 7
2D5E: 20 D5 37        JSR     $37D5               ; {code.writePointerTableRow} draw the record-field header row
2D61: A0 00           LDY     #$00                ; Y = record cursor, start at zero
2D63: A2 5C           LDX     #$5C                ; X = starting column base

loc_2d65:
2D65: 86 91           STX     $91                 ; {hard.workRam+91} seat the draw cursor low byte at the column base
2D67: A9 05           LDA     #$05                ; load the high byte of the draw cursor
2D69: 85 92           STA     $92                 ; {hard.workRam+92} set the draw cursor high byte to 0x05
2D6B: B9 04 00        LDA     $0004,Y             ; {hard.workRam+4} read the record's first field
2D6E: 84 8D           STY     $8D                 ; {hard.workRam+8D} save the record index
2D70: 38              SEC                         ; set carry to suppress a leading zero
2D71: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} print the first field as two digits
2D74: A4 8D           LDY     $8D                 ; {hard.workRam+8D} restore the record index
2D76: B9 03 00        LDA     $0003,Y             ; {hard.workRam+3} read the record's second field
2D79: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} print it as two digits, inheriting the leading-zero carry
2D7C: A4 8D           LDY     $8D                 ; {hard.workRam+8D} restore the record index
2D7E: B9 02 00        LDA     $0002,Y             ; {hard.workRam+2} read the record's third field
2D81: 18              CLC                         ; clear carry -- no leading-zero suppression
2D82: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} print the third field as two digits
2D85: A9 00           LDA     #$00                ; load a blank
2D87: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} write a blank separator cell and advance the cursor
2D8A: A4 8D           LDY     $8D                 ; {hard.workRam+8D} restore the record index
2D8C: 20 33 38        JSR     $3833               ; {code.plotZpTableByteAtCursor} plot the record's first glyph byte
2D8F: E6 8D           INC     $8D                 ; {hard.workRam+8D} advance the record index
2D91: A4 8D           LDY     $8D                 ; {hard.workRam+8D} reload the record index
2D93: 20 33 38        JSR     $3833               ; {code.plotZpTableByteAtCursor} plot the record's second glyph byte
2D96: E6 8D           INC     $8D                 ; {hard.workRam+8D} advance the record index
2D98: A4 8D           LDY     $8D                 ; {hard.workRam+8D} reload the record index
2D9A: 20 33 38        JSR     $3833               ; {code.plotZpTableByteAtCursor} plot the record's third glyph byte
2D9D: A5 91           LDA     $91                 ; {hard.workRam+91} read the advanced cursor low byte
2D9F: 29 1F           AND     #$1F                ; keep the column bits
2DA1: 09 40           ORA     #$40                ; set the bit that forms the next column base
2DA3: AA              TAX                         ; move it into X as the next column base
2DA4: CA              DEX                         ; back the base off by one
2DA5: A4 8D           LDY     $8D                 ; {hard.workRam+8D} restore the record index
2DA7: C8              INY                         ; step to the next record
2DA8: C0 18           CPY     #$18                ; done all records at index 0x18?
2DAA: 90 B9           BCC     $2D65               ; {code.loc_2d65} more records -- loop for the next column
2DAC: 60              RTS                         ; return

; ---- $2DAD-$2DAD: data ----
2DAD: 5F

decrementActiveObjectDelay:
2DAE: 86 8D           STX     $8D                 ; {hard.workRam+8D} save the caller's index
2DB0: A6 88           LDX     $88                 ; {hard.workRam+88} load the active-object selector
2DB2: D6 94           DEC     $94,X               ; {hard.workRam+94} tick this object's delay-bank entry down by one
2DB4: A6 8D           LDX     $8D                 ; {hard.workRam+8D} restore the caller's index

advancePathAccumulator:
2DB6: A4 86           LDY     $86                 ; {hard.workRam+86} read the enable/sign cell
2DB8: 30 50           BMI     $2E0A               ; {code.loc_2e0a} disabled (negative) -- return
2DBA: 86 8D           STX     $8D                 ; {hard.workRam+8D} save the caller's index
2DBC: F8              SED                         ; enter decimal (BCD) mode
2DBD: A6 88           LDX     $88                 ; {hard.workRam+88} load the active-object selector
2DBF: 18              CLC                         ; clear carry for the add
2DC0: 75 A7           ADC     $A7,X               ; {hard.workRam+A7} add the step into the accumulator low byte (BCD)
2DC2: 95 A7           STA     $A7,X               ; {hard.workRam+A7} store the low byte back
2DC4: B5 A9           LDA     $A9,X               ; {hard.workRam+A9} read the accumulator mid byte
2DC6: 65 8B           ADC     $8B                 ; {hard.workRam+8B} add the step's high part (BCD)
2DC8: 95 A9           STA     $A9,X               ; {hard.workRam+A9} store the mid byte back
2DCA: 90 0D           BCC     $2DD9               ; {code.loc_2dd9} no decimal carry -- skip the companion roll
2DCC: B5 A1           LDA     $A1,X               ; {hard.workRam+A1} carry: read the companion counter
2DCE: E9 02           SBC     #$02                ; step it down by two (BCD)
2DD0: 95 A1           STA     $A1,X               ; {hard.workRam+A1} store it back
2DD2: B5 AB           LDA     $AB,X               ; {hard.workRam+AB} read the second companion counter
2DD4: 18              CLC                         ; clear carry
2DD5: 69 01           ADC     #$01                ; bump it up by one (BCD)
2DD7: 95 AB           STA     $AB,X               ; {hard.workRam+AB} store it back

loc_2dd9:
2DD9: D8              CLD                         ; leave decimal mode
2DDA: A6 88           LDX     $88                 ; {hard.workRam+88} reload the active-object selector
2DDC: B5 A9           LDA     $A9,X               ; {hard.workRam+A9} read the accumulator mid byte
2DDE: D5 AD           CMP     $AD,X               ; {hard.workRam+AD} compare against the target low byte
2DE0: B5 AB           LDA     $AB,X               ; {hard.workRam+AB} read the accumulator high byte
2DE2: F5 AF           SBC     $AF,X               ; {hard.workRam+AF} finish the 16-bit compare against the target high byte
2DE4: 90 22           BCC     $2E08               ; {code.loc_2e08} accumulator still below the target -- not there yet, return
2DE6: 20 B3 21        JSR     $21B3               ; {code.readFdBitsTableByte} fetch the table-step low byte and its index
2DE9: F8              SED                         ; enter decimal mode
2DEA: 18              CLC                         ; clear carry
2DEB: 75 AD           ADC     $AD,X               ; {hard.workRam+AD} advance the target low byte by the table step (BCD)
2DED: 95 AD           STA     $AD,X               ; {hard.workRam+AD} store the target low byte
2DEF: B9 C0 21        LDA     $21C0,Y             ; {hard.rom+1C0} read the target-step high byte from the config table
2DF2: 75 AF           ADC     $AF,X               ; {hard.workRam+AF} advance the target high byte (BCD)
2DF4: 95 AF           STA     $AF,X               ; {hard.workRam+AF} store the target high byte
2DF6: D8              CLD                         ; leave decimal mode
2DF7: B5 A4           LDA     $A4,X               ; {hard.workRam+A4} read the phase index
2DF9: C9 06           CMP     #$06                ; phase at 0x06?
2DFB: F0 0B           BEQ     $2E08               ; {code.loc_2e08} exactly 0x06 -- done, return

loc_2dfd:
2DFD: B0 FE           BCS     $2DFD               ; {code.loc_2dfd} phase past 0x06 -- out of range, spin here forever (the watchdog resets the board)
2DFF: F6 A4           INC     $A4,X               ; {hard.workRam+A4} phase below 0x06 -- bump it
2E01: A9 11           LDA     #$11                ; load the tone-timer value
2E03: 85 B6           STA     $B6                 ; {hard.workRam+B6} arm the channel-2 priority SFX timer to 0x11
2E05: 20 B8 26        JSR     $26B8               ; {code.drawGridSideBorders} repaint the grid side borders

loc_2e08:
2E08: A6 8D           LDX     $8D                 ; {hard.workRam+8D} restore the caller's index

loc_2e0a:
2E0A: 60              RTS                         ; return

steerHeadAndSeedVelocity:
2E0B: A5 40           LDA     $40                 ; {hard.workRam+40} read the head's folded orientation
2E0D: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it through the orientation mask
2E0F: C9 34           CMP     #$34                ; at the top of the orientation range (0x34 or above)?
2E11: 90 03           BCC     $2E16               ; {code.loc_2e16} below the top -- continue
2E13: 4C 94 2E        JMP     $2E94               ; {code.guardHeadOrientationWrap} at the top -- guard the orientation wrap

loc_2e16:
2E16: C9 30           CMP     #$30                ; within the narrow top band (0x30 or above)?
2E18: B0 5D           BCS     $2E77               ; {code.loc_2e77} in the band -- go straight to the velocity-commit stage
2E1A: A5 70           LDA     $70                 ; {hard.workRam+70} read the head's folded position
2E1C: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it through the position mask
2E1E: C9 F8           CMP     #$F8                ; near the top of the position range (0xf8 or above)?
2E20: 90 04           BCC     $2E26               ; {code.loc_2e26} not near the top -- skip the reseed
2E22: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter
2E24: F0 03           BEQ     $2E29               ; {code.loc_2e29} only on the zero tick phase consider re-seeding the head

loc_2e26:
2E26: 4C C5 2E        JMP     $2EC5               ; {code.returnNoop} nothing to steer this tick -- jump to the shared return

loc_2e29:
2E29: A6 88           LDX     $88                 ; {hard.workRam+88} load the active object slot index
2E2B: B5 9A           LDA     $9A,X               ; {hard.workRam+9A} read that slot's centipede length counter
2E2D: C9 0B           CMP     #$0B                ; compare the length against 0x0b
2E2F: B0 F5           BCS     $2E26               ; {code.loc_2e26} segment already too long -- bail to the shared return
2E31: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
2E34: 29 03           AND     #$03                ; keep the low two bits of the roll
2E36: D0 EE           BNE     $2E26               ; {code.loc_2e26} roll did not permit a reseed -- bail
2E38: A9 14           LDA     #$14                ; load 0x14
2E3A: 85 B8           STA     $B8                 ; {hard.workRam+B8} stash it into the head cell $b8
2E3C: A9 30           LDA     #$30                ; load a fresh orientation constant 0x30
2E3E: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it with the orientation mask $ef
2E40: 85 40           STA     $40                 ; {hard.workRam+40} write the head's new orientation into $40
2E42: B5 AB           LDA     $AB,X               ; {hard.workRam+AB} read the slot's width byte from the $ab table
2E44: C9 02           CMP     #$02                ; compare width against 2
2E46: 90 12           BCC     $2E5A               ; {code.loc_2e5a} narrow slot -- take the small-velocity path
2E48: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
2E4B: 29 03           AND     #$03                ; keep the low two bits
2E4D: F0 0B           BEQ     $2E5A               ; {code.loc_2e5a} roll withheld the wide step -- take the small-velocity path
2E4F: A9 02           LDA     #$02                ; pick velocity magnitude 2 for the wide slot
2E51: 2C 0A 10        BIT     $100A               ; {hard.pokey+A} test the random register's sign bit
2E54: 10 0D           BPL     $2E63               ; {code.loc_2e63} sign clear -- keep the positive velocity and store it
2E56: A9 FE           LDA     #$FE                ; sign set -- flip to velocity -2
2E58: D0 09           BNE     $2E63               ; {code.loc_2e63} go store the signed velocity

loc_2e5a:
2E5A: A9 01           LDA     #$01                ; pick velocity magnitude 1
2E5C: 2C 0A 10        BIT     $100A               ; {hard.pokey+A} test the random register's sign bit
2E5F: 10 02           BPL     $2E63               ; {code.loc_2e63} sign clear -- keep the positive velocity
2E61: A9 FF           LDA     #$FF                ; sign set -- flip to velocity -1

loc_2e63:
2E63: 85 50           STA     $50                 ; {hard.workRam+50} store the random small velocity into the head-velocity seed $50
2E65: A9 00           LDA     #$00                ; load zero
2E67: 85 60           STA     $60                 ; {hard.workRam+60} clear the running head velocity $60
2E69: 85 80           STA     $80                 ; {hard.workRam+80} clear the shared column limit $80
2E6B: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
2E6E: 29 78           AND     #$78                ; keep bits 6..3 of the roll
2E70: 18              CLC                         ; clear carry for the add
2E71: 69 70           ADC     #$70                ; bias the random value up by 0x70
2E73: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it with the orientation mask $f0
2E75: 85 70           STA     $70                 ; {hard.workRam+70} write the head's fresh random position into $70

loc_2e77:
2E77: A5 43           LDA     $43                 ; {hard.workRam+43} read the $43 mode/control byte
2E79: 29 AF           AND     #$AF                ; mask its active mode bits
2E7B: D0 1D           BNE     $2E9A               ; {code.loc_2e9a} a mode bit is live -- reseed the whole wave
2E7D: A5 60           LDA     $60                 ; {hard.workRam+60} read the running head velocity $60
2E7F: A4 EF           LDY     $EF                 ; {hard.workRam+EF} load the direction selector $ef
2E81: F0 06           BEQ     $2E89               ; {code.loc_2e89} selector zero -- add the seed velocity
2E83: 38              SEC                         ; set carry for the subtract
2E84: E5 50           SBC     $50                 ; {hard.workRam+50} subtract the seed velocity $50 from the running velocity
2E86: 4C 8C 2E        JMP     $2E8C               ; {code.storeHeadVelocity} go commit the new velocity

loc_2e89:
2E89: 18              CLC                         ; clear carry for the add
2E8A: 65 50           ADC     $50                 ; {hard.workRam+50} add the seed velocity $50 onto the running velocity

storeHeadVelocity:
2E8C: 85 60           STA     $60                 ; {hard.workRam+60} commit the head's new velocity into $60
2E8E: 85 8B           STA     $8B                 ; {hard.workRam+8B} mirror the velocity into the $8b scratch cell
2E90: D0 0B           BNE     $2E9D               ; {code.advanceHeadOrientationAndStampTile} velocity nonzero -- advance the head's orientation
2E92: F0 06           BEQ     $2E9A               ; {code.loc_2e9a} velocity zero -- reseed the wave

guardHeadOrientationWrap:
2E94: 45 EF           EOR     $EF                 ; {hard.workRam+EF} unfold the forwarded orientation byte with $ef
2E96: C9 FA           CMP     #$FA                ; compare against the top of the orientation range 0xfa
2E98: B0 2B           BCS     $2EC5               ; {code.returnNoop} orientation topped out -- return

loc_2e9a:
2E9A: 4C E8 20        JMP     $20E8               ; {code.seedWaveState} reseed the wave state

advanceHeadOrientationAndStampTile:
2E9D: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter $00
2E9F: 29 03           AND     #$03                ; keep its low two bits
2EA1: D0 0D           BNE     $2EB0               ; {code.loc_2eb0} not the 4th tick -- skip the orientation rotate
2EA3: A5 40           LDA     $40                 ; {hard.workRam+40} read the folded head orientation $40
2EA5: 18              CLC                         ; clear carry for the rotate
2EA6: 69 01           ADC     #$01                ; rotate the orientation by one
2EA8: 29 03           AND     #$03                ; keep it within the low two bits
2EAA: 09 30           ORA     #$30                ; fold it back into the 0x30..0x33 range
2EAC: 45 EF           EOR     $EF                 ; {hard.workRam+EF} apply the orientation mask $ef
2EAE: 85 40           STA     $40                 ; {hard.workRam+40} store the rotated orientation

loc_2eb0:
2EB0: A0 00           LDY     #$00                ; target row 0 for the cell probe
2EB2: A5 70           LDA     $70                 ; {hard.workRam+70} load the head's position $70
2EB4: 20 2B 2C        JSR     $2C2B               ; {code.resolveTileCellAtXY} resolve the tile cell the head faces
2EB7: C9 40           CMP     #$40                ; compare the cell against 0x40
2EB9: B0 0A           BCS     $2EC5               ; {code.returnNoop} cell above the mushroom band -- return
2EBB: C9 3C           CMP     #$3C                ; compare the cell against 0x3c
2EBD: 90 06           BCC     $2EC5               ; {code.returnNoop} cell below the mushroom band -- return
2EBF: 29 FB           AND     #$FB                ; clear a bit of the eaten-mushroom marker
2EC1: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it with the orientation mask $ef
2EC3: 91 32           STA     ($32),Y             ; {hard.workRam+32} stamp the marker into the cell -- the head eats the mushroom

returnNoop:
2EC5: 60              RTS                         ; return

stepHeadSegment:
2EC6: A5 72           LDA     $72                 ; {hard.workRam+72} read the head coordinate $72
2EC8: A4 EF           LDY     $EF                 ; {hard.workRam+EF} load the vertical selector $ef
2ECA: F0 05           BEQ     $2ED1               ; {code.loc_2ed1} selector zero -- skip the fold
2ECC: 18              CLC                         ; clear carry for the add
2ECD: 69 07           ADC     #$07                ; bias the coordinate up by 7
2ECF: 49 FF           EOR     #$FF                ; invert it to mirror the coordinate for the flipped orientation

loc_2ed1:
2ED1: C9 F3           CMP     #$F3                ; compare the coordinate against the top band 0xf3
2ED3: B0 75           BCS     $2F4A               ; {code.loc_2f4a} head off the top of the field -- exit through the shared tail
2ED5: A9 04           LDA     #$04                ; load the row bias constant 0x04
2ED7: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it with the orientation mask $f0
2ED9: 18              CLC                         ; clear carry for the add
2EDA: 65 73           ADC     $73                 ; {hard.workRam+73} add the biased row coordinate $73
2EDC: C5 72           CMP     $72                 ; {hard.workRam+72} compare it against the head coordinate $72
2EDE: D0 25           BNE     $2F05               ; {code.loc_2f05} head not on its target row -- roll the head forward
2EE0: A5 43           LDA     $43                 ; {hard.workRam+43} read the $43 state gate
2EE2: 29 AF           AND     #$AF                ; mask its active mode bits
2EE4: D0 18           BNE     $2EFE               ; {code.loc_2efe} state busy -- drop the sweep into the spawn tick
2EE6: AD 01 0C        LDA     $0C01               ; {hard.in1} read the IN1 input port
2EE9: A6 86           LDX     $86                 ; {hard.workRam+86} read the owner slot $86
2EEB: 10 03           BPL     $2EF0               ; {code.loc_2ef0} owner non-negative -- keep the input reading
2EED: AD 0A 10        LDA     $100A               ; {hard.pokey+A} owner negative -- read the POKEY random register instead

loc_2ef0:
2EF0: C0 C0           CPY     #$C0                ; is the selector 0xc0?
2EF2: D0 06           BNE     $2EFA               ; {code.loc_2efa} no -- test the ordinary control bit
2EF4: 29 08           AND     #$08                ; test bit 3 of the probe
2EF6: F0 09           BEQ     $2F01               ; {code.loc_2f01} bit clear -- arm the footstep sound
2EF8: D0 04           BNE     $2EFE               ; {code.loc_2efe} bit set -- drop into the spawn tick

loc_2efa:
2EFA: 29 04           AND     #$04                ; test bit 2 of the probe
2EFC: F0 03           BEQ     $2F01               ; {code.loc_2f01} bit clear -- arm the footstep sound

loc_2efe:
2EFE: 4C 49 30        JMP     $3049               ; {code.tickSpawnCadence} drop the sweep into the spawn-cadence tick

loc_2f01:
2F01: A9 0B           LDA     #$0B                ; load the channel-3 SFX reload value 0x0b
2F03: 85 B4           STA     $B4                 ; {hard.workRam+B4} arm the channel-3 SFX timer $b4

loc_2f05:
2F05: A5 62           LDA     $62                 ; {hard.workRam+62} read the prior row coordinate $62
2F07: 85 8B           STA     $8B                 ; {hard.workRam+8B} publish it into the $8b scratch cell
2F09: A9 07           LDA     #$07                ; load the step constant 0x07
2F0B: 45 F4           EOR     $F4                 ; {hard.workRam+F4} fold it with the orientation byte $f4
2F0D: A4 72           LDY     $72                 ; {hard.workRam+72} stash the current head coordinate $72 in Y
2F0F: 18              CLC                         ; clear carry for the add
2F10: 65 72           ADC     $72                 ; {hard.workRam+72} step the head coordinate forward by $72
2F12: 85 72           STA     $72                 ; {hard.workRam+72} write the advanced head coordinate back to $72
2F14: 84 8D           STY     $8D                 ; {hard.workRam+8D} publish the prior head coordinate into $8d
2F16: A9 01           LDA     #$01                ; load the row-step constant 0x01
2F18: 45 F3           EOR     $F3                 ; {hard.workRam+F3} fold it with the orientation byte $f3
2F1A: 18              CLC                         ; clear carry for the add
2F1B: 65 8D           ADC     $8D                 ; {hard.workRam+8D} add the prior coordinate $8d
2F1D: A0 00           LDY     #$00                ; target row 0 for the cell probe
2F1F: 20 2B 2C        JSR     $2C2B               ; {code.resolveTileCellAtXY} resolve the destination grid cell ahead of the head
2F22: F0 29           BEQ     $2F4D               ; {code.loc_2f4d} destination empty -- continue into the per-segment router
2F24: 29 3F           AND     #$3F                ; keep the low six bits of the occupied cell
2F26: C9 38           CMP     #$38                ; compare against the boundary band 0x38
2F28: 90 20           BCC     $2F4A               ; {code.loc_2f4a} below the band -- exit through the shared tail
2F2A: E9 01           SBC     #$01                ; drop the cell code by one
2F2C: C9 3B           CMP     #$3B                ; is it boundary code 0x3b?
2F2E: F0 04           BEQ     $2F34               ; {code.loc_2f34} yes -- take the boundary-cell special path
2F30: C9 37           CMP     #$37                ; is it boundary code 0x37?
2F32: D0 0D           BNE     $2F41               ; {code.loc_2f41} no -- skip straight to the stamp

loc_2f34:
2F34: A9 00           LDA     #$00                ; load zero
2F36: 85 8B           STA     $8B                 ; {hard.workRam+8B} clear the step cell $8b
2F38: A9 01           LDA     #$01                ; load 1 for the accumulator step
2F3A: 20 B6 2D        JSR     $2DB6               ; {code.advancePathAccumulator} roll the path accumulator forward
2F3D: A0 00           LDY     #$00                ; target row 0
2F3F: A5 EF           LDA     $EF                 ; {hard.workRam+EF} load the orientation mask $ef

loc_2f41:
2F41: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold the stamp byte with $ef
2F43: 91 32           STA     ($32),Y             ; {hard.workRam+32} stamp the cell empty through the working tile pointer
2F45: D0 03           BNE     $2F4A               ; {code.loc_2f4a} stamp nonzero -- exit through the shared tail
2F47: 20 91 2B        JSR     $2B91               ; {code.maybeDecrementTableEntry} cell blanked -- decrement the matching mushroom tally

loc_2f4a:
2F4A: 4C 46 30        JMP     $3046               ; {code.loc_3046} jump to the shared exit-tail routine

loc_2f4d:
2F4D: A2 0D           LDX     #$0D                ; seed the segment index at the last slot 0x0d

routeSegmentByRange:
2F4F: B5 34           LDA     $34,X               ; {hard.workRam+34} read this slot's coordinate from the $34 array
2F51: C9 76           CMP     #$76                ; compare against the coarse X-band lower rail 0x76
2F53: 90 08           BCC     $2F5D               ; {code.loc_2f5d} below the near band -- take the range test
2F55: C9 B9           CMP     #$B9                ; compare against 0xb9
2F57: 90 69           BCC     $2FC2               ; {code.loc_2fc2} inside the far dead band -- skip this slot
2F59: C9 F8           CMP     #$F8                ; compare against the top rail 0xf8
2F5B: B0 65           BCS     $2FC2               ; {code.loc_2fc2} off the top -- skip this slot

loc_2f5d:
2F5D: B5 64           LDA     $64,X               ; {hard.workRam+64} read the slot's column coordinate from the $64 array
2F5F: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it with the orientation mask $f0
2F61: C9 F8           CMP     #$F8                ; compare the folded column against 0xf8
2F63: B0 5D           BCS     $2FC2               ; {code.loc_2fc2} off the horizontal edge -- skip this slot
2F65: 45 F0           EOR     $F0                 ; {hard.workRam+F0} unfold the column back
2F67: 38              SEC                         ; set carry for the subtract
2F68: E5 72           SBC     $72                 ; {hard.workRam+72} take the horizontal distance to the head $72
2F6A: 20 2B 38        JSR     $382B               ; {code.foldSignedMagnitude} fold that distance to its magnitude
2F6D: A8              TAY                         ; hold the horizontal distance in Y
2F6E: E0 0C           CPX     #$0C                ; is this the active head slot 0x0c?
2F70: D0 16           BNE     $2F88               ; {code.loc_2f88} no -- take the ordinary near-window test
2F72: B5 34           LDA     $34,X               ; {hard.workRam+34} read the slot coordinate again
2F74: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it with the orientation mask $ef
2F76: C9 20           CMP     #$20                ; compare against 0x20
2F78: B0 0E           BCS     $2F88               ; {code.loc_2f88} coordinate high -- take the ordinary near-window test
2F7A: A5 80           LDA     $80                 ; {hard.workRam+80} read the shared column limit $80
2F7C: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it with the orientation mask $f0
2F7E: C9 04           CMP     #$04                ; compare against 4
2F80: 90 06           BCC     $2F88               ; {code.loc_2f88} limit low -- take the ordinary near-window test
2F82: C0 07           CPY     #$07                ; compare the horizontal distance against 7
2F84: B0 3C           BCS     $2FC2               ; {code.loc_2fc2} too far horizontally -- skip this slot
2F86: 90 04           BCC     $2F8C               ; {code.loc_2f8c} within range -- go to the vertical distance test

loc_2f88:
2F88: C0 05           CPY     #$05                ; compare the horizontal distance against 5
2F8A: B0 36           BCS     $2FC2               ; {code.loc_2fc2} too far horizontally -- skip this slot

loc_2f8c:
2F8C: B5 54           LDA     $54,X               ; {hard.workRam+54} read the slot's row coordinate from the $54 array
2F8E: 38              SEC                         ; set carry for the subtract
2F8F: E5 62           SBC     $62                 ; {hard.workRam+62} take the vertical distance to the reference $62
2F91: 20 2B 38        JSR     $382B               ; {code.foldSignedMagnitude} fold that distance to its magnitude
2F94: A8              TAY                         ; hold the vertical distance in Y
2F95: E0 0D           CPX     #$0D                ; is this the last slot 0x0d?
2F97: F0 25           BEQ     $2FBE               ; {code.loc_2fbe} yes -- take the ballistic finish
2F99: E0 0C           CPX     #$0C                ; is this a trailing slot (X below 0x0c)?
2F9B: 90 60           BCC     $2FFD               ; {code.loc_2ffd} yes -- take the trailing-slot handler when the slot is below 0x0c
2F9D: B5 34           LDA     $34,X               ; {hard.workRam+34} read the head-slot coordinate again
2F9F: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it with the orientation mask $ef
2FA1: C9 20           CMP     #$20                ; compare against 0x20
2FA3: B0 10           BCS     $2FB5               ; {code.loc_2fb5} coordinate high -- take the wider vertical gate
2FA5: C0 06           CPY     #$06                ; compare the vertical distance against 6
2FA7: B0 19           BCS     $2FC2               ; {code.loc_2fc2} too far vertically -- skip this slot
2FA9: A0 02           LDY     #$02                ; set the collision result index to 2
2FAB: A9 04           LDA     #$04                ; load 4
2FAD: C5 80           CMP     $80                 ; {hard.workRam+80} compare 4 against the shared column limit $80
2FAF: F0 0A           BEQ     $2FBB               ; {code.loc_2fbb} already at the limit -- go seed the mover
2FB1: 85 80           STA     $80                 ; {hard.workRam+80} bump the shared column limit $80 to 4
2FB3: D0 95           BNE     $2F4A               ; {code.loc_2f4a} branch to the shared exit-tail routine

loc_2fb5:
2FB5: C0 0A           CPY     #$0A                ; compare the vertical distance against 0x0a
2FB7: B0 09           BCS     $2FC2               ; {code.loc_2fc2} too far vertically -- skip this slot
2FB9: A0 10           LDY     #$10                ; set the collision result index to 0x10

loc_2fbb:
2FBB: 4C 37 30        JMP     $3037               ; {code.loc_3037} jump to the mover seed

loc_2fbe:
2FBE: C0 0A           CPY     #$0A                ; last slot: is the vertical distance under 0x0a?
2FC0: 90 03           BCC     $2FC5               ; {code.loc_2fc5} yes -- take the ballistic finish

loc_2fc2:
2FC2: 4C 31 30        JMP     $3031               ; {code.advanceSegmentSlotLoop} skip this slot -- jump to the slot-loop step

loc_2fc5:
2FC5: A0 B6           LDY     #$B6                ; seed the shot origin cell $d7 to 0xb6
2FC7: 84 D7           STY     $D7                 ; {hard.workRam+D7} stash 0xb6 into the shot origin $d7
2FC9: A0 03           LDY     #$03                ; set the redraw index to 3
2FCB: A5 71           LDA     $71                 ; {hard.workRam+71} read the fired-from coordinate $71
2FCD: 38              SEC                         ; set carry for the subtract
2FCE: E5 73           SBC     $73                 ; {hard.workRam+73} subtract $73 to form the fired distance
2FD0: 20 2B 38        JSR     $382B               ; {code.foldSignedMagnitude} fold the fired distance to its magnitude
2FD3: C9 40           CMP     #$40                ; compare against 0x40
2FD5: B0 0C           BCS     $2FE3               ; {code.loc_2fe3} long shot -- take the far ballistic branch
2FD7: E6 D7           INC     $D7                 ; {hard.workRam+D7} bump the shot origin $d7
2FD9: A0 09           LDY     #$09                ; set the redraw index to 9
2FDB: C9 16           CMP     #$16                ; compare the fired distance against 0x16
2FDD: 90 04           BCC     $2FE3               ; {code.loc_2fe3} short shot -- take the near ballistic branch
2FDF: E6 D7           INC     $D7                 ; {hard.workRam+D7} bump the shot origin $d7 again
2FE1: A0 06           LDY     #$06                ; set the redraw index to 6

loc_2fe3:
2FE3: A9 80           LDA     #$80                ; load 0x80 to arm the ballistic-shot sweep cells
2FE5: 85 9F           STA     $9F                 ; {hard.workRam+9F} arm the shot sweep cell 0x9f
2FE7: 85 A1           STA     $A1                 ; {hard.workRam+A1} arm the companion sweep cell 0xa1
2FE9: A9 00           LDA     #$00                ; load zero to silence the channel-4 footstep timer
2FEB: 85 B5           STA     $B5                 ; {hard.workRam+B5} silence the channel-4 SFX timer 0xb5
2FED: A9 F0           LDA     #$F0                ; load the high vertical rail 0xf0
2FEF: C5 61           CMP     $61                 ; {hard.workRam+61} compare it against the shared vertical limit 0x61
2FF1: 90 06           BCC     $2FF9               ; {code.loc_2ff9} limit sits above 0xf0 -- go clamp it down
2FF3: A9 10           LDA     #$10                ; load the low vertical rail 0x10
2FF5: C5 61           CMP     $61                 ; {hard.workRam+61} compare it against the vertical limit 0x61
2FF7: 90 3E           BCC     $3037               ; {code.loc_3037} limit already inside the band -- skip the clamp store

loc_2ff9:
2FF9: 85 61           STA     $61                 ; {hard.workRam+61} store the clamped vertical limit back into 0x61
2FFB: D0 3A           BNE     $3037               ; {code.loc_3037} limit is nonzero -- head on into the path advance

loc_2ffd:
2FFD: C0 06           CPY     #$06                ; is the vertical distance 6 or beyond?
2FFF: B0 30           BCS     $3031               ; {code.advanceSegmentSlotLoop} past the trailing range -- step the slot loop
3001: A9 00           LDA     #$00                ; load zero
3003: 85 8B           STA     $8B                 ; {hard.workRam+8B} clear the scratch step cell 0x8b
3005: A0 10           LDY     #$10                ; preset the step addend to 0x10
3007: B5 34           LDA     $34,X               ; {hard.workRam+34} read this slot's phase byte 0x34,x
3009: 29 40           AND     #$40                ; isolate the bit-6 heading flag
300B: D0 04           BNE     $3011               ; {code.loc_3011} flag set -- keep the 0x10 step
300D: A0 00           LDY     #$00                ; clear the step addend to zero instead
300F: E6 8B           INC     $8B                 ; {hard.workRam+8B} bump the scratch step cell 0x8b

loc_3011:
3011: 98              TYA                         ; move the chosen step addend into A
3012: 20 AE 2D        JSR     $2DAE               ; {code.decrementActiveObjectDelay} tick this active object's spawn delay down
3015: E0 0B           CPX     #$0B                ; is X at slot 0x0b?
3017: F0 08           BEQ     $3021               ; {code.loc_3021} head slot -- skip the heading-bit clear
3019: B5 35           LDA     $35,X               ; {hard.workRam+35} read the slot's heading byte 0x35,x
301B: 30 04           BMI     $3021               ; {code.loc_3021} already negative -- leave it be
301D: 29 BF           AND     #$BF                ; clear bit 6 of the heading byte
301F: 95 35           STA     $35,X               ; {hard.workRam+35} store the cleared heading back

loc_3021:
3021: 20 10 23        JSR     $2310               ; {code.loadObjectTileInputs} marshal this object's tile-probe inputs
3024: 20 2B 2C        JSR     $2C2B               ; {code.resolveTileCellAtXY} resolve the grid cell under the object
3027: 86 8D           STX     $8D                 ; {hard.workRam+8D} stash the slot index across the stamp
3029: 20 A8 2B        JSR     $2BA8               ; {code.stampEmptyTileCell} stamp a mushroom into the empty cell
302C: A6 8D           LDX     $8D                 ; {hard.workRam+8D} restore the slot index
302E: 4C 3E 30        JMP     $303E               ; {code.loc_303e} jump into the row-redraw tail

advanceSegmentSlotLoop:
3031: CA              DEX                         ; step the segment cursor to the previous slot
3032: 30 15           BMI     $3049               ; {code.tickSpawnCadence} ran past the first slot -- end the sweep at the cadence tick
3034: 4C 4F 2F        JMP     $2F4F               ; {code.routeSegmentByRange} loop back to route the next segment slot

loc_3037:
3037: 84 8B           STY     $8B                 ; {hard.workRam+8B} stash the row step addend into 0x8b
3039: A9 00           LDA     #$00                ; seed the path accumulator with zero
303B: 20 B6 2D        JSR     $2DB6               ; {code.advancePathAccumulator} advance the segment's BCD path toward its target

loc_303e:
303E: A9 13           LDA     #$13                ; load the channel-1 effect arm value 0x13
3040: 85 B2           STA     $B2                 ; {hard.workRam+B2} arm the channel-1 effect timer 0xb2
3042: A9 FF           LDA     #$FF                ; load the slot-retired marker 0xff
3044: 95 34           STA     $34,X               ; {hard.workRam+34} retire slot X's row byte (high bit set frees it)

loc_3046:
3046: 20 79 2B        JSR     $2B79               ; {code.loc_2b79} run the 0x72/0x62 zero-page fixup

tickSpawnCadence:
3049: A6 88           LDX     $88                 ; {hard.workRam+88} load the active-object slot selector 0x88
304B: B5 94           LDA     $94,X               ; {hard.workRam+94} read this slot's spawn-tally byte 0x94,x
304D: 05 87           ORA     $87                 ; {hard.workRam+87} fold in the shared arm byte 0x87
304F: F0 10           BEQ     $3061               ; {code.loc_3061} both clear -- slot is idle, go advance its phase
3051: A5 41           LDA     $41                 ; {hard.workRam+41} read the folded timing key 0x41
3053: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it against the orientation mask 0xef
3055: C9 9C           CMP     #$9C                ; is the timing key at least 0x9c?
3057: 90 07           BCC     $3060               ; {code.loc_3060} below threshold -- nothing due, return
3059: C6 9F           DEC     $9F                 ; {hard.workRam+9F} tick the shared segment-spawn countdown 0x9f down
305B: D0 03           BNE     $3060               ; {code.loc_3060} countdown not yet spent -- return
305D: 20 C7 21        JSR     $21C7               ; {code.seedSegmentSpawnState} countdown hit zero -- seed the next segment spawn

loc_3060:
3060: 60              RTS                         ; return from the cadence tick

loc_3061:
3061: F6 9C           INC     $9C,X               ; {hard.workRam+9C} step this idle slot's phase counter 0x9c,x
3063: A9 40           LDA     #$40                ; load the arm value 0x40
3065: 85 87           STA     $87                 ; {hard.workRam+87} re-arm the shared gate byte 0x87
3067: 60              RTS                         ; return from the phase advance

updateSoundChannels:
3068: A6 86           LDX     $86                 ; {hard.workRam+86} read the master audio flag 0x86
306A: 10 0F           BPL     $307B               ; {code.loc_307b} audio is live -- go drive the voices
306C: A2 00           LDX     #$00                ; load zero for the mute
306E: 8E 01 10        STX     $1001               ; {hard.pokey+1} zero the channel-1 volume register
3071: 8E 03 10        STX     $1003               ; {hard.pokey+3} zero the channel-2 volume register
3074: 8E 05 10        STX     $1005               ; {hard.pokey+5} zero the channel-3 volume register
3077: 8E 07 10        STX     $1007               ; {hard.pokey+7} zero the channel-4 volume register
307A: 60              RTS                         ; all voices muted -- return

loc_307b:
307B: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter 0x00
307D: 4A              LSR     A                   ; shift the low bit into carry (odd/even frame)
307E: 90 19           BCC     $3099               ; {code.loc_3099} even frame -- skip the channel-4 voice
3080: A4 B5           LDY     $B5                 ; {hard.workRam+B5} read the channel-4 footstep timer 0xb5
3082: 98              TYA                         ; move it into A to test
3083: F0 11           BEQ     $3096               ; {code.loc_3096} timer spent -- leave channel 4 silent
3085: C6 B5           DEC     $B5                 ; {hard.workRam+B5} tick the channel-4 timer down
3087: D0 04           BNE     $308D               ; {code.loc_308d} not yet zero -- emit its current step
3089: A9 14           LDA     #$14                ; load the channel-4 reload value 0x14
308B: 85 B5           STA     $B5                 ; {hard.workRam+B5} reload the free-running channel-4 timer

loc_308d:
308D: B9 87 31        LDA     $3187,Y             ; {hard.rom+1187} fetch this step's channel-4 frequency from ROM
3090: 8D 06 10        STA     $1006               ; {hard.pokey+6} write it to the channel-4 frequency register
3093: B9 9B 31        LDA     $319B,Y             ; {hard.rom+119B} fetch this step's channel-4 volume from ROM

loc_3096:
3096: 8D 07 10        STA     $1007               ; {hard.pokey+7} write the channel-4 volume (or silence)

loc_3099:
3099: A4 B4           LDY     $B4                 ; {hard.workRam+B4} read the channel-3 timer 0xb4
309B: 98              TYA                         ; move it into A to test
309C: F0 0A           BEQ     $30A8               ; {code.loc_30a8} timer spent -- leave channel 3 silent
309E: C6 B4           DEC     $B4                 ; {hard.workRam+B4} tick the channel-3 timer down
30A0: B9 7C 31        LDA     $317C,Y             ; {hard.rom+117C} fetch this step's channel-3 frequency from ROM
30A3: 8D 04 10        STA     $1004               ; {hard.pokey+4} write it to the channel-3 frequency register
30A6: A9 64           LDA     #$64                ; load the fixed channel-3 volume 0x64

loc_30a8:
30A8: 8D 05 10        STA     $1005               ; {hard.pokey+5} write the channel-3 volume
30AB: A4 B6           LDY     $B6                 ; {hard.workRam+B6} read the channel-2 pitched pre-empt timer 0xb6
30AD: F0 28           BEQ     $30D7               ; {code.loc_30d7} pre-empt idle -- fall to the collision decision
30AF: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter 0x00
30B1: 29 07           AND     #$07                ; gate on every eighth frame
30B3: D0 73           BNE     $3128               ; {code.loc_3128} not this frame -- leave channel 2 alone
30B5: C6 B6           DEC     $B6                 ; {hard.workRam+B6} tick the pitched pre-empt timer down
30B7: 88              DEY                         ; pre-decrement its table index
30B8: F0 1D           BEQ     $30D7               ; {code.loc_30d7} pre-empt just expired -- release to the decision
30BA: B9 AF 31        LDA     $31AF,Y             ; {hard.rom+11AF} fetch the pitched-effect value from the 0x31af table
30BD: 8D 02 10        STA     $1002               ; {hard.pokey+2} write it to the channel-2 frequency register
30C0: A9 A4           LDA     #$A4                ; load the pitched-effect volume 0xa4
30C2: D0 61           BNE     $3125               ; {code.loc_3125} go store the channel-2 volume

loc_30c4:
30C4: A4 B8           LDY     $B8                 ; {hard.workRam+B8} read the channel-2 skitter sweep counter 0xb8
30C6: 88              DEY                         ; step the sweep counter down
30C7: D0 02           BNE     $30CB               ; {code.loc_30cb} not wrapped -- keep going
30C9: A0 14           LDY     #$14                ; reload the free-running sweep counter to 0x14

loc_30cb:
30CB: 84 B8           STY     $B8                 ; {hard.workRam+B8} store the sweep counter back
30CD: B9 C0 31        LDA     $31C0,Y             ; {hard.rom+11C0} fetch the sweep value from the 0x31c0 table
30D0: 8D 02 10        STA     $1002               ; {hard.pokey+2} write it to the channel-2 frequency register
30D3: A9 A4           LDA     #$A4                ; load the sweep volume 0xa4
30D5: D0 4E           BNE     $3125               ; {code.loc_3125} go store the channel-2 volume

loc_30d7:
30D7: A5 70           LDA     $70                 ; {hard.workRam+70} read the head position 0x70
30D9: 45 F0           EOR     $F0                 ; {hard.workRam+F0} fold it against the orientation byte 0xf0
30DB: C9 F8           CMP     #$F8                ; is the folded position at the top band 0xf8?
30DD: B0 36           BCS     $3115               ; {code.loc_3115} near the wall -- play the ordinary channel-2 effect
30DF: A5 43           LDA     $43                 ; {hard.workRam+43} read the state gate 0x43
30E1: 29 AF           AND     #$AF                ; mask its mode bits
30E3: D0 30           BNE     $3115               ; {code.loc_3115} a mode bit is set -- play the ordinary channel-2 effect
30E5: A5 40           LDA     $40                 ; {hard.workRam+40} read the head orientation 0x40
30E7: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it against the orientation mask 0xef
30E9: C9 34           CMP     #$34                ; is the orientation at 0x34 or more?
30EB: B0 28           BCS     $3115               ; {code.loc_3115} yes -- play the ordinary channel-2 effect
30ED: C9 20           CMP     #$20                ; is it at least 0x20?
30EF: B0 D3           BCS     $30C4               ; {code.loc_30c4} in the 0x20..0x34 band -- play the skitter sweep
30F1: A5 70           LDA     $70                 ; {hard.workRam+70} read the head position 0x70
30F3: 45 F4           EOR     $F4                 ; {hard.workRam+F4} fold it against 0xf4 for a noise pitch
30F5: 4A              LSR     A                   ; halve it
30F6: 49 FF           EOR     #$FF                ; complement it
30F8: 09 80           ORA     #$80                ; force the top bit so the noise stays high-register
30FA: 8D 02 10        STA     $1002               ; {hard.pokey+2} write the noise pitch to the channel-2 frequency register
30FD: A9 A4           LDA     #$A4                ; load the noise volume 0xa4
30FF: D0 24           BNE     $3125               ; {code.loc_3125} go store the channel-2 volume

loc_3101:
3101: A4 B2           LDY     $B2                 ; {hard.workRam+B2} read the channel-1 background timer 0xb2
3103: 98              TYA                         ; move it into A to test
3104: F0 0B           BEQ     $3111               ; {code.loc_3111} timer spent -- leave channel 1 silent
3106: C6 B2           DEC     $B2                 ; {hard.workRam+B2} tick the channel-1 background timer down
3108: B9 48 31        LDA     $3148,Y             ; {hard.rom+1148} fetch this step's channel-1 frequency from ROM
310B: 8D 00 10        STA     $1000               ; {hard.pokey} write it to the channel-1 frequency register
310E: B9 5B 31        LDA     $315B,Y             ; {hard.rom+115B} fetch this step's channel-1 volume from ROM

loc_3111:
3111: 8D 01 10        STA     $1001               ; {hard.pokey+1} write the channel-1 volume (or silence)
3114: 60              RTS                         ; return -- channel 1 done

loc_3115:
3115: A4 B3           LDY     $B3                 ; {hard.workRam+B3} read the channel-2 collision timer 0xb3
3117: 98              TYA                         ; move it into A to test
3118: F0 0B           BEQ     $3125               ; {code.loc_3125} timer spent -- silence channel 2
311A: C6 B3           DEC     $B3                 ; {hard.workRam+B3} tick the channel-2 collision timer down
311C: B9 6E 31        LDA     $316E,Y             ; {hard.rom+116E} fetch this step's channel-2 frequency from ROM
311F: 8D 02 10        STA     $1002               ; {hard.pokey+2} write it to the channel-2 frequency register
3122: B9 75 31        LDA     $3175,Y             ; {hard.rom+1175} fetch this step's channel-2 volume from ROM

loc_3125:
3125: 8D 03 10        STA     $1003               ; {hard.pokey+3} write the channel-2 volume (or silence)

loc_3128:
3128: A4 B7           LDY     $B7                 ; {hard.workRam+B7} read the channel-1 priority timer 0xb7
312A: F0 D5           BEQ     $3101               ; {code.loc_3101} priority idle -- use the plain background voice
312C: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter 0x00
312E: 29 03           AND     #$03                ; gate the priority effect on every fourth frame
3130: D0 16           BNE     $3148               ; {code.loc_3148} not this frame -- return
3132: C6 B7           DEC     $B7                 ; {hard.workRam+B7} tick the channel-1 priority timer down
3134: 88              DEY                         ; pre-decrement its table index
3135: F0 11           BEQ     $3148               ; {code.loc_3148} priority effect spent -- return
3137: B9 48 31        LDA     $3148,Y             ; {hard.rom+1148} fetch this step's channel-1 frequency from ROM
313A: 8D 00 10        STA     $1000               ; {hard.pokey} write it to the channel-1 frequency register
313D: B9 5B 31        LDA     $315B,Y             ; {hard.rom+115B} fetch this step's channel-1 volume from ROM
3140: F0 03           BEQ     $3145               ; {code.loc_3145} volume is zero -- store it as-is
3142: 18              CLC                         ; clear carry for the volume bump
3143: 69 02           ADC     #$02                ; nudge the priority volume up by 2 (louder than background)

loc_3145:
3145: 8D 01 10        STA     $1001               ; {hard.pokey+1} write the channel-1 priority volume

loc_3148:
3148: 60              RTS                         ; return from the sound update

; ---- $3149-$31D4: data ----
3149: 00 00 00 00 F0 E0 D0 C0 B0 A0 90 80 70 60 50 40
3159: 30 20 10 00 00 00 00 81 81 81 82 82 82 82 83 83
3169: 83 83 84 84 84 84 70 00 00 A0 00 C0 E0 A1 00 00
3179: A2 00 A2 A4 F0 E0 D0 C0 B0 A0 90 80 70 60 50 05
3189: 05 20 20 30 30 35 35 30 30 20 20 05 05 20 20 30
3199: 30 35 35 A1 00 A2 00 A3 00 A4 00 A3 00 A2 00 A1
31A9: 00 A2 00 A3 00 A2 00 28 28 30 28 28 30 3C 51 50
31B9: 50 60 50 50 60 74 A2 00 60 60 70 70 60 60 60 70
31C9: 70 70 50 50 80 80 50 50 50 80 80 80

transposeScreenBitmap:
31D5: A0 00           LDY     #$00                ; load zero for the low pointer byte
31D7: 84 32           STY     $32                 ; {hard.workRam+32} seat the tile pointer low byte at 0
31D9: A9 04           LDA     #$04                ; load the video base page 0x04
31DB: 85 33           STA     $33                 ; {hard.workRam+33} seat the tile pointer high byte at page 4
31DD: 84 8D           STY     $8D                 ; {hard.workRam+8D} clear the scratch column index

loc_31df:
31DF: A9 00           LDA     #$00                ; load zero
31E1: 85 8B           STA     $8B                 ; {hard.workRam+8B} clear the packed column-mask accumulator 0x8b
31E3: 84 8E           STY     $8E                 ; {hard.workRam+8E} save the row-start position into 0x8e
31E5: A2 08           LDX     #$08                ; count eight tiles per column group

loc_31e7:
31E7: B1 32           LDA     ($32),Y             ; {hard.workRam+32} read one tile cell through the pointer
31E9: 29 3F           AND     #$3F                ; keep only the low six bits (glyph code)
31EB: C9 38           CMP     #$38                ; compare against the solid glyph band 0x38
31ED: 26 8B           ROL     $8B                 ; {hard.workRam+8B} roll the solid/blank bit into the mask 0x8b
31EF: C8              INY                         ; step to the next tile
31F0: CA              DEX                         ; count this tile off
31F1: D0 F4           BNE     $31E7               ; {code.loc_31e7} loop for the whole eight-tile group
31F3: A6 8D           LDX     $8D                 ; {hard.workRam+8D} load the scratch column index
31F5: BD 00 01        LDA     $0100,X             ; {hard.workRam+100} read the buffered column from the 0x0100 scratch
31F8: E6 8D           INC     $8D                 ; {hard.workRam+8D} advance the scratch column index
31FA: A8              TAY                         ; hold the old buffered byte
31FB: A5 8B           LDA     $8B                 ; {hard.workRam+8B} load the freshly packed mask
31FD: 9D 00 01        STA     $0100,X             ; {hard.workRam+100} store the new mask into the column scratch
3200: 84 8B           STY     $8B                 ; {hard.workRam+8B} move the old buffered byte in to be written out
3202: A4 8E           LDY     $8E                 ; {hard.workRam+8E} restore the row-start position
3204: A2 08           LDX     #$08                ; count eight tiles per column group

loc_3206:
3206: A9 00           LDA     #$00                ; load a blank tile
3208: 26 8B           ROL     $8B                 ; {hard.workRam+8B} roll the top bit of the swapped-in mask into carry
320A: 90 04           BCC     $3210               ; {code.loc_3210} bit clear -- write the blank
320C: A9 3F           LDA     #$3F                ; load the solid glyph 0x3f
320E: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold it against the orientation mask for the solid tile

loc_3210:
3210: 91 32           STA     ($32),Y             ; {hard.workRam+32} write the tile (blank or solid) back through the pointer
3212: C8              INY                         ; step to the next tile
3213: CA              DEX                         ; count this tile off
3214: D0 F0           BNE     $3206               ; {code.loc_3206} loop for the whole eight-tile group
3216: 98              TYA                         ; move the pointer low position into A
3217: D0 02           BNE     $321B               ; {code.loc_321b} not wrapped past zero -- skip the page bump
3219: E6 33           INC     $33                 ; {hard.workRam+33} page the pointer high byte up on the row wrap

loc_321b:
321B: C0 C0           CPY     #$C0                ; has the low pointer reached 0xc0?
321D: D0 C0           BNE     $31DF               ; {code.loc_31df} no -- go pack the next group
321F: A5 33           LDA     $33                 ; {hard.workRam+33} read the pointer high byte
3221: C9 07           CMP     #$07                ; has it reached page 7?
3223: D0 BA           BNE     $31DF               ; {code.loc_31df} not the last page -- keep transposing
3225: 60              RTS                         ; whole grid covered -- return

clampAndHalveSignedDelta:
3226: C9 08           CMP     #$08                ; compare the signed delta against the low rail 0x08
3228: 90 0C           BCC     $3236               ; {code.loc_3236} below 0x08 -- pass the extreme through untouched
322A: C9 F8           CMP     #$F8                ; compare against the high rail 0xf8
322C: B0 08           BCS     $3236               ; {code.loc_3236} at or above 0xf8 -- pass the extreme through
322E: C9 80           CMP     #$80                ; test which half the delta lies in
3230: A9 08           LDA     #$08                ; load the low rail 0x08
3232: 90 02           BCC     $3236               ; {code.loc_3236} delta below 0x80 -- fold to the low rail
3234: A9 F8           LDA     #$F8                ; delta at or above 0x80 -- fold to the high rail 0xf8

loc_3236:
3236: C9 80           CMP     #$80                ; compare the clamped delta against 0x80 to capture its sign bit in carry
3238: 6A              ROR     A                   ; rotate right -- arithmetic halve of the delta, copying the sign back into bit7
3239: A8              TAY                         ; park the halved delta in Y for the caller's accumulate
323A: A9 00           LDA     #$00                ; clear A to build the dropped-fraction byte
323C: 6A              ROR     A                   ; rotate the bit shifted out of the halve into A's top bit -- the carried sub-pixel fraction
323D: 60              RTS                         ; return with the halved delta in Y and the fraction in A, carry left clear for the follow-on add

buildSortedObjectTable:
323E: A9 FF           LDA     #$FF                ; load 0xff to mark the object-table high-water cells
3240: A2 01           LDX     #$01                ; seed the object loop index to the second object (X=1)
3242: 85 C1           STA     $C1                 ; {hard.workRam+C1} stamp the high-water mark loc_c1 to 0xff
3244: 85 C2           STA     $C2                 ; {hard.workRam+C2} stamp the high-water mark loc_c2 to 0xff
3246: F8              SED                         ; enter decimal mode for the BCD rate accumulators
3247: A5 FB           LDA     $FB                 ; {hard.workRam+FB} read the low byte of the frame delta loc_fb
3249: 18              CLC                         ; clear carry before the multi-byte add
324A: 6D 8E 01        ADC     $018E               ; {hard.workRam+18E} add it into the wide rate accumulator low byte
324D: 8D 8E 01        STA     $018E               ; {hard.workRam+18E} store the wide accumulator low byte
3250: A5 FC           LDA     $FC                 ; {hard.workRam+FC} read the frame delta high byte loc_fc
3252: 6D 8F 01        ADC     $018F               ; {hard.workRam+18F} add it with carry into the next accumulator byte
3255: 8D 8F 01        STA     $018F               ; {hard.workRam+18F} store it
3258: AD 90 01        LDA     $0190               ; {hard.workRam+190} read the wide accumulator byte loc_0190
325B: 69 00           ADC     #$00                ; propagate the carry up
325D: 8D 90 01        STA     $0190               ; {hard.workRam+190} store it
3260: AD 91 01        LDA     $0191               ; {hard.workRam+191} read the wide accumulator top byte loc_0191
3263: 69 00           ADC     #$00                ; propagate the carry up
3265: B0 1C           BCS     $3283               ; {code.loc_3283} if the wide accumulator overflowed its top, skip advancing the narrow one
3267: 8D 91 01        STA     $0191               ; {hard.workRam+191} store the wide accumulator top byte
326A: AD 8B 01        LDA     $018B               ; {hard.workRam+18B} read the narrow rate accumulator low byte loc_018b
326D: 18              CLC                         ; clear carry
326E: 65 89           ADC     $89                 ; {hard.workRam+89} add the score rate loc_89 into it
3270: 8D 8B 01        STA     $018B               ; {hard.workRam+18B} store the narrow accumulator low byte
3273: AD 8C 01        LDA     $018C               ; {hard.workRam+18C} read the narrow accumulator byte loc_018c
3276: 69 00           ADC     #$00                ; propagate the carry up
3278: 8D 8C 01        STA     $018C               ; {hard.workRam+18C} store it
327B: AD 8D 01        LDA     $018D               ; {hard.workRam+18D} read the narrow accumulator top byte loc_018d
327E: 69 00           ADC     #$00                ; propagate the carry up
3280: 8D 8D 01        STA     $018D               ; {hard.workRam+18D} store it

loc_3283:
3283: D8              CLD                         ; leave decimal mode

loc_3284:
3284: A0 00           LDY     #$00                ; begin the record scan at the head of the object table

loc_3286:
3286: B9 02 00        LDA     $0002,Y             ; {hard.workRam+2} read the record's low key byte at loc_02+y
3289: D5 A8           CMP     $A8,X               ; {hard.workRam+A8} compare it against the object's low field loc_a8+x
328B: B9 03 00        LDA     $0003,Y             ; {hard.workRam+3} read the record's middle key byte loc_03+y
328E: F5 AA           SBC     $AA,X               ; {hard.workRam+AA} subtract the object's middle field loc_aa+x with borrow
3290: B9 04 00        LDA     $0004,Y             ; {hard.workRam+4} read the record's high key byte loc_04+y
3293: F5 AC           SBC     $AC,X               ; {hard.workRam+AC} subtract the object's high field loc_ac+x with borrow
3295: 90 2E           BCC     $32C5               ; {code.loc_32c5} record key smaller than the object -- insert the object at this slot
3297: C8              INY                         ; step to the next 3-byte record
3298: C8              INY                         ; step over the second key byte
3299: C8              INY                         ; step over the third key byte
329A: C0 18           CPY     #$18                ; reached the end of the 0x18-byte table?
329C: 90 E8           BCC     $3286               ; {code.loc_3286} no -- keep scanning for the insertion slot

loc_329e:
329E: CA              DEX                         ; move to the previous object
329F: 10 E3           BPL     $3284               ; {code.loc_3284} loop while objects remain
32A1: A5 C2           LDA     $C2                 ; {hard.workRam+C2} read the high-water mark loc_c2
32A3: 30 0E           BMI     $32B3               ; {code.loc_32b3} negative (unused) -- skip the clamp
32A5: C5 C1           CMP     $C1                 ; {hard.workRam+C1} compare it against loc_c1
32A7: 90 0A           BCC     $32B3               ; {code.loc_32b3} below loc_c1 -- skip the clamp
32A9: 69 02           ADC     #$02                ; bump the mark forward by one record (three bytes; carry is set here so +2 becomes +3)
32AB: C9 18           CMP     #$18                ; reached the 0x18 record cap?
32AD: 90 02           BCC     $32B1               ; {code.loc_32b1} below the cap -- keep the mark
32AF: A9 FF           LDA     #$FF                ; else clamp the mark to 0xff

loc_32b1:
32B1: 85 C2           STA     $C2                 ; {hard.workRam+C2} store the updated high-water mark loc_c2

loc_32b3:
32B3: A9 00           LDA     #$00                ; clear A
32B5: 85 C0           STA     $C0                 ; {hard.workRam+C0} clear loc_c0
32B7: A5 C2           LDA     $C2                 ; {hard.workRam+C2} read the high-water mark loc_c2
32B9: 25 C1           AND     $C1                 ; {hard.workRam+C1} AND it with loc_c1
32BB: 10 07           BPL     $32C4               ; {code.loc_32c4} either mark non-negative -- skip the grid redraw
32BD: A9 00           LDA     #$00                ; clear A
32BF: 85 01           STA     $01                 ; {hard.workRam+1} clear loc_01 before redrawing
32C1: 20 5C 2D        JSR     $2D5C               ; {code.plotRecordFieldColumns} redraw the whole record grid via plotRecordFieldColumns

loc_32c4:
32C4: 60              RTS                         ; return

loc_32c5:
32C5: 86 8D           STX     $8D                 ; {hard.workRam+8D} save the object index for the insert
32C7: 84 8E           STY     $8E                 ; {hard.workRam+8E} save the insertion point index
32C9: 94 C1           STY     $C1,X               ; {hard.workRam+C1} record the insertion point into the loc_c1+x high-water cell
32CB: A2 17           LDX     #$17                ; start shifting from the top record (index 0x17)

loc_32cd:
32CD: B5 17           LDA     $17,X               ; {hard.workRam+17} read the record byte at loc_17+x
32CF: 95 1A           STA     $1A,X               ; {hard.workRam+1A} move it up one 3-byte record to loc_1a+x
32D1: BD FF FF        LDA     $FFFF,X             ; read the parallel key byte just below the table base
32D4: 95 02           STA     $02,X               ; {hard.workRam+2} move it up one record to loc_02+x
32D6: CA              DEX                         ; step down one byte
32D7: E4 8E           CPX     $8E                 ; {hard.workRam+8E} reached the insertion point?
32D9: D0 F2           BNE     $32CD               ; {code.loc_32cd} no -- keep shifting records up
32DB: A9 01           LDA     #$01                ; load 1 to seed the vacated head record
32DD: 95 1A           STA     $1A,X               ; {hard.workRam+1A} write 01 into the freed record's first byte
32DF: A9 00           LDA     #$00                ; clear A
32E1: 95 1B           STA     $1B,X               ; {hard.workRam+1B} write 00 into the freed record's second byte
32E3: 95 1C           STA     $1C,X               ; {hard.workRam+1C} write 00 into the freed record's third byte
32E5: 85 B9           STA     $B9                 ; {hard.workRam+B9} clear the trackball accumulator loc_b9
32E7: A6 8D           LDX     $8D                 ; {hard.workRam+8D} restore the object index
32E9: B5 AC           LDA     $AC,X               ; {hard.workRam+AC} read the object's high key byte loc_ac+x
32EB: 99 04 00        STA     $0004,Y             ; {hard.workRam+4} write it into the freed slot's high key
32EE: B5 AA           LDA     $AA,X               ; {hard.workRam+AA} read the object's middle key byte loc_aa+x
32F0: 99 03 00        STA     $0003,Y             ; {hard.workRam+3} write it into the freed slot's middle key
32F3: B5 A8           LDA     $A8,X               ; {hard.workRam+A8} read the object's low key byte loc_a8+x
32F5: 99 02 00        STA     $0002,Y             ; {hard.workRam+2} write it into the freed slot's low key
32F8: A9 F0           LDA     #$F0                ; load the inserted flag value 0xf0
32FA: 85 01           STA     $01                 ; {hard.workRam+1} flag loc_01 that a record was inserted
32FC: D0 A0           BNE     $329E               ; {code.loc_329e} go back to advance the object loop

plotObjectCoordinates:
32FE: A9 1F           LDA     #$1F                ; load the score-row cursor low mask 0x1f
3300: 45 F5           EOR     $F5                 ; {hard.workRam+F5} fold in the flip byte loc_f5
3302: 85 91           STA     $91                 ; {hard.workRam+91} seed the draw cursor low byte loc_91
3304: A9 04           LDA     #$04                ; load the cursor high mask 0x04
3306: 45 F7           EOR     $F7                 ; {hard.workRam+F7} fold in the flip byte loc_f7
3308: 85 92           STA     $92                 ; {hard.workRam+92} seed the draw cursor high byte loc_92
330A: A5 AC           LDA     $AC                 ; {hard.workRam+AC} read the object's high coordinate byte loc_ac
330C: 38              SEC                         ; set carry -- digit mode with leading-zero blanking
330D: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two decimal digits (plotByteAsTwoDigits)
3310: A5 AA           LDA     $AA                 ; {hard.workRam+AA} read the object's middle coordinate byte loc_aa
3312: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits, carry threaded from the prior pair
3315: A5 A8           LDA     $A8                 ; {hard.workRam+A8} read the object's low coordinate byte loc_a8
3317: 18              CLC                         ; clear carry so the final pair prints plain
3318: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits
331B: A4 89           LDY     $89                 ; {hard.workRam+89} read the slot count loc_89
331D: 88              DEY                         ; decrement it
331E: F0 1D           BEQ     $333D               ; {code.loc_333d} if only one slot, skip the second object
3320: A9 07           LDA     #$07                ; load the second object's cursor high mask 0x07
3322: 45 F7           EOR     $F7                 ; {hard.workRam+F7} fold in the flip byte loc_f7
3324: 85 92           STA     $92                 ; {hard.workRam+92} seed the cursor high byte loc_92
3326: A9 1F           LDA     #$1F                ; load the cursor low mask 0x1f
3328: 45 F5           EOR     $F5                 ; {hard.workRam+F5} fold in the flip byte loc_f5
332A: 85 91           STA     $91                 ; {hard.workRam+91} seed the cursor low byte loc_91
332C: A5 AD           LDA     $AD                 ; {hard.workRam+AD} read the second object's high coordinate loc_ad
332E: 38              SEC                         ; set carry -- digit mode
332F: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits
3332: A5 AB           LDA     $AB                 ; {hard.workRam+AB} read the second object's middle coordinate loc_ab
3334: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits
3337: A5 A9           LDA     $A9                 ; {hard.workRam+A9} read the second object's low coordinate loc_a9
3339: 18              CLC                         ; clear carry
333A: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits

loc_333d:
333D: A9 9F           LDA     #$9F                ; load the score-line cursor low mask 0x9f
333F: 45 F5           EOR     $F5                 ; {hard.workRam+F5} fold in the flip byte loc_f5
3341: 85 91           STA     $91                 ; {hard.workRam+91} seed the draw cursor low byte loc_91
3343: A9 05           LDA     #$05                ; load the cursor high mask 0x05
3345: 45 F7           EOR     $F7                 ; {hard.workRam+F7} fold in the flip byte loc_f7
3347: 85 92           STA     $92                 ; {hard.workRam+92} seed the draw cursor high byte loc_92
3349: A5 04           LDA     $04                 ; {hard.workRam+4} read the score high byte loc_04
334B: 38              SEC                         ; set carry -- digit mode
334C: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits
334F: A5 03           LDA     $03                 ; {hard.workRam+3} read the score middle byte loc_03
3351: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits
3354: A5 02           LDA     $02                 ; {hard.workRam+2} read the score low byte loc_02
3356: 18              CLC                         ; clear carry for the final pair
3357: 4C 4F 38        JMP     $384F               ; {code.plotByteAsTwoDigits} tail into the two-digit plotter for the last pair

; ---- $335A-$335D: data ----
335A: FF FF FF F1

advanceAllSegmentColumns:
335E: A2 02           LDX     #$02                ; preload the column cursor to the last column (index 2)

advanceSegmentColumns:
3360: AD 01 0C        LDA     $0C01               ; {hard.in1} read input port IN1 for the per-column control bits
3363: E0 01           CPX     #$01                ; which column is this?
3365: F0 03           BEQ     $336A               ; {code.loc_336a} column 1 -- take the two-shift path toward bit 6
3367: B0 02           BCS     $336B               ; {code.loc_336b} column 2 -- take the single-shift path toward bit 7
3369: 0A              ASL     A                   ; column 0 -- one extra shift so bit 5 becomes the control bit

loc_336a:
336A: 0A              ASL     A                   ; shift again toward the selected control bit

loc_336b:
336B: 0A              ASL     A                   ; shift the per-column control bit out into carry
336C: B5 CF           LDA     $CF,X               ; {hard.workRam+CF} load this column's body/step cell SEGMENT_COL_BODY (0xcf array)
336E: 29 1F           AND     #$1F                ; keep the low 5-bit step index
3370: B0 37           BCS     $33A9               ; {code.loc_33a9} control bit set -- take the wrap/reset branch
3372: F0 10           BEQ     $3384               ; {code.loc_3384} step index already zero -- store it unchanged
3374: C9 1B           CMP     #$1B                ; step index past 0x1b?
3376: B0 0A           BCS     $3382               ; {code.loc_3382} yes -- back it off by one toward the clamp
3378: A8              TAY                         ; stash the step index in Y
3379: A5 D4           LDA     $D4                 ; {hard.workRam+D4} read the movement frame counter SEGMENT_MOVE_FRAME_COUNTER (0xd4)
337B: 29 07           AND     #$07                ; keep its low 3 bits
337D: C9 07           CMP     #$07                ; are they all set -- every 8th frame?
337F: 98              TYA                         ; restore the step index into A
3380: 90 02           BCC     $3384               ; {code.loc_3384} not the 8th frame -- store the step unchanged

loc_3382:
3382: E9 01           SBC     #$01                ; nudge the step index back toward its clamp by one

loc_3384:
3384: 95 CF           STA     $CF,X               ; {hard.workRam+CF} store the updated body/step cell
3386: AD 01 0C        LDA     $0C01               ; {hard.in1} read input port IN1 again
3389: 29 10           AND     #$10                ; isolate bit 4
338B: D0 04           BNE     $3391               ; {code.loc_3391} bit 4 set -- skip refilling the reload timer
338D: A9 F0           LDA     #$F0                ; load the reload value 0xf0
338F: 85 D2           STA     $D2                 ; {hard.workRam+D2} refill the shared reload timer SEGMENT_RELOAD_TIMER (0xd2)

loc_3391:
3391: A5 D2           LDA     $D2                 ; {hard.workRam+D2} read the reload timer
3393: F0 08           BEQ     $339D               ; {code.loc_339d} timer resting at zero -- nothing to blank
3395: C6 D2           DEC     $D2                 ; {hard.workRam+D2} count the reload timer down
3397: A9 00           LDA     #$00                ; load zero
3399: 95 CF           STA     $CF,X               ; {hard.workRam+CF} blank this column's body cell
339B: 95 CC           STA     $CC,X               ; {hard.workRam+CC} blank this column's life slot SEGMENT_COL_LIFE_TIMER (0xcc array)

loc_339d:
339D: 18              CLC                         ; clear the motion-contribution carry
339E: B5 CC           LDA     $CC,X               ; {hard.workRam+CC} read this column's life timer
33A0: F0 23           BEQ     $33C5               ; {code.loc_33c5} life timer already zero -- no motion this pass
33A2: D6 CC           DEC     $CC,X               ; {hard.workRam+CC} count the life timer down
33A4: D0 1F           BNE     $33C5               ; {code.loc_33c5} not yet zero -- no motion this pass
33A6: 38              SEC                         ; life timer hit zero this pass -- set the contribution carry
33A7: B0 1C           BCS     $33C5               ; {code.loc_33c5} take the motion-contribution path

loc_33a9:
33A9: C9 1B           CMP     #$1B                ; step index past 0x1b?
33AB: B0 09           BCS     $33B6               ; {code.loc_33b6} yes -- clamp the body to 0x1f
33AD: B5 CF           LDA     $CF,X               ; {hard.workRam+CF} reload the full body/step cell
33AF: 69 20           ADC     #$20                ; add 0x20 to advance one wrap unit
33B1: 90 D1           BCC     $3384               ; {code.loc_3384} no carry out -- store the wrapped value
33B3: F0 01           BEQ     $33B6               ; {code.loc_33b6} wrapped exactly to zero -- clamp to 0x1f
33B5: 18              CLC                         ; else clear carry for the plain store

loc_33b6:
33B6: A9 1F           LDA     #$1F                ; load the clamp value 0x1f
33B8: B0 CA           BCS     $3384               ; {code.loc_3384} carry set -- store the clamp value
33BA: 95 CF           STA     $CF,X               ; {hard.workRam+CF} store 0x1f into the body/step cell
33BC: B5 CC           LDA     $CC,X               ; {hard.workRam+CC} read this column's life timer
33BE: F0 01           BEQ     $33C1               ; {code.loc_33c1} timer zero -- reload it fresh
33C0: 38              SEC                         ; else mark a motion contribution

loc_33c1:
33C1: A9 78           LDA     #$78                ; load the life-timer reload value 0x78
33C3: 95 CC           STA     $CC,X               ; {hard.workRam+CC} load the life timer directly to 0x78

loc_33c5:
33C5: 90 2A           BCC     $33F1               ; {code.loc_33f1} no contribution this pass -- skip the accumulate
33C7: A9 00           LDA     #$00                ; start the per-column row delta at 0
33C9: E0 01           CPX     #$01                ; which column is this?
33CB: 90 16           BCC     $33E3               ; {code.loc_33e3} column 0 -- leave the row delta at 0
33CD: F0 0C           BEQ     $33DB               ; {code.loc_33db} column 1 -- derive the delta from bit 4 of loc_d3
33CF: A5 D3           LDA     $D3                 ; {hard.workRam+D3} column 2 -- read the phase cell loc_d3
33D1: 29 0C           AND     #$0C                ; keep bits 3-2
33D3: 4A              LSR     A                   ; shift them down
33D4: 4A              LSR     A                   ; down to a small row delta
33D5: F0 0C           BEQ     $33E3               ; {code.loc_33e3} zero -- no add
33D7: 69 02           ADC     #$02                ; else bias the row delta by 2
33D9: D0 08           BNE     $33E3               ; {code.loc_33e3} go accumulate the row delta

loc_33db:
33DB: A5 D3           LDA     $D3                 ; {hard.workRam+D3} column 1 -- read the phase cell loc_d3
33DD: 29 10           AND     #$10                ; keep bit 4
33DF: F0 02           BEQ     $33E3               ; {code.loc_33e3} clear -- leave the row delta at 0
33E1: A9 01           LDA     #$01                ; set -- row delta of 1

loc_33e3:
33E3: 38              SEC                         ; set carry so the fold adds delta+1
33E4: 48              PHA                         ; save the row delta on the stack
33E5: 65 CA           ADC     $CA                 ; {hard.workRam+CA} fold row-delta+1 into SEGMENT_MOVE_ACCUM (0xca)
33E7: 85 CA           STA     $CA                 ; {hard.workRam+CA} store the shared movement accumulator
33E9: 68              PLA                         ; restore the row delta
33EA: 38              SEC                         ; set carry so the fold adds delta+1
33EB: 65 C9           ADC     $C9                 ; {hard.workRam+C9} fold row-delta+1 into the parallel accumulator SEGMENT_MOVE_ACCUM_B (0xc9)
33ED: 85 C9           STA     $C9                 ; {hard.workRam+C9} store the second movement accumulator
33EF: F6 C5           INC     $C5,X               ; {hard.workRam+C5} bump this column's progress counter in the loc_c5 array

loc_33f1:
33F1: CA              DEX                         ; step the column cursor down to the next centipede body column
33F2: 30 03           BMI     $33F7               ; {code.loc_33f7} past the first column -- go measure the movement accumulator
33F4: 4C 60 33        JMP     $3360               ; {code.advanceSegmentColumns} more columns left -- loop back to walk the next body column

loc_33f7:
33F7: A5 D3           LDA     $D3                 ; {hard.workRam+D3} read the row-phase byte that says which row the creature is crossing
33F9: 4A              LSR     A                   ; shift the phase down
33FA: 4A              LSR     A                   ; shift again
33FB: 4A              LSR     A                   ; shift again
33FC: 4A              LSR     A                   ; shift again
33FD: 4A              LSR     A                   ; five shifts leave the row-phase index (phase >> 5)
33FE: A8              TAY                         ; hold that as the row index into the threshold table
33FF: A5 CA           LDA     $CA                 ; {hard.workRam+CA} read the segment-movement accumulator
3401: 38              SEC                         ; prep for the subtract
3402: F9 13 34        SBC     $3413,Y             ; {hard.rom+1413} subtract this row's crossing threshold from the accumulator
3405: 30 14           BMI     $341B               ; {code.stepPhasedCountersAndWrapCells} still short of the threshold -- leave the accumulator and fall to the phased tail
3407: 85 CA           STA     $CA                 ; {hard.workRam+CA} threshold met -- commit the reduced accumulator
3409: E6 CB           INC     $CB                 ; {hard.workRam+CB} bump the row-crossing counter: the creature has stepped one row down
340B: C0 03           CPY     #$03                ; is this the top row (index 3)?
340D: D0 0C           BNE     $341B               ; {code.stepPhasedCountersAndWrapCells} not the top row -- go do the phased bookkeeping
340F: E6 CB           INC     $CB                 ; {hard.workRam+CB} top row -- bump the crossing counter a second time so the top row marches faster
3411: D0 08           BNE     $341B               ; {code.stepPhasedCountersAndWrapCells} off to the phased tail (a wrap to zero here would fall through as the table guard)

; ---- $3413-$341A: data ----
3413: 7F 02 04 04 05 03 7F 7F

stepPhasedCountersAndWrapCells:
341B: A5 D3           LDA     $D3                 ; {hard.workRam+D3} read the row-phase byte
341D: 29 03           AND     #$03                ; keep the low two phase bits
341F: A8              TAY                         ; hold the phase as the sub-step selector
3420: F0 1A           BEQ     $343C               ; {code.loc_343c} phase 0 -- no sub-step to subtract, go store the accumulator
3422: 4A              LSR     A                   ; halve the phase
3423: 69 00           ADC     #$00                ; round the sub-step up with the carry (yields 0, 1, or 1->2)
3425: 49 FF           EOR     #$FF                ; one's-complement the sub-step to set up the subtract
3427: 38              SEC                         ; prep for the subtract
3428: 65 C9           ADC     $C9                 ; {hard.workRam+C9} subtract the sub-step from the accumulator low byte
342A: B0 08           BCS     $3434               ; {code.loc_3434} no borrow -- skip the high byte
342C: 65 CB           ADC     $CB                 ; {hard.workRam+CB} borrow -- pull it out of the accumulator high byte
342E: 30 0E           BMI     $343E               ; {code.loc_343e} underflow past zero -- floor the accumulator so motion never runs backward
3430: 85 CB           STA     $CB                 ; {hard.workRam+CB} store the accumulator high byte
3432: A9 00           LDA     #$00                ; low byte becomes zero at the floor

loc_3434:
3434: C0 02           CPY     #$02                ; was the phase 2 or more?
3436: B0 02           BCS     $343A               ; {code.loc_343a} phase 2+ -- take only one wrap-counter bump
3438: E6 C8           INC     $C8                 ; {hard.workRam+C8} lower phase -- bump the wrap counter an extra time

loc_343a:
343A: E6 C8           INC     $C8                 ; {hard.workRam+C8} bump the wrap counter

loc_343c:
343C: 85 C9           STA     $C9                 ; {hard.workRam+C9} store the accumulator low byte

loc_343e:
343E: E6 D4           INC     $D4                 ; {hard.workRam+D4} tick the free-running segment movement frame counter
3440: A5 D4           LDA     $D4                 ; {hard.workRam+D4} read the frame counter back
3442: 4A              LSR     A                   ; shift out its low bit
3443: B0 27           BCS     $346C               ; {code.loc_346c} odd frame -- nothing more to normalise this pass, return
3445: A0 00           LDY     #$00                ; clear the change tally for the normalise sweep
3447: A2 02           LDX     #$02                ; start at the last of the three column progress cells

loc_3449:
3449: B5 C5           LDA     $C5,X               ; {hard.workRam+C5} read this column's progress cell
344B: F0 09           BEQ     $3456               ; {code.loc_3456} empty -- skip it
344D: C9 10           CMP     #$10                ; is it 0x10 or more?
344F: 90 05           BCC     $3456               ; {code.loc_3456} below 0x10 -- skip it
3451: 69 EF           ADC     #$EF                ; subtract 0x10 to fold the progress cell into the 0x10 grid
3453: C8              INY                         ; count that this cell changed
3454: 95 C5           STA     $C5,X               ; {hard.workRam+C5} store the folded progress value back

loc_3456:
3456: CA              DEX                         ; step to the previous progress cell
3457: 10 F0           BPL     $3449               ; {code.loc_3449} loop over all three columns
3459: 98              TYA                         ; pull the change tally into A
345A: D0 10           BNE     $346C               ; {code.loc_346c} pass 1 changed something -- done for this frame
345C: A2 02           LDX     #$02                ; nothing changed -- run pass 2 from the last progress cell

loc_345e:
345E: B5 C5           LDA     $C5,X               ; {hard.workRam+C5} read this column's progress cell
3460: F0 07           BEQ     $3469               ; {code.loc_3469} empty -- skip it
3462: 18              CLC                         ; prep for the subtract
3463: 69 EF           ADC     #$EF                ; subtract 0x11 from the nonzero progress cell
3465: 95 C5           STA     $C5,X               ; {hard.workRam+C5} store it back
3467: 30 03           BMI     $346C               ; {code.loc_346c} result went negative -- stop the sweep here

loc_3469:
3469: CA              DEX                         ; step to the previous progress cell
346A: 10 F2           BPL     $345E               ; {code.loc_345e} loop over the progress cells

loc_346c:
346C: 60              RTS                         ; done -- return

; ---- $346D-$37D4: data ----
346D: C5 34 D0 34 DC 34 E7 34 F3 34 05 35 1A 35 2F 35
347D: 43 35 54 35 68 35 7C 35 8F 35 A1 35 B6 35 CB 35
348D: DF 35 EC 35 F9 35 0A 36 1D 36 34 36 54 36 6C 36
349D: 83 36 93 36 A2 36 B3 36 C2 36 D1 36 E6 36 F9 36
34AD: 04 37 13 37 2C 37 3F 37 4F 37 5B 37 67 37 73 37
34BD: 80 37 94 37 B0 37 C2 37 6E 05 51 06 50 4C 41 59
34CD: 45 52 A0 6E 05 51 06 53 50 49 45 4C 45 52 A0 6E
34DD: 05 51 06 4A 4F 55 45 55 52 A0 6E 05 51 06 4A 55
34ED: 47 41 44 4F 52 A0 13 05 AC 06 31 20 43 4F 49 4E
34FD: 20 32 20 50 4C 41 59 D3 F3 04 CC 06 31 20 4D 55
350D: 45 4E 5A 45 20 32 20 53 50 49 45 4C C5 F3 04 CC
351D: 06 31 20 50 49 45 43 45 20 32 20 4A 4F 55 45 55
352D: 52 D3 F3 04 CC 06 31 20 46 49 43 48 41 20 32 20
353D: 4A 55 45 47 4F D3 13 05 AC 06 31 20 43 4F 49 4E
354D: 20 31 20 50 4C 41 D9 F3 04 CC 06 31 20 4D 55 45
355D: 4E 5A 45 20 31 20 53 50 49 45 CC F3 04 CC 06 31
356D: 20 50 49 45 43 45 20 31 20 4A 4F 55 45 55 D2 F3
357D: 04 CC 06 31 20 46 49 43 48 41 20 31 20 4A 55 45
358D: 47 CF 13 05 AC 06 32 20 43 4F 49 4E 53 20 31 20
359D: 50 4C 41 D9 F3 04 CC 06 32 20 4D 55 45 4E 5A 45
35AD: 4E 20 31 20 53 50 49 45 CC F3 04 CC 06 32 20 50
35BD: 49 45 43 45 53 20 31 20 4A 4F 55 45 55 D2 F3 04
35CD: CC 06 32 20 46 49 43 48 41 53 20 31 20 4A 55 45
35DD: 47 CF 6F 05 50 06 47 41 4D 45 20 4F 56 45 D2 6F
35ED: 05 50 06 53 50 49 45 4C 45 4E 44 C5 0F 05 B0 06
35FD: 46 49 4E 20 44 45 20 50 41 52 54 49 C5 EF 04 D0
360D: 06 4A 55 45 47 4F 20 54 45 52 4D 49 4E 41 44 CF
361D: AB 04 14 07 45 4E 54 45 52 20 59 4F 55 52 20 49
362D: 4E 49 54 49 41 4C D3 2B 04 94 07 47 45 42 45 4E
363D: 20 53 49 45 20 49 48 52 45 20 49 4E 49 54 49 41
364D: 4C 45 4E 20 45 49 CE 8B 04 34 07 45 4E 54 52 45
365D: 5A 20 56 4F 53 20 49 4E 49 54 49 41 4C 45 D3 8B
366D: 04 34 07 45 4E 54 52 45 20 53 55 53 20 49 4E 49
367D: 43 49 41 4C 45 D3 F1 04 CE 06 42 4F 4E 55 53 20
368D: 45 56 45 52 59 A0 F1 04 CE 06 42 4F 4E 55 53 20
369D: 4A 45 44 45 A0 D1 04 EE 06 42 4F 4E 55 53 20 43
36AD: 48 41 51 55 45 A0 F1 04 CE 06 45 58 54 52 41 20
36BD: 43 41 44 41 A0 5D 05 62 06 48 49 47 48 20 53 43
36CD: 4F 52 45 D3 DD 04 E2 06 48 4F 45 43 48 53 54 45
36DD: 52 47 45 42 4E 49 53 53 C5 1D 05 A2 06 4D 45 49
36ED: 4C 4C 45 55 52 53 20 53 43 4F 52 C5 9D 05 22 06
36FD: 52 45 43 4F 52 44 D3 2C 05 93 06 47 52 45 41 54
370D: 20 53 43 4F 52 C5 8C 04 33 07 47 52 4F 53 53 41
371D: 52 54 49 47 45 53 20 45 52 47 45 42 4E 49 D3 EC
372D: 04 D3 06 53 50 4C 45 4E 44 49 44 45 20 53 43 4F
373D: 52 C5 0C 05 B3 06 47 52 41 4E 20 50 55 4E 54 41
374D: 4A C5 52 05 6D 06 43 52 45 44 49 54 53 A0 52 05
375D: 6D 06 4B 52 45 44 49 54 45 A0 52 05 6D 06 43 52
376D: 45 44 49 54 53 A0 52 05 6D 06 43 52 45 44 49 54
377D: 4F 53 A0 F0 04 CF 06 32 20 43 52 45 44 49 54 20
378D: 4D 49 4E 49 4D 55 CD 30 04 8F 07 47 45 4C 44 45
379D: 49 4E 57 55 52 46 20 46 55 52 20 32 20 53 50 49
37AD: 45 4C C5 F0 04 CF 06 32 20 4A 55 45 58 20 4D 49
37BD: 4E 49 4D 55 CD F0 04 CF 06 32 20 4A 55 45 47 41
37CD: 53 20 4D 49 4E 49 4D B0

writePointerTableRow:
37D5: 0A              ASL     A                   ; double the row selector
37D6: 66 8C           ROR     $8C                 ; {hard.workRam+8C} rotate the carry into the sign latch (marks whether the row should be blanked)
37D8: A8              TAY                         ; hold the selector as an index
37D9: 0A              ASL     A                   ; double it again
37DA: 85 8B           STA     $8B                 ; {hard.workRam+8B} stash the doubled selector
37DC: A5 FD           LDA     $FD                 ; {hard.workRam+FD} read the config/mode byte
37DE: 29 03           AND     #$03                ; keep its low two bits (the ROM table variant)
37E0: 05 8B           ORA     $8B                 ; {hard.workRam+8B} fold the variant into the selector
37E2: 0A              ASL     A                   ; double for a word-sized table stride
37E3: AA              TAX                         ; hold as the descriptor-table index
37E4: BD 6D 34        LDA     $346D,X             ; {hard.rom+146D} read the row descriptor's pointer low byte from the ROM table
37E7: 85 93           STA     $93                 ; {hard.workRam+93} store the descriptor pointer low byte
37E9: BD 6E 34        LDA     $346E,X             ; {hard.rom+146E} read the descriptor's pointer high byte
37EC: 85 94           STA     $94                 ; {hard.workRam+94} store the descriptor pointer high byte
37EE: A0 00           LDY     #$00                ; start at descriptor offset 0
37F0: A6 EF           LDX     $EF                 ; {hard.workRam+EF} read the direction selector
37F2: F0 02           BEQ     $37F6               ; {code.loc_37f6} selector clear -- use the first destination pair
37F4: A0 02           LDY     #$02                ; selector set -- use the second destination pair (offset 2)

loc_37f6:
37F6: B1 93           LDA     ($93),Y             ; {hard.workRam+93} read the screen destination low byte from the descriptor
37F8: 85 91           STA     $91                 ; {hard.workRam+91} seat the draw cursor low byte
37FA: C8              INY                         ; step to the next descriptor byte
37FB: B1 93           LDA     ($93),Y             ; {hard.workRam+93} read the screen destination high byte
37FD: 85 92           STA     $92                 ; {hard.workRam+92} seat the draw cursor high byte
37FF: A0 04           LDY     #$04                ; skip to offset 4 -- the start of the row's text bytes

rewritePointerTableRowFromStart:
3801: 84 8B           STY     $8B                 ; {hard.workRam+8B} remember the current text-byte index

loc_3803:
3803: A4 8B           LDY     $8B                 ; {hard.workRam+8B} load the text-byte index
3805: B1 93           LDA     ($93),Y             ; {hard.workRam+93} read a character code from the descriptor row
3807: 29 3F           AND     #$3F                ; mask to the 6-bit glyph code
3809: C9 20           CMP     #$20                ; is it a space?
380B: F0 04           BEQ     $3811               ; {code.loc_3811} space -- blank this cell
380D: A6 8C           LDX     $8C                 ; {hard.workRam+8C} read the sign latch
380F: 10 02           BPL     $3813               ; {code.loc_3813} positive -- keep the character

loc_3811:
3811: A9 00           LDA     #$00                ; blank glyph

loc_3813:
3813: C9 30           CMP     #$30                ; glyph code 0x30 or above?
3815: 90 02           BCC     $3819               ; {code.loc_3819} below -- keep it
3817: 29 2F           AND     #$2F                ; fold the high glyph code down into range

loc_3819:
3819: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} write the glyph and step the draw cursor along the row
381C: A4 8B           LDY     $8B                 ; {hard.workRam+8B} reload the text-byte index
381E: E6 8B           INC     $8B                 ; {hard.workRam+8B} advance to the next character
3820: B1 93           LDA     ($93),Y             ; {hard.workRam+93} re-read the original descriptor byte
3822: 10 DF           BPL     $3803               ; {code.loc_3803} high bit clear -- more of the row to write, loop
3824: 60              RTS                         ; high bit marks end of the row -- return

redrawPointerTableRowUnblanked:
3825: A0 00           LDY     #$00                ; start at offset 0
3827: 84 8C           STY     $8C                 ; {hard.workRam+8C} clear the sign latch so no cell gets blanked
3829: F0 D6           BEQ     $3801               ; {code.rewritePointerTableRowFromStart} jump into the row writer to redraw the row unblanked

foldSignedMagnitude:
382B: 10 05           BPL     $3832               ; {code.loc_3832} already positive -- nothing to negate, return

negateA:
382D: 49 FF           EOR     #$FF                ; one's-complement the value
382F: 18              CLC                         ; prep for the add
3830: 69 01           ADC     #$01                ; add one -- the two's-complement negation

loc_3832:
3832: 60              RTS                         ; return the (possibly negated) value

plotZpTableByteAtCursor:
3833: B9 1A 00        LDA     $001A,Y             ; {hard.workRam+1A} read a byte from the zero-page table indexed by Y

writeMaskedByteAndAdvancePointer:
3836: A8              TAY                         ; test the glyph value
3837: F0 02           BEQ     $383B               ; {code.loc_383b} zero -- write it straight through
3839: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold the glyph with the direction selector (flips its attribute)

loc_383b:
383B: A0 00           LDY     #$00                ; write into cell offset 0
383D: 91 91           STA     ($91),Y             ; {hard.workRam+91} poke the glyph into the cell the draw cursor points at
383F: A9 20           LDA     #$20                ; stride of 0x20 -- one step along the row/column
3841: 45 EF           EOR     $EF                 ; {hard.workRam+EF} fold the stride with the direction selector
3843: 18              CLC                         ; prep for the add
3844: 65 91           ADC     $91                 ; {hard.workRam+91} add the stride to the draw cursor low byte
3846: 85 91           STA     $91                 ; {hard.workRam+91} store the draw cursor low byte
3848: A5 F3           LDA     $F3                 ; {hard.workRam+F3} read the high stride
384A: 65 92           ADC     $92                 ; {hard.workRam+92} carry it into the draw cursor high byte
384C: 85 92           STA     $92                 ; {hard.workRam+92} store the draw cursor high byte
384E: 60              RTS                         ; return

plotByteAsTwoDigits:
384F: 48              PHA                         ; save the byte to plot
3850: 08              PHP                         ; save the carry (leading-zero suppression flag)
3851: 4A              LSR     A                   ; shift the high nibble down
3852: 4A              LSR     A                   ; shift again
3853: 4A              LSR     A                   ; shift again
3854: 4A              LSR     A                   ; four shifts leave the tens digit
3855: 28              PLP                         ; restore the suppression flag
3856: 20 5C 38        JSR     $385C               ; {code.plotNormalizedCharCode} plot the tens digit
3859: 68              PLA                         ; restore the whole byte
385A: 29 0F           AND     #$0F                ; keep the units nibble

plotNormalizedCharCode:
385C: 90 04           BCC     $3862               ; {code.loc_3862} carry clear -- plot this digit
385E: 29 0F           AND     #$0F                ; keep the low nibble
3860: F0 03           BEQ     $3865               ; {code.loc_3865} leading zero -- suppress it (skip the cell)

loc_3862:
3862: 18              CLC                         ; prep the digit
3863: 09 20           ORA     #$20                ; map the digit value to its glyph code

loc_3865:
3865: 08              PHP                         ; save the carry
3866: C9 2A           CMP     #$2A                ; glyph code 0x2a or above?
3868: 90 02           BCC     $386C               ; {code.loc_386c} below -- keep it
386A: E9 29           SBC     #$29                ; fold the high code down into range

loc_386c:
386C: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} write the digit glyph and step the draw cursor
386F: 28              PLP                         ; restore the carry
3870: 60              RTS                         ; return

serviceFrameIrq:
3871: 48              PHA                         ; save A across the frame interrupt
3872: 8A              TXA                         ; move X into A
3873: 48              PHA                         ; save X
3874: 98              TYA                         ; move Y into A
3875: 48              PHA                         ; save Y
3876: D8              CLD                         ; clear decimal mode for the ordinary bookkeeping
3877: A5 D2           LDA     $D2                 ; {hard.workRam+D2} read the shared segment reload timer
3879: F0 0A           BEQ     $3885               ; {code.loc_3885} timer idle -- skip the tone poke
387B: A9 10           LDA     #$10                ; tone value 0x10
387D: 8D 02 10        STA     $1002               ; {hard.pokey+2} write it to the POKEY channel-2 frequency register
3880: A9 AF           LDA     #$AF                ; control value 0xaf
3882: 8D 03 10        STA     $1003               ; {hard.pokey+3} write it to the POKEY channel-2 control register (sound the marching tone)

loc_3885:
3885: 2C 00 0C        BIT     $0C00               ; {hard.in0 / trackballX} test the vblank/service input port
3888: 70 03           BVS     $388D               ; {code.loc_388d} vblank edge present -- service this frame
388A: 4C 6D 39        JMP     $396D               ; {code.accumulateTrackballAndReturnFromIrq} no vblank yet -- jump to the trackball accumulate and return from interrupt

loc_388d:
388D: E6 8A           INC     $8A                 ; {hard.workRam+8A} bump the frame heartbeat latch the main loop waits on
388F: E6 00           INC     $00                 ; {hard.workRam} step the low frame counter
3891: D0 11           BNE     $38A4               ; {code.loc_38a4} no carry -- skip the high byte
3893: E6 01           INC     $01                 ; {hard.workRam+1} carry into the high frame counter
3895: F8              SED                         ; set decimal mode for the BCD add
3896: A5 FB           LDA     $FB                 ; {hard.workRam+FB} read the BCD time counter low byte
3898: 18              CLC                         ; prep for the add
3899: 69 01           ADC     #$01                ; add one in BCD
389B: 85 FB           STA     $FB                 ; {hard.workRam+FB} store the time counter low byte
389D: A5 FC           LDA     $FC                 ; {hard.workRam+FC} read the time counter high byte
389F: 69 00           ADC     #$00                ; carry into it
38A1: 85 FC           STA     $FC                 ; {hard.workRam+FC} store the time counter high byte
38A3: D8              CLD                         ; back to binary mode

loc_38a4:
38A4: A5 8A           LDA     $8A                 ; {hard.workRam+8A} read the frame heartbeat latch
38A6: C9 08           CMP     #$08                ; compare against 8

loc_38a8:
38A8: B0 FE           BCS     $38A8               ; {code.loc_38a8} spin here while the latch is 8 or more -- wait for the main loop to catch up
38AA: A5 C8           LDA     $C8                 ; {hard.workRam+C8} read the wrap counter
38AC: C9 25           CMP     #$25                ; compare against 0x25

loc_38ae:
38AE: B0 FE           BCS     $38AE               ; {code.loc_38ae} spin here while the wrap counter is 0x25 or more
38B0: C9 13           CMP     #$13                ; is the wrap counter 0x13 or more?
38B2: 90 04           BCC     $38B8               ; {code.loc_38b8} below -- skip the clamp
38B4: A9 12           LDA     #$12                ; clamp value 0x12
38B6: 85 C8           STA     $C8                 ; {hard.workRam+C8} store the clamped wrap counter

loc_38b8:
38B8: A6 88           LDX     $88                 ; {hard.workRam+88} read the current slot index
38BA: AD 03 0C        LDA     $0C03               ; {hard.in3} read input port IN3
38BD: E0 02           CPX     #$02                ; is this slot 2?
38BF: D0 04           BNE     $38C5               ; {code.loc_38c5} no -- take the trackball reading as-is
38C1: 0A              ASL     A                   ; shift the low nibble up
38C2: 0A              ASL     A                   ; shift again
38C3: 0A              ASL     A                   ; shift again
38C4: 0A              ASL     A                   ; four shifts align the alternate trackball axis into the high nibble

loc_38c5:
38C5: AC B8 01        LDY     $01B8               ; {hard.workRam+1B8} read the axis-0 trackball step state
38C8: 20 EA 39        JSR     $39EA               ; {code.stepAxisBySelectorBits} step the trackball axis from its selector bits
38CB: 8C B8 01        STY     $01B8               ; {hard.workRam+1B8} store the updated axis-0 step state
38CE: 48              PHA                         ; save the axis-0 delta
38CF: 98              TYA                         ; move the step into A
38D0: 18              CLC                         ; prep for the add
38D1: 65 B9           ADC     $B9                 ; {hard.workRam+B9} accumulate the axis-0 trackball delta
38D3: 85 B9           STA     $B9                 ; {hard.workRam+B9} store the axis-0 accumulator
38D5: 68              PLA                         ; restore the delta
38D6: AC B9 01        LDY     $01B9               ; {hard.workRam+1B9} read the axis-1 trackball step state
38D9: 20 EA 39        JSR     $39EA               ; {code.stepAxisBySelectorBits} step the trackball axis from its selector bits
38DC: 8C B9 01        STY     $01B9               ; {hard.workRam+1B9} store the updated axis-1 step state
38DF: 98              TYA                         ; move the step into A
38E0: 20 2D 38        JSR     $382D               ; {code.negateA} negate the axis-1 delta (its axis reads reversed)
38E3: 18              CLC                         ; prep for the add
38E4: 65 BB           ADC     $BB                 ; {hard.workRam+BB} accumulate the axis-1 trackball delta
38E6: 85 BB           STA     $BB                 ; {hard.workRam+BB} store the axis-1 accumulator
38E8: B5 C2           LDA     $C2,X               ; {hard.workRam+C2} read this slot's object-active flag
38EA: 30 08           BMI     $38F4               ; {code.loc_38f4} negative -- the slot is free/retired, branch away
38EC: C9 40           CMP     #$40                ; is the flag 0x40 or more?
38EE: 90 15           BCC     $3905               ; {code.loc_3905} below -- branch on
38F0: 29 3F           AND     #$3F                ; mask off the high control bits
38F2: 10 0B           BPL     $38FF               ; {code.loc_38ff} positive now -- branch on

loc_38f4:
38F4: 29 3F           AND     #$3F                ; mask the object's angle cell down to its low six bits
38F6: 18              CLC                         ; clear carry before the angle add
38F7: 69 03           ADC     #$03                ; advance the animating angle by 3
38F9: C9 2A           CMP     #$2A                ; compare the angle against 42, its wrap point
38FB: 90 02           BCC     $38FF               ; {code.loc_38ff} still under 42 -- keep the angle
38FD: A9 00           LDA     #$00                ; reached 42 -- wrap the angle back to zero

loc_38ff:
38FF: 95 C2           STA     $C2,X               ; {hard.workRam+C2} store the normalized angle back into the object's angle cell
3901: AA              TAX                         ; use the angle as the palette-record index
3902: 20 56 26        JSR     $2656               ; {code.loadPaletteRecordPair} fan a colour record out to refresh the object's palette pair

loc_3905:
3905: A2 0F           LDX     #$0F                ; start the shadow-build sweep at the top object slot

buildObjectShadowEntry:
3907: B5 64           LDA     $64,X               ; {hard.workRam+64} read this object's vertical field
3909: 9D E0 07        STA     $07E0,X             ; {hard.spriteRam+20} copy it into the object's vertical sprite-shadow row
390C: B5 54           LDA     $54,X               ; {hard.workRam+54} read the object's horizontal coordinate source
390E: A0 00           LDY     #$00                ; default the heading-sign carry to zero
3910: E0 0D           CPX     #$0D                ; is this object slot 13?
3912: F0 07           BEQ     $391B               ; {code.loc_391b} slot 13 skips the sign fold
3914: B4 44           LDY     $44,X               ; {hard.workRam+44} read the object's heading field
3916: 10 03           BPL     $391B               ; {code.loc_391b} heading positive -- no shadow adjustment
3918: 18              CLC                         ; clear carry before the nudge
3919: 69 01           ADC     #$01                ; heading negative -- nudge the horizontal shadow up by one

loc_391b:
391B: 9D D0 07        STA     $07D0,X             ; {hard.spriteRam+10} store the object's horizontal sprite-shadow coordinate
391E: 98              TYA                         ; bring the heading into A
391F: 29 80           AND     #$80                ; keep just its sign bit
3921: 85 99           STA     $99                 ; {hard.workRam+99} latch that sign for the shadow-code fold
3923: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read input port IN0
3926: 29 20           AND     #$20                ; isolate the service/self-test bit
3928: D0 05           BNE     $392F               ; {code.loc_392f} switch idle (normal play) -- go build the derived picture code
392A: B5 34           LDA     $34,X               ; {hard.workRam+34} self-test held -- take the tile/attribute source as-is
392C: 4C 56 39        JMP     $3956               ; {code.storeSpriteShadowEntry} hand the code to the shadow-store tail

loc_392f:
392F: B5 34           LDA     $34,X               ; {hard.workRam+34} normal play -- read the tile/attribute source to build the derived picture code
3931: E0 0C           CPX     #$0C                ; is this object slot below 12?
3933: B0 1F           BCS     $3954               ; {code.loc_3954} high slots keep the source code unchanged
3935: 29 3F           AND     #$3F                ; low slots keep the low six bits
3937: C9 30           CMP     #$30                ; already in the solid-glyph band?
3939: B0 19           BCS     $3954               ; {code.loc_3954} if so, keep it as the code
393B: 29 0F           AND     #$0F                ; otherwise keep the low nibble
393D: 85 98           STA     $98                 ; {hard.workRam+98} stash that low nibble
393F: B5 64           LDA     $64,X               ; {hard.workRam+64} read the vertical field again
3941: 29 07           AND     #$07                ; take its low three bits
3943: F0 0D           BEQ     $3952               ; {code.loc_3952} low three bits zero -- combine with a zero offset (just the stashed nibble)
3945: A8              TAY                         ; hold the three-bit value
3946: A9 08           LDA     #$08                ; default offset of 8
3948: C0 06           CPY     #$06                ; value 6 or more?
394A: B0 06           BCS     $3952               ; {code.loc_3952} then keep offset 8
394C: C0 03           CPY     #$03                ; value below 3?
394E: 90 02           BCC     $3952               ; {code.loc_3952} then keep offset 8
3950: A9 0C           LDA     #$0C                ; values 3 through 5 take offset 0x0c

loc_3952:
3952: 45 98           EOR     $98                 ; {hard.workRam+98} combine the offset with the stashed low nibble

loc_3954:
3954: 45 99           EOR     $99                 ; {hard.workRam+99} fold in the latched heading sign

storeSpriteShadowEntry:
3956: 9D C0 07        STA     $07C0,X             ; {hard.spriteRam} store the object's sprite-shadow picture code
3959: B5 34           LDA     $34,X               ; {hard.workRam+34} read the tile/attribute source for the attribute byte
395B: 29 40           AND     #$40                ; isolate bit 6 of the source
395D: F0 06           BEQ     $3965               ; {code.loc_3965} bit clear -- no attribute floor
395F: E0 0C           CPX     #$0C                ; is this object slot below 12?
3961: B0 02           BCS     $3965               ; {code.loc_3965} high slots skip the floor
3963: A9 0C           LDA     #$0C                ; low slots floor the attribute to 0x0c

loc_3965:
3965: 09 39           ORA     #$39                ; OR in the fixed attribute base
3967: 9D F0 07        STA     $07F0,X             ; {hard.spriteRam+30} store the object's sprite-shadow attribute
396A: CA              DEX                         ; step down to the next object slot
396B: 10 9A           BPL     $3907               ; {code.buildObjectShadowEntry} loop until every object's shadow is rebuilt

accumulateTrackballAndReturnFromIrq:
396D: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read input port IN0
3970: 29 20           AND     #$20                ; isolate the self-test bit
3972: D0 1F           BNE     $3993               ; {code.loc_3993} switch idle (normal play) -- run the segment-service and ROM-checksum branch
3974: A5 D5           LDA     $D5                 ; {hard.workRam+D5} self-test held -- read the diagnostic ramp counter
3976: 30 3B           BMI     $39B3               ; {code.loc_39b3} high bit set -- skip the colour ramp
3978: E6 D5           INC     $D5                 ; {hard.workRam+D5} climb the ramp counter
397A: 2C 00 0C        BIT     $0C00               ; {hard.in0 / trackballX} test IN0's vblank bit
397D: 50 04           BVC     $3983               ; {code.loc_3983} not the 32V edge -- leave the counter running
397F: A9 00           LDA     #$00                ; load zero
3981: 85 D5           STA     $D5                 ; {hard.workRam+D5} on the 32V edge reset the ramp counter

loc_3983:
3983: A5 D5           LDA     $D5                 ; {hard.workRam+D5} read the ramp counter
3985: 0A              ASL     A                   ; shift it up one place for the colour ramp
3986: 0A              ASL     A                   ; shift it up a second place
3987: A2 03           LDX     #$03                ; four diagnostic palette cells to write

loc_3989:
3989: 9D 04 14        STA     $1404,X             ; {hard.paletteRam+4} write the ramp value into a diagnostic palette cell
398C: 69 01           ADC     #$01                ; step the value up for the next palette cell
398E: CA              DEX                         ; step down the palette-cell index
398F: 10 F8           BPL     $3989               ; {code.loc_3989} loop across the four palette cells
3991: 30 20           BMI     $39B3               ; {code.loc_39b3} join the trackball integration

loc_3993:
3993: 20 5E 33        JSR     $335E               ; {code.advanceAllSegmentColumns} normal play -- run the segment-column service pass
3996: A2 02           LDX     #$02                ; three counter cells to mirror out

loc_3998:
3998: B5 C5           LDA     $C5,X               ; {hard.workRam+C5} read a segment-column progress counter
399A: 9D 00 1C        STA     $1C00,X             ; {hard.outLatch} mirror it to the output latch
399D: CA              DEX                         ; step down the mirror index
399E: 10 F8           BPL     $3998               ; {code.loc_3998} loop across the three counters
39A0: A2 0A           LDX     #$0A                ; eleven ROM bytes to fold for the checksum
39A2: A9 F4           LDA     #$F4                ; seed the checksum accumulator

loc_39a4:
39A4: 5D 03 20        EOR     $2003,X             ; {hard.rom+3} fold one byte of the ROM check table into the sum
39A7: CA              DEX                         ; step down the fold index
39A8: 10 FA           BPL     $39A4               ; {code.loc_39a4} loop across the ROM check table
39AA: AA              TAX                         ; test the folded checksum
39AB: F0 06           BEQ     $39B3               ; {code.loc_39b3} a good ROM image sums to zero
39AD: BA              TSX                         ; bad checksum -- grab the stack pointer
39AE: A9 03           LDA     #$03                ; fault marker value
39B0: 9D 04 01        STA     $0104,X             ; {hard.workRam+104} stash the fault marker in dead stack scratch

loc_39b3:
39B3: A2 02           LDX     #$02                ; start the trackball integration at axis 2

loc_39b5:
39B5: BD 00 0C        LDA     $0C00,X             ; {hard.in0 / trackballX} read this axis's raw trackball counter
39B8: A8              TAY                         ; keep the raw count to become the new sample
39B9: 38              SEC                         ; set carry for the subtract
39BA: F5 BD           SBC     $BD,X               ; {hard.workRam+BD} subtract the previous sample to get the delta
39BC: 94 BD           STY     $BD,X               ; {hard.workRam+BD} refresh the sample cell with the raw count
39BE: 29 0F           AND     #$0F                ; keep the low-nibble delta
39C0: C9 08           CMP     #$08                ; is the delta in the negative half?
39C2: 90 02           BCC     $39C6               ; {code.loc_39c6} positive delta needs no sign-extend
39C4: 09 F0           ORA     #$F0                ; sign-extend the negative nibble delta

loc_39c6:
39C6: A8              TAY                         ; hold the signed delta
39C7: F0 14           BEQ     $39DD               ; {code.loc_39dd} zero delta -- nothing to integrate this axis
39C9: 55 BA           EOR     $BA,X               ; {hard.workRam+BA} compare its sign against the last committed delta
39CB: 10 08           BPL     $39D5               ; {code.loc_39d5} same direction -- accept the delta
39CD: 98              TYA                         ; reversal -- bring the delta back into A
39CE: 5D 00 0C        EOR     $0C00,X             ; {hard.in0 / trackballX} check it against the raw counter's own sign
39D1: 10 02           BPL     $39D5               ; {code.loc_39d5} consistent reversal -- accept it
39D3: B4 BA           LDY     $BA,X               ; {hard.workRam+BA} jittery reversal -- reuse the last committed delta

loc_39d5:
39D5: 98              TYA                         ; move the chosen delta into A
39D6: 95 BA           STA     $BA,X               ; {hard.workRam+BA} commit it as this axis's last delta
39D8: 18              CLC                         ; clear carry before the accumulate
39D9: 75 B9           ADC     $B9,X               ; {hard.workRam+B9} fold the delta into this axis's accumulator
39DB: 95 B9           STA     $B9,X               ; {hard.workRam+B9} store the updated accumulator

loc_39dd:
39DD: CA              DEX                         ; step the index down one
39DE: CA              DEX                         ; step down again to reach the next axis
39DF: 10 D4           BPL     $39B5               ; {code.loc_39b5} loop over both trackball axes
39E1: 8D 00 18        STA     $1800               ; {hard.irqAck} write the interrupt-acknowledge port to clear the frame IRQ
39E4: 68              PLA                         ; pull the saved Y off the stack
39E5: A8              TAY                         ; restore Y
39E6: 68              PLA                         ; pull the saved X off the stack
39E7: AA              TAX                         ; restore X
39E8: 68              PLA                         ; restore A from the stack
39E9: 40              RTI                         ; return from the frame interrupt

stepAxisBySelectorBits:
39EA: 0A              ASL     A                   ; shift the selector's top bit into carry
39EB: 90 06           BCC     $39F3               ; {code.loc_39f3} a 0x selector steps the value down
39ED: 0A              ASL     A                   ; shift the next selector bit
39EE: 90 0E           BCC     $39FE               ; {code.loc_39fe} a 10 selector steps the value up
39F0: A0 00           LDY     #$00                ; an 11 selector zeroes the step value
39F2: 60              RTS                         ; return with the zeroed value

loc_39f3:
39F3: C0 FA           CPY     #$FA                ; is the step value already at the low clamp?
39F5: F0 05           BEQ     $39FC               ; {code.loc_39fc} at the floor -- hold it
39F7: B0 02           BCS     $39FB               ; {code.loc_39fb} above the window -- step it down
39F9: A0 00           LDY     #$00                ; below the window -- snap into range

loc_39fb:
39FB: 88              DEY                         ; step the value down one

loc_39fc:
39FC: 0A              ASL     A                   ; shift the selector byte on for the next axis
39FD: 60              RTS                         ; return the stepped value

loc_39fe:
39FE: C0 06           CPY     #$06                ; is the step value already at the high clamp?
3A00: F0 05           BEQ     $3A07               ; {code.loc_3a07} at the ceiling -- hold it
3A02: 90 02           BCC     $3A06               ; {code.loc_3a06} below the window -- step it up
3A04: A0 00           LDY     #$00                ; above the window -- snap into range

loc_3a06:
3A06: C8              INY                         ; step the value up one

loc_3a07:
3A07: 60              RTS                         ; return the stepped value

foldHighScoreChecksum:
3A08: A0 3C           LDY     #$3C                ; index the 61 high-score table bytes from the top
3A0A: A9 FF           LDA     #$FF                ; seed the checksum accumulator

loc_3a0c:
3A0C: 59 78 01        EOR     $0178,Y             ; {hard.workRam+178} fold one high-score table byte into the checksum
3A0F: 88              DEY                         ; step down the table index
3A10: 10 FA           BPL     $3A0C               ; {code.loc_3a0c} loop across the whole high-score table
3A12: AC B5 01        LDY     $01B5               ; {hard.workRam+1B5} read the previously stored checksum
3A15: 8D B5 01        STA     $01B5               ; {hard.workRam+1B5} publish the freshly folded checksum
3A18: 98              TYA                         ; bring the old checksum into A
3A19: 4D B5 01        EOR     $01B5               ; {hard.workRam+1B5} form old-XOR-new -- the change delta
3A1C: 60              RTS                         ; return the checksum delta

validateOrResetHighScores:
3A1D: A2 2F           LDX     #$2F                ; index the 48-byte ROM high-score template

loc_3a1f:
3A1F: BD 69 3A        LDA     $3A69,X             ; {hard.rom+1A69} read a template byte
3A22: 95 02           STA     $02,X               ; {hard.workRam+2} stage it into the zeropage copy
3A24: CA              DEX                         ; step down the template index
3A25: 10 F8           BPL     $3A1F               ; {code.loc_3a1f} loop across the whole template
3A27: 20 08 3A        JSR     $3A08               ; {code.foldHighScoreChecksum} fold the table checksum to test integrity
3A2A: D0 2B           BNE     $3A57               ; {code.loc_3a57} nonzero delta -- table corrupt, go reset it
3A2C: A5 FD           LDA     $FD                 ; {hard.workRam+FD} read the option/config byte
3A2E: 29 7C           AND     #$7C                ; keep the relevant DIP bits
3A30: CD 8A 01        CMP     $018A               ; {hard.workRam+18A} compare against the stored config snapshot
3A33: 8D 8A 01        STA     $018A               ; {hard.workRam+18A} overwrite the snapshot with the current config
3A36: D0 1E           BNE     $3A56               ; {code.loc_3a56} config changed -- keep the scores but bail
3A38: AD 7A 01        LDA     $017A               ; {hard.workRam+17A} read the leading high-score entry
3A3B: F0 1A           BEQ     $3A57               ; {code.loc_3a57} empty entry -- reset the table
3A3D: A2 08           LDX     #$08                ; nine bytes of the top entry to validate

loc_3a3f:
3A3F: BD 78 01        LDA     $0178,X             ; {hard.workRam+178} read a top-entry byte
3A42: 95 02           STA     $02,X               ; {hard.workRam+2} stage it into the zeropage copy
3A44: C9 9A           CMP     #$9A                ; is the byte out of BCD range?
3A46: B0 0F           BCS     $3A57               ; {code.loc_3a57} too high -- garbage, reset the table
3A48: 29 0F           AND     #$0F                ; isolate the low nibble
3A4A: C9 0A           CMP     #$0A                ; is the low nibble an illegal BCD digit?
3A4C: B0 09           BCS     $3A57               ; {code.loc_3a57} illegal -- reset the table
3A4E: BD 81 01        LDA     $0181,X             ; {hard.workRam+181} read the paired secondary entry byte
3A51: 95 1A           STA     $1A,X               ; {hard.workRam+1A} promote it into the zeropage working copy
3A53: CA              DEX                         ; step down the entry index
3A54: 10 E9           BPL     $3A3F               ; {code.loc_3a3f} loop across the top entry

loc_3a56:
3A56: 60              RTS                         ; return -- table validated

loc_3a57:
3A57: A9 00           LDA     #$00                ; reset path -- value to clear the table with
3A59: A2 3E           LDX     #$3E                ; index the 63 table bytes to wipe

loc_3a5b:
3A5B: 9D 78 01        STA     $0178,X             ; {hard.workRam+178} zero one high-score table byte
3A5E: CA              DEX                         ; step down the wipe index
3A5F: 10 FA           BPL     $3A5B               ; {code.loc_3a5b} loop until the whole table is blank
3A61: A5 FD           LDA     $FD                 ; {hard.workRam+FD} read the option/config byte
3A63: 29 7C           AND     #$7C                ; keep the relevant DIP bits
3A65: 8D 8A 01        STA     $018A               ; {hard.workRam+18A} stamp the config snapshot on the blank table
3A68: 60              RTS                         ; return -- table reset

; ---- $3A69-$3A98: data ----
3A69: 43 65 01 32 54 01 20 43 01 10 32 01 10 30 01 05
3A79: 28 01 01 22 01 02 21 01 05 0A 04 04 06 14 03 01
3A89: 04 04 03 02 05 04 00 04 05 17 04 06 17 07 0A 12

loadHighScoreTableFromEarom:
3A99: A2 3F           LDX     #$3F                ; index the 64 NVRAM cells from the top

loc_3a9b:
3A9B: 20 A7 3A        JSR     $3AA7               ; {code.readEaromCell} read one cell out of the EAROM
3A9E: 9D 78 01        STA     $0178,X             ; {hard.workRam+178} store it into the RAM high-score mirror
3AA1: CA              DEX                         ; step down the cell index
3AA2: 10 F7           BPL     $3A9B               ; {code.loc_3a9b} loop across the whole table
3AA4: 86 F9           STX     $F9                 ; {hard.workRam+F9} park the 0xff sentinel into the writeback cursor
3AA6: 60              RTS                         ; return -- mirror loaded fresh from NVRAM

readEaromCell:
3AA7: 9D 00 16        STA     $1600,X             ; {hard.earomWrite} latch cell address X into the EAROM
3AAA: A0 08           LDY     #$08                ; read mode with the clock held low
3AAC: 8C 80 16        STY     $1680               ; {hard.earomControl} drive that onto the EAROM control register
3AAF: C8              INY                         ; step to the clock-high value
3AB0: 8C 80 16        STY     $1680               ; {hard.earomControl} pulse the EAROM clock high
3AB3: 88              DEY                         ; step back to the clock-low value
3AB4: 8C 80 16        STY     $1680               ; {hard.earomControl} the falling clock edge latches the cell out
3AB7: A0 00           LDY     #$00                ; control value to release the chip
3AB9: BD 00 17        LDA     $1700,X             ; {hard.earomRead} read the addressed cell from the data-out window
3ABC: 8C 80 16        STY     $1680               ; {hard.earomControl} release EAROM chip-select and clock
3ABF: 60              RTS                         ; return the fetched cell byte

tickEaromWriteback:
3AC0: A5 00           LDA     $00                 ; {hard.workRam} read the frame counter
3AC2: 29 03           AND     #$03                ; only act every fourth frame
3AC4: D0 17           BNE     $3ADD               ; {code.loc_3add} other frames -- nothing to flush
3AC6: 8D 80 16        STA     $1680               ; {hard.earomControl} release the EAROM control lines before starting
3AC9: A6 F9           LDX     $F9                 ; {hard.workRam+F9} load the writeback cursor
3ACB: 30 10           BMI     $3ADD               ; {code.loc_3add} high bit set -- no dirty slot pending
3ACD: 46 FA           LSR     $FA                 ; {hard.workRam+FA} shift the phase word to consume this pass's bit
3ACF: 90 0D           BCC     $3ADE               ; {code.loc_3ade} bit clear -- take the scan/erase half
3AD1: A9 02           LDA     #$02                ; arm-write control value
3AD3: 8D 80 16        STA     $1680               ; {hard.earomControl} arm the EAROM for a write
3AD6: A9 0A           LDA     #$0A                ; commit-strobe control value
3AD8: 8D 80 16        STA     $1680               ; {hard.earomControl} strobe the freshly-erased cell to commit it
3ADB: C6 F9           DEC     $F9                 ; {hard.workRam+F9} step the writeback cursor down to the next slot

loc_3add:
3ADD: 60              RTS                         ; nothing to write back this pass -- return

loc_3ade:
3ADE: 78              SEI                         ; lock out interrupts while the high-score NVRAM is driven

loc_3adf:
3ADF: 20 A7 3A        JSR     $3AA7               ; {code.readEaromCell} read one cell out of the high-score EAROM
3AE2: DD 78 01        CMP     $0178,X             ; {hard.workRam+178} compare it against that slot of the high-score table mirror in RAM
3AE5: D0 07           BNE     $3AEE               ; {code.loc_3aee} they differ -- go commit this cell back to the EAROM
3AE7: CA              DEX                         ; step down to the previous high-score slot
3AE8: 10 F5           BPL     $3ADF               ; {code.loc_3adf} keep scanning the whole high-score block
3AEA: 58              CLI                         ; every cell matched -- let interrupts back in
3AEB: 86 F9           STX     $F9                 ; {hard.workRam+F9} remember the scan finished clean (index underflowed)
3AED: 60              RTS                         ; done -- return

loc_3aee:
3AEE: 58              CLI                         ; let interrupts back in before the write
3AEF: 86 F9           STX     $F9                 ; {hard.workRam+F9} stash the index of the slot that needs rewriting
3AF1: A9 06           LDA     #$06                ; load the EAROM control setup value
3AF3: 8D 80 16        STA     $1680               ; {hard.earomControl} prime the EAROM control latch to accept a write
3AF6: BD 78 01        LDA     $0178,X             ; {hard.workRam+178} read the fresh byte from the RAM high-score mirror
3AF9: 9D 00 16        STA     $1600,X             ; {hard.earomWrite} latch it into the EAROM data window at this slot
3AFC: A9 0E           LDA     #$0E                ; load the EAROM write-commit pulse value
3AFE: 8D 80 16        STA     $1680               ; {hard.earomControl} pulse the EAROM control latch to burn the byte in
3B01: E6 FA           INC     $FA                 ; {hard.workRam+FA} flip the erase/write phase word so the next pass performs the commit
3B03: 60              RTS                         ; done -- return

coldBootReset:
3B04: D8              CLD                         ; clear decimal mode so all arithmetic is plain binary
3B05: A2 FF           LDX     #$FF                ; set the index to the top of a page
3B07: 9A              TXS                         ; seat the stack pointer before handing off to boot
3B08: E8              INX                         ; roll the index to zero
3B09: 8A              TXA                         ; zero the accumulator -- the fill value for the RAM wipe

loc_3b0a:
3B0A: 95 00           STA     $00,X               ; {hard.workRam} wipe this low-page cell
3B0C: 9D 00 01        STA     $0100,X             ; {hard.workRam+100} wipe the matching stack-page cell
3B0F: 9D 00 04        STA     $0400,X             ; {hard.videoRam} wipe the matching video/object page-4 cell
3B12: 9D 00 05        STA     $0500,X             ; {hard.videoRam+100} wipe the matching page-5 cell
3B15: 9D 00 06        STA     $0600,X             ; {hard.videoRam+200} wipe the matching page-6 cell
3B18: 9D 00 07        STA     $0700,X             ; {hard.videoRam+300} wipe the matching page-7 cell
3B1B: CA              DEX                         ; step to the previous cell
3B1C: D0 EC           BNE     $3B0A               ; {code.loc_3b0a} loop until every plane of work RAM is blank
3B1E: 8D 0F 10        STA     $100F               ; {hard.pokey+F} silence the POKEY serial/keyboard control latch
3B21: 8D 08 10        STA     $1008               ; {hard.pokey+8} clear the POKEY audio control latch so no sound leaks
3B24: 8D 00 24        STA     $2400               ; {hard.rom+400} dead store the board ignores -- kept so the mirror matches
3B27: 8D 07 1C        STA     $1C07               ; {hard.outLatch+7} drop the flip-screen latch so the display orientation is defined
3B2A: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read the input port carrying the service switch
3B2D: 29 20           AND     #$20                ; isolate the service-switch bit
3B2F: F0 19           BEQ     $3B4A               ; {code.loc_3b4a} switch held -- drop into the operator self-test
3B31: AD 00 08        LDA     $0800               ; {hard.dsw1} normal boot -- read the option DIP bank
3B34: 85 FD           STA     $FD                 ; {hard.workRam+FD} snapshot the DIP config into the mode/control byte
3B36: CA              DEX                         ; roll the index to 0xff
3B37: 86 86           STX     $86                 ; {hard.workRam+86} seed the pending-wave flag to its power-on value
3B39: 86 C1           STX     $C1                 ; {hard.workRam+C1} seed a boot flag to its power-on value
3B3B: 86 C2           STX     $C2                 ; {hard.workRam+C2} seed a second boot flag to its power-on value
3B3D: A9 01           LDA     #$01                ; load the power-on value for the next flag
3B3F: 85 FF           STA     $FF                 ; {hard.workRam+FF} seed that flag to 1
3B41: 20 99 3A        JSR     $3A99               ; {code.loadHighScoreTableFromEarom} load the high-score mirror out of the NVRAM
3B44: 20 1D 3A        JSR     $3A1D               ; {code.validateOrResetHighScores} validate the high-score table, resetting it if corrupt
3B47: 4C 0E 20        JMP     $200E               ; {code.loc_200e} hand the machine to the game entry -- never returns

loc_3b4a:
3B4A: 8E 04 14        STX     $1404               ; {hard.paletteRam+4} self-test start -- clear the first playfield color cell
3B4D: 8E 01 10        STX     $1001               ; {hard.pokey+1} silence POKEY channel 1
3B50: 8E 03 10        STX     $1003               ; {hard.pokey+3} silence POKEY channel 2
3B53: 8E 05 10        STX     $1005               ; {hard.pokey+5} silence POKEY channel 3
3B56: 8E 07 10        STX     $1007               ; {hard.pokey+7} silence POKEY channel 4
3B59: E8              INX                         ; bump the color value to 1
3B5A: 8E 05 14        STX     $1405               ; {hard.paletteRam+5} paint color 1 into palette cell 05
3B5D: 8E 0D 14        STX     $140D               ; {hard.paletteRam+D} paint color 1 into palette cell 0d
3B60: E8              INX                         ; bump the color value to 2
3B61: 8E 06 14        STX     $1406               ; {hard.paletteRam+6} paint color 2 into palette cell 06
3B64: 8E 0E 14        STX     $140E               ; {hard.paletteRam+E} paint color 2 into palette cell 0e
3B67: E8              INX                         ; bump the color value to 3
3B68: 8E 07 14        STX     $1407               ; {hard.paletteRam+7} paint color 3 into palette cell 07
3B6B: 8E 0F 14        STX     $140F               ; {hard.paletteRam+F} paint color 3 into palette cell 0f
3B6E: A2 00           LDX     #$00                ; start the zeropage march at cell zero

loc_3b70:
3B70: B5 00           LDA     $00,X               ; {hard.workRam} read this zeropage cell
3B72: D0 43           BNE     $3BB7               ; {code.loc_3bb7} it should still read zero from the wipe -- else fault
3B74: A9 11           LDA     #$11                ; load the walking-bit test pattern

loc_3b76:
3B76: 95 00           STA     $00,X               ; {hard.workRam} write the pattern into the cell
3B78: A8              TAY                         ; keep a copy of the pattern
3B79: 55 00           EOR     $00,X               ; {hard.workRam} read it back and compare
3B7B: D0 3A           BNE     $3BB7               ; {code.loc_3bb7} the cell did not echo -- march fault
3B7D: 98              TYA                         ; restore the pattern
3B7E: 0A              ASL     A                   ; walk the single set bit up one place
3B7F: 90 F5           BCC     $3B76               ; {code.loc_3b76} keep walking the bit through the whole byte
3B81: E8              INX                         ; advance to the next zeropage cell
3B82: D0 EC           BNE     $3B70               ; {code.loc_3b70} loop across the whole zeropage
3B84: 8D 00 20        STA     $2000               ; {hard.rom / watchdog} pet the watchdog so it cannot reset the board mid-test
3B87: 8A              TXA                         ; drop the index into the accumulator
3B88: 85 8B           STA     $8B                 ; {hard.workRam+8B} clear the page-march pointer low byte
3B8A: 2A              ROL     A                   ; shift a page number into place

loc_3b8b:
3B8B: 85 8C           STA     $8C                 ; {hard.workRam+8C} set the page-march pointer high byte to this page
3B8D: A0 00           LDY     #$00                ; start at the first cell of the page

loc_3b8f:
3B8F: A2 11           LDX     #$11                ; load the walking-bit pattern for the page march
3B91: B1 8B           LDA     ($8B),Y             ; {hard.workRam+8B} read this page cell
3B93: D0 28           BNE     $3BBD               ; {code.loc_3bbd} it should read zero -- else page fault

loc_3b95:
3B95: 8A              TXA                         ; move the pattern into the accumulator
3B96: 91 8B           STA     ($8B),Y             ; {hard.workRam+8B} write the pattern into the page cell
3B98: 51 8B           EOR     ($8B),Y             ; {hard.workRam+8B} read it back and compare
3B9A: D0 21           BNE     $3BBD               ; {code.loc_3bbd} the cell did not echo -- page fault
3B9C: 8A              TXA                         ; move the pattern into the accumulator
3B9D: 0A              ASL     A                   ; walk the single set bit up one place
3B9E: AA              TAX                         ; hold the shifted pattern back in the index
3B9F: 90 F4           BCC     $3B95               ; {code.loc_3b95} keep walking the bit through the whole byte
3BA1: C8              INY                         ; advance to the next cell in the page
3BA2: D0 EB           BNE     $3B8F               ; {code.loc_3b8f} loop across the whole 256-byte page
3BA4: 8D 00 20        STA     $2000               ; {hard.rom / watchdog} pet the watchdog between pages
3BA7: E6 8C           INC     $8C                 ; {hard.workRam+8C} move to the next page number
3BA9: A5 8C           LDA     $8C                 ; {hard.workRam+8C} read the current page number
3BAB: C9 02           CMP     #$02                ; reached page 2?
3BAD: D0 02           BNE     $3BB1               ; {code.loc_3bb1} not page 2 -- carry on
3BAF: A9 04           LDA     #$04                ; skip the unmapped pages 2-3, jump ahead to page 4

loc_3bb1:
3BB1: C9 08           CMP     #$08                ; past the last tested page (7)?
3BB3: 90 D6           BCC     $3B8B               ; {code.loc_3b8b} still within pages 1-7 -- march the next page
3BB5: B0 5F           BCS     $3C16               ; {code.loc_3c16} all pages passed -- leave the memory march

loc_3bb7:
3BB7: C9 10           CMP     #$10                ; classify the fail flag for the beep count
3BB9: A9 00           LDA     #$00                ; clear the accumulator for the count build
3BBB: 10 12           BPL     $3BCF               ; {code.loc_3bcf} go set up the beep-and-halt reporter

loc_3bbd:
3BBD: A6 8C           LDX     $8C                 ; {hard.workRam+8C} page fault -- read which page failed
3BBF: E0 04           CPX     #$04                ; page below 4? report it in the simpler low-page style
3BC1: 90 F4           BCC     $3BB7               ; {code.loc_3bb7} low page -- fold the count the zeropage way
3BC3: AA              TAX                         ; stash the pattern in the index
3BC4: 98              TYA                         ; pull the failing byte position into the accumulator
3BC5: 29 30           AND     #$30                ; keep the position bits that encode the fault
3BC7: 4A              LSR     A                   ; shift the position down toward the low nibble
3BC8: 4A              LSR     A                   ; shift it down again
3BC9: 4A              LSR     A                   ; shift it down again
3BCA: 4A              LSR     A                   ; shift it into the low nibble
3BCB: 69 01           ADC     #$01                ; bump the beep count by one
3BCD: E0 10           CPX     #$10                ; fold the pattern bit into carry for the count

loc_3bcf:
3BCF: 2A              ROL     A                   ; roll that bit into the beep count
3BD0: A8              TAY                         ; hold the beep count in Y
3BD1: A9 40           LDA     #$40                ; load the diagnostic tone frequency
3BD3: 8D 00 10        STA     $1000               ; {hard.pokey} set POKEY channel-1 frequency for the beep
3BD6: A2 03           LDX     #$03                ; load the serial/keyboard control arm value
3BD8: 8E 0F 10        STX     $100F               ; {hard.pokey+F} arm the POKEY control latch for the tone

loc_3bdb:
3BDB: A2 10           LDX     #$10                ; load the vblank-edge count for one half-beep
3BDD: A9 AF           LDA     #$AF                ; load the tone-on control/volume value
3BDF: 8D 01 10        STA     $1001               ; {hard.pokey+1} turn the beep tone on

loc_3be2:
3BE2: 2C 00 0C        BIT     $0C00               ; {hard.in0 / trackballX} read the beam's vblank edge
3BE5: 50 FB           BVC     $3BE2               ; {code.loc_3be2} wait for the vblank edge to arrive

loc_3be7:
3BE7: 2C 00 0C        BIT     $0C00               ; {hard.in0 / trackballX} read the beam's vblank edge again
3BEA: 70 FB           BVS     $3BE7               ; {code.loc_3be7} wait for the edge to clear
3BEC: 8D 00 20        STA     $2000               ; {hard.rom / watchdog} pet the watchdog so the beep can play out
3BEF: CA              DEX                         ; count down one vblank edge of the tone-on half
3BF0: D0 F0           BNE     $3BE2               ; {code.loc_3be2} loop for the whole tone-on half of the beep
3BF2: 8E 01 10        STX     $1001               ; {hard.pokey+1} turn the beep tone off
3BF5: A2 10           LDX     #$10                ; load the vblank-edge count for the tone-off half

loc_3bf7:
3BF7: 2C 00 0C        BIT     $0C00               ; {hard.in0 / trackballX} read the beam's vblank edge
3BFA: 50 FB           BVC     $3BF7               ; {code.loc_3bf7} wait for the vblank edge to arrive

loc_3bfc:
3BFC: 2C 00 0C        BIT     $0C00               ; {hard.in0 / trackballX} read the beam's vblank edge again
3BFF: 70 FB           BVS     $3BFC               ; {code.loc_3bfc} wait for the edge to clear
3C01: 8D 00 20        STA     $2000               ; {hard.rom / watchdog} pet the watchdog so the silent half can play out
3C04: CA              DEX                         ; count down one vblank edge of the tone-off half
3C05: D0 F0           BNE     $3BF7               ; {code.loc_3bf7} loop for the whole tone-off half of the beep
3C07: 88              DEY                         ; one beep done -- count it off
3C08: 10 D1           BPL     $3BDB               ; {code.loc_3bdb} repeat until the beep count underflows

loc_3c0a:
3C0A: 8D 00 20        STA     $2000               ; {hard.rom / watchdog} pet the watchdog while waiting to halt
3C0D: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read the input port carrying the service switch
3C10: 29 20           AND     #$20                ; isolate the service-switch bit
3C12: F0 F6           BEQ     $3C0A               ; {code.loc_3c0a} still held -- keep petting and waiting

loc_3c14:
3C14: D0 FE           BNE     $3C14               ; {code.loc_3c14} hang the processor forever -- only a power cycle clears the fault

loc_3c16:
3C16: AD 01 0C        LDA     $0C01               ; {hard.in1} marches passed -- read the coin/option input port
3C19: 29 10           AND     #$10                ; isolate the coin/option bit
3C1B: F0 03           BEQ     $3C20               ; {code.loc_3c20} clear -- build the on-screen diagnostic
3C1D: 4C 97 3C        JMP     $3C97               ; {code.loc_3c97} set -- jump to the checksum-display screen (does not return)

loc_3c20:
3C20: AA              TAX                         ; roll the index to zero for the re-clear

loc_3c21:
3C21: 95 00           STA     $00,X               ; {hard.workRam} re-clear this zeropage cell
3C23: E8              INX                         ; advance to the next cell
3C24: D0 FB           BNE     $3C21               ; {code.loc_3c21} loop across the whole zeropage
3C26: A2 0F           LDX     #$0F                ; index the top of a 16-cell block
3C28: A9 F8           LDA     #$F8                ; load the fill glyph

loc_3c2a:
3C2A: 95 64           STA     $64,X               ; {hard.workRam+64} seed this cell of the loc_64 row with the fill glyph
3C2C: CA              DEX                         ; step down one cell
3C2D: 10 FB           BPL     $3C2A               ; {code.loc_3c2a} fill all sixteen row cells
3C2F: A9 07           LDA     #$07                ; start at video page 7
3C31: 85 8C           STA     $8C                 ; {hard.workRam+8C} set the page pointer high byte to page 7
3C33: A0 BF           LDY     #$BF                ; seed the offset near the top of the page

loc_3c35:
3C35: A9 2D           LDA     #$2D                ; load the starting glyph code for this row

loc_3c37:
3C37: A2 08           LDX     #$08                ; set the run length to eight cells

loc_3c39:
3C39: 91 8B           STA     ($8B),Y             ; {hard.workRam+8B} paint the glyph into this screen cell
3C3B: 88              DEY                         ; step back one cell
3C3C: CA              DEX                         ; count down the run
3C3D: D0 FA           BNE     $3C39               ; {code.loc_3c39} loop for a run of eight
3C3F: 38              SEC                         ; prepare a clean subtract
3C40: E9 01           SBC     #$01                ; step to the next glyph code down
3C42: C9 2A           CMP     #$2A                ; floor the glyph code at 0x2a
3C44: B0 F1           BCS     $3C37               ; {code.loc_3c37} keep painting descending glyph runs across the row
3C46: C0 FF           CPY     #$FF                ; whole page painted (offset wrapped)?
3C48: D0 EB           BNE     $3C35               ; {code.loc_3c35} not yet -- start the next row
3C4A: C6 8C           DEC     $8C                 ; {hard.workRam+8C} move down to the previous page
3C4C: A5 8C           LDA     $8C                 ; {hard.workRam+8C} read the current page number
3C4E: C9 04           CMP     #$04                ; reached page 4?
3C50: B0 E3           BCS     $3C35               ; {code.loc_3c35} still pages 7 down to 4 -- keep painting
3C52: 58              CLI                         ; enable interrupts for the input-response screen

loc_3c53:
3C53: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read the input port carrying the service switch
3C56: 29 20           AND     #$20                ; isolate the service-switch bit
3C58: D0 F9           BNE     $3C53               ; {code.loc_3c53} keep spinning while the service switch is idle; proceed once it is pressed
3C5A: 46 8A           LSR     $8A                 ; {hard.workRam+8A} shift the pacing value one place
3C5C: 8D 00 20        STA     $2000               ; {hard.rom / watchdog} pet the watchdog each pass
3C5F: AD 01 0C        LDA     $0C01               ; {hard.in1} read the control input port
3C62: 29 E0           AND     #$E0                ; keep the top three control bits
3C64: 49 E0           EOR     #$E0                ; flip them so an actuated control reads nonzero
3C66: F0 EB           BEQ     $3C53               ; {code.loc_3c53} nothing actuated yet -- keep waiting
3C68: A9 1D           LDA     #$1D                ; load the response fill color
3C6A: 78              SEI                         ; lock out interrupts to flood the screen

loc_3c6b:
3C6B: 9D 00 04        STA     $0400,X             ; {hard.videoRam} flood video page 4 with the response color
3C6E: 9D 00 05        STA     $0500,X             ; {hard.videoRam+100} flood video page 5 with the response color
3C71: 9D 00 06        STA     $0600,X             ; {hard.videoRam+200} flood video page 6 with the response color
3C74: E8              INX                         ; advance to the next cell
3C75: D0 F4           BNE     $3C6B               ; {code.loc_3c6b} flood the whole 256 cells

loc_3c77:
3C77: 9D 00 07        STA     $0700,X             ; {hard.videoRam+300} flood this cell of page 7 with the response color
3C7A: E8              INX                         ; advance to the next cell
3C7B: E0 C0           CPX     #$C0                ; reached the 0xc0 stopping point?
3C7D: 90 F8           BCC     $3C77               ; {code.loc_3c77} keep flooding page 7 up to the limit
3C7F: A2 08           LDX     #$08                ; load a bright palette value
3C81: 8E 05 14        STX     $1405               ; {hard.paletteRam+5} brighten palette cell 05
3C84: A2 0F           LDX     #$0F                ; load another bright palette value
3C86: 8E 04 14        STX     $1404               ; {hard.paletteRam+4} brighten the first playfield color cell

loc_3c89:
3C89: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read IN0, where the operator service switch lives, to hold the self-test review screen
3C8C: 29 20           AND     #$20                ; isolate bit 5, the service switch (low only while held)
3C8E: D0 F9           BNE     $3C89               ; {code.loc_3c89} switch released -- spin at the top without petting the watchdog, so letting go resets the board out of the test
3C90: 8D 00 20        STA     $2000               ; {hard.rom / watchdog} switch still held -- pet the watchdog so the review screen stays alive
3C93: 46 8A           LSR     $8A                 ; {hard.workRam+8A} shift the pacing byte 8a to time the hold
3C95: 10 F2           BPL     $3C89               ; {code.loc_3c89} loop the review hold forever; only a watchdog reset leaves it

loc_3c97:
3C97: A2 00           LDX     #$00                ; start the wipe index at 0

loc_3c99:
3C99: 8A              TXA                         ; copy the index into A
3C9A: 9D 00 07        STA     $0700,X             ; {hard.videoRam+300} paint an ascending tile-code ramp across the sprite/object page at 0x0700
3C9D: A9 00           LDA     #$00                ; load zero for the clears
3C9F: 95 00           STA     $00,X               ; {hard.workRam} clear this zero-page cell
3CA1: 9D 00 04        STA     $0400,X             ; {hard.videoRam} clear the matching page-4 object cell
3CA4: 9D 00 05        STA     $0500,X             ; {hard.videoRam+100} clear the matching page-5 object cell
3CA7: 9D 00 06        STA     $0600,X             ; {hard.videoRam+200} clear the matching page-6 object cell
3CAA: E8              INX                         ; step to the next cell
3CAB: D0 EC           BNE     $3C99               ; {code.loc_3c99} loop until all 256 cells are wiped
3CAD: CA              DEX                         ; roll the index down to 0xff
3CAE: 86 D5           STX     $D5                 ; {hard.workRam+D5} seed loc_d5 to 0xff
3CB0: 86 E3           STX     $E3                 ; {hard.workRam+E3} seed loc_e3 to 0xff
3CB2: 8D 03 1C        STA     $1C03               ; {hard.outLatch+3} clear output latch 3
3CB5: 8D 04 1C        STA     $1C04               ; {hard.outLatch+4} clear output latch 4
3CB8: A2 0F           LDX     #$0F                ; start the object-slot seed index at 0x0f

loc_3cba:
3CBA: 8A              TXA                         ; copy the slot index into A
3CBB: 09 80           ORA     #$80                ; set bit 7 to mark the slot free/retired
3CBD: 95 54           STA     $54,X               ; {hard.workRam+54} seed object coordinate slot 0x54+x as free
3CBF: 95 64           STA     $64,X               ; {hard.workRam+64} seed object coordinate slot 0x64+x as free
3CC1: CA              DEX                         ; step to the next slot
3CC2: 10 F6           BPL     $3CBA               ; {code.loc_3cba} loop over all sixteen object slots
3CC4: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
3CC7: 4D 0A 10        EOR     $100A               ; {hard.pokey+A} fold in a second read of the random register (the pair cancels at rest)
3CCA: 85 E5           STA     $E5                 ; {hard.workRam+E5} stash the mixed random value in loc_e5
3CCC: A9 03           LDA     #$03                ; load 3 for the POKEY control latch
3CCE: 8D 0F 10        STA     $100F               ; {hard.pokey+F} arm the POKEY control latch (SKCTL) so sound can play
3CD1: A2 00           LDX     #$00                ; clear the pointer low index
3CD3: 86 8B           STX     $8B                 ; {hard.workRam+8B} set the checksum pointer low byte 8b to 0
3CD5: A9 20           LDA     #$20                ; load 0x20 for the pointer high byte
3CD7: 85 8C           STA     $8C                 ; {hard.workRam+8C} point the checksum pointer at ROM page 0x20
3CD9: A2 1F           LDX     #$1F                ; count 0x1f pages to checksum
3CDB: A9 FF           LDA     #$FF                ; seed the running checksum accumulator to 0xff

loc_3cdd:
3CDD: A0 00           LDY     #$00                ; start each page at byte 0
3CDF: 8E 00 20        STX     $2000               ; {hard.rom / watchdog} pet the watchdog with the page counter while checksumming

loc_3ce2:
3CE2: 51 8B           EOR     ($8B),Y             ; {hard.workRam+8B} fold one ROM byte into the running checksum
3CE4: C8              INY                         ; step to the next byte in the page
3CE5: D0 FB           BNE     $3CE2               ; {code.loc_3ce2} loop over all 256 bytes of the page
3CE7: A8              TAY                         ; save the running checksum into Y
3CE8: 8A              TXA                         ; pull the page counter into A
3CE9: 29 07           AND     #$07                ; keep its low three bits to spot a bank boundary
3CEB: C9 01           CMP     #$01                ; test whether a bank has just finished
3CED: 98              TYA                         ; restore the checksum into A
3CEE: B0 03           BCS     $3CF3               ; {code.loc_3cf3} not a bank boundary yet -- keep summing
3CF0: 48              PHA                         ; bank complete: push this bank's checksum onto the stack
3CF1: A9 FF           LDA     #$FF                ; reseed the accumulator for the next bank

loc_3cf3:
3CF3: E6 8C           INC     $8C                 ; {hard.workRam+8C} advance the pointer to the next ROM page
3CF5: CA              DEX                         ; step to the next page
3CF6: 10 E5           BPL     $3CDD               ; {code.loc_3cdd} loop through every ROM page
3CF8: A9 04           LDA     #$04                ; set the plot cursor row to 4
3CFA: 85 92           STA     $92                 ; {hard.workRam+92} store the cursor high byte
3CFC: A2 03           LDX     #$03                ; four ROM banks to report

loc_3cfe:
3CFE: 8A              TXA                         ; copy the bank index into A
3CFF: 49 3F           EOR     #$3F                ; turn the bank index into its screen column
3D01: 85 91           STA     $91                 ; {hard.workRam+91} store the cursor low byte
3D03: 68              PLA                         ; pull one bank's checksum off the stack
3D04: F0 11           BEQ     $3D17               ; {code.loc_3d17} checksum zero means the bank is good -- skip its line
3D06: 48              PHA                         ; bad bank: keep the checksum
3D07: 8A              TXA                         ; copy the bank index into A
3D08: 09 20           ORA     #$20                ; build the bank's label glyph
3D0A: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot the bank label
3D0D: A9 00           LDA     #$00                ; load a blank
3D0F: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot the separator space
3D12: 68              PLA                         ; pull the bank checksum back
3D13: 18              CLC                         ; clear carry before the digit plot
3D14: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot the checksum as two hex digits

loc_3d17:
3D17: CA              DEX                         ; step to the next bank
3D18: 10 E4           BPL     $3CFE               ; {code.loc_3cfe} loop over all four banks
3D1A: 20 99 3A        JSR     $3A99               ; {code.loadHighScoreTableFromEarom} load the high-score table out of the EAROM
3D1D: A0 06           LDY     #$06                ; seven high-score header bytes to copy

loc_3d1f:
3D1F: B9 8B 01        LDA     $018B,Y             ; {hard.workRam+18B} read a high-score table byte
3D22: 99 8E 00        STA     $008E,Y             ; {hard.workRam+8E} mirror it into the working block at 0x8e
3D25: 88              DEY                         ; step to the previous byte
3D26: 10 F7           BPL     $3D1F               ; {code.loc_3d1f} loop until all seven are copied
3D28: F8              SED                         ; switch to decimal (BCD) arithmetic
3D29: AD 8B 01        LDA     $018B               ; {hard.workRam+18B} read the score's low byte (test the 3-byte score for all-zero)
3D2C: 0D 8C 01        ORA     $018C               ; {hard.workRam+18C} OR in the next score byte
3D2F: 0D 8D 01        ORA     $018D               ; {hard.workRam+18D} OR in the last score byte to test for an all-zero score
3D32: F0 1F           BEQ     $3D53               ; {code.loc_3d53} no score set -- skip the ranking
3D34: C8              INY                         ; seed the iteration counter

loc_3d35:
3D35: C8              INY                         ; advance the iteration counter
3D36: F0 1B           BEQ     $3D53               ; {code.loc_3d53} counter wrapped -- give up ranking
3D38: A5 91           LDA     $91                 ; {hard.workRam+91} load the working value low byte
3D3A: 38              SEC                         ; set carry for the subtract
3D3B: E5 8E           SBC     $8E                 ; {hard.workRam+8E} subtract the score low byte (BCD)
3D3D: 85 91           STA     $91                 ; {hard.workRam+91} store the low byte back
3D3F: A5 92           LDA     $92                 ; {hard.workRam+92} load the next working byte
3D41: E5 8F           SBC     $8F                 ; {hard.workRam+8F} subtract the next score byte with borrow
3D43: 85 92           STA     $92                 ; {hard.workRam+92} store it back
3D45: A5 93           LDA     $93                 ; {hard.workRam+93} load the next working byte
3D47: E5 90           SBC     $90                 ; {hard.workRam+90} subtract the next score byte with borrow
3D49: 85 93           STA     $93                 ; {hard.workRam+93} store it back
3D4B: A5 94           LDA     $94                 ; {hard.workRam+94} load the top working byte
3D4D: E9 00           SBC     #$00                ; subtract the borrow through the top byte
3D4F: 85 94           STA     $94                 ; {hard.workRam+94} store it back
3D51: 10 E2           BPL     $3D35               ; {code.loc_3d35} still non-negative -- subtract the score again

loc_3d53:
3D53: D8              CLD                         ; leave decimal mode
3D54: 84 8D           STY     $8D                 ; {hard.workRam+8D} store the derived rank count into loc_8d
3D56: 58              CLI                         ; re-enable interrupts

loc_3d57:
3D57: 46 8A           LSR     $8A                 ; {hard.workRam+8A} shift the frame-pacing byte 8a right, waiting for the heartbeat bit
3D59: 90 FC           BCC     $3D57               ; {code.loc_3d57} loop until a frame heartbeat lands in carry
3D5B: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read IN0
3D5E: 29 20           AND     #$20                ; isolate the service switch bit

loc_3d60:
3D60: D0 FE           BNE     $3D60               ; {code.loc_3d60} spin here while the service switch reads set
3D62: 8D 00 20        STA     $2000               ; {hard.rom / watchdog} pet the watchdog
3D65: AD 01 0C        LDA     $0C01               ; {hard.in1} read the control port IN1
3D68: 4A              LSR     A                   ; drop bit 0 of IN1 into carry
3D69: 26 EA           ROL     $EA                 ; {hard.workRam+EA} rotate that bit into the loc_ea edge-history shift register
3D6B: A5 EA           LDA     $EA                 ; {hard.workRam+EA} load the edge history
3D6D: 29 03           AND     #$03                ; keep its low two bits
3D6F: C9 02           CMP     #$02                ; test for the just-actuated edge pattern
3D71: D0 24           BNE     $3D97               ; {code.loc_3d97} no fresh edge on this control -- skip to the next
3D73: A5 E6           LDA     $E6                 ; {hard.workRam+E6} load the channel cursor e6
3D75: AA              TAX                         ; copy it into X to index the sound register
3D76: 18              CLC                         ; clear carry
3D77: 69 02           ADC     #$02                ; add 2
3D79: 29 06           AND     #$06                ; wrap it into the 0,2,4,6 cycle
3D7B: 85 E6           STA     $E6                 ; {hard.workRam+E6} store the advanced channel cursor e6
3D7D: A9 00           LDA     #$00                ; load a silence value
3D7F: 9D 01 10        STA     $1001,X             ; {hard.pokey+1} silence the selected POKEY channel volume register
3D82: A5 E7           LDA     $E7                 ; {hard.workRam+E7} load counter e7
3D84: 18              CLC                         ; clear carry
3D85: 69 01           ADC     #$01                ; add 1
3D87: 29 0F           AND     #$0F                ; wrap it to a nibble
3D89: 85 E7           STA     $E7                 ; {hard.workRam+E7} store the advanced counter e7
3D8B: A6 E8           LDX     $E8                 ; {hard.workRam+E8} load palette counter e8
3D8D: E8              INX                         ; step it up
3D8E: 8A              TXA                         ; copy it into A
3D8F: 29 0F           AND     #$0F                ; wrap it to a nibble
3D91: AA              TAX                         ; move it back into X
3D92: 8E 04 14        STX     $1404               ; {hard.paletteRam+4} write the cycling colour into palette cell 04
3D95: 86 E8           STX     $E8                 ; {hard.workRam+E8} store the palette counter e8

loc_3d97:
3D97: AD 01 0C        LDA     $0C01               ; {hard.in1} read the control port IN1
3D9A: 4A              LSR     A                   ; drop bit 0
3D9B: 4A              LSR     A                   ; shift bit 1 into carry
3D9C: 26 EB           ROL     $EB                 ; {hard.workRam+EB} rotate it into the loc_eb edge-history register
3D9E: A5 EB           LDA     $EB                 ; {hard.workRam+EB} load the edge history
3DA0: 29 03           AND     #$03                ; keep the low two bits
3DA2: C9 02           CMP     #$02                ; test for the just-actuated edge pattern
3DA4: D0 16           BNE     $3DBC               ; {code.loc_3dbc} no fresh edge on this control -- skip on
3DA6: E6 E9           INC     $E9                 ; {hard.workRam+E9} bump counter e9
3DA8: A5 E9           LDA     $E9                 ; {hard.workRam+E9} load it
3DAA: A0 01           LDY     #$01                ; start the palette fill at index 1

loc_3dac:
3DAC: 18              CLC                         ; clear carry
3DAD: 69 01           ADC     #$01                ; add 1
3DAF: 29 0F           AND     #$0F                ; wrap to a nibble
3DB1: 99 04 14        STA     $1404,Y             ; {hard.paletteRam+4} write the colour ramp into palette cells 05..07
3DB4: 99 0C 14        STA     $140C,Y             ; {hard.paletteRam+C} write the same into palette cells 0d..0f
3DB7: C8              INY                         ; step to the next palette cell
3DB8: C0 04           CPY     #$04                ; four cells done?
3DBA: 90 F0           BCC     $3DAC               ; {code.loc_3dac} loop until the palette triple is filled

loc_3dbc:
3DBC: AD 01 0C        LDA     $0C01               ; {hard.in1} read the control port IN1
3DBF: 4A              LSR     A                   ; drop bit 0
3DC0: 4A              LSR     A                   ; drop bit 1
3DC1: 4A              LSR     A                   ; shift bit 2 into carry
3DC2: 26 EC           ROL     $EC                 ; {hard.workRam+EC} rotate it into the loc_ec edge-history register
3DC4: A5 EC           LDA     $EC                 ; {hard.workRam+EC} load the edge history
3DC6: 29 03           AND     #$03                ; keep the low two bits
3DC8: 49 02           EOR     #$02                ; fold against the edge pattern
3DCA: D0 15           BNE     $3DE1               ; {code.loc_3de1} no fresh edge on this control -- skip on
3DCC: 85 BD           STA     $BD                 ; {hard.workRam+BD} clear loc_bd
3DCE: 85 BF           STA     $BF                 ; {hard.workRam+BF} clear loc_bf
3DD0: 8D 00 24        STA     $2400               ; {hard.rom+400} dead store the machine ignores at 0x2400
3DD3: A9 01           LDA     #$01                ; load 1
3DD5: 8D 07 1C        STA     $1C07               ; {hard.outLatch+7} drive the flip-screen latch to normal orientation
3DD8: 85 88           STA     $88                 ; {hard.workRam+88} set loc_88 to 1
3DDA: A2 0F           LDX     #$0F                ; sixteen object cells to bump

loc_3ddc:
3DDC: F6 34           INC     $34,X               ; {hard.workRam+34} bump object cell 0x34+x
3DDE: CA              DEX                         ; step to the previous cell
3DDF: 10 FB           BPL     $3DDC               ; {code.loc_3ddc} loop over all sixteen

loc_3de1:
3DE1: AD 01 0C        LDA     $0C01               ; {hard.in1} read the control port IN1
3DE4: 4A              LSR     A                   ; drop bit 0
3DE5: 4A              LSR     A                   ; drop bit 1
3DE6: 4A              LSR     A                   ; drop bit 2
3DE7: 4A              LSR     A                   ; shift bit 3 into carry
3DE8: 26 ED           ROL     $ED                 ; {hard.workRam+ED} rotate it into the loc_ed edge-history register
3DEA: A5 ED           LDA     $ED                 ; {hard.workRam+ED} load the edge history
3DEC: 29 03           AND     #$03                ; keep the low two bits
3DEE: 49 02           EOR     #$02                ; fold against the edge pattern
3DF0: D0 10           BNE     $3E02               ; {code.loc_3e02} no fresh edge on this control -- skip on
3DF2: 85 BD           STA     $BD                 ; {hard.workRam+BD} clear loc_bd
3DF4: 85 BF           STA     $BF                 ; {hard.workRam+BF} clear loc_bf
3DF6: 8D 00 24        STA     $2400               ; {hard.rom+400} dead store the machine ignores at 0x2400
3DF9: A9 02           LDA     #$02                ; set loc_88 to 2
3DFB: 85 88           STA     $88                 ; {hard.workRam+88} store it
3DFD: A9 FF           LDA     #$FF                ; load 0xff
3DFF: 8D 07 1C        STA     $1C07               ; {hard.outLatch+7} drive the flip-screen latch to flipped orientation

loc_3e02:
3E02: A9 05           LDA     #$05                ; load the plot cursor row value 5
3E04: 85 92           STA     $92                 ; {hard.workRam+92} set the cursor high byte
3E06: A9 38           LDA     #$38                ; load the plot cursor column value 0x38
3E08: 85 91           STA     $91                 ; {hard.workRam+91} set the cursor low byte
3E0A: AD 00 08        LDA     $0800               ; {hard.dsw1} read the option DIP bank DSW1
3E0D: 29 0C           AND     #$0C                ; keep bits 3-2
3E0F: 4A              LSR     A                   ; shift them down
3E10: 4A              LSR     A                   ; shift again
3E11: 69 01           ADC     #$01                ; add 1 to make a 1..4 count
3E13: 85 8B           STA     $8B                 ; {hard.workRam+8B} store the count into 8b
3E15: A2 05           LDX     #$05                ; five columns to plot

loc_3e17:
3E17: A9 1F           LDA     #$1F                ; load the filled block glyph
3E19: 24 8B           BIT     $8B                 ; {hard.workRam+8B} test the countdown byte 8b
3E1B: 10 02           BPL     $3E1F               ; {code.loc_3e1f} still positive -- keep the block glyph
3E1D: A9 00           LDA     #$00                ; else use a blank glyph

loc_3e1f:
3E1F: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot the glyph at the cursor
3E22: C6 8B           DEC     $8B                 ; {hard.workRam+8B} step the countdown byte 8b
3E24: CA              DEX                         ; next column
3E25: D0 F0           BNE     $3E17               ; {code.loc_3e17} loop the five columns
3E27: A9 37           LDA     #$37                ; load the plot cursor column value 0x37
3E29: 85 91           STA     $91                 ; {hard.workRam+91} set the cursor low byte
3E2B: A9 21           LDA     #$21                ; load the label glyph 0x21
3E2D: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot the label
3E30: AD 01 08        LDA     $0801               ; {hard.dsw2} read DIP bank DSW2
3E33: 29 10           AND     #$10                ; keep bit 4
3E35: 4A              LSR     A                   ; shift it down
3E36: 4A              LSR     A                   ; shift again
3E37: 4A              LSR     A                   ; shift again
3E38: 4A              LSR     A                   ; shift bit 4 to bit 0
3E39: 69 01           ADC     #$01                ; add 1
3E3B: 09 20           ORA     #$20                ; build the option glyph code
3E3D: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} plot the option glyph
3E40: AD 01 08        LDA     $0801               ; {hard.dsw2} read DIP bank DSW2 again
3E43: 29 0C           AND     #$0C                ; keep bits 3-2
3E45: 4A              LSR     A                   ; shift them down
3E46: 4A              LSR     A                   ; shift again
3E47: D0 02           BNE     $3E4B               ; {code.loc_3e4b} nonzero option -- branch onward
3E49: A9 FE           LDA     #$FE                ; else load the 0xfe marker

loc_3e4b:
3E4B: 69 03           ADC     #$03                ; add 3 to the tallied value to bias it into the glyph range
3E4D: 09 20           ORA     #$20                ; set bit 5 so the value reads as a printable character code
3E4F: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} emit that glyph and step the screen write pointer forward
3E52: A9 36           LDA     #$36                ; aim the write cursor low byte at cell 0x36
3E54: 85 91           STA     $91                 ; {hard.workRam+91} seat the draw cursor
3E56: A9 00           LDA     #$00                ; load zero
3E58: A8              TAY                         ; Y = 0, the base offset
3E59: 91 91           STA     ($91),Y             ; {hard.workRam+91} blank the cell the cursor sits on
3E5B: A0 40           LDY     #$40                ; step the offset 0x40 further down the column
3E5D: 91 91           STA     ($91),Y             ; {hard.workRam+91} blank that cell too
3E5F: AD 01 08        LDA     $0801               ; {hard.dsw2} read the DSW2 option bank
3E62: 4A              LSR     A                   ; shift the option bits right one
3E63: 4A              LSR     A                   ; shift right again
3E64: 4A              LSR     A                   ; shift right again
3E65: 4A              LSR     A                   ; shift right again
3E66: 4A              LSR     A                   ; fifth shift drops the top three option bits to the bottom
3E67: F0 1B           BEQ     $3E84               ; {code.loc_3e84} if that option field is zero, skip the bonus glyph
3E69: AA              TAX                         ; stash the option value as the table index
3E6A: C9 06           CMP     #$06                ; compare it against 6
3E6C: B0 16           BCS     $3E84               ; {code.loc_3e84} out of range -- skip the bonus glyph
3E6E: BD D8 3F        LDA     $3FD8,X             ; {hard.rom+1FD8} read the bonus glyph from the option table by that index
3E71: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} emit the bonus glyph
3E74: A9 00           LDA     #$00                ; load a blank
3E76: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} emit the blank spacer after it
3E79: A9 21           LDA     #$21                ; load glyph 0x21
3E7B: E0 03           CPX     #$03                ; is the option value exactly 3?
3E7D: D0 02           BNE     $3E81               ; {code.loc_3e81} no -- keep glyph 0x21
3E7F: A9 22           LDA     #$22                ; yes -- use glyph 0x22 instead

loc_3e81:
3E81: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} emit that trailing glyph

loc_3e84:
3E84: A9 3F           LDA     #$3F                ; load the ROM text-row pointer high byte 0x3f
3E86: 85 94           STA     $94                 ; {hard.workRam+94} set the row pointer high byte
3E88: A9 EE           LDA     #$EE                ; default the row pointer low byte to 0xee
3E8A: 2C 00 08        BIT     $0800               ; {hard.dsw1} test the DSW1 option bank
3E8D: 50 02           BVC     $3E91               ; {code.loc_3e91} option bit 6 clear -- keep the default text row
3E8F: A9 F2           LDA     #$F2                ; bit 6 set -- select the alternate text row at 0xf2

loc_3e91:
3E91: 85 93           STA     $93                 ; {hard.workRam+93} set the row pointer low byte
3E93: A9 35           LDA     #$35                ; load draw cursor 0x35
3E95: 85 91           STA     $91                 ; {hard.workRam+91} seat the draw cursor for the row
3E97: 20 25 38        JSR     $3825               ; {code.redrawPointerTableRowUnblanked} draw that option text row onto the screen
3E9A: AD 01 0C        LDA     $0C01               ; {hard.in1} read input port IN1
3E9D: 85 DF           STA     $DF                 ; {hard.workRam+DF} snapshot IN1
3E9F: AD 00 08        LDA     $0800               ; {hard.dsw1} read the DSW1 option bank
3EA2: 85 DD           STA     $DD                 ; {hard.workRam+DD} snapshot DSW1
3EA4: AD 01 08        LDA     $0801               ; {hard.dsw2} read the DSW2 option bank
3EA7: 85 DE           STA     $DE                 ; {hard.workRam+DE} snapshot DSW2
3EA9: AD 00 0C        LDA     $0C00               ; {hard.in0 / trackballX} read input port IN0
3EAC: 29 8F           AND     #$8F                ; keep only the meaningful IN0 bits
3EAE: 85 E0           STA     $E0                 ; {hard.workRam+E0} snapshot masked IN0
3EB0: AD 02 0C        LDA     $0C02               ; {hard.in2 / trackballY} read input port IN2
3EB3: 29 8F           AND     #$8F                ; keep only the meaningful IN2 bits
3EB5: 85 E1           STA     $E1                 ; {hard.workRam+E1} snapshot masked IN2
3EB7: AD 03 0C        LDA     $0C03               ; {hard.in3} read input port IN3
3EBA: 85 E2           STA     $E2                 ; {hard.workRam+E2} snapshot IN3
3EBC: AD 0A 10        LDA     $100A               ; {hard.pokey+A} read the POKEY random register
3EBF: 48              PHA                         ; stash the random sample
3EC0: 25 E3           AND     $E3                 ; {hard.workRam+E3} AND it into the stuck-high accumulator (a bit stays set only if every sample read 1)
3EC2: 85 E3           STA     $E3                 ; {hard.workRam+E3} store the running AND of random samples
3EC4: 68              PLA                         ; recover the random sample
3EC5: 05 E4           ORA     $E4                 ; {hard.workRam+E4} OR it into the stuck-low accumulator (a bit stays clear only if no sample ever read 1)
3EC7: 85 E4           STA     $E4                 ; {hard.workRam+E4} store the running OR of random samples
3EC9: A2 00           LDX     #$00                ; clear the bit-position counter
3ECB: AD 01 0C        LDA     $0C01               ; {hard.in1} read input port IN1 again
3ECE: 38              SEC                         ; set carry as the walking sentinel
3ECF: 2A              ROL     A                   ; rotate the sentinel into the value

loc_3ed0:
3ED0: B0 01           BCS     $3ED3               ; {code.loc_3ed3} if the top bit is set, stop counting
3ED2: E8              INX                         ; count one more empty bit position

loc_3ed3:
3ED3: 0A              ASL     A                   ; shift the next bit up
3ED4: D0 FA           BNE     $3ED0               ; {code.loc_3ed0} keep scanning until the value empties
3ED6: 8A              TXA                         ; move the highest-set-bit index into A
3ED7: A4 E6           LDY     $E6                 ; {hard.workRam+E6} load the tone channel offset
3ED9: 0A              ASL     A                   ; scale the index up (x2)
3EDA: 0A              ASL     A                   ; scale again (x4)
3EDB: 0A              ASL     A                   ; scale again (x8) into a tone pitch
3EDC: 99 00 10        STA     $1000,Y             ; {hard.pokey} set the POKEY tone frequency for the actuated input
3EDF: 8A              TXA                         ; reload the bit index
3EE0: 09 A0           ORA     #$A0                ; set the volume and distortion bits
3EE2: 99 01 10        STA     $1001,Y             ; {hard.pokey+1} sound the tone through the POKEY control register
3EE5: A6 E7           LDX     $E7                 ; {hard.workRam+E7} load the trackball object index
3EE7: A0 00           LDY     #$00                ; Y = 0, the clear value
3EE9: A5 B9           LDA     $B9                 ; {hard.workRam+B9} read the pending trackball delta on this axis
3EEB: 84 B9           STY     $B9                 ; {hard.workRam+B9} clear the pending delta now that it is consumed
3EED: 18              CLC                         ; clear carry for the add
3EEE: 75 54           ADC     $54,X               ; {hard.workRam+54} add the delta into the object's coordinate
3EF0: 95 54           STA     $54,X               ; {hard.workRam+54} store the advanced coordinate
3EF2: B5 64           LDA     $64,X               ; {hard.workRam+64} read the object's other-axis coordinate
3EF4: 38              SEC                         ; set carry for the subtract
3EF5: E5 BB           SBC     $BB                 ; {hard.workRam+BB} subtract the second pending trackball delta
3EF7: 84 BB           STY     $BB                 ; {hard.workRam+BB} clear that pending delta too
3EF9: 95 64           STA     $64,X               ; {hard.workRam+64} store the adjusted coordinate
3EFB: A0 D0           LDY     #$D0                ; point the screen offset at 0xd0
3EFD: A2 05           LDX     #$05                ; load the row counter -- six snapshot bytes to show

loc_3eff:
3EFF: 9A              TXS                         ; park the row index in the stack pointer as a scratch index
3F00: A2 07           LDX     #$07                ; load the bit counter -- eight bits

loc_3f02:
3F02: 8A              TXA                         ; save the bit counter in A
3F03: BA              TSX                         ; pull the row index back out of the stack pointer
3F04: 36 DD           ROL     $DD,X               ; {hard.workRam+DD} rotate the top bit of this snapshot byte into carry
3F06: AA              TAX                         ; restore the bit counter into X
3F07: A9 21           LDA     #$21                ; load the "bit set" glyph
3F09: B0 02           BCS     $3F0D               ; {code.loc_3f0d} bit was set -- keep it
3F0B: A9 20           LDA     #$20                ; bit was clear -- use the "bit clear" glyph

loc_3f0d:
3F0D: C8              INY                         ; step to the next screen cell
3F0E: 99 00 04        STA     $0400,Y             ; {hard.videoRam} write the on/off glyph into the switch-state row
3F11: CA              DEX                         ; next bit
3F12: 10 EE           BPL     $3F02               ; {code.loc_3f02} loop across all eight bits of the byte
3F14: 98              TYA                         ; move the screen offset into A
3F15: 38              SEC                         ; set carry for the subtract
3F16: E9 28           SBC     #$28                ; back up one full screen row (0x28)
3F18: A8              TAY                         ; restore the screen offset
3F19: BA              TSX                         ; pull the row index from the stack pointer
3F1A: CA              DEX                         ; next snapshot byte
3F1B: 10 E2           BPL     $3EFF               ; {code.loc_3eff} loop down through all the snapshot rows
3F1D: A9 04           LDA     #$04                ; aim the write pointer at screen page 4 (cursor high byte)
3F1F: 85 92           STA     $92                 ; {hard.workRam+92} store it for the digit plotter
3F21: A9 3A           LDA     #$3A                ; load draw cursor 0x3a
3F23: 85 91           STA     $91                 ; {hard.workRam+91} seat the draw cursor
3F25: A5 E4           LDA     $E4                 ; {hard.workRam+E4} read the stuck-low (OR) random accumulator
3F27: 49 FF           EOR     #$FF                ; invert it -- healthy bits should all have been set
3F29: 05 E3           ORA     $E3                 ; {hard.workRam+E3} fold in the stuck-high (AND) accumulator
3F2B: 05 E5           ORA     $E5                 ; {hard.workRam+E5} fold in the extra random-health flag
3F2D: F0 02           BEQ     $3F31               ; {code.loc_3f31} all bits toggled -- random test passes, skip the fault glyph
3F2F: A9 25           LDA     #$25                ; stuck bit found -- load the fault glyph

loc_3f31:
3F31: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} emit the random-test result glyph
3F34: 20 C0 3A        JSR     $3AC0               ; {code.tickEaromWriteback} service the deferred high-score EAROM write
3F37: 20 08 3A        JSR     $3A08               ; {code.foldHighScoreChecksum} fold the high-score table checksum
3F3A: 8C B5 01        STY     $01B5               ; {hard.workRam+1B5} store the checksum into the high-score checksum cell
3F3D: F0 16           BEQ     $3F55               ; {code.loc_3f55} checksum zero (table valid) -- go show the high score
3F3F: 48              PHA                         ; save the checksum byte
3F40: A9 3B           LDA     #$3B                ; load draw cursor 0x3b
3F42: 85 91           STA     $91                 ; {hard.workRam+91} seat the draw cursor
3F44: A9 24           LDA     #$24                ; load glyph 0x24
3F46: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} emit it
3F49: A9 00           LDA     #$00                ; load a blank
3F4B: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} emit the blank spacer
3F4E: 68              PLA                         ; recover the checksum byte
3F4F: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot the bad checksum as two digits
3F52: 4C D6 3F        JMP     $3FD6               ; {code.loc_3fd6} jump to the loop tail

loc_3f55:
3F55: A9 04           LDA     #$04                ; aim the write pointer at screen page 4 (cursor high byte)
3F57: 85 92           STA     $92                 ; {hard.workRam+92} store it for the digit plotter
3F59: A9 E9           LDA     #$E9                ; load draw cursor 0xe9
3F5B: 85 91           STA     $91                 ; {hard.workRam+91} seat the draw cursor at the high-score field
3F5D: 38              SEC                         ; set carry -- leading digit pair
3F5E: AD 8D 01        LDA     $018D               ; {hard.workRam+18D} read the high byte of the high score
3F61: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits
3F64: AD 8C 01        LDA     $018C               ; {hard.workRam+18C} read the middle high-score byte
3F67: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits
3F6A: AD 8B 01        LDA     $018B               ; {hard.workRam+18B} read the low high-score byte
3F6D: 18              CLC                         ; clear carry -- trailing digit pair
3F6E: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot it as two digits
3F71: A9 DE           LDA     #$DE                ; load the ROM text-row pointer low byte 0xde
3F73: 85 93           STA     $93                 ; {hard.workRam+93} set the row pointer low byte
3F75: A9 3F           LDA     #$3F                ; load the ROM text-row pointer high byte 0x3f
3F77: 85 94           STA     $94                 ; {hard.workRam+94} set the row pointer high byte
3F79: 20 25 38        JSR     $3825               ; {code.redrawPointerTableRowUnblanked} draw that text row (0x3fde) onto the screen
3F7C: A9 05           LDA     #$05                ; aim the write pointer at screen page 5 (cursor high byte)
3F7E: 85 92           STA     $92                 ; {hard.workRam+92} store it for the digit plotter
3F80: A9 08           LDA     #$08                ; load draw cursor 0x08
3F82: 85 91           STA     $91                 ; {hard.workRam+91} seat the draw cursor
3F84: A5 8D           LDA     $8D                 ; {hard.workRam+8D} read the derived high-score rank count (0x8d)
3F86: 4A              LSR     A                   ; shift its high nibble down one
3F87: 4A              LSR     A                   ; shift right again
3F88: 4A              LSR     A                   ; shift right again
3F89: 4A              LSR     A                   ; fourth shift brings the high nibble to the bottom
3F8A: F8              SED                         ; enter decimal mode
3F8B: 18              CLC                         ; clear carry
3F8C: 69 00           ADC     #$00                ; adjust the nibble into a BCD digit
3F8E: D8              CLD                         ; leave decimal mode
3F8F: 38              SEC                         ; set carry -- leading digit pair
3F90: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot the high-nibble value as two digits
3F93: A9 2E           LDA     #$2E                ; load the separator glyph 0x2e
3F95: 20 36 38        JSR     $3836               ; {code.writeMaskedByteAndAdvancePointer} emit the separator
3F98: A5 8D           LDA     $8D                 ; {hard.workRam+8D} read the config byte again
3F9A: 29 0F           AND     #$0F                ; keep only its low nibble
3F9C: F8              SED                         ; enter decimal mode
3F9D: 18              CLC                         ; clear carry
3F9E: 69 00           ADC     #$00                ; adjust the nibble into a BCD digit
3FA0: 85 8E           STA     $8E                 ; {hard.workRam+8E} stash it
3FA2: 65 8E           ADC     $8E                 ; {hard.workRam+8E} add it back (x2)
3FA4: 85 8E           STA     $8E                 ; {hard.workRam+8E} stash the doubled value
3FA6: 65 8E           ADC     $8E                 ; {hard.workRam+8E} add it once more (x3 total)
3FA8: D8              CLD                         ; leave decimal mode
3FA9: C9 60           CMP     #$60                ; compare the tripled value against 0x60
3FAB: 90 02           BCC     $3FAF               ; {code.loc_3faf} below 0x60 -- keep it
3FAD: A9 59           LDA     #$59                ; at or above -- clamp to 0x59

loc_3faf:
3FAF: 18              CLC                         ; clear carry -- trailing digit pair
3FB0: 20 4F 38        JSR     $384F               ; {code.plotByteAsTwoDigits} plot the scaled value as two digits
3FB3: A9 E4           LDA     #$E4                ; load the ROM text-row pointer low byte 0xe4
3FB5: 85 93           STA     $93                 ; {hard.workRam+93} set the row pointer low byte
3FB7: A9 3F           LDA     #$3F                ; load the ROM text-row pointer high byte 0x3f
3FB9: 85 94           STA     $94                 ; {hard.workRam+94} set the row pointer high byte
3FBB: 20 25 38        JSR     $3825               ; {code.redrawPointerTableRowUnblanked} draw that text row (0x3fe4) onto the screen
3FBE: A5 EA           LDA     $EA                 ; {hard.workRam+EA} read status cell 0xea
3FC0: 05 EB           ORA     $EB                 ; {hard.workRam+EB} fold in 0xeb
3FC2: 05 EC           ORA     $EC                 ; {hard.workRam+EC} fold in 0xec
3FC4: D0 10           BNE     $3FD6               ; {code.loc_3fd6} any set -- skip the checksum toggle
3FC6: AD B5 01        LDA     $01B5               ; {hard.workRam+1B5} read the high-score checksum
3FC9: 49 FF           EOR     #$FF                ; invert it
3FCB: 8D B5 01        STA     $01B5               ; {hard.workRam+1B5} write the toggled checksum back
3FCE: A9 3D           LDA     #$3D                ; load 0x3d
3FD0: 85 F9           STA     $F9                 ; {hard.workRam+F9} seed the pointer low byte at 0xf9
3FD2: A9 00           LDA     #$00                ; load zero
3FD4: 85 FA           STA     $FA                 ; {hard.workRam+FA} seed the pointer high byte at 0xfa

loc_3fd6:
3FD6: 4C 57 3D        JMP     $3D57               ; {code.loc_3d57} jump back to the top of the test-display loop

; ---- $3FD9-$3FF5: data ----
3FD9: 22 24 24 25 23 20 50 4C 41 59 D3 20 47 41 4D 45 ; _$$%#_PLAYs_GAME
3FE9: 20 54 49 4D C5 48 41 52 C4 45 41 53 D9          ; _TIMeHARdEASy

NMIService:
3FF6: 4C F6 3F        JMP     $3FF6               ; {code.NMIService} spin here forever -- the terminal halt after a diagnostic failure

3FF9: 0A  ; Padding byte before vectors. 

; These 6502 interrupt vectors ghost to FFFx

3FFA: F6 3F ; NMI vector to 3FF6 (unused -- infinite loop)
3FFC: 04 3B ; RESET vector to 3B04
3FFE: 71 38 ; IRQ vector to 3871
```

